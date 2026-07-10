|           | AOS-CX |     | 10.14     | Virtual |       |     |
| --------- | ------ | --- | --------- | ------- | ----- | --- |
| Switching |        |     | Extension |         | (VSX) |     |
Guide
| 6400, | 8100, | 8320, | 8325,  | 8360,  | 8400, | 9300, |
| ----- | ----- | ----- | ------ | ------ | ----- | ----- |
|       |       | 10000 | Switch | Series |       |       |
Published:November2023
Edition:1

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

| 2

Contents
Contents
| Contents                                    |                                                      |               |                |                 |        | 3   |
| ------------------------------------------- | ---------------------------------------------------- | ------------- | -------------- | --------------- | ------ | --- |
| About                                       | this document                                        |               |                |                 |        | 8   |
| Applicableproducts                          |                                                      |               |                |                 |        | 8   |
| Latestversionavailableonline                |                                                      |               |                |                 |        | 8   |
| Commandsyntaxnotationconventions            |                                                      |               |                |                 |        | 8   |
| Abouttheexamples                            |                                                      |               |                |                 |        | 9   |
| Identifyingswitchportsandinterfaces         |                                                      |               |                |                 |        | 10  |
| Identifyingmodularswitchcomponents          |                                                      |               |                |                 |        | 10  |
| Getting                                     | started                                              | with          | VSX            |                 |        | 12  |
| BenefitsofVSX                               |                                                      |               |                |                 |        | 12  |
| VSXsolutiontopologyoverview                 |                                                      |               |                |                 |        | 13  |
|                                             | SampleVSXsolutiontopology                            |               |                |                 |        | 13  |
|                                             | VSXLAG                                               |               |                |                 |        | 14  |
|                                             | VSF                                                  |               |                |                 |        | 14  |
|                                             | VSFversusVSX                                         |               |                |                 |        | 15  |
|                                             | ThecommonsystemMACaddress                            |               |                |                 |        | 15  |
| VSXsolutionrequirements                     |                                                      |               |                |                 |        | 16  |
| VSXcomponents                               |                                                      |               |                |                 |        | 16  |
| Inter-SwitchLink(ISL)                       |                                                      |               |                |                 |        | 17  |
|                                             | ISLconfigurations                                    |               |                |                 |        | 18  |
| Switchroles                                 |                                                      |               |                |                 |        | 19  |
| VSXswitchreboot                             |                                                      |               |                |                 |        | 20  |
| Periodicsynchronization                     |                                                      |               |                |                 |        | 20  |
| BFDandVSXsupport                            |                                                      |               |                |                 |        | 21  |
| Upgrading                                   | to                                                   | the           | latest version |                 | of VSX | 22  |
| UpgradingVSXfrom10.10orlaterto10.13         |                                                      |               |                |                 |        | 22  |
|                                             | Upgradingswitchesbyusingthevsxupdate-softwarecommand |               |                |                 |        | 23  |
| Setting                                     | up the                                               | VSX           | environment    |                 |        | 25  |
| VSXinthecorelayer                           |                                                      |               |                |                 |        | 25  |
| Configuringcore1andcore2forVSX              |                                                      |               |                |                 |        | 26  |
| ConfiguringthetwoaggregateVSXswitches       |                                                      |               |                |                 |        | 29  |
| ConfiguringanAOS-CXswitchasanaccessswitch   |                                                      |               |                |                 |        | 33  |
| Enabling                                    | VSX                                                  | configuration |                | synchronization |        | 36  |
| VSXconfigurationsynchronization             |                                                      |               |                |                 |        | 36  |
|                                             | FeaturessupportingVSX                                |               |                |                 |        | 36  |
|                                             | VSXsynchronizationrequirements                       |               |                |                 |        | 36  |
| EnablingVSXsynchronizationatthegloballevel  |                                                      |               |                |                 |        | 37  |
| EnablingVSXsynchronizationatthecontextlevel |                                                      |               |                |                 |        | 43  |
EnablingVSXsynchronizationofSTPconfigurationsbetweenVSXpeerswitches 46
| Monitoring | the | VSX | environment |     |     | 48  |
| ---------- | --- | --- | ----------- | --- | --- | --- |
3
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide

| WaystoviewthestatusofVSX                              |                                             | 48  |
| ----------------------------------------------------- | ------------------------------------------- | --- |
| ConsistencycheckingbetweenVSXswitches                 |                                             | 48  |
| ViewingtheshowcommandsforbothVSXswitchesfromoneswitch |                                             | 48  |
| Preventing                                            | traffic loss                                | 50  |
| Link-updelay                                          |                                             | 50  |
|                                                       | Thelink-updelaytimerduringanISLfailure      | 51  |
| Splitbrainscenario                                    |                                             | 53  |
| Keepalive                                             |                                             | 54  |
|                                                       | KeepaliveresponseinISLfailurescenarios      | 55  |
|                                                       | Keepalivescenario                           | 55  |
|                                                       | Keepaliveconfigurations                     | 56  |
|                                                       | Recommendednetworkconfigurationforkeepalive | 57  |
| Activegatewayandactiveforwarding                      |                                             | 59  |
|                                                       | Active-activelayer2                         | 59  |
|                                                       | Layer2configuration                         | 59  |
|                                                       | Active-activelayer3defaultgateway           | 60  |
|                                                       | ActivegatewayoverVSX                        | 60  |
|                                                       | VMACsandactivegateway                       | 61  |
|                                                       | Requirements                                | 61  |
|                                                       | ExampleofIPv4andIPv6activegatewaysonanSVI   | 62  |
|                                                       | IPmultinettingoverVSX                       | 63  |
|                                                       | Activegatewayconfigurations                 | 64  |
|                                                       | VRRPwithVSXconfiguration                    | 64  |
|                                                       | Activeforwarding                            | 65  |
|                                                       | Activeforwardingrequirements                | 65  |
|                                                       | Trafficflowscenario                         | 66  |
|                                                       | SampleActiveforwardingconfiguration         | 66  |
Deploymentoptionsforupstreamconnectivitywithactive-activeforwarding 66
|                                                   | Benefitsofactiveforwardingandactivegateway               | 66  |
| ------------------------------------------------- | -------------------------------------------------------- | --- |
| Virtualactivegateway                              |                                                          | 67  |
|                                                   | SupportedservicesonavirtualactivegatewaySVI              | 67  |
|                                                   | UnsupportedservicesforavirtualactivegatewaySVI           | 68  |
|                                                   | Samplevirtualactivegatewayconfiguration                  | 68  |
| Active-standbyDHCPrelay                           |                                                          | 69  |
|                                                   | DHCPrelayfailureiftheSVIisdownontheprimaryswitch         | 69  |
| Splitrecoverymode                                 |                                                          | 69  |
| VSXshutdown-on-split                              |                                                          | 70  |
| IGMPsnooping                                      |                                                          | 70  |
| DHCPrelaybackup                                   |                                                          | 71  |
| IPmulticastrouting                                |                                                          | 72  |
| RecommendedvaluesforsystemMACandactivegatewayVMAC |                                                          | 73  |
| STP over                                          | VSX                                                      | 75  |
| SupportedSTPmodes                                 |                                                          | 75  |
| HowSTPworkswithVSX                                |                                                          | 75  |
| MSTP                                              |                                                          | 76  |
|                                                   | MSTPconfigurations                                       | 77  |
|                                                   | VSXatthedistributionlayerwithMSTPenabled                 | 77  |
|                                                   | DistributionVSXpairconnectedtothecoreswitch(SVIsolution) | 79  |
|                                                   | SampleconfigurationsforMSTPonVSX                         | 80  |
VSXandMSTPloop-protectconfigurations(physicalandlogicalviews) 83
|       | ShowcommandsforMSTP             | 84  |
| ----- | ------------------------------- | --- |
|       | MSTPwithVSXguidelines           | 85  |
| RPVST |                                 | 85  |
|       | SampleRPVSTconfigurationwithVSX | 86  |
Contents|4

|                                            | VSXswitchwithRPVST,asrootandnonroot                   |          | 88  |
| ------------------------------------------ | ----------------------------------------------------- | -------- | --- |
|                                            | ConfiguringaVSXswitchasrootforoneormoreRPVSTinstances |          | 90  |
|                                            | ShowcommandsforRPVST                                  |          | 90  |
|                                            | HowtheMulti-Chassisroleworks                          |          | 91  |
|                                            | RPVSTwithVSXguidelines                                |          | 93  |
| Loop protect                               | configurations                                        | over VSX | 94  |
| HowloopprotectworksoverVSX                 |                                                       |          | 94  |
| SettinguploopprotectoverVSX                |                                                       |          | 98  |
| AnexampleconfigurationofloopprotectoverVSX |                                                       |          | 98  |
|                                            | VSXconfigurationsbeforeenablingloopprotect            |          | 99  |
|                                            | VSXprimaryswitchbeforeenablingloopprotect             |          | 99  |
|                                            | VSXsecondaryswitchbeforeenablingloopprotect           |          | 100 |
|                                            | Downstreamswitchbeforeenablingloopprotect             |          | 102 |
|                                            | VSXconfigurationsafterenablingloopprotect             |          | 103 |
|                                            | VSXprimaryswitchafterenablingloopprotect              |          | 103 |
|                                            | VSXsecondaryafterbeforeenablingloopprotect            |          | 104 |
|                                            | Downstreamswitchafterenablingloopprotect              |          | 105 |
| BestpracticesforloopprotectoverVSX         |                                                       |          | 105 |
| EVPN VSX                                   | support                                               |          | 106 |
| Upstream                                   | connectivity                                          |          | 107 |
| Upstreamconnectivityoptions                |                                                       |          | 107 |
| UpstreamroutingoverVSXLAGSVIlinks          |                                                       |          | 109 |
| VSX commands                               |                                                       |          | 113 |
| active-gateway                             |                                                       |          | 113 |
| config-syncdisable                         |                                                       |          | 119 |
| inter-switch-link{<PORT-NUM>|lag<LAG-ID>}  |                                                       |          | 120 |
| inter-switch-linkdead-interval             |                                                       |          | 121 |
| inter-switch-linkhello-interval            |                                                       |          | 122 |
| inter-switch-linkhold-time                 |                                                       |          | 123 |
| inter-switch-linkpeer-detect-interval      |                                                       |          | 124 |
| interfacelagmulti-chassis                  |                                                       |          | 125 |
| ipicmpredirect                             |                                                       |          | 126 |
| keepalivedead-interval                     |                                                       |          | 127 |
| keepalivehello-interval                    |                                                       |          | 128 |
| keepalivepeer                              |                                                       |          | 129 |
| keepaliveudp-port                          |                                                       |          | 130 |
| lacpfallback                               |                                                       |          | 131 |
| linkup-delay-timer                         |                                                       |          | 132 |
| linkup-delay-timerexcludelag-list          |                                                       |          | 134 |
| neighbor<IP-ADDRESS>vsx-sync-exclude       |                                                       |          | 135 |
| role{primary|secondary}                    |                                                       |          | 135 |
| showactive-gateway                         |                                                       |          | 136 |
| showactive-gateway<IFNAME>                 |                                                       |          | 138 |
| showinterface<VLAN-NAME>                   |                                                       |          | 139 |
| showlacpaggregates                         |                                                       |          | 140 |
| showlacpinterfaces                         |                                                       |          | 141 |
| showlacpinterfacesmulti-chassis            |                                                       |          | 144 |
| showrunning-configinterface                |                                                       |          | 146 |
| showrunning-configvsx                      |                                                       |          | 147 |
| showrunning-configvsx-sync                 |                                                       |          | 148 |
| showrunning-configvsx-syncpeer-diff        |                                                       |          | 149 |
| showsysteml2-vlan-mac-mode                 |                                                       |          | 150 |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 5

show vsx active-forwarding
show vsx brief
show vsx config-consistency
show vsx config-consistency lacp
show vsx configuration
show vsx configuration split-recovery
show vsx ip data-path
show vsx ip route
show vsx ipv6 data-path
show vsx ipv6 route
show vsx status
show vsx status config-sync
show vsx status peering
show vsx status shutdown-on-split
split recovery
system l2-vlan-mac-mode
system-mac
vsx
vsx active-forwarding
vsx shutdown-on-split
vsx-sync
vsx-sync (config-if, config-lag-if contexts)
vsx-sync (config-vlan-if context)
vsx-sync aaa
vsx-sync acl-log-timer
vsx-sync arp-security
vsx-sync bfd-global
vsx-sync bgp
vsx-sync copp-policy
vsx-sync dcb-global
vsx-sync dhcp-relay
vsx-sync dhcp-server
vsx-sync dhcpv6-server
vsx-sync dns
vsx-sync dhcp-snooping
vsx-sync evpn
vsx-sync icmp-tcp
vsx-sync keychain
vsx-sync lldp
vsx-sync loop-protect-global
vsx-sync mac-lockout
vsx-sync mclag-interfaces
vsx-sync nd-snooping
vsx-sync neighbor
vsx-sync ospf
vsx-sync policy-global
vsx-sync ptp-global
vsx-sync qos-global
vsx-sync route-map
vsx-sync sflow
vsx-sync sflow-global
vsx-sync snmp
vsx-sync ssh
vsx-sync static-routes
vsx-sync stp-global
vsx-sync telnet

150
152
153
155
157
158
158
160
162
164
166
169
170
171
172
173
175
176
177
178
179
182
187
188
189
191
192
192
194
195
196
197
198
199
200
201
202
203
204
205
205
206
208
209
210
211
212
212
213
214
215
216
217
218
219
220

Contents | 6

| vsx-synctime                  |           |                        | 221 |
| ----------------------------- | --------- | ---------------------- | --- |
| vsx-syncudp-forwarder         |           |                        | 222 |
| vsx-syncvrrp                  |           |                        | 223 |
| vsx-syncvsx-global            |           |                        | 224 |
| vsxupdate-software            |           |                        | 225 |
| vsxupdate-softwareboot-bank   |           |                        | 226 |
| Configuration                 | conflict  | finder recommendations | 229 |
| Samplerecommendations         |           |                        | 230 |
| Troubleshooting               |           |                        | 232 |
| ISLisout-of-sync              |           |                        | 232 |
|                               | Solution1 |                        | 232 |
|                               | Solution2 |                        | 233 |
|                               | Solution3 |                        | 233 |
| ISLisinblockingstate          |           |                        | 233 |
| TrafficdroponaVSXLAGinterface |           |                        | 235 |
TrafficlossaftertheISLhasbeenout-of-syncandkeepaliveisdown 236
| Failurescenariosandsplitrecovery |     |     | 236 |
| -------------------------------- | --- | --- | --- |
| Activegatewayisunreachable       |     |     | 237 |
BFDreportsaLAGasdownevenwhenhealthylinksarestillavailable 238
| Support                            | and Other | Resources | 240 |
| ---------------------------------- | --------- | --------- | --- |
| AccessingHPEArubaNetworkingSupport |           |           | 240 |
| AccessingUpdates                   |           |           | 241 |
| WarrantyInformation                |           |           | 241 |
| RegulatoryInformation              |           |           | 241 |
| DocumentationFeedback              |           |           | 241 |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 7

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n HPE Aruba Networking 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B,
R0X40C, R0X41A, R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C,
R0X26A, R0X27A, JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

n HPE Aruba Networking 8100 Switch Series (R9W94A, R9W95A, R9W96A, R9W97A)

n HPE Aruba Networking 8320 Switch Series (JL479A, JL579A, JL581A)

n HPE Aruba Networking 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n HPE Aruba Networking 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A,

JL709A, JL710A, JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C, JL709C, JL710C, JL711C,
JL704C, JL705C, JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

n HPE Aruba Networking 8400 Switch Series (JL366A, JL363A, JL687A)

n HPE Aruba Networking 9300 Switch Series (R9A29A, R9A30A, R8Z96A, S0F81A, S0F82A, S0F83A,

S0F84A, S0F85A, S0F86A, S0F87A, S0F88A, S0F95A, S0F965A)

n HPE Aruba Networking 10000 Switch Series (R8P13A, R8P14A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

Usage

example-text

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

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables
are enclosed in angle brackets (< >). Substitute the text—including

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide

8

Convention

Usage

n example-text

the enclosing angle brackets—with an actual value.

|

{ }

[ ]

… or

...

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

About this document | 9

switch(config-vlan-<VLAN-ID>)#

Where <VLAN-ID> is a variable representing the VLAN number.

Identifying switch ports and interfaces

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 6400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
member 1.

On the 83xx, 9300, and 10000 Switch Series

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

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

Identifying modular switch components

n Power supplies are on the front of the switch behind the bezel above the management modules.

Power supplies are labeled in software in the format: member/power supply:

o member: 1.

o power supply: 1 to 4.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

10

n Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

o member: 1.

o tray: 1 to 4.

o fan: 1 to 4.

n Fabric modules are not labeled on the switch but are labeled in software in the format:

member/module:

o member: 1.

o member: 1 or 2.

n The display module on the rear of the switch is not labeled with a member or slot number.

About this document | 11

Chapter 2

Getting started with VSX

Getting started with VSX

Aruba Virtual Switching Extension (VSX) is virtualization technology for aggregation/core switches
running the AOS-CX operating system. This solution lets the switches present as one virtualized switch in
critical areas. Configuration synchronization is one aspect of this VSX solution where the primary switch
configuration is synced to the secondary switch. This solution allows for a pseudo single plane of glass
configuration and helps keep key configuration pieces in synchronization as operational changes are
made. Since the solution is primarily for high availability, it is expected that most of the configuration
policy is the same across both peers.

VSX virtualizes the control plane of two aggregation switches to function as one device at layer 2 and as
independent devices at layer 3. From a datapath perspective, each device does an independent
forwarding lookup to decide how to handle traffic. Some of the forwarding databases, such as the MAC
and ARP tables, are synchronized between the two devices using a proprietary VSX control plane. Some
of the forwarding databases are built independently by each switch.

Benefits of VSX

VSX has similar benefits as Virtual Switching Framework (VSF), however, VSX also offers better high
availability required in core and data center environments. VSX binds two AOS-CX switches of the same
model type to operate as one device for layer 2. VSX also operates as independent nodes for layer 3.

n Control plane:

o Dual control plane for better resiliency

o Unified management (synchronized configuration and easy troubleshooting)

o Live software upgrade with near zero downtime

o In-chassis redundancy for the 8400 series switches and device level redundancy for all other

platforms, such as for the 832x and 6400 series switches.

n Layer 2 distributed LAGs (aggregation switches to access switches):

o Loop-free L2 multipathing (active-active)

o Rapid failover

o Simple configuration

o No Spanning Tree Required

n Layer 3 distributed LAGs (core switches to aggregate switches)

o Distributed Layer 3 over VSX pair (various options: Routed Only Ports (ROPs), Switched Virtual

Interfaces (SVIs), or LAG SVIs)

o Unified datapath (active-active first hop gateway)

o Layer 3 ECMP + Layer 2 VSX LAG (highly fault tolerant) with active-forwarding

n Active Gateway:

o Active-Active first hop gateway (VIP)

o No VRRP/HSRP

o Simple configuration (one command)

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide

12

o No gateway protocol overhead

o DHCP relay redundancy

o IP multinetting support

VSX solution topology overview

n Active gateway support: Active gateways can be configured for active-active routing. VRRP can be

used, as an alternative, for active-standby routing.

n ISL links assigned to higher bandwidth: An ISL link has a higher bandwidth compared to VSX links.
When planning the topology, consider sizing the ISL link according to the traffic volume required for
the east-west traffic of a single-homed VSX during a failover scenario.

n Increasing resiliency: When creating a LAG with multiple ports on each chassis-based switch, it is a
best practice to create the LAG with members from multiple line cards. This technique increases the
points of resiliency.

n Same VLAN configurations: Both VSX switches have the same VLAN configurations. Make sure that
no topology loop is formed because an ISL is added as a member to all the VLANs by default. You can
make configuration synchronization automatic between the VSX switches by enabling VSX
synchronization.

n Upstream device from VSX switches: Connections to the upstream device from the VSX switches

have sufficient bandwidth to handle traffic from all VSXs.

Core-1 and Core-2, shown in the following figure, can be third-party devices, as long as they support LACP for

downstream connectivity to the VSX LAG. VSX Synchronization syncs from the primary switch (shown as Agg-1 in

the following diagram) to the secondary switch (shown as Agg-2 in the following diagram).

To configure Core-1 and Core-2 with AOS-CX, see Configuring core 1 and core 2 for VSX.

To configure the aggregate 1 and aggregate 2, see Configuring the two aggregate VSX switches.

To configure the access switch, see Configuring an AOS-CX switch as an access switch.

After setting up the VSX topology, see Enabling VSX configuration synchronization. VSX synchronization
can be enabled globally for some features, and VSX synchronization can be enabled at the context level
for other features.

Sample VSX solution topology

Getting started with VSX | 13

VSX LAG

VSX LAGs span both aggregation switches. The two switches appear as one device to partner
downstream or upstream devices or both when forming a LAG with the VSX pair. The two switches
synchronize their databases and states over a user configured link referred to as an Inter-Switch Link
(ISL).

VSX LAGs are preferable to point-to-point transit VLANs for upstream connectivity when the routed only
port is not an option, such with the case of multiple VRFs. This configuration reduces the number of
transit VLANs and associated SVIs, simplifying operations and troubleshooting. Enable active forwarding
and active gateway to further optimize the traffic path. When you enable active forwarding and active
gateway, north-south and south-north traffic bypasses the ISL link.

VSF

Virtual Switching Framework (VSF) technology virtualizes multiple physical devices into one virtual fabric
which provides high availability because of the significant reduction in recovery time simplified network
design and management. VSF is ideal for campus access. VSF lets supported switches connected to each
other through Ethernet connections (copper or fiber) to behave like a single chassis switch.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

14

VSF versus VSX

VSF

VSX

Single control plane

Dual control plane

Single management plane with commander pushing
configuration on all members

Dual management plane with "opt-in" configuration
synchronization

Dual port state: Enabled

Default port state: Disabled

Layer 2 ports

Layer 3 ports

Ideal for campus access

Ideal for campus agg/core

The common system MAC address

The common system MAC address is used for preventing traffic disruptions when the primary switch is
restored after the secondary switch. A primary switch might be restored after the secondary switch in
scenarios, such as:

n A primary switch hardware replacement.

n A power outage with the primary switch restored after the secondary switch is restored.

When the primary switch is restored after the secondary switch, a traffic disruption might occur when
the ISL starts to sync because the MAC system address changes from the secondary switch to the
primary switch for the LACP. To avoid the traffic disruption, set the common system MAC address by
entering the system-mac <MAC-ADDR> command. This command creates a common system MAC
address between the two VSX switches. This common system MAC address prevents a traffic disruption

Getting started with VSX | 15

when the secondary switch comes up before the primary switch. If the common system MAC access is
enabled, the secondary switch uses the common system MAC address instead of its own system MAC
address, which prevents a traffic loss.

The system MAC address also maintains the same MSTP bridge ID across VSX switches, which act as a
single switch.

VSX solution requirements

n All VSX switches in an environment must have identical settings for the following:

o The VLAN membership for all VSX trunk ports.

o The loop protection configuration on a VLAN that is part of a VSX LAG.

n Available ports: Make sure that the VSX LAG interface on both the VSX primary and secondary

switches has a member port configured and enabled. Make sure that you also have a non-VSX port
that is available for the ISL.

n Mutually exclusive features:

o VSX active-forwarding and VSX active-gateway on the same VLAN interface

o VSX active-gateway and VRRP at SVI context

o VSX and MVRP

VSX active-gateway and VRRP can co-exist at global level

n Profiles for 832x series switches: All switches must be assigned either in profile L3-agg or L3-core.

n Support for Inter-Switch links (ISLs): VSX LAG does not support layer 3 processing, such as a
routed port; however, multiple Virtual Switch Interfaces (VSI) can be configured on the switch in
association with the VLANs carried over the given VSX LAG.

n Support for Layer 3: VSX LAG as a route only port is not supported. To enable Layer 3, create an SVI

associated to a given VLAN that is enabled on the VSX LAG.

n VLAN support: The same list of VLANs that are trunked over the VSX LAGs must be configured on

the primary and secondary VSX switches in the global configuration. The list of VLANs can be synced
to the secondary switch if the vsx-sync command is used in the VLAN context. Also verify that the
VLAN set is also permitted on the ISL on the primary and secondary VSX switches. To configure VLAN
trunking on the ISL, enter the vlan trunk allowed [<VLAN-LIST> | all] command. If a native VLAN is
defined, the switch automatically runs the vlan trunk allowed all command to ensure that the
default VLAN is allowed on the trunk. To allow only specific VLANs on the trunk, enter the vlan trunk
allowed <VLAN-LIST> command, for example: vlan trunk allowed 2,3,4

For steps about creating the ISL within a VSX LAG, see Configuring the two aggregate VSX switches.

n VSX active-forwarding, VSX active-gateway, and VSX LAG are supported with BFD.

n VSX switches and software versions: Both VSX peer switches must use the same software version
in most situations; however during an upgrade, one switch can run a different version than the peer
with some limitations, such as no VSX synchronization support.

VSX components

VSX has the following components:

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

16

n Active-standby DHCP server

n Common system MAC address

n DHCP forwarder redundancy

n Inter-Switch Link (ISL)

n IGMP snooping

n Keepalive

n Multiple Spanning Tree Protocol (MSTP)

n Split recovery mode

n Switch roles

Inter-Switch Link (ISL)

In the VSX solution topology, an Inter-Switch Link (ISL) is a layer 2 interface between two VSX peer
switches. Each VSX switch must be configured with an ISL link connected to its peer VSX switch. It is
recommended that this link is peer-to-peer and used for both datapath traffic forwarding and control
path VSX protocol exchange. The ISL interface is by default a member of all VLANs on the device. You
can change ISL membership through the command line, but you must ensure VLANs that contain VSX
LAG members are not excluded from the ISL.

In the datapath, traffic is forwarded natively with no additional encapsulation, unlike VSF. ISL is capable
of sending control path data, which requires oversize packets. The ISL MTU is automatically set to the
required size to accommodate oversize packets, and cannot be manually overwritten to avoid
generating an unintended outage. The token counters of ISL interface show this oversize control path
data as part of the ISL operation. The ISL link is the main pipeline for synchronizing data, such as from
the following components, during VSX stack join and also permanently between VSX peers:

n ARP table

n LACP states for VSX LAGs

n MAC table

n MSTP states

The ISL uses version control and provides backward compatibility regarding VSX synchronization
capabilities.

The ISL can span long distances (transceiver dependent). The traffic that passes over VSX links has no
additional encapsulation.

All ISL ports must have the same speed. The speed can be 10G, 25G, 40G, 50G or 100G, with 40G and
100G being the preferred speeds. For example: 2x40G.

Only R0X39A/C - R0X43A/C uplink ports support 50G DAC.

A 8100 Switch series can only configured as a VSX peer with another 8100 Switch series.

When you convert any layer 2 interface to be part of an ISL lag, the MTU value of the interface changes
to 9198 or 9500, depending on the switch platform. The show running-config or show running-config

Getting started with VSX | 17

allcommandsdonotdisplaythischangedMTUvalue.Forexample,ifyouconfiguretheinterfacewith
theMTUvalueof5000andconverttheinterfacetobepartofanISLlag,theMTUvaluechangesfrom
5000to9198or9500.Formoreinformation,seeAppliedinterfaceMTUValueandthecorresponding
platforms.
Theshow running-configorshow running-config allcommandsdisplaytheMTU valueas5000.Ifyou
wanttoviewtheactualMTUvalueoftheISLinterface,executetheshow interface <Interface-ID>
command.
Table1:AppliedinterfaceMTUValueandthecorrespondingplatforms
| Interface | MTU Value |     | Platforms |
| --------- | --------- | --- | --------- |
| 9198      |           |     | n 8320    |
n 8325
n 8400
n 9300
n 10000
9500
n 8100
n 8360
n 6400
ItisrecommendedtousethedefaultLACPtimerontheISLlag(30sforlacprateslow).
| Sample show | running-config | snippet |     |
| ----------- | -------------- | ------- | --- |
| interface   | 1/1/1          |         |     |
no shutdown
mtu 5000
description VSX-ISL
lag 256
| Sample show | interface   | snippet |     |
| ----------- | ----------- | ------- | --- |
| interface   | 1/1/1 is    | up      |     |
| Admin       | state is up |         |     |
Link state: up for 1 minute (since Mon Apr 05 07:25:14 UTC 2021)
| Link transitions: |     | 9   |     |
| ----------------- | --- | --- | --- |
Description:
| Hardware:     | Ethernet, | MAC Address: | 54:80:28:fd:78:fd |
| ------------- | --------- | ------------ | ----------------- |
| MTU 9198      |           |              |                   |
| Type SFP+DAC3 |           |              |                   |
Full-duplex
| qos trust        | none       |        |     |
| ---------------- | ---------- | ------ | --- |
| Speed            | 10000 Mb/s |        |     |
| Auto-negotiation |            | is off |     |
| Flow-control:    | off        |        |     |
| Error-control:   | off        |        |     |
ISL configurations
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 18

| Task                  | Command              | Example             |               |
| --------------------- | -------------------- | ------------------- | ------------- |
| ConfiguringanISLport. | inter-switch-link    | switch(config)#     | vsx           |
|                       |                      | switch(config-vsx)# | inter-switch- |
|                       |                      | link lag 100        |               |
| DeletinganISLport.    | no inter-switch-link | switch(config)#     | vsx           |
|                       |                      | switch(config-vsx)# | no inter-     |
switch-link
ConfiguringISLdeadinterval. inter-switch-link dead- switch(config)# vsx
interval <DEAD-INTERVAL>
|     |     | switch(config-vsx)# | inter-switch- |
| --- | --- | ------------------- | ------------- |
|     |     | link dead-interval  | 10            |
RestoredefaultISLdead no inter-switch-link switch(config)# vsx
| interval. | dead-interval |                           |           |
| --------- | ------------- | ------------------------- | --------- |
|           |               | switch(config-vsx)#       | no inter- |
|           |               | switch-link dead-interval |           |
ConfiguringtheISLhello inter-switch-link hello- switch(config)# vsx
interval.
|     | interval | switch(config-vsx)# | inter-switch- |
| --- | -------- | ------------------- | ------------- |
|     |          | link hello-interval | 3             |
RestoringdefaultISLhello no inter-switch-link switch(config)# vsx
interval.
|     | hello-interval | switch(config-vsx)#        | no inter- |
| --- | -------------- | -------------------------- | --------- |
|     |                | switch-link hello-interval |           |
ConfiguringISLholdtime. inter-switch-link hold- switch(config)# vsx
time
|     |     | switch(config-vsx)# | inter-switch- |
| --- | --- | ------------------- | ------------- |
|     |     | link hold-time      | 2             |
RestoringdefaultISLholdtime. no inter-switch-link switch(config)# vsx
hold-time
|     |     | switch(config-vsx)#   | no inter- |
| --- | --- | --------------------- | --------- |
|     |     | switch-link hold-time |           |
Configuringtheamountoftime inter-switch-link peer- switch(config)# vsx
| insecondsthatthedevice | detect-interval |                     |               |
| ---------------------- | --------------- | ------------------- | ------------- |
|                        |                 | switch(config-vsx)# | inter-switch- |
waitsfortheISLinterfaceto
link peer-detect-interval 180
linkupafterareboot.
Defaultvalues:
n Deadinterval:20seconds
n Hellointerval:1second
n Holdtime:0seconds
Peerdetectinterval:300seconds
n
Switch roles
EachVSXswitchmustbeconfiguredwitharole–primaryorsecondary.Therolesdonotindicatewhich
deviceisforwardingtrafficatagiventimeasVSXisanactive-activeforwardingsolution.Therolesare
usedtodeterminewhichdevicestaysactivewhenthereisaVSXsplit,suchaswhentheISLgoesdown,
GettingstartedwithVSX|19

and for determining the direction of configuration-sync. If the VSX ISL goes down, the primary switch
keeps forwarding traffic while the secondary switch blocks ports from participating in the VSX LAGs.

VSX switch reboot

After a VSX switch reboots, it has no entries for ARP, MAC, and routes. If downstream VSX LAG ports are
activated before all this information is relearned, traffic is dropped. To avoid a traffic drop, VSX LAGs on
the rebooted switch stay down until the restoration of LACP, MAC, ARP databases, and MSTP states if
MSTP is used.

The learning process for the VSX LAGs has two phases:

n Initial sync phase: The LACP states, MAC address table, ARP table, and potentially MSTP states are

downloaded from the forwarding switch to the freshly rebooted switch.

n Link-up delay phase: The downloaded entries are installed into the ASIC. Router adjacencies with

core nodes and learned upstream routes are also established.

The link-up delay phase is configurable with the linkup-delay-timer <DELAY-TIMER> command. The
default value is 180 seconds. Set the link-up delay timer to the maximum value of 600 seconds for a
network with many MAC addresses, a large ARP table, or a large routing table.

When both VSX switches reboot, the link-up delay timer is not used because both switches are trying to
relearn the LACP states, MAC address table, and ARP table.

To get upstream router adjacencies established during the link-up delay, the upstream LAGs have to be
excluded from the scope of the link-up delay. Run the linkup-delay-timer exclude lag-list <LAG-LIST>
for identifying the LAGs for exclusion.

For example, assume that you have a topology similar to the one in VSX solution topology overview, the
upstream LAGs (LAG 101 and LAG 102), would need to be identified by the linkup-delay-timer exclude
lag-list <LAG-LIST> for exclusion before a VSX switch reboot.

Periodic synchronization

Each VSX node synchronizes every second the following with its VSX peer through ISLP:

n Learned MAC addresses

n LACP states

n STP states

In a VSX scenario if all traffic from core to access flows through one switch only, the other device will
also learn about ARP/ND from its VSX peer. There is no functional impact to the normal datapath based
learning. VSX split and the rejoin scenario, such as periodic synchronization, resumes after the bulk
synchronization.

The IVRL induced neighbor entries are not synced either through the initial ARP synchronization or
periodic synchronization. The local IVRL will induce the learning on each side triggered by either a local
data-path ARP learned or the ongoing sync based-ARP learned in the source VRF.

If you enter one or more of the following commands on one VSX switch but not on the other VSX switch
or any configuration is incorrect on one switch , the ARP entries on both switches will become
unsynchronized:

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

20

n interface vlan

n shutdown for a VLAN

n no shutdown for a VLAN

If you run into this situation, correct the configuration and run the clear arp command, which clears the
ARP entries on both VSX nodes. After you run the clear arp command, the ARP entries are synchronized
on both switches.

The following image shows how periodic synchronization synchronizes LACP states, MAC, ARP/ND, and
MSTP. The image references the VSX synchronization between aggregate 1 (the primary VSX switch) and
aggregate 2 (the secondary VSX switch).

BFD and VSX support

BFD supports VSX LAG, active gateway, and active forwarding.

For 832x series switches: Several TCAMs (ternary content-addressable memory) are used to avoid
decreasing the time-to-live (TTL) to 254 on BFD single-hop packets received/sent on ISL interfaces.

For 8400 series switches: To account for the TTL decrement on active forwarding, the BFD daemon
supports packets with TTL equal to 254 on sessions running on ports with this functionality active.

Getting started with VSX | 21

Upgrading to the latest version of VSX

Chapter 3

Upgrading to the latest version of VSX

This chapter provides information about upgrading customer configurations to the latest version of the
Virtual Switching Extension (VSX).

n If you are upgrading from version 10.00, see the Virtual Switching Extension (VSX) Guide for 10.02 for
steps on how to upgrade VSX to version 10.02. Then, see the steps in this guide on how to upgrade
VSX from version 10.02.

n If you are upgrading from version 10.01/10.02, see the Virtual Switching Extension (VSX) Guide for 10.03

for steps on how to upgrade VSX to version 10.03. Then, see the steps in this guide on how to
upgrade VSX from version 10.03.

n If you are upgrading from version 10.03/10.04/10.05, see the Virtual Switching Extension (VSX) Guide for
10.06 for steps on how to upgrade VSX to version 10.06. Then, see the steps in this guide on how to
upgrade VSX from version 10.06.

n If you are upgrading from version 10.06/10.07/10.08/10.09, see the Virtual Switching Extension (VSX)

Guide for 10.09 for steps on how to upgrade VSX to version 10.10. Then, see the steps in this guide on
how to upgrade VSX from version 10.10.

Upgrading VSX from 10.10 or later to 10.13

You can upgrade to the latest version of AOS-CX using one of the following methods:

n Running the vsx update-software command: Follow the steps in Upgrading switches by using the

vsx update-software command for required steps before and after running the vsx update-software
command.

This command downloads new software from the TFTP server and verifies the download. After a
successful verification, the command installs the software to the alternative software bank of both
the VSX primary and secondary switches. The command then reboots them in sequence, the VSX
secondary switch followed by VSX primary switch. For example if a switch has booted with the
primary flash memory, then the command will install the software to secondary flash memory.

n Running the vsx update-software boot-bank command: This command upgrades the VSX pairs
using the specified boot bank on both the devices. Before running this command, copy the new
software by adding the TFTP URL into the software bank of both primary and secondary VSX switches.
Use this command in cases where the scheduled maintenance window is minimum or to avoid TFTP
server timeout. For more information about this command, see vsx update-software boot-bank.

n Using REST API : Refer to the latest REST API Guide.

To perform an upgrade using REST API, the minimum supported version of AOS-CX must be 10.07 or

later.

n Running Aruba NetEdit to upgrade to the latest version of VSX. Refer to the Aruba NetEdit

documentation.

n Schedule time not supported for a VSX software upgrade via the REST API.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide

22

| Upgrading |     | switches |     | by  | using | the | vsx update-software |     | command |
| --------- | --- | -------- | --- | --- | ----- | --- | ------------------- | --- | ------- |
Prerequisites
1. Ensurethatthereisascheduledmaintenancewindow.Therewillbeaminimaldisruptionof
serviceuntiltheupgradeiscompleted.
2. Ifyouhaveenabledloopprotect,entertheshow loop-protectcommandforverifyingthatthe
actiononloopdetectionhasavalueofTX disableontheVSXinterface.Ifthesettinghasa
differentvalue,resetthevaluetoTX disablebyenteringtheloop-protect action tx-disable
command:
|     | switch(config)#    |     |     | interface    |     | lag 2 multi-chassis |            |     |     |
| --- | ------------------ | --- | --- | ------------ | --- | ------------------- | ---------- | --- | --- |
|     | switch(config-if)# |     |     | loop-protect |     | action              | tx-disable |     |     |
|     | switch(config-if)# |     |     | exit         |     |                     |            |     |     |
|     | switch(config)#    |     |     | exit         |     |                     |            |     |     |
3. Thevsx update-softwarecommandprovidestheoptiontosavetheconfigurationonthe
primaryandsecondaryVSXswitches;however,youcansavetheconfigurationmanuallybyusing
oneofthefollowingmethods:
|     | n Tocopytherunningconfigurationintothestartupconfiguration: |         |      |                |     |                |     |     |     |
| --- | ----------------------------------------------------------- | ------- | ---- | -------------- | --- | -------------- | --- | --- | --- |
|     |                                                             | switch# | copy | running-config |     | startup-config |     |     |     |
Ifthestartupconfigurationisalreadypresent,thecommandoverwritesthepre-existingstartup
configuration.
n Tocopytherunningconfigurationintoacheckpointthathasnotbeencreatedyet:
|     |     | switch# | copy | running-config |     | checkpoint | <CHECKPOINT-NAME> |     |     |
| --- | --- | ------- | ---- | -------------- | --- | ---------- | ----------------- | --- | --- |
4. Checkthestatusoftheshow vsx briefcommandandvalidatetheISLisin-syncandthe
keepaliveisestablished.
5. Checktheoutputoftheshow lacp interfaces multi-chassiscommandandnotewhichLACP
interfacesareinaforwardingstateofup.
Procedure
1. Enterthevsx update-softwarecommand.Prefixthepath,fordownloadingthesoftware,with
tftp://,asshowninthefollowingexample:
switch# vsx update-software tftp://192.168.1.1/XL.10.0x.xxxx vrf mgmt
|     | Do  | you want | to  | save | the current | configuration |     | (y/n)? y |     |
| --- | --- | -------- | --- | ---- | ----------- | ------------- | --- | -------- | --- |
The running configuration was saved to the startup configuration.
This command will download new software to the %s image of both the VSX
|     | primary  |               | and secondary |      | systems, | then   | reboot   | them in sequence. |     |
| --- | -------- | ------------- | ------------- | ---- | -------- | ------ | -------- | ----------------- | --- |
|     | The      | VSX secondary |               | will | reboot   | first, | followed | by the primary.   |     |
|     | Continue |               | (y/n)?        | y    |          |        |          |                   |     |
VSX Primary Software Update Status : <VSX primary software update
status>
UpgradingtothelatestversionofVSX|23

VSX Secondary Software Update Status
status>
VSX ISL Status
Progress
[...........................................................................
..]
Secondary VSX system updated completely. Rebooting primary.

: <VSX secondary software update

: <VSX ISL status>

This command gives you the option to save the running configuration on the primary and
secondary VSX switches. After the command saves the running configuration, it downloads new
software from the TFTP server and verifies the download. After a successful verification, the
command installs the software to the alternative image of both the VSX primary and secondary
switches.

The command displays the status of the VSX primary and secondary switches during the upgrade.
The command also refreshes the progress bar as the image update progresses. Do not interrupt
the VSX primary CLI session until the software updates completes; however, software update
process can be stopped. If you stop the upgrade when the secondary switch has already installed
the image in its flash memory or the secondary switch has started the reboot the process, it
comes up with the new software. The primary switch continues to have with older software. You
can stop the software update process by pressing ctrl+c.

2. Run the show vsx brief command on both switches. Verify that ISL is In-Sync by running the
show vsx brief command on both switches. Verify in the output of the command that the
keepalive state is Keepalive-Established.

3. Validate on both switches that the downstream LACP links are all forwarding correctly by entering

the show lacp interfaces command.

4. Save the running configuration to the startup configuration:

switch# write memory
Success

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

24

Chapter 4
|         |            |             | Setting | up the | VSX environment |
| ------- | ---------- | ----------- | ------- | ------ | --------------- |
| Setting | up the VSX | environment |         |        |                 |
ThefollowingsectionsdescribethestepstosetuptheVSXenvironment,configurecore1andcore2for
VSX,andconfigureaggregateVSXswitches.
| VSX in | the core | layer |     |     |     |
| ------ | -------- | ----- | --- | --- | --- |
Whenmobilitycontrollersareattachedtothecorelayer,aVSXLAGmustbeinthecorelevel.Layer2is
onlyatthedistributionlayerwiththecorelayerbeinglayer2andlayer3.ThisconfigurationisforIPv6,
andtheconfigurationreducesthenumberoftransitVLANsandtheassociatedSVIsformanyVRFs.It
alsominimizestheShortestPathFirst(SPF)calculation.Thenumberoffibersisreducedandthereisfast
failoverbecauseofthesimplifiedtopology(nosquare-routing).
| Figure1 | VSXLAGinthecore(recommended) |     |     |     |     |
| ------- | ---------------------------- | --- | --- | --- | --- |
ThefollowingimageshowsanexamplethatSPFisslowerwhenVSXisnotinthecorebecauseofrouting
convergence.
25
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide

Configuring core 1 and core 2 for VSX

The steps in this section are for configuring core 1 and core 2 for VSX, as displayed in VSX LAG in the
core (recommended).

After completing these steps, configure the aggregate switches in your network topology, as described
in Configuring the two aggregate VSX switches. Then, enable VSX configuration synchronization for a
feature, as described in Enabling VSX configuration synchronization.

A VSX LAG supports a maximum of four member links per switch segment. A VSX LAG across a
downstream switch can have at most a total of eight member links. Run the show capacities command
for the maximum number of VSX LAGs supported for your type of switch.

The core can be third-party devices, as long as they support LACP for downstream connectivity to the
VSX LAG. VSX synchronization syncs from the primary switch (aggregate 1) to the secondary switch
(aggregate-2).

When creating a VSX LAG, select an equal number of member links in each segment for load balancing, such as

four member links (one segment) and four member links (another segment). Do not create a VSX LAG with four

member links in one switch and two member links on another segment. A switch can have a maximum of four

member links.

Setting up the VSX environment | 26

Procedure
1. Accessthepromptontheswitchyouwanttomaketheprimarycoreswitch.
2. Iftheswitchlacksahostname,createone:
| switch(config)# | hostname |     | example_host |     |
| --------------- | -------- | --- | ------------ | --- |
3. CreatetherequiredVLANS:
| switch(config)# | vlan | 1-20 |     |     |
| --------------- | ---- | ---- | --- | --- |
4. EnableOSPFv2:
| switch(config)#        | router | ospf         | 1       |           |
| ---------------------- | ------ | ------------ | ------- | --------- |
| switch(config-ospf-1)# |        | redistribute |         | connected |
| switch(config-ospf-1)# |        | area         | 0.0.0.0 |           |
5. EnableOSPFv3:
| switch(config)#          | router | ospfv3 | 1            |           |
| ------------------------ | ------ | ------ | ------------ | --------- |
| switch(config-ospfv3-1)# |        |        | redistribute | connected |
switch(config-ospfv3-1)#
area 0.0.0.0
| switch(config-ospfv3-1)# |     |     | exit |     |
| ------------------------ | --- | --- | ---- | --- |
OSPFv2andOSPFv3arenotrequiredtobeactivatedsimultaneously.ActivateOSPFv2and
OSPFV3accordingtotheneedsoftheenvironment.
6. CreatealoopbackinterfaceandenableOSPFv2/v3:
| switch(config)#             | interface |     | loopback   | 1              |
| --------------------------- | --------- | --- | ---------- | -------------- |
| switch(config-loopback-if)# |           |     | ip address | 3.3.3.3/24     |
| switch(config-loopback-if)# |           |     | ip ospf    | 1 area 0.0.0.0 |
| switch(config-loopback-if)# |           |     | exit       |                |
7. EnableOSPFv2/v3onthephysicalport:
| switch(config)#    | interface |          | 1/2/43 |     |
| ------------------ | --------- | -------- | ------ | --- |
| switch(config-if)# | no        | shutdown |        |     |
switch(config-if)#
|                    | ip   | address | 192.168.10.5/24 |               |
| ------------------ | ---- | ------- | --------------- | ------------- |
| switch(config-if)# | ipv6 | address |                 | 2001:11::3/64 |
| switch(config-if)# | ip   | ospf    | 1 area          | 0.0.0.0       |
| switch(config-if)# | ipv6 | ospfv3  | 1               | area 0.0.0.0  |
| switch(config-if)# | exit |         |                 |               |
8. CreateaVLANforthehostnetwork:
| switch(config)#          | vlan | 200 |           |                 |
| ------------------------ | ---- | --- | --------- | --------------- |
| switch(config-vlan-200)# |      |     | interface | vlan 200        |
| switch(config-if-vlan)#  |      | ip  | address   | 192.168.10.6/16 |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 27

| switch(config-if-vlan)# |     | ipv6 | address | 2001:200::1/64 |
| ----------------------- | --- | ---- | ------- | -------------- |
| switch(config-if-vlan)# |     | exit |         |                |
9. Enabletheportforhostcommunication:
| switch(config)#    | interface |          | 1/1/48 |     |
| ------------------ | --------- | -------- | ------ | --- |
| switch(config-if)# | no        | shutdown |        |     |
| switch(config-if)# | no        | routing  |        |     |
| switch(config-if)# | vlan      | access   | 200    |     |
| switch(config-if)# | exit      |          |        |     |
10. Entervsx:
| switch(config)# | vsx |     |     |     |
| --------------- | --- | --- | --- | --- |
switch(config-vsx)#
11. Entertherole primarycommandforassigningtheprimaryroletoaswitch.Ifyouhavealready
gonethroughthesestepsforconfiguringtheprimaryswitchandyouarenowconfiguringthe
| secondaryswitch,entertherole |     | secondarycommand. |     |     |
| ---------------------------- | --- | ----------------- | --- | --- |
Settingtheprimaryroleonaswitch:
| switch(config-vsx)# | role | primary |     |     |
| ------------------- | ---- | ------- | --- | --- |
Settingthesecondaryroleonaswitch:
| switch(config-vsx)# | role | secondary |     |     |
| ------------------- | ---- | --------- | --- | --- |
12. Configurealayer2interfaceasanISL:
| switch(config-vsx)# | inter-switch-link |     |     | lag 100 |
| ------------------- | ----------------- | --- | --- | ------- |
Inthisinstance,anISLwasconfiguredoverLAG100.
Beforeyouenterthiscommand,verifythattheinterfaceislayer2andtheLAGisnotaVSXLAG.
13. KeepalivehelpsthecoreswitchescontinuetostayinsynchduringanISLfailure.Whencreating
thekeepalivepath,makesurethatthepathdoesnotgoovertheISLoraVSXLAG.Keepalivecan
beconfiguretwowaysforcore1andcore2.Onewayistoenablekeepalivebetweencore1and
core2asadirectlink.Asecondwayistocreateakeepalivepathforaloopbackinterfacethrough
theupstreamthatlacksaVSXLAG.
| switch(config)#             | int loopback |     | 0          |                |
| --------------------------- | ------------ | --- | ---------- | -------------- |
| switch(config-loopback-if)# |              |     | ip address | 192.168.1.1/32 |
| switch(config-loopback-if)# |              |     | ip ospf    | 1 area 0       |
| switch(config-loopback-if)# |              |     | exit       |                |
| switch(config)#             | vsx          |     |            |                |
switch(config-vsx)# keepalive peer 192.168.1.2 source 192.168.1.1 vrf <KA-
SettinguptheVSXenvironment|28

VRF-NAME>
|     | switch(config-vsx)#         |     | exit     |            |               |
| --- | --------------------------- | --- | -------- | ---------- | ------------- |
|     | switch(config)#             | int | loopback | 0          |               |
|     | switch(config-loopback-if)# |     |          | vrf attach | <KA-VRF-NAME> |
Thesourceofthekeepaliveinterfacecanbeasupportedlayer3interfacethroughtheloopbackinterface,SVI,or
layer3interface.ThesourcemustbereachabletotheVSXpeerthroughlayer3.Thepathcanbeoverthecoreor
directpath.ThekeepalivepathmustnotbeovertheISL.SeeRecommendednetworkconfigurationforkeepalive.
©
14. Changethecontexttotheswitch(config)#context:
|     | switch(config-vsx)# |     | exit |     |     |
| --- | ------------------- | --- | ---- | --- | --- |
switch(config)#
15. ConfiguringaLAGinterfaceasanISL:
|     | switch(config)# | interface |     | lag <LAG-ID> |     |
| --- | --------------- | --------- | --- | ------------ | --- |
Forexample,configuringLAG100asanISLLAG:
|     | switch(config)#        | interface |                   | lag 100 |         |
| --- | ---------------------- | --------- | ----------------- | ------- | ------- |
|     | switch(config-lag-if)# |           | vsx               |         |         |
|     | switch(config-vsx)#    |           | inter-switch-link |         | lag 100 |
16. Repeatthepreviousstepsforthesecondarycoreswitch.
17. Entertheshow vsx configuration inter-switch-linkcommandforconfirmingthepropertiesof
theVSXLAG,suchasconfirmingiftheISLisin-sync.
switch#
|             |               | show vsx    | configuration       | inter-switch-link |              |
| ----------- | ------------- | ----------- | ------------------- | ----------------- | ------------ |
|             | Inter         | Switch Link | : 1/1/43            |                   |              |
|             | Hello         | Interval    | : 1 Seconds         |                   |              |
|             | Dead Interval |             | : 20                | Seconds           |              |
|             | Hold Time     |             | : 0 Seconds         |                   |              |
|             | System        | MAC         | : 10:00:00:00:00:01 |                   |              |
|             | Device        | Role        | : primary           |                   |              |
|             | Multichassis  | LAGs        | : lag100            |                   |              |
| Configuring |               | the two     | aggregate           |                   | VSX switches |
ThestepsinthissectionareforconfiguringthetwoaggregateVSXswitches,asdescribedinVSXsolution
topologyoverview.VSXswitchesdonotautomaticallyhaveVSXconfigurationsynchronizationenabled.
Aftercompletingthestepsinthissection,enableVSXconfigurationsynchronizationforafeature,as
describedinVSXconfigurationsynchronization.VSXsynchronizationsyncconfigurationinformation
fromtheprimaryswitch(Aggregate-1)tothesecondaryswitch(Aggregate-2).Aftercompletingthesteps
inthissection,enableVSXconfigurationsynchronizationforafeature,asdescribedinVSXconfiguration
synchronization.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 29

AVSXLAGsupportsamaximumoffourmemberlinksperswitchsegment.AVSXLAGacrossa
downstreamswitchcanhaveatmostatotalofeightmemberlinks.Runtheshow capacitiescommand
forthemaximumnumberofVSXLAGssupportedforyourtypeofswitch.
n WhencreatingaVSXLAG,selectanequalnumberofmemberlinksineachsegmentforloadbalancing,such
asfourmemberlinks(onesegment)andfourmemberlinks(anothersegment).DonotcreateaVSXLAG
withfourmemberlinksinoneswitchandtwomemberlinksonanothersegment.Aswitchcanhavea
maximumoffourmemberlinks.
n MakesurethattheVSXLAGinterfaceonboththeVSXprimaryandsecondaryswitcheshasamemberport
configuredandenabled.
n Makesurethatyoualsohaveanon-VSXportthatisavailablefortheISL.
Procedure
1. Accessthepromptontheswitchyouwanttomaketheprimaryaggregateswitch.
2. Iftheswitchdoesnothaveahostname,createone:
| switch(config)# | hostname | <HOSTNAME> |     |
| --------------- | -------- | ---------- | --- |
3. CreatetherequiredVLANS:
| switch(config)# | vlan 1-20 |     |     |
| --------------- | --------- | --- | --- |
4. CreatetheISLinterface:
| switch(config)#        | interface | lag 128     |          |
| ---------------------- | --------- | ----------- | -------- |
| switch(config-lag-if)# |           | no shutdown |          |
| switch(config-lag-if)# |           | no routing  |          |
| switch(config-lag-if)# |           | vlan trunk  | native 1 |
| switch(config-lag-if)# |           | lacp mode   | active   |
WhenanativeVLANisdefined(asshownthisexample),theswitchautomaticallyexecutesthe
vlan trunk allowed allcommandtoensurethatthedefaultVLANisallowedonthetrunk.Inthis
example,LAG128isbeingusedastheISL.
ThesamelistofVLANsthataretrunkedovertheVSXLAGsmustbeconfiguredontheprimary
andsecondaryVSXswitchesintheglobalconfiguration.ThelistofVLANscanbesyncedtothe
secondaryswitchifthevsx-synccommandisusedintheVLANcontext.AlsoverifythattheVLAN
setisalsopermittedontheISLontheprimaryandsecondaryVSXswitches.ToconfigureVLAN
trunkingontheISL,enterthevlan trunk allowed [<VLAN-LIST> | all]command.Ifanative
VLANisdefined,theswitchautomaticallyrunsthevlan trunk allowed allcommandtoensure
thatthedefaultVLANisallowedonthetrunk.ToallowonlyspecificVLANsonthetrunk,enterthe
vlan trunk allowed <VLAN-LIST>command,forexample:vlan trunk allowed 2,3,4
5. AddaphysicalinterfaceintotheLAG:
| switch(config)#    | interface   | 1/4/28 |     |
| ------------------ | ----------- | ------ | --- |
| switch(config-if)# | no shutdown |        |     |
| switch(config-if)# | lag         | 128    |     |
SettinguptheVSXenvironment|30

| switch(config)#    | interface | 1/4/32   |     |     |
| ------------------ | --------- | -------- | --- | --- |
| switch(config-if)# | no        | shutdown |     |     |
| switch(config-if)# | lag       | 128      |     |     |
6. Enabletheinterfaceforkeepalivecommunication:
| switch(config)#    | interface | 1/1/5   |                  |     |
| ------------------ | --------- | ------- | ---------------- | --- |
| switch(config-if)# | ip        | address | 192.168.100.1/24 |     |
7. Gotothevsxcontext:
| switch(config)# | vsx |     |     |     |
| --------------- | --- | --- | --- | --- |
switch(config-vsx)#
8. Entertherole primarycommandforassigningtheprimaryroletoaswitch.Ifyouhavealready
gonethroughthesestepsforconfiguringtheprimaryswitchandyouarenowconfiguringthe
| secondaryswitch,entertherole |     | secondarycommand. |     |     |
| ---------------------------- | --- | ----------------- | --- | --- |
Settingtheprimaryroleonaswitch:
| switch(config-vsx)# |     | role primary |     |     |
| ------------------- | --- | ------------ | --- | --- |
Settingthesecondaryroleonaswitch:
| switch(config-vsx)# |     | role secondary |     |     |
| ------------------- | --- | -------------- | --- | --- |
9. EnableISL:
| switch(config-vsx)# |     | inter-switch-link |     | lag 128 |
| ------------------- | --- | ----------------- | --- | ------- |
Inthisexample,ISLisbeingenabledforLAG128.
Beforeyouenterthiscommand,verifythattheinterfaceislayer2andtheLAGisnotaVSXLAG.
10. Enablekeepalive:
switch(config-vsx)# keepalive peer 192.168.100.2 source 192.168.100.1
Inthisexample,192.168.100.2isthepeerIPaddressand192.168.100.1isthesourceIPaddress.
11. Enablethemultichassisinterface:
| switch(config)#        | interface | lag         | 1 multi-chassis |     |
| ---------------------- | --------- | ----------- | --------------- | --- |
| switch(config-lag-if)# |           | no shutdown |                 |     |
| switch(config-lag-if)# |           | no routing  |                 |     |
| switch(config-lag-if)# |           | vlan        | trunk native    | 1   |
| switch(config-lag-if)# |           | vlan        | trunk allowed   | 11  |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 31

12. Addphysicalinterfacesintothemultichassisinterface:
| switch(config)#    | interface |          | 1/1/1 |     |     |
| ------------------ | --------- | -------- | ----- | --- | --- |
| switch(config-if)# | no        | shutdown |       |     |     |
| switch(config-if)# | lag       | 1        |       |     |     |
13. CreateanactivegatewaySVI:
| switch(config)#         | interface |     | vlan 11 |                  |     |
| ----------------------- | --------- | --- | ------- | ---------------- | --- |
| switch(config-if-vlan)# |           | ip  | address | 192.168.100.5/16 |     |
switch(config-if-vlan)#
|                         |     | ipv6           | address | 2001:DB8::2/64   |     |
| ----------------------- | --- | -------------- | ------- | ---------------- | --- |
| switch(config-if-vlan)# |     | active-gateway |         | ip 192.168.100.2 | mac |
00:00:00:00:00:01
| switch(config-if-vlan)# |     | active-gateway |     | ipv6 2001:DB8::3 | mac |
| ----------------------- | --- | -------------- | --- | ---------------- | --- |
00:00:01:00:00:01
14. EnableuplinkcommunicationforOSPFv2:
| switch(config)#        | router | ospf         | 1       |           |     |
| ---------------------- | ------ | ------------ | ------- | --------- | --- |
| switch(config-ospf-1)# |        | redistribute |         | connected |     |
| switch(config-ospf-1)# |        | area         | 0.0.0.0 |           |     |
Theredistribute connectedcommandisoptionalinthisexample.SeetheCommand-Line
InterfaceGuideforyourswitchandsoftwareversionformoreinformationabouttheredistribute
connectedcommand.
15. EnableuplinkcommunicationforOSPFv3:
| switch(config)#          | router | ospfv3 | 1            |           |     |
| ------------------------ | ------ | ------ | ------------ | --------- | --- |
| switch(config-ospfv3-1)# |        |        | redistribute | connected |     |
| switch(config-ospfv3-1)# |        |        | area 0.0.0.0 |           |     |
Theredistribute connectedcommandisoptionalinthisexample.SeetheCommand-LineInterface
Guideforyourswitchandsoftwareversionformoreinformationabouttheredistribute connected
command.
16. CreatetheloopbackinterfaceandenableOSPFv2:
switch(config)#
|                             | interface |     | loopback   | 1              |     |
| --------------------------- | --------- | --- | ---------- | -------------- | --- |
| switch(config-loopback-if)# |           |     | ip address | 192.168.0.1/32 |     |
| switch(config-loopback-if)# |           |     | ip ospf    | 1 area 0.0.0.0 |     |
17. EnableOSPFv2/v3onthephysicalport:
| switch(config)#    | interface |          | 1/4/30          |               |     |
| ------------------ | --------- | -------- | --------------- | ------------- | --- |
| switch(config-if)# | no        | shutdown |                 |               |     |
| switch(config-if)# | ip        | address  | 192.168.10.0/31 |               |     |
| switch(config-if)# | ipv6      | address  |                 | 2001:11::1/64 |     |
| switch(config-if)# | ip        | ospf     | 1 area          | 0.0.0.0       |     |
| switch(config-if)# | ipv6      | ospfv3   | 1               | area 0.0.0.0  |     |
SettinguptheVSXenvironment|32

18. Repeatthepreviousstepsforthesecondaryaggregateswitch.
19. Viewtherunningconfigurationbyenteringthefollowingontheprimaryandsecondaryswitches:
|     | switch# | show running-config |     |     |     |
| --- | ------- | ------------------- | --- | --- | --- |
20. VerifythattheISLlinkisin-sync,theroleoftheswitch,andthekeepalivestate(ifenabled)by
enteringthefollowingontheprimaryandsecondaryswitches:
|     | vsx-primary# | show             | vsx brief      |                         |     |
| --- | ------------ | ---------------- | -------------- | ----------------------- | --- |
|     | ISL State    |                  |                | : In-Sync               |     |
|     | Device       | State            |                | : Peer-Established      |     |
|     | Keepalive    | State            |                | : Keepalive-Established |     |
|     | Device       | Role             |                | : primary               |     |
|     | Number       | of Multi-chassis | LAG interfaces | : 2                     |     |
21. VerifytheVSXstatusbyenteringthefollowingontheprimaryandsecondaryswitches:
|     | switch#         | show vsx | status |     |     |
| --- | --------------- | -------- | ------ | --- | --- |
|     | VSX Operational | State    |        |     |     |
---------------------
|     | ISL          | channel      | : In-Sync         |     |                   |
| --- | ------------ | ------------ | ----------------- | --- | ----------------- |
|     | ISL          | mgmt channel | : operational     |     |                   |
|     | Config       | Sync Status  | : in-sync         |     |                   |
|     | NAE          |              | : peer_reachable  |     |                   |
|     | HTTPS        | Server       | : peer_reachable  |     |                   |
|     | Attribute    |              | Local             |     | Peer              |
|     | ------------ |              | --------          |     | --------          |
|     | ISL link     |              | 1/1/43            |     | 1/1/43            |
|     | ISL version  |              | 2                 |     | 2                 |
|     | System       | MAC          | 48:0f:cf:af:70:84 |     | 48:0f:cf:af:c2:84 |
|     | Platform     |              | 8320              |     | 8320              |
|     | Software     | Version      | 10.0x.xxxx        |     | 10.0x.xxxx        |
|     | Device       | Role         | primary           |     | secondary         |
22. VerifytheLACPinterfacestatusbyenteringthefollowingontheprimaryandsecondaryswitches:
|     | switch# | show lacp | interfaces |     |     |
| --- | ------- | --------- | ---------- | --- | --- |
23. Verifytheuplink(layer3communication)byenteringthefollowingontheprimaryandsecondary
switches:
|             | switch# | show ip ospf | neighbors |       |               |
| ----------- | ------- | ------------ | --------- | ----- | ------------- |
| Configuring |         | an AOS-CX    | switch    | as an | access switch |
AnaccessswitchcanbeanyswitchthatsupportsLACPorstaticlinkaggregation.Thestepsinthis
sectionarespecificallyforanAOS-CXswitch.Fornon-AOS-CXswitches,refertothedocumentationfor
yourswitchabouthowtoenableLACPorstaticlinkaggregation.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 33

Prerequisites
ThesestepsassumethatyouhaveanAOS-CXswitch.
Procedure
1. Iftheswitchlacksahostname,createone:
| switch(config)# | hostname | <HOSTNAME> |     |
| --------------- | -------- | ---------- | --- |
Forexample:
| switch(config)# | hostname | Finance01 |     |
| --------------- | -------- | --------- | --- |
2. CreateaVLAN:
| switch(config)# | vlan <VLAN-ID> |     |     |
| --------------- | -------------- | --- | --- |
Forexample:
| switch(config)# | vlan 11 |     |     |
| --------------- | ------- | --- | --- |
3. CreateaLAG:
| switch(config)# | interface | lag | <ID> |
| --------------- | --------- | --- | ---- |
Forexample:
| switch(config)# | interface | lag | 2   |
| --------------- | --------- | --- | --- |
4. EnableLACPfortheLAG:
| switch(config-lag-if)# |     | lacp mode | active |
| ---------------------- | --- | --------- | ------ |
5. Createeitheranaccessinterfaceoratrunkinterface.Youcancreatebothallowedandnative
trunkinterfacesontheaccessswitch.
n Tocreateanaccessinterface:
| switch(config-lag-if)# |     | vlan | access <VLAN_ID> |
| ---------------------- | --- | ---- | ---------------- |
Forexample:
| switch(config-lag-if)# |     | vlan access | 5   |
| ---------------------- | --- | ----------- | --- |
SettinguptheVSXenvironment|34

Tocreateanativetrunkinterface:
n
a. Tocreateanallowedtrunkinterface:
| switch(config-lag-if)# | vlan trunk | allowed | <VLAN_LIST> |
| ---------------------- | ---------- | ------- | ----------- |
Forexample:
| switch(config-lag-if)# | vlan trunk | allowed | 30,50,120 |
| ---------------------- | ---------- | ------- | --------- |
b. Tocreateanativetrunkinterface:
| switch(config-lag-if)# | vlan trunk | native | <VLAN_ID> [tag] |
| ---------------------- | ---------- | ------ | --------------- |
Forexample:
| switch(config-lag-if)# | vlan trunk | native | 30 tag |
| ---------------------- | ---------- | ------ | ------ |
ThetrunkparameterenablestaggingonanativeVLAN.Onlyincomingpacketsthataretagged
withthematchingVLANIDareaccepted.Incomingpacketsthatareuntaggedaredropped
exceptforBPDUs.Egresspacketsaretagged.
6. Formultipleaccessswitchesinyourtopology,repeattheprevioussteps.
7. Verifytheconfiguration:
switch# show lacp interfaces
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 35

Chapter 5

Enabling VSX configuration
synchronization

Enabling VSX configuration synchronization

VSX configuration synchronization simplifies VSX solution management, reduces configuration
misconfiguration and drift across VSX peer switches. With configuration synchronization enabled, the
primary peer configuration is synced to the secondary peer. This synchronization is controlled in an opt-
in manner by enabling VSX synchronization on a section of configuration.

VSX configuration synchronization

If one or more of the following scenarios occur, the secondary switch will receive the configuration
update after it fulfills synchronization requirements and is fully enabled:

n The secondary switch is not currently present.

n The secondary switch is not currently connected to the primary switch through the ISL.

n The secondary switch is not currently configured for VSX configuration synchronization at the time

VSX configuration synchronization is enabled on the primary switch.

You can only enable a specific configuration for syncing through the vsx-sync CLI extension on the
primary switch. This extension is blocked on the secondary peer switch except when VSX configuration-
synchronization is disabled or the ISL link is down.

Features supporting VSX

You can enable VSX synchronization at:

n The global level: See Enabling VSX synchronization at the global level for a listing of features

supporting VSX synchronization at the global level.

n The context level: See Enabling VSX synchronization at the context level for a listing of features

supporting VSX synchronization at the context level.

VSX synchronization requirements

n Software image versions must be the same on both switches.

n The output from the show vsx status command must show in-sync for Config Sync Status.

n Primary and secondary roles configured.

n An interswitch link must be configured.

n When enabling VSX synchronization under a physical interface, a VLAN interface, or a VSX LAG, create
on the secondary switch the physical interface, VLAN interface, or VSX LAG with the same name and
routing setting as on the primary switch. For example, if the primary switch has a physical interface of
1/1/1, you must create another physical interface of 1/1/1 on the secondary switch. Also, if the
primary VSX switch has routing enabled, the secondary switch must have routing enabled. Once the
name and routing information is the same, VSX synchronization synchronizes the additional
configuration information from the primary VSX switch to the secondary VSX switch.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide

36

Itisrecommendedto:
n EnablekeepaliveforpreventingtrafficlossduringanISLlinkfailure.
n AssignacommonsystemMACtopreventtrafficlossincaseswhenthesecondaryVSXswitchisrestored
beforetheprimaryVSXswitch.
| Enabling | VSX synchronization |     |     | at  | the | global | level |     |     |
| -------- | ------------------- | --- | --- | --- | --- | ------ | ----- | --- | --- |
ThecommandsinthistableareforenablingVSXsynchronizationatthegloballevelforafeature.
Command
| Feature | for | Example |     |     |     |     |     |     |     |
| ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
enabling
vsx-sync
AAA
|                 |     |     | switch(config)#     |     | vsx      |     |     |     |     |
| --------------- | --- | --- | ------------------- | --- | -------- | --- | --- | --- | --- |
| configurations, | aaa |     |                     |     |          |     |     |     |     |
|                 |     |     | switch(config-vsx)# |     | vsx-sync |     | aaa |     |     |
includinguser,
RADIUSserver,
andTACACS+
server.
| AccessListLog | vsx-sync |     |                 |     |             |     |           |     |     |
| ------------- | -------- | --- | --------------- | --- | ----------- | --- | --------- | --- | --- |
|               | acl-log- |     | switch(config)# |     | access-list |     | log timer | 30  |     |
Timer
|     |     |     | switch(config)# |     | vsx |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
timer
| configurations. |     |     | switch(config-vsx)# |     | vsx-sync |     | acl-log-timer |     |     |
| --------------- | --- | --- | ------------------- | --- | -------- | --- | ------------- | --- | --- |
vsx-sync
ARPsecurity
NOTE:ARPsecurityincludingdynamicARPinspectionisavailableonthe
arp-
| configuration. |     | 6400,8325,8400,and10000SwitchSeries. |     |     |     |     |     |     |     |
| -------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
security
|     |     |     | primary_sw(config)#     |     | vsx |          |                  |     |     |
| --- | --- | --- | ----------------------- | --- | --- | -------- | ---------------- | --- | --- |
|     |     |     | primary_sw(config-vsx)# |     |     | vsx-sync | arp-security     |     |     |
|     |     |     | primary_sw(config-vsx)# |     |     | vsx-sync | mclag-interfaces |     |     |
vsx-sync
BFD
|     | bfd-global |     | switch(config)# |     | bfd detect-multiplier |     |     | 1   |     |
| --- | ---------- | --- | --------------- | --- | --------------------- | --- | --- | --- | --- |
configurations.
|     |     |     | switch(config)#     |     | bfd min-transmit-interval     |     |            |     | 1000    |
| --- | --- | --- | ------------------- | --- | ----------------------------- | --- | ---------- | --- | ------- |
|     |     |     | switch(config)#     |     | bfd min-receive-interval      |     |            |     | 1000    |
|     |     |     | switch(config)#     |     | bfd echo-src-ip-address       |     |            |     | 2.2.2.2 |
|     |     |     | switch(config)#     |     | bfd min-echo-receive-interval |     |            |     | 1000    |
|     |     |     | switch(config)#     |     | vsx                           |     |            |     |         |
|     |     |     | switch(config-vsx)# |     | vsx-sync                      |     | bfd-global |     |         |
vsx-sync
BGP
|     | bgp |     | switch(config)# |     | ip aspath-list |     | list1 | seq | 10  |
| --- | --- | --- | --------------- | --- | -------------- | --- | ----- | --- | --- |
configurations.
|     |     |     | permit          | 10     |                      |         |     |          |      |
| --- | --- | --- | --------------- | ------ | -------------------- | ------- | --- | -------- | ---- |
|     |     |     | switch(config)# |        | ip community-list    |         |     | expanded | com1 |
|     |     |     | seq 10          | permit | 10                   |         |     |          |      |
|     |     |     | switch(config)# |        | ip extcommunity-list |         |     | standard |      |
|     |     |     | ext1 seq        | 10     | permit               | rt 10:4 |     |          |      |
EnablingVSXconfigurationsynchronization|37

Command
| Feature | for | Example |     |     |     |     |     |     |
| ------- | --- | ------- | --- | --- | --- | --- | --- | --- |
enabling
|     |     |     | switch(config)#                  | ip prefix-list |           | pref1    | seq 10       |     |
| --- | --- | --- | -------------------------------- | -------------- | --------- | -------- | ------------ | --- |
|     |     |     | permit any                       |                |           |          |              |     |
|     |     |     | switch(config)#                  | route-map      | rm1       | permit   |              |     |
|     |     |     | switch(config-route-map-rm1-10)# |                |           |          | match ip     |     |
|     |     |     | next-hop 1.1.1.1                 |                |           |          |              |     |
|     |     |     | switch(config)#                  | router         | bgp       | 100      |              |     |
|     |     |     | switch(config-bgp)#              | bgp            | router-id |          | 1.1.1.1      |     |
|     |     |     | switch(config-bgp)#              | neighbor       |           | 12.1.1.1 |              |     |
|     |     |     | remote-as 1                      |                |           |          |              |     |
|     |     |     | switch(config-bgp)#              | address-family |           |          | ipv4 unicast |     |
|     |     |     | switch(config-bgp-ipv4-uc)#      |                |           | neighbor | 12.1.1.1     |     |
activate
|     |     |     | switch(config)#     | vsx      |     |     |     |     |
| --- | --- | --- | ------------------- | -------- | --- | --- | --- | --- |
|     |     |     | switch(config-vsx)# | vsx-sync |     | bgp |     |     |
NOTE:AVSXsynchofBGPneighborsbetweenVSXpeersisperformedona
besteffortbasis.Directlyconnectedneighborswillbesyncedbythe
NDMD daemoninaVSXenvironment.NeighborslearnedovertheVxLAN
tunneloroverEVPNarenotsynchedthroughVSX,andtheVTEPswilllearn
theremoteneighborsindependently.Trafficlosswillnotbeseenifa
neighborismissinginonlytheprimaryorthesecondarymember.
| CoPPpolicy | vsx-sync |     |                 |     |     |     |     |     |
| ---------- | -------- | --- | --------------- | --- | --- | --- | --- | --- |
|            |          |     | switch(config)# | vsx |     |     |     |     |
copp-
configurations.
|     | policy |     | switch(config-vsx)# | vsx-sync |     | copp-policy |     |     |
| --- | ------ | --- | ------------------- | -------- | --- | ----------- | --- | --- |
vsx-sync
DCBx
|                |            |     | switch(config)#     | lldp dcbx        |     |            |          |     |
| -------------- | ---------- | --- | ------------------- | ---------------- | --- | ---------- | -------- | --- |
| configurations | dcb-global |     |                     |                  |     |            |          |     |
|                |            |     | switch(config)#     | dcbx application |     | iscsi      | priority | 7   |
| (8100,8325,    |            |     | switch(config)#     | vsx              |     |            |          |     |
|                |            |     | switch(config-vsx)# | vsx-sync         |     | dcb-global |          |     |
8360,9300,and
10000series
switches).
| DHCPv4and | vsx-sync   |     |                 |           |       |     |     |     |
| --------- | ---------- | --- | --------------- | --------- | ----- | --- | --- | --- |
|           | dhcp-relay |     | switch(config)# | interface | 1/1/1 |     |     |     |
DHCPv6relay
|     |     |     | switch(config-if)# | ip helper-address |     |     | 192.168.10.1 |     |
| --- | --- | --- | ------------------ | ----------------- | --- | --- | ------------ | --- |
configurations. switch(config-if)# ip helper-address 192.168.20.1
|              |          |     | switch(config)#     | interface         | 1/1/2  |                  |              |     |
| ------------ | -------- | --- | ------------------- | ----------------- | ------ | ---------------- | ------------ | --- |
|              |          |     | switch(config-if)#  | ip helper-address |        |                  | 192.168.30.1 |     |
|              |          |     | switch(config)#     | dhcp-relay        | option |                  | 82           |     |
|              |          |     | switch(config)#     | vsx               |        |                  |              |     |
|              |          |     | switch(config-vsx)# | vsx-sync          |        | dhcp-relay       |              |     |
| DHCPv4server | vsx-sync |     |                     |                   |        |                  |              |     |
|              | dhcp-    |     | switch(config)#     | dhcp-server       |        | external-storage |              |     |
configurations,
|     |     |     | dhcp-dbs file | dhcpv4_lease_file |     |     | delay 600 |     |
| --- | --- | --- | ------------- | ----------------- | --- | --- | --------- | --- |
server
| including |     |     | switch(config)#                  | dhcp-server |     | vrf default |           |     |
| --------- | --- | --- | -------------------------------- | ----------- | --- | ----------- | --------- | --- |
| external  |     |     | switch(config-dhcp-server)#      |             |     | pool test   |           |     |
|           |     |     | switch(config-dhcp-server-pool)# |             |     | range       | 10.0.0.20 |     |
storage
configurations.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 38

Command
| Feature | for | Example |     |     |     |     |     |     |
| ------- | --- | ------- | --- | --- | --- | --- | --- | --- |
enabling
10.0.0.30
|              |          |     | switch(config-dhcp-server-pool)# |               |                   |                  | default-router |     |
| ------------ | -------- | --- | -------------------------------- | ------------- | ----------------- | ---------------- | -------------- | --- |
|              |          |     | 10.0.0.1                         | 10.0.0.10     |                   |                  |                |     |
|              |          |     | switch(config-dhcp-server-pool)# |               |                   |                  | static-bind    |     |
|              |          |     | ip 10.0.0.1                      | mac           | 24:be:05:24:75:73 |                  |                |     |
|              |          |     | switch(config)#                  | vsx           |                   |                  |                |     |
|              |          |     | switch(config-vsx)#              |               | vsx-sync          | dhcp-server      |                |     |
| DHCPv6server | vsx-sync |     |                                  |               |                   |                  |                |     |
|              |          |     | switch(config)#                  | dhcpv6-server |                   | external-storage |                |     |
dhcpv6-
| configurations, |     |     | dhcpv6-dbs | file | dhcpv6_lease_file |     | delay | 600 |
| --------------- | --- | --- | ---------- | ---- | ----------------- | --- | ----- | --- |
server
including
|          |     |     | switch(config)#                    | dhcp-server |     | vrf  | default |         |
| -------- | --- | --- | ---------------------------------- | ----------- | --- | ---- | ------- | ------- |
| external |     |     | switch(config-dhcp-server)#        |             |     | pool | test    |         |
|          |     |     | switch(config-dhcpv6-server-pool)# |             |     |      | range   | 2001::1 |
storage
|                 |     |     | 2001::10                           | prefix-len | 64       |                    |             |     |
| --------------- | --- | --- | ---------------------------------- | ---------- | -------- | ------------------ | ----------- | --- |
| configurations. |     |     | switch(config-dhcpv6-server-pool)# |            |          |                    | option      | 22  |
|                 |     |     | ipv6 2001::12                      |            |          |                    |             |     |
|                 |     |     | switch(config-dhcpv6-server-pool)# |            |          |                    | static-bind |     |
|                 |     |     | ipv6 2001::11                      | client-id  |          | 1:0:a0:24:ab:fb:9c |             |     |
|                 |     |     | switch(config)#                    | vsx        |          |                    |             |     |
|                 |     |     | switch(config-vsx)#                |            | vsx-sync | dhcpv6-server      |             |     |
vsx-sync
DNS
|     | dns |     | switch(config)# | vsx |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
configurations.
|      |          |     | switch(config-vsx)# |      | vsx-sync | dns |     |     |
| ---- | -------- | --- | ------------------- | ---- | -------- | --- | --- | --- |
| EVPN | vsx-sync |     |                     |      |          |     |     |     |
|      |          |     | switch(config)#     | vlan | 2        |     |     |     |
evpn
| configurations.  |          |     | switch(config-vlan-2)#      |       |          | vsx-sync     |     |     |
| ---------------- | -------- | --- | --------------------------- | ----- | -------- | ------------ | --- | --- |
|                  |          |     | switch(config)#             | evpn  |          |              |     |     |
|                  |          |     | switch(config-evpn)#        |       | vlan     | 2            |     |     |
|                  |          |     | switch(config-evpn-vlan-2)# |       |          | rd 5:5       |     |     |
|                  |          |     | switch(config-evpn-vlan-2)# |       |          | route-target |     |     |
|                  |          |     | export 1:1                  |       |          |              |     |     |
|                  |          |     | switch(config-evpn-vlan-2)# |       |          | route-target |     |     |
|                  |          |     | import 1:1                  |       |          |              |     |     |
|                  |          |     | switch(config)#             | vsx   |          |              |     |     |
|                  |          |     | switch(config-vsx)#         |       | vsx-sync | evpn         |     |     |
| Globalclassifier | vsx-sync |     |                             |       |          |              |     |     |
|                  | policy-  |     | switch(config)#             | apply | policy   | testPolicy   |     | in  |
policy
|     |     |     | switch(config)# | vsx |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
global
| configurations. |          |     | switch(config-vsx)# |     | vsx-sync | policy-global |     |     |
| --------------- | -------- | --- | ------------------- | --- | -------- | ------------- | --- | --- |
| IPICMP          | vsx-sync |     |                     |     |          |               |     |     |
|                 |          |     | switch(config)#     | vsx |          |               |     |     |
icmp-tcp
| configurations. |     |     | switch(config-vsx)# |     | vsx-sync | icmp-tcp |     |     |
| --------------- | --- | --- | ------------------- | --- | -------- | -------- | --- | --- |
EnablingVSXconfigurationsynchronization|39

Command
| Feature | for | Example |     |     |     |     |     |
| ------- | --- | ------- | --- | --- | --- | --- | --- |
enabling
| LLDP | vsx-sync |                 |      |        |     |     |     |
| ---- | -------- | --------------- | ---- | ------ | --- | --- | --- |
|      |          | switch(config)# | lldp | reinit | 6   |     |     |
lldp
| configurations. |     | switch(config)#     | vsx |          |      |     |     |
| --------------- | --- | ------------------- | --- | -------- | ---- | --- | --- |
|                 |     | switch(config-vsx)# |     | vsx-sync | lldp |     |     |
vsx-sync
Loopprotect
|                 |       | switch(config)# | loop-protect |     | transmit- |     |     |
| --------------- | ----- | --------------- | ------------ | --- | --------- | --- | --- |
| configurations, | loop- |                 |              |     |           |     |     |
|                 |       | interval 10     |              |     |           |     |     |
protect-
| suchas |         | switch(config)# | loop-protect |     | re-enable-timer |     |     |
| ------ | ------- | --------------- | ------------ | --- | --------------- | --- | --- |
|        | globall | 300             |              |     |                 |     |     |
transmit-
|     |     | switch(config)# | vsx |     |     |     |     |
| --- | --- | --------------- | --- | --- | --- | --- | --- |
intervalandre-
|     |     | switch(config-vsx)# |     | vsx-sync | loop-protect-global |     |     |
| --- | --- | ------------------- | --- | -------- | ------------------- | --- | --- |
enable-timer.
vsx-sync
MAClockout
|     | mac- | switch(config)# | mac-lockout |     | 10:10:10:10:10:10 |     |     |
| --- | ---- | --------------- | ----------- | --- | ----------------- | --- | --- |
configurations.
|     |     | switch(config)# | vsx |     |     |     |     |
| --- | --- | --------------- | --- | --- | --- | --- | --- |
lockout
|            |          | switch(config-vsx)# |     | vsx-sync | mac-lockout |     |     |
| ---------- | -------- | ------------------- | --- | -------- | ----------- | --- | --- |
| NDsnooping | vsx-sync |                     |     |          |             |     |     |
|            |          | switch(config)#     | vsx |          |             |     |     |
nd-
configurations.
|     | snooping | switch(config-vsx)# |     | vsx-sync | nd-snooping |     |     |
| --- | -------- | ------------------- | --- | -------- | ----------- | --- | --- |
vsx-sync
OSPF
|                 |      | switch(config)#          | router | ospf         | 1          |           |     |
| --------------- | ---- | ------------------------ | ------ | ------------ | ---------- | --------- | --- |
| configurations. | ospf |                          |        |              |            |           |     |
|                 |      | switch(config-ospf-1)#   |        | area         | 0          |           |     |
|                 |      | switch(config-ospf-1)#   |        | area         | 1 nssa     |           |     |
|                 |      | switch(config-ospf-1)#   |        | area         | 2 stub     |           |     |
|                 |      | switch(config-ospf-1)#   |        | redistribute |            | connected |     |
|                 |      | route-map map1           |        |              |            |           |     |
|                 |      | switch(config)#          | router | ospfv3       | 1          |           |     |
|                 |      | switch(config-ospfv3-1)# |        |              | max-metric | router-   |     |
lsa on-startup
|                |          | switch(config-ospfv3-1)# |      |          | bfd all-interfaces |      |     |
| -------------- | -------- | ------------------------ | ---- | -------- | ------------------ | ---- | --- |
|                |          | switch(config-if)#       | ip   | ospf     | 1 area             | 0    |     |
|                |          | switch(config-if)#       | ip   | ospf     | hello-interval     |      | 33  |
|                |          | switch(config-if)#       | ipv6 | ospfv3   | 1                  | area | 0   |
|                |          | switch(config-if)#       | ipv6 | ospfv3   | dead-              |      |     |
|                |          | interval 55              |      |          |                    |      |     |
|                |          | switch(config)#          | vsx  |          |                    |      |     |
|                |          | switch(config-vsx)#      |      | vsx-sync | ospf               |      |     |
| Port-access    | vsx-sync |                          |      |          |                    |      |     |
| configuration. |          | switch(config-vsx)#      |      | vsx-sync | port-access        |      |     |
port-
|     |     | switch(config)# | vsx-sync |     | mclag-interfaces |     |     |
| --- | --- | --------------- | -------- | --- | ---------------- | --- | --- |
access
|     |     | switch(config)#            | port-access |              | lldp-group |           | l1   |
| --- | --- | -------------------------- | ----------- | ------------ | ---------- | --------- | ---- |
|     |     | switch(config-lldp-group)# |             |              | match      | sysname   | 6405 |
|     |     | switch(config-lldp-group)# |             |              | exit       |           |      |
|     |     | switch(config)#            | port-access |              | role       | r1        |      |
|     |     | switch(config-pa-role)#    |             | private-vlan |            | port-type |      |
secondary
|     |     | switch(config-pa-role)# |     | exit |     |     |     |
| --- | --- | ----------------------- | --- | ---- | --- | --- | --- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 40

Command
| Feature | for | Example |     |     |     |     |     |     |     |
| ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
enabling
|     |     |     | switch(config)#                |     | port-access |     | device-profile |     | dp1        |
| --- | --- | --- | ------------------------------ | --- | ----------- | --- | -------------- | --- | ---------- |
|     |     |     | switch(config-device-profile)# |     |             |     | enable         |     |            |
|     |     |     | switch(config-device-profile)# |     |             |     | associate      |     | role r1    |
|     |     |     | switch(config-device-profile)# |     |             |     | associate      |     | lldp-group |
l1
vsx-sync
QoS
|     |     |     | switch(config)# |     | vsx |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
qos-global
| Configurations, |     |     | switch(config-vsx)# |     | vsx-sync |     | qos-global |     |     |
| --------------- | --- | --- | ------------------- | --- | -------- | --- | ---------- | --- | --- |
suchasCoS
map,DSCP
map,andtrust
policy.
| Routemap | vsx-sync  |     |                 |     |                |     |       |     |     |
| -------- | --------- | --- | --------------- | --- | -------------- | --- | ----- | --- | --- |
|          | route-map |     | switch(config)# |     | ip aspath-list |     | list1 | seq | 10  |
configurations.
|                |          |     | permit                           | 10      |                      |         |            |          |     |
| -------------- | -------- | --- | -------------------------------- | ------- | -------------------- | ------- | ---------- | -------- | --- |
|                |          |     | switch(config)#                  |         | ip community-list    |         |            | expanded |     |
|                |          |     | com1                             | seq 10  | permit               | 10      |            |          |     |
|                |          |     | switch(config)#                  |         | ip extcommunity-list |         |            | standard |     |
|                |          |     | ext1                             | seq 10  | permit               | rt 10:4 |            |          |     |
|                |          |     | switch(config)#                  |         | ip prefix-list       |         | pref1      | seq      | 10  |
|                |          |     | permit                           | any     |                      |         |            |          |     |
|                |          |     | switch(config)#                  |         | route-map            | rm1     | permit     |          |     |
|                |          |     | switch(config-route-map-rm1-10)# |         |                      |         | match      |          | ip  |
|                |          |     | next-hop                         | 1.1.1.1 |                      |         |            |          |     |
|                |          |     | switch(config)#                  |         | vsx                  |         |            |          |     |
|                |          |     | switch(config-vsx)#              |         | vsx-sync             |         | route-map  |          |     |
| Staticneighbor | vsx-sync |     |                                  |         |                      |         |            |          |     |
|                |          |     | DUT-1(config-vsx)#               |         | show                 | run     | in vlan127 |          |     |
neighbor
| configurations. |     |     | interface | vlan127    |              |            |     |     |     |
| --------------- | --- | --- | --------- | ---------- | ------------ | ---------- | --- | --- | --- |
|                 |     |     |           | ip address | 137.1.1.1/16 |            |     |     |     |
|                 |     |     |           | ipv6       | address      | 7f00::1/64 |     |     |     |
|                 |     |     |           | arp ipv4   | 137.1.1.35   |            | mac |     |     |
00:12:01:00:00:1a
|     |     |     |     | arp ipv4 | 137.1.1.70 |     | mac |     |     |
| --- | --- | --- | --- | -------- | ---------- | --- | --- | --- | --- |
00:12:01:00:00:3d
exit
DUT-1(config-vsx)#
|     |     |     | switch(config)#     |     | vsx      |     |          |     |     |
| --- | --- | --- | ------------------- | --- | -------- | --- | -------- | --- | --- |
|     |     |     | switch(config-vsx)# |     | vsx-sync |     | neighbor |     |     |
vsx-sync
sFlow
|     | sflow |     | switch(config)# |     | vsx |     |     |     |     |
| --- | ----- | --- | --------------- | --- | --- | --- | --- | --- | --- |
configurations.
|             |          |     | switch(config-vsx)# |     | vsx-sync |           | sflow   |     |     |
| ----------- | -------- | --- | ------------------- | --- | -------- | --------- | ------- | --- | --- |
| sFlowglobal | vsx-sync |     |                     |     |          |           |         |     |     |
|             |          |     | switch(config)#     |     | sflow    | collector | 1.1.1.1 |     |     |
sflow-
| configurations. |     |     | switch(config)# |     | vsx |     |     |     |     |
| --------------- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
global
|     |     |     | switch(config-vsx)# |     | vsx-sync |     | sflow-global |     |     |
| --- | --- | --- | ------------------- | --- | -------- | --- | ------------ | --- | --- |
EnablingVSXconfigurationsynchronization|41

Command
| Feature | for | Example |     |     |
| ------- | --- | ------- | --- | --- |
enabling
| SNMP | vsx-sync |                 |     |     |
| ---- | -------- | --------------- | --- | --- |
|      |          | switch(config)# | vsx |     |
snmp
| configurations. |     | switch(config-vsx)# | vsx-sync | snmp |
| --------------- | --- | ------------------- | -------- | ---- |
vsx-sync
SSH
|     | ssh | switch(config)# | vsx |     |
| --- | --- | --------------- | --- | --- |
configurations.
|               |          | switch(config-vsx)# | vsx-sync | ssh |
| ------------- | -------- | ------------------- | -------- | --- |
| Staticroutes. | vsx-sync |                     |          |     |
|               |          | switch(config)#     | vsx      |     |
static-
|     |     | switch(config-vsx)# | vsx-sync | static-routes |
| --- | --- | ------------------- | -------- | ------------- |
routes
vsx-sync
STP
|     | stp-global | switch(config)# | spanning-tree | config-name |
| --- | ---------- | --------------- | ------------- | ----------- |
configurations.
abc
|              |          | switch(config)#     | spanning-tree | config-    |
| ------------ | -------- | ------------------- | ------------- | ---------- |
|              |          | revision 1          |               |            |
|              |          | switch(config)#     | vsx           |            |
|              |          | switch(config-vsx)# | vsx-sync      | stp-global |
| Time-related | vsx-sync |                     |               |            |
|              | time     | switch(config)#     | vsx           |            |
configurations,
|     |     | switch(config-vsx)# | vsx-sync | time |
| --- | --- | ------------------- | -------- | ---- |
includingNTP
andtimezone
configurations.
| UDPforwarder | vsx-sync |                 |     |     |
| ------------ | -------- | --------------- | --- | --- |
|              | upd-     | switch(config)# | vsx |     |
configurations.
|     |     | switch(config-vsx)# | vsx-sync | upd-forwarder |
| --- | --- | ------------------- | -------- | ------------- |
forwarder
vsx-sync
VRF
|     |     | switch(config)# | vsx |     |
| --- | --- | --------------- | --- | --- |
vrf
| configurations. |            | switch(config-vsx)# | vsx-sync | vrf |
| --------------- | ---------- | ------------------- | -------- | --- |
| VSX             | vsx-sync   |                     |          |     |
|                 | vsx-global | switch(config)#     | vsx      |     |
configurations:
|        |     | switch(config-vsx)# | inter-switch-link | dead-  |
| ------ | --- | ------------------- | ----------------- | ------ |
| n ISL: |     | interval 15         |                   |        |
|        |     | switch(config-vsx)# | inter-switch-link | hello- |
o Dead
|           |     | interval 2          |                   |       |
| --------- | --- | ------------------- | ----------------- | ----- |
| interval. |     | switch(config-vsx)# | inter-switch-link | hold- |
time 1
o Hello
|     |     | switch(config-vsx)# | vsx-sync | vsx-global |
| --- | --- | ------------------- | -------- | ---------- |
interval.
o Holdtime.
o Peer
detect
interval.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 42

Command
| Feature | for | Example |     |     |     |     |
| ------- | --- | ------- | --- | --- | --- | --- |
enabling
n Keepalive:
o Dead
interval.
o Hellow
interval.
o UDPport
number.
n Thedelay
timesetting
forthelink-
updelay
timer.
n Thesplit
recovery
setting.
n Thesystem
MAC
address.
| VSXLAG | vsx-sync |                 |     |     |     |     |
| ------ | -------- | --------------- | --- | --- | --- | --- |
|        | mclag-   | switch(config)# |     | vsx |     |     |
interfaces.
|     |     | switch(config-vsx)# |     | vsx-sync | mclag-interfaces |     |
| --- | --- | ------------------- | --- | -------- | ---------------- | --- |
interfaces
vsx-sync
VRRP
|     |     | switch(config)# |     | router vrrp | enable |     |
| --- | --- | --------------- | --- | ----------- | ------ | --- |
vrrp
configurations. switch(config-if)# vrrp 1 address-family ipv4
|     |     | switch(config-if-vrrp)# |     | address | 1.1.1.100 |     |
| --- | --- | ----------------------- | --- | ------- | --------- | --- |
primary
|          |                     | switch(config-if-vrrp)# |     | timers      | advertise      | 1000 |
| -------- | ------------------- | ----------------------- | --- | ----------- | -------------- | ---- |
|          |                     | switch(config-if-vrrp)# |     | no          | shutdown       |      |
|          |                     | switch(config-if)#      |     | vrr 1       | address-family | ipv6 |
|          |                     | switch(config)#         |     | vsx         |                |      |
|          |                     | switch(config-vsx)#     |     | vsx-sync    | vrrp           |      |
| Enabling | VSX synchronization |                         | at  | the context | level          |      |
ThecommandsinthistableareforenablingVSXsynchronizationatthecontextlevel,suchasforan
accesslist,aninterface,oraLAG.
EnablingVSXconfigurationsynchronization|43

WhenenablingVSXsynchronizationunderaphysicalinterface,aVLANinterface,oraVSXLAG,createonthe
secondaryswitchthephysicalinterface,VLANinterface,orVSXLAGwiththesamenameandroutingsettingas
ontheprimaryswitch.Forexample,iftheprimaryswitchhasaphysicalinterfaceof1/1/1,youmustcreate
anotherphysicalinterfaceof1/1/1onthesecondaryswitch.Also,iftheprimaryVSXswitchhasroutingenabled,
thesecondaryswitchmusthaveroutingenabled.Oncethenameandroutinginformationisthesame,VSX
synchronizationsynchronizestheadditionalconfigurationinformationfromtheprimaryVSXswitchtothe
secondaryVSXswitch.
Command
| Feature | Example |     |     |     |
| ------- | ------- | --- | --- | --- |
for enabling
Accesslists vsx-sync
EnablingVSXsynchronizationforaccesslistsassociatedwithinterface1/1/1:
associated access-
withinterface
lists
| orLAG. | switch(config)#    | interface | 1/1/1        |     |
| ------ | ------------------ | --------- | ------------ | --- |
|        | switch(config-if)# | vsx-sync  | access-lists |     |
EnablingVSXsynchronizationforaccesslistsunderinterfaceLAG2:
|     | switch(config)#        | interface | lag 2                 |             |
| --- | ---------------------- | --------- | --------------------- | ----------- |
|     | switch(config-lag-if)# |           | vsx-sync access-lists |             |
|     | switch(config-lag-if)# |           | apply access-list     | ip test1 in |
Anaccesslist vsx-sync
|     | switch(config)# | access-list | ip ITBoston |     |
| --- | --------------- | ----------- | ----------- | --- |
context.
|     | switch(config-acl-ip)# |     | vsx-sync |     |
| --- | ---------------------- | --- | -------- | --- |
Oneormore vsx-sync
EnablingVSXsyncforactivegatewaysunderinterfaceVLAN5:
active active-
| gateways | Enterontheprimaryswitch: |     |     |     |
| -------- | ------------------------ | --- | --- | --- |
gateways
associated
withan
|     | switch(config)# | interface | vlan 5 |     |
| --- | --------------- | --------- | ------ | --- |
interface.
|     | switch(config-if-vlan)# |     | vsx-sync active-gateways |     |
| --- | ----------------------- | --- | ------------------------ | --- |
Enteronthesecondaryswitch:
|     | switch(config)# | interface | vlan 5 |     |
| --- | --------------- | --------- | ------ | --- |
Aclass vsx-sync
|     | switch(config)# | class ip | ITHouston |     |
| --- | --------------- | -------- | --------- | --- |
context.
|     | switch(config-class-ip)# |     | vsx-sync |     |
| --- | ------------------------ | --- | -------- | --- |
Apolicy vsx-sync
| context. | switch(config)#        | policy | ITPaloAlto |     |
| -------- | ---------------------- | ------ | ---------- | --- |
|          | switch(config-policy)# |        | vsx-sync   |     |
AnIRDP vsx-sync
|     | switch(config)# | interface | 1/1/1 |     |
| --- | --------------- | --------- | ----- | --- |
association irdp
underan
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 44

Command
| Feature | Example |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
for enabling
interface
switch(config-if)#
| enabledfor |                    |     | ip irdp                   |     |     |     |
| ---------- | ------------------ | --- | ------------------------- | --- | --- | --- |
| syncing.   | switch(config-if)# |     | ip irdp minadvertinterval |     |     | 550 |
|            | switch(config-if)# |     | ip irdp maxadvertinterval |     |     | 850 |
|            | switch(config-if)# |     | ip irdp holdtime          |     | 900 |     |
|            | switch(config-if)# |     | vsx-sync irdp             |     |     |     |
QoS vsx-sync EnablingVSXsynchronizationforQoSassociationsunderinterface1/1/5:
associated qos
withan
| interfaceor | switch(config)#    | interface | 1/1/5        |     |     |     |
| ----------- | ------------------ | --------- | ------------ | --- | --- | --- |
| LAG.        | switch(config-if)# |           | vsx-sync qos |     |     |     |
EnablingVSXsynchronizationforQoSunderinterfaceLAG3:
|     | switch(config)#        | interface | lag      | 3   |     |     |
| --- | ---------------------- | --------- | -------- | --- | --- | --- |
|     | switch(config-lag-if)# |           | vsx-sync | qos |     |     |
AQoSqueue- vsx-sync
| profile. | switch(config)#       | qos | queue-profile |     | qprofile1      |     |
| -------- | --------------------- | --- | ------------- | --- | -------------- | --- |
|          | switch(config-queue)# |     | vsx-sync      |     |                |     |
|          | switch(config-queue)# |     | map queue     | 0   | local-priority | 7   |
|          | switch(config-queue)# |     | map queue     | 1   | local-priority | 6   |
|          | switch(config-queue)# |     | map queue     | 2   | local-priority | 5   |
|          | switch(config-queue)# |     | map queue     | 3   | local-priority | 4   |
|          | switch(config-queue)# |     | map queue     | 4   | local-priority | 3   |
|          | switch(config-queue)# |     | map queue     | 5   | local-priority | 2   |
switch(config-queue)#
|     |                       |     | map queue | 6   | local-priority | 1   |
| --- | --------------------- | --- | --------- | --- | -------------- | --- |
|     | switch(config-queue)# |     | map queue | 7   | local-priority | 0   |
AQoS vsx-sync
| schedule- | switch(config)#          | qos | schedule-profile |       | sprofile1 |     |
| --------- | ------------------------ | --- | ---------------- | ----- | --------- | --- |
| profile.  | switch(config-schedule)# |     | vsx-sync         |       |           |     |
|           | switch(config-schedule)# |     | dwrr             | queue | 0 weight  | 1   |
|           | switch(config-schedule)# |     | dwrr             | queue | 1 weight  | 10  |
|           | switch(config-schedule)# |     | dwrr             | queue | 2 weight  | 20  |
switch(config-schedule)#
|     |                          |     | dwrr | queue | 3 weight | 30  |
| --- | ------------------------ | --- | ---- | ----- | -------- | --- |
|     | switch(config-schedule)# |     | dwrr | queue | 4 weight | 40  |
|     | switch(config-schedule)# |     | dwrr | queue | 5 weight | 50  |
|     | switch(config-schedule)# |     | dwrr | queue | 6 weight | 60  |
|     | switch(config-schedule)# |     | dwrr | queue | 7 weight | 70  |
Portfilters vsx-sync
|     | switch(config)# | interface | 1/1/1 |     |     |     |
| --- | --------------- | --------- | ----- | --- | --- | --- |
underan portfilter
|     | switch(config-if)# |     | vsx-sync portfilter |     |     |     |
| --- | ------------------ | --- | ------------------- | --- | --- | --- |
interface.
|     | switch(config)#        | interface | lag      | 1          |     |     |
| --- | ---------------------- | --------- | -------- | ---------- | --- | --- |
|     | switch(config-lag-if)# |           | vsx-sync | portfilter |     |     |
Policiesunder vsx-sync EnablingVSXsyncforpoliciesunderinterfaceVLAN5:
EnablingVSXconfigurationsynchronization|45

Command
| Feature |     | Example |     |     |     |
| ------- | --- | ------- | --- | --- | --- |
for enabling
| aninterface. | policies | Enterontheprimaryswitch: |           |                   |     |
| ------------ | -------- | ------------------------ | --------- | ----------------- | --- |
|              |          | switch(config)#          | interface | vlan 5            |     |
|              |          | switch(config-if-vlan)#  |           | vsx-sync policies |     |
Enteronthesecondaryswitch:
|     |     | switch(config)# | interface | vlan 5 |     |
| --- | --- | --------------- | --------- | ------ | --- |
PVLAN port vsx-sync EnablingVSXsyncforPVLAN porttypeconfiguration:
| type | private- |     |     |     |     |
| ---- | -------- | --- | --- | --- | --- |
configuration
vlan port-
| underan |     | switch(config)# | interface | lag 8 |     |
| ------- | --- | --------------- | --------- | ----- | --- |
type
| interface |     | switch(config-lag-if)# |     | vsx-sync private-vlan | port- |
| --------- | --- | ---------------------- | --- | --------------------- | ----- |
type
enabledfor
syncing.
| Ratelimits | vsx-sync |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- |
EnablingVSXsynchronizationforratelimitswithinterface1/1/1:
associated
rate-limits
withinterface
| orLAG. |     | switch(config)# | interface | 1/1/1 |     |
| ------ | --- | --------------- | --------- | ----- | --- |
switch(config-if)#
|     |     |     |     | vsx-sync rate-limits |     |
| --- | --- | --- | --- | -------------------- | --- |
EnablingVSXsynchronizationforratelimitsunderinterfaceLAG3:
|             |          | switch(config)#        | interface | lag 3                |     |
| ----------- | -------- | ---------------------- | --------- | -------------------- | --- |
|             |          | switch(config-lag-if)# |           | vsx-sync rate-limits |     |
| VLANs       | vsx-sync |                        |           |                      |     |
|             |          | switch(config)#        | interface | 1/1/1                |     |
| association | vlans    |                        |           |                      |     |
|             |          | switch(config-if)#     |           | vsx-sync vlans       |     |
underan
interface
enabledfor
syncing.
| VSXactive-    | vsx active- |                         |      |                       |     |
| ------------- | ----------- | ----------------------- | ---- | --------------------- | --- |
|               |             | switch# interface       | vlan | 3                     |     |
| forwardingfor | forwarding  |                         |      |                       |     |
|               |             | switch(config-if-vlan)# |      | vsx active-forwarding |     |
aninterface
switch(config-vsx)#
VLAN.
| Enabling | VSX synchronization |          | of STP | configurations |     |
| -------- | ------------------- | -------- | ------ | -------------- | --- |
| between  | VSX peer            | switches |        |                |     |
Prerequisites
n TheVSXswitchessupportseveralSTPmodes,suchasMSTPandRPVST.ConfirmthattheseSTP
configurationsareidenticalontheVSXswitches.
n Youmustbeintheglobalconfigurationcontext:switch(config)#.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 46

Procedure

1. Enter:

switch(config)# vsx
switch(config-vsx)# vsx-sync stp-global

2. Enter:

switch(config-vsx)# vsx-sync vsx-global

3. Enter:

switch(config-vsx)# vsx-sync mclag-interfaces

Enabling VSX configuration synchronization | 47

Chapter 6
|            |     |      |     |             |        |     | Monitoring | the VSX | environment |     |
| ---------- | --- | ---- | --- | ----------- | ------ | --- | ---------- | ------- | ----------- | --- |
| Monitoring |     | the  | VSX | environment |        |     |            |         |             |     |
| Ways       | to  | view |     | the         | status | of  | VSX        |         |             |     |
YouviewthestatusofVSXbymultipletechniques:
n From the web UI: SeetheVSXpagetopicintheIntroductiontotheWebUIGuide.
| n           | From the | REST                | API:     | SeetheRESTAPIGuide. |         |     |              |     |     |     |
| ----------- | -------- | ------------------- | -------- | ------------------- | ------- | --- | ------------ | --- | --- | --- |
| n           | From the | CLI:SeeVSXcommands. |          |                     |         |     |              |     |     |     |
| Consistency |          |                     | checking |                     | between |     | VSX switches |     |     |     |
Usethefollowingcommandstoverifythatallconfigurationsarein-syncbetweenVSXswitches.These
commandsarehelpfulintroubleshootingconfigurationmismatchesacrossVSXpeerswitches.
| Task |     |     |     |     |     |     |     | Command |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
DisplayingtheVSXglobalconfigurationconsistencybetweentwo show vsx config-consistency
VSXswitches.Usethiscommandtotroubleshootconfiguration
mismatchesacrossVSXpeerswitches.
DisplayingVSXLACPconfigurationconsistencybetweentwoVSX show vsx config-consistency lacp
switches.Usethiscommandtotroubleshootconfiguration
[<LAG-NAME>]
mismatchesacrossVSXpeerswitches.
| Viewing |     | the | show |     | commands |     | for both | VSX switches |     | from |
| ------- | --- | --- | ---- | --- | -------- | --- | -------- | ------------ | --- | ---- |
one switch
YoucanviewtheoutputsoftheshowcommandfortheprimaryandsecondaryVSXswitchesfromone
switch.Whenyouenterashowcommandwiththevsx-peerparameter,thecommanddisplaysthe
outputfromthepeerdevice.
Forexample,thefollowingcommandwasenteredontheprimaryswitch.Thevsx-peerparameter
indicatestothesoftwaretodisplaytheoutputasifthecommandwasenteredonthesecondaryswitch.
|     | switch#         | show | vsx   | status | vsx-peer |     |     |     |     |     |
| --- | --------------- | ---- | ----- | ------ | -------- | --- | --- | --- | --- | --- |
|     | VSX Operational |      | State |        |          |     |     |     |     |     |
---------------------
|     | ISL          | channel |         |          | : In-Sync        |     |          |     |     |     |
| --- | ------------ | ------- | ------- | -------- | ---------------- | --- | -------- | --- | --- | --- |
|     | ISL          | mgmt    | channel |          | : operational    |     |          |     |     |     |
|     | Config       | Sync    | Status  |          | : in-sync        |     |          |     |     |     |
|     | NAE          |         |         |          | : peer_reachable |     |          |     |     |     |
|     | HTTPS        | Server  |         |          | : peer_reachable |     |          |     |     |     |
|     | Attribute    |         |         | Local    |                  |     | Peer     |     |     |     |
|     | ------------ |         |         | -------- |                  |     | -------- |     |     |     |
48
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide

| ISL link         | lag1              | lag1              |
| ---------------- | ----------------- | ----------------- |
| ISL version      | 2                 | 2                 |
| System MAC       | e0:07:1b:cb:72:e4 | 98:f2:b3:68:79:2e |
| Platform         | 8320              | 8320              |
| Software Version | 10.0x.xxxx        | 10.0x.xxxx        |
| Device Role      | secondary         | primary           |
Theshowcommandsthatdisplaythefilesystemcontents,suchasshowloggingorshowcore-dump,donot
supportthevsx-peerparameter.
IftheswitcheslacktheVSXconfigurationortheISLisdown,theoutputfromtheVSXpeerswitchisnot
displayed.
MonitoringtheVSXenvironment|49

Chapter 7

Preventing traffic loss

Preventing traffic loss

The following section describes strategies for preventing traffic loss.

Link-up delay

When a VSX device is rebooted, it has no entries for MAC, ARP, routes. If downstream VSX LAG ports are
activated before the information is relearned, traffic is dropped. To avoid a traffic drop, VSX LAGs on the
rebooted device stay down until the restore of LACP, MAC, ARP, and MSTP databases.

The learning process has two phases:

n Initial synchronization phase:

o This phase is the download phase where the rebooted node learns all the LACP+MAC+ARP+STP

database entries from its VSX peer through ISLP.

o The initial synchronization timer, which is not configurable, is the required time to download the

database information from the peer.

n Link-up delay phase:

o This phase is the duration for:

l

Installing the downloaded entries to the ASIC.

l Establishing router adjacencies with core nodes and learning upstream routes.

o The link-up delay timer default value is 180 seconds.

o Depending on the network size, ARP/routing tables size, you might be required to set the timer to

a higher value (maximum 600 seconds).

When both VSX devices reboot, the link-up delay timer is not used.

To get upstream router adjacencies established during the link-up delay, the upstream LAG (for example
LAG 101) has to be excluded from the scope of the link-up delay. Even if the upstream VSX node is not
excluded from the link-up delay timer, OSPFv2/OSPFv3 neighborship forms, when active-forwarding is
enabled on a VLAN. While the link-up delay timer is running, all SVIs that contain VSX LAG members are
kept in a pseudo-shutdown state.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide

50

The link-up delay timer during an ISL failure

Configure the link-up delay timer and exclude LAGs so that if an ISL goes down, the downed ISL does
not impact the state of the VLAN, and its SVI that is not a part of a VSX LAG. This SVI is part of at least
one orphan port (besides the ISL LAG which is not a VSX LAG).

The following scenario explains what happens:

n During the ISL going down (before the initial synchronization): As long as the secondary VSX
node has a port that is a member of a VSX LAG, the associated SVI of the VLAN (transported by the
VSX LAG) turns to OFF/SHUT on the VSX secondary node. This situation occurs regardless of orphan
ports carrying the given VLAN.

n During the running of the link-up delay timer (after the initial synchronization):

As long as the secondary VSX node has a port that is a member of a VSX LAG, the associated SVI of the
VLAN (transported by the VSX LAG) turns to OFF/SHUT on the VSX secondary node. This situation occurs
regardless of orphan ports carrying the given VLAN.

The associated SVI of the VLAN transported by VSX LAG restores to ON/UP on the VSX secondary node,
only if the following two conditions are met:

Preventing traffic loss | 51

o TheVSXLAGisexcludedfromthelink-updelaytimerbythefollowingcommand:linkup-delay-timer
exclude lag-list
o ThegivenVLANisnotallowedonaVSXLAGthatisnotinthepartoftheexclusionset.
ThefollowingexampleshowshowanetworkwasconfiguredsoanSVIthatwasnotpartofaVSXLAG
(SVI16inthiscase)wasrestored.Thisexamplealsoshowsthelink-updelaytimerandtheexclusionof
LAGs.
Thenetworkinthefollowingexamplewasconfiguredas:
n VLAN16isseton1/1/5(access).
n VLAN10taggedasVSXLAG11.*
n LAG1isnotaVSXLAG.*
n LAG2andLAG11areVSXLAGs.
*Thisinformationisnotaccessiblefromthefollowingexample.
| switch# | show vlan 10 |     |     |     |     |
| ------- | ------------ | --- | --- | --- | --- |
-------------------------------------------------------------------------------
| VLAN Name |     |     | Status Reason | Type | Interfaces |
| --------- | --- | --- | ------------- | ---- | ---------- |
-------------------------------------------------------------------------------
| 10 test_vlan10 |     |     | up ok | static | 1/1/7,lag1-lag2,lag11- |
| -------------- | --- | --- | ----- | ------ | ---------------------- |
lag12,
lag14,lag16,lag112
| switch# | show vlan 15 |     |     |     |     |
| ------- | ------------ | --- | --- | --- | --- |
-------------------------------------------------------------------------------
| VLAN Name |     |     | Status Reason | Type | Interfaces |
| --------- | --- | --- | ------------- | ---- | ---------- |
-------------------------------------------------------------------------------
| 15 ZTP_VLAN |              |     | up ok | static | lag1-lag2 |
| ----------- | ------------ | --- | ----- | ------ | --------- |
| switch#     | show vlan 16 |     |       |        |           |
-------------------------------------------------------------------------------
| VLAN Name |     |     | Status Reason | Type | Interfaces |
| --------- | --- | --- | ------------- | ---- | ---------- |
-------------------------------------------------------------------------------
| 16 VLAN16 |               |     | up ok | static | 1/1/5,lag1 |
| --------- | ------------- | --- | ----- | ------ | ---------- |
| switch#   | show vlan 200 |     |       |        |            |
-------------------------------------------------------------------------------
| VLAN Name |     |     | Status Reason | Type | Interfaces |
| --------- | --- | --- | ------------- | ---- | ---------- |
-------------------------------------------------------------------------------
| 200 interco_vlan |              |     | up ok | static | lag1-lag2 |
| ---------------- | ------------ | --- | ----- | ------ | --------- |
| switch#          | show run vsx |     |       |        |           |
vsx
| system-mac         | 00:00:00:01:01:01  |              |        |              |               |
| ------------------ | ------------------ | ------------ | ------ | ------------ | ------------- |
| inter-switch-link  |                    | lag 1        |        |              |               |
| role               | secondary          |              |        |              |               |
| keepalive          | peer 192.168.10.1  |              | source | 192.168.10.2 | vrf KeepAlive |
| linkup-delay-timer |                    | exclude      | lag 2  |              |               |
| linkup-delay-timer |                    | 60           |        |              |               |
| switch#            | show vsx status    | linkup-delay |        |              |               |
| Configured         | linkup delay-timer |              |        | : 60 seconds |               |
| Initial            | sync status        |              |        | : Completed  |               |
| Delay timer        | status             |              |        | : Running    |               |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 52

| Linkup     | Delay  | time       | l        |         |            | : 0 minutes                      | 58 seconds |
| ---------- | ------ | ---------- | -------- | ------- | ---------- | -------------------------------- | ---------- |
| Interfaces | that   | will       | be       | brought | up after   |                                  |            |
| delay      | timer  | expires    |          |         |            | : lag11-lag12,lag14,lag16,lag112 |            |
| Interfaces | that   | are        | excluded |         | from delay |                                  |            |
| timer      |        |            |          |         |            | : lag2                           |            |
| switch#    | show   | int vlan10 |          |         |            |                                  |            |
| Interface  | vlan10 | is         | down     |         |            |                                  |            |
| Admin      | state  | is up      |          |         |            |                                  |            |
Description:
| Hardware:    | Ethernet, |                   | MAC | Address:          | 94:f1:28:1d:ad:00 |     |     |
| ------------ | --------- | ----------------- | --- | ----------------- | ----------------- | --- | --- |
| IPv4 address |           | 10.10.10.3/26     |     |                   |                   |     |     |
| active       | gateway   | 10.10.10.1        |     | 00:00:00:00:11:01 |                   |     |     |
| active       | gateway   | 2002:0a0a:0a00::1 |     |                   | 00:00:00:00:66:01 |     |     |
| switch#      | sh int    | vlan15            |     |                   |                   |     |     |
| Interface    | vlan15    | is                | up  |                   |                   |     |     |
| Admin        | state     | is up             |     |                   |                   |     |     |
Description:
| Hardware:    | Ethernet, |                | MAC | Address: | 94:f1:28:1d:ad:00 |     |     |
| ------------ | --------- | -------------- | --- | -------- | ----------------- | --- | --- |
| IPv4 address |           | 10.10.15.12/24 |     |          |                   |     |     |
| switch#      | sh int    | vlan16         |     |          |                   |     |     |
| Interface    | vlan16    | is             | up  |          |                   |     |     |
| Admin        | state     | is up          |     |          |                   |     |     |
Description:
| Hardware:    | Ethernet, |               | MAC   | Address: | 94:f1:28:1d:ad:00 |     |     |
| ------------ | --------- | ------------- | ----- | -------- | ----------------- | --- | --- |
| IPv4 address |           | 10.10.16.2/24 |       |          |                   |     |     |
| switch#      | sh int    | vlan200       |       |          |                   |     |     |
| Interface    | vlan200   |               | is up |          |                   |     |     |
| Admin        | state     | is up         |       |          |                   |     |     |
Description:
| Hardware:    | Ethernet, |                | MAC | Address: | 94:f1:28:1d:ad:00 |     |     |
| ------------ | --------- | -------------- | --- | -------- | ----------------- | --- | --- |
| IPv4 address |           | 10.10.212.6/29 |     |          |                   |     |     |
Asexpected,SVI10isinpseudo-shutduringthelink-updelay.SVI10wasapartofLAG2whichisin
exclusion.SVI16isup,asexpectedbecauseSVI16wasnotpartofaVSXLAG.
| Split brain |     | scenario |     |     |     |     |     |
| ----------- | --- | -------- | --- | --- | --- | --- | --- |
AsplitbrainscenariooccurswhenbothkeepaliveandtheISLisdown,asshowninthefollowfigure.
WhentheISLisrestored,thereisnorebootofthesecondaryswitch.Ifsplitrecoveryisenabled(the
defaultsetting),thesecondaryVSXLAGsarebroughtupafterthetimesetbythelinkup-delay-timer
command.
Preventingtrafficloss|53

Keepalive

Keepalive is a layer 3 interface that is used to exchange heartbeats between VSX peer switches. The
heartbeats are exchanged by using the User Datagram Protocol (UDP) and port 7678 (default). During
an ISL failure, VSX switches use their keepalive connection to determine if both VSX switches are up and
running. This configuration helps the VSX switches find alternative paths to the ISL link in the network so
the two VSX switch can continue to stay in-sync.

Configure each VSX peer switch with a keepalive connection to the other VSX peer switch. This
connection is established over a routed network (IPv4 currently) and is not required to be a dedicated
peer-to-peer link unlike ISL. Keepalive packets are UDP-based.

Make sure that the VSX peer switches have layer 3 reachability for keepalive interfaces through directly
connected interfaces or routed through the upstream layer 3 network. Source of keepalive interfaces
can be a layer 3 interface (router port), a loopback interface, or a Switch Virtual Interface (SVI). An SVI is a
logical layer 3 interface configured per VLAN (one-to-one mapping) that performs all layer 3 processing
for packets to or from all switch ports associated with that VLAN.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

54

With respect to the keepalive path, it is highly recommended to separate keepalive traffic from the ISL link.

Use a dedicated layer 3 link and as a best practice, also use a dedicated VRF, as shown in Recommended network

configuration for keepalive.

Keepalive packets can be sourced from the supported layer 3 interface; however, the packet must not be

transported over the ISL.

In the case of 6400 and 8400 switch series, it highly recommended to use keepalive and ISL on different
line cards. A single point of failure on line card that has keepalive and ISL configuration might cause split
brain.

Keepalive response in ISL failure scenarios

n ISL link is down but the switches are still up and running: In this case, VSX switches use their

keepalive connection to determine that they are both up and running. Once that is determined, the
user-configured primary VSX switch keeps its multichassis (VSX) LAG links up and the secondary VSX
switch forces its VSX LAG links to go down with the appropriate reason. Once the ISL link is up, the
MAC and ARP tables of the primary switch are synchronized to the secondary switch. Then, the
configured delay timer starts. Once the delay timer expires, the secondary VSX switch brings up its
VSX LAG links.

n ISL link and one of the VSX switches is down: The running switch sees that the ISL and keepalive
connection are both down. Independent of the user configured role (primary or secondary), the
switch that is up continues to keep its VSX LAG links up. Subsequently when the peer switch returns,
the ISL link comes up first. Then, the returned VSX peer switch synchronizes its MAC and ARP tables
from the peer switch that stayed up. After the synchronization completes, the delay time starts. Once
the delay timer expires, the VSX peer switch brings up its VSX LAG links.

Keepalive scenario

The following diagram illustrates a scenario in which both VSX switches are up, but the ISL link is down.
The switches cannot exchange information.

The keepalive functionality brings down the link between Switch B and Switch C in the following
diagram. The traffic is forced to go from Switch C to Switch A and then through the Layer 3 network to
access Switch B. The keepalive path is over the Layer 3 network. Traffic traveling from Switch B to Switch
A is also forced to go through the Layer 3 network.

Preventing traffic loss | 55

Figure1 Keepalivetopology
DonothavethekeepalivepathgooverISL.Useadirect-linkconnectionforkeepalive.Ifthekeepalivepathuses
ISLasitsonlypathandanISLlinkfailureoccurs,theVSXswitcheswouldbeoutofsyncwithoutthekeepalive
functioning.
Keepalive configurations
| Task | Command |     | Example |     |
| ---- | ------- | --- | ------- | --- |
Configuringkeepalivepeer keepalive peer <IP-ADDR> switch(config-vsx)# keepalive
sourceandVRF.
|     | source <IP-ADDR> | [<VRF- | peer 192.168.1.1 | source   |
| --- | ---------------- | ------ | ---------------- | -------- |
|     | NAME>]           |        | 192.168.1.5      | vrf vrf1 |
Unconfiguringkeepalive. no keepalive switch(config-vsx)# no keepalive
ConfiguringkeepaliveUDP keepalive udp-port switch(config-vsx)# keepalive
| port. | <PORT-NUM> |     | udp-port | 2000 |
| ----- | ---------- | --- | -------- | ---- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 56

| Task |     | Command | Example |     |
| ---- | --- | ------- | ------- | --- |
Restoringdefaultkeepalive no keepalive udp-port switch(config-vsx)# no keepalive
UDPport.
udp-port
Configuringkeepalivehello keepalive hello-interval switch(config-vsx)# keepalive
| interval. |     | <HELLO-INTERVAL> | hello-interval | 3   |
| --------- | --- | ---------------- | -------------- | --- |
Restoringdefaultkeepalive no keepalive hello- switch(config-vsx)# no keepalive
| hellointerval. |     | interval | hello-interval |     |
| -------------- | --- | -------- | -------------- | --- |
Configuringkeepalivedead keepalive dead-interval switch(config-vsx)# keepalive
| interval. |     | <DEAD-INTERVAL> | dead-interval | 10  |
| --------- | --- | --------------- | ------------- | --- |
Restoringdefaultkeepalive no keepalive dead- switch(config-vsx)# no keepalive
deadinterval.
|     |     | interval | dead-interval |     |
| --- | --- | -------- | ------------- | --- |
Defaultvalues:
n Keepalivedeadinterval:3seconds
n Hellointerval:1second
n UDPportforthekeepaliveprotocol:7678
| Recommended | network | configuration | for keepalive |     |
| ----------- | ------- | ------------- | ------------- | --- |
Directlyconnectthekeepalivelink,asshowninthefollowingfigure.Avoidkeepalivecommunication
overtheISLcircuits.
Preventingtrafficloss|57

Figure 1 Recommended configuration for keepalive

Do not configure keepalive to go through the VSX LAG uplinks, as shown in the following image. This
scenario is not supported because:

n VSX LAG on the secondary will clear because split detection.

n Keepalive communication will stop between the VSX switches.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

58

| Figure2       | Notsupportedconfigurationforkeepalive |            |            |
| ------------- | ------------------------------------- | ---------- | ---------- |
| Active        | gateway                               | and active | forwarding |
| Active-active | layer                                 | 2          |            |
VSXLAGsspantwoswitchesandoperateinactive-activemode.Trafficbetweentheaccesslayerand
aggregationlayerswitchescanbeforwardedtoanyoftheactivelinks.Therearenoloopsandnoneed
forspanningtreeprotocolorblockedports.
Fromadatapathperspective,eachVSXswitchthatgetsapacketalwaysusesitslocallinksoftheLAGto
forwardtraffictothedestination.TheVSXswitchonlyusestheISLlinkifthelocalLAGlinksaredown.
| Layer 2 | configuration |     |     |
| ------- | ------------- | --- | --- |
Preventingtrafficloss|59

Networkdiagramshowingactive-activelayer2configuration.Agg1andAgg2areshownalongwiththe
locallinksoftheLAGtoforwardtraffictothedestination.
Thefollowingshowstheconfigurationdetailsfromthefigure:
| interface lag | 11 multi-chassis |     |     |
| ------------- | ---------------- | --- | --- |
description access-sw1
no shutdown
no routing
| vlan | trunk native  | 1          |     |
| ---- | ------------- | ---------- | --- |
| vlan | trunk allowed | 5,10,15,20 |     |
lacp mode active
| interface lag | 12 multi-chassis |     |     |
| ------------- | ---------------- | --- | --- |
description access-sw2
no shutdown
no routing
| vlan | trunk native  | 1          |     |
| ---- | ------------- | ---------- | --- |
| vlan | trunk allowed | 5,10,15,20 |     |
lacp mode active
| interface 1/1/1 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 11
| interface 1/1/2 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 12
| Active-active | layer | 3 default | gateway |
| ------------- | ----- | --------- | ------- |
VSXaggregationswitchescanbeconfiguredwithasharedvirtualIP(VIP)andasharedvirtualMAC
address(VMAC)onthelayer3VLANinterface.
TheVIP/VMACservesasthedefaultgatewayfortheaccesslayer.Thetwoswitchesthensharethe
routerMACandfunctionasanactive-activegatewayfortheIPsubnet.ThefirstVSXdevicethatreceives
trafficfromtheaccesslayer(basedonthehashingalgorithmovertheLAGinterface)routesitacrossto
theothersubnets.
| Active gateway | over | VSX |     |
| -------------- | ---- | --- | --- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 60

Activegatewayisafirsthopredundancyprotocolthateliminatesasinglepointoffailure.Theactive
gatewayfeatureisusedtoincreasetheavailabilityofthedefaultgatewayservicinghostsonthesame
subnet.Anactivegatewayimprovesthereliabilityandperformanceofthehostnetworkbyenablinga
virtualroutertoactasthedefaultgatewayforthatnetwork.
Ifyouhaveenabledactivegateway,VRRPisnotrequired.ActivegatewayissimilartoVRRPinthat
routedtrafficfromtheVSXnodeissourcedfromtheswitchinterfaceMACandnotthevirtualMAC
address(VMAC).EachactivegatewaysendsaperiodicbroadcasthellopackettoavoidVMACagingon
theaccessswitches.TheswitchviewstheactivegatewayIPasaselfIPaddress.
ActivegatewayispreferableoverVRRPbecausewithVRRPtrafficisstillpushedovertheISLlink,
resultinginlatencyinthenetwork.
| VMACs and active gateway |     |     |
| ------------------------ | --- | --- |
TherecanbeonlyonevirtualMACaddress(VMAC)eachforIPv4andIP6,andtheVIPandVMACmust
bethesameonbothVSXswitches.
Youcanhaveamaximumof16differentVMACsperVSXpair.YoucanconfigurethesameVMACfor
bothIPv4andIPv6.Forexample:YoucanhaveamaximumofeightVMACsforIPv4,simultaneously
havingamaximumofeightVMACsforIPv6.
Only15VMACsaresupportedon6400switchseries.
IfaVMACisdifferentforIPv4andIPv6,theswitchcreatestwodifferentinterfaces,oneforIPv4and
anotherforIPv6:
interface vlan2
| active-gateway ip   | mac 0a:0b:0c:0d:0e:0e |                          |
| ------------------- | --------------------- | ------------------------ |
| active-gateway ipv6 | mac 00:00:00:00:00:01 |                          |
| 0020a0b0c0d0e0eLink | encap:Ethernet        | HWaddr 0A:0B:0C:0D:0E:0E |
| 002000000000001Link | encap:Ethernet        | HWaddr 00:00:00:00:00:01 |
IfaVMACisthesameforIPv4andIPv6,onlyonekernelinterfaceiscreatedforbothIPv4andIPv6:
interface vlan3
| active-gateway ip   | mac 00:00:00:00:00:01 |                          |
| ------------------- | --------------------- | ------------------------ |
| active-gateway ipv6 | mac 00:00:00:00:00:01 |                          |
| 003000000000001Link | encap:Ethernet        | HWaddr 00:00:00:00:00:01 |
DonotusepeersystemMACaddressasanactive-gatewayVMAC.IfsameMACaddressisused,theVSX
synchronizationwilltrytosynctheconfigurationonsecondaryswitchandcausetrafficdisruptions.
Requirements
n Beforeconfiguringactivegateway,confirmthatanIPaddressisontheSVIthatisinthesamesubnet
astheactivegatewayIPyouaretryingtoconfigure.IfanactivegatewayIPdoesnothaveanSVIIP
withthesamesubnet,theCLIallowstheconfiguration,buttheactivegatewayIPwillnotbe
programmedinthekernel,resultingtheactivegatewaytobeunreachable.
Preventingtrafficloss|61

n An active gateway can be configured only over an SVI. If active gateway and SVI IP addresses are the
same, make sure that SVI IP addresses are consistent across VSX switches. If you have a VSX square
topology that contains two pairs of VSX switches, make sure that you do not have the same IP
address across all four VSX nodes in the square topology.

n Active gateway configuration must be the same in both the VSX peer switches.

n Having same VMAC and different active gateway IP addresses on different VSX segments in a square

topology is not supported. Ensure that you have either same VMAC and same active gateway IP
addresses or different VMAC and different active gateway IP addresses configured on two different
VSX segments. For 8320, 8325, 9300, and 10000 switch series, when VMAC and active gateway IP
addresses are same, make sure that the SVI status is identical on both the VSX segments.

n If a system has active forwarding enabled, reduce one VMAC from the total number of VMACs

supported in the system. An active gateway can have a maximum of 14 "unique" MAC addresses per
system, both IPv4 and IPv6 addresses are included in the count.

n If a system has active forwarding disabled, an active gateway can have a maximum of 16 "unique"

MAC addresses per system, both IPv4 and IPv6 addresses are included in the count.

n With IP multinetting, a maximum of 32 IPv4 active gateway and a maximum of 31 IPv6 active gateway

can be configured. A recommended configuration is a multidimension scale (MD) scale and a
maximum network limit, along with four IPv4 active gateways and four IPv6 active gateways per SVIs
with a maximum of 512 SVIs per chassis. An MD scale is when the VSX active-gateway along with
other supported features, such as layer 2, layer 3, and multi-VRF are enabled and the system
response/stability is validated against them.

n Link local IPv6 virtual IP address of an active gateway address is multicasted for router advertisement

so that the IPv6 address can be chosen as a default gateway.

n Active gateway configuration must be the same in both the VSX peer switches.

n Disable IP ICMP redirect when IP multinetting is enabled.

n Disable ICMP redirect when routing is enabled through an active gateway SVI where egress port

belongs to same VLAN as ingress.

Example of IPv4 and IPv6 active gateways on an SVI

Assume that you have IPv4 and IPv6 active gateways on an SVI. Each SVI uses a MAC address for IPv4
and one for IPv6. The configuration of the VSX with an active-gateway consumes a second MAC address
per SVI.

switch# sh int vlan10

Interface vlan10 is up
Admin state is up
Description: ACCESS switch mgmt
Hardware: Ethernet, MAC Address: 98:f2:b3:68:71:fe
IPv4 address 10.1.1.253/24
Rx L3: 0 packets, 0 bytes
Tx L3: 0 packets, 0 bytes

switch# sh run int vlan141
interface vlan141

description USER VLAN 10.141.0.0/16
ip address 10.141.255.253/16
ip ospf 1 area 0.0.0.0
ip pim-sparse enable

ip igmp enable
ip igmp version 2

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

62

exit

switch# config
switch(config)# int vlan10
switch(config-if-vlan)# active-gateway ip 10.1.1.254 mac 00:00:00:10:11:12
switch# sh int vlan10

Interface vlan10 is up
Admin state is up
Description: ACCESS switch mgmt
Hardware: Ethernet, MAC Address: 98:f2:b3:68:71:fe
IPv4 address 10.1.1.253/24
active gateway 10.1.1.254
Rx L3: 0 packets, 0 bytes
Tx L3: 0 packets, 0 bytes

00:00:00:10:11:12

Interface vlan10 is up
Admin state is up
Description: ACCESS switch mgmt
Hardware: Ethernet, MAC Address: 98:f2:b3:68:71:fe
IPv4 address 10.1.1.253/24
active gateway 10.1.1.254
Rx L3: 0 packets, 0 bytes
Tx L3: 0 packets, 0 bytes

00:00:00:10:11:12

IP multinetting over VSX

IP multinetting is the assignment of more than one IP interface to a single VLAN that is used to enable a

router to provide default gateway service to different address ranges associated with a single VLAN.

When using IP multinetting in an environment with VSX enabled, you must configure multiple active
gateway IP addresses per SVI so that you can reach multiple networks on the same VLAN. Make sure
that you configure an IP address for either the primary or secondary VSX switch on the SVI with the
same subnet.

The maximum number of supported active gateways per switch is 4,000. Since a maximum of 31
secondary IPv4 addresses can be configured on an SVI, 32 IPv4 active gateways (along with the primary
IPv4 address) can be configured per SVI with IP multinetting support. This support is also the same for
IPv6 addresses.

Disable IP ICMP redirect when IP multinetting is enabled.

Multiple active gateways IP addresses can be programmed on the same active gateway kernel interface,
as shown in the following example:

interface vlan3
ip address 10.0.0.1/24
ip address 20.0.0.1/24 secondary
active-gateway ip mac 00:00:00:00:00:01
active-gateway ip 10.0.0.3
active-gateway ip 20.0.0.3

003000000000001@vlan3: <NO-CARRIER,BROADCAST,UP,M-DOWN> mtu 1500 qdisc noqueue
state LOWERLAYERDOWN group default qlen 1000
link/ether 00:00:00:00:00:01 brd ff:ff:ff:ff:ff:ff
inet 10.0.0.3/32 scope global 003000000000001

Preventing traffic loss | 63

| valid_lft        | forever preferred_lft |        | forever         |     |     |     |
| ---------------- | --------------------- | ------ | --------------- | --- | --- | --- |
| inet 20.0.0.3/32 | scope                 | global | 003000000000001 |     |     |     |
| valid_lft        | forever preferred_lft |        | forever         |     |     |     |
ActivegatewayVMACandVIPscanbeconfiguredseparately:
| interface      | vlan3          |                   |     |     |     |     |
| -------------- | -------------- | ----------------- | --- | --- | --- | --- |
| ip address     | 10.0.0.1/24    |                   |     |     |     |     |
| ip address     | 20.0.0.1/24    | secondary         |     |     |     |     |
| active-gateway | ip mac         | 00:00:00:00:00:01 |     |     |     |     |
| active-gateway | ip 10.0.0.3    |                   |     |     |     |     |
| active-gateway | ip 20.0.0.3    |                   |     |     |     |     |
| Active gateway | configurations |                   |     |     |     |     |
Comma
| Task |     | Example |     |     |     |     |
| ---- | --- | ------- | --- | --- | --- | --- |
nd
active-
Configuring
|     |     | switch(config)# | vlan | 2   |     |     |
| --- | --- | --------------- | ---- | --- | --- | --- |
gateway
| avirtual |     | switch(config)# | interface | vlan 2 |     |     |
| -------- | --- | --------------- | --------- | ------ | --- | --- |
{ip |
| IPv4and |       | switch(config-if-vlan)# |     | ip address     | 10.0.0.1/24 |     |
| ------- | ----- | ----------------------- | --- | -------------- | ----------- | --- |
|         | ipv6} | switch(config-if-vlan)# |     |                |             |     |
| IPv6    |       |                         |     | active-gateway | ip 10.0.0.2 | mac |
[<IP-
00:00:00:00:00:01
| addressfor | ADDRESS> |                         |     |              |                 |     |
| ---------- | -------- | ----------------------- | --- | ------------ | --------------- | --- |
|            |          | switch(config-if-vlan)# |     | ipv6 address | aa:bb::cc:dd/24 |     |
aninterface
|       | ]    | switch(config-if-vlan)# |     | active-gateway | ipv6 2001:DB8::/32 |     |
| ----- | ---- | ----------------------- | --- | -------------- | ------------------ | --- |
| VLAN. | [mac | mac 00:00:00:01:00:01   |     |                |                    |     |
<MAC-
ADDRESS>
]
| Unconfiguri | no  |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- |
switch(config-if-vlan)#
| ngactive | active- |     |     | no active-gateway | ip  |     |
| -------- | ------- | --- | --- | ----------------- | --- | --- |
gatewayfor
gateway
active-
{ip |
active
ipv6}
routing.
[<IP-
ADDRESS>
]
[mac
<MAC-
ADDRESS>
]
SeeIPmultinettingoverVSXforadditionalexamplesofIPmultinetting.
| VRRP with | VSX configuration |     |     |     |     |     |
| --------- | ----------------- | --- | --- | --- | --- | --- |
VRRPissimilartoactivegatewayinthatitisafirsthopredundancyprotocolthateliminatesasingle
pointoffailure.OneVSXswitchactsasaVRRPActiverouterandtheotherswitchactsastheVRRP
Standby.BothVSXswitchesroutethetraffic.Theactivegateway/VRRPconfigurationmustbeconsistent
acrossthetwoVSXswitches.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 64

AlthoughactivegatewayandVRRParenolongergloballyexclusiveinaVSXconfiguration,active
gatewayandVRRParestillexclusiveonanSVI.AworkaroundistoconfigureVRRPononeSVI(SVIA),
andconfigureactive-gatewayontheotherSVI(SVIB).
ActivegatewayispreferabletoVRRPbecauseVRRPtrafficisstillpushedovertheISLlink,resultinginlatency.
| Sample VRRP configuration |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- |
IPV4:
| switch(config)#         | vlan      | 1-10        |                  |     |         |
| ----------------------- | --------- | ----------- | ---------------- | --- | ------- |
| switch(config)#         | router    | vrrp enable |                  |     |         |
| switch(config)#         | interface | vlan2       |                  |     |         |
| switch(config-if-vlan)# |           | ip address  | 192.168.1.253/16 |     |         |
| switch(config-if-vlan)# |           | no shutdown |                  |     |         |
| switch(config-if-vlan)# |           | vrrp 1      | address-family   |     | ipv4    |
| switch(config-if-vrrp)# |           | address     | 192.168.1.253    |     | primary |
| switch(config-if-vrrp)# |           | no shutdown |                  |     |         |
| switch(config-if-vrrp)# |           | exit        |                  |     |         |
| switch(config-if-vlan)# |           | exit        |                  |     |         |
switch(config)#
IPV4andIPV6:
| switch(config)#         | vlan      | 1-10         |                |              |         |
| ----------------------- | --------- | ------------ | -------------- | ------------ | ------- |
| switch(config)#         | router    | vrrp enable  |                |              |         |
| switch(config)#         | interface | vlan3        |                |              |         |
| switch(config-if-vlan)# |           | ip address   | 172.3.0.1/16   |              |         |
| switch(config-if-vlan)# |           | ipv6 address |                | 2002:3::1/64 |         |
| switch(config-if-vlan)# |           | ip ospf      | 1 area         | 0.0.0.0      |         |
| switch(config-if-vlan)# |           | ipv6 ospfv3  | 1              | area         | 0.0.0.0 |
| switch(config-if-vlan)# |           | vrrp 1       | address-family |              | ipv4    |
| switch(config-if-vrrp)# |           | address      | 172.3.0.10     |              | primary |
| switch(config-if-vrrp)# |           | no shutdown  |                |              |         |
| switch(config-if-vrrp)# |           | exit         |                |              |         |
| switch(config-if-vlan)# |           | vrrp 1       | address-family |              | ipv4    |
| switch(config-if-vrrp)# |           | address      | fe80::3        | primary      |         |
| switch(config-if-vrrp)# |           | no shutdown  |                |              |         |
| switch(config-if-vrrp)# |           | exit         |                |              |         |
switch(config)#
Active forwarding
Activeforwardingisanoptimizationforlayer3unicasttrafficflowingfromtheupstream(core)tothe
downstream(access)throughtheVSXpeers(aggregate).Activeforwardingpreventsthebridgedtraffic
fromswitchingovertheISL.ItalsominimizeslatencyandtheISLbandwidth.
| Active forwarding | requirements |     |     |     |     |
| ----------------- | ------------ | --- | --- | --- | --- |
n ActiveforwardingisenabledonaSVIfacingcorenetworkonaVSXenvironment.
n ActiveforwardingissupportedonSVIonly.
n Activeforwardingandactivegatewayaremutuallyexclusivefeatures.Youcannotenablebothactive
forwardingandactivegatewayonthesameSVI.
n AlthoughtheCLIitselfdoesnotlimitthenumberofactiveforwardingSVIs;themaximumnumberof
configuredactiveforwardingSVIsis256.
Preventingtrafficloss|65

n Active forwarding is supported on more than one SVI per VRF.

n Active forwarding cannot be configured when ICMP redirect is enabled.

Traffic flow scenario

Active forwarding mitigates the suboptimal path scenarios because of undeterministic layer 3 hashing
and layer 2 hashing, as described in the following ECMP (equal-cost multi-path routing) scenario.

This scenario describes a situation when active forwarding is not used. In a VSX environment, a core
network is connected to a VSX pair, forming an OSPF adjacency over a VSX LAG. The VSX LAG has ECMP
routes to the access network. The core has ECMP routes to choose between either the VSX primary
switch or the VSX secondary switch for traffic flowing from the core to the access network. Assume that
ECMP picked the VSX primary switch. This traffic is now subjected to the hashing algorithm over the VSX
LAG interface. Based on the chosen hashing algorithm, the layer 2 interface might route the traffic to
the VSX secondary switch. The secondary VSX switch then bridges this traffic over the ISL to the primary
VSX switch. The primary VSX switch in turn routes the traffic toward the access network, which causes
extra overhead with ISL bandwidth and network latency.

If active forwarding was enabled in the previous scenario, the traffic destined for the access network
would not be bridged over the ISL. The traffic would flow from north to south instead, resulting in less
network latency. For more information about the benefits of active forwarding, along with a diagram,
see Benefits of active forwarding and active gateway.

Sample Active forwarding configuration

Primary# configure terminal
Primary(config)# no ip icmp redirect
Primary(config)# interface vlan 1000
Primary(config-if-vlan)# vsx active-forwarding
Primary(config-if-vlan)# end

Deployment options for upstream connectivity with active-active forwarding

Aggregate core links can be configured in one of the following ways:

n Layer 3-LAG/routed ports: Simple VLAN-free configuration best suited when the network runs on a
single VRF domain. With multiple VRFs in the network, one would need multiple routed ports, one per
VRF.

n P2P SVI links: Each aggregate-core link is on its own VLAN. The layer 2 links can carry traffic for

multiple SVIs and therefore multiple VRFs can be carried over the same link.

n VSX multichassis LAGs: The aggregate-core links can be multichassis layer 2 links carrying traffic for
multiple SVIs and VRFs. This configuration provides for layer 2 LAG and layer 3 ECMP-based active-
active forwarding for traffic from core to access.

In these configurations, the two VSX switches run as independent control planes (OSPF/BGP) and
present themselves as different routers in the network. In the datapath however, they function as a
single router and support active-active forwarding.

Benefits of active forwarding and active gateway

The enabling of active forwarding and active gateway reduces latency in the network by bypassing the
ISL link for north-south and south-north traffic, resulting in one less hop.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

66

When active forwarding is enabled, the north-south unicast traffic bypasses the ISL link for Agg1 and
Agg2. Just as the south-north traffic bypasses the ISL link for Agg1 and Agg2 when active gateway is
enabled, as shown in the following figure.

Figure 1 Active Forwardng and Active Gateway example

Virtual active gateway

A virtual active gateway is created by configuring the same IPv4 address in both the interface-VLAN
context and the active-gateway context.

Virtual active gateway enables the user to configure the same IPv4 address as both the interface VLAN
(SVIs) address as well as the active gateway address. A virtual active gateway is useful when the primary
purpose of the SVI is to provide just a first hop gateway service to its clients and does not need a
separate set of IPv4 addresses on each device and a virtual IPv4 address to serve the gateway
functionality.

Supported services on a virtual active gateway SVI

n DHCP Relay

n ARP

n VRF

n ACLs

n Dual stack (IPv6 requires active gateway to have different real and virtual IP addresses).

Preventing traffic loss | 67

n IPv6ActiveGW(withrealSVIIPv6)
n VSXActive-GWmultinetforIP
| Unsupported |     | services | for | a virtual | active gateway | SVI |
| ----------- | --- | -------- | --- | --------- | -------------- | --- |
n Layer3IPServices,suchasOSPF,BGP,IGMP,andBFD.
DHCPOption82
n
n PINGfromtheVSXdevicetodownstreamclientswithSRCIPastheactivegatewayIP.
n IPv6virtualactivegateway
| Sample | virtual | active | gateway | configuration |     |     |
| ------ | ------- | ------ | ------- | ------------- | --- | --- |
Avirtualactivegatewayconfigurationiscreatedinthisexampleandshowninthefollowingfigure.
| switch(config)#         |     | vlan | 3          |             |     |     |
| ----------------------- | --- | ---- | ---------- | ----------- | --- | --- |
| switch(config-vlan-3)#  |     |      | interface  | vlan 3      |     |     |
| switch(config-if-vlan)# |     |      | ip address | 10.0.0.2/24 |     |     |
switch(config-if-vlan)# active-gateway ip 10.0.0.3 mac 00:00:00:00:aa:aa
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformationabout
theCLIcommands.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 68

| Active-standby |     | DHCP relay |     |     |     |
| -------------- | --- | ---------- | --- | --- | --- |
WhenVSXsynchronizationisenabledforDHCPrelay,onlytheprimaryVSXnoderelaysDHCPrequests
totheupstreamDHCPserver.ThesecondaryVSXnodeforwardsovertheISLtotheprimaryVSXswitch
theDHCPrequestsreceivedfromthedownstreamendpoints.ThesecondaryVSXswitchtakesover
DHCP-relayserviceuponprimaryfailuredetection(ISLdownandkeepalivedown).UpstreamDHCP
serversreceiveasingleDHCPrequest.DownstreamclientsreceiveasingleDHCPoffer.
Formoreinformation,refertovsx-syncdhcp-relay
| DHCP relay | failure | if the SVI | is down | on the primary | switch |
| ---------- | ------- | ---------- | ------- | -------------- | ------ |
OnlytheprimaryVSXnoderelaysDHCPrequeststotheupstreamDHCPserver.Shuttingdownthe
associatedSVIontheprimaryVSXnodepreventsanyDHCPrequeststoberelayed.
Formoreinformation,refertovsx-syncdhcp-relay
| Split recovery |     | mode |     |     |     |
| -------------- | --- | ---- | --- | --- | --- |
Preventingtrafficloss|69

Split recovery mode prevents traffic loss when the ISL goes out-of-sync and keepalive subsequently fails.
When the ISL goes out-of-sync and keepalive is established, the secondary VSX LAGs are brought down.
If keepalive then also fails, this situation causes a split condition. In this case, if split recovery mode is
enabled, the secondary switch restores its VSX LAGs so they are up. The secondary VSX node brings up
the VSX LAGs after 10 keepalive packets are missed, approximately 10 seconds after keepalive goes
down.

The no split recovery command disables split recovery mode. When split recovery mode is disabled
during a split condition, the secondary switch keeps it VSX LAGs down.

VSX shutdown-on-split

VSX shutdown-on-split method prevents traffic loss by shutting down the non-VSX interfaces on the VSX
secondary when the ISL goes down or when the switch reboots. When the ISL goes down, all the
secondary VSX links are brought down but the non-VSX interfaces on the secondary switch will stay up.
In this scenario, if firewall, any active links, or single homed devices are connected to the secondary
switch, then the traffic is sent to secondary links since non-VSX interfaces are up. This situation causes a
traffic drop at the secondary device. To avoid the traffic disruption, you can shut down the non-
VSX interfaces using the vsx shutdown-on-split command when the ISL goes out-of-sync. This makes
the link between the firewall and secondary to go down. For more information, see vsx shutdown-on-
split.

IGMP snooping

VSX switches can be configured for IGMP snooping on downstream VLANs facing the access switches.
When enabled, the IGMP group database is independently constructed on each VSX switch. Multicast
traffic to these groups is appropriately pruned/optimized.

Each VSX switch has an identical IGMP group database:

n Each VSX node individually learns any JOIN/LEAVE message received from a downstream VSX LAG.
For example: Agg-1 learns on downlink from SW1, whereas Agg-2 learns on the ISL as the ISL is
always included as a forwarding port for IGMP, as shown in the following figure.

n The VSX IGMP process translates the received IGMP from the ISL into an IGMP join message from the

VSX LAG.

Multicast traffic to these IGMP groups is pruned/forwarded based on the individual IGMP group
database on each VSX node. ISLP does not synchronize IGMP groups between VSX peers. The IGMP
database construction is a data-plane based process.

If a VSX node reboots, it must relearn all the IGMP groups. The VSX switch floods multicast traffic within
the VLANs that have active physical ports being forwarded. It then sends an All Hosts Query message.
When the VSX node receives all join messages, it relearns and recreates the IGMP groups database.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

70

DHCP relay backup

When the two VSX switches are configured for DHCP relay on their VLAN interfaces, only the primary
switch actively relays DHCP client requests to the upstream server. The secondary switch acts as a
backup. If the primary VSX switch goes down, the secondary switch takes over, such in the case with ISL
and keepalive both down. Even though both primary and secondary switches receive the DHCP request,
the primary switch takes precedence.

The secondary VSX node forwards over the ISL to the primary VSX switch the DHCP requests received
from the downstream endpoints. The upstream DHCP servers receive a single DHCP request. The
downstream clients receive a single DHCP offer.

Both devices do not end up relaying DHCP requests to the server as duplicates. That scenario is usually
the case with typical aggregation switches running VRRP-based redundancy.

If SVI is disabled on the primary VSX node and the primary goes down, the secondary switch will not take over

and no DHCP requests will be relayed.

Preventing traffic loss | 71

IP multicast routing

Multicast PIM routing provides fast failover. For each VSX downstream VLAN, both VSX switches as a PIM
Designate Router (DR). One node is the actual DR, the other node is the proxy DR.

From the PIM protocol view point (join, prune, register. The role of the proxy DR is equal to the role of
the actual DR. The proxy DR also sends PIM join messages to the upstream PIM router. Any VSX node
receives a copy of IGMP join on the SL. Both the DR and proxy DR maintain the same multicast tables
and build the shortest path tree.

The proxy DR does not route traffic to downstream nodes. The proxy DR only acts as a bridge, all mroute
entries present in the DB for downstream VLAN is being set as bridge entries in the proxy DR ASIC, for
example pointing to the DR VSX node. Only the actual DR performs multicast routing and forward traffic
destined to groups to its downstream VLANs in the data-path. There is no PIM asset mechanism as PIM
forwarder is the DR.

DR/Proxy DR election is done per VLAN. Election process is first DR priority, then the highest IP address.

Multicast PIM routing is enabled through the active-active command. For example:
switch(config)# router pim
switch(config-pim)# active-active

See the Command-Line Interface Guide for your switch model and software version for more information
about the active-active command.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

72

Recommended values for system MAC and active gateway
VMAC

It is highly recommended to use unicast MAC Address when assigning system-mac or active-gateway
virtual MAC address. There are four ranges reserved for private use of unicast. The values are:

n x2-xx-xx-xx-xx-xx

n x6-xx-xx-xx-xx-xx

n xA-xx-xx-xx-xx-xx

n xE-xx-xx-xx-xx-xx

x can be any hexadecimal value.

Preventing traffic loss | 73

| Function    | System-mac        | Active gateway    | Virtual MAC |
| ----------- | ----------------- | ----------------- | ----------- |
| Access      | 02:00:00:00:XX:00 | 12:00:00:00:XX:0Y |             |
| Aggregation | 02:01:00:00:XX:00 | 12:01:00:00:XX:0Y |             |
| Core        | 02:02:00:00:XX:00 | 12:02:00:00:XX:0Y |             |
Intheabovetable,XXrepresentstheuniqueclusterIDinthefunctionandYrepresentsthevirtualMAC
ID(0toF).
DonotusemulticastandbroadcastMACaddressassystem-macaddress.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 74

Chapter 8

STP over VSX

STP over VSX

Without a spanning tree, having more than one active path between a pair of nodes causes loops in the
network, which can result in duplication of messages, leading to a “broadcast storm” that can bring
down the network. STP ensures that only one active path exists between any two nodes in a spanning
tree instance. A spanning tree instance comprises a unique set of VLANs, and belongs to a specific
spanning tree region. A region can comprise multiple spanning tree instances (each with a different set
of VLANs), and allows one active path among regions in a network.

Spanning-tree guards and filters are not allowed for configuration on the ISL.

Supported STP modes

The VSX switches support the following spanning tree protocols (STPs) with VSX:

n MSTP: Multiple Spanning Tree Protocol.

n RPVST: Rapid per-VLAN Spanning Tree Protocol.

How STP works with VSX

Both VSX switches appear as a single common Spanning Tree Bridge ID to STP partner devices upstream
and downstream that participate to the same Spanning Tree domain. STP can be enabled on VSX
switches and any nonrouting ports. Both VSX LAGs and non-VSX LAGs can participate in STP topology to
avoid any loops.

STP on VSX uses the same bridge ID with the same MAC address on VSX LAGs and non-VSX LAGs, orphan
ports. This MAC address is referred to as a common Bridge ID which consists of Spanning Tree priority
and the switch MAC Address. The STP port state is the same for VSX LAG ports in VSX peer switches.

The Spanning Tree protocol runs independently on VSX nodes, which conforms to the dual-control plane
VSX architecture. The primary VSX node is responsible to run the protocol for the VSX LAGs. In the
normal state, the primary is "operational primary" and the secondary is "operational secondary". If a
primary VSX node failure occurs, the secondary VSX node becomes the STP operational primary. When
the primary VSX node goes back up, it takes back ownership of the STP operational primary role.

On VSX LAG ports, STP runs only from the operational primary, shown in the following figure. The
operational secondary, also shown in the following figure, holds precomputed STP information for
ready-state switch over thanks to STP states synchronization. The operational primary does STP state
synchronization to the operational secondary for links member of the VSX LAG. That happens as a part
of the initial sync (LACP, MAC, ARP, MSTP). During the switch-over, the new operational primary sends
the BPDU downstream or upstream within 6 seconds (the default) of the spanning tree BPDU failure
detection timer: 3x hello-timer (2s per default).

ISL is always part of STP, nonblocking and it sends and receives BPDUs.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide

75

n Do not use the same system STP address for the other nodes. For the internal Spanning Tree protocol

between VSX nodes, the Bridge_ID of the primary and secondary VSX nodes are derived from (-1, +1) from
the system-mac <MAC-ADDR> command. For example, if the system MAC address is 00:00:00:00:00:10,
then the other system MAC addresses cannot be 00:00:00:00:00:09, 00:00:00:00:00:10, and

00:00:00:00:00:11.

n You must have identical STP configurations on the primary and secondary VSX switches.

n It is recommended to have common system MAC addresses configured under the VSX context for stable

STP convergence and stability.

Figure 1 Sample MST on VSX configuration

This figure shows MSTP with a VSX configuration showing BID1 ports as blocking.

For more information, see system-mac.

MSTP

STP over VSX | 76

| MSTP       | configurations |     |       |           |         |     |
| ---------- | -------------- | --- | ----- | --------- | ------- | --- |
| VSX at the | distribution   |     | layer | with MSTP | enabled |     |
Inthefollowingfigure,theVSXpairisconfiguredasarootswitch.AlltheportsoftheVSXLAGs,non-VSX
LAGs,andorphanportsareinaforwardingstate.BridgeProtocolDataUnits(BPDUs),generatedbya
VSXpair,arethesameonallports,includingVSXLAG,non-VSXLAG,andorphan.Allswitchesmustbein
thesameMSTPregionconsistingofthesameconfigurationnameandrevisionnumber,assetbythe
spanning-tree config-name <CONFIG-NAME>andspanning-tree config-revision <REVISION-
NUMBER>commands.
SwitchesinthemultipleMSTPregionconsistofdifferentconfigurationnameandrevisionnumber.The
followingexampleistheextractofMSTPmultipleregionconfiguration:
VSXswitch
| Primary#         | configure | terminal      |     |                 |       |     |
| ---------------- | --------- | ------------- | --- | --------------- | ----- | --- |
| Primary(config)# |           | spanning-tree |     | config-name     | mstp1 |     |
| Primary(config)# |           | spanning-tree |     | config-revision |       | 1   |
Non-VSXswitch
| Core# configure |     | terminal      |     |                 |       |     |
| --------------- | --- | ------------- | --- | --------------- | ----- | --- |
| Core(config)#   |     | spanning-tree |     | config-name     | mstp2 |     |
| Core(config)#   |     | spanning-tree |     | config-revision |       | 2   |
TheconfigurationshouldbesimilaronbothVSXprimaryandsecondaryswitches.
Table1:Definitionsoftheabbreviationsusedinthefiguresprovidedinthistopic
| Abbreviation |     |     | Definition                                        |     |     |     |
| ------------ | --- | --- | ------------------------------------------------- | --- | --- | --- |
| AB           |     |     | Alternateblocking;theportisinablockedstate.       |     |     |     |
| DF           |     |     | Designatedforwarding;theportisinaforwardingstate. |     |     |     |
| RF           |     |     | Rootforwarding;theportisinaforwardingstate.       |     |     |     |
SeeSampleconfigurationsforMSTPonVSXfortheconfigurationforthetopologiesdisplayedinthe
figuresinthistopic.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 77

Figure 1 MSTP VSX pair as a root switch

In the following figure, the VSX pair is not a root switch for STP topology. One of the VSX LAG ports is in
the blocking state for resolving an L2 network loop. The VSX LAG port is in a blocking state on both VSX
peer switches.

STP over VSX | 78

Figure 2 MSTP VSX pair as a nonroot switch

Distribution VSX pair connected to the core switch (SVI solution)

In the following figure, the VSX switch could be either a root switch or a nonroot switch for STP topology.
One of the uplinks connected from the distribution layer to the core switch is in a blocking state because
the MSTP is enabled in a VSX pair connected to a core switch, but the SVP configured without MSTP is
enabled.

This configuration might also cause the flooding of the MSTP BPDUs (VLAN unaware) based on the VLAN
configuration. VLANs must be configured differently on both ports to avoid flooding back to another VSX
pair. Configure the BPDU filter on L2 ports connected to the core switch so that these ports will be in a
forwarding state.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

79

| Figure3 DistributionlayerwithVSXandMSTPconnectedtothecoreswitch |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- |
Formoreinformation,seeBFDreportsaLAGasdownevenwhenhealthylinksarestillavailable
| Sample configurations |     | for MSTP | on VSX |
| --------------------- | --- | -------- | ------ |
ForscaledMSTPonVSXconfigurations,configureallMSTPglobalandportconfigurationsandthenenableMSTP.
ThefollowingconfigurationsareshowninMSTPVSXpairasarootswitchandinMSTPVSXpairasa
nonrootswitch
| Configurations | on the | VSX primary | switch |
| -------------- | ------ | ----------- | ------ |
Thefollowingexampleisanextractfromaconfiguration:
vlan 1-512
spanning-tree
| spanning-tree  | priority        | 2          |                              |
| -------------- | --------------- | ---------- | ---------------------------- |
| spanning-tree  | config-name     | Region-One |                              |
| spanning-tree  | config-revision |            | 1                            |
| spanning-tree  | instance        | 1 vlan     | 1,65,129,193,257,321,385,449 |
| spanning-tree  | instance        | 2 vlan     | 2,66,130,194,258,322,386,450 |
| spanning-tree  | instance        | 3 vlan     | 3,67,131,195,259,323,387,451 |
| interface mgmt |                 |            |                              |
no shutdown
ip dhcp
| interface lag | 10 multi-chassis |     |     |
| ------------- | ---------------- | --- | --- |
no shutdown
no routing
| vlan trunk       | native 1         |     |     |
| ---------------- | ---------------- | --- | --- |
| vlan trunk       | allowed all      |     |     |
| lacp mode active |                  |     |     |
| interface lag    | 20 multi-chassis |     |     |
no shutdown
no routing
| vlan trunk | native 1 |     |     |
| ---------- | -------- | --- | --- |
STPoverVSX|80

| vlan trunk    | allowed all   |     |     |     |
| ------------- | ------------- | --- | --- | --- |
| lacp mode     | active        |     |     |     |
| spanning-tree | port-priority |     | 1   |     |
| interface     | 1/1/1         |     |     |     |
no shutdown
lag 10
| interface | 1/1/2 |     |     |     |
| --------- | ----- | --- | --- | --- |
no shutdown
lag 20
| interface | 1/1/47 |     |     |     |
| --------- | ------ | --- | --- | --- |
no shutdown
no routing
| vlan trunk | native 1    | tag |     |     |
| ---------- | ----------- | --- | --- | --- |
| vlan trunk | allowed all |     |     |     |
| interface  | 1/1/48      |     |     |     |
no shutdown
| ip address | 1.1.1.1/24 |     |     |     |
| ---------- | ---------- | --- | --- | --- |
vsx
| inter-switch-link | 1/1/47            |     |     |     |
| ----------------- | ----------------- | --- | --- | --- |
| system-mac        | 02:02:02:02:02:02 |     |     |     |
role primary
| keepalive          | peer 1.1.1.2 | source | 1.1.1.1   |        |
| ------------------ | ------------ | ------ | --------- | ------ |
| linkup-delay-timer | 30           |        |           |        |
| Configurations     | on the       | VSX    | secondary | switch |
Thefollowingexampleisanextractfromaconfiguration:
vlan 1-512
spanning-tree
| spanning-tree | priority        | 2   |                                   |     |
| ------------- | --------------- | --- | --------------------------------- | --- |
| spanning-tree | config-name     |     | Region-One                        |     |
| spanning-tree | config-revision |     | 1                                 |     |
| spanning-tree | instance        | 1   | vlan 1,65,129,193,257,321,385,449 |     |
| spanning-tree | instance        | 2   | vlan 2,66,130,194,258,322,386,450 |     |
| spanning-tree | instance        | 3   | vlan 3,67,131,195,259,323,387,451 |     |
| interface     | mgmt            |     |                                   |     |
no shutdown
ip dhcp
| interface | lag 10 multi-chassis |     |     |     |
| --------- | -------------------- | --- | --- | --- |
no shutdown
no routing
| vlan trunk | native 1             |     |     |     |
| ---------- | -------------------- | --- | --- | --- |
| vlan trunk | allowed all          |     |     |     |
| lacp mode  | active               |     |     |     |
| interface  | lag 20 multi-chassis |     |     |     |
no shutdown
no routing
| vlan trunk    | native 1      |     |     |     |
| ------------- | ------------- | --- | --- | --- |
| vlan trunk    | allowed all   |     |     |     |
| lacp mode     | active        |     |     |     |
| spanning-tree | port-priority |     | 1   |     |
| interface     | 1/1/3         |     |     |     |
no shutdown
no routing
| vlan trunk | native 1    | tag |     |     |
| ---------- | ----------- | --- | --- | --- |
| vlan trunk | allowed all |     |     |     |
| interface  | 1/1/4       |     |     |     |
no shutdown
lag 10
| interface | 1/1/45 |     |     |     |
| --------- | ------ | --- | --- | --- |
no shutdown
lag 20
| interface | 1/1/46 |     |     |     |
| --------- | ------ | --- | --- | --- |
no shutdown
| ip address | 1.1.1.2/24 |     |     |     |
| ---------- | ---------- | --- | --- | --- |
| interface  | 1/1/47     |     |     |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 81

no shutdown
no routing
| vlan access | 1   |     |
| ----------- | --- | --- |
vsx
| inter-switch-link | 1/1/3             |     |
| ----------------- | ----------------- | --- |
| system-mac        | 02:02:02:02:02:02 |     |
role secondary
| keepalive          | peer 1.1.1.1          | source 1.1.1.2 |
| ------------------ | --------------------- | -------------- |
| linkup-delay-timer | 30                    |                |
| Configurations     | on left-access-switch |                |
Thefollowingexampleisanextractfromaconfiguration:
vlan 1-512
spanning-tree
| spanning-tree | config-name     | Region-One                          |
| ------------- | --------------- | ----------------------------------- |
| spanning-tree | config-revision | 1                                   |
| spanning-tree | instance        | 1 vlan 1,65,129,193,257,321,385,449 |
| spanning-tree | instance        | 2 vlan 2,66,130,194,258,322,386,450 |
| spanning-tree | instance        | 3 vlan 3,67,131,195,259,323,387,451 |
| interface     | mgmt            |                                     |
no shutdown
ip dhcp
| interface | lag 10 |     |
| --------- | ------ | --- |
no shutdown
no routing
| vlan trunk | native 1    |     |
| ---------- | ----------- | --- |
| vlan trunk | allowed all |     |
| lacp mode  | active      |     |
| interface  | 1/1/5       |     |
no shutdown
lag 10
| interface | 1/1/6 |     |
| --------- | ----- | --- |
no shutdown
lag 10
| interface | 1/1/43 |     |
| --------- | ------ | --- |
no shutdown
no routing
| vlan trunk     | allowed all            |     |
| -------------- | ---------------------- | --- |
| Configurations | on right-access-switch |     |
Thefollowingexampleisanextractfromaconfiguration:
vlan 1-512
spanning-tree
| spanning-tree | config-name     | Region-One                          |
| ------------- | --------------- | ----------------------------------- |
| spanning-tree | config-revision | 1                                   |
| spanning-tree | instance        | 1 vlan 1,65,129,193,257,321,385,449 |
| spanning-tree | instance        | 2 vlan 2,66,130,194,258,322,386,450 |
| spanning-tree | instance        | 3 vlan 3,67,131,195,259,323,387,451 |
| interface     | mgmt            |                                     |
no shutdown
ip dhcp
| interface | lag 20 |     |
| --------- | ------ | --- |
no shutdown
no routing
| vlan trunk | native 1    |     |
| ---------- | ----------- | --- |
| vlan trunk | allowed all |     |
| lacp mode  | active      |     |
| interface  | 1/1/7       |     |
no shutdown
lag 20
| interface | 1/1/8 |     |
| --------- | ----- | --- |
no shutdown
lag 20
| interface | 1/1/41 |     |
| --------- | ------ | --- |
STPoverVSX|82

no shutdown
no routing
vlan trunk allowed all

VSX and MSTP loop-protect configurations (physical and logical views)

The figures in this topic show the physical and logical views for VSX and MSTP loop-protect
configurations with MSTP as the default instance.

Figure 1 Physical view of the VSX and MSTP loop-protect configurations

The configuration from the previous figure is shown in its logical view, so that you can see how the
network views the configuration. For example, the following figure shows that the VSX distributed pair
as one switch. The ports on Agg-2 are blocking traffic. The logical view in the next figure shows that the
traffic is distributed so that the traffic continues to flow.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

83

Figure 2 Logical view of the VSX and MSTP loop-protect configurations

STP interoperability with Loop-Protect in VSX

When both loop protect and STP are enabled on the switch:

n If switch first detects STP, STP blocks the port to stop the loop and loop protect feature will not come

into effect.

n If switch first detects loop protect, loop protect blocks the port to stop the loop and STP will not take

any effect as there are no loops.

n If loop protect has re-enable timer enabled, the port will be unblocked once the timer is expired. In

this case, whichever protocol detects the loop first will block the port.

Show commands for MSTP

Before running the show commands, make sure that you have enabled STP synchronization between VSX peer

switches. See Enabling VSX synchronization of STP configurations between VSX peer switches.

Task

Action

Verify that all switches are in the same MSTP region
with the instance mapping to VLAN.

Enter the show spanning-tree mst-config
command.

STP over VSX | 84

Task

Action

View the latest topology changes of the VSX peer.

1. Synchronize the time by entering the NTP (vsx-

sync time) command.

2. Enter the show spanning-tree mst <0-64> vsx-

peer command.

Verify that the following global parameters are the

1. Enter the show running-config spanning-tree

same on VSX switches:

command.

n STP mode
n STP region configuration for MSTP (config-name

2. Enter the show running-config spanning-tree

vsx-peer command.

and config-revision)

n STP instance to VLAN mapping
n STP instance priority

MSTP with VSX guidelines

n Path cost is not allowed to be configured on the ISL port.

n Layer 2 link connected parallel to ISL link is blocked by MSTP.

n Do not configure port-specific spanning tree configurations on the ISL.

n Multiple instances are supported though (default + 64).

n Topology changes for VSX LAGs are accounted on the active multichassis LAG role only.

n MSTP is supported in both VSX and non-VSX environments.

n The common bridge ID continues to be used even after the VSX split brain scenario is identified.

n STP configurations on VSX LAG ports must be the same on VSX switches. Use vsx-sync mclag-

interfaces command for syncing STP and LAG interface configurations.

n Run the show running-config spanning tree and show running-config spanning tree vsx-peer

commands for verifying that the following global parameters are the same on VSX switches:

o STP mode.

o STP region configuration for MSTP (config-name and config-revision)

o STP instance to VLAN mapping

o STP instance priority

Alternatively, you can also use vsx-sync stp-global to sync all the above mentioned global commands.

RPVST

A Rapid Per VLAN Spanning Tree (RPVST) system creates one STP instance per VLAN. You are required to
create the RPVST instance explicitly.

For example to create an RPVST instance:

switch(config)# spanning-tree vlan 1

To create multiple RPVST instances, enter a range:

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

85

| switch(config)# |       | spanning-tree | vlan 1-100 |
| --------------- | ----- | ------------- | ---------- |
| Sample          | RPVST | configuration | with VSX   |
ThefollowingfigureshowsasampleRPVSTconfiguration.
Theconfigurationforthisfigureisprovidedinthefollowingsections.
| VSX Primary | Configuration |     |     |
| ----------- | ------------- | --- | --- |
configure
| hostname | vsx-pri |     |     |
| -------- | ------- | --- | --- |
vlan 1,10,20
| spanning-tree | mode | rpvst |     |
| ------------- | ---- | ----- | --- |
spanning-tree
| spanning-tree | vlan | 1,10,20 |     |
| ------------- | ---- | ------- | --- |
| interface     | mgmt |         |     |
no shutdown
ip dhcp
| interface | lag 1 | multi-chassis |     |
| --------- | ----- | ------------- | --- |
no shutdown
no routing
| vlan | trunk native  | 1   |     |
| ---- | ------------- | --- | --- |
| vlan | trunk allowed | all |     |
STPoverVSX|86

| lacp mode     | active |     |
| ------------- | ------ | --- |
| interface lag | 100    |     |
no shutdown
no routing
| vlan trunk | native 1    |     |
| ---------- | ----------- | --- |
| vlan trunk | allowed all |     |
| lacp mode  | active      |     |
interface 1/1/1
no shutdown
lag 100
interface 1/1/3
no shutdown
lag 1
interface 1/1/2
no shutdown
routing
| ip address | 1.1.1.1/24 |     |
| ---------- | ---------- | --- |
vsx
| system-mac        | 04:04:04:04:04:04 |     |
| ----------------- | ----------------- | --- |
| inter-switch-link | lag               | 100 |
role primary
| keepalive     | peer 1.1.1.2  | source 1.1.1.1 |
| ------------- | ------------- | -------------- |
| VSX secondary | configuration |                |
configure
hostname vsx-sec
vlan 1,10,20
| spanning-tree | mode rpvst |     |
| ------------- | ---------- | --- |
spanning-tree
| spanning-tree | vlan 1,10,20 |     |
| ------------- | ------------ | --- |
interface mgmt
no shutdown
ip dhcp
| interface lag | 1 multi-chassis |     |
| ------------- | --------------- | --- |
no shutdown
no routing
| vlan trunk    | native 1    |     |
| ------------- | ----------- | --- |
| vlan trunk    | allowed all |     |
| lacp mode     | active      |     |
| interface lag | 100         |     |
no shutdown
no routing
| vlan trunk | native 1    |     |
| ---------- | ----------- | --- |
| vlan trunk | allowed all |     |
| lacp mode  | active      |     |
interface 1/1/7
no shutdown
lag 100
interface 1/1/9
no shutdown
lag 1
interface 1/1/8
no shutdown
routing
| ip address | 1.1.1.2/24 |     |
| ---------- | ---------- | --- |
vsx
| system-mac        | 04:04:04:04:04:04 |     |
| ----------------- | ----------------- | --- |
| inter-switch-link | lag               | 100 |
role secondary
| keepalive     | peer 1.1.1.1  | source 1.1.1.2 |
| ------------- | ------------- | -------------- |
| Access switch | configuration |                |
configure
hostname l2-access
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 87

vlan 1,10,20
| spanning-tree | mode rpvst |     |     |
| ------------- | ---------- | --- | --- |
spanning-tree
| spanning-tree | vlan 1,10,20 |     |     |
| ------------- | ------------ | --- | --- |
| interface     | mgmt         |     |     |
no shutdown
ip dhcp
| interface | lag 1 |     |     |
| --------- | ----- | --- | --- |
no shutdown
no routing
| vlan      | trunk native  | 1   |     |
| --------- | ------------- | --- | --- |
| vlan      | trunk allowed | all |     |
| lacp      | mode active   |     |     |
| interface | 1/1/10        |     |     |
no shutdown
| lag       | 1      |     |     |
| --------- | ------ | --- | --- |
| interface | 1/1/11 |     |     |
no shutdown
| lag        | 1           |             |         |
| ---------- | ----------- | ----------- | ------- |
| VSX switch | with RPVST, | as root and | nonroot |
Inthefollowingfigure,theVSXpairisconfiguredasarootswitch.AlltheportsoftheVSXLAGs,non-VSX
LAGs,andorphanportsareinaforwardingstate.BridgeProtocolDataUnits(BPDUs),generatedbya
VSXpair,arethesameonallports,includingVSXLAG,non-VSXLAG,andorphan.
Table1:Definitionsoftheabbreviationsusedinthefiguresprovidedinthistopic
| Abbreviation |     | Definition                                        |     |
| ------------ | --- | ------------------------------------------------- | --- |
| AB           |     | Alternateblocking;theportisinablockedstate.       |     |
| DF           |     | Designatedforwarding;theportisinaforwardingstate. |     |
| RF           |     | Rootforwarding;theportisinaforwardingstate.       |     |
TomaketheVSXswitchrootforoneormoreRPVSTinstances,settheswitchtothelowestbridge
identifierforthetree:
n ForoneRPVSTinstance:switch(config)# spanning-tree vlan 1 priority 1
FormorethanoneRPVSTinstance:switch(config)# spanning-tree vlan 1-100 priority 1orswitch
n
| (config)# | spanning-tree | vlan 10,20,30 | priority 1 |
| --------- | ------------- | ------------- | ---------- |
Thepriorityparameterhasarangeof0to15forsettingthepriorityoftheRPVST.Thepriorityvalue
isconfiguredasamultipleof4,096(Default:8).Forexample,whenpriorityparameterissetas1,the
priorityvalueis4,096.Whenthepriorityparameterissetto2,thepriorityvalueis8,192.Bydefault
thepriorityparameteris8,sothedefaultpriorityvalueis32,768.
STPoverVSX|88

Figure 1 RPVST VSX pair as a root switch

In the following figure, the VSX pair is not a root switch for STP topology. One of the VSX LAG ports is in
the blocking state for resolving an L2 network loop. The VSX LAG port is in a blocking state on both VSX
peer switches.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

89

Figure2 RPVSTVSXpairasanonrootswitch
Configuring a VSX switch as root for one or more RPVST instances
Procedure
1. ForasingleRPVSTinstance,enterforexample:
| switch(config)# | spanning-tree | vlan 1 priority | 1   |
| --------------- | ------------- | --------------- | --- |
2. FormultipleRPVSTinstances,enterarangeforexample:
| switch(config)# | spanning-tree | vlan 1-100    | priority 1 |
| --------------- | ------------- | ------------- | ---------- |
| switch(config)# | spanning-tree | vlan 10,20,30 | priority 1 |
More information
VSXswitchwithRPVST,asrootandnonroot
| Show commands | for RPVST |     |     |
| ------------- | --------- | --- | --- |
Beforerunningtheshowcommands,makesurethatyouhaveenabledSTPsynchronizationbetweenVSXpeer
switches.SeeEnablingVSXsynchronizationofSTPconfigurationsbetweenVSXpeerswitches.
STPoverVSX|90

Task

Action

View information on
the RPVST instance of
the specified VLAN.

View information on
the RPVST instance of
the specified VLAN and
displays details on the
RPVST instance for the
VLAN.

View information on
the RPVST instance of
the specified VLAN on
the peer VSX switch.

View information on
the RPVST instance of
the specified VLAN and
displays details on the
RPVST instance for the
VLAN on the peer VSX
switch.

Verify that the
following global
parameters are the
same on VSX switches:

n STP mode

n RPVST instance

creation

n RPVST instance

priority
configuration

View a summary of the
port roles or root
information.

switch# show spanning-tree vlan <VLAN-ID>

switch# show spanning-tree vlan <VLAN-ID> detail

The output of this command shows the value of the Multi-Chassis role. When a
switch has the Multi-Chassis role set to active, the switch performs the STP
operation. When a switch has the Multi-Chassis role set to standby, the switch relays
the information to the switch with the active role for STP tasks.
For an example of the output from this command, see How the Multi-Chassis role
works.

switch# spanning-tree vlan <VLAN-ID> vsx-peer

switch# show spanning-tree vlan <VLAN-ID> detail vsx-peer

1. Enter the show running-config spanning-tree command.

2. Enter the show running-config spanning-tree vsx-peer command.

switch# show spanning-tree summary {port | root}

How the Multi-Chassis role works

The switch performs the STP operation on the switch that has the Multi-Chassis role set to active. The
switch with the role set to standby relays the information to the switch with the active role for STP tasks.

The primary VSX switch has the Multi-Chassis role set to active by default, just as the secondary VSX
switch has the Multi-Chassis role set to standby by default. The Multi-Chassis role on the secondary
VSX switch changes from standby to active if the primary VSX switch goes down.

The show spanning-tree vlan <VLAN-ID> detail command provides information about the value of
the Multi-Chassis role. In the following example, the primary switch has the Multi-Chassis role set to
active, and the secondary switch has the Multi-Chassis role set to standby.

Example of the Multi-Chassis role with the active value:

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

91

| VSX-Primary# |     | show spanning-tree |     |     | vlan | 2 detail |     |     |     |
| ------------ | --- | ------------------ | --- | --- | ---- | -------- | --- | --- | --- |
VLAN2
| Spanning | tree | status       | : Enabled |                   | Protocol:   | RPVST      |             |          |      |
| -------- | ---- | ------------ | --------- | ----------------- | ----------- | ---------- | ----------- | -------- | ---- |
| Root     | ID   | Priority     |           | : 32768           |             |            |             |          |      |
|          |      | MAC-Address: |           | 38:21:c7:66:24:00 |             |            |             |          |      |
|          |      | This bridge  |           | is the            | root        |            |             |          |      |
|          |      | Hello        | time(in   | seconds):2        |             | Max Age(in | seconds):20 |          |      |
|          |      | Forward      | Delay(in  |                   | seconds):15 |            |             |          |      |
| Bridge   | ID   | Priority     | :         | 32768             |             |            |             |          |      |
|          |      | MAC-Address: |           | 38:21:c7:66:24:00 |             |            |             |          |      |
|          |      | Hello        | time(in   | seconds):2        |             | Max Age(in | seconds):20 |          |      |
|          |      | Forward      | Delay(in  |                   | seconds):15 |            |             |          |      |
| Port     |      | Role         |           | State             |             | Cost       |             | Priority | Type |
------------ -------------- ------------ ------------ ---------- ----------
| 1/3/1         |             | Designated |          | Forwarding |              | 1     |     | 128 | point_to_point |
| ------------- | ----------- | ---------- | -------- | ---------- | ------------ | ----- | --- | --- | -------------- |
| lag2          |             | Designated |          | Forwarding |              | 20000 |     | 64  | point_to_point |
| Topology      | change      | flag       |          |            | : True       |       |     |     |                |
| Number        | of topology |            | changes  |            | : 3          |       |     |     |                |
| Last topology |             | change     | occurred |            | : 47 seconds | ago   |     |     |                |
Port 1/3/1
Designated root has priority :32768 Address: 38:21:c7:66:24:00
Designated bridge has priority :32768 Address: 38:21:c7:66:24:00
| Designated | port           |          |     |            |     | : 1153    |     |     |     |
| ---------- | -------------- | -------- | --- | ---------- | --- | --------- | --- | --- | --- |
| Number     | of transitions |          | to  | forwarding |     | state : 1 |     |     |     |
| Bpdus sent | 28,            | received |     | 28         |     |           |     |     |     |
| TCN_Tx:    | 2, TCN_Rx:     |          | 0   |            |     |           |     |     |     |
Port lag2
Designated root has priority :32768 Address: 38:21:c7:66:24:00
Designated bridge has priority :32768 Address: 38:21:c7:66:24:00
| Designated    | port           |          |     |            |     | : 770     |     |     |     |
| ------------- | -------------- | -------- | --- | ---------- | --- | --------- | --- | --- | --- |
| Multi-Chassis |                | role     |     |            |     | :active   |     |     |     |
| Number        | of transitions |          | to  | forwarding |     | state : 1 |     |     |     |
| Bpdus sent    | 28,            | received |     | 3          |     |           |     |     |     |
| TCN_Tx:       | 2, TCN_Rx:     |          | 2   |            |     |           |     |     |     |
VSX-Secondary#
|     |     | show | spanning-tree |     | vlan | 2 detail |     |     |     |
| --- | --- | ---- | ------------- | --- | ---- | -------- | --- | --- | --- |
VLAN2
| Spanning | tree | status       | : Enabled |                   | Protocol:   | RPVST      |             |          |      |
| -------- | ---- | ------------ | --------- | ----------------- | ----------- | ---------- | ----------- | -------- | ---- |
| Root     | ID   | Priority     |           | : 32768           |             |            |             |          |      |
|          |      | MAC-Address: |           | 38:21:c7:66:24:00 |             |            |             |          |      |
|          |      | This bridge  |           | is the            | root        |            |             |          |      |
|          |      | Hello        | time(in   | seconds):2        |             | Max Age(in | seconds):20 |          |      |
|          |      | Forward      | Delay(in  |                   | seconds):15 |            |             |          |      |
| Bridge   | ID   | Priority     | :         | 32768             |             |            |             |          |      |
|          |      | MAC-Address: |           | 38:21:c7:66:24:00 |             |            |             |          |      |
|          |      | Hello        | time(in   | seconds):2        |             | Max Age(in | seconds):20 |          |      |
|          |      | Forward      | Delay(in  |                   | seconds):15 |            |             |          |      |
| Port     |      | Role         |           | State             |             | Cost       |             | Priority | Type |
------------ -------------- ------------ ------------ ---------- ----------
| 1/3/1    |        | Designated |     | Forwarding |         | 1     |     | 128 | point_to_point |
| -------- | ------ | ---------- | --- | ---------- | ------- | ----- | --- | --- | -------------- |
| lag2     |        | Designated |     | Forwarding |         | 20000 |     | 64  | point_to_point |
| Topology | change | flag       |     |            | : False |       |     |     |                |
STPoverVSX|92

| Number        | of topology | changes  | : 2          |     |
| ------------- | ----------- | -------- | ------------ | --- |
| Last topology | change      | occurred | : 35 seconds | ago |
Port 1/3/1
Designated root has priority :32768 Address: 38:21:c7:66:24:00
Designated bridge has priority :32768 Address: 38:21:c7:66:24:00
| Designated | port           |               |       | : 129 |
| ---------- | -------------- | ------------- | ----- | ----- |
| Number     | of transitions | to forwarding | state | : 2   |
| Bpdus sent | 24, received   | 22            |       |       |
| TCN_Tx:    | 1, TCN_Rx:     | 2             |       |       |
Port lag2
Designated root has priority :-32768 Address: 38:21:c7:66:24:00
Designated bridge has priority :-32768 Address: 38:21:c7:66:24:00
| Designated    | port           |               |       | :770     |
| ------------- | -------------- | ------------- | ----- | -------- |
| Multi-Chassis | role           |               |       | :standby |
| Number        | of transitions | to forwarding | state | : 3      |
| Bpdus sent    | 0, received    | 0             |       |          |
| TCN_Tx:       | 0, TCN_Rx:     | 0             |       |          |
| RPVST with    | VSX guidelines |               |       |          |
n PathcostisnotallowedtobeconfiguredontheISLport.
n Donotconfigureport-specificspanningtreeconfigurationsontheISL.
n DonothaveredundantlinkstotheISL.
n TopologychangesforVSXLAGsareaccountedontheactivemultichassisLAGroleonly.
n RPVSTissupportedinbothVSXandnon-VSXenvironments.
n ThecommonbridgeIDcontinuestobeusedevenaftertheVSXsplitbrainscenarioisidentified.
n STPconfigurationsonVSXLAGportsmustbethesameonVSXswitches.
n TofindthemaximumsupportedRPVSTinstancesthatcanbeconfigured,enterthefollowing
| command:show | capacities | rpvst |     |     |
| ------------ | ---------- | ----- | --- | --- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 93

Chapter 9
|              |                |     |     |      | Loop protect |     | configurations |     |     | over VSX |
| ------------ | -------------- | --- | --- | ---- | ------------ | --- | -------------- | --- | --- | -------- |
| Loop protect | configurations |     |     | over | VSX          |     |                |     |     |          |
LoopprotectcanbeenabledonVSX.Loopprotectisaswitchfeature,whichisusedtoidentifyand
preventlayer2loopsinanetwork.Theloopprotectfeatureblockstheportbasedontheconfigured
action,theseactionsmaybe:
n Tx-Disable
Tx-Rx-Disable
n
n Do-Not-Disable
SeetheLayer2BridgingGuideforinformationaboutloopprotect.TosetuploopprotectwithVSX,loop
protectmustbeenabledontheinterfacesontheprimaryandsecondaryVSXswitches.
| How loop | protect |     | works |     | over VSX |     |     |     |     |     |
| -------- | ------- | --- | ----- | --- | -------- | --- | --- | --- | --- | --- |
Assumethatyouhavetheloopprotectfeatureenabledonlag1/1/1ontheprimaryVSXswitchandloop
protectenabledonlag1/1/2onthesecondaryVSXswitch.Whenaloopoccurs,loopprotectnotifiesthe
secondaryVSXswitchthataloopisonthenetworkandinterface1/1/2wasblocked.Whenyouenter
show interface 1/1/2onthesecondaryswitch,theoutputfromthecommandindicatesthatthe
interfacewasblockedbyVSXwheninfacttheloopprotectfeatureblockedtheinterfacetostopthe
loop.
Ifyouentershow lacp interfacesonthedownstreamswitch,theforwardingstateoftheblocked
interfacesisdisplayedasdown,asshowninthefollowingexample:
| switch(config)#   |               | show    | lacp           | interfaces |                |          |     |            |     |     |
| ----------------- | ------------- | ------- | -------------- | ---------- | -------------- | -------- | --- | ---------- | --- | --- |
| State             | abbreviations |         | :              |            |                |          |     |            |     |     |
| A - Active        |               | P       | - Passive      |            | F - Aggregable |          | I - | Individual |     |     |
| S - Short-timeout |               | L       | - Long-timeout |            | N - InSync     |          | O - | OutofSync  |     |     |
| C - Collecting    |               | D       | - Distributing |            |                |          |     |            |     |     |
| X - State         | m/c           | expired |                |            | E - Default    | neighbor |     | state      |     |     |
| Actor             | details       | of all  | interfaces:    |            |                |          |     |            |     |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port |     | Port | State System-ID |     |     | System Aggr | Forwarding |     |
| ---- | ---- | ---- | --- | ---- | --------------- | --- | --- | ----------- | ---------- | --- |
|      | Name | Id   |     | Pri  |                 |     |     | Pri Key     | State      |     |
------------------------------------------------------------------------------
| 1/3/1 | lag1 | 130 |     | 1   | ALFNCD f8:60:f0:06:87:00 |     |     | 65534 1 | up         |     |
| ----- | ---- | --- | --- | --- | ------------------------ | --- | --- | ------- | ---------- | --- |
| 1/3/2 | lag1 | 131 |     | 1   | ALFNCD f8:60:f0:06:87:00 |     |     | 65534 1 | up         |     |
| 1/7/3 | lag2 | 388 |     | 1   | ALFOE f8:60:f0:06:87:00  |     |     | 65534 2 | lacp-block |     |
1/10/46 lag2 623 1 ALFOE f8:60:f0:06:87:00 65534 2 lacp-block
| Partner | details | of all | interfaces: |     |     |     |     |     |     |     |
| ------- | ------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
------------------------------------------------------------------------------
| Intf | Aggr | Port |     | Port | State System-ID |     |     | System Aggr |     |     |
| ---- | ---- | ---- | --- | ---- | --------------- | --- | --- | ----------- | --- | --- |
|      | Name | Id   |     | Pri  |                 |     |     | Pri Key     |     |     |
------------------------------------------------------------------------------
| 1/3/1 | lag1 | 206 |     | 1   | ALFNCD f8:60:f0:06:49:00 |     |     | 65534 1 |     |     |
| ----- | ---- | --- | --- | --- | ------------------------ | --- | --- | ------- | --- | --- |
94
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide

| 1/3/2   | lag1 |     | 1130 1  | ALFNCD | f8:60:f0:06:49:00 |     | 65534 1 |     |
| ------- | ---- | --- | ------- | ------ | ----------------- | --- | ------- | --- |
| 1/7/3   | lag2 |     | 0 65534 | PLFOEX | 00:00:00:00:00:00 |     | 65534 0 |     |
| 1/10/46 | lag2 |     | 0 65534 | PLFOEX | 00:00:00:00:00:00 |     | 65534 0 |     |
Interfacelag2,whichwasshownaslacp-blockedinthepreviousexampleisshownasdownonthe
primaryVSXswitch,asshowninthefollowingexample:
| switch(config)#   |               | show           | loop-protect    |            |                     |          |            |     |
| ----------------- | ------------- | -------------- | --------------- | ---------- | ------------------- | -------- | ---------- | --- |
| Status            | and Counters  |                | - Loop          | Protection | Information         |          |            |     |
| Transmit          | Interval      |                |                 | :          | 5 (sec)             |          |            |     |
| Port              | Re-enable     | Timer          |                 | :          | Disabled            |          |            |     |
| Interface         | lag1          |                |                 |            |                     |          |            |     |
| Loop-protect      |               | enabled        |                 | :          | Yes                 |          |            |     |
| Loop-Protect      |               | enabled        | VLANs           | :          | 1-100               |          |            |     |
| Action            | on            | loop detection |                 | :          | TX disable          |          |            |     |
| Loop              | detected      | count          |                 | :          | 1                   |          |            |     |
| Loop              | detected      |                |                 | :          | Yes                 |          |            |     |
| Detected          |               | on VLAN        |                 | :          | 10                  |          |            |     |
| Detected          |               | at             |                 | :          | 2019-09-27T00:12:55 |          |            |     |
| Interface         |               | status         |                 | :          | up                  |          |            |     |
| Interface         | lag2          |                |                 |            |                     |          |            |     |
| Loop-protect      |               | enabled        |                 | :          | Yes                 |          |            |     |
| Loop-Protect      |               | enabled        | VLANs           | :          | 2021-2121           |          |            |     |
| Action            | on            | loop detection |                 | :          | TX disable          |          |            |     |
| Loop              | detected      | count          |                 | :          | 1                   |          |            |     |
| Loop              | detected      |                |                 | :          | Yes                 |          |            |     |
| Detected          |               | on VLAN        |                 | :          | 2103                |          |            |     |
| Detected          |               | at             |                 | :          | 2019-09-27T00:13:14 |          |            |     |
| Interface         |               | status         |                 | :          | down                |          |            |     |
| switch(config)#   |               | show           | lacp interfaces |            |                     |          |            |     |
| State             | abbreviations |                | :               |            |                     |          |            |     |
| A - Active        |               | P              | - Passive       |            | F - Aggregable      | I -      | Individual |     |
| S - Short-timeout |               | L              | - Long-timeout  |            | N - InSync          | O -      | OutofSync  |     |
| C - Collecting    |               | D              | - Distributing  |            |                     |          |            |     |
| X - State         | m/c           | expired        |                 |            | E - Default         | neighbor | state      |     |
| Actor             | details       | of all         | interfaces:     |            |                     |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr |     | Port Port | State | System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --- | --------- | ----- | --------- | --- | ----------- | ---------- |
|      | Name |     | Id Pri    |       |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/4/14  | lag1(mc) |     | 206 1           | ALFNCD | f8:60:f0:06:49:00 |     | 65534 1 | up   |
| ------- | -------- | --- | --------------- | ------ | ----------------- | --- | ------- | ---- |
| 1/5/15  | lag2(mc) |     |                 |        |                   |     |         | down |
| Partner | details  | of  | all interfaces: |        |                   |     |         |      |
------------------------------------------------------------------------------
| Intf | Aggr |     | Port Port | State | System-ID |     | System Aggr |     |
| ---- | ---- | --- | --------- | ----- | --------- | --- | ----------- | --- |
|      | Name |     | Id Pri    |       |           |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/4/14 | lag1(mc)      |     | 130 1 | ALFNCD | f8:60:f0:06:87:00 |     | 65534 1 |     |
| ------ | ------------- | --- | ----- | ------ | ----------------- | --- | ------- | --- |
| 1/5/15 | lag2(mc)      |     |       |        |                   |     |         |     |
| State  | abbreviations |     | :     |        |                   |     |         |     |
LoopprotectconfigurationsoverVSX|95

| A - Active        | P - Passive      | F - Aggregable | I - | Individual |     |
| ----------------- | ---------------- | -------------- | --- | ---------- | --- |
| S - Short-timeout | L - Long-timeout | N - InSync     | O - | OutofSync  |     |
C - Collecting D - Distributing
| X - State     | m/c expired        | E - Default | neighbor | state |     |
| ------------- | ------------------ | ----------- | -------- | ----- | --- |
| Actor details | of all interfaces: |             |          |       |     |
------------------------------------------------------------------------------
| Intf | Aggr Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | -------------- | --------------- | --- | ----------- | ---------- |
|      | Name Id Pri    |                 |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/4/14  | lag1(mc) 206 1             | ALFNCD f8:60:f0:06:49:00 |     | 65534 1 | up   |
| ------- | -------------------------- | ------------------------ | --- | ------- | ---- |
| 1/5/15  | lag2(mc)                   |                          |     |         | down |
| Partner | details of all interfaces: |                          |     |         |      |
------------------------------------------------------------------------------
| Intf | Aggr Port Port | State System-ID |     | System Aggr |     |
| ---- | -------------- | --------------- | --- | ----------- | --- |
|      | Name Id Pri    |                 |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/4/14 | lag1(mc) 130 1 | ALFNCD f8:60:f0:06:87:00 |     | 65534 1 |     |
| ------ | -------------- | ------------------------ | --- | ------- | --- |
| 1/5/15 | lag2(mc)       |                          |     |         |     |
State abbreviations :
| A - Active        | P - Passive      | F - Aggregable | I - | Individual |     |
| ----------------- | ---------------- | -------------- | --- | ---------- | --- |
| S - Short-timeout | L - Long-timeout | N - InSync     | O - | OutofSync  |     |
C - Collecting D - Distributing
| X - State     | m/c expired        | E - Default | neighbor | state |     |
| ------------- | ------------------ | ----------- | -------- | ----- | --- |
| Actor details | of all interfaces: |             |          |       |     |
------------------------------------------------------------------------------
| Intf | Aggr Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | -------------- | --------------- | --- | ----------- | ---------- |
|      | Name Id Pri    |                 |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/4/14  | lag1(mc) 206 1             | ALFNCD f8:60:f0:06:49:00 |     | 65534 1 | up   |
| ------- | -------------------------- | ------------------------ | --- | ------- | ---- |
| 1/5/15  | lag2(mc)                   |                          |     |         | down |
| Partner | details of all interfaces: |                          |     |         |      |
------------------------------------------------------------------------------
| Intf | Aggr Port Port | State System-ID |     | System Aggr |     |
| ---- | -------------- | --------------- | --- | ----------- | --- |
|      | Name Id Pri    |                 |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/4/14 | lag1(mc) 130 1 | ALFNCD f8:60:f0:06:87:00 |     | 65534 1 |     |
| ------ | -------------- | ------------------------ | --- | ------- | --- |
| 1/5/15 | lag2(mc)       |                          |     |         |     |
State abbreviations :
| A - Active        | P - Passive      | F - Aggregable | I - | Individual |     |
| ----------------- | ---------------- | -------------- | --- | ---------- | --- |
| S - Short-timeout | L - Long-timeout | N - InSync     | O - | OutofSync  |     |
C - Collecting D - Distributing
| X - State     | m/c expired        | E - Default | neighbor | state |     |
| ------------- | ------------------ | ----------- | -------- | ----- | --- |
| Actor details | of all interfaces: |             |          |       |     |
------------------------------------------------------------------------------
| Intf | Aggr Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | -------------- | --------------- | --- | ----------- | ---------- |
|      | Name Id Pri    |                 |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/4/14 | lag1(mc) 206 1 | ALFNCD f8:60:f0:06:49:00 |     | 65534 1 | up   |
| ------ | -------------- | ------------------------ | --- | ------- | ---- |
| 1/5/15 | lag2(mc)       |                          |     |         | down |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 96

| Partner | details | of  | all interfaces: |     |     |     |     |
| ------- | ------- | --- | --------------- | --- | --- | --- | --- |
------------------------------------------------------------------------------
| Intf | Aggr |     | Port Port | State | System-ID |     | System Aggr |
| ---- | ---- | --- | --------- | ----- | --------- | --- | ----------- |
|      | Name |     | Id Pri    |       |           |     | Pri Key     |
------------------------------------------------------------------------------
| 1/4/14 | lag1(mc) |     | 130 1 | ALFNCD | f8:60:f0:06:87:00 |     | 65534 1 |
| ------ | -------- | --- | ----- | ------ | ----------------- | --- | ------- |
| 1/5/15 | lag2(mc) |     |       |        |                   |     |         |
Interfacelag2isalsoshownasdownonthesecondaryVSXswitch,asshowninthefollowingexample:
| switch(config)# |              | show           | loop-protect |            |             |     |     |
| --------------- | ------------ | -------------- | ------------ | ---------- | ----------- | --- | --- |
| Status          | and Counters |                | - Loop       | Protection | Information |     |     |
| Transmit        | Interval     |                |              | :          | 5 (sec)     |     |     |
| Port            | Re-enable    | Timer          |              | :          | 15 (sec)    |     |     |
| Interface       | lag1         |                |              |            |             |     |     |
| Loop-protect    |              | enabled        |              | :          | Yes         |     |     |
| Loop-Protect    |              | enabled        | VLANs        | :          | 1-100       |     |     |
| Action          | on           | loop detection |              | :          | TX disable  |     |     |
| Loop            | detected     | count          |              | :          | 0           |     |     |
| Loop            | detected     |                |              | :          | No          |     |     |
| Interface       |              | status         |              | :          | up          |     |     |
| Interface       | lag2         |                |              |            |             |     |     |
| Loop-protect    |              | enabled        |              | :          | Yes         |     |     |
| Loop-Protect    |              | enabled        | VLANs        | :          | 2021-2121   |     |     |
| Action          | on           | loop detection |              | :          | TX disable  |     |     |
| Loop            | detected     | count          |              | :          | 0           |     |     |
| Loop            | detected     |                |              | :          | No          |     |     |
| Interface       |              | status         |              | :          | down        |     |     |
switch(config)#
| Status            | and Counters  |                | - Loop          | Protection | Information    |     |            |
| ----------------- | ------------- | -------------- | --------------- | ---------- | -------------- | --- | ---------- |
| Transmit          | Interval      |                |                 | :          | 5 (sec)        |     |            |
| Port              | Re-enable     | Timer          |                 | :          | 15 (sec)       |     |            |
| Interface         | lag1          |                |                 |            |                |     |            |
| Loop-protect      |               | enabled        |                 | :          | Yes            |     |            |
| Loop-Protect      |               | enabled        | VLANs           | :          | 1-100          |     |            |
| Action            | on            | loop detection |                 | :          | TX disable     |     |            |
| Loop              | detected      | count          |                 | :          | 0              |     |            |
| Loop              | detected      |                |                 | :          | No             |     |            |
| Interface         |               | status         |                 | :          | up             |     |            |
| Interface         | lag2          |                |                 |            |                |     |            |
| Loop-protect      |               | enabled        |                 | :          | Yes            |     |            |
| Loop-Protect      |               | enabled        | VLANs           | :          | 2021-2121      |     |            |
| Action            | on            | loop detection |                 | :          | TX disable     |     |            |
| Loop              | detected      | count          |                 | :          | 0              |     |            |
| Loop              | detected      |                |                 | :          | No             |     |            |
| Interface         |               | status         |                 | :          | down           |     |            |
| switch(config)#   |               | show           | lacp interfaces |            |                |     |            |
| State             | abbreviations |                | :               |            |                |     |            |
| A - Active        |               | P              | - Passive       |            | F - Aggregable | I - | Individual |
| S - Short-timeout |               | L              | - Long-timeout  |            | N - InSync     | O - | OutofSync  |
LoopprotectconfigurationsoverVSX|97

| C - Collecting |             | D - Distributing |             |          |       |     |
| -------------- | ----------- | ---------------- | ----------- | -------- | ----- | --- |
| X - State      | m/c expired |                  | E - Default | neighbor | state |     |
| Actor          | details of  | all interfaces:  |             |          |       |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --------- | --------------- | --- | ----------- | ---------- |
|      | Name | Id Pri    |                 |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/3/2   | lag1(mc) | 1130 1             | ALFNCD f8:60:f0:06:49:00 |     | 65534 1 | up   |
| ------- | -------- | ------------------ | ------------------------ | --- | ------- | ---- |
| 1/9/3   | lag2(mc) |                    |                          |     |         | down |
| Partner | details  | of all interfaces: |                          |     |         |      |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-ID |     | System Aggr |     |
| ---- | ---- | --------- | --------------- | --- | ----------- | --- |
|      | Name | Id Pri    |                 |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/3/2   | lag1(mc) | 131 1   | ALFNCD f8:60:f0:06:87:00 |     | 65534 1 |     |
| ------- | -------- | ------- | ------------------------ | --- | ------- | --- |
| 1/9/3   | lag2(mc) |         |                          |     |         |     |
| Setting | up loop  | protect | over VSX                 |     |         |     |
TosetuploopprotectoverVSX:
1. CreatetheVSXLAG.
2. EnableloopprotectontheprimaryandsecondaryVSXswitches.SeetheLayer2BridgingGuidefor
informationabouthowtoenableloopprotectonaswitch.
| An example | configuration |     | of loop | protect | over | VSX |
| ---------- | ------------- | --- | ------- | ------- | ---- | --- |
Thefollowingfigureisasimplifiedconfiguration.Mostnetworkconfigurationswillhavemorethanone
downstreamswitch.
| Figure1 | ExampleofLoopProtectOverVSX |     |     |     |     |     |
| ------- | --------------------------- | --- | --- | --- | --- | --- |
Thefollowingsectionsprovideinformationabouttheconfigurationsontheswitchesbeforeandafter
configuringtheloopprotectfeature.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 98

| VSX configurations |     | before | enabling | loop | protect |     |
| ------------------ | --- | ------ | -------- | ---- | ------- | --- |
ThissectionprovidesconfigurationinformationfortheprimaryVSXswitch,secondaryVSXswitch,and
downstreamswitchbeforeloopprotectisenabled.
| VSX primary | switch         | before enabling | loop protect |     |     |     |
| ----------- | -------------- | --------------- | ------------ | --- | --- | --- |
| hostname    | Primary        |                 |              |     |     |     |
| module 1/1  | product-number | jl363a          |              |     |     |     |
cli-session
| timeout    | 0        |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- |
| ssh server | vrf mgmt |     |     |     |     |     |
vlan 1-2000
| interface | mgmt |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
no shutdown
ip dhcp
| interface | lag 1 multi-chassis |     |     |     |     |     |
| --------- | ------------------- | --- | --- | --- | --- | --- |
no shutdown
no routing
| vlan      | trunk native        | 1      |     |     |     |     |
| --------- | ------------------- | ------ | --- | --- | --- | --- |
| vlan      | trunk allowed       | 1-2000 |     |     |     |     |
| lacp      | mode active         |        |     |     |     |     |
| interface | lag 2 multi-chassis |        |     |     |     |     |
no shutdown
no routing
| vlan      | trunk native  | 1      |     |     |     |     |
| --------- | ------------- | ------ | --- | --- | --- | --- |
| vlan      | trunk allowed | 1-2000 |     |     |     |     |
| lacp      | mode active   |        |     |     |     |     |
| interface | 1/1/1         |        |     |     |     |     |
no shutdown
| lag       | 1     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
| interface | 1/1/2 |     |     |     |     |     |
no shutdown
| lag       | 2     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
| interface | 1/1/3 |     |     |     |     |     |
no shutdown
no routing
| vlan      | trunk native  | 1 tag |     |     |     |     |
| --------- | ------------- | ----- | --- | --- | --- | --- |
| vlan      | trunk allowed | all   |     |     |     |     |
| interface | 1/1/30        |       |     |     |     |     |
no shutdown
| ip address | 10.1.1.1/24 |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- |
vsx
| inter-switch-link |                   | 1/1/3            |                |     |                |     |
| ----------------- | ----------------- | ---------------- | -------------- | --- | -------------- | --- |
| role              | primary           |                  |                |     |                |     |
| keepalive         | peer              | 10.1.1.2 source  | 10.1.1.1       |     |                |     |
| LACP interface    | configuration     |                  |                |     |                |     |
| Primary#          | show lacp         | interfaces       |                |     |                |     |
| State             | abbreviations     | :                |                |     |                |     |
| A -               | Active            | P - Passive      | F - Aggregable |     | I - Individual |     |
| S -               | Short-timeout     | L - Long-timeout | N - InSync     |     | O - OutofSync  |     |
| C -               | Collecting        | D - Distributing |                |     |                |     |
| X -               | State m/c expired |                  | E - Default    |     | neighbor state |     |
| Actor             | details of        | all interfaces:  |                |     |                |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --------- | --------------- | --- | ----------- | ---------- |
|      | Name | Id Pri    |                 |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/1 | lag1(mc) | 1 1 | ALFNCD 04:09:73:62:c8:00 |     | 65534 1 | up  |
| ----- | -------- | --- | ------------------------ | --- | ------- | --- |
LoopprotectconfigurationsoverVSX|99

| 1/1/2   | lag2(mc) | 2      | 1 ALFNCD    | 04:09:73:62:c8:00 |     | 65534 2 | up  |
| ------- | -------- | ------ | ----------- | ----------------- | --- | ------- | --- |
| Partner | details  | of all | interfaces: |                   |     |         |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port State | System-ID |     | System Aggr |     |
| ---- | ---- | ---- | ---------- | --------- | --- | ----------- | --- |
|      | Name | Id   | Pri        |           |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/1/1 | lag1(mc)          | 18               | 1 ALFNCD | e0:07:1b:cb:e1:5a |          | 65534 1    |     |
| ----- | ----------------- | ---------------- | -------- | ----------------- | -------- | ---------- | --- |
| 1/1/2 | lag2(mc)          | 20               | 1 ALFNCD | e0:07:1b:cb:e1:5a |          | 65534 2    |     |
| State | abbreviations     | :                |          |                   |          |            |     |
| A -   | Active            | P - Passive      |          | F - Aggregable    | I -      | Individual |     |
| S -   | Short-timeout     | L - Long-timeout |          | N - InSync        | O -      | OutofSync  |     |
| C -   | Collecting        | D - Distributing |          |                   |          |            |     |
| X -   | State m/c expired |                  |          | E - Default       | neighbor | state      |     |
| Actor | details of        | all interfaces:  |          |                   |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port State | System-ID |     | System Aggr | Forwarding |
| ---- | ---- | ---- | ---------- | --------- | --- | ----------- | ---------- |
|      | Name | Id   | Pri        |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/1   | lag1(mc) | 1      | 1 ALFNCD    | 04:09:73:62:c8:00 |     | 65534 1 | up  |
| ------- | -------- | ------ | ----------- | ----------------- | --- | ------- | --- |
| 1/1/2   | lag2(mc) | 2      | 1 ALFNCD    | 04:09:73:62:c8:00 |     | 65534 2 | up  |
| Partner | details  | of all | interfaces: |                   |     |         |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port State | System-ID |     | System Aggr |     |
| ---- | ---- | ---- | ---------- | --------- | --- | ----------- | --- |
|      | Name | Id   | Pri        |           |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/1/1 | lag1(mc) | 18  | 1 ALFNCD | e0:07:1b:cb:e1:5a |     | 65534 1 |     |
| ----- | -------- | --- | -------- | ----------------- | --- | ------- | --- |
| 1/1/2 | lag2(mc) | 20  | 1 ALFNCD | e0:07:1b:cb:e1:5a |     | 65534 2 |     |
VSX configuration
| Primary#      | show vsx         | brief  |                |                         |     |     |     |
| ------------- | ---------------- | ------ | -------------- | ----------------------- | --- | --- | --- |
| ISL           | State            |        |                | : In-Sync               |     |     |     |
| Device        | State            |        |                | : Peer-Established      |     |     |     |
| Keepalive     | State            |        |                | : Keepalive-Established |     |     |     |
| Device        | Role             |        |                | : primary               |     |     |     |
| Number        | of Multi-chassis |        | LAG interfaces | : 2                     |     |     |     |
| VSX secondary | switch           | before | enabling       | loop protect            |     |     |     |
| hostname      | Secondary        |        |                |                         |     |     |     |
| module 1/1    | product-number   | jl363a |                |                         |     |     |     |
cli-session
| timeout    | 0        |     |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- | --- |
| ssh server | vrf mgmt |     |     |     |     |     |     |
vlan 1-2000
| interface | mgmt |     |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- |
no shutdown
ip dhcp
| interface | lag 1 multi-chassis |     |     |     |     |     |     |
| --------- | ------------------- | --- | --- | --- | --- | --- | --- |
no shutdown
no routing
| vlan      | trunk native        | 1      |     |     |     |     |     |
| --------- | ------------------- | ------ | --- | --- | --- | --- | --- |
| vlan      | trunk allowed       | 1-2000 |     |     |     |     |     |
| lacp      | mode active         |        |     |     |     |     |     |
| interface | lag 2 multi-chassis |        |     |     |     |     |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 100

no shutdown
no routing
| vlan | trunk native  | 1      |     |     |     |     |
| ---- | ------------- | ------ | --- | --- | --- | --- |
| vlan | trunk allowed | 1-2000 |     |     |     |     |
| lacp | mode active   |        |     |     |     |     |
interface 1/1/1
no shutdown
lag 1
interface 1/1/2
no shutdown
lag 2
interface 1/1/3
no shutdown
no routing
| vlan | trunk native  | 1 tag |     |     |     |     |
| ---- | ------------- | ----- | --- | --- | --- | --- |
| vlan | trunk allowed | all   |     |     |     |     |
interface 1/1/30
no shutdown
| ip  | address 10.1.1.2/24 |     |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- | --- |
vsx
| inter-switch-link |     | 1/1/3 |     |     |     |     |
| ----------------- | --- | ----- | --- | --- | --- | --- |
role secondary
| keepalive      | peer              | 10.1.1.1 source  | 10.1.1.2       |          |            |     |
| -------------- | ----------------- | ---------------- | -------------- | -------- | ---------- | --- |
| LACP interface | configuration     |                  |                |          |            |     |
| Secondary#     | show              | lacp interfaces  |                |          |            |     |
| State          | abbreviations     | :                |                |          |            |     |
| A -            | Active            | P - Passive      | F - Aggregable | I -      | Individual |     |
| S -            | Short-timeout     | L - Long-timeout | N - InSync     | O -      | OutofSync  |     |
| C -            | Collecting        | D - Distributing |                |          |            |     |
| X -            | State m/c expired |                  | E - Default    | neighbor | state      |     |
| Actor          | details of        | all interfaces:  |                |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --------- | --------------- | --- | ----------- | ---------- |
|      | Name | Id Pri    |                 |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/1   | lag1(mc) | 1001 1             | ALFNCD 04:09:73:62:c8:00 |     | 65534 1 | up  |
| ------- | -------- | ------------------ | ------------------------ | --- | ------- | --- |
| 1/1/2   | lag2(mc) | 1002 1             | ALFNCD 04:09:73:62:c8:00 |     | 65534 2 | up  |
| Partner | details  | of all interfaces: |                          |     |         |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-ID |     | System Aggr |     |
| ---- | ---- | --------- | --------------- | --- | ----------- | --- |
|      | Name | Id Pri    |                 |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/1/1 | lag1(mc)          | 19 1             | ALFNCD e0:07:1b:cb:e1:5a |          | 65534 1    |     |
| ----- | ----------------- | ---------------- | ------------------------ | -------- | ---------- | --- |
| 1/1/2 | lag2(mc)          | 31 1             | ALFNCD e0:07:1b:cb:e1:5a |          | 65534 2    |     |
| State | abbreviations     | :                |                          |          |            |     |
| A -   | Active            | P - Passive      | F - Aggregable           | I -      | Individual |     |
| S -   | Short-timeout     | L - Long-timeout | N - InSync               | O -      | OutofSync  |     |
| C -   | Collecting        | D - Distributing |                          |          |            |     |
| X -   | State m/c expired |                  | E - Default              | neighbor | state      |     |
| Actor | details of        | all interfaces:  |                          |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --------- | --------------- | --- | ----------- | ---------- |
|      | Name | Id Pri    |                 |     | Pri Key     | State      |
------------------------------------------------------------------------------
LoopprotectconfigurationsoverVSX|101

| 1/1/1   | lag1(mc) | 1001 1             | ALFNCD 04:09:73:62:c8:00 | 65534 1 | up  |
| ------- | -------- | ------------------ | ------------------------ | ------- | --- |
| 1/1/2   | lag2(mc) | 1002 1             | ALFNCD 04:09:73:62:c8:00 | 65534 2 | up  |
| Partner | details  | of all interfaces: |                          |         |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-ID | System Aggr |     |
| ---- | ---- | --------- | --------------- | ----------- | --- |
|      | Name | Id Pri    |                 | Pri Key     |     |
------------------------------------------------------------------------------
| 1/1/1 | lag1(mc) | 19 1 | ALFNCD e0:07:1b:cb:e1:5a | 65534 1 |     |
| ----- | -------- | ---- | ------------------------ | ------- | --- |
| 1/1/2 | lag2(mc) | 31 1 | ALFNCD e0:07:1b:cb:e1:5a | 65534 2 |     |
VSX configuration
| Secondary# | show             | vsx brief       |                         |     |     |
| ---------- | ---------------- | --------------- | ----------------------- | --- | --- |
| ISL State  |                  |                 | : In-Sync               |     |     |
| Device     | State            |                 | : Peer-Established      |     |     |
| Keepalive  | State            |                 | : Keepalive-Established |     |     |
| Device     | Role             |                 | : secondary             |     |     |
| Number     | of Multi-chassis | LAG             | interfaces : 2          |     |     |
| Downstream | switch           | before enabling | loop protect            |     |     |
| hostname   | Downstream       |                 |                         |     |     |
cli-session
| timeout    | 0        |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- |
| ssh server | vrf mgmt |     |     |     |     |
vlan 1-2000
| interface | mgmt |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
no shutdown
ip dhcp
| interface | lag 1 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
no routing
| vlan      | trunk native  | 1      |     |     |     |
| --------- | ------------- | ------ | --- | --- | --- |
| vlan      | trunk allowed | 1-2000 |     |     |     |
| lacp      | mode active   |        |     |     |     |
| interface | lag 2         |        |     |     |     |
no shutdown
no routing
| vlan      | trunk native  | 1      |     |     |     |
| --------- | ------------- | ------ | --- | --- | --- |
| vlan      | trunk allowed | 1-2000 |     |     |     |
| lacp      | mode active   |        |     |     |     |
| interface | 1/1/17        |        |     |     |     |
no shutdown
| lag       | 1      |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
| interface | 1/1/18 |     |     |     |     |
no shutdown
| lag       | 1      |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
| interface | 1/1/19 |     |     |     |     |
no shutdown
| lag       | 2      |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
| interface | 1/1/30 |     |     |     |     |
no shutdown
| lag | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
ThefollowingisanexampleofanLACPinterfaceconfiguration.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 102

| Downstream# | show              | lacp interfaces  |     |            |          |            |     |
| ----------- | ----------------- | ---------------- | --- | ---------- | -------- | ---------- | --- |
| State       | abbreviations     | :                |     |            |          |            |     |
| A -         | Active            | P - Passive      | F - | Aggregable | I -      | Individual |     |
| S -         | Short-timeout     | L - Long-timeout | N - | InSync     | O -      | OutofSync  |     |
| C -         | Collecting        | D - Distributing |     |            |          |            |     |
| X -         | State m/c expired |                  | E - | Default    | neighbor | state      |     |
| Actor       | details of        | all interfaces:  |     |            |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --------- | ----- | --------- | --- | ----------- | ---------- |
|      | Name | Id Pri    |       |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/17  | lag1    | 18 1               | ALFNCD | e0:07:1b:cb:e1:5a |     | 65534 1 | up  |
| ------- | ------- | ------------------ | ------ | ----------------- | --- | ------- | --- |
| 1/1/18  | lag1    | 19 1               | ALFNCD | e0:07:1b:cb:e1:5a |     | 65534 1 | up  |
| 1/1/19  | lag2    | 20 1               | ALFNCD | e0:07:1b:cb:e1:5a |     | 65534 2 | up  |
| 1/1/30  | lag2    | 31 1               | ALFNCD | e0:07:1b:cb:e1:5a |     | 65534 2 | up  |
| Partner | details | of all interfaces: |        |                   |     |         |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID |     | System Aggr |     |
| ---- | ---- | --------- | ----- | --------- | --- | ----------- | --- |
|      | Name | Id Pri    |       |           |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/1/17             | lag1 | 1 1    | ALFNCD   | 04:09:73:62:c8:00 |         | 65534 1 |     |
| ------------------ | ---- | ------ | -------- | ----------------- | ------- | ------- | --- |
| 1/1/18             | lag1 | 1001 1 | ALFNCD   | 04:09:73:62:c8:00 |         | 65534 1 |     |
| 1/1/19             | lag2 | 2 1    | ALFNCD   | 04:09:73:62:c8:00 |         | 65534 2 |     |
| 1/1/30             | lag2 | 1002 1 | ALFNCD   | 04:09:73:62:c8:00 |         | 65534 2 |     |
| VSX configurations |      | after  | enabling | loop              | protect |         |     |
ThissectionprovidesconfigurationinformationfortheprimaryVSXswitch,secondaryVSXswitch,and
downstreamswitchafterloopprotectisenabled.
| VSX primary | switch | after enabling | loop protect |     |     |     |     |
| ----------- | ------ | -------------- | ------------ | --- | --- | --- | --- |
Thefollowingconfigurationshowsthatloopprotectisenabled.
| hostname   | Primary        |        |     |     |     |     |     |
| ---------- | -------------- | ------ | --- | --- | --- | --- | --- |
| module 1/1 | product-number | jl363a |     |     |     |     |     |
cli-session
| timeout    | 0        |     |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- | --- |
| ssh server | vrf mgmt |     |     |     |     |     |     |
vlan 1-2000
| interface | mgmt |     |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- |
no shutdown
ip dhcp
| interface | lag 1 multi-chassis |     |     |     |     |     |     |
| --------- | ------------------- | --- | --- | --- | --- | --- | --- |
no shutdown
no routing
| vlan | trunk native  | 1      |     |     |     |     |     |
| ---- | ------------- | ------ | --- | --- | --- | --- | --- |
| vlan | trunk allowed | 1-2000 |     |     |     |     |     |
| lacp | mode active   |        |     |     |     |     |     |
loop-protect
| loop-protect | vlan                | 1-2000 |     |     |     |     |     |
| ------------ | ------------------- | ------ | --- | --- | --- | --- | --- |
| interface    | lag 2 multi-chassis |        |     |     |     |     |     |
no shutdown
no routing
| vlan | trunk native  | 1      |     |     |     |     |     |
| ---- | ------------- | ------ | --- | --- | --- | --- | --- |
| vlan | trunk allowed | 1-2000 |     |     |     |     |     |
LoopprotectconfigurationsoverVSX|103

| lacp | mode active |     |     |
| ---- | ----------- | --- | --- |
loop-protect
| loop-protect | vlan 1-2000 |     |     |
| ------------ | ----------- | --- | --- |
| interface    | 1/1/1       |     |     |
no shutdown
| lag       | 1     |     |     |
| --------- | ----- | --- | --- |
| interface | 1/1/2 |     |     |
no shutdown
| lag       | 2     |     |     |
| --------- | ----- | --- | --- |
| interface | 1/1/3 |     |     |
no shutdown
no routing
| vlan      | trunk native 1 | tag |     |
| --------- | -------------- | --- | --- |
| vlan      | trunk allowed  | all |     |
| interface | 1/1/30         |     |     |
no shutdown
| ip address | 10.1.1.1/24 |     |     |
| ---------- | ----------- | --- | --- |
vsx
| inter-switch-link | 1/1/3          |          |              |
| ----------------- | -------------- | -------- | ------------ |
| role              | primary        |          |              |
| keepalive         | peer 10.1.1.2  | source   | 10.1.1.1     |
| VSX secondary     | after before   | enabling | loop protect |
| hostname          | Secondary      |          |              |
| module 1/1        | product-number | jl363a   |              |
cli-session
| timeout    | 0        |     |     |
| ---------- | -------- | --- | --- |
| ssh server | vrf mgmt |     |     |
vlan 1-2000
| interface | mgmt |     |     |
| --------- | ---- | --- | --- |
no shutdown
ip dhcp
| interface | lag 1 multi-chassis |     |     |
| --------- | ------------------- | --- | --- |
no shutdown
no routing
| vlan | trunk native 1 |        |     |
| ---- | -------------- | ------ | --- |
| vlan | trunk allowed  | 1-2000 |     |
| lacp | mode active    |        |     |
loop-protect
| loop-protect | vlan 1-2000         |     |     |
| ------------ | ------------------- | --- | --- |
| interface    | lag 2 multi-chassis |     |     |
no shutdown
no routing
| vlan | trunk native 1 |        |     |
| ---- | -------------- | ------ | --- |
| vlan | trunk allowed  | 1-2000 |     |
| lacp | mode active    |        |     |
loop-protect
| loop-protect | vlan 1-2000 |     |     |
| ------------ | ----------- | --- | --- |
| interface    | 1/1/1       |     |     |
no shutdown
| lag       | 1     |     |     |
| --------- | ----- | --- | --- |
| interface | 1/1/2 |     |     |
no shutdown
| lag       | 2     |     |     |
| --------- | ----- | --- | --- |
| interface | 1/1/3 |     |     |
no shutdown
no routing
| vlan      | trunk native 1 | tag |     |
| --------- | -------------- | --- | --- |
| vlan      | trunk allowed  | all |     |
| interface | 1/1/30         |     |     |
no shutdown
| ip address | 10.1.1.2/24 |     |     |
| ---------- | ----------- | --- | --- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 104

vsx
| inter-switch-link   |        | 1/1/3           |              |     |
| ------------------- | ------ | --------------- | ------------ | --- |
| role secondary      |        |                 |              |     |
| keepalive           | peer   | 10.1.1.1 source | 10.1.1.2     |     |
| Downstream          | switch | after enabling  | loop protect |     |
| hostname Downstream |        |                 |              |     |
cli-session
| timeout    | 0        |     |     |     |
| ---------- | -------- | --- | --- | --- |
| ssh server | vrf mgmt |     |     |     |
vlan 1-2000
| interface mgmt |     |     |     |     |
| -------------- | --- | --- | --- | --- |
no shutdown
ip dhcp
| interface lag | 1   |     |     |     |
| ------------- | --- | --- | --- | --- |
no shutdown
no routing
| vlan trunk    | native  | 1      |     |     |
| ------------- | ------- | ------ | --- | --- |
| vlan trunk    | allowed | 1-2000 |     |     |
| lacp mode     | active  |        |     |     |
| interface lag | 2       |        |     |     |
no shutdown
no routing
| vlan trunk       | native  | 1      |     |     |
| ---------------- | ------- | ------ | --- | --- |
| vlan trunk       | allowed | 1-2000 |     |     |
| lacp mode        | active  |        |     |     |
| interface 1/1/17 |         |        |     |     |
no shutdown
| lag 1            |     |     |     |     |
| ---------------- | --- | --- | --- | --- |
| interface 1/1/18 |     |     |     |     |
no shutdown
| lag 1            |     |     |     |     |
| ---------------- | --- | --- | --- | --- |
| interface 1/1/19 |     |     |     |     |
no shutdown
| lag 2            |     |     |     |     |
| ---------------- | --- | --- | --- | --- |
| interface 1/1/30 |     |     |     |     |
no shutdown
| lag 2          |     |          |         |          |
| -------------- | --- | -------- | ------- | -------- |
| Best practices |     | for loop | protect | over VSX |
n EnableloopprotectonbothprimaryandsecondaryVSXswitches.
n DonotenableloopprotectontheISLlinkfortheprimaryandsecondaryVSXswitches.
n Ifyouenableanactionforloopprotect,suchasdo-not-disable,andanotheraction,suchasTx-Rx-
Disable,isalreadyineffect,loopprotectmustbedisabledandthenre-enabled.
n Ifyouruntheloop-protect action do-not-disablecommand,oneverytransmitinterval,theloopis
detectedandthedetectionisreportedthroughanSNMPtrapandaneventlogmessage.
Youcanviewtheeventsforjusttheloopprotectfeaturebyenteringtheshow events -d hpe-lpd
command.
n ThetotalnumberofVLANsacrossportsis(portsxVLANs)=4094portsperVLAN.Loopprotectcan
beconfiguredonamaximumof4094VLANsacrossallinterfaceswithoutupdatingCoPPpoliciesfor
loopprotect.IfyournetworkconfigurationrequiresyoutoconfiguremoreVLAN,updateyourCoPP
policiesvaluesforloopprotecttoensurethatyouallocatemoreresources.Youcanassigna
maximumof10,000VLANsacrossalltheinterfaces.
LoopprotectconfigurationsoverVSX|105

Chapter 10

EVPN VSX support

EVPN VSX support

Ethernet VPN (EVPN) is supported with VSX . The two VSX pairs act as independent BGP routing entities
to the other VXLAN tunnel endpoints (VTEPs) or spines for control packets. However, in the datapath,
both of them act as a single logical VTEP. This is achieved by using different IP addresses for establishing
the BGP session and using a common IP as next-hop to represent the VTEP.

For more information on EVPN VSX support, see the EVPN VSX support chapter in the VXLAN Guide.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide

106

Chapter 11
Upstream connectivity
| Upstream | connectivity |     |     |
| -------- | ------------ | --- | --- |
Thefollowingsectiondescribesupstreamconnectivityoptionsandconfigurationsforupstreamrouting
overVSXLAGSVIlinks.
| Upstream | connectivity |     | options |
| -------- | ------------ | --- | ------- |
Thisfirmwaresupportsthefollowingupstreamconnectivityoptions:
Routed Only Port (ROP):AphysicalportonaswitchthatprocessallLayer3functionsforpacketsto
n
orfromthesaidportwithoutanybindingtoVLANprocessing.SeeSVI(multipleVRFs)inaVSX
environment.
n Switched Virtual Interface (SVIs) (multiple VRFs):AnSVIisalogicalLayer3interfaceconfigured
perVLAN(one-to-onemapping)thatperformsallLayer3processingforpacketstoorfromallswitch
portsassociatedwiththatVLAN.SeeSVI(multipleVRFs)inaVSXenvironment.
| n VSX LAG | SVIs with multiple                   | VRFs.See | VSXLAGandlayer3ECMP |
| --------- | ------------------------------------ | -------- | ------------------- |
| Figure1   | ROPwithasingleVRFintheVSXenvironment |          |                     |
107
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide

Figure 2 SVI (multiple VRFs) in a VSX environment

Upstream connectivity | 108

Figure 3 VSX LAG and layer 3 ECMP

Upstream routing over VSX LAG SVI links

This section shows two configurations for upstream routing over VSX LAG SVI links:

n ECMP

n ECMP and VSX LAG

n Active gateway as next-hop router

The ECMP and VSX LAG configuration is the preferred configuration because LAGs introduce simplicity
by reducing the number of transit VLANs and associated SVIs. This simplified configuration results in a
minimized Sender Policy Framework (SPF) calculation time. The following figure shows that Core1 and
Core2 are not in a VSX LAG, but Agg1 and Agg2 are in a VSX LAG. This figure introduces the requirement
for MSTP because all the links between the aggregate and core are bridged (trunk ports with multiple
VLANs).

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

109

Figure 1 ECMP and VSX LAG in a VSX environment

The following figure differs from the previous figure in that Core1 and Core2 are in a VSX LAG, which
provides load balancing for ECMP. The transit VLANs shown in the following figure are per VRF.

Upstream connectivity | 110

Figure 2 ECMP in a VSX environment

If ECMP is not supported or firewall does not support dynamic routing protocols, active gateway can be
used as next-hop router. The following figure shows the specific use case of active/standby firewall with
active gateway as the next-hop router.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

111

Figure 3 Active gateway as a next-hop router

Upstream connectivity | 112

Chapter 12
VSX commands
VSX commands
VSXcommandsdonotapplytothe6300seriesswitches.
active-gateway
active-gateway
| ip [<IP-ADDRESS>]     | [mac <MAC-ADDRESS>  | [extended-mac]] |
| --------------------- | ------------------- | --------------- |
| ipv6 [<IPv6-ADDRESS>] | [[mac <MAC-ADDRESS> | [extended-mac]] |
l3-src-mac
no ...
Description
ConfiguresavirtualIPandvirtualMACforaninterfaceVLAN.Theextended-macoptionstoresMAC
addressesinasupplementaltablewhichallowsconfiguringmorethan16virtualMACaddresses.
Thenoformofthiscommandremovestheactivegatewayforactive-activerouting.
Thisconfigurationwilldisableflowtrackingstatisticscollection.
| Parameter    |     | Description                               |
| ------------ | --- | ----------------------------------------- |
| ip           |     | SpecifiestheconfigurationofanIPv4address. |
| <IP-ADDRESS> |     | SpecifiestheIPv4address.Syntax:A.B.C..    |
<MAC-ADDR> SpecifiestheVirtualMACaddress.Syntax:xx:xx:xx:xx:xx:xx
extended-mac
StorestheMACaddressintheextendedMACtable.
| ipv6 |     | SpecifiestheconfigurationofanIPv6address. |
| ---- | --- | ----------------------------------------- |
<IP-ADDRESS>
SpecifiestheIPv6address.Syntax:A:B::C:D
<MAC-ADDR> SpecifiestheVirtualMACaddress.Syntax:xx:xx:xx:xx:xx:xx
| extended-mac |     | StorestheMACaddressintheextendedMACtable. |
| ------------ | --- | ----------------------------------------- |
l3-src-mac ConfiguresthevirtualgatewayMACaddressasthesourceMAC
forroutedpackets.
| no  |     | Negatesanyconfiguredparameter. |
| --- | --- | ------------------------------ |
Usage
Beforeconfiguringactivegateway,confirmthatanIPaddressisontheSVIthatisinthesamesubnetas
theactivegatewayIPyouaretryingtoconfigure.IfanactivegatewayIPdoesnothaveanSVIIPwiththe
113
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide

same subnet, the CLI allows the configuration, but the active gateway IP will not be programmed in the
kernel, resulting the active gateway to be unreachable.

It is highly recommended that you use an IPv6 link-local address as a gateway (VIP) on the active
gateway IPv6 configuration.

If VRRP or active forwarding is configured on an SVI, active gateway cannot be configured. Active
gateway with overlapping networks is not allowed. Maximum of 16 unique virtual MACs are supported
in a system.

The maximum number of supported active gateways per switch is 4,000. Since a maximum of 31
secondary IPv4 addresses can be configured on an SVI, 32 IPv4 active gateways (along with the primary
IPv4 address) can be configured per SVI with IP multinetting support. This support is also the same for
IPv6 addresses.

The extended-mac option allows you to increase the maximum number of MAC addresses supported in
the system. The following are some important points to be considered for using this option:

n The extended-mac feature has some limitations over regular active gateway MACs. Therefore, it is

recommended to use the regular active-gateway MACs first.

n Maximum of 500 unique instances, containing the specified active gateway IP and MAC address as a

pair can be configured.

n Configuration of extended-mac can only be done on VLAN interfaces.

n Extended MAC addresses cannot be one of the 16 MAC addresses in the regular active-gateway

table.

n The mac-address matches will only match on the outer destination address of an overlay network

packet, making this feature useable only in underlay environments or overlay environments where
the L3 gateways using the extended-mac feature are distributed across all VTEPs.

n The extended-mac feature is mutually exclusive with the mac-lockout feature:

o If the mac-lockout entries are configured, the extended-mac configuration will fail .

o If the extended-mac entries are configured, the mac-lockout configuration will fail.

o When both mac-lockout and extended-mac options are configured through REST API, the mac-

lockout configuration will take precedence and become the active feature. A log message will be
displayed, explaining the conflict.

o If the mac-lockout feature is configured through REST API when the extended-mac feature is

active, then the extended-mac feature will be deactivated.

If the active gateway is configured with the same IP as an SVI IP, then IPv6 DAD cannot be configured
and the SVI IP cannot be changed.

The recommended order for configuring an active gateway with the same IPv6 address same as an SVI
on both VSX Peers is:

1.

IPv6 active gateway configuration

2. SVI IPv6 address configuration

If the configuration is applied in a different order, it may result in a DAD status of DUPLICATE. To
remove the DUPLICATE status of the SVI IP address, perform a shutdown and no shutdown on the
interface.

Do not use peer system MAC address as an active-gateway VMAC. If same MAC address is used, the VSX

synchronization will try to sync the configuration on secondary switch and cause traffic disruptions.

Examples

VSX commands | 114

Configuringactive-gateway,whentheIPaddressisdifferentfromtheSVIIPaddressonbothVSXpeers
(validforIPv4andIPv6):
Switch1:
| switch1(config-if-vlan)# | ip address | 192.168.1.250/24 |     |
| ------------------------ | ---------- | ---------------- | --- |
switch1(config-if-vlan)# active-gateway ip 192.168.1.253 mac 00:00:00:00:00:01
switch1(config-if-vlan)# active-gateway ipv6 fe80::01 mac 00:00:00:01:00:01
Switch2:
| switch2(config-if-vlan)# | ip address | 192.168.1.251/24 |     |
| ------------------------ | ---------- | ---------------- | --- |
switch2(config-if-vlan)#
|     | active-gateway | ip 192.168.1.253 | mac 00:00:00:00:00:01 |
| --- | -------------- | ---------------- | --------------------- |
switch2(config-if-vlan)# active-gateway ipv6 fe80::01 mac 00:00:00:01:00:01
Configuringactive-gatewaywhentheIPaddressisthesameastheSVIIPaddressonbothVSXpeers
(validforIPv4andIPv6):
Switch1:
| switch1(config-if-vlan)# | ip address | 192.168.1.250/24 |     |
| ------------------------ | ---------- | ---------------- | --- |
switch1(config-if-vlan)# active-gateway ip 192.168.1.250 mac 00:00:00:00:00:01
switch1(config-if-vlan)# active-gateway ipv6 fe80::100 mac 00:00:00:00:00:01
| switch1(config-if-vlan)# | ipv6 address | link-local | fe80::100/64 |
| ------------------------ | ------------ | ---------- | ------------ |
Switch2:
switch2(config-if-vlan)#
|     | ip address | 192.168.1.250/24 |     |
| --- | ---------- | ---------------- | --- |
switch2(config-if-vlan)# active-gateway ip 192.168.1.250 mac 00:00:00:00:00:01
switch2(config-if-vlan)# active-gateway ipv6 fe80::100 mac 00:00:00:00:00:01
| switch2(config-if-vlan)# | ipv6 address | link-local | fe80::100/64 |
| ------------------------ | ------------ | ---------- | ------------ |
Configuringonlytheactivegatewayaddress:
| switch(config-if-vlan)# | ip address     | 192.168.1.250/24 |     |
| ----------------------- | -------------- | ---------------- | --- |
| switch(config-if-vlan)# | active-gateway | ip 192.168.1.250 |     |
ConfiguringonlytheactivegatewayIPMACaddress:
switch2(config-if-vlan)#
|     | ip address | 192.168.1.250/24 |     |
| --- | ---------- | ---------------- | --- |
switch2(config-if-vlan)# active-gateway ip mac 00:00:00:01:00:01
ConfiguringtheactivegatewaywiththeextendedMACusage(IPv4andIPv6):
switch(config-if-vlan)# active-gateway ip mac 00:00:00:00:00:01 extended-mac
Warning: This configuration will disable flow tracking statistics collection.
switch(config-if-vlan)# active-gateway ipv6 mac 00:00:00:00:00:02 extended-mac
Warning: This configuration will disable flow tracking statistics collection.
switch(config-if-vlan)# active-gateway ip 10.0.0.2 mac 00:00:00:00:00:01 extended-
mac
switch(config-if-vlan)#
|     | active-gateway | ipv6 fe80::100 | mac 00:00:00:00:00:01 |
| --- | -------------- | -------------- | --------------------- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 115

extended-macc
Removingtheactivegatewayforactive-activerouting(IPv6andIPv4):
| switch(config-if-vlan)# | no active-gateway |     | ip   |     |
| ----------------------- | ----------------- | --- | ---- | --- |
| switch(config-if-vlan)# | no active-gateway |     | ipv6 |     |
Removingtheactivegatewayforactive-activeroutingforanIPaddress:
| switch(config-if-vlan)# | no active-gateway |     | ip 192.168.1.250 |     |
| ----------------------- | ----------------- | --- | ---------------- | --- |
Removingtheactivegatewayforactive-activeroutingforvirtualMACaddresses:
switch(config-if-vlan)#
|     | no active-gateway |     | ip mac |     |
| --- | ----------------- | --- | ------ | --- |
WhenconfiguringthevirtualactivegatewayforIPv6onanSVI,itisrecommendedtousethesame
globalIPv6andactivegatewayIPv6address.Similarly,ifyouwanttousetheIPv6link-localaddressfor
thevirtualactivegatewaythenthesameaddressshouldbeconfiguredforboththeSVIandtheactive
gateway.
GlobalIPv6address:
| switch(config-if-vlan)# | ipv6 address   | 1001::1/64 |              |     |
| ----------------------- | -------------- | ---------- | ------------ | --- |
| switch(config-if-vlan)# | active-gateway |            | ipv6 1001::1 |     |
switch(config-if-vlan)# active-gateway ipv6 mac 00:00:00:00:aa:01
IPv6-Link-Localaddress:
| switch(config-if-vlan)# | ipv6 address   | link-local | fe80::1/64   |     |
| ----------------------- | -------------- | ---------- | ------------ | --- |
| switch(config-if-vlan)# | active-gateway |            | ipv6 fe80::1 |     |
switch(config-if-vlan)# active-gateway ipv6 mac 00:00:00:00:aa:01
Configuringl3-src-mac,whenonlyaIPv4virtualMACisconfigured,aIPv4virtualMACisusedasa
sourceMACforIPv4routedpackets.
| switch(config-if-vlan)# | ip address | 192.168.1.250/24 |     |     |
| ----------------------- | ---------- | ---------------- | --- | --- |
switch(config-if-vlan)# active-gateway ip 192.168.1.253 mac 00:00:00:00:00:01
| switch(config-if-vlan)# | active-gateway |     | l3-src-mac |     |
| ----------------------- | -------------- | --- | ---------- | --- |
Configuringl3-src-mac,whenonlyaIPv6virtualMACisconfigured,aIPv6virtualMACisusedasa
sourceMACforIPv6routedpackets.
| switch(config-if-vlan)# | ip address | 192.168.1.250/24 |     |     |
| ----------------------- | ---------- | ---------------- | --- | --- |
switch(config-if-vlan)#
|                         | active-gateway |     | ipv6 fe80::01 | mac 00:00:00:01:00:01 |
| ----------------------- | -------------- | --- | ------------- | --------------------- |
| switch(config-if-vlan)# | active-gateway |     | l3-src-mac    |                       |
VSXcommands|116

Configuringl3-src-mac,whenbothIPv4andIPv6virtualMACsareconfigured,IPv4virtualMACisused
assourceMACforIPv4andIPv6routedpackets.ItisrecommendedtousethesamevirtualMACwhen
bothipv4andipv6vitrualMACsareconfigured.
| switch(config-if-vlan)# |     | ip  | address | 192.168.1.250/24 |     |     |     |     |
| ----------------------- | --- | --- | ------- | ---------------- | --- | --- | --- | --- |
switch(config-if-vlan)# active-gateway ip 192.168.1.253 mac 00:00:00:00:00:01
switch(config-if-vlan)#
|                         |     | active-gateway |     | ipv6       | fe80::01 | mac 00:00:00:00:00:01 |     |     |
| ----------------------- | --- | -------------- | --- | ---------- | -------- | --------------------- | --- | --- |
| switch(config-if-vlan)# |     | active-gateway |     | l3-src-mac |          |                       |     |     |
Whenipv4andipv6virtualMACsaresame,8325and10000switchessupport512SVIs.Whenipv4andipv6
virtualMACsaredifferent,8325and10000switchessupport341SVIs.
| Configuration | table | for supported |     | SVIs |     |           |           |      |
| ------------- | ----- | ------------- | --- | ---- | --- | --------- | --------- | ---- |
| Configuration |       |               |     |      |     | Platforms | Supported | SVIs |
Whenthel3-src-macIPv4isconfiguredonSVIalongwiththe 8320 Upto190
active-gateway
|     |     |     |     |     |     | 8325and10000 | Upto380 |     |
| --- | --- | --- | --- | --- | --- | ------------ | ------- | --- |
|     |     |     |     |     |     | 8360and6400  | Upto384 |     |
|     |     |     |     |     |     | 8100         | Upto256 |     |
Whenthel3-src-macIPv4andIPv6areconfiguredonSVIalong 8320 Upto165
withtheactive-gateway
|     |     |     |     |     |     | 8325and10000 | Upto330 |     |
| --- | --- | --- | --- | --- | --- | ------------ | ------- | --- |
|     |     |     |     |     |     | 8360and6400  | Upto384 |     |
|     |     |     |     |     |     | 8100         | Upto256 |     |
WhentheVSXactive-forwarding,VRRPandvirtual-macfeatures 8320,8325,8360, Goesdown
| areconfigured |     |     |     |     |     | 8100,6400,and |     |     |
| ------------- | --- | --- | --- | --- | --- | ------------- | --- | --- |
10000
Configuringl3-src-mac,whennovirtualMACsareconfigured,theSystemMACisusedassourceMAC
forroutedpackets.SuchconfigurationcangenerateaCLIwarningasshown.
| switch(config-if-vlan)# |                | ip             | address | 192.168.1.250/24 |     |     |     |     |
| ----------------------- | -------------- | -------------- | ------- | ---------------- | --- | --- | --- | --- |
| switch(config-if-vlan)# |                | active-gateway |         | l3-src-mac       |     |     |     |     |
| Warning:                | Active Gateway | VMAC           | is      | not configured   |     |     |     |     |
WithVSX-Syncconfigured,"active-gatewayl3-src-mac"configurationsyncestothepeerdevice.
Followingconfigurationfromvsx-primarydevicecangetsyncedtovsx-secondarydevice.
VSX-Primary-Switch:
| vsx-pri-switch(config-if-vlan)# |     |     |     | ip address | 192.168.1.250/24 |     |     |     |
| ------------------------------- | --- | --- | --- | ---------- | ---------------- | --- | --- | --- |
vsx-pri-switch(config-if-vlan)# active-gateway ip 192.168.1.253 mac
00:00:00:00:00:01
vsx-pri-switch(config-if-vlan)# active-gateway ipv6 fe80::01 mac 00:00:00:01:00:01
| vsx-pri-switch(config-if-vlan)# |     |     |     | active-gateway | l3-src-mac |     |     |     |
| ------------------------------- | --- | --- | --- | -------------- | ---------- | --- | --- | --- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 117

ForVSX-peerdevices,withoutVSX-Syncconfigured,itisexpectedthatvirtualMACsandl3-src-mac
configurationsareidenticalonbothdevicesforagiveninterfaceVLAN.Ifconfigurationsdon'tmatch,
eachdevicemayendupusingdifferentsourceMACforroutedtrafficforthisintefaceandconnectivity
fromconnecteddevicestothisVSX-peerdevicesmaygetaffected.
VSX-Primary-Switch:
| vsx-pri-switch(config-if-vlan)# |     |     | ip address | 192.168.1.250/24 |     |     |     |
| ------------------------------- | --- | --- | ---------- | ---------------- | --- | --- | --- |
vsx-pri-switch(config-if-vlan)# active-gateway ip 192.168.1.253 mac
00:00:00:00:00:01
vsx-pri-switch(config-if-vlan)# active-gateway ipv6 fe80::01 mac 00:00:00:01:00:01
| vsx-pri-switch(config-if-vlan)# |     |     | active-gateway | l3-src-mac |     |     |     |
| ------------------------------- | --- | --- | -------------- | ---------- | --- | --- | --- |
VSX-Secondary-Switch:
| vsx-sec-switch(config-if-vlan)# |     |     | ip address | 192.168.1.250/24 |     |     |     |
| ------------------------------- | --- | --- | ---------- | ---------------- | --- | --- | --- |
vsx-sec-switch(config-if-vlan)#
vsx-sec-switch(config-if-vlan)# active-gateway ip 192.168.1.253 mac
00:00:00:00:00:01
vsx-sec-switch(config-if-vlan)# active-gateway ipv6 fe80::01 mac 00:00:00:01:00:01
vsx-sec-switch(config-if-vlan)#
|     |     |     | active-gateway | l3-src-mac |     |     |     |
| --- | --- | --- | -------------- | ---------- | --- | --- | --- |
Configuringl2-vlan-mac-modefloodonaVLANinterface,l3-src-maccannotbeconfigured.Such
configurationcangenerateanerrorasshownandcommandwillnottakeaffect.
switch(config)#
|                         | system | l2-vlan-mac-mode |                  | flood      |     |     |     |
| ----------------------- | ------ | ---------------- | ---------------- | ---------- | --- | --- | --- |
| switch(config-if-vlan)# |        | ip address       | 192.168.1.250/24 |            |     |     |     |
| switch(config-if-vlan)# |        | active-gateway   |                  | l3-src-mac |     |     |     |
active-gateway l3-src-mac cannot be configured when l2-vlan-mac-mode flood is
configured.
| Configuration             | table | for supported | SVIs |     |              |              |      |
| ------------------------- | ----- | ------------- | ---- | --- | ------------ | ------------ | ---- |
| Configuration             |       |               |      |     | Platforms    | Supported    | SVIs |
| Whenfloodmodeisconfigured |       |               |      |     | 8320         | Lessthan512  |      |
|                           |       |               |      |     | 8325and10000 | Lessthan1024 |      |
Whentheactive-gatewayIPv4isconfiguredonSVIalongwiththe 8320 Upto190
floodmode
|     |     |     |     |     | 8325and10000 | Upto380 |     |
| --- | --- | --- | --- | --- | ------------ | ------- | --- |
Whentheactive-gatewayIPv4andIPv6areconfiguredonSVI 8320 Upto165
alongwiththefloodmode
|     |     |     |     |     | 8325and10000 | Upto330 |     |
| --- | --- | --- | --- | --- | ------------ | ------- | --- |
WhentheVSXactive-forwarding,VRRPandvirtual-macfeatures 8320,8325and Goesdown
| areconfigured |     |     |     |     | 10000 |     |     |
| ------------- | --- | --- | --- | --- | ----- | --- | --- |
Whenl3-src-macoptionisunconfigured,SystemMACusesassourceMACforroutedtraffic.
| switch(config-if-vlan)# |     | no active-gateway |     | l3-src-mac |     |     |     |
| ----------------------- | --- | ----------------- | --- | ---------- | --- | --- | --- |
VSXcommands|118

| Command History |     |     |                                                   |
| --------------- | --- | --- | ------------------------------------------------- |
| Release         |     |     | Modification                                      |
| 10.14           |     |     | AddedinformationrelatedtorolebasedIPFIX.          |
| 10.12.1000      |     |     | Addedtheextended-macfeaturesupportfor6400v2,8100, |
and8360v2switches.
| 10.12 |     |     | The l3-src-macparametersupportedfor6400,8100,and8360 |
| ----- | --- | --- | ---------------------------------------------------- |
switches.
10.10
Addedthel3-src-macparameterandcommandsupportedfor
9300switch.
10.09.0010 AddedIPv6supportforconfigurationofactivegatewayandSVI
withthesameaddress.
| 10.09 |     |     | Commandsupportedfor10000switch. |
| ----- | --- | --- | ------------------------------- |
10.08
Added<MAC-ADDRESS>parametertothenoformofthe
command.
| 10.07orearlier      |         |         | --        |
| ------------------- | ------- | ------- | --------- |
| Command Information |         |         |           |
| Platforms           | Command | context | Authority |
6300 config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8100
8360
8325
9300
10000
| config-sync    | disable |     |     |
| -------------- | ------- | --- | --- |
| config-sync    | disable |     |     |
| no config-sync | disable |     |     |
Description
PausesVSXsynchronization.
ThenoformofthiscommandrestartsVSXsynchronization.
Examples
PausesVSXconfigurationsynchronization:
| switch(config)#     | vsx |             |         |
| ------------------- | --- | ----------- | ------- |
| switch(config-vsx)# |     | config-sync | disable |
EnablestheVSXconfigurationsynchronization:
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 119

| switch(config)# | vsx |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
switch(config-vsx)#
|                     |         | no      | config-sync | disable      |     |
| ------------------- | ------- | ------- | ----------- | ------------ | --- |
| Command History     |         |         |             |              |     |
| Release             |         |         |             | Modification |     |
| 10.07orearlier      |         |         |             | --           |     |
| Command Information |         |         |             |              |     |
| Platforms           | Command | context |             | Authority    |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8100
8320
8325
8360
8400
9300
10000
| inter-switch-link    |             | {<PORT-NUM>    |       |           | | lag <LAG-ID>} |
| -------------------- | ----------- | -------------- | ----- | --------- | --------------- |
| inter-switch-link    | {<PORT-NUM> |                | | lag | <LAG-ID>} |                 |
| no inter-switch-link |             | [lag <LAG-ID>] |       |           |                 |
Description
ConfiguresaphysicalportoraLAGasaninterswitchlinkport.OnlyoneportorLAGcanbeconfigured
toactasanISL.OnceaportisconfiguredasanISL,itbecomesapartofallVLANsinasystem.
Thenoformofthiscommandclearstheconfigurationoftheinterswitchlinkportfromaphysicalport
oraLAG.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<PORT-NUM>
Specifiesaphysicalportontheswitch.Usetheformat
member/slot/port(forexample,1/3/1).Setstheporttoactas
ISL
<LAG-ID>
SpecifiestheLAGID.Runtheshow capacitiescommandfor
themaximumnumberofVSXLAGssupportedforyourparticular
typeofswitch.
Examples
Configuringport1/1/1asaninterswitchlinkport:
| switch(config-vsx)# |     | inter-switch-link |     | 1/1/1 |     |
| ------------------- | --- | ----------------- | --- | ----- | --- |
ConfiguringLAG100asaninterswitchlinkport:
VSXcommands|120

| switch(config-vsx)# |     | inter-switch-link |     | lag 100 |     |
| ------------------- | --- | ----------------- | --- | ------- | --- |
Clearstheinterswitchlinkport:
| switch(config-vsx)# |         | no inter-switch-link |                                                   |     |     |
| ------------------- | ------- | -------------------- | ------------------------------------------------- | --- | --- |
| Command History     |         |                      |                                                   |     |     |
| Release             |         |                      | Modification                                      |     |     |
| 10.08               |         |                      | Addedoptionallagparametertothenoformofthecommand. |     |     |
| 10.07orearlier      |         |                      | --                                                |     |     |
| Command Information |         |                      |                                                   |     |     |
| Platforms           | Command | context              | Authority                                         |     |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8100
8320
8325
8360
8400
9300
10000
| inter-switch-link    |               | dead-interval |                 |     |     |
| -------------------- | ------------- | ------------- | --------------- | --- | --- |
| inter-switch-link    | dead-interval |               | <DEAD-INTERVAL> |     |     |
| no inter-switch-link |               | dead-interval |                 |     |     |
Description
Setsthedeadintervalfortheinterswitchlinkprotocol.Thedeadintervalistheamountoftimetowait
forhellosfromapeerbeforedeclaringthepeertobedead.Thedefaultdeadintervaltimeis20
seconds.
Thenoformofthiscommandresetstheinterswitchlinkdeadintervaltothedefaultof20seconds.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<DEAD-INTERVAL> Specifiesthedeadintervalinseconds.Required.Range:2to20
seconds.
Examples
Settingthedeadintervalfortheinterswitchlinkprotocolto10seconds:
| switch(config)#     | vsx |                   |     |               |     |
| ------------------- | --- | ----------------- | --- | ------------- | --- |
| switch(config-vsx)# |     | inter-switch-link |     | dead-interval | 10  |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 121

Settingthedeadintervalfortheinterswitchlinkprotocoltothedefault:
| switch(config)#     | vsx     |         |                   |     |               |     |
| ------------------- | ------- | ------- | ----------------- | --- | ------------- | --- |
| switch(config-vsx)# |         | no vsx  | inter-switch-link |     | dead-interval |     |
| Command History     |         |         |                   |     |               |     |
| Release             |         |         | Modification      |     |               |     |
| 10.07orearlier      |         |         | --                |     |               |     |
| Command Information |         |         |                   |     |               |     |
| Platforms           | Command | context | Authority         |     |               |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --------------- | --- | --- | --- |
8320
8325
8360
8400
9300
10000
| inter-switch-link    |                | hello-interval |                  |     |     |     |
| -------------------- | -------------- | -------------- | ---------------- | --- | --- | --- |
| inter-switch-link    | hello-interval |                | <HELLO-INTERVAL> |     |     |     |
| no inter-switch-link |                | hello-interval |                  |     |     |     |
Description
Configurestheinterswitchlinkhello-interval.Thehellointervaldeterminesthefrequencyofahello
packetexchangetoconfirmthecontrolplaneofthepeerisalive.Thedefaulthello-intervalis1second.
Thenoformofthiscommandsetstheinterswitchlinkhello-intervaltothedefaultof1second.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<HELLO-INTERVAL> Specifieshellointervalinseconds.Range:1to5seconds.
Examples
Configuringtheinterswitchlinkhello-intervalto3seconds:
| switch(config)#     | vsx |                   |     |                |     |     |
| ------------------- | --- | ----------------- | --- | -------------- | --- | --- |
| switch(config-vsx)# |     | inter-switch-link |     | hello-interval |     | 3   |
Resettingtheinterswitchlinkhello-intervaltothedefaultof1second:
| switch(config)#     | vsx |                      |     |                |     |     |
| ------------------- | --- | -------------------- | --- | -------------- | --- | --- |
| switch(config-vsx)# |     | no inter-switch-link |     | hello-interval |     |     |
| Command History     |     |                      |     |                |     |     |
VSXcommands|122

| Release             |         |         | Modification |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --------------- | --- | --- |
8320
8325
8360
8400
9300
10000
| inter-switch-link    |           | hold-time       |     |     |     |
| -------------------- | --------- | --------------- | --- | --- | --- |
| inter-switch-link    | hold-time | <HOLD-INTERVAL> |     |     |     |
| no inter-switch-link |           | hold-time       |     |     |     |
Description
Setstheholdtimefortheinterswitchlinkprotocol.Aportistreatedasdownonlywhenitstaysdownfor
theconfiguredholdtimeinterval.Thedefaultholdtimeis0seconds.
Thenoformofthiscommandsetstheinterswitchlinkprotocolholdtimetothedefaultof0seconds.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<HOLD-INTERVAL> Specifiestheholdintervalinseconds.Required.Range:0to3
seconds.
Examples
Settingtheholdtimeforinterswitchlinkprotocolto2seconds:
| switch(config)#     | vsx |                   |     |           |     |
| ------------------- | --- | ----------------- | --- | --------- | --- |
| switch(config-vsx)# |     | inter-switch-link |     | hold-time | 2   |
Settingtheinterswitchlinkprotocolholdtimetothedefaultof0seconds:
| switch(config)#     | vsx |                      |              |           |     |
| ------------------- | --- | -------------------- | ------------ | --------- | --- |
| switch(config-vsx)# |     | no inter-switch-link |              | hold-time |     |
| Command History     |     |                      |              |           |     |
| Release             |     |                      | Modification |           |     |
| 10.07orearlier      |     |                      | --           |           |     |
| Command Information |     |                      |              |           |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 123

| Platforms | Command | context | Authority |     |     |
| --------- | ------- | ------- | --------- | --- | --- |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --------------- | --- | --- |
8320
8325
8360
8400
9300
10000
| inter-switch-link    |                      | peer-detect-interval |                        |     |     |
| -------------------- | -------------------- | -------------------- | ---------------------- | --- | --- |
| inter-switch-link    | peer-detect-interval |                      | <PEER-DETECT-INTERVAL> |     |     |
| no inter-switch-link |                      | peer-detect-interval |                        |     |     |
Description
SetstheamountoftimeinsecondsthattheVSXswitchwaitsfortheISLinterfacetolinkupaftera
reboot.IftheISLlinkdoesnotcomeupwithinthistimewindow,theVSXswitchdeclaresitselfassplit
fromitspeer.Thedefaultpeerdetectintervalis300seconds.
Thenoformofthiscommandsetstheinterswitchlinkprotocolpeerdetectintervaltothedefaultof300
seconds.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<PEER-DETECT-INTERVAL>
Specifiesthepeerdetectintervalinseconds.Required.Range:60
to1800seconds.
Usage
AfteraVSXswitchreboots,theswitchwaits5minutesbydefaulttoreceiveahellopacketbeforeit
declaresitselftobeout-of-sync.Theinter-switch-link peer-detect-interval <PEER-DETECT-
INTERVAL>commandletsyouchangehowlongtheswitchwaitstoreceivethehellopacketbeforethe
switchdeclaresitselftobeout-of-sync.
Examples
Settingthepeerdetectintervalto180seconds:
| switch(config)#     | vsx |                   |     |                      |     |
| ------------------- | --- | ----------------- | --- | -------------------- | --- |
| switch(config-vsx)# |     | inter-switch-link |     | peer-detect-interval | 180 |
Restoringthepeerdetectintervaltothedefault(300seconds):
| switch(config)#     | vsx |                      |              |                      |     |
| ------------------- | --- | -------------------- | ------------ | -------------------- | --- |
| switch(config-vsx)# |     | no inter-switch-link |              | peer-detect-interval |     |
| Command History     |     |                      |              |                      |     |
| Release             |     |                      | Modification |                      |     |
| 10.07orearlier      |     |                      | --           |                      |     |
VSXcommands|124

Command Information

Platforms

Command context

Authority

config-vsx

Administrators or local user group members with execution rights
for this command.

6400
8100
8320
8325
8360
8400
9300
10000

interface lag multi-chassis
interface lag <LAG-ID> multi-chassis [static]
no interface lag <LAG-ID>

Description

Configures a given LAG as a dynamic multichassis LAG (VSX LAG), which supports a maximum of four
member links per switch segment. A VSX LAG across a downstream switch can have at most a total of
eight member links.

The no form of this command removes a VSX LAG.

Parameter

<LAG-ID>

static

Usage

Description

Specifies the LAG ID. Run the show capacities vsx command
for the maximum number of VSX LAGs supported for your
particular type of switch; however, the maximum VSX LAG value
considers that one port is used for the ISL, which is not a VSX LAG.
Required.

Specifies the multichassis LAG as static. Optional.

A VSX LAG across a VSX pair can have at most a total of eight interfaces.

n When creating a VSX LAG, select an equal number of member links in each segment for load balancing, such

as four member links (one segment) and four member links (another segment). Do not create a VSX LAG

with four member links in one switch and two member links on another segment. A switch can have a

maximum of four member links.

n Make sure that the VSX LAG interface on both the VSX primary and secondary switches has a member port

configured and enabled.

n Make sure that you also have a non-VSX port that is available for the ISL.

n It is recommended to use hashing algorithm value as l3-src-dst (default) or l2-src-dst on the VSX LAG.

You cannot change the mode of a multichassis LAG without removing the multichassis LAG first. To
change a pre-existing VSX LAG to a static VSX LAG, first remove the VSX LAG with the no interface lag
<LAG-ID> command. Then, enter the interface lag <LAG-ID> multi-chassis static command.

Examples

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

125

ConfiguringLAG100asaVSXLAG:
| switch(config)# | interface |     | lag 100 multi-chassis |     |
| --------------- | --------- | --- | --------------------- | --- |
RemovingLAG100asaVSXLAG:
| switch(config)# | no  | interface | lag 100 |     |
| --------------- | --- | --------- | ------- | --- |
SpecifyingLAG100asastaticVSXLAG:
switch(config)#
|                     | interface |         | lag 100 multi-chassis | static |
| ------------------- | --------- | ------- | --------------------- | ------ |
| Command History     |           |         |                       |        |
| Release             |           |         | Modification          |        |
| 10.07orearlier      |           |         | --                    |        |
| Command Information |           |         |                       |        |
| Platforms           | Command   | context | Authority             |        |
6400 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8100
8320
8325
8360
8400
9300
10000
| ip icmp | redirect |     |     |     |
| ------- | -------- | --- | --- | --- |
ip icmp redirect
| no ip icmp redirect |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
Description
EnablesthesendingofICMPv4andICMPv6redirectmessagestothesourcehost.Enabledbydefault.
ThenoformofthiscommanddisablesICMPv4andICMPv6redirectmessagestothesourcehost.
Examples
EnablingICMPredirectmessages:
| switch(config)# | ip  | icmp redirect |     |     |
| --------------- | --- | ------------- | --- | --- |
DisablingICMPredirectmessages:
| switch(config)# | no  | ip icmp | redirect |     |
| --------------- | --- | ------- | -------- | --- |
VSXcommands|126

| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
6400 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8320
8325
8360
8400
9300
10000
| keepalive    | dead-interval |                 |     |     |
| ------------ | ------------- | --------------- | --- | --- |
| keepalive    | dead-interval | <DEAD-INTERVAL> |     |     |
| no keepalive | dead-interval |                 |     |     |
Description
Setsthedead-intervalforkeepaliveprotocol.Thedeadintervalistheamountoftimetowaitforhellos
fromapeerbeforedeclaringthepeertobedead.Thedefaultdead-intervalis3seconds.
Thenoformofthiscommandsetstheinterswitchlinkdead-intervaltothedefaultof3seconds.
| Parameter     |                 |     | Description |     |
| ------------- | --------------- | --- | ----------- | --- |
| dead-interval | <DEAD-INTERVAL> |     |             |     |
Specifiesthedead-intervalinseconds.Range:2to20seconds
Examples
Settingthedead-intervalforkeepaliveprotocolto10seconds:
| switch(config)#     | vsx |           |               |     |
| ------------------- | --- | --------- | ------------- | --- |
| switch(config-vsx)# |     | keepalive | dead-interval | 10  |
Settingthedead-intervalforkeepaliveprotocoltothedefault:
| switch(config)#     | vsx     |              |               |     |
| ------------------- | ------- | ------------ | ------------- | --- |
| switch(config-vsx)# |         | no keepalive | dead-interval |     |
| Command             | History |              |               |     |
| Release             |         |              | Modification  |     |
| 10.07orearlier      |         |              | --            |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 127

| Command   | Information |         |           |     |
| --------- | ----------- | ------- | --------- | --- |
| Platforms | Command     | context | Authority |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8100
8320
8325
8360
8400
9300
10000
| keepalive    | hello-interval |                  |     |     |
| ------------ | -------------- | ---------------- | --- | --- |
| keepalive    | hello-interval | <HELLO-INTERVAL> |     |     |
| no keepalive | hello-interval |                  |     |     |
Description
Setsthehello-intervalforkeepaliveprotocol.Thehellointervaldeterminesthefrequencyofahello
packetexchangetoconfirmthepeerisalive.Thedefaulthello-intervalis1second.
Thenoformofthiscommandsetsthehello-intervalforkeepaliveprotocoltothedefaultof1second.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
hello-interval <HELLO-INTERVAL> Specifiesthehello-intervalinseconds.Range:1to5seconds
Examples
Settingthehello-intervalforkeepaliveprotocolto3seconds:
| switch(config)#     | vsx |           |                |     |
| ------------------- | --- | --------- | -------------- | --- |
| switch(config-vsx)# |     | keepalive | hello-interval | 3   |
Resettingthehello-intervalforkeepaliveprotocoltothedefault:
| switch(config)#     | vsx         |              |                |     |
| ------------------- | ----------- | ------------ | -------------- | --- |
| switch(config-vsx)# |             | no keepalive | hello-interval |     |
| Command             | History     |              |                |     |
| Release             |             |              | Modification   |     |
| 10.07orearlier      |             |              | --             |     |
| Command             | Information |              |                |     |
| Platforms           | Command     | context      | Authority      |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
VSXcommands|128

Platforms

Command context

Authority

for this command.

8100
8320
8325
8360
8400
9300
10000

keepalive peer
keepalive peer <PEER-IP-ADDR> source <SOURCE-IP-ADDR> [vrf <VRF-NAME>]
no keepalive [peer <PEER-IP-ADDR> source <SOURCE-IP-ADDR> [vrf <VRF-NAME>]]

Description

Sets the source and peer IP addresses for keepalive packets in a specified VRF. If a VRF is not specified, it
sets to the default VRF. Both IPv4 and IPv6 are supported. Source and peer IP addresses for keepalive
packets can also be configured on the management VRF.

The no form of this command removes the source and peer IP addresses and VRF for the keepalive
protocol. VSX continues to work.

Parameter

Description

peer <PEER-IP-ADDR>

Specifies the peer IPv4 or IPv6 address. Syntax: A.B.C.D

source <IP-ADDR>

vrf <VRF-NAME>

Usage

Specifies the source IPv4 or IPv6 address. The source IP address is
the IP address assigned to the keepalive interface on the switch.
For example, if you are entering this command on the primary
switch, the source IP address would be the IP address assigned to
the keepalive interface on the primary switch. Syntax: A.B.C.D

Specifies the VRF name. If you are entering this command on the
primary switch, the peer IP address is the IP address assigned to
the keepalive interface for the secondary switch. If you are
entering this command on the secondary switch, the peer IP
address is the IP address assigned to the keepalive interface for
the primary switch. Syntax: String

To configure the keepalive feature, enter this command once on the primary switch and once on the
secondary switch. The keepalive feature is recommended for redundancy. If the ISL link goes down, the
keepalive connection keeps the traffic moving so that the peer and secondary switches can continue to
communicate. The keepalive connection is established over a routed network, and it does not have to
be a dedicated peer-to-peer link unlike ISL.

Examples

Setting the source and peer IP addresses for keepalive in the default VRF:

switch(config)# vsx
switch(config-vsx)# keepalive peer 192.168.1.1 source 192.168.1.5

Setting the source and peer IPv6 addresses for keepalive in the default VRF:

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

129

| switch(config)# | vsx |     |     |
| --------------- | --- | --- | --- |
switch(config-vsx)#
|     |     | keepalive peer | 2002:2 source 2002::3 |
| --- | --- | -------------- | --------------------- |
SettingthesourceandpeerIPaddressesforkeepaliveinthevrf1:
| switch(config)# | vsx |     |     |
| --------------- | --- | --- | --- |
switch(config-vsx)# keepalive peer 10.0.0.1 source 10.0.0.2 vrf vrf1
SettingthesourceandpeerIPaddressesforkeepaliveinthemanagamentVRF:
| switch(config)# | vsx |     |     |
| --------------- | --- | --- | --- |
switch(config-vsx)# keepalive peer 10.0.0.1 source 10.0.0.2 vrf mgmt
RemovingthesourceandpeerIPaddressesandVRFforthekeepaliveprotocol:
| switch(config)#     | vsx     |              |                                                 |
| ------------------- | ------- | ------------ | ----------------------------------------------- |
| switch(config-vsx)# |         | no keepalive |                                                 |
| Command History     |         |              |                                                 |
| Release             |         |              | Modification                                    |
| 10.08               |         |              | Addedoptionalparameterstothenoformofthecommand. |
| 10.07orearlier      |         |              | --                                              |
| Command Information |         |              |                                                 |
| Platforms           | Command | context      | Authority                                       |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| keepalive          | udp-port   |     |     |
| ------------------ | ---------- | --- | --- |
| keepalive udp-port | <PORT-NUM> |     |     |
| no keepalive       | udp-port   |     |     |
Description
SetstheUDPportforthekeepaliveprotocol.
ThenoformofthiscommandsetstheUDPportforkeepaliveprotocoltothedefaultof7678.
VSXcommands|130

| Parameter           |     |     | Description                             |
| ------------------- | --- | --- | --------------------------------------- |
| udp-port <PORT-NUM> |     |     | SpecifiesUDPportnumber.Range:1024-65535 |
Examples
SettingtheUDPportforkeepaliveprotocolto2000:
| switch(config)#     | vsx |           |               |
| ------------------- | --- | --------- | ------------- |
| switch(config-vsx)# |     | keepalive | udp-port 2000 |
SettingtheUDPportforkeepaliveprotocoltothedefaultof7678:
| switch(config)#     | vsx     |              |              |
| ------------------- | ------- | ------------ | ------------ |
| switch(config-vsx)# |         | no keepalive | udp-port     |
| Command History     |         |              |              |
| Release             |         |              | Modification |
| 10.07orearlier      |         |              | --           |
| Command Information |         |              |              |
| Platforms           | Command | context      | Authority    |
config-vsx
6400 Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
lacp fallback
lacp fallback
no lacp fallback
Description
SetsLACPfallbackonaVSXLAGport.WhennoLACPpartnerisdetected,theVSXLAGportmakes
membersoftheVSXLAGfunctionasnonbondedinterfaces.TocreateaVSXLAG,usetheinterface
lag multi-chassiscommand.
ThenoformofthiscommandsetstheVSXLAGtoablockstatewhennoLACPpartnerisdetected.
Usage
LACPfallbackissupportedonlywhenthereisasinglelinkfromthedownstreamorpeerdevicetoeach
VSXnode.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 131

Eventhoughthiscommandappearstobeacceptedonastandard/non-VSXLAG,thefallbackfeatureworksonlyon
aVSXLAG(multichassisLAG)interface.
Examples
EnablingLACPfallback:
| switch(config)#        | interface | lag 1         |     |
| ---------------------- | --------- | ------------- | --- |
| switch(config-lag-if)# |           | lacp fallback |     |
DisablesLACPfallback:
| switch(config)#        | interface | lag 1   |              |
| ---------------------- | --------- | ------- | ------------ |
| switch(config-lag-if)# |           | no lacp | fallback     |
| Command History        |           |         |              |
| Release                |           |         | Modification |
| 10.07orearlier         |           |         | --           |
| Command Information    |           |         |              |
| Platforms              | Command   | context | Authority    |
6400 config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
linkup-delay-timer
| linkup-delay-timer    | <DELAY-TIMER> |                 |     |
| --------------------- | ------------- | --------------- | --- |
| no linkup-delay-timer |               | [<DELAY-TIMER>] |     |
Description
ConfigurestheVSXlink-updelaytimer.TheVSXdelaytimerfeatureletsyouconfigurethedelaytimer,
whichdelaysbringingdownstreamVSXlinksup,followingaVSXdevicerebootoranISLflap.
ThenoformofthiscommandrestorestheVSXlink-updelaytimertoadefaultof180seconds.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<DELAY-TIMER> SpecifiestheVSXLAGbring-updelayinseconds.Range:0to600
seconds
VSXcommands|132

Usage
TherecommendeddelaytimersettingisdeterminedbythenumberofMACaddresses,ARPv4,and
routes.Thelink-updelaytimermightneedtobesettoahighervalueforlargernetworks,dependingon
theARPandroutingtablesize.
Table1:Recommendeddelaytimersettingsfor832xseriesswitches
Recommended delay
| MAC | ARPv4 | Routes |     |
| --- | ----- | ------ | --- |
timer setting
| 16K | 16K | 10K     | 120 |
| --- | --- | ------- | --- |
| 32K | 32K | 10K     | 120 |
| 47K | 47K | 10K     | 150 |
| 47K | 47K | 10K     | 250 |
| 47K | 47K | 10K     | 250 |
| 47K | 69K | 10KOSPF | 420 |
Table2:Recommendeddelaytimersettingsfor8400seriesswitches
Recommended delay
| MAC | ARPv4 | Routes |     |
| --- | ----- | ------ | --- |
timer setting
| 40K | 40K | 512             | 300 |
| --- | --- | --------------- | --- |
| 32K | 32K | 512             | 180 |
| 48K | 48K | 512             | 480 |
| 48K | 48K | 20KIPv4+20KIPV6 | 600 |
| 48K | 48K | 10KIPv4+10KIPv6 | 480 |
| 32K | -   | 10KIPv4         | 180 |
Examples
SettingtheVSXlink-updelaytimerto35seconds:
| switch(config)# vsx |                    |     |     |
| ------------------- | ------------------ | --- | --- |
| switch(config-vsx)# | linkup-delay-timer | 35  |     |
SettingtheVSXlink-updelaytimertothedefault:
| switch(config)# vsx |                       |     |     |
| ------------------- | --------------------- | --- | --- |
| switch(config-vsx)# | no linkup-delay-timer |     |     |
Command History
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 133

| Release |     |     |     |     | Modification |     |     |
| ------- | --- | --- | --- | --- | ------------ | --- | --- |
10.08
Addedoptional<DELAY-TIMER>parametertothenoformofthe
command.
| 10.07orearlier      |         |     |         |     | --        |     |     |
| ------------------- | ------- | --- | ------- | --- | --------- | --- | --- |
| Command Information |         |     |         |     |           |     |     |
| Platforms           | Command |     | context |     | Authority |     |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- |
8320
8325
8360
8400
9300
10000
| linkup-delay-timer    |     |         | exclude  |            | lag-list   |     |     |
| --------------------- | --- | ------- | -------- | ---------- | ---------- | --- | --- |
| linkup-delay-timer    |     | exclude | lag-list | <LAG-LIST> |            |     |     |
| no linkup-delay-timer |     | exclude | lag-list |            | <LAG-LIST> |     |     |
Description
ConfigurestheVSXlink-updelaytimerexcludelist.Itexcludesthebringingupofspecifieddownstream
VSXLAGs,followingadevicerebootoranISLflap.
ThenoformofthiscommandunconfigurestheVSXlink-updelaytimerexcludelist.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<LAG-LIST>
SpecifiesarangeorasetofLAGinterfacestoexclude.For
example:1or1-10or1,2,3or1,2-10.Range:1-128characters.
Examples
SpecifyingLAGstoexcludeLAG100:
| switch(config)#     |     | vsx                |     |     |     |                  |     |
| ------------------- | --- | ------------------ | --- | --- | --- | ---------------- | --- |
| switch(config-vsx)# |     | linkup-delay-timer |     |     |     | exclude lag-list | 100 |
UnconfiguringtheVSXlink-updelaytimerexcludelistforLAG100:
| switch(config)#     |     | vsx |                    |     |     |                  |     |
| ------------------- | --- | --- | ------------------ | --- | --- | ---------------- | --- |
| switch(config-vsx)# |     | no  | linkup-delay-timer |     |     | exclude lag-list | 100 |
| Command History     |     |     |                    |     |     |                  |     |
VSXcommands|134

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| neighbor              | <IP-ADDRESS> |                  | vsx-sync-exclude |
| --------------------- | ------------ | ---------------- | ---------------- |
| neighbor <IP-ADDRESS> |              | vsx-sync-exclude |                  |
Description
ExcludesVSXsyncfortheBGPneighbor.
Examples
ExcludingVSXsyncfortheBGPneighbor:
| switch(config-bgp)# |             | neighbor | 1.1.1.1 vsx-sync-exclude |
| ------------------- | ----------- | -------- | ------------------------ |
| Command             | History     |          |                          |
| Release             |             |          | Modification             |
| 10.07orearlier      |             |          | --                       |
| Command             | Information |          |                          |
| Platforms           | Command     | context  | Authority                |
6400 config-bgp Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8100
8320
8325
8360
8400
9300
10000
| role {primary | |            | secondary} |     |
| ------------- | ------------ | ---------- | --- |
| role {primary | | secondary} |            |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 135

no role
Description
ConfigurestheVSXdevicerole.
ThenoformofthiscommandremovesthedeviceroleoftheswitchinVSXandcausestheinterswitch
linktobeout-of-sync.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
{primary | secondary} SelectstheVSXroletoeitherprimaryorsecondaryforthedevice.
Usage
VSXhasnodefaultroledefinedforthedevice.Thedeviceroleassignsthedeviceastheprimaryor
secondaryforVSXsynchronization.ForISLtobein-sync,onedeviceinVSXmustbeconfiguredasthe
primaryandtheotherdevicemustbeconfiguredasthesecondary.
Examples
SettingtheVSXroletoprimary:
| switch(config)#     | vsx |              |     |
| ------------------- | --- | ------------ | --- |
| switch(config-vsx)# |     | role primary |     |
Removingthedevicerole:
| switch(config)#     | vsx     |         |              |
| ------------------- | ------- | ------- | ------------ |
| switch(config-vsx)# |         | no role |              |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
show active-gateway
| show active-gateway | [vsx-peer] |     |     |
| ------------------- | ---------- | --- | --- |
VSXcommands|136

Description
DisplaysthegatewayinformationconfiguredonSVIs,suchas:
n Numberofactive-gatewayinterfaceVLANs
n NumberofIPv4active-gatewayinterfaceVLANs
n NumberofIPv6active-gatewayinterfaceVLANs
PervirtualMACaddress
n
o IPv4referencecountanditsinterfaceVLANs
o IPv6referencecountanditsinterfaceVLANs
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| primary#               | show active-gateway    |                       |       |       |
| ---------------------- | ---------------------- | --------------------- | ----- | ----- |
| Number                 | of active-gateway      | interface             | VLANs | : 265 |
| Number                 | of IPv4 active-gateway | interface             | VLANs | : 264 |
| Number                 | of IPv6 active-gateway | interface             | VLANs | : 1   |
| VMAC 00:00:00:01:01:16 |                        | :                     |       |       |
| IPv4                   | ref count              | : 32                  |       |       |
| IPv4                   | interface VLANs        | : vlan192-223         |       |       |
| IPv6                   | ref count              | : 0                   |       |       |
| IPv6                   | interface VLANs        | : none                |       |       |
| VMAC 00:00:00:01:01:11 |                        | :                     |       |       |
| IPv4                   | ref count              | : 32                  |       |       |
| IPv4                   | interface VLANs        | : vlan32-63           |       |       |
| IPv6                   | ref count              | : 0                   |       |       |
| IPv6                   | interface VLANs        | : none                |       |       |
| VMAC 00:00:00:01:01:17 |                        | :                     |       |       |
| IPv4                   | ref count              | : 32                  |       |       |
| IPv4                   | interface VLANs        | : vlan224-255         |       |       |
| IPv6                   | ref count              | : 0                   |       |       |
| IPv6                   | interface VLANs        | : none                |       |       |
| VMAC 00:00:00:01:01:18 |                        | :                     |       |       |
| IPv4                   | ref count              | : 6                   |       |       |
| IPv4                   | interface VLANs        | : vlan256-259,300-301 |       |       |
| IPv6                   | ref count              | : 0                   |       |       |
| IPv6                   | interface VLANs        | : none                |       |       |
| VMAC 00:00:00:01:01:13 |                        | :                     |       |       |
| IPv4                   | ref count              | : 32                  |       |       |
| IPv4                   | interface VLANs        | : vlan96-127          |       |       |
| IPv6                   | ref count              | : 0                   |       |       |
| IPv6                   | interface VLANs        | : none                |       |       |
| VMAC 00:00:00:01:01:12 |                        | :                     |       |       |
| IPv4                   | ref count              | : 32                  |       |       |
| IPv4                   | interface VLANs        | : vlan64-95           |       |       |
| IPv6                   | ref count              | : 0                   |       |       |
| IPv6                   | interface VLANs        | : none                |       |       |
| VMAC 00:00:00:01:01:20 |                        | :                     |       |       |
| IPv4                   | ref count              | : 1                   |       |       |
| IPv4                   | interface VLANs        | : vlan4040            |       |       |
| IPv6                   | ref count              | : 0                   |       |       |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 137

| IPv6                   | interface | VLANs : none        |              |
| ---------------------- | --------- | ------------------- | ------------ |
| VMAC 00:00:00:01:01:14 |           | :                   |              |
| IPv4                   | ref count | : 32                |              |
| IPv4                   | interface | VLANs : vlan128-159 |              |
| IPv6                   | ref count | : 0                 |              |
| IPv6                   | interface | VLANs : none        |              |
| VMAC 00:00:00:01:01:10 |           | :                   |              |
| IPv4                   | ref count | : 31                |              |
| IPv4                   | interface | VLANs : vlan1-31    |              |
| IPv6                   | ref count | : 0                 |              |
| IPv6                   | interface | VLANs : none        |              |
| VMAC 00:00:00:01:01:15 |           | :                   |              |
| IPv4                   | ref count | : 32                |              |
| IPv4                   | interface | VLANs : vlan160-191 |              |
| IPv6                   | ref count | : 0                 |              |
| IPv6                   | interface | VLANs : none        |              |
| VMAC 00:00:00:03:00:12 |           | :                   |              |
| IPv4                   | ref count | : 1                 |              |
| IPv4                   | interface | VLANs : vlan2000    |              |
| IPv6                   | ref count | : 1                 |              |
| IPv6                   | interface | VLANs : vlan4000    |              |
| VMAC 00:00:00:01:01:19 |           | :                   |              |
| IPv4                   | ref count | : 1                 |              |
| IPv4                   | interface | VLANs : vlan4000    |              |
| IPv6                   | ref count | : 0                 |              |
| IPv6                   | interface | VLANs : none        |              |
| Command History        |           |                     |              |
| Release                |           |                     | Modification |
| 10.07orearlier         |           |                     | --           |
| Command Information    |           |                     |              |
| Platforms              | Command   | context             | Authority    |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
8325
8360
8400
9300
10000
| show active-gateway |          | <IFNAME>   |     |
| ------------------- | -------- | ---------- | --- |
| show active-gateway | <IFNAME> | [vsx-peer] |     |
Description
DisplaysthegatewayinformationperSVI,suchas:
n Active-GatewayIPV4anditsMACaddress
n Active-GatewayIPV6anditsMACaddress
VSXcommands|138

| Parameter |     |     | Description                   |     |
| --------- | --- | --- | ----------------------------- | --- |
| <IFNAME>  |     |     | SpecifiestheVSXinterfacename. |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch#        | show active-gateway | vlan2000    |     |                     |
| -------------- | ------------------- | ----------- | --- | ------------------- |
| Active-gateway | IPv4                | MAC address |     | : 00:00:00:01:01:18 |
| Active-gateway | IPv4                | address     |     |                     |
173.6.1.10
173.7.1.10
| Active-gateway | IPv6 | MAC address |     | : 00:00:00:03:00:12 |
| -------------- | ---- | ----------- | --- | ------------------- |
| Active-gateway | IPv6 | address     |     |                     |
173::2
173::3
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | ------------------------------------- | --- |
8325
8360
8400
9300
10000
| show interface |             | <VLAN-NAME> |     |     |
| -------------- | ----------- | ----------- | --- | --- |
| show interface | <VLAN-NAME> | [vsx-peer]  |     |     |
Description
DisplaysavirtualIPv4/IPv6andMACconfiguredforactive-activerouting.
| Parameter   |     |     | Description                        |     |
| ----------- | --- | --- | ---------------------------------- | --- |
| <VLAN-NAME> |     |     | SpecifiestheVLANname.Syntax:string |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 139

| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch#    |                | show interface |                | vlan100      |                   |                   |     |       |
| ---------- | -------------- | -------------- | -------------- | ------------ | ----------------- | ----------------- | --- | ----- |
| Interface  |                | vlan100        | is             | up           |                   |                   |     |       |
| Admin      | state          | is             | up             |              |                   |                   |     |       |
| Hardware:  |                | Ethernet,      |                | MAC Address: |                   | 48:0f:cf:af:c1:9e |     |       |
| IPv4       | address        |                | 192.168.1.1/24 |              |                   |                   |     |       |
| IPv4       | address        |                | 192.168.2.1/24 |              | secondary         |                   |     |       |
|            | active-gateway |                | ip             | mac          | 00:00:00:00:00:01 |                   |     |       |
|            | active-gateway |                | ip             | 192.168.1.1  |                   |                   |     |       |
|            | active-gateway |                | ip             | 192.168.2.2  |                   |                   |     |       |
|            | active-gateway |                | ipv6           | mac          | 00:00:00:00:00:01 |                   |     |       |
|            | active-gateway |                | ipv6           | fe80::1      |                   |                   |     |       |
| Statistics |                |                |                |              |                   | RX                | TX  | Total |
------------- -------------------- -------------------- --------------------
| L3             | Packets     |         |     |         |     | 8            | 2   | 10  |
| -------------- | ----------- | ------- | --- | ------- | --- | ------------ | --- | --- |
| L3             | Bytes       |         |     |         |     | 812          | 80  | 892 |
| Command        | History     |         |     |         |     |              |     |     |
| Release        |             |         |     |         |     | Modification |     |     |
| 10.07orearlier |             |         |     |         |     | --           |     |     |
| Command        | Information |         |     |         |     |              |     |     |
| Platforms      |             | Command |     | context |     | Authority    |     |     |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 8100 |     |     |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| ---- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
(#)
commandfromtheoperatorcontext(>)only.
8320
8325
8360
8400
9300
10000
| show      | lacp       | aggregates |              |     |     |            |     |     |
| --------- | ---------- | ---------- | ------------ | --- | --- | ---------- | --- | --- |
| show lacp | aggregates |            | [<LAG-NAME>] |     |     | [vsx-peer] |     |     |
Description
DisplaysaspecifiedLAGorallconfiguredLAGsalongwithVSXLAGs.
VSXcommands|140

| Parameter  |     |     |     |     | Description                                |
| ---------- | --- | --- | --- | --- | ------------------------------------------ |
| <LAG-NAME> |     |     |     |     | SpecifiestheLAGname.Optional.Syntax:string |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingallconfiguredLAGsalongwithVSXLAGs:
| switch#    |            | show lacp | aggregates   |                 |     |
| ---------- | ---------- | --------- | ------------ | --------------- | --- |
| Aggregate  |            | name      | : lag100     | (multi-chassis) |     |
| Interfaces |            |           | : 1/1/44     |                 |     |
| Peer       | interfaces |           | : 1/1/44     |                 |     |
| Heartbeat  |            | rate      | : Slow       |                 |     |
| Hash       |            |           | : l3-src-dst |                 |     |
| Aggregate  |            | mode      | : Active     |                 |     |
DisplayingaspecifiedLAG:
| switch#        |             | show lacp | aggregates   | lag100          |              |
| -------------- | ----------- | --------- | ------------ | --------------- | ------------ |
| Aggregate      |             | name      | : lag100     | (multi-chassis) |              |
| Interfaces     |             |           | : 1/1/44     |                 |              |
| Peer           | interfaces  |           | : 1/1/44     |                 |              |
| Heartbeat      |             | rate      | : Slow       |                 |              |
| Hash           |             |           | : l3-src-dst |                 |              |
| Aggregate      |             | mode      | : Active     |                 |              |
| Command        | History     |           |              |                 |              |
| Release        |             |           |              |                 | Modification |
| 10.07orearlier |             |           |              |                 | --           |
| Command        | Information |           |              |                 |              |
| Platforms      |             | Command   | context      |                 | Authority    |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | --- | --- | ------------------------------------- |
8325
8360
8400
9300
10000
| show      | lacp       | interfaces |            |            |     |
| --------- | ---------- | ---------- | ---------- | ---------- | --- |
| show lacp | interfaces |            | [<IFNAME>] | [vsx-peer] |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 141

Description
DisplaysanLACPconfigurationofthephysicalinterfaces,includingVSXs.Ifaninterfacenameispassed
asargument,itonlydisplaysanLACPconfigurationofaspecifiedinterface.
| Parameter |     |     |     | Description                        |     |     |     |     |
| --------- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
| <IFNAME>  |     |     |     | Optional:Specifiesaninterfacename. |     |     |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ThisexampledisplaysanLACPconfigurationofthephysicalinterfaces.Oneoftheinterfaceshasthe
lacp-blockforwardingstate.IfaVSXswitchhasloopprotectenabledonaninterfaceandaloopoccurs,
VSXblockstheinterfacetostoptheloop.Theforwardingstateoftheblockedinterfaceissettolacp-
block.
switch#
|       | show          | lacp interfaces |                |     |            |          |            |     |
| ----- | ------------- | --------------- | -------------- | --- | ---------- | -------- | ---------- | --- |
| State | abbreviations |                 | :              |     |            |          |            |     |
| A -   | Active        | P               | - Passive      | F - | Aggregable | I -      | Individual |     |
| S -   | Short-timeout | L               | - Long-timeout | N - | InSync     | O -      | OutofSync  |     |
| C -   | Collecting    | D               | - Distributing |     |            |          |            |     |
| X -   | State m/c     | expired         |                | E - | Default    | neighbor | state      |     |
| Actor | details       | of all          | interfaces:    |     |            |          |            |     |
----------------------------------------------------------------------------------
--
| Intf | Aggr | Port | Port | State System-id |     |     | System Aggr | Forwarding |
| ---- | ---- | ---- | ---- | --------------- | --- | --- | ----------- | ---------- |
|      | name | id   | Pri  |                 |     |     | Pri Key     | State      |
----------------------------------------------------------------------------------
--
| 1/1/1   | lag10   | 17     | 1           | ALFOE 70:72:cf:37:a3:5c  |     |     | 20 10  | lacp-block |
| ------- | ------- | ------ | ----------- | ------------------------ | --- | --- | ------ | ---------- |
| 1/1/2   | lag128  | 69     | 1           | ALFNCD 70:72:cf:37:a3:5c |     |     | 20 128 | up         |
| 1/1/3   | lag128  | 14     | 1           | ALFNCD 70:72:cf:37:a3:5c |     |     | 20 128 | up         |
| 1/1/4   | lag128  |        |             |                          |     |     |        | down       |
| 1/1/5   | lag20   |        |             |                          |     |     |        | up         |
| Partner | details | of all | interfaces: |                          |     |     |        |            |
------------------------------------------------------------------------------
| Intf | Aggr | Partner | Port | State | System-id |     | System   | Aggr |
| ---- | ---- | ------- | ---- | ----- | --------- | --- | -------- | ---- |
|      | name | Port-id | Pri  |       |           |     | Priority | Key  |
------------------------------------------------------------------------------
| 1/1/1 | lag10  | 0   | 65534 | PLFOEX | 00:00:00:00:00:00 |     | 65534 | 0   |
| ----- | ------ | --- | ----- | ------ | ----------------- | --- | ----- | --- |
| 1/1/2 | lag128 | 69  | 1     | PLFNCD | 70:72:cf:8c:60:a7 |     | 65534 | 128 |
| 1/1/3 | lag128 | 14  | 1     | PLFNCD | 70:72:cf:8c:60:a7 |     | 65534 | 128 |
1/1/4 lag128
1/1/5 lag20
DisplayingstaticLAG:
| switch# | show          | lacp interfaces |                |     |            |     |            |     |
| ------- | ------------- | --------------- | -------------- | --- | ---------- | --- | ---------- | --- |
| State   | abbreviations |                 | :              |     |            |     |            |     |
| A -     | Active        | P               | - Passive      | F - | Aggregable | I - | Individual |     |
| S -     | Short-timeout | L               | - Long-timeout | N - | InSync     | O - | OutofSync  |     |
VSXcommands|142

| C -   | Collecting |             | D - Distributing |     |     |           |          |       |     |
| ----- | ---------- | ----------- | ---------------- | --- | --- | --------- | -------- | ----- | --- |
| X -   | State      | m/c expired |                  |     | E   | - Default | neighbor | state |     |
| Actor | details    | of          | all interfaces:  |     |     |           |          |       |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port | State |     | System-id |     | System Aggr | Forwarding |
| ---- | ---- | ---- | ---- | ----- | --- | --------- | --- | ----------- | ---------- |
|      | Name | Id   | Pri  |       |     |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/1   | lag10   |     |                    |     |     |     |     |     | up  |
| ------- | ------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
| 1/1/2   | lag10   |     |                    |     |     |     |     |     | up  |
| Partner | details |     | of all interfaces: |     |     |     |     |     |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port | State |     | System-id |     | System Aggr |     |
| ---- | ---- | ---- | ---- | ----- | --- | --------- | --- | ----------- | --- |
|      | Name | Id   | Pri  |       |     |           |     | Pri Key     |     |
------------------------------------------------------------------------------
1/1/1 lag10
1/1/2 lag10
DisplayinganLACPconfigurationofthe1/1/1interface:
| switch#        | show          | lacp        | interfaces       | 1/1/1 |     |              |          |              |     |
| -------------- | ------------- | ----------- | ---------------- | ----- | --- | ------------ | -------- | ------------ | --- |
| State          | abbreviations |             | :                |       |     |              |          |              |     |
| A -            | Active        |             | P - Passive      |       | F   | - Aggregable | I        | - Individual |     |
| S -            | Short-timeout |             | L - Long-timeout |       | N   | - InSync     | O        | - OutofSync  |     |
| C -            | Collecting    |             | D - Distributing |       |     |              |          |              |     |
| X -            | State         | m/c expired |                  |       | E   | - Default    | neighbor | state        |     |
| Aggregate-name |               |             | : lag1           |       |     |              |          |              |     |
-------------------------------------------------
|     |     |     | Actor |     |     | Partner |     |     |     |
| --- | --- | --- | ----- | --- | --- | ------- | --- | --- | --- |
-------------------------------------------------
| Port-id         |     |     | | 28                |     |     | | 31                |     |     |     |
| --------------- | --- | --- | ------------------- | --- | --- | ------------------- | --- | --- | --- |
| Port-priority   |     |     | | 1                 |     |     | | 1                 |     |     |     |
| Key             |     |     | | 1                 |     |     | | 1                 |     |     |     |
| State           |     |     | | ALFNCD            |     |     | | ALFNCD            |     |     |     |
| System-id       |     |     | | 98:f2:b3:68:40:a0 |     |     | | 98:f2:b3:68:60:a6 |     |     |     |
| System-priority |     |     | | 65534             |     |     | | 65534             |     |     |     |
DisplayinganLACPconfigurationafterloop-protectisenabledontheprimaryVSXswitch:
switch#
|       | show          | lacp        | interfaces       |     |     |              |          |              |     |
| ----- | ------------- | ----------- | ---------------- | --- | --- | ------------ | -------- | ------------ | --- |
| State | abbreviations |             | :                |     |     |              |          |              |     |
| A -   | Active        |             | P - Passive      |     | F   | - Aggregable | I        | - Individual |     |
| S -   | Short-timeout |             | L - Long-timeout |     | N   | - InSync     | O        | - OutofSync  |     |
| C -   | Collecting    |             | D - Distributing |     |     |              |          |              |     |
| X -   | State         | m/c expired |                  |     | E   | - Default    | neighbor | state        |     |
| Actor | details       | of          | all interfaces:  |     |     |              |          |              |     |
------------------------------------------------------------------------------
| Intf | Aggr |     | Port Port | State |     | System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --- | --------- | ----- | --- | --------- | --- | ----------- | ---------- |
|      | Name |     | Id Pri    |       |     |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/4/14 | lag1(mc) |     | 206 1 | ALFNCD |     | f8:60:f0:06:49:00 |     | 65534 1 | up   |
| ------ | -------- | --- | ----- | ------ | --- | ----------------- | --- | ------- | ---- |
| 1/5/15 | lag2(mc) |     |       |        |     |                   |     |         | down |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 143

| Partner | details | of all interfaces: |     |     |     |     |     |
| ------- | ------- | ------------------ | --- | --- | --- | --- | --- |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port State | System-ID |     | System Aggr |     |
| ---- | ---- | ---- | ---------- | --------- | --- | ----------- | --- |
|      | Name | Id   | Pri        |           |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/4/14 | lag1(mc) | 130 | 1 ALFNCD | f8:60:f0:06:87:00 |     | 65534 1 |     |
| ------ | -------- | --- | -------- | ----------------- | --- | ------- | --- |
| 1/5/15 | lag2(mc) |     |          |                   |     |         |     |
DisplayinganLACPconfigurationafterloop-protectisenabledonthesecondaryVSXswitch:
| switch#           | show lacp     | interfaces       |     |                |          |            |     |
| ----------------- | ------------- | ---------------- | --- | -------------- | -------- | ---------- | --- |
| State             | abbreviations | :                |     |                |          |            |     |
| A - Active        |               | P - Passive      |     | F - Aggregable | I -      | Individual |     |
| S - Short-timeout |               | L - Long-timeout |     | N - InSync     | O -      | OutofSync  |     |
| C - Collecting    |               | D - Distributing |     |                |          |            |     |
| X - State         | m/c expired   |                  |     | E - Default    | neighbor | state      |     |
| Actor             | details of    | all interfaces:  |     |                |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port State | System-ID |     | System Aggr | Forwarding |
| ---- | ---- | ---- | ---------- | --------- | --- | ----------- | ---------- |
|      | Name | Id   | Pri        |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/3/2   | lag1(mc) | 1130               | 1 ALFNCD | f8:60:f0:06:49:00 |     | 65534 1 | up   |
| ------- | -------- | ------------------ | -------- | ----------------- | --- | ------- | ---- |
| 1/9/3   | lag2(mc) |                    |          |                   |     |         | down |
| Partner | details  | of all interfaces: |          |                   |     |         |      |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port State | System-ID |     | System Aggr |     |
| ---- | ---- | ---- | ---------- | --------- | --- | ----------- | --- |
|      | Name | Id   | Pri        |           |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/3/2          | lag1(mc)    | 131     | 1 ALFNCD | f8:60:f0:06:87:00                                    |     | 65534 1 |     |
| -------------- | ----------- | ------- | -------- | ---------------------------------------------------- | --- | ------- | --- |
| 1/9/3          | lag2(mc)    |         |          |                                                      |     |         |     |
| Command        | History     |         |          |                                                      |     |         |     |
| Release        |             |         |          | Modification                                         |     |         |     |
| 10.07orearlier |             |         |          | --                                                   |     |         |     |
| Command        | Information |         |          |                                                      |     |         |     |
| Platforms      | Command     | context |          | Authority                                            |     |         |     |
| 6400           |             |         |          | OperatorsorAdministratorsorlocalusergroupmemberswith |     |         |     |
Operator(>)orManager
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     |     | commandfromtheoperatorcontext(>)only. |     |     |     |
| ---- | --- | --- | --- | ------------------------------------- | --- | --- | --- |
8325
8360
8400
9300
10000
| show | lacp interfaces |     | multi-chassis |     |     |     |     |
| ---- | --------------- | --- | ------------- | --- | --- | --- | --- |
VSXcommands|144

| show lacp | interfaces |     | multi-chassis |     | [<IFNAME>] | [vsx-peer] |     |     |
| --------- | ---------- | --- | ------------- | --- | ---------- | ---------- | --- | --- |
Description
ShowsallconfiguredVSXremoteinterfacedetails.TheinterfacethathastheALFNCDstatushasbeen
syncedwiththepartnerandisreadyforflowdistribution.
| Parameter |     |     |     |     | Description                            |     |     |     |
| --------- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- |
| <IFNAME>  |     |     |     |     | SpecifiestheVSXinterfacename.Optional. |     |     |     |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch# | show          | lacp        | interfaces |              | multi-chassis |            |                |     |
| ------- | ------------- | ----------- | ---------- | ------------ | ------------- | ---------- | -------------- | --- |
| State   | abbreviations |             | :          |              |               |            |                |     |
| A -     | Active        |             | P -        | Passive      | F -           | Aggregable | I - Individual |     |
| S -     | Short-timeout |             | L -        | Long-timeout | N -           | InSync     | O - OutofSync  |     |
| C -     | Collecting    |             | D -        | Distributing |               |            |                |     |
| X -     | State         | m/c expired |            |              | E -           | Default    | neighbor state |     |
| Actor   | details       |             | of all     | interfaces:  |               |            |                |     |
------------------------------------------------------------------------------
| Intf | Aggregate |     | Port | Port     | State | System-ID |     | System Aggr  |
| ---- | --------- | --- | ---- | -------- | ----- | --------- | --- | ------------ |
|      | name      |     | id   | Priority |       |           |     | Priority Key |
------------------------------------------------------------------------------
| 1/1/2   | lag100(mc) |     | 2      | 1           | ALFNCD | 08:00:09:13:06:7c |     | 65534 100 |
| ------- | ---------- | --- | ------ | ----------- | ------ | ----------------- | --- | --------- |
| Partner | details    |     | of all | interfaces: |        |                   |     |           |
------------------------------------------------------------------------------
| Intf | Aggregate |     | Partner | Port     | State | System-ID |     | System Aggr  |
| ---- | --------- | --- | ------- | -------- | ----- | --------- | --- | ------------ |
|      | name      |     | Port-id | Priority |       |           |     | Priority Key |
------------------------------------------------------------------------------
| 1/1/2  | lag100(mc) |         | 2   | 1      | ALFNCD      | 08:00:09:05:24:f6 |     | 65534 10 |
| ------ | ---------- | ------- | --- | ------ | ----------- | ----------------- | --- | -------- |
| Remote | Actor      | details |     | of all | interfaces: |                   |     |          |
------------------------------------------------------------------------------
| Intf | Aggregate |     | Port | Port     | State | System-ID |     | System Aggr  |
| ---- | --------- | --- | ---- | -------- | ----- | --------- | --- | ------------ |
|      | name      |     | id   | Priority |       |           |     | Priority Key |
------------------------------------------------------------------------------
| 1/1/2  | lag100(mc) |     | 1002    | 1      | ALFNCD      | 08:00:09:13:06:7c |     | 65534 100 |
| ------ | ---------- | --- | ------- | ------ | ----------- | ----------------- | --- | --------- |
| Remote | Partner    |     | details | of all | interfaces: |                   |     |           |
------------------------------------------------------------------------------
| Intf | Aggregate |     | Partner | Port     | State | System-ID |     | System Aggr  |
| ---- | --------- | --- | ------- | -------- | ----- | --------- | --- | ------------ |
|      | name      |     | Port-id | Priority |       |           |     | Priority Key |
------------------------------------------------------------------------------
| 1/1/2   | lag100(mc) |     | 3   | 1   | ALFNCD | 08:00:09:05:24:f6 |     | 65534 10 |
| ------- | ---------- | --- | --- | --- | ------ | ----------------- | --- | -------- |
| Command | History    |     |     |     |        |                   |     |          |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 145

| Release        |             |         |         |     | Modification |
| -------------- | ----------- | ------- | ------- | --- | ------------ |
| 10.07orearlier |             |         |         |     | --           |
| Command        | Information |         |         |     |              |
| Platforms      |             | Command | context |     | Authority    |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 8100 |     |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | --- | --- | ----------------------------------------------------- |
(#)
commandfromtheoperatorcontext(>)only.
8320
8325
8360
8400
9300
10000
| show | running-config |     |           | interface |     |
| ---- | -------------- | --- | --------- | --------- | --- |
| show | running-config |     | interface |           |     |
Description
Displaysallconfiguredinterfacecommands,includingVSXcommands.
Example
| switch#        |                | show running-config |                  | interface |                       |
| -------------- | -------------- | ------------------- | ---------------- | --------- | --------------------- |
| interface      |                | lag 100             | multi-chassis    |           |                       |
|                | no shutdown    |                     |                  |           |                       |
|                | no routing     |                     |                  |           |                       |
|                | lacp           | mode active         |                  |           |                       |
| interface      |                | 1/1/1               |                  |           |                       |
|                | no shutdown    |                     |                  |           |                       |
|                | no routing     |                     |                  |           |                       |
| interface      |                | 1/1/2               |                  |           |                       |
|                | no shutdown    |                     |                  |           |                       |
|                | lag            | 100                 |                  |           |                       |
| interface      |                | 1/1/3               |                  |           |                       |
|                | no shutdown    |                     |                  |           |                       |
|                | ip address     | 192.168.1.2/24      |                  |           |                       |
| interface      |                | vlan100             |                  |           |                       |
|                | no shutdown    |                     |                  |           |                       |
|                | ip address     | 192.168.1.1/24      |                  |           |                       |
|                | active-gateway |                     | ip 192.168.1.253 |           | mac 00:00:00:00:00:01 |
|                | active-gateway |                     | ipv6 fe80::01    |           | mac 00:00:00:01:00:01 |
| Command        | History        |                     |                  |           |                       |
| Release        |                |                     |                  |           | Modification          |
| 10.07orearlier |                |                     |                  |           | --                    |
| Command        | Information    |                     |                  |           |                       |
VSXcommands|146

| Platforms |     | Command | context |     |     | Authority                                            |     |
| --------- | --- | ------- | ------- | --- | --- | ---------------------------------------------------- | --- |
| 6400      |     |         |         |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |
Operator(>)orManager
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     |     |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | --- | --- | --- | ------------------------------------- | --- |
8325
8360
8400
9300
10000
| show | running-config |     |     | vsx |     |     |     |
| ---- | -------------- | --- | --- | --- | --- | --- | --- |
| show | running-config | vsx |     |     |     |     |     |
Description
DisplaystheconfiguredVSXcommands.
Example
|     | switch# | show running-config |     | vsx |     |     |     |
| --- | ------- | ------------------- | --- | --- | --- | --- | --- |
vsx
|     | system-mac        | 10:00:00:00:00:01        |                      |                   |        |             |     |
| --- | ----------------- | ------------------------ | -------------------- | ----------------- | ------ | ----------- | --- |
|     | inter-switch-link |                          | hello-interval       |                   |        | 2           |     |
|     | inter-switch-link |                          | dead-interval        |                   |        | 3           |     |
|     | inter-switch-link |                          | hold-time            |                   | 3      |             |     |
|     | inter-switch-link |                          | peer-detect-interval |                   |        |             | 300 |
|     | role              | primary                  |                      |                   |        |             |     |
|     | keepalive         | udp-port                 | 1500                 |                   |        |             |     |
|     | keepalive         | hello-interval           |                      |                   | 2      |             |     |
|     | keepalive         | dead-interval            |                      | 4                 |        |             |     |
|     | keepalive         | peer                     | 192.168.1.1          |                   | source | 192.168.1.2 |     |
|     | inter-switch-link |                          | 1/1/43               |                   |        |             |     |
|     | interface         | lag 100                  | multi-chassis        |                   |        |             |     |
|     | no shutdown       |                          |                      |                   |        |             |     |
|     | no routing        |                          |                      |                   |        |             |     |
|     | vlan              | access 1                 |                      |                   |        |             |     |
|     | lacp              | mode active              |                      |                   |        |             |     |
|     | interface         | 1/1/44                   |                      |                   |        |             |     |
|     | no shutdown       |                          |                      |                   |        |             |     |
|     | lag 100           |                          |                      |                   |        |             |     |
|     | interface         | vlan2                    |                      |                   |        |             |     |
|     | ip address        | 10.0.0.2/24              |                      |                   |        |             |     |
|     | vsx-sync          | active-gateways          |                      |                   |        |             |     |
|     | active-gateway    |                          | ip mac               | 00:aa:bb:dd:ee:ff |        |             |     |
|     | active-gateway    |                          | ip 10.0.0.1          |                   |        |             |     |
|     | ipv6              | address 2000:0:0:1::1/64 |                      |                   |        |             |     |
|     | ipv6              | address 3000:0:0:1::1/64 |                      |                   |        |             |     |
|     | active-gateway    |                          | ipv6 mac             | 00:aa:aa:aa:aa:ab |        |             |     |
|     | active-gateway    |                          | ipv6 2000:0:0:1::3   |                   |        |             |     |
|     | active-gateway    |                          | ipv6 3000:0:0:1::3   |                   |        |             |     |
|     | interface         | vlan3                    |                      |                   |        |             |     |
|     | ipv6              | address link-local       |                      | fe80::100/64      |        |             |     |
|     | active-gateway    |                          | ip mac               | 00:aa:bb:dd:ee:ff |        |             |     |
|     | active-gateway    |                          | ip 10.0.0.1          |                   |        |             |     |
|     | active-gateway    |                          | ipv6 mac             | 00:aa:aa:aa:aa:ab |        |             |     |
|     | active-gateway    |                          | ipv6 fe80::100       |                   |        |             |     |
|     | interface         | vlan4                    |                      |                   |        |             |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 147

| active-gateway        |       | ip mac 00:aa:bb:dd:ee:ff |              |
| --------------------- | ----- | ------------------------ | ------------ |
| active-gateway        |       | ip 10.0.0.1              |              |
| interface             | vlan5 |                          |              |
| vsx active-forwarding |       |                          |              |
| Command History       |       |                          |              |
| Release               |       |                          | Modification |
10.09.0010 Commandwillnowdisplayresultsforconfigurationswherethe
activegatewayandSVIsharethesameIPv6address.
| 10.07orearlier      |         |         | --        |
| ------------------- | ------- | ------- | --------- |
| Command Information |         |         |           |
| Platforms           | Command | context | Authority |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 8100 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | ----------------------------------------------------- |
(#)
commandfromtheoperatorcontext(>)only.
8320
8325
8360
8400
9300
10000
| show running-config |          | vsx-sync |     |
| ------------------- | -------- | -------- | --- |
| show running-config | vsx-sync |          |     |
Description
Displaysthelinesofrunning-configurationthatVSXconfigurationsynchronizationisenabledon.The
commandalsoprovidesarolled-upviewofconfigurationexpectedtobesynced.Thiscommandcanbe
runfromtheprimaryorsecondarypeer.
Example
DisplayingtherunningconfigurationonwhichVSXsynchronizationisenabled:
| switch# | show running-config     | vsx-sync |     |
| ------- | ----------------------- | -------- | --- |
| Current | vsx-sync configuration: |          |     |
vlan 3
vsx-sync
| access-list | ip test1 |     |     |
| ----------- | -------- | --- | --- |
vsx-sync
!
| policy test2 |     |     |     |
| ------------ | --- | --- | --- |
vsx-sync
!
| Command History |     |     |     |
| --------------- | --- | --- | --- |
VSXcommands|148

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 8100 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | ----------------------------------------------------- |
(#)
commandfromtheoperatorcontext(>)only.
8320
8325
8360
8400
9300
10000
| show running-config |          | vsx-sync  | peer-diff |
| ------------------- | -------- | --------- | --------- |
| show running-config | vsx-sync | peer-diff |           |
Description
DisplaysthedifferencebetweentheconfigurationoffeaturesenabledforVSXsynchronizationonthe
primaryandsecondaryswitches.
Usage
Usethiscommandfordiagnosingerrors.Thiscommandprovidesvisibilityintowhichconfigurationlines
didnotsynchronizefromtheprimarypeertothesecondarypeer.Thiscommandcanberunfromthe
primaryorsecondarypeer.TheoutputisdisplayedintheGNUdiffunifiedformat.
Example
DisplayingtherunningconfigurationonwhichVSXsynchronizationisenabled:
| switch# | show running-config | vsx-sync | peer-diff |
| ------- | ------------------- | -------- | --------- |
--- /tmp/running-config-vsx.83e 2018-05-01 17:03:38.083281976 +0000
+++ /tmp/peer-running-config-vsx.83e 2018-05-01 17:03:38.077281976 +0000
| @@ -1,4             | +0,0 @@    |         |              |
| ------------------- | ---------- | ------- | ------------ |
| -access-list        | ip sync    |         |              |
| - vsx-sync          |            |         |              |
| - !                 |            |         |              |
| - 10                | permit any | any any |              |
| Command History     |            |         |              |
| Release             |            |         | Modification |
| 10.07orearlier      |            |         | --           |
| Command Information |            |         |              |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 149

| Platforms | Command | context | Authority                                            |
| --------- | ------- | ------- | ---------------------------------------------------- |
| 6400      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
8325
8360
8400
9300
10000
| show        | system l2-vlan-mac-mode |            |     |
| ----------- | ----------------------- | ---------- | --- |
| show system | l2-vlan-mac-mode        | [vsx-peer] |     |
Description
ThiscommanddisplaystheL2VLANMACModeconfigurationandstatus.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
FollowingexampleshowsL2VLANMACModeconfiguration.
| switch#        | show system | l2-vlan-mac-mode |                                 |
| -------------- | ----------- | ---------------- | ------------------------------- |
| Configured     | L2 VLAN     | MAC mode: flood  |                                 |
| Operational    | L2 VLAN     | MAC mode: flood  |                                 |
| Command        | History     |                  |                                 |
| Release        |             |                  | Modification                    |
| 10.09          |             |                  | Commandsupportedfor10000switch. |
| 10.07orearlier |             |                  | --                              |
| Command        | Information |                  |                                 |
| Platforms      | Command     | context          | Authority                       |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
8325
10000
| show | vsx active-forwarding |     |     |
| ---- | --------------------- | --- | --- |
VSXcommands|150

show vsx active-forwarding [interface <INTERFACE-VLAN>] [vsx-peer]
Description
ShowsalltheVSXactive-forwardingconfiguredinterfaceVLANsortheVSXactive-forwardingpeer
informationforaparticularinterfaceVLAN.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
interface <INTERFACE-VLAN> SpecifiestheinterfaceVLANname.Syntax:string
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingalistofVSXactive-forwardingenabledinterfaces:
| switch# | show vsx active-forwarding |     |                     |     |
| ------- | -------------------------- | --- | ------------------- | --- |
| List of | VSX active-forwarding      |     | enabled interfaces: |     |
vlan30
vlan32
vlan33
DisplayingtheVSXactive-forwardingpeerinformationforvlan30:
| switch#   | show vsx active-forwarding |                       | interface | vlan30   |
| --------- | -------------------------- | --------------------- | --------- | -------- |
| Interface | vlan30 has                 | VSX active-forwarding |           | enabled. |
| Interface | vlan30 Peer                | Data:                 |           |          |
| Peer MAC: | 94:f1:28:21:22:00          |                       |           |          |
| Peer IPv6 | Addresses:                 |                       |           |          |
fe80::96f1:28ff:fe21:2200
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | ------------------------------------- | --- |
8325
8360
8400
9300
10000
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 151

| show vsx       | brief      |     |     |
| -------------- | ---------- | --- | --- |
| show vsx brief | [vsx-peer] |     |     |
Description
DisplaysthebriefVSXstatus.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Theshow vsx briefcommanddisplaystheISLPdeviceprotocolstatesunderthe"DeviceState"
heading.
Table1:ISLPdeviceprotocolstates
Device
Definition
state
| Peer- | TheVSXswitchisinasteadystate.VSXLAGsareup. |     |     |
| ----- | ------------------------------------------ | --- | --- |
Established
Sync-Primary ISLconnectivitytothepeerVSXswitchisrestored,andtheVSXswitchissyncingstatestothe
peerVSXswitch.VSXLAGsareup.
Sync- ISLconnectivitytothepeerVSXswitchisrestored,andtheVSXswitchislearningstatesfrom
| Secondary | thepeerVSXswitch.VSXLAGsaredown. |     |     |
| --------- | -------------------------------- | --- | --- |
Sync- TheVSXswitchhaslearneditsstatesfromthepeerVSXswitch,andtheVSXswitchis
Secondary- monitoringforhardwaretobeprogrammed.VSXLAGsaredown.
Linkup-Delay
Split-System- TheVSXswitchhaslostISLconnectivitytothepeerVSXswitch.TheVSXswitchisoperatingas
| Primary | theprimaryVSXswitch.VSXLAGsareup. |     |     |
| ------- | --------------------------------- | --- | --- |
Split-System- TheVSXswitchhaslostISLconnectivitytothepeerVSXswitch.TheVSXswitchisoperatingas
| Secondary | thesecondaryVSXswitch.VSXLAGsaredown. |     |     |
| --------- | ------------------------------------- | --- | --- |
Waiting-For- TheVSXswitchiswaitingforconnectivitytothepeerVSXswitch.
Peer
Example
DisplayingthebriefVSXstatusfortheswitchyouareloggedinto:
| vsx-primary# | show vsx         | brief          |                         |
| ------------ | ---------------- | -------------- | ----------------------- |
| ISL State    |                  |                | : In-Sync               |
| Device       | State            |                | : Peer-Established      |
| Keepalive    | State            |                | : Keepalive-Established |
| Device       | Role             |                | : primary               |
| Number       | of Multi-chassis | LAG interfaces | : 2                     |
VSXcommands|152

DisplayingthebriefVSXstatusforthepeer(secondary)switchwhileenteringthecommandonthe
primaryswitch:
| vsx-primary# |                  | show | vsx brief | vsx-peer   |     |                         |
| ------------ | ---------------- | ---- | --------- | ---------- | --- | ----------------------- |
| ISL State    |                  |      |           |            |     | : In-Sync               |
| Device       | State            |      |           |            |     | : Peer-Established      |
| Keepalive    | State            |      |           |            |     | : Keepalive-Established |
| Device       | Role             |      |           |            |     | : secondary             |
| Number       | of Multi-chassis |      | LAG       | interfaces |     | : 2                     |
DisplayingthebriefVSXstatusforthepeer(primary)switchwhileenteringthecommandonthe
secondaryswitch:
| vsx-secondary# |                  | show    | vsx brief | vsx-peer   |              |                         |
| -------------- | ---------------- | ------- | --------- | ---------- | ------------ | ----------------------- |
| ISL State      |                  |         |           |            |              | : In-Sync               |
| Device         | State            |         |           |            |              | : Peer-Established      |
| Keepalive      | State            |         |           |            |              | : Keepalive-Established |
| Device         | Role             |         |           |            |              | : primary               |
| Number         | of Multi-chassis |         | LAG       | interfaces |              | : 2                     |
| Command        | History          |         |           |            |              |                         |
| Release        |                  |         |           |            | Modification |                         |
| 10.07orearlier |                  |         |           |            | --           |                         |
| Command        | Information      |         |           |            |              |                         |
| Platforms      |                  | Command | context   |            | Authority    |                         |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
| 8100 |     | (#) |     |     |                                       |     |
| ---- | --- | --- | --- | --- | ------------------------------------- | --- |
| 8320 |     |     |     |     | commandfromtheoperatorcontext(>)only. |     |
8325
8360
8400
9300
10000
| show vsx                    | config-consistency |     |     |            |     |     |
| --------------------------- | ------------------ | --- | --- | ---------- | --- | --- |
| show vsx config-consistency |                    |     |     | [vsx-peer] |     |     |
Description
DisplaystheVSXglobalconfigurationconsistencybetweentwoVSXswitches.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 153

Example
ThefollowingexampleshowsacomparisonbetweenthetwoVSXswitches.
switch#
show vsx config-consistency
| Configurations     |                 |     | Local             | Peer   |
| ------------------ | --------------- | --- | ----------------- | ------ |
| ------------------ |                 |     | ------            | ------ |
| software           | version         |     | 0.1.0             | 0.1.0  |
| ISL hello          | interval        |     | 1                 | 1      |
| ISL dead           | interval        |     | 5                 | 5      |
| ISL hold           | interval        |     | 0                 | 0      |
| ISL peer           | detect interval |     | 300               | 300    |
| Keepalive          | hello interval  |     | 1                 | 1      |
| Keepalive          | dead interval   |     | 3                 | 3      |
| Keepalive          | UDP port        |     | 7678              | 7678   |
| System             | MAC             |     | 10:00:00:00:00:01 |        |
10:00:00:00:00:01
| VSX VLAN | List |     |     |     |
| -------- | ---- | --- | --- | --- |
-------------
| Local ISL  | VLANs :    | 1,100 |     |     |
| ---------- | ---------- | ----- | --- | --- |
| Peer ISL   | VLANs :    | 1,10  |     |     |
| VSX Active | Forwarding |       |     |     |
---------------------
| Interface          | VLANs | : 2, 5-9  |            |        |
| ------------------ | ----- | --------- | ---------- | ------ |
| Peer Interface     | VLANs | : 2, 5-10 |            |        |
| STP Configurations |       |           | Local      | Peer   |
| ------------------ |       |           | ------     | ------ |
| STP Enabled        |       |           | True       | True   |
| STP Mode           |       |           | rpvst-auto | rpvst- |
auto
| MST Config | Name |     | 10:00:00:00:00:01 |     |
| ---------- | ---- | --- | ----------------- | --- |
10:00:00:00:00:01
| MST Config  | Revision     |          | 0   | 0   |
| ----------- | ------------ | -------- | --- | --- |
| MST Config  | Digest       |          | -   | -   |
| MST hello   | time(in      | seconds) | 2   | 2   |
| MST maximum | age(in       | seconds) | 20  | 20  |
| MST maximum | hops         |          | 20  | 20  |
| MST number  | of instances |          | -   | -   |
| RPVST VLAN  | List:        |          |     |     |
----------------
Local: 2,5-9
Peer : 2,5-9
```
| Command        | History     |              |     |     |
| -------------- | ----------- | ------------ | --- | --- |
| Release        |             | Modification |     |     |
| 10.07orearlier |             | --           |     |     |
| Command        | Information |              |     |     |
VSXcommands|154

| Platforms | Command | context | Authority                                            |     |
| --------- | ------- | ------- | ---------------------------------------------------- | --- |
| 6400      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |
Operator(>)orManager
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | ------------------------------------- | --- |
8325
8360
8400
9300
10000
| show vsx                    | config-consistency |                   | lacp       |     |
| --------------------------- | ------------------ | ----------------- | ---------- | --- |
| show vsx config-consistency |                    | lacp [<LAG-NAME>] | [vsx-peer] |     |
Description
DisplaysVSXLACPconfigurationconsistencybetweentwoVSXswitches.
| Parameter  |     |     | Description                                |     |
| ---------- | --- | --- | ------------------------------------------ | --- |
| <LAG-NAME> |     |     | SpecifiestheLAGname.Optional.Syntax:string |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch#            | show vsx config-consistency |     | lacp            |                 |
| ------------------ | --------------------------- | --- | --------------- | --------------- |
| Configurations     |                             |     | Local           | Peer            |
| ------------------ |                             |     | ------          | ------          |
| Name               |                             |     | lag100          | lag100          |
| Loop protect       | enabled                     |     | false           | true            |
| Hash scheme        |                             |     | l2-src-dst-hash | l2-src-dst-hash |
| Qos cos            | override                    |     | 0               | 0               |
| Qos dscp           | override                    |     | 0               | 0               |
| Qos trust          |                             |     |                 |                 |
| VSX VLAN           | list                        |     |                 |                 |
1
| Peer VSX | VLAN list |     |     |     |
| -------- | --------- | --- | --- | --- |
1,10
| STP link-type      |         |     | point-to-point | point-to-point |
| ------------------ | ------- | --- | -------------- | -------------- |
| STP port-type      |         |     | admin-network  | admin-network  |
| STP bpdu-filter    |         |     | Disabled       | Disabled       |
| STP bpdu-guard     |         |     | Disabled       | Disabled       |
| STP loop-guard     |         |     | Disabled       | Disabled       |
| STP root-guard     |         |     | Disabled       | Disabled       |
| STP tcn-guard      |         |     | Disabled       | Disabled       |
| Configurations     |         |     | Local          | Peer           |
| ------------------ |         |     | ------         | ------         |
| Name               |         |     | lag111         | lag111         |
| Loop protect       | enabled |     | false          | false          |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 155

| Hash scheme |          |     |     | l2-src-dst-hash |     | l2-src-dst-hash |
| ----------- | -------- | --- | --- | --------------- | --- | --------------- |
| Qos cos     | override |     |     | 0               |     | 0               |
| Qos dscp    | override |     |     | 0               |     | 0               |
Qos trust
| VSX VLAN | list |     |     |     |     |     |
| -------- | ---- | --- | --- | --- | --- | --- |
1
| Peer VSX | VLAN list |     |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- | --- |
1
| STP link-type   |     |     |     | point-to-point |     | point-to-point |
| --------------- | --- | --- | --- | -------------- | --- | -------------- |
| STP port-type   |     |     |     | admin-network  |     | admin-network  |
| STP bpdu-filter |     |     |     | Disabled       |     | Disabled       |
| STP bpdu-guard  |     |     |     | Disabled       |     | Disabled       |
| STP loop-guard  |     |     |     | Disabled       |     | Disabled       |
| STP root-guard  |     |     |     | Disabled       |     | Disabled       |
| STP tcn-guard   |     |     |     | Disabled       |     | Disabled       |
------------------------------------------------------
switch (config-if-vlan)# show traffic-insight test monitor-type dns-average-
| latency | mon2 |     |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- |
error-statistics
| Name |     |     | :   | mntr2               |     |     |
| ---- | --- | --- | --- | ------------------- | --- | --- |
| Type |     |     | :   | dns-average-latency |     |     |
Start time for error monitoring : 10/10/2022 04:12:13.923691 UTC
End time for error monitoring : 10/10/2022 04:17:13.964505 UTC
client_mac dns_server_ip number_of_ dns_name dns_server_ dns_
format_
|     |     |     | dns_failures |     | _errors | failures |
| --- | --- | --- | ------------ | --- | ------- | -------- |
errors
----------------------------------------------------------------------------------
------
| aa:aa:aa:aa:aa:aa |     | 172.0.0.1 |     | 200 | 50  | 100 |
| ----------------- | --- | --------- | --- | --- | --- | --- |
50
| bb:bb:bb:bb:bb:bb |     | 172.1.1.1 |     | 50  | 10  | 20  |
| ----------------- | --- | --------- | --- | --- | --- | --- |
20
| cc:cc:cc:cc:cc:cc |     | 172.2.2.2 |     | 150 | 75  | 25  |
| ----------------- | --- | --------- | --- | --- | --- | --- |
50
| Command History     |         |         |              |     |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- | --- |
| Release             |         |         | Modification |     |     |     |
| 10.07orearlier      |         |         | --           |     |     |     |
| Command Information |         |         |              |     |     |     |
| Platforms           | Command | context | Authority    |     |     |     |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
| 8100 | (#) |     |                                       |     |     |     |
| ---- | --- | --- | ------------------------------------- | --- | --- | --- |
| 8320 |     |     | commandfromtheoperatorcontext(>)only. |     |     |     |
8325
8360
8400
9300
10000
VSXcommands|156

| show vsx | configuration |     |
| -------- | ------------- | --- |
show vsx configuration {inter-switch-link | keepalive} [vsx-peer]
Description
DisplaystheISLconfigurationorkeepaliveprotocolconfigurationinVSX.
Parameter Description
{inter-switch-link | keepalive} Selectsinter-switch-linkorkeepalive.
inter-switch-link DisplaystheISLconfigurationinVSX.
keepalive DisplaysthekeepaliveprotocolconfigurationinVSX.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingtheISLconfigurationinVSX:
| switch#        | show vsx configuration | inter-switch-link   |
| -------------- | ---------------------- | ------------------- |
| Inter Switch   | Link                   | : 1/1/43            |
| Hello Interval |                        | : 1 Seconds         |
| Dead Interval  |                        | : 20 Seconds        |
| Hold Time      |                        | : 0 Seconds         |
| Peer detect    | interval               | : 300 Seconds       |
| System         | MAC                    | : 10:00:00:00:00:01 |
| Device         | Role                   | : primary           |
| Multichassis   | LAGs                   | : lag100            |
DisplayingthekeepaliveprotocolconfigurationinVSX:
| switch#        | show vsx configuration | keepalive     |
| -------------- | ---------------------- | ------------- |
| Keepalive      | Interface              | : 1/1/1       |
| Keepalive      | VRF                    | : test1       |
| Source         | IP Address             | : 192.168.1.1 |
| Peer IP        | Address                | : 192.168.1.2 |
| UDP Port       |                        | : 7678        |
| Hello Interval |                        | : 1 Seconds   |
| Dead Interval  |                        | : 3 Seconds   |
| Command        | History                |               |
Release Modification
10.07orearlier --
| Command | Information |     |
| ------- | ----------- | --- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 157

| Platforms | Command | context | Authority                                            |
| --------- | ------- | ------- | ---------------------------------------------------- |
| 6400      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
8325
8360
8400
9300
10000
| show vsx               | configuration |                | split-recovery |
| ---------------------- | ------------- | -------------- | -------------- |
| show vsx configuration |               | split-recovery | [vsx-peer]     |
Description
Displaysthestateofthesplitrecoverymode.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch#        | show vsx    | configuration | split-recovery |
| -------------- | ----------- | ------------- | -------------- |
| Split Recovery | Mode        | : Enabled     |                |
| Command        | History     |               |                |
| Release        |             |               | Modification   |
| 10.07orearlier |             |               | --             |
| Command        | Information |               |                |
| Platforms      | Command     | context       | Authority      |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 8100 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | ----------------------------------------------------- |
(#)
commandfromtheoperatorcontext(>)only.
8320
8325
8360
8400
9300
10000
| show vsx | ip data-path |     |     |
| -------- | ------------ | --- | --- |
show vsx ip data-path [<IP-ADDR> | <IP-ADDR>/<MASK>] [vrf <VRF-NAME>] [vsx-peer]
VSXcommands|158

Description
DisplaysthedatapathoftheIPv4routepresentonlocalandVSXpeerdevices.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<IP-ADDR> | <IP-ADDR>/<MASK>] Selectsoneofthefollowing:<IP-ADDR>or<IP-ADDR>/<MASK>
| <IP-ADDR> |     |     |     | SpecifiesthedatapathforanIPv4addressbasedonthe |
| --------- | --- | --- | --- | ---------------------------------------------- |
parametersprovided.
<IP-ADDR>/<MASK> SpecifiesthedatapathforanIPv4addressanditsspecified
subnet.Optional.Syntax:A.B.C.D/M
| vrf <VRF-NAME> |     |     |     | ShowstheIPv4datapathforaspecifiedVRF. |
| -------------- | --- | --- | --- | ------------------------------------- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
DisplayingthedatapathonaVSXswitchfor192.0.2.0:
| switch#   | show | vsx ip data-path |     | 192.0.2.0     |
| --------- | ---- | ---------------- | --- | ------------- |
| IPv4 Data | Path | Information      |     | For 192.0.2.0 |
Local Device
------------
| Route : | 192.0.2.0/32 |             |         |                     |
| ------- | ------------ | ----------- | ------- | ------------------- |
| Egress  | L3           | Interface   | : 1/1/2 |                     |
| Next    | Hop          | MAC Address |         | : 08:00:09:ea:d7:d1 |
| Egress  | Port         | : 1/1/2     |         |                     |
| Egress  | L3           | Interface   | : 1/1/3 |                     |
| Nexthop | Hop          | MAC Address |         | : 08:00:09:8e:59:1d |
| Egress  | Port         | : 1/1/3     |         |                     |
Peer Device
------------
| Route : | 192.0.2.0/32 |           |             |     |
| ------- | ------------ | --------- | ----------- | --- |
| Egress  | L3           | Interface | : loopback1 |     |
DisplayingthedatapathonaVSXswitchfor198.51.100.0/32:
| switch#   | show | vsx ip data-path |     | 198.51.100.0/32     |
| --------- | ---- | ---------------- | --- | ------------------- |
| IPv4 Data | Path | Information      |     | For 198.51.100.0/32 |
Local Device
------------
| Route : | 198.51.100.0/32 |           |         |     |
| ------- | --------------- | --------- | ------- | --- |
| Egress  | L3              | Interface | : 1/1/4 |     |
DisplayingthedatapathsonaVSXswitchfor198.51.100.1:
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 159

switch# show vsx ip data-path 198.51.100.1

IPv4 Data Path Information For 198.51.100.1

Local Device
------------
Route : 198.51.100.1/32

Egress L3 Interface : 1/1/4

Peer Device
------------
Route : 198.51.100.0/24

Egress L3 Interface : 1/1/2
Next Hop MAC Address
Egress Port

: 1/1/2

: 08:00:09:db:21:e8

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

Operator (>) or Manager
(#)

Administrators or local user group members with execution rights
for this command.

6400
8100
8320
8325
8360
8400
9300
10000

show vsx ip route
show vsx ip route [<IP-ADDR> | <IP-ADDR>/<MASK> | unique] [vrf <VRF-NAME> | all-vrfs]
[vsx-peer]

Description

Displays a specified LAG or all configured LAGs along with VSX LAGs.

Parameter

Description

<IP-ADDR> | <IP-ADDR>/<MASK> | unique]

<IP-ADDR>

<IP-ADDR>/<MASK>

Selects one of the following: <IP-ADDR>, <IP-
ADDR>/<MASK> , or unique

Specifies the route information for an IPv4 address
based on the parameters provided.

Specifies the route information for an IPv4 address and
its specified subnet. Optional. Syntax: A.B.C.D/M

VSX commands | 160

| Parameter |     |     |     | Description                                   |
| --------- | --- | --- | --- | --------------------------------------------- |
| unique    |     |     |     | Specifiesroutesthatarepresentonlyontheprimary |
switchoronlyonthesecondaryswitch.Theroutesthat
arepresentonboththeprimaryandsecondaryswitch
areexcluded.Optional.Syntaxstring.
| vrf <VRF-NAME> | | all-vrfs |     |     | SelectstheVRFnameorallVRFs.                   |
| -------------- | ---------- | --- | --- | --------------------------------------------- |
| <VRF-NAME>     |            |     |     | ShowstheIPv4routeinformationforaspecifiedVRF. |
| all-vrf        |            |     |     | ShowstheIPv4routeinformationforallVRFs.       |
| vsx-peer       |            |     |     | ShowstheoutputfromtheVSXpeerswitch.Ifthe      |
switchesdonothavetheVSXconfigurationortheISLis
down,theoutputfromtheVSXpeerswitchisnot
displayed.Thisparameterisavailableonswitchesthat
supportVSX.
Examples
DisplayingIPv4routesonaVSXswitch:
| switch# show    | vsx ip            | route   |           |      |
| --------------- | ----------------- | ------- | --------- | ---- |
| IPv4 Forwarding | Routes            |         |           |      |
| '[x/y]' denotes | [distance/metric] |         |           |      |
| 192.0.2.0/32,   | vrf               | default |           |      |
| via 192.0.2.1,  |                   | [1/0],  | static on | vsx1 |
| via 192.0.2.2,  |                   | [1/0],  | static on | vsx2 |
DisplayingIPv4routesonaVSXswitch:
| switch# show    | vsx ip            | route     |          |      |
| --------------- | ----------------- | --------- | -------- | ---- |
| IPv4 Forwarding | Routes            |           |          |      |
| '[x/y]' denotes | [distance/metric] |           |          |      |
| 192.0.2.3/24,   | vrf               | default   |          |      |
| via 1/1/3,      | [0/0],            | connected | on       | vsx1 |
| via 192.0.2.2,  |                   | [110/2],  | ospf on  | vsx2 |
| 192.0.2.4/32,   | vrf               | default   |          |      |
| via 1/1/3,      | [0/0],            | local     | on vsx1  |      |
| 192.0.2.5/24,   | vrf               | default   |          |      |
| via 1/1/4,      | [0/0],            | connected | on       | vsx1 |
| via 192.0.2.2,  |                   | [110/3],  | ospf on  | vsx2 |
| 192.0.2.6/32,   | vrf               | default   |          |      |
| via 1/1/4,      | [0/0],            | local     | on vsx1  |      |
| 192.0.2.7/32,   | vrf               | default   |          |      |
| via 192.0.2.8,  |                   | [110/1],  | ospf on  | vsx1 |
| via 192.0.2.1,  |                   | [110/1],  | ospf on  | vsx1 |
| via loopback1,  |                   | [0/0],    | local on | vsx2 |
DisplayingIPv4uniqueroutesonaVSXswitch:
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 161

| switch#         | show vsx ip               | route unique  |         |
| --------------- | ------------------------- | ------------- | ------- |
| IPv4 Forwarding | Routes                    |               |         |
| '[x/y]'         | denotes [distance/metric] |               |         |
| 192.0.2.0/32,   | vrf                       | default       |         |
| via             | 192.0.2.2,                | [1/0], static | on vsx2 |
| 192.0.2.9/32,   | vrf                       | default       |         |
| via             | 192.0.2.1,                | [1/0], static | on vsx1 |
DisplayingIPv4routesonaVSXswitchfor192.0.2.10:
| switch#             | show vsx ip               | route 192.0.2.10 |              |
| ------------------- | ------------------------- | ---------------- | ------------ |
| IPv4 Forwarding     | Routes                    |                  |              |
| '[x/y]'             | denotes [distance/metric] |                  |              |
| 192.0.2.10/32,      | vrf                       | default          |              |
| via                 | 192.0.2.1,                | [1/0], static    | on vsx1      |
| via                 | 192.0.2.2,                | [1/0], static    | on vsx2      |
| Command History     |                           |                  |              |
| Release             |                           |                  | Modification |
| 10.07orearlier      |                           |                  | --           |
| Command Information |                           |                  |              |
| Platforms           | Command                   | context          | Authority    |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 8100 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | ----------------------------------------------------- |
(#)
commandfromtheoperatorcontext(>)only.
8320
8325
8360
8400
9300
10000
| show vsx | ipv6 | data-path |     |
| -------- | ---- | --------- | --- |
show vsx ipv6 data-path [<IPv6-ADDR> | <IPv6-ADDR>/<MASK>] [vrf <VRF-NAME>] [vsx-peer]
Description
DisplaysthedatapathoftheIPv6routeonlocalandpeerVSXdevices.
| Parameter   |                       |     | Description |
| ----------- | --------------------- | --- | ----------- |
| <IPV6-ADDR> | | <IPV6-ADDR>/<MASK>] |     |             |
Selectsoneofthefollowing:<IPV6-ADDR>or<IPV6-
VSXcommands|162

| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
ADDR>/<MASK>
| <IPV6-ADDR> |     |     |     | SpecifiesthedatapathforanIPv6addressbasedonthe |
| ----------- | --- | --- | --- | ---------------------------------------------- |
parametersprovided.
<IPV6-ADDR>/<MASK> SpecifiesthedatapathforanIPv6addressanditsspecified
subnet.Optional.Syntax:A.B.C.D/M
| vrf <VRF-NAME> |     |     |     | ShowstheIPv6datapathforaspecifiedVRF.              |
| -------------- | --- | --- | --- | -------------------------------------------------- |
| vsx-peer       |     |     |     | ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdo |
nothavetheVSXconfigurationortheISLisdown,theoutput
fromtheVSXpeerswitchisnotdisplayed.Thisparameteris
availableonswitchesthatsupportVSX.
Examples
DisplayinganIPv6datapathonaVSXswitch:
| switch#   | show vsx | ipv6        | data-path | 1000:: |
| --------- | -------- | ----------- | --------- | ------ |
| IPv6 Data | Path     | Information | For       | 1000:: |
Local Device
------------
| Route : | 1000::/64 |           |         |     |
| ------- | --------- | --------- | ------- | --- |
| Egress  | L3        | Interface | : 1/1/2 |     |
Peer Device
------------
| Route : | 1000::/64 |           |         |     |
| ------- | --------- | --------- | ------- | --- |
| Egress  | L3        | Interface | : 1/1/2 |     |
DisplayinganIPv6datapathonaVSXswitch:
| switch#   | show vsx | ipv6        | data-path | 2000:: |
| --------- | -------- | ----------- | --------- | ------ |
| IPv6 Data | Path     | Information | For       | 2000:: |
Local Device
------------
| Route : | 2000::/64 |           |         |                   |
| ------- | --------- | --------- | ------- | ----------------- |
| Egress  | L3        | Interface | : 1/1/2 |                   |
| Next    | Hop MAC   | Address   | :       | 08:00:09:0e:0c:1b |
| Egress  | Port      | : 1/1/2   |         |                   |
DisplayingIPv6datapathfor3000::/64onaVSXswitch:
| switch#   | show vsx | ipv6        | data-path | 3000::/64 |
| --------- | -------- | ----------- | --------- | --------- |
| IPv6 Data | Path     | Information | For       | 3000::/64 |
Local Device
------------
| Route : | 3000::/64 |           |         |                   |
| ------- | --------- | --------- | ------- | ----------------- |
| Egress  | L3        | Interface | : 1/1/2 |                   |
| Next    | Hop MAC   | Address   | :       | 08:00:09:0e:0c:1b |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 163

Egress Port

: 1/1/2

IPv6 Data Path Information For 3000::/64

Local Device
------------
Route : 3000::/64

Egress L3 Interface : 1/1/2
Next Hop MAC Address
Egress Port

: 1/1/2

: 08:00:09:0e:0c:1b

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

6400
8100
8320
8325
8360
8400
9300
10000

show vsx ipv6 route
show vsx ipv6 route [<IPv6-ADDR> | <IPv6-ADDR>/<MASK> | unique]

[vrf <VRF-NAME> | all-vrfs] [vsx-peer]

Description

Displays a specified LAG or all configured LAGs along with VSX LAGs.

Parameter

Description

<IPV6-ADDR> | <IPV6-ADDR>/<MASK> | unique]

<IPV6-ADDR>

<IPV6-ADDR>/<MASK>

unique

Selects one of the following: <IPV6-ADDR>, <IPV6-
ADDR>/<MASK> , or unique

Specifies the route information for an IPv4 address
based on the parameters provided.

Specifies the route information for an IPv4 address
and its specified subnet. Optional. Syntax:
A.B.C.D/M

Specifies routes that are present only on the
primary switch or only on the secondary switch. The
routes that are present on both the primary and
secondary switch are excluded. Optional. Syntax
string.

VSX commands | 164

| Parameter      |            |     | Description                               |
| -------------- | ---------- | --- | ----------------------------------------- |
| vrf <VRF-NAME> | | all-vrfs |     | SelectstheVRFnameorallVRFs.               |
| <VRF-NAME>     |            |     | ShowstheIPv4routeinformationforaspecified |
VRF.
all-vrf
ShowstheIPv4routeinformationforallVRFs.
| vsx-peer |     |     | ShowstheoutputfromtheVSXpeerswitch.Ifthe |
| -------- | --- | --- | ---------------------------------------- |
switchesdonothavetheVSXconfigurationorthe
ISLisdown,theoutputfromtheVSXpeerswitchis
notdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingIPv6routesonaVSXswitch:
| switch# show    | vsx ipv6 route    |                   |     |
| --------------- | ----------------- | ----------------- | --- |
| IPv6 Forwarding | Routes            |                   |     |
| '[x/y]' denotes | [distance/metric] |                   |     |
| 1000::/64,      | vrf default       |                   |     |
| via 1/1/2,      | [0/0],            | connected on vsx1 |     |
| via 1/1/2,      | [0/0],            | connected on vsx2 |     |
| 1000::1/128,    | vrf default       |                   |     |
| via 1/1/2,      | [0/0],            | local on vsx1     |     |
DisplayingIPv6uniqueroutesonaVSXswitch:
| switch# show    | vsx ipv6 route    | unique         |     |
| --------------- | ----------------- | -------------- | --- |
| IPv6 Forwarding | Routes            |                |     |
| '[x/y]' denotes | [distance/metric] |                |     |
| 1000::1/128,    | vrf default       |                |     |
| via 1/1/2,      | [0/0],            | local on vsx1  |     |
| 1000::2/128,    | vrf default       |                |     |
| via 1/1/2,      | [0/0],            | local on vsx2  |     |
| 3000::/64,      | vrf default       |                |     |
| via 1000::2,    | [1/0],            | static on vsx1 |     |
DisplayingIPv6routesonaVSXswitchfor2000::/64:
| switch# show    | vsx ipv6 route    | 2000::/64      |     |
| --------------- | ----------------- | -------------- | --- |
| IPv6 Forwarding | Routes            |                |     |
| '[x/y]' denotes | [distance/metric] |                |     |
| 2000::/64,      | vrf default       |                |     |
| via 1000::2,    | [1/0],            | static on vsx1 |     |
| via 1000::1,    | [1/0],            | static on vsx2 |     |
| Command History |                   |                |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 165

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

6400
8100
8320
8325
8360
8400
9300
10000

show vsx status
show vsx status [inter-switch-link | keepalive | linkup-delay] [vsx-peer]

Description

Displays global VSX status or a specified status determined by the selected parameter.

Parameter

Description

[inter-switch-link | keepalive | linkup-delay]

inter-switch-link

keepalive

linkup-delay

vsx-peer

Examples

Selects one of the following: inter-switch-
link, keepalive, or linkup-delay

Specifies the display of the ISL status in VSX.

Specifies the display of the VSX keepalive
protocol status.

Specifies the display of the VSX link-up delay
information, such as the:

n Configured link-up delay timer.
n Delay timer status.
n Initial sync status.
n LAGs on which the delay timer is running.
n Status of the LAGs excluded from the link-

up delay timer.

n Interfaces that are shut down during VSX

split.

n Interfaces that are shut down during VSX

split

Shows the output from the VSX peer switch. If
the switches do not have the VSX configuration
or the ISL is down, the output from the VSX
peer switch is not displayed. This parameter is
available on switches that support VSX.

VSX commands | 166

DisplayingtheglobalVSXstatus:
| switch#         | show vsx | status |     |     |
| --------------- | -------- | ------ | --- | --- |
| VSX Operational | State    |        |     |     |
---------------------
| ISL channel  |             | : In-Sync         |     |                   |
| ------------ | ----------- | ----------------- | --- | ----------------- |
| ISL mgmt     | channel     | : operational     |     |                   |
| Config       | Sync Status | : in-sync         |     |                   |
| NAE          |             | : peer_reachable  |     |                   |
| HTTPS        | Server      | : peer_reachable  |     |                   |
| Attribute    |             | Local             |     | Peer              |
| ------------ |             | --------          |     | --------          |
| ISL link     |             | 1/1/43            |     | 1/1/43            |
| ISL version  |             | 2                 |     | 2                 |
| System       | MAC         | 48:0f:cf:af:70:84 |     | 48:0f:cf:af:c2:84 |
| Platform     |             | 8320              |     | 8320              |
| Software     | Version     | 10.0x.xxxx        |     | 10.0x.xxxx        |
| Device       | Role        | primary           |     | secondary         |
DisplayingtheISLstatusinVSX:
| switch#      | show vsx | status inter-switch-link |     |     |
| ------------ | -------- | ------------------------ | --- | --- |
| State        |          | : In-Sync                |     |     |
| Link Status  |          | : up                     |     |     |
| Mgmt state   |          | : operational            |     |     |
| Inter-switch | link     | Statistics               |     |     |
----------------------------
| Hello Packets | Tx    | : 4572  |     |     |
| ------------- | ----- | ------- | --- | --- |
| Hello Packets | Rx    | : 4573  |     |     |
| Data Packets  | Tx    | : 80634 |     |     |
| Data Packets  | Rx    | : 80637 |     |     |
| Mgmt Packets  | Tx    | : 25946 |     |     |
| Mgmt Packets  | Rx    | : 25167 |     |     |
| Mgmt Packet   | Drops | : 0     |     |     |
DisplayingtheVSXkeepaliveprotocolstatus:
switch#
|                  | show vsx | status keepalive        |            |      |
| ---------------- | -------- | ----------------------- | ---------- | ---- |
| Keepalive        | State    | : Keepalive-Established |            |      |
| Last Established |          | : Thu Jun               | 8 09:03:01 | 2018 |
| Last Failed      |          | : Thu Jun               | 8 09:04:02 | 2018 |
| Peer System      | Id       | : 58:1f:cf:af:a0:84     |            |      |
| Peer Device      | Role     | : primary               |            |      |
| Keepalive        | Counters |                         |            |      |
| Keepalive        | Packets  | Tx : 322                |            |      |
| Keepalive        | Packets  | Rx : 121                |            |      |
| Keepalive        | Timeouts | : 0                     |            |      |
| Keepalive        | Packets  | Dropped : 14            |            |      |
DisplayingtheVSXlink-updelaystatuswhileARP/MACVSXsynchronizationisinprogress:
| switch# | show vsx | status linkup-delay |     |     |
| ------- | -------- | ------------------- | --- | --- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 167

| Configured   | linkup delay-timer |     |     |     | : 180 seconds      |     |
| ------------ | ------------------ | --- | --- | --- | ------------------ | --- |
| Initial      | sync status        |     |     |     | : In-progress      |     |
| Delay timer  | status             |     |     |     | : Waiting-to-start |     |
| Linkup Delay | time left          |     |     |     | :                  |     |
Interfaces that will be brought up after delay timer expires : lag20,lag30-lag31
| Interfaces | enabled for     | shutdown-on-split   | that will | be brought |        |     |
| ---------- | --------------- | ------------------- | --------- | ---------- | ------ | --- |
| up after   | the delay timer | expires             |           |            | :      |     |
| Interfaces | that are        | excluded from delay | timer     |            | : lag2 |     |
DisplayingtheVSXlink-updelaystatuswithARP/MACVSXsynchronizationcompletedwiththedelay
timerrunning:
| switch#      | show vsx status    | linkup-delay |     |     |               |     |
| ------------ | ------------------ | ------------ | --- | --- | ------------- | --- |
| Configured   | linkup delay-timer |              |     |     | : 180 seconds |     |
| Initial      | sync status        |              |     |     | : Completed   |     |
| Delay timer  | status             |              |     |     | : Running     |     |
| Linkup Delay | time left          |              |     |     | : 1 minutes   | 22  |
seconds
Interfaces that will be brought up after delay timer expires : lag20,lag30-lag31
| Interfaces | enabled for     | shutdown-on-split   | that will | be brought |        |     |
| ---------- | --------------- | ------------------- | --------- | ---------- | ------ | --- |
| up after   | the delay timer | expires             |           |            | :      |     |
| Interfaces | that are        | excluded from delay | timer     |            | : lag2 |     |
DisplayingtheVSXlink-updelaystatuswithARP/MACVSXsynchronizationcompletedandthedelay
timerexpired:
DisplayingtheglobalVSXstatusforthepeerswitch:
| vsx-primary#    | show vsx | status vsx-peer |     |     |     |     |
| --------------- | -------- | --------------- | --- | --- | --- | --- |
| VSX Operational | State    |                 |     |     |     |     |
---------------------
| ISL channel  |             | : In-Sync         |                   |     |     |     |
| ------------ | ----------- | ----------------- | ----------------- | --- | --- | --- |
| ISL mgmt     | channel     | : operational     |                   |     |     |     |
| Config       | Sync Status | : in-sync         |                   |     |     |     |
| NAE          |             | : peer_reachable  |                   |     |     |     |
| HTTPS        | Server      | : peer_reachable  |                   |     |     |     |
| Attribute    |             | Local             | Peer              |     |     |     |
| ------------ |             | --------          | --------          |     |     |     |
| ISL link     |             | lag1              | lag1              |     |     |     |
| ISL version  |             | 2                 | 2                 |     |     |     |
| System MAC   |             | e0:07:1b:cb:72:e4 | 98:f2:b3:68:79:2e |     |     |     |
| Platform     |             | 8320              | 8320              |     |     |     |
| Software     | Version     | 10.0x.xxxx        | 10.0x.xxxx        |     |     |     |
| Device Role  |             | secondary         | primary           |     |     |     |
Displayingthestatusforanout-of-syncstatusforVSX.
| switch#    | show vsx status    | linkup-delay |     |     |              |     |
| ---------- | ------------------ | ------------ | --- | --- | ------------ | --- |
| Configured | linkup delay-timer |              |     |     | : 20 seconds |     |
| Initial    | sync status        |              |     |     | :            |     |
VSXcommands|168

| Delay timer  | status    |                       |            |       |                 | :   |
| ------------ | --------- | --------------------- | ---------- | ----- | --------------- | --- |
| Linkup Delay | time      | left                  |            |       |                 | :   |
| Interfaces   | that will | be brought            | up after   | delay | timer expires   | :   |
| Interfaces   | enabled   | for shutdown-on-split |            | that  | will be brought |     |
| up after     | the delay | timer expires         |            |       |                 | :   |
| Interfaces   | that are  | excluded              | from delay | timer |                 | :   |
DisplayingthestatusVSXlink-updelaystatuswheninterfacesenabledforshutdown-on-split.
| switch#      | show vsx status | linkup-delay |     |     |     |                    |
| ------------ | --------------- | ------------ | --- | --- | --- | ------------------ |
| Configured   | linkup          | delay-timer  |     |     |     | : 180 seconds      |
| Initial      | sync status     |              |     |     |     | : In-progress      |
| Delay timer  | status          |              |     |     |     | : Waiting-to-start |
| Linkup Delay | time            | left         |     |     |     | :                  |
Interfaces that will be brought up after delay timer expires : lag8,lag256
| Interfaces | enabled   | for shutdown-on-split |     | that | will be brought |                  |
| ---------- | --------- | --------------------- | --- | ---- | --------------- | ---------------- |
| up after   | the delay | timer expires         |     |      |                 | : 1/1/27,1/1/37, |
vlan2-vlan57
| Interfaces     | that are    | excluded | from delay   | timer |     | :   |
| -------------- | ----------- | -------- | ------------ | ----- | --- | --- |
| Command        | History     |          |              |       |     |     |
| Release        |             |          | Modification |       |     |     |
| 10.07orearlier |             |          | --           |       |     |     |
| Command        | Information |          |              |       |     |     |
| Platforms      | Command     | context  | Authority    |       |     |     |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     | commandfromtheoperatorcontext(>)only. |     |     |     |
| ---- | --- | --- | ------------------------------------- | --- | --- | --- |
8325
8360
8400
9300
10000
| show vsx        | status      | config-sync |     |     |     |     |
| --------------- | ----------- | ----------- | --- | --- | --- | --- |
| show vsx status | config-sync | [vsx-peer]  |     |     |     |     |
Description
DisplaysVSXconfigurationsynchronizationstatusforpeers.Thiscommandcanberunfromtheprimary
orsecondarypeertoviewtheconfigurationsynchronizationstate.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 169

Example
| switch#     | show vsx status | config-sync   |             |      |
| ----------- | --------------- | ------------- | ----------- | ---- |
| Admin State |                 | : Enabled     |             |      |
| Operational | State           | : Operational |             |      |
| Error State |                 | : None        |             |      |
| Recommended | remediation     | : N/A         |             |      |
| Current     | Time            | : Wed Jul     | 18 23:41:07 | 2018 |
| Last Sync   | Time            | : Wed Jul     | 18 23:38:26 | 2018 |
TheAdminStateparametercanbeconfiguredindividuallyoneachoftheswitchesontheVSXpair.Hence
differenceinvaluesdoesnotimplyafailure.
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | ------------------------------------- | --- |
8325
8360
8400
9300
10000
| show vsx        | status  | peering |     |     |
| --------------- | ------- | ------- | --- | --- |
| show vsx status | peering |         |     |     |
Description
DisplayssynchronizationpeeringstatusandhardwarepeeringstatusformodulessuchasMAC,
neighbor,spanning-tree,androute.ThiscommandcanbeusedtoviewthestatusofVSXpeering,
followingaVSXdevicerebootoranISLflap.
FollowingarethepossiblevaluesforVSXpeeringstatus:
n Complete—VSXpeeringprocessissuccessfullycompleted.
n In-progress—VSXpeeringisbeingprocessed.
n Not-started—VSXpeeringprocessisyettobestarted.
Examples
DisplayingtheVSXpeeringstatus:
VSXcommands|170

| switch# | show | vsx status | peering |     |     |
| ------- | ---- | ---------- | ------- | --- | --- |
----------------------------------------------------------------
| Module |     |     | Sync-Status |     | Hardware-Status |
| ------ | --- | --- | ----------- | --- | --------------- |
----------------------------------------------------------------
| MAC            |             |     | In-progress |     | Not-started  |
| -------------- | ----------- | --- | ----------- | --- | ------------ |
| Neighbor       |             |     | Complete    |     | In-progress  |
| Route          |             |     | Complete    |     | Complete     |
| Spanning-tree  |             |     | In-progress |     | Not-started  |
| EVPN           |             |     | In-progress |     | Not-started  |
| Command        | History     |     |             |     |              |
| Release        |             |     |             |     | Modification |
| 10.07orearlier |             |     |             |     | --           |
| Command        | Information |     |             |     |              |
| Platforms      | Command     |     | context     |     | Authority    |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 8320 |     |     |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | --- | --- | ------------------------------------- |
8325
8360
8400
9300
10000
| show vsx        | status |                   | shutdown-on-split |     |     |
| --------------- | ------ | ----------------- | ----------------- | --- | --- |
| show vsx status |        | shutdown-on-split |                   |     |     |
Description
DisplaysthestatusoftheinterfacesthatareshutdownduringaVSX split.
Youcanalsouseshow interfacecommandtoviewthestatusoftheinterface.Forexample,assumethatyou
haveshutdownthenon-vsxinterface1/1/2duringtheVSX split.Whenyouentershow interfacecommandon
thesecondaryswitch,theoutputfromthecommandindicatesthattheinterfacewasblockedbyVSX feature.
Examples
DisplayingthestatusofinterfacesthatareshutdownduringtheVSXsplit:
| switch(config)# |     | show | vsx status | shutdown-on-split |     |
| --------------- | --- | ---- | ---------- | ----------------- | --- |
List of non-vsx interfaces enabled for split shutdown and its status.
| Interfaces |         |     |          | Status |     |
| ---------- | ------- | --- | -------- | ------ | --- |
| 1/1/1      |         |     | Disabled |        |     |
| lag100     |         |     | Disabled |        |     |
| vlan2      |         |     | Disabled |        |     |
| Command    | History |     |          |        |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 171

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 8100 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | ----------------------------------------------------- |
(#)
commandfromtheoperatorcontext(>)only.
8320
8325
8360
8400
9300
10000
split recovery
split-recovery
no split-recovery
Description
Enablessplitrecoverymode.Splitrecoverymodeisenabledbydefault.
Thenoformofthiscommanddisablessplit-recoverymode.
Usage
SplitrecoverymodepreventstrafficlosswhentheISLgoesout-of-syncandkeepalivesubsequently
fails.WhentheISLgoesout-of-syncandkeepaliveisestablished,thesecondaryVSXLAGsarebrought
down.Ifkeepalivethenalsofails,thissituationcausesasplitcondition.Inthiscase,ifsplitrecovery
modeisenabled,thesecondaryswitchrestoresitsVSXLAGssotheyareup.
Whensplitrecoverymodeisdisabledduringasplitcondition,thesecondaryswitchkeepsitVSXLAGs
down.
Examples
Enablingsplitrecoverymode:
| switch(config-vsx)# |     | split-recovery |     |
| ------------------- | --- | -------------- | --- |
Disablingsplitrecoverymode:
| switch(config-vsx)# |     | no split-recovery |              |
| ------------------- | --- | ----------------- | ------------ |
| Command History     |     |                   |              |
| Release             |     |                   | Modification |
| 10.07orearlier      |     |                   | --           |
VSXcommands|172

| Command   | Information |     |         |           |
| --------- | ----------- | --- | ------- | --------- |
| Platforms | Command     |     | context | Authority |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8100
8320
8325
8360
8400
9300
10000
| system    | l2-vlan-mac-mode |     |              |     |
| --------- | ---------------- | --- | ------------ | --- |
| system    | l2-vlan-mac-mode |     | {drop|flood} |     |
| no system | l2-vlan-mac-mode |     | {drop|flood} |     |
Description
Thiscommandconfigurestheforwardingactionforpacketsreceivedonanl2VLANportwhenswitch
systemMACaddressasthedestinationMACaddress.
Thenoformofthiscommandconfigurestheswitchtothedefaultsettingofdroppingpackets.
| Parameter |     |     |     | Description                                    |
| --------- | --- | --- | --- | ---------------------------------------------- |
| drop      |     |     |     | Forwardingactionofthepacketsistodrop.(default) |
| flood     |     |     |     | Forwardingactionofthepacketsistoflood.         |
Whenfloodmodeisconfigured,8320and8325or10000switchessupportlessthan512and1024SVIs
respectively.Whentheactive-gatewayisconfiguredonSVIalongwiththefloodmode,itsupportsupto10SVIs.
Examples
Thefollowingexampleforfloodthepackets:
| switch(config)# |     | system | l2-vlan-mac-mode | flood |
| --------------- | --- | ------ | ---------------- | ----- |
Thefollowingexamplefordropthepackets:
| switch(config)# |     | system | l2-vlan-mac-mode | drop |
| --------------- | --- | ------ | ---------------- | ---- |
TheFollowingexampleforpacketsdefaultsetting:
| switch(config)# |     | no system | l2-vlan-mac-mode |     |
| --------------- | --- | --------- | ---------------- | --- |
TheFollowingexamplefordefaultsettingofsysteml2-vlan-mac-modedropcommand:
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 173

| switch(config)# | no  | system l2-vlan-mac-mode |     | drop |     |     |     |
| --------------- | --- | ----------------------- | --- | ---- | --- | --- | --- |
TheFollowingexamplefordefaultsettingofsysteml2-vlan-mac-modefloodcommand:
| switch(config)# | no  | system l2-vlan-mac-mode |     | flood |     |     |     |
| --------------- | --- | ----------------------- | --- | ----- | --- | --- | --- |
Configuringl3-src-maconaVLANinterface,l2-vlan-mac-modefloodcannotbeconfigured.Such
configurationcangenerateanerrorasshownandcommandwillnottakeaffect.
| switch(config-if-vlan)# |        | active-gateway   |     | l3-src-mac |     |     |     |
| ----------------------- | ------ | ---------------- | --- | ---------- | --- | --- | --- |
| switch(config)#         | system | l2-vlan-mac-mode |     | flood      |     |     |     |
l2-vlan-mac-mode flood cannot be configured when active-gateway l3-src-mac is
configured.
| Configuration             | table | for supported | SVIs |     |              |              |      |
| ------------------------- | ----- | ------------- | ---- | --- | ------------ | ------------ | ---- |
| Configuration             |       |               |      |     | Platforms    | Supported    | SVIs |
| Whenfloodmodeisconfigured |       |               |      |     | 8320         | Lessthan512  |      |
|                           |       |               |      |     | 8325and10000 | Lessthan1024 |      |
Whentheactive-gatewayIPv4isconfiguredonSVIalongwiththe 8320 Upto190
floodmode
|     |     |     |     |     | 8325and10000 | Upto380 |     |
| --- | --- | --- | --- | --- | ------------ | ------- | --- |
Whentheactive-gatewayIPv4andIPv6areconfiguredonSVI 8320 Upto165
alongwiththefloodmode
|     |     |     |     |     | 8325and10000 | Upto330 |     |
| --- | --- | --- | --- | --- | ------------ | ------- | --- |
WhentheVSXactive-forwarding,VRRPandvirtual-macfeatures 8320,8325and Goesdown
| areconfigured  |             |         |                                 |     | 10000 |     |     |
| -------------- | ----------- | ------- | ------------------------------- | --- | ----- | --- | --- |
| Command        | History     |         |                                 |     |       |     |     |
| Release        |             |         | Modification                    |     |       |     |     |
| 10.09          |             |         | Commandsupportedfor10000switch. |     |       |     |     |
| 10.07orearlier |             |         | --                              |     |       |     |     |
| Command        | Information |         |                                 |     |       |     |     |
| Platforms      | Command     | context | Authority                       |     |       |     |     |
6400 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |     |     |     |
| ---- | --- | --- | --------------- | --- | --- | --- | --- |
8320
8325
10000
VSXcommands|174

system-mac
system-mac <MAC-ADDR>
no system-mac [<MAC-ADDR>]

Description

Sets the MAC address as the VSX system MAC address to be used by control plane protocols, such as
STP and LACP. A pair of VSX switches must have the same VSX system MAC.

The no form of this command unconfigures the VSX system MAC address to be used by control plane
protocols.

Parameter

<MAC-ADDR>

Usage

Description

Specifies the MAC address in a colon separated format, such as
XX:XX:XX:XX:XX:XX, for control plane protocols.

The system-mac <MAC-ADDR> command is highly recommended for preventing traffic disruptions
when the primary VSX switch restores after the secondary VSX switch, such as during:

n A primary switch hardware replacement.

n A power outage with the primary switch restore after the secondary switch restore.

When the primary switch is restored after the secondary switch, a traffic disruption might occur when
the ISL starts to sync. This situation occurs because the MAC system address changes from the
secondary switch to the primary switch for the LACP. To avoid the traffic disruption, set the common
system MAC address by entering the system-mac <MAC-ADDR> command. This command creates a
common system MAC address between the two VSX switches. This common system MAC address
prevents a traffic disruption when the secondary switch comes up before the primary switch. If the
common system MAC access is enabled, the secondary switch uses the common system MAC address
instead of its own system MAC address, which prevents a traffic loss.

The system MAC address also maintains the same MSTP bridge ID across VSX switches, which act as a
single switch.

Examples

Setting a MAC address as the VSX system MAC address to be used by control plane protocols:

switch(config-vsx)# system-mac 02:01:00:00:01:00

Unconfiguring a VSX system MAC address to be used by control plane protocols:

switch(config-vsx)# no system-mac 02:01:00:00:01:00

Null system MAC address such as 00:00:00:00:00:00 is not allowed.

Command History

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

175

| Release             |         |         | Modification               |
| ------------------- | ------- | ------- | -------------------------- |
| 10.08               |         |         | Updatednoformofthecommand. |
| 10.07orearlier      |         |         | --                         |
| Command Information |         |         |                            |
| Platforms           | Command | context | Authority                  |
config-vsx
6400 Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
vsx
vsx
no vsx
Description
CreatestheVSXcontextontheswitch.
ThenoformofthiscommanddisablestheVSXcontextontheswitchandremovesallrelated
configurationsettings.
Examples
CreatingtheVSXcontextontheswitch:
| switch(config)# | vsx |     |     |
| --------------- | --- | --- | --- |
switch(config-vsx)#
RemovingtheVSXcontextandallVSXconfigurationsettingsfromtheswitch:
| switch(config-vsx)# |             | no vsx           |     |
| ------------------- | ----------- | ---------------- | --- |
| VSX configuration   |             | will be deleted. |     |
| Do you want         | to continue | (y/n)?           | y   |
switch(config)#
| Command History     |     |     |              |
| ------------------- | --- | --- | ------------ |
| Release             |     |     | Modification |
| 10.07orearlier      |     |     | --           |
| Command Information |     |     |              |
VSXcommands|176

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6400 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
vsx active-forwarding
vsx active-forwarding
no vsx active-forwarding
Description
ConfiguresVSXactive-forwardingonaninterfaceVLAN.
ThenoformofthiscommandunconfiguresVSXactive-forwardingonaVLANinterface.
Usage
ActiveforwardingcannotbeconfiguredwhenICMPredirectisenabled.TheICMPredirectsettingis
globalnotperSVI.Entertheno ip icmp redirectcommandfordisablingICMPredirectattheswitch
(config)#prompt.
Ifasystemhasactiveforwardingenabled,anactivegatewaycanhaveamaximumof14"unique"MAC
addressespersystem,includingIPv4andIPv6addresses.
Ifasystemhasactiveforwardingdisabled,anactivegatewaycanhaveamaximumof16"unique"MAC
addressespersystem,includingIPv4andIPv6addresses.
Examples
SuccessfullyenablingVSXactive-forwarding:
| switch# | interface | vlan 3 |     |
| ------- | --------- | ------ | --- |
switch(config-if-vlan)#
vsx active-forwarding
switch(config-vsx)#
UnconfiguringVSXactive-forwarding:
| switch#                 | interface | vlan 3 |                   |
| ----------------------- | --------- | ------ | ----------------- |
| switch(config-if-vlan)# |           | no vsx | active-forwarding |
switch(config-vsx)#
| Command History     |     |     |              |
| ------------------- | --- | --- | ------------ |
| Release             |     |     | Modification |
| 10.07orearlier      |     |     | --           |
| Command Information |     |     |              |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 177

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6400 config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
vsx shutdown-on-split
vsx shutdown-on-split
no vsx shutdown-on-split
Description
Shutsdowntheconfigurednon-VSXinterfacesontheVSXsecondaryalongwithVSX interfacesduringa
VSXsplit.
Thenoformofthiscommandresumesthenon-VSXinterfacesthatareshutdownduringtheVSXsplit.
ThiscommandhasnoeffectontheVSXprimaryduringasplit.However,whenappliedontheVSXprimary,the
commandwillbringdownthenon-VSXinterfacesuntillinkupdelaytimerexpiresduringtheVSXprimaryreboot.
Examples
Shuttingdownthenon-VSXinterface1/1/1duringtheVSXsplit:
| switch(config)#       | interface | 1/1/1                 |     |
| --------------------- | --------- | --------------------- | --- |
| switch(config-if)#    |           | vsx shutdown-on-split |     |
| switch(config)#       | interface | lag 1                 |     |
| witch(config-lag-if)# |           | vsx shutdown-on-split |     |
Shuttingdownthenon-VSXinterfaceLAG5duringtheVSXsplit:
| switch(config)#        | interface | lag 5                 |     |
| ---------------------- | --------- | --------------------- | --- |
| switch(config-lag-if)# |           | vsx shutdown-on-split |     |
Shuttingdownthenon-VSXSVIduringtheVSXsplit:
| switch(config)#         | interface | vlan                  | 2   |
| ----------------------- | --------- | --------------------- | --- |
| switch(config-if-vlan)# |           | vsx shutdown-on-split |     |
Resumingthenon-VSXinterfacethatareshutdownduringtheVSXsplit:
| switch(config-if)# |     | no vsx shutdown-on-split |     |
| ------------------ | --- | ------------------------ | --- |
| Command History    |     |                          |     |
VSXcommands|178

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

config-if
config-lag-if
config-if-vlan

Administrators or local user group members with execution rights
for this command.

6400
8100
8320
8325
8360
8400
9300
10000

vsx-sync
vsx-sync
no vsx-sync

Description

Enables VSX synchronization for the entire context for the following features from the primary VSX node
to the secondary peer switch:

n Access list context

n Classifier context

n Object group context

n Policy-based routing profile context

n Policy context

n QoS queue profile context

n QoS schedule profile context

n VLAN context

The no form of this command disables VSX synchronization for the entire context for a feature, but it
does not remove the feature configurations from the secondary peer. Any subsequent configuration
changes made under the specific configuration context are not synchronized to the secondary peer
switch.

Usage

Make sure that you are in the correct context for the feature that you are trying to enable VSX
synchronization:

Feature context for enabling VSX syn-
chronization

Command for accessing correct context for
the vsx-sync command*

Access list context for an ACL type, such as IPv4, IPv6,
or MAC.

access-list <ACL-TYPE> <ACL-NAME>

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

179

Feature context for enabling VSX syn- Command for accessing correct context for
| chronization |     |     | the vsx-sync | command* |
| ------------ | --- | --- | ------------ | -------- |
Classcontextforaclasstype,suchasIPv4,IPv6,or class <CLASS-TYPE> <CLASS-NAME>
MAC.
ObjectgroupcontextforIPv4 object-group ip address <OBJECT-GROUP-
NAME>
ObjectgroupcontextforIPv6 object-group ipv6 address <OBJECT-GROUP-
NAME>
Objectgroupcontextforports object-group port <OBJECT-GROUP-NAME>
| Policy-basedroutingprofilecontext |     |     | pbr <ACTION-LIST-NAME> |     |
| --------------------------------- | --- | --- | ---------------------- | --- |
| Policycontext                     |     |     | policy <POLICY-NAME>   |     |
QoSqueueprofilecontext qos queue-profile <QUEUE-PROFILE-NAME>
QoSscheduleprofilecontext qos schedule-profile <SCHEDULE-PROFILE-
NAME>
| VLANcontext |     |     | vlan <ID> |     |
| ----------- | --- | --- | --------- | --- |
*Thecommandslistedinthiscolumnareenteredattheswitch(config)#prompt,asshowninthe
followingexamples.
Examples
EnablingVSXsynchronizationforthisIPv4accesslistcontexttothesecondarypeer:
| switch(config)#        | access-list | ip ITBoston |     |     |
| ---------------------- | ----------- | ----------- | --- | --- |
| switch(config-acl-ip)# | vsx-sync    |             |     |     |
EnablingVSXsynchronizationforthisIPv6accesslistcontexttothesecondarypeer:
| switch(config)#          | access-list | ipv6 ITRoseville |     |     |
| ------------------------ | ----------- | ---------------- | --- | --- |
| switch(config-acl-ipv6)# |             | vsx-sync         |     |     |
EnablingVSXsynchronizationforthisMACaccesslistcontexttothesecondarypeer:
| switch(config)#          | access-list | mac ITBangalore |     |     |
| ------------------------ | ----------- | --------------- | --- | --- |
| switch(config-acl-ipv6)# |             | vsx-sync        |     |     |
EnablingVSXsynchronizationforthisIPv4classcontexttothesecondarypeer:
| switch(config)#          | class ip | ITengineering |     |     |
| ------------------------ | -------- | ------------- | --- | --- |
| switch(config-class-ip)# |          | vsx-sync      |     |     |
EnablingVSXsynchronizationforthisobjectgroupcontextforIPv4:
VSXcommands|180

| switch(config)# | object-group | ip address | group1 |
| --------------- | ------------ | ---------- | ------ |
switch(config-addrgroup-ip)#
1.1.1.1
| switch(config-addrgroup-ip)# |     | vsx-sync |     |
| ---------------------------- | --- | -------- | --- |
EnablingVSXsynchronizationforthisQoSqueueprofilecontexttothesecondarypeer:
| switch(config)#       | qos queue-profile | test_queue_profile |     |
| --------------------- | ----------------- | ------------------ | --- |
| switch(config-queue)# | vsx-sync          |                    |     |
EnablingVSXsynchronizationforthisQoSscheduleprofilecontexttothesecondarypeer:
| switch(config)#          | qos schedule-profile |     | test_queue_profile1 |
| ------------------------ | -------------------- | --- | ------------------- |
| switch(config-schedule)# | vsx-sync             |     |                     |
EnablingVSXsynchronizationforthisPBRprofilecontexttothesecondarypeer:
| switch(config)#                             | pbr engineering |     |          |
| ------------------------------------------- | --------------- | --- | -------- |
| switch(config-pbr-action-list-engineering)# |                 |     | vsx-sync |
EnablingVSXsynchronizationforthispolicycontexttothesecondarypeer:
| switch(config)#        | policy ITPaloAlto |     |     |
| ---------------------- | ----------------- | --- | --- |
| switch(config-policy)# | vsx-sync          |     |     |
EnablingVSXsynchronizationforthisVLANcontexttothesecondarypeer:
switch(config)#
vlan 1
| switch(config-vlan-1)# | vsx-sync |     |     |
| ---------------------- | -------- | --- | --- |
DisablingVSXsynchronizationforthisIPv4classcontexttothesecondarypeer:
| switch(config)#          | class ip ITengineering |          |     |
| ------------------------ | ---------------------- | -------- | --- |
| switch(config-class-ip)# | no                     | vsx-sync |     |
DisablingVSXsynchronizationforthisobjectgroupcontextforIPv4:
| switch(config)#              | object-group | ip address  | group1 |
| ---------------------------- | ------------ | ----------- | ------ |
| switch(config-addrgroup-ip)# |              | no vsx-sync |        |
DisablingVSXsynchronizationforthisQoSqueueprofilecontexttothesecondarypeer:
| switch(config)#       | qos queue-profile | test_queue_profile |     |
| --------------------- | ----------------- | ------------------ | --- |
| switch(config-queue)# | no vsx-sync       |                    |     |
DisablingVSXsynchronizationforthisQoSscheduleprofilecontexttothesecondarypeer:
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 181

| switch(config)# |     | qos schedule-profile |     | test_queue_profile1 |     |
| --------------- | --- | -------------------- | --- | ------------------- | --- |
switch(config-schedule)#
no vsx-sync
DisablingVSXsynchronizationforthisPBRprofilecontexttothesecondarypeer:
| switch(config)#                             |     | pbr engineering |     |             |     |
| ------------------------------------------- | --- | --------------- | --- | ----------- | --- |
| switch(config-pbr-action-list-engineering)# |     |                 |     | no vsx-sync |     |
DisablingVSXsynchronizationforthispolicycontexttothesecondarypeer:
| switch(config)#        |     | policy | ITPaloAlto  |     |     |
| ---------------------- | --- | ------ | ----------- | --- | --- |
| switch(config-policy)# |     |        | no vsx-sync |     |     |
DisablingVSXsynchronizationforthisMACaccesslistcontexttothesecondarypeer:
| switch(config)#          |     | access-list | mac ITBangalore |     |     |
| ------------------------ | --- | ----------- | --------------- | --- | --- |
| switch(config-acl-ipv6)# |     |             | no vsx-sync     |     |     |
DisablingVSXsynchronizationforthisVLANcontexttothesecondarypeer:
| switch(config)#        |                       | vlan | 1           |              |                                |
| ---------------------- | --------------------- | ---- | ----------- | ------------ | ------------------------------ |
| switch(config-vlan-1)# |                       |      | no vsx-sync |              |                                |
| Command                | History               |      |             |              |                                |
| Release                |                       |      |             | Modification |                                |
| 10.07orearlier         |                       |      |             | --           |                                |
| Command                | Information           |      |             |              |                                |
| Platforms              | Command               |      | context     |              | Authority                      |
| 6400                   | config-acl-<ACL-TYPE> |      |             |              | Administratorsorlocalusergroup |
| 8100                   | config-addrgroup-ip   |      |             |              | memberswithexecutionrightsfor  |
| 8320                   | config-addrgroup-ipv6 |      |             |              | thiscommand.                   |
config-class-<CLASS-TYPE>
8325
| 8360 | config-policy                             |     |     |     |     |
| ---- | ----------------------------------------- | --- | --- | --- | --- |
| 8400 | config-portgroup                          |     |     |     |     |
| 9300 | config-pbr-action-list-<ACTION-LIST-NAME> |     |     |     |     |
config-queue
10000
config-schedule-<NAME>
config-vlan-<VLAN-ID>
| vsx-sync | (config-if, |     | config-lag-if | contexts) |     |
| -------- | ----------- | --- | ------------- | --------- | --- |
vsx-sync {[access-lists] [qos] [rate-limits] [vlans] [policies] [irdp] [portfilter]
| [private-vlan | port-type] |     | [dhcp-snooping]} |     |     |
| ------------- | ---------- | --- | ---------------- | --- | --- |
no vsx-sync {[access-lists] [qos] [rate-limits] [vlans] [policies] [irdp] [portfilter]
| [private-vlan | port-type] |     | [dhcp-snooping]} |     |     |
| ------------- | ---------- | --- | ---------------- | --- | --- |
VSXcommands|182

Description

Enables VSX synchronization for the following for a logical interface or a LAG instance:

n Access lists

n IRDP configurations

n QoS

n Rate limits

n Port filter configurations

n VLAN associations

n PVLAN port type configurations

n DHCP snooping

This command enables VSX synchronization for individual associations and to the combination of
associations to the interface context. To synchronize the associations, you must configure the same
interface on the peer switch.

When enabling VSX synchronization under a physical interface, under a VLAN interface, or a VSX LAG, create on

the secondary switch the physical interface, VLAN interface, or VSX LAG with the same name and routing setting

as on the primary switch. For example, if the primary switch has a physical interface of 1/1/1, you must create

another physical interface of 1/1/1 on the secondary switch. Also, if the primary VSX switch has routing enabled,

the secondary switch must have routing enabled. Once the name and routing information is the same, VSX

synchronization synchronizes the additional configuration information from the primary VSX switch to the

secondary VSX switch.

The no form of this command disables VSX synchronization, but it does not remove the feature
configurations from the secondary peer.

Parameter

{[access-lists] [qos] [rate-limits] [vlans] [policies]

[irdp] [portfilter] [private-vlan port-type] [dhcp-snooping]}

access-lists

qos

rate-limits

vlans

Description

Specifies one or more of
the features for which to
enable VSX
synchronization.

Specifies the access lists
that are associated under
the interface enabled for
VSX syncing.

Specifies the QoS
associated under the
interface enabled for VSX
syncing.

Specifies the rate limits
that are associated under
the interface enabled for
VSX syncing.

Specifies the VLANs that
are associated under the
interface enabled for VSX
syncing.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

183

| Parameter |     |     |     | Description            |
| --------- | --- | --- | --- | ---------------------- |
| policies  |     |     |     | Specifiestheclassifier |
policiesthatare
associatedunderthe
interfaceenabledforVSX
syncing.
| irdp |     |     |     | SpecifiestheInternet |
| ---- | --- | --- | --- | -------------------- |
RouterDiscoveryProtocol
(IRDP)configurationsthat
areassociatedunderthe
interfaceenabledforVSX
syncing.
| portfilter |     |     |     | Specifiestheportfilter |
| ---------- | --- | --- | --- | ---------------------- |
configurationsthatare
associatedunderthe
interfaceenabledforVSX
syncing.
| private-vlan | port-type |     |     | SpecifiesthePVLANport |
| ------------ | --------- | --- | --- | --------------------- |
typeconfigurationsthat
areassociatedunderthe
interfaceenabledforVSX
syncing.
| dhcp-snooping |     |     |     | SpecifiestheDHCP |
| ------------- | --- | --- | --- | ---------------- |
snoopingconfiguration
parametersthatare
associatedunderthe
interfaceenabledforVSX
syncing.
Example
EnablingVSXsynchronizationforVLANsassociatedwithlogicalinterface1/1/1:
| switch(config)#    | interface | 1/1/1 |     |     |
| ------------------ | --------- | ----- | --- | --- |
| switch(config-if)# | vsx-sync  | vlans |     |     |
EnablingVSXsynchronizationforaccesslistsassociatedwithlogicalinterface1/1/1:
| switch(config)#    | interface | 1/1/1        |     |     |
| ------------------ | --------- | ------------ | --- | --- |
| switch(config-if)# | vsx-sync  | access-lists |     |     |
EnablingVSXsynchronizationforaccesslistsandpoliciesthatareassociatedwithlogicalinterface1/1/1:
| switch(config)#    | interface | 1/1/1        |          |     |
| ------------------ | --------- | ------------ | -------- | --- |
| switch(config-if)# | vsx-sync  | access-lists | policies |     |
EnablingVSXsynchronizationforVLANsandQoSthatareassociatedunderlogicalinterface1/1/5:
| switch(config)#    | interface | 1/1/5     |     |     |
| ------------------ | --------- | --------- | --- | --- |
| switch(config-if)# | vsx-sync  | vlans qos |     |     |
VSXcommands|184

EnablingVSXsynchronizationforratelimitsthatareassociatedunderlogicalinterface1/1/5:
| switch(config)#    | interface | 1/1/5       |     |     |
| ------------------ | --------- | ----------- | --- | --- |
| switch(config-if)# | vsx-sync  | rate-limits |     |     |
EnablingVSXsynchronizationforratelimits,VLANs,QoS,accesslists,policiesassociatedwithlogical
interface1/1/1:
| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)# vsx-sync rate-limits vlans qos access-lists policies
EnablingVSXsynchronizationforVLAN1underinterfaceLAG1:
| switch(config)# | interface | lag 1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-lag-if)#
|                        |     | vsx-sync   | vlans  |     |
| ---------------------- | --- | ---------- | ------ | --- |
| switch(config-lag-if)# |     | vlan trunk | native | 1   |
EnablingVSXsynchronizationforanaccesslistunderinterfaceLAG2:
| switch(config)#        | interface | lag 2             |              |             |
| ---------------------- | --------- | ----------------- | ------------ | ----------- |
| switch(config-lag-if)# |           | vsx-sync          | access-lists |             |
| switch(config-lag-if)# |           | apply access-list |              | ip test1 in |
EnablingVSXsynchronizationforaQoSunderinterfaceLAG3:
| switch(config)# | interface | lag 3 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-lag-if)#
|                        |     | vsx-sync  | qos              |      |
| ---------------------- | --- | --------- | ---------------- | ---- |
| switch(config-lag-if)# |     | apply qos | schedule-profile | test |
EnablingVSXsynchronizationforaratelimitunderinterfaceLAG4:
| switch(config)#        | interface | lag 4      |             |         |
| ---------------------- | --------- | ---------- | ----------- | ------- |
| switch(config-lag-if)# |           | vsx-sync   | rate-limits |         |
| switch(config-lag-if)# |           | rate-limit | broadcast   | 23 kbps |
EnablingVSXsynchronizationforapolicynamedtestunderinterfaceLAG5:
| switch(config)# | interface | lag 5 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-lag-if)#
|                        |     | vsx-sync     | policies |     |
| ---------------------- | --- | ------------ | -------- | --- |
| switch(config-lag-if)# |     | apply policy | test     | in  |
EnablingVSXsynchronizationforapolicynamedtest1,aratelimitof23kbps,aQoSnamedtest,VLAN
1,andanaccesslistnamedtest1underinterfaceLAG6:
| switch(config)# | interface | lag 6 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-lag-if)# vsx-sync policies rate-limits qos vlans access-lists
| switch(config-lag-if)# |     | apply policy | test1            | in      |
| ---------------------- | --- | ------------ | ---------------- | ------- |
| switch(config-lag-if)# |     | rate-limit   | broadcast        | 23 kbps |
| switch(config-lag-if)# |     | apply qos    | schedule-profile | test    |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 185

| switch(config-lag-if)# |     | vlan | trunk native | 1   |     |
| ---------------------- | --- | ---- | ------------ | --- | --- |
switch(config-lag-if)#
|     |     | apply | access-list | ip test | 1 in |
| --- | --- | ----- | ----------- | ------- | ---- |
EnablingVSXsynchronizationforaportfilter:
| switch(config)#        | interface | 1/1/1    |            |     |     |
| ---------------------- | --------- | -------- | ---------- | --- | --- |
| switch(config-if)#     | vsx-sync  |          | portfilter |     |     |
| switch(config)#        | interface | lag      | 1          |     |     |
| switch(config-lag-if)# |           | vsx-sync | portfilter |     |     |
EnablingVSXsynchronizationforaPVLANporttypeconfigurationunderinterfaceLAG3:
| switch(config)#        | interface | lag      | 3                      |     |     |
| ---------------------- | --------- | -------- | ---------------------- | --- | --- |
| switch(config-lag-if)# |           | vsx-sync | private-vlan-port-type |     |     |
EnablingVSXsynchronizationforDHCPsnoopingconfigurationunderinterfaceLAG9:
switch(config)#
|                        | interface | lag      | 9 multi-chassis |     |     |
| ---------------------- | --------- | -------- | --------------- | --- | --- |
| switch(config-lag-if)# |           | vsx-sync | dhcp-snooping   |     |     |
DisablingVSXsynchronizationforDHCPsnoopingconfigurationunderinterfaceLAG9:
| switch(config)#        | interface | lag         | 9 multi-chassis |     |     |
| ---------------------- | --------- | ----------- | --------------- | --- | --- |
| switch(config-lag-if)# |           | no vsx-sync | dhcp-snooping   |     |     |
DisablingVSXsynchronizationforaccesslistsandpoliciesunderlogicalinterface1/1/1:
| switch(config)#    | interface | 1/1/1    |              |          |     |
| ------------------ | --------- | -------- | ------------ | -------- | --- |
| switch(config-if)# | no        | vsx-sync | access-lists | policies |     |
DisablingVSXsynchronizationforaccesslistsandpoliciesunderinterfaceLAG2:
| switch(config)#    | interface | lag      | 2            |          |     |
| ------------------ | --------- | -------- | ------------ | -------- | --- |
| switch(config-if)# | no        | vsx-sync | access-lists | policies |     |
EnablingVSXsynchronizationofIRDPconfigurationsunderlogicalinterface1/1/1.Thefirstfivelinesin
theexampleconfigureIRDPandthelastlineenablesVSXsynchronizationforIRDPconfigurations
associatedunderinterface1/1/1:
switch(config)#
|                    | interface | 1/1/1                  |      |     |     |
| ------------------ | --------- | ---------------------- | ---- | --- | --- |
| switch(config-if)# | ip        | irdp                   |      |     |     |
| switch(config-if)# | ip        | irdp minadvertinterval |      | 550 |     |
| switch(config-if)# | ip        | irdp maxadvertinterval |      | 850 |     |
| switch(config-if)# | ip        | irdp holdtime          | 900  |     |     |
| switch(config-if)# | vsx-sync  |                        | irdp |     |     |
DisablingVSXsynchronizationforaPVLANporttypeconfigurationunderinterfaceLAG8:
VSXcommands|186

| switch(config)# |     | interface |     | lag 8 |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- |
switch(config-lag-if)#
|     |     |     | no  | vsx-sync | private-vlan-port-typeno | vsx-sync private-vlan- |
| --- | --- | --- | --- | -------- | ------------------------ | ---------------------- |
port-type
| Command | History |     |     |     |                                              |     |
| ------- | ------- | --- | --- | --- | -------------------------------------------- | --- |
| Release |         |     |     |     | Modification                                 |     |
| 10.09   |         |     |     |     | Addedprivate-vlan-port-typeparameter.Updated |     |
examples.
| 10.07orearlier |             |     |         |     | --        |     |
| -------------- | ----------- | --- | ------- | --- | --------- | --- |
| Command        | Information |     |         |     |           |     |
| Platforms      | Command     |     | context |     | Authority |     |
6400 config-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-lag-if |     |     |     | forthiscommand. |     |
| --- | ------------- | --- | --- | --- | --------------- | --- |
8325
8360
8400
9300
10000
| vsx-sync    | (config-vlan-if    |     |     |             | context) |     |
| ----------- | ------------------ | --- | --- | ----------- | -------- | --- |
| vsx-sync    | {[active-gateways] |     |     | [policies]} |          |     |
| no vsx-sync | {[active-gateways] |     |     | [policies]} |          |     |
Description
EnablesVSXsyncofactivegatewaysorpoliciesassociatedunderaninterface.Tosynchronizethe
associations,youmustconfigurethesameinterface vlanonthepeerswitch.
ThenoformofthiscommandremovesVSXsynchronizationforactivegatewaysorpoliciesassociated
underaninterface,butitdoesnotremovethefeatureconfigurationsfromthesecondarypeerswitch.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
{[active-gateways] [policies]} SpecifiesoneormoreofthefeaturesforwhichtoenableVSX
synchronization.
access-gateways Specifiesthatactivegatewaysassociatedwithaninterfaceare
enabledforVSXsyncing.
policies
Specifiesthatpoliciesassociatedwithaninterfaceareenabledfor
VSXsyncing.
Usage
ConfigureanSVIonthesecondaryswitch;however,youdonotneedtorunthevsx-sync active-
gatewayscommandonthesecondaryVSXswitch.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 187

DonotusepeersystemMACaddressasanactive-gatewayVMAC.IfsameMACaddressisused,theVSX
synchronizationwilltrytosynctheconfigurationonsecondaryswitchandcausetrafficdisruptions.
Examples
EnablingVSXsynchronizationforanactivegatewayassociatedwithVLAN1:
| switch(config)#         | interface | vlan     | 1               |     |
| ----------------------- | --------- | -------- | --------------- | --- |
| switch(config-if-vlan)# |           | vsx-sync | active-gateways |     |
EnablingVSXsynchronizationforpoliciesassociatedwithVLAN1:
| switch(config)#         | interface | vlan     | 1        |     |
| ----------------------- | --------- | -------- | -------- | --- |
| switch(config-if-vlan)# |           | vsx-sync | policies |     |
EnablingVSXsynchronizationforactivegatewaysandpoliciesassociatedwithVLAN1:
| switch(config)# | interface | vlan | 1   |     |
| --------------- | --------- | ---- | --- | --- |
switch(config-if-vlan)# active-gateway ip 10.10.10.10 mac 23:24:25:26:27:28
switch(config-if-vlan)# active-gateway ipv6 fd12:3456:789a:1::1 mac
| fd12:3456:789a:1::1     |     | 23:24:25:26:27:28 |                 |          |
| ----------------------- | --- | ----------------- | --------------- | -------- |
| switch(config-if-vlan)# |     | vsx-sync          | active-gateways | policies |
DisablingVSXsynchronizationforactivegatewaysassociatedwithVLAN1:
| switch(config)#         | interface | vlan        | 1               |     |
| ----------------------- | --------- | ----------- | --------------- | --- |
| switch(config-if-vlan)# |           | no vsx-sync | active-gateways |     |
| Command History         |           |             |                 |     |
| Release                 |           |             | Modification    |     |
| 10.07orearlier          |           |             | --              |     |
| Command Information     |           |             |                 |     |
| Platforms               | Command   | context     | Authority       |     |
6400 config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync     | aaa |     |     |     |
| ------------ | --- | --- | --- | --- |
| vsx-sync aaa |     |     |     |     |
VSXcommands|188

| no vsx-sync | aaa |     |     |
| ----------- | --- | --- | --- |
Description
EnablesVSXsynchronizationofallAAAconfigurations,includinguser,RADIUSserver,andTACACS+
server,ontheprimaryVSXnodetothesecondarypeerswitch.
ThenoformofthiscommandremovesVSXsynchronizationofglobalAAAconfigurations,butitdoes
notremovetheexistingglobalAAAfeatureconfigurationsfromthesecondarypeerswitch.
Examples
EnablingVSXsyncfortheAAAconfigurationstothesecondarypeer:
| switch(config)#     | vsx |          |     |
| ------------------- | --- | -------- | --- |
| switch(config-vsx)# |     | vsx-sync | aaa |
DisablingVSXsyncfortheAAAconfigurationstothesecondarypeer:
| switch(config)#     | vsx     |             |              |
| ------------------- | ------- | ----------- | ------------ |
| switch(config-vsx)# |         | no vsx-sync | aaa          |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
config-vsx
6400 Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| vsx-sync               | acl-log-timer |     |     |
| ---------------------- | ------------- | --- | --- |
| vsx-sync acl-log-timer |               |     |     |
| no vsx-sync            | acl-log-timer |     |     |
Description
EnablesVSXsynchronizationofaccesslistlogtimerconfigurationsontheprimaryVSXnodetothe
secondarypeer.
ThenoformofthiscommandremovesVSXsynchronizationofaccesslistlogtimerconfigurationstothe
secondarypeer.However,itdoesnotremovethepreviouslysyncedconfigurationsfromthesecondary
peerswitch.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 189

Examples
EnablingVSXsyncfortheaccesslistlogtimerconfigurations:
switch(config)#
|                     | access-list |          | log           | timer 30 |
| ------------------- | ----------- | -------- | ------------- | -------- |
| switch(config)#     | vsx         |          |               |          |
| switch(config-vsx)# |             | vsx-sync | acl-log-timer |          |
DisablingVSXsyncfortheaccesslistlogtimerconfigurations:
| switch(config)#     | vsx     |             |     |               |
| ------------------- | ------- | ----------- | --- | ------------- |
| switch(config-vsx)# |         | no vsx-sync |     | acl-log-timer |
| Command History     |         |             |     |               |
| Release             |         |             |     | Modification  |
| 10.07orearlier      |         |             |     | --            |
| Command Information |         |             |     |               |
| Platforms           | Command | context     |     | Authority     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
VSXcommands|190

| vsx-sync              | arp-security |     |     |
| --------------------- | ------------ | --- | --- |
| vsx-sync arp-security |              |     |     |
| no vsx-sync           | arp-security |     |     |
Description
EnablesVSXsynchronizationoftheARPsecurityconfigurationsontheprimaryVSXswitchtothe
secondarypeerswitch.Afteryouentervsx-sync arp-security,youmustentervsx-sync mclag-
interfacesforenablingVSXsynchronizationfortheARPsecurityfeature.
ThenoformofthiscommandremovesVSXsynchronizationofARPsecurityconfigurationsonVLAN
modeandLAGinterfacemodetothesecondarypeerswitch.However,itdoesnotremovetheexisting
ARPsecurityconfigurationsfromthesecondarypeerswitch.
Examples
EnablingofVSXsynchronizationforARPsecurityfeatureconfigurationstoasecondarypeer:
| primary_sw(config)#     |     | vsx      |                  |
| ----------------------- | --- | -------- | ---------------- |
| primary_sw(config-vsx)# |     | vsx-sync | arp-security     |
| primary_sw(config-vsx)# |     | vsx-sync | mclag-interfaces |
DisablingtheVSXsynchronizationforARPsecurityfeatureconfigurationstoasecondarypeer:
| primary_sw(config)#     |         | vsx         |                                         |
| ----------------------- | ------- | ----------- | --------------------------------------- |
| primary_sw(config-vsx)# |         | no vsx-sync | arp-security                            |
| switch(config-vsx)#     |         | no vsx-sync | mclag-interfaces                        |
| Command History         |         |             |                                         |
| Release                 |         |             | Modification                            |
| 10.11.1000              |         |             | Commandintroducedonthe8325SwitchSeries  |
| 10.11.1000              |         |             | Commandintroducedonthe10000SwitchSeries |
| 10.07orearlier          |         |             | --                                      |
| Command Information     |         |             |                                         |
| Platforms               | Command | context     | Authority                               |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8400
10000
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 191

| vsx-sync            | bfd-global |     |     |     |     |
| ------------------- | ---------- | --- | --- | --- | --- |
| vsx-sync bfd-global |            |     |     |     |     |
| no vsx-sync         | bfd-global |     |     |     |     |
Description
EnablessyncingofglobalBFDconfigurations,suchasecho-src-ip-address,detect-multiplier,min-
transmit-interval,andmin-receive-interval,ontheprimaryVSXnodetothesecondarypeer.
ThiscommandenablesVSXsynchronizationonlyatthetoplevelandnotatthecontextlevel.
ThenoformofthiscommanddisablesthesyncingofglobalBFDconfigurationstothesecondarypeer,
butitdoesnotremovetheexistingglobalBFDfeatureconfigurationsfromit.
Examples
EnablingVSXsynchronizationforvariousglobalBFDconfigurations:
| switch(config)#     | bfd | detect-multiplier         |            | 1       |      |
| ------------------- | --- | ------------------------- | ---------- | ------- | ---- |
| switch(config)#     | bfd | min-transmit-interval     |            | 1000    |      |
| switch(config)#     | bfd | min-receive-interval      |            | 1000    |      |
| switch(config)#     | bfd | echo-src-ip-address       |            | 2.2.2.2 |      |
| switch(config)#     | bfd | min-echo-receive-interval |            |         | 1000 |
| switch(config)#     | vsx |                           |            |         |      |
| switch(config-vsx)# |     | vsx-sync                  | bfd-global |         |      |
DisablingVSXsynchronizationforglobalBFDconfigurations:
| switch(config)#     | vsx     |             |              |     |     |
| ------------------- | ------- | ----------- | ------------ | --- | --- |
| switch(config-vsx)# |         | no vsx-sync | bfd-global   |     |     |
| Command History     |         |             |              |     |     |
| Release             |         |             | Modification |     |     |
| 10.07orearlier      |         |             | --           |     |     |
| Command Information |         |             |              |     |     |
| Platforms           | Command | context     | Authority    |     |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --------------- | --- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync | bgp |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
VSXcommands|192

| vsx-sync    | bgp |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| no vsx-sync | bgp |     |     |     |     |     |     |     |
Description
EnablessyncingofBGPconfigurationsontheprimaryVSXswitchtothesecondarypeerswitch.
ThenoformofthiscommanddisablessyncingBGP,aspathlists,communitylists,prefixlists,androute
mapconfigurationstothesecondarypeer,butitdoesnotremovethepreviouslysyncedconfigurations
fromthesecondarypeerswitch.
Usage
ThefollowingBGPconfigurationsaresynchronized:aspathlists,communitylists,prefixlists,androute
mapconfigurations.Tomaintaintheuniquenessofaswitchintheautonomoussystem,theBGProuter
ID,BGPclusterID,andBGPneighborupdate-sourcearenotsynchronized.Thisexclusionisrequiredfor
BGPfunctionalitytoworkseamlesslyevenwithVSXtopology.
Severalsettingsarealsonotsynced.Theneighbor <IP address> shutdownsettingisnotsynced
becausesyncingthatsettingwouldcauseboththeprimaryandsecondaryVSXnodestowardsthecore
togodown.Inroutemapconfigurations,thefollowingsettingsarealsonotsyncedfromtheprimary
VSXswitchtothesecondaryVSXswitch,becausethenext-hopisalwayssetdifferentlyfortheprimary
andsecondaryVSXpeers:
| n set ip   | nexthop | <IP-ADDR> |           |     |     |     |     |     |
| ---------- | ------- | --------- | --------- | --- | --- | --- | --- | --- |
| n set ipv6 | nexthop | global    | <IP-ADDR> |     |     |     |     |     |
Ifthenext-hopmustbesameforbothprimaryandsecondaryVSXpeers,configurethesamevalueon
theindividualswitches.
Examples
EnablingVSXsyncfortheBGPconfigurations:
| switch(config)# |     | ip  | aspath-list |     | list1 | seq 10 | permit | 10  |
| --------------- | --- | --- | ----------- | --- | ----- | ------ | ------ | --- |
switch(config)# ip community-list expanded com1 seq 10 permit 10
switch(config)# ip extcommunity-list standard ext1 seq 10 permit rt 10:4
| switch(config)#                  |     | ip prefix-list |                |            | pref1 seq | 10        | permit   | any     |
| -------------------------------- | --- | -------------- | -------------- | ---------- | --------- | --------- | -------- | ------- |
| switch(config)#                  |     | route-map      |                | rm1 permit |           |           |          |         |
| switch(config-route-map-rm1-10)# |     |                |                |            | match     | ip        | next-hop | 1.1.1.1 |
| switch(config)#                  |     | router         | bgp            | 100        |           |           |          |         |
| switch(config-bgp)#              |     |                | bgp router-id  |            | 1.1.1.1   |           |          |         |
| switch(config-bgp)#              |     |                | neighbor       | 12.1.1.1   |           | remote-as |          | 1       |
| switch(config-bgp)#              |     |                | address-family |            | ipv4      | unicast   |          |         |
| switch(config-bgp-ipv4-uc)#      |     |                |                | neighbor   | 12.1.1.1  |           | activate |         |
| switch(config)#                  |     | vsx            |                |            |           |           |          |         |
| switch(config-vsx)#              |     |                | vsx-sync       | bgp        |           |           |          |         |
DisablingVSXsyncfortheBGPconfigurations:
| switch(config)#     |         | vsx |             |     |     |     |     |     |
| ------------------- | ------- | --- | ----------- | --- | --- | --- | --- | --- |
| switch(config-vsx)# |         |     | no vsx-sync |     | bgp |     |     |     |
| Command             | History |     |             |     |     |     |     |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 193

| Release             |         |         | Modification |     |
| ------------------- | ------- | ------- | ------------ | --- |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync             | copp-policy |     |     |     |
| -------------------- | ----------- | --- | --- | --- |
| vsx-sync copp-policy |             |     |     |     |
| no vsx-sync          | copp-policy |     |     |     |
Description
EnablesVSXsynchronizationofCoPPpolicyconfigurationsontheprimaryVSXnodetothesecondary
peerswitch.
ThenoformofthiscommandremovesVSXsynchronizationofglobalCoPPconfigurations,butitdoes
notremovetheexistingglobalCoPPconfigurationsfromthesecondarypeerswitch.
Examples
Thefirstthreelinesinthefollowingexampleshowthesettingofseveralpolicyconfigurations.Thelast
twolinesoftheexampleshowtheenablingofVSXsynchronizationforCoPPpolicyconfigurations.
switch(config)#
|                      | copp-policy | mypolicy            |             |      |
| -------------------- | ----------- | ------------------- | ----------- | ---- |
| switch(config-copp)# |             | class arp-broadcast |             | drop |
| switch(config-copp)# |             | no class            | arp-unicast |      |
| switch(config)#      | vsx         |                     |             |      |
| switch(config-vsx)#  |             | vsx-sync            | copp-policy |      |
DisablingVSXsynchronizationforglobalCoPPconfigurations:
| switch(config)#     | vsx |             |              |     |
| ------------------- | --- | ----------- | ------------ | --- |
| switch(config-vsx)# |     | no vsx-sync | copp-policy  |     |
| Command History     |     |             |              |     |
| Release             |     |             | Modification |     |
| 10.07orearlier      |     |             | --           |     |
| Command Information |     |             |              |     |
VSXcommands|194

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync            | dcb-global |     |     |     |
| ------------------- | ---------- | --- | --- | --- |
| vsx-sync dcb-global |            |     |     |     |
| no vsx-sync         | dcb-global |     |     |     |
Description
EnablesVSXsynchronizationofglobalDCBxconfigurationsfromtheprimaryVSXnodetothesecondary
peer.
ThenoformofthecommanddisablesVSXsynchronizationofglobalDCBxconfigurationstothe
secondarypeer;however,itdoesnotremovetheexistingDCBxfeatureconfigurationsfromthe
secondarypeer.
Usage
ThefollowingcommandsaresyncedfromprimaryVSXnodetosecondaryVSXnode:
n lldp dcbx
n dcbx application
Examples
ThefirsttwolinesinthefollowingexampleshowthesettingofglobalDCBxconfigurations.Thelasttwo
linesintheexampleshowtheenablingofVSXsynchronizationforglobalDCBxconfigurations.
| switch(config)#     | lldp | dcbx        |                |     |
| ------------------- | ---- | ----------- | -------------- | --- |
| switch(config)#     | dcbx | application | iscsi priority | 7   |
| switch(config)#     | vsx  |             |                |     |
| switch(config-vsx)# |      | vsx-sync    | dcb-global     |     |
DisablingVSXsynchronizationforglobalDCBxconfigurations:
| switch(config)#     | vsx |             |              |     |
| ------------------- | --- | ----------- | ------------ | --- |
| switch(config-vsx)# |     | no vsx-sync | dcb-global   |     |
| Command History     |     |             |              |     |
| Release             |     |             | Modification |     |
| 10.07orearlier      |     |             | --           |     |
| Command Information |     |             |              |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 195

| Platforms | Command | context |     |     | Authority |
| --------- | ------- | ------- | --- | --- | --------- |
8325 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8360 |     |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
9300
10000
| vsx-sync            | dhcp-relay |     |     |     |     |
| ------------------- | ---------- | --- | --- | --- | --- |
| vsx-sync dhcp-relay |            |     |     |     |     |
| no vsx-sync         | dhcp-relay |     |     |     |     |
Description
EnablesVSXsynchronizationofDHCPv4andDHCPv6relayconfigurationsontheprimaryVSXnodeto
thesecondarypeer.
ThenoformofthecommanddisablestheVSXsynchronizationofDHCPv4andDHCPv6relay
configurationstothesecondarypeer;however,itdoesnotremovetheexistingDHCPv4andDHCPv6
relayconfigurationsfromthesecondaryVSXpeer.
Examples
ThisexampleenablesVSXsynchronizationforDHCPv4relayconfigurations.Thefirstsixlinesinthe
exampleshowDHCPv4relayconfigurations.ThelasttwolinesshowhowtoenableVSXsynchronization
fortheDHCPrelayconfigurations:
| switch(config)#     |     | interface         | 1/1/1  |            |              |
| ------------------- | --- | ----------------- | ------ | ---------- | ------------ |
| switch(config-if)#  |     | ip helper-address |        |            | 192.168.10.1 |
| switch(config-if)#  |     | ip helper-address |        |            | 192.168.20.1 |
| switch(config)#     |     | interface         | 1/1/2  |            |              |
| switch(config-if)#  |     | ip helper-address |        |            | 192.168.30.1 |
| switch(config)#     |     | dhcp-relay        | option |            | 82           |
| switch(config)#     |     | vsx               |        |            |              |
| switch(config-vsx)# |     | vsx-sync          |        | dhcp-relay |              |
ThisexampleenablesVSXsynchronizationforDHCPv6relayconfigurations.Thefirstsevenlinesinthe
exampleshowDHCPv6relayconfigurations.ThelasttwolinesshowhowtoenableVSXsynchronization
fortheDHCPrelayconfigurations:
| switch(config)#    |     | dhcpv6-relay |                |     |                        |
| ------------------ | --- | ------------ | -------------- | --- | ---------------------- |
| switch(config)#    |     | interface    | 1/1/1          |     |                        |
| switch(config-if)# |     | ipv6         | helper-address |     | unicast 2001:db8:0:1:: |
switch(config-if)# ipv6 helper-address multicast FF01::1:1000 egress 1/1/2
| switch(config)#     |     | interface    | 1/1/2          |            |                        |
| ------------------- | --- | ------------ | -------------- | ---------- | ---------------------- |
| switch(config-if)#  |     | ipv6         | helper-address |            | unicast 2001:db8:0:2:: |
| switch(config)#     |     | dhcpv6-relay |                | option     | 79                     |
| switch(config)#     |     | vsx          |                |            |                        |
| switch(config-vsx)# |     | vsx-sync     |                | dhcp-relay |                        |
DisablingVSXsynchronizationforDHCPrelayconfigurations:
| switch(config)#     |     | vsx |          |            |     |
| ------------------- | --- | --- | -------- | ---------- | --- |
| switch(config-vsx)# |     | no  | vsx-sync | dhcp-relay |     |
VSXcommands|196

| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync             | dhcp-server |     |     |     |
| -------------------- | ----------- | --- | --- | --- |
| vsx-sync dhcp-server |             |     |     |     |
| no vsx-sync          | dhcp-server |     |     |     |
Description
EnablesVSXsynchronizationofallDHCPv4serverconfigurations,includingexternalstorage
configurations,ontheprimaryVSXnodetothesecondarypeer.OnlytheprimaryVSXnodeanswers
DHCPservicerequests,andleasescanonlybeexportedfromtheprimaryVSXnode.
ThenoformofthecommanddisablesVSXsynchronizationofDHCPv4serverconfigurationstothe
secondarypeer;however,itdoesnotremovetheexistingDHCPv4serverfeatureconfigurationsfrom
thesecondarypeer.
Examples
ThefirstsixlinesinthefollowingexampleshowthesettingofaDHCPv4serverconfiguration.Thelast
lineoftheexampleshowstheenablingofVSXsynchronizationforglobalDHCPv4serverconfigurations.
switch(config)# dhcp-server external-storage dhcp-dbs file dhcpv4_lease_file delay
600
| switch(config)#                  | dhcp-server |     | vrf default     |           |
| -------------------------------- | ----------- | --- | --------------- | --------- |
| switch(config-dhcp-server)#      |             |     | pool test       |           |
| switch(config-dhcp-server-pool)# |             |     | range 10.0.0.20 | 10.0.0.30 |
switch(config-dhcp-server-pool)# default-router 10.0.0.1 10.0.0.10
switch(config-dhcp-server-pool)# static-bind ip 10.0.0.1 mac 24:be:05:24:75:73
| switch(config)# | vsx |     |     |     |
| --------------- | --- | --- | --- | --- |
switch(config-vsx)#
|     |     | vsx-sync | dhcp-server |     |
| --- | --- | -------- | ----------- | --- |
DisablingVSXsynchronizationforglobalDHCPv4serverconfigurations:
| switch(config)#     | vsx |             |             |     |
| ------------------- | --- | ----------- | ----------- | --- |
| switch(config-vsx)# |     | no vsx-sync | dhcp-server |     |
| Command History     |     |             |             |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 197

| Release             |         |         | Modification |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --------------- | --- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync               | dhcpv6-server |     |     |     |     |
| ---------------------- | ------------- | --- | --- | --- | --- |
| vsx-sync dhcpv6-server |               |     |     |     |     |
| no vsx-sync            | dhcpv6-server |     |     |     |     |
Description
EnablesVSXsynchronizationofallDHCPv6serverconfigurations,includingexternalstorage
configurations,ontheprimaryVSXnodetothesecondarypeer.
ThenoformofthecommanddisablesVSXsynchronizationofDHCPv6serverconfigurationstothe
secondarypeer;however,itdoesnotremovetheexistingDHCPv6serverfeatureconfigurationsfrom
thesecondarypeer.
Examples
ThefirstsixlinesinthefollowingexampleshowthesettingofaDHCPv6serverconfiguration.Thelast
twolinesoftheexampleshowtheenablingofVSXsynchronizationforglobalDHCPv6server
configurations.
switch(config)# dhcpv6-server external-storage dhcpv6-dbs file dhcpv6_lease_file
| delay 600                   |               |     |             |     |     |
| --------------------------- | ------------- | --- | ----------- | --- | --- |
| switch(config)#             | dhcpv6-server |     | vrf default |     |     |
| switch(config-dhcp-server)# |               |     | pool test   |     |     |
switch(config-dhcpv6-server-pool)# range 2001::1 2001::10 prefix-len 64
| switch(config-dhcpv6-server-pool)# |     |     | option | 22 ipv6 2001::12 |     |
| ---------------------------------- | --- | --- | ------ | ---------------- | --- |
switch(config-dhcpv6-server-pool)#
|     |     |     | static-bind | ipv6 2001::11 | client-id |
| --- | --- | --- | ----------- | ------------- | --------- |
1:0:a0:24:ab:fb:9c
| switch(config)#     | vsx |          |               |     |     |
| ------------------- | --- | -------- | ------------- | --- | --- |
| switch(config-vsx)# |     | vsx-sync | dhcpv6-server |     |     |
DisablingVSXsynchronizationforglobalDHCPv6serverconfigurations:
| switch(config)#     | vsx |             |               |     |     |
| ------------------- | --- | ----------- | ------------- | --- | --- |
| switch(config-vsx)# |     | no vsx-sync | dhcpv6-server |     |     |
| Command History     |     |             |               |     |     |
VSXcommands|198

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| vsx-sync     | dns |     |     |
| ------------ | --- | --- | --- |
| vsx-sync dns |     |     |     |
| no vsx-sync  | dns |     |     |
Description
EnablesVSXsynchronizationoftheglobalDNSconfigurationsontheprimaryVSXnodetothe
secondarypeerswitch.
ThenoformofthiscommandremovesVSXsynchronizationforglobalDNSconfigurations,butitdoes
notremovethefeatureconfigurationsfromthesecondarypeerswitch.
Examples
ThefirstlineinthefollowingexampleshowsthesettingofaDNSconfiguration.Thelasttwolinesofthe
exampleshowtheenablingofVSXsynchronizationforglobalDNSconfigurations.
switch(config)#
|                     | ip  | dns domain-name | domain.com |
| ------------------- | --- | --------------- | ---------- |
| switch(config)#     | vsx |                 |            |
| switch(config-vsx)# |     | vsx-sync        | dns        |
DisablingVSXsynchronizationforglobalDNSconfigurations:
| switch(config)#     | vsx |             |              |
| ------------------- | --- | ----------- | ------------ |
| switch(config-vsx)# |     | no vsx-sync | dns          |
| Command History     |     |             |              |
| Release             |     |             | Modification |
| 10.07orearlier      |     |             | --           |
| Command Information |     |             |              |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 199

| Platforms | Command |     | context | Authority |     |
| --------- | ------- | --- | ------- | --------- | --- |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --------------- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync    | dhcp-snooping |     |     |     |     |
| ----------- | ------------- | --- | --- | --- | --- |
| vsx-sync    | dhcp-snooping |     |     |     |     |
| no vsx-sync | dhcp-snooping |     |     |     |     |
Description
EnablesVSXsynchronizationofDHCPsnoopingconfigurationsontheprimarynodetothesecondary
peerswitch.
TosynchronizeDHCPsnoopingconfigurationsassociatedwithaparticularVLANandinterface,
configurethesameVLANandinterfaceonthepeerdevice.
ThenoformofthiscommanddisablessyncingDHCPsnoopingconfigurationstothesecondarypeer,
butitdoesnotremovethepreviouslysyncedconfigurationsfromthesecondarypeer.
Examples
EnablingVSXsyncfortheDHCPsnoopingconfigurationstothesecondarypeer:
| switch(config)#     |     | vsx |          |               |     |
| ------------------- | --- | --- | -------- | ------------- | --- |
| switch(config-vsx)# |     |     | vsx-sync | dhcp-snooping |     |
DisablingVSXsyncfortheDHCPsnoopingconfigurationstothesecondarypeer:
| switch(config)#     |          | vsx   |             |               |     |
| ------------------- | -------- | ----- | ----------- | ------------- | --- |
| switch(config-vsx)# |          |       | no vsx-sync | dhcp-snooping |     |
| In the DHCP         | snooping | guard | policy      | context       |     |
EnablingVSX-syncfortheDHCPv6snoopingguardpolicypol:
| switch(config)#                     |     | dhcpv6-snooping |     | guard-policy | po1 |
| ----------------------------------- | --- | --------------- | --- | ------------ | --- |
| switch(config-dhcpv6-guard-policy)# |     |                 |     | vsx-sync     |     |
DisablingVSX-syncfortheDHCPv6snoopingguardpolicypol:
| switch(config)#                     |         | dhcpv6-snooping |     | guard-policy | po1 |
| ----------------------------------- | ------- | --------------- | --- | ------------ | --- |
| switch(config-dhcpv6-guard-policy)# |         |                 |     | no vsx-sync  |     |
| Command                             | History |                 |     |              |     |
VSXcommands|200

| Release             |            |         | Modification       |                                           |
| ------------------- | ---------- | ------- | ------------------ | ----------------------------------------- |
| 10.10               |            |         | Commandintroduced. |                                           |
| Command Information |            |         |                    |                                           |
| Platforms           | Command    | context |                    | Authority                                 |
| 6400                | config-vsx |         |                    | Administratorsorlocalusergroupmemberswith |
8100 config-dhcpv6-guard-policy executionrightsforthiscommand.
8360
8400
| vsx-sync      | evpn |     |     |     |
| ------------- | ---- | --- | --- | --- |
| vsx-sync evpn |      |     |     |     |
| no vsx-sync   | evpn |     |     |     |
Description
EnablessyncingofallEVPNcontext-relatedconfigurationsonprimaryVSXnodetothesecondarypeer
switch.
ThenoformofthiscommanddisablessyncingEVPNconfigurationstothesecondarypeer,butitdoes
notremovethepreviouslysyncedconfigurationsfromthesecondarypeerswitch.
Asaprerequisite,VLANvsx-syncmustbeenabledseparatelyfortheVLANconfigurationsinsideEVPNcontextto
getsynced.
Examples
EnablingVSXsyncfortheEVPNconfigurations:
| switch(config)#             | vlan | 2        |     |     |
| --------------------------- | ---- | -------- | --- | --- |
| switch(config-vlan-2)#      |      | vsx-sync |     |     |
| switch(config)#             | evpn |          |     |     |
| switch(config-evpn)#        |      | vlan 2   |     |     |
| switch(config-evpn-vlan-2)# |      | rd       | 5:5 |     |
switch(config-evpn-vlan-2)#
|                             |     | route-target |      | export 1:1 |
| --------------------------- | --- | ------------ | ---- | ---------- |
| switch(config-evpn-vlan-2)# |     | route-target |      | import 1:1 |
| switch(config)#             | vsx |              |      |            |
| switch(config-vsx)#         |     | vsx-sync     | evpn |            |
DisablingVSXsyncfortheEVPNconfigurations:
| switch(config)#     | vsx |             |              |     |
| ------------------- | --- | ----------- | ------------ | --- |
| switch(config-vsx)# |     | no vsx-sync | evpn         |     |
| Command History     |     |             |              |     |
| Release             |     |             | Modification |     |
| 10.07orearlier      |     |             | --           |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 201

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8100
8320
8325
8360
8400
9300
10000
| vsx-sync          | icmp-tcp |     |     |
| ----------------- | -------- | --- | --- |
| vsx-sync icmp-tcp |          |     |     |
| no vsx-sync       | icmp-tcp |     |     |
Description
EnablesVSXsynchronizationofIPICMPconfigurations,includingip icmp unreachable,ip icmp
redirect,andip icmp throttleconfigurations,onprimaryVSXnodetothesecondarypeer.
ThenoformofthecommanddisablestheVSXsynchronizationofIPICMPconfigurationstothe
secondarypeer.However,itdoesnotremovetheexistingIPICMPconfigurationsfromthesecondary
VSXpeer.
Examples
EnablingVSXsynchronizationforIPICMPconfigurations:
| switch(config)#     | vsx |          |          |
| ------------------- | --- | -------- | -------- |
| switch(config-vsx)# |     | vsx-sync | icmp-tcp |
DisablingVSXsynchronizationforIPICMPconfigurations:
| switch(config)#     | vsx     |             |              |
| ------------------- | ------- | ----------- | ------------ |
| switch(config-vsx)# |         | no vsx-sync | icmp-tcp     |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
VSXcommands|202

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
8325
8360
8400
9300
10000
| vsx-sync          | keychain |     |     |     |
| ----------------- | -------- | --- | --- | --- |
| vsx-sync keychain |          |     |     |     |
| no vsx-sync       | keychain |     |     |     |
Description
EnablessynchronizingofkeychainconfigurationsonprimaryVSXnodetothesecondarypeer.Thereis
noconfigurationsynchronizationfromsecondarytoprimarypeer.
Ifanyadditionalmodificationorconfigurationismadeontheprimaryforthekeychainsetoffeatures,
thefeatureswillbeauto-synchronized.
Thenoformofthecommanddisablessynchronizingkeychainconfigurationstothesecondarypeer.
Butitdoesnotremovethepreviouslysynchronizedconfigurationsfromthesecondarypeer.
Examples
EnablingsynchronizingofkeychainconfigurationsonprimaryVSXnodetothesecondarypeer:
| switch(config)# | keychain | ospf_keys |     |     |
| --------------- | -------- | --------- | --- | --- |
switch(config-keychain)#
key 1
switch(config-keychain-key)# send-lifetime start-time 10:10:10 10/25/2019 end-time
| 10:10:10                     | 11/25/2019 |          |                 |                   |
| ---------------------------- | ---------- | -------- | --------------- | ----------------- |
| switch(config-keychain-key)# |            |          | accept-lifetime | duration infinite |
| switch(config)#              | vsx        |          |                 |                   |
| switch(config-vsx)#          |            | vsx-sync | keychain        |                   |
Disablingsynchronizingkeychainconfigurationstothesecondarypeer:
| switch(config)#     | vsx     |             |              |     |
| ------------------- | ------- | ----------- | ------------ | --- |
| switch(config-vsx)# |         | no vsx-sync | keychain     |     |
| Command History     |         |             |              |     |
| Release             |         |             | Modification |     |
| 10.07orearlier      |         |             | --           |     |
| Command Information |         |             |              |     |
| Platforms           | Command | context     | Authority    |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 203

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8320
8325
8360
8400
9300
10000
| vsx-sync      | lldp |     |     |
| ------------- | ---- | --- | --- |
| vsx-sync lldp |      |     |     |
| no vsx-sync   | lldp |     |     |
Description
EnablesVSXsynchronizationoftheLLDPconfigurationsontheprimaryVSXnodetothesecondary
peer.
ThenoformofthiscommanddisableVSXsynchronizationofLLDPconfigurationstothesecondary
peer,butitdoesnotremovetheexistingLLDPfeatureconfigurationsfromthesecondarypeerswitch.
Examples
ThefirstlineinthefollowingexampleshowsthesettingofanLLDPconfiguration.Thelasttwolinesof
theexampleshowtheenablingofVSXsynchronizationforLLDPconfigurations.
| switch(config)#     |     | lldp reinit | 6    |
| ------------------- | --- | ----------- | ---- |
| switch(config)#     | vsx |             |      |
| switch(config-vsx)# |     | vsx-sync    | lldp |
DisablingVSXsynchronizationofLLDPconfigurations:
| switch(config)#     | vsx     |             |              |
| ------------------- | ------- | ----------- | ------------ |
| switch(config-vsx)# |         | no vsx-sync | lldp         |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
VSXcommands|204

| vsx-sync                     | loop-protect-global |     |     |     |
| ---------------------------- | ------------------- | --- | --- | --- |
| vsx-sync loop-protect-global |                     |     |     |     |
| no vsx-sync                  | loop-protect-global |     |     |     |
Description
EnablestheVSXsynchronizationofgloballoopprotectconfigurations,suchastransmit-intervalandre-
enable-timer,ontheprimaryVSXnodetothesecondarypeerswitch.ToenableVSXsynchronizationat
thecontextlevelforthisfeature,enterthevsx-sync mclag-interfacescommandatthecontextlevel.
ThenoformofthiscommandremovesVSXsynchronizationofgloballoopprotectconfigurations,butit
doesnotremovetheexistinggloballoopprotectfeatureconfigurationsfromthesecondarypeerswitch.
Examples
Thefirsttwolinesinthefollowingexampleshowthesettingofgloballoopprotectconfigurations.The
lasttwolinesoftheexampleshowtheenablingofVSXsynchronizationforgloballoopprotect
configurations.
| switch(config)#     | loop-protect |          | transmit-interval   | 10  |
| ------------------- | ------------ | -------- | ------------------- | --- |
| switch(config)#     | loop-protect |          | re-enable-timer     | 300 |
| switch(config)#     | vsx          |          |                     |     |
| switch(config-vsx)# |              | vsx-sync | loop-protect-global |     |
DisablingVSXsynchronizationofgloballoopprotectconfigurations:
| switch(config)#     | vsx     |             |                     |     |
| ------------------- | ------- | ----------- | ------------------- | --- |
| switch(config-vsx)# |         | no vsx-sync | loop-protect-global |     |
| Command History     |         |             |                     |     |
| Release             |         |             | Modification        |     |
| 10.07orearlier      |         |             | --                  |     |
| Command Information |         |             |                     |     |
| Platforms           | Command | context     | Authority           |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync | mac-lockout |     |     |     |
| -------- | ----------- | --- | --- | --- |
AppliesonlytotheAruba6400SwitchSeries.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 205

| vsx-sync mac-lockout |             |     |     |     |
| -------------------- | ----------- | --- | --- | --- |
| no vsx-sync          | mac-lockout |     |     |     |
Description
EnablesVSXsynchronizationoftheMACLockoutconfigurationsontheprimaryVSXnodetothe
secondarypeer.
ThenoformofthiscommanddisablessyncingMACLockoutconfigurationstothesecondarypeer.
However,itdoesnotremovetheexistingMACLockoutfeatureconfigurationsfromthesecondarypeer.
Examples
EnablingVSXsynchronizationforMACLockoutconfigurations:
| switch(config)#     | mac-lockout |          | 10:10:10:10:10:10 |     |
| ------------------- | ----------- | -------- | ----------------- | --- |
| switch(config)#     | vsx         |          |                   |     |
| switch(config-vsx)# |             | vsx-sync | mac-lockout       |     |
DisablingVSXsynchronizationforMACLockoutconfigurations:
| switch(config)#     | vsx     |             |     |              |
| ------------------- | ------- | ----------- | --- | ------------ |
| switch(config-vsx)# |         | no vsx-sync |     | mac-lockout  |
| Command History     |         |             |     |              |
| Release             |         |             |     | Modification |
| 10.07orearlier      |         |             |     | --           |
| Command Information |         |             |     |              |
| Platforms           | Command | context     |     | Authority    |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| vsx-sync                  | mclag-interfaces |     |     |     |
| ------------------------- | ---------------- | --- | --- | --- |
| vsx-sync mclag-interfaces |                  |     |     |     |
| no vsx-sync               | mclag-interfaces |     |     |     |
Description
EnablestheVSXsynchronizationofVSXLAGinterfaceassociationsandattributesontheprimaryVSX
switchtothesecondarypeerswitch.TheUsagesectioninthistopicprovidesalistingofspecific
associationsandattributesthataresynchronizedtothesecondaryswitch.
ThenoformofthiscommandremovesVSXsynchronizationofglobalVSXLAGandattributes,butit
doesnotremovetheexistingVSXLAGfeatureconfigurationsfromthesecondarypeerswitch.
Usage
TheVSXLAGinterfaceassociationsandattributesthatsupportVSXsynchronizationareforexample:
Interfaceassociations:
VSXcommands|206

n Accesslists
n Policies
QoS
n
n Portaccess
n Portfilters
n Ratelimits
n VLANs
Supportedattributes:
n LAGdescription
n LACP
n Loopprotect
n QoStrust
n sFlow
n STP
ThisconfigurationoverridestheexistingVSXsynchronizationassociationscreatedundertheVSXLAG
interfacecontext.Alsowiththisconfiguration,thesystemblocksfurtherconfigurationofVSX
synchronizationassociationsundertheVSXLAGcontext.
Examples
ThefirstfourlinesinthefollowingexampleshowthecreationandconfigurationofaVSXLAG.Thelast
twolinesoftheexampleshowtheenablingofVSXsynchronizationforVSXLAGinterfaceassociations
andattributes.
| switch(config)#        | interface | lag         | 1 multi-chassis  |         |
| ---------------------- | --------- | ----------- | ---------------- | ------- |
| switch(config-lag-if)# |           | access-list | ip MY_IP_ACL     | in      |
| switch(config-lag-if)# |           | rate-limit  | broadcast        | 50 kbps |
| switch(config-lag-if)# |           | qos trust   | cos              |         |
| switch(config-lag-if)# |           | exit        |                  |         |
| switch(config)#        | vsx       |             |                  |         |
| switch(config-vsx)#    |           | vsx-sync    | mclag-interfaces |         |
DisablingtheVSXsynchronizationofVSXLAGinterfaceassociationsandattributes:
| switch(config)#     | vsx |             |                  |     |
| ------------------- | --- | ----------- | ---------------- | --- |
| switch(config-vsx)# |     | no vsx-sync | mclag-interfaces |     |
Command History
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
Command Information
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 207

| Platforms | Command | context |     | Authority |     |
| --------- | ------- | ------- | --- | --------- | --- |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --------------- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync             | nd-snooping |     |     |     |     |
| -------------------- | ----------- | --- | --- | --- | --- |
| vsx-sync nd-snooping |             |     |     |     |     |
| no vsx-sync          | nd-snooping |     |     |     |     |
Description
EnablesVSXsynchronizationofNDsnoopingconfigurationsontheprimaryVSXnodetothesecondary
peerswitch.
TosynchronizeNDsnoopingconfigurationsassociatedwithaparticularVLANandinterface,configure
thesameVLANandinterfaceonthepeerdevice.
WhenRAguardpolicyisenabled,thiscommandalsosynchronizesRAguardpolicyrelated
configurations.
ThenoformofthiscommanddisablessyncingNDsnoopingconfigurationstothesecondarypeer,but
itdoesnotremovethepreviouslysyncedconfigurationsfromthesecondarypeer.
Examples
EnablingVSXsyncfortheNDsnoopingconfigurationstothesecondarypeer:
| switch(config)#        |     | interface   | 1/1/3       |             |            |
| ---------------------- | --- | ----------- | ----------- | ----------- | ---------- |
| switch(config-if)#     |     | no routing  |             |             |            |
| switch(config-if)#     |     | nd-snooping |             | trust       |            |
| switch(config)#        |     | vlan 2      |             |             |            |
| switch(config-vlan-2)# |     |             | nd-snooping |             |            |
| switch(config-vlan-2)# |     |             | nd-snooping | ra-drop     |            |
| switch(config-vlan-2)# |     |             | nd-snooping | prefix-list | 2001::2/64 |
| switch(config)#        |     | vsx         |             |             |            |
| switch(config-vsx)#    |     | vsx-sync    |             | nd-snooping |            |
DisablingVSXsyncfortheNDsnoopingconfigurationstothesecondarypeer:
| switch(config)#     |     | vsx |          |              |     |
| ------------------- | --- | --- | -------- | ------------ | --- |
| switch(config-vsx)# |     | no  | vsx-sync | nd-snooping  |     |
| Command History     |     |     |          |              |     |
| Release             |     |     |          | Modification |     |
| 10.07orearlier      |     |     |          | --           |     |
| Command Information |     |     |          |              |     |
VSXcommands|208

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| vsx-sync          | neighbor |     |     |
| ----------------- | -------- | --- | --- |
| vsx-sync neighbor |          |     |     |
| no vsx-sync       | neighbor |     |     |
Description
EnablesVSXsynchronizationofIPv4andIPv6staticneighborsconfigurationonprimaryVSXnodetothe
secondarypeer.Thereisnoconfigurationsyncfromsecondarytoprimarypeer.Ifanynewmodification
oradditionalconfigurationismadeontheprimarynodeforIPv4andIPv6staticneighbors
configuration,theywillbeauto-synced.
ThenoformofthiscommandVSXsynchronizationofIPv4andIPv6staticneighborsconfigurationsto
thesecondarypeer,butitdoesnotremovethepreviouslysyncedconfigurationsfromthesecondary
peerswitch.
Examples
EnablingVSXsyncfortheIPv4andIPv6staticneighborsconfigurations:
| DUT-1 (config-vsx)# |         | show run             | in vlan127            |
| ------------------- | ------- | -------------------- | --------------------- |
| interface           | vlan127 |                      |                       |
|                     | ip      | address 137.1.1.1/16 |                       |
|                     | ipv6    | address 7f00::1/64   |                       |
|                     | arp     | ipv4 137.1.1.35      | mac 00:12:01:00:00:1a |
|                     | arp     | ipv4 137.1.1.70      | mac 00:12:01:00:00:3d |
exit
DUT-1(config-vsx)
| switch(config)#     | vsx |          |          |
| ------------------- | --- | -------- | -------- |
| switch(config-vsx)# |     | vsx-sync | neighbor |
DisablingVSXsyncfortheIPv4andIPv6staticneighborsconfigurations:
| switch(config)#     | vsx |             |              |
| ------------------- | --- | ----------- | ------------ |
| switch(config-vsx)# |     | no vsx-sync | neighbor     |
| Command History     |     |             |              |
| Release             |     |             | Modification |
| 10.07orearlier      |     |             | --           |
| Command Information |     |             |              |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 209

| Platforms | Command |     | context |     | Authority |     |     |     |
| --------- | ------- | --- | ------- | --- | --------- | --- | --- | --- |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync      | ospf |     |     |     |     |     |     |     |
| ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| vsx-sync ospf |      |     |     |     |     |     |     |     |
| no vsx-sync   | ospf |     |     |     |     |     |     |     |
Description
EnablessyncingofOSPF(includingOSPFv2andOPSFv3),routemap,andkeychainconfigurationson
theprimaryVSXswitch.Thereisnoconfigurationsyncfromsecondarytoprimarypeer.
TosynchronizeOSPFconfigurationsattheportlevelcontext,configurethesameportonthepeer
device.
ThenoformofthiscommanddisablessyncingofOSPF,routemap,andkeychainconfigurationstothe
secondarypeer.Butitdoesnotremovethepreviouslysyncedconfigurationsfromthesecondarypeer
switch.
TheOSPFrouterIDisnotsynchronized.ThisexclusionisneededbecausetherouterIDuniquelyidentifiesthe
router.ThetwoOSPFrouterswiththesamerouterIDdonotformanadjacencybetweenthem.
Examples
EnablingVSXsyncfortheOSPFconfigurationstothesecondarypeer:
| switch(config)#          |     | router   | ospf         | 1              |            |     |            |      |
| ------------------------ | --- | -------- | ------------ | -------------- | ---------- | --- | ---------- | ---- |
| switch(config-ospf-1)#   |     |          | area         | 0              |            |     |            |      |
| switch(config-ospf-1)#   |     |          | area         | 1 nssa         |            |     |            |      |
| switch(config-ospf-1)#   |     |          | area         | 2 stub         |            |     |            |      |
| switch(config-ospf-1)#   |     |          | redistribute |                | connected  |     | route-map  | map1 |
| switch(config)#          |     | router   | ospfv3       | 1              |            |     |            |      |
| switch(config-ospfv3-1)# |     |          | max-metric   |                | router-lsa |     | on-startup |      |
| switch(config-ospfv3-1)# |     |          | bfd          | all-interfaces |            |     |            |      |
| switch(config-if)#       |     | ip       | ospf         | 1 area         | 0          |     |            |      |
| switch(config-if)#       |     | ip       | ospf         | hello-interval |            | 33  |            |      |
| switch(config-if)#       |     | ipv6     | ospfv3       | 1              | area 0     |     |            |      |
| switch(config-if)#       |     | ipv6     | ospfv3       | dead-interval  |            |     | 55         |      |
| switch(config)#          |     | vsx      |              |                |            |     |            |      |
| switch(config-vsx)#      |     | vsx-sync |              | ospf           |            |     |            |      |
DisablingVSXsyncfortheOSPFconfigurationstothesecondarypeer:
| switch(config)#     |     | vsx |          |      |     |     |     |     |
| ------------------- | --- | --- | -------- | ---- | --- | --- | --- | --- |
| switch(config-vsx)# |     | no  | vsx-sync | ospf |     |     |     |     |
| Command History     |     |     |          |      |     |     |     |     |
VSXcommands|210

| Release             |         |         | Modification |     |
| ------------------- | ------- | ------- | ------------ | --- |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync               | policy-global |     |     |     |
| ---------------------- | ------------- | --- | --- | --- |
| vsx-sync policy-global |               |     |     |     |
| no vsx-sync            | policy-global |     |     |     |
Description
EnablesVSXsynchronizationofglobalclassifierpolicyconfigurationsontheprimaryVSXnodetothe
secondarypeerswitch.
ThenoformofthiscommanddisablesVSXsynchronizationofglobalpolicyconfigurationstothe
secondarypeer,butitdoesnotremovethepreviouslysyncedconfigurationsfromthesecondarypeer
switch.
Examples
EnablingVSXsyncfortheglobalpolicyconfigurationstothesecondarypeer:
switch(config)#
|                     | apply | policy   | testPolicy    | in  |
| ------------------- | ----- | -------- | ------------- | --- |
| switch(config)#     | vsx   |          |               |     |
| switch(config-vsx)# |       | vsx-sync | policy-global |     |
DisablingVSXsyncfortheglobalpolicyconfigurationstothesecondarypeer:
| switch(config)#     | vsx |             |               |     |
| ------------------- | --- | ----------- | ------------- | --- |
| switch(config-vsx)# |     | no vsx-sync | policy-global |     |
| Command History     |     |             |               |     |
| Release             |     |             | Modification  |     |
| 10.07orearlier      |     |             | --            |     |
| Command Information |     |             |               |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 211

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| vsx-sync            | ptp-global |     |     |     |
| ------------------- | ---------- | --- | --- | --- |
| vsx-sync ptp-global |            |     |     |     |
| no vsx-sync         | ptp-global |     |     |     |
Description
EnablessynchronizationofPrecisionTimeProtocol(PTP)configurationontheVSX peerswitch.
ThenoformofthiscommanddisablesthesynchronizationofPTPconfigurationontheVSX peerswitch.
However,thiswillnotdeletetheexistingPTPconfigurationonthepeerswitch.
Examples
EnablingVSXsynchronizationforPTPconfiguration:
| switch(config)#     | ptp | profile | 1588v2      |            |
| ------------------- | --- | ------- | ----------- | ---------- |
| switch(config-ptp)# |     | mode    | transparent | end-to-end |
switch(config-ptp)#
exit
| switch(config)#     | vsx |          |            |     |
| ------------------- | --- | -------- | ---------- | --- |
| switch(config-vsx)# |     | vsx-sync | ptp-global |     |
DisablingVSXsynchronizationforPTPconfiguration:
| switch(config)#     | vsx     |             |     |                    |
| ------------------- | ------- | ----------- | --- | ------------------ |
| switch(config-vsx)# |         | no vsx-sync |     | ptp-global         |
| Command History     |         |             |     |                    |
| Release             |         |             |     | Modification       |
| 10.12               |         |             |     | Commandintroduced. |
| Command Information |         |             |     |                    |
| Platforms           | Command | context     |     | Authority          |
8360 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| vsx-sync | qos-global |     |     |     |
| -------- | ---------- | --- | --- | --- |
VSXcommands|212

| vsx-sync qos-global |            |     |     |     |     |
| ------------------- | ---------- | --- | --- | --- | --- |
| no vsx-sync         | qos-global |     |     |     |     |
Description
EnablestheVSXsynchronizationofglobalQoSconfigurations,suchasCoSmap,DSCPmap,andtrust
policy,ontheprimaryVSXnodetothesecondarypeerswitch.ToenableVSXsynchronizationatthe
contextlevelforthisfeature,enterthevsx-sync qoscommandatthecontextlevel.
ThenoformofthiscommandremovesVSXsynchronizationofglobalQoSconfigurations,butitdoes
notremovetheexistingglobalQoSfeatureconfigurationsfromthesecondarypeerswitch.
Examples
ThefirstfivelinesinthefollowingexampleshowthesettingofglobalQoSconfigurations.Thelasttwo
linesoftheexampleshowtheenablingofVSXsynchronizationforglobalQoSconfigurations.
| switch(config)#     | qos | cos-map  | 1    | local-priority   | 0   |
| ------------------- | --- | -------- | ---- | ---------------- | --- |
| switch(config)#     | qos | cos-map  | 0    | local-priority   | 1   |
| switch(config)#     | qos | cos-map  | 2    | local-priority   | 2   |
| switch(config)#     | qos | dscp-map |      | 2 local-priority | 3   |
| switch(config)#     | qos | trust    | dscp |                  |     |
| switch(config)#     | vsx |          |      |                  |     |
| switch(config-vsx)# |     | vsx-sync |      | qos-global       |     |
DisablingVSXsynchronizationofglobalQoSconfigurations:
| switch(config)#     | vsx     |         |          |              |     |
| ------------------- | ------- | ------- | -------- | ------------ | --- |
| switch(config-vsx)# |         | no      | vsx-sync | qos-global   |     |
| Command History     |         |         |          |              |     |
| Release             |         |         |          | Modification |     |
| 10.07orearlier      |         |         |          | --           |     |
| Command Information |         |         |          |              |     |
| Platforms           | Command | context |          | Authority    |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --------------- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync           | route-map |     |     |     |     |
| ------------------ | --------- | --- | --- | --- | --- |
| vsx-sync route-map |           |     |     |     |     |
| no vsx-sync        | route-map |     |     |     |     |
Description
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 213

EnablessyncingofallAsPathlists,communitylists,prefixlists,androutemapconfigurationson
primaryVSXnodetothesecondarypeerswitch.Thereisnoconfigurationsyncfromthesecondaryto
primarypeer.
ThenoformofthiscommanddisablessyncingofAsPathlists,communitylists,prefixlists,androute
mapconfigurationstothesecondarypeer,butitdoesnotremovethepreviouslysyncedconfigurations
fromthesecondarypeerswitch.
Whenvsx-syncforBGPorOSPFisconfigured,routemapconfigurationsaresynchronizedfromprimaryVSXnode
tothesecondarypeerduetothedependencyinconfigurations.
Examples
EnablingVSXsyncfortheroutemapconfigurations:
| switch(config)# |     | ip aspath-list |     | list1 | seq 10 permit | 10  |
| --------------- | --- | -------------- | --- | ----- | ------------- | --- |
switch(config)# ip community-list expanded com1 seq 10 permit 10
switch(config)# ip extcommunity-list standard ext1 seq 10 permit rt 10:4
| switch(config)#                  |     | ip prefix-list |     | pref1 seq | 10 permit   | any     |
| -------------------------------- | --- | -------------- | --- | --------- | ----------- | ------- |
| switch(config)#                  |     | route-map      | rm1 | permit    |             |         |
| switch(config-route-map-rm1-10)# |     |                |     | match     | ip next-hop | 1.1.1.1 |
| switch(config)#                  |     | vsx            |     |           |             |         |
| switch(config-vsx)#              |     | vsx-sync       |     | route-map |             |         |
DisablingVSXsyncfortheroutemapconfigurations:
| switch(config)#     |         | vsx     |          |              |     |     |
| ------------------- | ------- | ------- | -------- | ------------ | --- | --- |
| switch(config-vsx)# |         | no      | vsx-sync | route-map    |     |     |
| Command History     |         |         |          |              |     |     |
| Release             |         |         |          | Modification |     |     |
| 10.07orearlier      |         |         |          | --           |     |     |
| Command Information |         |         |          |              |     |     |
| Platforms           | Command | context |          | Authority    |     |     |
config-vsx
6400 Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- |
8320
8325
8360
8400
9300
10000
| vsx-sync       | sflow |     |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- | --- |
| vsx-sync sflow |       |     |     |     |     |     |
| no vsx-sync    | sflow |     |     |     |     |     |
VSXcommands|214

Description
EnablesVSXsynchronizationofthesFlowconfigurationsontheprimaryVSXnodetothesecondary
peer.
ThenoformofthiscommandremovesVSXsynchronizationofglobalsFlowconfigurations,butitdoes
notremovetheexistingglobalsFlowfeatureconfigurationsfromthesecondarypeerswitch.
Usage
TomaintaincompliancewithsFlowcollectorfunctionalityfornon-VSXtopology,thevsx-sync sflow
commandonprimaryVSXpeerisexpectedtosyncallsFlowconfigurations,exceptfortheagent-ip
configuration.ThisexclusionisrequiredforsFlowcollectorfunctionalitytoworkseamlesslyevenwith
VSXtopology.
Examples
ThefirstlineinthefollowingexampleshowsthesettingofansFlowconfiguration.Thelasttwolinesof
theexampleshowtheenablingofVSXsynchronizationforsFlowconfigurations.
| switch(config)#     | sflow | agent-ip | 10.0.0.100 |
| ------------------- | ----- | -------- | ---------- |
| switch(config)#     | vsx   |          |            |
| switch(config-vsx)# |       | vsx-sync | sflow      |
DisablingVSXsynchronizationofglobalsFlowconfigurations:
| switch(config)#     | vsx     |             |              |
| ------------------- | ------- | ----------- | ------------ |
| switch(config-vsx)# |         | no vsx-sync | sflow        |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| vsx-sync              | sflow-global |     |     |
| --------------------- | ------------ | --- | --- |
| vsx-sync sflow-global |              |     |     |
| no vsx-sync           | sflow-global |     |     |
Description
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 215

EnablesVSXsynchronizationofthesFlowglobalconfigurationsontheprimaryVSXnodetothe
secondarypeer.
ThenoformofthiscommanddisablesVSXsynchronizationofglobalsFlowconfigurations,butitdoes
notremovetheexistingsFlowfeatureconfigurationsfromthesecondarypeerswitch.
Usage
TomaintaincompliancewithsFlowcollectorfunctionalityfornon-VSXtopology,thevsx-sync sflow
commandonprimaryVSXpeerisexpectedtosyncallsFlowconfigurations,exceptfortheagent-ip
configuration.ThisexclusionisrequiredforsFlowcollectorfunctionalitytoworkseamlesslyevenwith
VSXtopology.VSXsyncsonlytheglobalsFLowconfigurationsandnotthesFlowconfigurationsunder
physicalorLAGinterfaces.
Examples
ThefirstlineinthefollowingexampleshowsthesettingofansFlowconfiguration.Thelasttwolinesof
theexampleshowtheenablingofVSXsynchronizationforsFlowconfigurations.
| switch(config)#     | sflow | collector | 1.1.1.1      |
| ------------------- | ----- | --------- | ------------ |
| switch(config)#     | vsx   |           |              |
| switch(config-vsx)# |       | vsx-sync  | sflow-global |
DisablingVSXsynchronizationofglobalsFlowconfigurations:
| switch(config)#     | vsx     |             |              |
| ------------------- | ------- | ----------- | ------------ |
| switch(config-vsx)# |         | no vsx-sync | sflow-global |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
config-vsx
6400 Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| vsx-sync      | snmp |     |     |
| ------------- | ---- | --- | --- |
| vsx-sync snmp |      |     |     |
| no vsx-sync   | snmp |     |     |
Description
VSXcommands|216

EnablesVSXsynchronizationofSNMPconfigurationsontheprimaryVSXnodetothesecondarypeer.
ThenoformofthiscommandremovesVSXsynchronizationofglobalSNMPconfigurations,butitdoes
notremovetheexistingglobalSNMPfeatureconfigurationsfromthesecondarypeerswitch.
Examples
EnablingVSXsynchronizationforSNMPconfiguration:
| switch(config)#     | vsx |          |      |
| ------------------- | --- | -------- | ---- |
| switch(config-vsx)# |     | vsx-sync | snmp |
DisablingVSXsynchronizationforSNMPconfiguration:
| switch(config)#     | vsx     |             |              |
| ------------------- | ------- | ----------- | ------------ |
| switch(config-vsx)# |         | no vsx-sync | snmp         |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| vsx-sync     | ssh |     |     |
| ------------ | --- | --- | --- |
| vsx-sync ssh |     |     |     |
| no vsx-sync  | ssh |     |     |
Description
EnablesVSXsynchronizationofSSHserverconfigurationsontheprimaryVSXnodetothesecondary
peerswitch.
ThenoformofthiscommandremovesVSXsynchronizationofglobalSSHconfigurations,butitdoes
notremovetheexistingglobalSSHfeatureconfigurationsfromthesecondarypeerswitch.
Examples
ThefirstlineinthefollowingexampleshowsthesettingofanSSHserverconfiguration.Thelasttwo
linesoftheexampleshowtheenablingofVSXsynchronizationforSSHserverconfigurations.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 217

| switch(config)# | ssh | certified-algorithms-only |     |
| --------------- | --- | ------------------------- | --- |
switch(config)#
vsx
| switch(config-vsx)# |     | vsx-sync | ssh |
| ------------------- | --- | -------- | --- |
DisablingVSXsynchronizationforglobalSSHserverconfigurations:
| switch(config)#     | vsx     |             |              |
| ------------------- | ------- | ----------- | ------------ |
| switch(config-vsx)# |         | no vsx-sync | ssh          |
| Command History     |         |             |              |
| Release             |         |             | Modification |
| 10.07orearlier      |         |             | --           |
| Command Information |         |             |              |
| Platforms           | Command | context     | Authority    |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| vsx-sync               | static-routes |     |     |
| ---------------------- | ------------- | --- | --- |
| vsx-sync static-routes |               |     |     |
| no vsx-sync            | static-routes |     |     |
Description
EnablesVSXsynchronizationofstaticrouteconfigurationsontheprimaryVSXnodetothesecondary
peerswitch.
ThenoformofthiscommandremovesVSXsynchronizationofglobalstaticrouteconfigurations,butit
doesnotremovetheexistingglobalstaticroutefeatureconfigurationsfromthesecondarypeerswitch.
Examples
EnablingVSXsynchronizationforstaticroutes:
| switch(config)#     | vsx |          |               |
| ------------------- | --- | -------- | ------------- |
| switch(config-vsx)# |     | vsx-sync | static-routes |
DisablingVSXsynchronizationforstaticroutes:
VSXcommands|218

| switch(config)# | vsx |     |     |     |
| --------------- | --- | --- | --- | --- |
switch(config-vsx)#
|                     |         | no vsx-sync | static-routes |     |
| ------------------- | ------- | ----------- | ------------- | --- |
| Command History     |         |             |               |     |
| Release             |         |             | Modification  |     |
| 10.07orearlier      |         |             | --            |     |
| Command Information |         |             |               |     |
| Platforms           | Command | context     | Authority     |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8100
8320
8325
8360
8400
9300
10000
| vsx-sync            | stp-global |     |     |     |
| ------------------- | ---------- | --- | --- | --- |
| vsx-sync stp-global |            |     |     |     |
| no vsx-sync         | stp-global |     |     |     |
Description
EnablestheVSXsynchronizationofglobalSTPconfigurationsontheprimaryVSXnodetothesecondary
peerswitch.Usethevsx-sync mclag-interfacescommandtosynccontextlevelspanningtrees.To
enableVSXsynchronizationatthecontextlevelforthisfeature,enterthevsx-sync mclag-interfaces
commandatthecontextlevel.
ThenoformofthiscommandremovesVSXsynchronizationofglobalSTPconfigurations,butitdoesnot
removetheexistingglobalSTPfeatureconfigurationsfromthesecondarypeerswitch.
Examples
ThefirsttwolinesinthefollowingexampleshowthesettingofglobalSTPconfigurations.Thelasttwo
linesoftheexampleshowtheenablingofVSXsynchronizationforglobalSTPconfigurations.
| switch(config)#     | spanning-tree |          | config-name     | abc |
| ------------------- | ------------- | -------- | --------------- | --- |
| switch(config)#     | spanning-tree |          | config-revision | 1   |
| switch(config)#     | vsx           |          |                 |     |
| switch(config-vsx)# |               | vsx-sync | stp-global      |     |
DisablingVSXsynchronizationofglobalSTPconfigurations:
| switch(config)#     | vsx |             |            |     |
| ------------------- | --- | ----------- | ---------- | --- |
| switch(config-vsx)# |     | no vsx-sync | stp-global |     |
| Command History     |     |             |            |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 219

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| vsx-sync        | telnet |     |     |
| --------------- | ------ | --- | --- |
| vsx-sync telnet |        |     |     |
| no vsx-sync     | telnet |     |     |
Description
EnablesVSXsynchronizationofTelnetserverconfigurationsfromtheprimaryVSXnodetothe
secondarypeer.TosynchronizeTelnetconfigurationsassociatedwithaparticularVRF,youneedto
configurethesameVRFonthepeerdevice.
ThenoformofthecommanddisablesVSXsynchronizationofTelnetserverconfigurationstothe
secondarypeer,however,itdoesnotremovetheexistingTelnetserverconfigurationsfromthe
secondarypeer.
Examples
EnablingVSX synchronizationofTelnetservers:
| switch(config)#     | telnet | server   | vrf main |
| ------------------- | ------ | -------- | -------- |
| switch(config)#     | vsx    |          |          |
| switch(config-vsx)# |        | vsx-sync | telnet   |
DisablingVSX synchronizationofTelnetservers:
| switch(config)#     | vsx |             |                                                      |
| ------------------- | --- | ----------- | ---------------------------------------------------- |
| switch(config-vsx)# |     | no vsx-sync | telnet                                               |
| Command History     |     |             |                                                      |
| Release             |     |             | Modification                                         |
| 10.11               |     |             | Commandintroducedonthe8320,8325,8360,8400,9300,10000 |
SwitchSeries.
| 10.08.1000 |     |     | Commandintroducedonthe6400SwitchSeries. |
| ---------- | --- | --- | --------------------------------------- |
VSXcommands|220

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8100
8320
8325
8360
8400
9300
10000
| vsx-sync      | time |     |     |
| ------------- | ---- | --- | --- |
| vsx-sync time |      |     |     |
| no vsx-sync   | time |     |     |
Description
EnablesVSXsynchronizationoftime-relatedconfigurations,includingNTPandtimezoneconfigurations,
ontheprimaryVSXnodeonthesecondarypeerswitch.
ThenoformofthiscommandremovesVSXsynchronizationofglobaltime-relatedconfigurations,butit
doesnotremovetheexistingglobaltime-relatedfeatureconfigurationsfromthesecondarypeer
switch.
Examples
Thefirsttwolinesinthefollowingexampleshowthesettingoftime-relatedconfigurations.Thelasttwo
linesoftheexampleshowtheenablingofVSXsynchronizationfortime-relatedconfigurations.
| switch(config)#     | ntp   | authentication |      |
| ------------------- | ----- | -------------- | ---- |
| switch(config)#     | clock | timezone       | utc  |
| switch(config)#     | vsx   |                |      |
| switch(config-vsx)# |       | vsx-sync       | time |
DisablingVSXsynchronizationfortime-relatedconfigurations:
| switch(config)#     | vsx |             |              |
| ------------------- | --- | ----------- | ------------ |
| switch(config-vsx)# |     | no vsx-sync | time         |
| Command History     |     |             |              |
| Release             |     |             | Modification |
| 10.07orearlier      |     |             | --           |
| Command Information |     |             |              |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 221

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| vsx-sync               | udp-forwarder |     |     |
| ---------------------- | ------------- | --- | --- |
| vsx-sync udp-forwarder |               |     |     |
| no vsx-sync            | udp-forwarder |     |     |
Description
EnablesVSXsynchronizationofUDPforwarderconfigurationsontheprimaryVSXnodetothe
secondarypeer.
ThenoformofthecommanddisablestheVSXsynchronizationofUDPforwarderconfigurationstothe
secondarypeer;however,itdoesnotremovetheexistingudp-forwarderconfigurationsfromthe
secondaryVSXpeer.
Examples
EnablingVSXsynchronizationforUDPforwarderconfigurations:
| switch(config)#     | vsx |          |               |
| ------------------- | --- | -------- | ------------- |
| switch(config-vsx)# |     | vsx-sync | udp-forwarder |
DisablingVSXsynchronizationforUDPforwarderconfigurations:
| switch(config)#     | vsx     |             |               |
| ------------------- | ------- | ----------- | ------------- |
| switch(config-vsx)# |         | no vsx-sync | udp-forwarder |
| Command History     |         |             |               |
| Release             |         |             | Modification  |
| 10.07orearlier      |         |             | --            |
| Command Information |         |             |               |
| Platforms           | Command | context     | Authority     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
VSXcommands|222

| Platforms | Command |     | context | Authority |     |
| --------- | ------- | --- | ------- | --------- | --- |
9300
10000
| vsx-sync      | vrrp |     |     |     |     |
| ------------- | ---- | --- | --- | --- | --- |
| vsx-sync vrrp |      |     |     |     |     |
| no vsx-sync   | vrrp |     |     |     |     |
Description
EnablesVSXsynchronizationofallVRRPconfigurationsontheprimaryVSXnodetothesecondarypeer
switch.Thereisnoconfigurationsyncfromsecondarytoprimarypeer.
TosynchronizeVRRPconfigurationsattheportlevelcontext,thesameportmustbeconfiguredonthe
peerdevicewithIPaddress.
ThenoformofthiscommanddisablessyncingVRRPconfigurationstothesecondarypeer,butitdoes
notremovethepreviouslysyncedconfigurationsfromthesecondarypeer.
BFDIPistheIPaddressofVRRPpeerdevice.Henceitcannotbesynced.
Intheownerscenario,incasethepriorityissynced,bothVSXprimaryandsecondarydeviceswillhave255as
theirpriority.Iftheprimarydevicegoesdownandcomesupagain,thesecondarydevicewillstillactastheActive
inspiteoftheprimarydevicebeingtheowner.Henceprioritycannotbesynced.
Examples
EnablingVSXsyncfortheVRRPconfigurationstothesecondarypeer:
| switch(config)#         |     | router   | vrrp enable      |           |         |
| ----------------------- | --- | -------- | ---------------- | --------- | ------- |
| switch(config-if)#      |     | vrrp     | 1 address-family |           | ipv4    |
| switch(config-if-vrrp)# |     |          | address          | 1.1.1.100 | primary |
| switch(config-if-vrrp)# |     |          | timers           | advertise | 1000    |
| switch(config-if-vrrp)# |     |          | no shutdown      |           |         |
| switch(config-if)#      |     | vrr      | 1 address-family |           | ipv6    |
| switch(config)#         |     | vsx      |                  |           |         |
| switch(config-vsx)#     |     | vsx-sync |                  | vrrp      |         |
DisablingVSXsyncfortheVRRPconfigurationstothesecondarypeer:
switch(config)#
| switch(config-vsx)# |     | no  | vsx-sync | vrrp |     |
| ------------------- | --- | --- | -------- | ---- | --- |
| Command History     |     |     |          |      |     |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 223

| Release        |             |     |         |     | Modification |
| -------------- | ----------- | --- | ------- | --- | ------------ |
| 10.07orearlier |             |     |         |     | --           |
| Command        | Information |     |         |     |              |
| Platforms      | Command     |     | context |     | Authority    |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
| vsx-sync    | vsx-global |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | --- |
| vsx-sync    | vsx-global |     |     |     |     |
| no vsx-sync | vsx-global |     |     |     |     |
Description
EnablesVSXsynchronizationofglobalVSXconfigurationsontheprimaryVSXnodetothesecondary
peer.
ThenoformofthecommanddisablesVSXsynchronizationofglobalVSXconfigurationstothe
secondarypeer;however,itdoesnotremovetheexistingVSXfeatureconfigurationsfromthe
secondarypeer.
Usage
ThefollowingcommandsaresyncedfromprimaryVSXnodetosecondaryVSXnode:
| n inter-switch-link |     | dead-interval  |     |                 | <DEAD-INTERVAL>  |
| ------------------- | --- | -------------- | --- | --------------- | ---------------- |
| n inter-switch-link |     | hello-interval |     |                 | <HELLO-INTERVAL> |
| n inter-switch-link |     | hold-time      |     | <HOLD-INTERVAL> |                  |
n inter-switch-link peer-detect-interval <PEER-DETECT-INTERVAL>
| keepalive | dead-interval |     | <DEAD-INTERVAL> |     |     |
| --------- | ------------- | --- | --------------- | --- | --- |
n
| keepalive | hello-interval |     |     | <HELLO-INTERVAL> |     |
| --------- | -------------- | --- | --- | ---------------- | --- |
n
| n keepalive          | udp-port | <PORT-NUM>    |     |     |     |
| -------------------- | -------- | ------------- | --- | --- | --- |
| n linkup-delay-timer |          | <DELAY-TIMER> |     |     |     |
n split-recovery
| n system-mac | <MAC-ADDR> |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- |
Examples
ThefirstthreelinesinthefollowingexampleshowthesettingofglobalVSXconfigurations.Thelastline
intheexampleshowstheenablingofVSXsynchronizationforglobalVSXconfigurations.
VSXcommands|224

| switch(config)# | vsx |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
switch(config-vsx)#
|                     |     | inter-switch-link |            | dead-interval  |     | 15  |
| ------------------- | --- | ----------------- | ---------- | -------------- | --- | --- |
| switch(config-vsx)# |     | inter-switch-link |            | hello-interval |     | 2   |
| switch(config-vsx)# |     | inter-switch-link |            | hold-time      | 1   |     |
| switch(config-vsx)# |     | vsx-sync          | vsx-global |                |     |     |
DisablingVSXsynchronizationforglobalVSXconfigurations:
| switch(config)#     | vsx     |             |              |     |     |     |
| ------------------- | ------- | ----------- | ------------ | --- | --- | --- |
| switch(config-vsx)# |         | no vsx-sync | vsx-global   |     |     |     |
| Command History     |         |             |              |     |     |     |
| Release             |         |             | Modification |     |     |     |
| 10.07orearlier      |         |             | --           |     |     |     |
| Command Information |         |             |              |     |     |     |
| Platforms           | Command | context     | Authority    |     |     |     |
6400 config-vsx Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --------------- | --- | --- | --- |
8320
8325
8360
8400
9300
10000
vsx update-software
| vsx update-software |     | <REMOTE-URL> | [vrf | <VRF-NAME>] |     |     |
| ------------------- | --- | ------------ | ---- | ----------- | --- | --- |
Description
Thiscommandletsyouupdatethesoftware.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<REMOTE-URL> SpecifiestheTFTPURLfordownloadingthesoftware.Syntax:
tftp://{<IP-ADDRESS>|<HOSTNAME>}[:<PORT>]
[;blocksize=<VAL>]/<FILE-NAME>
vrf <VRF-NAME>
SpecifiestheVRFnamefordownloadingthesoftware.Optional
Usage
Thiscommandgivesyoutheoptiontosavetherunningconfigurationontheprimaryandsecondary
VSXswitches.Afterthecommandsavestherunningconfiguration,itdownloadsnewsoftwarefromthe
TFTPserverandverifiesthedownload.Afterasuccessfulverification,thecommandinstallsthesoftware
tothealternativeimageofboththeVSXprimaryandsecondaryswitches.
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 225

ThecommanddisplaysthestatusoftheVSXprimaryandsecondaryswitchesduringtheupgrade.The
commandalsorefreshestheprogressbarastheimageupdateprogresses.DonotinterrupttheVSX
primaryCLIsessionuntilthesoftwareupdatescompletes;however,softwareupdateprocesscanbe
stopped.Ifyoustoptheupgradewhenthesecondaryswitchhasalreadyinstalledtheimageinitsflash
memoryorthesecondaryswitchhasstartedthereboottheprocess,itcomesupwiththenewsoftware.
Theprimaryswitchcontinuestohavewitholdersoftware.Youcanstopthesoftwareupdateprocessby
pressingctrl+c.
Example
UpdatingthesoftwareusingTFTP:
switch# vsx update-software tftp://192.168.1.1/XL.10.0x.xxxx vrf mgmt
| Do you | want to | save | the | current | configuration |     | (y/n)? | y   |
| ------ | ------- | ---- | --- | ------- | ------------- | --- | ------ | --- |
The running configuration was saved to the startup configuration.
This command will download new software to the %s image of both the VSX primary
and
secondary systems, then reboot them in sequence. The VSX secondary will reboot
| first,   | followed | by  | the | primary. |     |     |     |     |
| -------- | -------- | --- | --- | -------- | --- | --- | --- | --- |
| Continue | (y/n)?   | y   |     |          |     |     |     |     |
VSX Primary Software Update Status : <VSX primary software update status>
VSX Secondary Software Update Status : <VSX secondary software update status>
| VSX ISL | Status |     |     |     |     | : <VSX | ISL | status> |
| ------- | ------ | --- | --- | --- | --- | ------ | --- | ------- |
Progress
[..........................................................................]
| Secondary      | VSX         | system | updated | completely. |              | Rebooting |     | primary. |
| -------------- | ----------- | ------ | ------- | ----------- | ------------ | --------- | --- | -------- |
| Command        | History     |        |         |             |              |           |     |          |
| Release        |             |        |         |             | Modification |           |     |          |
| 10.07orearlier |             |        |         |             | --           |           |     |          |
| Command        | Information |        |         |             |              |           |     |          |
| Platforms      | Command     |        | context |             | Authority    |           |     |          |
6400 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 8100 |     |     |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --- | --- | --------------- | --- | --- | --- |
8320
8325
8360
8400
9300
10000
| vsx update-software |     |           |     | boot-bank |     |              |     |     |
| ------------------- | --- | --------- | --- | --------- | --- | ------------ | --- | --- |
| vsx update-software |     | boot-bank |     | {primary  |     | | secondary} |     |     |
Description
UpgradestheVSXpairsusingthespecifiedbankonboththedevices.Thiscommandcompareswhether
theimageversionsaresameinboththeprimaryandsecondaryswitchesandrebootsthemin
sequence,theVSXsecondaryswitchfollowedbyVSXprimaryswitch.
VSXcommands|226

Beforeexecutingthiscommand,downloadthesoftwareimageandinstallintherequiredbootbanks.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
boot-bank
Specifiesthebootbankwheretheimageispre-staged.
{primary | secondary} SelectseitherprimaryorsecondaryVSXswitchforthesoftware
upgrade.
Usage
Thiscommandgivesyoutheoptiontosavetherunningconfigurationontheprimaryandsecondary
VSXswitches.Afterthecommandsavestherunningconfiguration,itdownloadsnewsoftwarefromthe
TFTPserverandverifiesthedownload.Afterasuccessfulverification,thecommandinstallsthesoftware
tothealternativeimageofboththeVSXprimaryandsecondaryswitches.
ThecommanddisplaysthestatusoftheVSXprimaryandsecondaryswitchesduringtheupgrade.The
commandalsorefreshestheprogressbarastheimageupdateprogresses.DonotinterrupttheVSX
primaryCLIsessionuntilthesoftwareupdatescompletes;however,softwareupdateprocesscanbe
stopped.Ifyoustoptheupgradewhenthesecondaryswitchhasalreadyinstalledtheimageinitsflash
memoryorthesecondaryswitchhasstartedthereboottheprocess,itcomesupwiththenewsoftware.
Theprimaryswitchcontinuestohavewitholdersoftware.Youcanstopthesoftwareupdateprocessby
pressingctrl+c.
Example
Selectingprimarybankforupgrade:
| switch# | vsx update-software | boot-bank                 | primary |     |
| ------- | ------------------- | ------------------------- | ------- | --- |
| Do you  | want to save        | the current configuration | (y/n)?  | y   |
The running configuration was saved to the startup configuration.
This command will upgrade both VSX primary and secondary systems, using pre-staged
image 'X' installed in secondary bank on both devices, then reboot
them in sequence. The VSX secondary will reboot first, followed by primary.
| Continue    | (y/n)? y |               |          |         |
| ----------- | -------- | ------------- | -------- | ------- |
| VSX Primary | Software | Update Status | : Reboot | started |
VSX Secondary Software Update Status : Image updated successfully
| VSX ISL | Status |     | : Up |     |
| ------- | ------ | --- | ---- | --- |
Progress [......................................................................]
| Secondary | VSX system | updated completely. | Rebooting | primary. |
| --------- | ---------- | ------------------- | --------- | -------- |
Selectingsecondarybankforupgrade:
| switch# | vsx update-software | boot-bank                 | secondary |     |
| ------- | ------------------- | ------------------------- | --------- | --- |
| Do you  | want to save        | the current configuration | (y/n)?    | y   |
The running configuration was saved to the startup configuration.
This command will upgrade both VSX primary and secondary systems, using pre-staged
image 'X' installed in secondary bank on both devices, then reboot
them in sequence. The VSX secondary will reboot first, followed by primary.
| Continue    | (y/n)? y |               |          |         |
| ----------- | -------- | ------------- | -------- | ------- |
| VSX Primary | Software | Update Status | : Reboot | started |
VSX Secondary Software Update Status : Image updated successfully
| VSX ISL | Status |     | : Up |     |
| ------- | ------ | --- | ---- | --- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 227

Progress [.......................................................................]
| Secondary      | VSX system  | updated completely. | Rebooting    | primary. |
| -------------- | ----------- | ------------------- | ------------ | -------- |
| Command        | History     |                     |              |          |
| Release        |             |                     | Modification |          |
| 10.07orearlier |             |                     | --           |          |
| Command        | Information |                     |              |          |
| Platforms      | Command     | context             | Authority    |          |
6400 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8100
8320
8325
8360
8400
9300
10000
VSXcommands|228

Chapter 13

Configuration conflict finder
recommendations

Configuration conflict finder recommendations

Configuration Conflict Finder (CCF) is a configuration troubleshooting solution that allows admins and
support to automatically determine switch configuration anomalies using a set of feature configuration
templates. This ensures specific features are error-free and validates the switch's configuration. CCF is
an especially useful tool for CX users, support personnel, and ERT.

CCF detects misconfigurations including:

n Incomplete or inter-dependent configurations

n Mutually exclusive configurations

CCF provides the following recommendations for VSX environments:

n VSX Active gateway and Active forwarding cannot be configured for the same SVI

n VSX Active forwarding configuration is not consistent across VSX peers

n IPv6 subnetmask is not consistent across VSX peers

n IPv4 subnetmask is not consistent across VSX peers

n VSX system MAC should be consistent across VSX peers

n VSX device roles should be different across VSX peers

n VSX ISL hello interval should be consistent across VSX peers

n VSX ISL dead interval should be consistent across VSX peers

n VSX ISL peer detect interval should be consistent across VSX peers

n VSX Keepalive UDP port should be consistent across VSX peers

n VSX Keepalive dead interval should be consistent across VSX peers

n VSX Keepalive hello interval should be consistent across VSX peers

n Link up delay timers should be consistent across VSX peers

n Link up delay timer exclude LAG should be consistent across VSX peers

n Configuration-sync should be consistent across VSX peers

n Split-recovery should be consistent across VSX peers

n Active Gateway IP should be consistent across the VSX peers

n Active Gateway MAC should be consistent across the VSX peers

n Active Gateway IPv6 should be consistent across the VSX peers

n Active Gateway IPv6 MAC should be consistent across the VSX peers

n Interface VLAN VRF should be consistent across the VSX peers

n MCLAG should be consistent across VSX peers

n MCLAG LACP mode should be consistent across VSX peers

n MCLAG LACP rate should be consistent across VSX peers

n MCLAG native VLAN should be consistent across VSX peers

n MCLAG allowed VLAN should be consistent across VSX peers

n MCLAG VLAN list should be subset of ISL VLAN list. ALL VLANs on the MCLAG should be there on the

ISL

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide

229

n MCLAGnativeVLANshouldbepartofallowedVLANlist
n ISLnativeVLANshouldbepartofallowedVLANlist
ISLLAGshouldhavememberinterfaceanditshouldbeadministrativelyup
n
n MCLAGshouldhavememberinterfaceanditshouldbeadministrativelyup
n ISLnativeVLANshouldbepartofallowedVLANlist
n VSXISLinterfaceshouldbeadministrativelyup
n VSXISLLAGinterfaceshouldbeadministrativelyup
n RoutingcannotbeenabledonISLorMCLAGinterface
n MultichassisconfigurationisrecommendedforVSXredundancy
n MCLAGnativeVLANtagshouldbeconsistentacrossVSXpeers
n LAGnativeVLANIDshouldbeconsistentacrossVSXpeers
n LAGnativeVLANtagshouldbeconsistentacrossVSXpeers
n InterfacevlannativetagshouldbeconsistentacrossVSXpeers
n LAGLACPmodeshouldbeconsistentacrossVSXpeers
n LAGLACPrateshouldbeconsistentacrossVSXpeers
| Sample            | recommendations |                |     |     |     |
| ----------------- | --------------- | -------------- | --- | --- | --- |
| Active-forwarding |                 | recommendation |     |     |     |
switch#
|     | switch | config-validator |     | mode vsx-sync |     |
| --- | ------ | ---------------- | --- | ------------- | --- |
Line number 83: VSX Active forwarding configuration is not consistent across VSX
peers
| Admin-down  | recommendation |                   |     |               |                |
| ----------- | -------------- | ----------------- | --- | ------------- | -------------- |
| switch#     | switch         | config-validator  |     | mode vsx-sync |                |
| Line number |                | 41: Configuration |     | `no shutdown` | is recommended |
VLAN recommendations
| switch# | show      | run              | | line                |                     |     |
| ------- | --------- | ---------------- | --------------------- | ------------------- | --- |
| 46      |           | lacp             | mode active           |                     |     |
| 47      | interface |                  | lag 128 multi-chassis |                     |     |
| 48      |           | no shutdown      |                       |                     |     |
| 49      |           | no routing       |                       |                     |     |
| 50      |           | vlan             | trunk native          | 1                   |     |
| 51      |           | vlan             | trunk allowed         | 1,1000-1001         |     |
| 52      |           | lacp             | mode active           |                     |     |
| 53      | interface |                  | lag 256               |                     |     |
| 54      |           | no shutdown      |                       |                     |     |
| 55      |           | no routing       |                       |                     |     |
| 56      |           | vlan             | trunk native          | 1 tag               |     |
| 57      |           | vlan             | trunk allowed         | 1000-1001,2001-2512 |     |
| 58      |           | lacp             | mode active           |                     |     |
| switch# | switch    | config-validator |                       | mode vsx-sync       |     |
Line number 51: MCLAG VLAN list should be subset of ISL VLAN list. ALL VLANs on
| the MCLAG | should |     | be there on | the ISL |     |
| --------- | ------ | --- | ----------- | ------- | --- |
Configurationconflictfinderrecommendations|230

Line number 56: LAG native VLAN tag should be consistent across VSX peers
Line number 56: ISL native VLAN should be part of allowed VLAN list
Timer recommendations
| switch# switch | config-validator | mode vsx-sync |
| -------------- | ---------------- | ------------- |
Line number : VSX ISL hello interval should be consistent across VSX peers. Peer
| Line number | 5300 |     |
| ----------- | ---- | --- |
Line number : VSX ISL dead interval should be consistent across VSX peers. Peer
| Line number | 5301 |     |
| ----------- | ---- | --- |
Line number : VSX ISL hold time should be consistent across VSX peers. Peer Line
number 5302
Line number : VSX ISL peer detect interval should be consistent across VSX peers.
| Peer Line number | 5303 |     |
| ---------------- | ---- | --- |
Line number : VSX Keepalive dead interval should be consistent across VSX peers.
| Peer Line number | 5306 |     |
| ---------------- | ---- | --- |
Line number : VSX Keepalive hello interval should be consistent across VSX peers.
| Peer Line number | 5307 |     |
| ---------------- | ---- | --- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 231

Chapter 14
Troubleshooting
Troubleshooting
ThefollowingsectiondescribesfailureandrecoveryscenariosforVSX.
OnallVSXplatforms,Routed-inACLsonlymatchpacketswhenthosepacketsarebothroutedonthatswitchand
thepacketsingresstheVSXpaironthatswitch.Therefore,apacketarrivingviaISLatthesecondVSXnodedoes
nothavearouted-inACLapplied.Inordertoensurepacketsareappropriatelyfilteredbyrouted-inACLs,VSX
pairsshouldbeconfiguredsuchthatbothroutingandrouted-inACLfilteringoccuronthefirstVSXnodethat
packetsenter.
ISL is out-of-sync
Solution 1
Cause
MismatchwiththeISLversionorswitchplatformorboth.
Action
| 1. Runtheshow   | vsx statuscommand. |        |     |     |
| --------------- | ------------------ | ------ | --- | --- |
| switch# show    | vsx                | status |     |     |
| VSX Operational | State              |        |     |     |
---------------------
| ISL channel  |             |                   | : In-Sync          |                   |
| ------------ | ----------- | ----------------- | ------------------ | ----------------- |
| ISL mgmt     | channel     |                   | : operational      |                   |
| Config       | Sync Status |                   | : in-sync          |                   |
| NAE          |             |                   | : peer_unreachable |                   |
| HTTPS Server |             |                   | : peer_unreachable |                   |
| Attribute    |             | Local             |                    | Peer              |
| ------------ |             | --------          |                    | --------          |
| ISL link     |             | 1/1/43            |                    | 1/1/43            |
| ISL version  |             | 2                 |                    | 2                 |
| System MAC   |             | 48:0f:cf:af:70:84 |                    | 48:0f:cf:af:c2:84 |
| Platform     |             | 8320              |                    | 8320              |
| Software     | Version     | 10.0x.xxxx        |                    | 10.0x.xxxx        |
| Device Role  |             | primary           |                    | secondary         |
Inthefollowingexample,theISLchannelisshownasin-sync;however,iftheISLchannelwasnot
in-sync,adifferentstatuswouldbeprovided.
| switch(config)#   | user | admin | password |     |
| ----------------- | ---- | ----- | -------- | --- |
| Changing password | for  | user  | admin    |     |
Enter password:************
Confirm password:************
232
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide

2. IfthereisanISLversionmismatch,updatethesoftwaresotheISLversionisthesameonthe
localandpeerVSXswitch.
3. Iftheswitcheshavemismatchingplatforms,createanISLlinkthatconnectstwoVSXswitches
withthesameplatform.
| Solution | 2   |     |     |
| -------- | --- | --- | --- |
Cause
TheroleisnotconfiguredonanyoftheVSXswitchesorthesameroleisconfiguredonbothVSX
switches.
Action
| 1.  | Runtheshow | vsx statuscommand. |     |
| --- | ---------- | ------------------ | --- |
Iftherolesaresetincorrectly,thecommanddisplaystherole inconsistentstatus.
2. SettherolescorrectlysothatoneoftheVSXswitcheshastheprimaryroleandtheotherswitch
hasthesecondaryrole.Tosetaswitchrole,entertherole {primary | secondary}command.
| Solution | 3   |     |     |
| -------- | --- | --- | --- |
Cause
TheISLinterfaceisdownonanyoneswitchintheVSXpair.
Action
1. CheckISLstateandISLlinkstatusbyentering:switch#
show vsx status inter-switch-link
switch#
|     | show         | vsx status      | inter-switch-link |
| --- | ------------ | --------------- | ----------------- |
|     | State        |                 | : In-Sync         |
|     | Link Status  |                 | : up              |
|     | Mgmt state   |                 | : operational     |
|     | Inter-switch | link Statistics |                   |
----------------------------
|     | Hello Packets | Tx    | : 4572  |
| --- | ------------- | ----- | ------- |
|     | Hello Packets | Rx    | : 4573  |
|     | Data Packets  | Tx    | : 80634 |
|     | Data Packets  | Rx    | : 80637 |
|     | Mgmt Packets  | Tx    | : 25946 |
|     | Mgmt Packets  | Rx    | : 25167 |
|     | Mgmt Packet   | Drops | : 0     |
Inthefollowingexample,theISLstateandlinkstatusareshownasin-syncandup;however,if
theISLinterfaceisdown,adifferentstatuswouldbeprovided.
2. Re-enabletheISLinterfacebygoingtothatinterfacecontextandenteringno shutdown:
|     | switch(config)# | interface | 1/1/1 |
| --- | --------------- | --------- | ----- |
switch(config-if)#
| ISL is | in blocking | state |     |
| ------ | ----------- | ----- | --- |
Troubleshooting|233

Symptom

The VSX LAGs are shown as Blocking in the output of the show spanning-tree detail command.

switch# show spanning-tree detail
Spanning tree status : Enabled Protocol: MSTP

MST0
Root ID Priority : 32768

MAC-Address: 02:02:02:02:02:02
This bridge is the root
Hello time (in seconds):2 Max Age (in seconds):20
Forward Delay (in seconds):15

Bridge ID Priority: 32768

MAC-Address: 02:02:02:02:02:02
Hello time (in seconds):2 Max Age (in seconds):20
Forward Delay (in seconds):15

Role

State

Port
------ -------- -------- ------ -------- -------
lag1
Disabled Blocking 20000
lag100 Disabled Blocking 20000

Priority Type

shared
shared

64
64

Cost

Topology change flag : False
Number of topology changes : 0
Last topology change occurred: 3876 seconds ago
Timers: Hello expiry 0, Forward delay expiry 0

Port lag1 id 321
Designated root has priority : 32768 Address: 02:02:02:02:02:02
Designated bridge has priority : 32768 Address: 02:02:02:02:02:02
Designated port id : 0
Multi-Chassis role : active

Number of transitions to forwarding state: 0
Bpdus sent 0, received 0

Port lag100 id 420
Designated root has priority : 32768 Address: 02:02:02:02:02:02
Designated bridge has priority : 32768 Address: 02:02:02:02:02:02
Designated port id : 0
Number of transitions to forwarding state: 0
Bpdus sent 0, received 0

Cause

n Mismatch MSTP configurations on VSX peer switches.

n Switches are not in the same MSTP region within the VSX environment.

n STP configurations on VSX LAG ports must be the same on VSX switches.

n The VSX pair is configured as a nonroot switch.

Action

1. Run the following commands for determining what is causing the ISL to be in a blocking state:

switch# show running-config spanning-tree
switch# show spanning-tree mst-config
switch# show vsx status

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

234

When you run the show vsx status command, verify that the ISL is in-sync.

2. Verify that the VSX peer switches are in the active and standby role when the ISL is the in-sync

state by entering the show spanning-tree detail command:

switch# show spanning-tree detail
Spanning tree status : Enabled Protocol: MSTP

MST0
Root ID Priority : 32768

MAC-Address: 02:02:02:02:02:02
This bridge is the root
Hello time (in seconds):2 Max Age (in seconds):20
Forward Delay (in seconds):15

Bridge ID Priority: 32768

MAC-Address: 02:02:02:02:02:02
Hello time (in seconds):2 Max Age (in seconds):20
Forward Delay (in seconds):15

Role

State

Port
------ -------- -------- ------ -------- -------
Disabled Blocking 20000
lag1
lag100 Disabled Blocking 20000

Priority Type

shared
shared

64
64

Cost

Topology change flag : False
Number of topology changes : 0
Last topology change occurred: 3876 seconds ago

Timers: Hello expiry 0, Forward delay expiry 0

Port lag1 id 321
Designated root has priority : 32768 Address: 02:02:02:02:02:02
Designated bridge has priority : 32768 Address: 02:02:02:02:02:02
Designated port id : 0
Multi-Chassis role : active
Number of transitions to forwarding state: 0
Bpdus sent 0, received 0

3. Verify if MSTP configurations are the same on the VSX peer switches by entering the following

commands:

switch# show running-config spanning-tree
switch# show running-config spanning-tree vsx-peer

4.

In a converged network, if any of MSTP ports are disabled by loop protect because different
instances have different root switches, remove loop protect configuration from those ports.

5. Preferably, enable loop-protect on only edge ports or ports connected to STP unaware switches.

The admin path cost configured on downstream switches results in the VSX pair seeing the root switch
as equal cost to the root switch from both VSX pair switches.

Traffic drop on a VSX LAG interface

Take the following actions:

Troubleshooting | 235

1. VerifythattheVSXLAGinterfaceisin-syncwithbothpeeranddownstreamswitchesbyentering:
|     | switch# show | lacp interfaces | multi-chassis |
| --- | ------------ | --------------- | ------------- |
2. VerifythattheVLANmembershipoftheVSXisthesameonbothVSXswitchesbyentering:
|     | switch# show | vsx config-consistency | lacp <LAG-NAME> |
| --- | ------------ | ---------------------- | --------------- |
3. VerifythatallMACaddressesareprogrammedcorrectlyonbothVSXswitchesbyentering:
|     | switch# show | mac-address-table |       |
| --- | ------------ | ----------------- | ----- |
|     | switch# show | mac-address-table | count |
Traffic loss after the ISL has been out-of-sync and keepalive
is down
Symptom
TrafficlossisseenaftertheISLhasbeenout-of-syncandkeepaliveisdown.
Cause
IftheISLbecomesout-of-syncandkeepaliveisestablished,thesecondaryVSXLAGsarebroughtdown.
Ifkeepalivethenfailsandyouhavesplitrecoverymodeenabled(defaultsetting),thesecondaryswitch
bringsupitsVSXLAGs.Thissplitconditionleadstotrafficlossbecauseoftheasymmetrictrafficflow.
Action
1. DisablesplitrecoverymodebyenteringthefollowingcommandonthesecondaryVSXswitch:
|     | switch(config)#     | vsx               |     |
| --- | ------------------- | ----------------- | --- |
|     | switch(config-vsx)# | no split-recovery |     |
Thiscommandshutsdownthesecondarylinktostoptheasymmetrictrafficflow.
2. ApplythesamesettingontheprimaryVSXswitchforconsistencyandincasethereisa
primary/secondaryroleswapintheconfiguration.
| Failure | scenarios       | and split | recovery |
| ------- | --------------- | --------- | -------- |
| Figure1 | ExampleTopology |           |          |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 236

Table 1: Failure Scenarios

Failure scenarios

Result with split recovery
off

Result with split recovery on
(default)

Keepalive is down and ISL is up. This
scenario is shown with label "b" in
the figure.

No impact, except for the loss

of the split detection.

No impact, except for the loss of the
split detection.

ISL is down, but keepalive is up. This
scenario is shown with label "a" in
the figure.

Secondary VSX switch brings

down VSX LAG member ports.

Secondary VSX switch brings down
VSX LAG member ports.

ISL is down, but keepalive is up, as
shown with label "a" in the figure.
Then, after sometime, keepalive also
goes down, as shown with label b.

Secondary VSX switch brings

Label a: The secondary VSX switch

down VSX LAG member ports.

brings down VSX LAG member ports.

Then, the secondary VSX LAGs

stay down.

Label b: The secondary VSX switch

restores VSX LAG member ports.

At the same time, ISL goes down and
keepalive goes down, as shown with
label "a" and "b" in the following
figure. Then, keepalive is restored, as
shown with label b.

Label a and b: All VSX LAG ports

Label a and b: All VSX LAG ports stay

stay up.

up.

Label b: Then, the secondary

Label b: Then, the secondary VSX

VSX switch brings down the

switch brings down the VSX LAG

VSX LAG member ports.

member ports.

Active gateway is unreachable

Symptom

You are unable to ping the active gateway.

Action

Troubleshooting | 237

1. Verifythatkernelinterfaceiscreatedforactivegateway:
003000000000001@vlan3: <NO-CARRIER,BROADCAST,UP,M-DOWN> mtu 1500 qdisc
|     | noqueue        | state      |                   |         |      |      |                   |     |     |
| --- | -------------- | ---------- | ----------------- | ------- | ---- | ---- | ----------------- | --- | --- |
|     | LOWERLAYERDOWN |            | group             | default | qlen | 1000 |                   |     |     |
|     |                | link/ether | 00:00:00:00:00:01 |         |      | brd  | ff:ff:ff:ff:ff:ff |     |     |
2. VerifythattheactivegatewayIPisprogrammedcorrectlyonkernelinterface:
003000000000001@vlan3: <NO-CARRIER,BROADCAST,UP,M-DOWN> mtu 1500 qdisc
|     | noqueue        | state            |                   |               |        |                 |                   |     |     |
| --- | -------------- | ---------------- | ----------------- | ------------- | ------ | --------------- | ----------------- | --- | --- |
|     | LOWERLAYERDOWN |                  | group             | default       | qlen   | 1000            |                   |     |     |
|     |                | link/ether       | 00:00:00:00:00:01 |               |        | brd             | ff:ff:ff:ff:ff:ff |     |     |
|     |                | inet 10.0.0.3/32 |                   | scope         | global | 003000000000001 |                   |     |     |
|     |                | valid_lft        | forever           | preferred_lft |        |                 | forever           |     |     |
|     |                | inet 20.0.0.3/32 |                   | scope         | global | 003000000000001 |                   |     |     |
|     |                | valid_lft        | forever           | preferred_lft |        |                 | forever           |     |     |
3. VerifythattheactivegatewayVMACiscorrectlyconfiguredinthehardware.Thecommandused
isplatform-specific.Refertothehardwaredocumentationforyourswitch.
Thefollowingexamplefromthe8400seriesswitch:
|     | 8400X:/home/admin# |     |     | ovs-appctl | l3pd/show |      | router-mac | –a      |           |
| --- | ------------------ | --- | --- | ---------- | --------- | ---- | ---------- | ------- | --------- |
| BFD | reports            | a   | LAG | as down    |           | even | when       | healthy | links are |
still available
Symptom
TheBidirectionalForwardDetection(BFD)featurereportsaLinkAggregation(LAG),asbeingdown,even
thoughtherearehealthyLAGlinksavailable.TheLAG,containingthedownedlink,willeventually
rebalancethetraffictoitsotherlinks.
Cause
ThisnotificationoccurswhentheminimumBFDcontrolpacketreceptionintervalissetatafasterrate
thantheLinkAggregationControlProtocol(LACP)rateandLAGrebalancingoccurs.BFDassumesthat
thelinkisdownwithoutrealizingthattheLAGisrebalancingthetrafficload.
Action
1. SettheminimumBFDcontrolpacketreceptionintervaltoaslowerratethantheLACPrateorset
theLACPratetoafasterratethantheminimumBFDcontrolpacketreceptioninterval.
a. TofindthecurrentsettingsoftheminimumBFDcontrolpacketreceptioninterval,enterthe
show running-configcommand.
TheminimumBFDcontrolpacketreceptionintervalsettingislistedasbfd min-receive-
intervalinthecommandoutputandthemeasurementisinms.
b. TofindthecurrentrateofLACP,entertheshow lacp aggregatescommand.
|     | TheLACPrateislistedastheHeatbeat |     |     |     |     | rateinthecommandoutput. |     |     |     |
| --- | -------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | --- |
AOS-CX10.14VirtualSwitchingExtension(VSX)Guide|(6400,8xxx,9300,10000SwitchSeries) 238

c. To change the minimum BFD control packet reception interval, enter the bfd min-receive-

interval command.

d. To change the LACP rate, enter the lacp rate {fast | slow} command.

Troubleshooting | 239

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

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

Airheads social
forums and
Knowledge Base

HPE Aruba
Networking
Hardware
Documentation
and Translations
Portal

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide

240

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
| HPEAruba | https://developer.arubanetworks.com/ |     |
| -------- | ------------------------------------ | --- |
Networking
DeveloperHub
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
(docsfeedback-switching@hpe.com).Whensubmittingyourfeedback,includethedocumenttitle,part
number,edition,andpublicationdatelocatedonthefrontcoverofthedocument.Foronlinehelp
SupportandOtherResources|241

content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.14 Virtual Switching Extension (VSX) Guide | (6400, 8xxx, 9300, 10000 Switch Series)

242