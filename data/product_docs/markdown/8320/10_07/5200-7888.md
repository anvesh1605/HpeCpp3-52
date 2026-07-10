|           | AOS-CX |     | 10.07     | Virtual |       |     |
| --------- | ------ | --- | --------- | ------- | ----- | --- |
| Switching |        |     | Extension |         | (VSX) |     |
Guide
| 6400, | 8320, | 8325, | 8360, | 8400 | Switch | Series |
| ----- | ----- | ----- | ----- | ---- | ------ | ------ |
PartNumber:5200-7888
Published:March2022
Edition:4

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

| 2

Contents
Contents
| Contents                                    |                                                      |                |                 | 3   |
| ------------------------------------------- | ---------------------------------------------------- | -------------- | --------------- | --- |
| About                                       | this document                                        |                |                 | 8   |
| Applicableproducts                          |                                                      |                |                 | 8   |
| Latestversionavailableonline                |                                                      |                |                 | 8   |
| Commandsyntaxnotationconventions            |                                                      |                |                 | 8   |
| Abouttheexamples                            |                                                      |                |                 | 9   |
| Identifyingswitchportsandinterfaces         |                                                      |                |                 | 9   |
| Identifyingmodularswitchcomponents          |                                                      |                |                 | 10  |
| Getting                                     | started with                                         | VSX            |                 | 11  |
| BenefitsofVSX                               |                                                      |                |                 | 11  |
| VSXsolutiontopologyoverview                 |                                                      |                |                 | 12  |
|                                             | SampleVSXsolutiontopology                            |                |                 | 12  |
|                                             | VSXLAG                                               |                |                 | 13  |
|                                             | VSF                                                  |                |                 | 13  |
|                                             | VSFversusVSX                                         |                |                 | 14  |
|                                             | ThecommonsystemMACaddress                            |                |                 | 14  |
| VSXsolutionrequirements                     |                                                      |                |                 | 15  |
| VSXcomponents                               |                                                      |                |                 | 15  |
| Inter-SwitchLink(ISL)                       |                                                      |                |                 | 16  |
|                                             | ISLconfigurations                                    |                |                 | 17  |
| Switchroles                                 |                                                      |                |                 | 18  |
| VSXswitchreboot                             |                                                      |                |                 | 18  |
| Periodicsynchronization                     |                                                      |                |                 | 19  |
| BFDandVSXsupport                            |                                                      |                |                 | 20  |
| Upgrading                                   | to the                                               | latest version | of VSX          | 21  |
| UpgradingVSXfrom10.03orlaterto10.07         |                                                      |                |                 | 21  |
|                                             | Upgradingswitchesbyusingthevsxupdate-softwarecommand |                |                 | 21  |
| Setting                                     | up the VSX                                           | environment    |                 | 24  |
| VSXinthecorelayer                           |                                                      |                |                 | 24  |
| Configuringcore1andcore2forVSX              |                                                      |                |                 | 25  |
| ConfiguringthetwoaggregateVSXswitches       |                                                      |                |                 | 28  |
| ConfiguringanAOS-CXswitchasanaccessswitch   |                                                      |                |                 | 32  |
| Enabling                                    | VSX configuration                                    |                | synchronization | 35  |
| VSXconfigurationsynchronization             |                                                      |                |                 | 35  |
|                                             | FeaturessupportingVSX                                |                |                 | 35  |
|                                             | VSXsynchronizationrequirements                       |                |                 | 35  |
| EnablingVSXsynchronizationatthegloballevel  |                                                      |                |                 | 36  |
| EnablingVSXsynchronizationatthecontextlevel |                                                      |                |                 | 42  |
EnablingVSXsynchronizationofSTPconfigurationsbetweenVSXpeerswitches 44
| Monitoring                                            | the VSX | environment |     | 46  |
| ----------------------------------------------------- | ------- | ----------- | --- | --- |
| WaystoviewthestatusofVSX                              |         |             |     | 46  |
| ConsistencycheckingbetweenVSXswitches                 |         |             |     | 46  |
| ViewingtheshowcommandsforbothVSXswitchesfromoneswitch |         |             |     | 46  |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide| (6400,8xxx
3
SwitchSeries)

| Preventing                       | traffic loss                                | 48  |
| -------------------------------- | ------------------------------------------- | --- |
| Link-updelay                     |                                             | 48  |
|                                  | Thelink-updelaytimerduringanISLfailure      | 49  |
| Splitbrainscenario               |                                             | 51  |
| Keepalive                        |                                             | 52  |
|                                  | KeepaliveresponseinISLfailurescenarios      | 53  |
|                                  | Keepalivescenario                           | 53  |
|                                  | Keepaliveconfigurations                     | 54  |
|                                  | Recommendednetworkconfigurationforkeepalive | 55  |
| Activegatewayandactiveforwarding |                                             | 57  |
|                                  | Active-activelayer2                         | 57  |
|                                  | Layer2configuration                         | 57  |
|                                  | Active-activelayer3defaultgateway           | 58  |
|                                  | ActivegatewayoverVSX                        | 58  |
|                                  | VMACsandactivegateway                       | 59  |
|                                  | Requirements                                | 59  |
|                                  | ExampleofIPv4andIPv6activegatewaysonanSVI   | 60  |
|                                  | IPmultinettingoverVSX                       | 61  |
|                                  | Activegatewayconfigurations                 | 62  |
|                                  | VRRPwithVSXconfiguration                    | 62  |
|                                  | Activeforwarding                            | 63  |
|                                  | Activeforwardingrequirements                | 63  |
|                                  | Trafficflowscenario                         | 63  |
|                                  | SampleActiveforwardingconfiguration         | 64  |
Deploymentoptionsforupstreamconnectivitywithactive-activeforwarding 64
|                                                   | Benefitsofactiveforwardingandactivegateway               | 64  |
| ------------------------------------------------- | -------------------------------------------------------- | --- |
| Virtualactivegateway                              |                                                          | 65  |
|                                                   | SupportedservicesonavirtualactivegatewaySVI              | 65  |
|                                                   | UnsupportedservicesforavirtualactivegatewaySVI           | 65  |
|                                                   | Samplevirtualactivegatewayconfiguration                  | 66  |
| Active-standbyDHCPrelay                           |                                                          | 66  |
|                                                   | DHCPrelayfailureiftheSVIisdownontheprimaryswitch         | 67  |
| Splitrecoverymode                                 |                                                          | 67  |
| VSXshutdown-on-split                              |                                                          | 67  |
| IGMPsnooping                                      |                                                          | 67  |
| DHCPrelaybackup                                   |                                                          | 68  |
| IPmulticastrouting                                |                                                          | 69  |
| RecommendedvaluesforsystemMACandactivegatewayVMAC |                                                          | 70  |
| STP over                                          | VSX                                                      | 72  |
| SupportedSTPmodes                                 |                                                          | 72  |
| HowSTPworkswithVSX                                |                                                          | 72  |
| MSTP                                              |                                                          | 73  |
|                                                   | MSTPconfigurations                                       | 73  |
|                                                   | VSXatthedistributionlayerwithMSTPenabled                 | 74  |
|                                                   | DistributionVSXpairconnectedtothecoreswitch(SVIsolution) | 76  |
|                                                   | SampleconfigurationsforMSTPonVSX                         | 77  |
VSXandMSTPloop-protectconfigurations(physicalandlogicalviews) 80
|       | ShowcommandsforMSTP                                   | 81  |
| ----- | ----------------------------------------------------- | --- |
|       | MSTPwithVSXguidelines                                 | 82  |
| RPVST |                                                       | 82  |
|       | SampleRPVSTconfigurationwithVSX                       | 82  |
|       | VSXswitchwithRPVST,asrootandnonroot                   | 85  |
|       | ConfiguringaVSXswitchasrootforoneormoreRPVSTinstances | 87  |
|       | ShowcommandsforRPVST                                  | 87  |
|       | HowtheMulti-Chassisroleworks                          | 88  |
Contents|4

|                                            | RPVSTwithVSXguidelines                      |          | 90  |
| ------------------------------------------ | ------------------------------------------- | -------- | --- |
| Loop protect                               | configurations                              | over VSX | 91  |
| HowloopprotectworksoverVSX                 |                                             |          | 91  |
| SettinguploopprotectoverVSX                |                                             |          | 93  |
| AnexampleconfigurationofloopprotectoverVSX |                                             |          | 93  |
|                                            | VSXconfigurationsbeforeenablingloopprotect  |          | 94  |
|                                            | VSXprimaryswitchbeforeenablingloopprotect   |          | 94  |
|                                            | VSXsecondaryswitchbeforeenablingloopprotect |          | 95  |
|                                            | Downstreamswitchbeforeenablingloopprotect   |          | 97  |
|                                            | VSXconfigurationsafterenablingloopprotect   |          | 98  |
|                                            | VSXprimaryswitchafterenablingloopprotect    |          | 98  |
|                                            | VSXsecondaryafterbeforeenablingloopprotect  |          | 99  |
|                                            | Downstreamswitchafterenablingloopprotect    |          | 99  |
| BestpracticesforloopprotectoverVSX         |                                             |          | 100 |
| EVPN VSX                                   | support                                     |          | 101 |
| Upstream                                   | connectivity                                |          | 102 |
| Upstreamconnectivityoptions                |                                             |          | 102 |
| UpstreamroutingoverVSXLAGSVIlinks          |                                             |          | 105 |
| VSX commands                               |                                             |          | 109 |
| active-gateway                             |                                             |          | 109 |
| config-syncdisable                         |                                             |          | 111 |
| inter-switch-link{<PORT-NUM>|lag<LAG-ID>}  |                                             |          | 111 |
| inter-switch-linkdead-interval             |                                             |          | 112 |
| inter-switch-linkhello-interval            |                                             |          | 113 |
| inter-switch-linkhold-time                 |                                             |          | 114 |
| inter-switch-linkpeer-detect-interval      |                                             |          | 114 |
| interfacelagmulti-chassis                  |                                             |          | 115 |
| ipicmpredirect                             |                                             |          | 116 |
| keepalivedead-interval                     |                                             |          | 117 |
| keepalivehello-interval                    |                                             |          | 117 |
| keepalivepeer                              |                                             |          | 118 |
| keepaliveudp-port                          |                                             |          | 119 |
| lacpfallback                               |                                             |          | 120 |
| linkup-delay-timer                         |                                             |          | 121 |
| linkup-delay-timerexcludelag-list          |                                             |          | 122 |
| neighbor<IP-ADDRESS>vsx-sync-exclude       |                                             |          | 123 |
| role{primary|secondary}                    |                                             |          | 123 |
| showactive-gateway                         |                                             |          | 124 |
| showactive-gateway<IFNAME>                 |                                             |          | 126 |
| showinterface<VLAN-NAME>                   |                                             |          | 126 |
| showlacpaggregates                         |                                             |          | 127 |
| showlacpinterfaces                         |                                             |          | 128 |
| showlacpinterfacesmulti-chassis            |                                             |          | 131 |
| showrunning-configinterface                |                                             |          | 132 |
| showrunning-configvsx                      |                                             |          | 133 |
| showrunning-configvsx-sync                 |                                             |          | 134 |
| showrunning-configvsx-syncpeer-diff        |                                             |          | 134 |
| showvsxactive-forwarding                   |                                             |          | 135 |
| showvsxbrief                               |                                             |          | 136 |
| showvsxconfig-consistency                  |                                             |          | 137 |
| showvsxconfig-consistencylacp              |                                             |          | 138 |
| showvsxconfiguration                       |                                             |          | 139 |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 5

show vsx configuration split-recovery
show vsx ip data-path
show vsx ip route
show vsx ipv6 data-path
show vsx ipv6 route
show vsx status
show vsx status config-sync
show vsx status shutdown-on-split
split recovery
system-mac
vsx
vsx active-forwarding
vsx shutdown-on-split
vsx-sync
vsx-sync {[access-lists] [qos] [rate-limits] [vlans] [policies] [irdp] [portfilter]}
vsx-sync {[active-gateways] [policies]}
vsx-sync aaa
vsx-sync acl-log-timer
vsx-sync arp-security
vsx-sync bfd-global
vsx-sync bgp
vsx-sync copp-policy
vsx-sync dcb-global (8325 and 8360 series switches only)
vsx-sync dhcp-relay
vsx-sync dhcp-server
vsx-sync dhcpv6-server
vsx-sync dns
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
vsx-sync qos-global
vsx-sync route-map
vsx-sync sflow
vsx-sync sflow-global
vsx-sync snmp
vsx-sync ssh
vsx-sync static-routes
vsx-sync stp-global
vsx-sync time
vsx-sync udp-forwarder
vsx-sync vrrp
vsx-sync vsx-global
vsx update-software
vsx update-software boot-bank

Troubleshooting

ISL is out-of-sync
Solution 1

140
141
142
144
146
147
150
151
152
152
153
154
155
156
159
162
164
164
165
166
166
167
168
169
170
171
172
172
173
174
174
175
176
176
178
179
179
180
181
182
182
183
184
185
185
186
187
187
188
189
190
191

193
193
193

Contents | 6

|                               | Solution2 |     | 193 |
| ----------------------------- | --------- | --- | --- |
|                               | Solution3 |     | 194 |
| ISLisinblockingstate          |           |     | 194 |
| TrafficdroponaVSXLAGinterface |           |     | 196 |
TrafficlossaftertheISLhasbeenout-of-syncandkeepaliveisdown 197
| Failurescenariosandsplitrecovery |     |     | 197 |
| -------------------------------- | --- | --- | --- |
| Activegatewayisunreachable       |     |     | 198 |
BFDreportsaLAGasdownevenwhenhealthylinksarestillavailable 199
| PingbetweenVSXpeerIPaddressesfails |                    |           | 200 |
| ---------------------------------- | ------------------ | --------- | --- |
| Support                            | and Other          | Resources | 201 |
| AccessingArubaSupport              |                    |           | 201 |
| AccessingUpdates                   |                    |           | 201 |
|                                    | ArubaSupportPortal |           | 201 |
|                                    | MyNetworking       |           | 202 |
| WarrantyInformation                |                    |           | 202 |
| RegulatoryInformation              |                    |           | 202 |
| DocumentationFeedback              |                    |           | 202 |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 7

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A)

n Aruba 8400 Switch Series (JL375A, JL376A)

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

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables are
enclosed in angle brackets (< >). Substitute the text—including the
enclosing angle brackets—with an actual value.

n For output formats where italic text can be displayed, variables might

or might not be enclosed in angle brackets. Substitute the text
including the enclosing angle brackets, if any, with an actual value.

|

Vertical bar. A logical OR that separates multiple items from which you can
choose only one.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

8

Convention

Usage

{ }

[ ]

… or

...

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
Examples in this document are representative and might not match your particular switch or environment.

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

In certain configuration contexts, the prompt may include variable information. For example, when in the
VLAN configuration context, a VLAN number appears in the prompt:
switch(config-vlan-100)#

When referring to this context, this document uses the syntax:
switch(config-vlan-<VLAN-ID>)#

Where <VLAN-ID> is a variable representing the VLAN number.

Identifying switch ports and interfaces
Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 6400 Switch Series

About this document | 9

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

On the 83xx Switch Series

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

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

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

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

10

Chapter 2

Getting started with VSX

Getting started with VSX

Aruba Virtual Switching Extension (VSX) is virtualization technology for aggregation/core switches running
the AOS-CX operating system. This solution lets the switches present as one virtualized switch in critical
areas. Configuration synchronization is one aspect of this VSX solution where the primary switch
configuration is synced to the secondary switch. This solution allows for a pseudo single plane of glass
configuration and helps keep key configuration pieces in synchronization as operational changes are made.
Since the solution is primarily for high availability, it is expected that most of the configuration policy is the
same across both peers.

VSX virtualizes the control plane of two aggregation switches to function as one device at layer 2 and as
independent devices at layer 3. From a datapath perspective, each device does an independent forwarding
lookup to decide how to handle traffic. Some of the forwarding databases, such as the MAC and ARP tables,
are synchronized between the two devices using a proprietary VSX control plane. Some of the forwarding
databases are built independently by each switch.

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

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

11

o No gateway protocol overhead

o DHCP relay redundancy

o IP multinetting support

VSX solution topology overview

n Active gateway support: Active gateways can be configured for active-active routing. VRRP can be

used, as an alternative, for active-standby routing.

n ISL links assigned to higher bandwidth: An ISL link has a higher bandwidth compared to VSX links.

When planning the topology, consider sizing the ISL link according to the traffic volume required for the
east-west traffic of a single-homed VSX during a failover scenario.

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

After setting up the VSX topology, see Enabling VSX configuration synchronization. VSX synchronization can
be enabled globally for some features, and VSX synchronization can be enabled at the context level for
other features.

Sample VSX solution topology

Getting started with VSX | 12

VSX LAG

VSX LAGs span both aggregation switches. The two switches appear as one device to partner downstream or
upstream devices or both when forming a LAG with the VSX pair. The two switches synchronize their
databases and states over a user configured link referred to as an Inter-Switch Link (ISL).

VSX LAGs are preferable to point-to-point transit VLANs for upstream connectivity when the routed only
port is not an option, such with the case of multiple VRFs. This configuration reduces the number of transit
VLANs and associated SVIs, simplifying operations and troubleshooting. Enable active forwarding and active
gateway to further optimize the traffic path. When you enable active forwarding and active gateway, north-
south and south-north traffic bypasses the ISL link.

VSF

Virtual Switching Framework (VSF) technology virtualizes multiple physical devices into one virtual fabric
which provides high availability because of the significant reduction in recovery time simplified network
design and management. VSF is ideal for campus access. VSF lets supported switches connected to each
other through Ethernet connections (copper or fiber) to behave like a single chassis switch.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

13

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

When the primary switch is restored after the secondary switch, a traffic disruption might occur when the
ISL starts to sync because the MAC system address changes from the secondary switch to the primary
switch for the LACP. To avoid the traffic disruption, set the common system MAC address by entering the
system-mac <MAC-ADDR> command. This command creates a common system MAC address between the
two VSX switches. This common system MAC address prevents a traffic disruption when the secondary

Getting started with VSX | 14

switch comes up before the primary switch. If the common system MAC access is enabled, the secondary
switch uses the common system MAC address instead of its own system MAC address, which prevents a
traffic loss.

The system MAC address also maintains the same MSTP bridge ID across VSX switches, which act as a single
switch.

VSX solution requirements

n All VSX switches in an environment must have identical settings for the following:

o The VLAN membership for all VSX trunk ports.

o The loop protection configuration on a VLAN that is part of a VSX LAG.

n Available ports: Make sure that the VSX LAG interface on both the VSX primary and secondary

switches has a member port configured and enabled. Make sure that you also have a non-VSX port that
is available for the ISL.

n Mutually exclusive features:

o VSX active-forwarding and VSX active-gateway on the same VLAN interface

o VSX active-gateway and VRRP at SVI context

o VSX and MVRP

VSX active-gateway and VRRP can co-exist at global level

n Profiles for 832x series switches: All switches must be assigned either in profile L3-agg or L3-core.

n Support for Inter-Switch links (ISLs): VSX LAG does not support layer 3 processing, such as a routed

port; however, multiple Virtual Switch Interfaces (VSI) can be configured on the switch in association with
the VLANs carried over the given VSX LAG.

n Support for Layer 3: VSX LAG as a route only port is not supported. To enable Layer 3, create an SVI

associated to a given VLAN that is enabled on the VSX LAG.

n VLAN support: The same list of VLANs that are trunked over the VSX LAGs must be configured on the
primary and secondary VSX switches in the global configuration. The list of VLANs can be synced to the
secondary switch if the vsx-sync command is used in the VLAN context. Also verify that the VLAN set is
also permitted on the ISL on the primary and secondary VSX switches. To configure VLAN trunking on the
ISL, enter the vlan trunk allowed [<VLAN-LIST> | all] command. If a native VLAN is defined, the
switch automatically runs the vlan trunk allowed all command to ensure that the default VLAN is
allowed on the trunk. To allow only specific VLANs on the trunk, enter the vlan trunk allowed <VLAN-
LIST> command, for example: vlan trunk allowed 2,3,4

For steps about creating the ISL within a VSX LAG, see Configuring the two aggregate VSX switches.

n VSX active-forwarding, VSX active-gateway, and VSX LAG are supported with BFD.

n VSX switches and software versions: Both VSX peer switches must use the same software version in
most situations; however during an upgrade, one switch can run a different version than the peer with
some limitations, such as no VSX synchronization support.

VSX components
VSX has the following components:

n Active-standby DHCP server

n Common system MAC address

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

15

n DHCP forwarder redundancy

n Inter-Switch Link (ISL)

n IGMP snooping

n Keepalive

n Multiple Spanning Tree Protocol (MSTP)

n Split recovery mode

n Switch roles

Inter-Switch Link (ISL)
In the VSX solution topology, an Inter-Switch Link (ISL) is a layer 2 interface between two VSX peer switches.
Each VSX switch must be configured with an ISL link connected to its peer VSX switch. It is recommended
that this link is peer-to-peer and used for both datapath traffic forwarding and control path VSX protocol
exchange. The ISL interface is by default a member of all VLANs on the device. You can change ISL
membership through the command line, but you must ensure VLANs that contain VSX LAG members are
not excluded from the ISL.

In the datapath, traffic is forwarded natively with no additional encapsulation, unlike VSF. ISL is capable of
sending control path data, which requires oversize packets. The ISL MTU is automatically set to the required
size to accommodate oversize packets, and cannot be manually overwritten to avoid generating an
unintended outage. The token counters of ISL interface show this oversize control path data as part of the
ISL operation. The ISL link is the main pipeline for synchronizing data, such as from the following
components, during VSX stack join and also permanently between VSX peers:

n ARP table

n LACP states for VSX LAGs

n MAC table

n MSTP states

The ISL uses version control and provides backward compatibility regarding VSX synchronization
capabilities.

The ISL can span long distances (transceiver dependent). The traffic that passes over VSX links has no
additional encapsulation.

All ISL ports must have the same speed. The speed can be 10G, 25G, 40G, or 100G, with 40G and 100G
being the preferred speeds. For example: 2x40G.

When you convert any layer 2 interface to be part of an ISL lag, the MTU value of the interface changes to
9198, but this value will not be displayed under the show running-config and show running-config all
commands. For example, if you configure interface with MTU value of 5000, and convert the interface to be
part of an ISL lag, the MTU value changes from 5000 to 9198. But under show running-config and show

running-config all, the MTU value is still displayed as 5000. If you want to view the actual MTU value of

the ISL interface, you must execute the show interface <Interface-ID> command.

Sample show running-config snippet

Getting started with VSX | 16

| interface | 1/1/1no | shutdown |     |     |     |     |
| --------- | ------- | -------- | --- | --- | --- | --- |
mtu 5000
description VSX-ISL
lag 256
| Sample show       | interface   | snippet  |            |                 |           |     |
| ----------------- | ----------- | -------- | ---------- | --------------- | --------- | --- |
| interface         | 1/1/1 is    | up       |            |                 |           |     |
| Admin             | state is up |          |            |                 |           |     |
| Link state:       | up for      | 1 minute | (since Mon | Apr 05 07:25:14 | UTC 2021) |     |
| Link transitions: |             | 9        |            |                 |           |     |
Description:
| Hardware:     | Ethernet, | MAC Address: | 54:80:28:fd:78:fd |     |     |     |
| ------------- | --------- | ------------ | ----------------- | --- | --- | --- |
| MTU 9198      |           |              |                   |     |     |     |
| Type SFP+DAC3 |           |              |                   |     |     |     |
Full-duplex
| qos trust        | none       |        |     |     |     |     |
| ---------------- | ---------- | ------ | --- | --- | --- | --- |
| Speed            | 10000 Mb/s |        |     |     |     |     |
| Auto-negotiation |            | is off |     |     |     |     |
| Flow-control:    | off        |        |     |     |     |     |
| Error-control:   | off        |        |     |     |     |     |
ISL configurations
| Task                  |     |     | Command              |     | Example             |               |
| --------------------- | --- | --- | -------------------- | --- | ------------------- | ------------- |
| ConfiguringanISLport. |     |     | inter-switch-link    |     | switch(config)#     | vsx           |
|                       |     |     |                      |     | switch(config-vsx)# | inter-switch- |
|                       |     |     |                      |     | link lag 100        |               |
| DeletinganISLport.    |     |     | no inter-switch-link |     | switch(config)#     | vsx           |
|                       |     |     |                      |     | switch(config-vsx)# | no inter-     |
switch-link
ConfiguringISLdeadinterval. inter-switch-link dead- switch(config)# vsx
|     |     |     | interval <DEAD-INTERVAL> |     |                     |               |
| --- | --- | --- | ------------------------ | --- | ------------------- | ------------- |
|     |     |     |                          |     | switch(config-vsx)# | inter-switch- |
|     |     |     |                          |     | link dead-interval  | 10            |
RestoredefaultISLdead no inter-switch-link switch(config)# vsx
| interval. |     |     | dead-interval |     |     |     |
| --------- | --- | --- | ------------- | --- | --- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 17

| Task | Command |     | Example             |           |
| ---- | ------- | --- | ------------------- | --------- |
|      |         |     | switch(config-vsx)# | no inter- |
switch-link dead-interval
ConfiguringtheISLhello inter-switch-link hello- switch(config)# vsx
| interval. | interval <HELLO-INTERVAL> |     |                     |               |
| --------- | ------------------------- | --- | ------------------- | ------------- |
|           |                           |     | switch(config-vsx)# | inter-switch- |
|           |                           |     | link hello-interval | 3             |
RestoringdefaultISLhello no inter-switch-link switch(config)# vsx
| interval. | hello-interval |     |                     |           |
| --------- | -------------- | --- | ------------------- | --------- |
|           |                |     | switch(config-vsx)# | no inter- |
switch-link hello-interval
ConfiguringISLholdtime. inter-switch-link hold- switch(config)# vsx
time <HOLD-INTERVAL>
|     |     |     | switch(config-vsx)# | inter-switch- |
| --- | --- | --- | ------------------- | ------------- |
|     |     |     | link hold-time 2    |               |
RestoringdefaultISLholdtime. no inter-switch-link switch(config)# vsx
|     | hold-time |     | switch(config-vsx)# | no inter- |
| --- | --------- | --- | ------------------- | --------- |
switch-link hold-time
Configuringtheamountoftime inter-switch-link peer- switch(config)# vsx
insecondsthatthedevicewaits
|                            | detect-interval  | <PEER- | switch(config-vsx)#       | inter-switch- |
| -------------------------- | ---------------- | ------ | ------------------------- | ------------- |
| fortheISLinterfacetolinkup | DETECT-INTERVAL> |        |                           |               |
|                            |                  |        | link peer-detect-interval | 180           |
afterareboot.
Defaultvalues:
Deadinterval:20seconds
n
n Hellointerval:1second
n Holdtime:0seconds
n Peerdetectinterval:300seconds
Switch roles
EachVSXswitchmustbeconfiguredwitharole–primaryorsecondary.Therolesdonotindicatewhich
deviceisforwardingtrafficatagiventimeasVSXisanactive-activeforwardingsolution.Therolesareused
todeterminewhichdevicestaysactivewhenthereisaVSXsplit,suchaswhentheISLgoesdown,andfor
determiningthedirectionofconfiguration-sync.IftheVSXISLgoesdown,theprimaryswitchkeeps
forwardingtrafficwhilethesecondaryswitchblocksportsfromparticipatingintheVSXLAGs.
VSX switch reboot
AfteraVSXswitchreboots,ithasnoentriesforARP,MAC,androutes.IfdownstreamVSXLAGportsare
activatedbeforeallthisinformationisrelearned,trafficisdropped.Toavoidatrafficdrop,VSXLAGsonthe
rebootedswitchstaydownuntiltherestorationofLACP,MAC,ARPdatabases,andMSTPstatesifMSTPis
used.
ThelearningprocessfortheVSXLAGshastwophases:
n Initialsync phase:TheLACPstates,MACaddresstable,ARPtable,andpotentiallyMSTPstatesare
downloadedfromtheforwardingswitchtothefreshlyrebootedswitch.
GettingstartedwithVSX|18

n Link-up delay phase: The downloaded entries are installed into the ASIC. Router adjacencies with core

nodes and learned upstream routes are also established.

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

In a VSX scenario if all traffic from core to access flows through one switch only, the other device will also
learn about ARP/ND from its VSX peer. There is no functional impact to the normal datapath based learning.
VSX split and the rejoin scenario, such as periodic synchronization, resumes after the bulk synchronization.

The IVRL induced neighbor entries are not synced either through the initial ARP synchronization or periodic
synchronization. The local IVRL will induce the learning on each side triggered by either a local data-path ARP
learned or the ongoing sync based-ARP learned in the source VRF.

If you enter one or more of the following commands on one VSX switch but not on the other VSX switch or
any configuration is incorrect on one switch , the ARP entries on both switches will become unsynchronized:

n interface vlan

n shutdown for a VLAN

n no shutdown for a VLAN

If you run into this situation, correct the configuration and run the clear arp command, which clears the
ARP entries on both VSX nodes. After you run the clear arp command, the ARP entries are synchronized
on both switches.

The following image shows how periodic synchronization synchronizes LACP states, MAC, ARP/ND, and
MSTP. The image references the VSX synchronization between aggregate 1 (the primary VSX switch) and
aggregate 2 (the secondary VSX switch).

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

19

BFD and VSX support
BFD supports VSX LAG, active gateway, and active forwarding.

For 832x series switches: Several TCAMs (ternary content-addressable memory) are used to avoid
decreasing the time-to-live (TTL) to 254 on BFD single-hop packets received/sent on ISL interfaces.

For 8400 series switches: To account for the TTL decrement on active forwarding, the BFD daemon
supports packets with TTL equal to 254 on sessions running on ports with this functionality active.

Getting started with VSX | 20

Upgrading to the latest version of VSX

Chapter 3

Upgrading to the latest version of VSX

This chapter provides information about upgrading customer configurations to the latest version of the
Virtual Switching Extension (VSX).

n If you are upgrading from version 10.00, see the Virtual Switching Extension (VSX) Guide for 10.02 for

steps on how to upgrade VSX to version 10.02. Then, see the steps in this guide on how to upgrade VSX
from version 10.02.

n If you are upgrading from version 10.01/10.02, see the Virtual Switching Extension (VSX) Guide for 10.03
for steps on how to upgrade VSX to version 10.03. Then, see the steps in this guide on how to upgrade
VSX from version 10.03.

Upgrading VSX from 10.03 or later to 10.07
You can upgrade to the latest version of AOS-CX using one of the following methods:

n Running the vsx update-software command: Follow the steps in Upgrading switches by using the vsx
update-software command for required steps before and after running the vsx update-software vsx
update-software command.

This command downloads new software from the TFTP server and verifies the download. After a successful
verification, the command installs the software to the alternative software bank of both the VSX primary
and secondary switches. The command then reboots them in sequence, the VSX secondary switch followed
by VSX primary switch. For example if a switch has booted with the primary flash memory, then the
command will install the software to secondary flash memory.

n Running the vsx update-software boot-bank command: This command upgrades the VSX pairs

using the specified boot bank on both the devices. Before running this command, copy the new software
by adding the TFTP URL into the software bank of both primary and secondary VSX switches. Use this
command in cases where the scheduled maintenance window is minimum or to avoid TFTP server
timeout. For more information about this command, see vsx update-software boot-bank.

To perform an upgrade using vsx update-software boot-bank command, the minimum
supported version of AOS-CX must be 10.04 or later.

n Using REST API : Refer to the latest REST API Guide.

To perform an upgrade using REST API, the minimum supported version of AOS-CX must be 10.07 or

later.

n Running Aruba NetEdit to upgrade to the latest version of VSX. Refer to the Aruba NetEdit

documentation.

Upgrading switches by using the vsx update-software command

Prerequisites

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

21

1. Ensure that there is a scheduled maintenance window. There will be a minimal disruption of service

until the upgrade is completed.

2.

If you have enabled loop protect, enter the show loop-protect command for verifying that the
action on loop detection has a value of TX disable on the VSX interface. If the setting has a different
value, reset the value to TX disable by entering the loop-protect action tx-disable command:

switch(config)# interface lag 2 multi-chassis
switch(config-if)# loop-protect action tx-disable
switch(config-if)# exit
switch(config)# exit

3. The vsx update-software command provides the option to save the configuration on the primary
and secondary VSX switches; however, you can save the configuration manually by using one of the
following methods:
n To copy the running configuration into the startup configuration:

switch# copy running-config startup-config

If the startup configuration is already present, the command overwrites the pre-existing startup
configuration.

n To copy the running configuration into a checkpoint that has not been created yet:

switch# copy running-config checkpoint <CHECKPOINT-NAME>

4. Check the status of the show vsx brief command and validate the ISL is in-sync and the keepalive is

established.

5. Check the output of the show lacp interfaces multi-chassis command and note which LACP

interfaces are in a forwarding state of up.

Procedure

1. Enter the vsx update-software command. Prefix the path, for downloading the software, with

tftp://, as shown in the following example:

switch# vsx update-software tftp://192.168.1.1/XL.10.0x.xxxx vrf mgmt
Do you want to save the current configuration (y/n)? y
The running configuration was saved to the startup configuration.

This command will download new software to the %s image of both the VSX

primary and secondary systems, then reboot them in sequence.
The VSX secondary will reboot first, followed by the primary.
Continue (y/n)? y
VSX Primary Software Update Status
VSX Secondary Software Update Status
status>
VSX ISL Status
Progress
[.............................................................................
]
Secondary VSX system updated completely. Rebooting primary.

: <VSX primary software update status>
: <VSX secondary software update

: <VSX ISL status>

Upgrading to the latest version of VSX | 22

This command gives you the option to save the running configuration on the primary and secondary
VSX switches. After the command saves the running configuration, it downloads new software from
the TFTP server and verifies the download. After a successful verification, the command installs the
software to the alternative image of both the VSX primary and secondary switches.

The command displays the status of the VSX primary and secondary switches during the upgrade.
The command also refreshes the progress bar as the image update progresses. Do not interrupt the
VSX primary CLI session until the software updates completes; however, software update process can
be stopped. If you stop the upgrade when the secondary switch has already installed the image in its
flash memory or the secondary switch has started the reboot the process, it comes up with the new
software. The primary switch continues to have with older software. You can stop the software
update process by pressing ctrl+c.

2. Run the show vsx brief command on both switches. Verify that ISL is In-Sync by running the show

vsx brief command on both switches. Verify in the output of the command that the keepalive state
is Keepalive-Established.

3. Validate on both switches that the downstream LACP links are all forwarding correctly by entering the

show lacp interfaces command.

4. Save the running configuration to the startup configuration:

switch# write memory
Success

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

23

Chapter 4
|         |            |             | Setting | up the | VSX environment |
| ------- | ---------- | ----------- | ------- | ------ | --------------- |
| Setting | up the VSX | environment |         |        |                 |
ThefollowingsectionsdescribethestepstosetuptheVSXenvironment,configurecore1andcore2for
VSX,andconfigureaggregateVSXswitches.
| VSX in | the core | layer |     |     |     |
| ------ | -------- | ----- | --- | --- | --- |
Whenmobilitycontrollersareattachedtothecorelayer,aVSXLAGmustbeinthecorelevel.Layer2isonly
atthedistributionlayerwiththecorelayerbeinglayer2andlayer3.ThisconfigurationisforIPv6,andthe
configurationreducesthenumberoftransitVLANsandtheassociatedSVIsformanyVRFs.Italsominimizes
theShortestPathFirst(SPF)calculation.Thenumberoffibersisreducedandthereisfastfailoverbecauseof
thesimplifiedtopology(nosquare-routing).
| Figure 1 | VSXLAGinthecore(recommended) |     |     |     |     |
| -------- | ---------------------------- | --- | --- | --- | --- |
ThefollowingimageshowsanexamplethatSPFisslowerwhenVSXisnotinthecorebecauseofrouting
convergence.
24
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide| (6400,8xxxSwitchSeries)

Configuring core 1 and core 2 for VSX
The steps in this section are for configuring core 1 and core 2 for VSX, as displayed in VSX LAG in the core
(recommended).

After completing these steps, configure the aggregate switches in your network topology, as described in
Configuring the two aggregate VSX switches. Then, enable VSX configuration synchronization for a feature,
as described in Enabling VSX configuration synchronization.

A VSX LAG supports a maximum of four member links per switch segment. A VSX LAG across a downstream
switch can have at most a total of eight member links. Run the show capacities command for the
maximum number of VSX LAGs supported for your type of switch.

The core can be third-party devices, as long as they support LACP for downstream connectivity to the VSX
LAG. VSX synchronization syncs from the primary switch (aggregate 1) to the secondary switch (aggregate-
2).

When creating a VSX LAG, select an equal number of member links in each segment for load balancing, such as

four member links (one segment) and four member links (another segment). Do not create a VSX LAG with four

member links in one switch and two member links on another segment. A switch can have a maximum of four

member links.

Setting up the VSX environment | 25

Procedure
1. Accessthepromptontheswitchyouwanttomaketheprimarycoreswitch.
2. Iftheswitchlacksahostname,createone:
| switch(config)# | hostname |     | <HOSTNAME> |     |
| --------------- | -------- | --- | ---------- | --- |
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
OSPFv2andOSPFv3arenotrequiredtobeactivatedsimultaneously.ActivateOSPFv2andOSPFV3
accordingtotheneedsoftheenvironment.
6. CreatealoopbackinterfaceandenableOSPFv2/v3:
| switch(config)#             | interface |     | loopback   | 1              |
| --------------------------- | --------- | --- | ---------- | -------------- |
| switch(config-loopback-if)# |           |     | ip address | 3.3.3.3/24     |
| switch(config-loopback-if)# |           |     | ip ospf    | 1 area 0.0.0.0 |
| switch(config-loopback-if)# |           |     | exit       |                |
7. EnableOSPFv2/v3onthephysicalport:
| switch(config)#    | interface |          | 1/2/43          |               |
| ------------------ | --------- | -------- | --------------- | ------------- |
| switch(config-if)# | no        | shutdown |                 |               |
| switch(config-if)# | ip        | address  | 192.168.10.5/24 |               |
| switch(config-if)# | ipv6      | address  |                 | 2001:11::3/64 |
| switch(config-if)# | ip        | ospf     | 1 area          | 0.0.0.0       |
| switch(config-if)# | ipv6      | ospfv3   | 1               | area 0.0.0.0  |
| switch(config-if)# | exit      |          |                 |               |
8. CreateaVLANforthehostnetwork:
| switch(config)#          | vlan | 200 |           |                 |
| ------------------------ | ---- | --- | --------- | --------------- |
| switch(config-vlan-200)# |      |     | interface | vlan 200        |
| switch(config-if-vlan)#  |      | ip  | address   | 192.168.10.6/16 |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 26

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
11. Entertheroleprimarycommandforassigningtheprimaryroletoaswitch.Ifyouhavealreadygone
throughthesestepsforconfiguringtheprimaryswitchandyouarenowconfiguringthesecondary
switch,entertherolesecondarycommand.
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
13. KeepalivehelpsthecoreswitchescontinuetostayinsynchduringanISLfailure.Whencreatingthe
keepalivepath,makesurethatthepathdoesnotgoovertheISLoraVSXLAG.Keepalivecanbe
configuretwowaysforcore1andcore2.Onewayistoenablekeepalivebetweencore1andcore2
asadirectlink.Asecondwayistocreateakeepalivepathforaloopbackinterfacethroughthe
upstreamthatlacksaVSXLAG.
| switch(config)#             | int loopback |     | 0          |                |
| --------------------------- | ------------ | --- | ---------- | -------------- |
| switch(config-loopback-if)# |              |     | ip address | 192.168.1.1/32 |
| switch(config-loopback-if)# |              |     | ip ospf    | 1 area 0       |
| switch(config-loopback-if)# |              |     | exit       |                |
SettinguptheVSXenvironment|27

|     | switch(config)# | vsx |     |     |
| --- | --------------- | --- | --- | --- |
switch(config-vsx)# keepalive peer 192.168.1.2 source 192.168.1.1 vrf <KA-VRF-
NAME>
|     | switch(config-vsx)#         |     | exit       |               |
| --- | --------------------------- | --- | ---------- | ------------- |
|     | switch(config)#             | int | loopback 0 |               |
|     | switch(config-loopback-if)# |     | vrf attach | <KA-VRF-NAME> |
Thesourceofthekeepaliveinterfacecanbeasupportedlayer3interfacethroughtheloopback
interface,SVI,orlayer3interface.ThesourcemustbereachabletotheVSXpeerthroughlayer3.
Thepathcanbeoverthecoreordirectpath.ThekeepalivepathmustnotbeovertheISL.See
Recommendednetworkconfigurationforkeepalive.
14. Changethecontexttotheswitch(config)#context:
|     | switch(config-vsx)# |     | exit |     |
| --- | ------------------- | --- | ---- | --- |
switch(config)#
15. ConfiguringaLAGinterfaceasanISL:
|     | switch(config)# | interface | lag <LAG-ID> |     |
| --- | --------------- | --------- | ------------ | --- |
Forexample,configuringLAG100asanISLLAG:
|     | switch(config)#        | interface | lag 100           |         |
| --- | ---------------------- | --------- | ----------------- | ------- |
|     | switch(config-lag-if)# |           | vsx               |         |
|     | switch(config-vsx)#    |           | inter-switch-link | lag 100 |
16. Repeatthepreviousstepsforthesecondarycoreswitch.
17. Entertheshowvsxconfigurationinter-switch-linkcommandforconfirmingthepropertiesoftheVSX
LAG,suchasconfirmingiftheISLisin-sync.
switch#
|             |               | show vsx    | configuration inter-switch-link |              |
| ----------- | ------------- | ----------- | ------------------------------- | ------------ |
|             | Inter         | Switch Link | : 1/1/43                        |              |
|             | Hello         | Interval    | : 1 Seconds                     |              |
|             | Dead Interval |             | : 20 Seconds                    |              |
|             | Hold Time     |             | : 0 Seconds                     |              |
|             | System        | MAC         | : 10:00:00:00:00:01             |              |
|             | Device        | Role        | : primary                       |              |
|             | Multichassis  | LAGs        | : lag100                        |              |
| Configuring |               | the two     | aggregate                       | VSX switches |
ThestepsinthissectionareforconfiguringthetwoaggregateVSXswitches,asdescribedinVSXsolution
topologyoverview.VSXswitchesdonotautomaticallyhaveVSXconfigurationsynchronizationenabled.
Aftercompletingthestepsinthissection,enableVSXconfigurationsynchronizationforafeature,as
describedinVSXconfigurationsynchronization.VSXsynchronizationsyncconfigurationinformationfrom
theprimaryswitch(Aggregate-1)tothesecondaryswitch(Aggregate-2).Aftercompletingthestepsinthis
section,enableVSXconfigurationsynchronizationforafeature,asdescribedinVSXconfiguration
synchronization.
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 28

AVSXLAGsupportsamaximumoffourmemberlinksperswitchsegment.AVSXLAGacrossadownstream
switchcanhaveatmostatotalofeightmemberlinks.Runtheshow capacitiescommandforthe
maximumnumberofVSXLAGssupportedforyourtypeofswitch.
n WhencreatingaVSXLAG,selectanequalnumberofmemberlinksineachsegmentforloadbalancing,such
asfourmemberlinks(onesegment)andfourmemberlinks(anothersegment).DonotcreateaVSXLAG
withfourmemberlinksinoneswitchandtwomemberlinksonanothersegment.Aswitchcanhavea
maximumoffourmemberlinks.
MakesurethattheVSXLAGinterfaceonboththeVSXprimaryandsecondaryswitcheshasamemberport
n
configuredandenabled.
Makesurethatyoualsohaveanon-VSXportthatisavailablefortheISL.
n
Procedure
1. Accessthepromptontheswitchyouwanttomaketheprimaryaggregateswitch.
2. Iftheswitchdoesnothaveahostname,createone:
| switch(config)# | hostname | <HOSTNAME> |     |
| --------------- | -------- | ---------- | --- |
3. CreatetherequiredVLANS:
| switch(config)# | vlan 1-20 |     |     |
| --------------- | --------- | --- | --- |
4. CreatetheISLinterface:
| switch(config)#        | interface | lag 128             |     |
| ---------------------- | --------- | ------------------- | --- |
| switch(config-lag-if)# |           | no shutdown         |     |
| switch(config-lag-if)# |           | no routing          |     |
| switch(config-lag-if)# |           | vlan trunk native 1 |     |
| switch(config-lag-if)# |           | lacp mode active    |     |
WhenanativeVLANisdefined(asshownthisexample),theswitchautomaticallyexecutesthevlan
trunk allowed allcommandtoensurethatthedefaultVLANisallowedonthetrunk.Inthis
example,LAG128isbeingusedastheISL.
ThesamelistofVLANsthataretrunkedovertheVSXLAGsmustbeconfiguredontheprimaryand
secondaryVSXswitchesintheglobalconfiguration.ThelistofVLANscanbesyncedtothesecondary
switchifthevsx-synccommandisusedintheVLANcontext.AlsoverifythattheVLANsetisalso
permittedontheISLontheprimaryandsecondaryVSXswitches.ToconfigureVLANtrunkingonthe
ISL,enterthevlan trunk allowed [<VLAN-LIST> | all]command.IfanativeVLANisdefined,the
switchautomaticallyrunsthevlan allcommandtoensurethatthedefaultVLANis
trunk allowed
allowedonthetrunk.ToallowonlyspecificVLANsonthetrunk,enterthevlan trunk allowed
| <VLAN-LIST>command,forexample:vlan |     | trunk allowed | 2,3,4 |
| ---------------------------------- | --- | ------------- | ----- |
5. AddaphysicalinterfaceintotheLAG:
| switch(config)#    | interface   | 1/4/28 |     |
| ------------------ | ----------- | ------ | --- |
| switch(config-if)# | no shutdown |        |     |
SettinguptheVSXenvironment|29

| switch(config-if)# | lag         | 128    |     |
| ------------------ | ----------- | ------ | --- |
| switch(config)#    | interface   | 1/4/32 |     |
| switch(config-if)# | no shutdown |        |     |
| switch(config-if)# | lag         | 128    |     |
6. Enabletheinterfaceforkeepalivecommunication:
| switch(config)#    | interface  | 1/1/5            |     |
| ------------------ | ---------- | ---------------- | --- |
| switch(config-if)# | ip address | 192.168.100.1/24 |     |
7. Gotothevsxcontext:
| switch(config)# | vsx |     |     |
| --------------- | --- | --- | --- |
switch(config-vsx)#
8. Entertheroleprimarycommandforassigningtheprimaryroletoaswitch.Ifyouhavealreadygone
throughthesestepsforconfiguringtheprimaryswitchandyouarenowconfiguringthesecondary
switch,entertherolesecondarycommand.
Settingtheprimaryroleonaswitch:
| switch(config-vsx)# | role | primary |     |
| ------------------- | ---- | ------- | --- |
Settingthesecondaryroleonaswitch:
| switch(config-vsx)# | role | secondary |     |
| ------------------- | ---- | --------- | --- |
9. EnableISL:
| switch(config-vsx)# | inter-switch-link |     | lag 128 |
| ------------------- | ----------------- | --- | ------- |
Inthisexample,ISLisbeingenabledforLAG128.
Beforeyouenterthiscommand,verifythattheinterfaceislayer2andtheLAGisnotaVSXLAG.
10. Enablekeepalive:
switch(config-vsx)# keepalive peer 192.168.100.2 source 192.168.100.1
Inthisexample,192.168.100.2isthepeerIPaddressand192.168.100.1isthesourceIPaddress.
11. Enablethemultichassisinterface:
| switch(config)#        | interface | lag 1 multi-chassis |     |
| ---------------------- | --------- | ------------------- | --- |
| switch(config-lag-if)# |           | no shutdown         |     |
| switch(config-lag-if)# |           | no routing          |     |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 30

| switch(config-lag-if)# |     | vlan | trunk | native  | 1   |
| ---------------------- | --- | ---- | ----- | ------- | --- |
| switch(config-lag-if)# |     | vlan | trunk | allowed | 11  |
12. Addphysicalinterfacesintothemultichassisinterface:
| switch(config)#    | interface |          | 1/1/1 |     |     |
| ------------------ | --------- | -------- | ----- | --- | --- |
| switch(config-if)# | no        | shutdown |       |     |     |
| switch(config-if)# | lag       | 1        |       |     |     |
13. CreateanactivegatewaySVI:
| switch(config)#         | interface |      | vlan    | 11               |                |
| ----------------------- | --------- | ---- | ------- | ---------------- | -------------- |
| switch(config-if-vlan)# |           | ip   | address | 192.168.100.5/16 |                |
| switch(config-if-vlan)# |           | ipv6 | address |                  | 2001:DB8::2/64 |
switch(config-if-vlan)# active-gateway ip 192.168.100.2 mac 00:00:00:00:00:01
switch(config-if-vlan)# active-gateway ipv6 2001:DB8::3 mac 00:00:01:00:00:01
14. EnableuplinkcommunicationforOSPFv2:
| switch(config)#        | router | ospf         | 1       |     |           |
| ---------------------- | ------ | ------------ | ------- | --- | --------- |
| switch(config-ospf-1)# |        | redistribute |         |     | connected |
| switch(config-ospf-1)# |        | area         | 0.0.0.0 |     |           |
Theredistribute connectedcommandisoptionalinthisexample.SeetheCommand-LineInterface
Guideforyourswitchandsoftwareversionformoreinformationabouttheredistribute
connectedcommand.
15. EnableuplinkcommunicationforOSPFv3:
| switch(config)#          | router | ospfv3 | 1            |     |           |
| ------------------------ | ------ | ------ | ------------ | --- | --------- |
| switch(config-ospfv3-1)# |        |        | redistribute |     | connected |
| switch(config-ospfv3-1)# |        |        | area 0.0.0.0 |     |           |
Theredistribute connectedcommandisoptionalinthisexample.SeetheCommand-LineInterface
Guideforyourswitchandsoftwareversionformoreinformationabouttheredistribute
connectedcommand.
16. CreatetheloopbackinterfaceandenableOSPFv2:
| switch(config)#             | interface |     | loopback | 1       |                |
| --------------------------- | --------- | --- | -------- | ------- | -------------- |
| switch(config-loopback-if)# |           |     | ip       | address | 192.168.0.1/32 |
| switch(config-loopback-if)# |           |     | ip       | ospf    | 1 area 0.0.0.0 |
17. EnableOSPFv2/v3onthephysicalport:
| switch(config)#    | interface |          | 1/4/30          |     |     |
| ------------------ | --------- | -------- | --------------- | --- | --- |
| switch(config-if)# | no        | shutdown |                 |     |     |
| switch(config-if)# | ip        | address  | 192.168.10.0/31 |     |     |
SettinguptheVSXenvironment|31

|     | switch(config-if)# |     | ipv6    | address | 2001:11::1/64 |         |     |     |
| --- | ------------------ | --- | ------- | ------- | ------------- | ------- | --- | --- |
|     | switch(config-if)# |     | ip ospf | 1       | area 0.0.0.0  |         |     |     |
|     | switch(config-if)# |     | ipv6    | ospfv3  | 1 area        | 0.0.0.0 |     |     |
18. Repeatthepreviousstepsforthesecondaryaggregateswitch.
19. Viewtherunningconfigurationbyenteringthefollowingontheprimaryandsecondaryswitches:
|     | switch# | show running-config |     |     |     |     |     |     |
| --- | ------- | ------------------- | --- | --- | --- | --- | --- | --- |
20. VerifythattheISLlinkisin-sync,theroleoftheswitch,andthekeepalivestate(ifenabled)byentering
thefollowingontheprimaryandsecondaryswitches:
|     | vsx-primary# | show             | vsx brief |                |     |                         |     |     |
| --- | ------------ | ---------------- | --------- | -------------- | --- | ----------------------- | --- | --- |
|     | ISL State    |                  |           |                |     | : In-Sync               |     |     |
|     | Device       | State            |           |                |     | : Peer-Established      |     |     |
|     | Keepalive    | State            |           |                |     | : Keepalive-Established |     |     |
|     | Device       | Role             |           |                |     | : primary               |     |     |
|     | Number       | of Multi-chassis |           | LAG interfaces |     | : 2                     |     |     |
21. VerifytheVSXstatusbyenteringthefollowingontheprimaryandsecondaryswitches:
|     | switch#         | show vsx | status |     |     |     |     |     |
| --- | --------------- | -------- | ------ | --- | --- | --- | --- | --- |
|     | VSX Operational |          | State  |     |     |     |     |     |
---------------------
|     | ISL          | channel      |                   | : In-Sync        |     |     |                   |     |
| --- | ------------ | ------------ | ----------------- | ---------------- | --- | --- | ----------------- | --- |
|     | ISL          | mgmt channel |                   | : operational    |     |     |                   |     |
|     | Config       | Sync Status  |                   | : in-sync        |     |     |                   |     |
|     | NAE          |              |                   | : peer_reachable |     |     |                   |     |
|     | HTTPS        | Server       |                   | : peer_reachable |     |     |                   |     |
|     | Attribute    |              | Local             |                  |     |     | Peer              |     |
|     | ------------ |              | --------          |                  |     |     | --------          |     |
|     | ISL link     |              | 1/1/43            |                  |     |     | 1/1/43            |     |
|     | ISL version  |              | 2                 |                  |     |     | 2                 |     |
|     | System       | MAC          | 48:0f:cf:af:70:84 |                  |     |     | 48:0f:cf:af:c2:84 |     |
|     | Platform     |              | 8320              |                  |     |     | 8320              |     |
|     | Software     | Version      | 10.0x.xxxx        |                  |     |     | 10.0x.xxxx        |     |
|     | Device       | Role         | primary           |                  |     |     | secondary         |     |
22. VerifytheLACPinterfacestatusbyenteringthefollowingontheprimaryandsecondaryswitches:
|     | switch# | show lacp | interfaces |     |     |     |     |     |
| --- | ------- | --------- | ---------- | --- | --- | --- | --- | --- |
23. Verifytheuplink(layer3communication)byenteringthefollowingontheprimaryandsecondary
switches:
|             | switch# | show ip   | ospf neighbors |        |     |       |        |        |
| ----------- | ------- | --------- | -------------- | ------ | --- | ----- | ------ | ------ |
| Configuring |         | an AOS-CX |                | switch |     | as an | access | switch |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 32

AnaccessswitchcanbeanyswitchthatsupportsLACPorstaticlinkaggregation.Thestepsinthissection
arespecificallyforanAOS-CXswitch.Fornon-AOS-CXswitches,refertothedocumentationforyourswitch
abouthowtoenableLACPorstaticlinkaggregation.
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
5. Createeitheranaccessinterfaceoratrunkinterface.Youcancreatebothallowedandnativetrunk
interfacesontheaccessswitch.
Tocreateanaccessinterface:
n
| switch(config-lag-if)# |     | vlan | access <VLAN_ID> |
| ---------------------- | --- | ---- | ---------------- |
Forexample:
SettinguptheVSXenvironment|33

| switch(config-lag-if)# | vlan access | 5   |     |
| ---------------------- | ----------- | --- | --- |
Tocreateanativetrunkinterface:
n
a. Tocreateanallowedtrunkinterface:
| switch(config-lag-if)# |     | vlan trunk allowed | <VLAN_LIST> |
| ---------------------- | --- | ------------------ | ----------- |
Forexample:
| switch(config-lag-if)# |     | vlan trunk allowed | 30,50,120 |
| ---------------------- | --- | ------------------ | --------- |
b. Tocreateanativetrunkinterface:
| switch(config-lag-if)# |     | vlan trunk native | <VLAN_ID> [tag] |
| ---------------------- | --- | ----------------- | --------------- |
Forexample:
| switch(config-lag-if)# |     | vlan trunk native | 30 tag |
| ---------------------- | --- | ----------------- | ------ |
ThetrunkparameterenablestaggingonanativeVLAN.Onlyincomingpacketsthataretaggedwith
thematchingVLANIDareaccepted.Incomingpacketsthatareuntaggedaredroppedexceptfor
BPDUs.Egresspacketsaretagged.
6. Formultipleaccessswitchesinyourtopology,repeattheprevioussteps.
7. Verifytheconfiguration:
| switch# show lacp interfaces |     |     |     |
| ---------------------------- | --- | --- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 34

Chapter 5

Enabling VSX configuration
synchronization

Enabling VSX configuration synchronization

VSX configuration synchronization simplifies VSX solution management, reduces configuration
misconfiguration and drift across VSX peer switches. With configuration synchronization enabled, the
primary peer configuration is synced to the secondary peer. This synchronization is controlled in an opt-in
manner by enabling VSX synchronization on a section of configuration.

VSX configuration synchronization
If one or more of the following scenarios occur, the secondary switch will receive the configuration update
after it fulfills synchronization requirements and is fully enabled:

n The secondary switch is not currently present.

n The secondary switch is not currently connected to the primary switch through the ISL.

n The secondary switch is not currently configured for VSX configuration synchronization at the time VSX

configuration synchronization is enabled on the primary switch.

You can only enable a specific configuration for syncing through the vsx-sync CLI extension on the primary
switch. This extension is blocked on the secondary peer switch except when VSX configuration-
synchronization is disabled or the ISL link is down.

Features supporting VSX

You can enable VSX synchronization at:

n The global level: See Enabling VSX synchronization at the global level for a listing of features supporting

VSX synchronization at the global level.

n The context level: See Enabling VSX synchronization at the context level for a listing of features

supporting VSX synchronization at the context level.

VSX synchronization requirements

n Software image versions must be the same on both switches.

n The output from the show vsx status command must show in-sync for Config Sync Status.

n Primary and secondary roles configured.

n An interswitch link must be configured.

n When enabling VSX synchronization under a physical interface, a VLAN interface, or a VSX LAG, create on
the secondary switch the physical interface, VLAN interface, or VSX LAG with the same name and routing
setting as on the primary switch. For example, if the primary switch has a physical interface of 1/1/1, you
must create another physical interface of 1/1/1 on the secondary switch. Also, if the primary VSX switch
has routing enabled, the secondary switch must have routing enabled. Once the name and routing
information is the same, VSX synchronization synchronizes the additional configuration information from
the primary VSX switch to the secondary VSX switch.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

35

Itisrecommendedto:
n EnablekeepaliveforpreventingtrafficlossduringanISLlinkfailure.
n AssignacommonsystemMACtopreventtrafficlossincaseswhenthesecondaryVSXswitchisrestored
beforetheprimaryVSXswitch.
| Enabling | VSX | synchronization |     | at the | global |     | level |     |     |     |
| -------- | --- | --------------- | --- | ------ | ------ | --- | ----- | --- | --- | --- |
ThecommandsinthistableareforenablingVSXsynchronizationatthegloballevelforafeature.
Commandfor
| Feature |     |     | Example |     |     |     |     |     |     |     |
| ------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
enabling
vsx-sync aaa
AAAconfigurations,
|     |     |     | switch(config)# |     | vsx |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
includinguser,
|     |     |     | switch(config-vsx)# |     |     | vsx-sync |     | aaa |     |     |
| --- | --- | --- | ------------------- | --- | --- | -------- | --- | --- | --- | --- |
RADIUSserver,and
TACACS+server.
vsx-sync acl-
AccessListLog
|     |     |     | switch(config)# |     | access-list |     |     | log timer | 30  |     |
| --- | --- | --- | --------------- | --- | ----------- | --- | --- | --------- | --- | --- |
log-timer
| Timer           |     |     | switch(config)#     |     | vsx |          |     |               |     |     |
| --------------- | --- | --- | ------------------- | --- | --- | -------- | --- | ------------- | --- | --- |
| configurations. |     |     | switch(config-vsx)# |     |     | vsx-sync |     | acl-log-timer |     |     |
vsx-sync arp-
ARPsecurity
|     |     | security | primary_sw(config)# |     |     | vsx |     |     |     |     |
| --- | --- | -------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
configurations.
|     |     |     | primary_sw(config-vsx)# |     |     |     | vsx-sync | arp-security |     |     |
| --- | --- | --- | ----------------------- | --- | --- | --- | -------- | ------------ | --- | --- |
|     |     |     | primary_sw(config-vsx)# |     |     |     | vsx-sync | mclag-       |     |     |
interfaces
| BFDconfigurations. |     | vsx-sync bfd- |                 |     |     |                       |     |     |     |      |
| ------------------ | --- | ------------- | --------------- | --- | --- | --------------------- | --- | --- | --- | ---- |
|                    |     | global        | switch(config)# |     | bfd | detect-multiplier     |     |     | 1   |      |
|                    |     |               | switch(config)# |     | bfd | min-transmit-interval |     |     |     | 1000 |
|                    |     |               | switch(config)# |     | bfd | min-receive-interval  |     |     |     | 1000 |
|                    |     |               | switch(config)# |     | bfd | echo-src-ip-address   |     |     |     |      |
2.2.2.2
|     |     |     | switch(config)# |     | bfd | min-echo-receive-interval |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | ------------------------- | --- | --- | --- | --- |
1000
|                    |     |              | switch(config)#     |           | vsx |                |     |            |          |     |
| ------------------ | --- | ------------ | ------------------- | --------- | --- | -------------- | --- | ---------- | -------- | --- |
|                    |     |              | switch(config-vsx)# |           |     | vsx-sync       |     | bfd-global |          |     |
| BGPconfigurations. |     | vsx-sync bgp |                     |           |     |                |     |            |          |     |
|                    |     |              | switch(config)#     |           |     | ip aspath-list |     | list1      | seq      | 10  |
|                    |     |              |                     | permit 10 |     |                |     |            |          |     |
|                    |     |              | switch(config)#     |           | ip  | community-list |     |            | expanded |     |
com1
|     |     |     |                                  | seq 10 permit | 10        |                   |      |        |          |     |
| --- | --- | --- | -------------------------------- | ------------- | --------- | ----------------- | ---- | ------ | -------- | --- |
|     |     |     | switch(config)#                  |               | ip        | extcommunity-list |      |        | standard |     |
|     |     |     |                                  | ext1 seq      | 10 permit | rt                | 10:4 |        |          |     |
|     |     |     | switch(config)#                  |               | ip        | prefix-list       |      | pref1  | seq      | 10  |
|     |     |     |                                  | permit any    |           |                   |      |        |          |     |
|     |     |     | switch(config)#                  |               | route-map |                   | rm1  | permit |          |     |
|     |     |     | switch(config-route-map-rm1-10)# |               |           |                   |      |        | match    | ip  |
EnablingVSXconfigurationsynchronization|36

Commandfor
| Feature |     | Example |     |     |     |
| ------- | --- | ------- | --- | --- | --- |
enabling
|     |     | next-hop 1.1.1.1    |                |           |         |
| --- | --- | ------------------- | -------------- | --------- | ------- |
|     |     | switch(config)#     | router         | bgp 100   |         |
|     |     | switch(config-bgp)# | bgp            | router-id | 1.1.1.1 |
|     |     | switch(config-bgp)# | neighbor       | 12.1.1.1  |         |
|     |     | remote-as 1         |                |           |         |
|     |     | switch(config-bgp)# | address-family |           | ipv4    |
unicast
switch(config-bgp-ipv4-uc)#
|     |     |     |     | neighbor | 12.1.1.1 |
| --- | --- | --- | --- | -------- | -------- |
activate
|     |     | switch(config)#     | vsx      |     |     |
| --- | --- | ------------------- | -------- | --- | --- |
|     |     | switch(config-vsx)# | vsx-sync | bgp |     |
vsx-sync copp-
CoPPpolicy
|     |     | switch(config)# | vsx |     |     |
| --- | --- | --------------- | --- | --- | --- |
policy
| configurations. |               | switch(config-vsx)# | vsx-sync  | copp-policy |     |
| --------------- | ------------- | ------------------- | --------- | ----------- | --- |
| DCBx            | vsx-sync dcb- |                     |           |             |     |
|                 | global        | switch(config)#     | lldp dcbx |             |     |
configurations
|                  |                | switch(config)#     | dcbx application |            | iscsi |
| ---------------- | -------------- | ------------------- | ---------------- | ---------- | ----- |
| (8325and8360     |                | priority 7          |                  |            |       |
| seriesswitches). |                | switch(config)#     | vsx              |            |       |
|                  |                | switch(config-vsx)# | vsx-sync         | dcb-global |       |
| DHCPv4and        | vsx-sync dhcp- |                     |                  |            |       |
switch(config)#
|     | relay |     | interface | 1/1/1 |     |
| --- | ----- | --- | --------- | ----- | --- |
DHCPv6relay
|                 |     | switch(config-if)# | ip helper-address |     |     |
| --------------- | --- | ------------------ | ----------------- | --- | --- |
| configurations. |     | 192.168.10.1       |                   |     |     |
|                 |     | switch(config-if)# | ip helper-address |     |     |
192.168.20.1
|     |     | switch(config)#    | interface         | 1/1/2 |     |
| --- | --- | ------------------ | ----------------- | ----- | --- |
|     |     | switch(config-if)# | ip helper-address |       |     |
192.168.30.1
|     |     | switch(config)# | dhcp-relay | option | 82  |
| --- | --- | --------------- | ---------- | ------ | --- |
|     |     | switch(config)# | vsx        |        |     |
switch(config-vsx)#
|     |     |     | vsx-sync | dhcp-relay |     |
| --- | --- | --- | -------- | ---------- | --- |
vsx-sync dhcp-
DHCPv4server
|                   |        | switch(config)#             | dhcp-server       | external-storage |           |
| ----------------- | ------ | --------------------------- | ----------------- | ---------------- | --------- |
| configurations,   | server |                             |                   |                  |           |
|                   |        | dhcp-dbs file               | dhcpv4_lease_file |                  | delay 600 |
| includingexternal |        | switch(config)#             | dhcp-server       | vrf              | default   |
|                   |        | switch(config-dhcp-server)# |                   | pool             | test      |
storage
|     |     | switch(config-dhcp-server-pool)# |     |     | range |
| --- | --- | -------------------------------- | --- | --- | ----- |
configurations.
10.0.0.20
10.0.0.30
|     |     | switch(config-dhcp-server-pool)# |     |     | default- |
| --- | --- | -------------------------------- | --- | --- | -------- |
router
|     |     | 10.0.0.1 10.0.0.10               |                       |             |             |
| --- | --- | -------------------------------- | --------------------- | ----------- | ----------- |
|     |     | switch(config-dhcp-server-pool)# |                       |             | static-bind |
|     |     | ip 10.0.0.1                      | mac 24:be:05:24:75:73 |             |             |
|     |     | switch(config)#                  | vsx                   |             |             |
|     |     | switch(config-vsx)#              | vsx-sync              | dhcp-server |             |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 37

Commandfor
| Feature |     | Example |     |     |     |
| ------- | --- | ------- | --- | --- | --- |
enabling
| DHCPv6server | vsx-sync      |                 |               |                  |     |
| ------------ | ------------- | --------------- | ------------- | ---------------- | --- |
|              | dhcpv6-server | switch(config)# | dhcpv6-server | external-storage |     |
configurations,
|                   |     | dhcpv6-dbs                  | file dhcpv6_lease_file |             | delay 600 |
| ----------------- | --- | --------------------------- | ---------------------- | ----------- | --------- |
| includingexternal |     | switch(config)#             | dhcp-server            | vrf default |           |
|                   |     | switch(config-dhcp-server)# |                        | pool        | test      |
storage
|     |     | switch(config-dhcpv6-server-pool)# |     |     | range |
| --- | --- | ---------------------------------- | --- | --- | ----- |
configurations.
2001::1
|     |     | 2001::10 | prefix-len 64 |     |     |
| --- | --- | -------- | ------------- | --- | --- |
switch(config-dhcpv6-server-pool)#
option 22
ipv6 2001::12
|                    |              | switch(config-dhcpv6-server-pool)# |           |                    | static-bind |
| ------------------ | ------------ | ---------------------------------- | --------- | ------------------ | ----------- |
|                    |              | ipv6 2001::11                      | client-id | 1:0:a0:24:ab:fb:9c |             |
|                    |              | switch(config)#                    | vsx       |                    |             |
|                    |              | switch(config-vsx)#                | vsx-sync  | dhcpv6-server      |             |
| DNSconfigurations. | vsx-sync dns |                                    |           |                    |             |
|                    |              | switch(config)#                    | vsx       |                    |             |
switch(config-vsx)#
|     |     |     | vsx-sync | dns |     |
| --- | --- | --- | -------- | --- | --- |
vsx-sync evpn
EVPN
|     |     | switch(config)# | vlan 2 |     |     |
| --- | --- | --------------- | ------ | --- | --- |
configurations.
|                  |          | switch(config-vlan-2)#      |              | vsx-sync     |     |
| ---------------- | -------- | --------------------------- | ------------ | ------------ | --- |
|                  |          | switch(config)#             | evpn         |              |     |
|                  |          | switch(config-evpn)#        | vlan         | 2            |     |
|                  |          | switch(config-evpn-vlan-2)# |              | rd 5:5       |     |
|                  |          | switch(config-evpn-vlan-2)# |              | route-target |     |
|                  |          | export 1:1                  |              |              |     |
|                  |          | switch(config-evpn-vlan-2)# |              | route-target |     |
|                  |          | import 1:1                  |              |              |     |
|                  |          | switch(config)#             | vsx          |              |     |
|                  |          | switch(config-vsx)#         | vsx-sync     | evpn         |     |
| Globalclassifier | vsx-sync |                             |              |              |     |
|                  |          | switch(config)#             | apply policy | testPolicy   | in  |
policy-global
| policy          |     | switch(config)#     | vsx      |               |     |
| --------------- | --- | ------------------- | -------- | ------------- | --- |
| configurations. |     | switch(config-vsx)# |          |               |     |
|                 |     |                     | vsx-sync | policy-global |     |
vsx-sync icmp-
IPICMP
|                 |               | switch(config)#     | vsx         |          |     |
| --------------- | ------------- | ------------------- | ----------- | -------- | --- |
| configurations. | tcp           |                     |             |          |     |
|                 |               | switch(config-vsx)# | vsx-sync    | icmp-tcp |     |
| LLDP            | vsx-sync lldp |                     |             |          |     |
|                 |               | switch(config)#     | lldp reinit | 6        |     |
| configurations. |               | switch(config)#     |             |          |     |
vsx
|     |     | switch(config-vsx)# | vsx-sync | lldp |     |
| --- | --- | ------------------- | -------- | ---- | --- |
vsx-sync loop-
Loopprotect
|                 |                 | switch(config)# | loop-protect | transmit-       |     |
| --------------- | --------------- | --------------- | ------------ | --------------- | --- |
| configurations, | protect-globall |                 |              |                 |     |
|                 |                 | interval        | 10           |                 |     |
| suchastransmit- |                 | switch(config)# | loop-protect | re-enable-timer |     |
300
intervalandre-
|     |     | switch(config)# | vsx |     |     |
| --- | --- | --------------- | --- | --- | --- |
enable-timer.
EnablingVSXconfigurationsynchronization|38

Commandfor
| Feature | Example |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
enabling
|     | switch(config-vsx)# |     |     | vsx-sync | loop-protect- |     |     |
| --- | ------------------- | --- | --- | -------- | ------------- | --- | --- |
global
MAClockout vsx-sync mac-
|     | switch(config)# |     | mac-lockout |     | 10:10:10:10:10:10 |     |     |
| --- | --------------- | --- | ----------- | --- | ----------------- | --- | --- |
lockout
| configurations. | switch(config)# |     | vsx |     |     |     |     |
| --------------- | --------------- | --- | --- | --- | --- | --- | --- |
switch(config-vsx)#
|     |     |     |     | vsx-sync | mac-lockout |     |     |
| --- | --- | --- | --- | -------- | ----------- | --- | --- |
vsx-sync nd-
NDsnooping
|     | switch(config)# |     | vsx |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- | --- |
configurations. snooping
|     | switch(config-vsx)# |     |     | vsx-sync | nd-snooping |     |     |
| --- | ------------------- | --- | --- | -------- | ----------- | --- | --- |
Staticneighbor vsx-sync
|     | DUT-1(config-vsx)# |     | show | run | in  | vlan127 |     |
| --- | ------------------ | --- | ---- | --- | --- | ------- | --- |
neighbor
| configurations. | interface | vlan127    |              |            |     |     |     |
| --------------- | --------- | ---------- | ------------ | ---------- | --- | --- | --- |
|                 |           | ip address | 137.1.1.1/16 |            |     |     |     |
|                 |           | ipv6       | address      | 7f00::1/64 |     |     |     |
|                 |           | arp ipv4   | 137.1.1.35   |            | mac |     |     |
00:12:01:00:00:1a
|     |     | arp ipv4 | 137.1.1.70 |     | mac |     |     |
| --- | --- | -------- | ---------- | --- | --- | --- | --- |
00:12:01:00:00:3d
exit
DUT-1(config-vsx)#
|     | switch(config)# |     | vsx |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- | --- |
switch(config-vsx)#
|     |     |     |     | vsx-sync | neighbor |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | --- |
vsx-sync ospf
OSPF
|     | switch(config)# |     | router | ospf | 1   |     |     |
| --- | --------------- | --- | ------ | ---- | --- | --- | --- |
configurations.
|     | switch(config-ospf-1)# |      |     | area         | 0      |           |     |
| --- | ---------------------- | ---- | --- | ------------ | ------ | --------- | --- |
|     | switch(config-ospf-1)# |      |     | area         | 1 nssa |           |     |
|     | switch(config-ospf-1)# |      |     | area         | 2 stub |           |     |
|     | switch(config-ospf-1)# |      |     | redistribute |        | connected |     |
|     | route-map              | map1 |     |              |        |           |     |
switch(config)#
|     |                          |     | router | ospfv3 | 1          |         |     |
| --- | ------------------------ | --- | ------ | ------ | ---------- | ------- | --- |
|     | switch(config-ospfv3-1)# |     |        |        | max-metric | router- |     |
lsa on-startup
|     | switch(config-ospfv3-1)# |     |      |        | bfd all-interfaces |          |     |
| --- | ------------------------ | --- | ---- | ------ | ------------------ | -------- | --- |
|     | switch(config-if)#       |     | ip   | ospf   | 1 area             | 0        |     |
|     | switch(config-if)#       |     | ip   | ospf   | hello-interval     |          | 33  |
|     | switch(config-if)#       |     | ipv6 | ospfv3 |                    | 1 area 0 |     |
|     | switch(config-if)#       |     | ipv6 | ospfv3 |                    | dead-    |     |
|     | interval                 | 55  |      |        |                    |          |     |
|     | switch(config)#          |     | vsx  |        |                    |          |     |
switch(config-vsx)#
|     |     |     |     | vsx-sync | ospf |     |     |
| --- | --- | --- | --- | -------- | ---- | --- | --- |
vsx-sync route-
Routemap
|     | switch(config)# |     | ip  | aspath-list |     | list1 seq | 10  |
| --- | --------------- | --- | --- | ----------- | --- | --------- | --- |
configurations. map
|     | permit          | 10     |                      |         |     |          |     |
| --- | --------------- | ------ | -------------------- | ------- | --- | -------- | --- |
|     | switch(config)# |        | ip community-list    |         |     | expanded |     |
|     | com1            | seq 10 | permit               | 10      |     |          |     |
|     | switch(config)# |        | ip extcommunity-list |         |     | standard |     |
|     | ext1            | seq 10 | permit               | rt 10:4 |     |          |     |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 39

Commandfor
Feature Example
enabling
|     | switch(config)#                  | ip prefix-list | pref1 seq  | 10  |
| --- | -------------------------------- | -------------- | ---------- | --- |
|     | permit any                       |                |            |     |
|     | switch(config)#                  | route-map      | rm1 permit |     |
|     | switch(config-route-map-rm1-10)# |                | match      | ip  |
|     | next-hop 1.1.1.1                 |                |            |     |
|     | switch(config)#                  | vsx            |            |     |
|     | switch(config-vsx)#              | vsx-sync       | route-map  |     |
QoSConfigurations, vsx-sync qos-
| global | switch(config)# | vsx |     |     |
| ------ | --------------- | --- | --- | --- |
suchasCoSmap,
|     | switch(config-vsx)# | vsx-sync | qos-global |     |
| --- | ------------------- | -------- | ---------- | --- |
DSCPmap,and
trustpolicy.
vsx-sync sflow
sFlow
|     | switch(config)# | vsx |     |     |
| --- | --------------- | --- | --- | --- |
configurations.
|     | switch(config-vsx)# | vsx-sync | sflow |     |
| --- | ------------------- | -------- | ----- | --- |
sFlowglobal vsx-sync sflow-
switch(config)#
| global |     | sflow collector | 1.1.1.1 |     |
| ------ | --- | --------------- | ------- | --- |
configurations.
|     | switch(config)#     | vsx      |              |     |
| --- | ------------------- | -------- | ------------ | --- |
|     | switch(config-vsx)# | vsx-sync | sflow-global |     |
vsx-sync snmp
SNMP
|     | switch(config)# | vsx |     |     |
| --- | --------------- | --- | --- | --- |
configurations.
|     | switch(config-vsx)# | vsx-sync | snmp |     |
| --- | ------------------- | -------- | ---- | --- |
SSHconfigurations. vsx-sync ssh
|     | switch(config)#     | vsx      |     |     |
| --- | ------------------- | -------- | --- | --- |
|     | switch(config-vsx)# | vsx-sync | ssh |     |
vsx-sync
Staticroutes.
|     | switch(config)# | vsx |     |     |
| --- | --------------- | --- | --- | --- |
static-routes
|     | switch(config-vsx)# | vsx-sync | static-routes |     |
| --- | ------------------- | -------- | ------------- | --- |
STPconfigurations. vsx-sync stp-
| global | switch(config)# | spanning-tree | config-name |     |
| ------ | --------------- | ------------- | ----------- | --- |
abc
|     | switch(config)#     | spanning-tree | config-    |     |
| --- | ------------------- | ------------- | ---------- | --- |
|     | revision 1          |               |            |     |
|     | switch(config)#     | vsx           |            |     |
|     | switch(config-vsx)# | vsx-sync      | stp-global |     |
Time-related vsx-sync time
switch(config)#
vsx
configurations,
|     | switch(config-vsx)# | vsx-sync | time |     |
| --- | ------------------- | -------- | ---- | --- |
includingNTPand
timezone
configurations.
EnablingVSXconfigurationsynchronization|40

Commandfor
| Feature |     | Example |     |     |     |
| ------- | --- | ------- | --- | --- | --- |
enabling
| UDPforwarder | vsx-sync upd- |                 |     |     |     |
| ------------ | ------------- | --------------- | --- | --- | --- |
|              | forwarder     | switch(config)# | vsx |     |     |
configurations.
|                    |               | switch(config-vsx)# | vsx-sync | upd-forwarder |     |
| ------------------ | ------------- | ------------------- | -------- | ------------- | --- |
| VRFconfigurations. | vsx-sync vrf  |                     |          |               |     |
|                    |               | switch(config)#     | vsx      |               |     |
|                    |               | switch(config-vsx)# | vsx-sync | vrf           |     |
| VSXconfigurations: | vsx-sync vsx- |                     |          |               |     |
|                    | global        | switch(config)#     | vsx      |               |     |
ISL:
| n   |     | switch(config-vsx)# | inter-switch-link |     | dead- |
| --- | --- | ------------------- | ----------------- | --- | ----- |
|     |     | interval 15         |                   |     |       |
o Deadinterval.
|          |     | switch(config-vsx)# | inter-switch-link |     | hello- |
| -------- | --- | ------------------- | ----------------- | --- | ------ |
| o Hellow |     | interval 2          |                   |     |        |
|          |     | switch(config-vsx)# | inter-switch-link |     | hold-  |
interval.
time 1
| o Holdtime. |     | switch(config-vsx)# |          |            |     |
| ----------- | --- | ------------------- | -------- | ---------- | --- |
|             |     |                     | vsx-sync | vsx-global |     |
o Peerdetect
interval.
Keepalive:
n
o Deadinterval.
o Hellow
interval.
o UDPport
number.
Thedelaytime
n
settingforthe
link-updelay
timer.
n Thesplit
recoverysetting.
Thesystem
n
MACaddress.
| VSXLAGinterfaces. | vsx-sync mclag- |                 |     |     |     |
| ----------------- | --------------- | --------------- | --- | --- | --- |
|                   |                 | switch(config)# | vsx |     |     |
interfaces
|     |     | switch(config-vsx)# | vsx-sync | mclag-interfaces |     |
| --- | --- | ------------------- | -------- | ---------------- | --- |
vsx-sync vrrp
VRRP
|     |     | switch(config)# | router vrrp | enable |     |
| --- | --- | --------------- | ----------- | ------ | --- |
configurations.
|     |     | switch(config-if)#      | vrrp 1  | address-family | ipv4 |
| --- | --- | ----------------------- | ------- | -------------- | ---- |
|     |     | switch(config-if-vrrp)# | address | 1.1.1.100      |      |
primary
|     |     | switch(config-if-vrrp)# | timers   | advertise      | 1000 |
| --- | --- | ----------------------- | -------- | -------------- | ---- |
|     |     | switch(config-if-vrrp)# | no       | shutdown       |      |
|     |     | switch(config-if)#      | vrr 1    | address-family | ipv6 |
|     |     | switch(config)#         | vsx      |                |      |
|     |     | switch(config-vsx)#     | vsx-sync | vrrp           |      |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 41

| Enabling | VSX synchronization | at the | context | level |     |
| -------- | ------------------- | ------ | ------- | ----- | --- |
ThecommandsinthistableareforenablingVSXsynchronizationatthecontextlevel,suchasforanaccess
list,aninterface,oraLAG.
WhenenablingVSXsynchronizationunderaphysicalinterface,aVLANinterface,oraVSXLAG,createonthe
secondaryswitchthephysicalinterface,VLANinterface,orVSXLAGwiththesamenameandroutingsettingas
ontheprimaryswitch.Forexample,iftheprimaryswitchhasaphysicalinterfaceof1/1/1,youmustcreate
anotherphysicalinterfaceof1/1/1onthesecondaryswitch.Also,iftheprimaryVSXswitchhasroutingenabled,
thesecondaryswitchmusthaveroutingenabled.Oncethenameandroutinginformationisthesame,VSX
synchronizationsynchronizestheadditionalconfigurationinformationfromtheprimaryVSXswitchtothe
secondaryVSXswitch.
Command
| Feature |     | Example |     |     |     |
| ------- | --- | ------- | --- | --- | --- |
forenabling
| Accesslists | vsx-sync |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
EnablingVSXsynchronizationforaccesslistsassociatedwithinterface
| associatedwith | access- |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- |
1/1/1:
| interfaceorLAG. | lists |                 |           |       |     |
| --------------- | ----- | --------------- | --------- | ----- | --- |
|                 |       | switch(config)# | interface | 1/1/1 |     |
switch(config-if)#
|     |     |     | vsx-sync | access-lists |     |
| --- | --- | --- | -------- | ------------ | --- |
EnablingVSXsynchronizationforaccesslistsunderinterfaceLAG2:
|     |     | switch(config)#        | interface | lag 2                 |     |
| --- | --- | ---------------------- | --------- | --------------------- | --- |
|     |     | switch(config-lag-if)# |           | vsx-sync access-lists |     |
|     |     | switch(config-lag-if)# |           | apply access-list     | ip  |
test1 in
| Anaccesslist | vsx-sync |     |     |     |     |
| ------------ | -------- | --- | --- | --- | --- |
switch(config)#
| context.        |          |                        | access-list | ip ITBoston |     |
| --------------- | -------- | ---------------------- | ----------- | ----------- | --- |
|                 |          | switch(config-acl-ip)# |             | vsx-sync    |     |
| Oneormoreactive | vsx-sync |                        |             |             |     |
EnablingVSXsyncforactivegatewaysunderinterfaceVLAN5:
gatewaysassociated
active-
| withaninterface. |     | Enterontheprimaryswitch: |     |     |     |
| ---------------- | --- | ------------------------ | --- | --- | --- |
gateways
|     |     | switch(config)#         | interface | vlan 5                   |     |
| --- | --- | ----------------------- | --------- | ------------------------ | --- |
|     |     | switch(config-if-vlan)# |           | vsx-sync active-gateways |     |
Enteronthesecondaryswitch:
|                |          | switch(config)#          | interface | vlan 5    |     |
| -------------- | -------- | ------------------------ | --------- | --------- | --- |
| Aclasscontext. | vsx-sync |                          |           |           |     |
|                |          | switch(config)#          | class ip  | ITHouston |     |
|                |          | switch(config-class-ip)# |           | vsx-sync  |     |
EnablingVSXconfigurationsynchronization|42

Command
| Feature | Example |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- |
forenabling
Apolicycontext. vsx-sync
switch(config)#
policy ITPaloAlto
|     | switch(config-policy)# |     | vsx-sync |     |     |
| --- | ---------------------- | --- | -------- | --- | --- |
AnIRDPassociation vsx-sync
| underaninterface | switch(config)# | interface | 1/1/1 |     |     |
| ---------------- | --------------- | --------- | ----- | --- | --- |
irdp
| enabledforsyncing. | switch(config-if)# | ip irdp |                   |     |     |
| ------------------ | ------------------ | ------- | ----------------- | --- | --- |
|                    | switch(config-if)# | ip irdp | minadvertinterval |     | 550 |
|                    | switch(config-if)# | ip irdp | maxadvertinterval |     | 850 |
|                    | switch(config-if)# | ip irdp | holdtime          | 900 |     |
switch(config-if)#
|     |     | vsx-sync | irdp |     |     |
| --- | --- | -------- | ---- | --- | --- |
QoSassociatedwith vsx-sync
EnablingVSXsynchronizationforQoSassociationsunderinterface
aninterfaceorLAG.
qos 1/1/5:
|     | switch(config)#    | interface | 1/1/5 |     |     |
| --- | ------------------ | --------- | ----- | --- | --- |
|     | switch(config-if)# | vsx-sync  | qos   |     |     |
EnablingVSXsynchronizationforQoSunderinterfaceLAG3:
switch(config)#
|     |                        | interface | lag 3    |     |     |
| --- | ---------------------- | --------- | -------- | --- | --- |
|     | switch(config-lag-if)# |           | vsx-sync | qos |     |
AQoSqueue-profile. vsx-sync
|     | switch(config)#       | qos queue-profile |       | qprofile1        |     |
| --- | --------------------- | ----------------- | ----- | ---------------- | --- |
|     | switch(config-queue)# | vsx-sync          |       |                  |     |
|     | switch(config-queue)# | map               | queue | 0 local-priority |     |
7
|     | switch(config-queue)# | map | queue | 1 local-priority |     |
| --- | --------------------- | --- | ----- | ---------------- | --- |
6
|     | switch(config-queue)# | map | queue | 2 local-priority |     |
| --- | --------------------- | --- | ----- | ---------------- | --- |
5
|     | switch(config-queue)# | map | queue | 3 local-priority |     |
| --- | --------------------- | --- | ----- | ---------------- | --- |
4
|     | switch(config-queue)# | map | queue | 4 local-priority |     |
| --- | --------------------- | --- | ----- | ---------------- | --- |
3
|     | switch(config-queue)# | map | queue | 5 local-priority |     |
| --- | --------------------- | --- | ----- | ---------------- | --- |
2
|     | switch(config-queue)# | map | queue | 6 local-priority |     |
| --- | --------------------- | --- | ----- | ---------------- | --- |
1
|     | switch(config-queue)# | map | queue | 7 local-priority |     |
| --- | --------------------- | --- | ----- | ---------------- | --- |
0
AQoSschedule- vsx-sync
| profile. | switch(config)#          | qos schedule-profile |          | sprofile1      |     |
| -------- | ------------------------ | -------------------- | -------- | -------------- | --- |
|          | switch(config-schedule)# |                      | vsx-sync |                |     |
|          | switch(config-schedule)# |                      | dwrr     | queue 0 weight | 1   |
|          | switch(config-schedule)# |                      | dwrr     | queue 1 weight | 10  |
switch(config-schedule)#
|     |                          |     | dwrr | queue 2 weight | 20  |
| --- | ------------------------ | --- | ---- | -------------- | --- |
|     | switch(config-schedule)# |     | dwrr | queue 3 weight | 30  |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 43

Command
| Feature |     |     | Example |     |     |     |
| ------- | --- | --- | ------- | --- | --- | --- |
forenabling
switch(config-schedule)#
|                    |            |     |                          |           | dwrr queue          | 4 weight 40 |
| ------------------ | ---------- | --- | ------------------------ | --------- | ------------------- | ----------- |
|                    |            |     | switch(config-schedule)# |           | dwrr queue          | 5 weight 50 |
|                    |            |     | switch(config-schedule)# |           | dwrr queue          | 6 weight 60 |
|                    |            |     | switch(config-schedule)# |           | dwrr queue          | 7 weight 70 |
| Portfiltersunderan | vsx-sync   |     |                          |           |                     |             |
|                    |            |     | switch(config)#          | interface | 1/1/1               |             |
| interface.         | portfilter |     |                          |           |                     |             |
|                    |            |     | switch(config-if)#       | vsx-sync  | portfilter          |             |
|                    |            |     | switch(config)#          | interface | lag 1               |             |
|                    |            |     | switch(config-lag-if)#   |           | vsx-sync portfilter |             |
Policiesunderan vsx-sync EnablingVSXsyncforpoliciesunderinterfaceVLAN5:
| interface. | policies |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- |
Enterontheprimaryswitch:
|     |     |     | switch(config)# | interface | vlan 5 |     |
| --- | --- | --- | --------------- | --------- | ------ | --- |
switch(config-if-vlan)#
vsx-sync policies
Enteronthesecondaryswitch:
|            |          |     | switch(config)# | interface | vlan 5 |     |
| ---------- | -------- | --- | --------------- | --------- | ------ | --- |
| Ratelimits | vsx-sync |     |                 |           |        |     |
EnablingVSXsynchronizationforratelimitswithinterface1/1/1:
| associatedwith | rate-limits |     |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | --- | --- |
interfaceorLAG.
|     |     |     | switch(config)#    | interface | 1/1/1       |     |
| --- | --- | --- | ------------------ | --------- | ----------- | --- |
|     |     |     | switch(config-if)# | vsx-sync  | rate-limits |     |
EnablingVSXsynchronizationforratelimitsunderinterfaceLAG3:
|                    |             |     | switch(config)#        | interface | lag 3                |     |
| ------------------ | ----------- | --- | ---------------------- | --------- | -------------------- | --- |
|                    |             |     | switch(config-lag-if)# |           | vsx-sync rate-limits |     |
| VLANsassociation   | vsx-sync    |     |                        |           |                      |     |
| underaninterface   | vlans       |     | switch(config)#        | interface | 1/1/1                |     |
| enabledforsyncing. |             |     | switch(config-if)#     | vsx-sync  | vlans                |     |
| VSXactive-         | vsx active- |     |                        |           |                      |     |
| forwardingforan    |             |     | switch# interface      | vlan      | 3                    |     |
forwarding
|     |     |     | switch(config-if-vlan)# |     | vsx active-forwarding |     |
| --- | --- | --- | ----------------------- | --- | --------------------- | --- |
interfaceVLAN.
switch(config-vsx)#
| Enabling | VSX synchronization |          | of STP | configurations |     |     |
| -------- | ------------------- | -------- | ------ | -------------- | --- | --- |
| between  | VSX peer            | switches |        |                |     |     |
EnablingVSXconfigurationsynchronization|44

Prerequisites

n The VSX switches support several STP modes, such as MSTP and RPVST. Confirm that these STP

configurations are identical on the VSX switches.

n You must be in the global configuration context: switch(config)#.

Procedure

1. Enter:

switch(config)# vsx
switch(config-vsx)# vsx-sync stp-global

2. Enter:

switch(config-vsx)# vsx-sync vsx-global

3. Enter:

switch(config-vsx)# vsx-sync mclag-interfaces

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

45

Chapter 6
|            |     |      |                 |        |     | Monitoring |     | the VSX | environment |     |
| ---------- | --- | ---- | --------------- | ------ | --- | ---------- | --- | ------- | ----------- | --- |
| Monitoring |     | the  | VSX environment |        |     |            |     |         |             |     |
| Ways       | to  | view | the             | status | of  | VSX        |     |         |             |     |
YouviewthestatusofVSXbymultipletechniques:
n Fromthe webUI: SeetheVSXpagetopicintheIntroductiontotheWebUIGuide.
| n   | Fromthe | REST                | API: SeetheRESTAPIGuide. |     |     |     |     |     |     |     |
| --- | ------- | ------------------- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     | Fromthe | CLI:SeeVSXcommands. |                          |     |     |     |     |     |     |     |
n
| Consistency |     |     | checking |     | between |     | VSX switches |     |     |     |
| ----------- | --- | --- | -------- | --- | ------- | --- | ------------ | --- | --- | --- |
Usethefollowingcommandstoverifythatallconfigurationsarein-syncbetweenVSXswitches.These
commandsarehelpfulintroubleshootingconfigurationmismatchesacrossVSXpeerswitches.
| Task |     |     |     |     |     |     |     | Command |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
DisplayingtheVSXglobalconfigurationconsistencybetweentwo showvsxconfig-consistency
VSXswitches.Usethiscommandtotroubleshootconfiguration
mismatchesacrossVSXpeerswitches.
DisplayingVSXLACPconfigurationconsistencybetweentwoVSX showvsxconfig-consistencylacp[<LAG-
| switches.Usethiscommandtotroubleshootconfiguration |     |     |     |     |     |     |     | NAME>] |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
mismatchesacrossVSXpeerswitches.
| Viewing |     | the | show | commands |     |     | for both | VSX switches |     | from |
| ------- | --- | --- | ---- | -------- | --- | --- | -------- | ------------ | --- | ---- |
one switch
YoucanviewtheoutputsoftheshowcommandfortheprimaryandsecondaryVSXswitchesfromone
switch.Whenyouenterashowcommandwiththevsx-peerparameter,thecommanddisplaystheoutput
fromthepeerdevice.
Forexample,thefollowingcommandwasenteredontheprimaryswitch.Thevsx-peerparameterindicates
tothesoftwaretodisplaytheoutputasifthecommandwasenteredonthesecondaryswitch.
|     | switch#         | show | vsx status | vsx-peer |     |     |     |     |     |     |
| --- | --------------- | ---- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
|     | VSX Operational |      | State      |          |     |     |     |     |     |     |
---------------------
|     | ISL          | channel      |          | :   | In-Sync        |          |     |     |     |     |
| --- | ------------ | ------------ | -------- | --- | -------------- | -------- | --- | --- | --- | --- |
|     | ISL          | mgmt channel |          | :   | operational    |          |     |     |     |     |
|     | Config       | Sync         | Status   | :   | in-sync        |          |     |     |     |     |
|     | NAE          |              |          | :   | peer_reachable |          |     |     |     |     |
|     | HTTPS        | Server       |          | :   | peer_reachable |          |     |     |     |     |
|     | Attribute    |              | Local    |     |                | Peer     |     |     |     |     |
|     | ------------ |              | -------- |     |                | -------- |     |     |     |     |
|     | ISL link     |              | lag1     |     |                | lag1     |     |     |     |     |
46
| AOS-CX10.07VirtualSwitchingExtension(VSX)Guide| |     |     |     |     | (6400,8xxxSwitchSeries) |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |

| ISL version      | 2                 | 2                 |
| ---------------- | ----------------- | ----------------- |
| System MAC       | e0:07:1b:cb:72:e4 | 98:f2:b3:68:79:2e |
| Platform         | 8320              | 8320              |
| Software Version | 10.0x.xxxx        | 10.0x.xxxx        |
| Device Role      | secondary         | primary           |
Theshowcommandsthatdisplaythefilesystemcontents,suchasshow loggingorshow core-dump,donot
supportthevsx-peerparameter.
IftheswitcheslacktheVSXconfigurationortheISLisdown,theoutputfromtheVSXpeerswitchisnot
displayed.
MonitoringtheVSXenvironment|47

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

o Depending on the network size, ARP/routing tables size, you might be required to set the timer to a

higher value (maximum 600 seconds).

When both VSX devices reboot, the link-up delay timer is not used.

To get upstream router adjacencies established during the link-up delay, the upstream LAG (for example LAG
101) has to be excluded from the scope of the link-up delay. Even if the upstream VSX node is not excluded
from the link-up delay timer, OSPFv2/OSPFv3 neighborship forms, when active-forwarding is enabled on a
VLAN. While the link-up delay timer is running, all SVIs that contain VSX LAG members are kept in a pseudo-
shutdown state.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

48

The link-up delay timer during an ISL failure

Configure the link-up delay timer and exclude LAGs so that if an ISL goes down, the downed ISL does not
impact the state of the VLAN, and its SVI that is not a part of a VSX LAG. This SVI is part of at least one
orphan port (besides the ISL LAG which is not a VSX LAG).

The following scenario explains what happens:

n During the ISL going down (before the initial synchronization): As long as the secondary VSX

node has a port that is a member of a VSX LAG, the associated SVI of the VLAN (transported by the VSX
LAG) turns to OFF/SHUT on the VSX secondary node. This situation occurs regardless of orphan ports
carrying the given VLAN.

n During the running of the link-up delay timer (after the initial synchronization):

As long as the secondary VSX node has a port that is a member of a VSX LAG, the associated SVI of the
VLAN (transported by the VSX LAG) turns to OFF/SHUT on the VSX secondary node. This situation occurs
regardless of orphan ports carrying the given VLAN.

The associated SVI of the VLAN transported by VSX LAG restores to ON/UP on the VSX secondary node,
only if the following two conditions are met:

Preventing traffic loss | 49

o TheVSXLAGisexcludedfromthelink-updelaytimerbythefollowingcommand:linkup-delay-timer
exclude lag-list
o ThegivenVLANisnotallowedonaVSXLAGthatisnotinthepartoftheexclusionset.
ThefollowingexampleshowshowanetworkwasconfiguredsoanSVIthatwasnotpartofaVSXLAG(SVI
16inthiscase)wasrestored.Thisexamplealsoshowsthelink-updelaytimerandtheexclusionofLAGs.
Thenetworkinthefollowingexamplewasconfiguredas:
n VLAN16isseton1/1/5(access).
n VLAN10taggedasVSXLAG11.*
LAG1isnotaVSXLAG.*
n
LAG2andLAG11areVSXLAGs.
n
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
| Linkup Delay       | time l             |              |        | : 0 minutes  | 58 seconds    |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 50

| Interfaces | that   | will       | be       | brought | up after   |                                  |
| ---------- | ------ | ---------- | -------- | ------- | ---------- | -------------------------------- |
| delay      | timer  | expires    |          |         |            | : lag11-lag12,lag14,lag16,lag112 |
| Interfaces | that   | are        | excluded |         | from delay |                                  |
| timer      |        |            |          |         |            | : lag2                           |
| switch#    | show   | int vlan10 |          |         |            |                                  |
| Interface  | vlan10 | is         | down     |         |            |                                  |
| Admin      | state  | is up      |          |         |            |                                  |
Description:
| Hardware:    | Ethernet, |                   | MAC | Address:          | 94:f1:28:1d:ad:00 |     |
| ------------ | --------- | ----------------- | --- | ----------------- | ----------------- | --- |
| IPv4 address |           | 10.10.10.3/26     |     |                   |                   |     |
| active       | gateway   | 10.10.10.1        |     | 00:00:00:00:11:01 |                   |     |
| active       | gateway   | 2002:0a0a:0a00::1 |     |                   | 00:00:00:00:66:01 |     |
| switch#      | sh int    | vlan15            |     |                   |                   |     |
| Interface    | vlan15    | is                | up  |                   |                   |     |
| Admin        | state     | is up             |     |                   |                   |     |
Description:
| Hardware:    | Ethernet, |                | MAC | Address: | 94:f1:28:1d:ad:00 |     |
| ------------ | --------- | -------------- | --- | -------- | ----------------- | --- |
| IPv4 address |           | 10.10.15.12/24 |     |          |                   |     |
| switch#      | sh int    | vlan16         |     |          |                   |     |
| Interface    | vlan16    | is             | up  |          |                   |     |
| Admin        | state     | is up          |     |          |                   |     |
Description:
| Hardware:    | Ethernet, |               | MAC   | Address: | 94:f1:28:1d:ad:00 |     |
| ------------ | --------- | ------------- | ----- | -------- | ----------------- | --- |
| IPv4 address |           | 10.10.16.2/24 |       |          |                   |     |
| switch#      | sh int    | vlan200       |       |          |                   |     |
| Interface    | vlan200   |               | is up |          |                   |     |
| Admin        | state     | is up         |       |          |                   |     |
Description:
| Hardware:    | Ethernet, |                | MAC | Address: | 94:f1:28:1d:ad:00 |     |
| ------------ | --------- | -------------- | --- | -------- | ----------------- | --- |
| IPv4 address |           | 10.10.212.6/29 |     |          |                   |     |
Asexpected,SVI10isinpseudo-shutduringthelink-updelay.SVI10wasapartofLAG2whichisin
exclusion.SVI16isup,asexpectedbecauseSVI16wasnotpartofaVSXLAG.
| Split brain |     | scenario |     |     |     |     |
| ----------- | --- | -------- | --- | --- | --- | --- |
AsplitbrainscenariooccurswhenbothkeepaliveandtheISLisdown,asshowninthefollowfigure.When
theISLisrestored,thereisnorebootofthesecondaryswitch.Ifsplitrecoveryisenabled(thedefault
setting),thesecondaryVSXLAGsarebroughtupafterthetimesetbythelinkup-delay-timercommand.
Preventingtrafficloss|51

Keepalive
Keepalive is a layer 3 interface that is used to exchange heartbeats between VSX peer switches. The
heartbeats are exchanged by using the User Datagram Protocol (UDP) and port 7678 (default). During an
ISL failure, VSX switches use their keepalive connection to determine if both VSX switches are up and
running. This configuration helps the VSX switches find alternative paths to the ISL link in the network so the
two VSX switch can continue to stay in-sync.

Configure each VSX peer switch with a keepalive connection to the other VSX peer switch. This connection is
established over a routed network (IPv4 currently) and is not required to be a dedicated peer-to-peer link
unlike ISL. Keepalive packets are UDP-based.

Make sure that the VSX peer switches have layer 3 reachability for keepalive interfaces through directly
connected interfaces or routed through the upstream layer 3 network. Source of keepalive interfaces can be
a layer 3 interface (router port), a loopback interface, or a Switch Virtual Interface (SVI). An SVI is a logical
layer 3 interface configured per VLAN (one-to-one mapping) that performs all layer 3 processing for packets
to or from all switch ports associated with that VLAN.

With respect to the keepalive path, it is highly recommended to separate keepalive traffic from the ISL link.

Use a dedicated layer 3 link and as a best practice, also use a dedicated VRF, as shown in Recommended network

configuration for keepalive.

Keepalive packets can be sourced from the supported layer 3 interface; however, the packet must not be

transported over the ISL.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

52

In the case of 6400 and 8400 switch series, it highly recommended to use keepalive and ISL on different line
cards. A single point of failure on line card that has keepalive and ISL configuration might cause split brain.

Keepalive response in ISL failure scenarios

n ISL link is down but the switches are still up and running: In this case, VSX switches use their

keepalive connection to determine that they are both up and running. Once that is determined, the user-
configured primary VSX switch keeps its multichassis (VSX) LAG links up and the secondary VSX switch
forces its VSX LAG links to go down with the appropriate reason. Once the ISL link is up, the MAC and ARP
tables of the primary switch are synchronized to the secondary switch. Then, the configured delay timer
starts. Once the delay timer expires, the secondary VSX switch brings up its VSX LAG links.

n ISL link and one of the VSX switches is down: The running switch sees that the ISL and keepalive

connection are both down. Independent of the user configured role (primary or secondary), the switch
that is up continues to keep its VSX LAG links up. Subsequently when the peer switch returns, the ISL link
comes up first. Then, the returned VSX peer switch synchronizes its MAC and ARP tables from the peer
switch that stayed up. After the synchronization completes, the delay time starts. Once the delay timer
expires, the VSX peer switch brings up its VSX LAG links.

Keepalive scenario

The following diagram illustrates a scenario in which both VSX switches are up, but the ISL link is down. The
switches cannot exchange information.

The keepalive functionality brings down the link between Switch B and Switch C in the following diagram.
The traffic is forced to go from Switch C to Switch A and then through the Layer 3 network to access Switch
B. The keepalive path is over the Layer 3 network. Traffic traveling from Switch B to Switch A is also forced
to go through the Layer 3 network.

Preventing traffic loss | 53

Figure 2 Keepalivetopology
DonothavethekeepalivepathgooverISL.Useadirect-linkconnectionforkeepalive.Ifthekeepalivepathuses
ISLasitsonlypathandanISLlinkfailureoccurs,theVSXswitcheswouldbeoutofsyncwithoutthekeepalive
functioning.
Keepalive configurations
| Task | Command |     | Example |     |     |
| ---- | ------- | --- | ------- | --- | --- |
Configuringkeepalivepeer keepalive peer <IP-ADDR> switch(config-vsx)# keepalive peer
sourceandVRF.
|     | source <IP-ADDR> | [<VRF- | 192.168.1.1 | source 192.168.1.5 | vrf |
| --- | ---------------- | ------ | ----------- | ------------------ | --- |
|     | NAME>]           |        | vrf1        |                    |     |
Unconfiguringkeepalive. no keepalive switch(config-vsx)# no keepalive
ConfiguringkeepaliveUDP keepalive udp-port switch(config-vsx)# keepalive udp-
| port. | <PORT-NUM> |     | port 2000 |     |     |
| ----- | ---------- | --- | --------- | --- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 54

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
Directlyconnectthekeepalivelink,asshowninthefollowingfigure.Avoidkeepalivecommunicationover
theISLcircuits.
Preventingtrafficloss|55

Figure 3 Recommended configuration for keepalive

Do not configure keepalive to go through the VSX LAG uplinks, as shown in the following image. This
scenario is not supported because:

n VSX LAG on the secondary will clear because split detection.

n Keepalive communication will stop between the VSX switches.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

56

| Figure 4      | Notsupportedconfigurationforkeepalive |            |            |
| ------------- | ------------------------------------- | ---------- | ---------- |
| Active        | gateway                               | and active | forwarding |
| Active-active | layer                                 | 2          |            |
VSXLAGsspantwoswitchesandoperateinactive-activemode.Trafficbetweentheaccesslayerand
aggregationlayerswitchescanbeforwardedtoanyoftheactivelinks.Therearenoloopsandnoneedfor
spanningtreeprotocolorblockedports.
Fromadatapathperspective,eachVSXswitchthatgetsapacketalwaysusesitslocallinksoftheLAGto
forwardtraffictothedestination.TheVSXswitchonlyusestheISLlinkifthelocalLAGlinksaredown.
Layer 2configuration
Preventingtrafficloss|57

Networkdiagramshowingactive-activelayer2configuration.Agg1andAgg2areshownalongwiththelocal
linksoftheLAGtoforwardtraffictothedestination.
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
VSXaggregationswitchescanbeconfiguredwithasharedvirtualIP(VIP)andasharedvirtualMACaddress
(VMAC)onthelayer3VLANinterface.
TheVIP/VMACservesasthedefaultgatewayfortheaccesslayer.Thetwoswitchesthensharetherouter
MACandfunctionasanactive-activegatewayfortheIPsubnet.ThefirstVSXdevicethatreceivestraffic
fromtheaccesslayer(basedonthehashingalgorithmovertheLAGinterface)routesitacrosstotheother
subnets.
| Active gateway | over | VSX |     |
| -------------- | ---- | --- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 58

Activegatewayisafirsthopredundancyprotocolthateliminatesasinglepointoffailure.Theactive
gatewayfeatureisusedtoincreasetheavailabilityofthedefaultgatewayservicinghostsonthesame
subnet.Anactivegatewayimprovesthereliabilityandperformanceofthehostnetworkbyenablinga
virtualroutertoactasthedefaultgatewayforthatnetwork.
Ifyouhaveenabledactivegateway,VRRPisnotrequired.ActivegatewayissimilartoVRRPinthatrouted
trafficfromtheVSXnodeissourcedfromtheswitchinterfaceMACandnotthevirtualMACaddress
(VMAC).EachactivegatewaysendsaperiodicbroadcasthellopackettoavoidVMACagingontheaccess
switches.TheswitchviewstheactivegatewayIPasaselfIPaddress.
ActivegatewayispreferableoverVRRPbecausewithVRRPtrafficisstillpushedovertheISLlink,resultingin
latencyinthenetwork.
| VMACsandactive gateway |     |     |
| ---------------------- | --- | --- |
TherecanbeonlyonevirtualMACaddress(VMAC)eachforIPv4andIP6,andtheVIPandVMACmustbe
thesameonbothVSXswitches.
Youcanhaveamaximumof16differentVMACsperVSXpair.YoucanconfigurethesameVMACforboth
IPv4andIPv6.Forexample:YoucanhaveamaximumofeightVMACsforIPv4,simultaneouslyhavinga
maximumofeightVMACsforIPv6.
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
n Beforeconfiguringactivegateway,confirmthatanIPaddressisontheSVIthatisinthesamesubnetas
theactivegatewayIPyouaretryingtoconfigure.IfanactivegatewayIPdoesnothaveanSVIIPwiththe
samesubnet,theCLIallowstheconfiguration,buttheactivegatewayIPwillnotbeprogrammedinthe
kernel,resultingtheactivegatewaytobeunreachable.
Preventingtrafficloss|59

AnactivegatewaycanbeconfiguredonlyoveranSVI.IfactivegatewayandSVIIPaddressesarethe
n
same,makesurethatSVIIPaddressesareconsistentacrossVSXswitches.IfyouhaveaVSXsquare
topologythatcontainstwopairsofVSXswitches,makesurethatyoudonothavethesameIPaddress
acrossallfourVSXnodesinthesquaretopology.
ActivegatewayconfigurationmustbethesameinboththeVSXpeerswitches.
n
n HavingsameVMACanddifferentactivegatewayIPaddressesondifferentVSXsegmentsinasquare
topologyisnotsupported.EnsurethatyouhaveeithersameVMACandsameactivegatewayIP
addressesordifferentVMACanddifferentactivegatewayIPaddressesconfiguredontwodifferentVSX
segments.For8320and8325switchseries,whenVMACandactivegatewayIPaddressesaresame,
makesurethattheSVIstatusisidenticalonboththeVSXsegments.
n Ifasystemhasactiveforwardingenabled,reduceoneVMACfromthetotalnumberofVMACssupported
inthesystem.Anactivegatewaycanhaveamaximumof14"unique"MACaddressespersystem,both
IPv4andIPv6addressesareincludedinthecount.
n Ifasystemhasactiveforwardingdisabled,anactivegatewaycanhaveamaximumof16"unique"MAC
addressespersystem,bothIPv4andIPv6addressesareincludedinthecount.
n WithIPmultinetting,amaximumof32IPv4activegatewayandamaximumof31IPv6activegateway
canbeconfigured.Arecommendedconfigurationisamultidimensionscale(MD)scaleandamaximum
networklimit,alongwithfourIPv4activegatewaysandfourIPv6activegatewaysperSVIswitha
maximumof512SVIsperchassis.AnMDscaleiswhentheVSXactive-gatewayalongwithother
supportedfeatures,suchaslayer2,layer3,andmulti-VRFareenabledandthesystemresponse/stability
isvalidatedagainstthem.
n LinklocalIPv6virtualIPaddressofanactivegatewayaddressismulticastedforrouteradvertisementso
thattheIPv6addresscanbechosenasadefaultgateway.
ActivegatewayconfigurationmustbethesameinboththeVSXpeerswitches.
n
n DisableIPICMPredirectwhenIPmultinettingisenabled.
n DisableICMPredirectwhenroutingisenabledthroughanactivegatewaySVIwhereegressportbelongs
tosameVLANasingress.
| Example |     | of IPv4andIPv6active |     |     | gatewayson | an SVI |
| ------- | --- | -------------------- | --- | --- | ---------- | ------ |
AssumethatyouhaveIPv4andIPv6activegatewaysonanSVI.EachSVIusesaMACaddressforIPv4and
oneforIPv6.TheconfigurationoftheVSXwithanactive-gatewayconsumesasecondMACaddressperSVI.
|     | switch#      | sh int     | vlan10            |               |                   |     |
| --- | ------------ | ---------- | ----------------- | ------------- | ----------------- | --- |
|     | Interface    | vlan10     | is up             |               |                   |     |
|     | Admin        | state      | is up             |               |                   |     |
|     | Description: |            | ACCESS switch     | mgmt          |                   |     |
|     | Hardware:    | Ethernet,  | MAC               | Address:      | 98:f2:b3:68:71:fe |     |
|     | IPv4         | address    | 10.1.1.253/24     |               |                   |     |
|     | Rx L3:       | 0 packets, | 0 bytes           |               |                   |     |
|     | Tx L3:       | 0 packets, | 0 bytes           |               |                   |     |
|     | switch#      | sh run     | int vlan141       |               |                   |     |
|     | interface    | vlan141    |                   |               |                   |     |
|     | description  |            | USER VLAN         | 10.141.0.0/16 |                   |     |
|     | ip           | address    | 10.141.255.253/16 |               |                   |     |
|     | ip           | ospf 1     | area 0.0.0.0      |               |                   |     |
|     | ip           | pim-sparse | enable            |               |                   |     |
|     | ip           | igmp       | enable            |               |                   |     |
|     | ip           | igmp       | version 2         |               |                   |     |
exit
|     | switch# | config |     |     |     |     |
| --- | ------- | ------ | --- | --- | --- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 60

| switch(config)# |     | int | vlan10 |     |     |     |     |
| --------------- | --- | --- | ------ | --- | --- | --- | --- |
switch(config-if-vlan)#
|                 |            |               |         | active-gateway |                   | ip 10.1.1.254     | mac 00:00:00:10:11:12 |
| --------------- | ---------- | ------------- | ------- | -------------- | ----------------- | ----------------- | --------------------- |
| switch#         | sh int     | vlan10        |         |                |                   |                   |                       |
| Interface       | vlan10     |               | is up   |                |                   |                   |                       |
| Admin state     |            | is up         |         |                |                   |                   |                       |
| Description:    |            | ACCESS        | switch  | mgmt           |                   |                   |                       |
| Hardware:       | Ethernet,  |               | MAC     | Address:       | 98:f2:b3:68:71:fe |                   |                       |
| IPv4 address    |            | 10.1.1.253/24 |         |                |                   |                   |                       |
| active          | gateway    | 10.1.1.254    |         |                |                   | 00:00:00:10:11:12 |                       |
| Rx L3:          | 0 packets, |               | 0 bytes |                |                   |                   |                       |
| Tx L3:          | 0 packets, |               | 0 bytes |                |                   |                   |                       |
| IP multinetting |            |               | over    | VSX            |                   |                   |                       |
IPmultinettingistheassignmentofmorethanoneIPinterfacetoasingleVLANthatisusedtoenablea
routertoprovidedefaultgatewayservicetodifferentaddressrangesassociatedwithasingleVLAN.
WhenusingIPmultinettinginanenvironmentwithVSXenabled,youmustconfiguremultipleactive
gatewayIPaddressesperSVIsothatyoucanreachmultiplenetworksonthesameVLAN.Makesurethat
youconfigureanIPaddressforeithertheprimaryorsecondaryVSXswitchontheSVIwiththesame
subnet.
Themaximumnumberofsupportedactivegatewaysperswitchis4,000.Sinceamaximumof31secondary
IPv4addressescanbeconfiguredonanSVI,32IPv4activegateways(alongwiththeprimaryIPv4address)
canbeconfiguredperSVIwithIPmultinettingsupport.ThissupportisalsothesameforIPv6addresses.
DisableIPICMPredirectwhenIPmultinettingisenabled.
MultipleactivegatewaysIPaddressescanbeprogrammedonthesameactivegatewaykernelinterface,as
showninthefollowingexample:
| interface      | vlan3       |     |                       |     |     |     |     |
| -------------- | ----------- | --- | --------------------- | --- | --- | --- | --- |
| ip address     | 10.0.0.1/24 |     |                       |     |     |     |     |
| ip address     | 20.0.0.1/24 |     | secondary             |     |     |     |     |
| active-gateway |             | ip  | mac 00:00:00:00:00:01 |     |     |     |     |
| active-gateway |             | ip  | 10.0.0.3              |     |     |     |     |
| active-gateway |             | ip  | 20.0.0.3              |     |     |     |     |
003000000000001@vlan3: <NO-CARRIER,BROADCAST,UP,M-DOWN> mtu 1500 qdisc noqueue
| state LOWERLAYERDOWN |                   |     | group         | default | qlen                  | 1000 |     |
| -------------------- | ----------------- | --- | ------------- | ------- | --------------------- | ---- | --- |
| link/ether           | 00:00:00:00:00:01 |     |               |         | brd ff:ff:ff:ff:ff:ff |      |     |
| inet 10.0.0.3/32     |                   |     | scope global  |         | 003000000000001       |      |     |
| valid_lft            | forever           |     | preferred_lft |         | forever               |      |     |
| inet 20.0.0.3/32     |                   |     | scope global  |         | 003000000000001       |      |     |
| valid_lft            | forever           |     | preferred_lft |         | forever               |      |     |
ActivegatewayVMACandVIPscanbeconfiguredseparately:
| interface      | vlan3       |     |                       |     |     |     |     |
| -------------- | ----------- | --- | --------------------- | --- | --- | --- | --- |
| ip address     | 10.0.0.1/24 |     |                       |     |     |     |     |
| ip address     | 20.0.0.1/24 |     | secondary             |     |     |     |     |
| active-gateway |             | ip  | mac 00:00:00:00:00:01 |     |     |     |     |
| active-gateway |             | ip  | 10.0.0.3              |     |     |     |     |
| active-gateway |             | ip  | 20.0.0.3              |     |     |     |     |
Preventingtrafficloss|61

| Active | gateway configurations |     |     |     |     |     |
| ------ | ---------------------- | --- | --- | --- | --- | --- |
Comma
| Task |     | Example |     |     |     |     |
| ---- | --- | ------- | --- | --- | --- | --- |
nd
active-
Configurin
|           |         | switch(config)# | vlan 2    |        |     |     |
| --------- | ------- | --------------- | --------- | ------ | --- | --- |
| gavirtual | gateway |                 |           |        |     |     |
|           |         | switch(config)# | interface | vlan 2 |     |     |
{ip |
| IPv4and |     | switch(config-if-vlan)# |     | ip address | 10.0.0.1/24 |     |
| ------- | --- | ----------------------- | --- | ---------- | ----------- | --- |
ipv6}
|     |     | switch(config-if-vlan)# |     | active-gateway | ip 10.0.0.2 | mac |
| --- | --- | ----------------------- | --- | -------------- | ----------- | --- |
IPv6
|         | [<IP-  | 00:00:00:00:00:01       |     |              |                 |     |
| ------- | ------ | ----------------------- | --- | ------------ | --------------- | --- |
| address | ADDRES |                         |     |              |                 |     |
|         |        | switch(config-if-vlan)# |     | ipv6 address | aa:bb::cc:dd/24 |     |
foran
S>] switch(config-if-vlan)# active-gateway ipv6 2001:DB8::/32
| interface | [mac | mac 00:00:00:01:00:01 |     |     |     |     |
| --------- | ---- | --------------------- | --- | --- | --- | --- |
<MAC-
VLAN.
ADDRES
S>]
| Unconfigur | no      |                         |     |                   |     |     |
| ---------- | ------- | ----------------------- | --- | ----------------- | --- | --- |
|            |         | switch(config-if-vlan)# |     | no active-gateway | ip  |     |
| ingactive  | active- |                         |     |                   |     |     |
| gateway    | gateway |                         |     |                   |     |     |
foractive-
{ip |
active
ipv6}
routing.
[<IP-
ADDRES
S>]
[mac
<MAC-
ADDRES
S>]
SeeIPmultinettingoverVSXforadditionalexamplesofIPmultinetting.
| VRRP with | VSX configuration |     |     |     |     |     |
| --------- | ----------------- | --- | --- | --- | --- | --- |
VRRPissimilartoactivegatewayinthatitisafirsthopredundancyprotocolthateliminatesasinglepointof
failure.OneVSXswitchactsasaVRRPmasterandtheotherswitchactsastheVRRPbackup.BothVSX
switchesroutethetraffic.Theactivegateway/VRRPconfigurationmustbeconsistentacrossthetwoVSX
switches.
AlthoughactivegatewayandVRRParenolongergloballyexclusiveinaVSXconfiguration,activegateway
andVRRParestillexclusiveonanSVI.AworkaroundistoconfigureVRRPononeSVI(SVIA),andconfigure
active-gatewayontheotherSVI(SVIB).
ActivegatewayispreferabletoVRRPbecauseVRRPtrafficisstillpushedovertheISLlink,resultinginlatency.
Sample VRRPconfiguration
IPV4:
| switch(config)# | vlan      | 1-10        |     |     |     |     |
| --------------- | --------- | ----------- | --- | --- | --- | --- |
| switch(config)# | router    | vrrp enable |     |     |     |     |
| switch(config)# | interface | vlan2       |     |     |     |     |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 62

| switch(config-if-vlan)# |     | ip address | 192.168.1.253/16 |     |
| ----------------------- | --- | ---------- | ---------------- | --- |
switch(config-if-vlan)#
no shutdown
| switch(config-if-vlan)# |     | vrrp 1 address-family |               | ipv4    |
| ----------------------- | --- | --------------------- | ------------- | ------- |
| switch(config-if-vrrp)# |     | address               | 192.168.1.253 | primary |
| switch(config-if-vrrp)# |     | no shutdown           |               |         |
| switch(config-if-vrrp)# |     | exit                  |               |         |
| switch(config-if-vlan)# |     | exit                  |               |         |
switch(config)#
IPV4andIPV6:
| switch(config)# | vlan 1-10 |     |     |     |
| --------------- | --------- | --- | --- | --- |
switch(config)#
|                         | router    | vrrp enable           |                |         |
| ----------------------- | --------- | --------------------- | -------------- | ------- |
| switch(config)#         | interface | vlan3                 |                |         |
| switch(config-if-vlan)# |           | ip address            | 172.3.0.1/16   |         |
| switch(config-if-vlan)# |           | ipv6 address          | 2002:3::1/64   |         |
| switch(config-if-vlan)# |           | ip ospf               | 1 area 0.0.0.0 |         |
| switch(config-if-vlan)# |           | ipv6 ospfv3           | 1 area         | 0.0.0.0 |
| switch(config-if-vlan)# |           | vrrp 1 address-family |                | ipv4    |
| switch(config-if-vrrp)# |           | address               | 172.3.0.10     | primary |
| switch(config-if-vrrp)# |           | no shutdown           |                |         |
| switch(config-if-vrrp)# |           | exit                  |                |         |
switch(config-if-vlan)#
|                         |     | vrrp 1 address-family |                 | ipv4 |
| ----------------------- | --- | --------------------- | --------------- | ---- |
| switch(config-if-vrrp)# |     | address               | fe80::3 primary |      |
| switch(config-if-vrrp)# |     | no shutdown           |                 |      |
| switch(config-if-vrrp)# |     | exit                  |                 |      |
switch(config)#
Active forwarding
Activeforwardingisanoptimizationforlayer3unicasttrafficflowingfromtheupstream(core)tothe
downstream(access)throughtheVSXpeers(aggregate).Activeforwardingpreventsthebridgedtrafficfrom
switchingovertheISL.ItalsominimizeslatencyandtheISLbandwidth.
Active forwardingrequirements
ActiveforwardingisenabledonaSVIfacingcorenetworkonaVSXenvironment.
n
ActiveforwardingissupportedonSVIonly.
n
Activeforwardingandactivegatewayaremutuallyexclusivefeatures.Youcannotenablebothactive
n
forwardingandactivegatewayonthesameSVI.
AlthoughtheCLIitselfdoesnotlimitthenumberofactiveforwardingSVIs;themaximumnumberof
n
configuredactiveforwardingSVIsis256.
ActiveforwardingissupportedonmorethanoneSVIperVRF.
n
ActiveforwardingcannotbeconfiguredwhenICMPredirectisenabled.
n
| Traffic flow scenario |     |     |     |     |
| --------------------- | --- | --- | --- | --- |
Activeforwardingmitigatesthesuboptimalpathscenariosbecauseofundeterministiclayer3hashingand
layer2hashing,asdescribedinthefollowingECMP(equal-costmulti-pathrouting)scenario.
Thisscenariodescribesasituationwhenactiveforwardingisnotused.InaVSXenvironment,acorenetwork
isconnectedtoaVSXpair,forminganOSPFadjacencyoveraVSXLAG.TheVSXLAGhasECMProutestothe
accessnetwork.ThecorehasECMProutestochoosebetweeneithertheVSXprimaryswitchortheVSX
secondaryswitchfortrafficflowingfromthecoretotheaccessnetwork.AssumethatECMPpickedtheVSX
primaryswitch.ThistrafficisnowsubjectedtothehashingalgorithmovertheVSXLAGinterface.Basedon
thechosenhashingalgorithm,thelayer2interfacemightroutethetraffictotheVSXsecondaryswitch.The
Preventingtrafficloss|63

secondaryVSXswitchthenbridgesthistrafficovertheISLtotheprimaryVSXswitch.TheprimaryVSX
switchinturnroutesthetraffictowardtheaccessnetwork,whichcausesextraoverheadwithISLbandwidth
andnetworklatency.
Ifactiveforwardingwasenabledinthepreviousscenario,thetrafficdestinedfortheaccessnetworkwould
notbebridgedovertheISL.Thetrafficwouldflowfromnorthtosouthinstead,resultinginlessnetwork
latency.Formoreinformationaboutthebenefitsofactiveforwarding,alongwithadiagram,seeBenefitsof
activeforwardingandactivegateway.
| Sample                   | Active forwardingconfiguration |            |                       |     |     |
| ------------------------ | ------------------------------ | ---------- | --------------------- | --- | --- |
| Primary#                 | configure                      | terminal   |                       |     |     |
| Primary(config)#         |                                | no ip icmp | redirect              |     |     |
| Primary(config)#         |                                | interface  | vlan 1000             |     |     |
| Primary(config-if-vlan)# |                                |            | vsx active-forwarding |     |     |
| Primary(config-if-vlan)# |                                |            | end                   |     |     |
Deploymentoptionsfor upstreamconnectivitywith active-active forwarding
Aggregatecorelinkscanbeconfiguredinoneofthefollowingways:
n Layer3-LAG/routedports:SimpleVLAN-freeconfigurationbestsuitedwhenthenetworkrunsona
singleVRFdomain.WithmultipleVRFsinthenetwork,onewouldneedmultipleroutedports,oneper
VRF.
n P2PSVIlinks:Eachaggregate-corelinkisonitsownVLAN.Thelayer2linkscancarrytrafficformultiple
SVIsandthereforemultipleVRFscanbecarriedoverthesamelink.
VSX multichassis LAGs:Theaggregate-corelinkscanbemultichassislayer2linkscarryingtrafficfor
n
multipleSVIsandVRFs.Thisconfigurationprovidesforlayer2LAGandlayer3ECMP-basedactive-active
forwardingfortrafficfromcoretoaccess.
Intheseconfigurations,thetwoVSXswitchesrunasindependentcontrolplanes(OSPF/BGP)andpresent
themselvesasdifferentroutersinthenetwork.Inthedatapathhowever,theyfunctionasasinglerouter
andsupportactive-activeforwarding.
| Benefits | of active | forwarding |     | and active | gateway |
| -------- | --------- | ---------- | --- | ---------- | ------- |
TheenablingofactiveforwardingandactivegatewayreduceslatencyinthenetworkbybypassingtheISL
linkfornorth-southandsouth-northtraffic,resultinginonelesshop.
Whenactiveforwardingisenabled,thenorth-southunicasttrafficbypassestheISLlinkforAgg1andAgg2.
Justasthesouth-northtrafficbypassestheISLlinkforAgg1andAgg2whenactivegatewayisenabled,as
showninthefollowingfigure.
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 64

| Figure 5 | ActiveForwardngandActiveGatewayexample |         |     |     |
| -------- | -------------------------------------- | ------- | --- | --- |
| Virtual  | active                                 | gateway |     |     |
AvirtualactivegatewayiscreatedbyconfiguringthesameIPv4addressinboththeinterface-VLANcontext
andtheactive-gatewaycontext.
VirtualactivegatewayenablestheusertoconfigurethesameIPv4addressasboththeinterfaceVLAN(SVIs)
addressaswellastheactivegatewayaddress.Avirtualactivegatewayisusefulwhentheprimarypurpose
oftheSVIistoprovidejustafirsthopgatewayservicetoitsclientsanddoesnotneedaseparatesetofIPv4
addressesoneachdeviceandavirtualIPv4addresstoservethegatewayfunctionality.
| Supported | services | on a virtual | active gateway | SVI |
| --------- | -------- | ------------ | -------------- | --- |
n DHCPRelay
n ARP
n VRF
ACLs
n
Dualstack(IPv6requiresactivegatewaytohavedifferentrealandvirtualIPaddresses).
n
n IPv6ActiveGW(withrealSVIIPv6)
n VSXActive-GWmultinetforIP
| Unsupported |     | services for a virtual | active gateway | SVI |
| ----------- | --- | ---------------------- | -------------- | --- |
Preventingtrafficloss|65

Layer3IPServices,suchasOSPF,BGP,IGMP,andBFD.
n
DHCPOption82
n
PINGfromtheVSXdevicetodownstreamclientswithSRCIPastheactivegatewayIP.
n
n IPv6virtualactivegateway
| Sample | virtual | active | gateway | configuration |
| ------ | ------- | ------ | ------- | ------------- |
Avirtualactivegatewayconfigurationiscreatedinthisexampleandshowninthefollowingfigure.
| switch(config)#         |     | vlan | 3          |             |
| ----------------------- | --- | ---- | ---------- | ----------- |
| switch(config-vlan-3)#  |     |      | interface  | vlan 3      |
| switch(config-if-vlan)# |     |      | ip address | 10.0.0.2/24 |
switch(config-if-vlan)# active-gateway ip 10.0.0.3 mac 00:00:00:00:aa:aa
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformationabout
theCLIcommands.
| Active-standby |     |     | DHCP | relay |
| -------------- | --- | --- | ---- | ----- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 66

When VSX synchronization is enabled for DHCP relay, only the primary VSX node relays DHCP requests
tothe upstream DHCP server. The secondary VSX node forwards over the ISL to the primary VSX switch
theDHCP requests received from the downstream endpoints. The secondary VSX switch takes over DHCP-
relayservice upon primary failure detection (ISL down and keepalive down). Upstream DHCP servers receive
asingle DHCP request. Downstream clients receive a single DHCP offer.

For more information, refer to vsx-sync dhcp-relay

DHCP relay failure if the SVI is down on the primary switch

Only the primary VSX node relays DHCP requests to the upstream DHCP server. Shutting down the
associated SVI on the primary VSX node prevents any DHCP requests to be relayed.

For more information, refer to vsx-sync dhcp-relay

Split recovery mode
Split recovery mode prevents traffic loss when the ISL goes out-of-sync and keepalive subsequently fails.
When the ISL goes out-of-sync and keepalive is established, the secondary VSX LAGs are brought down. If
keepalive then also fails, this situation causes a split condition. In this case, if split recovery mode is enabled,
the secondary switch restores its VSX LAGs so they are up. The secondary VSX node brings up the VSX LAGs
after 10 keepalive packets are missed, approximately 10 seconds after keepalive goes down.

The no split recovery command disables split recovery mode. When split recovery mode is disabled
during a split condition, the secondary switch keeps it VSX LAGs down.

VSX shutdown-on-split
VSX shutdown-on-split method prevents traffic loss by shutting down the non-VSX interfaces on the VSX
secondary when the ISL goes down or when the switch reboots. When the ISL goes down, all the secondary
VSX links are brought down but the non-VSX interfaces on the secondary switch will stay up. In this scenario,
if firewall, any active links, or single homed devices are connected to the secondary switch, then the traffic is
sent to secondary links since non-VSX interfaces are up. This situation causes a traffic drop at the secondary
device. To avoid the traffic disruption, you can shut down the non-VSX interfaces using the vsx shutdown-
on-split command when the ISL goes out-of-sync. This makes the link between the firewall and secondary
to go down. For more information, see vsx shutdown-on-split.

IGMP snooping
VSX switches can be configured for IGMP snooping on downstream VLANs facing the access switches. When
enabled, the IGMP group database is independently constructed on each VSX switch. Multicast traffic to
these groups is appropriately pruned/optimized.

Each VSX switch has an identical IGMP group database:

n Each VSX node individually learns any JOIN/LEAVE message received from a downstream VSX LAG. For
example: Agg-1 learns on downlink from SW1, whereas Agg-2 learns on the ISL as the ISL is always
included as a forwarding port for IGMP, as shown in the following figure.

n The VSX IGMP process translates the received IGMP from the ISL into an IGMP join message from the

VSX LAG.

Multicast traffic to these IGMP groups is pruned/forwarded based on the individual IGMP group database
on each VSX node. ISLP does not synchronize IGMP groups between VSX peers. The IGMP database
construction is a data-plane based process.

Preventing traffic loss | 67

If a VSX node reboots, it must relearn all the IGMP groups. The VSX switch floods multicast traffic within the
VLANs that have active physical ports being forwarded. It then sends an All Hosts Query message. When the
VSX node receives all join messages, it relearns and recreates the IGMP groups database.

DHCP relay backup
When the two VSX switches are configured for DHCP relay on their VLAN interfaces, only the primary switch
actively relays DHCP client requests to the upstream server. The secondary switch acts as a backup. If the
primary VSX switch goes down, the secondary switch takes over, such in the case with ISL and keepalive
both down. Even though both primary and secondary switches receive the DHCP request, the primary
switch takes precedence.

The secondary VSX node forwards over the ISL to the primary VSX switch the DHCP requests received from
the downstream endpoints. The upstream DHCP servers receive a single DHCP request. The downstream
clients receive a single DHCP offer.

Both devices do not end up relaying DHCP requests to the server as duplicates. That scenario is usually the
case with typical aggregation switches running VRRP-based redundancy.

If SVI is disabled on the primary VSX node and the primary goes down, the secondary switch will not take over and

no DHCP requests will be relayed.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

68

IP multicast routing
Multicast PIM routing provides fast failover. For each VSX downstream VLAN, both VSX switches as a PIM
Designate Router (DR). One node is the actual DR, the other node is the proxy DR.

From the PIM protocol view point (join, prune, register. The role of the proxy DR is equal to the role of the
actual DR. The proxy DR also sends PIM join messages to the upstream PIM router. Any VSX node receives a
copy of IGMP join on the SL. Both the DR and proxy DR maintain the same multicast tables and build the
shortest path tree.

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

Preventing traffic loss | 69

Recommended values for system MAC and active gateway
VMAC
It is highly recommended to use unicast MAC Address when assigning system-mac or active-gateway virtual
MAC address. There are four ranges reserved for private use of unicast. The values are:

n x2-xx-xx-xx-xx-xx

n x6-xx-xx-xx-xx-xx

n xA-xx-xx-xx-xx-xx

n xE-xx-xx-xx-xx-xx

x can be any hexadecimal value.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

70

| Function    | System-mac        | Active gateway    | VirtualMAC |
| ----------- | ----------------- | ----------------- | ---------- |
| Access      | 02:00:00:00:XX:00 | 12:00:00:00:XX:0Y |            |
| Aggregation | 02:01:00:00:XX:00 | 12:01:00:00:XX:0Y |            |
| Core        | 02:02:00:00:XX:00 | 12:02:00:00:XX:0Y |            |
Intheabovetable,XXrepresentstheuniqueclusterIDinthefunctionandYrepresentsthevirtualMACID
(0toF).
DonotusemulticastandbroadcastMACaddressassystem-macaddress.
Preventingtrafficloss|71

Chapter 8

STP over VSX

STP over VSX

Without a spanning tree, having more than one active path between a pair of nodes causes loops in the
network, which can result in duplication of messages, leading to a “broadcast storm” that can bring down the
network. STP ensures that only one active path exists between any two nodes in a spanning tree instance. A
spanning tree instance comprises a unique set of VLANs, and belongs to a specific spanning tree region. A
region can comprise multiple spanning tree instances (each with a different set of VLANs), and allows one
active path among regions in a network.

Spanning-tree guards and filters are not allowed for configuration on the ISL.

Supported STP modes
The VSX switches support the following spanning tree protocols (STPs) with VSX:

n MSTP: Multiple Spanning Tree Protocol.

n RPVST: Rapid per-VLAN Spanning Tree Protocol.

How STP works with VSX
Both VSX switches appear as a single common Spanning Tree Bridge ID to STP partner devices upstream and
downstream that participate to the same Spanning Tree domain. STP can be enabled on VSX switches and
any nonrouting ports. Both VSX LAGs and non-VSX LAGs can participate in STP topology to avoid any loops.

STP on VSX uses the same bridge ID with the same MAC address on VSX LAGs and non-VSX LAGs, orphan
ports. This MAC address is referred to as a common Bridge ID which consists of Spanning Tree priority and
the switch MAC Address. The STP port state is the same for VSX LAG ports in VSX peer switches.

The Spanning Tree protocol runs independently on VSX nodes, which conforms to the dual-control plane
VSX architecture. The primary VSX node is responsible to run the protocol for the VSX LAGs. In the normal
state, the primary is "operational primary" and the secondary is "operational secondary". If a primary VSX
node failure occurs, the secondary VSX node becomes the STP operational primary. When the primary VSX
node goes back up, it takes back ownership of the STP operational primary role.

On VSX LAG ports, STP runs only from the operational primary, shown in the following figure. The
operational secondary, also shown in the following figure, holds precomputed STP information for ready-
state switch over thanks to STP states synchronization. The operational primary does STP state
synchronization to the operational secondary for links member of the VSX LAG. That happens as a part of
the initial sync (LACP, MAC, ARP, MSTP). During the switch-over, the new operational primary sends the
BPDU downstream or upstream within 6 seconds (the default) of the spanning tree BPDU failure detection
timer: 3x hello-timer (2s per default).

ISL is always part of STP, nonblocking and it sends and receives BPDUs.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

72

n Do not use the same system STP address for the other nodes. For the internal Spanning Tree protocol

between VSX nodes, the Bridge_ID of the primary and secondary VSX nodes are derived from (-1, +1) from
the system-mac <MAC-ADDR> command. For example, if the system MAC address is 00:00:00:00:00:10, then
the other system MAC addresses cannot be 00:00:00:00:00:09, 00:00:00:00:00:10, and 00:00:00:00:00:11.

n You must have identical STP configurations on the primary and secondary VSX switches.

n It is recommended to have common system MAC addresses configured under the VSX context for stable STP

convergence and stability.

Figure 6 Sample MST on VSX configuration

This figure shows MSTP with a VSX configuration showing BID1 ports as blocking.

For more information, see system-mac.

MSTP

MSTP configurations

STP over VSX | 73

| VSX atthe | distribution |     | layer | with MSTPenabled |     |     |
| --------- | ------------ | --- | ----- | ---------------- | --- | --- |
Inthefollowingfigure,theVSXpairisconfiguredasarootswitch.AlltheportsoftheVSXLAGs,non-VSX
LAGs,andorphanportsareinaforwardingstate.BridgeProtocolDataUnits(BPDUs),generatedbyaVSX
pair,arethesameonallports,includingVSXLAG,non-VSXLAG,andorphan.Allswitchesmustbeinthe
sameMSTPregionconsistingofthesameconfigurationnameandrevisionnumber,assetbythespanning-
<CONFIG-NAME>andspanning-tree <REVISION-NUMBER>commands.
| tree config-name |     |     |     |     |     | config-revision |
| ---------------- | --- | --- | --- | --- | --- | --------------- |
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
Table 1: Definitionsoftheabbreviationsusedinthefiguresprovidedinthistopic
| Abbreviation |     |     | Definition                                        |     |     |     |
| ------------ | --- | --- | ------------------------------------------------- | --- | --- | --- |
| AB           |     |     | Alternateblocking;theportisinablockedstate.       |     |     |     |
| DF           |     |     | Designatedforwarding;theportisinaforwardingstate. |     |     |     |
| RF           |     |     | Rootforwarding;theportisinaforwardingstate.       |     |     |     |
SeeSampleconfigurationsforMSTPonVSXfortheconfigurationforthetopologiesdisplayedinthefigures
inthistopic.
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 74

Figure 7 MSTP VSX pair as a root switch

In the following figure, the VSX pair is not a root switch for STP topology. One of the VSX LAG ports is in the
blocking state for resolving an L2 network loop. The VSX LAG port is in a blocking state on both VSX peer
switches.

STP over VSX | 75

Figure 8 MSTP VSX pair as a nonroot switch

Distribution VSX pair connected to the core switch (SVI solution)

In the following figure, the VSX switch could be either a root switch or a nonroot switch for STP topology.
One of the uplinks connected from the distribution layer to the core switch is in a blocking state because the
MSTP is enabled in a VSX pair connected to a core switch, but the SVP configured without MSTP is enabled.

This configuration might also cause the flooding of the MSTP BPDUs (VLAN unaware) based on the VLAN
configuration. VLANs must be configured differently on both ports to avoid flooding back to another VSX
pair. Configure the BPDU filter on L2 ports connected to the core switch so that these ports will be in a
forwarding state.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

76

| Figure 9 DistributionlayerwithVSXandMSTPconnectedtothecoreswitch |     |     |
| ---------------------------------------------------------------- | --- | --- |
Formoreinformation,seeBFDreportsaLAGasdownevenwhenhealthylinksarestillavailable
| Sample configurationsfor |     | MSTPon VSX |
| ------------------------ | --- | ---------- |
ForscaledMSTPonVSXconfigurations,configureallMSTPglobalandportconfigurationsandthenenableMSTP.
ThefollowingconfigurationsareshowninMSTPVSXpairasarootswitchandinMSTPVSXpairasanonroot
switch
| Configurations | on the | VSX primary switch |
| -------------- | ------ | ------------------ |
Thefollowingexampleisanextractfromaconfiguration:
vlan 1-512
spanning-tree
| spanning-tree  | priority        | 2                                   |
| -------------- | --------------- | ----------------------------------- |
| spanning-tree  | config-name     | Region-One                          |
| spanning-tree  | config-revision | 1                                   |
| spanning-tree  | instance        | 1 vlan 1,65,129,193,257,321,385,449 |
| spanning-tree  | instance        | 2 vlan 2,66,130,194,258,322,386,450 |
| spanning-tree  | instance        | 3 vlan 3,67,131,195,259,323,387,451 |
| interface mgmt |                 |                                     |
no shutdown
ip dhcp
| interface lag | 10 multi-chassis |     |
| ------------- | ---------------- | --- |
no shutdown
no routing
| vlan trunk       | native 1         |     |
| ---------------- | ---------------- | --- |
| vlan trunk       | allowed all      |     |
| lacp mode active |                  |     |
| interface lag    | 20 multi-chassis |     |
no shutdown
no routing
STPoverVSX|77

| vlan trunk    | native 1      |     |     |
| ------------- | ------------- | --- | --- |
| vlan trunk    | allowed all   |     |     |
| lacp mode     | active        |     |     |
| spanning-tree | port-priority |     | 1   |
| interface     | 1/1/1         |     |     |
no shutdown
lag 10
| interface | 1/1/2 |     |     |
| --------- | ----- | --- | --- |
no shutdown
lag 20
| interface | 1/1/47 |     |     |
| --------- | ------ | --- | --- |
no shutdown
no routing
| vlan trunk | native 1    | tag |     |
| ---------- | ----------- | --- | --- |
| vlan trunk | allowed all |     |     |
| interface  | 1/1/48      |     |     |
no shutdown
| ip address | 1.1.1.1/24 |     |     |
| ---------- | ---------- | --- | --- |
vsx
| inter-switch-link | 1/1/47            |     |     |
| ----------------- | ----------------- | --- | --- |
| system-mac        | 02:02:02:02:02:02 |     |     |
role primary
| keepalive          | peer 1.1.1.2 | source        | 1.1.1.1 |
| ------------------ | ------------ | ------------- | ------- |
| linkup-delay-timer | 30           |               |         |
| Configurations     | on the       | VSX secondary | switch  |
Thefollowingexampleisanextractfromaconfiguration:
vlan 1-512
spanning-tree
| spanning-tree | priority        | 2          |                              |
| ------------- | --------------- | ---------- | ---------------------------- |
| spanning-tree | config-name     | Region-One |                              |
| spanning-tree | config-revision |            | 1                            |
| spanning-tree | instance        | 1 vlan     | 1,65,129,193,257,321,385,449 |
| spanning-tree | instance        | 2 vlan     | 2,66,130,194,258,322,386,450 |
| spanning-tree | instance        | 3 vlan     | 3,67,131,195,259,323,387,451 |
| interface     | mgmt            |            |                              |
no shutdown
ip dhcp
| interface | lag 10 multi-chassis |     |     |
| --------- | -------------------- | --- | --- |
no shutdown
no routing
| vlan trunk | native 1             |     |     |
| ---------- | -------------------- | --- | --- |
| vlan trunk | allowed all          |     |     |
| lacp mode  | active               |     |     |
| interface  | lag 20 multi-chassis |     |     |
no shutdown
no routing
| vlan trunk    | native 1      |     |     |
| ------------- | ------------- | --- | --- |
| vlan trunk    | allowed all   |     |     |
| lacp mode     | active        |     |     |
| spanning-tree | port-priority |     | 1   |
| interface     | 1/1/3         |     |     |
no shutdown
no routing
| vlan trunk | native 1    | tag |     |
| ---------- | ----------- | --- | --- |
| vlan trunk | allowed all |     |     |
| interface  | 1/1/4       |     |     |
no shutdown
lag 10
| interface | 1/1/45 |     |     |
| --------- | ------ | --- | --- |
no shutdown
lag 20
| interface | 1/1/46 |     |     |
| --------- | ------ | --- | --- |
no shutdown
| ip address | 1.1.1.2/24 |     |     |
| ---------- | ---------- | --- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 78

| interface | 1/1/47 |     |
| --------- | ------ | --- |
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
STPoverVSX|79

interface 1/1/41
no shutdown
no routing
vlan trunk allowed all

VSX and MSTP loop-protect configurations (physical and logical views)

The figures in this topic show the physical and logical views for VSX and MSTP loop-protect configurations
with MSTP as the default instance.

Figure 10 Physical view of the VSX and MSTP loop-protect configurations

The configuration from the previous figure is shown in its logical view, so that you can see how the network
views the configuration. For example, the following figure shows that the VSX distributed pair as one switch.
The ports on Agg-2 are blocking traffic. The logical view in the next figure shows that the traffic is distributed
so that the traffic continues to flow.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

80

Figure 11 Logical view of the VSX and MSTP loop-protect configurations

STP interoperability with Loop-Protect in VSX

When both loop protect and STP are enabled on the switch:

n If switch first detects STP, STP blocks the port to stop the loop and loop protect feature will not come

into effect.

n If switch first detects loop protect, loop protect blocks the port to stop the loop and STP will not take any

effect as there are no loops.

n If loop protect has re-enable timer enabled, the port will be unblocked once the timer is expired. In this

case, whichever protocol detects the loop first will block the port.

Show commands for MSTP

Before running the show commands, make sure that you have enabled STP synchronization between VSX peer

switches. See Enabling VSX synchronization of STP configurations between VSX peer switches.

STP over VSX | 81

Task

Action

Verify that all switches are in the same MSTP region
with the instance mapping to VLAN.

Enter the show spanning-tree mst-config
command.

View the latest topology changes of the VSX peer.

1. Synchronize the time by entering the NTP (vsx-

sync time) command.

2. Enter the show spanning-tree mst <0-64>

vsx-peer command.

Verify that the following global parameters are the

1. Enter the show running-config spanning-

same on VSX switches:

tree command.

n STP mode
n STP region configuration for MSTP (config-name

2. Enter the show running-config spanning-

tree vsx-peer command.

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
switch(config)# spanning-tree vlan 1-100

Sample RPVST configuration with VSX

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

82

The following figure shows a sample RPVST configuration.

The configuration for this figure is provided in the following sections.

VSX Primary Configuration

configure
hostname vsx-pri
vlan 1,10,20
spanning-tree mode rpvst
spanning-tree
spanning-tree vlan 1,10,20
interface mgmt

no shutdown
ip dhcp

interface lag 1 multi-chassis

no shutdown
no routing
vlan trunk native 1
vlan trunk allowed all
lacp mode active

interface lag 100

no shutdown
no routing
vlan trunk native 1
vlan trunk allowed all
lacp mode active

STP over VSX | 83

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
| keepalive | peer 1.1.1.2 | source 1.1.1.1 |
| --------- | ------------ | -------------- |
VSX secondaryconfiguration
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
| keepalive    | peer 1.1.1.1  | source 1.1.1.2 |
| ------------ | ------------- | -------------- |
| Accessswitch | configuration |                |
configure
hostname l2-access
vlan 1,10,20
| spanning-tree | mode rpvst |     |
| ------------- | ---------- | --- |
spanning-tree
| spanning-tree | vlan 1,10,20 |     |
| ------------- | ------------ | --- |
interface mgmt
no shutdown
ip dhcp
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 84

| interface lag 1 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
no routing
| vlan trunk       | native 1    |     |     |
| ---------------- | ----------- | --- | --- |
| vlan trunk       | allowed all |     |     |
| lacp mode active |             |     |     |
interface 1/1/10
no shutdown
lag 1
interface 1/1/11
no shutdown
lag 1
| VSX switch with | RPVST,asrootandnonroot |     |     |
| --------------- | ---------------------- | --- | --- |
Inthefollowingfigure,theVSXpairisconfiguredasarootswitch.AlltheportsoftheVSXLAGs,non-VSX
LAGs,andorphanportsareinaforwardingstate.BridgeProtocolDataUnits(BPDUs),generatedbyaVSX
pair,arethesameonallports,includingVSXLAG,non-VSXLAG,andorphan.
Table1:Definitions of theabbreviations used in thefigures provided in this topic
| Abbreviation |     | Definition                                        |     |
| ------------ | --- | ------------------------------------------------- | --- |
| AB           |     | Alternateblocking;theportisinablockedstate.       |     |
| DF           |     | Designatedforwarding;theportisinaforwardingstate. |     |
| RF           |     | Rootforwarding;theportisinaforwardingstate.       |     |
TomaketheVSXswitchrootforoneormoreRPVSTinstances,settheswitchtothelowestbridgeidentifier
forthetree:
n Forone RPVST instance: switch(config)# spanning-tree vlan 1 priority 1
n Formore than one RPVST instance:switch(config)# spanning-tree vlan 1-100 priority 1or
| switch(config)# | spanning-tree | vlan 10,20,30 | priority 1 |
| --------------- | ------------- | ------------- | ---------- |
Thepriorityparameterhasarangeof0to15forsettingthepriorityoftheRPVST.Thepriorityvalueis
configuredasamultipleof4,096(Default:8).Forexample,whenpriorityparameterissetas1,the
priorityvalueis4,096.Whenthepriorityparameterissetto2,thepriorityvalueis8,192.Bydefaultthe
priorityparameteris8,sothedefaultpriorityvalueis32,768.
STPoverVSX|85

Figure 12 RPVST VSX pair as a root switch

In the following figure, the VSX pair is not a root switch for STP topology. One of the VSX LAG ports is in the
blocking state for resolving an L2 network loop. The VSX LAG port is in a blocking state on both VSX peer
switches.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

86

| Figure 13 RPVSTVSXpairasanonrootswitch |            |           |             |                |
| -------------------------------------- | ---------- | --------- | ----------- | -------------- |
| Configuringa                           | VSX switch | asrootfor | one or more | RPVSTinstances |
Procedure
1. ForasingleRPVSTinstance,enterforexample:
| switch(config)# |     | spanning-tree | vlan 1 priority | 1   |
| --------------- | --- | ------------- | --------------- | --- |
2. FormultipleRPVSTinstances,enterarangeforexample:
| switch(config)# |     | spanning-tree | vlan 1-100    | priority 1 |
| --------------- | --- | ------------- | ------------- | ---------- |
| switch(config)# |     | spanning-tree | vlan 10,20,30 | priority 1 |
More information
VSXswitchwithRPVST,asrootandnonroot
| Show commands |     | for RPVST |     |     |
| ------------- | --- | --------- | --- | --- |
Beforerunningtheshowcommands,makesurethatyouhaveenabledSTPsynchronizationbetweenVSXpeer
switches.SeeEnablingVSXsynchronizationofSTPconfigurationsbetweenVSXpeerswitches.
STPoverVSX|87

Task

Action

View information on the RPVST
instance of the specified VLAN.

switch# show spanning-tree vlan <VLAN-ID>

View information on the RPVST
instance of the specified VLAN
and displays details on the RPVST
instance for the VLAN.

View information on the RPVST
instance of the specified VLAN on
the peer VSX switch.

View information on the RPVST
instance of the specified VLAN
and displays details on the RPVST
instance for the VLAN on the
peer VSX switch.

switch# show spanning-tree vlan <VLAN-ID> detail

The output of this command shows the value of the Multi-Chassis role.
When a switch has the Multi-Chassis role set to active, the switch
performs the STP operation. When a switch has the Multi-Chassis role set
to standby, the switch relays the information to the switch with the active
role for STP tasks.
For an example of the output from this command, see How the Multi-Chassis
role works.

switch# spanning-tree vlan <VLAN-ID> vsx-peer

switch# show spanning-tree vlan <VLAN-ID> detail vsx-
peer

Verify that the following global
parameters are the same on VSX
switches:

1. Enter the show running-config spanning-tree command.

2. Enter the show running-config spanning-tree vsx-peer

command.

n STP mode

n RPVST instance creation

n RPVST instance priority

configuration

View a summary of the port roles
or root information.

switch# show spanning-tree summary {port | root}

How the Multi-Chassis role works

The switch performs the STP operation on the switch that has the Multi-Chassis role set to active. The
switch with the role set to standby relays the information to the switch with the active role for STP tasks.

The primary VSX switch has the Multi-Chassis role set to active by default, just as the secondary VSX switch
has the Multi-Chassis role set to standby by default. The Multi-Chassis role on the secondary VSX switch
changes from standby to active if the primary VSX switch goes down.

The show spanning-tree vlan <VLAN-ID> detail command provides information about the value of the
Multi-Chassis role. In the following example, the primary switch has the Multi-Chassis role set to active,
and the secondary switch has the Multi-Chassis role set to standby.

Example of the Multi-Chassis role with the active value:

VSX-Primary# show spanning-tree vlan 2 detail

VLAN2

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

88

| Spanning | tree | status       | : Enabled |                   | Protocol: | RPVST      |             |          |      |
| -------- | ---- | ------------ | --------- | ----------------- | --------- | ---------- | ----------- | -------- | ---- |
| Root     | ID   | Priority     |           | : 32768           |           |            |             |          |      |
|          |      | MAC-Address: |           | 38:21:c7:66:24:00 |           |            |             |          |      |
|          |      | This bridge  |           | is the            | root      |            |             |          |      |
|          |      | Hello        | time(in   | seconds):2        |           | Max Age(in | seconds):20 |          |      |
|          |      | Forward      | Delay(in  | seconds):15       |           |            |             |          |      |
| Bridge   | ID   | Priority     | :         | 32768             |           |            |             |          |      |
|          |      | MAC-Address: |           | 38:21:c7:66:24:00 |           |            |             |          |      |
|          |      | Hello        | time(in   | seconds):2        |           | Max Age(in | seconds):20 |          |      |
|          |      | Forward      | Delay(in  | seconds):15       |           |            |             |          |      |
| Port     |      | Role         |           | State             |           | Cost       |             | Priority | Type |
------------ -------------- ------------ ------------ ---------- ----------
| 1/3/1         |             | Designated |          | Forwarding |            | 1     |     | 128 | point_to_point |
| ------------- | ----------- | ---------- | -------- | ---------- | ---------- | ----- | --- | --- | -------------- |
| lag2          |             | Designated |          | Forwarding |            | 20000 |     | 64  | point_to_point |
| Topology      | change      | flag       |          | :          | True       |       |     |     |                |
| Number        | of topology |            | changes  | :          | 3          |       |     |     |                |
| Last topology |             | change     | occurred | :          | 47 seconds | ago   |     |     |                |
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
| Designated     | port           |          |               |            |      | : 770     |     |     |     |
| -------------- | -------------- | -------- | ------------- | ---------- | ---- | --------- | --- | --- | --- |
| Multi-Chassis  |                | role     |               |            |      | :active   |     |     |     |
| Number         | of transitions |          | to            | forwarding |      | state : 1 |     |     |     |
| Bpdus sent     | 28,            | received |               | 3          |      |           |     |     |     |
| TCN_Tx:        | 2, TCN_Rx:     |          | 2             |            |      |           |     |     |     |
| VSX-Secondary# |                | show     | spanning-tree |            | vlan | 2 detail  |     |     |     |
VLAN2
| Spanning | tree | status       | : Enabled |                   | Protocol: | RPVST      |             |          |      |
| -------- | ---- | ------------ | --------- | ----------------- | --------- | ---------- | ----------- | -------- | ---- |
| Root     | ID   | Priority     |           | : 32768           |           |            |             |          |      |
|          |      | MAC-Address: |           | 38:21:c7:66:24:00 |           |            |             |          |      |
|          |      | This bridge  |           | is the            | root      |            |             |          |      |
|          |      | Hello        | time(in   | seconds):2        |           | Max Age(in | seconds):20 |          |      |
|          |      | Forward      | Delay(in  | seconds):15       |           |            |             |          |      |
| Bridge   | ID   | Priority     | :         | 32768             |           |            |             |          |      |
|          |      | MAC-Address: |           | 38:21:c7:66:24:00 |           |            |             |          |      |
|          |      | Hello        | time(in   | seconds):2        |           | Max Age(in | seconds):20 |          |      |
|          |      | Forward      | Delay(in  | seconds):15       |           |            |             |          |      |
| Port     |      | Role         |           | State             |           | Cost       |             | Priority | Type |
------------ -------------- ------------ ------------ ---------- ----------
| 1/3/1         |             | Designated |          | Forwarding |            | 1     |     | 128 | point_to_point |
| ------------- | ----------- | ---------- | -------- | ---------- | ---------- | ----- | --- | --- | -------------- |
| lag2          |             | Designated |          | Forwarding |            | 20000 |     | 64  | point_to_point |
| Topology      | change      | flag       |          | :          | False      |       |     |     |                |
| Number        | of topology |            | changes  | :          | 2          |       |     |     |                |
| Last topology |             | change     | occurred | :          | 35 seconds | ago   |     |     |                |
STPoverVSX|89

Port 1/3/1
Designated root has priority :32768 Address: 38:21:c7:66:24:00
Designated bridge has priority :32768 Address: 38:21:c7:66:24:00
| Designated | port           |               | : 129     |
| ---------- | -------------- | ------------- | --------- |
| Number     | of transitions | to forwarding | state : 2 |
| Bpdus sent | 24, received   | 22            |           |
| TCN_Tx:    | 1, TCN_Rx:     | 2             |           |
Port lag2
Designated root has priority :-32768 Address: 38:21:c7:66:24:00
Designated bridge has priority :-32768 Address: 38:21:c7:66:24:00
| Designated    | port           |               | :770      |
| ------------- | -------------- | ------------- | --------- |
| Multi-Chassis | role           |               | :standby  |
| Number        | of transitions | to forwarding | state : 3 |
| Bpdus sent    | 0, received    | 0             |           |
| TCN_Tx:       | 0, TCN_Rx:     | 0             |           |
| RPVST with    | VSX guidelines |               |           |
n PathcostisnotallowedtobeconfiguredontheISLport.
Donotconfigureport-specificspanningtreeconfigurationsontheISL.
n
DonothaveredundantlinkstotheISL.
n
TopologychangesforVSXLAGsareaccountedontheactivemultichassisLAGroleonly.
n
n RPVSTissupportedinbothVSXandnon-VSXenvironments.
n ThecommonbridgeIDcontinuestobeusedevenaftertheVSXsplitbrainscenarioisidentified.
n STPconfigurationsonVSXLAGportsmustbethesameonVSXswitches.
n TofindthemaximumsupportedRPVSTinstancesthatcanbeconfigured,enterthefollowingcommand:
| show capacities | rpvst |     |     |
| --------------- | ----- | --- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 90

Chapter 9
|              |                |     |     |      | Loop protect |     | configurations |     | over VSX |
| ------------ | -------------- | --- | --- | ---- | ------------ | --- | -------------- | --- | -------- |
| Loop protect | configurations |     |     | over | VSX          |     |                |     |          |
LoopprotectcanbeenabledonVSX.Loopprotectisaswitchfeature,whichisusedtoidentifyandprevent
layer2loopsinanetwork.Theloopprotectfeatureblockstheportbasedontheconfiguredaction,these
actionsmaybe:
n Tx-Disable
n Tx-Rx-Disable
n Do-Not-Disable
SeetheLayer2BridgingGuideforinformationaboutloopprotect.TosetuploopprotectwithVSX,loop
protectmustbeenabledontheinterfacesontheprimaryandsecondaryVSXswitches.
| How loop | protect |     | works |     | over VSX |     |     |     |     |
| -------- | ------- | --- | ----- | --- | -------- | --- | --- | --- | --- |
Assumethatyouhavetheloopprotectfeatureenabledonlag1/1/1ontheprimaryVSXswitchandloop
protectenabledonlag1/1/2onthesecondaryVSXswitch.Whenaloopoccurs,loopprotectnotifiesthe
secondaryVSXswitchthataloopisonthenetworkandinterface1/1/2wasblocked.Whenyouentershow
interface 1/1/2onthesecondaryswitch,theoutputfromthecommandindicatesthattheinterfacewas
blockedbyVSXwheninfacttheloopprotectfeatureblockedtheinterfacetostoptheloop.
Ifyouentershow lacp interfacesonthedownstreamswitch,theforwardingstateoftheblocked
interfacesisdisplayedasdown,asshowninthefollowingexample:
| switch(config)#   |               | show    | lacp         | interfaces |                |          |                |     |     |
| ----------------- | ------------- | ------- | ------------ | ---------- | -------------- | -------- | -------------- | --- | --- |
| State             | abbreviations | :       |              |            |                |          |                |     |     |
| A - Active        |               | P -     | Passive      |            | F - Aggregable |          | I - Individual |     |     |
| S - Short-timeout |               | L -     | Long-timeout |            | N - InSync     |          | O - OutofSync  |     |     |
| C - Collecting    |               | D -     | Distributing |            |                |          |                |     |     |
| X - State         | m/c           | expired |              |            | E - Default    | neighbor | state          |     |     |
| Actor             | details       | of all  | interfaces:  |            |                |          |                |     |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port |     | State System-ID |     | System Aggr | Forwarding |     |
| ---- | ---- | ---- | ---- | --- | --------------- | --- | ----------- | ---------- | --- |
|      | Name | Id   | Pri  |     |                 |     | Pri Key     | State      |     |
------------------------------------------------------------------------------
| 1/3/1 | lag1 | 130 | 1   |     | ALFNCD f8:60:f0:06:87:00 |     | 65534 1 | up         |     |
| ----- | ---- | --- | --- | --- | ------------------------ | --- | ------- | ---------- | --- |
| 1/3/2 | lag1 | 131 | 1   |     | ALFNCD f8:60:f0:06:87:00 |     | 65534 1 | up         |     |
| 1/7/3 | lag2 | 388 | 1   |     | ALFOE f8:60:f0:06:87:00  |     | 65534 2 | lacp-block |     |
1/10/46 lag2 623 1 ALFOE f8:60:f0:06:87:00 65534 2 lacp-block
| Partner | details | of all | interfaces: |     |     |     |     |     |     |
| ------- | ------- | ------ | ----------- | --- | --- | --- | --- | --- | --- |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port |     | State System-ID |     | System Aggr |     |     |
| ---- | ---- | ---- | ---- | --- | --------------- | --- | ----------- | --- | --- |
|      | Name | Id   | Pri  |     |                 |     | Pri Key     |     |     |
------------------------------------------------------------------------------
| 1/3/1 | lag1 | 206  | 1   |     | ALFNCD f8:60:f0:06:49:00 |     | 65534 1 |     |     |
| ----- | ---- | ---- | --- | --- | ------------------------ | --- | ------- | --- | --- |
| 1/3/2 | lag1 | 1130 | 1   |     | ALFNCD f8:60:f0:06:49:00 |     | 65534 1 |     |     |
91
| AOS-CX10.07VirtualSwitchingExtension(VSX)Guide| |     |     |     |     | (6400,8xxxSwitchSeries) |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |

| 1/7/3   | lag2 |     | 0   | 65534 | PLFOEX | 00:00:00:00:00:00 |     | 65534 0 |     |
| ------- | ---- | --- | --- | ----- | ------ | ----------------- | --- | ------- | --- |
| 1/10/46 | lag2 |     | 0   | 65534 | PLFOEX | 00:00:00:00:00:00 |     | 65534 0 |     |
Interfacelag2,whichwasshownaslacp-blockedinthepreviousexampleisshownasdownontheprimary
VSXswitch,asshowninthefollowingexample:
switch(config)#
|                 |                 |              | show           | loop-protect   |            |                     |          |              |     |
| --------------- | --------------- | ------------ | -------------- | -------------- | ---------- | ------------------- | -------- | ------------ | --- |
| Status          |                 | and Counters |                | - Loop         | Protection | Information         |          |              |     |
| Transmit        |                 | Interval     |                |                | :          | 5 (sec)             |          |              |     |
| Port            | Re-enable       |              | Timer          |                | :          | Disabled            |          |              |     |
| Interface       |                 | lag1         |                |                |            |                     |          |              |     |
|                 | Loop-protect    |              | enabled        |                | :          | Yes                 |          |              |     |
|                 | Loop-Protect    |              | enabled        | VLANs          | :          | 1-100               |          |              |     |
|                 | Action          | on           | loop detection |                | :          | TX disable          |          |              |     |
|                 | Loop            | detected     | count          |                | :          | 1                   |          |              |     |
|                 | Loop            | detected     |                |                | :          | Yes                 |          |              |     |
|                 | Detected        |              | on VLAN        |                | :          | 10                  |          |              |     |
|                 | Detected        |              | at             |                | :          | 2019-09-27T00:12:55 |          |              |     |
|                 | Interface       |              | status         |                | :          | up                  |          |              |     |
| Interface       |                 | lag2         |                |                |            |                     |          |              |     |
|                 | Loop-protect    |              | enabled        |                | :          | Yes                 |          |              |     |
|                 | Loop-Protect    |              | enabled        | VLANs          | :          | 2021-2121           |          |              |     |
|                 | Action          | on           | loop detection |                | :          | TX disable          |          |              |     |
|                 | Loop            | detected     | count          |                | :          | 1                   |          |              |     |
|                 | Loop            | detected     |                |                | :          | Yes                 |          |              |     |
|                 | Detected        |              | on VLAN        |                | :          | 2103                |          |              |     |
|                 | Detected        |              | at             |                | :          | 2019-09-27T00:13:14 |          |              |     |
|                 | Interface       |              | status         |                | :          | down                |          |              |     |
| switch(config)# |                 |              | show           | lacp           | interfaces |                     |          |              |     |
| State           | abbreviations   |              |                | :              |            |                     |          |              |     |
| A               | - Active        |              | P              | - Passive      |            | F - Aggregable      | I        | - Individual |     |
| S               | - Short-timeout |              | L              | - Long-timeout |            | N - InSync          | O        | - OutofSync  |     |
| C               | - Collecting    |              | D              | - Distributing |            |                     |          |              |     |
| X               | - State         | m/c          | expired        |                |            | E - Default         | neighbor | state        |     |
| Actor           | details         |              | of all         | interfaces:    |            |                     |          |              |     |
------------------------------------------------------------------------------
| Intf |     | Aggr |     | Port Port | State | System-ID |     | System Aggr | Forwarding |
| ---- | --- | ---- | --- | --------- | ----- | --------- | --- | ----------- | ---------- |
|      |     | Name |     | Id Pri    |       |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/4/14  |     | lag1(mc) |     | 206 1           | ALFNCD | f8:60:f0:06:49:00 |     | 65534 1 | up   |
| ------- | --- | -------- | --- | --------------- | ------ | ----------------- | --- | ------- | ---- |
| 1/5/15  |     | lag2(mc) |     |                 |        |                   |     |         | down |
| Partner |     | details  | of  | all interfaces: |        |                   |     |         |      |
------------------------------------------------------------------------------
| Intf |     | Aggr |     | Port Port | State | System-ID |     | System Aggr |     |
| ---- | --- | ---- | --- | --------- | ----- | --------- | --- | ----------- | --- |
|      |     | Name |     | Id Pri    |       |           |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/4/14 |     | lag1(mc) |     | 130 1 | ALFNCD | f8:60:f0:06:87:00 |     | 65534 1 |     |
| ------ | --- | -------- | --- | ----- | ------ | ----------------- | --- | ------- | --- |
| 1/5/15 |     | lag2(mc) |     |       |        |                   |     |         |     |
Interfacelag2isalsoshownasdownonthesecondaryVSXswitch,asshowninthefollowingexample:
LoopprotectconfigurationsoverVSX|92

|     | switch(config)#   |               | show           | loop-protect     |            |             |                |          |            |     |
| --- | ----------------- | ------------- | -------------- | ---------------- | ---------- | ----------- | -------------- | -------- | ---------- | --- |
|     | Status            | and Counters  |                | - Loop           | Protection |             | Information    |          |            |     |
|     | Transmit          | Interval      |                |                  |            | : 5         | (sec)          |          |            |     |
|     | Port              | Re-enable     | Timer          |                  |            | : 15        | (sec)          |          |            |     |
|     | Interface         | lag1          |                |                  |            |             |                |          |            |     |
|     | Loop-protect      |               | enabled        |                  |            | : Yes       |                |          |            |     |
|     | Loop-Protect      |               | enabled        |                  | VLANs      | : 1-100     |                |          |            |     |
|     | Action            | on            | loop detection |                  |            | : TX        | disable        |          |            |     |
|     | Loop              | detected      | count          |                  |            | : 0         |                |          |            |     |
|     | Loop              | detected      |                |                  |            | : No        |                |          |            |     |
|     | Interface         |               | status         |                  |            | : up        |                |          |            |     |
|     | Interface         | lag2          |                |                  |            |             |                |          |            |     |
|     | Loop-protect      |               | enabled        |                  |            | : Yes       |                |          |            |     |
|     | Loop-Protect      |               | enabled        |                  | VLANs      | : 2021-2121 |                |          |            |     |
|     | Action            | on            | loop detection |                  |            | : TX        | disable        |          |            |     |
|     | Loop              | detected      | count          |                  |            | : 0         |                |          |            |     |
|     | Loop              | detected      |                |                  |            | : No        |                |          |            |     |
|     | Interface         |               | status         |                  |            | : down      |                |          |            |     |
|     | switch(config)#   |               | show           | lacp             | interfaces |             |                |          |            |     |
|     | State             | abbreviations |                | :                |            |             |                |          |            |     |
|     | A - Active        |               |                | P - Passive      |            |             | F - Aggregable | I -      | Individual |     |
|     | S - Short-timeout |               |                | L - Long-timeout |            |             | N - InSync     | O -      | OutofSync  |     |
|     | C - Collecting    |               |                | D - Distributing |            |             |                |          |            |     |
|     | X - State         | m/c           | expired        |                  |            |             | E - Default    | neighbor | state      |     |
|     | Actor             | details       | of all         | interfaces:      |            |             |                |          |            |     |
------------------------------------------------------------------------------
|     | Intf | Aggr |     | Port | Port | State | System-ID |     | System Aggr | Forwarding |
| --- | ---- | ---- | --- | ---- | ---- | ----- | --------- | --- | ----------- | ---------- |
|     |      | Name |     | Id   | Pri  |       |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
|     | 1/3/2   | lag1(mc) |     | 1130 | 1           | ALFNCD | f8:60:f0:06:49:00 |     | 65534 1 | up   |
| --- | ------- | -------- | --- | ---- | ----------- | ------ | ----------------- | --- | ------- | ---- |
|     | 1/9/3   | lag2(mc) |     |      |             |        |                   |     |         | down |
|     | Partner | details  | of  | all  | interfaces: |        |                   |     |         |      |
------------------------------------------------------------------------------
|     | Intf | Aggr |     | Port | Port | State | System-ID |     | System Aggr |     |
| --- | ---- | ---- | --- | ---- | ---- | ----- | --------- | --- | ----------- | --- |
|     |      | Name |     | Id   | Pri  |       |           |     | Pri Key     |     |
------------------------------------------------------------------------------
|         | 1/3/2 | lag1(mc) |      | 131     | 1   | ALFNCD | f8:60:f0:06:87:00 |     | 65534 1 |     |
| ------- | ----- | -------- | ---- | ------- | --- | ------ | ----------------- | --- | ------- | --- |
|         | 1/9/3 | lag2(mc) |      |         |     |        |                   |     |         |     |
| Setting |       | up       | loop | protect |     | over   | VSX               |     |         |     |
TosetuploopprotectoverVSX:
1. CreatetheVSXLAG.
2. EnableloopprotectontheprimaryandsecondaryVSXswitches.SeetheLayer2BridgingGuidefor
informationabouthowtoenableloopprotectonaswitch.
| An  | example |     | configuration |     |     |     | of loop | protect | over | VSX |
| --- | ------- | --- | ------------- | --- | --- | --- | ------- | ------- | ---- | --- |
Thefollowingfigureisasimplifiedconfiguration.Mostnetworkconfigurationswillhavemorethanone
downstreamswitch.
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 93

| Figure 14 | ExampleofLoopProtectOverVSX |     |     |     |
| --------- | --------------------------- | --- | --- | --- |
Thefollowingsectionsprovideinformationabouttheconfigurationsontheswitchesbeforeandafter
configuringtheloopprotectfeature.
| VSX configurations |     | before | enabling | loop protect |
| ------------------ | --- | ------ | -------- | ------------ |
ThissectionprovidesconfigurationinformationfortheprimaryVSXswitch,secondaryVSXswitch,and
downstreamswitchbeforeloopprotectisenabled.
| VSX primaryswitch | before         | enablingloopprotect |     |     |
| ----------------- | -------------- | ------------------- | --- | --- |
| hostname          | Primary        |                     |     |     |
| module 1/1        | product-number | jl363a              |     |     |
cli-session
| timeout    | 0        |     |     |     |
| ---------- | -------- | --- | --- | --- |
| ssh server | vrf mgmt |     |     |     |
vlan 1-2000
| interface | mgmt |     |     |     |
| --------- | ---- | --- | --- | --- |
no shutdown
ip dhcp
| interface | lag 1 multi-chassis |     |     |     |
| --------- | ------------------- | --- | --- | --- |
no shutdown
no routing
| vlan      | trunk native 1      |        |     |     |
| --------- | ------------------- | ------ | --- | --- |
| vlan      | trunk allowed       | 1-2000 |     |     |
| lacp      | mode active         |        |     |     |
| interface | lag 2 multi-chassis |        |     |     |
no shutdown
no routing
| vlan      | trunk native 1 |        |     |     |
| --------- | -------------- | ------ | --- | --- |
| vlan      | trunk allowed  | 1-2000 |     |     |
| lacp      | mode active    |        |     |     |
| interface | 1/1/1          |        |     |     |
no shutdown
| lag       | 1     |     |     |     |
| --------- | ----- | --- | --- | --- |
| interface | 1/1/2 |     |     |     |
no shutdown
| lag       | 2     |     |     |     |
| --------- | ----- | --- | --- | --- |
| interface | 1/1/3 |     |     |     |
no shutdown
no routing
LoopprotectconfigurationsoverVSX|94

| vlan      | trunk native  | 1 tag |     |     |     |     |     |
| --------- | ------------- | ----- | --- | --- | --- | --- | --- |
| vlan      | trunk allowed | all   |     |     |     |     |     |
| interface | 1/1/30        |       |     |     |     |     |     |
no shutdown
| ip address | 10.1.1.1/24 |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- | --- |
vsx
| inter-switch-link |                   | 1/1/3            |          |              |          |            |     |
| ----------------- | ----------------- | ---------------- | -------- | ------------ | -------- | ---------- | --- |
| role              | primary           |                  |          |              |          |            |     |
| keepalive         | peer              | 10.1.1.2 source  | 10.1.1.1 |              |          |            |     |
| LACPinterface     | configuration     |                  |          |              |          |            |     |
| Primary#          | show lacp         | interfaces       |          |              |          |            |     |
| State             | abbreviations     | :                |          |              |          |            |     |
| A -               | Active            | P - Passive      | F        | - Aggregable | I -      | Individual |     |
| S -               | Short-timeout     | L - Long-timeout | N        | - InSync     | O -      | OutofSync  |     |
| C -               | Collecting        | D - Distributing |          |              |          |            |     |
| X -               | State m/c expired |                  | E        | - Default    | neighbor | state      |     |
| Actor             | details of        | all interfaces:  |          |              |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --------- | ----- | --------- | --- | ----------- | ---------- |
|      | Name | Id Pri    |       |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/1   | lag1(mc) | 1 1                | ALFNCD | 04:09:73:62:c8:00 |     | 65534 1 | up  |
| ------- | -------- | ------------------ | ------ | ----------------- | --- | ------- | --- |
| 1/1/2   | lag2(mc) | 2 1                | ALFNCD | 04:09:73:62:c8:00 |     | 65534 2 | up  |
| Partner | details  | of all interfaces: |        |                   |     |         |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID |     | System Aggr |     |
| ---- | ---- | --------- | ----- | --------- | --- | ----------- | --- |
|      | Name | Id Pri    |       |           |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/1/1 | lag1(mc) | 18 1 | ALFNCD | e0:07:1b:cb:e1:5a |     | 65534 1 |     |
| ----- | -------- | ---- | ------ | ----------------- | --- | ------- | --- |
| 1/1/2 | lag2(mc) | 20 1 | ALFNCD | e0:07:1b:cb:e1:5a |     | 65534 2 |     |
VSX configuration
| Primary#            | show vsx         | brief  |                     |                         |     |     |     |
| ------------------- | ---------------- | ------ | ------------------- | ----------------------- | --- | --- | --- |
| ISL                 | State            |        |                     | : In-Sync               |     |     |     |
| Device              | State            |        |                     | : Peer-Established      |     |     |     |
| Keepalive           | State            |        |                     | : Keepalive-Established |     |     |     |
| Device              | Role             |        |                     | : primary               |     |     |     |
| Number              | of Multi-chassis | LAG    | interfaces          | : 2                     |     |     |     |
| VSX secondaryswitch |                  | before | enablingloopprotect |                         |     |     |     |
| hostname            | Secondary        |        |                     |                         |     |     |     |
| module 1/1          | product-number   | jl363a |                     |                         |     |     |     |
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
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 95

| lacp      | mode active         |     |     |     |     |     |     |
| --------- | ------------------- | --- | --- | --- | --- | --- | --- |
| interface | lag 2 multi-chassis |     |     |     |     |     |     |
no shutdown
no routing
| vlan | trunk native  | 1      |     |     |     |     |     |
| ---- | ------------- | ------ | --- | --- | --- | --- | --- |
| vlan | trunk allowed | 1-2000 |     |     |     |     |     |
| lacp | mode active   |        |     |     |     |     |     |
interface 1/1/1
no shutdown
lag 1
interface 1/1/2
no shutdown
lag 2
interface 1/1/3
no shutdown
no routing
| vlan | trunk native  | 1 tag |     |     |     |     |     |
| ---- | ------------- | ----- | --- | --- | --- | --- | --- |
| vlan | trunk allowed | all   |     |     |     |     |     |
interface 1/1/30
no shutdown
| ip  | address 10.1.1.2/24 |     |     |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- | --- | --- |
vsx
| inter-switch-link |     | 1/1/3 |     |     |     |     |     |
| ----------------- | --- | ----- | --- | --- | --- | --- | --- |
role secondary
| keepalive     | peer              | 10.1.1.1 source  | 10.1.1.2 |              |          |            |     |
| ------------- | ----------------- | ---------------- | -------- | ------------ | -------- | ---------- | --- |
| LACPinterface | configuration     |                  |          |              |          |            |     |
| Secondary#    | show              | lacp interfaces  |          |              |          |            |     |
| State         | abbreviations     | :                |          |              |          |            |     |
| A -           | Active            | P - Passive      | F        | - Aggregable | I -      | Individual |     |
| S -           | Short-timeout     | L - Long-timeout | N        | - InSync     | O -      | OutofSync  |     |
| C -           | Collecting        | D - Distributing |          |              |          |            |     |
| X -           | State m/c expired |                  | E        | - Default    | neighbor | state      |     |
| Actor         | details of        | all interfaces:  |          |              |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --------- | ----- | --------- | --- | ----------- | ---------- |
|      | Name | Id Pri    |       |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/1   | lag1(mc) | 1001 1             | ALFNCD | 04:09:73:62:c8:00 |     | 65534 1 | up  |
| ------- | -------- | ------------------ | ------ | ----------------- | --- | ------- | --- |
| 1/1/2   | lag2(mc) | 1002 1             | ALFNCD | 04:09:73:62:c8:00 |     | 65534 2 | up  |
| Partner | details  | of all interfaces: |        |                   |     |         |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID |     | System Aggr |     |
| ---- | ---- | --------- | ----- | --------- | --- | ----------- | --- |
|      | Name | Id Pri    |       |           |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/1/1 | lag1(mc) | 19 1 | ALFNCD | e0:07:1b:cb:e1:5a |     | 65534 1 |     |
| ----- | -------- | ---- | ------ | ----------------- | --- | ------- | --- |
| 1/1/2 | lag2(mc) | 31 1 | ALFNCD | e0:07:1b:cb:e1:5a |     | 65534 2 |     |
VSX configuration
Secondary#
|           | show             | vsx brief |            |                         |     |     |     |
| --------- | ---------------- | --------- | ---------- | ----------------------- | --- | --- | --- |
| ISL       | State            |           |            | : In-Sync               |     |     |     |
| Device    | State            |           |            | : Peer-Established      |     |     |     |
| Keepalive | State            |           |            | : Keepalive-Established |     |     |     |
| Device    | Role             |           |            | : secondary             |     |     |     |
| Number    | of Multi-chassis | LAG       | interfaces | : 2                     |     |     |     |
LoopprotectconfigurationsoverVSX|96

| Downstreamswitch |     | before enablingloopprotect |     |     |     |     |
| ---------------- | --- | -------------------------- | --- | --- | --- | --- |
hostname Downstream
cli-session
| timeout    | 0        |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- |
| ssh server | vrf mgmt |     |     |     |     |     |
vlan 1-2000
interface mgmt
no shutdown
ip dhcp
| interface | lag 1 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
no shutdown
no routing
| vlan trunk | native  | 1      |     |     |     |     |
| ---------- | ------- | ------ | --- | --- | --- | --- |
| vlan trunk | allowed | 1-2000 |     |     |     |     |
| lacp mode  | active  |        |     |     |     |     |
| interface  | lag 2   |        |     |     |     |     |
no shutdown
no routing
| vlan trunk | native  | 1      |     |     |     |     |
| ---------- | ------- | ------ | --- | --- | --- | --- |
| vlan trunk | allowed | 1-2000 |     |     |     |     |
| lacp mode  | active  |        |     |     |     |     |
interface 1/1/17
no shutdown
lag 1
interface 1/1/18
no shutdown
lag 1
interface 1/1/19
no shutdown
lag 2
interface 1/1/30
no shutdown
lag 2
ThefollowingisanexampleofanLACPinterfaceconfiguration.
| Downstream#         | show        | lacp interfaces  |                |          |            |     |
| ------------------- | ----------- | ---------------- | -------------- | -------- | ---------- | --- |
| State abbreviations |             | :                |                |          |            |     |
| A - Active          |             | P - Passive      | F - Aggregable | I -      | Individual |     |
| S - Short-timeout   |             | L - Long-timeout | N - InSync     | O -      | OutofSync  |     |
| C - Collecting      |             | D - Distributing |                |          |            |     |
| X - State           | m/c expired |                  | E - Default    | neighbor | state      |     |
| Actor details       | of          | all interfaces:  |                |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --------- | --------------- | --- | ----------- | ---------- |
|      | Name | Id Pri    |                 |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/17  | lag1    | 18 1               | ALFNCD e0:07:1b:cb:e1:5a |     | 65534 1 | up  |
| ------- | ------- | ------------------ | ------------------------ | --- | ------- | --- |
| 1/1/18  | lag1    | 19 1               | ALFNCD e0:07:1b:cb:e1:5a |     | 65534 1 | up  |
| 1/1/19  | lag2    | 20 1               | ALFNCD e0:07:1b:cb:e1:5a |     | 65534 2 | up  |
| 1/1/30  | lag2    | 31 1               | ALFNCD e0:07:1b:cb:e1:5a |     | 65534 2 | up  |
| Partner | details | of all interfaces: |                          |     |         |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-ID |     | System Aggr |     |
| ---- | ---- | --------- | --------------- | --- | ----------- | --- |
|      | Name | Id Pri    |                 |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/1/17 | lag1 | 1 1 | ALFNCD 04:09:73:62:c8:00 |     | 65534 1 |     |
| ------ | ---- | --- | ------------------------ | --- | ------- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 97

| 1/1/18             | lag1 | 1001 1 | ALFNCD   | 04:09:73:62:c8:00 | 65534 1 |
| ------------------ | ---- | ------ | -------- | ----------------- | ------- |
| 1/1/19             | lag2 | 2 1    | ALFNCD   | 04:09:73:62:c8:00 | 65534 2 |
| 1/1/30             | lag2 | 1002 1 | ALFNCD   | 04:09:73:62:c8:00 | 65534 2 |
| VSX configurations |      | after  | enabling | loop protect      |         |
ThissectionprovidesconfigurationinformationfortheprimaryVSXswitch,secondaryVSXswitch,and
downstreamswitchafterloopprotectisenabled.
| VSX primaryswitch |     | after enablingloopprotect |     |     |     |
| ----------------- | --- | ------------------------- | --- | --- | --- |
Thefollowingconfigurationshowsthatloopprotectisenabled.
| hostname   | Primary        |        |     |     |     |
| ---------- | -------------- | ------ | --- | --- | --- |
| module 1/1 | product-number | jl363a |     |     |     |
cli-session
| timeout    | 0        |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- |
| ssh server | vrf mgmt |     |     |     |     |
vlan 1-2000
| interface | mgmt |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
no shutdown
ip dhcp
| interface | lag 1 multi-chassis |     |     |     |     |
| --------- | ------------------- | --- | --- | --- | --- |
no shutdown
no routing
| vlan | trunk native  | 1      |     |     |     |
| ---- | ------------- | ------ | --- | --- | --- |
| vlan | trunk allowed | 1-2000 |     |     |     |
| lacp | mode active   |        |     |     |     |
loop-protect
| loop-protect | vlan                | 1-2000 |     |     |     |
| ------------ | ------------------- | ------ | --- | --- | --- |
| interface    | lag 2 multi-chassis |        |     |     |     |
no shutdown
no routing
| vlan | trunk native  | 1      |     |     |     |
| ---- | ------------- | ------ | --- | --- | --- |
| vlan | trunk allowed | 1-2000 |     |     |     |
| lacp | mode active   |        |     |     |     |
loop-protect
| loop-protect | vlan  | 1-2000 |     |     |     |
| ------------ | ----- | ------ | --- | --- | --- |
| interface    | 1/1/1 |        |     |     |     |
no shutdown
| lag       | 1     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
| interface | 1/1/2 |     |     |     |     |
no shutdown
| lag       | 2     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
| interface | 1/1/3 |     |     |     |     |
no shutdown
no routing
| vlan      | trunk native  | 1 tag |     |     |     |
| --------- | ------------- | ----- | --- | --- | --- |
| vlan      | trunk allowed | all   |     |     |     |
| interface | 1/1/30        |       |     |     |     |
no shutdown
| ip address | 10.1.1.1/24 |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- |
vsx
| inter-switch-link |         | 1/1/3           |          |     |     |
| ----------------- | ------- | --------------- | -------- | --- | --- |
| role              | primary |                 |          |     |     |
| keepalive         | peer    | 10.1.1.2 source | 10.1.1.1 |     |     |
LoopprotectconfigurationsoverVSX|98

| VSX secondaryafter | before         | enablingloopprotect |
| ------------------ | -------------- | ------------------- |
| hostname           | Secondary      |                     |
| module 1/1         | product-number | jl363a              |
cli-session
| timeout    | 0        |     |
| ---------- | -------- | --- |
| ssh server | vrf mgmt |     |
vlan 1-2000
| interface | mgmt |     |
| --------- | ---- | --- |
no shutdown
ip dhcp
| interface | lag 1 multi-chassis |     |
| --------- | ------------------- | --- |
no shutdown
no routing
| vlan | trunk native 1 |        |
| ---- | -------------- | ------ |
| vlan | trunk allowed  | 1-2000 |
| lacp | mode active    |        |
loop-protect
| loop-protect | vlan 1-2000         |     |
| ------------ | ------------------- | --- |
| interface    | lag 2 multi-chassis |     |
no shutdown
no routing
| vlan | trunk native 1 |        |
| ---- | -------------- | ------ |
| vlan | trunk allowed  | 1-2000 |
| lacp | mode active    |        |
loop-protect
| loop-protect | vlan 1-2000 |     |
| ------------ | ----------- | --- |
| interface    | 1/1/1       |     |
no shutdown
| lag       | 1     |     |
| --------- | ----- | --- |
| interface | 1/1/2 |     |
no shutdown
| lag       | 2     |     |
| --------- | ----- | --- |
| interface | 1/1/3 |     |
no shutdown
no routing
| vlan      | trunk native 1 | tag |
| --------- | -------------- | --- |
| vlan      | trunk allowed  | all |
| interface | 1/1/30         |     |
no shutdown
| ip address | 10.1.1.2/24 |     |
| ---------- | ----------- | --- |
vsx
| inter-switch-link | 1/1/3         |                     |
| ----------------- | ------------- | ------------------- |
| role              | secondary     |                     |
| keepalive         | peer 10.1.1.1 | source 10.1.1.2     |
| Downstreamswitch  | after         | enablingloopprotect |
| hostname          | Downstream    |                     |
cli-session
| timeout    | 0        |     |
| ---------- | -------- | --- |
| ssh server | vrf mgmt |     |
vlan 1-2000
| interface | mgmt |     |
| --------- | ---- | --- |
no shutdown
ip dhcp
| interface | lag 1 |     |
| --------- | ----- | --- |
no shutdown
no routing
| vlan      | trunk native 1 |        |
| --------- | -------------- | ------ |
| vlan      | trunk allowed  | 1-2000 |
| lacp      | mode active    |        |
| interface | lag 2          |        |
no shutdown
no routing
| vlan | trunk native 1 |     |
| ---- | -------------- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 99

vlan trunk allowed 1-2000
lacp mode active

interface 1/1/17

no shutdown
lag 1

interface 1/1/18

no shutdown
lag 1

interface 1/1/19

no shutdown
lag 2

interface 1/1/30

no shutdown
lag 2

Best practices for loop protect over VSX

n Enable loop protect on both primary and secondary VSX switches.

n Do not enable loop protect on the ISL link for the primary and secondary VSX switches.

n If you enable an action for loop protect, such as do-not-disable, and another action, such as Tx-Rx-

Disable, is already in effect, loop protect must be disabled and then re-enabled.

n If you run the loop-protect action do-not-disable command, on every transmit interval, the loop is

detected and the detection is reported through an SNMP trap and an event log message.

You can view the events for just the loop protect feature by entering the show events -d hpe-lpd
command.

n The total number of VLANs across ports is (ports x VLANs) = 4094 ports per VLAN. Loop protect can be
configured on a maximum of 4094 VLANs across all interfaces without updating CoPP policies for loop
protect. If your network configuration requires you to configure more VLAN, update your CoPP policies
values for loop protect to ensure that you allocate more resources. You can assign a maximum of 10,000
VLANs across all the interfaces.

Loop protect configurations over VSX | 100

Chapter 10

EVPN VSX support

EVPN VSX support

Ethernet VPN (EVPN) is supported with VSX . The two VSX pairs act as independent BGP routing entities to
the other VXLAN tunnel endpoints (VTEPs) or spines for control packets. However, in the datapath, both of
them act as a single logical VTEP. This is achieved by using different IP addresses for establishing the BGP
session and using a common IP as next-hop to represent the VTEP.

For more information on EVPN VSX support, see the EVPN VSX support chapter in the VXLAN Guide.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

101

Chapter 11
Upstream connectivity
| Upstream | connectivity |     |
| -------- | ------------ | --- |
Thefollowingsectiondescribesupstreamconnectivityoptionsandconfigurationsforupstreamroutingover
VSXLAGSVIlinks.
| Upstream | connectivity | options |
| -------- | ------------ | ------- |
Thisfirmwaresupportsthefollowingupstreamconnectivityoptions:
RoutedOnly Port (ROP):AphysicalportonaswitchthatprocessallLayer3functionsforpacketstoor
n
fromthesaidportwithoutanybindingtoVLANprocessing.SeeSVI(multipleVRFs)inaVSXenvironment.
SwitchedVirtualInterface (SVIs) (multiple VRFs):AnSVIisalogicalLayer3interfaceconfiguredper
n
VLAN(one-to-onemapping)thatperformsallLayer3processingforpacketstoorfromallswitchports
associatedwiththatVLAN.SeeSVI(multipleVRFs)inaVSXenvironment.
| n VSX LAG | SVIs with multiple | VRFs.See VSXLAGandlayer3ECMP |
| --------- | ------------------ | ---------------------------- |
102
| AOS-CX10.07VirtualSwitchingExtension(VSX)Guide| |     | (6400,8xxxSwitchSeries) |
| ----------------------------------------------- | --- | ----------------------- |

Figure 15 ROP with a single VRF in the VSX environment

Upstream connectivity | 103

Figure 16 SVI (multiple VRFs) in a VSX environment

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

104

Figure 17 VSX LAG and layer 3 ECMP

Upstream routing over VSX LAG SVI links
This section shows two configurations for upstream routing over VSX LAG SVI links:

n ECMP

n ECMP and VSX LAG

n Active gateway as next-hop router

The ECMP and VSX LAG configuration is the preferred configuration because LAGs introduce simplicity by
reducing the number of transit VLANs and associated SVIs. This simplified configuration results in a
minimized Sender Policy Framework (SPF) calculation time. The following figure shows that Core1 and Core2
are not in a VSX LAG, but Agg1 and Agg2 are in a VSX LAG. This figure introduces the requirement for MSTP
because all the links between the aggregate and core are bridged (trunk ports with multiple VLANs).

Upstream connectivity | 105

Figure 18 ECMP and VSX LAG in a VSX environment

The following figure differs from the previous figure in that Core1 and Core2 are in a VSX LAG, which
provides load balancing for ECMP. The transit VLANs shown in the following figure are per VRF.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

106

Figure 19 ECMP in a VSX environment

If ECMP is not supported or firewall does not support dynamic routing protocols, active gateway can be
used as next-hop router. The following figure shows the specific use case of active/standby firewall with
active gateway as the next-hop router.

Upstream connectivity | 107

Figure 20 Active gateway as a next-hop router

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

108

Chapter 12

VSX commands

VSX commands

VSX commands do not apply to the 6300 series switches.

active-gateway

Syntax

active-gateway {ip | ipv6} [<IP-ADDRESS>] [mac <MAC-ADDRESS>]
no active-gateway {ip | ipv6} [<IP-ADDRESS>] [mac]

Description

Configures a virtual IP and virtual MAC for an interface VLAN

The no form of this command removes the active gateway for active-active routing.

Command context

config-if-vlan

Parameters

ip

Specifies the configuration of an IPv4 address.

ipv6

Specifies the configuration of an IPv6 address.

<IP-ADDRESS>

Specifies the IPv4 or IPv6 address.

n Syntax for IPv4: A.B.C.D

n Syntax for IPv6: A:B::C:D

<MAC-ADDR>

Specifies the Virtual MAC address. Syntax: xx:xx:xx:xx:xx:xx

Authority

Administrators or local user group members with execution rights for this command.

Usage

Before configuring active gateway, confirm that an IP address is on the SVI that is in the same subnet as the
active gateway IP you are trying to configure. If an active gateway IP does not have an SVI IP with the same
subnet, the CLI allows the configuration, but the active gateway IP will not be programmed in the kernel,
resulting the active gateway to be unreachable.

Active forwarding cannot be configured when ICMP redirect is enabled. Enter the no ip icmp redirect
command for disabling ICMP redirect.

It is highly recommended that you use an IPv6 link-local address as a gateway (VIP) on the active gateway
IPv6 configuration.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

109

IfVRRPoractiveforwardingisconfiguredonanSVI,activegatewaycannotbeconfigured.Activegateway
withoverlappingnetworksisnotallowed.Maximumof16uniquevirtualMACsaresupportedinasystem.
Themaximumnumberofsupportedactivegatewaysperswitchis4,000.Sinceamaximumof31secondary
IPv4addressescanbeconfiguredonanSVI,32IPv4activegateways(alongwiththeprimaryIPv4address)
canbeconfiguredperSVIwithIPmultinettingsupport.ThissupportisalsothesameforIPv6addresses.
DonotusepeersystemMACaddressasanactive-gatewayVMAC.IfsameMACaddressisused,theVSX
synchronizationwilltrytosynctheconfigurationonsecondaryswitchandcausetrafficdisruptions.
Examples
Configuringactive-gatewaywhentheIPaddressisdifferentfromtheSVIIPaddressonbothVSXpeers
(validforIPv6andIPv4):
Switch1:
| switch1(config-if-vlan)# | ip address | 192.168.1.250/24 |
| ------------------------ | ---------- | ---------------- |
switch1(config-if-vlan)# active-gateway ip 192.168.1.253 mac 00:00:00:00:00:01
switch1(config-if-vlan)# active-gateway ipv6 fe80::01 mac 00:00:00:01:00:01
Switch2:
| switch2(config-if-vlan)# | ip address | 192.168.1.251/24 |
| ------------------------ | ---------- | ---------------- |
switch2(config-if-vlan)# active-gateway ip 192.168.1.253 mac 00:00:00:00:00:01
switch2(config-if-vlan)# active-gateway ipv6 fe80::01 mac 00:00:00:01:00:01
Configuringactive-gatewaywhentheIPaddressisthesameastheSVIIPaddressonbothVSXpeers(valid
forIPv4only):
Switch1:
| switch1(config-if-vlan)# | ip address | 192.168.1.250/24 |
| ------------------------ | ---------- | ---------------- |
switch(config-if-vlan)# active-gateway ip 192.168.1.250 mac 00:00:00:00:00:01
Switch2:
| switch2(config-if-vlan)# | ip address | 192.168.1.250/24 |
| ------------------------ | ---------- | ---------------- |
switch2(config-if-vlan)# active-gateway ip 192.168.1.250 mac 00:00:00:00:00:01
Configuringonlytheactivegatewayaddress:
| switch(config-if-vlan)# | ip address     | 192.168.1.250/24 |
| ----------------------- | -------------- | ---------------- |
| switch(config-if-vlan)# | active-gateway | ip 192.168.1.250 |
ConfiguringonlytheactivegatewayIPMACaddress:
| switch2(config-if-vlan)# | ip address     | 192.168.1.250/24         |
| ------------------------ | -------------- | ------------------------ |
| switch2(config-if-vlan)# | active-gateway | ip mac 00:00:00:01:00:01 |
Removingtheactivegatewayforactive-activerouting(IPv6andIPv4):
VSXcommands|110

| switch(config-if-vlan)# |     | no active-gateway |     | ip  |
| ----------------------- | --- | ----------------- | --- | --- |
switch(config-if-vlan)#
|     |     | no active-gateway |     | ipv6 |
| --- | --- | ----------------- | --- | ---- |
Removingtheactivegatewayforactive-activeroutingforanIPaddress:
| switch(config-if-vlan)# |     | no active-gateway |     | ip 192.168.1.250 |
| ----------------------- | --- | ----------------- | --- | ---------------- |
Removingtheactivegatewayforactive-activeroutingforvirtualMACaddresses:
| switch(config-if-vlan)# |         | no active-gateway |     | ip mac |
| ----------------------- | ------- | ----------------- | --- | ------ |
| config-sync             | disable |                   |     |        |
Syntax
| config-sync disable |         |     |     |     |
| ------------------- | ------- | --- | --- | --- |
| no config-sync      | disable |     |     |     |
Description
PausesVSXsynchronization.
ThenoformofthiscommandrestartsVSXsynchronization.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
PausesVSXconfigurationsynchronization:
| switch(config)#     | vsx |             |         |     |
| ------------------- | --- | ----------- | ------- | --- |
| switch(config-vsx)# |     | config-sync | disable |     |
EnablestheVSXconfigurationsynchronization:
| switch(config)#     | vsx |                |         |                 |
| ------------------- | --- | -------------- | ------- | --------------- |
| switch(config-vsx)# |     | no config-sync | disable |                 |
| inter-switch-link   |     | {<PORT-NUM>    |         | | lag <LAG-ID>} |
Syntax
| inter-switch-link | {<PORT-NUM> | |   | lag <LAG-ID>} |     |
| ----------------- | ----------- | --- | ------------- | --- |
no inter-switch-link
Description
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 111

Configures a physical port or a LAG as an interswitch link port. Only one port or LAG can be configured to
act as an ISL. Once a port is configured as an ISL, it becomes a part of all VLANs in a system.

The no form of this command clears the configuration of the interswitch link port from a physical port or a
LAG.

Command context

config-vsx

Parameters

<PORT-NUM>

Specifies a physical port on the switch. Use the format member/slot/port (for example, 1/3/1). Sets the
port to act as ISL

<LAG-ID>

Specifies the LAG ID. Run the show capacities command for the maximum number of VSX LAGs
supported for your particular type of switch.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring port 1/1/1 as an interswitch link port:

switch(config-vsx)# inter-switch-link 1/1/1

Configuring LAG 100 as an interswitch link port:

switch(config-vsx)# inter-switch-link lag 100

Clears the interswitch link port:

switch(config-vsx)# no inter-switch-link

inter-switch-link dead-interval

Syntax

inter-switch-link dead-interval <DEAD-INTERVAL>
no inter-switch-link dead-interval

Description

Sets the dead interval for the interswitch link protocol. The dead interval is the amount of time to wait for
hellos from a peer before declaring the peer to be dead. The default dead interval time is 20 seconds.

The no form of this command resets the interswitch link dead interval to the default of 20 seconds.

Command context

config-vsx

Parameters

<DEAD-INTERVAL>

VSX commands | 112

Specifiesthedeadintervalinseconds.Required.Range:2to20seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingthedeadintervalfortheinterswitchlinkprotocolto10seconds:
| switch(config)#     | vsx               |     |               |     |
| ------------------- | ----------------- | --- | ------------- | --- |
| switch(config-vsx)# | inter-switch-link |     | dead-interval | 10  |
Settingthedeadintervalfortheinterswitchlinkprotocoltothedefault:
| switch(config)#     | vsx            |                   |               |     |
| ------------------- | -------------- | ----------------- | ------------- | --- |
| switch(config-vsx)# | no vsx         | inter-switch-link | dead-interval |     |
| inter-switch-link   | hello-interval |                   |               |     |
Syntax
| inter-switch-link    | hello-interval | <HELLO-INTERVAL> |     |     |
| -------------------- | -------------- | ---------------- | --- | --- |
| no inter-switch-link | hello-interval |                  |     |     |
Description
Configurestheinterswitchlinkhello-interval.Thehellointervaldeterminesthefrequencyofahellopacket
exchangetoconfirmthecontrolplaneofthepeerisalive.Thedefaulthello-intervalis1second.
Thenoformofthiscommandsetstheinterswitchlinkhello-intervaltothedefaultof1second.
Commandcontext
config-vsx
Parameters
<HELLO-INTERVAL>
Specifieshellointervalinseconds.Range:1to5seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringtheinterswitchlinkhello-intervalto3seconds:
| switch(config)#     | vsx               |     |                |     |
| ------------------- | ----------------- | --- | -------------- | --- |
| switch(config-vsx)# | inter-switch-link |     | hello-interval | 3   |
Resettingtheinterswitchlinkhello-intervaltothedefaultof1second:
| switch(config)#     | vsx                  |     |                |     |
| ------------------- | -------------------- | --- | -------------- | --- |
| switch(config-vsx)# | no inter-switch-link |     | hello-interval |     |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 113

| inter-switch-link |     | hold-time |     |     |
| ----------------- | --- | --------- | --- | --- |
Syntax
| inter-switch-link    | hold-time | <HOLD-INTERVAL> |     |     |
| -------------------- | --------- | --------------- | --- | --- |
| no inter-switch-link | hold-time |                 |     |     |
Description
Setstheholdtimefortheinterswitchlinkprotocol.Aportistreatedasdownonlywhenitstaysdownforthe
configuredholdtimeinterval.Thedefaultholdtimeis0seconds.
Thenoformofthiscommandsetstheinterswitchlinkprotocolholdtimetothedefaultof0seconds.
Commandcontext
config-vsx
Parameters
<HOLD-INTERVAL>
Specifiestheholdintervalinseconds.Required.Range:0to3seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingtheholdtimeforinterswitchlinkprotocolto2seconds:
| switch(config)# | vsx |     |     |     |
| --------------- | --- | --- | --- | --- |
switch(config-vsx)#
|     | inter-switch-link |     | hold-time | 2   |
| --- | ----------------- | --- | --------- | --- |
Settingtheinterswitchlinkprotocolholdtimetothedefaultof0seconds:
| switch(config)#     | vsx |                      |           |     |
| ------------------- | --- | -------------------- | --------- | --- |
| switch(config-vsx)# | no  | inter-switch-link    | hold-time |     |
| inter-switch-link   |     | peer-detect-interval |           |     |
Syntax
| inter-switch-link    | peer-detect-interval |     | <PEER-DETECT-INTERVAL> |     |
| -------------------- | -------------------- | --- | ---------------------- | --- |
| no inter-switch-link | peer-detect-interval |     |                        |     |
Description
SetstheamountoftimeinsecondsthattheVSXswitchwaitsfortheISLinterfacetolinkupafterareboot.
IftheISLlinkdoesnotcomeupwithinthistimewindow,theVSXswitchdeclaresitselfassplitfromitspeer.
Thedefaultpeerdetectintervalis300seconds.
Thenoformofthiscommandsetstheinterswitchlinkprotocolpeerdetectintervaltothedefaultof300
seconds.
Commandcontext
config-vsx
Parameters
VSXcommands|114

<PEER-DETECT-INTERVAL>

Specifies the peer detect interval in seconds. Required. Range: 60 to 1800 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

After a VSX switch reboots, the switch waits 5 minutes by default to receive a hello packet before it declares
itself to be out-of-sync. The inter-switch-link peer-detect-interval <PEER-DETECT-INTERVAL>
command lets you change how long the switch waits to receive the hello packet before the switch declares
itself to be out-of-sync.

Examples

Setting the peer detect interval to 180 seconds:

switch(config)# vsx
switch(config-vsx)# inter-switch-link peer-detect-interval 180

Restoring the peer detect interval to the default (300 seconds):

switch(config)# vsx
switch(config-vsx)# no inter-switch-link peer-detect-interval

interface lag multi-chassis

Syntax

interface lag <LAG-ID> multi-chassis [static]
no interface lag <LAG-ID>

Description

Configures a given LAG as a dynamic multichassis LAG (VSX LAG), which supports a maximum of four
member links per switch segment. A VSX LAG across a downstream switch can have at most a total of eight
member links.

The no form of this command removes a VSX LAG.

Command context

config

Parameters

<LAG-ID>

Specifies the LAG ID. Run the show capacities vsx command for the maximum number of VSX LAGs
supported for your particular type of switch; however, the maximum VSX LAG value considers that one
port is used for the ISL, which is not a VSX LAG. Required.

static

Specifies the multichassis LAG as static. Optional.

Authority

Administrators or local user group members with execution rights for this command.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

115

Usage

A VSX LAG across a VSX pair can have at most a total of eight interfaces.

n When creating a VSX LAG, select an equal number of member links in each segment for load balancing, such

as four member links (one segment) and four member links (another segment). Do not create a VSX LAG

with four member links in one switch and two member links on another segment. A switch can have a

maximum of four member links.

n Make sure that the VSX LAG interface on both the VSX primary and secondary switches has a member port

configured and enabled.

n Make sure that you also have a non-VSX port that is available for the ISL.

You cannot change the mode of a multichassis LAG without removing the multichassis LAG first. To change
a pre-existing VSX LAG to a static VSX LAG, first remove the VSX LAG with the no interface lag <LAG-ID>
command. Then, enter the interface lag <LAG-ID> multi-chassis static command.

Examples

Configuring LAG 100 as a VSX LAG:

switch(config)# interface lag 100 multi-chassis

Removing LAG 100 as a VSX LAG:

switch(config)# no interface lag 100

Specifying LAG 100 as a static VSX LAG:

switch(config)# interface lag 100 multi-chassis static

ip icmp redirect

Syntax

ip icmp redirect
no ip icmp redirect

Description

Enables the sending of ICMPv4 and ICMPv6 redirect messages to the source host. Enabled by default.

The no form of this command disables ICMPv4 and ICMPv6 redirect messages to the source host.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ICMP redirect messages:

VSX commands | 116

| switch(config)# |     | ip icmp | redirect |     |
| --------------- | --- | ------- | -------- | --- |
DisablingICMPredirectmessages:
| switch(config)# |     | no ip icmp    | redirect |     |
| --------------- | --- | ------------- | -------- | --- |
| keepalive       |     | dead-interval |          |     |
Syntax
| keepalive    | dead-interval | <DEAD-INTERVAL> |     |     |
| ------------ | ------------- | --------------- | --- | --- |
| no keepalive | dead-interval |                 |     |     |
Description
Setsthedead-intervalforkeepaliveprotocol.Thedeadintervalistheamountoftimetowaitforhellosfrom
apeerbeforedeclaringthepeertobedead.Thedefaultdead-intervalis3seconds.
Thenoformofthiscommandsetstheinterswitchlinkdead-intervaltothedefaultof3seconds.
Commandcontext
config-vsx
Parameters
| dead-interval | <DEAD-INTERVAL> |     |     |     |
| ------------- | --------------- | --- | --- | --- |
Specifiesthedead-intervalinseconds.Range:2to20seconds
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingthedead-intervalforkeepaliveprotocolto10seconds:
| switch(config)#     |     | vsx       |               |     |
| ------------------- | --- | --------- | ------------- | --- |
| switch(config-vsx)# |     | keepalive | dead-interval | 10  |
Settingthedead-intervalforkeepaliveprotocoltothedefault:
| switch(config)#     |     | vsx            |               |     |
| ------------------- | --- | -------------- | ------------- | --- |
| switch(config-vsx)# |     | no keepalive   | dead-interval |     |
| keepalive           |     | hello-interval |               |     |
Syntax
| keepalive    | hello-interval | <HELLO-INTERVAL> |     |     |
| ------------ | -------------- | ---------------- | --- | --- |
| no keepalive | hello-interval |                  |     |     |
Description
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 117

Sets the hello-interval for keepalive protocol. The hello interval determines the frequency of a hello packet
exchange to confirm the peer is alive. The default hello-interval is 1 second.

The no form of this command sets the hello-interval for keepalive protocol to the default of 1 second.

Command context

config-vsx

Parameters

hello-interval <HELLO-INTERVAL>

Specifies the hello-interval in seconds. Range: 1 to 5 seconds

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the hello-interval for keepalive protocol to 3 seconds:

switch(config)# vsx
switch(config-vsx)# keepalive hello-interval 3

Resetting the hello-interval for keepalive protocol to the default:

switch(config)# vsx
switch(config-vsx)# no keepalive hello-interval

keepalive peer

Syntax

keepalive peer <PEER-IP-ADDR> source <SOURCE-IP-ADDR> [vrf <VRF-NAME>]
no keepalive

Description

Sets the source and peer IP addresses for keepalive packets in a specified VRF. If a VRF is not specified, it
sets to the default VRF.

The no form of this command removes the source and peer IP addresses and VRF for the keepalive
protocol. VSX continues to work.

Command context

config-vsx

Parameters

peer <PEER-IP-ADDR>

Specifies the peer IPv4 address. Syntax: A.B.C.D

source <IP-ADDR>

Specifies the source IPv4 address. The source IP address is the IP address assigned to the keepalive
interface on the switch. For example, if you are entering this command on the primary switch, the source
IP address would be the IP address assigned to the keepalive interface on the primary switch. Syntax:
A.B.C.D

vrf <VRF-NAME>

VSX commands | 118

Specifies the VRF name. If you are entering this command on the primary switch, the peer IP address is
the IP address assigned to the keepalive interface for the secondary switch. If you are entering this
command on the secondary switch, the peer IP address is the IP address assigned to the keepalive
interface for the primary switch. Syntax: String

Authority

Administrators or local user group members with execution rights for this command.

Usage

To configure the keepalive feature, enter this command once on the primary switch and once on the
secondary switch. The keepalive feature is recommended for redundancy. If the ISL link goes down, the
keepalive connection keeps the traffic moving so that the peer and secondary switches can continue to
communicate. The keepalive connection is established over a routed network, and it does not have to be a
dedicated peer-to-peer link unlike ISL.

Examples

Setting the source and peer IP addresses for keepalive in the default VRF:

switch(config)# vsx
switch(config-vsx)# keepalive peer 192.168.1.1 source 192.168.1.5

Setting the source and peer IP addresses for keepalive in the vrf1:

switch(config)# vsx
switch(config-vsx)# keepalive peer 10.0.0.1 source 10.0.0.2 vrf vrf1

Removing the source and peer IP addresses and VRF for the keepalive protocol:

switch(config)# vsx
switch(config-vsx)# no keepalive

keepalive udp-port

Syntax

keepalive udp-port <PORT-NUM>
no keepalive udp-port

Description

Sets the UDP port for the keepalive protocol.

The no form of this command sets the UDP port for keepalive protocol to the default of 7678.

Command context

config-vsx

Parameters

udp-port <PORT-NUM>

Specifies UDP port number. Range: 1024-65535

Authority

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

119

Administrators or local user group members with execution rights for this command.

Examples

Setting the UDP port for keepalive protocol to 2000:

switch(config)# vsx
switch(config-vsx)# keepalive udp-port 2000

Setting the UDP port for keepalive protocol to the default of 7678:

switch(config)# vsx
switch(config-vsx)# no keepalive udp-port

lacp fallback

Syntax

lacp fallback
no lacp fallback

Description

Sets LACP fallback on a VSX LAG port. When no LACP partner is detected, the VSX LAG port makes members
of the VSX LAG function as nonbonded interfaces. To create a VSX LAG, use the interface lag multi-
chassis command.

The no form of this command sets the VSX LAG to a block state when no LACP partner is detected.

Command context

config-lag-if

Authority

Administrators or local user group members with execution rights for this command.

Usage

LACP fallback is supported only when there is a single link from the downstream or peer device to each VSX
node.

Even though this command appears to be accepted on a standard/non-VSX LAG, the fallback feature works only on

a VSX LAG (multichassis LAG) interface.

Examples

Enabling LACP fallback:

switch(config)# interface lag 1
switch(config-lag-if)# lacp fallback

Disables LACP fallback:

VSX commands | 120

| switch(config)# | interface | lag 1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-lag-if)#
|     |     | no lacp fallback |     |     |
| --- | --- | ---------------- | --- | --- |
linkup-delay-timer
Syntax
| linkup-delay-timer | <DELAY-TIMER> |     |     |     |
| ------------------ | ------------- | --- | --- | --- |
no linkup-delay-timer
Description
ConfigurestheVSXlink-updelaytimer.TheVSXdelaytimerfeatureletsyouconfigurethedelaytimer,which
delaysbringingdownstreamVSXlinksup,followingaVSXdevicerebootoranISLflap.
ThenoformofthiscommandrestorestheVSXlink-updelaytimertoadefaultof180seconds.
Commandcontext
config-vsx
Parameters
<DELAY-TIMER>
SpecifiestheVSXLAGbring-updelayinseconds.Range:0to600seconds
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
TherecommendeddelaytimersettingisdeterminedbythenumberofMACaddresses,ARPv4,androutes.
Thelink-updelaytimermightneedtobesettoahighervalueforlargernetworks,dependingontheARP
androutingtablesize.
Table 3: Recommendeddelaytimersettingsfor832xseriesswitches
Recommendeddelay
| MAC | ARPv4 |     | Routes |     |
| --- | ----- | --- | ------ | --- |
timersetting
| 16K | 16K |     | 10K     | 120 |
| --- | --- | --- | ------- | --- |
| 32K | 32K |     | 10K     | 120 |
| 47K | 47K |     | 10K     | 150 |
| 47K | 47K |     | 10K     | 250 |
| 47K | 47K |     | 10K     | 250 |
| 47K | 69K |     | 10KOSPF | 420 |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 121

Table 4: Recommendeddelaytimersettingsfor8400seriesswitches
Recommendeddelay
| MAC | ARPv4 |     |     | Routes |     |
| --- | ----- | --- | --- | ------ | --- |
timersetting
| 40K | 40K |     |     | 512             | 300 |
| --- | --- | --- | --- | --------------- | --- |
| 32K | 32K |     |     | 512             | 180 |
| 48K | 48K |     |     | 512             | 480 |
| 48K | 48K |     |     | 20KIPv4+20KIPV6 | 600 |
| 48K | 48K |     |     | 10KIPv4+10KIPv6 | 480 |
| 32K | -   |     |     | 10KIPv4         | 180 |
Examples
SettingtheVSXlink-updelaytimerto35seconds:
| switch(config)#     | vsx                |     |     |     |     |
| ------------------- | ------------------ | --- | --- | --- | --- |
| switch(config-vsx)# | linkup-delay-timer |     |     | 35  |     |
SettingtheVSXlink-updelaytimertothedefault:
| switch(config)#     | vsx |                    |     |          |     |
| ------------------- | --- | ------------------ | --- | -------- | --- |
| switch(config-vsx)# | no  | linkup-delay-timer |     |          |     |
| linkup-delay-timer  |     | exclude            |     | lag-list |     |
Syntax
| linkup-delay-timer    | exclude | lag-list | <LAG-LIST> |            |     |
| --------------------- | ------- | -------- | ---------- | ---------- | --- |
| no linkup-delay-timer | exclude | lag-list |            | <LAG-LIST> |     |
Description
ConfigurestheVSXlink-updelaytimerexcludelist.ItexcludesthebringingupofspecifieddownstreamVSX
LAGs,followingadevicerebootoranISLflap.
ThenoformofthiscommandunconfigurestheVSXlink-updelaytimerexcludelist.
Commandcontext
config-vsx
Parameters
<LAG-LIST>
SpecifiesarangeorasetofLAGinterfacestoexclude.Forexample:1or1-10or1,2,3or1,2-10.Range:
1-128characters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
VSXcommands|122

SpecifyingLAGstoexcludeLAG100:
| switch(config)#     | vsx |                    |                  |     |
| ------------------- | --- | ------------------ | ---------------- | --- |
| switch(config-vsx)# |     | linkup-delay-timer | exclude lag-list | 100 |
UnconfiguringtheVSXlink-updelaytimerexcludelistforLAG100:
| switch(config)#     | vsx          |                       |                  |     |
| ------------------- | ------------ | --------------------- | ---------------- | --- |
| switch(config-vsx)# |              | no linkup-delay-timer | exclude lag-list | 100 |
| neighbor            | <IP-ADDRESS> |                       | vsx-sync-exclude |     |
Syntax
| neighbor <IP-ADDRESS> |     | vsx-sync-exclude |     |     |
| --------------------- | --- | ---------------- | --- | --- |
Description
ExcludesVSXsyncfortheBGPneighbor.
Commandcontext
config-bgp
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ExcludingVSXsyncfortheBGPneighbor:
| switch(config-bgp)# |     | neighbor | 1.1.1.1 vsx-sync-exclude |     |
| ------------------- | --- | -------- | ------------------------ | --- |
switch#
| role {primary |     | | secondary} |     |     |
| ------------- | --- | ------------ | --- | --- |
Syntax
| role {primary | | secondary} |     |     |     |
| ------------- | ------------ | --- | --- | --- |
no role
Description
ConfigurestheVSXdevicerole.
ThenoformofthiscommandremovesthedeviceroleoftheswitchinVSXandcausestheinterswitchlinkto
beout-of-sync.
Commandcontext
config-vsx
Parameters
| {primary | secondary} |     |     |     |     |
| --------------------- | --- | --- | --- | --- |
SelectstheVSXroletoeitherprimaryorsecondaryforthedevice.
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 123

Authority

Administrators or local user group members with execution rights for this command.

Usage

VSX has no default role defined for the device. The device role assigns the device as the primary or
secondary for VSX synchronization. For ISL to be in-sync, one device in VSX must be configured as the
primary and the other device must be configured as the secondary.

Examples

Setting the VSX role to primary:

switch(config)# vsx
switch(config-vsx)# role primary

Removing the device role:

switch(config)# vsx
switch(config-vsx)# no role

show active-gateway

Syntax

show active-gateway [vsx-peer]

Description

Displays the gateway information configured on SVIs, such as:

n Number of active-gateway interface VLANs

n Number of IPv4 active-gateway interface VLANs

n Number of IPv6 active-gateway interface VLANs

n Per virtual MAC address

o IPv4 reference count and its interface VLANs

o IPv6 reference count and its interface VLANs

Command context

Operator (>) or Manager (#)

Parameters

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

VSX commands | 124

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
| IPv6                   | interface VLANs        | : none                |       |       |
| VMAC 00:00:00:01:01:14 |                        | :                     |       |       |
| IPv4                   | ref count              | : 32                  |       |       |
| IPv4                   | interface VLANs        | : vlan128-159         |       |       |
| IPv6                   | ref count              | : 0                   |       |       |
| IPv6                   | interface VLANs        | : none                |       |       |
| VMAC 00:00:00:01:01:10 |                        | :                     |       |       |
| IPv4                   | ref count              | : 31                  |       |       |
| IPv4                   | interface VLANs        | : vlan1-31            |       |       |
| IPv6                   | ref count              | : 0                   |       |       |
| IPv6                   | interface VLANs        | : none                |       |       |
| VMAC 00:00:00:01:01:15 |                        | :                     |       |       |
| IPv4                   | ref count              | : 32                  |       |       |
| IPv4                   | interface VLANs        | : vlan160-191         |       |       |
| IPv6                   | ref count              | : 0                   |       |       |
| IPv6                   | interface VLANs        | : none                |       |       |
| VMAC 00:00:00:03:00:12 |                        | :                     |       |       |
| IPv4                   | ref count              | : 1                   |       |       |
| IPv4                   | interface VLANs        | : vlan2000            |       |       |
| IPv6                   | ref count              | : 1                   |       |       |
| IPv6                   | interface VLANs        | : vlan4000            |       |       |
| VMAC 00:00:00:01:01:19 |                        | :                     |       |       |
| IPv4                   | ref count              | : 1                   |       |       |
| IPv4                   | interface VLANs        | : vlan4000            |       |       |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 125

| IPv6                | ref count | : 0          |     |
| ------------------- | --------- | ------------ | --- |
| IPv6                | interface | VLANs : none |     |
| show active-gateway |           | <IFNAME>     |     |
Syntax
| show active-gateway | <IFNAME> | [vsx-peer] |     |
| ------------------- | -------- | ---------- | --- |
Description
DisplaysthegatewayinformationperSVI,suchas:
n Active-GatewayIPV4anditsMACaddress
n Active-GatewayIPV6anditsMACaddress
Commandcontext
Operator(>)orManager(#)
Parameters
<IFNAME>
SpecifiestheVSXinterfacename.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
| switch#        | show active-gateway | vlan2000    |                     |
| -------------- | ------------------- | ----------- | ------------------- |
| Active-gateway | IPv4                | MAC address | : 00:00:00:01:01:18 |
| Active-gateway | IPv4                | address     |                     |
173.6.1.10
173.7.1.10
| Active-gateway | IPv6 | MAC address | : 00:00:00:03:00:12 |
| -------------- | ---- | ----------- | ------------------- |
| Active-gateway | IPv6 | address     |                     |
173::2
173::3
| show interface |     | <VLAN-NAME> |     |
| -------------- | --- | ----------- | --- |
Syntax
| show interface | <VLAN-NAME> | [vsx-peer] |     |
| -------------- | ----------- | ---------- | --- |
Description
DisplaysavirtualIPv4/IPv6andMACconfiguredforactive-activerouting.
VSXcommands|126

Commandcontext
Operator(>)orManager(#)
Parameters
<VLAN-NAME>
SpecifiestheVLANname.Syntax:string
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#    | show           | interface      | vlan100        |                   |                   |     |       |
| ---------- | -------------- | -------------- | -------------- | ----------------- | ----------------- | --- | ----- |
| Interface  |                | vlan100        | is up          |                   |                   |     |       |
| Admin      | state          | is up          |                |                   |                   |     |       |
| Hardware:  |                | Ethernet,      | MAC Address:   |                   | 48:0f:cf:af:c1:9e |     |       |
| IPv4       | address        | 192.168.1.1/24 |                |                   |                   |     |       |
| IPv4       | address        | 192.168.2.1/24 |                | secondary         |                   |     |       |
|            | active-gateway |                | ip mac         | 00:00:00:00:00:01 |                   |     |       |
|            | active-gateway |                | ip 192.168.1.1 |                   |                   |     |       |
|            | active-gateway |                | ip 192.168.2.2 |                   |                   |     |       |
|            | active-gateway |                | ipv6 mac       | 00:00:00:00:00:01 |                   |     |       |
|            | active-gateway |                | ipv6 fe80::1   |                   |                   |     |       |
| Statistics |                |                |                |                   | RX                | TX  | Total |
------------- -------------------- -------------------- --------------------
| L3   | Packets |            |     |     | 8   | 2   | 10  |
| ---- | ------- | ---------- | --- | --- | --- | --- | --- |
| L3   | Bytes   |            |     |     | 812 | 80  | 892 |
| show | lacp    | aggregates |     |     |     |     |     |
Syntax
| show lacp | aggregates |     | [<LAG-NAME>] |     | [vsx-peer] |     |     |
| --------- | ---------- | --- | ------------ | --- | ---------- | --- | --- |
Description
DisplaysaspecifiedLAGorallconfiguredLAGsalongwithVSXLAGs.
Commandcontext
Operator(>)orManager(#)
Parameters
<LAG-NAME>
SpecifiestheLAGname.Optional.Syntax:string
[vsx-peer]
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 127

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
DisplayingallconfiguredLAGsalongwithVSXLAGs:
| switch#    | show       | lacp aggregates |                 |
| ---------- | ---------- | --------------- | --------------- |
| Aggregate  |            | name : lag100   | (multi-chassis) |
| Interfaces |            | : 1/1/44        |                 |
| Peer       | interfaces | : 1/1/44        |                 |
| Heartbeat  |            | rate : Slow     |                 |
| Hash       |            | : l3-src-dst    |                 |
| Aggregate  |            | mode : Active   |                 |
DisplayingaspecifiedLAG:
| switch#    | show       | lacp aggregates | lag100          |
| ---------- | ---------- | --------------- | --------------- |
| Aggregate  |            | name : lag100   | (multi-chassis) |
| Interfaces |            | : 1/1/44        |                 |
| Peer       | interfaces | : 1/1/44        |                 |
| Heartbeat  |            | rate : Slow     |                 |
| Hash       |            | : l3-src-dst    |                 |
| Aggregate  |            | mode : Active   |                 |
| show       | lacp       | interfaces      |                 |
Syntax
| show lacp | interfaces | [<IFNAME>] | [vsx-peer] |
| --------- | ---------- | ---------- | ---------- |
Description
DisplaysanLACPconfigurationofthephysicalinterfaces,includingVSXs.Ifaninterfacenameispassedas
argument,itonlydisplaysanLACPconfigurationofaspecifiedinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
<IFNAME>
Optional:Specifiesaninterfacename.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
VSXcommands|128

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ThisexampledisplaysanLACPconfigurationofthephysicalinterfaces.Oneoftheinterfaceshasthelacp-
blockforwardingstate.IfaVSXswitchhasloopprotectenabledonaninterfaceandaloopoccurs,VSX
blockstheinterfacetostoptheloop.Theforwardingstateoftheblockedinterfaceissettolacp-block.
| switch# | show          | lacp interfaces |                |     |     |            |          |            |     |
| ------- | ------------- | --------------- | -------------- | --- | --- | ---------- | -------- | ---------- | --- |
| State   | abbreviations |                 | :              |     |     |            |          |            |     |
| A -     | Active        | P               | - Passive      |     | F - | Aggregable | I -      | Individual |     |
| S -     | Short-timeout | L               | - Long-timeout |     | N - | InSync     | O -      | OutofSync  |     |
| C -     | Collecting    | D               | - Distributing |     |     |            |          |            |     |
| X -     | State m/c     | expired         |                |     | E - | Default    | neighbor | state      |     |
| Actor   | details       | of all          | interfaces:    |     |     |            |          |            |     |
------------------------------------------------------------------------------------
| Intf | Aggr | Port | Port | State | System-id |     |     | System | Aggr Forwarding |
| ---- | ---- | ---- | ---- | ----- | --------- | --- | --- | ------ | --------------- |
|      | name | id   | Pri  |       |           |     |     | Pri    | Key State       |
------------------------------------------------------------------------------------
| 1/1/1   | lag10   | 17  | 1               | ALFOE  | 70:72:cf:37:a3:5c |     |     | 20  | 10 lacp-block |
| ------- | ------- | --- | --------------- | ------ | ----------------- | --- | --- | --- | ------------- |
| 1/1/2   | lag128  | 69  | 1               | ALFNCD | 70:72:cf:37:a3:5c |     |     | 20  | 128 up        |
| 1/1/3   | lag128  | 14  | 1               | ALFNCD | 70:72:cf:37:a3:5c |     |     | 20  | 128 up        |
| 1/1/4   | lag128  |     |                 |        |                   |     |     |     | down          |
| 1/1/5   | lag20   |     |                 |        |                   |     |     |     | up            |
| Partner | details | of  | all interfaces: |        |                   |     |     |     |               |
------------------------------------------------------------------------------
| Intf | Aggr | Partner | Port |     | State | System-id |     | System   | Aggr |
| ---- | ---- | ------- | ---- | --- | ----- | --------- | --- | -------- | ---- |
|      | name | Port-id | Pri  |     |       |           |     | Priority | Key  |
------------------------------------------------------------------------------
| 1/1/1 | lag10  | 0   | 65534 |     | PLFOEX | 00:00:00:00:00:00 |     | 65534 | 0   |
| ----- | ------ | --- | ----- | --- | ------ | ----------------- | --- | ----- | --- |
| 1/1/2 | lag128 | 69  | 1     |     | PLFNCD | 70:72:cf:8c:60:a7 |     | 65534 | 128 |
| 1/1/3 | lag128 | 14  | 1     |     | PLFNCD | 70:72:cf:8c:60:a7 |     | 65534 | 128 |
1/1/4 lag128
1/1/5 lag20
DisplayingstaticLAG:
| switch# | show          | lacp interfaces |                |     |     |            |          |            |     |
| ------- | ------------- | --------------- | -------------- | --- | --- | ---------- | -------- | ---------- | --- |
| State   | abbreviations |                 | :              |     |     |            |          |            |     |
| A -     | Active        | P               | - Passive      |     | F - | Aggregable | I -      | Individual |     |
| S -     | Short-timeout | L               | - Long-timeout |     | N - | InSync     | O -      | OutofSync  |     |
| C -     | Collecting    | D               | - Distributing |     |     |            |          |            |     |
| X -     | State m/c     | expired         |                |     | E - | Default    | neighbor | state      |     |
| Actor   | details       | of all          | interfaces:    |     |     |            |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port | State | System-id |     |     | System Aggr | Forwarding |
| ---- | ---- | ---- | ---- | ----- | --------- | --- | --- | ----------- | ---------- |
|      | Name | Id   | Pri  |       |           |     |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/1   | lag10   |     |                 |     |     |     |     |     | up  |
| ------- | ------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| 1/1/2   | lag10   |     |                 |     |     |     |     |     | up  |
| Partner | details | of  | all interfaces: |     |     |     |     |     |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port | State | System-id |     |     | System Aggr |     |
| ---- | ---- | ---- | ---- | ----- | --------- | --- | --- | ----------- | --- |
|      | Name | Id   | Pri  |       |           |     |     | Pri Key     |     |
------------------------------------------------------------------------------
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 129

1/1/1 lag10
1/1/2 lag10
DisplayinganLACPconfigurationofthe1/1/1interface:
| switch#           | show lacp     | interfaces       | 1/1/1 |              |                |     |
| ----------------- | ------------- | ---------------- | ----- | ------------ | -------------- | --- |
| State             | abbreviations | :                |       |              |                |     |
| A - Active        |               | P - Passive      | F     | - Aggregable | I - Individual |     |
| S - Short-timeout |               | L - Long-timeout | N     | - InSync     | O - OutofSync  |     |
| C - Collecting    |               | D - Distributing |       |              |                |     |
| X - State         | m/c expired   |                  | E     | - Default    | neighbor state |     |
| Aggregate-name    |               | : lag1           |       |              |                |     |
-------------------------------------------------
|     |     | Actor |     | Partner |     |     |
| --- | --- | ----- | --- | ------- | --- | --- |
-------------------------------------------------
| Port-id         |     | | 28                |     | | 31                |     |     |
| --------------- | --- | ------------------- | --- | ------------------- | --- | --- |
| Port-priority   |     | | 1                 |     | | 1                 |     |     |
| Key             |     | | 1                 |     | | 1                 |     |     |
| State           |     | | ALFNCD            |     | | ALFNCD            |     |     |
| System-id       |     | | 98:f2:b3:68:40:a0 |     | | 98:f2:b3:68:60:a6 |     |     |
| System-priority |     | | 65534             |     | | 65534             |     |     |
DisplayinganLACPconfigurationafterloop-protectisenabledontheprimaryVSXswitch:
| switch#           | show lacp     | interfaces       |     |              |                |     |
| ----------------- | ------------- | ---------------- | --- | ------------ | -------------- | --- |
| State             | abbreviations | :                |     |              |                |     |
| A - Active        |               | P - Passive      | F   | - Aggregable | I - Individual |     |
| S - Short-timeout |               | L - Long-timeout | N   | - InSync     | O - OutofSync  |     |
| C - Collecting    |               | D - Distributing |     |              |                |     |
| X - State         | m/c expired   |                  | E   | - Default    | neighbor state |     |
| Actor             | details of    | all interfaces:  |     |              |                |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID | System Aggr | Forwarding |
| ---- | ---- | --------- | ----- | --------- | ----------- | ---------- |
|      | Name | Id Pri    |       |           | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/4/14  | lag1(mc) | 206 1              | ALFNCD | f8:60:f0:06:49:00 | 65534 1 | up   |
| ------- | -------- | ------------------ | ------ | ----------------- | ------- | ---- |
| 1/5/15  | lag2(mc) |                    |        |                   |         | down |
| Partner | details  | of all interfaces: |        |                   |         |      |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID | System Aggr |     |
| ---- | ---- | --------- | ----- | --------- | ----------- | --- |
|      | Name | Id Pri    |       |           | Pri Key     |     |
------------------------------------------------------------------------------
| 1/4/14 | lag1(mc) | 130 1 | ALFNCD | f8:60:f0:06:87:00 | 65534 1 |     |
| ------ | -------- | ----- | ------ | ----------------- | ------- | --- |
| 1/5/15 | lag2(mc) |       |        |                   |         |     |
DisplayinganLACPconfigurationafterloop-protectisenabledonthesecondaryVSXswitch:
switch#
|       | show lacp     | interfaces |     |     |     |     |
| ----- | ------------- | ---------- | --- | --- | --- | --- |
| State | abbreviations | :          |     |     |     |     |
VSXcommands|130

| A -   | Active        | P - Passive        | F - | Aggregable | I -      | Individual |     |
| ----- | ------------- | ------------------ | --- | ---------- | -------- | ---------- | --- |
| S -   | Short-timeout | L - Long-timeout   | N - | InSync     | O -      | OutofSync  |     |
| C -   | Collecting    | D - Distributing   |     |            |          |            |     |
| X -   | State         | m/c expired        | E - | Default    | neighbor | state      |     |
| Actor | details       | of all interfaces: |     |            |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --------- | ----- | --------- | --- | ----------- | ---------- |
|      | Name | Id Pri    |       |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/3/2   | lag1(mc) | 1130 1             | ALFNCD | f8:60:f0:06:49:00 |     | 65534 1 | up   |
| ------- | -------- | ------------------ | ------ | ----------------- | --- | ------- | ---- |
| 1/9/3   | lag2(mc) |                    |        |                   |     |         | down |
| Partner | details  | of all interfaces: |        |                   |     |         |      |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID |     | System Aggr |     |
| ---- | ---- | --------- | ----- | --------- | --- | ----------- | --- |
|      | Name | Id Pri    |       |           |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/3/2 | lag1(mc) | 131 1      | ALFNCD        | f8:60:f0:06:87:00 |     | 65534 1 |     |
| ----- | -------- | ---------- | ------------- | ----------------- | --- | ------- | --- |
| 1/9/3 | lag2(mc) |            |               |                   |     |         |     |
| show  | lacp     | interfaces | multi-chassis |                   |     |         |     |
Syntax
| show lacp | interfaces | multi-chassis | [<IFNAME>] | [vsx-peer] |     |     |     |
| --------- | ---------- | ------------- | ---------- | ---------- | --- | --- | --- |
Description
ShowsallconfiguredVSXremoteinterfacedetails.TheinterfacethathastheALFNCDstatushasbeen
syncedwiththepartnerandisreadyforflowdistribution.
Commandcontext
Operator(>)orManager(#)
Parameters
<IFNAME>
SpecifiestheVSXinterfacename.Optional.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
| switch# | show          | lacp interfaces  | multi-chassis |            |     |            |     |
| ------- | ------------- | ---------------- | ------------- | ---------- | --- | ---------- | --- |
| State   | abbreviations | :                |               |            |     |            |     |
| A -     | Active        | P - Passive      | F -           | Aggregable | I - | Individual |     |
| S -     | Short-timeout | L - Long-timeout | N -           | InSync     | O - | OutofSync  |     |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 131

| C - Collecting |         |             | D -    | Distributing |             |                |     |
| -------------- | ------- | ----------- | ------ | ------------ | ----------- | -------------- | --- |
| X - State      |         | m/c expired |        |              | E - Default | neighbor state |     |
| Actor          | details |             | of all | interfaces:  |             |                |     |
------------------------------------------------------------------------------
| Intf | Aggregate |     | Port | Port     | State | System-ID | System Aggr  |
| ---- | --------- | --- | ---- | -------- | ----- | --------- | ------------ |
|      | name      |     | id   | Priority |       |           | Priority Key |
------------------------------------------------------------------------------
| 1/1/2   | lag100(mc) |     | 2      | 1           | ALFNCD | 08:00:09:13:06:7c | 65534 100 |
| ------- | ---------- | --- | ------ | ----------- | ------ | ----------------- | --------- |
| Partner | details    |     | of all | interfaces: |        |                   |           |
------------------------------------------------------------------------------
| Intf | Aggregate |     | Partner | Port     | State | System-ID | System Aggr  |
| ---- | --------- | --- | ------- | -------- | ----- | --------- | ------------ |
|      | name      |     | Port-id | Priority |       |           | Priority Key |
------------------------------------------------------------------------------
| 1/1/2  | lag100(mc) |         | 2   | 1                  | ALFNCD | 08:00:09:05:24:f6 | 65534 10 |
| ------ | ---------- | ------- | --- | ------------------ | ------ | ----------------- | -------- |
| Remote | Actor      | details |     | of all interfaces: |        |                   |          |
------------------------------------------------------------------------------
| Intf | Aggregate |     | Port | Port     | State System-ID |     | System Aggr  |
| ---- | --------- | --- | ---- | -------- | --------------- | --- | ------------ |
|      | name      |     | id   | Priority |                 |     | Priority Key |
------------------------------------------------------------------------------
| 1/1/2  | lag100(mc) |     | 1002    | 1                  | ALFNCD 08:00:09:13:06:7c |     | 65534 100 |
| ------ | ---------- | --- | ------- | ------------------ | ------------------------ | --- | --------- |
| Remote | Partner    |     | details | of all interfaces: |                          |     |           |
------------------------------------------------------------------------------
| Intf | Aggregate |     | Partner | Port     | State System-ID |     | System Aggr  |
| ---- | --------- | --- | ------- | -------- | --------------- | --- | ------------ |
|      | name      |     | Port-id | Priority |                 |     | Priority Key |
------------------------------------------------------------------------------
| 1/1/2 | lag100(mc)     |     | 3   | 1         | ALFNCD 08:00:09:05:24:f6 |     | 65534 10 |
| ----- | -------------- | --- | --- | --------- | ------------------------ | --- | -------- |
| show  | running-config |     |     | interface |                          |     |          |
Syntax
| show running-config |     |     | interface |     |     |     |     |
| ------------------- | --- | --- | --------- | --- | --- | --- | --- |
Description
Displaysallconfiguredinterfacecommands,includingVSXcommands.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#   | show | running-config |               | interface |     |     |     |
| --------- | ---- | -------------- | ------------- | --------- | --- | --- | --- |
| interface |      | lag 100        | multi-chassis |           |     |     |     |
no shutdown
no routing
VSXcommands|132

| lacp mode | active |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
| interface | 1/1/1  |     |     |     |     |
no shutdown
no routing
| interface | 1/1/2 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
| lag 100   |       |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
| interface | 1/1/3 |     |     |     |     |
no shutdown
| ip address | 192.168.1.2/24 |     |     |     |     |
| ---------- | -------------- | --- | --- | --- | --- |
| interface  | vlan100        |     |     |     |     |
no shutdown
| ip address          | 192.168.1.1/24 |                  |     |                       |                   |
| ------------------- | -------------- | ---------------- | --- | --------------------- | ----------------- |
| active-gateway      |                | ip 192.168.1.253 |     | mac                   | 00:00:00:00:00:01 |
| active-gateway      |                | ipv6 fe80::01    |     | mac 00:00:00:01:00:01 |                   |
| show running-config |                |                  | vsx |                       |                   |
Syntax
| show running-config |     | vsx |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
Description
DisplaystheconfiguredVSXcommands.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# show | running-config |     | vsx |     |     |
| ------------ | -------------- | --- | --- | --- | --- |
vsx
| system-mac        | 10:00:00:00:00:01 |                      |        |             |     |
| ----------------- | ----------------- | -------------------- | ------ | ----------- | --- |
| inter-switch-link |                   | hello-interval       |        | 2           |     |
| inter-switch-link |                   | dead-interval        |        | 3           |     |
| inter-switch-link |                   | hold-time            | 3      |             |     |
| inter-switch-link |                   | peer-detect-interval |        |             | 300 |
| role primary      |                   |                      |        |             |     |
| keepalive         | udp-port          | 1500                 |        |             |     |
| keepalive         | hello-interval    |                      | 2      |             |     |
| keepalive         | dead-interval     |                      | 4      |             |     |
| keepalive         | peer              | 192.168.1.1          | source | 192.168.1.2 |     |
| inter-switch-link |                   | 1/1/43               |        |             |     |
| interface         | lag 100           | multi-chassis        |        |             |     |
no shutdown
no routing
| vlan access | 1      |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- |
| lacp mode   | active |     |     |     |     |
| interface   | 1/1/44 |     |     |     |     |
no shutdown
lag 100
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 133

| show running-config |     | vsx-sync |     |
| ------------------- | --- | -------- | --- |
Syntax
| show running-config | vsx-sync |     |     |
| ------------------- | -------- | --- | --- |
Description
Displaysthelinesofrunning-configurationthatVSXconfigurationsynchronizationisenabledon.The
commandalsoprovidesarolled-upviewofconfigurationexpectedtobesynced.Thiscommandcanberun
fromtheprimaryorsecondarypeer.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
DisplayingtherunningconfigurationonwhichVSXsynchronizationisenabled:
| switch# show     | running-config | vsx-sync |     |
| ---------------- | -------------- | -------- | --- |
| Current vsx-sync | configuration: |          |     |
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
| show running-config |     | vsx-sync | peer-diff |
| ------------------- | --- | -------- | --------- |
Syntax
| show running-config | vsx-sync | peer-diff |     |
| ------------------- | -------- | --------- | --- |
Description
DisplaysthedifferencebetweentheconfigurationoffeaturesenabledforVSXsynchronizationonthe
primaryandsecondaryswitches.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
VSXcommands|134

Use this command for diagnosing errors. This command provides visibility into which configuration lines did
not synchronize from the primary peer to the secondary peer. This command can be run from the primary
or secondary peer. The output is displayed in the GNU diff unified format.

Example

Displaying the running configuration on which VSX synchronization is enabled:

switch# show running-config vsx-sync peer-diff
--- /tmp/running-config-vsx.83e 2018-05-01 17:03:38.083281976 +0000
+++ /tmp/peer-running-config-vsx.83e
@@ -1,4 +0,0 @@
-access-list ip sync
-
-
-

vsx-sync
!
10 permit any any any

2018-05-01 17:03:38.077281976 +0000

show vsx active-forwarding

Syntax

show vsx active-forwarding [interface <INTERFACE-VLAN>] [vsx-peer]

Description

Shows all the VSX active-forwarding configured interface VLANs or the VSX active-forwarding peer
information for a particular interface VLAN.

Command context

Operator (>) or Manager (#)

Parameters

interface <INTERFACE-VLAN>

Specifies the interface VLAN name. Syntax: string

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Displaying a list of VSX active-forwarding enabled interfaces:

switch# show vsx active-forwarding
List of VSX active-forwarding enabled interfaces:
vlan30
vlan32
vlan33

Displaying the VSX active-forwarding peer information for vlan30:

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

135

| switch#   | show vsx active-forwarding |                       | interface | vlan30   |
| --------- | -------------------------- | --------------------- | --------- | -------- |
| Interface | vlan30 has                 | VSX active-forwarding |           | enabled. |
| Interface | vlan30 Peer                | Data:                 |           |          |
| Peer MAC: | 94:f1:28:21:22:00          |                       |           |          |
| Peer IPv6 | Addresses:                 |                       |           |          |
fe80::96f1:28ff:fe21:2200
| show vsx | brief |     |     |     |
| -------- | ----- | --- | --- | --- |
Syntax
| show vsx brief | [vsx-peer] |     |     |     |
| -------------- | ---------- | --- | --- | --- |
Description
DisplaysthebriefVSXstatus.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
Theshow vsx briefcommanddisplaystheISLPdeviceprotocolstatesunderthe"DeviceState"heading.
Table 5: ISLPdeviceprotocolstates
Device
Definition
state
| Peer- | TheVSXswitchisinasteadystate.VSXLAGsareup. |     |     |     |
| ----- | ------------------------------------------ | --- | --- | --- |
Established
Sync- ISLconnectivitytothepeerVSXswitchisrestored,andtheVSXswitchissyncingstatestothepeer
| Primary | VSXswitch.VSXLAGsareup. |     |     |     |
| ------- | ----------------------- | --- | --- | --- |
Sync- ISLconnectivitytothepeerVSXswitchisrestored,andtheVSXswitchislearningstatesfromthe
| Secondary | peerVSXswitch.VSXLAGsaredown. |     |     |     |
| --------- | ----------------------------- | --- | --- | --- |
Sync- TheVSXswitchhaslearneditsstatesfromthepeerVSXswitch,andtheVSXswitchismonitoring
| Secondary- | forhardwaretobeprogrammed.VSXLAGsaredown. |     |     |     |
| ---------- | ----------------------------------------- | --- | --- | --- |
Linkup-
Delay
VSXcommands|136

Device
Definition
state
Split- TheVSXswitchhaslostISLconnectivitytothepeerVSXswitch.TheVSXswitchisoperatingasthe
| System- | primaryVSXswitch.VSXLAGsareup. |     |     |
| ------- | ------------------------------ | --- | --- |
Primary
Split- TheVSXswitchhaslostISLconnectivitytothepeerVSXswitch.TheVSXswitchisoperatingasthe
| System- | secondaryVSXswitch.VSXLAGsaredown. |     |     |
| ------- | ---------------------------------- | --- | --- |
Secondary
| Waiting- | TheVSXswitchiswaitingforconnectivitytothepeerVSXswitch. |     |     |
| -------- | ------------------------------------------------------- | --- | --- |
For-Peer
Example
DisplayingthebriefVSXstatusfortheswitchyouareloggedinto:
| vsx-primary# | show vsx         | brief          |                         |
| ------------ | ---------------- | -------------- | ----------------------- |
| ISL State    |                  |                | : In-Sync               |
| Device       | State            |                | : Peer-Established      |
| Keepalive    | State            |                | : Keepalive-Established |
| Device       | Role             |                | : primary               |
| Number       | of Multi-chassis | LAG interfaces | : 2                     |
DisplayingthebriefVSXstatusforthepeer(secondary)switchwhileenteringthecommandontheprimary
switch:
| vsx-primary# | show vsx         | brief vsx-peer |                         |
| ------------ | ---------------- | -------------- | ----------------------- |
| ISL State    |                  |                | : In-Sync               |
| Device       | State            |                | : Peer-Established      |
| Keepalive    | State            |                | : Keepalive-Established |
| Device       | Role             |                | : secondary             |
| Number       | of Multi-chassis | LAG interfaces | : 2                     |
DisplayingthebriefVSXstatusforthepeer(primary)switchwhileenteringthecommandonthesecondary
switch:
| vsx-secondary# | show vsx           | brief vsx-peer |                         |
| -------------- | ------------------ | -------------- | ----------------------- |
| ISL State      |                    |                | : In-Sync               |
| Device         | State              |                | : Peer-Established      |
| Keepalive      | State              |                | : Keepalive-Established |
| Device         | Role               |                | : primary               |
| Number         | of Multi-chassis   | LAG interfaces | : 2                     |
| show vsx       | config-consistency |                |                         |
Syntax
| show vsx config-consistency |     | [vsx-peer] |     |
| --------------------------- | --- | ---------- | --- |
Description
DisplaystheVSXglobalconfigurationconsistencybetweentwoVSXswitches.
Commandcontext
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 137

Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ThefollowingexampleshowsacomparisonbetweenthetwoVSXswitches.
| switch#            | show vsx config-consistency |     |                 |        |
| ------------------ | --------------------------- | --- | --------------- | ------ |
| Configurations     |                             |     | Local           | Peer   |
| ------------------ |                             |     | ------          | ------ |
| Software           | Version                     |     | XL.10.0x.xxxxAE |        |
XL.10.0x.xxxxAE
| System | MAC |     | 94:f1:28:ef:25:00 |     |
| ------ | --- | --- | ----------------- | --- |
f4:03:43:80:28:00
| System    | Profile        |     | Advanced | Advanced |
| --------- | -------------- | --- | -------- | -------- |
| ISL hello | interval       |     | 1        | 1        |
| ISL dead  | interval       |     | 20       | 20       |
| ISL hold  | interval       |     | 0        | 0        |
| Keepalive | hello interval |     | 1        | 1        |
| Keepalive | dead interval  |     | 3        | 3        |
| Keepalive | UDP port       |     | 7678     | 7678     |
| VSX VLAN  | List           |     |          |          |
-------------
| Local ISL  | VLANs :    | 1,100 |     |     |
| ---------- | ---------- | ----- | --- | --- |
| Peer ISL   | VLANs :    | 1,10  |     |     |
| VSX Active | Forwarding |       |     |     |
---------------------
| Interface      | VLANs              | : 2, 5-9  |      |     |
| -------------- | ------------------ | --------- | ---- | --- |
| Peer Interface | VLANs              | : 2, 5-10 |      |     |
| show vsx       | config-consistency |           | lacp |     |
Syntax
| show vsx config-consistency |     | lacp [<LAG-NAME>] | [vsx-peer] |     |
| --------------------------- | --- | ----------------- | ---------- | --- |
Description
DisplaysVSXLACPconfigurationconsistencybetweentwoVSXswitches.
Commandcontext
Operator(>)orManager(#)
Parameters
<LAG-NAME>
VSXcommands|138

SpecifiestheLAGname.Optional.Syntax:string
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# show       | vsx config-consistency | lacp            |                 |
| ------------------ | ---------------------- | --------------- | --------------- |
| Configurations     |                        | Local           | Peer            |
| ------------------ |                        | ------          | ------          |
| Name               |                        | lag100          | lag100          |
| Loop protect       | enabled                | false           | true            |
| Hash scheme        |                        | l2-src-dst-hash | l2-src-dst-hash |
| Qos cos override   |                        | 0               | 0               |
| Qos dscp override  |                        | 0               | 0               |
Qos trust
| VSX VLAN list |     |     |     |
| ------------- | --- | --- | --- |
1
| Peer VSX VLAN | list |     |     |
| ------------- | ---- | --- | --- |
1,10
| STP link-type      |         | point-to-point  | point-to-point  |
| ------------------ | ------- | --------------- | --------------- |
| STP port-type      |         | admin-network   | admin-network   |
| STP bpdu-filter    |         | Disabled        | Disabled        |
| STP bpdu-guard     |         | Disabled        | Disabled        |
| STP loop-guard     |         | Disabled        | Disabled        |
| STP root-guard     |         | Disabled        | Disabled        |
| STP tcn-guard      |         | Disabled        | Disabled        |
| Configurations     |         | Local           | Peer            |
| ------------------ |         | ------          | ------          |
| Name               |         | lag111          | lag111          |
| Loop protect       | enabled | false           | false           |
| Hash scheme        |         | l2-src-dst-hash | l2-src-dst-hash |
| Qos cos override   |         | 0               | 0               |
| Qos dscp override  |         | 0               | 0               |
Qos trust
| VSX VLAN list |     |     |     |
| ------------- | --- | --- | --- |
1
| Peer VSX VLAN | list |     |     |
| ------------- | ---- | --- | --- |
1
| STP link-type   |     | point-to-point | point-to-point |
| --------------- | --- | -------------- | -------------- |
| STP port-type   |     | admin-network  | admin-network  |
| STP bpdu-filter |     | Disabled       | Disabled       |
| STP bpdu-guard  |     | Disabled       | Disabled       |
| STP loop-guard  |     | Disabled       | Disabled       |
| STP root-guard  |     | Disabled       | Disabled       |
| STP tcn-guard   |     | Disabled       | Disabled       |
------------------------------------------------------
| show vsx | configuration |     |     |
| -------- | ------------- | --- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 139

Syntax
show vsx configuration {inter-switch-link | keepalive} [vsx-peer]
Description
DisplaystheISLconfigurationorkeepaliveprotocolconfigurationinVSX.
Commandcontext
Operator(>)orManager(#)
Parameters
| {inter-switch-link | | keepalive} |     |     |
| ------------------ | ------------ | --- | --- |
Selectsinter-switch-linkorkeepalive.
inter-switch-link
DisplaystheISLconfigurationinVSX.
keepalive
DisplaysthekeepaliveprotocolconfigurationinVSX.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
DisplayingtheISLconfigurationinVSX:
| switch#        | show vsx configuration |                     | inter-switch-link |
| -------------- | ---------------------- | ------------------- | ----------------- |
| Inter Switch   | Link                   | : 1/1/43            |                   |
| Hello Interval |                        | : 1 Seconds         |                   |
| Dead Interval  |                        | : 20 Seconds        |                   |
| Hold Time      |                        | : 0 Seconds         |                   |
| Peer detect    | interval               | : 300 Seconds       |                   |
| System         | MAC                    | : 10:00:00:00:00:01 |                   |
| Device         | Role                   | : primary           |                   |
| Multichassis   | LAGs                   | : lag100            |                   |
DisplayingthekeepaliveprotocolconfigurationinVSX:
| switch#        | show vsx configuration |               | keepalive      |
| -------------- | ---------------------- | ------------- | -------------- |
| Keepalive      | Interface              | : 1/1/1       |                |
| Keepalive      | VRF                    | : test1       |                |
| Source         | IP Address             | : 192.168.1.1 |                |
| Peer IP        | Address                | : 192.168.1.2 |                |
| UDP Port       |                        | : 7678        |                |
| Hello Interval |                        | : 1           | Seconds        |
| Dead Interval  |                        | : 3           | Seconds        |
| show vsx       | configuration          |               | split-recovery |
Syntax
VSXcommands|140

show vsx configuration split-recovery [vsx-peer]

Description

Displays the state of the split recovery mode.

Command context

Operator (>) or Manager (#)

Parameters

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show vsx configuration split-recovery
Split Recovery Mode

: Enabled

show vsx ip data-path

Syntax

show vsx ip data-path [<IP-ADDR> | <IP-ADDR>/<MASK>] [vrf <VRF-NAME>] [vsx-peer]

Description

Displays the datapath of the IPv4 route present on local and VSX peer devices.

Command context

Operator (>) or Manager (#)

Parameters

<IP-ADDR> | <IP-ADDR>/<MASK>]

Selects one of the following: <IP-ADDR> or <IP-ADDR>/<MASK>
<IP-ADDR>

Specifies the datapath for an IPv4 address based on the parameters provided.

<IP-ADDR>/<MASK>

Specifies the datapath for an IPv4 address and its specified subnet. Optional. Syntax: A.B.C.D/M

vrf <VRF-NAME>

Shows the IPv4 datapath for a specified VRF.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

141

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
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
| switch#   | show | vsx ip data-path |     | 198.51.100.1     |
| --------- | ---- | ---------------- | --- | ---------------- |
| IPv4 Data | Path | Information      |     | For 198.51.100.1 |
Local Device
------------
| Route : | 198.51.100.1/32 |           |         |     |
| ------- | --------------- | --------- | ------- | --- |
| Egress  | L3              | Interface | : 1/1/4 |     |
Peer Device
------------
| Route :  | 198.51.100.0/24 |             |         |                     |
| -------- | --------------- | ----------- | ------- | ------------------- |
| Egress   | L3              | Interface   | : 1/1/2 |                     |
| Next     | Hop             | MAC Address |         | : 08:00:09:db:21:e8 |
| Egress   | Port            | : 1/1/2     |         |                     |
| show vsx | ip              | route       |         |                     |
Syntax
VSXcommands|142

show vsx ip route [<IP-ADDR> | <IP-ADDR>/<MASK> | unique] [vrf <VRF-NAME> | all-vrfs] [vsx-
peer]
Description
DisplaysaspecifiedLAGorallconfiguredLAGsalongwithVSXLAGs.
Commandcontext
Operator(>)orManager(#)
Parameters
| <IP-ADDR> | | <IP-ADDR>/<MASK> | | unique] |     |
| --------- | ------------------ | --------- | --- |
Selectsoneofthefollowing:<IP-ADDR>,<IP-ADDR>/<MASK>,orunique
<IP-ADDR>
SpecifiestherouteinformationforanIPv4addressbasedontheparametersprovided.
<IP-ADDR>/<MASK>
SpecifiestherouteinformationforanIPv4addressanditsspecifiedsubnet.Optional.Syntax:
A.B.C.D/M
unique
Specifiesroutesthatarepresentonlyontheprimaryswitchoronlyonthesecondaryswitch.Theroutes
thatarepresentonboththeprimaryandsecondaryswitchareexcluded.Optional.Syntaxstring.
| vrf <VRF-NAME> | | all-vrfs |     |     |
| -------------- | ---------- | --- | --- |
SelectstheVRFnameorallVRFs.
<VRF-NAME>
ShowstheIPv4routeinformationforaspecifiedVRF.
all-vrf
ShowstheIPv4routeinformationforallVRFs.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
DisplayingIPv4routesonaVSXswitch:
| switch#       | show vsx ip               | route         |         |
| ------------- | ------------------------- | ------------- | ------- |
| IPv4          | Forwarding Routes         |               |         |
| '[x/y]'       | denotes [distance/metric] |               |         |
| 192.0.2.0/32, | vrf                       | default       |         |
|               | via 192.0.2.1,            | [1/0], static | on vsx1 |
|               | via 192.0.2.2,            | [1/0], static | on vsx2 |
DisplayingIPv4routesonaVSXswitch:
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 143

| switch# show    | vsx ip            | route     |               |
| --------------- | ----------------- | --------- | ------------- |
| IPv4 Forwarding | Routes            |           |               |
| '[x/y]' denotes | [distance/metric] |           |               |
| 192.0.2.3/24,   | vrf               | default   |               |
| via 1/1/3,      | [0/0],            | connected | on vsx1       |
| via 192.0.2.2,  |                   | [110/2],  | ospf on vsx2  |
| 192.0.2.4/32,   | vrf               | default   |               |
| via 1/1/3,      | [0/0],            | local     | on vsx1       |
| 192.0.2.5/24,   | vrf               | default   |               |
| via 1/1/4,      | [0/0],            | connected | on vsx1       |
| via 192.0.2.2,  |                   | [110/3],  | ospf on vsx2  |
| 192.0.2.6/32,   | vrf               | default   |               |
| via 1/1/4,      | [0/0],            | local     | on vsx1       |
| 192.0.2.7/32,   | vrf               | default   |               |
| via 192.0.2.8,  |                   | [110/1],  | ospf on vsx1  |
| via 192.0.2.1,  |                   | [110/1],  | ospf on vsx1  |
| via loopback1,  |                   | [0/0],    | local on vsx2 |
DisplayingIPv4uniqueroutesonaVSXswitch:
| switch# show    | vsx ip            | route unique |                |
| --------------- | ----------------- | ------------ | -------------- |
| IPv4 Forwarding | Routes            |              |                |
| '[x/y]' denotes | [distance/metric] |              |                |
| 192.0.2.0/32,   | vrf               | default      |                |
| via 192.0.2.2,  |                   | [1/0],       | static on vsx2 |
| 192.0.2.9/32,   | vrf               | default      |                |
| via 192.0.2.1,  |                   | [1/0],       | static on vsx1 |
DisplayingIPv4routesonaVSXswitchfor192.0.2.10:
| switch# show    | vsx ip            | route 192.0.2.10 |                |
| --------------- | ----------------- | ---------------- | -------------- |
| IPv4 Forwarding | Routes            |                  |                |
| '[x/y]' denotes | [distance/metric] |                  |                |
| 192.0.2.10/32,  | vrf               | default          |                |
| via 192.0.2.1,  |                   | [1/0],           | static on vsx1 |
| via 192.0.2.2,  |                   | [1/0],           | static on vsx2 |
| show vsx        | ipv6              | data-path        |                |
Syntax
show vsx ipv6 data-path [<IPv6-ADDR> | <IPv6-ADDR>/<MASK>] [vrf <VRF-NAME>] [vsx-peer]
Description
DisplaysthedatapathoftheIPv6routeonlocalandpeerVSXdevices.
Commandcontext
Operator(>)orManager(#)
VSXcommands|144

Parameters
| <IPV6-ADDR> | | <IPV6-ADDR>/<MASK>] |     |     |     |
| ----------- | --------------------- | --- | --- | --- |
Selectsoneofthefollowing:<IPV6-ADDR>or<IPV6-ADDR>/<MASK>
<IPV6-ADDR>
SpecifiesthedatapathforanIPv6addressbasedontheparametersprovided.
<IPV6-ADDR>/<MASK>
SpecifiesthedatapathforanIPv6addressanditsspecifiedsubnet.Optional.Syntax:A.B.C.D/M
vrf <VRF-NAME>
ShowstheIPv6datapathforaspecifiedVRF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
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
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 145

------------
| Route | :      | 3000::/64 |           |     |                     |     |
| ----- | ------ | --------- | --------- | --- | ------------------- | --- |
|       | Egress | L3        | Interface | :   | 1/1/2               |     |
|       | Next   | Hop MAC   | Address   |     | : 08:00:09:0e:0c:1b |     |
|       | Egress | Port      | : 1/1/2   |     |                     |     |
| show  | vsx    | ipv6      | route     |     |                     |     |
Syntax
| show | vsx ipv6        | route | [<IPv6-ADDR> |     | | <IPv6-ADDR>/<MASK> | | unique] |
| ---- | --------------- | ----- | ------------ | --- | -------------------- | --------- |
|      | [vrf <VRF-NAME> |       | | all-vrfs]  |     | [vsx-peer]           |           |
Description
DisplaysaspecifiedLAGorallconfiguredLAGsalongwithVSXLAGs.
Commandcontext
Operator(>)orManager(#)
Parameters
| <IPV6-ADDR> |     | | <IPV6-ADDR>/<MASK> |     |     | | unique] |     |
| ----------- | --- | -------------------- | --- | --- | --------- | --- |
Selectsoneofthefollowing:<IPV6-ADDR>,<IPV6-ADDR>/<MASK>,orunique
<IPV6-ADDR>
SpecifiestherouteinformationforanIPv4addressbasedontheparametersprovided.
<IPV6-ADDR>/<MASK>
SpecifiestherouteinformationforanIPv4addressanditsspecifiedsubnet.Optional.Syntax:
A.B.C.D/M
unique
Specifiesroutesthatarepresentonlyontheprimaryswitchoronlyonthesecondaryswitch.The
routesthatarepresentonboththeprimaryandsecondaryswitchareexcluded.Optional.Syntax
string.
| vrf | <VRF-NAME> | |   | all-vrfs |     |     |     |
| --- | ---------- | --- | -------- | --- | --- | --- |
SelectstheVRFnameorallVRFs.
<VRF-NAME>
ShowstheIPv4routeinformationforaspecifiedVRF.
all-vrf
ShowstheIPv4routeinformationforallVRFs.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
DisplayingIPv6routesonaVSXswitch:
VSXcommands|146

| switch#      | show       | vsx         | ipv6 route        |           |         |
| ------------ | ---------- | ----------- | ----------------- | --------- | ------- |
| IPv6         | Forwarding |             | Routes            |           |         |
| '[x/y]'      | denotes    |             | [distance/metric] |           |         |
| 1000::/64,   |            | vrf default |                   |           |         |
|              | via 1/1/2, |             | [0/0],            | connected | on vsx1 |
|              | via 1/1/2, |             | [0/0],            | connected | on vsx2 |
| 1000::1/128, |            | vrf         | default           |           |         |
|              | via 1/1/2, |             | [0/0],            | local     | on vsx1 |
DisplayingIPv6uniqueroutesonaVSXswitch:
| switch#      | show         | vsx         | ipv6 route        | unique |         |
| ------------ | ------------ | ----------- | ----------------- | ------ | ------- |
| IPv6         | Forwarding   |             | Routes            |        |         |
| '[x/y]'      | denotes      |             | [distance/metric] |        |         |
| 1000::1/128, |              | vrf         | default           |        |         |
|              | via 1/1/2,   |             | [0/0],            | local  | on vsx1 |
| 1000::2/128, |              | vrf         | default           |        |         |
|              | via 1/1/2,   |             | [0/0],            | local  | on vsx2 |
| 3000::/64,   |              | vrf default |                   |        |         |
|              | via 1000::2, |             | [1/0],            | static | on vsx1 |
DisplayingIPv6routesonaVSXswitchfor2000::/64:
| switch#    | show         | vsx         | ipv6 route        | 2000::/64 |         |
| ---------- | ------------ | ----------- | ----------------- | --------- | ------- |
| IPv6       | Forwarding   |             | Routes            |           |         |
| '[x/y]'    | denotes      |             | [distance/metric] |           |         |
| 2000::/64, |              | vrf default |                   |           |         |
|            | via 1000::2, |             | [1/0],            | static    | on vsx1 |
|            | via 1000::1, |             | [1/0],            | static    | on vsx2 |
| show       | vsx          | status      |                   |           |         |
Syntax
show vsx status [inter-switch-link | keepalive | linkup-delay] [vsx-peer]
Description
DisplaysglobalVSXstatusoraspecifiedstatusdeterminedbytheselectedparameter.
Commandcontext
Operator(>)orManager(#)
Parameters
| [inter-switch-link |     |     | | keepalive | | linkup-delay] |     |
| ------------------ | --- | --- | ----------- | --------------- | --- |
Selectsoneofthefollowing:inter-switch-link,keepalive,orlinkup-delay
inter-switch-link
SpecifiesthedisplayoftheISLstatusinVSX.
keepalive
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 147

SpecifiesthedisplayoftheVSXkeepaliveprotocolstatus.
linkup-delay
SpecifiesthedisplayoftheVSXlink-updelayinformation,suchasthe:
n Configuredlink-updelaytimer.
n Delaytimerstatus.
n Initialsyncstatus.
n LAGsonwhichthedelaytimerisrunning.
StatusoftheLAGsexcludedfromthelink-updelaytimer.
n
InterfacesthatareshutdownduringVSXsplit.
n
n Timeremainingfortheinterfacestobebroughtup.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
DisplayingtheglobalVSXstatus:
switch#
show vsx status
| VSX Operational | State |     |     |
| --------------- | ----- | --- | --- |
---------------------
| ISL channel      |                   | : In-Sync        |                   |
| ---------------- | ----------------- | ---------------- | ----------------- |
| ISL mgmt         | channel           | : operational    |                   |
| Config Sync      | Status            | : in-sync        |                   |
| NAE              |                   | : peer_reachable |                   |
| HTTPS Server     |                   | : peer_reachable |                   |
| Attribute        | Local             |                  | Peer              |
| ------------     | --------          |                  | --------          |
| ISL link         | 1/1/43            |                  | 1/1/43            |
| ISL version      | 2                 |                  | 2                 |
| System MAC       | 48:0f:cf:af:70:84 |                  | 48:0f:cf:af:c2:84 |
| Platform         | 8320              |                  | 8320              |
| Software Version | 10.0x.xxxx        |                  | 10.0x.xxxx        |
| Device Role      | primary           |                  | secondary         |
DisplayingtheISLstatusinVSX:
switch#
| show         | vsx status      | inter-switch-link |     |
| ------------ | --------------- | ----------------- | --- |
| State        |                 | : In-Sync         |     |
| Link Status  |                 | : up              |     |
| Mgmt state   |                 | : operational     |     |
| Inter-switch | link Statistics |                   |     |
----------------------------
| Hello Packets | Tx  | : 4572 |     |
| ------------- | --- | ------ | --- |
| Hello Packets | Rx  | : 4573 |     |
VSXcommands|148

| Data Packets | Tx    | : 80634 |     |     |     |     |
| ------------ | ----- | ------- | --- | --- | --- | --- |
| Data Packets | Rx    | : 80637 |     |     |     |     |
| Mgmt Packets | Tx    | : 25946 |     |     |     |     |
| Mgmt Packets | Rx    | : 25167 |     |     |     |     |
| Mgmt Packet  | Drops | : 0     |     |     |     |     |
DisplayingtheVSXkeepaliveprotocolstatus:
| switch#          | show vsx status | keepalive               |            |      |     |     |
| ---------------- | --------------- | ----------------------- | ---------- | ---- | --- | --- |
| Keepalive        | State           | : Keepalive-Established |            |      |     |     |
| Last Established |                 | : Thu Jun               | 8 09:03:01 | 2018 |     |     |
| Last Failed      |                 | : Thu Jun               | 8 09:04:02 | 2018 |     |     |
| Peer System      | Id              | : 58:1f:cf:af:a0:84     |            |      |     |     |
| Peer Device      | Role            | : primary               |            |      |     |     |
| Keepalive        | Counters        |                         |            |      |     |     |
| Keepalive        | Packets Tx      | : 322                   |            |      |     |     |
| Keepalive        | Packets Rx      | : 121                   |            |      |     |     |
| Keepalive        | Timeouts        | : 0                     |            |      |     |     |
| Keepalive        | Packets Dropped | : 14                    |            |      |     |     |
DisplayingtheVSXlink-updelaystatuswhileARP/MACVSXsynchronizationisinprogress:
switch#
|             | show vsx status    | linkup-delay |     |     |                    |     |
| ----------- | ------------------ | ------------ | --- | --- | ------------------ | --- |
| Configured  | linkup delay-timer |              |     |     | : 180 seconds      |     |
| Initial     | sync status        |              |     |     | : In-progress      |     |
| Delay timer | status             |              |     |     | : Waiting-to-start |     |
| Linkup      | Delay time left    |              |     |     | :                  |     |
Interfaces that will be brought up after delay timer expires : lag20,lag30-lag31
| Interfaces | enabled for     | shutdown-on-split | that        | will be brought |        |     |
| ---------- | --------------- | ----------------- | ----------- | --------------- | ------ | --- |
| up after   | the delay timer | expires           |             |                 | :      |     |
| Interfaces | that are        | excluded from     | delay timer |                 | : lag2 |     |
DisplayingtheVSXlink-updelaystatuswithARP/MACVSXsynchronizationcompletedwiththedelaytimer
running:
| switch#     | show vsx status    | linkup-delay |     |     |               |            |
| ----------- | ------------------ | ------------ | --- | --- | ------------- | ---------- |
| Configured  | linkup delay-timer |              |     |     | : 180 seconds |            |
| Initial     | sync status        |              |     |     | : Completed   |            |
| Delay timer | status             |              |     |     | : Running     |            |
| Linkup      | Delay time left    |              |     |     | : 1 minutes   | 22 seconds |
Interfaces that will be brought up after delay timer expires : lag20,lag30-lag31
| Interfaces | enabled for     | shutdown-on-split | that        | will be brought |        |     |
| ---------- | --------------- | ----------------- | ----------- | --------------- | ------ | --- |
| up after   | the delay timer | expires           |             |                 | :      |     |
| Interfaces | that are        | excluded from     | delay timer |                 | : lag2 |     |
DisplayingtheVSXlink-updelaystatuswithARP/MACVSXsynchronizationcompletedandthedelaytimer
expired:
| switch#    | show vsx status    | linkup-delay |     |     |               |     |
| ---------- | ------------------ | ------------ | --- | --- | ------------- | --- |
| Configured | linkup delay-timer |              |     |     | : 180 seconds |     |
| Initial    | sync status        |              |     |     | : Completed   |     |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 149

|     | Delay timer  | status |      |     |     |     |     | : Completed |
| --- | ------------ | ------ | ---- | --- | --- | --- | --- | ----------- |
|     | Linkup Delay | time   | left |     |     |     |     | :           |
Interfaces that will be brought up after delay timer expires : lag2
|     | Interfaces | enabled   | for      | shutdown-on-split |            | that  | will be brought |     |
| --- | ---------- | --------- | -------- | ----------------- | ---------- | ----- | --------------- | --- |
|     | up after   | the delay | timer    | expires           |            |       |                 | :   |
|     | Interfaces | that are  | excluded |                   | from delay | timer |                 | :   |
DisplayingtheglobalVSXstatusforthepeerswitch:
|     | vsx-primary#    | show  | vsx | status | vsx-peer |     |     |     |
| --- | --------------- | ----- | --- | ------ | -------- | --- | --- | --- |
|     | VSX Operational | State |     |        |          |     |     |     |
---------------------
|     | ISL channel  |             |                   | : In-Sync        |     |                   |     |     |
| --- | ------------ | ----------- | ----------------- | ---------------- | --- | ----------------- | --- | --- |
|     | ISL mgmt     | channel     |                   | : operational    |     |                   |     |     |
|     | Config       | Sync Status |                   | : in-sync        |     |                   |     |     |
|     | NAE          |             |                   | : peer_reachable |     |                   |     |     |
|     | HTTPS        | Server      |                   | : peer_reachable |     |                   |     |     |
|     | Attribute    |             | Local             |                  |     | Peer              |     |     |
|     | ------------ |             | --------          |                  |     | --------          |     |     |
|     | ISL link     |             | lag1              |                  |     | lag1              |     |     |
|     | ISL version  |             | 2                 |                  |     | 2                 |     |     |
|     | System MAC   |             | e0:07:1b:cb:72:e4 |                  |     | 98:f2:b3:68:79:2e |     |     |
|     | Platform     |             | 8320              |                  |     | 8320              |     |     |
|     | Software     | Version     | 10.0x.xxxx        |                  |     | 10.0x.xxxx        |     |     |
|     | Device Role  |             | secondary         |                  |     | primary           |     |     |
Displayingthestatusforanout-of-syncstatusforVSX.
|     | switch#      | show vsx    | status      | linkup-delay      |            |       |                 |              |
| --- | ------------ | ----------- | ----------- | ----------------- | ---------- | ----- | --------------- | ------------ |
|     | Configured   | linkup      | delay-timer |                   |            |       |                 | : 20 seconds |
|     | Initial      | sync status |             |                   |            |       |                 | :            |
|     | Delay timer  | status      |             |                   |            |       |                 | :            |
|     | Linkup Delay | time        | left        |                   |            |       |                 | :            |
|     | Interfaces   | that will   | be          | brought           | up after   | delay | timer expires   | :            |
|     | Interfaces   | enabled     | for         | shutdown-on-split |            | that  | will be brought |              |
|     | up after     | the delay   | timer       | expires           |            |       |                 | :            |
|     | Interfaces   | that are    | excluded    |                   | from delay | timer |                 | :            |
DisplayingthestatusVSXlink-updelaystatuswheninterfacesenabledforshutdown-on-split.
|     | switch#      | show vsx    | status      | linkup-delay |     |     |     |                    |
| --- | ------------ | ----------- | ----------- | ------------ | --- | --- | --- | ------------------ |
|     | Configured   | linkup      | delay-timer |              |     |     |     | : 180 seconds      |
|     | Initial      | sync status |             |              |     |     |     | : In-progress      |
|     | Delay timer  | status      |             |              |     |     |     | : Waiting-to-start |
|     | Linkup Delay | time        | left        |              |     |     |     | :                  |
Interfaces that will be brought up after delay timer expires : lag8,lag256
|     | Interfaces | enabled   | for   | shutdown-on-split |     | that | will be brought |                  |
| --- | ---------- | --------- | ----- | ----------------- | --- | ---- | --------------- | ---------------- |
|     | up after   | the delay | timer | expires           |     |      |                 | : 1/1/27,1/1/37, |
vlan2-vlan57
|      | Interfaces | that are | excluded |             | from delay | timer |     | :   |
| ---- | ---------- | -------- | -------- | ----------- | ---------- | ----- | --- | --- |
| show | vsx        | status   |          | config-sync |            |       |     |     |
Syntax
VSXcommands|150

| show vsx status | config-sync | [vsx-peer] |     |     |
| --------------- | ----------- | ---------- | --- | --- |
Description
DisplaysVSXconfigurationsynchronizationstatusforpeers.Thiscommandcanberunfromtheprimaryor
secondarypeertoviewtheconfigurationsynchronizationstate.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
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
| show vsx | status | shutdown-on-split |     |     |
| -------- | ------ | ----------------- | --- | --- |
Syntax
| show vsx status | shutdown-on-split |     |     |     |
| --------------- | ----------------- | --- | --- | --- |
Description
DisplaysthestatusoftheinterfacesthatareshutdownduringaVSX split.
Youcanalsouseshow interfacecommandtoviewthestatusoftheinterface.Forexample,assumethatyou
haveshutdownthenon-vsxinterface1/1/2duringtheVSX split.Whenyouentershow interfacecommandon
thesecondaryswitch,theoutputfromthecommandindicatesthattheinterfacewasblockedbyVSX feature.
Commandcontext
Operator(>)orManager(#)
Authority
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 151

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Displaying the status of interfaces that are shut down during the VSX split:

switch(config)# show vsx status shutdown-on-split
List of non-vsx interfaces enabled for split shutdown and its status.

Interfaces
1/1/1
lag100
vlan2

Status
Disabled
Disabled
Disabled

split recovery

Syntax

split-recovery
no split-recovery

Description

Enables split recovery mode. Split recovery mode is enabled by default.

The no form of this command disables split-recovery mode.

Command context

config-vsx

Authority

Administrators or local user group members with execution rights for this command.

Usage

Split recovery mode prevents traffic loss when the ISL goes out-of-sync and keepalive subsequently fails.
When the ISL goes out-of-sync and keepalive is established, the secondary VSX LAGs are brought down. If
keepalive then also fails, this situation causes a split condition. In this case, if split recovery mode is enabled,
the secondary switch restores its VSX LAGs so they are up.

When split recovery mode is disabled during a split condition, the secondary switch keeps it VSX LAGs down.

Examples

Enabling split recovery mode:
switch(config-vsx)# split-recovery

Disabling split recovery mode:
switch(config-vsx)# no split-recovery

system-mac

Syntax

system-mac <MAC-ADDR>
no system-mac <MAC-ADDR>

VSX commands | 152

Description

Sets the MAC address as the VSX system MAC address to be used by control plane protocols, such as STP
and LACP. A pair of VSX switches must have the same VSX system MAC.

The no form of this command unconfigures the VSX system MAC address to be used by control plane
protocols.

Command context

config-vsx

Parameters

<MAC-ADDR>

Specifies the MAC address in a colon separated format, such as XX:XX:XX:XX:XX:XX, for control plane
protocols.

Authority

Administrators or local user group members with execution rights for this command.

Usage

The system-mac <MAC-ADDR> command is highly recommended for preventing traffic disruptions when the
primary VSX switch restores after the secondary VSX switch, such as during:

n A primary switch hardware replacement.

n A power outage with the primary switch restore after the secondary switch restore.

When the primary switch is restored after the secondary switch, a traffic disruption might occur when the
ISL starts to sync. This situation occurs because the MAC system address changes from the secondary
switch to the primary switch for the LACP. To avoid the traffic disruption, set the common system MAC
address by entering the system-mac <MAC-ADDR> command. This command creates a common system MAC
address between the two VSX switches. This common system MAC address prevents a traffic disruption
when the secondary switch comes up before the primary switch. If the common system MAC access is
enabled, the secondary switch uses the common system MAC address instead of its own system MAC
address, which prevents a traffic loss.

The system MAC address also maintains the same MSTP bridge ID across VSX switches, which act as a single
switch.

Examples

Setting a MAC address as the VSX system MAC address to be used by control plane protocols:
switch(config-vsx)# system-mac 02:01:00:00:01:00

Unconfiguring a VSX system MAC address to be used by control plane protocols:
switch(config-vsx)# no system-mac 02:01:00:00:01:00

Null system MAC address such as 00:00:00:00:00:00 is not allowed.

vsx

Syntax

vsx
no vsx

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

153

Description

Creates the VSX context on the switch.

The no form of this command disables the VSX context on the switch and removes all related configuration
settings.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating the VSX context on the switch:

switch(config)# vsx
switch(config-vsx)#

Removing the VSX context and all VSX configuration settings from the switch:

switch(config-vsx)# no vsx
VSX configuration will be deleted.
Do you want to continue (y/n)? y
switch(config)#

vsx active-forwarding

Syntax

vsx active-forwarding
no vsx active-forwarding

Description

Configures VSX active-forwarding on an interface VLAN.

The no form of this command unconfigures VSX active-forwarding on a VLAN interface.

Command context

config-if-vlan

Authority

Administrators or local user group members with execution rights for this command.

Usage

Active forwarding cannot be configured when ICMP redirect is enabled. The ICMP redirect setting is global
not per SVI. Enter the no ip icmp redirect command for disabling ICMP redirect at the switch(config)#
prompt.

If a system has active forwarding enabled, an active gateway can have a maximum of 14 "unique" MAC
addresses per system, including IPv4 and IPv6 addresses.

If a system has active forwarding disabled, an active gateway can have a maximum of 16 "unique" MAC
addresses per system, including IPv4 and IPv6 addresses.

VSX commands | 154

Examples
SuccessfullyenablingVSXactive-forwarding:
switch#
interface vlan 3
| switch(config-if-vlan)# |     | vsx active-forwarding |
| ----------------------- | --- | --------------------- |
switch(config-vsx)#
UnconfiguringVSXactive-forwarding:
| switch# interface       | vlan | 3                        |
| ----------------------- | ---- | ------------------------ |
| switch(config-if-vlan)# |      | no vsx active-forwarding |
switch(config-vsx)#
vsx shutdown-on-split
Syntax
vsx shutdown-on-split
no vsx shutdown-on-split
Description
Shutsdowntheconfigurednon-VSXinterfacesontheVSXsecondaryalongwithVSX interfacesduringaVSX
split.
Thenoformofthiscommandresumesthenon-VSXinterfacesthatareshutdownduringtheVSXsplit.
ThiscommandhasnoeffectontheVSXprimaryduringasplit.However,whenappliedontheVSXprimary,the
commandwillbringdownthenon-VSXinterfacesuntillinkupdelaytimerexpiresduringtheVSXprimaryreboot.
Commandcontext
config-if
config-lag-if
config-if-vlan
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Shuttingdownthenon-VSXinterface1/1/1duringtheVSXsplit:
| switch(config)#       | interface | 1/1/1             |
| --------------------- | --------- | ----------------- |
| switch(config-if)#    | vsx       | shutdown-on-split |
| switch(config)#       | interface | lag 1             |
| witch(config-lag-if)# | vsx       | shutdown-on-split |
Shuttingdownthenon-VSXinterfaceLAG5duringtheVSXsplit:
| switch(config)#        | interface | lag 5                 |
| ---------------------- | --------- | --------------------- |
| switch(config-lag-if)# |           | vsx shutdown-on-split |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 155

Shutting down the non-VSX SVI during the VSX split:

switch(config)# interface vlan 2
switch(config-if-vlan)# vsx shutdown-on-split

Resuming the non-VSX interface that are shutdown during the VSX split:

switch(config-if)# no vsx shutdown-on-split

vsx-sync

Syntax

vsx-sync
no vsx-sync

Description

Enables VSX synchronization for the entire context for the following features from the primary VSX node to
the secondary peer switch:

n Access list context

n Classifier context

n Object group context

n Policy-based routing profile context

n Policy context

n QoS queue profile context

n QoS schedule profile context

n VLAN context

The no form of this command disables VSX synchronization for the entire context for a feature, but it does
not remove the feature configurations from the secondary peer. Any subsequent configuration changes
made under the specific configuration context are not synchronized to the secondary peer switch.

Command context

config-acl-<ACL-TYPE>
config-addrgroup-ip
config-addrgroup-ipv6
config-class-<CLASS-TYPE>
config-policy
config-portgroup
config-pbr-action-list-<ACTION-LIST-NAME>
config-queue
config-schedule
config-vlan-<ID>

Authority

Administrators or local user group members with execution rights for this command.

Usage

Make sure that you are in the correct context for the feature that you are trying to enable VSX
synchronization:

VSX commands | 156

Feature context forenabling VSX syn- Commandforaccessing correct context for
chronization the vsx-synccommand*
AccesslistcontextforanACLtype,suchasIPv4,IPv6, access-list <ACL-TYPE> <ACL-NAME>
orMAC.
Classcontextforaclasstype,suchasIPv4,IPv6,or class <CLASS-TYPE> <CLASS-NAME>
MAC.
ObjectgroupcontextforIPv4 object-group ip address <OBJECT-GROUP-
NAME>
ObjectgroupcontextforIPv6 object-group ipv6 address <OBJECT-GROUP-
NAME>
Objectgroupcontextforports object-group port <OBJECT-GROUP-NAME>
Policy-basedroutingprofilecontext pbr <ACTION-LIST-NAME>
Policycontext policy <POLICY-NAME>
QoSqueueprofilecontext qos queue-profile <QUEUE-PROFILE-NAME>
QoSscheduleprofilecontext qos schedule-profile <SCHEDULE-PROFILE-
NAME>
VLANcontext vlan <ID>
*Thecommandslistedinthiscolumnareenteredattheswitch(config)#prompt,asshowninthefollowing
examples.
Examples
EnablingVSXsynchronizationforthisIPv4accesslistcontexttothesecondarypeer:
| switch(config)#        | access-list | ip ITBoston |
| ---------------------- | ----------- | ----------- |
| switch(config-acl-ip)# | vsx-sync    |             |
EnablingVSXsynchronizationforthisIPv6accesslistcontexttothesecondarypeer:
| switch(config)#          | access-list | ipv6 ITRoseville |
| ------------------------ | ----------- | ---------------- |
| switch(config-acl-ipv6)# |             | vsx-sync         |
EnablingVSXsynchronizationforthisMACaccesslistcontexttothesecondarypeer:
| switch(config)#          | access-list | mac ITBangalore |
| ------------------------ | ----------- | --------------- |
| switch(config-acl-ipv6)# |             | vsx-sync        |
EnablingVSXsynchronizationforthisIPv4classcontexttothesecondarypeer:
| switch(config)#          | class ip | ITengineering |
| ------------------------ | -------- | ------------- |
| switch(config-class-ip)# |          | vsx-sync      |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 157

EnablingVSXsynchronizationforthisobjectgroupcontextforIPv4:
| switch(config)#              | object-group | ip address | group1 |
| ---------------------------- | ------------ | ---------- | ------ |
| switch(config-addrgroup-ip)# |              | 1.1.1.1    |        |
| switch(config-addrgroup-ip)# |              | vsx-sync   |        |
EnablingVSXsynchronizationforthisQoSqueueprofilecontexttothesecondarypeer:
| switch(config)# | qos queue-profile | test_queue_profile |     |
| --------------- | ----------------- | ------------------ | --- |
switch(config-queue)#
vsx-sync
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
| switch(config)#        | vlan 1   |     |     |
| ---------------------- | -------- | --- | --- |
| switch(config-vlan-1)# | vsx-sync |     |     |
DisablingVSXsynchronizationforthisIPv4classcontexttothesecondarypeer:
| switch(config)# | class ip ITengineering |     |     |
| --------------- | ---------------------- | --- | --- |
switch(config-class-ip)#
no vsx-sync
DisablingVSXsynchronizationforthisobjectgroupcontextforIPv4:
| switch(config)#              | object-group | ip address  | group1 |
| ---------------------------- | ------------ | ----------- | ------ |
| switch(config-addrgroup-ip)# |              | no vsx-sync |        |
DisablingVSXsynchronizationforthisQoSqueueprofilecontexttothesecondarypeer:
| switch(config)#       | qos queue-profile | test_queue_profile |     |
| --------------------- | ----------------- | ------------------ | --- |
| switch(config-queue)# | no vsx-sync       |                    |     |
DisablingVSXsynchronizationforthisQoSscheduleprofilecontexttothesecondarypeer:
VSXcommands|158

| switch(config)# | qos schedule-profile | test_queue_profile1 |
| --------------- | -------------------- | ------------------- |
switch(config-schedule)#
no vsx-sync
DisablingVSXsynchronizationforthisPBRprofilecontexttothesecondarypeer:
| switch(config)# | pbr engineering |     |
| --------------- | --------------- | --- |
switch(config-pbr-action-list-engineering)# no vsx-sync
DisablingVSXsynchronizationforthispolicycontexttothesecondarypeer:
| switch(config)#        | policy ITPaloAlto |          |
| ---------------------- | ----------------- | -------- |
| switch(config-policy)# | no                | vsx-sync |
DisablingVSXsynchronizationforthisMACaccesslistcontexttothesecondarypeer:
| switch(config)#          | access-list | mac ITBangalore |
| ------------------------ | ----------- | --------------- |
| switch(config-acl-ipv6)# |             | no vsx-sync     |
DisablingVSXsynchronizationforthisVLANcontexttothesecondarypeer:
| switch(config)#        | vlan 1 |          |
| ---------------------- | ------ | -------- |
| switch(config-vlan-1)# | no     | vsx-sync |
vsx-sync {[access-lists] [qos] [rate-limits] [vlans] [policies]
[irdp] [portfilter]}
Syntax
vsx-sync {[access-lists] [qos] [rate-limits] [vlans] [policies] [irdp] [portfilter]}
no vsx-sync {[access-lists] [qos] [rate-limits] [vlans] [policies] [irdp] [portfilter]}
Description
EnablesVSXsynchronizationforthefollowingforalogicalinterfaceoraLAGinstance:
Accesslists
n
IRDPconfigurations
n
n QoS
n Ratelimits
n Portfilterconfigurations
n VLANassociations
ThiscommandenablesVSXsynchronizationforindividualassociationsandtothecombinationof
associationstotheinterfacecontext.Tosynchronizetheassociations,youmustconfigurethesame
interfaceonthepeerswitch.
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 159

When enabling VSX synchronization under a physical interface, under a VLAN interface, or a VSX LAG, create on

the secondary switch the physical interface, VLAN interface, or VSX LAG with the same name and routing setting

as on the primary switch. For example, if the primary switch has a physical interface of 1/1/1, you must create

another physical interface of 1/1/1 on the secondary switch. Also, if the primary VSX switch has routing enabled,

the secondary switch must have routing enabled. Once the name and routing information is the same, VSX

synchronization synchronizes the additional configuration information from the primary VSX switch to the

secondary VSX switch.

The no form of this command disables VSX synchronization, but it does not remove the feature
configurations from the secondary peer.

Command context

config-if
config-lag-if

Parameters

{[access-lists] [qos] [rate-limits] [vlans] [policies] [irdp] [portfilter]}

Specifies one or more of the features for which to enable VSX synchronization.
access-lists

Specifies the access lists that are associated under the interface enabled for VSX syncing.

qos

Specifies the QoS associated under the interface enabled for VSX syncing.

rate-limits

Specifies the rate limits that are associated under the interface enabled for VSX syncing.

vlans

Specifies the VLANs that are associated under the interface enabled for VSX syncing.

policies

Specifies the classifier policies that are associated under the interface enabled for VSX syncing.

irdp

Specifies the Internet Router Discovery Protocol (IRDP) configurations that are associated under the
interface enabled for VSX syncing.

portfilter

Specifies the port filter configurations that are associated under the interface enabled for VSX
syncing.

Authority

Administrators or local user group members with execution rights for this command.

Example

Enabling VSX synchronization for VLANs associated with logical interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# vsx-sync vlans

Enabling VSX synchronization for access lists associated with logical interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# vsx-sync access-lists

VSX commands | 160

EnablingVSXsynchronizationforaccesslistsandpoliciesthatareassociatedwithlogicalinterface1/1/1:
| switch(config)#    | interface | 1/1/1        |     |          |
| ------------------ | --------- | ------------ | --- | -------- |
| switch(config-if)# | vsx-sync  | access-lists |     | policies |
EnablingVSXsynchronizationforQoSthatareassociatedunderlogicalinterface1/1/5:
| switch(config)#    | interface | 1/1/5 |     |     |
| ------------------ | --------- | ----- | --- | --- |
| switch(config-if)# | vsx-sync  | vlans | qos |     |
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
| switch(config)#        | interface | lag 1      |        |     |
| ---------------------- | --------- | ---------- | ------ | --- |
| switch(config-lag-if)# |           | vsx-sync   | vlans  |     |
| switch(config-lag-if)# |           | vlan trunk | native | 1   |
EnablingVSXsynchronizationforanaccesslistunderinterfaceLAG2:
| switch(config)#        | interface | lag 2             |              |             |
| ---------------------- | --------- | ----------------- | ------------ | ----------- |
| switch(config-lag-if)# |           | vsx-sync          | access-lists |             |
| switch(config-lag-if)# |           | apply access-list |              | ip test1 in |
EnablingVSXsynchronizationforaQoSunderinterfaceLAG3:
| switch(config)#        | interface | lag 3     |                  |      |
| ---------------------- | --------- | --------- | ---------------- | ---- |
| switch(config-lag-if)# |           | vsx-sync  | qos              |      |
| switch(config-lag-if)# |           | apply qos | schedule-profile | test |
EnablingVSXsynchronizationforaratelimitunderinterfaceLAG4:
| switch(config)#        | interface | lag 4      |             |         |
| ---------------------- | --------- | ---------- | ----------- | ------- |
| switch(config-lag-if)# |           | vsx-sync   | rate-limits |         |
| switch(config-lag-if)# |           | rate-limit | broadcast   | 23 kbps |
EnablingVSXsynchronizationforapolicynamedtestunderinterfaceLAG5:
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 161

| switch(config)# |     | interface | lag | 5   |     |     |     |
| --------------- | --- | --------- | --- | --- | --- | --- | --- |
switch(config-lag-if)#
|                        |     |     | vsx-sync | policies |      |     |     |
| ---------------------- | --- | --- | -------- | -------- | ---- | --- | --- |
| switch(config-lag-if)# |     |     | apply    | policy   | test | in  |     |
EnablingVSXsynchronizationforapolicynamedtest1,aratelimitof23kbps,aQoSnamedtest,VLAN1,
andanaccesslistnamedtest1underinterfaceLAG6:
| switch(config)# |     | interface | lag | 6   |     |     |     |
| --------------- | --- | --------- | --- | --- | --- | --- | --- |
switch(config-lag-if)# vsx-sync policies rate-limits qos vlans access-lists
| switch(config-lag-if)# |     |     | apply      | policy      | test1            | in      |      |
| ---------------------- | --- | --- | ---------- | ----------- | ---------------- | ------- | ---- |
| switch(config-lag-if)# |     |     | rate-limit |             | broadcast        | 23      | kbps |
| switch(config-lag-if)# |     |     | apply      | qos         | schedule-profile |         | test |
| switch(config-lag-if)# |     |     | vlan       | trunk       | native           | 1       |      |
| switch(config-lag-if)# |     |     | apply      | access-list |                  | ip test | 1 in |
EnablingVSXsynchronizationforaportfilter:
switch(config)#
|                    |     | interface | 1/1/1 |            |     |     |     |
| ------------------ | --- | --------- | ----- | ---------- | --- | --- | --- |
| switch(config-if)# |     | vsx-sync  |       | portfilter |     |     |     |
| switch(config)#    |     | interface | lag   | 1          |     |     |     |
switch(config-lag-if)#
|     |     |     | vsx-sync | portfilter |     |     |     |
| --- | --- | --- | -------- | ---------- | --- | --- | --- |
DisablingVSXsynchronizationforaccesslistsandpoliciesunderlogicalinterface1/1/1:
| switch(config)#    |     | interface | 1/1/1    |              |     |          |     |
| ------------------ | --- | --------- | -------- | ------------ | --- | -------- | --- |
| switch(config-if)# |     | no        | vsx-sync | access-lists |     | policies |     |
DisablingVSXsynchronizationforaccesslistsandpoliciesunderinterfaceLAG2:
| switch(config)#    |     | interface | lag      | 2            |     |          |     |
| ------------------ | --- | --------- | -------- | ------------ | --- | -------- | --- |
| switch(config-if)# |     | no        | vsx-sync | access-lists |     | policies |     |
EnablingVSXsynchronizationofIRDPconfigurationsunderlogicalinterface1/1/1.Thefirstfivelinesinthe
exampleconfigureIRDPandthelastlineenablesVSXsynchronizationforIRDPconfigurationsassociated
underinterface1/1/1:
| switch(config)#    |     | interface | 1/1/1                  |     |     |     |     |
| ------------------ | --- | --------- | ---------------------- | --- | --- | --- | --- |
| switch(config-if)# |     | ip        | irdp                   |     |     |     |     |
| switch(config-if)# |     | ip        | irdp minadvertinterval |     |     | 550 |     |
| switch(config-if)# |     | ip        | irdp maxadvertinterval |     |     | 850 |     |
| switch(config-if)# |     | ip        | irdp holdtime          |     | 900 |     |     |
switch(config-if)#
|          |                    | vsx-sync |     | irdp |     |             |     |
| -------- | ------------------ | -------- | --- | ---- | --- | ----------- | --- |
| vsx-sync | {[active-gateways] |          |     |      |     | [policies]} |     |
Syntax
| vsx-sync    | {[active-gateways] |     | [policies]} |             |     |     |     |
| ----------- | ------------------ | --- | ----------- | ----------- | --- | --- | --- |
| no vsx-sync | {[active-gateways] |     |             | [policies]} |     |     |     |
VSXcommands|162

Description
EnablesVSXsyncofactivegatewaysorpoliciesassociatedunderaninterface.Tosynchronizethe
associations,youmustconfigurethesameinterface vlanonthepeerswitch.
ThenoformofthiscommandremovesVSXsynchronizationforactivegatewaysorpoliciesassociatedunder
aninterface,butitdoesnotremovethefeatureconfigurationsfromthesecondarypeerswitch.
Commandcontext
config-if-vlan
Parameters
| {[active-gateways] | [policies]} |     |     |     |
| ------------------ | ----------- | --- | --- | --- |
SpecifiesoneormoreofthefeaturesforwhichtoenableVSXsynchronization.
access-gateways
SpecifiesthatactivegatewaysassociatedwithaninterfaceareenabledforVSXsyncing.
policies
SpecifiesthatpoliciesassociatedwithaninterfaceareenabledforVSXsyncing.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
ConfigureanSVIonthesecondaryswitch;however,youdonotneedtorunthevsx-sync active-gateways
commandonthesecondaryVSXswitch.
DonotusepeersystemMACaddressasanactive-gatewayVMAC.IfsameMACaddressisused,theVSX
synchronizationwilltrytosynctheconfigurationonsecondaryswitchandcausetrafficdisruptions.
Examples
EnablingVSXsynchronizationforanactivegatewayassociatedwithVLAN1:
| switch(config)#         | interface | vlan 1                   |     |     |
| ----------------------- | --------- | ------------------------ | --- | --- |
| switch(config-if-vlan)# |           | vsx-sync active-gateways |     |     |
EnablingVSXsynchronizationforpoliciesassociatedwithVLAN1:
| switch(config)#         | interface | vlan 1            |     |     |
| ----------------------- | --------- | ----------------- | --- | --- |
| switch(config-if-vlan)# |           | vsx-sync policies |     |     |
EnablingVSXsynchronizationforactivegatewaysandpoliciesassociatedwithVLAN1:
| switch(config)# | interface | vlan 1 |     |     |
| --------------- | --------- | ------ | --- | --- |
switch(config-if-vlan)#
|     |     | active-gateway | ip 10.10.10.10 | mac 23:24:25:26:27:28 |
| --- | --- | -------------- | -------------- | --------------------- |
switch(config-if-vlan)# active-gateway ipv6 fd12:3456:789a:1::1 mac
| fd12:3456:789a:1::1     | 23:24:25:26:27:28 |                          |     |          |
| ----------------------- | ----------------- | ------------------------ | --- | -------- |
| switch(config-if-vlan)# |                   | vsx-sync active-gateways |     | policies |
DisablingVSXsynchronizationforactivegatewaysassociatedwithVLAN1:
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 163

switch(config)# interface vlan 1
switch(config-if-vlan)# no vsx-sync active-gateways

vsx-sync aaa

Syntax

vsx-sync aaa
no vsx-sync aaa

Description

Enables VSX synchronization of all AAA configurations, including user, RADIUS server, and TACACS+ server,
on the primary VSX node to the secondary peer switch. To synchronize AAA configurations associated with a
particular VRF, you must configure the same VRF on the peer switch.

The no form of this command removes VSX synchronization of global AAA configurations, but it does not
remove the existing global AAA feature configurations from the secondary peer switch.

Command context

config-vsx

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling VSX sync for the AAA configurations to the secondary peer:

switch(config)# vsx
switch(config-vsx)# vsx-sync aaa

Disabling VSX sync for the AAA configurations to the secondary peer:

switch(config)# vsx
switch(config-vsx)# no vsx-sync aaa

vsx-sync acl-log-timer

Syntax

vsx-sync acl-log-timer
no vsx-sync acl-log-timer

Description

Enables VSX synchronization of access list log timer configurations on the primary VSX node to the
secondary peer.

The no form of this command removes VSX synchronization of access list log timer configurations to the
secondary peer. However, it does not remove the previously synced configurations from the secondary
peer switch.

Command context

VSX commands | 164

config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVSXsyncfortheaccesslistlogtimerconfigurations:
| switch(config)# | access-list | log timer | 30  |
| --------------- | ----------- | --------- | --- |
switch(config)#
vsx
| switch(config-vsx)# | vsx-sync | acl-log-timer |     |
| ------------------- | -------- | ------------- | --- |
DisablingVSXsyncfortheaccesslistlogtimerconfigurations:
| switch(config)#       | vsx         |               |     |
| --------------------- | ----------- | ------------- | --- |
| switch(config-vsx)#   | no vsx-sync | acl-log-timer |     |
| vsx-sync arp-security |             |               |     |
Syntax
vsx-sync arp-security
no vsx-sync arp-security
Description
EnablesVSXsynchronizationoftheARPsecurityconfigurationsontheprimaryVSXswitchtothesecondary
peerswitch.Afteryouentervsx-sync arp-security,youmustentervsx-sync mclag-interfacesfor
enablingVSXsynchronizationfortheARPsecurityfeature.
ThenoformofthiscommandremovesVSXsynchronizationofARPsecurityconfigurationsonVLANmode
andLAGinterfacemodetothesecondarypeerswitch.However,itdoesnotremovetheexistingARP
securityconfigurationsfromthesecondarypeerswitch.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingofVSXsynchronizationforARPsecurityfeatureconfigurationstosecondarypeer:
| primary_sw(config)#     | vsx      |                  |     |
| ----------------------- | -------- | ---------------- | --- |
| primary_sw(config-vsx)# | vsx-sync | arp-security     |     |
| primary_sw(config-vsx)# | vsx-sync | mclag-interfaces |     |
DisablingtheVSXsynchronizationforARPsecurityfeatureconfigurationstosecondarypeer:
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 165

| primary_sw(config)# | vsx |     |     |
| ------------------- | --- | --- | --- |
primary_sw(config-vsx)#
no vsx-sync arp-security
| switch(config-vsx)# | no vsx-sync | mclag-interfaces |     |
| ------------------- | ----------- | ---------------- | --- |
| vsx-sync bfd-global |             |                  |     |
Syntax
vsx-sync bfd-global
no vsx-sync bfd-global
Description
EnablessyncingofglobalBFDconfigurations,suchasecho-src-ip-address,detect-multiplier,min-
transmit-interval,andmin-receive-interval,ontheprimaryVSXnodetothesecondarypeer.
ThiscommandenablesVSXsynchronizationonlyatthetoplevelandnotatthecontextlevel.
ThenoformofthiscommanddisablesthesyncingofglobalBFDconfigurationstothesecondarypeer,but
itdoesnotremovetheexistingglobalBFDfeatureconfigurationsfromit.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVSXsynchronizationforvariousglobalBFDconfigurations:
| switch(config)#     | bfd detect-multiplier         |            | 1       |
| ------------------- | ----------------------------- | ---------- | ------- |
| switch(config)#     | bfd min-transmit-interval     |            | 1000    |
| switch(config)#     | bfd min-receive-interval      |            | 1000    |
| switch(config)#     | bfd echo-src-ip-address       |            | 2.2.2.2 |
| switch(config)#     | bfd min-echo-receive-interval |            | 1000    |
| switch(config)#     | vsx                           |            |         |
| switch(config-vsx)# | vsx-sync                      | bfd-global |         |
DisablingVSXsynchronizationforglobalBFDconfigurations:
| switch(config)#     | vsx         |            |     |
| ------------------- | ----------- | ---------- | --- |
| switch(config-vsx)# | no vsx-sync | bfd-global |     |
| vsx-sync bgp        |             |            |     |
Syntax
vsx-sync bgp
no vsx-sync bgp
Description
VSXcommands|166

EnablessyncingofBGPconfigurationsontheprimaryVSXswitchtothesecondarypeerswitch.
ThenoformofthiscommanddisablessyncingBGP,aspathlists,communitylists,prefixlists,androutemap
configurationstothesecondarypeer,butitdoesnotremovethepreviouslysyncedconfigurationsfromthe
secondarypeerswitch.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
ThefollowingBGPconfigurationsaresynchronized:aspathlists,communitylists,prefixlists,androutemap
configurations.Tomaintaintheuniquenessofaswitchintheautonomoussystem,theBGProuterID,BGP
clusterID,andBGPneighborupdate-sourcearenotsynchronized.ThisexclusionisrequiredforBGP
functionalitytoworkseamlesslyevenwithVSXtopology.
Severalsettingsarealsonotsynced.Theneighbor <IP address> shutdownsettingisnotsyncedbecause
syncingthatsettingwouldcauseboththeprimaryandsecondaryVSXnodestowardsthecoretogodown.
Inroutemapconfigurations,thefollowingsettingsarealsonotsyncedfromtheprimaryVSXswitchtothe
secondaryVSXswitch,becausethenext-hopisalwayssetdifferentlyfortheprimaryandsecondaryVSX
peers:
| n set ip   | nexthop | <IP-ADDR> |           |     |     |     |     |     |     |
| ---------- | ------- | --------- | --------- | --- | --- | --- | --- | --- | --- |
| n set ipv6 | nexthop | global    | <IP-ADDR> |     |     |     |     |     |     |
Ifthenext-hopmustbesameforbothprimaryandsecondaryVSXpeers,configurethesamevalueonthe
individualswitches.
Examples
EnablingVSXsyncfortheBGPconfigurations:
| switch(config)# |     | ip                | aspath-list |     | list1    | seq 10 | permit | 10            |     |
| --------------- | --- | ----------------- | ----------- | --- | -------- | ------ | ------ | ------------- | --- |
| switch(config)# |     | ip community-list |             |     | expanded |        | com1   | seq 10 permit | 10  |
switch(config)# ip extcommunity-list standard ext1 seq 10 permit rt 10:4
| switch(config)#                  |     | ip prefix-list |                |            | pref1 seq | 10        | permit   | any     |     |
| -------------------------------- | --- | -------------- | -------------- | ---------- | --------- | --------- | -------- | ------- | --- |
| switch(config)#                  |     | route-map      |                | rm1 permit |           |           |          |         |     |
| switch(config-route-map-rm1-10)# |     |                |                |            | match     | ip        | next-hop | 1.1.1.1 |     |
| switch(config)#                  |     | router         | bgp            | 100        |           |           |          |         |     |
| switch(config-bgp)#              |     |                | bgp router-id  |            | 1.1.1.1   |           |          |         |     |
| switch(config-bgp)#              |     |                | neighbor       | 12.1.1.1   |           | remote-as |          | 1       |     |
| switch(config-bgp)#              |     |                | address-family |            | ipv4      | unicast   |          |         |     |
| switch(config-bgp-ipv4-uc)#      |     |                |                | neighbor   | 12.1.1.1  |           | activate |         |     |
| switch(config)#                  |     | vsx            |                |            |           |           |          |         |     |
| switch(config-vsx)#              |     |                | vsx-sync       | bgp        |           |           |          |         |     |
DisablingVSXsyncfortheBGPconfigurations:
| switch(config)#     |             | vsx |             |     |     |     |     |     |     |
| ------------------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| switch(config-vsx)# |             |     | no vsx-sync |     | bgp |     |     |     |     |
| vsx-sync            | copp-policy |     |             |     |     |     |     |     |     |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 167

Syntax
| vsx-sync copp-policy |             |     |     |     |     |     |
| -------------------- | ----------- | --- | --- | --- | --- | --- |
| no vsx-sync          | copp-policy |     |     |     |     |     |
Description
EnablesVSXsynchronizationofCoPPpolicyconfigurationsontheprimaryVSXnodetothesecondarypeer
switch.
ThenoformofthiscommandremovesVSXsynchronizationofglobalCoPPconfigurations,butitdoesnot
removetheexistingglobalCoPPconfigurationsfromthesecondarypeerswitch.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Thefirstthreelinesinthefollowingexampleshowthesettingofseveralpolicyconfigurations.Thelasttwo
linesoftheexampleshowtheenablingofVSXsynchronizationforCoPPpolicyconfigurations.
| switch(config)#      | copp-policy | mypolicy            |             |      |     |     |
| -------------------- | ----------- | ------------------- | ----------- | ---- | --- | --- |
| switch(config-copp)# |             | class arp-broadcast |             | drop |     |     |
| switch(config-copp)# |             | no class            | arp-unicast |      |     |     |
| switch(config)#      | vsx         |                     |             |      |     |     |
| switch(config-vsx)#  |             | vsx-sync            | copp-policy |      |     |     |
DisablingVSXsynchronizationforglobalCoPPconfigurations:
| switch(config)#     | vsx        |             |             |             |          |       |
| ------------------- | ---------- | ----------- | ----------- | ----------- | -------- | ----- |
| switch(config-vsx)# |            | no vsx-sync | copp-policy |             |          |       |
| vsx-sync            | dcb-global | (8325       | and         | 8360 series | switches | only) |
Syntax
| vsx-sync dcb-global |            |     |     |     |     |     |
| ------------------- | ---------- | --- | --- | --- | --- | --- |
| no vsx-sync         | dcb-global |     |     |     |     |     |
Description
EnablesVSXsynchronizationofglobalDCBxconfigurationsfromtheprimaryVSXnodetothesecondary
peer.
ThenoformofthecommanddisablesVSXsynchronizationofglobalDCBxconfigurationstothesecondary
peer;however,itdoesnotremovetheexistingDCBxfeatureconfigurationsfromthesecondarypeer.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
VSXcommands|168

Usage
ThefollowingcommandsaresyncedfromprimaryVSXnodetosecondaryVSXnode:
n lldp dcbx
n dcbx application
Examples
ThefirsttwolinesinthefollowingexampleshowthesettingofglobalDCBxconfigurations.Thelasttwo
linesintheexampleshowtheenablingofVSXsynchronizationforglobalDCBxconfigurations.
| switch(config)#     | lldp dcbx        |            |                |     |
| ------------------- | ---------------- | ---------- | -------------- | --- |
| switch(config)#     | dcbx application |            | iscsi priority | 7   |
| switch(config)#     | vsx              |            |                |     |
| switch(config-vsx)# | vsx-sync         | dcb-global |                |     |
DisablingVSXsynchronizationforglobalDCBxconfigurations:
| switch(config)#     | vsx |          |            |     |
| ------------------- | --- | -------- | ---------- | --- |
| switch(config-vsx)# | no  | vsx-sync | dcb-global |     |
| vsx-sync dhcp-relay |     |          |            |     |
Syntax
vsx-sync dhcp-relay
no vsx-sync dhcp-relay
Description
EnablesVSXsynchronizationofDHCPv4andDHCPv6relayconfigurationsontheprimaryVSXnodetothe
secondarypeer.
ThenoformofthecommanddisablestheVSXsynchronizationofDHCPv4andDHCPv6relay
configurationstothesecondarypeer;however,itdoesnotremovetheexistingDHCPv4andDHCPv6relay
configurationsfromthesecondaryVSXpeer.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ThisexampleenablesVSXsynchronizationforDHCPv4relayconfigurations.Thefirstsixlinesintheexample
showDHCPv4relayconfigurations.ThelasttwolinesshowhowtoenableVSXsynchronizationforthe
DHCPrelayconfigurations:
| switch(config)#    | interface         | 1/1/1 |              |     |
| ------------------ | ----------------- | ----- | ------------ | --- |
| switch(config-if)# | ip helper-address |       | 192.168.10.1 |     |
| switch(config-if)# | ip helper-address |       | 192.168.20.1 |     |
| switch(config)#    | interface         | 1/1/2 |              |     |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 169

| switch(config-if)# | ip helper-address |     |     | 192.168.30.1 |
| ------------------ | ----------------- | --- | --- | ------------ |
switch(config)#
|                     | dhcp-relay | option | 82         |     |
| ------------------- | ---------- | ------ | ---------- | --- |
| switch(config)#     | vsx        |        |            |     |
| switch(config-vsx)# | vsx-sync   |        | dhcp-relay |     |
ThisexampleenablesVSXsynchronizationforDHCPv6relayconfigurations.Thefirstsevenlinesinthe
exampleshowDHCPv6relayconfigurations.ThelasttwolinesshowhowtoenableVSXsynchronizationfor
theDHCPrelayconfigurations:
| switch(config)# | dhcpv6-relay |     |     |     |
| --------------- | ------------ | --- | --- | --- |
switch(config)#
|                    | interface | 1/1/1          |     |                        |
| ------------------ | --------- | -------------- | --- | ---------------------- |
| switch(config-if)# | ipv6      | helper-address |     | unicast 2001:db8:0:1:: |
switch(config-if)# ipv6 helper-address multicast FF01::1:1000 egress 1/1/2
| switch(config)#     | interface    | 1/1/2          |            |                        |
| ------------------- | ------------ | -------------- | ---------- | ---------------------- |
| switch(config-if)#  | ipv6         | helper-address |            | unicast 2001:db8:0:2:: |
| switch(config)#     | dhcpv6-relay |                | option     | 79                     |
| switch(config)#     | vsx          |                |            |                        |
| switch(config-vsx)# | vsx-sync     |                | dhcp-relay |                        |
DisablingVSXsynchronizationforDHCPrelayconfigurations:
switch(config)#
vsx
| switch(config-vsx)#  | no  | vsx-sync | dhcp-relay |     |
| -------------------- | --- | -------- | ---------- | --- |
| vsx-sync dhcp-server |     |          |            |     |
Syntax
vsx-sync dhcp-server
no vsx-sync dhcp-server
Description
EnablesVSXsynchronizationofallDHCPv4serverconfigurations,includingexternalstorageconfigurations,
ontheprimaryVSXnodetothesecondarypeer.TosynchronizeDHCPv4serverconfigurationsassociated
withaparticularVRF,configurethesameVRFonthepeerdevice.OnlytheprimaryVSXnodeanswersDHCP
servicerequests,andleasescanonlybeexportedfromtheprimaryVSXnode.
ThenoformofthecommanddisablesVSXsynchronizationofDHCPv4serverconfigurationstothe
secondarypeer;however,itdoesnotremovetheexistingDHCPv4serverfeatureconfigurationsfromthe
secondarypeer.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ThefirstsixlinesinthefollowingexampleshowthesettingofaDHCPv4serverconfiguration.Thelastline
oftheexampleshowstheenablingofVSXsynchronizationforglobalDHCPv4serverconfigurations.
VSXcommands|170

switch(config)# dhcp-server external-storage dhcp-dbs file dhcpv4_lease_file delay
600
| switch(config)#                  | dhcp-server | vrf default     |           |
| -------------------------------- | ----------- | --------------- | --------- |
| switch(config-dhcp-server)#      |             | pool test       |           |
| switch(config-dhcp-server-pool)# |             | range 10.0.0.20 | 10.0.0.30 |
switch(config-dhcp-server-pool)# default-router 10.0.0.1 10.0.0.10
switch(config-dhcp-server-pool)# static-bind ip 10.0.0.1 mac 24:be:05:24:75:73
| switch(config)#     | vsx      |             |     |
| ------------------- | -------- | ----------- | --- |
| switch(config-vsx)# | vsx-sync | dhcp-server |     |
DisablingVSXsynchronizationforglobalDHCPv4serverconfigurations:
switch(config)#
vsx
| switch(config-vsx)#    | no vsx-sync | dhcp-server |     |
| ---------------------- | ----------- | ----------- | --- |
| vsx-sync dhcpv6-server |             |             |     |
Syntax
vsx-sync dhcpv6-server
no vsx-sync dhcpv6-server
Description
EnablesVSXsynchronizationofallDHCPv6serverconfigurations,includingexternalstorageconfigurations,
ontheprimaryVSXnodetothesecondarypeer.TosynchronizeDHCPv6serverconfigurationsassociated
withaparticularVRF,configurethesameVRFonthepeerdevice.
ThenoformofthecommanddisablesVSXsynchronizationofDHCPv6serverconfigurationstothe
secondarypeer;however,itdoesnotremovetheexistingDHCPv6serverfeatureconfigurationsfromthe
secondarypeer.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ThefirstsixlinesinthefollowingexampleshowthesettingofaDHCPv6serverconfiguration.Thelasttwo
linesoftheexampleshowtheenablingofVSXsynchronizationforglobalDHCPv6serverconfigurations.
switch(config)# dhcpv6-server external-storage dhcpv6-dbs file dhcpv6_lease_file
delay 600
| switch(config)#             | dhcpv6-server | vrf default |     |
| --------------------------- | ------------- | ----------- | --- |
| switch(config-dhcp-server)# |               | pool test   |     |
switch(config-dhcpv6-server-pool)# range 2001::1 2001::10 prefix-len 64
| switch(config-dhcpv6-server-pool)# |     | option | 22 ipv6 2001::12 |
| ---------------------------------- | --- | ------ | ---------------- |
switch(config-dhcpv6-server-pool)# static-bind ipv6 2001::11 client-id
1:0:a0:24:ab:fb:9c
| switch(config)#     | vsx      |               |     |
| ------------------- | -------- | ------------- | --- |
| switch(config-vsx)# | vsx-sync | dhcpv6-server |     |
DisablingVSXsynchronizationforglobalDHCPv6serverconfigurations:
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 171

| switch(config)# | vsx |     |
| --------------- | --- | --- |
switch(config-vsx)#
|              | no vsx-sync | dhcpv6-server |
| ------------ | ----------- | ------------- |
| vsx-sync dns |             |               |
Syntax
vsx-sync dns
no vsx-sync dns
Description
EnablesVSXsynchronizationoftheglobalDNSconfigurationsontheprimaryVSXnodetothesecondary
peerswitch.TosynchronizeDNSconfigurationsassociatedwithparticularVRF,youmustconfigurethe
sameVRFonthepeerswitch.
ThenoformofthiscommandremovesVSXsynchronizationforglobalDNSconfigurations,butitdoesnot
removethefeatureconfigurationsfromthesecondarypeerswitch.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ThefirstlineinthefollowingexampleshowsthesettingofaDNSconfiguration.Thelasttwolinesofthe
exampleshowtheenablingofVSXsynchronizationforglobalDNSconfigurations.
| switch(config)#     | ip dns domain-name | domain.com |
| ------------------- | ------------------ | ---------- |
| switch(config)#     | vsx                |            |
| switch(config-vsx)# | vsx-sync           | dns        |
DisablingVSXsynchronizationforglobalDNSconfigurations:
| switch(config)#     | vsx         |     |
| ------------------- | ----------- | --- |
| switch(config-vsx)# | no vsx-sync | dns |
| vsx-sync evpn       |             |     |
Syntax
vsx-sync evpn
no vsx-sync evpn
Description
EnablessyncingofallEVPNcontext-relatedconfigurationsonprimaryVSXnodetothesecondarypeer
switch.
ThenoformofthiscommanddisablessyncingEVPNconfigurationstothesecondarypeer,butitdoesnot
removethepreviouslysyncedconfigurationsfromthesecondarypeerswitch.
VSXcommands|172

Asaprerequisite,VLANvsx-syncmustbeenabledseparatelyfortheVLANconfigurationsinsideEVPNcontextto
getsynced.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVSXsyncfortheEVPNconfigurations:
| switch(config)# vlan        | 2            |            |
| --------------------------- | ------------ | ---------- |
| switch(config-vlan-2)#      | vsx-sync     |            |
| switch(config)# evpn        |              |            |
| switch(config-evpn)#        | vlan 2       |            |
| switch(config-evpn-vlan-2)# | rd           | 5:5        |
| switch(config-evpn-vlan-2)# | route-target | export 1:1 |
| switch(config-evpn-vlan-2)# | route-target | import 1:1 |
| switch(config)# vsx         |              |            |
| switch(config-vsx)#         | vsx-sync     | evpn       |
DisablingVSXsyncfortheEVPNconfigurations:
| switch(config)# vsx |             |      |
| ------------------- | ----------- | ---- |
| switch(config-vsx)# | no vsx-sync | evpn |
vsx-sync icmp-tcp
Syntax
vsx-sync icmp-tcp
no vsx-sync icmp-tcp
Description
EnablesVSXsynchronizationofIPICMPconfigurations,includingip icmp unreachable,ip icmp redirect,
andip icmp throttleconfigurations,onprimaryVSXnodetothesecondarypeer.Tosynchronizeip icmp
unreachable,ip icmp redirect,andip icmp throttleconfigurations,associatedwithparticularVRF,
configurethesameVRFonthepeerdevice.
ThenoformofthecommanddisablestheVSXsynchronizationofIPICMPconfigurationstothesecondary
peer.However,itdoesnotremovetheexistingIPICMPconfigurationsfromthesecondaryVSXpeer.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 173

EnablingVSXsynchronizationforIPICMPconfigurations:
| switch(config)# vsx |          |          |     |
| ------------------- | -------- | -------- | --- |
| switch(config-vsx)# | vsx-sync | icmp-tcp |     |
DisablingVSXsynchronizationforIPICMPconfigurations:
| switch(config)# vsx |             |          |     |
| ------------------- | ----------- | -------- | --- |
| switch(config-vsx)# | no vsx-sync | icmp-tcp |     |
vsx-sync keychain
Syntax
vsx-sync keychain
no vsx-sync keychain
Description
EnablessynchronizingofkeychainconfigurationsonprimaryVSXnodetothesecondarypeer.Thereisno
configurationsynchronizationfromsecondarytoprimarypeer.
Ifanyadditionalmodificationorconfigurationismadeontheprimaryforthekeychainsetoffeatures,the
featureswillbeauto-synchronized.
Thenoformofthecommanddisablessynchronizingkeychainconfigurationstothesecondarypeer.Butit
doesnotremovethepreviouslysynchronizedconfigurationsfromthesecondarypeer.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingsynchronizingofkeychainconfigurationsonprimaryVSXnodetothesecondarypeer:
| switch(config)# keychain | ospf_keys |     |     |
| ------------------------ | --------- | --- | --- |
| switch(config-keychain)# | key       | 1   |     |
switch(config-keychain-key)# send-lifetime start-time 10:10:10 10/25/2019 end-time
10:10:10 11/25/2019
| switch(config-keychain-key)# |          | accept-lifetime | duration infinite |
| ---------------------------- | -------- | --------------- | ----------------- |
| switch(config)# vsx          |          |                 |                   |
| switch(config-vsx)#          | vsx-sync | keychain        |                   |
Disablingsynchronizingkeychainconfigurationstothesecondarypeer:
| switch(config)# vsx |             |          |     |
| ------------------- | ----------- | -------- | --- |
| switch(config-vsx)# | no vsx-sync | keychain |     |
vsx-sync lldp
VSXcommands|174

Syntax

vsx-sync lldp
no vsx-sync lldp

Description

Enables VSX synchronization of the LLDP configurations on the primary VSX node to the secondary peer.

The no form of this command disable VSX synchronization of LLDP configurations to the secondary peer,
but it does not remove the existing LLDP feature configurations from the secondary peer switch.

Command context

config-vsx

Authority

Administrators or local user group members with execution rights for this command.

Examples

The first line in the following example shows the setting of an LLDP configuration. The last two lines of the
example show the enabling of VSX synchronization for LLDP configurations.

switch(config)# lldp reinit 6
switch(config)# vsx
switch(config-vsx)# vsx-sync lldp

Disabling VSX synchronization of LLDP configurations:

switch(config)# vsx
switch(config-vsx)# no vsx-sync lldp

vsx-sync loop-protect-global

Syntax

vsx-sync loop-protect-global
no vsx-sync loop-protect-global

Description

Enables the VSX synchronization of global loop protect configurations, such as transmit-interval and re-
enable-timer, on the primary VSX node to the secondary peer switch. To enable VSX synchronization at the
context level for this feature, enter the vsx-sync mclag-interfaces command at the context level.

The no form of this command removes VSX synchronization of global loop protect configurations, but it
does not remove the existing global loop protect feature configurations from the secondary peer switch.

Command context

config-vsx

Authority

Administrators or local user group members with execution rights for this command.

Examples

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

175

Thefirsttwolinesinthefollowingexampleshowthesettingofgloballoopprotectconfigurations.Thelast
twolinesoftheexampleshowtheenablingofVSXsynchronizationforgloballoopprotectconfigurations.
| switch(config)#     | loop-protect | transmit-interval   | 10  |
| ------------------- | ------------ | ------------------- | --- |
| switch(config)#     | loop-protect | re-enable-timer     | 300 |
| switch(config)#     | vsx          |                     |     |
| switch(config-vsx)# | vsx-sync     | loop-protect-global |     |
DisablingVSXsynchronizationofgloballoopprotectconfigurations:
| switch(config)#      | vsx         |                     |     |
| -------------------- | ----------- | ------------------- | --- |
| switch(config-vsx)#  | no vsx-sync | loop-protect-global |     |
| vsx-sync mac-lockout |             |                     |     |
AppliesonlytotheAruba6400SwitchSeries.
Syntax
vsx-sync mac-lockout
no vsx-sync mac-lockout
Description
EnablesVSXsynchronizationoftheMACLockoutconfigurationsontheprimaryVSXnodetothesecondary
peer.
ThenoformofthiscommanddisablessyncingMACLockoutconfigurationstothesecondarypeer.
However,itdoesnotremovetheexistingMACLockoutfeatureconfigurationsfromthesecondarypeer.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVSXsynchronizationforMACLockoutconfigurations:
switch(config)#
|                     | mac-lockout | 10:10:10:10:10:10 |     |
| ------------------- | ----------- | ----------------- | --- |
| switch(config)#     | vsx         |                   |     |
| switch(config-vsx)# | vsx-sync    | mac-lockout       |     |
DisablingVSXsynchronizationforMACLockoutconfigurations:
| switch(config)#           | vsx         |             |     |
| ------------------------- | ----------- | ----------- | --- |
| switch(config-vsx)#       | no vsx-sync | mac-lockout |     |
| vsx-sync mclag-interfaces |             |             |     |
VSXcommands|176

Syntax

vsx-sync mclag-interfaces
no vsx-sync mclag-interfaces

Description

Enables the VSX synchronization of VSX LAG interface associations and attributes on the primary VSX switch
to the secondary peer switch. The Usage section in this topic provides a listing of specific associations and
attributes that are synchronized to the secondary switch.

The no form of this command removes VSX synchronization of global VSX LAG and attributes, but it does
not remove the existing VSX LAG feature configurations from the secondary peer switch.

Command context

config-vsx

Authority

Administrators or local user group members with execution rights for this command.

Usage

The VSX LAG interface associations and attributes that support VSX synchronization are for example:

Interface associations:

n Access lists

n Policies

n QoS

n Port filters

n Rate limits

n VLANs

Supported attributes:

n LAG description

n LACP

n Loop protect

n QoS trust

n sFlow

n STP

This configuration overrides the existing VSX synchronization associations created under the VSX LAG
interface context. Also with this configuration, the system blocks further configuration of VSX
synchronization associations under the VSX LAG context.

Examples

The first four lines in the following example show the creation and configuration of a VSX LAG. The last two
lines of the example show the enabling of VSX synchronization for VSX LAG interface associations and
attributes.

switch(config)# interface lag 1 multi-chassis
switch(config-lag-if)# access-list ip MY_IP_ACL in

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

177

| switch(config-lag-if)# |     | rate-limit | broadcast | 50 kbps |
| ---------------------- | --- | ---------- | --------- | ------- |
switch(config-lag-if)#
|                        |     | qos trust | cos              |     |
| ---------------------- | --- | --------- | ---------------- | --- |
| switch(config-lag-if)# |     | exit      |                  |     |
| switch(config)#        | vsx |           |                  |     |
| switch(config-vsx)#    |     | vsx-sync  | mclag-interfaces |     |
DisablingtheVSXsynchronizationofVSXLAGinterfaceassociationsandattributes:
| switch(config)#      | vsx |             |                  |     |
| -------------------- | --- | ----------- | ---------------- | --- |
| switch(config-vsx)#  |     | no vsx-sync | mclag-interfaces |     |
| vsx-sync nd-snooping |     |             |                  |     |
Syntax
vsx-sync nd-snooping
no vsx-sync nd-snooping
Description
EnablesVSXsynchronizationofNDsnoopingconfigurationsontheprimaryVSXnodetothesecondary
peerswitch.
TosynchronizeNDsnoopingconfigurationsassociatedwithaparticularVLANandinterface,configurethe
sameVLANandinterfaceonthepeerdevice.
ThenoformofthiscommanddisablessyncingNDsnoopingconfigurationstothesecondarypeer,butit
doesnotremovethepreviouslysyncedconfigurationsfromthesecondarypeer.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVSXsyncfortheNDsnoopingconfigurationstothesecondarypeer:
| switch(config)#        | interface   | 1/1/3       |             |            |
| ---------------------- | ----------- | ----------- | ----------- | ---------- |
| switch(config-if)#     | no          | routing     |             |            |
| switch(config-if)#     | nd-snooping |             | trust       |            |
| switch(config)#        | vlan        | 2           |             |            |
| switch(config-vlan-2)# |             | nd-snooping |             |            |
| switch(config-vlan-2)# |             | nd-snooping | ra-drop     |            |
| switch(config-vlan-2)# |             | nd-snooping | prefix-list | 2001::2/64 |
| switch(config)#        | vsx         |             |             |            |
| switch(config-vsx)#    |             | vsx-sync    | nd-snooping |            |
DisablingVSXsyncfortheNDsnoopingconfigurationstothesecondarypeer:
| switch(config)#     | vsx |             |             |     |
| ------------------- | --- | ----------- | ----------- | --- |
| switch(config-vsx)# |     | no vsx-sync | nd-snooping |     |
VSXcommands|178

vsx-sync neighbor
Syntax
vsx-sync neighbor
no vsx-sync neighbor
Description
EnablesVSXsynchronizationofIPv4andIPv6staticneighborsconfigurationonprimaryVSXnodetothe
secondarypeer.Thereisnoconfigurationsyncfromsecondarytoprimarypeer.Ifanynewmodificationor
additionalconfigurationismadeontheprimarynodeforIPv4andIPv6staticneighborsconfiguration,they
willbeauto-synced.
ThenoformofthiscommandVSXsynchronizationofIPv4andIPv6staticneighborsconfigurationstothe
secondarypeer,butitdoesnotremovethepreviouslysyncedconfigurationsfromthesecondarypeer
switch.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVSXsyncfortheIPv4andIPv6staticneighborsconfigurations:
| DUT-1 (config-vsx)# | show run | in vlan127 |
| ------------------- | -------- | ---------- |
interface vlan127
ip address 137.1.1.1/16
| ipv6 | address 7f00::1/64 |                       |
| ---- | ------------------ | --------------------- |
| arp  | ipv4 137.1.1.35    | mac 00:12:01:00:00:1a |
| arp  | ipv4 137.1.1.70    | mac 00:12:01:00:00:3d |
exit
DUT-1(config-vsx)
| switch(config)# vsx |          |          |
| ------------------- | -------- | -------- |
| switch(config-vsx)# | vsx-sync | neighbor |
DisablingVSXsyncfortheIPv4andIPv6staticneighborsconfigurations:
| switch(config)# vsx |             |          |
| ------------------- | ----------- | -------- |
| switch(config-vsx)# | no vsx-sync | neighbor |
vsx-sync ospf
Syntax
vsx-sync ospf
no vsx-sync ospf
Description
EnablessyncingofOSPF(includingOSPFv2andOPSFv3),routemap,andkeychainconfigurationsonthe
primaryVSXswitch.Thereisnoconfigurationsyncfromsecondarytoprimarypeer.
TosynchronizeOSPFconfigurationsattheportlevelcontext,configurethesameportonthepeerdevice.
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 179

ThenoformofthiscommanddisablessyncingofOSPF,routemap,andkeychainconfigurationstothe
secondarypeer.Butitdoesnotremovethepreviouslysyncedconfigurationsfromthesecondarypeer
switch.
TheOSPFrouterIDisnotsynchronized.ThisexclusionisneededbecausetherouterIDuniquelyidentifiesthe
router.ThetwoOSPFrouterswiththesamerouterIDdonotformanadjacencybetweenthem.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVSXsyncfortheOSPFconfigurationstothesecondarypeer:
| switch(config)#          | router | ospf         | 1                  |            |     |            |      |
| ------------------------ | ------ | ------------ | ------------------ | ---------- | --- | ---------- | ---- |
| switch(config-ospf-1)#   |        | area         | 0                  |            |     |            |      |
| switch(config-ospf-1)#   |        | area         | 1 nssa             |            |     |            |      |
| switch(config-ospf-1)#   |        | area         | 2 stub             |            |     |            |      |
| switch(config-ospf-1)#   |        | redistribute |                    | connected  |     | route-map  | map1 |
| switch(config)#          | router | ospfv3       | 1                  |            |     |            |      |
| switch(config-ospfv3-1)# |        |              | max-metric         | router-lsa |     | on-startup |      |
| switch(config-ospfv3-1)# |        |              | bfd all-interfaces |            |     |            |      |
| switch(config-if)#       | ip     | ospf         | 1 area             | 0          |     |            |      |
| switch(config-if)#       | ip     | ospf         | hello-interval     |            | 33  |            |      |
| switch(config-if)#       | ipv6   | ospfv3       | 1                  | area 0     |     |            |      |
| switch(config-if)#       | ipv6   | ospfv3       | dead-interval      |            |     | 55         |      |
| switch(config)#          | vsx    |              |                    |            |     |            |      |
| switch(config-vsx)#      |        | vsx-sync     | ospf               |            |     |            |      |
DisablingVSXsyncfortheOSPFconfigurationstothesecondarypeer:
| switch(config)#        | vsx |             |      |     |     |     |     |
| ---------------------- | --- | ----------- | ---- | --- | --- | --- | --- |
| switch(config-vsx)#    |     | no vsx-sync | ospf |     |     |     |     |
| vsx-sync policy-global |     |             |      |     |     |     |     |
Syntax
vsx-sync policy-global
no vsx-sync policy-global
Description
EnablesVSXsynchronizationofglobalclassifierpolicyconfigurationsontheprimaryVSXnodetothe
secondarypeerswitch.
ThenoformofthiscommanddisablesVSXsynchronizationofglobalpolicyconfigurationstothesecondary
peer,butitdoesnotremovethepreviouslysyncedconfigurationsfromthesecondarypeerswitch.
Commandcontext
config-vsx
VSXcommands|180

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVSXsyncfortheglobalpolicyconfigurationstothesecondarypeer:
| switch(config)#     | apply policy | testPolicy    | in  |
| ------------------- | ------------ | ------------- | --- |
| switch(config)#     | vsx          |               |     |
| switch(config-vsx)# | vsx-sync     | policy-global |     |
DisablingVSXsyncfortheglobalpolicyconfigurationstothesecondarypeer:
| switch(config)#     | vsx |                        |     |
| ------------------- | --- | ---------------------- | --- |
| switch(config-vsx)# | no  | vsx-sync policy-global |     |
| vsx-sync qos-global |     |                        |     |
Syntax
vsx-sync qos-global
no vsx-sync qos-global
Description
EnablestheVSXsynchronizationofglobalQoSconfigurations,suchasCoSmap,DSCPmap,andtrustpolicy,
ontheprimaryVSXnodetothesecondarypeerswitch.ToenableVSXsynchronizationatthecontextlevel
| forthisfeature,enterthevsx-sync |     | qoscommandatthecontextlevel. |     |
| ------------------------------- | --- | ---------------------------- | --- |
ThenoformofthiscommandremovesVSXsynchronizationofglobalQoSconfigurations,butitdoesnot
removetheexistingglobalQoSfeatureconfigurationsfromthesecondarypeerswitch.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ThefirstfivelinesinthefollowingexampleshowthesettingofglobalQoSconfigurations.Thelasttwolines
oftheexampleshowtheenablingofVSXsynchronizationforglobalQoSconfigurations.
| switch(config)# | qos cos-map | 1 local-priority | 0   |
| --------------- | ----------- | ---------------- | --- |
| switch(config)# | qos cos-map | 0 local-priority | 1   |
switch(config)#
|                     | qos cos-map  | 2 local-priority | 2   |
| ------------------- | ------------ | ---------------- | --- |
| switch(config)#     | qos dscp-map | 2 local-priority | 3   |
| switch(config)#     | qos trust    | dscp             |     |
| switch(config)#     | vsx          |                  |     |
| switch(config-vsx)# | vsx-sync     | qos-global       |     |
DisablingVSXsynchronizationofglobalQoSconfigurations:
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 181

| switch(config)# | vsx |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
switch(config-vsx)#
|                    | no  | vsx-sync | qos-global |     |     |     |
| ------------------ | --- | -------- | ---------- | --- | --- | --- |
| vsx-sync route-map |     |          |            |     |     |     |
Syntax
vsx-sync route-map
no vsx-sync route-map
Description
EnablessyncingofallAsPathlists,communitylists,prefixlists,androutemapconfigurationsonprimary
VSXnodetothesecondarypeerswitch.Thereisnoconfigurationsyncfromthesecondarytoprimarypeer.
ThenoformofthiscommanddisablessyncingofAsPathlists,communitylists,prefixlists,androutemap
configurationstothesecondarypeer,butitdoesnotremovethepreviouslysyncedconfigurationsfromthe
secondarypeerswitch.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVSXsyncfortheroutemapconfigurations:
| switch(config)# | ip aspath-list    |     | list1    | seq 10 | permit 10     |     |
| --------------- | ----------------- | --- | -------- | ------ | ------------- | --- |
| switch(config)# | ip community-list |     | expanded | com1   | seq 10 permit | 10  |
switch(config)# ip extcommunity-list standard ext1 seq 10 permit rt 10:4
| switch(config)#                  | ip prefix-list |           | pref1 seq | 10 permit   | any     |     |
| -------------------------------- | -------------- | --------- | --------- | ----------- | ------- | --- |
| switch(config)#                  | route-map      | rm1       | permit    |             |         |     |
| switch(config-route-map-rm1-10)# |                |           | match     | ip next-hop | 1.1.1.1 |     |
| switch(config)#                  | vsx            |           |           |             |         |     |
| switch(config-vsx)#              | vsx-sync       | route-map |           |             |         |     |
DisablingVSXsyncfortheroutemapconfigurations:
| switch(config)#     | vsx |          |           |     |     |     |
| ------------------- | --- | -------- | --------- | --- | --- | --- |
| switch(config-vsx)# | no  | vsx-sync | route-map |     |     |     |
| vsx-sync sflow      |     |          |           |     |     |     |
Syntax
vsx-sync sflow
no vsx-sync sflow
Description
EnablesVSXsynchronizationofthesFlowconfigurationsontheprimaryVSXnodetothesecondarypeer.
VSXcommands|182

The no form of this command removes VSX synchronization of global sFlow configurations, but it does not
remove the existing global sFlow feature configurations from the secondary peer switch.

Command context

config-vsx

Authority

Administrators or local user group members with execution rights for this command.

Usage

To maintain compliance with sFlow collector functionality for non-VSX topology, the vsx-sync sflow
command on primary VSX peer is expected to sync all sFlow configurations, except for the agent-ip
configuration. This exclusion is required for sFlow collector functionality to work seamlessly even with VSX
topology. To synchronize sFlow configurations associated with particular VRF, you must configure the same
VRF on the peer device.

Examples

The first line in the following example shows the setting of an sFlow configuration. The last two lines of the
example show the enabling of VSX synchronization for sFlow configurations.

switch(config)# sflow agent-ip 10.0.0.100
switch(config)# vsx
switch(config-vsx)# vsx-sync sflow

Disabling VSX synchronization of global sFlow configurations:

switch(config)# vsx
switch(config-vsx)# no vsx-sync sflow

vsx-sync sflow-global

Syntax

vsx-sync sflow-global
no vsx-sync sflow-global

Description

Enables VSX synchronization of the sFlow global configurations on the primary VSX node to the secondary
peer.

To synchronize sFlow configurations associated with a particular VRF, you must configure the same VRF on
the peer device.

The no form of this command disables VSX synchronization of global sFlow configurations, but it does not
remove the existing sFlow feature configurations from the secondary peer switch.

Command context

config-vsx

Authority

Administrators or local user group members with execution rights for this command.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

183

Usage
TomaintaincompliancewithsFlowcollectorfunctionalityfornon-VSXtopology,thevsx-sync
sflow
commandonprimaryVSXpeerisexpectedtosyncallsFlowconfigurations,exceptfortheagent-ip
configuration.ThisexclusionisrequiredforsFlowcollectorfunctionalitytoworkseamlesslyevenwithVSX
topology.VSXsyncsonlytheglobalsFLowconfigurationsandnotthesFlowconfigurationsunderphysical
orLAGinterfaces.
Examples
ThefirstlineinthefollowingexampleshowsthesettingofansFlowconfiguration.Thelasttwolinesofthe
exampleshowtheenablingofVSXsynchronizationforsFlowconfigurations.
| switch(config)#     | sflow collector | 1.1.1.1      |
| ------------------- | --------------- | ------------ |
| switch(config)#     | vsx             |              |
| switch(config-vsx)# | vsx-sync        | sflow-global |
DisablingVSXsynchronizationofglobalsFlowconfigurations:
| switch(config)#     | vsx         |              |
| ------------------- | ----------- | ------------ |
| switch(config-vsx)# | no vsx-sync | sflow-global |
| vsx-sync snmp       |             |              |
Syntax
vsx-sync snmp
no vsx-sync snmp
Description
EnablesVSXsynchronizationofSNMPconfigurationsontheprimaryVSXnodetothesecondarypeer.To
synchronizeSNMPconfigurationsassociatedwithaparticularVRF,youmustconfigurethesameVRFonthe
peerdevice.
ThenoformofthiscommandremovesVSXsynchronizationofglobalSNMPconfigurations,butitdoesnot
removetheexistingglobalSNMPfeatureconfigurationsfromthesecondarypeerswitch.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVSXsynchronizationforSNMPconfiguration:
| switch(config)#     | vsx      |      |
| ------------------- | -------- | ---- |
| switch(config-vsx)# | vsx-sync | snmp |
DisablingVSXsynchronizationforSNMPconfiguration:
VSXcommands|184

switch(config)# vsx
switch(config-vsx)# no vsx-sync snmp

vsx-sync ssh

Syntax

vsx-sync ssh
no vsx-sync ssh

Description

Enables VSX synchronization of SSH server configurations on the primary VSX node to the secondary peer
switch. To synchronize SSH configurations associated with particular VRF, you must configure the same VRF
on the peer device.

The no form of this command removes VSX synchronization of global SSH configurations, but it does not
remove the existing global SSH feature configurations from the secondary peer switch.

Command context

config-vsx

Authority

Administrators or local user group members with execution rights for this command.

Examples

The first line in the following example shows the setting of an SSH server configuration. The last two lines of
the example show the enabling of VSX synchronization for SSH server configurations.

switch(config)# ssh certified-algorithms-only
switch(config)# vsx
switch(config-vsx)# vsx-sync ssh

Disabling VSX synchronization for global SSH server configurations:

switch(config)# vsx
switch(config-vsx)# no vsx-sync ssh

vsx-sync static-routes

Syntax

vsx-sync static-routes
no vsx-sync static-routes

Description

Enables VSX synchronization of static route configurations on the primary VSX node to the secondary peer
switch. To synchronize static route configurations associated with particular VRF, you must configure the
same VRF on the peer switch.

The no form of this command removes VSX synchronization of global static route configurations, but it does
not remove the existing global static route feature configurations from the secondary peer switch.

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

185

Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVSXsynchronizationforstaticroutes:
| switch(config)#     | vsx      |               |     |
| ------------------- | -------- | ------------- | --- |
| switch(config-vsx)# | vsx-sync | static-routes |     |
DisablingVSXsynchronizationforstaticroutes:
| switch(config)# | vsx |     |     |
| --------------- | --- | --- | --- |
switch(config-vsx)#
|                     | no vsx-sync | static-routes |     |
| ------------------- | ----------- | ------------- | --- |
| vsx-sync stp-global |             |               |     |
Syntax
vsx-sync stp-global
no vsx-sync stp-global
Description
EnablestheVSXsynchronizationofglobalSTPconfigurationsontheprimaryVSXnodetothesecondary
peerswitch.Usethevsx-sync mclag-interfacescommandtosynccontextlevelspanningtrees.Toenable
VSXsynchronizationatthecontextlevelforthisfeature,enterthevsx-sync mclag-interfacescommand
atthecontextlevel.
ThenoformofthiscommandremovesVSXsynchronizationofglobalSTPconfigurations,butitdoesnot
removetheexistingglobalSTPfeatureconfigurationsfromthesecondarypeerswitch.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ThefirsttwolinesinthefollowingexampleshowthesettingofglobalSTPconfigurations.Thelasttwolines
oftheexampleshowtheenablingofVSXsynchronizationforglobalSTPconfigurations.
| switch(config)#     | spanning-tree | config-name     | abc |
| ------------------- | ------------- | --------------- | --- |
| switch(config)#     | spanning-tree | config-revision | 1   |
| switch(config)#     | vsx           |                 |     |
| switch(config-vsx)# | vsx-sync      | stp-global      |     |
DisablingVSXsynchronizationofglobalSTPconfigurations:
VSXcommands|186

| switch(config)# | vsx |     |
| --------------- | --- | --- |
switch(config-vsx)#
|               | no vsx-sync | stp-global |
| ------------- | ----------- | ---------- |
| vsx-sync time |             |            |
Syntax
vsx-sync time
no vsx-sync time
Description
EnablesVSXsynchronizationoftime-relatedconfigurations,includingNTPandtimezoneconfigurations,on
theprimaryVSXnodeonthesecondarypeerswitch.TosynchronizeNTPconfigurationsassociatedwitha
particularVRF,youmustconfigurethesameVRFonthepeerswitch.
ThenoformofthiscommandremovesVSXsynchronizationofglobaltime-relatedconfigurations,butit
doesnotremovetheexistingglobaltime-relatedfeatureconfigurationsfromthesecondarypeerswitch.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Thefirsttwolinesinthefollowingexampleshowthesettingoftime-relatedconfigurations.Thelasttwo
linesoftheexampleshowtheenablingofVSXsynchronizationfortime-relatedconfigurations.
| switch(config)#     | ntp authentication |      |
| ------------------- | ------------------ | ---- |
| switch(config)#     | clock timezone     | utc  |
| switch(config)#     | vsx                |      |
| switch(config-vsx)# | vsx-sync           | time |
DisablingVSXsynchronizationfortime-relatedconfigurations:
| switch(config)#        | vsx         |      |
| ---------------------- | ----------- | ---- |
| switch(config-vsx)#    | no vsx-sync | time |
| vsx-sync udp-forwarder |             |      |
Syntax
vsx-sync udp-forwarder
no vsx-sync udp-forwarder
Description
EnablesVSXsynchronizationofUDPforwarderconfigurationsontheprimaryVSXnodetothesecondary
peer.
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 187

The no form of the command disables the VSX synchronization of UDP forwarder configurations to the
secondary peer; however, it does not remove the existing udp-forwarder configurations from the secondary
VSX peer.

Command context

config-vsx

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling VSX synchronization for UDP forwarder configurations:

switch(config)# vsx
switch(config-vsx)# vsx-sync udp-forwarder

Disabling VSX synchronization for UDP forwarder configurations:

switch(config)# vsx
switch(config-vsx)# no vsx-sync udp-forwarder

vsx-sync vrrp

Syntax

vsx-sync vrrp
no vsx-sync vrrp

Description

Enables VSX synchronization of all VRRP configurations on the primary VSX node to the secondary peer
switch. There is no configuration sync from secondary to primary peer.

To synchronize VRRP configurations at the port level context, the same port must be configured on the peer
device with IP address.

The no form of this command disables syncing VRRP configurations to the secondary peer, but it does not
remove the previously synced configurations from the secondary peer.

BFD IP is the IP address of VRRP peer device. Hence it cannot be synced.

In the owner scenario, in case the priority is synced, both VSX primary and secondary devices will have 255 as

their priority. If the primary device goes down and comes up again, the secondary device will still act as the

master in spite of the primary device being the owner. Hence priority cannot be synced.

Command context

config-vsx

Authority

Administrators or local user group members with execution rights for this command.

Examples

VSX commands | 188

EnablingVSXsyncfortheVRRPconfigurationstothesecondarypeer:
| switch(config)#         |     | router | vrrp    | enable         |         |
| ----------------------- | --- | ------ | ------- | -------------- | ------- |
| switch(config-if)#      |     | vrrp   | 1       | address-family | ipv4    |
| switch(config-if-vrrp)# |     |        | address | 1.1.1.100      | primary |
| switch(config-if-vrrp)# |     |        | timers  | advertise      | 1000    |
| switch(config-if-vrrp)# |     |        | no      | shutdown       |         |
| switch(config-if)#      |     | vrr    | 1       | address-family | ipv6    |
switch(config)#
vsx
| switch(config-vsx)# |     |     | vsx-sync | vrrp |     |
| ------------------- | --- | --- | -------- | ---- | --- |
DisablingVSXsyncfortheVRRPconfigurationstothesecondarypeer:
| switch(config)#     |            | vsx |             |      |     |
| ------------------- | ---------- | --- | ----------- | ---- | --- |
| switch(config-vsx)# |            |     | no vsx-sync | vrrp |     |
| vsx-sync            | vsx-global |     |             |      |     |
Syntax
| vsx-sync    | vsx-global |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | --- |
| no vsx-sync | vsx-global |     |     |     |     |
Description
EnablesVSXsynchronizationofglobalVSXconfigurationsontheprimaryVSXnodetothesecondarypeer.
ThenoformofthecommanddisablesVSXsynchronizationofglobalVSXconfigurationstothesecondary
peer;however,itdoesnotremovetheexistingVSXfeatureconfigurationsfromthesecondarypeer.
Commandcontext
config-vsx
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
ThefollowingcommandsaresyncedfromprimaryVSXnodetosecondaryVSXnode:
| n inter-switch-link |               | dead-interval        |                 | <DEAD-INTERVAL>  |                        |
| ------------------- | ------------- | -------------------- | --------------- | ---------------- | ---------------------- |
| n inter-switch-link |               | hello-interval       |                 | <HELLO-INTERVAL> |                        |
| n inter-switch-link |               | hold-time            |                 | <HOLD-INTERVAL>  |                        |
| n inter-switch-link |               | peer-detect-interval |                 |                  | <PEER-DETECT-INTERVAL> |
| keepalive           | dead-interval |                      | <DEAD-INTERVAL> |                  |                        |
n
| n keepalive          | hello-interval |               | <HELLO-INTERVAL> |     |     |
| -------------------- | -------------- | ------------- | ---------------- | --- | --- |
| n keepalive          | udp-port       | <PORT-NUM>    |                  |     |     |
| n linkup-delay-timer |                | <DELAY-TIMER> |                  |     |     |
n split-recovery
| n system-mac | <MAC-ADDR> |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- |
Examples
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 189

ThefirstthreelinesinthefollowingexampleshowthesettingofglobalVSXconfigurations.Thelastlinein
theexampleshowstheenablingofVSXsynchronizationforglobalVSXconfigurations.
| switch(config)#     | vsx               |                |     |
| ------------------- | ----------------- | -------------- | --- |
| switch(config-vsx)# | inter-switch-link | dead-interval  | 15  |
| switch(config-vsx)# | inter-switch-link | hello-interval | 2   |
| switch(config-vsx)# | inter-switch-link | hold-time      | 1   |
| switch(config-vsx)# | vsx-sync          | vsx-global     |     |
DisablingVSXsynchronizationforglobalVSXconfigurations:
| switch(config)#     | vsx         |            |     |
| ------------------- | ----------- | ---------- | --- |
| switch(config-vsx)# | no vsx-sync | vsx-global |     |
vsx update-software
Syntax
| vsx update-software | <REMOTE-URL> | [vrf <VRF-NAME>] |     |
| ------------------- | ------------ | ---------------- | --- |
Description
Thiscommandletsyouupdatethesoftware.
Commandcontext
Manager(#)
Parameters
<REMOTE-URL>
SpecifiestheTFTPURLfordownloadingthesoftware.Syntax:tftp://{<IP-ADDRESS>|<HOSTNAME>}
[:<PORT>][;blocksize=<VAL>]/<FILE-NAME>
vrf <VRF-NAME>
SpecifiestheVRFnamefordownloadingthesoftware.Optional
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
ThiscommandgivesyoutheoptiontosavetherunningconfigurationontheprimaryandsecondaryVSX
switches.Afterthecommandsavestherunningconfiguration,itdownloadsnewsoftwarefromtheTFTP
serverandverifiesthedownload.Afterasuccessfulverification,thecommandinstallsthesoftwaretothe
alternativeimageofboththeVSXprimaryandsecondaryswitches.
ThecommanddisplaysthestatusoftheVSXprimaryandsecondaryswitchesduringtheupgrade.The
commandalsorefreshestheprogressbarastheimageupdateprogresses.DonotinterrupttheVSX
primaryCLIsessionuntilthesoftwareupdatescompletes;however,softwareupdateprocesscanbe
stopped.Ifyoustoptheupgradewhenthesecondaryswitchhasalreadyinstalledtheimageinitsflash
memoryorthesecondaryswitchhasstartedthereboottheprocess,itcomesupwiththenewsoftware.
Theprimaryswitchcontinuestohavewitholdersoftware.Youcanstopthesoftwareupdateprocessby
pressingctrl+c.
Example
VSXcommands|190

Updating the software using TFTP:

switch# vsx update-software tftp://192.168.1.1/XL.10.0x.xxxx vrf mgmt
Do you want to save the current configuration (y/n)? y
The running configuration was saved to the startup configuration.

This command will download new software to the %s image of both the VSX primary and
secondary systems, then reboot them in sequence. The VSX secondary will reboot
first, followed by the primary.
Continue (y/n)? y
VSX Primary Software Update Status
VSX Secondary Software Update Status
VSX ISL Status
Progress
[..........................................................................]
Secondary VSX system updated completely. Rebooting primary.

: <VSX primary software update status>
: <VSX secondary software update status>
: <VSX ISL status>

vsx update-software boot-bank

Syntax

vsx update-software boot-bank {primary | secondary}

Description

Upgrades the VSX pairs using the specified bank on both the devices. This command compares whether the
image versions are same in both the primary and secondary switches and reboots them in sequence, the
VSX secondary switch followed by VSX primary switch.

Before executing this command, download the software image and install in the required boot banks.

Command context

Manager (#)

Parameters

boot-bank

Specifies the boot bank where the image is pre-staged .

{primary | secondary}

Selects either primary or secondary VSX switch for the software upgrade.

Authority

Administrators or local user group members with execution rights for this command.

Usage

This command gives you the option to save the running configuration on the primary and secondary VSX
switches. After the command saves the running configuration, it downloads new software from the TFTP
server and verifies the download. After a successful verification, the command installs the software to the
alternative image of both the VSX primary and secondary switches.

The command displays the status of the VSX primary and secondary switches during the upgrade. The
command also refreshes the progress bar as the image update progresses. Do not interrupt the VSX primary
CLI session until the software updates completes; however, software update process can be stopped. If you
stop the upgrade when the secondary switch has already installed the image in its flash memory or the

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

191

secondaryswitchhasstartedthereboottheprocess,itcomesupwiththenewsoftware.Theprimaryswitch
continuestohavewitholdersoftware.Youcanstopthesoftwareupdateprocessbypressingctrl+c.
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
Progress [.......................................................................]
| Secondary | VSX system | updated completely. | Rebooting | primary. |
| --------- | ---------- | ------------------- | --------- | -------- |
VSXcommands|192

Chapter 13
Troubleshooting
Troubleshooting
ISL is out-of-sync
Solution 1
Cause
MismatchwiththeISLversionorswitchplatformorboth.
Action
| 1. Runtheshow vsx | statuscommand. |     |     |
| ----------------- | -------------- | --- | --- |
Inthefollowingexample,theISLchannelisshownasin-sync;however,iftheISLchannelwasnotin-
sync,adifferentstatuswouldbeprovided.
| switch# show    | vsx   | status |     |
| --------------- | ----- | ------ | --- |
| VSX Operational | State |        |     |
---------------------
| ISL channel       |             | : In-Sync          |                   |
| ----------------- | ----------- | ------------------ | ----------------- |
| ISL mgmt          | channel     | : operational      |                   |
| Config            | Sync Status | : in-sync          |                   |
| NAE               |             | : peer_unreachable |                   |
| HTTPS Server      |             | : peer_unreachable |                   |
| Attribute         |             | Local              | Peer              |
| ------------      |             | --------           | --------          |
| ISL link          |             | 1/1/43             | 1/1/43            |
| ISL version       |             | 2                  | 2                 |
| System MAC        |             | 48:0f:cf:af:70:84  | 48:0f:cf:af:c2:84 |
| Platform          |             | 8320               | 8320              |
| Software          | Version     | 10.0x.xxxx         | 10.0x.xxxx        |
| Device Role       |             | primary            | secondary         |
| switch(config)#   | user        | admin password     |                   |
| Changing password | for         | user admin         |                   |
Enter password:************
Confirm password:************
2. IfthereisanISLversionmismatch,updatethesoftwaresotheISLversionisthesameonthelocal
andpeerVSXswitch.
3. Iftheswitcheshavemismatchingplatforms,createanISLlinkthatconnectstwoVSXswitcheswith
thesameplatform.
Solution 2
Cause
TheroleisnotconfiguredonanyoftheVSXswitchesorthesameroleisconfiguredonbothVSXswitches.
Action
193
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide| (6400,8xxxSwitchSeries)

| 1.  | Runtheshow | vsx | statuscommand. |     |     |     |
| --- | ---------- | --- | -------------- | --- | --- | --- |
Iftherolesaresetincorrectly,thecommanddisplaystherole inconsistentstatus.
2. SettherolescorrectlysothatoneoftheVSXswitcheshastheprimaryroleandtheotherswitchhas
thesecondaryrole.Tosetaswitchrole,entertherole {primary | secondary}command.
| Solution | 3   |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
Cause
TheISLinterfaceisdownonanyoneswitchintheVSXpair.
Action
1. CheckISLstateandISLlinkstatusbyentering:switch# show vsx status inter-switch-link
Inthefollowingexample,theISLstateandlinkstatusareshownasin-syncandup;however,ifthe
ISLinterfaceisdown,adifferentstatuswouldbeprovided.
|     | switch#      | show   | vsx status |            | inter-switch-link |     |
| --- | ------------ | ------ | ---------- | ---------- | ----------------- | --- |
|     | State        |        |            |            | : In-Sync         |     |
|     | Link         | Status |            |            | : up              |     |
|     | Mgmt         | state  |            |            | : operational     |     |
|     | Inter-switch |        | link       | Statistics |                   |     |
----------------------------
|     | Hello | Packets | Tx    |     | : 4572  |     |
| --- | ----- | ------- | ----- | --- | ------- | --- |
|     | Hello | Packets | Rx    |     | : 4573  |     |
|     | Data  | Packets | Tx    |     | : 80634 |     |
|     | Data  | Packets | Rx    |     | : 80637 |     |
|     | Mgmt  | Packets | Tx    |     | : 25946 |     |
|     | Mgmt  | Packets | Rx    |     | : 25167 |     |
|     | Mgmt  | Packet  | Drops |     | : 0     |     |
2. Re-enabletheISLinterfacebygoingtothatinterfacecontextandenteringno shutdown:
|        | switch(config)#    |          | interface |             | 1/1/1 |     |
| ------ | ------------------ | -------- | --------- | ----------- | ----- | --- |
|        | switch(config-if)# |          |           | no shutdown |       |     |
| ISL is | in                 | blocking |           | state       |       |     |
Symptom
TheVSXLAGsareshownasBlockingintheoutputoftheshow spanning-tree detailcommand.
| switch#  | show | spanning-tree |           | detail |           |      |
| -------- | ---- | ------------- | --------- | ------ | --------- | ---- |
| Spanning | tree | status        | : Enabled |        | Protocol: | MSTP |
MST0
| Root | ID Priority  |        | : 32768           |             |         |                 |
| ---- | ------------ | ------ | ----------------- | ----------- | ------- | --------------- |
|      | MAC-Address: |        | 02:02:02:02:02:02 |             |         |                 |
|      | This         | bridge | is the            | root        |         |                 |
|      | Hello        | time   | (in seconds):2    |             | Max Age | (in seconds):20 |
|      | Forward      | Delay  | (in               | seconds):15 |         |                 |
Troubleshooting|194

Bridge ID Priority: 32768

MAC-Address: 02:02:02:02:02:02
Hello time (in seconds):2 Max Age (in seconds):20
Forward Delay (in seconds):15

Role

State

Port
------ -------- -------- ------ -------- -------
lag1
Disabled Blocking 20000 64
lag100 Disabled Blocking 20000 64

shared
shared

Priority Type

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

When you run the show vsx status command, verify that the ISL is in-sync.

2. Verify that the VSX peer switches are in the active and standby role when the ISL is the in-sync state

by entering the show spanning-tree detail command:

switch# show spanning-tree detail
Spanning tree status : Enabled Protocol: MSTP

MST0
Root ID Priority : 32768

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

195

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
Disabled Blocking 20000 64
lag1
lag100 Disabled Blocking 20000 64

shared
shared

Priority Type

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

The admin path cost configured on downstream switches results in the VSX pair seeing the root
switch as equal cost to the root switch from both VSX pair switches.

Traffic drop on a VSX LAG interface
Take the following actions:

1. Verify that the VSX LAG interface is in-sync with both peer and down stream switches by entering:

switch# show lacp interfaces multi-chassis

2. Verify that the VLAN membership of the VSX is the same on both VSX switches by entering:

switch# show vsx config-consistency lacp <LAG-NAME>

Troubleshooting | 196

3. VerifythatallMACaddressesareprogrammedcorrectlyonbothVSXswitchesbyentering:
|           | switch# show | mac-address-table |          |             |     |
| --------- | ------------ | ----------------- | -------- | ----------- | --- |
|           | switch# show | mac-address-table | count    |             |     |
| Traffic   | loss after   | the ISL           | has been | out-of-sync | and |
| keepalive | is           | down              |          |             |     |
Symptom
TrafficlossisseenaftertheISLhasbeenout-of-syncandkeepaliveisdown.
Cause
IftheISLbecomesout-of-syncandkeepaliveisestablished,thesecondaryVSXLAGsarebroughtdown.If
keepalivethenfailsandyouhavesplitrecoverymodeenabled(defaultsetting),thesecondaryswitchbrings
upitsVSXLAGs.Thissplitconditionleadstotrafficlossbecauseoftheasymmetrictrafficflow.
Action
1. DisablesplitrecoverymodebyenteringthefollowingcommandonthesecondaryVSXswitch:
|     | switch(config)#     | vsx               |     |     |     |
| --- | ------------------- | ----------------- | --- | --- | --- |
|     | switch(config-vsx)# | no split-recovery |     |     |     |
Thiscommandshutsdownthesecondarylinktostoptheasymmetrictrafficflow.
2. ApplythesamesettingontheprimaryVSXswitchforconsistencyandincasethereisa
primary/secondaryroleswapintheconfiguration.
| Failure | scenarios | and | split recovery |     |     |
| ------- | --------- | --- | -------------- | --- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 197

| Figure 21 | ExampleTopology  |             |                |             |                |     |
| --------- | ---------------- | ----------- | -------------- | ----------- | -------------- | --- |
| Table 6:  | FailureScenarios |             |                |             |                |     |
|           |                  | Result with | split recovery | Result with | split recovery | on  |
| Failure   | scenarios        |             |                |             |                |     |
off (default)
KeepaliveisdownandISLisup.This Noimpact,exceptforthelossofthe
Noimpact,exceptfortheloss
| scenarioisshownwithlabel"b"in |     |     |     | splitdetection. |     |     |
| ----------------------------- | --- | --- | --- | --------------- | --- | --- |
ofthesplitdetection.
thefigure.
ISLisdown,butkeepaliveisup.This SecondaryVSXswitchbrings SecondaryVSXswitchbringsdown
| scenarioisshownwithlabel"a"in |     |     |     | VSXLAGmemberports. |     |     |
| ----------------------------- | --- | --- | --- | ------------------ | --- | --- |
downVSXLAGmemberports.
thefigure.
ISLisdown,butkeepaliveisup,as
SecondaryVSXswitchbrings Labela:ThesecondaryVSXswitch
shownwithlabel"a"inthefigure.
downVSXLAGmemberports. bringsdownVSXLAGmemberports.
Then,aftersometime,keepalivealso
Then,thesecondaryVSXLAGs
| goesdown,asshownwithlabelb. |     |     |     | Labelb:ThesecondaryVSXswitch |     |     |
| --------------------------- | --- | --- | --- | ---------------------------- | --- | --- |
staydown.
restoresVSXLAGmemberports.
Atthesametime,ISLgoesdownand
Labelaandb:AllVSXLAGports Labelaandb:AllVSXLAGportsstay
keepalivegoesdown,asshownwith
stayup. up.
label"a"and"b"inthefollowing
figure.Then,keepaliveisrestored,as Labelb:Then,thesecondary Labelb:Then,thesecondaryVSX
shownwithlabelb. VSXswitchbringsdowntheVSX switchbringsdowntheVSXLAG
LAGmemberports. memberports.
| Active | gateway | is unreachable |     |     |     |     |
| ------ | ------- | -------------- | --- | --- | --- | --- |
Symptom
Youareunabletopingtheactivegateway.
Troubleshooting|198

Action
1. Verifythatkernelinterfaceiscreatedforactivegateway:
003000000000001@vlan3: <NO-CARRIER,BROADCAST,UP,M-DOWN> mtu 1500 qdisc noqueue
state
|     | LOWERLAYERDOWN |     | group             | default | qlen | 1000                  |     |     |
| --- | -------------- | --- | ----------------- | ------- | ---- | --------------------- | --- | --- |
|     | link/ether     |     | 00:00:00:00:00:01 |         |      | brd ff:ff:ff:ff:ff:ff |     |     |
2. VerifythattheactivegatewayIPisprogrammedcorrectlyonkernelinterface:
003000000000001@vlan3: <NO-CARRIER,BROADCAST,UP,M-DOWN> mtu 1500 qdisc noqueue
state
|     | LOWERLAYERDOWN |             | group             | default       | qlen   | 1000                  |     |     |
| --- | -------------- | ----------- | ----------------- | ------------- | ------ | --------------------- | --- | --- |
|     | link/ether     |             | 00:00:00:00:00:01 |               |        | brd ff:ff:ff:ff:ff:ff |     |     |
|     | inet           | 10.0.0.3/32 |                   | scope         | global | 003000000000001       |     |     |
|     | valid_lft      |             | forever           | preferred_lft |        | forever               |     |     |
|     | inet           | 20.0.0.3/32 |                   | scope         | global | 003000000000001       |     |     |
|     | valid_lft      |             | forever           | preferred_lft |        | forever               |     |     |
3. VerifythattheactivegatewayVMACiscorrectlyconfiguredinthehardware.Thecommandusedis
platform-specific.Refertothehardwaredocumentationforyourswitch.
Thefollowingexamplefromthe8400seriesswitch:
|     | 8400X:/home/admin# |     |     | ovs-appctl | l3pd/show | router-mac | –a      |           |
| --- | ------------------ | --- | --- | ---------- | --------- | ---------- | ------- | --------- |
| BFD | reports            | a   | LAG | as down    |           | even when  | healthy | links are |
still available
Symptom
TheBidirectionalForwardDetection(BFD)featurereportsaLinkAggregation(LAG),asbeingdown,even
thoughtherearehealthyLAGlinksavailable.TheLAG,containingthedownedlink,willeventuallyrebalance
thetraffictoitsotherlinks.
Cause
ThisnotificationoccurswhentheminimumBFDcontrolpacketreceptionintervalissetatafasterratethan
theLinkAggregationControlProtocol(LACP)rateandLAGrebalancingoccurs.BFDassumesthatthelinkis
downwithoutrealizingthattheLAGisrebalancingthetrafficload.
Action
1. SettheminimumBFDcontrolpacketreceptionintervaltoaslowerratethantheLACPrateorsetthe
LACPratetoafasterratethantheminimumBFDcontrolpacketreceptioninterval.
a. TofindthecurrentsettingsoftheminimumBFDcontrolpacketreceptioninterval,enterthe
show running-configcommand.
TheminimumBFDcontrolpacketreceptionintervalsettingislistedasbfd min-receive-
intervalinthecommandoutputandthemeasurementisinms.
b. TofindthecurrentrateofLACP,entertheshow lacp aggregatescommand.
|     | TheLACPrateislistedastheHeatbeat |     |     |     |     | rateinthecommandoutput. |     |     |
| --- | -------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- |
AOS-CX10.07VirtualSwitchingExtension(VSX)Guide|(6400,8xxxSwitchSeries) 199

c. To change the minimum BFD control packet reception interval, enter the bfd min-receive-

interval command.

d. To change the LACP rate, enter the lacp rate {fast | slow} command.

Ping between VSX peer IP addresses fails

Symptom

For the native VLAN, tag is the default option. As a result, if the ISL is configured as vlan trunk native 1
(without tag), the ping between VSX peer IP addresses can fail because of a mismatch in the source VLAN
number.

This issue impacts 6400 and 8360 Switch series only.

Action

For ISL, configure the native VLAN with the tag option.

switch# vlan trunk native 1 tag

Troubleshooting | 200

Support and Other Resources

Chapter 14

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

AOS-CX 10.07 Virtual Switching Extension (VSX) Guide | (6400, 8xxx Switch Series)

201

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

Support and Other Resources | 202