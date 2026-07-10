| AOS-CX |       | 10.07 | Multicast |       |      | Guide  |
| ------ | ----- | ----- | --------- | ----- | ---- | ------ |
| 6300,  | 6400, | 8320, | 8325,     | 8360, | 8400 | Switch |
Series
PartNumber:5200-7876a
Published:June2021
Edition:1

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

| 2

Contents
Contents
| Contents                                         |                                      |          |        | 3   |
| ------------------------------------------------ | ------------------------------------ | -------- | ------ | --- |
| About                                            | this document                        |          |        | 11  |
| Applicableproducts                               |                                      |          |        | 11  |
| Latestversionavailableonline                     |                                      |          |        | 11  |
| Commandsyntaxnotationconventions                 |                                      |          |        | 11  |
| Abouttheexamples                                 |                                      |          |        | 12  |
| Identifyingswitchportsandinterfaces              |                                      |          |        | 12  |
| Identifyingmodularswitchcomponents               |                                      |          |        | 13  |
| Multicast                                        | overview                             |          |        | 15  |
| Multicastprotocols                               |                                      |          |        | 15  |
| Multicastaddresses                               |                                      |          |        | 16  |
| Internet                                         | Group Management                     | Protocol | (IGMP) | 17  |
| IGMPdefaults,protocols,andsupportedconfiguration |                                      |          |        | 17  |
| HowtheIGMPprotocolworks                          |                                      |          |        | 17  |
| ConsiderationswhenconfiguringIGMP                |                                      |          |        | 18  |
| IGMPconfigurationtasklist                        |                                      |          |        | 19  |
| EnablingordisablingIGMP                          |                                      |          |        | 19  |
| SpecifyingtheIGMPversion                         |                                      |          |        | 19  |
| ConfiguringIGMPstaticgroups                      |                                      |          |        | 20  |
| ConfiguringIGMPqueryandresponseparameters        |                                      |          |        | 20  |
| DisablingIGMP                                    |                                      |          |        | 21  |
| ViewingIGMPinformation                           |                                      |          |        | 21  |
| IGMPconfigurationexample                         |                                      |          |        | 22  |
| IGMPcommands                                     |                                      |          |        | 22  |
|                                                  | ipigmp                               |          |        | 23  |
|                                                  | ipigmpapplyaccess-list               |          |        | 23  |
|                                                  | ipigmplast-member-query-interval     |          |        | 24  |
|                                                  | ipigmpquerier                        |          |        | 25  |
|                                                  | ipigmpquerierinterval                |          |        | 25  |
|                                                  | ipigmpquerierquery-max-response-time |          |        | 26  |
|                                                  | ipigmprobustness                     |          |        | 27  |
|                                                  | ipigmpstatic-group                   |          |        | 27  |
|                                                  | ipigmpversion                        |          |        | 28  |
|                                                  | ipigmpversionstrict                  |          |        | 29  |
|                                                  | noipigmp                             |          |        | 29  |
|                                                  | showipigmp                           |          |        | 30  |
|                                                  | showipigmpcounters                   |          |        | 32  |
|                                                  | showipigmpgroup                      |          |        | 34  |
|                                                  | showipigmpgroups                     |          |        | 36  |
|                                                  | showipigmpinterface                  |          |        | 38  |
|                                                  | showipigmpinterfacecounters          |          |        | 39  |
|                                                  | showipigmpinterfacegroup             |          |        | 40  |
|                                                  | showipigmpinterfacegroups            |          |        | 41  |
|                                                  | showipigmpinterfacestatistics        |          |        | 42  |
|                                                  | showipigmpstatic-groups              |          |        | 43  |
3
AOS-CX10.07MulticastGuide| (6300,6400,8xxxSwitchSeries)

show ip igmp statistics

IGMP snooping

IGMP snooping defaults, protocols, and supported configuration
How IGMP snooping works
IGMP snooping configuration task list
Enabling or disabling IGMP snooping
Specifying the IGMP snooping version
Configuring IGMP snooping static groups
Enabling drop-unknown filters
Configuring IGMP snooping fast learn ports globally
Configuring IGMP snooping per port filtering
Disabling IGMP snooping
Viewing IGMP snooping information
IGMP snooping commands

ip igmp snooping {enable|disable}
ip igmp snooping apply access-list
ip igmp snooping auto vlan
ip igmp snooping blocked vlan
ip igmp snooping drop-unknown
ip igmp snooping fastlearn
ip igmp snooping fastleave vlan
ip igmp snooping forced fastleave vlan
ip igmp snooping forward vlan
ip igmp snooping static-group
ip igmp snooping version
no ip igmp snooping
show ip igmp snooping
show ip igmp snooping counters
show ip igmp snooping groups
show ip igmp snooping static-groups
show ip igmp snooping statistics
show ip igmp snooping vlan <VLAN-ID>
show ip igmp snooping vlan <VLAN-ID> counters
show ip igmp snooping vlan <VLAN-ID> group port
show ip igmp snooping vlan <VLAN-ID> statistics

MLD snooping

MLD snooping functionality
MLD snooping global configuration commands

ipv6 mld snooping

MLD snooping VLAN configuration commands

ipv6 mld snooping
ipv6 mld snooping apply access-list
ipv6 mld snooping auto vlan
ipv6 mld snooping blocked vlan
ipv6 mld snooping fastlearn
ipv6 mld snooping fastleave vlan
ipv6 mld snooping forced fastleave
ipv6 mld snooping forward vlan
ipv6 mld snooping [static-group <X:X::X:X>]
ipv6 mld snooping [version <ver>]

MLD snooping show commands

show ipv6 mld snooping
show ipv6 mld snooping [counters]
show ipv6 mld snooping [groups]

44

47
47
48
49
49
49
50
50
50
51
51
52
52
52
53
54
54
55
56
57
57
58
59
60
60
61
61
62
63
64
64
66
68
69

70
70
70
70
71
71
71
72
73
74
74
75
76
76
77
77
78
78
79

Contents | 4

|     | showipv6mldsnooping[statistics]                |     |     |     |     | 80  |
| --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
|     | showipv6mldsnooping[vlan<vlan-id>[counters]]   |     |     |     |     | 80  |
|     | showipv6mldsnooping[vlan<vlan-id>[statistics]] |     |     |     |     | 82  |
showipv6mldsnooping[vlan<vlan-id>[group[<group-ip>][source<source-ip>]]] 82
|                                          | showipv6mldsnooping[vlan<vlan-id>[group[port<port_id>]]  |     |     |     |     | 84  |
| ---------------------------------------- | -------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                          | showipv6mldsnooping[static-groups]                       |     |     |     |     | 85  |
| MLDconfigurationcommandsforinterfaceVLAN |                                                          |     |     |     |     | 85  |
|                                          | ipv6mld{enable|disable}                                  |     |     |     |     | 85  |
|                                          | ipv6mldapplyaccess-list                                  |     |     |     |     | 86  |
|                                          | noipv6mld                                                |     |     |     |     | 87  |
|                                          | ipv6mldquerier                                           |     |     |     |     | 87  |
|                                          | ipv6mldquerier[interval<interval-value>]                 |     |     |     |     | 88  |
|                                          | ipv6mldlast-member-query-interval<interval-value>        |     |     |     |     | 88  |
|                                          | ipv6mldquerierquery-max-response-time<response-time>     |     |     |     |     | 89  |
|                                          | ipv6mldrobustness                                        |     |     |     |     | 89  |
|                                          | ipv6mldstatic-group<MULTICAST-GROUP-IP>                  |     |     |     |     | 90  |
|                                          | ipv6mldversion<VERSION>                                  |     |     |     |     | 90  |
|                                          | ipv6mldversion<VERSION>[strict]                          |     |     |     |     | 91  |
| MLDshowcommandsforinterfaceVLAN          |                                                          |     |     |     |     | 91  |
|                                          | showipv6mld                                              |     |     |     |     | 91  |
|                                          | showipv6mld[interface<intf_id>|vlan<vlan-id>]            |     |     |     |     | 92  |
|                                          | showipv6mld[vrf<vrf_name>|all-vrfs]                      |     |     |     |     | 93  |
|                                          | showipv6mld[interface<intf-id>|vlan<vlan-id>][counters]] |     |     |     |     | 94  |
|                                          | showipv6mld[interface<intf-id>|vlan<vlan-id>][groups]]   |     |     |     |     | 95  |
showipv6mld[interface(<intf-id>|vlan<vlan-id>)[group<group_ip>][source
|     | <source_ip>]]]]                             |     |     |     |     | 96  |
| --- | ------------------------------------------- | --- | --- | --- | --- | --- |
|     | showipv6mld[groups]                         |     |     |     |     | 97  |
|     | showipv6mldgroups[all-vrfs|vrf<vrf_name>]   |     |     |     |     | 98  |
|     | showipv6mld[interface<intf-id>[counters]]   |     |     |     |     | 99  |
|     | showipv6mld[interface<intf-id>[statistics]] |     |     |     |     | 100 |
|     | showipv6mld[interface<intf-id>[groups]]     |     |     |     |     | 101 |
showipv6mld[interface(<intf-id>|vlan<vlan-id>)[group<group_ip>][source
|     | <source_ip>]]]]                                      |     |     |     |     | 101 |
| --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
|     | showipv6mld[group<group_ip>[all-vrfs|vrf<vrf_name>]] |     |     |     |     | 102 |
showipv6mld[group<group_ip>[source<source_ip>[all-vrfs|vrf<vrf_name>]]] 104
|                                                         | showipv6mld[interfacevlan<vlan-id>[statistics]]    |           |          |          |         | 105 |
| ------------------------------------------------------- | -------------------------------------------------- | --------- | -------- | -------- | ------- | --- |
|                                                         | showipv6mld[static-groups[vrf<vrf_name>|all-vrfs]] |           |          |          |         | 106 |
|                                                         | showipv6mldcounters                                |           |          |          |         | 107 |
| MLDconfigurationcommandsforinterface                    |                                                    |           |          |          |         | 108 |
|                                                         | ipv6mld{enable|disable}                            |           |          |          |         | 108 |
|                                                         | ipv6mldapplyaccess-list                            |           |          |          |         | 108 |
|                                                         | noipv6mld                                          |           |          |          |         | 109 |
|                                                         | ipv6mldquerier                                     |           |          |          |         | 110 |
|                                                         | ipv6mldquerier[interval<interval-value>]           |           |          |          |         | 110 |
|                                                         | ipv6mldlast-member-query-interval                  |           |          |          |         | 111 |
|                                                         | ipv6mldquerierquery-max-response-time              |           |          |          |         | 111 |
|                                                         | ipv6mldrobustness                                  |           |          |          |         | 112 |
|                                                         | ipv6mldstatic-group                                |           |          |          |         | 112 |
|                                                         | ipv6mldversion                                     |           |          |          |         | 113 |
|                                                         | ipv6mldversion[strict]                             |           |          |          |         | 113 |
| Protocol                                                | Independent                                        | Multicast | - Sparse | Mode (V4 | and V6) | 115 |
| ProtocolIndependentMulticast-SparseMode(PIM-SM)overview |                                                    |           |          |          |         | 115 |
| PIM-SMdefaults,protocols,andsupportedconfiguration      |                                                    |           |          |          |         | 115 |
| PIM-SMroutertypes                                       |                                                    |           |          |          |         | 116 |
| HowPIM-SMworks                                          |                                                    |           |          |          |         | 118 |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 5

Enabling/disabling PIM-SM in an interface
Configuring PIM-SM options in an interface
Viewing PIM information
PIM-SM configuration example
PIM-SM configuration task list

Enabling or disabling PIM globally
Configuring join/prune interval
Enabling/disabling multicast traffic to SPT
Configuring an RP
Configuring a BSR
Configuring RPF override
Removing all PIM-SM related configurations on an interface
PIM graceful shutdown

PIM-SM commands for IPv4

accept-register access-list
accept-rp
active-active
bfd all-interfaces
bsr-candidate bsm-interval
bsr-candidate hash-mask-length
bsr-candidate priority
bsr-candidate source-ip-interface
disable
enable
ip pim-sparse {enable|disable}
ip pim-sparse bfd
ip pim-sparse dr-priority
ip pim-sparse hello-delay
ip pim-sparse hello-interval
ip pim-sparse ip-addr
ip pim-sparse lan-prune-delay
ip pim-sparse override-interval
ip pim-sparse propagation-delay
join-prune-interval
multicast-route-limit
no ip pim-sparse
register-rate-limit
router pim
rp-address <IP-ADDR>
rp-candidate group-prefix
rp-candidate hold-time
rp-candidate priority
rp-candidate source-ip-interface
rpf-override
show ip mroute
show ip mroute brief
show ip mroute <GROUP-ADDR>
show ip pim
show ip pim bsr
show ip pim bsr elected
show ip pim bsr local
show ip pim interface
show ip pim interface <INTERFACE-NAME>
show ip pim interface <INTERFACE-NAME> counters
show ip pim neighbor
show ip pim pending

120
120
123
124
126
127
127
128
128
130
132
132
133
134
134
135
136
137
138
138
139
139
140
141
141
142
142
143
144
145
145
146
147
148
148
149
149
150
151
152
152
153
153
154
155
156
157
159
159
161
162
163
164
165
166
167

Contents | 6

|                                                        | showippimrp-candidate                 |           |         |          |         | 168 |
| ------------------------------------------------------ | ------------------------------------- | --------- | ------- | -------- | ------- | --- |
|                                                        | showippimrp-set                       |           |         |          |         | 169 |
|                                                        | showippimrp-setlearned                |           |         |          |         | 170 |
|                                                        | showippimrp-setstatic                 |           |         |          |         | 171 |
|                                                        | showippimrpf-override                 |           |         |          |         | 172 |
|                                                        | showippimrpf-overridesource           |           |         |          |         | 173 |
|                                                        | sources-per-group                     |           |         |          |         | 174 |
|                                                        | spt-threshold                         |           |         |          |         | 175 |
| PIM-SMcommandsforIPv6                                  |                                       |           |         |          |         | 175 |
|                                                        | accept-registeraccess-list            |           |         |          |         | 175 |
|                                                        | accept-rp                             |           |         |          |         | 176 |
|                                                        | bsr-candidatebsm-interval             |           |         |          |         | 177 |
|                                                        | bsr-candidatehash-mask-length         |           |         |          |         | 178 |
|                                                        | bsr-candidatepriority                 |           |         |          |         | 178 |
|                                                        | bsr-candidatesource-ip-interface      |           |         |          |         | 179 |
|                                                        | disable                               |           |         |          |         | 180 |
|                                                        | enable                                |           |         |          |         | 180 |
|                                                        | ipv6pim6-sparse{enable|disable}       |           |         |          |         | 181 |
|                                                        | ipv6pim6-sparsebfd                    |           |         |          |         | 181 |
|                                                        | ipv6pim6-sparsedr-priority            |           |         |          |         | 182 |
|                                                        | ipv6pim6-sparsehello-delay            |           |         |          |         | 183 |
|                                                        | ipv6pim6-sparsehello-interval         |           |         |          |         | 184 |
|                                                        | ipv6pim6-sparseipv6-addr              |           |         |          |         | 184 |
|                                                        | ipv6pim6-sparselan-prune-delay        |           |         |          |         | 185 |
|                                                        | ipv6pim6-sparseoverride-interval      |           |         |          |         | 186 |
|                                                        | ipv6pim6-sparsepropagation-delay      |           |         |          |         | 187 |
|                                                        | join-prune-interval                   |           |         |          |         | 187 |
|                                                        | noipv6pim6-sparse                     |           |         |          |         | 188 |
|                                                        | routerpim6                            |           |         |          |         | 188 |
|                                                        | rp-address<IPv6-ADDR>                 |           |         |          |         | 189 |
|                                                        | rp-candidategroup-prefix              |           |         |          |         | 190 |
|                                                        | rp-candidatehold-time                 |           |         |          |         | 190 |
|                                                        | rp-candidatepriority                  |           |         |          |         | 191 |
|                                                        | rp-candidatesource-ip-interface       |           |         |          |         | 192 |
|                                                        | rpf-override                          |           |         |          |         | 193 |
|                                                        | showipv6mroute<GROUP-ADDR>            |           |         |          |         | 194 |
|                                                        | showipv6mroute                        |           |         |          |         | 195 |
|                                                        | showipv6mroutebrief                   |           |         |          |         | 196 |
|                                                        | showipv6pim6                          |           |         |          |         | 197 |
|                                                        | showipv6pim6bsr                       |           |         |          |         | 198 |
|                                                        | showipv6pim6bsrelected                |           |         |          |         | 200 |
|                                                        | showipv6pim6bsrlocal                  |           |         |          |         | 201 |
|                                                        | showipv6pim6interface<INTERFACE-NAME> |           |         |          |         | 201 |
|                                                        | showipv6pim6interface                 |           |         |          |         | 202 |
|                                                        | showipv6pim6neighbor                  |           |         |          |         | 203 |
|                                                        | showipv6pim6pending                   |           |         |          |         | 204 |
|                                                        | showipv6pim6rp-candidate              |           |         |          |         | 205 |
|                                                        | showipv6pim6rpf-override              |           |         |          |         | 206 |
|                                                        | showipv6pim6rpf-overridesource        |           |         |          |         | 207 |
|                                                        | showipv6pim6rp-set                    |           |         |          |         | 208 |
|                                                        | showipv6pim6rp-setlearned             |           |         |          |         | 209 |
|                                                        | showipv6pim6rp-setstatic              |           |         |          |         | 210 |
|                                                        | spt-threshold                         |           |         |          |         | 211 |
| Protocol                                               | Independent                           | Multicast | - Dense | Mode (V4 | and V6) | 212 |
| ProtocolIndependentMulticast-DenseMode(PIM-DM)overview |                                       |           |         |          |         | 212 |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 7

| PIM-DMdefaults,protocols,andsupportedconfigurations |                                            |           |          |        | 212 |
| --------------------------------------------------- | ------------------------------------------ | --------- | -------- | ------ | --- |
| PIM-DMconfigurationexample                          |                                            |           |          |        | 213 |
| PIM-DMfeatures                                      |                                            |           |          |        | 213 |
| PIM-DMcommandsforIPv4                               |                                            |           |          |        | 214 |
|                                                     | disable                                    |           |          |        | 214 |
|                                                     | enable                                     |           |          |        | 214 |
|                                                     | noippim-dense{enable|disable}              |           |          |        | 215 |
|                                                     | ippim-densebfd                             |           |          |        | 216 |
|                                                     | ippim-densegraft-retry-interval            |           |          |        | 216 |
|                                                     | ippim-densehello-delay                     |           |          |        | 217 |
|                                                     | ippim-densehello-interval                  |           |          |        | 218 |
|                                                     | ippim-denseip-addr                         |           |          |        | 219 |
|                                                     | ippim-denselan-prune-delay                 |           |          |        | 219 |
|                                                     | ippim-densemax-graft-retries               |           |          |        | 220 |
|                                                     | ippim-denseoverride-interval               |           |          |        | 221 |
|                                                     | ippim-densepropagation-delay               |           |          |        | 222 |
|                                                     | ippim-densettl-threshold                   |           |          |        | 222 |
|                                                     | routerpim                                  |           |          |        | 223 |
|                                                     | showipmroute                               |           |          |        | 224 |
|                                                     | showipmroute<GROUP-ADDR>                   |           |          |        | 225 |
|                                                     | showipmroutebrief                          |           |          |        | 227 |
|                                                     | showippim                                  |           |          |        | 227 |
|                                                     | showippiminterface                         |           |          |        | 228 |
|                                                     | showippiminterface<INTERFACE-NAME>         |           |          |        | 229 |
|                                                     | showippiminterface<INTERFACE-NAME>counters |           |          |        | 230 |
|                                                     | showippimneighbor                          |           |          |        | 231 |
|                                                     | state-refresh-interval                     |           |          |        | 232 |
| PIM-DMcommandsforIPv6                               |                                            |           |          |        | 232 |
|                                                     | disable                                    |           |          |        | 232 |
|                                                     | enable                                     |           |          |        | 233 |
|                                                     | ipv6pim6-dense{enable|disable}             |           |          |        | 233 |
|                                                     | ipv6pim6-densebfd                          |           |          |        | 234 |
|                                                     | ipv6pim6-densegraft-retry-interval         |           |          |        | 235 |
|                                                     | ipv6pim6-densehello-delay                  |           |          |        | 236 |
|                                                     | ipv6pim6-densehello-interval               |           |          |        | 236 |
|                                                     | ipv6pim6-denseipv6-addr                    |           |          |        | 237 |
|                                                     | ipv6pim6-denselan-prune-delay              |           |          |        | 238 |
|                                                     | ipv6pim6-densemax-graft-retries            |           |          |        | 238 |
|                                                     | ipv6pim6-denseoverride-interval            |           |          |        | 239 |
|                                                     | ipv6pim6-densepropagation-delay            |           |          |        | 240 |
|                                                     | ipv6pim6-densettl-threshold                |           |          |        | 241 |
|                                                     | noipv6pim6-dense                           |           |          |        | 242 |
|                                                     | showipv6pim6                               |           |          |        | 242 |
|                                                     | showipv6pim6interface                      |           |          |        | 243 |
|                                                     | showipv6pim6interface<INTERFACE-NAME>      |           |          |        | 244 |
|                                                     | showipv6mroute                             |           |          |        | 244 |
|                                                     | showipv6mroutebrief                        |           |          |        | 246 |
|                                                     | showipv6mroute<GROUP-ADDR>                 |           |          |        | 247 |
|                                                     | showipv6pim6neighbor                       |           |          |        | 249 |
|                                                     | routerpim6                                 |           |          |        | 249 |
|                                                     | state-refresh-interval                     |           |          |        | 250 |
| Multicast                                           | Source                                     | Discovery | Protocol | (MSDP) | 252 |
| MulticastSourceDiscoveryProtocol(MSDP)overview      |                                            |           |          |        | 252 |
| MSDProuterconfigcommands                            |                                            |           |          |        | 252 |
|                                                     | disable                                    |           |          |        | 252 |
Contents|8

|                               | enable                           |     | 253 |
| ----------------------------- | -------------------------------- | --- | --- |
|                               | routermsdp                       |     | 253 |
|                               | sa-interval                      |     | 254 |
| MSDPpeerconfigurationcommands |                                  |     | 254 |
|                               | connection-retry-interval        |     | 254 |
|                               | connect-source                   |     | 255 |
|                               | description                      |     | 255 |
|                               | disable                          |     | 256 |
|                               | enable                           |     | 257 |
|                               | ipmsdppeer                       |     | 257 |
|                               | keepalive                        |     | 258 |
|                               | mesh-group                       |     | 258 |
|                               | password                         |     | 259 |
|                               | sa-filteraccess-list             |     | 260 |
| MSDPshowcommands              |                                  |     | 261 |
|                               | showipmsdpcount                  |     | 261 |
|                               | showipmsdppeer                   |     | 262 |
|                               | showipmsdpsa-cache               |     | 263 |
|                               | showipmsdpsummary                |     | 263 |
| mDNS                          | gateway                          |     | 265 |
| mDNSgatewayoverview           |                                  |     | 265 |
| ConfiguringmDNSgateway        |                                  |     | 266 |
| mDNSgatewaycommands           |                                  |     | 267 |
|                               | debugmdns                        |     | 267 |
|                               | description                      |     | 268 |
|                               | id                               |     | 268 |
|                               | mdns-sd                          |     | 269 |
|                               | mdns-sdapply-profiletx           |     | 269 |
|                               | mdns-sdenable                    |     | 270 |
|                               | mdns-sdprofile                   |     | 271 |
|                               | mdns-sdservice                   |     | 271 |
|                               | clearmdns-sdstatistics           |     | 272 |
|                               | <sequence-number>                |     | 272 |
|                               | showmdns-sdservice-entries       |     | 274 |
|                               | showmdns-sdstatistics            |     | 275 |
|                               | showmdns-sdstatisticsprofile     |     | 275 |
|                               | showmdns-sdsummary               |     | 276 |
|                               | showrunning-configinterface      |     | 277 |
|                               | showrunning-configmdns-sdprofile |     | 277 |
|                               | showrunning-configmdns-sdservice |     | 278 |
| Multicast                     | VXLAN                            |     | 279 |
| IGMP                          |                                  |     | 280 |
| PIM-SM                        |                                  |     | 280 |
SampleMulticastoverVXLANConfigofaVSXLeafinSymmetricIRBtopology 281
| MulticastVXLANcommands |                                  |           | 284 |
| ---------------------- | -------------------------------- | --------- | --- |
|                        | ippim-sparsevsx-virtual-neighbor |           | 284 |
|                        | redistributelocal-mac            |           | 285 |
|                        | showipmroute                     |           | 285 |
|                        | showippimneighbor                |           | 287 |
| Support                | and other                        | resources | 289 |
| AccessingArubaSupport  |                                  |           | 289 |
| Accessingupdates       |                                  |           | 289 |
|                        | ArubaSupportPortal               |           | 289 |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 9

My Networking
Warranty information
Regulatory information
Documentation feedback

290
290
290
290

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

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A)

n Aruba 8400 Switch Series (JL375A, JL376A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and other resources.

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

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

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

About this document | 12

member/slot/port

On the 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

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

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

13

n Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

o member: 1.

o tray: 1 to 4.

o fan: 1 to 4.

n Fabric modules are not labeled on the switch but are labeled in software in the format: member/module:

o member: 1.

o member: 1 or 2.

n The display module on the rear of the switch is not labeled with a member or slot number.

About this document | 14

Chapter 2

Multicast overview

Multicast overview

Multicast addressing allows one-to-many or many-to-many communication among hosts on a network.
Typical applications of multicast communication include: audio and video streaming, desktop conferencing,
collaborative computing, and similar applications.

In a network where IP multicast traffic is transmitted for multimedia applications, such traffic is blocked at
routed interface (VLAN) boundaries unless a multicast routing protocol is running. Protocol Independent
Multicast (PIM) is a family of routing protocols that form multicast trees to forward traffic from multicast
sources to subnets that have used a protocol such as IGMP to request the traffic. PIM relies on the unicast
routing tables created by any of several unicast routing protocols to identify the path back to a multicast
source (Reverse Path Forwarding, or RPF). With this information, PIM sets up the distribution tree for the
multicast traffic. IGMP provides the multicast traffic link between a host and a multicast router running PIM-
SM. Both PIM-SM and IGMP must be enabled on VLANs whose member ports have directly connected hosts
with a valid need to join multicast groups.

IGMP snooping (Internet Group Management Protocol controls) can be configured per-VLAN basis to reduce
unnecessary bandwidth usage. In the factory default state (IGMP and IGMP snooping disabled), the switch
simply floods all IP multicast traffic it receives on a given VLAN through all ports on that VLAN (except the
port on which it received the traffic). This can result in significant and unnecessary bandwidth usage in
networks where IP multicast traffic is a factor. Enabling IGMP allows the ports to detect IGMP queries and
report packets and manage IP multicast traffic through the switch. IGMP will be configured on the hosts,
and multicast traffic will be generated by one or more servers (inside or outside of the local network).
Switches in the network (that support IGMP snooping) can then be configured to direct the multicast traffic
to only the ports where needed. If multiple VLANs are configured, you can configure IGMP snooping on a
per-VLAN basis.

Multicast Listener Discovery (MLD) is an IPv6 protocol used on a local link for multicast group management.
MLD snooping is a subset of the MLD protocol that operates at the port level and conserves network
bandwidth by reducing the flooding of multicast IPv6 packets.

Multicast protocols
Layer 3 multicast protocols include:

n IGMP (Internet Group Management Protocol) for last-hop multicast group management. Current RFCs

include:

o IGMPv2 (RFC 2236)

o IGMPv3 (RFC 3376)

n PIM (Protocol Independent Multicast) for intra-domain multicast routing.

o PIM-SM (Sparse mode) (RFC 4601)

o PIM-DM (Dense mode) (RFC 3973)

o BSR (Bootstrap router) (RFC 5059)

n MSDP (Multicast Source Discovery Protocol) (RFC 3618)

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

15

MLD(MulticastListenerDiscovery)v1andv2
n
MLDv1-RFC2710
o
o MLDv2-RFC3810
| Layer2 | multicast | protocol: |
| ------ | --------- | --------- |
n IGMPsnoopingforIPv4multicastfiltering.
n MLDsnoopingforIPv6multicastfiltering.
| Multicast | addresses |     |
| --------- | --------- | --- |
EachmulticasthostgroupisidentifiedbyasingleIPaddressintherangeof224.0.0.0through
239.255.255.255.
| n Forthe | 8320/8325                                        | switch:AOS-CXsupports4KIPv4multicastflows. |
| -------- | ------------------------------------------------ | ------------------------------------------ |
| n Forthe | 8400 switch:AOS-CXsupports16KIPv4multicastflows. |                                            |
| Forthe   | 6400/6300                                        | switch:AOS-CXsupports4KIPv4multicastflows. |
n
Foralistofallreservedandwellknownmulticastaddresses,seethestandardsdocumentatthefollowing
links:
n https://www.iana.org/assignments/multicast-addresses/multicast-addresses.xhtml
n https://www.iana.org/assignments/ipv6-multicast-addresses/ipv6-multicast-addresses.xhtml
Multicastoverview|16

Internet Group Management Protocol
(IGMP)

Chapter 3

Internet Group Management Protocol (IGMP)

In a network where IP multicast traffic is transmitted for various multimedia applications, you can use the
switch to reduce unnecessary bandwidth usage on a per-port basis by configuring IGMP (Internet Group
Management Protocol). IGMPv3 (RFC 3376) and IGMPv2 (RFC 2236) are the current RFCs for IGMP.

In the factory default state (IGMP disabled), the switch simply floods all IP multicast traffic it receives on a
given VLAN through all ports on that VLAN (except the port on which it received the traffic). This can result in
significant and unnecessary bandwidth usage in networks where IP multicast traffic is a factor. Enabling
IGMP allows the ports to detect IGMP queries and report packets and manage IP multicast traffic through
the switch.

IGMP is useful in multimedia applications such as LAN TV, desktop conferencing, and collaborative
computing, where there is MultiPoint communication; that is, communication from one to many hosts, or
communication originating from many hosts and destined for many other hosts.

In such MultiPoint applications, IGMP will be configured on the hosts, and multicast traffic will be generated
by one or more servers (inside or outside of the local network). Switches in the network (that support IGMP)
can then be configured to direct the multicast traffic to only the ports where needed. If multiple VLANs are
configured, you can configure IGMP on a per-VLAN basis.

Enabling IGMP allows the router to become querier. If there is another querier in the LAN, the router will
resume non querier functionality and will respond to query/report packets.

IGMP defaults, protocols, and supported configuration

IGMP default configuration:

n IGMP is disabled by default.

n The default IGMP version is IGMPv3.

IGMP supported protocols include:

n IGMPv2 (RFC 2236)

n IGMPv3 (RFC 3376)

Static groups:

You can configure a maximum of 32 IGMP static groups.

How the IGMP protocol works
IGMP manages multicast group memberships based on the query and response mechanism.

IGMP is an internal protocol of the IP suite. IP manages multicast traffic by using switches, multicast routers,
and hosts that support IGMP. A multicast router is not necessary as long as a switch is configured to support
IGMP with the querier feature enabled. A set of hosts, routers, and/or switches that send or receive
multicast data streams to or from the same sources, is called a multicast group. All devices in the group use
the same multicast group address.

The multicast group uses three fundamental types of messages to communicate:

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

17

n Query: A message sent from the querier (multicast router or switch) asking for a response from each host
belonging to the multicast group. If a multicast router supporting IGMP is not present, the switch must
assume this function to elicit group membership information from the hosts on the network.

n Join: A message sent by a host to the querier to indicate that the host wants to be or is a member of a

given group indicated in the join message.

n Leave group: A message sent by a host to the querier to indicate that the host has ceased to be a

member of a specific multicast group.

An IP multicast packet includes the multicast group (address) to which the packet belongs. When an IGMP
client connected to a switch port needs to receive multicast traffic from a specific group, it joins the group
by sending an IGMP join request to the network. (The multicast group specified in the join request is
determined by the requesting application running on the IGMP client.)

When the client is ready to leave the multicast group, it sends a Leave Group message to the network and
ceases to be a group member. When the leave request is detected, the appropriate IGMP device ceases
transmitting traffic for the designated multicast group through the port on which the leave request was
received (as long as there are no other current members of that group on the affected port.)

Thus, IGMP identifies members of a multicast group (within a subnet) and allows IGMP-configured hosts
(and routers) to join or leave multicast groups.

Considerations when configuring IGMP
With the factory default setting, multicast data transmitted from the sources will be flooded on all ports in
the VLAN. Configuring IGMP snooping avoids flooding and causes the switch to forward data only to the
receivers.

The function of the IGMP querier is to poll other IGMP-enabled devices in an IGMP-enabled interface to
elicit group membership information. On enabling IGMP, the router performs this function if there is no
other device in the interface to act as querier.

Basic steps to configure IGMP:

1. Configure VLANs.

2. Configure ports and assign them to the VLANs.

3. Configure the L3 interface (an interface VLAN/route only port/L3 LAG) and assign an IP address to

the interface.

4. Enable IGMP.

5. Choose the desired IGMP version. The default is version 3.

IGMP configuration considerations:

n For IGMP to be operational, the interface has to be administratively up. For interface VLANs, the L2 VLAN

has to be up and one of the ports in the VLAN has to be up.

n The IP address must be assigned for the interface to become querier. Without an IP address, the device

will remain in a non querier state.

n A querier is required for proper IGMP operation. For this reason, you must enable IGMP on the L3

Interface. If the querier functionality is not configured or disabled, you must ensure that there is an
IGMP querier in the same VLAN.

n For IGMP snooping to be operational on a VLAN, the VLAN has to be administratively up and at least one

port in the VLAN has to be up.

n If IGMP snooping is enabled on the VLAN, and IGMP is enabled on the interface VLAN, and the
configured version does not match, the lowest version is chosen as the operating version.

Internet Group Management Protocol (IGMP) | 18

n If the switch becomes the querier for a particular interface, then subsequently detects queries

transmitted from another device on the same VLAN, the switch ceases to operate as the querier for that
interface.

n The switch automatically ceases querier operation in an IGMP-enabled interface if it detects another

querier on the interface. You can also use the switch CLI to disable the querier capability.

n Multicast traffic will be flooded on the VLAN, if TTL=1 or TTL>255 regardless of IGMP joins and group

membership within the VLAN.

IGMP configuration task list
Tasks at a glance.

n Enabling or disabling IGMP

n Specifying the IGMP version

n Configuring IGMP static groups

n Configuring IGMP query and response parameters

n Disabling IGMP

n Viewing IGMP information

Enabling or disabling IGMP

Prerequisites

You must be in an interface configuration context, as indicated by the switch(config-if)# prompt, switch
(config-if-vlan)# prompt, or switch(config-lag-if)# prompt.

For IGMP to be operational, the interface has to be up. To become querier, the interface must have an IP
address associated with it.

Procedure

IGMP is disabled by default. Enable IGMP on an interface using the following command.
ip igmp {enable | disable}

For example, the following command enables IGMP on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp enable

Use the disable parameter to disable IGMP on an interface.

Specifying the IGMP version
The version can be either 2 (IGMPv2) or 3 (IGMPv3). The default is 3. IGMPv2 supports filtering based on
groups. IGMPv3 is more advanced and includes filtering based on source and groups.

If using the strict option, packets that do not match the configured version will be dropped.

Prerequisites

You must be in an interface configuration context, as indicated by the switch(config-if)# prompt, switch
(config-if-vlan)# prompt, or switch(config-lag-if)# prompt.

Procedure

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

19

SpecifytheIGMPversionforaninterfaceusingoneofthefollowingcommands.
| ip igmp version | <VERSION> |        |     |     |     |
| --------------- | --------- | ------ | --- | --- | --- |
| ip igmp version | <VERSION> | strict |     |     |     |
Forexample,thefollowingcommandsetstheIGMPversionto2oninterfaceVLAN2:
| switch(config)#         | interface | vlan    | 2       |     |     |
| ----------------------- | --------- | ------- | ------- | --- | --- |
| switch(config-if-vlan)# |           | ip igmp | version | 2   |     |
AndthefollowingcommandsetsIGMPstrictversionto2oninterfaceVLAN5:
| switch(config)#         | interface | vlan    | 5       |          |     |
| ----------------------- | --------- | ------- | ------- | -------- | --- |
| switch(config-if-vlan)# |           | ip igmp | version | 2 strict |     |
switch(config-if-vlan)#
|             |      | no ip  | igmp version | 2 strict |     |
| ----------- | ---- | ------ | ------------ | -------- | --- |
| Configuring | IGMP | static | groups       |          |     |
Theswitchwillalwaysfloodthetrafficdestinedforagroupconfiguredasstaticgroup.Sothehostswill
receivethetrafficforstaticgroupseveniftheyhavenotsubscribedforthatgroup.Youcanconfigurea
maximumof32IGMPstaticgroups.
Prerequisites
Youmustbeinaninterfaceconfigurationcontext,asindicatedbytheswitch(config-if)#prompt,switch
(config-if-vlan)#prompt,orswitch(config-lag-if)#prompt.
Procedure
ConfigureanIGMPstaticgrouponaninterfaceusingthefollowingcommand.
| ip igmp static-group | <MULTICAST-GROUP-IP> |     |     |     |     |
| -------------------- | -------------------- | --- | --- | --- | --- |
Forexample,thefollowingcommandconfiguresanIGMPstaticmulticastgroupas239.1.1.1oninterface
VLAN2:
| switch(config)#         | interface | vlan    | 2            |           |     |
| ----------------------- | --------- | ------- | ------------ | --------- | --- |
| switch(config-if-vlan)# |           | ip igmp | static-group | 239.1.1.1 |     |
ThenoformofthecommandremovesanIGMPstaticgroup.
| Configuring | IGMP | query | and | response | parameters |
| ----------- | ---- | ----- | --- | -------- | ---------- |
Configurequeryandresponseparameterssuchasquerierinterval,lastmemberqueryinterval,max
responsetime,androbustness.
Prerequisites
Youmustbeinaninterfaceconfigurationcontext,asindicatedbytheswitch(config-if)#prompt,switch
(config-if-vlan)#prompt,orswitch(config-lag-if)#prompt.
Procedure
InternetGroupManagementProtocol(IGMP)|20

ConfigureIGMPqueryandresponseparametersonaninterfaceusingthefollowingcommands.
MakesurethattheIGMPquerierisenabled.(InIGMPv3theIGMPquerierisenabledbydefault.)
n
ConfiguretheIGMPquerieronaninterfaceusingthefollowingcommand:ip igmp querier.
ConfiguretheIGMPquerierintervalonaninterfaceusingthefollowingcommand:ip
n igmp querier
interval
<INTERVAL-VALUE>.Theintervalisfrom5-300seconds,withadefaultof125.
n ConfiguretheIGMPlastmemberqueryintervalvalueinsecondsonaninterfaceusingthefollowing
| command:ip igmp | last-member-query-interval |     |     |
| --------------- | -------------------------- | --- | --- |
<INTERVAL-VALUE>.Theintervalisfrom1-2seconds,withadefaultof1.
n ConfiguretheIGMPmaxresponsetimevalueinsecondsonaninterfaceusingthefollowingcommand:
ip igmp querier query-max-response-time <RESPONSE-TIME>.Theresponsetimeisfrom10-128
seconds,withadefaultof10.
ConfiguretheIGMProbustness(thenumberoftimestoretryaquery)onaninterfaceusingthe
n
followingcommand:ip igmp robustness <VALUE>.Therobustnessvalueisfrom1-7withdefaultof2.
Forexample,thefollowingcommandconfigurestheIGMPquerierinterfaceintervalas100oninterface
VLAN2.Thenoformofthecommandsetstheintervaltothedefault.
| switch(config)#         | interface | vlan 2          |              |
| ----------------------- | --------- | --------------- | ------------ |
| switch(config-if-vlan)# |           | ip igmp querier | interval 100 |
switch(config-if-vlan)#
|                |     | no ip igmp querier | interval |
| -------------- | --- | ------------------ | -------- |
| Disabling IGMP |     |                    |          |
Prerequisites
Youmustbeinaninterfaceconfigurationcontext,asindicatedbytheswitch(config-if)#prompt,switch
(config-if-vlan)#prompt,orswitch(config-lag-if)#prompt.
Procedure
RemoveIGMPfromaninterfaceusingthefollowingcommand.
no ip igmp
Forexample,thefollowingcommandremovesIGMPoninterfaceVLAN2:
| switch(config)#         | interface   | vlan 2     |     |
| ----------------------- | ----------- | ---------- | --- |
| switch(config-if-vlan)# |             | no ip igmp |     |
| Viewing IGMP            | information |            |     |
Forsomecommands,youcanspecifyviewinginformationbyinterfaceorbyVRF.
Prerequisites
UsetheseshowcommandsfromtheOperator(>)orManager(#)context.
Procedure
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 21

ToviewIGMPinformation,usethefollowingcommands.
ToviewIGMPconfigurationdetailsandstatus,use:show ip igmporuseshow ip igmp interface.
n
n ToviewIGMPstatisticsandgroupsjoined,use:show ip igmp statisticsoruseshow ip igmp
interface statistics.
ToviewIGMPcounters,use:show ip igmp countersoruseshow ip igmp interface counters.
n
| n ToviewIGMPstaticgroups,use:show |     | ip igmp static-groups. |
| --------------------------------- | --- | ---------------------- |
n ToviewIGMPgroupinformation,use:show ip igmp groupsoruseshow ip igmp interface groups.
n ToviewIGMPgroupdetailsforaspecificgroupandsource,use:show ip igmp grouporuseshow ip
igmp interface group.OptionallyyoucanalsodisplayjoinedgroupdetailsbyVRF.
| IGMP configuration | example |     |
| ------------------ | ------- | --- |
Theoutputofthefollowingshow running-configcommandshowsanexampleofanIGMPconfiguration
withIGMPsnooping.
Onthe6400SwitchSeries,interfaceidentificationdiffers.
switch# show running-config
Current configuration:
!
!
!
!
!
vlan 1
no shutdown
vlan 2
| ip igmp snooping | enable        |            |
| ---------------- | ------------- | ---------- |
| ip igmp snooping | version 2     |            |
| ip igmp snooping | forward 1/1/1 |            |
| ip igmp snooping | blocked 1/1/3 |            |
| ip igmp snooping | static group  | 239.1.1.10 |
| ip igmp snooping | static group  | 239.1.1.11 |
interface 1/1/1
no shutdown
no routing
| vlan access 2 |     |     |
| ------------- | --- | --- |
interface 1/1/2
no shutdown
no routing
| vlan access 2 |     |     |
| ------------- | --- | --- |
interface 1/1/3
no shutdown
no routing
| vlan access 2 |     |     |
| ------------- | --- | --- |
interface vlan2
no shutdown
| ip address 20.1.1.1/24 |     |     |
| ---------------------- | --- | --- |
ip igmp enable
| ip igmp version                    | 2          |     |
| ---------------------------------- | ---------- | --- |
| ip igmp querier                    | interval 5 |     |
| ip igmp robustness                 | 5          |     |
| ip igmp last-member-query-interval |            | 2   |
| ip igmp query-max-response-time    |            | 50  |
| ip igmp static-group               | 239.1.1.1  |     |
IGMP commands
InternetGroupManagementProtocol(IGMP)|22

Forcommandsintheinterfaceconfigurationcontext,theinterfacemustbeanL3interface.Thesupported
contextsincludes:config-if,config-if-vlan,config-lag-if.
ip igmp
Syntax
| ip igmp | {enable | | disable} |     |
| ------- | ------- | ---------- | --- |
Description
EnablesordisablesIGMPonthecurrentinterface.IGMPisdisabledbydefault.
Commandcontext
config-if-vlan
config-if
config-lag-if
Parameters
enable
EnableIGMP.
disable
DisableIGMP.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingIGMPoninterfaceVLAN2:
switch(config)#
|                         |     | interface | vlan 2         |
| ----------------------- | --- | --------- | -------------- |
| switch(config-if-vlan)# |     |           | ip igmp enable |
DisablingIGMPoninterfaceVLAN2:
| switch(config)#         |       | interface   | vlan 2          |
| ----------------------- | ----- | ----------- | --------------- |
| switch(config-if-vlan)# |       |             | ip igmp disable |
| ip igmp                 | apply | access-list |                 |
Syntax
| ip igmp    | apply access-list |             | <ACL-NAME> |
| ---------- | ----------------- | ----------- | ---------- |
| no ip igmp | apply             | access-list | <ACL-NAME> |
Description
ConfigurestheACLonaparticularinterfacetofiltertheIGMPjoinorleavepacketsbasedonrulessetinthe
particularACLname.
ThenoformofthiscommandunconfigurestherulessetfortheACL.
ThisconfigurationwilloverridetheACLassociatedwithIGMPsnoopingonthecorrespondingL2VLAN.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 23

Commandcontext
config-if-vlan
Parameters
access-list
AssociatesanACLwiththeIGMP.
<ACL-NAME>
SpecifiesthenameoftheACL.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
ExistingclassifiercommandsareusedtoconfiguretheACL.IncaseanIGMPv3packetwithmultiplegroup
addressesisreceived,itwillonlyprocessthepermittedgroupaddressesbasedontheACLruleset,andany
existingjoinswilltimeout.Ifthereisnomatchorifthereisadenyrulematch,thepacketisdropped.
Examples
ConfiguringtheACLonaVLANtofilterIGMPpacketsbasedonrulessetinaccesslistmygroup:
| switch(config)#         |     | access-list | ip          | mygroup           |         |
| ----------------------- | --- | ----------- | ----------- | ----------------- | ------- |
| switch(config-acl-ip)#  |     |             | permit igmp | any 239.1.1.1     |         |
| switch(config-acl-ip)#  |     |             | exit        |                   |         |
| switch(config)#         |     | interface   | vlan        | 2                 |         |
| switch(config-if-vlan)# |     |             | ip igmp     | apply access-list | mygroup |
ConfiguringtheACLtoremovetherulessetinaccesslistmygroup:
| switch(config-if-vlan)# |                            |     | no ip igmp | apply access-list | mygroup |
| ----------------------- | -------------------------- | --- | ---------- | ----------------- | ------- |
| ip igmp                 | last-member-query-interval |     |            |                   |         |
Syntax
| ip igmp    | last-member-query-interval |     |     | <INTERVAL-VALUE> |     |
| ---------- | -------------------------- | --- | --- | ---------------- | --- |
| no ip igmp | last-member-query-interval |     |     | <INTERVAL-VALUE> |     |
Description
ConfiguresanIGMPlastmemberqueryintervalvalueinsecondsonaninterface,dependingonthe
commandcontextyouarein.
Thenoformofthiscommandsetsthevaluetoadefaultof1secondonaninterface.
Commandcontext
config-if-vlan
config-if
config-lag-if
Parameters
<INTERVAL-VALUE>
SpecifiesanIGMPlast-member-query-intervalontheinterface.Default:1second.Range:1-2seconds.
InternetGroupManagementProtocol(IGMP)|24

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringanIGMPlastmemberqueryintervalof2oninterfaceVLAN2:
| switch(config)#         |         | interface vlan 2 |                            |     |
| ----------------------- | ------- | ---------------- | -------------------------- | --- |
| switch(config-if-vlan)# |         | ip igmp          | last-member-query-interval | 2   |
| switch(config-if-vlan)# |         | no ip igmp       | last-member-query-interval |     |
| ip igmp                 | querier |                  |                            |     |
Syntax
| ip igmp    | querier |     |     |     |
| ---------- | ------- | --- | --- | --- |
| no ip igmp | querier |     |     |     |
Description
ConfiguresanIGMPquerieronaninterface,dependingonthecommandcontextyouarein.This
functionalitywillallowaninterfacetojoininthequerier-electionprocess.
ThenoformofthiscommanddisablesIGMPquerieronaninterface.
Commandcontext
config-if-vlan
config-if
config-lag-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringanIGMPquerieroninterfaceVLAN2:
| switch(config)#         |         | interface vlan 2 |         |     |
| ----------------------- | ------- | ---------------- | ------- | --- |
| switch(config-if-vlan)# |         | ip igmp          | querier |     |
| switch(config-if-vlan)# |         | no ip igmp       | querier |     |
| ip igmp                 | querier | interval         |         |     |
Syntax
| ip igmp    | querier interval | <INTERVAL-VALUE> |     |     |
| ---------- | ---------------- | ---------------- | --- | --- |
| no ip igmp | querier          | interval         |     |     |
Description
ConfigurestheintervalbetweenIGMPqueriesonaninterface,dependingonthecommandcontextyouare
in.
ThenoformofthiscommandsetstheIGMPquerierintervaltothedefaultvalueof125secondsonan
interface.
Commandcontext
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 25

config-if-vlan

config-if

config-lag-if

Parameters

<INTERVAL-VALUE>

Specifies the IGMP querier interval in seconds on the interface. Default: 125 seconds. Range: 5-300.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring an IGMP querier interface interval of 100 on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp querier interval 100

Resetting an IGMP querier interval to the default value:

switch(config-if-vlan)# no ip igmp querier interval

ip igmp querier query-max-response-time

Syntax

ip igmp querier query-max-response-time <RESPONSE-TIME>
no ip igmp querier query-max-response-time <RESPONSE-TIME>

Description

Configures the IGMP querier max response time value in seconds on an interface, depending on the
command context you are in.

The no form of this command sets the querier max response time value to the default of 10 seconds on an
interface.

Command context

config-if-vlan

config-if

config-lag-if

Parameters

<RESPONSE-TIME>

Specifies the IGMP querier max response time value on the interface. Default: 10 seconds. Range: 10-
128 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the IGMP querier maximum response time of 50 for interface VLAN 2:

Internet Group Management Protocol (IGMP) | 26

| switch(config)# |     | interface | vlan 2 |     |
| --------------- | --- | --------- | ------ | --- |
switch(config-if-vlan)#
ip igmp query-max-response-time 50
ResettinganIGMPquerierintervaltothedefaultvalue:
| switch(config-if-vlan)# |            |     | no ip igmp | query-max-response-time |
| ----------------------- | ---------- | --- | ---------- | ----------------------- |
| ip igmp                 | robustness |     |            |                         |
Syntax
| ip igmp    | robustness | <VALUE> |     |     |
| ---------- | ---------- | ------- | --- | --- |
| no ip igmp | robustness | <VALUE> |     |     |
Description
ConfiguresIGMProbustnessonaninterface,dependingonthecommandcontext.Therobustness
parameterallowstuningfortheexpectedpacketlossonasubnet.
Thenoformofthiscommandsetstherobustnessvaluetothedefaultof2onaninterface.
Commandcontext
config-if-vlan
config-if
config-lag-if
Parameters
<VALUE>
SpecifiesanIGMProbustnessvalueontheinterface.Default:2.Range:1-7.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringanIGMProbustnessof5oninterfaceVLAN2:
| switch(config)#         |     | interface | vlan 2  |              |
| ----------------------- | --- | --------- | ------- | ------------ |
| switch(config-if-vlan)# |     |           | ip igmp | robustness 5 |
ResettingtheIGMProbustnesstothedefault:
| switch(config-if-vlan)# |              |     | no ip igmp | robustness |
| ----------------------- | ------------ | --- | ---------- | ---------- |
| ip igmp                 | static-group |     |            |            |
Syntax
| ip igmp    | static-group | <MULTICAST-GROUP-IP> |     |     |
| ---------- | ------------ | -------------------- | --- | --- |
| no ip igmp | static-group | <MULTICAST-GROUP-IP> |     |     |
Description
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 27

Configures an IGMP static multicast group on an interface, depending on the command context you are in.
You can configure a maximum of 32 IGMP static groups.

The no form of the command unconfigures IGMP static multicast group on an interface.

Command context

config-if-vlan

config-if

config-lag-if

Parameters

<MULTICAST-GROUP-IP>

Specifies an IGMP static multicast group IP address on the interface. Format: A.B.C.D

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring an IGMP static group on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp static-group 239.1.1.1

Resetting an IGMP static group on an interface to the default (none):

switch(config-if)# no ip igmp static-group 239.1.1.10

ip igmp version

Syntax

ip igmp version <VERSION>

Description

Configures the IGMP version on an interface, depending on the command context you are in.

Command context

config-if-vlan

config-if

config-lag-if

Parameters

<VERSION>

Specifies the IGMP version on the interface. Select 2 for IGMPv2 (RFC2236). Select 3 for IGMPv3
(RFC3376). Values: 2 or 3.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Internet Group Management Protocol (IGMP) | 28

ConfiguringanIGMPversiononinterfaceVLAN2:
| switch(config)#         |     | interface | vlan | 2            |     |
| ----------------------- | --- | --------- | ---- | ------------ | --- |
| switch(config-if-vlan)# |     |           | ip   | igmp version | 2   |
ConfiguringanIGMPversiononinterface1/1/1:
| switch(config)#    |         | interface | 1/1/1   |           |     |
| ------------------ | ------- | --------- | ------- | --------- | --- |
| switch(config-if)# |         |           | ip igmp | version 2 |     |
| ip igmp            | version | strict    |         |           |     |
Syntax
| ip igmp    | version | <VERSION> | strict |     |     |
| ---------- | ------- | --------- | ------ | --- | --- |
| no ip igmp | version | <VERSION> | strict |     |     |
Description
ConfiguresanIGMPstrictversiononaninterface,dependingonthecommandcontextyouarein.Drops
packetsthatdonotmatchtheconfiguredversion.
Thenoformofthecommandremovesthestrictversionconfigurationfromtheinterface.
Commandcontext
config-if-vlan
config-if
config-lag-if
Parameters
<VERSION>
SpecifiestheIGMPversionontheinterface.Select2forIGMPv2(RFC2236).Select3forIGMPv3
(RFC3376).Values:2or3.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringtheIGMPstrictversionto2oninterfaceVLAN2:
| switch(config)#         |     | interface | vlan | 2            |          |
| ----------------------- | --- | --------- | ---- | ------------ | -------- |
| switch(config-if-vlan)# |     |           | ip   | igmp version | 2 strict |
ResettingtheIGMPstrictversiontothedefault(none):
| switch(config-if)# |      |     | no ip igmp | version | 2 strict |
| ------------------ | ---- | --- | ---------- | ------- | -------- |
| no ip              | igmp |     |            |         |          |
Syntax
no ip igmp
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 29

Description
DisablesallIGMPconfigurationsonaninterface,dependingonthecommandcontextyouarein.
Commandcontext
config-if-vlan
config-if
config-lag-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
RemovesIGMPoninterfaceVLAN2:
| switch(config)#         | interface | vlan 2     |     |
| ----------------------- | --------- | ---------- | --- |
| switch(config-if-vlan)# |           | no ip igmp |     |
| show ip                 | igmp      |            |     |
Syntax
| show ip igmp | [vrf <VRF-NAME> | | all-vrfs] | [vsx-peer] |
| ------------ | --------------- | ----------- | ---------- |
Description
ShowsIGMPconfigurationinformationandstatus,orshowsinformationbyVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
| vrf <VRF-NAME> | | all-vrfs |     |     |
| -------------- | ---------- | --- | --- |
Optional.UsedtoshowinformationbyVRF.SpecifytheVRFbyVRFname.Withno<VRF-NAME>
specified,thedefaultVRFisimplied.ToshowinformationforallVRFs,specifyall-vrfs.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPconfigurationandstatus:
| switch#   | show ip igmp |     |     |
| --------- | ------------ | --- | --- |
| VRF Name  | : default    |     |     |
| Interface | : vlan2      |     |     |
InternetGroupManagementProtocol(IGMP)|30

| IGMP Configured |            | Version |         | : 3        |     |     |
| --------------- | ---------- | ------- | ------- | ---------- | --- | --- |
| IGMP Operating  |            | Version |         | : 3        |     |     |
| Querier         | State      |         |         | : Querier  |     |     |
| Querier         | IP [this   | switch] |         | : 20.1.1.1 |     |     |
| Querier         | Uptime     |         |         | : 1m       | 4s  |     |
| Querier         | Expiration |         | Time    | : 0m       | 1s  |     |
| IGMP Snoop      | Enabled    |         | on VLAN | : True     |     |     |
ShowingIGMPinformationforVRFtest:
| switch#                | show        | ip igmp | vrf          | test        |           |           |
| ---------------------- | ----------- | ------- | ------------ | ----------- | --------- | --------- |
| VRF Name               | : test      |         |              |             |           |           |
| Interface              | :           | 1/1/2   |              |             |           |           |
| IGMP Configured        |             | Version |              | : 3         |           |           |
| IGMP Operating         |             | Version |              | : 2         |           |           |
| Querier                | State       |         |              | : Querier   |           |           |
| Querier                | IP [this    | switch] |              | : 100.1.1.1 |           |           |
| Querier                | Uptime      |         |              | : 2m        | 55s       |           |
| Querier                | Expiration  |         | Time         | : 0m        | 16s       |           |
| Active Group           |             | Address | Vers         | Mode        | Uptime    | Expires   |
| ---------------------- |             |         | ----         | ----        | --------- | --------- |
| 240.100.3.194          |             |         | 3            | INC         | 0m 30s    | 3m 50s    |
| IGMP is                | not enabled |         | on interface |             | 1/1/3     |           |
| VRF Name               | : test      |         |              |             |           |           |
| Interface              | :           | vlan2   |              |             |           |           |
| IGMP Configured        |             | Version |              | : 3         |           |           |
| IGMP Operating         |             | Version |              | : 3         |           |           |
| Querier                | State       |         |              | : Querier   |           |           |
| Querier                | IP [this    | switch] |              | : 20.1.1.1  |           |           |
| Querier                | Uptime      |         |              | : 1m        | 4s        |           |
| Querier                | Expiration  |         | Time         | : 0m        | 1s        |           |
| IGMP Snoop             | Enabled     |         | on VLAN      | : True      |           |           |
| Active Group           |             | Address | Vers         | Mode        | Uptime    | Expires   |
| ---------------------- |             |         | ----         | ----        | --------- | --------- |
| 238.224.153.165        |             |         | 2            |             | 0m 38s    | 3m 42s    |
| VRF Name               | : test      |         |              |             |           |           |
| Interface              | :           | vlan10  |              |             |           |           |
| IGMP Configured        |             | Version |              | : 3         |           |           |
| IGMP Operating         |             | Version |              | : 3         |           |           |
| Querier                | State       |         |              | : Querier   |           |           |
| Querier                | IP [this    | switch] |              | : 10.1.1.1  |           |           |
| Querier                | Uptime      |         |              | : 1m        | 4s        |           |
| Querier                | Expiration  |         | Time         | : 0m        | 1s        |           |
| IGMP Snoop             | Enabled     |         | on VLAN      | : True      |           |           |
| Active Group           |             | Address | Vers         | Mode        | Uptime    | Expires   |
| ---------------------- |             |         | ----         | ----        | --------- | --------- |
| 239.209.3.194          |             |         | 3            | INC         | 0m 38s    | 3m 42s    |
ShowingIGMPinformationforallVRFs:
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 31

| switch#                | show       | ip igmp  | all-vrfs |             |           |           |
| ---------------------- | ---------- | -------- | -------- | ----------- | --------- | --------- |
| VRF Name               | :          | test     |          |             |           |           |
| Interface              | :          | 1/1/2    |          |             |           |           |
| IGMP Configured        |            | Version  |          | : 3         |           |           |
| IGMP Operating         |            | Version  |          | : 2         |           |           |
| Querier                | State      |          |          | : Querier   |           |           |
| Querier                | IP [this   | switch]  |          | : 100.1.1.1 |           |           |
| Querier                | Uptime     |          |          | : 2m        | 55s       |           |
| Querier                | Expiration |          | Time     | : 0m        | 16s       |           |
| Active                 | Group      | Address  | Vers     | Mode        | Uptime    | Expires   |
| ---------------------- |            |          | ----     | ----        | --------- | --------- |
| 240.100.3.194          |            |          | 3        | INC         | 0m 30s    | 3m 50s    |
| VRF Name               | :          | test     |          |             |           |           |
| Interface              | :          | vlan2    |          |             |           |           |
| IGMP Configured        |            | Version  |          | : 3         |           |           |
| IGMP Operating         |            | Version  |          | : 3         |           |           |
| Querier                | State      |          |          | : Querier   |           |           |
| Querier                | IP [this   | switch]  |          | : 20.1.1.1  |           |           |
| Querier                | Uptime     |          |          | : 1m        | 4s        |           |
| Querier                | Expiration |          | Time     | : 0m        | 1s        |           |
| IGMP Snoop             | Enabled    |          | on VLAN  | : True      |           |           |
| Active                 | Group      | Address  | Vers     | Mode        | Uptime    | Expires   |
| ---------------------- |            |          | ----     | ----        | --------- | --------- |
| 238.224.153.165        |            |          | 2        |             | 0m 38s    | 3m 42s    |
| VRF Name               | :          | default  |          |             |           |           |
| Interface              | :          | vlan5    |          |             |           |           |
| IGMP Configured        |            | Version  |          | : 3         |           |           |
| IGMP Operating         |            | Version  |          | : 2         |           |           |
| Querier                | State      |          |          | : Querier   |           |           |
| Querier                | IP [this   | switch]  |          | : 50.1.1.1  |           |           |
| Querier                | Uptime     |          |          | : 1m        | 1s        |           |
| Querier                | Expiration |          | Time     | : 0m        | 4s        |           |
| IGMP Snoop             | Enabled    |          | on VLAN  | : False     |           |           |
| VRF Name               | :          | test     |          |             |           |           |
| Interface              | :          | vlan10   |          |             |           |           |
| IGMP Configured        |            | Version  |          | : 3         |           |           |
| IGMP Operating         |            | Version  |          | : 3         |           |           |
| Querier                | State      |          |          | : Querier   |           |           |
| Querier                | IP [this   | switch]  |          | : 10.1.1.1  |           |           |
| Querier                | Uptime     |          |          | : 1m        | 4s        |           |
| Querier                | Expiration |          | Time     | : 0m        | 1s        |           |
| IGMP Snoop             | Enabled    |          | on VLAN  | : True      |           |           |
| Active                 | Group      | Address  | Vers     | Mode        | Uptime    | Expires   |
| ---------------------- |            |          | ----     | ----        | --------- | --------- |
| 239.209.3.194          |            |          | 3        | INC         | 0m 38s    | 3m 42s    |
| show ip                | igmp       | counters |          |             |           |           |
Syntax
| show ip igmp | counters |     | [vrf | <VRF-NAME> | | all-vrfs] | [vsx-peer] |
| ------------ | -------- | --- | ---- | ---------- | ----------- | ---------- |
Description
ShowsIGMPcounterdetails,orshowscountersbyVRF.
Commandcontext
Operator(>)orManager(#)
InternetGroupManagementProtocol(IGMP)|32

Parameters
| vrf <VRF-NAME> | |   | all-vrfs |     |     |     |     |
| -------------- | --- | -------- | --- | --- | --- | --- |
Optional.UsedtoshowinformationbyVRF.SpecifytheVRFbyVRFname.Withno<VRF-NAME>specified,
thedefaultVRFisimplied.Specifyall-vrfstoshowinformationforallVRFs.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPcounters:
| switch# | show | ip igmp | counters |     |     |     |
| ------- | ---- | ------- | -------- | --- | --- | --- |
IGMP Counters
| Interface  | Name     |          | : vlan2   |     |               |               |
| ---------- | -------- | -------- | --------- | --- | ------------- | ------------- |
| VRF Name   |          |          | : default |     |               |               |
| Membership | Timeout  |          | : 0       |     |               |               |
|            |          |          |           |     | Rx            | Tx            |
|            |          |          |           |     | ------------- | ------------- |
| V1 All     | Hosts    | Queries  |           |     | 0             | 0             |
| V2 All     | Hosts    | Queries  |           |     | 0             | 12            |
| V3 All     | Hosts    | Queries  |           |     | 0             | 0             |
| V2 Group   | Specific | Queries  |           |     | 0             | 0             |
| V3 Group   | Specific | Queries  |           |     | 0             | 0             |
| Group And  | Source   | Specific | Queries   |     | 0             | 0             |
| V3 Member  | Reports  |          |           |     | 0             | N/A           |
| V2 Member  | Reports  |          |           |     | 0             | N/A           |
| V1 Member  | Reports  |          |           |     | 0             | N/A           |
| V2 Member  | Leaves   |          |           |     | 0             | N/A           |
| Packets    | dropped  | by       | ACL       |     | 0             | N/A           |
ShowingIGMPcountersforthedefaultVRF:
| switch# | show | ip igmp | counters | vrf default |     |     |
| ------- | ---- | ------- | -------- | ----------- | --- | --- |
IGMP Counters
| Interface  | Name     |          | : vlan2   |     |               |               |
| ---------- | -------- | -------- | --------- | --- | ------------- | ------------- |
| VRF Name   |          |          | : default |     |               |               |
| Membership | Timeout  |          | : 0       |     |               |               |
|            |          |          |           |     | Rx            | Tx            |
|            |          |          |           |     | ------------- | ------------- |
| V1 All     | Hosts    | Queries  |           |     | 0             | 0             |
| V2 All     | Hosts    | Queries  |           |     | 0             | 12            |
| V3 All     | Hosts    | Queries  |           |     | 0             | 0             |
| V2 Group   | Specific | Queries  |           |     | 0             | 0             |
| V3 Group   | Specific | Queries  |           |     | 0             | 0             |
| Group And  | Source   | Specific | Queries   |     | 0             | 0             |
| V3 Member  | Reports  |          |           |     | 0             | N/A           |
| V2 Member  | Reports  |          |           |     | 0             | N/A           |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 33

| V1 Member | Reports |        |     |     | 0   |     | N/A |
| --------- | ------- | ------ | --- | --- | --- | --- | --- |
| V2 Member | Leaves  |        |     |     | 0   |     | N/A |
| Packets   | dropped | by ACL |     |     | 0   |     | N/A |
| show ip   | igmp    | group  |     |     |     |     |     |
Syntax
show ip igmp group <GROUP-IP> [source <SOURCE-IP>] [vrf <VRF-NAME> | all-vrfs] [vsx-peer]
Description
ShowsIGMPjoinedgroupinformationforthespecifiedgroup,orshowsjoinedgroupsourceanddisplay
informationbyVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
<GROUP-IP>
SpecifiestheIPaddressofthegroup.Format:A.B.C.D
source <SOURCE-IP>
SpecifiestheIPaddressofthesource.Format:A.B.C.D
| vrf <VRF-NAME> | |   | all-vrfs |     |     |     |     |     |
| -------------- | --- | -------- | --- | --- | --- | --- | --- |
Optional.UsedtoshowinformationbyVRF.SpecifytheVRFbyVRFname.Withno<VRF-NAME>
specified,thedefaultVRFisimplied.Specifyall-vrfstoshowinformationforallVRFs.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPjoinedgroupdetailsforgroup239.1.1.10:
| switch#       | show        | ip igmp      | group   | 239.1.1.10       |       |           |         |
| ------------- | ----------- | ------------ | ------- | ---------------- | ----- | --------- | ------- |
| IGMP group    | information |              | for     | group 239.1.1.10 |       |           |         |
| Interface     | Name        | : vlan2      |         |                  |       |           |         |
| VRF Name      |             | : default    |         |                  |       |           |         |
| Group Address |             | : 239.1.1.10 |         |                  |       |           |         |
| Last Reporter |             | : 100.1.1.10 |         |                  |       |           |         |
|               |             |              |         | V1               | V2    | Sources   | Sources |
| Vers Mode     | Uptime      |              | Expires | Timer            | Timer | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3 EXC | 16m | 34s | 2m 27s |     |     |     |     |
| ----- | --- | --- | ------ | --- | --- | --- | --- |
ShowingIGMPjoinedgroupdetailsforgroup239.1.1.10andsource10.1.1.10:
InternetGroupManagementProtocol(IGMP)|34

| switch#        | show ip igmp | group      | 239.1.1.10 |     | source 10.1.1.10 |     |     |
| -------------- | ------------ | ---------- | ---------- | --- | ---------------- | --- | --- |
| Interface      | Name :       | vlan2      |            |     |                  |     |     |
| VRF Name       | : default    |            |            |     |                  |     |     |
| Group Address  | :            | 239.1.1.10 |            |     |                  |     |     |
| Source         | Address :    | 10.1.1.10  |            |     |                  |     |     |
| Mode Uptime    | Expire       |            |            |     |                  |     |     |
| ---- --------- | -------      |            |            |     |                  |     |     |
| 0m             | 13s 4m       | 7s         |            |     |                  |     |     |
ShowingIGMPjoinedgroupdetailsforgroup239.1.1.10forallVRFs:
| switch#       | show ip igmp | group        | 239.1.1.10 |            | all-vrfs |           |         |
| ------------- | ------------ | ------------ | ---------- | ---------- | -------- | --------- | ------- |
| IGMP group    | information  | for          | group      | 239.1.1.10 |          |           |         |
| Interface     | Name         | : vlan10     |            |            |          |           |         |
| VRF Name      |              | : default    |            |            |          |           |         |
| Group Address |              | : 239.1.1.10 |            |            |          |           |         |
| Last Reporter |              | : 100.1.1.10 |            |            |          |           |         |
|               |              |              |            | V1         | V2       | Sources   | Sources |
| Vers Mode     | Uptime       | Expires      |            | Timer      | Timer    | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3 EXC | 17m 5s | 4m 2s |     |     |     |     |     |
| ----- | ------ | ----- | --- | --- | --- | --- | --- |
ShowingIGMPjoinedgroupdetailsforgroup239.1.1.10source10.1.1.10forallVRFs:
| switch#        | show ip igmp | group      | 239.1.1.10 |     | source 10.1.1.10 | all-vrfs |     |
| -------------- | ------------ | ---------- | ---------- | --- | ---------------- | -------- | --- |
| Interface      | Name :       | vlan10     |            |     |                  |          |     |
| VRF Name       | : default    |            |            |     |                  |          |     |
| Group Address  | :            | 239.1.1.10 |            |     |                  |          |     |
| Source         | Address :    | 10.1.1.10  |            |     |                  |          |     |
| Mode Uptime    | Expire       |            |            |     |                  |          |     |
| ---- --------- | -------      |            |            |     |                  |          |     |
| 0m             | 39s 3m       | 41s        |            |     |                  |          |     |
ShowingIGMPjoinedgroupdetailsgroup239.1.1.10forthedefaultVRF:
| switch#       | show ip igmp | group        | 239.1.1.10 |            | vrf default |           |         |
| ------------- | ------------ | ------------ | ---------- | ---------- | ----------- | --------- | ------- |
| IGMP group    | information  | for          | group      | 239.1.1.10 |             |           |         |
| Interface     | Name         | : vlan2      |            |            |             |           |         |
| VRF Name      |              | : default    |            |            |             |           |         |
| Group Address |              | : 239.1.1.10 |            |            |             |           |         |
| Last Reporter |              | : 100.1.1.10 |            |            |             |           |         |
|               |              |              |            | V1         | V2          | Sources   | Sources |
| Vers Mode     | Uptime       | Expires      |            | Timer      | Timer       | Forwarded | Blocked |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 35

---- ---- --------- --------- --------- --------- --------- --------
| 3 EXC | 17m 35s | 3m 32s |     |     |
| ----- | ------- | ------ | --- | --- |
ShowingIGMPjoinedgroupdetailsgroup239.1.1.10source10.1.1.10forthedefaultVRF:
switch# show ip igmp group 239.1.1.10 source 10.1.1.10 vrf default
| Interface      | Name :      | vlan10     |     |     |
| -------------- | ----------- | ---------- | --- | --- |
| VRF Name       | : default   |            |     |     |
| Group          | Address :   | 239.1.1.10 |     |     |
| Source         | Address :   | 10.1.1.10  |     |     |
| Mode Uptime    | Expire      |            |     |     |
| ---- --------- | -------     |            |     |     |
| 0m             | 59s 3m      | 21s        |     |     |
| show ip        | igmp groups |            |     |     |
Syntax
| show ip igmp | groups | [vrf <VRF-NAME> | | all-vrfs] | [vsx-peer] |
| ------------ | ------ | --------------- | ----------- | ---------- |
Description
ShowsIGMPgroupinformation,oryoucandisplaygroupinformationbyVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
| vrf <VRF-NAME> | | all-vrfs |     |     |     |
| -------------- | ---------- | --- | --- | --- |
Optional.UsedtoshowinformationbyVRF.SpecifytheVRFbyVRFname.Withno<VRF-NAME>
specified,thedefaultVRFisimplied.Specifyall-vrfstoshowinformationforallVRFs.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPgroupinformation:
| switch#    | show ip igmp | groups       |            |     |
| ---------- | ------------ | ------------ | ---------- | --- |
| IGMP group | information  | for group    | 239.1.1.10 |     |
| Interface  | Name         | : vlan2      |            |     |
| VRF Name   |              | : default    |            |     |
| Group      | Address      | : 239.1.1.10 |            |     |
InternetGroupManagementProtocol(IGMP)|36

| Last Reporter |        | : 100.1.1.10 |       |       |           |         |
| ------------- | ------ | ------------ | ----- | ----- | --------- | ------- |
|               |        |              | V1    | V2    | Sources   | Sources |
| Vers Mode     | Uptime | Expires      | Timer | Timer | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3 EXC         | 0m 36s      | 3m 44s       |                  |       |           |         |
| ------------- | ----------- | ------------ | ---------------- | ----- | --------- | ------- |
| IGMP group    | information | for          | group 239.1.1.11 |       |           |         |
| Interface     | Name        | : vlan2      |                  |       |           |         |
| VRF Name      |             | : default    |                  |       |           |         |
| Group Address |             | : 239.1.1.11 |                  |       |           |         |
| Last Reporter |             | : 100.1.1.10 |                  |       |           |         |
|               |             |              | V1               | V2    | Sources   | Sources |
| Vers Mode     | Uptime      | Expires      | Timer            | Timer | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3 EXC | 0m 36s | 3m 44s |     |     |     |     |
| ----- | ------ | ------ | --- | --- | --- | --- |
ShowingIGMPgroupsforallVRFs:
switch#
|               | show ip igmp | groups       | all-vrfs        |       |           |         |
| ------------- | ------------ | ------------ | --------------- | ----- | --------- | ------- |
| IGMP group    | information  | for          | group 239.1.1.1 |       |           |         |
| Interface     | Name         | : vlan10     |                 |       |           |         |
| VRF Name      |              | : test       |                 |       |           |         |
| Group Address |              | : 239.1.1.1  |                 |       |           |         |
| Last Reporter |              | : 100.1.1.20 |                 |       |           |         |
|               |              |              | V1              | V2    | Sources   | Sources |
| Vers Mode     | Uptime       | Expires      | Timer           | Timer | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3 EXC         | 0m 13s      | 4m 7s        |                 |       |           |         |
| ------------- | ----------- | ------------ | --------------- | ----- | --------- | ------- |
| IGMP group    | information | for          | group 239.1.1.2 |       |           |         |
| Interface     | Name        | : vlan10     |                 |       |           |         |
| VRF Name      |             | : test       |                 |       |           |         |
| Group Address |             | : 239.1.1.2  |                 |       |           |         |
| Last Reporter |             | : 100.1.1.20 |                 |       |           |         |
|               |             |              | V1              | V2    | Sources   | Sources |
| Vers Mode     | Uptime      | Expires      | Timer           | Timer | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3 EXC         | 0m 13s      | 4m 7s        |                 |       |           |         |
| ------------- | ----------- | ------------ | --------------- | ----- | --------- | ------- |
| IGMP group    | information | for          | group 239.1.1.1 |       |           |         |
| Interface     | Name        | : vlan20     |                 |       |           |         |
| VRF Name      |             | : default    |                 |       |           |         |
| Group Address |             | : 239.1.1.1  |                 |       |           |         |
| Last Reporter |             | : 200.1.1.10 |                 |       |           |         |
|               |             |              | V1              | V2    | Sources   | Sources |
| Vers Mode     | Uptime      | Expires      | Timer           | Timer | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3 EXC | 0m 13s | 4m 7s |     |     |     |     |
| ----- | ------ | ----- | --- | --- | --- | --- |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 37

| IGMP group    | information | for          | group | 239.1.1.2 |           |         |
| ------------- | ----------- | ------------ | ----- | --------- | --------- | ------- |
| Interface     | Name        | : vlan20     |       |           |           |         |
| VRF Name      |             | : default    |       |           |           |         |
| Group         | Address     | : 239.1.1.2  |       |           |           |         |
| Last Reporter |             | : 200.1.1.10 |       |           |           |         |
|               |             |              | V1    | V2        | Sources   | Sources |
| Vers Mode     | Uptime      | Expires      | Timer | Timer     | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3 EXC | 0m 13s | 4m 7s |     |     |     |     |
| ----- | ------ | ----- | --- | --- | --- | --- |
ShowingIGMPgroupsforthedefaultVRF:
| switch#       | show ip     | igmp groups  | vrf   | default    |           |         |
| ------------- | ----------- | ------------ | ----- | ---------- | --------- | ------- |
| IGMP group    | information | for          | group | 239.1.1.10 |           |         |
| Interface     | Name        | : vlan2      |       |            |           |         |
| VRF Name      |             | : default    |       |            |           |         |
| Group         | Address     | : 239.1.1.10 |       |            |           |         |
| Last Reporter |             | : 100.1.1.10 |       |            |           |         |
|               |             |              | V1    | V2         | Sources   | Sources |
| Vers Mode     | Uptime      | Expires      | Timer | Timer      | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3 EXC         | 9m 23s      | 3m 20s       |       |            |           |         |
| ------------- | ----------- | ------------ | ----- | ---------- | --------- | ------- |
| IGMP group    | information | for          | group | 239.1.1.11 |           |         |
| Interface     | Name        | : vlan2      |       |            |           |         |
| VRF Name      |             | : default    |       |            |           |         |
| Group         | Address     | : 239.1.1.11 |       |            |           |         |
| Last Reporter |             | : 100.1.1.10 |       |            |           |         |
|               |             |              | V1    | V2         | Sources   | Sources |
| Vers Mode     | Uptime      | Expires      | Timer | Timer      | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3 EXC   | 9m 23s         | 3m 20s |     |     |     |     |
| ------- | -------------- | ------ | --- | --- | --- | --- |
| show ip | igmp interface |        |     |     |     |     |
Syntax
| show ip igmp | interface | {<INTF-ID>|vlan |     | <VLAN-ID>} | [vsx-peer] |     |
| ------------ | --------- | --------------- | --- | ---------- | ---------- | --- |
Description
ShowsIGMPconfigurationinformationforaspecificinterface(VLAN,portorLAG).
Commandcontext
Operator(>)orManager(#)
Parameters
<INTF-ID>
InternetGroupManagementProtocol(IGMP)|38

Specifies an interface (such as 1/1/2 or LAG10).

vlan <VLAN-ID>

Specifies a VLAN. Values: 1-4094.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP configuration information for interface VLAN 2:

switch# show ip igmp interface vlan 2

IGMP Configured Version : 3
: 3
IGMP Operating Version
Querier State
: Querier
Querier IP [this switch] : 20.1.1.1
Querier Uptime
Querier Expiration Time : 0m 1s
Snoop Enabled on VLAN

: 1m 46s

: True

show ip igmp interface counters

Syntax

show ip igmp interface {<INTF-ID> | vlan <VLAN-ID>} counters [vsx-peer]

Description

Shows IGMP counter details for a specific interface or VLAN interface.

Command context

Operator (>) or Manager (#)

Parameters

<INTF-ID>

Specifies an interface (such as 1/1/2).

vlan <VLAN-ID>

Specifies a VLAN. Values: 1-4094.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

39

ShowingIGMPcountersforinterfaceVLAN2:
| switch#    | show     | ip      | igmp interface |         | vlan 2 counters |               |               |
| ---------- | -------- | ------- | -------------- | ------- | --------------- | ------------- | ------------- |
| IGMP       | Counters |         |                |         |                 |               |               |
| Interface  |          | Name    | : vlan2        |         |                 |               |               |
| VRF        | Name     |         | : default      |         |                 |               |               |
| Membership |          | Timeout | : 0            |         |                 |               |               |
|            |          |         |                |         |                 | Rx            | Tx            |
|            |          |         |                |         |                 | ------------- | ------------- |
| V1 All     | Hosts    | Queries |                |         |                 | 0             | 0             |
| V2 All     | Hosts    | Queries |                |         |                 | 0             | 0             |
| V3 All     | Hosts    | Queries |                |         |                 | 0             | 29            |
| V2 Group   | Specific |         | Queries        |         |                 | 0             | 0             |
| V3 Group   | Specific |         | Queries        |         |                 | 0             | 2             |
| Group      | And      | Source  | Specific       | Queries |                 | 0             | 2             |
| V3 Member  |          | Reports |                |         |                 | 0             | N/A           |
| V2 Member  |          | Reports |                |         |                 | 0             | N/A           |
| V1 Member  |          | Reports |                |         |                 | 0             | N/A           |
| V2 Member  |          | Leaves  |                |         |                 | 0             | N/A           |
| Packets    | dropped  |         | by ACL         |         |                 | 0             | N/A           |
| show       | ip igmp  |         | interface      |         | group           |               |               |
Syntax
show ip igmp interface {<INTF-ID> | vlan <VLAN-ID>} group <GROUP-ID> [source <SOURCE-IP>]
[vsx-peer]
Description
ShowsIGMPjoinedgroupinformationforaspecificinterfaceorVLANinterface,orspecifyasourceIP.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTF-ID>
Specifiesaninterface(suchas1/1/2).
vlan <VLAN-ID>
SpecifiesaVLAN.Values:1-4094.
<GROUP-ID>
SpecifiestheIPaddressofthegroup.Format:A.B.C.D
source <SOURCE-IP>
SpecifiestheIPaddressofthesource.Format:A.B.C.D
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
InternetGroupManagementProtocol(IGMP)|40

ShowingIGMPjoinedgroupdetailsforgroup239.1.1.1forinterfaceVLAN10:
| switch#   | show     | ip igmp     | interface    | vlan 10         | group 239.1.1.1 |           |         |
| --------- | -------- | ----------- | ------------ | --------------- | --------------- | --------- | ------- |
| IGMP      | group    | information | for          | group 239.1.1.1 |                 |           |         |
| Interface |          | Name        | : vlan10     |                 |                 |           |         |
| VRF       | Name     |             | : default    |                 |                 |           |         |
| Group     | Address  |             | : 239.1.1.1  |                 |                 |           |         |
| Last      | Reporter |             | : 100.1.1.10 |                 |                 |           |         |
|           |          |             |              | V1              | V2              | Sources   | Sources |
| Vers      | Mode     | Uptime      | Expires      | Timer           | Timer           | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3      | INC       | 8m 10s  | 2m 21s    |     |     | 1   |     |
| ------ | --------- | ------- | --------- | --- | --- | --- | --- |
| Group  | Address   | :       | 239.1.1.1 |     |     |     |     |
| Source | Address   | :       | 10.1.1.1  |     |     |     |     |
| Mode   | Uptime    | Expire  |           |     |     |     |     |
| ----   | --------- | ------- |           |     |     |     |     |
| INC    | 8m 10s    | 2m      | 21s       |     |     |     |     |
ShowingIGMPjoinedgroupdetailsforgroup239.1.1.1forinterfaceVLAN10withsourcedetailsfor
10.1.1.1:
switch# show ip igmp interface vlan 10 group 239.1.1.1 source 10.1.1.1
| Interface |           | Name :    | vlan10    |        |     |     |     |
| --------- | --------- | --------- | --------- | ------ | --- | --- | --- |
| VRF       | Name      | : default |           |        |     |     |     |
| Group     | Address   | :         | 239.1.1.1 |        |     |     |     |
| Source    | Address   | :         | 10.1.1.1  |        |     |     |     |
| Mode      | Uptime    | Expire    |           |        |     |     |     |
| ----      | --------- | -------   |           |        |     |     |     |
| INC       | 8m 52s    | 3m        | 51s       |        |     |     |     |
| show      | ip igmp   | interface |           | groups |     |     |     |
Syntax
show ip igmp interface {<INTF-ID> | vlan <VLAN-ID>} groups [vsx-peer]
Description
ShowsIGMPgroupinformationforaspecificinterfaceorVLANinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTF-ID>
Specifiesaninterface(suchas1/1/2).
vlan <VLAN-ID>
SpecifiesaVLAN.Values:1-4094.
[vsx-peer]
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 41

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPgroupsforinterfaceVLAN2:
| switch#   | show ip igmp      | interface    | vlan 2          | groups |           |         |
| --------- | ----------------- | ------------ | --------------- | ------ | --------- | ------- |
| IGMP      | group information | for          | group 239.1.1.1 |        |           |         |
| Interface | Name              | : vlan2      |                 |        |           |         |
| VRF       | Name              | : default    |                 |        |           |         |
| Group     | Address           | : 239.1.1.1  |                 |        |           |         |
| Last      | Reporter          | : 100.1.1.10 |                 |        |           |         |
|           |                   |              | V1              | V2     | Sources   | Sources |
| Vers      | Mode Uptime       | Expires      | Timer           | Timer  | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3      | INC 4m 40s    | 3m 51s    |     |     | 1   |     |
| ------ | ------------- | --------- | --- | --- | --- | --- |
| Group  | Address :     | 239.1.1.1 |     |     |     |     |
| Source | Address :     | 10.1.1.1  |     |     |     |     |
| Mode   | Uptime Expire |           |     |     |     |     |
----------------------
| INC       | 4m 40s 3m         | 51s          |                 |       |           |         |
| --------- | ----------------- | ------------ | --------------- | ----- | --------- | ------- |
| IGMP      | group information | for          | group 239.1.1.2 |       |           |         |
| Interface | Name              | : vlan2      |                 |       |           |         |
| VRF       | Name              | : default    |                 |       |           |         |
| Group     | Address           | : 239.1.1.2  |                 |       |           |         |
| Last      | Reporter          | : 100.1.1.10 |                 |       |           |         |
|           |                   |              | V1              | V2    | Sources   | Sources |
| Vers      | Mode Uptime       | Expires      | Timer           | Timer | Forwarded | Blocked |
---- ---- --------- --------- --------- --------- --------- --------
| 3      | INC 4m 40s        | 3m 51s    |            |     | 1   |     |
| ------ | ----------------- | --------- | ---------- | --- | --- | --- |
| Group  | Address :         | 239.1.1.2 |            |     |     |     |
| Source | Address :         | 10.1.1.1  |            |     |     |     |
| Mode   | Uptime Expire     |           |            |     |     |     |
| ----   | --------- ------- |           |            |     |     |     |
| INC    | 4m 40s 3m         | 51s       |            |     |     |     |
| show   | ip igmp interface |           | statistics |     |     |     |
Syntax
show ip igmp interface {<INTF-ID> | vlan <VLAN-ID>} statistics [vsx-peer]
Description
InternetGroupManagementProtocol(IGMP)|42

ShowsIGMPstatisticsforaspecificinterfaceorVLANinterface,includinggroupsjoined.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTF-ID>
Specifiesaninterface(suchas1/1/2orLAG1).
vlan <VLAN-ID>
SpecifiesaVLAN.Values:1-4094.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPstatisticsforinterfaceVLAN2:
| switch# | show ip igmp interface | vlan 2 statistics |
| ------- | ---------------------- | ----------------- |
IGMP statistics
| Interface       | Name : vlan2       |     |
| --------------- | ------------------ | --- |
| VRF Name        | : default          |     |
| Number          | of Include Groups  | : 2 |
| Number          | of Exclude Groups  | : 0 |
| Number          | of Static Groups   | : 0 |
| Total Multicast | Groups Joined      | : 2 |
| show ip         | igmp static-groups |     |
Syntax
show ip igmp static-groups [vrf <VRF-NAME> | all-vrfs] [vsx-peer]
Description
ShowsIGMPstaticgroups,orshowsinformationbyVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
| vrf <VRF-NAME> | | all-vrfs |     |
| -------------- | ---------- | --- |
Optional.UsedtoshowinformationbyVRF.SpecifytheVRFbyVRFname.Withno<VRF-NAME>specified,
thedefaultVRFisimplied.Specifyall-vrfstoshowinformationforallVRFs.
[vsx-peer]
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 43

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPstatic-groupinformation:
| switch#         | show ip igmp      | static-groups       |     |     |
| --------------- | ----------------- | ------------------- | --- | --- |
| IGMP Static     | Group             | Address Information |     |     |
| VRF Name        | default           |                     |     |     |
| Interface       | Name              | Group Address       |     |     |
| --------------- | ----------------- |                     |     |     |
| vlan10          |                   | 238.1.1.1           |     |     |
ShowingIGMPstatics-groupinformationforallVRFs:
| switch#         | show ip igmp      | static-groups       | all-vrfs |     |
| --------------- | ----------------- | ------------------- | -------- | --- |
| IGMP Static     | Group             | Address Information |          |     |
| VRF Name        | :test             |                     |          |     |
| Interface       | Name              | Group Address       |          |     |
| --------------- | ----------------- |                     |          |     |
| vlan20          |                   | 239.1.1.1           |          |     |
| VRF Name        | :default          |                     |          |     |
| Interface       | Name              | Group Address       |          |     |
| --------------- | ----------------- |                     |          |     |
| vlan10          |                   | 238.1.1.1           |          |     |
ShowingIGMPstatic-groupinformationforVRFtest:
| switch#         | show ip igmp      | static-groups       | vrf test |     |
| --------------- | ----------------- | ------------------- | -------- | --- |
| IGMP Static     | Group             | Address Information |          |     |
| VRF Name        | :test             |                     |          |     |
| Interface       | Name              | Group Address       |          |     |
| --------------- | ----------------- |                     |          |     |
| vlan20          |                   | 239.1.1.1           |          |     |
| show ip         | igmp statistics   |                     |          |     |
Syntax
| show ip igmp | statistics | [vrf <VRF-NAME> | | all-vrfs] | [vsx-peer] |
| ------------ | ---------- | --------------- | ----------- | ---------- |
Description
ShowsIGMPstatistics,includinggroupsjoined,orshowsstatisticsbyVRF.
Commandcontext
InternetGroupManagementProtocol(IGMP)|44

Operator(>)orManager(#)
Parameters
| vrf <VRF-NAME> | | all-vrfs |     |
| -------------- | ---------- | --- |
Optional.UsedtoshowinformationbyVRF.SpecifytheVRFbyVRFname.Withno<VRF-NAME>specified,
thedefaultVRFisimplied.Specifyall-vrfstoshowinformationforallVRFs.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPstatistics:
| switch# | show ip igmp statistics |     |
| ------- | ----------------------- | --- |
IGMP statistics
| VRF Name        | : default         |     |
| --------------- | ----------------- | --- |
| Number          | of Include Groups | : 1 |
| Number          | of Exclude Groups | : 0 |
| Number          | of Static Groups  | : 0 |
| Total Multicast | Groups Joined     | : 1 |
ShowingIGMPstatisticsforallVRFs:
| switch# | show ip igmp statistics | all-vrfs |
| ------- | ----------------------- | -------- |
IGMP statistics
| VRF Name        | : test            |     |
| --------------- | ----------------- | --- |
| Number          | of Include Groups | : 2 |
| Number          | of Exclude Groups | : 0 |
| Number          | of Static Groups  | : 0 |
| Total Multicast | Groups Joined     | : 2 |
| VRF Name        | : default         |     |
| Number          | of Include Groups | : 1 |
| Number          | of Exclude Groups | : 0 |
| Number          | of Static Groups  | : 0 |
| Total Multicast | Groups Joined     | : 1 |
ShowingIGMPstatisticsforVRFtest:
| switch# | show ip igmp statistics | vrf test |
| ------- | ----------------------- | -------- |
IGMP statistics
| VRF Name | : test            |     |
| -------- | ----------------- | --- |
| Number   | of Include Groups | : 2 |
| Number   | of Exclude Groups | : 0 |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 45

Number of Static Groups
:
Total Multicast Groups Joined :

0
2

Internet Group Management Protocol (IGMP) | 46

Chapter 4

IGMP snooping

IGMP snooping

IGMP snooping runs on a Layer 2 device as a multicast constraining mechanism to improve multicast
forwarding efficiency. It creates Layer 2 multicast forwarding entries from IGMP packets that are exchanged
between the hosts and the router.

When IGMP snooping is not enabled, the snooping switch floods multicast packets to all hosts in a VLAN.
IGMP L2 snooping switch provides the benefit of conserving bandwidth on those segments of the network
where no node has expressed interest in receiving packets addressed to the group address. When IGMP
snooping is enabled, the L2 snooping switch forwards multicast packets of known multicast groups to only
the receivers.

IGMP snooping defaults, protocols, and supported
configuration

IGMP snooping default configuration:

n IGMP snooping is disabled by default.

n Version 3 is used by default.

IGMP snooping related protocols:

n IGMPv2 (RFC 2236)

n IGMPv3 (RFC 2276)

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

47

n Considerations for Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD)

Snooping Switches (RFC 4541)

Static groups:

You can configure a maximum of 32 IGMP snooping static groups.

How IGMP snooping works
IGMP message types include: Query, Report (Join), and Leave Group. An IGMP snooping enabled Layer 2
device performs differently depending on the message type.

Query

A message sent from the querier (multicast router or switch) asking for a response from each host belonging
to the multicast group. If a multicast router supporting IGMP is not present, then the switch must assume
this function in order to elicit group membership information from the hosts on the network.

The IGMP querier periodically sends IGMP general queries to all hosts and routers on the local subnet to
check for the existence of multicast group members. After receiving an IGMP general query, the snooping
switch forwards the query to all ports in the VLAN except the receiving port.

Report (Join)

A message sent by a host to the querier to indicate that the host wants to be or is a member of a given
group indicated in the report message.

A host sends an IGMP report to the IGMP querier for the following purposes:

n Responds to queries if the host is a multicast group member.

n Applies for a multicast group membership.

After receiving an IGMP report from a host, the snooping switch forwards the report through all the router
ports in the VLAN. It also looks up the forwarding table for a matching entry as follows:

n If no match is found, the snooping switch creates a forwarding entry with the receiving port as an

outgoing interface. It also starts group membership expiry timer for the port to track the amount of time
that must pass before a multicast router decides there are no more members of a group on a network.

n If a match is found but the matching forwarding entry does not contain the receiving port, the snooping
switch adds the receiving port to the outgoing interface list. It also starts group membership expiry timer
for the port.

n If a match is found and the matching forwarding entry contains the receiving port, the snooping switch

restarts the group membership expiry timer for the port.

Leave Group

A message sent by a host to the querier to indicate that the host has ceased to be a member of a specific
multicast group.

An IGMPv1 receiver host does not send any leave messages when it leaves a multicast group. The snooping
switch cannot immediately update the status of the port that connects to the receiver host. The snooping
switch does not remove the port from the outgoing interface list in the associated forwarding entry until the
group membership timer expires.

An IGMPv2 or IGMPv3 host sends an IGMP leave message when it leaves a multicast group. Upon receiving
leave message, the switch forwards the IGMP leave message to all router ports in the VLAN . IGMP querier
then sends an IGMP group-specific query to the multicast group to identify whether the group has active
receivers attached to the receiving port.

IGMP snooping | 48

After receiving the IGMP group-specific query, the switch forwards the query through all router ports and
member ports of the group in the VLAN. Then, it waits for the responding IGMP report message from the
directly connected hosts. If the port does not receive an IGMP report message when the group membership
timer expires, the snooping switch removes the port from the forwarding entry for the multicast group.

IGMP snooping configuration task list

n Enabling or Disabling IGMP Snooping

n Specifying the IGMP snooping version

n Configuring IGMP snooping static groups

n Enabling Drop-Unknown Filters

n Configuring IGMP snooping fast learn ports globally

n Configuring IGMP snooping per port filtering

n Disabling IGMP Snooping

n Viewing IGMP snooping information

Enabling or disabling IGMP snooping
IGMP snooping is disabled by default. The default behavior is to flood multicast traffic in the VLAN. Use the
following to enable IGMP snooping.

Prerequisites

You must be in the VLAN configuration context, as indicated by the switch(config-vlan)# prompt.

The VLAN has to be configured and up.

Procedure

Enable IGMP snooping on a VLAN using the following command.
ip igmp snooping {enable | disable}

For example, the following command enables IGMP snooping on VLAN 2:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping enable

Use the no command to disable IGMP snooping on a VLAN.

Specifying the IGMP snooping version
The IGMP snooping version can be either 2 (IGMPv2) or 3 (IGMPv3). The default is 3. IGMPv2 supports
filtering based on groups. IGMPv3 is more advanced and includes filtering based on source and groups.

Prerequisites

You must be in the VLAN configuration context, as indicated by the switch(config-vlan)# prompt.

Procedure

Specify the IGMP snooping version for a VLAN using the following command.

ip igmp snooping version <VERSION>

For example, the following command sets the IGMP snooping version to 2 on VLAN 2:

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

49

| switch(config)# |     | vlan 2 |     |     |     |     |     |
| --------------- | --- | ------ | --- | --- | --- | --- | --- |
switch(config-vlan)#
|             |     | ip   | igmp snooping |     | version | 2      |     |
| ----------- | --- | ---- | ------------- | --- | ------- | ------ | --- |
| Configuring |     | IGMP | snooping      |     | static  | groups |     |
ConfigureIGMPsnoopingstaticgroups.
Prerequisites
YoumustbeintheVLANconfigurationcontext,asindicatedbytheswitch(config-vlan)#prompt.
Procedure
ConfigureanIGMPsnoopingstaticgrouponaVLANusingthefollowingcommand.
| ip igmp snooping |     | static-group | <MULTICAST-IP-ADDRESS> |     |     |     |     |
| ---------------- | --- | ------------ | ---------------------- | --- | --- | --- | --- |
Forexample,thefollowingcommandconfigurestheIGMPsnoopingstaticmulticastgroupas239.1.1.1on
VLAN2:
| switch(config)#      |     | vlan 2 |               |     |              |           |     |
| -------------------- | --- | ------ | ------------- | --- | ------------ | --------- | --- |
| switch(config-vlan)# |     | ip     | igmp snooping |     | static-group | 239.1.1.1 |     |
ThenoformofthecommandremovestheIGMPsnoopingstaticgroup.
| Enabling | drop-unknown |     |     | filters |     |     |     |
| -------- | ------------ | --- | --- | ------- | --- | --- | --- |
WhileIGMPsnoopingisenabled,thetrafficwillbeforwardedonlytojoinedports.Configuringdrop
unknownfilters,ensuresthatpacketsarenotforwardedtoportswherearequestforthetrafficstreamhas
notbeenreceived.
ThiscouldeitherbeafilteracrossallVLANs(vlan-shared)orperVLAN(vlan-exclusive).Thedefaultis
vlan-shared.
Prerequisites
Youmustbeintheconfigurationcontext,asindicatedbytheswitch(config)#prompt.
Procedure
Globallyenabledroppingmulticastdatausingthefollowingcommand.
| ip igmp snooping |     | drop-unknown | {vlan-shared |     | | vlan-exclusive} |     |     |
| ---------------- | --- | ------------ | ------------ | --- | ----------------- | --- | --- |
Forexample,thefollowingcommandconfiguresasharedVLANfilterontheswitch:
| switch(config)# |     | ip igmp | snooping | drop-unknown |      | vlan-shared |                |
| --------------- | --- | ------- | -------- | ------------ | ---- | ----------- | -------------- |
| Configuring     |     | IGMP    | snooping |              | fast | learn       | ports globally |
Configuringfastlearnonaportenablesfasterresponsetotopologychangenotifications.Whenspanning
treechangestheportstatefromblockedtoforwarding,thedeviceactingasquerierwillimmediatelysenda
generalqueryonthefastlearnenabledport.Thenthedeviceactingasanon-querierwillreplaythejoins.
Thiswillhelpinfasterconvergenceofmulticastflows.
Prerequisites
IGMPsnooping|50

Youmustbeintheconfigurationcontext,asindicatedbytheswitch(config)#prompt.
Procedure
ConfigureoneormoreportsasIGMPsnoopingfastlearnportsusingthefollowingcommand.
| ip igmp snooping | fastlearn | <PORT-LIST> |     |     |     |
| ---------------- | --------- | ----------- | --- | --- | --- |
Forexample,thefollowingcommandconfiguresports1/1/1-1/1/3asfastlearnports:
| switch(config)# | ip igmp | snooping | fastlearn | 1/1/1-1/1/3 |           |
| --------------- | ------- | -------- | --------- | ----------- | --------- |
| Configuring     | IGMP    | snooping | per       | port        | filtering |
ConfigureIGMPsnoopingtraffichandlingbyspecifyingauto,blocked,orforwardforaport,listofportsor
rangeofports.InautomodetrafficflowiscontrolledbytheIGMPjoins/leaves.Automodeisthedefault.In
blockedmode,joinsandtrafficarealwaysblockedonthisport.Inforwardmodetrafficisalwaysforwarded
onthisport,irrespectiveofjoins.
Prerequisites
YoumustbeintheVLANconfigurationcontext,asindicatedbytheswitch(config-vlan)#prompt.
Procedure
ConfigureIGMPsnoopingtraffichandlingforportsonaVLANusingthefollowingcommands.
n Configurethespecifiedportsinautomodeusingthefollowingcommand:ip igmp snooping auto
<PORT-LIST>.
Configurethespecifiedportsinblockedmodeusingthefollowingcommand:ip
n igmp snooping
| blocked <PORT-LIST>. |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- |
n Configurethespecifiedportsinforwardmodeusingthefollowingcommand:ip igmp snooping
forward
<PORT-LIST>.
Forexample,thefollowingcommandconfiguresports1/1/1,1/1/2,and1/1/3inautomodeforVLAN2:
| switch(config)#      | vlan | 2                |      |                   |     |
| -------------------- | ---- | ---------------- | ---- | ----------------- | --- |
| switch(config-vlan)# |      | ip igmp snooping | auto | 1/1/1,1/1/2-1/1/3 |     |
| Disabling            | IGMP | snooping         |      |                   |     |
Prerequisites
YoumustbeintheVLANconfigurationcontext,asindicatedbytheswitch(config-vlan)#prompt.
Procedure
DisableIGMPsnoopingonaVLANusingthefollowingcommand.
| no ip igmp snooping |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
Forexample,thefollowingcommandremovesIGMPsnoopingonVLAN2:
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 51

| switch(config)# | vlan | 2   |     |     |
| --------------- | ---- | --- | --- | --- |
switch(config-vlan)#
|         |      | no ip igmp | snooping    |     |
| ------- | ---- | ---------- | ----------- | --- |
| Viewing | IGMP | snooping   | information |     |
Prerequisites
UsetheseshowcommandsfromtheOperator(>)orManager(#)context.
Procedure
ToviewIGMPsnoopinginformation,usethefollowingcommands.
n ToviewIGMPsnoopingconfigurationdetailsandstatus,use:show ip igmp snooping.
n ToviewIGMPsnoopingquerypacketTx,Rx,andErrorpacketcounterdetails,use:show ip igmp
| snooping | counters. |     |     |     |
| -------- | --------- | --- | --- | --- |
n ToviewIGMPsnoopinggroupinformation,use:show ip igmp snooping groups.
n ToviewIGMPsnoopingprotocolinformationandthenumberofgroupsjoined,use:show ip igmp
| snooping | statistics. |     |     |     |
| -------- | ----------- | --- | --- | --- |
n ToviewIGMPsnoopingquerypacketTx,Rx,andErrorpacketcountersforthespecifiedVLAN,use:show
| ip igmp | snooping vlan | counters. |     |     |
| ------- | ------------- | --------- | --- | --- |
ToviewIGMPsnoopingstatisticsdetailsforthespecifiedVLANincludingthenumberofdifferentgroups
n
| joinedfortheVLAN,use:show |     | ip igmp | snooping | vlan statistics. |
| ------------------------- | --- | ------- | -------- | ---------------- |
ToviewIGMPsnoopinggroupinformationforthespecifiedVLAN,use:show ip igmp snooping vlan.
n
ToviewIGMPsnoopinggroupdetailsforthespecifiedVLANincludinginformationaboutallIGMP
n
snoopinggroupsorsourceslearnedonaparticularport,use:show ip igmp snooping vlan group
port.
n ToviewIGMPsnoopingstaticgroupsdetailsforthespecifiedVLAN,use:show ip igmp snooping
static-groups.
| IGMP    | snooping | commands         |     |     |
| ------- | -------- | ---------------- | --- | --- |
| ip igmp | snooping | {enable|disable} |     |     |
Syntax
| ip igmp | snooping {enable | | disable} |     |     |
| ------- | ---------------- | ---------- | --- | --- |
Description
EnablesordisablesIGMPsnoopingontheVLAN.Bydefault,IGMPsnoopingisdisabled.
Commandcontext
config-vlan
Parameters
| {enable | | disable} |     |     |     |
| ------- | ---------- | --- | --- | --- |
SpecifiesenablingordisablingIGMPsnoopingontheVLAN.Default:disable.
Authority
IGMPsnooping|52

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnableIGMPsnoopingonaVLAN:
| switch(config)#      | vlan | 2       |                 |
| -------------------- | ---- | ------- | --------------- |
| switch(config-vlan)# |      | ip igmp | snooping enable |
DisableIGMPsnoopingonaVLAN:
| switch(config)#      | vlan     | 2       |                  |
| -------------------- | -------- | ------- | ---------------- |
| switch(config-vlan)# |          | ip igmp | snooping disable |
| ip igmp              | snooping | apply   | access-list      |
Syntax
| ip igmp    | snooping apply | access-list | <ACL-NAME> |
| ---------- | -------------- | ----------- | ---------- |
| no ip igmp | snooping apply | access-list | <ACL-NAME> |
Description
ConfigurestheACLonaparticularinterfacetofiltertheIGMPjoinorleavepacketsbasedonrulessetinthe
particularACLname.
ThenoformofthiscommandunconfigurestherulessetfortheACL.
ThisconfigurationwilloverridetheACLassociatedwithIGMPsnoopingonthecorrespondingL2VLAN.
Commandcontext
config-vlan
Parameters
access-list
AssociatesanACLwiththeIGMP.
<ACL-NAME>
SpecifiesthenameoftheACL.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
ExistingclassifiercommandsareusedtoconfiguretheACL.IncaseanIGMPv3packetwithmultiplegroup
addressesisreceived,itwillonlyprocessthepermittedgroupaddressesbasedontheACLruleset,andany
existingjoinswilltimeout.Ifthereisnomatchorifthereisadenyrulematch,thepacketisdropped.
IftheaccesslistisconfiguredforbothL2VLANandL3VLAN,theL3VLANconfigurationwillbeapplied.
Examples
ConfiguringtheACLtofilterIGMPpacketsbasedonrulessetinaccesslistmygroup:
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 53

| switch(config)# |     |     | access-list |     | ip mygroup |     |     |     |
| --------------- | --- | --- | ----------- | --- | ---------- | --- | --- | --- |
switch(config-acl-ip)#
|                        |     |     |           | permit  | igmp     | any 239.1.1.1 |             |         |
| ---------------------- | --- | --- | --------- | ------- | -------- | ------------- | ----------- | ------- |
| switch(config-acl-ip)# |     |     |           | exit    |          |               |             |         |
| switch(config)#        |     |     | interface | vlan    | 2        |               |             |         |
| switch(config-vlan)#   |     |     |           | ip igmp | snooping | apply         | access-list | mygroup |
ConfiguringtheACLtoremovetherulessetinaccesslistmygroup:
switch(config-vlan)# no ip igmp snooping apply access-list mygroup
| ip igmp | snooping |     | auto |     | vlan |     |     |     |
| ------- | -------- | --- | ---- | --- | ---- | --- | --- | --- |
Syntax
| ip igmp    | snooping | [auto | vlan  | <VLAN-LIST>] |              |     |     |     |
| ---------- | -------- | ----- | ----- | ------------ | ------------ | --- | --- | --- |
| no ip igmp | snooping |       | [auto | vlan         | <VLAN-LIST>] |     |     |     |
Description
Configuresthespecifiedportsinautomode.InautomodetrafficflowiscontrolledbytheIGMP
joins/leaves.Automodeisthedefault.
ThenoformofthiscommandremovesautomodeportsfortheVLAN.
Commandcontext
config-if
Parameters
<VLAN-LIST>
Required:SpecifiesalistofVLANsonwhichtheportshouldbeconfiguredasanautoport.Specifiesthe
numberofasingleVLANoraseriesofnumbersforarangeofVLANs,separatedbycommas(10,20,30,
40),dashes(10-40),orboth(10-40,60).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ConfiguringautoportsforVLANontheinterface:
| switch#            | configure |     | terminal  |         |          |           |       |     |
| ------------------ | --------- | --- | --------- | ------- | -------- | --------- | ----- | --- |
| switch(config)#    |           |     | int 1/1/1 |         |          |           |       |     |
| switch(config-if)# |           |     | no        | shut    |          |           |       |     |
| switch(config-if)# |           |     | no        | routing |          |           |       |     |
| switch(config-if)# |           |     | vlan      | trunk   | allowed  | 10-20     |       |     |
| switch(config-if)# |           |     | ip        | igmp    | snooping | auto vlan | 10    |     |
| switch(config-if)# |           |     | ip        | igmp    | snooping | auto vlan | 10-20 |     |
| ip igmp            | snooping  |     | blocked   |         | vlan     |           |       |     |
Syntax
| ip igmp    | snooping | [blocked |          | vlan | <VLAN-LIST>] |     |     |     |
| ---------- | -------- | -------- | -------- | ---- | ------------ | --- | --- | --- |
| no ip igmp | snooping |          | [blocked | vlan | <VLAN-LIST>] |     |     |     |
IGMPsnooping|54

Description
ConfiguresthespecifiedportsinblockedmodeforthespecifiedVLANlist.Inblockedmode,joinsandtraffic
arealwaysblockedonthisport.
Thenoformofthiscommanddisablesblockedports.
Commandcontext
config-if
Parameters
<VLAN-LIST>
Required:SpecifiesalistofVLANsonwhichtheportshouldbeconfiguredasablockedport.Specifies
thenumberofasingleVLANoraseriesofnumbersforarangeofVLANs,separatedbycommas(10,20,
30,40),dashes(10-40),orboth(10-40,60).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ConfiguringblockedportsfortheVLANontheinterface:
| switch#            | configure | terminal     |               |              |       |
| ------------------ | --------- | ------------ | ------------- | ------------ | ----- |
| switch(config)#    |           | int 1/1/1    |               |              |       |
| switch(config-if)# |           | no shut      |               |              |       |
| switch(config-if)# |           | no routing   |               |              |       |
| switch(config-if)# |           | vlan         | trunk allowed | 10-20        |       |
| switch(config-if)# |           | ip igmp      | snooping      | blocked vlan | 10    |
| switch(config-if)# |           | ip igmp      | snooping      | blocked vlan | 10-20 |
| ip igmp            | snooping  | drop-unknown |               |              |       |
Syntax
| ip igmp    | snooping drop-unknown |              | {vlan-shared | | vlan-exclusive} |     |
| ---------- | --------------------- | ------------ | ------------ | ----------------- | --- |
| no ip igmp | snooping              | drop-unknown |              |                   |     |
Description
Configuresdrop-unknownmode.WhileIGMPsnoopingisenabled,thetrafficwillbeforwardedonlyto
portsthatmadeanIGMPrequestforthemulticast.Dropunknownfiltersensurethatpacketsarenot
forwardedtoportsthatdidnotmakearequestforthetrafficstream.Thiscouldeitherbeafilteracrossall
VLANs(vlan-shared)orperVLAN(vlan-exclusive).Thedefaultisvlan-shared.
Thenoformofthiscommanddisablesdropunknownontheswitch.
Commandcontext
config
Parameters
vlan-shared
EnablessharedVLANfilterontheswitch.Default:vlan-shared.
vlan-exclusive
EnablesexclusivedropunknownfilterperVLAN.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 55

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringsharedVLANfilterontheswitch:
| switch(config)# |     | ip igmp | snooping | drop-unknown | vlan-shared |
| --------------- | --- | ------- | -------- | ------------ | ----------- |
ConfiguringexclusivedropunknownfilterperVLAN:
| switch(config)# |     | ip igmp | snooping | drop-unknown | vlan-exclusive |
| --------------- | --- | ------- | -------- | ------------ | -------------- |
Disablingdropunknownontheswitch:
| switch(config)# |          | no ip | igmp snooping | drop-unknown |     |
| --------------- | -------- | ----- | ------------- | ------------ | --- |
| ip igmp         | snooping |       | fastlearn     |              |     |
Syntax
| ip igmp    | snooping | fastlearn | <PORT-LIST> |     |     |
| ---------- | -------- | --------- | ----------- | --- | --- |
| no ip igmp | snooping | fastlearn | <PORT-LIST> |     |     |
Description
Enablestheporttolearngroupinformationwhenreceivingatopologychangenotification.Bydefault,fast
learnisnotenabledonports.
Thenoformofthiscommanddisablesfastlearnonthespecifiedports.
Commandcontext
config
Parameters
| fastlearn | <PORT-LIST> |     |     |     |     |
| --------- | ----------- | --- | --- | --- | --- |
Specifiesalistofoneormoreportstobeconfiguredasfastlearnports.Youcanspecifyasingleport,a
comma-separatedlistofportsorarangeofportssuchas1/1/1-1/1/3.YoumayalsoenteranL2LAG(1-
128).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringfastlearnports:
| switch(config)# |     | ip igmp | snooping | fastlearn | 1/1/3       |
| --------------- | --- | ------- | -------- | --------- | ----------- |
| switch(config)# |     | ip igmp | snooping | fastlearn | 1/1/1-1/1/2 |
| switch(config)# |     | ip igmp | snooping | fastlearn | 1/1/5,1/1/6 |
IGMPsnooping|56

| ip igmp | snooping |     | fastleave |     | vlan |     |
| ------- | -------- | --- | --------- | --- | ---- | --- |
Syntax
| ip igmp    | snooping | [fastleave |     | vlan <VLAN-LIST>] |              |     |
| ---------- | -------- | ---------- | --- | ----------------- | ------------ | --- |
| no ip igmp | snooping | [fastleave |     | vlan              | <VLAN-LIST>] |     |
Description
EnablestheswitchtoimmediatelyremovetheIGMPclientfromitsIGMPtableandceasetransmitting
multicasttraffictotheclient.
Thenoformofthiscommanddisablesfastleaveonthespecifiedports.
Commandcontext
config-if
Parameters
<VLAN-LIST>
SpecifiesalistofVLANsonwhichtheportshouldbeconfiguredasafastleaveport.Specifiesthenumber
ofasingleVLANoraseriesofnumbersforarangeofVLANs,separatedbycommas(10,20,30,40),
dashes(10-40),orboth(10-40,60).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
IGMPfastleaveisconfiguredforportsonaper-VLANbasis.UponreceivingaLeaveGroupmessage,the
queriersendsanIGMPGroup-SpecificQuerymessageoutoftheinterfacetoensurethatnootherreceivers
areconnectedtotheinterface.Ifreceiversaredirectlyattachedtotheswitch,itisinefficienttosendthe
membershipqueryasthereceiverwantingtoleaveistheonlyconnectedhost.
Whenafastleaveenabledswitchportisconnectedtoasinglehostandreceivesaleave,theswitchdoesnot
waitforthequerierstatusupdateinterval,butinsteadimmediatelyremovestheIGMPclientfromitsIGMP
tableandceasestransmittingmulticasttraffictotheclient.(Iftheswitchdetectsmultipleendnodesonthe
port,FastleavedoesnotactivateregardlessofwhetheroneormoreoftheseendnodesareIGMPclients.)
ThisprocessingspeedsuptheoverallleaveprocessandalsoeliminatestheCPUoverheadofhavingto
generateanIGMPGroup-SpecificQuerymessage.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ConfiguringfastleaveportsfortheVLANontheinterface:
| switch#            | configure |     | terminal   |          |               |            |
| ------------------ | --------- | --- | ---------- | -------- | ------------- | ---------- |
| switch(config)#    |           | int | 1/1/1      |          |               |            |
| switch(config-if)# |           |     | no shut    |          |               |            |
| switch(config-if)# |           |     | no routing |          |               |            |
| switch(config-if)# |           |     | vlan       | trunk    | allowed 10-20 |            |
| switch(config-if)# |           |     | ip igmp    | snooping | fastleave     | vlan 10    |
| switch(config-if)# |           |     | ip igmp    | snooping | fastleave     | vlan 10-20 |
| ip igmp            | snooping  |     | forced     |          | fastleave     | vlan       |
Syntax
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 57

| ip igmp    | snooping | [forced-fastleave |     |     | vlan <VLAN-LIST>] |     |
| ---------- | -------- | ----------------- | --- | --- | ----------------- | --- |
| no ip igmp | snooping | [forced-fastleave |     |     | vlan <VLAN-LIST>] |     |
Description
Configuresthespecifiedportsinforcedfastleavemode.
Thenoformofthiscommanddisablesforcedfastleaveonthespecifiedports.
Commandcontext
config-if
Parameters
<VLAN-LIST>
SpecifiesalistofVLANsonwhichtheportshouldbeconfiguredasaforcedfastleaveport.Specifiesthe
numberofasingleVLANoraseriesofnumbersforarangeofVLANs,separatedbycommas(10,20,30,
40),dashes(10-40),orboth(10-40,60).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Withforcedfastleaveenabled,IGMPspeedsuptheprocessofblockingunnecessarymulticasttraffictoa
switchportthatisconnectedtomultipleendnodes.Whenaporthavingmultipleendnodesreceivesaleave
grouprequestfromoneendnodeforagivenmulticastgroup,forcedfastleaveactivatesandwaitsfora
secondtoreceiveajoinrequestfromanyothermemberofthesamegrouponthatport.Iftheportdoes
notreceiveajoinrequestforthatgroupwithintheforcedfastleaveinterval,theswitchthenblocksany
furthertraffictothatgrouponthatport.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringforced-fastleaveportsforVLANsontheinterface:
| switch#            | configure |     | terminal   |               |       |     |
| ------------------ | --------- | --- | ---------- | ------------- | ----- | --- |
| switch(config)#    |           | int | 1/1/1      |               |       |     |
| switch(config-if)# |           |     | no shut    |               |       |     |
| switch(config-if)# |           |     | no routing |               |       |     |
| switch(config-if)# |           |     | vlan       | trunk allowed | 10-20 |     |
switch(config-if)#
|                    |          |     | ip igmp | snooping | forced-fastleave | vlan 10    |
| ------------------ | -------- | --- | ------- | -------- | ---------------- | ---------- |
| switch(config-if)# |          |     | ip igmp | snooping | forced-fastleave | vlan 10-20 |
| ip igmp            | snooping |     | forward |          | vlan             |            |
Syntax
| ip igmp    | snooping | forward | [vlan | <VLAN-LIST>]       |     |     |
| ---------- | -------- | ------- | ----- | ------------------ | --- | --- |
| no ip igmp | snooping | forward |       | [vlan <VLAN-LIST>] |     |     |
Description
ConfiguresthespecifiedportsinforwardmodeinthegivenVLANlist.Inforwardmode,trafficisalways
forwardedonthisport,irrespectiveofjoins.
Thenoformofthiscommanddisablesforwardports.
Commandcontext
IGMPsnooping|58

config-if
Parameters
<VLAN-LIST>
Required:SpecifiesalistofVLANsonwhichtheportshouldbeconfiguredasaforwardport.Specifies
thenumberofasingleVLANoraseriesofnumbersforarangeofVLANs,separatedbycommas(10,20,
30,40),dashes(10-40),orboth(10-40,60).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ConfiguringforwardportsfortheVLANontheinterface:
| switch#            | configure | terminal   |               |              |     |
| ------------------ | --------- | ---------- | ------------- | ------------ | --- |
| switch(config)#    |           | int 1/1/1  |               |              |     |
| switch(config-if)# |           | no shut    |               |              |     |
| switch(config-if)# |           | no routing |               |              |     |
| switch(config-if)# |           | vlan       | trunk allowed | 10-20        |     |
| switch(config-if)# |           | ip igmp    | snooping      | forward vlan | 10  |
switch(config-if)#
|         |          | ip igmp      | snooping | forward vlan | 10-20 |
| ------- | -------- | ------------ | -------- | ------------ | ----- |
| ip igmp | snooping | static-group |          |              |       |
Syntax
| ip igmp    | snooping static-group |              | <MULTICAST-IP-ADDRESS> |     |     |
| ---------- | --------------------- | ------------ | ---------------------- | --- | --- |
| no ip igmp | snooping              | static-group | <MULTICAST-IP-ADDRESS> |     |     |
Description
ConfiguresanIGMPsnoopingstaticmulticastgroup.Youcanconfigureamaximumof32IGMPsnooping
staticgroups.
Thenoformofthiscommanddisablesstaticmulticastgroup.
Commandcontext
config-vlan
Parameters
<MULTICAST-IP-ADDRESS>
SpecifiestheIGMPstaticmulticastgroupIPaddress.Format:A.B.C.D
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringIGMPsnoopingstaticgroup:
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 59

| switch(config)# | vlan | 2   |     |     |
| --------------- | ---- | --- | --- | --- |
switch(config-vlan)#
|                      |          | ip igmp    | snooping static-group | 239.1.1.1 |
| -------------------- | -------- | ---------- | --------------------- | --------- |
| switch(config-vlan)# |          | no ip igmp | snooping static-group | 239.1.1.1 |
| ip igmp              | snooping | version    |                       |           |
Syntax
| ip igmp | snooping version | <VERSION> |     |     |
| ------- | ---------------- | --------- | --- | --- |
Description
ConfigurestheIGMPsnoopingversionontheVLAN.
Commandcontext
config-vlan
Parameters
<VERSION>
SpecifiestheIGMPsnoopingversion.Select2forIGMPv2(RFC2236).Select3forIGMPv3(RFC3376).
Values:2or3.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringIGMPsnoopingversionontheVLAN:
| switch(config)#      | vlan          | 2       |                    |     |
| -------------------- | ------------- | ------- | ------------------ | --- |
| switch(config-vlan)# |               | ip igmp | snooping version 2 |     |
| no ip                | igmp snooping |         |                    |     |
Syntax
| no ip igmp | snooping |     |     |     |
| ---------- | -------- | --- | --- | --- |
Description
DisablesallIGMPsnoopingconfigurationsontheVLAN.
Commandcontext
config-vlan
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DisablingallIGMPsnoopingconfigurationsontheVLAN:
IGMPsnooping|60

| switch(config)# |     | vlan | 2   |     |     |
| --------------- | --- | ---- | --- | --- | --- |
switch(config-vlan)#
|      |         |          | no  | ip igmp snooping |     |
| ---- | ------- | -------- | --- | ---------------- | --- |
| show | ip igmp | snooping |     |                  |     |
Syntax
| show ip | igmp snooping |     | [vsx-peer] |     |     |
| ------- | ------------- | --- | ---------- | --- | --- |
Description
ShowsIGMPsnoopingconfigurationinformationandstatusforallVLANs.
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
Examples
ShowingIGMPsnoopingconfigurationandstatus:
| switch# | show         | ip igmp        | snooping |            |          |
| ------- | ------------ | -------------- | -------- | ---------- | -------- |
| IGMP    | Snooping     | Protocol       | Info     |            |          |
| Total   | VLANs        | with IGMP      | enabled  |            | : 1      |
| IGMP    | Drop Unknown | Multicast      |          |            | : Global |
| VLAN    | ID : 1       |                |          |            |          |
| VLAN    | Name :       | DEFAULT_VLAN_1 |          |            |          |
| IGMP    | Snooping     | is not         | enabled  |            |          |
| VLAN    | ID : 2       |                |          |            |          |
| VLAN    | Name :       | VLAN2          |          |            |          |
| IGMP    | Configured   | Version        |          | : 3        |          |
| IGMP    | Operating    | Version        | :        | 3          |          |
| Querier | Address      | [this          | switch]  | : 20.1.1.1 |          |
| Querier | Port         | :              |          |            |          |
| Querier | UpTime       | :0m            | 21s      |            |          |
| Querier | Expiration   |                | Time     | :0m 2s     |          |
| show    | ip igmp      | snooping       |          | counters   |          |
Syntax
| show ip | igmp snooping |     | counters | [vsx-peer] |     |
| ------- | ------------- | --- | -------- | ---------- | --- |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 61

Description
ShowsIGMPsnoopingquerypacketTx,Rx,andErrorpacketcounterdetails.
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
Examples
ShowingIGMPsnoopingpacketcounters:
| switch#     | show     | ip      | igmp     | snooping | counters |     |
| ----------- | -------- | ------- | -------- | -------- | -------- | --- |
| IGMP        | Snooping | VLAN    | Counters |          |          |     |
| Rx Counters |          | :       |          |          |          |     |
| V1 All      | Hosts    | Queries |          |          |          | 0   |
| V2 All      | Hosts    | Queries |          |          |          | 0   |
| V3 All      | Hosts    | Queries |          |          |          | 3   |
| V2 Group    | Specific |         | Queries  |          |          | 0   |
| V3 Group    | Specific |         | Queries  |          |          | 0   |
| Group       | And      | Source  | Specific | Queries  |          | 0   |
| V1 Member   |          | Reports |          |          |          | 0   |
| V2 Member   |          | Reports |          |          |          | 0   |
| V3 Member   |          | Reports |          |          |          | 2   |
| V2 Member   |          | Leaves  |          |          |          | 0   |
| Tx Counters |          | :       |          |          |          |     |
| Flood       | on vlan  |         |          |          |          | 44  |
| V2 Group    | Specific |         | Queries  |          |          | 0   |
| V3 Group    | Specific |         | Queries  |          |          | 0   |
Errors:
| Unknown    | Message   |         | Type             |         |           | 0   |
| ---------- | --------- | ------- | ---------------- | ------- | --------- | --- |
| Malformed  |           | Packets |                  |         |           | 0   |
| Bad        | Checksum  |         |                  |         |           | 0   |
| Packet     | received  |         | on IGMP-disabled |         | Interface | 0   |
| Interface  |           | Wrong   | Version          | Queries |           | 0   |
| Packets    | dropped   |         | by ACL           |         |           | 0   |
| Port       | Counters: |         |                  |         |           |     |
| Membership |           | Timeout |                  |         |           | 0   |
| show       | ip igmp   |         | snooping         |         | groups    |     |
IGMPsnooping|62

Syntax

show ip igmp snooping groups [vsx-peer]

Description

Shows IGMP snooping group information.

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

Showing IGMP snooping groups:

switch# show ip igmp snooping groups
IGMP Group Address Information

VLAN ID Group Address
-----------------------------------------------------------------
2

Last Reporter

239.1.1.3

10.1.1.1

Expires

0m 10s

UpTime

0m 4s

Type

Filter

show ip igmp snooping static-groups

Syntax

show ip igmp snooping static-groups [vsx-peer]

Description

Shows IGMP snooping static group details.

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

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

63

Examples
ShowingIGMPsnoopingstaticgroupdetails:
switch#
|      | show     | ip igmp       | snooping | static-groups |     |
| ---- | -------- | ------------- | -------- | ------------- | --- |
| IGMP | Static   | Group Address |          | Information   |     |
| VLAN | ID Group | Address       |          |               |     |
------------------------
| 10   | 239.1.1.10 |          |     |            |     |
| ---- | ---------- | -------- | --- | ---------- | --- |
| 10   | 239.1.1.11 |          |     |            |     |
| show | ip igmp    | snooping |     | statistics |     |
Syntax
| show ip | igmp | snooping | statistics | [vsx-peer] |     |
| ------- | ---- | -------- | ---------- | ---------- | --- |
Description
ShowsIGMPsnoopingprotocolinformationandthejoinedgroupstatistics.
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
Examples
ShowingIGMPsnoopingstatistics:
| switch# | show             | ip igmp           | snooping | statistics     |                 |
| ------- | ---------------- | ----------------- | -------- | -------------- | --------------- |
| IGMP    | Snooping         | Protocol          | Info     |                |                 |
| Total   | VLANs            | with IGMP         | enabled  |                | : 1             |
| IGMP    | Drop             | Unknown Multicast |          |                | : Global        |
| IGMP    | Snooping         | Joined            | Groups   | Statistics     |                 |
| VLAN    | ID VLAN          | Name              |          | Total Static   | INCLUDE EXCLUDE |
| ------- | ---------------- |                   |          | ------ ------  | ------- ------- |
| 1       | DEFAULT_VLAN_1   |                   |          | 0 0            | 0 0             |
| 2       | VLAN10           |                   |          | 2 2            | 0 0             |
| show    | ip igmp          | snooping          |          | vlan <VLAN-ID> |                 |
IGMPsnooping|64

Syntax
| show ip igmp | snooping      |     | vlan <VLAN-ID> | [group | [<group-ip>] |     |
| ------------ | ------------- | --- | -------------- | ------ | ------------ | --- |
| [source      | <source-ip>]] |     | [vsx-peer]     |        |              |     |
Description
ShowsIGMPsnoopingprotocolinformationforthespecifiedVLAN.Youcanalsospecifyagroupandsource
toshowgroupandsourceinformation.
Commandcontext
Operator(>)orManager(#)
Parameters
<VLAN-ID>
SpecifiesaVLAN.Range:1-4094.
group <group-ip>
Specifiesagrouptodisplayportandgroupinformation.Format:A.B.C.D
source <source-ip>
Specifiesasourcetodisplaysourceinformationforthegroup.Format:A.B.C.D
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPsnoopingprotocolinformationforVLAN2:
| switch#               | show       | ip igmp    | snooping   | vlan 2    |           |            |
| --------------------- | ---------- | ---------- | ---------- | --------- | --------- | ---------- |
| IGMP Snooping         |            | Protocol   | Info       |           |           |            |
| Total                 | VLANs      | with IGMP  | enabled    |           | : 1       |            |
| IGMP Drop             | Unknown    | Multicast  |            |           | : Global  |            |
| VLAN ID               | : 2        |            |            |           |           |            |
| VLAN Name             | :          | VLAN2      |            |           |           |            |
| IGMP Configured       |            | Version    | : 3        |           |           |            |
| IGMP Operating        |            | Version    | : 3        |           |           |            |
| Querier               | Address    | : 20.1.1.1 |            |           |           |            |
| Querier               | Port       | : 1/1/1    |            |           |           |            |
| Querier               | UpTime     | :          |            |           |           |            |
| Querier               | Expiration |            | Time :     |           |           |            |
| Active                | Group      | Address    | Tracking   | Vers Mode | Uptime    | Expires    |
| --------------------- |            |            | ---------- | ---- ---- | --------- | ---------- |
| 239.1.1.2             |            |            | Filter     | 3 INC     | 0m 27s    | 0m 13s     |
ShowingIGMPsnoopinggroupinformationforgroup239.1.1.2onVLAN2:
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 65

| switch# | show     | ip igmp     | snooping    |     | vlan    | 2   | group | 239.1.1.2 |       |           |         |
| ------- | -------- | ----------- | ----------- | --- | ------- | --- | ----- | --------- | ----- | --------- | ------- |
| IGMP    | ports    | and group   | information |     |         | for | group | 239.1.1.2 |       |           |         |
| VLAN    | ID       | : 2         |             |     |         |     |       |           |       |           |         |
| VLAN    | Name     | : VLAN2     |             |     |         |     |       |           |       |           |         |
| Group   | Address  | : 239.1.1.2 |             |     |         |     |       |           |       |           |         |
| Last    | Reporter | : 10.1.1.1  |             |     |         |     |       |           |       |           |         |
| Group   | Type     | : Filter    |             |     |         |     |       |           |       |           |         |
|         |          |             |             |     |         |     | V1    |           | V2    | Sources   | Sources |
| Port    |          | Vers Mode   | Uptime      |     | Expires |     | Timer |           | Timer | Forwarded | Blocked |
--------- ---- ---- --------- --------- --------- --------- --------- --------
| 1/1/6     |         | 3 INC          | 0m        | 41s       | 3m  | 39s              |     |      |     | 3   | 0   |
| --------- | ------- | -------------- | --------- | --------- | --- | ---------------- | --- | ---- | --- | --- | --- |
| Group     | Address | :              | 239.1.1.2 |           |     |                  |     |      |     |     |     |
| Source    | Address | :              | 30.1.1.1  |           |     |                  |     |      |     |     |     |
| Source    | Type    | :              | Filter    |           |     |                  |     |      |     |     |     |
| Port      |         | Mode Uptime    |           | Expires   |     | Configured       |     | Mode |     |     |     |
| --------- |         | ---- --------- |           | --------- |     | ---------------- |     |      |     |     |     |
| 1/1/6     |         | INC 0m         | 41s       | 3m        | 39s | Auto             |     |      |     |     |     |
| Group     | Address | :              | 239.1.1.2 |           |     |                  |     |      |     |     |     |
| Source    | Address | :              | 30.1.1.2  |           |     |                  |     |      |     |     |     |
| Source    | Type    | :              | Filter    |           |     |                  |     |      |     |     |     |
| Port      |         | Mode Uptime    |           | Expires   |     | Configured       |     | Mode |     |     |     |
| --------- |         | ---- --------- |           | --------- |     | ---------------- |     |      |     |     |     |
| 1/1/6     |         | INC 0m         | 41s       | 3m        | 39s | Auto             |     |      |     |     |     |
| Group     | Address | :              | 239.1.1.2 |           |     |                  |     |      |     |     |     |
| Source    | Address | :              | 30.1.1.3  |           |     |                  |     |      |     |     |     |
| Source    | Type    | :              | Filter    |           |     |                  |     |      |     |     |     |
| Port      |         | Mode Uptime    |           | Expires   |     | Configured       |     | Mode |     |     |     |
| --------- |         | ---- --------- |           | --------- |     | ---------------- |     |      |     |     |     |
| 1/1/6     |         | INC 0m         | 41s       | 3m        | 39s | Auto             |     |      |     |     |     |
ShowingIGMPsnoopinggroupinformationforgroup239.1.1.2onVLAN2andsource30.1.1.1:
switch#
|           | show    | ip igmp        | snooping  |           | vlan | 2                | group | 239.1.1.2 | source   | 30.1.1.1 |     |
| --------- | ------- | -------------- | --------- | --------- | ---- | ---------------- | ----- | --------- | -------- | -------- | --- |
| VLAN      | ID      | : 2            |           |           |      |                  |       |           |          |          |     |
| VLAN      | Name    | : VLAN2        |           |           |      |                  |       |           |          |          |     |
| Group     | Address | :              | 239.1.1.2 |           |      |                  |       |           |          |          |     |
| Source    | Address | :              | 30.1.1.1  |           |      |                  |       |           |          |          |     |
| Source    | Type    | :              | Filter    |           |      |                  |       |           |          |          |     |
| Port      |         | Mode Uptime    |           | Expires   |      | Configured       |       | Mode      |          |          |     |
| --------- |         | ---- --------- |           | --------- |      | ---------------- |       |           |          |          |     |
| 1/1/6     |         | INC 0m         | 41s       | 3m        | 39s  | Auto             |       |           |          |          |     |
| show      | ip igmp | snooping       |           |           | vlan | <VLAN-ID>        |       |           | counters |          |     |
Syntax
| show ip | igmp | snooping | vlan | <VLAN-ID> |     | counters |     | [vsx-peer] |     |     |     |
| ------- | ---- | -------- | ---- | --------- | --- | -------- | --- | ---------- | --- | --- | --- |
Description
IGMPsnooping|66

ShowsIGMPsnoopingquerypacketTx,Rx,ErrorpacketcountersforthespecifiedVLAN.
Commandcontext
Operator(>)orManager(#)
Parameters
<VLAN-ID>
SpecifiesaVLAN.Range:1-4094.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPsnoopingcountersforVLAN2:
| Switch#       | show ip       | igmp snooping |         | vlan 2 counters |     |
| ------------- | ------------- | ------------- | ------- | --------------- | --- |
| IGMP Snooping | VLAN          | Counters      |         |                 |     |
| VLAN ID       | : 2           |               |         |                 |     |
| VLAN Name     | : VLAN2       |               |         |                 |     |
| Rx Counters   | :             |               |         |                 |     |
| V1 All        | Hosts Queries |               |         |                 | 0   |
| V2 All        | Hosts Queries |               |         |                 | 0   |
| V3 All        | Hosts Queries |               |         |                 | 3   |
| V2 Group      | Specific      | Queries       |         |                 | 0   |
| V3 Group      | Specific      | Queries       |         |                 | 0   |
| Group And     | Source        | Specific      | Queries |                 | 0   |
| V1 Member     | Reports       |               |         |                 | 0   |
| V2 Member     | Reports       |               |         |                 | 0   |
| V3 Member     | Reports       |               |         |                 | 2   |
| V2 Member     | Leaves        |               |         |                 | 0   |
| Tx Counters   | :             |               |         |                 |     |
| Flood on      | vlan          |               |         |                 | 71  |
| V2 Group      | Specific      | Queries       |         |                 | 0   |
| V3 Group      | Specific      | Queries       |         |                 | 0   |
Errors:
| Unknown      | Message  | Type             |         |           | 0   |
| ------------ | -------- | ---------------- | ------- | --------- | --- |
| Malformed    | Packets  |                  |         |           | 0   |
| Bad Checksum |          |                  |         |           | 0   |
| Packet       | received | on IGMP-disabled |         | Interface | 0   |
| Interface    | Wrong    | Version          | Queries |           | 0   |
| Packet       | dropped  | by ACL           |         |           | 0   |
Port Counters:
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 67

| Membership | Timeout |     |     |     | 0   |     |     |
| ---------- | ------- | --- | --- | --- | --- | --- | --- |
Switch#
| show | ip igmp snooping |     | vlan <VLAN-ID> |     | group | port |     |
| ---- | ---------------- | --- | -------------- | --- | ----- | ---- | --- |
Syntax
show ip igmp snooping vlan <VLAN-ID> group port <PORT-ID> [vsx-peer]
Description
ShowsIGMPsnoopinggroupdetailsforthespecifiedVLAN.ItshowsinformationaboutallIGMPsnooping
groupsorsourceslearnedonaparticularport.
Commandcontext
Operator(>)orManager(#)
Parameters
<VLAN-ID>
SpecifiesaVLAN.Range:1-4094.
<PORT-ID>
SpecifiesaportofaVLANtodisplayinformationaboutallIGMPv3snoopinggroups/sourceslearnona
particularport.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPsnoopinggroupdetailsforVLAN2port1/1/6:
| switch# | show ip igmp        | snooping | vlan 2  | group port | 1/1/6 |           |         |
| ------- | ------------------- | -------- | ------- | ---------- | ----- | --------- | ------- |
| VLAN    | ID : 2              |          |         |            |       |           |         |
| VLAN    | Name : VLAN2        |          |         |            |       |           |         |
| Group   | Address : 239.1.1.1 |          |         |            |       |           |         |
| Last    | Reporter : 10.1.1.1 |          |         |            |       |           |         |
| Group   | Type : Filter       |          |         |            |       |           |         |
|         |                     |          |         | V1         | V2    | Sources   | Sources |
| Port    | Vers Mode           | Uptime   | Expires | Timer      | Timer | Forwarded | Blocked |
--------- ---- ---- --------- --------- --------- --------- --------- --------
| 1/1/6 | 2 EXC               | 0m 21s | 1m 12s |     | 2m 48s | 0   | 0   |
| ----- | ------------------- | ------ | ------ | --- | ------ | --- | --- |
| VLAN  | ID : 2              |        |        |     |        |     |     |
| VLAN  | Name : VLAN2        |        |        |     |        |     |     |
| Group | Address : 239.1.1.2 |        |        |     |        |     |     |
IGMPsnooping|68

| Last  | Reporter | : 10.1.1.1 |        |         |       |       |           |         |
| ----- | -------- | ---------- | ------ | ------- | ----- | ----- | --------- | ------- |
| Group | Type     | : Filter   |        |         |       |       |           |         |
|       |          |            |        |         | V1    | V2    | Sources   | Sources |
| Port  | Vers     | Mode       | Uptime | Expires | Timer | Timer | Forwarded | Blocked |
--------- ---- ---- --------- --------- --------- --------- --------- --------
| 1/1/6 | 2       | EXC      | 0m 21s | 1m 32s         |     | 2m 48s     | 0   | 0   |
| ----- | ------- | -------- | ------ | -------------- | --- | ---------- | --- | --- |
| show  | ip igmp | snooping |        | vlan <VLAN-ID> |     | statistics |     |     |
Syntax
| show ip | igmp snooping | vlan | <VLAN-ID> | statistics | [vsx-peer] |     |     |     |
| ------- | ------------- | ---- | --------- | ---------- | ---------- | --- | --- | --- |
Description
ShowsIGMPsnoopingstatisticsdetailsforthespecifiedVLAN.Italsoshowsinformationonthedifferent
groupsjoinedintheVLAN.
Commandcontext
Operator(>)orManager(#)
Parameters
<VLAN-ID>
SpecifiesaVLAN.Range:1-4094.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingIGMPsnoopingstatisticsforVLAN2:
| switch# | show         | ip igmp    | snooping | vlan 2 | statistics |     |     |     |
| ------- | ------------ | ---------- | -------- | ------ | ---------- | --- | --- | --- |
| IGMP    | Snooping     | statistics |          |        |            |     |     |     |
| VLAN    | ID :         | 2          |          |        |            |     |     |     |
| VLAN    | Name : VLAN2 |            |          |        |            |     |     |     |
| Number  | of Include   | Groups     |          | : 1    |            |     |     |     |
| Number  | of Exclude   | Groups     |          | : 0    |            |     |     |     |
| Number  | of Static    | Groups     |          | : 1    |            |     |     |     |
| Total   | Multicast    | Groups     | Joined   | : 2    |            |     |     |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 69

Chapter 5

MLD snooping

MLD snooping

MLD snooping functionality
Multicast Listener Discovery (MLD) snooping optimizes multicast traffic across the network to prevent traffic
from flooding ports on a VLAN.

n For example, one of the features of MLD snooping lets you configure the network so that traffic is

forwarded only to ports that initiate an MLD request for multicast.

n Another feature of MLD lets you enable a setting so that packets that do not match the configured

version are dropped.

n You can also block ports from traffic.

MLD snooping global configuration commands

ipv6 mld snooping

Syntax

ipv6 mld snooping [drop-unknown [vlan-shared | vlan-exclusive]]
[no] ipv6 mld snooping

Description

This command configures the drop unknown mode. While MLD snooping is enabled, the traffic will be
forwarded only to ports that initiate an MLD request for multicast. Drop unknown mode can be a filter
across all VLANs (vlan-shared) or per VLAN (exclusive-vlan). The default configuration is vlan-shared.

The no form of this command disables drop unknown mode on the switch.

Command context

config

Parameters

vlan-shared

Required: Enable shared VLAN filter on the switch.

vlan-exclusive

Required: Enable exclusive drop unknown filter per VLAN.

Authority

Administrators or local user group members with execution rights for this command.

Example

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

70

| switch(config)# |     |     | ipv6 | mld snooping | drop-unknown |     | vlan-shared |
| --------------- | --- | --- | ---- | ------------ | ------------ | --- | ----------- |
switch(config)#
|                 |          |     | ipv6    | mld snooping  | drop-unknown |              | vlan-exclusive |
| --------------- | -------- | --- | ------- | ------------- | ------------ | ------------ | -------------- |
| switch(config)# |          |     | no ipv6 | mld snooping  |              | drop-unknown |                |
| MLD snooping    |          |     | VLAN    | configuration |              |              | commands       |
| ipv6 mld        | snooping |     |         |               |              |              |                |
Syntax
| ipv6 mld | snooping | {enable |     | | disable} |     |     |     |
| -------- | -------- | ------- | --- | ---------- | --- | --- | --- |
Description
ThiscommandenablesordisablesMLDsnoopingontheVLAN.
ThenoformofthiscommanddisablesallMLDsnoopingconfigurationsontheVLAN.
Commandcontext
config-vlan-<VLAN-ID>
Parameters
enable
Required:EnableMLDsnoopingontheVLAN.
disable
Required:DisableMLDsnoopingontheVLAN.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
EnableMLDsnoopingonVLAN2:
| switch(config)#      |     |     | vlan | 2        |          |         |     |
| -------------------- | --- | --- | ---- | -------- | -------- | ------- | --- |
| switch(config-vlan)# |     |     |      | ipv6 mld | snooping | enable  |     |
| switch(config-vlan)# |     |     |      | ipv6 mld | snooping | disable |     |
RemoveallMLDsnoopingconfigurationsonVLAN2:
| switch(config)#      |          |     | vlan | 2       |              |     |     |
| -------------------- | -------- | --- | ---- | ------- | ------------ | --- | --- |
| switch(config-vlan)# |          |     |      | no ipv6 | mld snooping |     |     |
| ipv6 mld             | snooping |     |      | apply   | access-list  |     |     |
Syntax
| ipv6 mld    | snooping | apply | access-list |             | <ACL-NAME> |            |     |
| ----------- | -------- | ----- | ----------- | ----------- | ---------- | ---------- | --- |
| no ipv6 mld | snooping |       | apply       | access-list |            | <ACL-NAME> |     |
Description
ConfigurestheACLonaparticularinterfacetofiltertheMLDjoinorleavepacketsbasedonrulessetinthe
particularACLname.
MLDsnooping|71

ThenoformofthiscommanddisablestherulessetfortheACL.
ThisconfigurationwilloverridetheACLassociatedwithIGMPsnoopingonthecorrespondingL2VLAN.
Commandcontext
config-vlan
Parameters
access-list
AssociatesanACLwiththeIGMP.
<ACL-NAME>
SpecifiesthenameoftheACL.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
ExistingclassifiercommandsareusedtoconfiguretheACL.IncaseanMLDv2packetwithmultiplegroup
addressesisreceived,itwillonlyprocessthepermittedgroupaddressesbasedontheACLruleset,andany
existingjoinswilltimeout.Ifthereisnomatchorifthereisadenyrulematch,thepacketisdropped.
IftheaccesslistisconfiguredforbothL2VLANandL3VLAN,theL3VLANconfigurationwillbeapplied.
Examples
ConfiguringtheACLtofilterMLDpacketsbasedonrulessetinaccesslistmygroup:
| switch(config)# |     | access-list |     | ipv6 mygroup |     |     |
| --------------- | --- | ----------- | --- | ------------ | --- | --- |
switch(config-acl-ip)#
|                        |     |           | permit | icmpv6       | any ff55::1       |         |
| ---------------------- | --- | --------- | ------ | ------------ | ----------------- | ------- |
| switch(config-acl-ip)# |     |           | exit   |              |                   |         |
| switch(config)#        |     | interface |        | vlan 2       |                   |         |
| switch(config-vlan)#   |     |           | ipv6   | mld snooping | apply access-list | mygroup |
ConfiguringtheACLtoremovetherulessetinaccesslistmygroup:
switch(config-vlan)# no ipv6 mld snooping apply access-list mygroup
| ipv6 mld | snooping |     | auto | vlan |     |     |
| -------- | -------- | --- | ---- | ---- | --- | --- |
Syntax
| ipv6 mld    | snooping | [auto | vlan       | <VLAN-LIST>] |     |     |
| ----------- | -------- | ----- | ---------- | ------------ | --- | --- |
| no ipv6 mld | snooping |       | [auto vlan | <VLAN-LIST>] |     |     |
Description
Thiscommandconfiguresthegivenportsinautomode,whichisthedefaultportmode.
Thenoformofthiscommanddisablesautoports.
Commandcontext
config-vlan-<VLAN-ID>
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 72

Parameters
<VLAN-LIST>
Required:SpecifiesalistofVLANsonwhichtheportshouldbeconfiguredasanautoport.Specifiesthe
numberofasingleVLANoraseriesofnumbersforarangeofVLANs,separatedbycommas(10,20,30,
40),dashes(10-40),orboth(10-40,60).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ConfiguringautoportsforVLANsontheinterface:
| switch#              | configure | terminal   |              |           |       |
| -------------------- | --------- | ---------- | ------------ | --------- | ----- |
| switch(config)#      | int       | 1/1/1      |              |           |       |
| switch(config-vlan)# |           | no shut    |              |           |       |
| switch(config-vlan)# |           | no routing |              |           |       |
| switch(config-vlan)# |           | ipv6       | mld snooping | auto vlan | 10    |
| switch(config-vlan)# |           | ipv6       | mld snooping | auto vlan | 10-20 |
| ipv6 mld             | snooping  | blocked    | vlan         |           |       |
Syntax
| ipv6 mld    | snooping [blocked | vlan     | <VLAN-LIST>]      |     |     |
| ----------- | ----------------- | -------- | ----------------- | --- | --- |
| no ipv6 mld | snooping          | [blocked | vlan <VLAN-LIST>] |     |     |
Description
Bydefaultportsareconfiguredinautomode.Thiscommandconfiguresthegivenportsinblockedmode.
Thenoformofthiscommandremovesblockedports.
Commandcontext
config-vlan-<VLAN-ID>
Parameters
<VLAN-LIST>
Required:SpecifiesalistofVLANsonwhichtheportshouldbeconfiguredasablockedport.Specifies
thenumberofasingleVLANoraseriesofnumbersforarangeofVLANs,separatedbycommas(10,20,
30,40),dashes(10-40),orboth(10-40,60).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ConfiguringblockedportsfortheVLANsontheinterface:
| switch#         | configure | terminal |     |     |     |
| --------------- | --------- | -------- | --- | --- | --- |
| switch(config)# | int       | 1/1/1    |     |     |     |
switch(config-vlan)#
no shut
MLDsnooping|73

| switch(config-vlan)# |     |     | no routing |     |     |     |     |
| -------------------- | --- | --- | ---------- | --- | --- | --- | --- |
switch(config-vlan)#
|                      |          |     | ipv6      | mld snooping | blocked | vlan | 10    |
| -------------------- | -------- | --- | --------- | ------------ | ------- | ---- | ----- |
| switch(config-vlan)# |          |     | ipv6      | mld snooping | blocked | vlan | 10-20 |
| ipv6 mld             | snooping |     | fastlearn |              |         |      |       |
Syntax
| ipv6 mld | snooping | fastlearn | <port-list> |     |     |     |     |
| -------- | -------- | --------- | ----------- | --- | --- | --- | --- |
Description
Thiscommandenablestheporttolearngroupinformationonreceivingtopologychangenotification.
Thenoformofthiscommanddisablesfastlearnontheports.
Commandcontext
config
Parameters
port-list
Required:1/1/1-1/1/2,portstobeconfiguredasfastlearnports.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)# |          | ipv6 | mld       | snooping | fastlearn | 1/1/3       |     |
| --------------- | -------- | ---- | --------- | -------- | --------- | ----------- | --- |
| switch(config)# |          | ipv6 | mld       | snooping | fastlearn | 1/1/1-1/1/2 |     |
| switch(config)# |          | ipv6 | mld       | snooping | fastlearn | 1/1/5,1/1/6 |     |
| ipv6 mld        | snooping |      | fastleave |          | vlan      |             |     |
Syntax
| ipv6 mld    | snooping | [fastleave |            | vlan | <VLAN-LIST>] |     |     |
| ----------- | -------- | ---------- | ---------- | ---- | ------------ | --- | --- |
| no ipv6 mld | snooping |            | [fastleave | vlan | <VLAN-LIST>] |     |     |
Description
Configuresthespecifiedportsasfastleaveports.Enablestheswitchtoimmediatelyremoveaninterface
fromthebridgetableuponreceivingtheleavegroupmessage.
Thenoformofthiscommanddisablesfastleaveconfigurationontheports.
Commandcontext
config-vlan-<VLAN-ID>
Parameters
<VLAN-LIST>
SpecifiesalistofVLANsonwhichtheportshouldbeconfiguredasafastleaveport.Specifiesthenumber
ofasingleVLANoraseriesofnumbersforarangeofVLANs,separatedbycommas(10,20,30,40),
dashes(10-40),orboth(10-40,60).
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 74

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
MLDfastleaveisconfiguredforportsonaper-VLANbasis.Bydefault,thequeriersendsaMLDGroup-
SpecificQuerymessageoutoftheinterface,uponwhichtheleavegroupmessageisreceivedtoensurethat
nootherreceiversareconnectedtotheinterface.Ifreceiversaredirectlyattachedtotheswitch,itis
inefficienttosendthemembershipqueryasthereceiverwantingtoleaveistheonlyconnectedhost.
FastleaveprocessingeliminatestheMLDGroup-SpecificQuerymessage.Thus,itallowstheswitchto
immediatelyremoveaninterfacefromthebridgetableuponreceivingtheleaveGroupmessage.This
processingspeedsuptheoverallleaveprocessandalsoeliminatestheCPUoverheadofhavingtogenerate
anMLDGroup-SpecificQuerymessage.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ConfiguringfastleaveportsfortheVLAN:
| switch#              | configure | terminal   |                    |            |
| -------------------- | --------- | ---------- | ------------------ | ---------- |
| switch(config)#      | int       | 1/1/1      |                    |            |
| switch(config-vlan)# |           | no shut    |                    |            |
| switch(config-vlan)# |           | no routing |                    |            |
| switch(config-vlan)# |           | ipv6 mld   | snooping fastleave | vlan 10    |
| switch(config-vlan)# |           | ipv6 mld   | snooping fastleave | vlan 10-20 |
| ipv6 mld             | snooping  | forced     | fastleave          |            |
Syntax
| ipv6 mld    | snooping [forced-fastleave |                   | <VLAN-LIST>] |     |
| ----------- | -------------------------- | ----------------- | ------------ | --- |
| no ipv6 mld | snooping                   | [forced-fastleave | <VLAN-LIST>] |     |
Description
Configuresthegivenportsinforcedfastleavemode.
Thenoformofthiscommanddisablesforcedfastleaveconfigurationontheports.
Commandcontext
config-vlan-<VLAN-ID>
Parameters
<VLAN-LIST>
SpecifiesalistofVLANsonwhichtheportshouldbeconfiguredasaforcedfastleaveport.Specifiesthe
numberofasingleVLANoraseriesofnumbersforarangeofVLANs,separatedbycommas(10,20,30,
40),dashes(10-40),orboth(10-40,60).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Withforcedfastleaveenabled,MLDspeedsuptheprocessofblockingunnecessarymulticasttraffictoa
switchportthatisconnectedtomultipleendnodes.Whenaporthavingmultipleendnodesreceivesaleave
grouprequestfromoneendnodeforagivenmulticastgroup,forcedfastleaveactivatesandwaitsasmall
MLDsnooping|75

amountoftimetoreceiveajoinrequestfromanyothermemberofthesamegrouponthatport.Iftheport
doesnotreceiveajoinrequestforthatgroupwithintheforcedfastleaveinterval,theswitchthenblocksany
furthertraffictothatgrouponthatport.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringforced-fastleaveportsfortheVLAN:
| switch#              | configure |     | terminal   |              |                  |         |
| -------------------- | --------- | --- | ---------- | ------------ | ---------------- | ------- |
| switch(config)#      |           | int | 1/1/1      |              |                  |         |
| switch(config-vlan)# |           |     | no shut    |              |                  |         |
| switch(config-vlan)# |           |     | no routing |              |                  |         |
| switch(config-vlan)# |           |     | ipv6       | mld snooping | forced-fastleave | vlan 10 |
switch(config-vlan)# ipv6 mld snooping forced-fastleave vlan 10-20
| ipv6 mld | snooping |     | forward | vlan |     |     |
| -------- | -------- | --- | ------- | ---- | --- | --- |
Syntax
| ipv6 mld    | snooping | [forward | vlan     | <VLAN-LIST>]      |     |     |
| ----------- | -------- | -------- | -------- | ----------------- | --- | --- |
| no ipv6 mld | snooping |          | [forward | vlan <VLAN-LIST>] |     |     |
Description
Bydefaultportsareconfiguredinautomode.Thiscommandconfiguresthegivenportsinforwardmode.
Thenoformofthiscommanddisablesforwardports.
Commandcontext
config-vlan-<VLAN-ID>
Parameters
<VLAN-LIST>
Required:SpecifiesalistofVLANsonwhichportsshouldbeconfiguredasforwardports.Specifiesthe
numberofasingleVLANoraseriesofnumbersforarangeofVLANs,separatedbycommas(10,20,30,
40),dashes(10-40),orboth(10-40,60).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ConfiguringforwardportsforVLANsontheinterface:
| switch#              | configure |     | terminal      |              |              |       |
| -------------------- | --------- | --- | ------------- | ------------ | ------------ | ----- |
| switch(config)#      |           | int | 1/1/1         |              |              |       |
| switch(config-vlan)# |           |     | no shut       |              |              |       |
| switch(config-vlan)# |           |     | no routing    |              |              |       |
| switch(config-vlan)# |           |     | ipv6          | mld snooping | forward vlan | 10    |
| switch(config-vlan)# |           |     | ipv6          | mld snooping | forward vlan | 10-20 |
| ipv6 mld             | snooping  |     | [static-group |              | <X:X::X:X>]  |       |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 76

Syntax
| ipv6 mld | snooping [static-group |     | <X:X::X:X>] |     |     |
| -------- | ---------------------- | --- | ----------- | --- | --- |
Description
Thiscommandconfiguresstaticmulticastgroup.
Thenoformofthiscommanddisablesstaticmulticastgroup.
Commandcontext
config-vlan-<VLAN-ID>
Parameters
static-group
Required:<X:X::X:X>,MLDstaticmulticastgroup.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config)#      | vlan     | 2        |              |              |         |
| -------------------- | -------- | -------- | ------------ | ------------ | ------- |
| switch(config-vlan)# |          | ipv6     | mld snooping | static-group | ff12::c |
| switch(config-vlan)# |          | no ipv6  | mld snooping | static-group | ff12::c |
| ipv6 mld             | snooping | [version | <ver>]       |              |         |
Syntax
| ipv6 mld | snooping [version | <ver>] |     |     |     |
| -------- | ----------------- | ------ | --- | --- | --- |
Description
ThiscommandconfigurestheMLDsnoopingversionontheVLAN.MLDversion2isthedefault.
Commandcontext
config-vlan-<VLAN-ID>
Parameters
ver
Required:1-2,MLDsnoopingversion.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config)#      | vlan | 2    |              |           |     |
| -------------------- | ---- | ---- | ------------ | --------- | --- |
| switch(config-vlan)# |      | ipv6 | mld snooping | version 2 |     |
| MLD snooping         |      | show | commands     |           |     |
MLDsnooping|77

| show | ipv6 | mld | snooping |     |     |
| ---- | ---- | --- | -------- | --- | --- |
Syntax
| show ipv6 | mld | snooping |     |     |     |
| --------- | --- | -------- | --- | --- | --- |
Description
ThiscommandshowsMLDsnoopingconfigurationdetailsforallVLANs.
Commandcontext
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show       | ipv6     | mld snooping  |               |                            |
| ------- | ---------- | -------- | ------------- | ------------- | -------------------------- |
| MLD     | Snooping   | Protocol | Info          |               |                            |
| Total   | VLANs      | with     | MLD enabled   |               | : 1                        |
| Current | count      |          | of multicast  | groups joined | : 0                        |
| MLD     | Drop       | Unknown  | Multicast     |               | : Global                   |
| VLAN    | ID         |          |               |               | : 1                        |
| VLAN    | Name       |          |               |               | : DEFAULT_VLAN_1           |
| MLD     | Snooping   | is       | not enabled   |               |                            |
| VLAN    | ID         |          |               |               | : 2                        |
| VLAN    | Name       |          |               |               | : VLAN2                    |
| MLD     | Configured |          | Version       |               | : 2                        |
| MLD     | Operating  |          | Version       |               | : 2                        |
| Querier | Address    |          | [this switch] |               | : fe80::218:71ff:fec4:2f00 |
| Querier | Port       |          |               |               | :                          |
| Querier | UpTime     |          |               |               | :0m 21s                    |
| Querier | Expiration |          | Time          |               | :0m 2s                     |
| show    | ipv6       | mld      | snooping      | [counters]    |                            |
Syntax
| show ipv6 | mld | snooping | [counters] |     |     |
| --------- | --- | -------- | ---------- | --- | --- |
Description
ThiscommandshowsMLDsnoopingquerypacketTx,Rx,andErrorpacketcounterdetails.
Commandcontext
Manager(#)
Parameters
counters
Optional,showMLDsnoopingcounters.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 78

Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show           | ipv6    | mld      | snooping | counters |     |
| ------- | -------------- | ------- | -------- | -------- | -------- | --- |
| MLD     | Snooping       | VLAN    | Counters |          |          |     |
| Rx      | Counters       | :       |          |          |          |     |
| V1      | All Hosts      | Queries |          |          |          | 0   |
| V2      | All Hosts      | Queries |          |          |          | 0   |
| V2      | Group Specific |         | Queries  |          |          | 0   |
| Group   | And            | Source  | Specific | Queries  |          | 0   |
| V1      | Member         | Reports |          |          |          | 0   |
| V2      | Member         | Reports |          |          |          | 0   |
| V1      | Member         | Leaves  |          |          |          | 0   |
| Tx      | Counters       | :       |          |          |          |     |
| Flood   | on vlan        |         |          |          |          | 44  |
| V1      | Group Specific |         | Queries  |          |          | 0   |
| V2      | Group Specific |         | Queries  |          |          | 0   |
Errors:
| Unknown    | Message   |         | Type            |         |           | 0   |
| ---------- | --------- | ------- | --------------- | ------- | --------- | --- |
| Malformed  |           | Packets |                 |         |           | 0   |
| Bad        | Checksum  |         |                 |         |           | 0   |
| Packet     | received  |         | on MLD-disabled |         | Interface | 0   |
| Interface  |           | Wrong   | Version         | Queries |           | 0   |
| Packets    | dropped   |         | by ACL          |         |           | 0   |
| Port       | Counters: |         |                 |         |           |     |
| Membership |           | Timeout |                 |         |           | 0   |
| show       | ipv6      | mld     | snooping        |         | [groups]  |     |
Syntax
| show ipv6 | mld | snooping | [groups] |     |     |     |
| --------- | --- | -------- | -------- | --- | --- | --- |
Description
ThiscommandshowsMLDsnoopinggroupdetailsforthespecifiedVLAN.
Commandcontext
Manager(#)
Parameters
groups
Optional,showMLDsnoopinggroupsinformation.
Authority
MLDsnooping|79

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show     | ipv6    | mld         | snooping | groups |        |     |               |      |
| ------- | -------- | ------- | ----------- | -------- | ------ | ------ | --- | ------------- | ---- |
| MLD     | Group    | Address | Information |          |        |        |     |               |      |
| VLAN    | ID Group |         | Address     | Expires  |        | UpTime |     | Last Reporter | Type |
------- ----------------- --------- --------- ------------------------------ ----
| 10   | ff12::c |     |          | 3m  | 54s          | 0m  | 26s | 2001::1 | Filter |
| ---- | ------- | --- | -------- | --- | ------------ | --- | --- | ------- | ------ |
| 10   | ff12::d |     |          | 4m  | 17s          | 0m  | 3s  | 2001::1 |        |
| show | ipv6    | mld | snooping |     | [statistics] |     |     |         |        |
Syntax
| show ipv6 | mld | snooping | [statistics] |     |     |     |     |     |     |
| --------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
Description
ThiscommandshowsMLDsnoopingstatisticsinformation.
Commandcontext
Manager(#)
Parameters
statistics
Optional,showMLDsnoopingstatistics.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show             | ipv6     | mld          | snooping | statistics |        |           |             |     |
| ------- | ---------------- | -------- | ------------ | -------- | ---------- | ------ | --------- | ----------- | --- |
| MLD     | Snooping         | Protocol |              | Info     |            |        |           |             |     |
| Total   | VLANs            | with     | MLD enabled  |          |            |        | :         | 1           |     |
| Current | count            |          | of multicast |          | groups     | joined | :         | 2           |     |
| MLD     | Drop             | Unknown  | Multicast    |          |            |        | :         | Global      |     |
| MLD     | Snooping         | Joined   | Groups       |          | Statistics |        |           |             |     |
| VLAN    | ID VLAN          | Name     |              | Total    | Static     |        | INCLUDE   | EXCLUDE     |     |
| ------- | ---------------- |          |              | ------   | ------     |        | -------   | -------     |     |
| 1       | DEFAULT_VLAN_1   |          |              | 0        | 0          |        | 0         | 0           |     |
| 2       | VLAN2            |          |              | 2        | 2          |        | 0         | 0           |     |
| show    | ipv6             | mld      | snooping     |          | [vlan      |        | <vlan-id> | [counters]] |     |
Syntax
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 80

| show ipv6 | mld | snooping | [vlan | <vlan-id> | [counters]] |     |
| --------- | --- | -------- | ----- | --------- | ----------- | --- |
Description
ThiscommandshowsMLDsnoopingprotocolinformationandnumberofdifferentgroupsjoinedforthe
VLAN.
Commandcontext
Manager(#)
Parameters
vlan-id
Required,1-4094,showsMLDsnoopinginformation.
counters
Optional,showsMLDquerypacketTx,Rx,ErrorpacketcountersonaspecifiedVLAN.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show           | ipv6    | mld      | snooping | vlan 2 counters |     |
| ------- | -------------- | ------- | -------- | -------- | --------------- | --- |
| MLD     | Snooping       | VLAN    | Counters |          |                 |     |
| VLAN    | ID             | : 2     |          |          |                 |     |
| VLAN    | Name           | : VLAN2 |          |          |                 |     |
| Rx      | Counters       | :       |          |          |                 |     |
| V1      | All Hosts      | Queries |          |          |                 | 0   |
| V2      | All Hosts      | Queries |          |          |                 | 0   |
| V1      | Group Specific |         | Queries  |          |                 | 0   |
| V2      | Group Specific |         | Queries  |          |                 | 0   |
| Group   | And            | Source  | Specific | Queries  |                 | 0   |
| V1      | Member         | Reports |          |          |                 | 0   |
| V2      | Member         | Reports |          |          |                 | 0   |
| V1      | Member         | Leaves  |          |          |                 | 0   |
| Tx      | Counters       | :       |          |          |                 |     |
| Flood   | on vlan        |         |          |          |                 | 71  |
| V1      | Group Specific |         | Queries  |          |                 | 0   |
| V2      | Group Specific |         | Queries  |          |                 | 0   |
Errors:
| Unknown    | Message   |         | Type            |         |           | 0   |
| ---------- | --------- | ------- | --------------- | ------- | --------- | --- |
| Malformed  |           | Packets |                 |         |           | 0   |
| Bad        | Checksum  |         |                 |         |           | 0   |
| Packet     | received  |         | on MLD-disabled |         | Interface | 0   |
| Interface  |           | Wrong   | Version         | Queries |           | 0   |
| Packets    | dropped   |         | by ACL          |         |           | 0   |
| Port       | Counters: |         |                 |         |           |     |
| Membership |           | Timeout |                 |         |           | 0   |
switch#
MLDsnooping|81

| show | ipv6 | mld snooping | [vlan <vlan-id> | [statistics]] |
| ---- | ---- | ------------ | --------------- | ------------- |
Syntax
| show ipv6 | mld | snooping [vlan <vlan-id> | [statistics]] |     |
| --------- | --- | ------------------------ | ------------- | --- |
Description
ThiscommandshowsMLDsnoopingstatisticsdetailsforthespecifiedVLAN,includingthenumberof
differentgroupsjoinedfortheVLAN.
Commandcontext
Manager(#)
Parameters
vlan-id
Required,1-4094,showsMLDquerypacketTx,Rx,errorpacketcountersonVLAN.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show      | ipv6 mld snooping | vlan 2 statistics |     |
| ------- | --------- | ----------------- | ----------------- | --- |
| MLD     | Snooping  | statistics        |                   |     |
| VLAN    | ID        | : 2               |                   |     |
| VLAN    | Name      | : VLAN2           |                   |     |
| Number  | of        | Include Groups    | : 1               |     |
| Number  | of        | Exclude Groups    | : 0               |     |
| Number  | of        | Static Groups     | : 1               |     |
| Total   | Multicast | Groups Joined     | : 2               |     |
show ipv6 mld snooping [vlan <vlan-id> [group [<group-ip>] [source
<source-ip>]]]
Syntax
show ipv6 mld snooping [vlan <vlan-id> [group [<group-ip>] [source <source-ip>]]]
Description
ThiscommandshowsMLDsnoopingdetailsforthespecifiedVLAN,includingthenumberofdifferent
groupsjoinedfortheVLAN.
Commandcontext
Manager(#)
Parameters
vlan-id
Required:1-4094,showsMLDprotocolinformationforthespecifiedVLAN.
group-ip
Optional:X:X::X:X,MLDsourceinformationforthespecifiedgroup.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 82

source-ip
Optional:X:X::X:X,MLDsourceinformationforthespecifiedgroup.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
switch#
|                | show       | ipv6     | mld snooping  |        | vlan 2 |     |                          |     |      |      |        |         |
| -------------- | ---------- | -------- | ------------- | ------ | ------ | --- | ------------------------ | --- | ---- | ---- | ------ | ------- |
| MLD Snooping   |            | Protocol | Info          |        |        |     |                          |     |      |      |        |         |
| Total          | VLANs      | with     | MLD enabled   |        |        | :   | 2                        |     |      |      |        |         |
| Current        | count      | of       | multicast     | groups | joined | :   | 0                        |     |      |      |        |         |
| MLD Drop       | Unknown    |          | Multicast     |        |        | :   | Global                   |     |      |      |        |         |
| VLAN           | ID         |          |               |        |        | :   | 2                        |     |      |      |        |         |
| VLAN           | Name       |          |               |        |        | :   | VLAN2                    |     |      |      |        |         |
| MLD Configured |            |          | Version       |        |        | :   | 2                        |     |      |      |        |         |
| MLD Operating  |            | Version  |               |        |        | :   | 2                        |     |      |      |        |         |
| Querier        | Address    |          | [this switch] |        |        | :   | fe80::218:71ff:fec4:2f00 |     |      |      |        |         |
| Querier        | Port       |          |               |        |        | :   |                          |     |      |      |        |         |
| Querier        | UpTime     |          |               |        |        | :0m | 21s                      |     |      |      |        |         |
| Querier        | Expiration |          | Time          |        |        | :0m | 2s                       |     |      |      |        |         |
| Active         | Group      | Address  |               |        |        |     | Tracking                 |     | Vers | Mode | Uptime | Expires |
------------------------------------------- --------- ---- ----- --------- ---------
| ff05::2:1 |          |           |              |     |           |       | Filter    |           | 2   | EXC     | 0m 17s | 4m 3s |
| --------- | -------- | --------- | ------------ | --- | --------- | ----- | --------- | --------- | --- | ------- | ------ | ----- |
| switch#   | show     | ipv6      | mld snooping |     | vlan 2    | group |           |           |     |         |        |       |
| MLD ports |          | and group | information  |     | for group |       | ff05::2:1 |           |     |         |        |       |
| VLAN      | ID       |           |              |     |           | :     | 2         |           |     |         |        |       |
| VLAN      | Name     |           |              |     |           | :     | VLAN2     |           |     |         |        |       |
| Group     | Address  |           |              |     |           | :     | ff05::2:1 |           |     |         |        |       |
| Last      | Reporter |           |              |     |           | :     | 2001::1   |           |     |         |        |       |
| Group     | Type     |           |              |     |           | :     | Filter    |           |     |         |        |       |
|           |          |           |              |     |           | V1    |           | Sources   |     | Sources |        |       |
| Port      |          | Vers      | Mode Uptime  |     | Expires   | Timer |           | Forwarded |     | Blocked |        |       |
--------- ---- ---- --------- --------- --------- --------- --------
| 1/1/1     |          | 2         | EXC 0m 5s    |     | 4m 15s    | 4m    | 15s       | 0       |     | 0       |     |     |
| --------- | -------- | --------- | ------------ | --- | --------- | ----- | --------- | ------- | --- | ------- | --- | --- |
| switch#   | show     | ipv6      | mld snooping |     | vlan 2    | group | ff05::2:1 |         |     |         |     |     |
| MLD ports |          | and group | information  |     | for group |       | ff05::2:1 |         |     |         |     |     |
| VLAN      | ID       |           |              |     |           | :     | 2         |         |     |         |     |     |
| VLAN      | Name     |           |              |     |           | :     | VLAN2     |         |     |         |     |     |
| Group     | Address  |           |              |     |           | :     | ff05::2:1 |         |     |         |     |     |
| Last      | Reporter |           |              |     |           | :     | 2001::1   |         |     |         |     |     |
| Group     | Type     |           |              |     |           | :     | Filter    |         |     |         |     |     |
|           |          |           |              |     |           | V1    |           | Sources |     | Sources |     |     |
MLDsnooping|83

| Port |     | Vers Mode | Uptime | Expires |     | Timer | Forwarded | Blocked |
| ---- | --- | --------- | ------ | ------- | --- | ----- | --------- | ------- |
--------- ---- ---- --------- --------- --------- --------- --------
| 1/1/1 |     | 2 EXC | 0m  | 5s 4m | 15s | 4m 15s | 0   | 0   |
| ----- | --- | ----- | --- | ----- | --- | ------ | --- | --- |
switch# show ipv mld snooping vlan 2 group ff05::2:1 source 3000::3
| VLAN      | ID      |                |     |           |                  | : 2         |      |     |
| --------- | ------- | -------------- | --- | --------- | ---------------- | ----------- | ---- | --- |
| VLAN      | Name    |                |     |           |                  | : VLAN2     |      |     |
| Group     | Address |                |     |           |                  | : ff05::2:1 |      |     |
| Source    | Address |                |     |           |                  | : 3000::3   |      |     |
| Source    | Type    |                |     |           |                  | : Filter    |      |     |
| Port      |         | Mode Uptime    |     | Expires   | Configured       |             | Mode |     |
| --------- |         | ---- --------- |     | --------- | ---------------- |             |      |     |
| 1/1/1     |         | INC 0m         | 27s | 3m 53s    | Auto             |             |      |     |
show ipv6 mld snooping [vlan <vlan-id> [group [port <port_id>]]
Syntax
| show ipv6 | mld | snooping | [vlan | <vlan-id> | [group | [port | <port_id>]] |     |
| --------- | --- | -------- | ----- | --------- | ------ | ----- | ----------- | --- |
Description
ThiscommandshowsMLDsnoopingdetailsforthespecifiedVLAN,includingthenumberofdifferent
groupsjoinedfortheVLAN.
Commandcontext
Manager(#)
Parameters
port-id
Required:<PORT>,showsMLDprotocolinformationforthespecifiedportofaVLAN.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show     | ipv       | mld snooping | vlan    | 2 group | port  | 1/1/1     |         |
| ------- | -------- | --------- | ------------ | ------- | ------- | ----- | --------- | ------- |
| VLAN    | ID       | : 2       |              |         |         |       |           |         |
| VLAN    | Name     | : VLAN2   |              |         |         |       |           |         |
| Group   | Address  | :         | ff05::2:1    |         |         |       |           |         |
| Last    | Reporter | :         | fe80::1      |         |         |       |           |         |
| Group   | Type     | :         | Filter       |         |         |       |           |         |
|         |          |           |              |         |         | V1    | Sources   | Sources |
| Port    |          | Vers Mode | Uptime       | Expires |         | Timer | Forwarded | Blocked |
--------- ---- ---- --------- --------- --------- --------- --------
| 1/1/1 |     | 2 INC | 1m  | 46s 2m | 34s |     | 3   | 0   |
| ----- | --- | ----- | --- | ------ | --- | --- | --- | --- |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 84

| Group     | Address | :              | ff05::2:1 |                  |      |     |
| --------- | ------- | -------------- | --------- | ---------------- | ---- | --- |
| Source    | Address | :              | 3000::1   |                  |      |     |
| Source    | Type    | :              | Filter    |                  |      |     |
| Port      |         | Mode Uptime    | Expires   | Configured       | Mode |     |
| --------- |         | ---- --------- | --------- | ---------------- |      |     |
| 1/1/1     |         | INC 1m         | 46s 2m    | 34s Auto         |      |     |
| Group     | Address | :              | ff05::2:1 |                  |      |     |
| Source    | Address | :              | 3000::2   |                  |      |     |
| Source    | Type    | :              | Filter    |                  |      |     |
| Port      |         | Mode Uptime    | Expires   | Configured       | Mode |     |
| --------- |         | ---- --------- | --------- | ---------------- |      |     |
| 1/1/1     |         | INC 1m         | 46s 2m    | 34s Auto         |      |     |
| Group     | Address | :              | ff05::2:1 |                  |      |     |
| Source    | Address | :              | 3000::3   |                  |      |     |
| Source    | Type    | :              | Filter    |                  |      |     |
| Port      |         | Mode Uptime    | Expires   | Configured       | Mode |     |
| --------- |         | ---- --------- | --------- | ---------------- |      |     |
| 1/1/1     |         | INC 1m         | 46s 2m    | 34s Auto         |      |     |
| show      | ipv6    | mld            | snooping  | [static-groups]  |      |     |
Syntax
| show ipv6 | mld | snooping | [static-groups] |     |     |     |
| --------- | --- | -------- | --------------- | --- | --- | --- |
Description
ThiscommandshowsMLDsnoopingstaticgroupdetails,includingthenumberofstaticgroupsjoined.
Commandcontext
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show                                     | ipv6    | mld snooping        | static-groups |               |      |
| ------- | ---------------------------------------- | ------- | ------------------- | ------------- | ------------- | ---- |
| MLD     | Static                                   | Group   | Address Information |               |               |      |
| VLAN    | ID Group                                 | Address |                     |               |               |      |
| ------- | ---------------------------------------- |         |                     |               |               |      |
| 10      | ff12::1                                  |         |                     |               |               |      |
| 10      | ff12::2                                  |         |                     |               |               |      |
| MLD     | configuration                            |         | commands            |               | for interface | VLAN |
| ipv6    | mld {enable                              |         | | disable}          |               |               |      |
MLDsnooping|85

Syntax

ipv6 mld {enable | disable}

Description

This command enables or disables MLD on the interface VLAN.

Command context

config-if-vlan

Parameters

enable

Required: Enable MLD on the interface VLAN.

disable

Required: Disable MLD on the interface VLAN.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 mld enable
switch(config-if-vlan)# ipv6 mld disable

ipv6 mld apply access-list

Syntax

ipv6 mld apply access-list <ACL-NAME>
no ipv6 mld apply access-list <ACL-NAME>

Description

Configures the ACL on a particular interface to filter the MLD join or leave packets based on rules set in the
particular ACL name.

The no form of this command disables the rules set for the ACL.

Command context

config-vlan

Parameters

access-list

Associates an ACL with the IGMP.

<ACL-NAME>

Specifies the name of the ACL.

Authority

Administrators or local user group members with execution rights for this command.

Usage

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

86

ExistingclassifiercommandsareusedtoconfiguretheACL.IncaseanMLDv2packetwithmultiplegroup
addressesisreceived,itwillonlyprocessthepermittedgroupaddressesbasedontheACLruleset,andany
existingjoinswilltimeout.Ifthereisnomatchorifthereisadenyrulematch,thepacketisdropped.
Examples
ConfiguringtheACLtofilterMLDpacketsbasedonrulessetinaccesslistmygroup:
| switch(config)#        | access-list | ipv6     | mygroup            |         |
| ---------------------- | ----------- | -------- | ------------------ | ------- |
| switch(config-acl-ip)# |             | permit   | icmpv6 any ff55::1 |         |
| switch(config-acl-ip)# |             | exit     |                    |         |
| switch(config)#        | interface   | vlan     | 2                  |         |
| switch(config-vlan)#   |             | ipv6 mld | apply access-list  | mygroup |
ConfiguringtheACLtoremovetherulessetinaccesslistmygroup:
| switch(config-vlan)# |     | no ipv6 mld | apply access-list | mygroup |
| -------------------- | --- | ----------- | ----------------- | ------- |
no ipv6 mld
Syntax
no ipv6 mld
Description
ThiscommandremovesallMLDconfigurationsontheinterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Commandcontext
config-if
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#    | interface | 1/1/1    |     |     |
| ------------------ | --------- | -------- | --- | --- |
| switch(config-if)# | no        | ipv6 mld |     |     |
| ipv6 mld querier   |           |          |     |     |
Syntax
ipv6 mld querier
Description
ThiscommandconfiguresMLDquerier.
ThenoformofthiscommanddisablesMLDquerier.
Commandcontext
config-if-vlan
MLDsnooping|87

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config)#         |     | interface | vlan | 2           |     |     |
| ----------------------- | --- | --------- | ---- | ----------- | --- | --- |
| switch(config-if-vlan)# |     |           | ipv6 | mld querier |     |     |
switch(config-if-vlan)#
|          |         |           | no ipv6 | mld querier       |     |     |
| -------- | ------- | --------- | ------- | ----------------- | --- | --- |
| ipv6 mld | querier | [interval |         | <interval-value>] |     |     |
Syntax
| ipv6 mld | querier | [interval | <interval-value>] |     |     |     |
| -------- | ------- | --------- | ----------------- | --- | --- | --- |
Description
ThiscommandconfiguresMLDquerierinterval.Thedefaultinterval-valueis125.
Commandcontext
config-if-vlan
Parameters
interval-value
Required:5-300,configuresMLDquerierinterval.
Defaultinterval-valueis125.Usetheno ipv6 mld querier intervalcommandtosetinterval-valuetothe
default.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config)#         |                            | interface | vlan    | 2           |          |                  |
| ----------------------- | -------------------------- | --------- | ------- | ----------- | -------- | ---------------- |
| switch(config-if-vlan)# |                            |           | ipv6    | mld querier | interval | 100              |
| switch(config-if-vlan)# |                            |           | no ipv6 | mld querier |          | interval         |
| ipv6 mld                | last-member-query-interval |           |         |             |          | <interval-value> |
Syntax
| ipv6 mld | last-member-query-interval |     |     | <interval-value> |     |     |
| -------- | -------------------------- | --- | --- | ---------------- | --- | --- |
Description
ThiscommandconfiguresMLDlastmemberqueryintervalvalueinseconds.Thedefaultinterval-valueis1
second.
Commandcontext
config-if-vlan
Parameters
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 88

interval-value
Required:1-2,configuresMLDlast-member-query-interval.
Defaultinterval-valueis1second.Usethe no ipv6 mld last-member-query-intervalcommandtoset
interval-valuetothedefault.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config)#         |         | interface               | vlan 2      |                            |                 |     |
| ----------------------- | ------- | ----------------------- | ----------- | -------------------------- | --------------- | --- |
| switch(config-if-vlan)# |         |                         | ipv6 mld    | last-member-query-interval |                 | 2   |
| switch(config-if-vlan)# |         |                         | no ipv6 mld | last-member-query-interval |                 |     |
| ipv6 mld                | querier | query-max-response-time |             |                            | <response-time> |     |
Syntax
| ipv6 mld | querier | query-max-response-time |     | <response-time> |     |     |
| -------- | ------- | ----------------------- | --- | --------------- | --- | --- |
Description
ThiscommandconfiguresMLDmaxresponsetimevalueinseconds.Thedefaultmax-response-time-value
is10seconds.
Commandcontext
config-if-vlan
Parameters
max-response-time-value
Required:10-128,configuresMLDqueriermax-response-time.
Defaultmax-response-time-valueis10seconds.Usetheno ipv6 mld querier query-max-response-time
commandtosetmax-response-time-valuetothedefault.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config)#         |            | interface | vlan 2      |                         |     |     |
| ----------------------- | ---------- | --------- | ----------- | ----------------------- | --- | --- |
| switch(config-if-vlan)# |            |           | ipv6 mld    | query-max-response-time |     | 50  |
| switch(config-if-vlan)# |            |           | no ipv6 mld | query-max-response-time |     |     |
| ipv6 mld                | robustness |           |             |                         |     |     |
Syntax
| ipv6 mld | robustness | <VALUE> |     |     |     |     |
| -------- | ---------- | ------- | --- | --- | --- | --- |
Description
MLDsnooping|89

ThiscommandconfiguresMLDrobustness.Therobustnessvaluerepresentsthenumberoftimesthe
querierretriesqueriesontheconnectedsubnets.Thedefaultrobustness-valueis2seconds.
Commandcontext
config-if-vlan
Parameters
<VALUE>
Required:1-7,configuresMLDrobustness.
Defaultrobustness-valueis2seconds.Usetheno ipv6 mld robustnesscommandtosetrobustness-valueto
thedefault.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config)#         |              | interface vlan 2     |            |     |
| ----------------------- | ------------ | -------------------- | ---------- | --- |
| switch(config-if-vlan)# |              | ipv6 mld             | robustness | 5   |
| switch(config-if-vlan)# |              | no ipv6 mld          | robustness |     |
| ipv6 mld                | static-group | <MULTICAST-GROUP-IP> |            |     |
Syntax
| ipv6 mld | static-group | <MULTICAST-GROUP-IP> |     |     |
| -------- | ------------ | -------------------- | --- | --- |
Description
ThiscommandconfiguresMLDstaticgroup.
Commandcontext
config-if-vlan
Parameters
<MULTICAST-GROUP-IP>
Required:X:X::X:X,configuresMLDstaticgroup.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config)#         |         | interface vlan 2 |              |         |
| ----------------------- | ------- | ---------------- | ------------ | ------- |
| switch(config-if-vlan)# |         | ipv6 mld         | static-group | ff12::c |
| switch(config-if-vlan)# |         | no ipv6 mld      | static-group | ff12::c |
| ipv6 mld                | version | <VERSION>        |              |         |
Syntax
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 90

| ipv6 mld | version | <VERSION> |     |     |     |     |
| -------- | ------- | --------- | --- | --- | --- | --- |
Description
ThiscommandconfiguresMLDversion.
Commandcontext
config-if-vlan
Parameters
<VERSION>
Required:1-2,configuresMLDversion.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config)#         |         | interface | vlan      | 2           |     |     |
| ----------------------- | ------- | --------- | --------- | ----------- | --- | --- |
| switch(config-if-vlan)# |         |           | ipv6      | mld version | 2   |     |
| ipv6 mld                | version |           | <VERSION> | [strict]    |     |     |
Syntax
| ipv6 mld | version | <VERSION> | [strict] |     |     |     |
| -------- | ------- | --------- | -------- | --- | --- | --- |
Description
ThiscommandconfiguresMLDstrictversion.Packetsthatdonotmatchtheconfiguredversionwillbe
dropped.Bydefault,strictoptionisnotenabled.
Commandcontext
config-if-vlan
Parameters
<VERSION>
Required:1-2,configuresMLDversion.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config)#         |     | interface | vlan    | 2             |          |      |
| ----------------------- | --- | --------- | ------- | ------------- | -------- | ---- |
| switch(config-if-vlan)# |     |           | ipv6    | mld version   | 2 strict |      |
| switch(config-if-vlan)# |     |           | no ipv6 | mld version   | 2 strict |      |
| MLD show                |     | commands  |         | for interface |          | VLAN |
| show ipv6               | mld |           |         |               |          |      |
MLDsnooping|91

Syntax
| show ipv6 | mld |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- |
Description
ThiscommandshowsMLDconfigurationonVLAN.
Commandcontext
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#   | show          | ipv6    | mld        |     |                           |                   |
| --------- | ------------- | ------- | ---------- | --- | ------------------------- | ----------------- |
| VRF       | Name          |         |            | :   | default                   |                   |
| Interface |               |         |            | :   | vlan10                    |                   |
| MLD       | Configured    | Version |            | :   | 2                         |                   |
| MLD       | Operating     | Version |            | :   | 2                         |                   |
| Querier   | State         |         |            | :   | Querier                   |                   |
| Querier   | IP            | [this   | switch]    | :   | fe80::7272:cfff:fe96:d3ec |                   |
| Querier   | Uptime        |         |            | :   | 39m 44s                   |                   |
| Querier   | Expiration    |         | Time       | :   | 0m 31s                    |                   |
| MLD       | Snoop Enabled |         | on VLAN    | :   | True                      |                   |
| show      | ipv6          | mld     | [interface |     | <intf_id>                 | | vlan <vlan-id>] |
Syntax
| show ipv6 | mld | [interface | <IFNAME> |     | | vlan <VLAN-ID>] |     |
| --------- | --- | ---------- | -------- | --- | ----------------- | --- |
Description
ThiscommandshowsMLDconfigurationonaspecificVLAN.
Commandcontext
Manager(#)
Parameters
<VLAN-ID>
Required:1-4094,showsMLDconfigurationonaspecifiedVLAN.
<IFNAME>
Required:ShowsMLDconfigurationonaspecifiedinterface.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 92

| switch# | show       | ipv6    | mld     | interface  | vlan                      | 10         |     |
| ------- | ---------- | ------- | ------- | ---------- | ------------------------- | ---------- | --- |
| MLD     | Configured | Version |         | : 2        |                           |            |     |
| MLD     | Operating  | Version |         | : 2        |                           |            |     |
| Querier | State      |         |         | :          | Querier                   |            |     |
| Querier | IP         | [this   | switch] | :          | fe80::7272:cfff:fe96:d3ec |            |     |
| Querier | Uptime     |         |         | :          | 40m 42s                   |            |     |
| Querier | Expiration |         | Time    | :          | 1m 39s                    |            |     |
| MLD     | Snoop      | Enabled | on VLAN | :          | True                      |            |     |
| switch# | show       | ipv6    | mld     | interface  | 1/1/2                     |            |     |
| MLD     | Configured | Version |         | : 2        |                           |            |     |
| MLD     | Operating  | Version |         | : 2        |                           |            |     |
| Querier | State      |         |         | :          | Querier                   |            |     |
| Querier | IP         | [this   | switch] | :          | fe80::7272:cfff:fe96:d3ec |            |     |
| Querier | Uptime     |         |         | :          | 40m 42s                   |            |     |
| Querier | Expiration |         | Time    | :          | 1m 39s                    |            |     |
| MLD     | Snoop      | Enabled | on VLAN | :          | True                      |            |     |
| show    | ipv6       | mld     | [vrf    | <vrf_name> |                           | | all-vrfs | ]   |
Syntax
| show ipv6 | mld | [vrf | <VRF-NAME> | |   | all-vrfs | ]   |     |
| --------- | --- | ---- | ---------- | --- | -------- | --- | --- |
Description
ThiscommandshowsMLDinformationforthespecifiedVRF.
Commandcontext
Manager(#)
Parameters
<VRF-NAME>
Optional:showsMLDinformationstatusinaspecificVRF.
all-vrfs
Optional:showsMLDinformationstatusforallVRFs.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch(config)# |            |           | show ipv6 | mld | all-vrfs                |     |     |
| --------------- | ---------- | --------- | --------- | --- | ----------------------- | --- | --- |
| VRF             | Name       | : default |           |     |                         |     |     |
| Interface       |            | : vlan2   |           |     |                         |     |     |
| MLD             | Configured | Version   |           | : 2 |                         |     |     |
| MLD             | Operating  | Version   |           | : 2 |                         |     |     |
| Querier         | State      |           |           | :   | Querier                 |     |     |
| Querier         | IP         | [this     | switch]   | :   | fe80::a00:9ff:fe06:67cd |     |     |
| Querier         | Uptime     |           |           | :   | 23m 53s                 |     |     |
| Querier         | Expiration |           | Time      | :   | 0m 17s                  |     |     |
| MLD             | Snoop      | Enabled   | on VLAN   | :   | True                    |     |     |
MLDsnooping|93

| Active | Group | Address |     |     |     | Vers Mode | Uptime | Expires |
| ------ | ----- | ------- | --- | --- | --- | --------- | ------ | ------- |
-------------------------------------------- ---- ---- --------- ---------
| ff05::2:1 |            |         |         |     |                         | 2 INC     | 3m 56s | 1m 47s  |
| --------- | ---------- | ------- | ------- | --- | ----------------------- | --------- | ------ | ------- |
| VRF       | Name       | : red   |         |     |                         |           |        |         |
| Interface |            | : vlan3 |         |     |                         |           |        |         |
| MLD       | Configured | Version |         | : 2 |                         |           |        |         |
| MLD       | Operating  | Version |         | : 2 |                         |           |        |         |
| Querier   | State      |         |         | :   | Querier                 |           |        |         |
| Querier   | IP         | [this   | switch] | :   | fe80::a00:9ff:fe06:67cd |           |        |         |
| Querier   | Uptime     |         |         | :   | 23m 53s                 |           |        |         |
| Querier   | Expiration |         | Time    | :   | 0m 17s                  |           |        |         |
| MLD       | Snoop      | Enabled | on VLAN | :   | True                    |           |        |         |
| Active    | Group      | Address |         |     |                         | Vers Mode | Uptime | Expires |
-------------------------------------------- ---- ---- --------- ---------
| ff05::2:1       |            |         |           |     |                         | 2 INC     | 2m 30s | 1m 50s  |
| --------------- | ---------- | ------- | --------- | --- | ----------------------- | --------- | ------ | ------- |
| switch(config)# |            |         | show ipv6 | mld | vrf red                 |           |        |         |
| VRF             | Name       | : red   |           |     |                         |           |        |         |
| Interface       |            | : vlan3 |           |     |                         |           |        |         |
| MLD             | Configured | Version |           | : 2 |                         |           |        |         |
| MLD             | Operating  | Version |           | : 2 |                         |           |        |         |
| Querier         | State      |         |           | :   | Querier                 |           |        |         |
| Querier         | IP         | [this   | switch]   | :   | fe80::a00:9ff:fe06:67cd |           |        |         |
| Querier         | Uptime     |         |           | :   | 24m 13s                 |           |        |         |
| Querier         | Expiration |         | Time      | :   | 2m 3s                   |           |        |         |
| MLD             | Snoop      | Enabled | on VLAN   | :   | True                    |           |        |         |
| Active          | Group      | Address |           |     |                         | Vers Mode | Uptime | Expires |
-------------------------------------------- ---- ---- --------- ---------
| ff05::2:1 |     |     |     |     |     | 2 INC | 2m 50s | 1m 30s |
| --------- | --- | --- | --- | --- | --- | ----- | ------ | ------ |
show ipv6 mld [interface <intf-id> | vlan <vlan-id>] [counters]]
Syntax
| show ipv6 | mld | [interface |     | <intf-id> | | vlan <vlan-id>] | [counters]] |     |     |
| --------- | --- | ---------- | --- | --------- | ----------------- | ----------- | --- | --- |
Description
ThiscommandshowsMLDquerypacketTxandRxonaspecificVLAN.
Commandcontext
Manager(#)
Parameters
vlan-id
Required:1-4094,showsMLDconfigurationonaspecifiedVLAN.
intf-id
Required:IFNAME,showsMLDconfigurationonaspecifiedinterface.
counters
Optional:ShowsMLDquerypacketcounterTx-RxonaspecifiedVLAN.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 94

Example
| switch#    | show           | ipv6    | mld interface |         | vlan 2 counters |               |               |
| ---------- | -------------- | ------- | ------------- | ------- | --------------- | ------------- | ------------- |
| MLD        | Counters       |         |               |         |                 |               |               |
| Interface  |                | Name    | : vlan2       |         |                 |               |               |
| VRF        | Name           |         | : default     |         |                 |               |               |
| Membership |                | Timeout | : 0           |         |                 |               |               |
|            |                |         |               |         |                 | Rx            | Tx            |
|            |                |         |               |         |                 | ------------- | ------------- |
| V1         | All Hosts      | Queries |               |         |                 | 0             | 0             |
| V2         | All Hosts      | Queries |               |         |                 | 0             | 0             |
| V1         | Group Specific |         | Queries       |         |                 | 0             | 0             |
| V2         | Group Specific |         | Queries       |         |                 | 0             | 2             |
| Group      | And            | Source  | Specific      | Queries |                 | 0             | 2             |
| V2         | Member         | Reports |               |         |                 | 0             | N/A           |
| V1         | Member         | Reports |               |         |                 | 0             | N/A           |
| V1         | Member         | Leaves  |               |         |                 | 0             | N/A           |
| Packets    | dropped        |         | by ACL        |         |                 | 0             | N/A           |
| switch#    | show           | ipv6    | mld interface |         | 1/1/1 counters  |               |               |
| MLD        | Counters       |         |               |         |                 |               |               |
| Interface  |                | Name    | : 1/1/1       |         |                 |               |               |
| VRF        | Name           |         | : default     |         |                 |               |               |
| Membership |                | Timeout | : 0           |         |                 |               |               |
|            |                |         |               |         |                 | Rx            | Tx            |
|            |                |         |               |         |                 | ------------- | ------------- |
| V1         | All Hosts      | Queries |               |         |                 | 0             | 0             |
| V2         | All Hosts      | Queries |               |         |                 | 0             | 0             |
| V1         | Group Specific |         | Queries       |         |                 | 0             | 0             |
| V2         | Group Specific |         | Queries       |         |                 | 0             | 0             |
| Group      | And            | Source  | Specific      | Queries |                 | 0             | 0             |
| V2         | Member         | Reports |               |         |                 | 0             | N/A           |
| V1         | Member         | Reports |               |         |                 | 0             | N/A           |
| V1         | Member         | Leaves  |               |         |                 | 0             | N/A           |
| Packets    | dropped        |         | by ACL        |         |                 | 0             | N/A           |
show ipv6 mld [interface <intf-id> | vlan <vlan-id>] [groups]]
Syntax
| show ipv6 | mld | [interface | <intf-id> |     | | vlan <vlan-id>] | [groups]] |     |
| --------- | --- | ---------- | --------- | --- | ----------------- | --------- | --- |
Description
ThiscommandshowsMLDgroupsjoineddetails.
Commandcontext
Manager(#)
Parameters
vlan-id
Required:1-4094,showsMLDinformationonaspecifiedVLAN.
intf-id
Required:IFNAME,showsMLDinformationonaspecifiedinterface.
groups
MLDsnooping|95

Optional:ShowsMLDgroupsinformationonaspecifiedinterface.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#       | show ipv    | mld interface | vlan 2    | groups    |          |
| ------------- | ----------- | ------------- | --------- | --------- | -------- |
| MLD group     | information | for group     | ff05::2:1 |           |          |
| Interface     | Name        | : vlan2       |           |           |          |
| VRF Name      |             | : default     |           |           |          |
| Group Address |             | : ff05::2:1   |           |           |          |
| Last Reporter |             | : fe80::1     |           |           |          |
|               |             |               | V1        | Sources   | Sources  |
| Vers Mode     | Uptime      | Expires       | Timer     | Forwarded | Blocked  |
| ---- ----     | ---------   | ---------     | --------- | --------- | -------- |
| 2 INC         | 6m 2s       | 0m 4s         |           | 1         |          |
| Group Address | :           | ff05::2:1     |           |           |          |
| Source        | Address :   | 3000::1       |           |           |          |
| Mode Uptime   | Expire      |               |           |           |          |
| ---- -------- | --------    |               |           |           |          |
| INC 6m        | 2s 0m       | 4s            |           |           |          |
show ipv6 mld [interface (<intf-id> | vlan <vlan-id>) [group <group_
| ip>] [source | <source_ip>]]]] |     |     |     |     |
| ------------ | --------------- | --- | --- | --- | --- |
Syntax
show ipv6 mld [interface (<intf-id> | vlan <vlan-id>) [group <group_ip>] [source <source_
ip>]]]]
Description
ThiscommandshowsMLDjoinedgroupdetailsonaspecifiedinterface.
Commandcontext
Manager(#)
Parameters
group_ip
Required:X:X::X:X,showsMLDjoinedgroupdetails.
source_ip
Required:X:X::X:X,showsMLDjoinedgroupdetailsforaspecifiedsource.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 96

| switch#       | show ipv    | mld interface | vlan 2    | group ff55::5 |          |
| ------------- | ----------- | ------------- | --------- | ------------- | -------- |
| MLD group     | information | for group     | ff55::5   |               |          |
| Interface     | Name        | : vlan2       |           |               |          |
| VRF Name      |             | : default     |           |               |          |
| Group Address |             | : ff55::5     |           |               |          |
| Last Reporter |             | : fe80::1     |           |               |          |
|               |             |               | V1        | Sources       | Sources  |
| Vers Mode     | Uptime      | Expires       | Timer     | Forwarded     | Blocked  |
| ---- ----     | ---------   | ---------     | --------- | ---------     | -------- |
| 2 INC         | 6m 2s       | 0m 4s         |           | 1             |          |
| Group Address |             | : ff55::5     |           |               |          |
| Source        | Address     | : 3000::1     |           |               |          |
| Mode Uptime   | Expire      |               |           |               |          |
| ---- -------- | --------    |               |           |               |          |
| INC 6m        | 2s 0m       | 4s            |           |               |          |
switch# show ipv mld interface vlan 2 group ff55::5 source 3000::1
| Interface     | Name     | : vlan2   |     |     |     |
| ------------- | -------- | --------- | --- | --- | --- |
| VRF Name      |          | : default |     |     |     |
| Group Address |          | : ff55::5 |     |     |     |
| Source        | Address  | : 3000::1 |     |     |     |
| Mode Uptime   | Expire   |           |     |     |     |
| ---- -------- | -------- |           |     |     |     |
| INC 9m        | 37s 2m   | 0s        |     |     |     |
| show ipv6     | mld      | [groups]  |     |     |     |
Syntax
| show ipv6 | mld [groups] |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- |
Description
ThiscommandshowsMLDgroupsjoineddetails.
Commandcontext
Manager(#)
Parameters
groups
Options:showsMLDgroupsinformation.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show ipv6 | mld groups |     |     |     |
| ------- | --------- | ---------- | --- | --- | --- |
MLDsnooping|97

| MLD       | group    | information | for          | group     | ff05::2:11 |                   |          |
| --------- | -------- | ----------- | ------------ | --------- | ---------- | ----------------- | -------- |
| Interface |          | Name        | : vlan2      |           |            |                   |          |
| VRF       | Name     |             | : default    |           |            |                   |          |
| Group     | Address  |             | : ff05::2:11 |           |            |                   |          |
| Last      | Reporter |             | : 2001::1    |           |            |                   |          |
|           |          |             |              |           | V1         | Sources           | Sources  |
| Vers      | Mode     | Uptime      | Expires      |           | Timer      | Forwarded         | Blocked  |
| ----      | ----     | ---------   | ---------    |           | ---------  | ---------         | -------- |
| 1         |          | 2m 27s      | 1m           | 53s       | 1m 53s     |                   |          |
| MLD       | group    | information | for          | group     | ff05::2:12 |                   |          |
| Interface |          | Name        | : vlan2      |           |            |                   |          |
| VRF       | Name     |             | : default    |           |            |                   |          |
| Group     | Address  |             | : ff05::2:12 |           |            |                   |          |
| Last      | Reporter |             | : 2001::1    |           |            |                   |          |
|           |          |             |              |           | V1         | Sources           | Sources  |
| Vers      | Mode     | Uptime      | Expires      |           | Timer      | Forwarded         | Blocked  |
| ----      | ----     | ---------   | ---------    |           | ---------  | ---------         | -------- |
| 1         |          | 0m 3s       | 4m           | 18s       | 4m 18s     |                   |          |
| show      | ipv6     | mld         | groups       | [all-vrfs |            | | vrf <vrf_name>] |          |
Syntax
| show ipv6 | mld | groups | [all-vrfs | |   | vrf <vrf_name>] |     |     |
| --------- | --- | ------ | --------- | --- | --------------- | --- | --- |
Description
ThiscommandshowsMLDgroupsjoineddetailsonVRFs.
Commandcontext
Manager(#)
Parameters
all-vrfs
Optional:showsMLDgroupsjoinedinallVRFs.
vrf-name
Optional:showsMLDgroupsjoinedinaspecificVRF.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show  | ipv6        | mld groups |       | all-vrfs   |     |     |
| ------- | ----- | ----------- | ---------- | ----- | ---------- | --- | --- |
| MLD     | group | information | for        | group | ff05::2:11 |     |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 98

| Interface | Name              | : vlan1      |                  |             |          |
| --------- | ----------------- | ------------ | ---------------- | ----------- | -------- |
| VRF       | Name              | : default    |                  |             |          |
| Group     | Address           | : ff05::2:11 |                  |             |          |
| Last      | Reporter          | : 2001::1    |                  |             |          |
|           |                   |              | V1               | Sources     | Sources  |
| Vers      | Mode Uptime       | Expires      | Timer            | Forwarded   | Blocked  |
| ----      | ---- ---------    | ---------    | ---------        | ---------   | -------- |
| 1         | 4m 4s             | 2m 38s       | 2m 38s           |             |          |
| MLD       | group information | for          | group ff05::2:12 |             |          |
| Interface | Name              | : vlan3      |                  |             |          |
| VRF       | Name              | : red        |                  |             |          |
| Group     | Address           | : ff05::2:12 |                  |             |          |
| Last      | Reporter          | : 2001::1    |                  |             |          |
|           |                   |              | V1               | Sources     | Sources  |
| Vers      | Mode Uptime       | Expires      | Timer            | Forwarded   | Blocked  |
| ----      | ---- ---------    | ---------    | ---------        | ---------   | -------- |
| 1         | 1m 36s            | 2m 45s       | 2m 45s           |             |          |
| switch#   | show ipv6         | mld groups   | vrf default      |             |          |
| MLD       | group information | for          | group ff05::2:11 |             |          |
| Interface | Name              | : vlan2      |                  |             |          |
| VRF       | Name              | : default    |                  |             |          |
| Group     | Address           | : ff05::2:11 |                  |             |          |
| Last      | Reporter          | : 2001::1    |                  |             |          |
|           |                   |              | V1               | Sources     | Sources  |
| Vers      | Mode Uptime       | Expires      | Timer            | Forwarded   | Blocked  |
| ----      | ---- ---------    | ---------    | ---------        | ---------   | -------- |
| 1         | 5m 25s            | 1m 17s       | 1m 17s           |             |          |
| show      | ipv6 mld          | [interface   | <intf-id>        | [counters]] |          |
Syntax
| show ipv6 | mld [interface | <intf-id> | [counters]] |     |     |
| --------- | -------------- | --------- | ----------- | --- | --- |
Description
ThiscommandshowsMLDquerypacketTxandRxonaspecificinterface.
Commandcontext
Manager(#)
Parameters
intf-id
Required:showsMLDconfigurationonaspecifiedinterface.
counters
Optional:showsMLDquerypacketcounterTx-Rxonaspecifiedinterface.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
MLDsnooping|99

Example
| switch#    | show           | ipv6    | mld interface |         | 1/1/1 counters |               |               |
| ---------- | -------------- | ------- | ------------- | ------- | -------------- | ------------- | ------------- |
| MLD        | Counters       |         |               |         |                |               |               |
| Interface  |                | Name    | : 1/1/1       |         |                |               |               |
| VRF        | Name           |         | : default     |         |                |               |               |
| Membership |                | Timeout | : 0           |         |                |               |               |
|            |                |         |               |         |                | Rx            | Tx            |
|            |                |         |               |         |                | ------------- | ------------- |
| V1         | All Hosts      | Queries |               |         |                | 0             | 0             |
| V2         | All Hosts      | Queries |               |         |                | 0             | 9             |
| V1         | Group Specific |         | Queries       |         |                | 0             | 0             |
| V2         | Group Specific |         | Queries       |         |                | 0             | 0             |
| Group      | And            | Source  | Specific      | Queries |                | 0             | 0             |
| V2         | Member         | Reports |               |         |                | 0             | N/A           |
| V1         | Member         | Reports |               |         |                | 0             | N/A           |
| V1         | Member         | Leaves  |               |         |                | 0             | N/A           |
| Packets    | dropped        |         | by ACL        |         |                | 0             | N/A           |
| show       | ipv6           | mld     | [interface    |         | <intf-id>      | [statistics]] |               |
Syntax
| show ipv6 | mld | [interface | <intf-id> |     | [statistics]] |     |     |
| --------- | --- | ---------- | --------- | --- | ------------- | --- | --- |
Description
ThiscommandshowsMLDstatisticsonaspecificinterface.
Commandcontext
Manager(#)
Parameters
intf-id
Required:showsMLDstatisticsonaspecifiedinterface.
statistics
Optional:showsMLDstatisticsonaspecifiedinterface.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#   | show       | ipv6    | mld interface |     | 1/1/1 statistics |     |     |
| --------- | ---------- | ------- | ------------- | --- | ---------------- | --- | --- |
| MLD       | statistics |         |               |     |                  |     |     |
| Interface |            | Name    | : 1/1/1       |     |                  |     |     |
| VRF       | Name       |         | : default     |     |                  |     |     |
| Number    | of         | Include | Groups        |     | : 2              |     |     |
| Number    | of         | Exclude | Groups        |     | : 0              |     |     |
| Number    | of         | Static  | Groups        |     | : 0              |     |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 100

| Total | Multicast | Groups | Joined     | : 2       |           |     |
| ----- | --------- | ------ | ---------- | --------- | --------- | --- |
| show  | ipv6      | mld    | [interface | <intf-id> | [groups]] |     |
Syntax
| show ipv6 | mld | [interface | <intf-id> | [groups]] |     |     |
| --------- | --- | ---------- | --------- | --------- | --- | --- |
Description
ThiscommandshowsMLDgroupsjoineddetails.
Commandcontext
Manager(#)
Parameters
intf-id
Required:showsMLDconfigurationonaspecifiedinterface.
groups
Optional:showsMLDgroupsinformation.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#   | show     | ipv6        | mld interface             | 1/1/1     | groups    |          |
| --------- | -------- | ----------- | ------------------------- | --------- | --------- | -------- |
| MLD       | group    | information | for group                 | ff55::1   |           |          |
| Interface |          | Name        | : 1/1/1                   |           |           |          |
| VRF       | Name     |             | : default                 |           |           |          |
| Group     | Address  |             | : ff55::1                 |           |           |          |
| Last      | Reporter |             | : fe80::a00:9ff:fe77:1062 |           |           |          |
|           |          |             |                           | V1        | Sources   | Sources  |
| Vers      | Mode     | Uptime      | Expires                   | Timer     | Forwarded | Blocked  |
| ----      | ----     | ---------   | ---------                 | --------- | --------- | -------- |
| 2         | EXC      | 0m 14s      | 4m 6s                     |           |           |          |
show ipv6 mld [interface (<intf-id> | vlan <vlan-id>) [group <group_
| ip>] [source |     | <source_ip>]]]] |     |     |     |     |
| ------------ | --- | --------------- | --- | --- | --- | --- |
Syntax
show ipv6 mld [interface (<intf-id> | vlan <vlan-id>) [group <group_ip>] [source <source_
ip>]]]]
Description
ThiscommandshowsMLDjoinedgroupdetailsonaspecifiedinterface.
Commandcontext
MLDsnooping|101

Manager(#)
Parameters
group_ip
Required:X:X::X:X,showsMLDjoinedgroupdetails.
source_ip
Required:X:X::X:X,showsMLDjoinedgroupdetailsforaspecifiedsource.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#   | show     | ipv         | mld interface |       | vlan      | 2 group   | ff55::5 |          |
| --------- | -------- | ----------- | ------------- | ----- | --------- | --------- | ------- | -------- |
| MLD       | group    | information | for           | group | ff55::5   |           |         |          |
| Interface |          | Name        | : vlan2       |       |           |           |         |          |
| VRF       | Name     |             | : default     |       |           |           |         |          |
| Group     | Address  |             | : ff55::5     |       |           |           |         |          |
| Last      | Reporter |             | : fe80::1     |       |           |           |         |          |
|           |          |             |               |       | V1        | Sources   |         | Sources  |
| Vers      | Mode     | Uptime      | Expires       |       | Timer     | Forwarded |         | Blocked  |
| ----      | ----     | ---------   | ---------     |       | --------- | --------- |         | -------- |
| 2         | INC      | 6m 2s       | 0m            | 4s    |           | 1         |         |          |
| Group     | Address  |             | : ff55::5     |       |           |           |         |          |
| Source    | Address  |             | : 3000::1     |       |           |           |         |          |
| Mode      | Uptime   | Expire      |               |       |           |           |         |          |
| ----      | -------- | --------    |               |       |           |           |         |          |
| INC       | 6m 2s    | 0m          | 4s            |       |           |           |         |          |
switch# show ipv mld interface vlan 2 group ff55::5 source 3000::1
| Interface |          | Name     | : vlan2   |            |     |     |           |                    |
| --------- | -------- | -------- | --------- | ---------- | --- | --- | --------- | ------------------ |
| VRF       | Name     |          | : default |            |     |     |           |                    |
| Group     | Address  |          | : ff55::5 |            |     |     |           |                    |
| Source    | Address  |          | : 3000::1 |            |     |     |           |                    |
| Mode      | Uptime   | Expire   |           |            |     |     |           |                    |
| ----      | -------- | -------- |           |            |     |     |           |                    |
| INC       | 9m 37s   | 2m       | 0s        |            |     |     |           |                    |
| show      | ipv6     | mld      | [group    | <group_ip> |     |     | [all-vrfs | | vrf <vrf_name>]] |
Syntax
| show ipv6 | mld | [group | <group_ip> |     | [all-vrfs | |   | vrf <vrf_name>]] |     |
| --------- | --- | ------ | ---------- | --- | --------- | --- | ---------------- | --- |
Description
ThiscommandshowsMLDjoinedgroupdetailsonVRF.
Commandcontext
Manager(#)
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 102

Parameters
group_ip
Required:X:X::X:X,showsMLDjoinedgroupdetails.
all-vrfs
Optional:showsMLDgroupsjoinedinallVRFs.
vrf
Optional:showsMLDgroupsjoinedinaspecificVRF.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#       | show ipv6   | mld group                 | ff55::1          |           |          |
| ------------- | ----------- | ------------------------- | ---------------- | --------- | -------- |
| MLD group     | information | for                       | group ff55::1    |           |          |
| Interface     | Name        | : 1/1/1                   |                  |           |          |
| VRF Name      |             | : default                 |                  |           |          |
| Group Address |             | : ff55::1                 |                  |           |          |
| Last Reporter |             | : fe80::a00:9ff:fe77:1062 |                  |           |          |
|               |             |                           | V1               | Sources   | Sources  |
| Vers Mode     | Uptime      | Expires                   | Timer            | Forwarded | Blocked  |
| ---- ----     | ---------   | ---------                 | ---------        | --------- | -------- |
| 2 EXC         | 3m 12s      | 3m 46s                    |                  |           |          |
| switch#       | show ipv6   | mld group                 | ff05::2:11       | all-vrfs  |          |
| MLD group     | information | for                       | group ff05::2:11 |           |          |
| Interface     | Name        | : vlan2                   |                  |           |          |
| VRF Name      |             | : default                 |                  |           |          |
| Group Address |             | : ff05::2:11              |                  |           |          |
| Last Reporter |             | : 2001::1                 |                  |           |          |
|               |             |                           | V1               | Sources   | Sources  |
| Vers Mode     | Uptime      | Expires                   | Timer            | Forwarded | Blocked  |
| ---- ----     | ---------   | ---------                 | ---------        | --------- | -------- |
| 1             | 1m 16s      | 3m 4s                     | 3m 4s            |           |          |
| MLD group     | information | for                       | group ff05::2:11 |           |          |
| Interface     | Name        | : vlan3                   |                  |           |          |
| VRF Name      |             | : red                     |                  |           |          |
| Group Address |             | : ff05::2:11              |                  |           |          |
| Last Reporter |             | : 2001::1                 |                  |           |          |
|               |             |                           | V1               | Sources   | Sources  |
| Vers Mode     | Uptime      | Expires                   | Timer            | Forwarded | Blocked  |
| ---- ----     | ---------   | ---------                 | ---------        | --------- | -------- |
| 1             | 0m 52s      | 3m 28s                    | 3m 28s           |           |          |
| switch#       | show ipv6   | mld group                 | ff05::2:11       | vrf red   |          |
MLDsnooping|103

| MLD group     | information | for          | group ff05::2:11 |           |          |
| ------------- | ----------- | ------------ | ---------------- | --------- | -------- |
| Interface     | Name        | : vlan3      |                  |           |          |
| VRF Name      |             | : red        |                  |           |          |
| Group Address |             | : ff05::2:11 |                  |           |          |
| Last Reporter |             | : 2001::1    |                  |           |          |
|               |             |              | V1               | Sources   | Sources  |
| Vers Mode     | Uptime      | Expires      | Timer            | Forwarded | Blocked  |
| ---- ----     | ---------   | ---------    | ---------        | --------- | -------- |
| 1             | 1m 24s      | 2m 56s       | 2m 56s           |           |          |
show ipv6 mld [group <group_ip> [source <source_ip> [all-vrfs | vrf
<vrf_name>]]]
Syntax
show ipv6 mld [group <group_ip> [source <source_ip> [all-vrfs | vrf <vrf_name>]]]
Description
ThiscommandshowsMLDjoinedgroupdetailsforasourceonVRF.
Commandcontext
Manager(#)
Parameters
group_ip
Required:X:X::X:X,showsMLDjoinedgroupdetails.
source_ip
Required:X:X::X:X,showsMLDjoinedgroupdetailsforasource.
all-vrfs
Optional:showsMLDgroupsjoinedinallVRFs.
vrf
Optional:showsMLDgroupsjoinedinaspecificVRF.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#       | show ipv6 | mld group | ff05::2:1 | source 3000::1 |     |
| ------------- | --------- | --------- | --------- | -------------- | --- |
| Interface     | Name :    | vlan2     |           |                |     |
| VRF Name      | : default |           |           |                |     |
| Group Address | :         | ff05::2:1 |           |                |     |
| Source        | Address : | 3000::1   |           |                |     |
| Mode Uptime   | Expire    |           |           |                |     |
| ---- -------- | --------  |           |           |                |     |
| INC 0m        | 53s 3m    | 27s       |           |                |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 104

| switch#   | show     | ipv6           | mld group | ff05::2:1 | source 3000::1 | all-vrfs      |
| --------- | -------- | -------------- | --------- | --------- | -------------- | ------------- |
| Interface |          | Name :         | vlan2     |           |                |               |
| VRF       | Name     | : default      |           |           |                |               |
| Group     | Address  | : ff05::2:1    |           |           |                |               |
| Source    | Address  | : 3000::1      |           |           |                |               |
| Mode      | Uptime   | Expire         |           |           |                |               |
| ----      | -------- | --------       |           |           |                |               |
| INC       | 1m 38s   | 4m             | 5s        |           |                |               |
| Interface |          | Name :         | vlan3     |           |                |               |
| VRF       | Name     | : red          |           |           |                |               |
| Group     | Address  | : ff05::2:1    |           |           |                |               |
| Source    | Address  | : 3000::1      |           |           |                |               |
| Mode      | Uptime   | Expire         |           |           |                |               |
| ----      | -------- | --------       |           |           |                |               |
| INC       | 0m 12s   | 4m             | 8s        |           |                |               |
| switch#   | show     | ipv6           | mld group | ff05::2:1 | source 3000::1 | vrf red       |
| Interface |          | Name :         | vlan3     |           |                |               |
| VRF       | Name     | : red          |           |           |                |               |
| Group     | Address  | : ff05::2:1    |           |           |                |               |
| Source    | Address  | : 3000::1      |           |           |                |               |
| Mode      | Uptime   | Expire         |           |           |                |               |
| ----      | -------- | --------       |           |           |                |               |
| INC       | 0m 23s   | 3m             | 57s       |           |                |               |
| show      | ipv6     | mld [interface |           | vlan      | <vlan-id>      | [statistics]] |
Syntax
| show ipv6 | mld | [interface | vlan | <vlan-id> | [statistics]] |     |
| --------- | --- | ---------- | ---- | --------- | ------------- | --- |
Description
ThiscommandshowsMLDstatisticsonaspecificinterfaceVLAN.
Commandcontext
Manager(#)
Parameters
vlan-id
Required:1-4094,showsMLDinformationonaspecifiedVLAN.
statistics
Optional:showsMLDquerypacketTx,Rx,ErrorpacketcountersonaspecifiedVLAN.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show | ipv6 | mld interface | vlan | 2 statistics |     |
| ------- | ---- | ---- | ------------- | ---- | ------------ | --- |
MLDsnooping|105

| MLD       | statistics |                    |        |      |            |              |
| --------- | ---------- | ------------------ | ------ | ---- | ---------- | ------------ |
| Interface |            | Name : vlan2       |        |      |            |              |
| VRF       | Name       | : default          |        |      |            |              |
| Number    | of         | Include Groups     |        | : 2  |            |              |
| Number    | of         | Exclude Groups     |        | : 0  |            |              |
| Number    | of         | Static Groups      |        | : 0  |            |              |
| Total     | Multicast  | Groups             | Joined | : 2  |            |              |
| show      | ipv6       | mld [static-groups |        | [vrf | <vrf_name> | | all-vrfs]] |
Syntax
| show ipv6 | mld | [static-groups | [vrf | <vrf_name> | | all-vrfs]] |     |
| --------- | --- | -------------- | ---- | ---------- | ------------ | --- |
Description
ThiscommandshowsMLDstaticgroups.
Commandcontext
Manager(#)
Parameters
all-vrfs
Optional:showsMLDgroupsjoinedinallVRFs.
vrf
Optional:showsMLDgroupsjoinedinaspecificVRF.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#         | show   | ipv6 mld                                  | static-groups |          |      |     |
| --------------- | ------ | ----------------------------------------- | ------------- | -------- | ---- | --- |
| MLD             | Static | Group Address                             | Information   |          |      |     |
| VRF             | Name   | :default                                  |               |          |      |     |
| Interface       |        | Name Group                                | Address       |          |      |     |
| --------------- |        | ----------------------------------------- |               |          |      |     |
| vlan2           |        | ff12::c                                   |               |          |      |     |
| vlan2           |        | ff12::d                                   |               |          |      |     |
| switch#         | show   | ipv6 mld                                  | static-groups | vrf      | test |     |
| MLD             | Static | Group Address                             | Information   |          |      |     |
| VRF             | Name   | :test                                     |               |          |      |     |
| Interface       |        | Name Group                                | Address       |          |      |     |
| --------------- |        | ----------------------------------------- |               |          |      |     |
| vlan3           |        | ff13::1                                   |               |          |      |     |
| vlan3           |        | ff13::2                                   |               |          |      |     |
| switch#         | show   | ipv6 mld                                  | static-groups | all-vrfs |      |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 106

| MLD             | Static | Group                                     | Address  | Information |     |     |     |
| --------------- | ------ | ----------------------------------------- | -------- | ----------- | --- | --- | --- |
| VRF             | Name   | :default                                  |          |             |     |     |     |
| Interface       |        | Name                                      | Group    | Address     |     |     |     |
| --------------- |        | ----------------------------------------- |          |             |     |     |     |
| vlan2           |        | ff12::c                                   |          |             |     |     |     |
| vlan2           |        | ff12::d                                   |          |             |     |     |     |
| VRF             | Name   | :test                                     |          |             |     |     |     |
| Interface       |        | Name                                      | Group    | Address     |     |     |     |
| --------------- |        | ----------------------------------------- |          |             |     |     |     |
| vlan3           |        | ff13::1                                   |          |             |     |     |     |
| vlan3           |        | ff13::2                                   |          |             |     |     |     |
| show            | ipv6   | mld                                       | counters |             |     |     |     |
Syntax
| show ipv6 | mld | [counters | [ vrf | <vrf_name> | ]]  |     |     |
| --------- | --- | --------- | ----- | ---------- | --- | --- | --- |
Description
ThiscommandshowsMLDcounters.
Commandcontext
Manager(#)
Parameters
vrf
Optional:showsMLDcounterstatusinaspecificVRF.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#    | show           | ipv6    | mld counters |         |         |               |               |
| ---------- | -------------- | ------- | ------------ | ------- | ------- | ------------- | ------------- |
| MLD        | Counters       |         |              |         |         |               |               |
| Interface  |                | Name    | : vlan2      |         |         |               |               |
| VRF        | Name           |         | : default    |         |         |               |               |
| Membership |                | Timeout | : 0          |         |         |               |               |
|            |                |         |              |         |         | Rx            | Tx            |
|            |                |         |              |         |         | ------------- | ------------- |
| V1         | All Hosts      | Queries |              |         |         | 0             | 0             |
| V2         | All Hosts      | Queries |              |         |         | 0             | 12            |
| V1         | Group Specific |         | Queries      |         |         | 0             | 0             |
| V2         | Group Specific |         | Queries      |         |         | 0             | 0             |
| Group      | And            | Source  | Specific     | Queries |         | 0             | 0             |
| V2         | Member         | Reports |              |         |         | 0             | N/A           |
| V1         | Member         | Reports |              |         |         | 0             | N/A           |
| V1         | Member         | Leaves  |              |         |         | 0             | N/A           |
| Packets    | dropped        | by      | ACL          |         |         | 0             | N/A           |
| switch#    | show           | ipv6    | mld counters | vrf     | default |               |               |
MLDsnooping|107

| MLD Counters      |            |          |            |               |               |
| ----------------- | ---------- | -------- | ---------- | ------------- | ------------- |
| Interface         | Name       |          | : vlan2    |               |               |
| VRF Name          |            |          | : default  |               |               |
| Membership        | Timeout    |          | : 0        |               |               |
|                   |            |          |            | Rx            | Tx            |
|                   |            |          |            | ------------- | ------------- |
| V1 All            | Hosts      | Queries  |            | 0             | 0             |
| V2 All            | Hosts      | Queries  |            | 0             | 12            |
| V1 Group          | Specific   | Queries  |            | 0             | 0             |
| V2 Group          | Specific   | Queries  |            | 0             | 0             |
| Group             | And Source | Specific | Queries    | 0             | 0             |
| V2 Member         | Reports    |          |            | 0             | N/A           |
| V1 Member         | Reports    |          |            | 0             | N/A           |
| V1 Member         | Leaves     |          |            | 0             | N/A           |
| Packets           | dropped    | by       | ACL        | 0             | N/A           |
| MLD configuration |            |          | commands   | for interface |               |
| ipv6 mld          | {enable    |          | | disable} |               |               |
Syntax
| ipv6 mld | {enable | | disable} |     |     |     |
| -------- | ------- | ---------- | --- | --- | --- |
Description
ThiscommandenablesordisablesMLDontheinterface.
Commandcontext
config-if
Parameters
enable
Required:EnableMLDontheinterface.
disable
Required:DisableMLDontheinterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#    |       | interface   | 1/1/1            |     |     |
| ------------------ | ----- | ----------- | ---------------- | --- | --- |
| switch(config-if)# |       |             | ipv6 mld enable  |     |     |
| switch(config-if)# |       |             | ipv6 mld disable |     |     |
| ipv6 mld           | apply | access-list |                  |     |     |
Syntax
| ipv6 mld    | apply access-list |             | <ACL-NAME> |     |     |
| ----------- | ----------------- | ----------- | ---------- | --- | --- |
| no ipv6 mld | apply             | access-list | <ACL-NAME> |     |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 108

Description

Configures the ACL on a particular interface to filter the MLD join or leave packets based on rules set in the
particular ACL name.

The no form of this command removes the rules set for the ACL.

Command context

config-vlan

Parameters

access-list

Associates an ACL with the IGMP.

<ACL-NAME>

Specifies the name of the ACL.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Existing classifier commands are used to configure the ACL. In case an MLDv2 packet with multiple group
addresses is received, it will only process the permitted group addresses based on the ACL rule set, and any
existing joins will time out. If there is no match or if there is a deny rule match, the packet is dropped.

Examples

On the 6400 Switch Series, interface identification differs.

Configuring the ACL to filter MLD packets based on rules set in access list mygroup:

switch(config)# access-list ipv6 mygroup
switch(config-acl-ip)# permit icmpv6 any ff55::1
switch(config-acl-ip)# exit
switch(config)# interface 1/1/1
switch(config-vlan)# ipv6 mld apply access-list mygroup

Configuring the ACL to remove the rules set in access list mygroup:

switch(config-vlan)# no ipv6 mld apply access-list mygroup

no ipv6 mld

Syntax

no ipv6 mld

Description

This command removes all MLD configurations on the interface.

Authority

Administrators or local user group members with execution rights for this command.

Command context

config-if

MLD snooping | 109

Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
switch(config)#
|                    |         | interface 1/1/1 |     |
| ------------------ | ------- | --------------- | --- |
| switch(config-if)# |         | no ipv6 mld     |     |
| ipv6 mld           | querier |                 |     |
Syntax
| ipv6 mld | querier |     |     |
| -------- | ------- | --- | --- |
Description
ThiscommandconfiguresMLDquerier.Thisfunctionalitywillallowtheinterfacetojoininthequerier-
electionprocess.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
switch(config)#
|                    |         | interface 1/1/1 |                   |
| ------------------ | ------- | --------------- | ----------------- |
| switch(config-if)# |         | ipv6 mld        | querier           |
| switch(config-if)# |         | no ipv6 mld     | querier           |
| ipv6 mld           | querier | [interval       | <interval-value>] |
Syntax
| ipv6 mld | querier [interval | <interval-value>] |     |
| -------- | ----------------- | ----------------- | --- |
Description
ThiscommandconfiguresMLDquerierinterval.Thedefaultinterval-valueis125.
Commandcontext
config-if
Parameters
interval-value
Required:5-300,configuresMLDquerierinterval.
Defaultinterval-valueis125.Usetheno ipv6 mld querier intervalcommandtosetinterval-valuetothe
default.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 110

Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
switch(config)#
|                    |                            | interface | 1/1/1       |              |     |
| ------------------ | -------------------------- | --------- | ----------- | ------------ | --- |
| switch(config-if)# |                            | ipv6      | mld querier | interval 100 |     |
| switch(config-if)# |                            | no ipv6   | mld querier | interval     |     |
| ipv6 mld           | last-member-query-interval |           |             |              |     |
Syntax
| ipv6 mld | last-member-query-interval |     |     | <interval-value> |     |
| -------- | -------------------------- | --- | --- | ---------------- | --- |
Description
ThiscommandconfiguresMLDlastmemberqueryintervalvalueinseconds.Thedefaultinterval-valueis1
second.
Commandcontext
config-if
Parameters
interval-value
Required:1-2,configuresMLDlast-member-query-interval.
Defaultinterval-valueis1second.Usetheno ipv6 mld last-member-query-intervalcommandtoset
interval-valuetothedefault.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#    |         | interface               | 1/1/1                          |     |     |
| ------------------ | ------- | ----------------------- | ------------------------------ | --- | --- |
| switch(config-if)# |         | ipv6                    | mld last-member-query-interval |     | 2   |
| switch(config-if)# |         | no ipv6                 | mld last-member-query-interval |     |     |
| ipv6 mld           | querier | query-max-response-time |                                |     |     |
Syntax
| ipv6 mld | querier | query-max-response-time |     | <response-time> |     |
| -------- | ------- | ----------------------- | --- | --------------- | --- |
Description
ThiscommandconfiguresMLDmaxresponsetimevalueinseconds.Thedefaultmax-response-time-value
is10seconds.
Commandcontext
config-if
MLDsnooping|111

Parameters
max-response-time-value
Required:10-128,configuresMLDqueriermax-response-time.
Defaultmax-response-time-valueis10seconds.Usetheno ipv6 mld querier query-max-response-time
commandtosetmax-response-time-valuetothedefault.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#     | interface | 1/1/1                       |     |     |
| ------------------- | --------- | --------------------------- | --- | --- |
| switch(config-if)#  | ipv6      | mld query-max-response-time |     | 50  |
| switch(config-if)#  | no ipv6   | mld query-max-response-time |     |     |
| ipv6 mld robustness |           |                             |     |     |
Syntax
| ipv6 mld robustness | <value> |     |     |     |
| ------------------- | ------- | --- | --- | --- |
Description
ThiscommandconfiguresMLDrobustness.Therobustnessvaluerepresentsthenumberoftimesthe
querierretriesqueriesontheconnectedsubnets.Thedefaultrobustness-valueis2seconds.
Commandcontext
config-if
Parameters
robustness-value
Required:1-7,configuresMLDrobustness.
Defaultrobustness-valueis2seconds.Usetheno ipv6 mld robustnesscommandtosetrobustness-valueto
thedefault.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#       | interface | 1/1l/1         |     |     |
| --------------------- | --------- | -------------- | --- | --- |
| switch(config-if)#    | ipv6      | mld robustness | 5   |     |
| switch(config-if)#    | no ipv6   | mld robustness |     |     |
| ipv6 mld static-group |           |                |     |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 112

Syntax
| ipv6 mld | static-group | <multicast-group-ip> |     |     |     |
| -------- | ------------ | -------------------- | --- | --- | --- |
Description
ThiscommandconfiguresMLDstaticgroup.
Commandcontext
config-if
Parameters
multicast-group-ip
Required:X:X::X:X,configuresMLDstaticgroup.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#    |         | interface | 1/1/1            |     |         |
| ------------------ | ------- | --------- | ---------------- | --- | ------- |
| switch(config-if)# |         | ipv6      | mld static-group |     | ff12::c |
| switch(config-if)# |         | no ipv6   | mld static-group |     | ff12::c |
| ipv6 mld           | version |           |                  |     |         |
Syntax
| ipv6 mld | version | <version> |     |     |     |
| -------- | ------- | --------- | --- | --- | --- |
Description
ThiscommandconfiguresMLDversion.
Commandcontext
config-if
Parameters
version
Required:1-2,configuresMLDversion.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#    |         | interface | 1/1/1       |     |     |
| ------------------ | ------- | --------- | ----------- | --- | --- |
| switch(config-if)# |         | ipv6      | mld version | 2   |     |
| ipv6 mld           | version | [strict]  |             |     |     |
MLDsnooping|113

Syntax
| ipv6 mld version | <version> |     | [strict] |     |
| ---------------- | --------- | --- | -------- | --- |
Description
ThiscommandconfiguresMLDstrictversion.Packetsthatdonotmatchtheconfiguredversionwillbe
dropped.Bydefault,strictoptionisnotenabled.
Commandcontext
config-if
Parameters
version
Required:1-2,configuresMLDversion.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#    |     | interface | 1/1/1       |          |
| ------------------ | --- | --------- | ----------- | -------- |
| switch(config-if)# |     | ipv6      | mld version | 2 strict |
switch(config-if)#
|     |     | no ipv6 | mld version | 2 strict |
| --- | --- | ------- | ----------- | -------- |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 114

|          |             |           |          |             |          |     |           |     | Chapter  | 6   |
| -------- | ----------- | --------- | -------- | ----------- | -------- | --- | --------- | --- | -------- | --- |
|          |             |           | Protocol | Independent |          |     | Multicast |     | - Sparse |     |
|          |             |           |          |             |          |     | Mode      | (V4 | and      | V6) |
| Protocol | Independent | Multicast | - Sparse |             | Mode (V4 | and | V6)       |     |          |     |
Inanetwork,IPmulticasttraffictransmittedformultimediaapplicationsisblockedatroutedinterface
boundariesunlessamulticastroutingprotocolisrunning.ProtocolIndependentMulticast(PIM)isafamily
ofroutingprotocols.Itformsmulticasttreestoforwardtrafficfrommulticastsourcestosubnetswhichuse
protocolssuchasIGMPandMLDtorequestthetraffic.
| Protocol | Independent |     | Multicast |     | - Sparse |     | Mode | (PIM-SM) |     |     |
| -------- | ----------- | --- | --------- | --- | -------- | --- | ---- | -------- | --- | --- |
overview
PIMreliesontheunicastroutingtablestoidentifythepathbacktoamulticastsource(reversepath
forwarding(RPF)).Theunicastroutingprotocolscreatetheunicastroutingtables.Withthisinformation,PIM
setsupthedistributiontreeforthemulticasttraffic.
PIM-SparseMode(PIM-SM)canbeconfiguredonphysicalports,VLANinterfaces,LAGinterfaces,and
loopbackinterfaces.Allsuchconfigurationsworkinthementionedinterfacescontext.
IGMP/MLDprovidesthemulticasttrafficlinkbetweenahostandamulticastrouterrunningPIM-SM.Both
PIM-SMandIGMP/MLDmustbeenabledonVLANswhosememberportshavedirectlyconnectedhosts
withavalidneedtojoinmulticastgroups.
PIM-SMusesthepullmodeformulticastforwarding,anditissuitableforlargeandmedium-sizednetworks
withsparselyandwidelydistributedmulticastgroupmembers.
PIM-SMassumesthatmosthostsdonotwanttoreceivemulticasttraffic.Itusesanonfloodingmulticast
modeltodirecttrafficfromthesourcetotheinterfacewhentherearemulticastreceiversinthegroup.Asa
result,thismodelsendstrafficonlytotheroutersthatspecificallyrequestit.
| PIM-SM | defaults, | protocols, |     | and | supported |     | configuration |     |     |     |
| ------ | --------- | ---------- | --- | --- | --------- | --- | ------------- | --- | --- | --- |
Defaultconfiguration
PIM-SMisdisabledbydefault.WhenPIM-SMisenabled,switchingtoSPTandLANprunedelayarethe
defaultconfigurationactivated.
PIM specification
ComplieswithPIM-SMspecification(RFC4061).
BSR implementation
ComplieswithRFC5059(scopezonesarenotsupported).
Routingprotocolsupport
PIMusesunicastroutinginformationfromanyoftheroutingprotocolsthatarerunningonthesystem,
suchasOSPFv2,OSPFv3,BGP.StaticroutesarealsosupportedwithNexthopIPaddresses.
| Maxinterface | supportper |     | flow |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
115
| AOS-CX10.07MulticastGuide| | (6300,6400,8xxxSwitchSeries) |     |     |     |     |     |     |     |     |     |
| -------------------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Up to 127 outbound interfaces (and 1 inbound interface) are supported in the multicast routing table at
any given time. The sum of all outbound interfaces across all current flows on a router may not exceed
127.

PIM enabled interfaces (L3 and SVI)

The maximum PIM enabled interface is 1000 with an upper limit of 128 per VRF.

IGMP and MLD compatibility

PIM-SM is compatible with IGMP version 2 and version 3, MLD version 1 and version 2, and is fully
interoperable with IGMP/MLD for determining multicast flows.

VRRP

PIM-SM is fully interoperable with VRRP to quickly transition multicast routes in a failover.

VRF support

PIM-SM can run on multiple VRF instances in parallel. It is supported on all VRFs supported in the system.

Static RPs count

PIM-SM supports a maximum of 8 static RPs per VRF.

PIM-SM router types
Within a PIM-SM domain, PIM-SM routers can be configured to fill one or more of the following roles:

n Designated router (DR): A router performing this function forwards multicast traffic from a unicast

source to the appropriate distribution (rendezvous) point.

n Bootstrap router (BSR): A router elected to this function keeps all routers in a PIM-SM domain

informed of the currently assigned rendezvous point (RP) for each multicast group currently known in
the domain.

n Rendezvous point (RP): A router elected as an RP for a multicast group receives requested multicast
traffic from a DR and forwards it toward the multicast receivers requesting the traffic. An RP can be
manually configured or dynamically elected through the BSR process.

n Static RP: This option forwards traffic in the same way as an RP, but requires manual configuration on

all routers in the domain to be effective.

n Candidate RP (C-RP): The C-RP periodically sends advertisement messages to the BSR, which collects

RP-set information for RP election. The BSR starts a holdtime timer for a C-RP after it receives an
advertisement message. If the BSR does not receive any advertisement message when the timer expires,
it considers the C-RP failed or unreachable.

All of these can be enabled on each of several routers in a PIM-SM domain.

DR

In a LAN segment populated by one or more routers running PIM-SM, one such router is elected the DR for
that LAN segment. When the DR receives a Join request from a multicast receiver on that LAN segment, it
forwards the join toward the router operating as the RP for the requested multicast group.

Where multiple PIM-SM routers exist in a LAN segment, the following criteria is used to elect a DR:

1. The router configured with the highest DR priority in the LAN segment is elected.

2.

If multiple routers in the LAN segment are configured with the same DR priority, the router having
the highest IP address is elected.

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 116

In a given domain, each LAN segment capable of receiving multicast traffic from a unicast source should
have at least one DR. (Enabling PIM-SM on a LAN segment automatically enables the router as a DR for that
LAN segment.) Because there is an election process for DR on each LAN segment, all routers on a LAN
segment must be enabled for DR. Where it is important to ensure that a particular router is elected as the
DR for a given LAN segment, you can increase the DR priority on that LAN segment configuration for that
router.

If it is necessary to prevent a router from operating as a DR on a given LAN segment, disable DR operation
by configuring the DR priority as zero (0).

BSR

Before a DR can forward encapsulated packets for a specific multicast group to an RP, it must know which
router in the domain is the elected RP for that multicast group. The BSR function enables this operation by
doing the following:

1. Learns the group-to-RP mappings on the C-RPs in the domain by reading the periodic advertisements

each one sends to the BSR.

2. Distributes the aggregate Candidate-RP (C-RP) information as an RP-set to the PIM-SM routers in the
domain. This is followed by an election to assign a specific multicast group or range of groups to the
C-RPs in the domain. The software supports assignment of up to four multicast addresses and/or
ranges of multicast addresses to a Candidate Rendezvous Point.

The BSR periodically sends bootstrap messages to the other PIM-SM routers in the domain to maintain and
update the RP-set data throughout the domain, and to maintain its status as the elected BSR.

RP

Instead of flooding multicast traffic as is done with PIM-DM, PIM-SM uses a set of multiple routers to
operate as RPs. Each RP controls multicast traffic forwarding for one or more multicast groups as follows:

n Receives traffic from multicast sources (S) through a DR.

n Receives multicast joins from routers requesting multicast traffic.

n Forwards the requested multicast traffic to the requesting routers.

The routers requesting multicast traffic are either edge routers or intermediate routers. Edge routers are
directly connected to specific multicast receivers using IGMP/MLD to request traffic. Intermediate routers
are on the path between edge routers and the RP. This is known as an RP Tree (RPT) where only the
multicast address appears in the routing table. For example:

( *, G ), where:

* = a variable (wildcard) representing the IP address of any multicast source

G = a particular multicast group address.

C-RP

Within a PIM-SM domain, different RPs support different multicast addresses or ranges of multicast
addresses. That is, a given PIM-SM multicast group or range of groups is supported by only one active RP,
although other C-RPs can also be configured with overlapping or identical support.

A C-RP's group-prefix configuration identifies the multicast groups the RP is enabled to support.

If multiple C-RPs have group-prefixes configured so that any of these RPs can support a given multicast
group, then the following criteria are used to select the RP to support the group:

1. The C-RP configured with the longest group-prefix mask applicable to the multicast group is selected

to support the group. Step 2 of this procedure applies if multiple RP candidates meet this criterion.

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

117

2. The C-RP configured with the highest priority is selected. Step 3 of this procedure applies if multiple

RP candidates meet this criterion

3. A hash function (using the configured bsr-candidate hash-mask-length value) generates a series of
mask length values that are individually assigned to the set of eligible C-RPs. If the hash function
matches a single RP candidate to a longer mask length than the other candidates, that candidate is
selected to support the group. Apply step 4 of this procedure if the hash function matches the
longest mask length to multiple RP candidates.

4. The C-RP having the highest IP address is selected to support the group.

Also, within a PIM-SM domain, a router can be configured as a C-RP available for a given multicast group or
range of groups and as the static RP for a given multicast group or range of groups. The recommended
practice is to use C-RPs for all multicast groups unless there is a need to ensure that a specific group or range
of groups is always supported by the same routing switch.

Loopback, Route Only Port (ROP), and Switched Virtual Interface (SVI) are interfaces that can be configured
as RPs. Anycast RP is also supported with the help of MSDP mesh groups.

Static RP

Like C-RPs, static RPs control multicast forwarding of specific multicast groups or ranges of contiguous
groups. However, static RPs are not dynamically learned, and increase the configuration and monitoring
effort to maintain them. As a result, static RPs are not recommended for use except where one of the
following conditions applies:

n It is desirable to designate a specific router interface as a backup RP for specific groups.

n Specific multicast groups are expected, and a static RP would help to avoid overloading a given RP with a

high volume of multicast traffic.

n A C-RP for the same groups is less reliable than another RP that would not normally be elected to support

the groups.

n Tighter traffic control or a higher priority is desired for specific multicast groups.

How PIM-SM works
PIM-SM (PIM Sparse Mode) assumes that most hosts do not want to receive multicast traffic. It uses a
nonflooding multicast model to direct traffic from the source to the interface when there are multicast
receivers in the group. As a result, this model sends traffic only to the routers that specifically request it.

In a given PIM-SM domain, routers identified as DRs, RPs, and a BSR participate in delivering multicast traffic
to the IP multicast receivers that request it. This approach avoids the flooding method of distributing
multicast traffic (employed by PIM-DM) and is best suited for lower bandwidth situations.

The software supports the following operation to enable multicast traffic delivery within a PIM-SM domain:

n From a pool of eligible DR candidates in each LAN segment, one DR is elected for each LAN segment

interface having at least one PIM-SM router. In a multinetted domain, this DR supports multicast traffic
from a source on any subnet in the LAN segment.

n From a pool of eligible BSR candidates in the domain, one BSR is elected for the entire domain.

n From a pool of eligible C-RPs, one is elected to support each multicast group or range of groups allowed
in the domain, excluding any group supported only by static RPs. The multicast groups allowed in the
domain are determined by the aggregation of the groups allowed by the individually configured RPs and
any static RPs. C-RPs and static RPs can be configured with overlapping support for a given set of
multicast groups.

Neighbor discovery

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 118

In a PIM domain, each PIM interface on a router periodically multicasts PIM hello messages to all other PIM
routers (identified by the address 224.0.0.13 for V4 and ff02::d for V6) on the local subnet. Through the
exchanging of hello messages, all PIM routers on the subnet determine their PIM neighbors, maintain PIM
neighboring relationship with other routers, and build and maintain shortest path trees (SPTs).

DR election

A designated router (DR) is required on both the source-side network and receiver-side network. A source-
side DR acts on behalf of the multicast source to send register messages to the RP. The receiver-side DR acts
on behalf of the multicast receivers to send join messages to the RP.

The DR election process is as follows:

1. The routers on the shared-media LAN send hello messages to one another. The hello messages

contain the DR priority for DR election. The router with the highest DR priority is elected as the DR.

2. The router with the highest IP address wins the DR election under one of following conditions:

n All the routers have the same DR election priority.

n A router does not support carrying the DR priority in hello messages.

If the DR fails, its PIM neighbor lifetime expires and the other routers will initiate to elect a new DR.

Rendezvous point tree (RPT)

When a DR in a VLAN receives traffic for a particular multicast group from a source on that VLAN, the DR
encapsulates the traffic and forwards it to the RP elected to support that multicast group. The RP
decapsulates the traffic and forwards it on toward the multicast receivers requesting that group. This forms
an RPT extending from the DR through any intermediate PIM-SM routers leading to the PIM-SM edge
routers for the multicast receivers requesting the traffic. (If the RP has no current join requests for the
group, the traffic is dropped at the RP.)

Shortest path tree (SPT)

SPTs are especially useful in high data-rate applications where reducing unnecessary traffic concentrations
and throughput delays are significant. In the default PIM-SM configuration, SPT operation is automatically
enabled.

In the default PIM-SM configuration, after an edge router receives the first packet of traffic for a multicast
group requested by a multicast receiver on that router, it uses Reverse Path Forwarding (RPF) to learn the
shortest path to the group source. The edge router then stops using the RPT and begins using the shortest
path tree (SPT) connecting the multicast source and the multicast receiver. In this case, when the edge
router begins receiving group traffic from the multicast source through the SPT, it sends a prune message to
the RP tree to terminate sending the requested group traffic on that route. (This results in entries for both
the RP path and the STP in the routing table.) When completed, the switchover from the RPT to a shorter
SPT can reduce unnecessary traffic concentrations in the network and reduce multicast traffic throughput
delays.

The switchover from RPT to SPT is not instantaneous. For a short period, packets for a given multicast group
may be received from both the RPT and the SPT. Also, in some topologies, the RPT and SPT to the same edge
router may be identical.

Reverse Path Forward

Reverse Path Forward (RPF) checking is a core multicast routing mechanism that ensures that multicast
traffic received arrived on the expected router interface before it is considered for further processing. If the
RPF check fails for a multicast packet, the packet is discarded.

For traffic arriving on the SPT, the expected incoming interface for a given source/group multicast flow is the
interface towards the source address of the traffic (as determined by the unicast routing system). For traffic

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

119

arrivingontheRPtree,theexpectedincominginterfaceistheinterfacetowardstheRP.PIMmustbe
enabledonallpathswheretheunicastroutepointsanECMPpathtothesource.
RPFoverrideisafeaturethatallowstheoverrideofthenormalRPFlookupmechanismandindicatestothe
routerthatitmayacceptmulticasttrafficonaninterfaceotherthanthatwhichwouldbenormallyselected
bytheRPFlookupmechanism.Thisincludesacceptingtrafficfromasourcedirectlyconnectedtotherouter
whenthesourceIPaddressisinvalidforthesubnetorVLANtowhichitisconnected.Trafficmayalsobe
acceptedfromavalidPIMneighborthatisnotonthereversepathtowardsthesourceofthereceived
multicasttraffic.
RPFcheckingisappliedtoallmulticasttrafficandissignificantinpreventingnetworkloops.Uptoeight
manualRPFoverridescanbespecified.
TheRPF-addressindicatesoneoftwodistinctRPFcandidates:
1. AvalidPIMneighboraddressfromwhichforwardedmulticasttrafficisacceptedwithasource
addressof<source-addr/src-mask>.
2. AlocalrouteraddressonaPIM-enabledinterfacetowhich<source-addr/src-mask>isdirectly
connected.ThelocalrouterwillassumetheroleofDRforthisflowandregisterstheflowwithanRP,
ifconfigured.
| Enabling/disabling |     | PIM-SM | in an interface |
| ------------------ | --- | ------ | --------------- |
Prerequisites
Youmustbeintheinterfaceconfigurationcontext,asindicatedbytheswitch(config-if)#prompt,
switch(config-if-vlan)#prompt,orswitch(config-lag-if)#prompt.
Procedure
EnableordisablePIM-SMinaninterfaceusingthefollowingcommand.
Forexample,thefollowingcommandenablesPIM-SMoninterfacevlan40:
ForIPv4configurations:
| ip pim-sparse {enable|disable} |           |               |             |
| ------------------------------ | --------- | ------------- | ----------- |
| switch(config)#                | interface | vlan40        |             |
| switch(config-if-vlan)#        |           | ip address    | 40.0.0.4/24 |
| switch(config-if-vlan)#        |           | ip pim-sparse | enable      |
ForIPv6configurations:
| ipv6 pim6-sparse        | {enable|disable} |            |             |
| ----------------------- | ---------------- | ---------- | ----------- |
| switch(config)#         | interface        | vlan40     |             |
| switch(config-if-vlan)# |                  | ip address | 2001::01/64 |
switch(config-if-vlan)#
|     |     | ipv6 pim6-sparse | enable |
| --- | --- | ---------------- | ------ |
ThenoformofthecommanddisablesPIM-SMinaninterface.
| Configuring | PIM-SM | options | in an interface |
| ----------- | ------ | ------- | --------------- |
YoucanconfigurevariousPIM-SMoptionsinaninterfaceasdescribedinthefollowingsteps.
Prerequisites
ProtocolIndependentMulticast-SparseMode(V4andV6)|120

Youmustceconfigurationcontext,asindicatedbytheswitch(config-if)#prompt,switch(config-if-
vlan)#prompt,orswitch(config-lag-if)#prompt.
Procedure
1. ConfigurethefrequencyatwhichtheroutertransmitsPIMhellomessagesonthecurrentinterface
usingthefollowingcommand.
ForIPv4configurations:
| ip pim-sparse | hello-interval |     |     | <INTERVAL-VALUE> |     |     |     |     |
| ------------- | -------------- | --- | --- | ---------------- | --- | --- | --- | --- |
Forexample,thefollowingcommandsetstheV4hellointervalto60secondsonthe1/1/4interface:
switch(config)#
|                    |     | interface |               | 1/1/4 |                |     |     |     |
| ------------------ | --- | --------- | ------------- | ----- | -------------- | --- | --- | --- |
| switch(config-if)# |     |           | ip pim-sparse |       | hello-interval |     | 60  |     |
ForIPv6configurations:
| ipv6 pim6-sparse |     | hello-interval |     | <INTERVAL-VALUE> |     |     |     |     |
| ---------------- | --- | -------------- | --- | ---------------- | --- | --- | --- | --- |
Forexample,thefollowingcommandsetstheV6hellointervalto60secondsonthe1/1/4interface:
| switch(config)#    |     | interface |                  | 1/1/4 |                |     |     |     |
| ------------------ | --- | --------- | ---------------- | ----- | -------------- | --- | --- | --- |
| switch(config-if)# |     |           | ipv6 pim6-sparse |       | hello-interval |     |     | 60  |
2. ChangethemaximumtimebeforetheroutertransmitstheinitialPIMhellomessageontheinterface
usingthefollowingcommand.
ForIPv4configurations:
| ip pim-sparse | hello-delay |     | <DELAY-VALUE> |     |     |     |     |     |
| ------------- | ----------- | --- | ------------- | --- | --- | --- | --- | --- |
Forexample,thefollowingcommandsetsthehellodelayto4secondsontheVLAN40interface:
switch(config)#
|                         |     | interface |     | vlan40     |     |             |     |     |
| ----------------------- | --- | --------- | --- | ---------- | --- | ----------- | --- | --- |
| switch(config-if-vlan)# |     |           | ip  | pim-sparse |     | hello-delay |     | 4   |
ForIPv6configurations:
| ipv6 pim6-sparse |     | hello-delay |     | <DELAY-VALUE> |     |     |     |     |
| ---------------- | --- | ----------- | --- | ------------- | --- | --- | --- | --- |
Forexample,thefollowingcommandsetsthehellodelayto4secondsontheVLAN40interface:
| switch(config)#         |     | interface |      | vlan40      |     |             |     |     |
| ----------------------- | --- | --------- | ---- | ----------- | --- | ----------- | --- | --- |
| switch(config-if-vlan)# |     |           | ipv6 | pim6-sparse |     | hello-delay |     | 4   |
3. SpecifythepriorityvaluetouseontheinterfaceintheDesignatedRouter(DR)electionprocessusing
thefollowingcommand.
ForIPv4configurations:
| ip pim-sparse | dr-priority |     | <PRIORITY-VALUE> |     |     |     |     |     |
| ------------- | ----------- | --- | ---------------- | --- | --- | --- | --- | --- |
Forexample,thefollowingcommandsetstheDRpriorityto4444ontheVLAN40interface:
| switch(config)#         |     | interface |     | vlan40     |     |             |     |      |
| ----------------------- | --- | --------- | --- | ---------- | --- | ----------- | --- | ---- |
| switch(config-if-vlan)# |     |           | ip  | pim-sparse |     | dr-priority |     | 4444 |
ForIPv6configurations:
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 121

| ipv6 pim6-sparse | dr-priority | <PRIORITY-VALUE> |     |     |     |
| ---------------- | ----------- | ---------------- | --- | --- | --- |
Forexample,thefollowingcommandsetstheDRpriorityto4444ontheVLAN40interface:
| switch(config)#         | interface | vlan40 |             |             |      |
| ----------------------- | --------- | ------ | ----------- | ----------- | ---- |
| switch(config-if-vlan)# |           | ipv6   | pim6-sparse | dr-priority | 4444 |
4. EnabletheLANprunedelayoptionontheinterfaceusingthefollowingcommand.
ForIPv4configurations:
| ip pim-sparse | lan-prune-delay |     |     |     |     |
| ------------- | --------------- | --- | --- | --- | --- |
ForIPv6configurations:
| ipv6 pim6-sparse | lan-prune-delay |     |     |     |     |
| ---------------- | --------------- | --- | --- | --- | --- |
5. ConfigurethevalueinsertedintotheOverrideIntervalfieldofaLANPruneDelayoptiononthe
interfaceusingthefollowingcommand.
ForIPv4configurations:
| ip pim-sparse | override-interval |     | <INTERVAL-VALUE> |     |     |
| ------------- | ----------------- | --- | ---------------- | --- | --- |
Forexample,thefollowingcommandsetstheoverrideintervalvalueto4000msoninterface
VLAN40:
| switch(config)#         | interface | vlan40        |     |                   |      |
| ----------------------- | --------- | ------------- | --- | ----------------- | ---- |
| switch(config-if-vlan)# |           | ip pim-sparse |     | override-interval | 4000 |
ForIPv6configurations:
| ipv6 pim6-sparse | override-interval |     | <INTERVAL-VALUE> |     |     |
| ---------------- | ----------------- | --- | ---------------- | --- | --- |
Forexample,thefollowingcommandsetstheoverrideintervalvalueto4000msoninterface
VLAN40:
| switch(config)#         | interface | vlan40 |             |                   |      |
| ----------------------- | --------- | ------ | ----------- | ----------------- | ---- |
| switch(config-if-vlan)# |           | ipv6   | pim6-sparse | override-interval | 4000 |
6. ConfigurethepropagationdelayvalueinsertedintotheLANPruneDelayoptionontheinterface
usingthefollowingcommand.
ForIPv4configurations:
| ip pim-sparse | propagation-delay |     | <DELAY-VALUE> |     |     |
| ------------- | ----------------- | --- | ------------- | --- | --- |
Forexample,thefollowingcommandsetsthepropagationdelayvalueto400msoninterface
VLAN40:
| switch(config)#         | interface | vlan40        |     |                   |     |
| ----------------------- | --------- | ------------- | --- | ----------------- | --- |
| switch(config-if-vlan)# |           | ip pim-sparse |     | propagation-delay | 400 |
ForIPv6configurations:
| ipv6 pim6-sparse | propagation-delay |     | <DELAY-VALUE> |     |     |
| ---------------- | ----------------- | --- | ------------- | --- | --- |
Forexample,thefollowingcommandsetsthepropagationdelayvalueto400msoninterface
VLAN40:
ProtocolIndependentMulticast-SparseMode(V4andV6)|122

| switch(config)# | interface | vlan40 |     |     |
| --------------- | --------- | ------ | --- | --- |
switch(config-if-vlan)#
|     |     | ipv6 pim6-sparse | propagation-delay | 400 |
| --- | --- | ---------------- | ----------------- | --- |
7. ConfigurethesourceIPaddresstobeusedinPIMpacketstransmittedfromtheinterfaceusingthe
followingcommand.
ForIPv4configurations:
| ip pim-sparse | ip-addr {<IP-ADDR-VALUE> |     | | any} |     |
| ------------- | ------------------------ | --- | ------ | --- |
Forexample,thefollowingcommandspecifiestheIPv4address40.0.0.4:
| switch(config)#         | interface | vlan40        |                  |     |
| ----------------------- | --------- | ------------- | ---------------- | --- |
| switch(config-if-vlan)# |           | ip pim-sparse | ip-addr 40.0.0.4 |     |
ForIPv6configurations:
| ipv6 pim6-sparse | ipv6-addr | {<IPv6-ADDR-VALUE> | | any} |     |
| ---------------- | --------- | ------------------ | ------ | --- |
Forexample,thefollowingcommandspecifiestheIPv6address2001::02:
| switch(config)# | interface | vlan40 |     |     |
| --------------- | --------- | ------ | --- | --- |
switch(config-if-vlan)#
|             |             | ipv6 pim6-sparse | ipv6-addr | 2001::02 |
| ----------- | ----------- | ---------------- | --------- | -------- |
| Viewing PIM | information |                  |           |          |
Forsomecommands,youcanspecifyviewinginformationbyinterfaceorVRF.
Prerequisites
UsetheseshowcommandsfromtheOperator(>)orManager(#)context.
Procedure
1. TodisplayPIMinformationforanIPv4configuration,usethefollowingshowcommands.
| ToviewPIMrouterinformation,use:show |     |     | ip pim. |     |
| ----------------------------------- | --- | --- | ------- | --- |
n
n ToviewinformationaboutthePIMinterfacesconfiguredontherouter,use:show ip pim
interface.
ToviewinformationaboutaPIMinterface,use:show ip pim interface <INTERFACE-NAME>.
n
n ToviewPIMpacketcounterinformationforaninterface,use:show ip pim interface
| <INTERFACE-NAME>                      | counters. |     |                  |     |
| ------------------------------------- | --------- | --- | ---------------- | --- |
| ToviewPIMneighborinformation,use:show |           |     | ip pim neighbor. |     |
n
| n ToviewRPinformation,use:show |     | ip  | pim rp-set. |     |
| ------------------------------ | --- | --- | ----------- | --- |
n ToviewinformationforstaticallyconfiguredRPassignments,use:show ip pim rp-set static.
n ToviewinformationfordynamicallylearnedRPassignments,use:show ip pim rp-set learned.
| n ToviewcandidateRPinformation,use:show |     |     | ip pim rp-candidate. |     |
| --------------------------------------- | --- | --- | -------------------- | --- |
ToviewinformationaboutBSRcandidatesinthedomain,use:show ip pim bsr.
n
ToviewinformationaboutBSRcandidatesonthelocalrouter,use:show ip pim bsr local.
n
ToviewinformationabouttheelectedBSRinthedomain,use:show elected.
| n   |     |     |     | ip pim bsr |
| --- | --- | --- | --- | ---------- |
n ToviewtheRPFoverrideconfiguration,use:show ip pim rpf-override.
n ToviewRPFoverrideconfigurationforasource,use:show ip pim rpf-override source.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 123

|     |     | ToviewpendingjoinsonaPIMrouter,use:show |     |     |     |     |        | pending. |
| --- | --- | --------------------------------------- | --- | --- | --- | --- | ------ | -------- |
|     | n   |                                         |     |     |     |     | ip pim |          |
n Toviewmulticastroutinginformation,use:show ip mrouteoruseshow ip mroute brief.
n Toviewmulticastroutinginformationforagroupaddress,use:show ip mroute <GROUP-ADDR>.
2. TodisplayPIMinformationforanIPv6configuration,usethefollowingshowcommands.
|     | n   | ToviewPIMrouterinformation,use:show |     |     |     | ipv6 | pim6. |     |
| --- | --- | ----------------------------------- | --- | --- | --- | ---- | ----- | --- |
ToviewinformationaboutthePIMinterfacesconfiguredontherouter,use:show ipv6 pim6
n
interface.
n ToviewinformationaboutaPIMinterface,use:show ipv6 pimv6 interface <INTERFACE-NAME>.
|     |     | ToviewPIMneighborinformation,use:show |     |     |     | ipv6 | pim6 | neighbor. |
| --- | --- | ------------------------------------- | --- | --- | --- | ---- | ---- | --------- |
n
|     |     | ToviewRPinformation,use:show |     |     | ipv6 | pim6 rp-set. |     |     |
| --- | --- | ---------------------------- | --- | --- | ---- | ------------ | --- | --- |
n
n ToviewinformationforstaticallyconfiguredRPassignments,use:show ipv6 pim6 rp-set
static.
ToviewinformationfordynamicallylearnedRPassignments,use:show ipv6 pim6 rp-set
n
learned.
|     |     | ToviewcandidateRPinformation,use:show |     |     |     | ipv6 | pim6 | rp-candidate. |
| --- | --- | ------------------------------------- | --- | --- | --- | ---- | ---- | ------------- |
n
ToviewinformationaboutBSRcandidatesinthedomain,use:show ipv6 pim6 bsr.
n
n ToviewinformationaboutBSRcandidatesonthelocalrouter,use:show ipv6 pim6 bsr local.
n ToviewinformationabouttheelectedBSRinthedomain,use:show ipv6 pim6 bsr elected.
n ToviewtheRPFoverrideconfiguration,use:show ipv6 pim6 rpf-override.
n ToviewRPFoverrideconfigurationforasource,use:show ipv6 pim6 rpf-override source.
|     |     | ToviewpendingjoinsonaPIMrouter,use:show |     |     |     |     | ipv6 pim6 | pending. |
| --- | --- | --------------------------------------- | --- | --- | --- | --- | --------- | -------- |
n
Toviewmulticastroutinginformation,use:show ipv6 mrouteoruseshow ipv6 mroute brief.
n
Toviewmulticastroutinginformationforagroupaddress,use:show <GROUP-ADDR>.
|        | n   |     |               |         |     |     |     | ipv6 mroute |
| ------ | --- | --- | ------------- | ------- | --- | --- | --- | ----------- |
| PIM-SM |     |     | configuration | example |     |     |     |             |
ThefollowingisasampletopologydiagramforaPIM-SMconfiguration.
|     | Multicast |            | +-----------+ |                      |     |       | +-----------+ |                 |
| --- | --------- | ---------- | ------------- | -------------------- | --- | ----- | ------------- | --------------- |
|     | Source    |            | |             | |1/1/1               |     | 1/1/1 |               | |1/1/2          |
|     |           |            | 1/1/2 Router1 | +------------------+ |     |       | Router2       | +-------------+ |
|     |           | +--------| |               | |CBSR                |     |       | |             | | IGMP          |
|     |           |            | |             | |CRP                 |     |       | |             | | Clients       |
|     |           |            | +-----------+ |                      |     |       | +-----------+ |                 |
Inthistopology,themulticastsourceisconnectedtoRouter1andClientsareconnectedtoRouter2.
Router1andRouter2aredirectlyconnectedsoyoucanverifytheneighborshipusingtheshow ip pim
neighbor
command.
SecondlyRouter1interface1/1/1istheBSRcandidateandRPcandidateinthisdomain.Thisinformation
needstobepropagatedacrossthenetworkandneedstobeconsistentonallroutersinthetopology.To
verifythis,usetheshow ip pim rp-setcommandforgroupmappinginformationandtheshow ip pim
bsrcommandforelectedBSRinformation.Iftheyshowinconsistentinformation,youcouldseepossible
multicastoutages.
ProtocolIndependentMulticast-SparseMode(V4andV6)|124

Ifthejoinsareseenbytheroutersbeforethestreamscanflow,bothrouteswilldisplaythoserequestsin
theshow ip pim pendingcommandoutput.
Oncethemulticastsourcestreamsstarttoflow,eachrouterinthepathwilladdmulticastrouter(mroute)
entries,whichcanbeverifiedusingtheshow ip mroutecommand.
Theoutputofthefollowingshow running-configcommandshowsanexampleofPIM-SMconfiguration
forIPv4.
| switch# show running-config |     |     |
| --------------------------- | --- | --- |
Current configuration:
!
!
!
!
!
Router1
---------------
| router ospf 1 |           |     |
| ------------- | --------- | --- |
| redistribute  | connected |     |
area 0.0.0.0
router pim
enable
| bsr-candidate | source-ip-interface | 1/1/1       |
| ------------- | ------------------- | ----------- |
| rp-candidate  | source-ip-interface | 1/1/1       |
| rp-candidate  | group-prefix        | 224.0.0.0/4 |
interface 1/1/1
| ip address    | 10.10.10.1/24 |     |
| ------------- | ------------- | --- |
| ip ospf 1     | area 0.0.0.0  |     |
| ip pim-sparse | enable        |     |
interface 1/1/2
| ip address    | 20.20.20.1/24 |     |
| ------------- | ------------- | --- |
| ip pim-sparse | enable        |     |
Router2
---------------
| router ospf 1 |           |     |
| ------------- | --------- | --- |
| redistribute  | connected |     |
area 0.0.0.0
router pim
enable
interface 1/1/1
| ip address    | 10.10.10.2/24 |     |
| ------------- | ------------- | --- |
| ip ospf 1     | area 0.0.0.0  |     |
| ip pim-sparse | enable        |     |
interface 1/1/2
| ip address     | 30.30.30.1/24 |     |
| -------------- | ------------- | --- |
| ip pim-sparse  | enable        |     |
| ip igmp enable |               |     |
Theoutputofthefollowingshow running-configcommandshowsanexampleofPIM-SMconfiguration
forIPv6.
| switch# show running-config |     |     |
| --------------------------- | --- | --- |
Current configuration:
!
!
!
!
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 125

!
Router1
---------------
| router        | ospfv3  | 1                   |          |           |
| ------------- | ------- | ------------------- | -------- | --------- |
| redistribute  |         | connected           |          |           |
| area          | 0.0.0.0 |                     |          |           |
| router        | pim6    |                     |          |           |
| bsr-candidate |         | source-ip-interface |          | loopback1 |
| rp-candidate  |         | source-ip-interface |          | loopback1 |
| rp-candidate  |         | group-prefix        | ff00::/8 |           |
enable
| interface | loopback    | 1              |     |     |
| --------- | ----------- | -------------- | --- | --- |
| ipv6      | address     | 1000::1000/64  |     |     |
| ipv6      | ospfv3      | 1 area 0.0.0.0 |     |     |
| ipv6      | pim6-sparse | enable         |     |     |
| interface | 1/1/1       |                |     |     |
| ipv6      | address     | 2000::1/64     |     |     |
| ipv6      | ospfv3      | 1 area 0.0.0.0 |     |     |
| ipv6      | pim6-sparse | enable         |     |     |
| interface | 1/1/2       |                |     |     |
| ipv6      | address     | 4000::1/64     |     |     |
| ipv6      | pim6-sparse | enable         |     |     |
Router2
---------------
| router       | ospfv3  | 1         |     |     |
| ------------ | ------- | --------- | --- | --- |
| redistribute |         | connected |     |     |
| area         | 0.0.0.0 |           |     |     |
| router       | pim6    |           |     |     |
enable
| interface | 1/1/1         |                |     |           |
| --------- | ------------- | -------------- | --- | --------- |
| ipv6      | address       | 2000::2/64     |     |           |
| ipv6      | ospfv3        | 1 area 0.0.0.0 |     |           |
| ipv6      | pim6-sparse   | enable         |     |           |
| interface | 1/1/2         |                |     |           |
| ipv6      | address       | 5000::1/64     |     |           |
| ipv6      | pim-sparse    | enable         |     |           |
| ipv6      | mld enable    |                |     |           |
| PIM-SM    | configuration |                |     | task list |
Tasksataglance.
n EnablingordisablingPIMglobally
n Configuringjoin/pruneinterval
n Enabling/disablingmulticasttraffictoSPT
n ConfiguringanRP
ConfiguringaBSR
n
ConfiguringRPFoverride
n
Enabling/disablingPIM-SMinaninterface
n
ProtocolIndependentMulticast-SparseMode(V4andV6)|126

ConfiguringPIM-SMoptionsinaninterface
n
RemovingallPIM-SMrelatedconfigurationsonaninterface
n
ViewingPIMinformation
n
n PIMgracefulshutdown
| Enabling | or disabling | PIM globally |
| -------- | ------------ | ------------ |
Prerequisites
YoumustbeinthePIMconfigurationcontext,asindicatedbytheswitch(config-pim)#promptforIPv4or
theswitch(config-pim6)#promptforIPv6.
Procedure
EnablePIMgloballyonarouterusingthefollowingcommand.
enable
Forexample,thefollowingcommandenablesPIMglobally:
ForIPv4configurations:
| switch#             | configure terminal |     |
| ------------------- | ------------------ | --- |
| switch(config)#     | router             | pim |
| switch(config-pim)# | enable             |     |
ForIPv6configurations:
| switch#              | configure terminal |      |
| -------------------- | ------------------ | ---- |
| switch(config)#      | router             | pim6 |
| switch(config-pim6)# | enable             |      |
YoucanenablePIMgloballyandenablePIM-SMattheinterfacelevel.WhenPIM-SMisnotenabledonthe
interface,irrespectiveoftheglobalPIMstatus,unknownmulticasttrafficdoesnotgetrouted.WhenPIM-
SMisenabledontheinterface,multicasttrafficisroutedtotheinterfacewherethereareclientsjoined,
providedPIMisenabledglobally.
UsethedisablecommandtodisablePIMgloballyonarouter.Youcouldusethiscommandtotemporarily
disablePIMgloballywithoutremovingtheindividualinterfaceconfiguration.
| Configuring | join/prune | interval |
| ----------- | ---------- | -------- |
ConfiguretheintervalatwhichtherouterwillsendperiodicPIM-SMjoinorpruneintervalmessages.
Prerequisites
YoumustbeinthePIMconfigurationcontext,asindicatedbytheswitch(config-pim)#promptforIPv4or
theswitch(config-pim6)#promptforIPv6.
Procedure
Configurethejoin/pruneintervalusingthefollowingcommand.
join-prune-interval <INTERVAL-VALUE>
Forexample,thefollowingcommandsetsthejoin/pruneintervalto400seconds:
ForIPv4configurations:
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 127

| switch# configure | terminal |     |     |
| ----------------- | -------- | --- | --- |
switch(config)#
router pim
| switch(config-pim)# | join-prune-interval | 400 |     |
| ------------------- | ------------------- | --- | --- |
ForIPv6configurations:
| switch# configure      | terminal            |     |     |
| ---------------------- | ------------------- | --- | --- |
| switch(config)# router | pim6                |     |     |
| switch(config-pim6)#   | join-prune-interval | 400 |     |
Thenoformofthecommandsetstheintervaltothedefaultof60seconds.
| Enabling/disabling | multicast | traffic | to SPT |
| ------------------ | --------- | ------- | ------ |
SwitchingtoSPTisenabledbydefault.
Prerequisites
YoumustbeinthePIMconfigurationcontext,asindicatedbytheswitch(config-pim)#promptforIPv4or
theswitch(config-pim6)#promptforIPv6.
Procedure
Enableordisabletherouter'sabilitytoswitchmulticasttrafficflowstotheShortestPathTree(SPT)using
thefollowingcommand.
spt-threshold
Forexample,thefollowingcommandenablesswitchingtrafficflowstotheSPT:
ForIPv4configurations:
| switch(config)# router | pim           |     |     |
| ---------------------- | ------------- | --- | --- |
| switch(config-pim)#    | spt-threshold |     |     |
ForIPv6configurations:
| switch(config)# router | pim6          |     |     |
| ---------------------- | ------------- | --- | --- |
| switch(config-pim6)#   | spt-threshold |     |     |
ThenoformofthecommanddisablesswitchingtoSPT.
| Configuring an | RP  |     |     |
| -------------- | --- | --- | --- |
AnRPcanbemanuallyconfigured(staticRP)ordynamicallyelectedthroughtheBootstrapRouter(BSR)
mechanism(CandidateRPorC-RP).
Prerequisites
YoumustbeinthePIMconfigurationcontext,asindicatedbytheswitch(config-pim)#promptforIPv4or
theswitch(config-pim6)#promptforIPv6.
ARendezvousPoint(RP)canprovideservicesformultipleorallmulticastgroups.However,onlyoneRP
n
canforwardmulticasttrafficforamulticastgroupatatime.
ProtocolIndependentMulticast-SparseMode(V4andV6)|128

Foralarge-scaledPIMnetwork,configuringstaticRPsisatediousjob.Generally,staticRPsarebackups
n
fordynamicRPstoenhancetherobustnessandoperationalmanageabilityonamulticastnetwork.
n WhenconfiguringastaticRP,youmustconfigurethesamestaticRPonallroutersinthePIM-SMdomain.
WhenyouconfigureaCandidateRP(C-RP),reservearelativelylargebandwidthbetweentheC-RPand
n
otherdevicesinthePIM-SMdomain.
Procedure
1. ConfigureastaticRPusingthefollowingcommand.
| rp-address | <IP-ADDR> | [<GRP-ADDR/GRP-MASK>] | [override] |
| ---------- | --------- | --------------------- | ---------- |
Forexample,thefollowingcommandconfiguresastaticRPof40.0.0.8forthemulticastgroup:
ForIPv4configurations:
| switch(config)# |     | router pim |     |
| --------------- | --- | ---------- | --- |
switch(config-pim)#
|     |     | rp-address | 40.0.0.8 226.0.0.4/24 |
| --- | --- | ---------- | --------------------- |
ForIPv6configurations:
| switch(config)#      |     | router pim6 |                       |
| -------------------- | --- | ----------- | --------------------- |
| switch(config-pim6)# |     | rp-address  | 2002::02 ff08::1:4/64 |
2. ConfigureaC-RPusingthefollowingcommand.
rp-candidate source-ip-interface <INTERFACE-NAME> [group-prefix <GRP-ADDR/GRP-MASK>]
Forexample,thefollowingcommandconfiguresaC-RPusingloopback1asthesourcefortheC-RP
routerIPaddressandassociatesthemulticastgroupwiththeC-RProuter:
ForIPv4configurations:
| switch(config)# |     | router pim |     |
| --------------- | --- | ---------- | --- |
switch(config-pim)# rp-candidate source-ip-interface loopback1 group-prefix
230.0.0.4/24
ForIPv6configurations:
| switch(config)# |     | router pim6 |     |
| --------------- | --- | ----------- | --- |
switch(config-pim6)# rp-candidate source-ip-interface loopback1 group-prefix
ff08::1:3/64
ForaC-RP,youcanconfigurevariousoptionsasshowninthefollowingsteps.C-RPcanbeconfigured
onanSVIorROPinterfacealso.
3. AddorremovemulticastgroupsfortheC-RP,asneeded,usingthefollowingcommand.
| rp-candidate | group-prefix | <GRP-ADDR/GRP-MASK> |     |
| ------------ | ------------ | ------------------- | --- |
Forexample,thefollowingcommandsconfigureaC-RPusingVLAN40asthesourcefortheC-RP
routerIPaddressandthenaddsthemulticastgrouptotheC-RP:
ForIPv4configurations:
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 129

| switch(config)# |     | router pim |     |     |     |
| --------------- | --- | ---------- | --- | --- | --- |
switch(config-pim)#
|                     |     | rp-candidate | source-ip-interface |              | vlan40 |
| ------------------- | --- | ------------ | ------------------- | ------------ | ------ |
| switch(config-pim)# |     | rp-candidate | group-prefix        | 230.0.0.4/24 |        |
ForIPv6configurations:
| switch(config)#      |     | router pim6  |                     |              |        |
| -------------------- | --- | ------------ | ------------------- | ------------ | ------ |
| switch(config-pim6)# |     | rp-candidate | source-ip-interface |              | vlan40 |
| switch(config-pim6)# |     | rp-candidate | group-prefix        | ff08::1:3/64 |        |
4. Configurethehold-timeaC-RPincludesinitsadvertisementstotheBSRusingthefollowing
command.
| rp-candidate | hold-time | <TIME-VALUE> |     |     |     |
| ------------ | --------- | ------------ | --- | --- | --- |
Forexample,thefollowingcommandsetsthehold-timeto250seconds:
ForIPv4configurations:
| switch(config)#     |     | router pim   |           |     |     |
| ------------------- | --- | ------------ | --------- | --- | --- |
| switch(config-pim)# |     | rp-candidate | hold-time | 250 |     |
ForIPv6configurations:
| switch(config)#      |     | router pim6  |           |     |     |
| -------------------- | --- | ------------ | --------- | --- | --- |
| switch(config-pim6)# |     | rp-candidate | hold-time | 250 |     |
5. SetthepriorityforaC-RPusingthefollowingcommand.
| rp-candidate | priority | <PRIORITY-VALUE> |     |     |     |
| ------------ | -------- | ---------------- | --- | --- | --- |
Forexample,thefollowingcommandsetsthepriorityto250:
ForIPv4configurations:
| switch(config)#     |     | router pim   |          |     |     |
| ------------------- | --- | ------------ | -------- | --- | --- |
| switch(config-pim)# |     | rp-candidate | priority | 250 |     |
ForIPv6configurations:
| switch(config)#      |       | router pim6  |          |     |     |
| -------------------- | ----- | ------------ | -------- | --- | --- |
| switch(config-pim6)# |       | rp-candidate | priority | 250 |     |
| Configuring          | a BSR |              |          |     |     |
ConfiguretheroutertoadvertiseitselfastheCandidateBootstrapRouter(Candidate-BSR)forthePIM-SM
domain.
Prerequisites
YoumustbeinthePIMconfigurationcontext,asindicatedbytheswitch(config-pim)#promptforIPv4or
theswitch(config-pim6)#promptforIPv6.
PIM-SMmustbeenabledontheinterfaceusedasthesourceIPinterface.
Procedure
ProtocolIndependentMulticast-SparseMode(V4andV6)|130

1. ConfigureaCandidate-BSRusingthefollowingcommand.
| bsr-candidate | source-ip-interface |     | <INTERFACE-NAME> |     |     |
| ------------- | ------------------- | --- | ---------------- | --- | --- |
Forexample,thefollowingcommandconfiguresaCandidate-BSRusinginterface1/1/4asthesource
fortherouterIPaddress.ThiscommandcanalsobeappliedtoanL3VLANorL3LAG.
ForIPv4configurations:
| switch(config)#     | router | pim           |                     |     |       |
| ------------------- | ------ | ------------- | ------------------- | --- | ----- |
| switch(config-pim)# |        | bsr-candidate | source-ip-interface |     | 1/1/4 |
ForIPv6configurations:
| switch(config)#      | router | pim6          |                     |     |       |
| -------------------- | ------ | ------------- | ------------------- | --- | ----- |
| switch(config-pim6)# |        | bsr-candidate | source-ip-interface |     | 1/1/4 |
Candidate-BSRcanbeenabledonaloopbackinterfaceaswell.ForaCandidate-BSR,youcan
configurevariousoptionsasshowninthefollowingsteps.
2. Configurethebootstrapmessage(BSM)intervalforsendingperiodicRP-Setmessagesusingthe
followingcommand.
| bsr-candidate | bsm-interval | <INTERVAL-VALUE> |     |     |     |
| ------------- | ------------ | ---------------- | --- | --- | --- |
Forexample,thefollowingcommandconfiguresabootstrapmessageintervalof150seconds:
ForIPv4configurations:
| switch(config)#     | router | pim           |              |     |     |
| ------------------- | ------ | ------------- | ------------ | --- | --- |
| switch(config-pim)# |        | bsr-candidate | bsm-interval | 150 |     |
ForIPv6configurations:
| switch(config)#      | router | pim6          |              |     |     |
| -------------------- | ------ | ------------- | ------------ | --- | --- |
| switch(config-pim6)# |        | bsr-candidate | bsm-interval | 150 |     |
3. SettheprioritytoapplytotherouterwhenaBSRelectionprocessoccursinthePIM-SMdomain
usingthefollowingcommand.
| bsr-candidate | priority | <PRIORITY-VALUE> |     |     |     |
| ------------- | -------- | ---------------- | --- | --- | --- |
Forexample,thefollowingcommandconfiguresthepriorityas250:
ForIPv4configurations:
| switch(config)#     | router | pim           |              |     |     |
| ------------------- | ------ | ------------- | ------------ | --- | --- |
| switch(config-pim)# |        | bsr-candidate | priority 250 |     |     |
ForIPv6configurations:
| switch(config)#      | router | pim6          |          |     |     |
| -------------------- | ------ | ------------- | -------- | --- | --- |
| switch(config-pim6)# |        | bsr-candidate | priority | 250 |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 131

4. Configurethelength(inbits)ofthehash-maskusingthefollowingcommand.Usedtocontrolthe
distributionofmulticastgroupsamongtheC-RPinadomainwherethereisoverlappingcoverageof
thegroupsamongtheRPs.
|     | bsr-candidate |     | hash-mask-length |     |     | <LENGTH-VALUE> |     |     |     |
| --- | ------------- | --- | ---------------- | --- | --- | -------------- | --- | --- | --- |
Forexample,thefollowingcommandconfiguresthehash-masklengthto4:
ForIPv4configurations:
switch(config)#
|             |                      |      |                 | router   | pim           |     |                  |     |     |
| ----------- | -------------------- | ---- | --------------- | -------- | ------------- | --- | ---------------- | --- | --- |
|             | switch(config-pim)#  |      |                 |          | bsr-candidate |     | hash-mask-length |     | 4   |
|             | For                  | IPv6 | configurations: |          |               |     |                  |     |     |
|             | switch(config)#      |      |                 | router   | pim6          |     |                  |     |     |
|             | switch(config-pim6)# |      |                 |          | bsr-candidate |     | hash-mask-length |     | 4   |
| Configuring |                      |      | RPF             | override |               |     |                  |     |     |
ConfigureReversePathForward(RPF)overridetoallowtheoverrideofthenormalRPFlookupmechanism,
indicatingtotherouterthatitmayacceptmulticasttrafficonaninterfaceotherthantheonethatwould
normallybeselectedbytheRPFlookupmechanism.
RPFcheckingensuresthatmulticasttrafficreceivedarrivedontheexpectedrouterinterfacebeforeitis
consideredforfurtherprocessing.IftheRPFcheckfailsforamulticastpacket,thepacketisdiscarded.
RPFoverrideentrygetsprecedenceoverrouteslearnedfromroutingprotocolsorstaticroutes.Itmustalso
benotedthatPIMwillnotswitchtoanalternatepathiftheconfiguredRPFneighborisnotreachable.
Prerequisites
YoumustbeinthePIMconfigurationcontext,asindicatedbytheswitch(config-pim)#promptforIPv4or
theswitch(config-pim6)#promptforIPv6.
Procedure
Add,edit,ordeleteRPFoverridesusingthefollowingcommand.
| rpf-override |     | <SRC-ADDR/SRC-MASK><RPF-ADDR|INTERFACE-NAME> |     |     |     |     |     |     |     |
| ------------ | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ForIPv4configurations:
|     | switch(config)#     |     | router |              | pim |             |     |          |     |
| --- | ------------------- | --- | ------ | ------------ | --- | ----------- | --- | -------- | --- |
|     | switch(config-pim)# |     |        | rpf-override |     | 40.0.0.4/24 |     | 30.0.0.4 |     |
ForIPv6configurations:
|          | switch(config)#      |     | router |              | pim6    |                |     |       |                 |
| -------- | -------------------- | --- | ------ | ------------ | ------- | -------------- | --- | ----- | --------------- |
|          | switch(config-pim6)# |     |        | rpf-override |         | 50::4/24       |     | 40::1 |                 |
| Removing |                      | all | PIM-SM |              | related | configurations |     |       | on an interface |
Prerequisites
Youmustbeintheinterfaceconfigurationcontext,asindicatedbytheswitch(config-if)#prompt,
switch(config-if-vlan)#prompt,orswitch(config-lag-if)#prompt.
ProtocolIndependentMulticast-SparseMode(V4andV6)|132

Procedure

Remove all PIM-SM related configurations for the interface using the following command.

For IPv4 configurations:

no ip pim-sparse

For IPv6 configurations:

no ipv6 pim6-sparse

PIM graceful shutdown

The PIM active-active solution makes one of the VSX device act as DR and other device as proxy-DR for each
of the downstream VLANs. Both the VSX peers behave the same as far as the protocol is concerned with
only the DR forwarding the multicast traffic to downstream routers. The PIM active-active feature is enabled
on VSX devices connected to access switches on one side with hosts behind the access switches. The DR
election depends on the IP address and a single VSX device doesn't be the DR for all of the downstream
VLANs.

When a VSX device which is acting as DR for some of the downstream VLANs starts rebooting, traffic loss
would be seen for the multicast streams in those downstream VLANs for few seconds. The VSX software
upgrade process involves rebooting each VSX device with new software. The secondary VSX device is
upgraded before primary VSX device. If the secondary is acting as DR for some of downstream VLANs then
after the VSX software upgrade is triggered multicast traffic loss will be seen twice for the streams present in
those VLANs; once during secondary VSX device reboot and then during primary VSX device reboot.

With graceful shutdown traffic loss won't be seen for any of multicast streams. Instead, some duplicates are
expected for 1-3 seconds for each stream.

The sequence of events during each VSX device upgrade is outlined below:

1. The first step is based on device role and is applicable only to the primary device. According to VSX
software upgrade process, the device upgrade is triggered in the primary after the secondary
upgrade. The secondary should already have all the multicast routes before taking over the DR role
from the primary. After the secondary device reboots the primary device waits for few minutes so
that the secondary learns the multicast routes and is ready to take over the DR role. The wait time in
primary device depends on the number of multicast routes present.

2. DR roles of all the downstream VLANs are offloaded to its peer. At the end of this step the device

which is going to reboot will be a proxy-DR for all the downstream VLANs.

3. After the interface role change, each multicast flow in the hardware is changed simultaneously in both
the DR and proxy-DR based on the new roles they have taken. The new DR converts bridge entries to
route entries and the proxy-DR converts route entries to bridge entries in the hardware.

The wait times for the primary upgrade before multicast graceful shutdown process starts are listed below:

Number of MRoutes

Timer value

0

< 1024

< 2048

< 4096

< 8192

0

120 seconds

150 seconds

210 seconds

300 seconds

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

133

| NumberofMRoutes |     |     |     | Timervalue |
| --------------- | --- | --- | --- | ---------- |
| <16284          |     |     |     | 360seconds |
| >16384          |     |     |     | 480seconds |
Therecommendedconfigurationsforgracefulshutdownareasfollows:
1. ThemulticastgracefulshutdownisapplicableonlytothetopologieswhicharesupportedforthePIM
active-activesolution.OthertopologieswillexperiencemulticasttrafficlossduringaVSXsoftware
upgrade.
2. TherobustnesstimerforIGMP/MLDprotocolshouldbeincreased.Therobustnesstimerhelpsto
increasetheexpirationtimeofIGMP/MLDjoins.ThisisneededduringVSXdevicerebootsothatjoins
don'texpire.TheconfiguredvaluedependsonhowmuchtimetheVSXdevicereboottakes.Ifthe
robustnessvalueisconfiguredatthemaximumvalueof8,thentheexpirationtimeofmulticastjoins
canincreaseupto16minuteswithdefaultquery-interval.Usethebelowcommandtoconfigure
robustnesstimer:
|     | switch(config-if)#ip |     | igmp robustness | <2-8> |
| --- | -------------------- | --- | --------------- | ----- |
3. IfOSPFv2/v3isenabled,itisrecommendednottoconfiguretheVSXdeviceasOSPFv2/v3DRfor
anyoftheinterfaces.UsefollowingcommandstoconfiguretheotherroutersasDRforaninterface:
|     | ip ospf priority | <0-255>  |         |     |
| --- | ---------------- | -------- | ------- | --- |
|     | ipv6 ospfv3      | priority | <0-255> |     |
4. IfBGPisenabled,itisrecommendedtoincreaseBGPgracefulrestarttimerforeveryBGP-enabled
interface.TherecommendedvalueofBGPgracefulrestarttimershouldbethesameasthewaittime
intheprimarybeforethemulticastgracefulshutdownprocessstarts.Refertothetableinprevious
sectionwhichmentionsthewaittimes.UsefollowingcommandtoreconfiguretheBGPgraceful
restarttimer:
|                 | bgp graceful | restart     | restart-time | <1-3600> |
| --------------- | ------------ | ----------- | ------------ | -------- |
| PIM-SM          | commands     |             | for IPv4     |          |
| accept-register |              | access-list |              |          |
Syntax
| accept-register    |     | access-list | <ACL-RULE> |     |
| ------------------ | --- | ----------- | ---------- | --- |
| no accept-register |     | access-list | <ACL-RULE> |     |
Description
ConfiguresACLonRPtofilterPIMRegisterpacketsfromunauthorizedsources.TheACLspecifiedwill
containthe(S,G)trafficinregisterpacketstopermittedordenied.
ThenoformofthiscommandremovesthecurrentlyconfiguredACLrule.
Commandcontext
config-pim
Parameters
<ACL-RULE>
ProtocolIndependentMulticast-SparseMode(V4andV6)|134

Specifies the ACL rule name.

Authority

Administrators or local user group members with execution rights for this command.

Usage

When register ACL is associated with a PIM Router, PIM protocol will store the source and destination
address details along with the action (permit or deny). If there are any existing flows, the user will need to
disable and enable PIM on the interface to apply the ACL.

Upon receiving the register messages, a look up is made to check if the S and G in the packet is in the
permitted list. If there is no match or if there is a deny rule match, a register stop message is immediately
sent and the packet is dropped and no further action is taken. Permitted packets will go through the normal
flow.

Loopback interfaces are special interfaces where only unicast PIM messages are updated. This includes
Register, Register Stop, and Candidate RP Advertisements.

When a loopback interface is configured as the RP, the ACL drop counters will be updated on the interface
on which the packets are received.

Examples

Configuring ACL on RP with an ACL rule named pim_reg_acl:

switch(config)# access-list ip pim_reg_acl
switch(config-acl-ip)# 10 permit any 20.1.1.1 225.1.1.2
switch(config-acl-ip)# 20 deny any 30.1.1.1 225.1.1.3
switch(config)# router pim
switch(config-pim)# accept-register access-list pim_reg_acl

accept-rp

Syntax

accept-rp <IP-ADDR> access-list <ACL-RULE>
no accept-rp <IP-ADDR> access-list <ACL-RULE>

Description

Enables PIM router to filter PIM join/prune messages destined for a specific RP and specific groups. The ACL
specifies the group addresses which are allowed or denied. Up to 8 RP addresses and group ACL can be
associated with the PIM router.

The no form of this command removes the currently configured ACL rule.

Command context

config-pim

Parameters

<IP-ADDR>

Specifies the IPv4 address of the static RP. Format: A.B.C.D

<ACL-RULE>

Specifies the ACL rule name.

Authority

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

135

Administrators or local user group members with execution rights for this command.

Usage

PIM will store the accepted RP address and the associated group ACL. When a join or prune message is
received, a RP look up is made for the packet. If the RP is in the configured list and if the group in the
join/prune packet is allowed in the ACL, the packet is allowed. Otherwise the packet is dropped.

To allow join/prune message from any groups, group address in the ACL can be wild-carded. In this case,
only RP address check is performed.

This command impacts only (*,G) join/prune messages. If there are any existing flows, the user will need to
disable and enable PIM on the interface to apply the ACL.

Loopback interfaces are special interfaces where only unicast PIM messages are updated. This includes
Register, Register Stop, and Candidate RP Advertisements.

When a loopback interface is configured as the RP, the ACL drop counters will be updated on the interface
on which the packets are received.

If there is an active flow which is in the SPT, the traffic flow through the SPT will continue. Only (*,G) join/prune

messages are dropped. (S,G) join/prune messages will not be impacted.

Examples

Configuring ACL on a RP with an ACL rule named pim_rp_grp_acl to filter join/prune messages:

switch(config)# access-list ip pim_rp_grp_acl
switch(config-acl-ip)# 10 permit any any 225.1.1.2/255.255.255.0
switch(config-acl-ip)# 20 permit any any 239.1.1.2/255.255.255.0
switch(config)-acl-ip# router pim
switch(config-pim)# accept-rp 30.1.1.1 access-list pim_rp_grp_acl

active-active

Syntax

active-active
no active-active

Description

Enables the PIM active-active mechanism per VRF on VSX. The default is disabled.

The no form of this command disables the PIM active-active mechanism.

Command context

config-pim

Authority

Administrators or local user group members with execution rights for this command.

Usage

PIM active-active keeps the multicast forwarding state synchronized on both VSX peer devices.
Synchronization is achieved by electing the VSX peer that has the highest IP address as a designated router
(DR) and the other as Proxy-DR.

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 136

If you want the multicast traffic to flow through VSX primary, assign higher IP addresses to the interfaces in
VSX primary. When the VSX peer that is acting as the DR goes down, traffic is recovered faster since the
multicast routes are synchronized.
Recommendations:

n Do not configure the DR priority of interfaces when active-active is enabled. The DR priority will be set

to high on DR and default on Proxy-DR and any user-configured DR priority will be ignored.

n Always configure keepalive between VSX peers. If the ISL goes down when keepalive is not configured,

both VSX peers start acting independently as DRs, resulting in duplicate traffic.

n Do not configure IGMP joins on transit VLANS.

n RP redundancy is not supported on the active-active mechanism. If one of the VSX peers is configured
as RP and it goes down, the new traffic flows will not be converged until the RP is elected. For a static RP,
new flows will never be converged until the VSX peer is back up.

Examples

Enabling the PIM active-active mechanism:

switch(config)# router pim
switch(config-pim)# active-active

Disabling the PIM active-active mechanism:

switch(config)# router pim
switch(config-pim)# no active-active

bfd all-interfaces

Syntax

bfd all-interfaces
no bfd all-interfaces

Description

Enables BFD on all PIM interfaces. BFD can be disabled at individual PIM interface using the ip pim-sparse
bfd disable command.

The no form of this command disables BFD for all the interfaces.

Command context

config-pim

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling and disabling BFD on all PIM interfaces:

switch(config)# router pim
switch(config-pim)# bfd all-interfaces
switch(config-pim)# no bfd all-interfaces

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

137

| bsr-candidate | bsm-interval |     |     |     |
| ------------- | ------------ | --- | --- | --- |
Syntax
| bsr-candidate    | bsm-interval | <INTERVAL-VALUE> |     |     |
| ---------------- | ------------ | ---------------- | --- | --- |
| no bsr-candidate | bsm-interval |                  |     |     |
Description
ConfigurestheintervalinsecondstosendperiodicRP-SetmessagestoallPIM-SMinterfacesonarouter
thatoperatesastheBSRinadomain.Thissettingmustbesmallerthantherp-candidate hold-time
settings(rangeof30to255;default150)configuredintheRPsoperatinginthedomain.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetsittothedefaultof60
seconds.
Commandcontext
config-pim
Parameters
<INTERVAL-VALUE>
SpecifiestheBSR-candidateBSMintervalinseconds.Default:60seconds.Range:5-300.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ConfiguringandremovingBSR-candidateBSM-interval:
| switch(config)#     | router           | pim              |              |     |
| ------------------- | ---------------- | ---------------- | ------------ | --- |
| switch(config-pim)# |                  | bsr-candidate    | bsm-interval | 150 |
| switch(config-pim)# |                  | no bsr-candidate | bsm-interval |     |
| bsr-candidate       | hash-mask-length |                  |              |     |
Syntax
| bsr-candidate    | hash-mask-length | <LENGTH-VALUE> |     |     |
| ---------------- | ---------------- | -------------- | --- | --- |
| no bsr-candidate | hash-mask-length |                |     |     |
Description
ControlsthedistributionofmulticastgroupsamongtheC-RP,inadomainwherethereisoverlapping
coverageofthegroupsamongtheRPs.Thisvaluespecifiesthelength(numberofsignificantbits)when
allocatingthisdistribution.Alongerhash-mask-lengthresultsinfewermulticastgroups,foreachblockof
groupaddressesassignedtotheRPs.MultipleblocksofaddressesassignedtoeachC-RPresultsinwider
dispersalofaddresses.Includesenhancedload-sharingforthemulticasttrafficforthedifferentgroupsthat
areusedinthedomainatthesametime.
Thenoformofthiscommandremovescurrentlyconfiguredvalueandsetstothedefaultof30.
Commandcontext
config-pim
Parameters
<LENGTH-VALUE>
ProtocolIndependentMulticast-SparseMode(V4andV6)|138

Specifiesthelength(inbits)ofthehashmask.Default:30.Range:1-32.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ConfiguringandremovingtheBSR-candidatehash-mask-length:
| switch(config)#     | router   | pim              |                  |     |
| ------------------- | -------- | ---------------- | ---------------- | --- |
| switch(config-pim)# |          | bsr-candidate    | hash-mask-length | 4   |
| switch(config-pim)# |          | no bsr-candidate | hash-mask-length |     |
| bsr-candidate       | priority |                  |                  |     |
Syntax
| bsr-candidate    | priority | <PRIORITY-VALUE> |     |     |
| ---------------- | -------- | ---------------- | --- | --- |
| no bsr-candidate | priority |                  |     |     |
Description
ConfigurestheprioritytoapplytotherouterwhenaBSRelectionprocessoccursinthePIM-SMdomain.
ThecandidatewiththehighestprioritybecomestheBSRforthedomain.Ifthehighestpriorityissharedby
multiplerouters,thecandidatehavingthehighestIPaddressbecomestheBSRofthedomain.Zero(0)is
thelowestpriority.TomakeBSRselectioneasilypredictable,usethiscommandtoassignadifferentpriority
toeachcandidateBSRinthePIM-SMdomain.
Thenoformofthiscommandremovescurrentlyconfiguredvalueandsetstothedefaultof0.
Commandcontext
config-pim
Parameters
<PRIORITY-VALUE>
SpecifiesthepriorityfortheCandidateBootstraprouter.Default:0.Range:0-255
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ConfiguringandremovingtheBSR-candidatepriority:
| switch(config)#     | router              | pim              |              |     |
| ------------------- | ------------------- | ---------------- | ------------ | --- |
| switch(config-pim)# |                     | bsr-candidate    | priority 250 |     |
| switch(config-pim)# |                     | no bsr-candidate | priority     |     |
| bsr-candidate       | source-ip-interface |                  |              |     |
Syntax
| bsr-candidate    | source-ip-interface |     | <INTERFACE-NAME> |     |
| ---------------- | ------------------- | --- | ---------------- | --- |
| no bsr-candidate | source-ip-interface |     | <INTERFACE-NAME> |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 139

Description

Configures the router to advertise itself as a candidate PIM-SM BSR on the interface specified, and enables
BSR candidate operation. The result makes the router eligible to be elected as the BSR for the PIM-SM
domain in which it operates. One BSR candidate interface is allowed per-router.

The no form of this command removes the Candidate BSR configuration.

Command context

config-pim

Parameters

<INTERFACE-NAME>

Specifies the interface to use as a source for Candidate-BSR router IP address. Interface can be a VLAN
interface (such as vlan15) or routed interfaces (such as lag 1 or 1 / 1 / 19). PIM-SM must be enabled on
this interface (use the ip pim-sparse enable command).

Authority

Administrators or local user group members with execution rights for this command.

Example

On the 6400 Switch Series, interface identification differs.

Configuring and removing the BSR-candidate interface:

switch(config)# router pim
switch(config-pim)# bsr-candidate source-ip-interface 1/1/4
switch(config-pim)# bsr-candidate source-ip-interface vlan5
switch(config-pim)# no rp-candidate source-ip-interface 1/1/4

disable

Syntax

disable

Description

Disables PIM globally on the router. PIM is disabled by default.

Using the disable command will cause all the multicast routes to be erased from hardware.

Command context

config-pim

Authority

Administrators or local user group members with execution rights for this command.

Example

Disabling PIM router:

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 140

switch(config)# router pim
switch(config-pim)# disable

enable

Syntax

enable

Description

Enables PIM globally on the router.

Command context

config-pim

Authority

Administrators or local user group members with execution rights for this command.

Example

Enabling PIM router:

switch(config)# router pim
switch(config-pim)# enable

ip pim-sparse {enable|disable}

Syntax

ip pim-sparse {enable|disable}

Description

Enables or disables PIM-SM in the current interface. PIM-SM is disabled by default on an interface. IP
address must be configured on the interface to enable PIM-SM.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

enable

Specifies PIM SM on the interface. IP address must be configured on the interface to enable PIM-SM.

disable

Disables PIM SM on the interface.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling and disabling PIM-SM:

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

141

| switch(config)# | interface | vlan 40 |     |
| --------------- | --------- | ------- | --- |
switch(config-if-vlan)#
|                         |     | ip address    | 40.0.0.4/24 |
| ----------------------- | --- | ------------- | ----------- |
| switch(config-if-vlan)# |     | ip pim-sparse | enable      |
| switch(config-if-vlan)# |     | ip pim-sparse | disable     |
| ip pim-sparse           | bfd |               |             |
Syntax
| ip pim-sparse bfd | [disable] |     |     |
| ----------------- | --------- | --- | --- |
| no ip pim-sparse  | bfd       |     |     |
Description
ConfiguresBFDonaper-interfacebasisforoneinterfaceassociatedwiththePIMprocess.
ThenoformofthiscommandremovestheBFDconfigurationontheinterfaceandsetsittothedefault
configuration.
IfBFDisenabledglobally,itwillbeenabledbydefaultonallinterfaces.Theonlyexceptioniswhenitisdisabled
| specificallyonaninterfaceusingtheip |     | pim-sparse | bfd disablecommand. |
| ----------------------------------- | --- | ---------- | ------------------- |
IfBFDisdisabledglobally,itwillbedisabledbydefaultonallinterfaces.Theonlyexceptioniswhenitisenabled
| specificallyonaninterfaceusingtheip |     | pim-sparse | bfdcommand. |
| ----------------------------------- | --- | ---------- | ----------- |
Commandcontext
config-if
config-if-vlan
Parameters
disable
DisablestheBFDconfigurationontheinterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingtheBFDconfigurationontheinterface:
| switch(config)# | interface | vlan 40 |     |
| --------------- | --------- | ------- | --- |
switch(config-if-vlan)#
|     |     | ip pim-sparse | bfd |
| --- | --- | ------------- | --- |
RemovingtheBFDconfigurationontheinterface:
| switch(config-if-vlan)# |     | no ip pim-sparse | bfd |
| ----------------------- | --- | ---------------- | --- |
DisablingtheBFDconfigurationontheinterfaceandoverridingtheglobalsetting:
| switch(config-if-vlan)# |             | ip pim-sparse | bfd disable |
| ----------------------- | ----------- | ------------- | ----------- |
| ip pim-sparse           | dr-priority |               |             |
ProtocolIndependentMulticast-SparseMode(V4andV6)|142

Syntax
| ip pim-sparse    | dr-priority | <PRIORITY-VALUE> |     |     |
| ---------------- | ----------- | ---------------- | --- | --- |
| no ip pim-sparse | dr-priority |                  |     |     |
Description
Changestherouterpriorityforthedesignatedrouter(DR)electionprocessinthecurrentinterface.
Anumericallyhighervaluemeansahigherpriority.Ifmultipleroutessharethehighestpriority,therouter
withthehighestIPaddressisselectedastheDR.
Thenoformofthiscommandremovescurrentlyconfiguredvalueandsetstothedefaultof1.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<PRIORITY-VALUE>
SpecifiesthepriorityvaluetouseontheinterfaceintheDRelectionprocess.Required.Default:1.
Range:0-to294967295.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringandremovingtheinterfacepriorityvalue:
| switch(config)#         | interface   | vlan 40          |             |      |
| ----------------------- | ----------- | ---------------- | ----------- | ---- |
| switch(config-if-vlan)# |             | ip pim-sparse    | dr-priority | 4444 |
| switch(config-if-vlan)# |             | no ip pim-sparse | dr-priority |      |
| ip pim-sparse           | hello-delay |                  |             |      |
Syntax
| ip pim-sparse    | hello-delay | <DELAY-VALUE> |     |     |
| ---------------- | ----------- | ------------- | --- | --- |
| no ip pim-sparse | hello-delay |               |     |     |
Description
ConfiguresthemaximumtimeinsecondsbeforetherouteractuallytransmitstheinitialPIMhellomessage
onthecurrentinterface.
Thenoformofthiscommandremovescurrentlyconfiguredvalueandsetstothedefaultof5seconds.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<DELAY-VALUE>
Specifiesthehello-delayinseconds,whichisthemaximumtimebeforeatriggeredPIMHellomessageis
transmittedonthisinterface.Default:5.Range:0to5.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 143

Authority

Administrators or local user group members with execution rights for this command.

Usage

n In cases where a new interface activates connections with multiple routers. If all the connected routers

sent hello packets at the same time, the receiving router could become momentarily overloaded.

n This command randomizes the transmission delay to a time between zero and the hello delay setting.

Using zero means no delay. After the router sends the initial hello packet to a newly detected interface, it
sends subsequent hello packets according to the current hello interval setting.

Example

Configuring and removing hello-delay interface:

switch(config)# interface vlan 40
switch(config-if-vlan)# ip pim-sparse hello-delay 4
switch(config-if-vlan)# no ip pim-sparse hello-delay

ip pim-sparse hello-interval

Syntax

ip pim-sparse hello-interval <INTERVAL-VALUE>
no ip pim-sparse hello-interval

Description

Configures the frequency at which the router transmits PIM hello messages on the current interface.

The no form of this command removes the currently configured value and sets to the default of 30 seconds.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

<INTERVAL-VALUE>

Specifies the frequency at which PIM Hello messages are transmitted on this interface. Range: 5 to 300.
Default: 30.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n The router uses hello packets to inform neighbor routers of its presence.

n The router also uses this setting to compute the hello holdtime, which is included in hello packets sent to

neighbor routers.

n Hello holdtime tells neighbor routers how long to wait for the next hello packet from the router. If

another packet does not arrive within that time, the router removes the neighbor adjacency on that
interface from the PIM adjacency table, which removes any flows running on that interface.

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 144

Shorteningthehellointervalreducesthehelloholdtime.Iftheydonotreceiveanewhellopacketwhen
n
expected,itchangeshowquicklyotherroutersstopsendingtraffictotherouter.
Example
Configuringandremovingsparsehello-interval:
| switch(config)#         | interface | vlan 20          |                |     |
| ----------------------- | --------- | ---------------- | -------------- | --- |
| switch(config-if-vlan)# |           | ip pim-sparse    | hello-interval | 60  |
| switch(config-if-vlan)# |           | no ip pim-sparse | hello-interval |     |
| ip pim-sparse           | ip-addr   |                  |                |     |
Syntax
| ip pim-sparse    | ip-addr {<IP-ADDR-VALUE> |     | | any} |     |
| ---------------- | ------------------------ | --- | ------ | --- |
| no ip pim-sparse | ip-addr                  |     |        |     |
Description
EnablestheroutertodynamicallydeterminethesourceIPaddresstouseforPIM-SMpacketssentfromthe
interfaceortousethespecificIPaddress.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetstothedefaultofany.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<IP-ADDR-VALUE>
SpecifiesanIPaddressasthesourceIPfortheinterface.
any
SpecifiesdynamicallydeterminingthesourceIPfromthecurrentIPaddressoftheinterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringandremovingsourceIPaddress:
| switch(config)#         | interface       | vlan 40          |                  |     |
| ----------------------- | --------------- | ---------------- | ---------------- | --- |
| switch(config-if-vlan)# |                 | ip pim-sparse    | ip-addr 40.0.0.4 |     |
| switch(config-if-vlan)# |                 | no ip pim-sparse | ip-addr          |     |
| ip pim-sparse           | lan-prune-delay |                  |                  |     |
Syntax
| ip pim-sparse    | lan-prune-delay |     |     |     |
| ---------------- | --------------- | --- | --- | --- |
| no ip pim-sparse | lan-prune-delay |     |     |     |
Description
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 145

Enables the LAN prune delay option on the current interface. The default is enabled.

With LAN-prune-delay enabled, the router informs downstream neighbors how long it will wait before
pruning a flow after receiving a prune request. Other downstream routers on the same interface must send
a join to override the prune before the LAN-prune-delay time to continue the flow. Prompts any
downstream neighbors with multicast receivers continuing to belong to the flow to reply with a join. If no
joins are received after the LAN-prune-delay period, the router prunes the flow. The propagation-delay and
override-interval settings determine the LAN-prune-delay setting.

The no form of this command disables the LAN prune delay option.

Command context

config-if
config-if-vlan
config-lag-if

Authority

Administrators or local user group members with execution rights for this command.

Example

Enabling and disabling the LAN prune delay:

switch(config)# interface vlan 40
switch(config-if-vlan)# ip pim-sparse lan-prune-delay
switch(config-if-vlan)# no ip pim-sparse lan-prune-delay

ip pim-sparse override-interval

Syntax

ip pim-sparse override-interval <INTERVAL-VALUE>
no ip pim-sparse override-interval

Description

Configures the override interval that gets inserted into the Override Interval field of a LAN Prune Delay
option.

The no form of this command removes the currently configured value and sets the value to the default of
2500 ms.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

<INTERVAL-VALUE>

Specifies the override interval of a LAN Prune Delay option in ms. Range: 500 to 6000. Default: 2500.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 146

AroutersharingaVLANwithothermulticastroutersusestheoverride-intervalvaluealongwiththe
propagation-delayvaluetocomputethelan-prune-delaysetting.Thesettingspecifieshowlongtowaitfor
aPIM-SMjoinafterreceivingaprunepacketfromdownstreamforaparticularmulticastgroup.
Examplescenario:
AnetworkmayhavemultiplerouterssharingVLANX.Whenanupstreamrouterisforwardingtrafficfrom
multicastgroupXtoVLANY,ifoneoftheroutersonVLANYdoesnotwantthistraffic,itissuesaprune
responsetotheupstreamneighbor.Theupstreamneighborthengoesintoaprunependingstateforgroup
XonVLANY.Duringthisperiod,theupstreamneighborcontinuestoforwardthetraffic.Duringthe
pendingperiod,anotherrouteronVLANYcansendagroupXjointotheupstreamneighbor.Ifthis
happens,theupstreamneighbordropstheprunependingstatusandcontinuesforwardingthetraffic.But
ifnoroutersontheVLANsendajoin,theupstreamrouterprunes.
Example
Configuringandremovingtheoverrideinterval:
| switch(config)#         | interface         | vlan 40          |                   |      |
| ----------------------- | ----------------- | ---------------- | ----------------- | ---- |
| switch(config-if-vlan)# |                   | ip pim-sparse    | override-interval | 4000 |
| switch(config-if-vlan)# |                   | no ip pim-sparse | override-interval |      |
| ip pim-sparse           | propagation-delay |                  |                   |      |
Syntax
| ip pim-sparse    | propagation-delay | <DELAY-VALUE> |     |     |
| ---------------- | ----------------- | ------------- | --- | --- |
| no ip pim-sparse | propagation-delay |               |     |     |
Description
ConfiguresthepropagationdelaythatgetsinsertedintotheLANprunedelayfieldofaLANPruneDelay
option.
Thenoformofthiscommandremovescurrentlyconfiguredvalueandsetstothedefaultof500ms.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<DELAY-VALUE>
Specifiesthepropagationdelayvalueinms.Range:250to2000.Default:500.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringandremovingthepropagationdelay:
| switch(config)#         | interface | vlan 40          |                   |     |
| ----------------------- | --------- | ---------------- | ----------------- | --- |
| switch(config-if-vlan)# |           | ip pim-sparse    | propagation-delay | 400 |
| switch(config-if-vlan)# |           | no ip pim-sparse | propagation-delay |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 147

join-prune-interval

Syntax

join-prune-interval <INTERVAL-VALUE>
no join-prune-interval

Description

Configures the frequency at which the router will send periodic join or prune-interval messages.

The no form of this command sets the interval to the default value of 60 seconds.

Command context

config-pim

Parameters

<INTERVAL-VALUE>

Specifies the join-prune-interval in seconds. Range 5 to 65535 Default: 60.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring join prune interval:

switch(config)# router pim
switch(config-pim)# join-prune-interval 400
switch(config-pim)# no join-prune-interval

multicast-route-limit

Syntax

multicast-route-limit <limit>
no multicast-route-limit <limit>

Description

Configures the limit on the maximum number of multicast route entries that can be programmed. When
the limit is configured, multicast route entries created because of IGMP or MLD membership reports, and
multicast route entries created because of multicast streams are restricted to the configured limit.

The no form of this command removes the currently configured limit value.

Command context

config-pim

Parameters

<limit>

Specifies the value to be configured as the multicast route limit. Range: 1 to 4294967295.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 148

Flows exceeding the configured multicast route limit will be programmed as a bridge entry and will not have
the outgoing interfaces list populated. This configuration prevents creation of new multicast routes when
limits are reached. At the time of configuration, if the device has more multicast routes than the configured
limit, existing multicast routes continue to exist until they are removed.

The flows are programmed in the HW on a FCFS basis. There could be scenarios where the flow is forwarded
in neighbor router, but it may not be forwarded on the current router because of exceeding the limits
configured on the current router. In such cases, it is recommended to configure higher limits to avoid traffic
outage.

Examples

Configuring and removing the multicast route rate limit:

switch(config)# router pim
switch(config-pim)# multicast-route-limit 1024
switch(config-pim)# no multicast-route-limit

no ip pim-sparse

Syntax

no ip pim-sparse

Description

Removes all the PIM-SM related configurations for the interface.

Command context

config-if
config-if-vlan
config-lag-if

Authority

Administrators or local user group members with execution rights for this command.

Example

Removing PIM-SM configuration:

switch(config)# interface vlan 40
switch(config-if-vlan)# no ip pim-sparse

register-rate-limit

Syntax

register-rate-limit <limit>
no register-rate-limit <limit>

Description

Configures the limit on the maximum number of register messages sent per second for every unique (S,G)
entry. By default, there is no maximum rate set. When the limit is configured, register messages generation
is limited to the configured value.

The no form of this command removes the currently configured limit value.

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

149

Commandcontext
config-pim
Parameters
<limit>
Specifiesthevaluetobeconfiguredastheregisterratelimit.Range:1to4294967295.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringandremovingtheregisterratelimit:
| switch(config)#     | router pim             |     |     |
| ------------------- | ---------------------- | --- | --- |
| switch(config-pim)# | register-rate-limit    |     | 10  |
| switch(config-pim)# | no register-rate-limit |     |     |
router pim
Syntax
| router pim [vrf    | <VRF-NAME>] |     |     |
| ------------------ | ----------- | --- | --- |
| no router pim [vrf | <VRF-NAME>] |     |     |
Description
ChangesthecurrentcontexttothePIMconfigurationcontext.IfnoVRFisspecified,thedefaultVRFis
assumed.
ThenoformofthiscommandremovesthePIMconfigurationfromthespecifiedcontextorthedefaultVRF.
Commandcontext
config
Parameters
vrf <VRF-NAME>
SpecifiesthenameofaVRF.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringdefaultrouterPIM:
| switch(config)# | router pim |     |     |
| --------------- | ---------- | --- | --- |
switch(config-pim)#
ConfiguringspecifiedrouterPIM:
| switch(config)# | router pim | vrf green |     |
| --------------- | ---------- | --------- | --- |
switch(config-pim)#
ProtocolIndependentMulticast-SparseMode(V4andV6)|150

RemovingrouterPIM:
| switch(config)# |           | no router | pim |     |     |     |
| --------------- | --------- | --------- | --- | --- | --- | --- |
| rp-address      | <IP-ADDR> |           |     |     |     |     |
Syntax
| rp-address    | <IP-ADDR> | [<GRP-ADDR/GRP-MASK>] |     |     | [override] |     |
| ------------- | --------- | --------------------- | --- | --- | ---------- | --- |
| no rp-address | <IP-ADDR> | [<GRP-ADDR/GRP-MASK>] |     |     | [override] |     |
Description
StaticallyconfigurestherouterastheRPforaspecifiedmulticastgrouporrangeofmulticastgroups.This
mustbeconfiguredonallPIM-SMroutersinthedomain.Ifgroupaddressisnotspecified,itappliestoall
IPv4multicastaddresses(224.0.0.0-239.255.255.255).PIM-SMsupportsamaximumof8staticRPsper
VRF.
ThenoformofthiscommandremovesstaticRPconfigurationanditsprecedence.
Commandcontext
config-pim
Parameters
<IP-ADDR>
SpecifiestheaddressofthestaticRPinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to
255.
<GRP-ADDR>
SpecifiesthemulticastgroupaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to
255.
<GRP-MASK>
SpecifiestheaddressmaskinCIDRformat(x),wherexisadecimalnumberfrom0to128.
override
SpecifieshigherprecedencetostaticRPoverCandidateRP.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
WhereastaticRPandaC-RPareconfiguredtosupportthesamemulticastgroupsandthemulticastgroup
maskforthestaticRPisequaltoorgreaterthanthesamemaskfortheapplicableC-RPs,thiscommand
assignsthehigherprecedencetothestaticRP,resultingintheC-RPoperatingonlyasabackupRPforthe
configuredgroup.Withoutoverride,theC-RPhasprecedenceoverastaticRPconfiguredforthesame
multicastgrouporgroups.
Examples
| switch(config)#     |     | router     | pim        |          |              |           |
| ------------------- | --- | ---------- | ---------- | -------- | ------------ | --------- |
| switch(config-pim)# |     | rp-address |            | 40.0.0.4 | 230.0.0.4/24 | ovverride |
| switch(config-pim)# |     | rp-address |            | 40.0.0.8 | 222.0.0.4/24 |           |
| switch(config-pim)# |     | no         | rp-address | 40.0.0.4 | 230.0.0.4/24 |           |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 151

| rp-candidate | group-prefix |     |     |     |
| ------------ | ------------ | --- | --- | --- |
Syntax
| rp-candidate    | group-prefix | <GRP-ADDR/GRP-MASK> |     |     |
| --------------- | ------------ | ------------------- | --- | --- |
| no rp-candidate | group-prefix | <GRP-ADDR/GRP-MASK> |     |     |
Description
AddsmulticastgroupaddresstothecurrentCandidateRendezvousPoint(C-RP)configuration.
ThenoformofthiscommandremovesC-RPmulticastgroupaddress.
Commandcontext
config-pim
Parameters
<GRP-ADDR>
SpecifiesthemulticastgroupaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to
255.
<GRP-MASK>
SpecifiestheaddressmaskinCIDRformat(x),wherexisadecimalnumberfrom0to128.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringandremovingcandidategroupprefix:
| switch(config)#     |           | router pim      |              |              |
| ------------------- | --------- | --------------- | ------------ | ------------ |
| switch(config-pim)# |           | rp-candidate    | group-prefix | 230.0.0.4/24 |
| switch(config-pim)# |           | no rp-candidate | group-prefix | 230.0.0.4/24 |
| rp-candidate        | hold-time |                 |              |              |
Syntax
| rp-candidate    | hold-time | <TIME-VALUE> |     |     |
| --------------- | --------- | ------------ | --- | --- |
| no rp-candidate | hold-time |              |     |     |
Description
Changesthehold-timeaC-RPincludesinitsadvertisementstotheBSR.
Hold-timeisincludedintheadvertisementstheC-RPperiodicallysendstotheelectedBSRforthedomain.
AlsoupdatestheBSRonhowlongtowaitafterthelastadvertisementfromthereportingRPbefore
assumingithasbecomeunavailable.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetsittothedefaultvalue150
seconds.
Commandcontext
config-pim
Parameters
<TIME-VALUE>
ProtocolIndependentMulticast-SparseMode(V4andV6)|152

Specifiesthehold-timevalueinsecondstobesentinC-RP-Advmessages.Range:30to250.Default:
150.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Settingandremovingthecandidateholdtime:
| switch(config)# router | pim |     |     |
| ---------------------- | --- | --- | --- |
switch(config-pim)#
|                       | rp-candidate    | hold-time | 250 |
| --------------------- | --------------- | --------- | --- |
| switch(config-pim)#   | no rp-candidate | hold-time |     |
| rp-candidate priority |                 |           |     |
Syntax
| rp-candidate priority | <PRIORITY-VALUE> |     |     |
| --------------------- | ---------------- | --- | --- |
no rp-candidate priority
Description
ChangesthecurrentprioritysettingforaC-RP.WheremultipleC-RPconfigurationsareusedtosupportthe
samemulticastgroups,thecandidatehavingthehighestpriorityiselected.Zero(0)isthehighestpriority,
and255isthelowestpriority.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetsittothedefaultof192.
Commandcontext
config-pim
Parameters
<PRIORITY-VALUE>
SpecifiesthepriorityvaluefortheCandidate-RProuter.Range:0to255.Default:192.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Configuringandremovingcandidatepriority:
| switch(config)# router           | pim             |          |     |
| -------------------------------- | --------------- | -------- | --- |
| switch(config-pim)#              | rp-candidate    | priority | 250 |
| switch(config-pim)#              | no rp-candidate | priority |     |
| rp-candidate source-ip-interface |                 |          |     |
Syntax
rp-candidate source-ip-interface <INTERFACE-NAME> [group-prefix <GRP-ADDR/GRP-MASK>]
no rp-candidate source-ip-interface <INTERFACE-NAME> [group-prefix <GRP-ADDR/GRP-MASK>]
Description
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 153

Enables the Candidate Rendezvous Point (C-RP) operation, and configures the router to advertise itself as a
C-RP to the Bootstrap Router (BSR) for the current domain.

This step includes the option to allow the C-RP to be a candidate for all possible multicast groups, or for up
to four multicast groups, or ranges of groups. If group-prefix is not given, it considers for all multicast group
addresses.

The no form of this command removes the C-RP configuration.

Command context

config-pim

Parameters

<INTERFACE-NAME>

Specifies the interface to use as a source for the C-RP router IP address.

<GRP-ADDR>

Specifies the multicast group address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to
255.
<GRP-MASK>

Specifies the address mask in CIDR format (x), where x is a decimal number from 0 to 128.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring and removing candidate source IP interface:

switch(config)# router pim
switch(config-pim)# rp-candidate source-ip-interface vlan40 group-prefix
230.0.0.4/24
switch(config-pim)# no rp-candidate source-ip-interface vlan20

rpf-override

Syntax

rpf-override <SRC-ADDR/SRC-MASK> <RPF-ADDR|INTERFACE-NAME>
no rpf-override <SRC-ADDR/SRC-MASK> <RPF-ADDR|INTERFACE-NAME>

Description

The Reverse Path Forward (RPF) override, allows overriding the normal RPF lookup mechanism, and
indicates to the router that it may accept multicast traffic on an interface other than the one that the RPF
lookup mechanism would normally select. This includes accepting traffic from an invalid source IP address
for the subnet or VLAN that is directly connected to the router. Traffic may also be accepted from a valid
PIM neighbor that is not on the reverse path towards the source of the received multicast traffic.

The no form of this command removes currently configured RPF entry.

Command context

config-pim

Parameters

<SRC-ADDR/SRC-MASK>

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 154

Specifies the multicast source IPv4 address in IPv4 format (x.x.x.x), where x is a decimal number from 0
to 255. And the number of bits in the address mask in CIDR format (x), where x is a decimal number from
0 to 128.
<RPF-ADDR>

Specifies the RPF address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255.

<INTERFACE-NAME>

Specifies the RPF interface name.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n Reverse Path Forward (RPF) checking is a core multicast routing mechanism. The RPF ensures that the
multicast traffic received arrives on the expected router interface before further processing. If the RPF
check fails for a multicast packet, the packet is discarded. For multicast traffic flow that arrives on the
SPT, the expected incoming interface for a given source or group is the interface towards the source
address of the traffic (determined by the unicast routing system). For traffic arriving on the RP tree, the
expected incoming interface is the interface towards the RP.

n RPF checking is applied to all multicast traffic and is significant in preventing network loops. Up to eight
manual RPF overrides can be specified. The RPF-address indicates one of two distinct RPF candidates:
1. A valid PIM neighbor address from which forwarded multicast traffic is accepted with a source

address of <source-addr/src-mask>.

2. A local router address on a PIM-enabled interface to which <source-addr/src-mask> is directly

connected. If configured, the local router will assume the role of DR for this flow and registers the
flow with an RP.

Example

Configuring and removing RPF override:

switch(config)# router pim
switch(config-pim)# rpf-override 40.0.0.4/24 30.0.0.4
switch(config-pim)# no rpf-override 40.0.0.4/24 30.0.0.4

show ip mroute

Syntax

show ip mroute [all-vrfs | vrf <VRF-NAME>] [vsx-peer]

Description

Shows multicast routing information. Optionally, you can show specific information by VRF. If no options
are specified, it shows information for the default VRF.

Command context

Operator (>) or Manager (#)

Parameters

all-vrfs

Shows mroute information for all VRFs.

vrf <VRF-NAME>

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

155

SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingIPmrouteforallVRFs:
| switch#    | show ip    | mroute all-vrfs |
| ---------- | ---------- | --------------- |
| VRF        | : blue     |                 |
| Total      | number of  | entries : 1     |
| Group      | Address    | : 239.1.1.1     |
| Source     | Address    | : 40.0.0.5      |
| Incoming   | interface  | : vlan3         |
| Downstream | Interface  |                 |
| Interface  | State      |                 |
| ---------  | -----      |                 |
| vlan2      | forwarding |                 |
| VRF        | : green    |                 |
| Total      | number of  | entries : 2     |
| Group      | Address    | : 239.1.1.1     |
| Source     | Address    | : 40.0.0.4      |
| Neighbor   |            | : 10.1.1.1      |
| Incoming   | interface  | : vlan2         |
| Downstream | Interface  |                 |
| Interface  | State      |                 |
| ---------  | -----      |                 |
| vlan5      | forwarding |                 |
| Group      | Address    | : 239.1.1.1     |
| Source     | Address    | : 40.0.0.5      |
| Neighbor   |            | : 10.1.1.2      |
| Incoming   | interface  | : vlan1         |
| Downstream | Interface  |                 |
| Interface  | State      |                 |
| ---------  | -----      |                 |
| vlan6      | forwarding |                 |
| VRF        | : default  |                 |
| Total      | number of  | entries : 1     |
| Group      | Address    | : 10.1.1.14     |
| Source     | Address    | : 40.0.0.6      |
| Neighbor   |            | : 10.1.1.2      |
| Incoming   | interface  | : 1/1/5         |
| Downstream | Interface  |                 |
| Interface  | State      |                 |
| ---------  | -----      |                 |
| 1/1/3      | forwarding |                 |
| 1/1/1      | pruned     |                 |
| show       | ip mroute  | brief           |
ProtocolIndependentMulticast-SparseMode(V4andV6)|156

Syntax
| show ip | mroute brief | [al-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |     |
| ------- | ------------ | -------- | ----------------- | ---------- | --- |
Description
Showsbriefversionofthemulticastroutinginformation.Optionally,youcanspecifythedisplay
informationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsmrouteinformationbrieflyforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingtheIPmroutebrief:
switch#
|               | show ip   | mroute         | brief   |          |           |
| ------------- | --------- | -------------- | ------- | -------- | --------- |
| VRF           | : default |                |         |          |           |
| Total         | number of | entries        | : 1     |          |           |
| Group         | Address   | Source         | Address | Neighbor | Interface |
| ------------- |           | -------------- |         | -------- | --------- |
| 239.1.1.1     |           | 40.0.0.6       |         | 10.1.1.2 | vlan5     |
| show          | ip mroute | <GROUP-ADDR>   |         |          |           |
Syntax
| show ip   | mroute <GROUP-ADDR> |             | [<SOURCE-ADDR>] |     |     |
| --------- | ------------------- | ----------- | --------------- | --- | --- |
| [all-vrfs | | vrf               | <vrf-name>] | [vsx-peer]      |     |     |
Description
Showsthemulticastroutinginformationforthegivengroupaddress.Optionally,youcanspecifydisplay
informationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
<GROUP-ADDR>
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 157

SpecifiesagroupaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
<SOURCE-ADDR>
SpecifiesshowinformationforthegroupfromthissourceinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255.
all-vrfs
ShowsmrouteinformationforthegroupforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showinginformationforgroup239.1.1.1andVRFgreen:
| switch# | show | ip mroute 239.1.1.1 | vrf green |
| ------- | ---- | ------------------- | --------- |
VRF : green
| Group      | Address    |          | : 239.1.1.1 |
| ---------- | ---------- | -------- | ----------- |
| Source     | Address    |          | : 40.0.0.5  |
| Neighbor   |            |          | : 10.1.1.2  |
| Incoming   | interface  |          | : vlan1     |
| Unicast    | Routing    | Protocol | : connected |
| Metric     |            |          | : 1234      |
| Metric     | Pref       |          | : 1234      |
| Downstream | Interface  |          |             |
| Interface  | State      |          |             |
| ---------  | -----      |          |             |
| vlan6      | forwarding |          |             |
Showinginformationforgroup239.1.1.1fromsource40.0.0.5andallVRFs:
switch#
|     | show | ip mroute 239.1.1.1 | 40.0.0.5 all-vrfs |
| --- | ---- | ------------------- | ----------------- |
VRF : blue
| Group      | Address    |          | : 239.1.1.1 |
| ---------- | ---------- | -------- | ----------- |
| Source     | Address    |          | : 40.0.0.5  |
| Incoming   | interface  |          | : vlan3     |
| Unicast    | Routing    | Protocol | : connected |
| Metric     |            |          | : 1234      |
| Metric     | Pref       |          | : 1234      |
| Downstream | Interface  |          |             |
| Interface  | State      |          |             |
| ---------  | -----      |          |             |
| vlan2      | forwarding |          |             |
VRF : green
ProtocolIndependentMulticast-SparseMode(V4andV6)|158

| Group      | Address    |          | : 239.1.1.1 |
| ---------- | ---------- | -------- | ----------- |
| Source     | Address    |          | : 40.0.0.5  |
| Neighbor   |            |          | : 10.1.1.2  |
| Incoming   | interface  |          | : vlan1     |
| Unicast    | Routing    | Protocol | : connected |
| Metric     |            |          | : 1234      |
| Metric     | Pref       |          | : 1234      |
| Downstream | Interface  |          |             |
| Interface  | State      |          |             |
| ---------  | -----      |          |             |
| vlan6      | forwarding |          |             |
| show ip    | pim        |          |             |
Syntax
| show ip pim | [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |
| ----------- | --------- | ----------------- | ---------- |
Description
ShowsthePIMrouterinformation.Optionally,youcanspecifydisplayinformationbyVRF.Ifnooptionsare
specified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsPIMrouterinformationonallVRFs.
vrf <VRF-NAME>
SpecifythenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingIPPIMrouter:
| switch#       | show ip    | pim |           |
| ------------- | ---------- | --- | --------- |
| PIM Global    | Parameters |     |           |
| VRF           |            |     | : default |
| PIM Status    |            |     | : enable  |
| SPT Threshold |            |     | : enabled |
| show ip       | pim bsr    |     |           |
Syntax
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 159

| show ip pim | bsr | [all-vrfs |     | | vrf <VRF-NAME>] | [vsx-peer] |
| ----------- | --- | --------- | --- | ----------------- | ---------- |
Description
ShowstheinformationaboutBSRcandidatesinthedomainandmulticastgroupsitsupports.Optionally,
youcanspecifythedisplayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthe
defaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
Optional.ShowsPIMcandidateBSRinformationforallVRFs.
vrf <VRF-NAME>
Optional.ShowsPIMcandidateBSRinformationforaparticularVRF.Ifthe<VRF-NAME>isnotspecified,it
showsinformationforthedefaultVRF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowinginformationaboutBSRcandidates:
| switch#         | show      | ip pim          | bsr    | all-vrfs      |                    |
| --------------- | --------- | --------------- | ------ | ------------- | ------------------ |
| Status          | and       | Counters-       | PIM-SM | Bootstrap     | Router Information |
| VRF             |           |                 |        | : default     |                    |
| E-BSR           | Address   |                 |        | : 10.0.0.1    |                    |
| E-BSR           | Priority  |                 |        | : 0           |                    |
| E-BSR           | Hash      | Mask Length     |        | : 30          |                    |
| E-BSR           | Up Time   |                 |        | : 3000 secs   |                    |
| Next            | Bootstrap | Message         |        | : 80 secs     |                    |
| C-BSR           | Admin     | Status          |        | : This system | is a Candidate-BSR |
| C-BSR           | Address   |                 |        | : 2.2.2.2/24  |                    |
| C-BSR           | Priority  |                 |        | : 34          |                    |
| C-BSR           | Hash      | Mask Length     |        | : 30          |                    |
| C-BSR           | Message   | Interval        |        | : 76          |                    |
| C-BSR           | Source    | IP Interface    |        | : vlan10      |                    |
| C-RP            | Admin     | Status          |        | : This system | is a Candidate-RP  |
| C-RP            | Address   |                 |        | : 2.2.2.2     |                    |
| C-RP            | Hold Time |                 |        | : 150         |                    |
| C-RP            | Advertise | Period          |        | : 60          |                    |
| C-RP            | Priority  |                 |        | : 192         |                    |
| C-RP            | Source    | IP Interface    |        | : vlan10      |                    |
| Group           | Address   | Group           |        | Mask          |                    |
| --------------- |           | --------------- |        |               |                    |
ProtocolIndependentMulticast-SparseMode(V4andV6)|160

| 226.2.2.2       |           |          | 255.255.255.255 |      |             |                    |     |
| --------------- | --------- | -------- | --------------- | ---- | ----------- | ------------------ | --- |
| 228.2.2.2       |           |          | 255.255.255.255 |      |             |                    |     |
| 232.2.2.2       |           |          | 255.255.255.255 |      |             |                    |     |
| VRF             |           |          |                 | :    | green       |                    |     |
| E-BSR           | Address   |          |                 | :    | 2.2.2.2     |                    |     |
| E-BSR           | Priority  |          |                 | :    | 0           |                    |     |
| E-BSR           | Hash      | Mask     | Length          | :    | 30          |                    |     |
| E-BSR           | Up Time   |          |                 | :    | 3000 secs   |                    |     |
| Next            | Bootstrap |          | Message         | :    | 80 secs     |                    |     |
| C-BSR           | Admin     | Status   |                 | :    | This system | is a Candidate-BSR |     |
| C-BSR           | Address   |          |                 | :    | 2.2.2.2/24  |                    |     |
| C-BSR           | Priority  |          |                 | :    | 34          |                    |     |
| C-BSR           | Hash      | Mask     | Length          | :    | 32          |                    |     |
| C-BSR           | Message   | Interval |                 | :    | 60          |                    |     |
| C-BSR           | Source    | IP       | Interface       | :    | vlan10      |                    |     |
| C-RP            | Admin     | Status   |                 | :    | This system | is a Candidate-RP  |     |
| C-RP            | Address   |          |                 | :    | 2.2.2.2     |                    |     |
| C-RP            | Hold      | Time     |                 | :    | 150         |                    |     |
| C-RP            | Advertise |          | Period          | :    | 60          |                    |     |
| C-RP            | Priority  |          |                 | :    | 192         |                    |     |
| C-RP            | Source    | IP       | Interface       | :    | vlan10      |                    |     |
| Group           | Address   |          | Group           | Mask |             |                    |     |
| --------------- |           |          | --------------- |      |             |                    |     |
| 231.2.2.2       |           |          | 255.255.255.255 |      |             |                    |     |
| 232.2.2.2       |           |          | 255.255.255.255 |      |             |                    |     |
| 235.2.2.2       |           |          | 255.255.255.255 |      |             |                    |     |
| show            | ip pim    | bsr      | elected         |      |             |                    |     |
Syntax
| show ip | pim | bsr elected | [all-vrfs |     | | vrf | <VRF-NAME>] | [vsx-peer] |
| ------- | --- | ----------- | --------- | --- | ----- | ----------- | ---------- |
Description
ShowsinformationabouttheelectedBSRinthedomainandmulticastgroupsitsupports.Optionallyyou
canspecifydisplayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
SelectsallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 161

Example
ShowingPIMelectedbootstraprouterinformation:
switch#
|        | show          | ip pim  | bsr    | elected    | all-vrfs  |                    |
| ------ | ------------- | ------- | ------ | ---------- | --------- | ------------------ |
| Status | and Counters- |         | PIM-SM | Elected    | Bootstrap | Router Information |
| VRF    |               |         |        | : default  |           |                    |
| E-BSR  | Address       |         |        | : 10.0.0.1 |           |                    |
| E-BSR  | Priority      |         |        | : 0        |           |                    |
| E-BSR  | Hash Mask     | Length  |        | : 30       |           |                    |
| E-BSR  | Up Time       |         |        | : 3000     | secs      |                    |
| Next   | Bootstrap     | Message |        | : 80       | secs      |                    |
| VRF    |               |         |        | : green    |           |                    |
| E-BSR  | Address       |         |        | : 20.0.0.1 |           |                    |
| E-BSR  | Priority      |         |        | : 0        |           |                    |
| E-BSR  | Hash Mask     | Length  |        | : 30       |           |                    |
| E-BSR  | Up Time       |         |        | : 3000     | secs      |                    |
| Next   | Bootstrap     | Message |        | : 80       | secs      |                    |
| show   | ip pim        | bsr     | local  |            |           |                    |
Syntax
| show ip | pim bsr | local | [all-vrfs |     | | vrf <VRF-NAME>] | [vsx-peer] |
| ------- | ------- | ----- | --------- | --- | ----------------- | ---------- |
Description
ShowstheinformationaboutBSRcandidatesonthelocalrouterandmulticastgroupsitsupports.
Optionally,youcanspecifydisplayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationfor
thedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
SelectsallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowinglocalCandidateBSR:
ProtocolIndependentMulticast-SparseMode(V4andV6)|162

| switch# | show     | ip pim       | bsr local | all-vrfs     |               |     |                 |
| ------- | -------- | ------------ | --------- | ------------ | ------------- | --- | --------------- |
| Status  | and      | Counters     | - PIM-SM  | Local        | Candidate-BSR |     | Information     |
| VRF     |          |              |           | : default    |               |     |                 |
| C-BSR   | Admin    | Status       |           | : This       | system        | is  | a Candidate-BSR |
| C-BSR   | Address  |              |           | : 2.2.2.2/24 |               |     |                 |
| C-BSR   | Priority |              |           | : 34         |               |     |                 |
| C-BSR   | Hash     | Mask Length  |           | : 30         |               |     |                 |
| C-BSR   | Message  | Interval     |           | : 76         |               |     |                 |
| C-BSR   | Source   | IP Interface |           | : vlan10     |               |     |                 |
| VRF     |          |              |           | : green      |               |     |                 |
| C-BSR   | Admin    | Status       |           | : This       | system        | is  | a Candidate-BSR |
| C-BSR   | Address  |              |           | : 2.2.2.2/24 |               |     |                 |
| C-BSR   | Priority |              |           | : 34         |               |     |                 |
| C-BSR   | Hash     | Mask Length  |           | : 32         |               |     |                 |
| C-BSR   | Message  | Interval     |           | : 60         |               |     |                 |
| C-BSR   | Source   | IP Interface |           | : vlan10     |               |     |                 |
| show ip | pim      | interface    |           |              |               |     |                 |
Syntax
| show ip pim | interface |     | [all-vrfs | | vrf | <VRF-NAME>] |     | [vsx-peer] |
| ----------- | --------- | --- | --------- | ----- | ----------- | --- | ---------- |
Description
ShowstheinformationaboutPIMinterfacescurrentlyconfiguredintherouter.Optionally,youcanspecify
displayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
SelectsallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMinterface:
| switch#        | show | ip pim | interface |     |     |     |     |
| -------------- | ---- | ------ | --------- | --- | --- | --- | --- |
| PIM Interfaces |      |        |           |     |     |     |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 163

| VRF:               | default |           |                   |                  |            |     |     |     |
| ------------------ | ------- | --------- | ----------------- | ---------------- | ---------- | --- | --- | --- |
| Interface          |         |           | IP Address        |                  | mode       |     |     |     |
| ------------------ |         |           | ----------------- |                  | ---------- |     |     |     |
| 1/1/1              |         |           | 40.0.0.4/24       |                  | sparse     |     |     |     |
| 1/1/2              |         |           | 50.0.0.4/24       |                  | sparse     |     |     |     |
| show               | ip pim  | interface |                   | <INTERFACE-NAME> |            |     |     |     |
Syntax
| show ip | pim interface |     | <INTERFACE-NAME> |     | [vsx-peer] |     |     |     |
| ------- | ------------- | --- | ---------------- | --- | ---------- | --- | --- | --- |
Description
ShowsdetailedinformationaboutthePIMinterfacecurrentlyconfigured.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-NAME>
SpecifiesaninterfaceforshowingPIMinterfaceinformation.InterfacecanalsobeaLAGorVLAN.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMinterfaceinformationforinterface1/1/2:
| switch#     | show       | ip            | pim interface | 1/1/2  |     |             |       |       |
| ----------- | ---------- | ------------- | ------------- | ------ | --- | ----------- | ----- | ----- |
| PIM         | Interfaces |               |               |        |     |             |       |       |
| VRF:        | default    |               |               |        |     |             |       |       |
| Interface   |            | : 1/1/2       |               |        |     |             |       |       |
| IP Address  |            | : 50.0.0.4/24 |               |        |     |             |       |       |
| Mode        |            | : sparse      |               |        |     |             |       |       |
| Designated  |            | Router        | :             |        |     |             |       |       |
| Hello       | Interval   | (sec)         | :             | 30     |     |             |       |       |
| Hello       | Delay      | (sec)         | :             | 5      |     |             |       |       |
| Override    | Interval   |               | (msec)        | : 2500 |     | Lan Prune   | Delay | : Yes |
| Propagation |            | Delay         | (msec)        | : 500  |     | DR Priority |       | : 1   |
| Neighbor    | Timeout    |               |               | : 105  |     |             |       |       |
ProtocolIndependentMulticast-SparseMode(V4andV6)|164

| show | ip pim | interface |     | <INTERFACE-NAME> |     | counters |
| ---- | ------ | --------- | --- | ---------------- | --- | -------- |
Syntax
| show ip | pim interface | <INTERFACE-NAME> |     |     | counters [vsx-peer] |     |
| ------- | ------------- | ---------------- | --- | --- | ------------------- | --- |
Description
ShowsthePIMpacketcountersinformationforthespecifiedinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-NAME>
Specifiestheinterfacetoshowpacketcounterinformation.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
LoopbackinterfacesarespecialinterfaceswhereonlyunicastPIMmessagesareupdated.Thisincludes
Register,RegisterStop,andCandidateRPAdvertisements.
WhenaloopbackinterfaceisconfiguredastheRP,theACLdropcounterswillbeupdatedontheinterface
onwhichthepacketsarereceived.
Example
ShowingPIMpacketcounters:
| switch#     | show           | ip pim interface |           | vlan1     | counters |     |
| ----------- | -------------- | ---------------- | --------- | --------- | -------- | --- |
| Interface   |                | :                | vlan1     |           |          |     |
| VRF         |                | :                | default   |           |          |     |
| Rx Counters |                | :                |           |           |          |     |
| Hello       |                |                  |           |           | 4        |     |
| State       | Refresh        |                  |           |           | 0        |     |
| Join/Prune  |                |                  |           |           | 1        |     |
| RPadv       |                |                  |           |           | 0        |     |
| Graft       |                |                  |           |           | 0        |     |
| GraftAck    |                |                  |           |           | 0        |     |
| Assert      |                |                  |           |           | 0        |     |
| Bsm         |                |                  |           |           | 0        |     |
| Register    |                |                  |           |           | 0        |     |
| Register    | Stop           |                  |           |           | 0        |     |
| Register    | Drops(Register |                  | ACL       | hitcount) | 10       |     |
| Join/Prune  |                | Drops(RP ACL     | hitcount) |           | 5        |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 165

Tx Counters :

Hello
State Refresh
Join/Prune
RPadv
Graft
GraftAck
Assert
Bsm
Register
Register Stop

9
0
0
0
0
0
0
0
0
0

Invalid Rx Counters :

Hello
State Refresh
Join/Prune
RPadv
Graft
GraftAck
Assert
Bsm

0
0
0
0
0
0
0
0

show ip pim neighbor

Syntax

show ip pim neighbor [<IP-ADDR>]

[all-vrfs | vrf <VRF-NAME>] [vsx-peer]

Description

Shows PIM neighbor information. Optionally, you can specify display information by VRF. If no options are
specified, it shows information for the default VRF.

Parameters

all-vrfs

Selects all VRFs.

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Showing PIM neighbor information:

switch# show ip pim neighbor

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 166

PIM Neighbor
| VRF         |             | : default   |
| ----------- | ----------- | ----------- |
| IP Address  |             | : 40.0.0.44 |
| Interface   |             | : 1/1/1     |
| Up Time     | (sec)       | : 544       |
| Expire Time | (sec)       | : 80        |
| DR Priority |             | : 40        |
| show ip     | pim pending |             |
Syntax
| show ip pim | pending [<GROUP-ADDR>] |            |
| ----------- | ---------------------- | ---------- |
| [all-vrfs   | | vrf <VRF-NAME>]      | [vsx-peer] |
Description
ShowsthependingjoinsonaPIMrouter.OptionallyyoucanspecifydisplayinformationbyVRF.Ifno
optionsarespecified,itshowsinformationforthedefaultVRF.
UsethiscommandtodeterminewhatflowsarebeingrequestedonthePIMnetwork.Ifdataavailabilityfor
aflowisexpected,andajoinfortheflowispending,thetroubleshootingsearchmovestothesourceofthat
flow,sincetheroutersareverifiedtobeseeingtherequestfordata.
Commandcontext
Operator(>)orManager(#)
Parameters
<GROUP-ADDR>
SpecifiesagroupaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
all-vrfs
SelectsallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingpendingPIMjoins:
| switch# | show ip pim | pending |
| ------- | ----------- | ------- |
Join Pending
VRF : default
| Group | 234.0.20.4 |     |
| ----- | ---------- | --- |
| (*,G) | Pending    |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 167

|       |            | Incoming | Interface: |     | 1/1/32 |     |     |
| ----- | ---------- | -------- | ---------- | --- | ------ | --- | --- |
| Group | 234.0.20.5 |          |            |     |        |     |     |
(*,G) Pending
|       |            | Incoming | Interface: |     | 1/2/32 |     |     |
| ----- | ---------- | -------- | ---------- | --- | ------ | --- | --- |
| Group | 234.0.20.6 |          |            |     |        |     |     |
(*,G) Pending
|       |            | Incoming | Interface: |     | 1/1/32 |     |     |
| ----- | ---------- | -------- | ---------- | --- | ------ | --- | --- |
| Group | 234.0.20.7 |          |            |     |        |     |     |
(*,G) Pending
|         |     | Incoming     | Interface: |     | 1/1/2 |     |     |
| ------- | --- | ------------ | ---------- | --- | ----- | --- | --- |
| show ip | pim | rp-candidate |            |     |       |     |     |
Syntax
| show ip | pim rp-candidate |     |     | [all-vrfs | | vrf | <VRF-NAME>] | [vsx-peer] |
| ------- | ---------------- | --- | --- | --------- | ----- | ----------- | ---------- |
Description
ShowsthecandidateRPoperationalandconfigurationinformation.Optionally,youcanspecifydisplay
informationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
SelectsallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMRPcandidate:
switch#
|        | show      | ip pim       | rp-candidate |             | all-vrfs     |                   |     |
| ------ | --------- | ------------ | ------------ | ----------- | ------------ | ----------------- | --- |
| Status | and       | Counters-    |              | PIM-SM      | Candidate-RP | Information       |     |
| VRF    |           |              |              | : Green     |              |                   |     |
| C-RP   | Admin     | Status       |              | : This      | system       | is a Candidate-RP |     |
| C-RP   | Address   |              |              | : 10.1.1.27 |              |                   |     |
| C-RP   | Hold      | Time         |              | : 150       |              |                   |     |
| C-RP   | Advertise | Period       |              | : 60        |              |                   |     |
| C-RP   | Priority  |              |              | : 192       |              |                   |     |
| C-RP   | Source    | IP Interface |              | :           | Vlan10       |                   |     |
ProtocolIndependentMulticast-SparseMode(V4andV6)|168

| Group           | Address      | Group           | Mask          |                   |
| --------------- | ------------ | --------------- | ------------- | ----------------- |
| --------------- |              | --------------- |               |                   |
| 239.10.10.240   |              | 255.255.255.252 |               |                   |
| 236.0.0.0       |              | 255.255.255.0   |               |                   |
| VRF             |              |                 | : Red         |                   |
| C-RP            | Admin Status |                 | : This system | is a Candidate-RP |
| C-RP            | Address      |                 | : 20.1.1.27   |                   |
| C-RP            | Hold Time    |                 | : 150         |                   |
| C-RP            | Advertise    | Period          | : 60          |                   |
| C-RP            | Priority     |                 | : 192         |                   |
| C-RP            | Source       | IP Interface    | : Vlan20      |                   |
| Group           | Address      | Group           | Mask          |                   |
| --------------- |              | --------------- |               |                   |
| 239.10.10.240   |              | 255.255.255.252 |               |                   |
| 236.0.0.0       |              | 255.255.255.0   |               |                   |
| show ip         | pim          | rp-set          |               |                   |
Syntax
| show ip pim | rp-set | [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |
| ----------- | ------ | --------- | ----------------- | ---------- |
Description
ShowsthemulticastgroupsupportforboththelearnedC-RPassignmentsandanystaticallyconfiguredRP
assignments.Optionally,youcanspecifydisplayinformationbyVRF.Ifnooptionsarespecified,itshows
informationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
SelectsallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMRPsetinformation:
| switch# | show    | ip pim rp-set | all-vrfs |     |
| ------- | ------- | ------------- | -------- | --- |
| VRF:    | default |               |          |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 169

| Status          | and Counters    | - PIM-SM Static  | RP-Set Information |           |             |
| --------------- | --------------- | ---------------- | ------------------ | --------- | ----------- |
| Group           | Address Group   | Mask             | RP Address         | Override  |             |
| --------------- | --------------- |                  | ---------------    | --------  |             |
| 233.100.128.255 | 255.255.255.255 |                  | 100.10.10.1        | Yes       |             |
| 238.100.128.255 | 255.255.255.255 |                  | 100.10.10.3        | Yes       |             |
| Status          | and Counters    | - PIM-SM Learned | RP-Set Information |           |             |
| Group           | Address Group   | Mask             | RP Address         | Hold Time | Expire Time |
--------------- --------------- --------------- --------- -----------
| 223.2.2.34      | 255.0.0.0       |                  | 9.0.0.25           | 12        | 0           |
| --------------- | --------------- | ---------------- | ------------------ | --------- | ----------- |
| VRF:            | green           |                  |                    |           |             |
| Status          | and Counters    | - PIM-SM Static  | RP-Set Information |           |             |
| Group           | Address Group   | Mask             | RP Address         | Override  |             |
| --------------- | --------------- |                  | ---------------    | --------  |             |
| 226.102.128.255 | 255.255.255.255 |                  | 105.10.10.3        | Yes       |             |
| 234.102.128.255 | 255.255.255.255 |                  | 110.10.10.3        | Yes       |             |
| Status          | and Counters    | - PIM-SM Learned | RP-Set Information |           |             |
| Group           | Address Group   | Mask             | RP Address         | Hold Time | Expire Time |
--------------- --------------- --------------- --------- -----------
| 223.2.2.34 | 255.0.0.0     |         | 9.0.0.25 | 12  | 0   |
| ---------- | ------------- | ------- | -------- | --- | --- |
| 229.2.2.34 | 255.0.0.0     |         | 9.0.0.25 | 10  | 0   |
| show       | ip pim rp-set | learned |          |     |     |
Syntax
show ip pim rp-set learned [all-vrfs | vrf <VRF-NAME>] [vsx-peer]
Description
ShowsthemulticastgroupsupportfordynamicallylearnedRPassignments.Optionally,youcanspecify
displayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
SelectsallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMRPsetlearnedinformation:
ProtocolIndependentMulticast-SparseMode(V4andV6)|170

| switch# | show    | ip pim   | rp-set learned | all-vrfs                   |           |             |
| ------- | ------- | -------- | -------------- | -------------------------- | --------- | ----------- |
| VRF:    | default |          |                |                            |           |             |
| Status  | and     | Counters | - PIM-SM       | Learned RP-Set Information |           |             |
| Group   | Address | Group    | Mask           | RP Address                 | Hold Time | Expire Time |
--------------- --------------- --------------- --------- -----------
| 223.2.2.34 |         | 255.0.0.0 |          | 9.0.0.25                   | 12        | 0           |
| ---------- | ------- | --------- | -------- | -------------------------- | --------- | ----------- |
| VRF:       | green   |           |          |                            |           |             |
| Status     | and     | Counters  | - PIM-SM | Learned RP-Set Information |           |             |
| Group      | Address | Group     | Mask     | RP Address                 | Hold Time | Expire Time |
--------------- --------------- --------------- --------- -----------
| 223.2.2.34 |        | 255.0.0.0 |        | 9.0.0.25 | 12  | 0   |
| ---------- | ------ | --------- | ------ | -------- | --- | --- |
| 229.2.2.34 |        | 255.0.0.0 |        | 9.0.0.25 | 10  | 0   |
| show       | ip pim | rp-set    | static |          |     |     |
Syntax
| show ip | pim rp-set | static | [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |     |
| ------- | ---------- | ------ | --------- | ----------------- | ---------- | --- |
Description
ShowsthemulticastgroupsupportforstaticallyconfiguredRPassignments.Optionally,youcanspecify
displayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
SelectsallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMStaticRPsetinformation:
| switch# | show    | ip pim   | rp-set static | all-vrfs                  |          |     |
| ------- | ------- | -------- | ------------- | ------------------------- | -------- | --- |
| VRF:    | default |          |               |                           |          |     |
| Status  | and     | Counters | - PIM-SM      | Static RP-Set Information |          |     |
| Group   | Address | Group    | Mask          | RP Address                | Override |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 171

| --------------- |              | --------------- |          | ---------------           | -------- |
| --------------- | ------------ | --------------- | -------- | ------------------------- | -------- |
| 233.100.128.255 |              | 255.255.255.255 |          | 100.10.10.1               | Yes      |
| 238.100.128.255 |              | 255.255.255.255 |          | 100.10.10.3               | Yes      |
| VRF:            | green        |                 |          |                           |          |
| Status          | and Counters |                 | - PIM-SM | Static RP-Set Information |          |
| Group           | Address      | Group           | Mask     | RP Address                | Override |
| --------------- |              | --------------- |          | ---------------           | -------- |
| 226.102.128.255 |              | 255.255.255.255 |          | 105.10.10.3               | Yes      |
| 234.102.128.255 |              | 255.255.255.255 |          | 110.10.10.3               | Yes      |
| show ip         | pim          | rpf-override    |          |                           |          |
Syntax
| show ip pim | rpf-override |     | [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |
| ----------- | ------------ | --- | --------- | ----------------- | ---------- |
Description
ShowstheRPFoverrideconfiguration,whichcanbeusefulinformationwhentroubleshootingpotentialRPF
misconfigurations.Optionally,youcanspecifydisplayinformationbyVRF.Ifnooptionsarespecified,it
showsinformationforthedefaultVRF
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
Optional.ShowsPIMRPFoverrideinformationforallVRFs.
vrf <VRF-NAME>
Optional.ShowsPIMRPFoverrideinformationforaparticularVRF.Ifthe<VRF-NAME>isnotspecified,it
showsinformationforthedefaultVRF
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingPIMRPFoverride:
| switch#              | show ip      | pim | rpf-override       | all-vrfs |     |
| -------------------- | ------------ | --- | ------------------ | -------- | --- |
| VRF                  |              |     | : default          |          |     |
| Static               | RPF Override |     |                    |          |     |
| Multicast            | Source       | RPF | IP Address         |          |     |
| -------------------- |              |     | ------------------ |          |     |
| 10.0.0.2/32          |              |     | 1.1.1.1            |          |     |
ProtocolIndependentMulticast-SparseMode(V4andV6)|172

| VRF                  |                     | : green            |        |
| -------------------- | ------------------- | ------------------ | ------ |
| Static               | RPF Override        |                    |        |
| Multicast            | Source              | RPF IP Address     |        |
| -------------------- |                     | ------------------ |        |
| 10.0.0.2/32          |                     | 1.1.1.1            |        |
| 10.1.1.1/32          |                     | 1.1.1.2            |        |
| show                 | ip pim rpf-override |                    | source |
Syntax
| show ip   | pim rpf-override | source      | <IP-ADDR>  |
| --------- | ---------------- | ----------- | ---------- |
| [all-vrfs | | vrf            | <VRF-NAME>] | [vsx-peer] |
Description
ShowstheRPFoverrideconfigurationforthespecifiedsource.Optionally,youcanspecifydisplay
informationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
source <IP-ADDR>
SpecifiestheRPFsourceaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
all-vrfs
SelectsallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingPIMRPFoverridesource:
switch#
|           | show ip pim  | rpf-override   | source 10.0.0.2 |
| --------- | ------------ | -------------- | --------------- |
| VRF       |              | : default      |                 |
| Static    | RPF Override |                |                 |
| Multicast | Source       | RPF IP Address |                 |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 173

| -------------------- |     | ------------------ |     |     |
| -------------------- | --- | ------------------ | --- | --- |
| 10.0.0.2             |     | 1.1.1.1            |     |     |
ShowingPIMRPFoverridesourceforallVRFs:
| switch#              | show ip pim  | rpf-override       | source 10.0.0.2 | all-vrfs |
| -------------------- | ------------ | ------------------ | --------------- | -------- |
| VRF                  |              | : default          |                 |          |
| Static               | RPF Override |                    |                 |          |
| Multicast            | Source RPF   | IP Address         |                 |          |
| -------------------- |              | ------------------ |                 |          |
| 10.0.0.2             |              | 1.1.1.1            |                 |          |
| VRF                  |              | : green            |                 |          |
| Static               | RPF Override |                    |                 |          |
| Multicast            | Source RPF   | IP Address         |                 |          |
| -------------------- |              | ------------------ |                 |          |
| 10.0.0.2             |              | 1.1.1.1            |                 |          |
sources-per-group
Syntax
| sources-per-group    | <limit> |         |     |     |
| -------------------- | ------- | ------- | --- | --- |
| no sources-per-group |         | <limit> |     |     |
Description
Configuresthetotalnumberofsourcesallowedforagroupontherouter.Bydefault,thereisnolimiton
thenumberofsourcesforagroup.Whenthenumberofsourcesforagroupexceedstheconfiguredlimit,
multicasttrafficfromadditionalsourceswillbedropped.
Thenoformofthiscommandremovesthecurrentlyconfiguredlimitvalue.
Commandcontext
config-pim
Parameters
<limit>
Specifiesthevaluetobeconfiguredasthesourcesallowedpergroup.Range:1to4294967295.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Flowsexceedingthelimitwillbeprogrammedasabridgeentryandwillnothavetheoutgoinginterfaceslist
populated.Thisconfigurationdoesnotallownewsourcesforthegroup.Atthetimeofconfiguration,ifthe
devicehasmoresourcesforthegivengroupthantheconfiguredvalue,alreadyallowedsourcescontinueto
existuntiltheyareremoved.
TheflowsareprogrammedintheHWonaFCFSbasis.Therecouldbescenarioswheretheflowisforwarded
inneighborrouter,butitmaynotbeforwardedonthecurrentrouterbecauseofexceedingthelimits
configuredonthecurrentrouter.Insuchcases,itisrecommendedtoconfigurehigherlimitstoavoidtraffic
outage.
ProtocolIndependentMulticast-SparseMode(V4andV6)|174

Examples
Configuringandremovingthesourcesallowedpergroup:
switch(config)#
|                     |     | router            | pim               |     |
| ------------------- | --- | ----------------- | ----------------- | --- |
| switch(config-pim)# |     | sources-per-group |                   | 4   |
| switch(config-pim)# |     | no                | sources-per-group |     |
spt-threshold
Syntax
spt-threshold
no spt-threshold
Description
Enablestheroutertoswitchthemulticasttrafficflowstotheshortestpathtree.Defaultisenabled.
Thenoformofthiscommanddisablestheroutersabilitytoswitchthemulticasttrafficflowstotheshortest
pathtree.
Toapplythisconfigurationauserneedstoapplydisable/enablePIMglobally.
Commandcontext
config-pim
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
EnablinganddisablingtheSPTthreshold:
| switch(config)#     |          | router        | pim           |     |
| ------------------- | -------- | ------------- | ------------- | --- |
| switch(config-pim)# |          | spt-threshold |               |     |
| switch(config-pim)# |          | no            | spt-threshold |     |
| PIM-SM              | commands |               | for IPv6      |     |
| accept-register     |          | access-list   |               |     |
Syntax
| accept-register    |     | access-list | <ACL-RULE> |     |
| ------------------ | --- | ----------- | ---------- | --- |
| no accept-register |     | access-list | <ACL-RULE> |     |
Description
ConfiguresACLonRPtofilterPIMRegisterpacketsfromunauthorizedsources.TheACLspecifiedwill
containthe(S,G)trafficinregisterpacketstopermittedordenied.
ThenoformofthiscommandremovesthecurrentlyconfiguredACLrule.
Commandcontext
config-pim6
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 175

Parameters

<ACL-RULE>

Specifies the ACL rule name.

Authority

Administrators or local user group members with execution rights for this command.

Usage

When register ACL is associated with a PIM Router, PIM protocol will store the source and destination
address details along with the action (permit or deny).

Upon receiving the register messages, a look up is made to check if the S and G in the packet is in the
permitted list. If there is no match or if there is a deny rule match, a register stop message is immediately
sent and the packet is dropped and no further action is taken. Permitted packets will go through the normal
flow.

Loopback interfaces are special interfaces where only unicast PIM messages are updated. This includes
Register, Register Stop, and Candidate RP Advertisements.

When a loopback interface is configured as the RP, the ACL drop counters will be updated on the interface
on which the packets are received.

Examples

Configuring ACL on RP with an ACL rule named pim_regv6_acl:

switch(config)# access-list ipv6 pim_regv6_acl
switch(config-acl-ipv6)# 10 permit any 20.::1 ff1e::1
switch(config-acl-ipv6)# 20 deny any 30::1 ff1e::3
switch(config)# router pim6
switch(config-pim6)# accept-register access-list pim_regv6_acl

accept-rp

Syntax

accept-rp <IPv6-ADDR> access-list <ACL-RULE>
no accept-rp <IPv6-ADDR> access-list <ACL-RULE>

Description

Enables PIM router to filter PIM join/prune messages destined for a specific RP and specific groups. The ACL
specifies the group addresses which are allowed or denied. Up to 8 RP addresses and group ACL can be
associated with the PIM router.

The no form of this command removes the currently configured ACL rule.

Command context

config-pim6

Parameters

<IPv6-ADDR>

Specifies an address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F.

<ACL-RULE>

Specifies the ACL rule name.

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 176

Authority

Administrators or local user group members with execution rights for this command.

Usage

PIM will store the accepted RP address and the associated group ACL. When a join or prune message is
received, a RP look up is made for the packet. If the RP is in the configured list and if the group in the
join/prune packet is allowed in the ACL, the packet is allowed. Otherwise the packet is dropped.

To allow join/prune message from any groups, group address in the ACL can be wild-carded. In this case,
only RP address check is performed.

This command impacts only (*,G) join/prune messages. If there are any existing flows, the user will need to
disable and enable PIM on the interface to apply the ACL.

Loopback interfaces are special interfaces where only unicast PIM messages are updated. This includes
Register, Register Stop, and Candidate RP Advertisements.

When a loopback interface is configured as the RP, the ACL drop counters will be updated on the interface
on which the packets are received.

If there is an active flow which is in the SPT, the traffic flow through the SPT will continue. Only (*,G) join/prune
messages are dropped. (S,G) join/prune messages will not be impacted.

Examples

Configuring ACL on RP with an ACL rule named pim_rpv6_grp_acl to filter join/prune messages:

switch(config-pim)# access-list ip pim_rpv6_grp_acl
switch(config-acl-ipv6)# 10 permit any any ff2e::2/64
switch(config-acl-ipv6)# 20 permit any any ff1e::1/64
switch(config-acl-ipv6)# router pim6
switch(config-pim6)# accept-rp 30::1 access-list pim_rpv6_grp_acl

bsr-candidate bsm-interval

Syntax

bsr-candidate bsm-interval <INTERVAL-VALUE>
no bsr-candidate bsm-interval

Description

Configures the interval in seconds to send periodic RP-Set messages to all PIM-SM interfaces on a router
that operates as the BSR in a domain. This setting must be smaller than the rp-candidate hold-time
settings (range of 30 to 255; default 150) configured in the RPs operating in the domain.

The no form of this command removes the currently configured value and sets it to the default of 60
seconds.

Command context

config-pim6

Parameters

<INTERVAL-VALUE>

Specifies the BSR-candidate BSM interval in seconds. Range: 5 to 300. Default: 60.

Authority

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

177

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ConfiguringandremovingBSR-candidateBSM-interval:
| switch(config)#      | router           | pim6             |              |     |
| -------------------- | ---------------- | ---------------- | ------------ | --- |
| switch(config-pim6)# |                  | bsr-candidate    | bsm-interval | 150 |
| switch(config-pim6)# |                  | no bsr-candidate | bsm-interval |     |
| bsr-candidate        | hash-mask-length |                  |              |     |
Syntax
| bsr-candidate    | hash-mask-length | <LENGTH-VALUE> |     |     |
| ---------------- | ---------------- | -------------- | --- | --- |
| no bsr-candidate | hash-mask-length |                |     |     |
Description
ControlsthedistributionofmulticastgroupsamongtheC-RP,inadomainwherethereisoverlapping
coverageofthegroupsamongtheRPs.Thisvaluespecifiesthelength(numberofsignificantbits)when
allocatingthisdistribution.Alongerhash-mask-lengthresultsinfewermulticastgroups,foreachblockof
groupaddressesassignedtotheRPs.MultipleblocksofaddressesassignedtoeachC-RPresultsinwider
dispersalofaddresses.Includesenhancedload-sharingforthemulticasttrafficforthedifferentgroupsthat
areusedinthedomainatthesametime.
Thenoformofthiscommandremovescurrentlyconfiguredvalueandsetstothedefaultof126.
Commandcontext
config-pim6
Parameters
<LENGTH-VALUE>
Specifiesthelength(inbits)ofthehashmask.Range:1to128.Default:126.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ConfiguringandremovingtheBSR-candidatehash-mask-length:
| switch(config)#      | router   | pim6             |                  |     |
| -------------------- | -------- | ---------------- | ---------------- | --- |
| switch(config-pim6)# |          | bsr-candidate    | hash-mask-length | 4   |
| switch(config-pim6)# |          | no bsr-candidate | hash-mask-length |     |
| bsr-candidate        | priority |                  |                  |     |
Syntax
| bsr-candidate    | priority | <PRIORITY-VALUE> |     |     |
| ---------------- | -------- | ---------------- | --- | --- |
| no bsr-candidate | priority |                  |     |     |
Description
ProtocolIndependentMulticast-SparseMode(V4andV6)|178

Configures the priority to apply to the router when a BSR election process occurs in the PIM-SM domain.
The candidate with the highest priority becomes the BSR for the domain. If the highest priority is shared by
multiple routers, the candidate having the highest IP address becomes the BSR of the domain. Zero (0) is
the lowest priority. To make BSR selection easily predictable, use this command to assign a different priority
to each candidate BSR in the PIM-SM domain.

The no form of this command removes currently configured value and sets to the default of 0.

Command context

config-pim6

Parameters

<PRIORITY-VALUE>

Specifies the priority for the Candidate Bootstrap router. Range: 0 to 255. Default: 0.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configuring and removing the BSR-candidate priority:

switch(config)# router pim6
switch(config-pim6)# bsr-candidate priority 250
switch(config-pim6)# no bsr-candidate priority

bsr-candidate source-ip-interface

Syntax

bsr-candidate source-ip-interface <INTERFACE-NAME>
no bsr-candidate source-ip-interface <INTERFACE-NAME>

Description

Configures the router to advertise itself as a candidate PIM-SM BSR on the interface specified, and enables
BSR candidate operation. The result makes the router eligible to be elected as the BSR for the PIM-SM
domain in which it operates. One BSR candidate interface is allowed per-router.

The no form of this command removes the Candidate BSR configuration.

Command context

config-pim6

Parameters

<INTERFACE-NAME>

Specifies the interface to use as a source for Candidate-BSR router IP address. Interface can be a VLAN
interface, routed interface, or LAG. PIM-SM must be enabled on this interface with the command ipv6
pimv6-sparse enable.

Authority

Administrators or local user group members with execution rights for this command.

Example

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

179

On the 6400 Switch Series, interface identification differs.

Configuring and removing the BSR-candidate interface:

switch(config)# router pim6
switch(config-pim6)# bsr-candidate source-ip-interface 1/1/4
switch(config-pim6)# no rp-candidate source-ip-interface 1/1/4

disable

Syntax

disable

Description

Disables PIMv6 globally on the router.

Using the disable command will cause all the multicast routes to be erased from hardware.

Command context

config-pim6

Authority

Administrators or local user group members with execution rights for this command.

Example

Disabling PIM router:

switch(config)# router pim6
switch(config-pim6)# disable

enable

Syntax

enable

Description

Enables PIMv6 globally on the router.

Command context

config-pim6

Authority

Administrators or local user group members with execution rights for this command.

Example

Enabling PIM router:

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 180

| switch(config)# | router | pim6 |     |
| --------------- | ------ | ---- | --- |
switch(config-pim6)#
enable
| ipv6 pim6-sparse |     | {enable|disable} |     |
| ---------------- | --- | ---------------- | --- |
Syntax
| ipv6 pim6-sparse | {enable | | disable} |     |
| ---------------- | ------- | ---------- | --- |
Description
EnablesordisablesPIM-SMonthecurrentinterface.PIM-SMisdisabledbydefaultonaninterface.AnIPv6
addressmustbeconfiguredontheinterfacetoenablePIM-SM.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
enable
EnablesPIM-SMontheinterface.IPv6addressmustbeconfiguredontheinterfacetoenablePIM-SM
| (usetheipv6 | <X:X::X:X/M>command). |     |     |
| ----------- | --------------------- | --- | --- |
address
disable
DisablesPIMSMontheinterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablinganddisablingPIM-SMonaninterface:
| switch(config)#         | interface | vlan40           |             |
| ----------------------- | --------- | ---------------- | ----------- |
| switch(config-if-vlan)# |           | ipv6 address     | 2001::01/64 |
| switch(config-if-vlan)# |           | ipv6 pim6-sparse | enable      |
| switch(config-if-vlan)# |           | ipv6 pim6-sparse | disable     |
| ipv6 pim6-sparse        |           | bfd              |             |
Syntax
| ipv6 pim6-sparse    | bfd [disable] |     |     |
| ------------------- | ------------- | --- | --- |
| no ipv6 pim6-sparse | bfd           |     |     |
Description
ConfiguresBFDonaper-interfacebasisforaninterfaceassociatedwiththePIMprocess.
ThenoformofthiscommandremovestheBFDconfigurationontheinterfaceandsetsittothedefault
configuration.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 181

IfBFDisenabledglobally,itwillbeenabledbydefaultonallinterfaces.Theonlyexceptioniswhenitisdisabled
specificallyonaninterfaceusingtheipv6 pim6-sparse bfd disablecommand.
IfBFDisdisabledglobally,itwillbedisabledbydefaultonallinterfaces.Theonlyexceptioniswhenitisenabled
| specificallyonaninterfaceusingtheipv6 |     | pim6-sparse | bfdcommand. |
| ------------------------------------- | --- | ----------- | ----------- |
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
disable
DisablestheBFDconfigurationontheinterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingtheBFDconfigurationontheinterface:
| switch(config)#         | interface | vlan 40          |     |
| ----------------------- | --------- | ---------------- | --- |
| switch(config-if-vlan)# |           | ipv6 pim6-sparse | bfd |
DisablingtheBFDconfigurationontheinterface:
| switch(config-if-vlan)# |     | ipv6 pim6-sparse | bfd disable |
| ----------------------- | --- | ---------------- | ----------- |
RemovingtheBFDconfigurationontheinterface:
| switch(config-if-vlan)# |             | no ipv6 pim6-sparse | bfd |
| ----------------------- | ----------- | ------------------- | --- |
| ipv6 pim6-sparse        | dr-priority |                     |     |
Syntax
| ipv6 pim6-sparse    | dr-priority | <PRIORITY-VALUE> |     |
| ------------------- | ----------- | ---------------- | --- |
| no ipv6 pim6-sparse | dr-priority |                  |     |
Description
Changestherouterpriorityforthedesignatedrouter(DR)electionprocessinthecurrentinterface.
Anumericallyhighervaluemeansahigherpriority.Ifmultipleroutessharethehighestpriority,therouter
withthehighestIPaddressisselectedastheDR.
Thenoformofthiscommandremovescurrentlyconfiguredvalueandsetstothedefaultof1.
Commandcontext
config-if
config-if-vlan
config-lag-if
ProtocolIndependentMulticast-SparseMode(V4andV6)|182

Parameters

<PRIORITY-VALUE>

Specifies the priority value to use on the interface in the DR election process. Range: 0 to 4294967295.
Default: 1.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring and removing the interface priority value:

switch(config)# interface vlan 40
switch(config-if-vlan)# ipv6 pim6-sparse dr-priority 4444
switch(config-if-vlan)# no ipv6 pim6-sparse dr-priority

ipv6 pim6-sparse hello-delay

Syntax

ipv6 pim6-sparse hello-delay <DELAY-VALUE>
no ipv6 pim6-sparse hello-delay

Description

Configures the maximum time in seconds before the router actually transmits the initial PIM hello message
on the current interface.

The no form of this command removes currently configured value and sets to the default of 5 seconds.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

<DELAY-VALUE>

Specifies the hello-delay in seconds, which is the maximum time before a triggered PIM Hello message is
transmitted on this interface. Range: 0 to 5. Default: 5.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n In cases where a new interface activates connections with multiple routers. If all the connected routers

sent hello packets at the same time, the receiving router could become momentarily overloaded.

n This command randomizes the transmission delay to a time between zero and the hello delay setting.

Using zero means no delay. After the router sends the initial hello packet to a newly detected interface, it
sends subsequent hello packets according to the current hello interval setting.

Example

Configuring and removing hello-delay interface:

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

183

| switch(config)# |     | interface | vlan 40 |     |     |     |
| --------------- | --- | --------- | ------- | --- | --- | --- |
switch(config-if-vlan)#
|                         |                |                | ipv6 pim6-sparse    |     | hello-delay | 4   |
| ----------------------- | -------------- | -------------- | ------------------- | --- | ----------- | --- |
| switch(config-if-vlan)# |                |                | no ipv6 pim6-sparse |     | hello-delay |     |
| ipv6 pim6-sparse        |                | hello-interval |                     |     |             |     |
| ipv6 pim6-sparse        | hello-interval |                | <INTERVAL-VALUE>    |     |             |     |
| no ipv6 pim6-sparse     |                | hello-interval |                     |     |             |     |
Description
ConfiguresthefrequencyatwhichtheroutertransmitsPIMhellomessagesonthecurrentinterface.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetstothedefaultof30seconds.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<INTERVAL-VALUE>
SpecifiesthefrequencyatwhichPIMHellomessagesaretransmittedonthisinterfaceinseconds.Range:
5to300.Default:30.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
n Therouteruseshellopacketstoinformneighborroutersofitspresence.
n Therouteralsousesthissettingtocomputethehelloholdtime,whichisincludedinhellopacketssentto
neighborrouters.
n Helloholdtimetellsneighborroutershowlongtowaitforthenexthellopacketfromtherouter.If
anotherpacketdoesnotarrivewithinthattime,therouterremovestheneighboradjacencyonthat
interfacefromthePIMadjacencytable,whichremovesanyflowsrunningonthatinterface.
Shorteningthehellointervalreducesthehelloholdtime.Iftheydonotreceiveanewhellopacketwhen
n
expected,itchangeshowquicklyotherroutersstopsendingtraffictotherouter.
Example
Configuringandremovingsparsehello-interval:
| switch(config-if)# |     | ipv6      | pim6-sparse      | hello-interval |                | 60  |
| ------------------ | --- | --------- | ---------------- | -------------- | -------------- | --- |
| switch(config-if)# |     | no        | ipv6 pim6-sparse |                | hello-interval |     |
| ipv6 pim6-sparse   |     | ipv6-addr |                  |                |                |     |
Syntax
| ipv6 pim6-sparse    | ipv6-addr |           | {<IPv6-ADDR-VALUE> |     | | any} |     |
| ------------------- | --------- | --------- | ------------------ | --- | ------ | --- |
| no ipv6 pim6-sparse |           | ipv6-addr |                    |     |        |     |
Description
ProtocolIndependentMulticast-SparseMode(V4andV6)|184

Enables the router to dynamically determine the source IP address to use for PIM-SM packets sent from the
interface or to use the specific IPv6 address.

The no form of this command removes the currently configured value and sets to the default of any.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

<IP-ADDR-VALUE>

Specifies the source IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is
a hexadecimal number from 0 to F.

any

Specifies dynamically determining the source IP from the current IP address of the interface.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring and removing source IP address:

switch(config)# interface vlan40
switch(config-if-vlan)# ipv6 pim6-sparse ipv6-addr 2001::02
switch(config-if-vlan)# no ipv6 pim6-sparse ipv6-addr

ipv6 pim6-sparse lan-prune-delay

Syntax

ipv6 pim6-sparse lan-prune-delay
no ipv6 pim6-sparse lan-prune-delay

Description

Enables the LAN prune delay option on the current interface. The default is enabled.

With LAN-prune-delay enabled, the router informs downstream neighbors how long it will wait before
pruning a flow after receiving a prune request. Other downstream routers on the same interface must send
a join to override the prune before the LAN-prune-delay time to continue the flow. Prompts any
downstream neighbors with multicast receivers continuing to belong to the flow to reply with a join. If no
joins are received after the LAN-prune-delay period, the router prunes the flow. The propagation-delay and
override-interval settings determine the LAN-prune-delay setting.

The no form of this command disables the LAN prune delay option.

Command context

config-if
config-if-vlan
config-lag-if

Authority

Administrators or local user group members with execution rights for this command.

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

185

Example

Enabling and disabling the LAN prune delay:

switch(config)# interface vlan40
switch(config-if-vlan)# ipv6 pim6-sparse lan-prune-delay
switch(config-if-vlan)# no ipv6 pim6-sparse lan-prune-delay

ipv6 pim6-sparse override-interval

Syntax

ipv6 pim6-sparse override-interval <INTERVAL-VALUE>
no ipv6 pim6-sparse override-interval

Description

Configures the override interval that gets inserted into the Override Interval field of a LAN Prune Delay
option.

The no form of this command removes the currently configured value and sets the value to the default of
2500 ms.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

<INTERVAL-VALUE>

Specifies the override interval of a LAN Prune Delay option in ms. Range: 500 to 6000. Default: 2500.

Authority

Administrators or local user group members with execution rights for this command.

Usage

A router sharing a VLAN with other multicast routers uses the override-interval value along with the
propagation-delay value to compute the lan-prune-delay setting. The setting specifies how long to wait for
a PIM-SM join after receiving a prune packet from downstream for a particular multicast group.

Example scenario:

A network may have multiple routers sharing VLAN X. When an upstream router is forwarding traffic from
multicast group X to VLAN Y, if one of the routers on VLAN Y does not want this traffic, it issues a prune
response to the upstream neighbor. The upstream neighbor then goes into a prune pending state for group
X on VLAN Y. During this period, the upstream neighbor continues to forward the traffic. During the
pending period, another router on VLAN Y can send a group X join to the upstream neighbor. If this
happens, the upstream neighbor drops the prune pending status and continues forwarding the traffic. But
if no routers on the VLAN send a join, the upstream router prunes.

Example

Configuring and removing the override interval:

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 186

| switch(config)# | interface | vlan40 |     |     |
| --------------- | --------- | ------ | --- | --- |
switch(config-if-vlan)#
|                         |                   | ipv6 pim6-sparse    | override-interval | 4000 |
| ----------------------- | ----------------- | ------------------- | ----------------- | ---- |
| switch(config-if-vlan)# |                   | no ipv6 pim6-sparse | override-interval |      |
| ipv6 pim6-sparse        | propagation-delay |                     |                   |      |
Syntax
| ipv6 pim6-sparse    | propagation-delay | <DELAY-VALUE> |     |     |
| ------------------- | ----------------- | ------------- | --- | --- |
| no ipv6 pim6-sparse | propagation-delay |               |     |     |
Description
ConfiguresthepropagationdelaythatgetsinsertedintotheLANprunedelayfieldofaLANPruneDelay
option.
Thenoformofthiscommandremovescurrentlyconfiguredvalueandsetstothedefaultof500ms.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<DELAY-VALUE>
Specifiesthepropagationdelayvalueinms.Range:250to2000.Default:500.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringandremovingthepropagationdelay:
| switch(config)#         | interface | vlan 40             |                   |     |
| ----------------------- | --------- | ------------------- | ----------------- | --- |
| switch(config-if-vlan)# |           | ipv6 pim6-sparse    | propagation-delay | 400 |
| switch(config-if-vlan)# |           | no ipv6 pim6-sparse | propagation-delay |     |
join-prune-interval
Syntax
| join-prune-interval | <INTERVAL-VALUE> |     |     |     |
| ------------------- | ---------------- | --- | --- | --- |
no join-prune-interval
Description
Configuresthefrequencyatwhichtherouterwillsendperiodicjoinorprune-intervalmessages.
Thenoformofthiscommandsetstheintervaltothedefaultvalueof60seconds.
Commandcontext
config-pim6
Parameters
<INTERVAL-VALUE>
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 187

Specifiesthejoin-prune-intervalinseconds.Range5to65535.Default:60.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringjoinpruneinterval:
| switch(config)#      |             | router              | pim6                |     |
| -------------------- | ----------- | ------------------- | ------------------- | --- |
| switch(config-pim6)# |             | join-prune-interval |                     | 400 |
| switch(config-pim6)# |             | no                  | join-prune-interval |     |
| no ipv6              | pim6-sparse |                     |                     |     |
Syntax
| no ipv6 | pim6-sparse |     |     |     |
| ------- | ----------- | --- | --- | --- |
Description
RemovesallthePIM-SMrelatedIPv6configurationsfortheinterface.
Commandcontext
config-if
config-if-vlan
config-lag-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
RemovingPIM-SMconfiguration:
| switch(config)#         |      | interface | vlan40              |     |
| ----------------------- | ---- | --------- | ------------------- | --- |
| switch(config-if-vlan)# |      |           | no ipv6 pim6-sparse |     |
| router                  | pim6 |           |                     |     |
Syntax
| router    | pim6 [vrf | <VRF-NAME>] |     |     |
| --------- | --------- | ----------- | --- | --- |
| no router | pim6 [vrf | <VRF-NAME>] |     |     |
Description
ChangesthecurrentcontexttothePIMv6configurationcontext.IfnoVRFisspecified,thedefaultVRFis
assumed.
ThenoformofthiscommandremovesthePIMconfigurationfromthespecifiedcontextorthedefaultVRF.
Commandcontext
config
Parameters
ProtocolIndependentMulticast-SparseMode(V4andV6)|188

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring default router PIM:

switch(config)# router pim6
switch(config-pim6)#

Configuring specified router PIM:

switch(config)# router pim6 vrf Green
switch(config-pim6)#

Removing router PIM:

switch(config)# no router pim6

rp-address <IPv6-ADDR>

Syntax

rp-address <IPv6-ADDR> [<GRP-ADDR/GRP-MASK>] [override]
no rp-address <IPv6-ADDR> [<GRP-ADDR/GRP-MASK>] [override]

Description

Statically configures the router as the RP for a specified multicast group or range of multicast groups. This
must be configured on all PIM-SM routers in the domain. If group address is not specified, it applies to all
IPv6 multicast addresses.

The no form of this command removes static RP configuration and its precedence.

Command context

config-pim

Parameters

<IPv6-ADDR>

Specifies an address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F.

<GRP-ADDR>

Specifies the range of multicast group addresses in IPv6 format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a hexadecimal number from 0 to F.

<GRP-MASK>

Specifies the number of bits in the address mask in CIDR format (x), where x is a decimal number from 0
to 128.
override

Specifies higher precedence to static RP over Candidate RP.

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

189

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
WhereastaticRPandaC-RPareconfiguredtosupportthesamemulticastgroupsandthemulticastgroup
maskforthestaticRPisequaltoorgreaterthanthesamemaskfortheapplicableC-RPs,thiscommand
assignsthehigherprecedencetothestaticRP,resultingintheC-RPoperatingonlyasabackupRPforthe
configuredgroup.Withoutoverride,theC-RPhasprecedenceoverastaticRPconfiguredforthesame
multicastgrouporgroups.
Examples
| switch(config)#      | router       | pim6          |                       |              |           |
| -------------------- | ------------ | ------------- | --------------------- | ------------ | --------- |
| switch(config-pim6)# |              | rp-address    | 2001::01 ff08::1:3/64 |              | ovverride |
| switch(config-pim6)# |              | rp-address    | 2002::02 ff08::1:4/64 |              |           |
| switch(config-pim6)# |              | no rp-address | 2002::02              | ff08::1:4/64 |           |
| rp-candidate         | group-prefix |               |                       |              |           |
Syntax
| rp-candidate    | group-prefix | <GRP-ADDR/GRP-MASK> |     |     |     |
| --------------- | ------------ | ------------------- | --- | --- | --- |
| no rp-candidate | group-prefix | <GRP-ADDR/GRP-MASK> |     |     |     |
Description
AddsmulticastgroupaddresstothecurrentCandidateRendezvousPoint(C-RP)configuration.
ThenoformofthiscommandremovesC-RPmulticastgroupaddress.
Commandcontext
config-pim6
Parameters
<GRP-ADDR>
SpecifiesthemulticastgroupaddressinIPv6format(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),
wherexisahexadecimalnumberfrom0toF.
<GRP-MASK>
SpecifiesthenumberofbitsintheaddressmaskinCIDRformat(x),wherexisadecimalnumberfrom0
to128.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringandremovingcandidategroupprefix:
| switch(config)#      | router | pim6         |              |              |     |
| -------------------- | ------ | ------------ | ------------ | ------------ | --- |
| switch(config-pim6)# |        | rp-candidate | group-prefix | ff08::1:3/64 |     |
switch(config-pim6)#
|              |           | no rp-candidate | group-prefix | ff08::1:3/64 |     |
| ------------ | --------- | --------------- | ------------ | ------------ | --- |
| rp-candidate | hold-time |                 |              |              |     |
ProtocolIndependentMulticast-SparseMode(V4andV6)|190

Syntax
| rp-candidate    | hold-time | <TIME-VALUE> |     |     |
| --------------- | --------- | ------------ | --- | --- |
| no rp-candidate | hold-time |              |     |     |
Description
Changesthehold-timeaC-RPincludesinitsadvertisementstotheBSR.
Hold-timeisincludedintheadvertisementstheC-RPperiodicallysendstotheelectedBSRforthedomain.
AlsoupdatestheBSRonhowlongtowaitafterthelastadvertisementfromthereportingRPbefore
assumingithasbecomeunavailable.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetsittothedefaultvalue150
seconds.
Commandcontext
config-pim6
Parameters
<TIME-VALUE>
Specifiesthehold-timevalueinsecondstobesentinC-RP-Advmessages.Range:30-255.Default:150.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Settingandremovingthecandidateholdtime:
| switch(config)#      |          | router pim6     |           |     |
| -------------------- | -------- | --------------- | --------- | --- |
| switch(config-pim6)# |          | rp-candidate    | hold-time | 250 |
| switch(config-pim6)# |          | no rp-candidate | hold-time |     |
| rp-candidate         | priority |                 |           |     |
Syntax
| rp-candidate    | priority | <PRIORITY-VALUE> |     |     |
| --------------- | -------- | ---------------- | --- | --- |
| no rp-candidate | priority |                  |     |     |
Description
ChangesthecurrentprioritysettingforaC-RP.WheremultipleC-RPconfigurationsareusedtosupportthe
samemulticastgroups,thecandidatehavingthehighestpriorityiselected.Zero(0)isthehighestpriority,
and255isthelowestpriority.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetsittothedefaultof192.
Commandcontext
config-pim
Parameters
<PRIORITY-VALUE>
SpecifiesthepriorityvaluefortheCandidate-RProuter.Range:0to255.Default:192.
Authority
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 191

Administrators or local user group members with execution rights for this command.

Example

Configuring and removing candidate priority:

switch(config)# router pim6
switch(config-pim6)# rp-candidate priority 250
switch(config-pim6)# no rp-candidate priority

rp-candidate source-ip-interface

Syntax

rp-candidate source-ip-interface <INTERFACE-NAME> [group-prefix <GRP-ADDR/GRP-MASK>]
no rp-candidate source-ip-interface <INTERFACE-NAME> [group-prefix <GRP-ADDR/GRP-MASK>]

Description

Enables the Candidate Rendezvous Point (C-RP) operation, and configures the router to advertise itself as a
C-RP to the Bootstrap Router (BSR) for the current domain.

This step includes the option to allow the C-RP to be a candidate for all possible multicast groups, or for up
to four multicast groups, or ranges of groups. If group-prefix is not given, it considers for all multicast group
addresses.

The no form of this command removes the C-RP configuration.

Command context

config-pim6

Parameters

<INTERFACE-NAME>

Specifies the interface to use as a source for the C-RP router IP address.

group-prefix <GRP-ADDR/GRP-MASK>

Specifies the multicast group address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),
where x is a hexadecimal number from 0 to F. And the number of bits in the address mask in CIDR
format (x), where x is a decimal number from 0 to 128.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring a C-RP using VLAN 40 as the source for the C-RP router IP address and associating the
ff08::1:3/64 multicast group with the C-RP router:

switch(config)# router pim6
switch(config-pim6)# rp-candidate source-ip-interface vlan40 group-prefix
ff08::1:3/64

Configuring a C-RP using loopback1 as the source for the C-RP router IP address and associating the
ff08::1:3/64 multicast group with the C-RP router:

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 192

switch(config)# router pim6
switch(config-pim6)# rp-candidate source-ip-interface loopback1 group-prefix
ff08::1:3/64

Removing the candidate source IP interface:

switch(config-pim6)# no rp-candidate source-ip-interface vlan20

rpf-override

Syntax

rpf-override <SRC-ADDR/SRC-MASK> <RPF-ADDR|INTERFACE-NAME>
no rpf-override <SRC-ADDR/SRC-MASK> <RPF-ADDR|INTERFACE-NAME>

Description

The Reverse Path Forward (RPF) override, allows overriding the normal RPF lookup mechanism, and
indicates to the router that it may accept multicast traffic on an interface other than the one that the RPF
lookup mechanism would normally select. This includes accepting traffic from an invalid source IP address
for the subnet or VLAN that is directly connected to the router. Traffic may also be accepted from a valid
PIM neighbor that is not on the reverse path towards the source of the received multicast traffic.

The no form of this command removes currently configured RPF entry.

Command context

config-pim6

Parameters

<SRC-ADDR>

Specifies the multicast source address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),
where x is a hexadecimal number from 0 to F.

<SRC-MASK>

Specifies the number of bits in the address mask in CIDR format (x), where x is a decimal number from 0
to 128.
<RPF-ADDR>

Specifies the RPF address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F.

<INTERFACE-NAME>

Specifies the RPF interface name.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n Reverse Path Forward (RPF) checking is a core multicast routing mechanism. The RPF ensures that the
multicast traffic received arrives on the expected router interface before further processing. If the RPF
check fails for a multicast packet, the packet is discarded. For multicast traffic flow that arrives on the
SPT, the expected incoming interface for a given source or group is the interface towards the source
address of the traffic (determined by the unicast routing system). For traffic arriving on the RP tree, the
expected incoming interface is the interface towards the RP.

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

193

n RPF checking is applied to all multicast traffic and is significant in preventing network loops. Up to eight
manual RPF overrides can be specified. The RPF-address indicates one of two distinct RPF candidates:
1. A valid PIM neighbor address from which forwarded multicast traffic is accepted with a source

address of <source-addr/src-mask>.

2. A local router address on a PIM-enabled interface to which <source-addr/src-mask> is directly

connected. If configured, the local router will assume the role of DR for this flow and registers the
flow with an RP.

Example

Configuring and removing RPF override:

switch(config)# router pim6
switch(config-pim6)# rpf-override 50::4/24 40::1
switch(config-pim)# no rpf-override 50::4/24 40::1

show ipv6 mroute <GROUP-ADDR>

Syntax

show ipv6 mroute <GROUP-ADDR> [<SOURCE-ADDR>]

[all-vrfs | vrf <vrf-name>] [vsx-peer]

Description

Shows the multicast routing information for the given group address. Optionally, you can specify display
information by VRF. If no options are specified, it shows information for the default VRF.

Command context

Operator (>) or Manager (#)

Parameters

<GROUP-ADDR>

Specifies a group address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F.

<SOURCE-ADDR>

Specifies a source IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F.

all-vrfs

Shows information for all VRFs.

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Protocol Independent Multicast - Sparse Mode (V4 and V6) | 194

Showinginformationforgroupff08::1:3andVRFgreen:
| switch#  | show ipv6 mroute | ff08::1:3   | vrf green |
| -------- | ---------------- | ----------- | --------- |
| VRF      | : green          |             |           |
| Group    | Address          | : ff08::1:3 |           |
| Source   | Address          | : 2001::03  |           |
| Neighbor |                  | : 2003::04  |           |
| Incoming | interface        | : 1/1/1     |           |
| Outgoing | Interface List   | :           |           |
Interface State
--------- -----
1/1/4 pruned
Showinginformationforgroupff08::1:3fromsource2001::03andallVRFs:
| switch#  | show ipv6 mroute | ff08::1:3   | 2001::03 all-vrfs |
| -------- | ---------------- | ----------- | ----------------- |
| VRF      | : blue           |             |                   |
| Group    | Address          | : ff08::1:3 |                   |
| Source   | Address          | : 2001::03  |                   |
| Neighbor |                  | : 2003::04  |                   |
| Incoming | interface        | : 1/1/1     |                   |
| Outgoing | Interface List   | :           |                   |
Interface State
--------- -----
1/1/4 pruned
| VRF      | : green        |             |     |
| -------- | -------------- | ----------- | --- |
| Group    | Address        | : ff08::1:3 |     |
| Source   | Address        | : 2001::03  |     |
| Neighbor |                | : 2003::04  |     |
| Incoming | interface      | : 1/1/2     |     |
| Outgoing | Interface List | :           |     |
Interface State
--------- -----
1/1/4 pruned
| show | ipv6 mroute |     |     |
| ---- | ----------- | --- | --- |
Syntax
| show ipv6 | mroute [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |
| --------- | ---------------- | ----------------- | ---------- |
Description
Showsmulticastroutinginformation.Optionally,youcanshowspecificinformationbyVRF.Ifnooptions
arespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 195

vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingIPv6mroute:
| switch#   | show      | ipv6       | mroute  | all-vrfs  |     |
| --------- | --------- | ---------- | ------- | --------- | --- |
| IP        | Multicast | Route      | Entries |           |     |
| VRF       | : blu     |            |         |           |     |
| Total     | number    | of entries | :       | 2         |     |
| Group     | Address   |            | :       | ff08::1:3 |     |
| Source    | Address   |            | :       | 2002::04  |     |
| Neighbor  |           |            | :       | 2001::04  |     |
| Incoming  | interface |            | :       | 1/1/2     |     |
| Outgoing  | Interface |            | List :  |           |     |
| Interface |           | State      |         |           |     |
| --------- |           | -----      |         |           |     |
| 1/1/3     |           | pruned     |         |           |     |
| 1/1/4     |           | forwarding |         |           |     |
| Group     | Address   |            | :       | ff08::1:4 |     |
| Source    | Address   |            | :       | 2003::04  |     |
| Neighbor  |           |            | :       | 2001::04  |     |
| Incoming  | interface |            | :       | 1/1/2     |     |
| Outgoing  | Interface |            | List :  |           |     |
| Interface |           | State      |         |           |     |
| --------- |           | -----      |         |           |     |
| 1/1/3     |           | pruned     |         |           |     |
| VRF       | : default |            |         |           |     |
| Total     | number    | of entries | :       | 1         |     |
| Group     | Address   |            | :       | ff08::1:5 |     |
| Source    | Address   |            | :       | 2001::03  |     |
| Neighbor  |           |            | :       | 2003::04  |     |
| Incoming  | interface |            | :       | 1/1/1     |     |
| Outgoing  | Interface |            | List :  |           |     |
| Interface |           | State      |         |           |     |
| --------- |           | -----      |         |           |     |
| 1/1/4     |           | pruned     |         |           |     |
| show      | ipv6      | mroute     | brief   |           |     |
Syntax
| show ipv6 | mroute | brief | [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |
| --------- | ------ | ----- | --------- | ----------------- | ---------- |
Description
ProtocolIndependentMulticast-SparseMode(V4andV6)|196

Showsbriefversionofthemulticastroutinginformation.Optionally,youcanspecifythedisplay
informationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingtheIPv6mroutebrief:
| switch#   | show ipv6           | mroute brief all-vrfs |     |
| --------- | ------------------- | --------------------- | --- |
| IP        | Multicast Route     | Entries               |     |
| VRF       | : blu               |                       |     |
| Total     | number of entries   | : 2                   |     |
| Group     | Address : ff08::1:3 |                       |     |
| Source    | Address : 2002::04  |                       |     |
| Neighbor  | : 2003::04          |                       |     |
| Interface | :                   | 1/1/2                 |     |
| Group     | Address : ff08::1:4 |                       |     |
| Source    | Address : 2002::03  |                       |     |
| Neighbor  | : 2003::05          |                       |     |
| Interface | :                   | 1/1/3                 |     |
| VRF       | : default           |                       |     |
| Total     | number of entries   | : 1                   |     |
| Group     | Address : ff08::1:5 |                       |     |
| Source    | Address : 2001::03  |                       |     |
| Neighbor  | : 2002::01          |                       |     |
| Interface | :                   | 1/1/1                 |     |
| show      | ipv6 pim6           |                       |     |
Syntax
| show ipv6 | pim6 [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |
| --------- | -------------- | ----------------- | ---------- |
Description
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 197

ShowsthePIMrouterinformation.Optionally,youcanspecifydisplayinformationbyVRF.Ifnooptionsare
specified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingtheIPv6PIMrouter:
| switch#    | show ipv6 pim6    |            |     |
| ---------- | ----------------- | ---------- | --- |
| PIM        | Global Parameters |            |     |
| VRF        |                   | : default  |     |
| PIM        | Status            | : Enabled  |     |
| Join/Prune | Interval (sec)    | : 46       |     |
| SPT        | Threshold         | : Disabled |     |
| show       | ipv6 pim6 bsr     |            |     |
Syntax
| show ipv6 | pim6 bsr [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |
| --------- | ------------------ | ----------------- | ---------- |
Description
ShowstheinformationaboutBSRcandidatesinthedomainandmulticastgroupsitsupports.Optionally,
youcanspecifythedisplayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthe
defaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ProtocolIndependentMulticast-SparseMode(V4andV6)|198

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowinginformationaboutBSRcandidates:
| switch#        | show ipv6      | pim6 bsr all-vrfs |           |                    |
| -------------- | -------------- | ----------------- | --------- | ------------------ |
| Status         | and Counters-  | PIM-SM(IPv6)      | Bootstrap | Router Information |
| VRF            |                | : blu             |           |                    |
| E-BSR Address  |                | : 2006::06        |           |                    |
| E-BSR Priority |                | : 0               |           |                    |
| E-BSR Hash     | Mask Length    | : 0               |           |                    |
| E-BSR Up       | Time           | : 0 secs          |           |                    |
| Next Bootstrap | Message        | : 0 secs          |           |                    |
| C-BSR Admin    | Status         | : This            | system is | a Candidate-BSR    |
| C-BSR Address  |                | : 2007::01        |           |                    |
| C-BSR Priority |                | : 40              |           |                    |
| C-BSR Hash     | Mask Length    | : 36              |           |                    |
| C-BSR Message  | Interval       | : 50              |           |                    |
| C-BSR Source   | IP Interface   | : lag1            |           |                    |
| C-RP Admin     | Status         | : This            | system is | a Candidate-RP     |
| C-RP Address   |                | : 2007::01        |           |                    |
| C-RP Hold      | Time           | : 60              |           |                    |
| C-RP Advertise | Period         | : 60              |           |                    |
| C-RP Priority  |                | : 46              |           |                    |
| C-RP Source    | IP Interface   | : lag1            |           |                    |
| Group Prefix   | : ff00::/8     |                   |           |                    |
| Group Prefix   | : ff08::1:3/64 |                   |           |                    |
| Group Prefix   | : ff08::1:4/64 |                   |           |                    |
| VRF            |                | : default         |           |                    |
| E-BSR Address  |                | : 2001::01        |           |                    |
| E-BSR Priority |                | : 40              |           |                    |
| E-BSR Hash     | Mask Length    | : 36              |           |                    |
| E-BSR Up       | Time           | : 53              | mins      |                    |
| Next Bootstrap | Message        | : 88              | secs      |                    |
| C-BSR Admin    | Status         | : This            | system is | a Candidate-BSR    |
| C-BSR Address  |                | : 2001::01        |           |                    |
| C-BSR Priority |                | : 40              |           |                    |
| C-BSR Hash     | Mask Length    | : 36              |           |                    |
| C-BSR Message  | Interval       | : 50              |           |                    |
| C-BSR Source   | IP Interface   | : 1/1/1           |           |                    |
| C-RP Admin     | Status         | : This            | system is | a Candidate-RP     |
| C-RP Address   |                | : 2001::01        |           |                    |
| C-RP Hold      | Time           | : 60              |           |                    |
| C-RP Advertise | Period         | : 60              |           |                    |
| C-RP Priority  |                | : 46              |           |                    |
| C-RP Source    | IP Interface   | : 1/1/1           |           |                    |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 199

| Group Prefix | : ff00::/8     |         |     |
| ------------ | -------------- | ------- | --- |
| Group Prefix | : ff08::1:5/64 |         |     |
| Group Prefix | : ff08::1:6/64 |         |     |
| show ipv6    | pim6 bsr       | elected |     |
Syntax
show ipv6 pim6 bsr elected [all-vrfs | vrf <VRF-NAME>] [vsx-peer]
Description
ShowsinformationabouttheelectedBSRinthedomainandmulticastgroupsitsupports.Optionallyyou
canspecifydisplayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMelectedbootstraprouterinformation:
| switch# | show ipv6 pim6 | bsr elected | all-vrfs |
| ------- | -------------- | ----------- | -------- |
Status and Counters - PIM-SM(IPv6) Elected Bootstrap Router Information
| VRF            |             | : blu      |     |
| -------------- | ----------- | ---------- | --- |
| E-BSR Address  |             | : 2005::05 |     |
| E-BSR Priority |             | : 0        |     |
| E-BSR Hash     | Mask Length | : 0        |     |
| E-BSR Up       | Time        | : 0 secs   |     |
| Next Bootstrap | Message     | : 0 secs   |     |
| VRF            |             | : default  |     |
| E-BSR Address  |             | : 2002::02 |     |
| E-BSR Priority |             | : 0        |     |
| E-BSR Hash     | Mask Length | : 30       |     |
| E-BSR Up       | Time        | : 50 mins  |     |
| Next Bootstrap | Message     | : 88 secs  |     |
ProtocolIndependentMulticast-SparseMode(V4andV6)|200

| show | ipv6 | pim6 | bsr local |     |     |     |
| ---- | ---- | ---- | --------- | --- | --- | --- |
Syntax
| show ipv6 | pim6 | bsr local | [all-vrfs | | vrf | <VRF-NAME>] | [vsx-peer] |
| --------- | ---- | --------- | --------- | ----- | ----------- | ---------- |
Description
ShowstheinformationaboutBSRcandidatesonthelocalrouterandmulticastgroupsitsupports.
Optionally,youcanspecifydisplayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationfor
thedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowinglocalCandidateBSR:
| switch# | show | ipv6 | pim6 bsr local | all-vrfs |     |     |
| ------- | ---- | ---- | -------------- | -------- | --- | --- |
Status and Counters - PIM-SM(IPv6) Local Candidate-BSR Information
| VRF   |          |              | :         | blu              |                    |     |
| ----- | -------- | ------------ | --------- | ---------------- | ------------------ | --- |
| C-BSR | Admin    | Status       | :         | This system      | is a Candidate-BSR |     |
| C-BSR | Address  |              | :         | 2007::01         |                    |     |
| C-BSR | Priority |              | :         | 40               |                    |     |
| C-BSR | Hash     | Mask Length  | :         | 36               |                    |     |
| C-BSR | Message  | Interval     | :         | 50               |                    |     |
| C-BSR | Source   | IP Interface | :         | lag1             |                    |     |
| VRF   |          |              | :         | default          |                    |     |
| C-BSR | Admin    | Status       | :         | This system      | is a Candidate-BSR |     |
| C-BSR | Address  |              | :         | 2001::01         |                    |     |
| C-BSR | Priority |              | :         | 40               |                    |     |
| C-BSR | Hash     | Mask Length  | :         | 36               |                    |     |
| C-BSR | Message  | Interval     | :         | 50               |                    |     |
| C-BSR | Source   | IP Interface | :         | 1/1/1            |                    |     |
| show  | ipv6     | pim6         | interface | <INTERFACE-NAME> |                    |     |
Syntax
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 201

| show ipv6 | pim6 | interface | <INTERFACE-NAME> |     | [vsx-peer] |     |     |     |
| --------- | ---- | --------- | ---------------- | --- | ---------- | --- | --- | --- |
Description
ShowsdetailedinformationaboutthePIMinterfacecurrentlyconfigured.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-NAME>
SpecifiesaninterfaceforshowingPIMinterfaceinformation.InterfacecanalsobeaLAGorVLAN.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingPIMinterfaceinformationforinterface1/1/1:
| switch#     | show       | ipv6                         | pim6 interface | 1/1/1 |     |             |       |       |
| ----------- | ---------- | ---------------------------- | -------------- | ----- | --- | ----------- | ----- | ----- |
| PIM         | Interfaces |                              |                |       |     |             |       |       |
| VRF:        | default    |                              |                |       |     |             |       |       |
| Interface   |            | : 1/1/1                      |                |       |     |             |       |       |
| IPv6        | Address    | : fe80::a00:9ff:feec:dc0e/64 |                |       |     |             |       |       |
| Mode        |            | : sparse                     |                |       |     |             |       |       |
| Designated  |            | Router                       | :              |       |     |             |       |       |
| Hello       | Interval   | (sec)                        | : 30           |       |     |             |       |       |
| Hello       | Delay      | (sec)                        | : 4            |       |     |             |       |       |
| Override    | Interval   |                              | (msec)         | : 500 |     | Lan Prune   | Delay | : Yes |
| Propagation |            | Delay                        | (msec)         | : 350 |     | DR Priority |       | : 3   |
| Neighbor    | Timeout    |                              |                | : 0   |     |             |       |       |
| show        | ipv6       | pim6                         | interface      |       |     |             |       |       |
Syntax
| show ipv6 | pim6 | interface | [all-vrfs | | vrf | <VRF-NAME>] | [vsx-peer] |     |     |
| --------- | ---- | --------- | --------- | ----- | ----------- | ---------- | --- | --- |
Description
ShowstheinformationaboutPIMinterfacescurrentlyconfiguredintherouter.Optionally,youcanspecify
displayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
ProtocolIndependentMulticast-SparseMode(V4andV6)|202

Parameters

all-vrfs

Shows information for all VRFs.

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Showing PIM interface:

switch# show ipv6 pim6 interface
PIM Interfaces

VRF: default

IP Address

Interface
mode
------------------ -------------------------------------------------------------- -
---------
1/1/1
sparse

fe80::a00:9ff:feec:dc0e/64

show ipv6 pim6 neighbor

Syntax

show ipv6 pim6 neighbor [<IPv6-ADDR>]

[all-vrfs | vrf <VRF-NAME>] [vsx-peer]

Description

Shows PIM neighbor information. Optionally, you can specify display information by VRF. If no options are
specified, it shows information for the default VRF.

Parameters

<IPv6-ADDR>

Specifies a neighbor address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F.

all-vrfs

Shows information for all VRFs.

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

203

Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingPIMneighborinformation:
| switch#   | show       | ipv6  | pim6 neighbor |     |
| --------- | ---------- | ----- | ------------- | --- |
| PIM       | Neighbor   |       |               |     |
| VRF       |            |       | : default     |     |
| IP        | Address    |       | : 2001::02    |     |
| Interface |            |       | : 1/1/1       |     |
| Up        | Time (sec) |       | : 0           |     |
| Expire    | Time       | (sec) | : 0           |     |
| DR        | Priority   |       | : 44          |     |
| show      | ipv6       | pim6  | pending       |     |
Syntax
| show ipv6 | pim6 | pending | [<GROUP-ADDR>] |            |
| --------- | ---- | ------- | -------------- | ---------- |
| [all-vrfs |      | | vrf   | <VRF-NAME>]    | [vsx-peer] |
Description
ShowsthependingjoinsonaPIMrouter.OptionallyyoucanspecifydisplayinformationbyVRF.Ifno
optionsarespecified,itshowsinformationforthedefaultVRF.
UsethiscommandtodeterminewhatflowsarebeingrequestedonthePIMnetwork.Ifdataavailabilityfor
aflowisexpected,andajoinfortheflowispending,thetroubleshootingsearchmovestothesourceofthat
flow,sincetheroutersareverifiedtobeseeingtherequestfordata.
Commandcontext
Operator(>)orManager(#)
Parameters
<GROUP-ADDR>
SpecifiesagroupaddressinIPv6format(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
ProtocolIndependentMulticast-SparseMode(V4andV6)|204

Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingpendingPIMjoins:
| switch# | show ipv6 pim6 | pending |     |     |
| ------- | -------------- | ------- | --- | --- |
Join Pending
VRF : default
| Group     | ff08::1:3 |              |       |     |
| --------- | --------- | ------------ | ----- | --- |
| (*,G)     | Pending   |              |       |     |
|           | Incoming  | Interface:   | 1/1/1 |     |
| Group     | ff08::1:4 |              |       |     |
| (*,G)     | Pending   |              |       |     |
|           | Incoming  | Interface:   | 1/1/1 |     |
| show ipv6 | pim6      | rp-candidate |       |     |
Syntax
show ipv6 pim6 rp-candidate [all-vrfs | vrf <VRF-NAME>] [vsx-peer]
Description
ShowsthecandidateRPoperationalandconfigurationinformation.Optionally,youcanspecifydisplay
informationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMRPcandidate:
| switch#      | show ipv6 pim6 | rp-candidate | all-vrfs     |              |
| ------------ | -------------- | ------------ | ------------ | ------------ |
| Status       | and Counters-  | PIM-SM(IPv6) | Candidate-RP | Information  |
| VRF          |                | : blu        |              |              |
| C-RP Admin   | Status         | : This       | system is a  | Candidate-RP |
| C-RP Address |                | : 2007::01   |              |              |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 205

| C-RP Hold      | Time              | : 60          |                   |
| -------------- | ----------------- | ------------- | ----------------- |
| C-RP Advertise | Period            | : 60          |                   |
| C-RP Priority  |                   | : 46          |                   |
| C-RP Source    | IP Interface      | : lag1        |                   |
| Group Prefix   | : ff00::/8        |               |                   |
| Group Prefix   | : ff08::1:3/64    |               |                   |
| Group Prefix   | : ff08::1:4/64    |               |                   |
| VRF            |                   | : default     |                   |
| C-RP Admin     | Status            | : This system | is a Candidate-RP |
| C-RP Address   |                   | : 2001::01    |                   |
| C-RP Hold      | Time              | : 60          |                   |
| C-RP Advertise | Period            | : 60          |                   |
| C-RP Priority  |                   | : 46          |                   |
| C-RP Source    | IP Interface      | : 1/1/1       |                   |
| Group Prefix   | : ff00::/8        |               |                   |
| Group Prefix   | : ff08::1:5/64    |               |                   |
| Group Prefix   | : ff08::1:6/64    |               |                   |
| show ipv6      | pim6 rpf-override |               |                   |
Syntax
show ipv6 pim6 rpf-override [all-vrfs | vrf <VRF-NAME>] [vsx-peer]
Description
ShowstheRPFoverrideconfiguration,whichcanbeusefulinformationwhentroubleshootingpotentialRPF
misconfigurations.Optionally,youcanspecifydisplayinformationbyVRF.Ifnooptionsarespecified,it
showsinformationforthedefaultVRF
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMRPFoverride:
ProtocolIndependentMulticast-SparseMode(V4andV6)|206

| switch#   | show         | ipv6 pim6             | rpf-override |     | all-vrfs |
| --------- | ------------ | --------------------- | ------------ | --- | -------- |
| VRF       | : Green      |                       |              |     |          |
| Static    | RPF          | Override              |              |     |          |
| Multicast |              | Source : 2003::1/128  |              |     |          |
| RPF       | IPv6 Address | : 2001::01            |              |     |          |
| Multicast |              | Source : 2005::1/128  |              |     |          |
| RPF       | IPv6 Address | : 2007::01            |              |     |          |
| VRF       | : Red        |                       |              |     |          |
| Static    | RPF          | Override              |              |     |          |
| Multicast |              | Source : 2004::02/128 |              |     |          |
| RPF       | IPv6 Address | : 2002::02            |              |     |          |
| show      | ipv6         | pim6 rpf-override     |              |     | source   |
Syntax
| show ipv6 | pim6 | rpf-override      | source | <IPv6-ADDR> |     |
| --------- | ---- | ----------------- | ------ | ----------- | --- |
| [all-vrfs |      | | vrf <VRF-NAME>] |        | [vsx-peer]  |     |
Description
ShowstheRPFoverrideconfigurationforthespecifiedsource.Optionally,youcanspecifydisplay
informationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
source <IPv6-ADDR>
SpecifiestheRPFsourceaddressinIPv6format(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherex
isahexadecimalnumberfrom0toF.
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingPIMRPFoverridesource:
| switch# | show      | ipv6 pim6 | rpf-override |     | source 2004::02 |
| ------- | --------- | --------- | ------------ | --- | --------------- |
| VRF     | : default |           |              |     |                 |
| Static  | RPF       | Override  |              |     |                 |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 207

| Multicast | Source  | : 2004::02/128 |     |     |     |     |     |
| --------- | ------- | -------------- | --- | --- | --- | --- | --- |
| RPF IPv6  | Address | : 2002::02     |     |     |     |     |     |
ShowingPIMRPFoverridesourceforallVRFs:
| switch#   | show         | ipv6 pim6 | rpf-override |     | source | 2004::02 | all-vrfs |
| --------- | ------------ | --------- | ------------ | --- | ------ | -------- | -------- |
| VRF       | : Red        |           |              |     |        |          |          |
| Static    | RPF          | Override  |              |     |        |          |          |
| Multicast |              | Source :  | 2004::02/128 |     |        |          |          |
| RPF       | IPv6 Address | :         | 2002::02     |     |        |          |          |
| show      | ipv6         | pim6      | rp-set       |     |        |          |          |
Syntax
| show ipv6 | pim6 | rp-set | [all-vrfs | | vrf | <VRF-NAME>] | [vsx-peer] |     |
| --------- | ---- | ------ | --------- | ----- | ----------- | ---------- | --- |
Description
ShowsthemulticastgroupsupportforboththelearnedC-RPassignmentsandanystaticallyconfiguredRP
assignments.Optionally,youcanspecifydisplayinformationbyVRF.Ifnooptionsarespecified,itshows
informationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMRPsetinformation:
| switch# | show    | ipv6 pim6  | rp-set         | all-vrfs |               |     |             |
| ------- | ------- | ---------- | -------------- | -------- | ------------- | --- | ----------- |
| VRF:    | blu     |            |                |          |               |     |             |
| Status  | and     | Counters   | - PIM-SM(IPv6) |          | Static RP-Set |     | Information |
| Group   | Prefix  | : ff00::/8 |                |          |               |     |             |
| RP      | Address | : 2004::04 |                |          |               |     |             |
ProtocolIndependentMulticast-SparseMode(V4andV6)|208

| Override     | [No] : No    |                |                |             |
| ------------ | ------------ | -------------- | -------------- | ----------- |
| Status       | and Counters | - PIM-SM(IPv6) | Learned RP-Set | Information |
| Group Prefix |              | : ff08::1:3/64 |                |             |
| RP Address   |              | : 2007::01     |                |             |
| Hold Time    | (sec)        | : 60           |                |             |
| Expire       | Time (sec)   | : 0            |                |             |
| Group Prefix |              | : ff08::1:4/64 |                |             |
| RP Address   |              | : 2007::01     |                |             |
| Hold Time    | (sec)        | : 60           |                |             |
| Expire       | Time (sec)   | : 92           |                |             |
| VRF: default |              |                |                |             |
| Status       | and Counters | - PIM-SM(IPv6) | Static RP-Set  | Information |
| Group Prefix | : ff00::/8   |                |                |             |
| RP Address   | : 2003::03   |                |                |             |
| Override     | [No] : No    |                |                |             |
| Status       | and Counters | - PIM-SM(IPv6) | Learned RP-Set | Information |
| Group Prefix |              | : ff08::1:5/64 |                |             |
| RP Address   |              | : 2001::01     |                |             |
| Hold Time    | (sec)        | : 60           |                |             |
| Expire       | Time (sec)   | : 0            |                |             |
| Group Prefix |              | : ff08::1:6/64 |                |             |
| RP Address   |              | : 2002::01     |                |             |
| Hold Time    | (sec)        | : 60           |                |             |
| Expire       | Time (sec)   | : 92           |                |             |
| show ipv6    | pim6         | rp-set learned |                |             |
Syntax
show ipv6 pim6 rp-set learned [all-vrfs | vrf <VRF-NAME>] [vsx-peer]
Description
ShowsthemulticastgroupsupportfordynamicallylearnedRPassignments.Optionally,youcanspecify
displayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 209

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMRPsetlearnedinformation:
| switch#      | show ipv6    | pim6 rp-set learned | all-vrfs       |             |
| ------------ | ------------ | ------------------- | -------------- | ----------- |
| VRF: blu     |              |                     |                |             |
| Status       | and Counters | - PIM-SM(IPv6)      | Learned RP-Set | Information |
| Group Prefix |              | : ff08::1:3/64      |                |             |
| RP Address   |              | : 2007::01          |                |             |
| Hold Time    | (sec)        | : 60                |                |             |
| Expire       | Time (sec)   | : 0                 |                |             |
| Group Prefix |              | : ff08::1:4/64      |                |             |
| RP Address   |              | : 2007::01          |                |             |
| Hold Time    | (sec)        | : 60                |                |             |
| Expire       | Time (sec)   | : 92                |                |             |
| VRF: default |              |                     |                |             |
| Status       | and Counters | - PIM-SM(IPv6)      | Learned RP-Set | Information |
| Group Prefix |              | : ff08::1:5/64      |                |             |
| RP Address   |              | : 2001::01          |                |             |
| Hold Time    | (sec)        | : 60                |                |             |
| Expire       | Time (sec)   | : 0                 |                |             |
| Group Prefix |              | : ff08::1:6/64      |                |             |
| RP Address   |              | : 2002::01          |                |             |
| Hold Time    | (sec)        | : 60                |                |             |
| Expire       | Time (sec)   | : 92                |                |             |
| show ipv6    | pim6         | rp-set static       |                |             |
Syntax
show ipv6 pim6 rp-set static [all-vrfs | vrf <VRF-NAME>] [vsx-peer]
Description
ShowsthemulticastgroupsupportforstaticallyconfiguredRPassignments.Optionally,youcanspecify
displayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
ProtocolIndependentMulticast-SparseMode(V4andV6)|210

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMStaticRPsetinformation:
| switch# | show ipv6 pim6 | rp-set static | all-vrfs |     |
| ------- | -------------- | ------------- | -------- | --- |
VRF: blu
| Status and   | Counters   | - PIM-SM(IPv6) | Static RP-Set | Information |
| ------------ | ---------- | -------------- | ------------- | ----------- |
| Group Prefix | : ff00::/8 |                |               |             |
| RP Address   | : 2004::04 |                |               |             |
| Override     | [No] : No  |                |               |             |
VRF: default
| Status and   | Counters   | - PIM-SM(IPv6) | Static RP-Set | Information |
| ------------ | ---------- | -------------- | ------------- | ----------- |
| Group Prefix | : ff00::/8 |                |               |             |
| RP Address   | : 2003::03 |                |               |             |
| Override     | [No] : No  |                |               |             |
spt-threshold
Syntax
spt-threshold
no spt-threshold
Description
Enablestheroutertoswitchthemulticasttrafficflowstotheshortestpathtree.Defaultisenabled.
Thenoformofthiscommanddisablestheroutersabilitytoswitchthemulticasttrafficflowstotheshortest
pathtree.
Toapplythisconfigurationauserneedstoapplydisable/enablePIMglobally.
Commandcontext
config-pim6
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
EnablinganddisablingtheSPTthreshold:
| switch(config)#      | router | pim6             |     |     |
| -------------------- | ------ | ---------------- | --- | --- |
| switch(config-pim6)# |        | spt-threshold    |     |     |
| switch(config-pim6)# |        | no spt-threshold |     |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 211

Protocol Independent Multicast - Dense
Mode (V4 and V6)

Chapter 7

Protocol Independent Multicast - Dense Mode (V4 and V6)

In a network, IP multicast traffic transmitted for multimedia applications is blocked at routed interface
boundaries unless a multicast routing protocol is running. Protocol Independent Multicast (PIM) is a family
of routing protocols. It forms multicast trees to forward traffic from multicast sources to subnets which use
protocols such as IGMP and MLD to request the traffic.

Protocol Independent Multicast - Dense Mode (PIM-DM)
overview

PIM relies on the unicast routing tables to identify the path back to a multicast source. This routing method
is known as reverse path forwarding (RPF). The unicast routing protocols create the unicast routing tables.
With this information, PIM sets up the distribution tree for the multicast traffic.

PIM-DM operates at the router level to direct traffic for a particular multicast group along the most efficient
path to the network which has hosts that have joined that group. A unicast source address and a multicast
group address comprise a given source/group (S/G) pair. Multicast traffic moving from a source to a
multicast group address creates a flow to one or more areas of the network requiring the traffic. The flow
destination is the multicast group address and not a specific host or VLAN. A single multicast flow has one
source and one multicast group address (destination), but may reach many hosts in different subnets,
depending on which hosts have issued joins for the same multicast group.

PIM routes the multicast traffic for a particular S/G pair on paths between the source unicast address and to
the interfaces where it is requested (by joins from hosts connected to those subnets.) Physical destinations
for a particular multicast group can be hosts in different networks. Individual hosts use IGMP/MLD
configured per-subnet to send joins requesting membership in a particular multicast group. All hosts that
have joined a given multicast group (defined by a multicast address) remain in that group as long as they
continue to issue periodic joins.

PIM-DM interoperates with IGMP/MLD and the switch's routing protocols. PIM operates independently of
the routing protocol that is chosen to run on the switches. So PIM-DM can be used with RIP, OSPF, BGP, or
static routes configured. PIM-DM uses a unicast routing table to find the path to the originator of the
multicast traffic and sets up multicast trees for distributing multicast traffic.

PIM-DM defaults, protocols, and supported configurations

Default configuration

PIM-DM is disabled by default. Either PIM-SM or PIM-DM can be configured within a VRF at a time. All the
interfaces within the VRF must run with same mode.

Routing protocol support

PIM uses unicast routing information from any of the routing protocols that are running on the system,
such as OSPFv2, OSPFv3, BGP. Static routes are also supported with Nexthop IP addresses.

PIM enabled interfaces (L3 and SVI)

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

212

PIM can be enabled across all VRFs on a maximum of 1,000 interfaces with an upper limit of 128 per VRF.

Although up to 128 PIM DM enabled interfaces can be configured, when configuring trunk interfaces with multiple

Dense enabled SVIs, the trunk interfaces must have sufficient bandwidth or have only the required number of

trunks it can support. This ensures that the link utilization is not exceeded due to the initial flooding nature of the

protocol.

IGMP and MLD compatibility

PIM-DM is compatible with IGMP version 2 and version 3, MLD version 1 and version 2, and is fully
interoperable with IGMP/MLD for determining multicast flows.

VRRP

PIM-DM is fully interoperable with VRRP to quickly transition multicast routes in a failover.

VRF support

PIM-DM can run on multiple VRF instances in parallel. It is supported on all VRFs supported in the system.

Limitations

PIM-DM currently does not support the following:

n VxLAN, 6in4, 6in6, and GRE interfaces

n PIM-DM cannot be enabled on VSX deployments.

PIM-DM configuration example
When the routing switch detects a new multicast flow, it initially floods the traffic throughout the PIM-DM
domain, then it prunes the traffic on the branches (network paths) where joins have not been received from
individual hosts. The following is a sample topology diagram for a PIM-DM configuration.

Figure 1 PM-DM Configuration Examples

The routing switch maintains individual branches in the multicast tree as long as there is at least one host
maintaining a membership in the multicast group. When all the hosts in a particular subnet drop out of the
group, PIM-DM prunes that interface from the multicast tree. Similarly, if the routing switch detects a join
from a host in a pruned interface, it adds that branch back into the tree.

Unlike PIM-SM, the number of mroutes created with dense mode is typically high since the source router
floods the traffic initially to all the PIM neighbors. If we have two routers connected with many VLAN trunks,
the resulting mroutes on the receiver router will be proportional to the number of SVIs configured. Ensure
that the given flows are within the limits of the receiver router's mroute scale.

PIM-DM features

Multicast flow management

Multicast flow management refers to how the routing switch manages forwarding and pruned flows. This is
useful when planning topologies to include multicast support and when viewing and interpreting the show
command output for PIM-DM features.

Initial flood and prune

Protocol Independent Multicast - Dense Mode (V4 and V6) | 213

When a router running PIM-DM receives a new multicast flow, it initially floods the traffic to all downstream
multicast routers. Branches that do not have members send Prune messages toward the source to prune
off the unwanted/unnecessary traffic.

Maintaining the prune state

For a multicast group "X" on a given interface, when the last host belonging to group "X" leaves the group,
PIM places that interface in a prune state. Multicast traffic from group "X" is now blocked to that interface.
The prune state remains until a host on the same interface issues a join for group "X", in which case the
router cancels the prune state and changes the flow to the forwarding state.

State-refresh packets and bandwidth conservation

A multicast switch, if directly connected to a multicast source (such as a video conference application),
periodically transmits state-refresh packets to downstream multicast routers. On routers that have pruned
the multicast flow, the state-refresh packets keep the pruned state alive. On routers that have been added
to the network after the initial flooding and pruning of a multicast group, the state-refresh packets inform
the newly added router of the current state of that branch. So if all multicast routers in a network support
the state-refresh packet, the multicast router directly connected to the multicast source performs only one
flood-prune cycle to the edge of the network when a new flow (multicast group) is introduced and preserves
bandwidth for other uses.

PIM-DM commands for IPv4

disable

Syntax

disable

Description

Disables PIM globally on the router. PIM is disabled by default.

Using the disable command will cause all the multicast routes to be erased from hardware.

Command context

config-pim

Authority

Administrators or local user group members with execution rights for this command.

Example

Disabling PIM router:

switch(config)# router pim
switch(config-pim)# disable

enable

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

214

Syntax

enable

Description

Enables PIM globally on the router.

Command context

config-pim

Authority

Administrators or local user group members with execution rights for this command.

Example

Enabling PIM router:

switch(config)# router pim
switch(config-pim)# enable

no ip pim-dense {enable|disable}

Syntax

no ip pim-dense {enable|disable}

Description

Enables or disables PIM-DM in the current interface. PIM-DM is disabled by default on an interface. IP
address must be configured on the interface to enable PIM-DM.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

enable

Specifies PIM-DM on the interface. IP address must be configured on the interface to enable PIM-DM
(use the ip address <A.B.C.D/M> command).

disable

Disables PIM-DM on the interface.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling and disabling PIM-SM in an interface:

switch(config)# interface vlan40
switch(config-if-vlan)# ip address 40.0.0.4/24
switch(config-if-vlan)# ip pim-dense enable

Protocol Independent Multicast - Dense Mode (V4 and V6) | 215

switch(config-if-vlan)#
| switch(config-if-vlan)# |     | ip pim-dense |     | disable |     |
| ----------------------- | --- | ------------ | --- | ------- | --- |
| ip pim-dense            | bfd |              |     |         |     |
Syntax
| ip pim-dense bfd | [disable] |     |     |     |     |
| ---------------- | --------- | --- | --- | --- | --- |
| no ip pim-dense  | bfd       |     |     |     |     |
Description
ConfiguresBFDonaper-interfacebasisforaninterfaceassociatedwiththePIMprocess.
ThenoformofthiscommandremovestheBFDconfigurationontheinterfaceandsetsittothedefault
configuration.
IfBFDisenabledglobally,itwillbeenabledbydefaultonallinterfaces.Theonlyexceptioniswhenitisdisabled
| specificallyonaninterfaceusingtheip |     |     | pim-dense |     | bfd disablecommand. |
| ----------------------------------- | --- | --- | --------- | --- | ------------------- |
IfBFDisdisabledglobally,itwillbedisabledbydefaultonallinterfaces.Theonlyexceptioniswhenitisenabled
| specificallyonaninterfaceusingtheip |     |     | pim-dense |     | bfdcommand. |
| ----------------------------------- | --- | --- | --------- | --- | ----------- |
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
disable
DisablestheBFDconfigurationontheinterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingtheBFDconfigurationontheinterface:
| switch(config)#         | interface |     | vlan40    |     |     |
| ----------------------- | --------- | --- | --------- | --- | --- |
| switch(config-if-vlan)# |           | ip  | pim-dense |     | bfd |
RemovingtheBFDconfigurationontheinterface:
| switch(config-if-vlan)# |     | no  | ip pim-dense |     | bfd |
| ----------------------- | --- | --- | ------------ | --- | --- |
DisablingtheBFDconfigurationontheinterfaceandoverridingtheglobalsetting:
| switch(config-if-vlan)# |                      | ip  | pim-dense |     | bfd disable |
| ----------------------- | -------------------- | --- | --------- | --- | ----------- |
| ip pim-dense            | graft-retry-interval |     |           |     |             |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 216

Syntax
| ip pim-dense    | graft-retry-interval |     | <INTERVAL-VALUE> |     |     |
| --------------- | -------------------- | --- | ---------------- | --- | --- |
| no ip pim-dense | graft-retry-interval |     |                  |     |     |
Description
Configurestheintervalforwhichtheroutingswitchwaitsforthegraftacknowledgmentfromanother
routerbeforeresendingthegraftrequest.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetstothedefaultof3seconds.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<INTERVAL-VALUE>
Specifiestheintervaltheroutingswitchwaitsforthegraftacknowledgement.Default:3seconds.Range:
1-10seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Graftpacketsresultwhenadownstreamroutertransmitsarequesttojoinaflow.Theupstreamrouter
respondswithagraftacknowledgmentpacket.Ifthegraftacknowledgmentisnotreceivedwithinthetime
periodofthegraft-retry-interval,itresendsthegraftpacket.
Example
Configuringandremovingdensegraftretryinterval:
| switch(config)#         | interface   | vlan40 |              |                      |     |
| ----------------------- | ----------- | ------ | ------------ | -------------------- | --- |
| switch(config-if-vlan)# |             | ip     | pim-dense    | graft-retry-interval | 5   |
| switch(config-if-vlan)# |             | no     | ip pim-dense | graft-retry-interval |     |
| ip pim-dense            | hello-delay |        |              |                      |     |
Syntax
| ip pim-dense    | hello-delay | <DELAY-VALUE> |     |     |     |
| --------------- | ----------- | ------------- | --- | --- | --- |
| no ip pim-dense | hello-delay |               |     |     |     |
Description
ConfiguresthemaximumtimeinsecondsbeforetherouteractuallytransmitstheinitialPIMhellomessage
onthecurrentinterface.
Thenoformofthiscommandremovescurrentlyconfiguredvalueandsetstothedefaultof5seconds.
Commandcontext
config-if
config-if-vlan
config-lag-if
ProtocolIndependentMulticast-DenseMode(V4andV6)|217

Parameters

<DELAY-VALUE>

Specifies the hello-delay in seconds, which is the maximum time before a triggered PIM Hello message is
transmitted on this interface. Default: 5 seconds. Range: 0-5 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

In cases where a new interface activates connections with multiple routers, if all the connected routers send
hello packets at the same time, the receiving router could become momentarily overloaded. This command
randomizes the transmission delay to a time between zero and the hello delay setting. Using zero means no
delay. After the router sends the initial hello packet to a newly detected interface, it sends subsequent hello
packets according to the current hello interval setting.

Example

Configuring and removing hello-delay interface:

switch(config)# interface vlan40
switch(config-if-vlan)# ip pim-dense hello-delay 4
switch(config-if-vlan)# no ip pim-dense hello-delay

ip pim-dense hello-interval

Syntax

ip pim-dense hello-interval <INTERVAL-VALUE>
no ip pim-dense hello-interval

Description

Configures the frequency at which the router transmits PIM hello messages on the current interface.

The no form of this command removes the currently configured value and sets to the default of 30 seconds.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

<INTERVAL-VALUE>

Specifies the frequency at which PIM Hello messages are transmitted on this interface. Default: 30
seconds. Range: 5-300 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

218

Therouteruseshellopacketstoinformneighborroutersofitspresence.
n
Therouteralsousesthissettingtocomputethehelloholdtime,whichisincludedinhellopacketssentto
n
neighborrouters.
Helloholdtimetellsneighborroutershowlongtowaitforthenexthellopacketfromtherouter.If
n
anotherpacketdoesnotarrivewithinthattime,therouterremovestheneighboradjacencyonthat
interfacefromthePIMadjacencytable,whichremovesanyflowsrunningonthatinterface.
n Shorteningthehellointervalreducesthehelloholdtime.Iftheydonotreceiveanewhellopacketwhen
expected,itchangeshowquicklyotherroutersstopsendingtraffictotherouter.
Example
Configuringandremovingdensehello-interval:
| switch(config)#    |     | interface | 1/1/4     |                |     |     |
| ------------------ | --- | --------- | --------- | -------------- | --- | --- |
| switch(config-if)# |     | ip        | pim-dense | hello-interval |     | 60  |
switch(config-if)#
|              |     | no      | ip pim-dense | hello-interval |     |     |
| ------------ | --- | ------- | ------------ | -------------- | --- | --- |
| ip pim-dense |     | ip-addr |              |                |     |     |
Syntax
| ip pim-dense    | ip-addr | {<IP-ADDR-VALUE> |     | |   | any} |     |
| --------------- | ------- | ---------------- | --- | --- | ---- | --- |
| no ip pim-dense |         | ip-addr          |     |     |      |     |
Description
EnablestheroutertodynamicallydeterminethesourceIPaddresstouseforPIMpacketssentfromthe
interfaceortousethespecificIPaddress.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetstothedefaultofany.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<IP-ADDR-VALUE>
SpecifiesanIPaddressasthesourceIPfortheinterface.
any
SpecifiesdynamicallydeterminingthesourceIPfromthecurrentIPaddressoftheinterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringandremovingsourceIPaddress:
| switch(config)#         |     | interface       | vlan40       |           |         |          |
| ----------------------- | --- | --------------- | ------------ | --------- | ------- | -------- |
| switch(config-if-vlan)# |     |                 | ip pim-dense |           | ip-addr | 40.0.0.4 |
| switch(config-if-vlan)# |     |                 | no ip        | pim-dense | ip-addr |          |
| ip pim-dense            |     | lan-prune-delay |              |           |         |          |
ProtocolIndependentMulticast-DenseMode(V4andV6)|219

Syntax
| ip pim-dense    | lan-prune-delay |     |     |
| --------------- | --------------- | --- | --- |
| no ip pim-dense | lan-prune-delay |     |     |
Description
EnablestheLANprunedelayoptiononthecurrentinterface.Thedefaultstatusisenabled.
ThenoformofthiscommanddisablestheLANprunedelayoption.
Commandcontext
config-if
config-if-vlan
config-lag-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
WithLAN-prune-delayenabled,therouterinformsdownstreamneighborshowlongitwillwaitbefore
pruningaflowafterreceivingaprunerequest.Otherdownstreamroutersonthesameinterfacemustsend
ajointooverridetheprunebeforetheLAN-prune-delaytimetocontinuetheflow.Promptsany
downstreamneighborswithmulticastreceiverscontinuingtobelongtotheflowtoreplywithajoin.Ifno
joinsarereceivedaftertheLAN-prune-delayperiod,therouterprunestheflow.Thepropagation-delayand
override-intervalsettingsdeterminetheLAN-prune-delaysetting.
Example
EnablinganddisablingtheLANprunedelay:
| switch(config)#         | interface         | vlan40          |                 |
| ----------------------- | ----------------- | --------------- | --------------- |
| switch(config-if-vlan)# |                   | ip pim-dense    | lan-prune-delay |
| switch(config-if-vlan)# |                   | no ip pim-dense | lan-prune-delay |
| ip pim-dense            | max-graft-retries |                 |                 |
Syntax
| ip pim-dense    | max-graft-retries | <ATTEMPT-VALUE> |     |
| --------------- | ----------------- | --------------- | --- |
| no ip pim-dense | max-graft-retries |                 |     |
Description
Configuresthenumberofattemptstheroutingswitchwillretrysendingthesamegraftpackettojoinaflow.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetstothedefaultof3attempts.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<INTERVAL-VALUE>
Specifiesthenumberofretriesfortheroutingswitchtoresendthegraftpacket.Default:3attempts.
Range:1-10attempts.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 220

Authority

Administrators or local user group members with execution rights for this command.

Usage

If a graft acknowledgment response is not received after the specified number of retries, the routing switch
ceases trying to join the flow. In this case the flow is removed until either a state-refresh from upstream re-
initiates the flow or an upstream router floods the flow. Increasing this value helps to improve multicast
reliability.

Example

Configuring and removing dense graft retry interval:

switch(config)# interface vlan40
switch(config-if-vlan)# ip pim-dense max-graft-retries 6
switch(config-if-vlan)# no ip pim-dense max-graft-retries

ip pim-dense override-interval

Syntax

ip pim-dense override-interval <INTERVAL-VALUE>
no ip pim-dense override-interval

Description

Configures the override interval that gets inserted into the Override Interval field of a LAN Prune Delay
option.

The no form of this command removes the currently configured value and sets the value to the default of
2500 ms.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

<INTERVAL-VALUE>

Specifies the override interval of a LAN Prune Delay option in ms. Default: 2500 ms. Range: 500-6000.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Each router on the LAN expresses its view of the amount of randomization necessary in the Override
Interval field of the LAN Prune Delay option. When all routers on a LAN use the LAN Prune Delay Option, all
routers on the LAN MUST set their Override_Interval to the largest Override value on the LAN.

Example

Configuring and removing the override interval:

Protocol Independent Multicast - Dense Mode (V4 and V6) | 221

| switch(config)# | interface | vlan40 |     |     |
| --------------- | --------- | ------ | --- | --- |
switch(config-if-vlan)#
|                         |                   | ip pim-dense    | override-interval | 4000 |
| ----------------------- | ----------------- | --------------- | ----------------- | ---- |
| switch(config-if-vlan)# |                   | no ip pim-dense | override-interval |      |
| ip pim-dense            | propagation-delay |                 |                   |      |
Syntax
| ip pim-dense    | propagation-delay | <DELAY-VALUE> |     |     |
| --------------- | ----------------- | ------------- | --- | --- |
| no ip pim-dense | propagation-delay |               |     |     |
Description
ConfiguresthepropagationdelaythatgetsinsertedintotheLANprunedelayfieldofaLANPruneDelay
option.
Thenoformofthiscommandremovescurrentlyconfiguredvalueandsetstothedefaultof500ms.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<DELAY-VALUE>
Specifiesthepropagationdelayvalueinms.Default:500ms.Range:250-2000ms.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
TheLANDelayinsertedbyarouterintheLANPruneDelayoptionexpressestheexpectedmessage
propagationdelayonthelink.WhenallroutersonalinkusetheLANPruneDelayOption,allroutersonthe
LANMUSTsetPropagationDelaytothelargestLANDelayontheLAN.
Examples
Configuringandremovingthepropagationdelay:
| switch(config)#         | interface     | vlan40          |                   |     |
| ----------------------- | ------------- | --------------- | ----------------- | --- |
| switch(config-if-vlan)# |               | ip pim-dense    | propagation-delay | 400 |
| switch(config-if-vlan)# |               | no ip pim-dense | propagation-delay |     |
| ip pim-dense            | ttl-threshold |                 |                   |     |
Syntax
| ip pim-dense    | ttl-threshold | <THRESHOLD-VALUE> |     |     |
| --------------- | ------------- | ----------------- | --- | --- |
| no ip pim-dense | ttl-threshold |                   |     |     |
Description
Configuresthemulticastdatagramtime-to-live(routerhop-count)thresholdfortheinterface.Astate-
refreshpacketwithaTTLlessthanthisthresholdwillnotbeforwardedouttheinterface.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetstothedefaultof3attempts.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 222

Command context

config-if
config-if-vlan
config-lag-if

Parameters

<THRESHOLD-VALUE>

Specifies the time to live threshold. Default: 3 attempts. Range: 0-255.

Authority

Administrators or local user group members with execution rights for this command.

Usage

The interface connected to the multicast source does not receive state refresh packets and thus is not state-
refresh capable. Downstream VLANs in the switches are state-refresh capable. This parameter provides a
method for containing multicast traffic within a network, or even within specific areas of a network. Initially,
the multicast traffic source sets a TTL value in the packets it transmits. Each time one of these packets
passes through a multicast routing device, the TTL setting decrements by 1. If the packet arrives with a TTL
lower than the ttl-threshold, the routing switch does not forward the packet. The following aspects of the
TTL setting of incoming multicast packets must be considered, before changing this parameter on a routing
switch:

n A value that is too high will allow multicast traffic to go beyond the internal network.

n A value that is too low may prevent some intended hosts from receiving the desired multicast traffic.

n A value of 0 will forward multicast traffic regardless of the packet TTL setting.

Example

Configuring and removing the time to live threshold:

switch(config)# interface vlan40
switch(config-if-vlan)# ip pim-dense ttl-threshold 8
switch(config-if-vlan)# no ip pim-dense ttl-threshold

router pim

Syntax

router pim [vrf <VRF-NAME>]
no router pim [vrf <VRF-NAME>]

Description

Changes the current context to the PIM configuration context. If no VRF is specified, the default VRF is
assumed.

The no form of this command removes the PIM configuration from the specified context or the default VRF.

Command context

config

Parameters

vrf <VRF-NAME>

Specifies the name of a VRF.

Protocol Independent Multicast - Dense Mode (V4 and V6) | 223

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring default router PIM:

switch(config)# router pim
switch(config-pim)#

Configuring specified router PIM:

switch(config)# router pim vrf green
switch(config-pim)#

Removing router PIM:

switch(config)# no router pim

show ip mroute

Syntax

show ip mroute [all-vrfs | vrf <VRF-NAME>] [vsx-peer]

Description

Shows multicast routing information. Optionally, you can show specific information by VRF. If no options
are specified, it shows information for the default VRF.

Command context

Operator (>) or Manager (#)

Parameters

all-vrfs

Shows mroute information for all VRFs. Optional.

vrf <VRF-NAME>

Shows mroute information for a particular VRF. If the <VRF-NAME> is not specified, it shows information for
the default VRF. Optional.
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Showing IP mroute for all VRFs:

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

224

| switch#    | show      | ip mroute    | all-vrfs    |
| ---------- | --------- | ------------ | ----------- |
| VRF        | : blue    |              |             |
| Total      | number    | of entries   | : 1         |
| Group      | Address   |              | : 239.1.1.1 |
| Source     | Address   |              | : 40.0.0.5  |
| Incoming   | interface |              | : vlan3     |
| Downstream |           | Interface    |             |
| Interface  |           | State        |             |
| ---------  |           | -----        |             |
| vlan2      |           | forwarding   |             |
| VRF        | : green   |              |             |
| Total      | number    | of entries   | : 2         |
| Group      | Address   |              | : 239.1.1.1 |
| Source     | Address   |              | : 40.0.0.4  |
| Neighbor   |           |              | : 10.1.1.1  |
| Incoming   | interface |              | : vlan2     |
| Downstream |           | Interface    |             |
| Interface  |           | State        |             |
| ---------  |           | -----        |             |
| vlan5      |           | forwarding   |             |
| Group      | Address   |              | : 239.1.1.1 |
| Source     | Address   |              | : 40.0.0.5  |
| Neighbor   |           |              | : 10.1.1.2  |
| Incoming   | interface |              | : vlan1     |
| Downstream |           | Interface    |             |
| Interface  |           | State        |             |
| ---------  |           | -----        |             |
| vlan6      |           | forwarding   |             |
| VRF        | : default |              |             |
| Total      | number    | of entries   | : 1         |
| Group      | Address   |              | : 10.1.1.14 |
| Source     | Address   |              | : 40.0.0.6  |
| Neighbor   |           |              | : 10.1.1.2  |
| Incoming   | interface |              | : 1/1/5     |
| Downstream |           | Interface    |             |
| Interface  |           | State        |             |
| ---------  |           | -----        |             |
| 1/1/3      |           | forwarding   |             |
| show       | ip mroute | <GROUP-ADDR> |             |
Syntax
| show ip   | mroute | <GROUP-ADDR>      | [<SOURCE-ADDR>] |
| --------- | ------ | ----------------- | --------------- |
| [all-vrfs |        | | vrf <vrf-name>] | [vsx-peer]      |
Description
Showsthemulticastroutinginformationforthegivengroupaddress.Optionally,youcanspecifydisplay
informationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
ProtocolIndependentMulticast-DenseMode(V4andV6)|225

<GROUP-ADDR>
SpecifiesagroupaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
<SOURCE-ADDR>
SpecifiesshowinformationforthegroupfromthissourceinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255.
all-vrfs
ShowsmrouteinformationforthegroupforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showinginformationforgroup239.1.1.1andVRFgreen:
switch#
|     | show | ip mroute 239.1.1.1 | vrf green |
| --- | ---- | ------------------- | --------- |
VRF : green
| Group      | Address    |          | : 239.1.1.1 |
| ---------- | ---------- | -------- | ----------- |
| Source     | Address    |          | : 40.0.0.5  |
| Neighbor   |            |          | : 10.1.1.2  |
| Incoming   | interface  |          | : vlan1     |
| Unicast    | Routing    | Protocol | : connected |
| Metric     |            |          | : 1234      |
| Metric     | Pref       |          | : 1234      |
| Downstream | Interface  |          |             |
| Interface  | State      |          |             |
| ---------  | -----      |          |             |
| vlan6      | forwarding |          |             |
Showinginformationforgroup239.1.1.1fromsource40.0.0.5andallVRFs:
| switch# | show | ip mroute 239.1.1.1 | 40.0.0.5 all-vrfs |
| ------- | ---- | ------------------- | ----------------- |
VRF : blue
| Group      | Address    |          | : 239.1.1.1 |
| ---------- | ---------- | -------- | ----------- |
| Source     | Address    |          | : 40.0.0.5  |
| Incoming   | interface  |          | : vlan3     |
| Unicast    | Routing    | Protocol | : connected |
| Metric     |            |          | : 1234      |
| Metric     | Pref       |          | : 1234      |
| Downstream | Interface  |          |             |
| Interface  | State      |          |             |
| ---------  | -----      |          |             |
| vlan2      | forwarding |          |             |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 226

| VRF        | : green    |          |             |     |     |
| ---------- | ---------- | -------- | ----------- | --- | --- |
| Group      | Address    |          | : 239.1.1.1 |     |     |
| Source     | Address    |          | : 40.0.0.5  |     |     |
| Neighbor   |            |          | : 10.1.1.2  |     |     |
| Incoming   | interface  |          | : vlan1     |     |     |
| Unicast    | Routing    | Protocol | : connected |     |     |
| Metric     |            |          | : 1234      |     |     |
| Metric     | Pref       |          | : 1234      |     |     |
| Downstream | Interface  |          |             |     |     |
| Interface  | State      |          |             |     |     |
| ---------  | -----      |          |             |     |     |
| vlan6      | forwarding |          |             |     |     |
| show       | ip mroute  | brief    |             |     |     |
Syntax
| show ip | mroute brief | [al-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |     |
| ------- | ------------ | -------- | ----------------- | ---------- | --- |
Description
Showsbriefversionofthemulticastroutinginformation.Optionally,youcanspecifythedisplay
informationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsmrouteinformationbrieflyforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingtheIPmroutebrief:
| switch#       | show      | ip mroute      | brief   |          |           |
| ------------- | --------- | -------------- | ------- | -------- | --------- |
| VRF           | : default |                |         |          |           |
| Total         | number    | of entries     | : 1     |          |           |
| Group         | Address   | Source         | Address | Neighbor | Interface |
| ------------- |           | -------------- |         | -------- | --------- |
| 239.1.1.1     |           | 40.0.0.6       |         | 10.1.1.2 | vlan5     |
| show          | ip pim    |                |         |          |           |
ProtocolIndependentMulticast-DenseMode(V4andV6)|227

Syntax
| show ip pim | [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |     |
| ----------- | --------- | ----------------- | ---------- | --- |
Description
ShowsthePIMrouterinformation.Optionally,youcanspecifydisplayinformationbyVRF.Ifnooptionsare
specified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
Optional.ShowsPIMrouterinformationonallVRFs.
vrf <VRF-NAME>
Optional.ShowsPIMrouterinformationforaparticularVRF.Ifthe<VRF-NAME>isnotspecified,itshows
informationforthedefaultVRF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingIPPIMrouter:
| switch#       | show ip          | pim   |           |     |
| ------------- | ---------------- | ----- | --------- | --- |
| PIM Global    | Parameters       |       |           |     |
| VRF           |                  |       | : default |     |
| PIM Status    |                  |       | : Enabled |     |
| Join/Prune    | Interval         | (sec) | : 60      |     |
| SPT Threshold |                  |       | : Enabled |     |
| State         | Refresh Interval | (sec) | : 60      |     |
| show ip       | pim interface    |       |           |     |
Syntax
| show ip pim | interface | [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |
| ----------- | --------- | --------- | ----------------- | ---------- |
Description
ShowstheinformationaboutPIMinterfacescurrentlyconfiguredintherouter.Optionally,youcanspecify
displayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 228

all-vrfs
Optional.ShowsPIMinterfaceinformationforallVRFs.
vrf <VRF-NAME>
Optional.ShowsPIMinterfaceinformationforaparticularVRF.Ifthe<VRF-NAME>isnotspecified,it
showsthedefaultVRFinformation.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMinterface:
| switch#            | show ip          | pim interface     |            |
| ------------------ | ---------------- | ----------------- | ---------- |
| PIM                | Interfaces       |                   |            |
| VRF:               | default          |                   |            |
| Interface          |                  | IP Address        | mode       |
| ------------------ |                  | ----------------- | ---------- |
| 1/1/1              |                  | 40.0.0.4/24       | dense      |
| 1/1/2              |                  | 50.0.0.4/24       | dense      |
| show               | ip pim interface | <INTERFACE-NAME>  |            |
Syntax
| show ip | pim interface | <INTERFACE-NAME> | [vsx-peer] |
| ------- | ------------- | ---------------- | ---------- |
Description
ShowsdetailedinformationaboutthePIMinterfacecurrentlyconfigured.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-NAME>
SpecifiesaninterfaceforshowingPIMinterfaceinformation.InterfacecanalsobeaLAGorVLAN.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ProtocolIndependentMulticast-DenseMode(V4andV6)|229

ShowingPIMinterfaceinformationforinterface1/1/2:
| switch#     | show ip             | pim interface | 1/1/2            |     |             |          |       |
| ----------- | ------------------- | ------------- | ---------------- | --- | ----------- | -------- | ----- |
| PIM         | Interfaces          |               |                  |     |             |          |       |
| VRF:        | default             |               |                  |     |             |          |       |
| Interface   | : 1/1/2             |               |                  |     |             |          |       |
| IP Address  | : 50.0.0.4/24       |               |                  |     |             |          |       |
| Mode        | : dense             |               |                  |     |             |          |       |
| Designated  | Router              | :             |                  |     |             |          |       |
| Hello       | Interval            | (sec)         | : 30             |     |             |          |       |
| Hello       | Delay (sec)         |               | : 5              |     |             |          |       |
| Graft       | Retry Interval(sec) |               | : 3              |     |             |          |       |
| Max         | Graft Retries       |               | : 5              |     |             |          |       |
| SR TTL      | Threshold           |               | : 8              |     |             |          |       |
| Override    | Interval            | (msec)        | : 2500           |     | Lan Prune   | Delay    | : Yes |
| Propagation | Delay               | (msec)        | : 500            |     | DR Priority |          | : 1   |
| Neighbor    | Timeout             |               | : 105            |     |             |          |       |
| show        | ip pim interface    |               | <INTERFACE-NAME> |     |             | counters |       |
Syntax
| show ip | pim interface | <INTERFACE-NAME> |     | counters | [vsx-peer] |     |     |
| ------- | ------------- | ---------------- | --- | -------- | ---------- | --- | --- |
Description
ShowsthePIMpacketcountersinformationforthespecifiedinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-NAME>
Specifiestheinterfacetoshowpacketcounterinformation.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMpacketcounters:
| switch#   | show ip | pim interface | vlan1 | counters |     |     |     |
| --------- | ------- | ------------- | ----- | -------- | --- | --- | --- |
| Interface |         | : vlan1       |       |          |     |     |     |
| VRF       |         | : default     |       |          |     |     |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 230

Rx Counters :

Hello
State Refresh
Join/Prune
RPadv
Graft
GraftAck
Assert
Bsm

Tx Counters :

Hello
State Refresh
Join/Prune
RPadv
Graft
GraftAck
Assert
Bsm

4
0
1
0
0
0
0
0

9
0
0
0
0
0
0
0

Invalid Rx Counters :

Hello
State Refresh
Join/Prune
RPadv
Graft
GraftAck
Assert
Bsm

0
0
0
0
0
0
0
0

show ip pim neighbor

Syntax

show ip pim neighbor [<IP-ADDR>]

[all-vrfs | vrf <VRF-NAME>] [vsx-peer]

Description

Shows PIM neighbor information. Optionally, you can specify display information by VRF. If no options are
specified, it shows information for the default VRF.

Parameters

all-vrfs

Selects all VRFs.

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Protocol Independent Multicast - Dense Mode (V4 and V6) | 231

Example
ShowingPIMneighborinformation:
switch#
|              | show ip pim | neighbor    |     |
| ------------ | ----------- | ----------- | --- |
| PIM Neighbor |             |             |     |
| VRF          |             | : default   |     |
| IP Address   |             | : 40.0.0.44 |     |
| Interface    |             | : 1/1/1     |     |
| Up Time      | (sec)       | : 544       |     |
| Expire       | Time (sec)  | : 80        |     |
| DR Priority  |             | : 40        |     |
state-refresh-interval
Syntax
| state-refresh | <INTERVAL-VALUE> |     |     |
| ------------- | ---------------- | --- | --- |
no state-refresh
Description
Configurestheintervalbetweensuccessivestate-refreshmessagesoriginatedbytheroutingswitch.Only
theroutingswitchconnecteddirectlytothemulticastsourceinitiatesstate-refreshpackets.AllotherPIM
routersinthenetworkonlypropagatethesestate-refreshpackets.
Thenoformofthiscommandsetstheintervaltothedefaultvalueof60seconds.
Commandcontext
config-pim
Parameters
<INTERVAL-VALUE>
Specifiesthestaterefreshintervalinseconds.Default:60seconds.Range10-100.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringthestaterefreshinterval:
| switch(config)#     | router   | pim              |      |
| ------------------- | -------- | ---------------- | ---- |
| switch(config-pim)# |          | state-refresh    | 30   |
| switch(config-pim)# |          | no state-refresh |      |
| PIM-DM              | commands | for              | IPv6 |
disable
Syntax
disable
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 232

Description

Disables PIMv6 globally on the router.

Using the disable command will cause all the multicast routes to be erased from hardware.

Command context

config-pim6

Authority

Administrators or local user group members with execution rights for this command.

Example

Disabling PIM router:

switch(config)# router pim6
switch(config-pim6)# disable

enable

Syntax

enable

Description

Enables PIMv6 globally on the router.

Command context

config-pim6

Authority

Administrators or local user group members with execution rights for this command.

Example

Enabling PIM router:

switch(config)# router pim6
switch(config-pim6)# enable

ipv6 pim6-dense {enable|disable}

Syntax

ipv6 pim6-dense {enable | disable}

Description

Enables or disables PIM-DM on the current interface. PIM-DM is disabled by default on an interface. An IPv6
address must be configured on the interface to enable PIM-DM.

Protocol Independent Multicast - Dense Mode (V4 and V6) | 233

Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
enable
EnablesPIM-DMontheinterface.IPv6addressmustbeconfiguredontheinterfacetoenablePIM-SM
| (usetheipv6 address | <X:X::X:X/M>command). |     |     |     |
| ------------------- | --------------------- | --- | --- | --- |
disable
DisablesPIM-DMontheinterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablinganddisablingPIM-DMonaninterface:
| switch(config)#         | interface | vlan40 |            |             |
| ----------------------- | --------- | ------ | ---------- | ----------- |
| switch(config-if-vlan)# |           | ipv6   | address    | 2001::01/64 |
| switch(config-if-vlan)# |           | ipv6   | pim6-dense | enable      |
| switch(config-if-vlan)# |           | ipv6   | pim6-dense | disable     |
| ipv6 pim6-dense         | bfd       |        |            |             |
Syntax
| ipv6 pim6-dense    | bfd [disable] |     |     |     |
| ------------------ | ------------- | --- | --- | --- |
| no ipv6 pim6-dense | bfd           |     |     |     |
Description
ConfiguresBFDonaper-interfacebasisforaninterfaceassociatedwiththePIMprocess.
ThenoformofthiscommandremovestheBFDconfigurationontheinterfaceandsetsittothedefault
configuration.
IfBFDisenabledglobally,itwillbeenabledbydefaultonallinterfaces.Theonlyexceptioniswhenitisdisabled
specificallyonaninterfaceusingtheipv6 pim6-dense bfd disablecommand.
IfBFDisdisabledglobally,itwillbedisabledbydefaultonallinterfaces.Theonlyexceptioniswhenitisenabled
| specificallyonaninterfaceusingtheipv6 |     |     | pim6-dense | bfdcommand. |
| ------------------------------------- | --- | --- | ---------- | ----------- |
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
disable
DisablestheBFDconfigurationontheinterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 234

Examples
EnablingtheBFDconfigurationontheinterface:
switch(config)#
|                         | interface | vlan40          |     |
| ----------------------- | --------- | --------------- | --- |
| switch(config-if-vlan)# |           | ipv6 pim6-dense | bfd |
DisablingtheBFDconfigurationontheinterface:
| switch(config-if-vlan)# |     | ipv6 pim6-dense | bfd disable |
| ----------------------- | --- | --------------- | ----------- |
RemovingtheBFDconfigurationontheinterface:
| switch(config-if-vlan)# |                      | no ipv6 pim6-dense | bfd |
| ----------------------- | -------------------- | ------------------ | --- |
| ipv6 pim6-dense         | graft-retry-interval |                    |     |
Syntax
| ipv6 pim6-dense    | graft-retry-interval | <INTERVAL-VALUE> |     |
| ------------------ | -------------------- | ---------------- | --- |
| no ipv6 pim6-dense | graft-retry-interval |                  |     |
Description
Configurestheintervalforwhichtheroutingswitchwaitsforthegraftacknowledgmentfromanother
routerbeforeresendingthegraftrequest.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetstothedefaultof3seconds.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<INTERVAL-VALUE>
Specifiestheintervaltheroutingswitchwaitsforthegraftacknowledgement.Default:3seconds.Range:
1-10.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Graftpacketsresultwhenadownstreamroutertransmitsarequesttojoinaflow.Theupstreamrouter
respondswithagraftacknowledgmentpacket.Ifthegraftacknowledgmentisnotreceivedwithinthetime
periodofthegraft-retry-interval,itresendsthegraftpacket.
Example
Configuringandremovingdensegraftretryinterval:
ProtocolIndependentMulticast-DenseMode(V4andV6)|235

| switch(config)# | interface | vlan40 |     |     |
| --------------- | --------- | ------ | --- | --- |
switch(config-if-vlan)#
|                         |             | ipv6 pim6-dense    | graft-retry-interval | 5   |
| ----------------------- | ----------- | ------------------ | -------------------- | --- |
| switch(config-if-vlan)# |             | no ipv6 pim6-dense | graft-retry-interval |     |
| ipv6 pim6-dense         | hello-delay |                    |                      |     |
Syntax
| ipv6 pim6-dense    | hello-delay | <DELAY-VALUE> |     |     |
| ------------------ | ----------- | ------------- | --- | --- |
| no ipv6 pim6-dense | hello-delay |               |     |     |
Description
ConfiguresthemaximumtimeinsecondsbeforetherouteractuallytransmitstheinitialPIMhellomessage
onthecurrentinterface.
Thenoformofthiscommandremovescurrentlyconfiguredvalueandsetstothedefaultof5seconds.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<DELAY-VALUE>
Specifiesthehello-delayinseconds,whichisthemaximumtimebeforeatriggeredPIMHellomessageis
transmittedonthisinterface.Default:5seconds.Range:0-5.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
n Incaseswhereanewinterfaceactivatesconnectionswithmultiplerouters,ifalltheconnectedrouters
senthellopacketsatthesametime,thereceivingroutercouldbecomemomentarilyoverloaded.
n Thiscommandrandomizesthetransmissiondelaytoatimebetweenzeroandthehellodelaysetting.
Usingzeromeansnodelay.Aftertheroutersendstheinitialhellopackettoanewlydetectedinterface,it
sendssubsequenthellopacketsaccordingtothecurrenthellointervalsetting.
Example
Configuringandremovinghello-delayinterface:
| switch(config)#         | interface      | vlan40             |             |     |
| ----------------------- | -------------- | ------------------ | ----------- | --- |
| switch(config-if-vlan)# |                | ipv6 pim6-dense    | hello-delay | 4   |
| switch(config-if-vlan)# |                | no ipv6 pim6-dense | hello-delay |     |
| ipv6 pim6-dense         | hello-interval |                    |             |     |
Syntax
| ipv6 pim6-dense    | hello-interval | <INTERVAL-VALUE> |     |     |
| ------------------ | -------------- | ---------------- | --- | --- |
| no ipv6 pim6-dense | hello-interval |                  |     |     |
Description
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 236

Configures the frequency at which the router transmits PIM hello messages on the current interface.

The no form of this command removes the currently configured value and sets to the default of 30 seconds.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

<INTERVAL-VALUE>

Specifies the frequency at which PIM Hello messages are transmitted on this interface. Default: 30
seconds. Range: 5-300.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n The router uses hello packets to inform neighbor routers of its presence.

n The router also uses this setting to compute the hello holdtime, which is included in hello packets sent to

neighbor routers.

n Hello holdtime tells neighbor routers how long to wait for the next hello packet from the router. If

another packet does not arrive within that time, the router removes the neighbor adjacency on that
interface from the PIM adjacency table, which removes any flows running on that interface.

n Shortening the hello interval reduces the hello holdtime. If they do not receive a new hello packet when

expected, it changes how quickly other routers stop sending traffic to the router.

Example

Configuring and removing dense hello-interval:

switch(config)# interface 1/1/4
switch(config-if)# ipv6 pim6-dense hello-interval 60
switch(config-if)# no ipv6 pim6-dense hello-interval

ipv6 pim6-dense ipv6-addr

Syntax

ipv6 pim6-dense ipv6-addr {<IPV6-ADDR-VALUE> | any}
no ipv6 pim6-dense ipv6-addr

Description

Enables the router to dynamically determine the source IP address to use for PIM packets sent from the
interface or to use the specific IP address.

The no form of this command removes the currently configured value and sets to the default of any.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

Protocol Independent Multicast - Dense Mode (V4 and V6) | 237

<IPV6-ADDR-VALUE>
SpecifiesanIPv6addressasthesourceIPfortheinterface.
any
SpecifiesdynamicallydeterminingthesourceIPfromthecurrentIPv6addressoftheinterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringandremovingthesourceIPaddress:
| switch(config)#         | interface       | vlan40             |                  |
| ----------------------- | --------------- | ------------------ | ---------------- |
| switch(config-if-vlan)# |                 | ipv6 pim6-dense    | ip-addr 2001::02 |
| switch(config-if-vlan)# |                 | no ipv6 pim6-dense | ipv6-addr        |
| ipv6 pim6-dense         | lan-prune-delay |                    |                  |
Syntax
| ipv6 pim6-dense    | lan-prune-delay |     |     |
| ------------------ | --------------- | --- | --- |
| no ipv6 pim6-dense | lan-prune-delay |     |     |
Description
EnablestheLANprunedelayoptiononthecurrentinterface.Thedefaultstatusisenabled.
ThenoformofthiscommanddisablestheLANprunedelayoption.
Commandcontext
config-if
config-if-vlan
config-lag-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
WithLAN-prune-delayenabled,therouterinformsdownstreamneighborshowlongitwillwaitbefore
pruningaflowafterreceivingaprunerequest.Otherdownstreamroutersonthesameinterfacemustsend
ajointooverridetheprunebeforetheLAN-prune-delaytimetocontinuetheflow.Promptsany
downstreamneighborswithmulticastreceiverscontinuingtobelongtotheflowtoreplywithajoin.Ifno
joinsarereceivedaftertheLAN-prune-delayperiod,therouterprunestheflow.Thepropagation-delayand
override-intervalsettingsdeterminetheLAN-prune-delaysetting.
Example
EnablinganddisablingtheLANprunedelay:
| switch(config)#         | interface         | vlan40             |                 |
| ----------------------- | ----------------- | ------------------ | --------------- |
| switch(config-if-vlan)# |                   | ipv6 pim6-dense    | lan-prune-delay |
| switch(config-if-vlan)# |                   | no ipv6 pim6-dense | lan-prune-delay |
| ipv6 pim6-dense         | max-graft-retries |                    |                 |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 238

Syntax
| ipv6 pim6-dense    | max-graft-retries | <ATTEMPT-VALUE> |     |     |
| ------------------ | ----------------- | --------------- | --- | --- |
| no ipv6 pim6-dense | max-graft-retries |                 |     |     |
Description
Configuresthenumberofattemptstheroutingswitchwillretrysendingthesamegraftpackettojoina
flow.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetstothedefaultof3attempts.
Commandcontext
config-if
config-if-vlan
config-lag-if
Parameters
<INTERVAL-VALUE>
Specifiesthenumberofretriesfortheroutingswitchtoresendthegraftpacket.Default:3attempts.
Range:1-10.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Ifagraftacknowledgmentresponseisnotreceivedafterthespecifiednumberofretries,theroutingswitch
ceasestryingtojointheflow.Inthiscasetheflowisremoveduntileitherastate-refreshfromupstreamre-
initiatesthefloworanupstreamrouterfloodstheflow.Increasingthisvaluehelpstoimprovemulticast
reliability.
Example
Configuringandremovingthedensegraftretryinterval:
| switch(config)#         | interface         | vlan40             |                   |     |
| ----------------------- | ----------------- | ------------------ | ----------------- | --- |
| switch(config-if-vlan)# |                   | ipv6 pim6-dense    | max-graft-retries | 6   |
| switch(config-if-vlan)# |                   | no ipv6 pim6-dense | max-graft-retries |     |
| ipv6 pim6-dense         | override-interval |                    |                   |     |
Syntax
| ipv6 pim6-dense    | override-interval | <INTERVAL-VALUE> |     |     |
| ------------------ | ----------------- | ---------------- | --- | --- |
| no ipv6 pim6-dense | override-interval |                  |     |     |
Description
ConfigurestheoverrideintervalthatgetsinsertedintotheOverrideIntervalfieldofaLANPruneDelay
option.
Thenoformofthiscommandremovesthecurrentlyconfiguredvalueandsetsthevaluetothedefaultof
2500ms.
Commandcontext
config-if
config-if-vlan
ProtocolIndependentMulticast-DenseMode(V4andV6)|239

config-lag-if

Parameters

<INTERVAL-VALUE>

Specifies the override interval of a LAN Prune Delay option in ms. Default: 2500 ms. Range: 500-6000.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Each router on the LAN expresses its view of the amount of randomization necessary in the Override
Interval field of the LAN Prune Delay option. When all routers on a LAN use the LAN Prune Delay Option, all
routers on the LAN MUST set their Override_Interval to the largest Override value on the LAN.

Example

Configuring and removing the override interval:

switch(config)# interface vlan40
switch(config-if-vlan)# ipv6 pim6-dense override-interval 4000
switch(config-if-vlan)# no ipv6 pim6-dense override-interval

ipv6 pim6-dense propagation-delay

Syntax

ipv6 pim6-dense propagation-delay <DELAY-VALUE>
no ipv6 pim6-dense propagation-delay

Description

Configures the propagation delay that gets inserted into the LAN prune delay field of a LAN Prune Delay
option.

The no form of this command removes currently configured value and sets to the default of 500 ms.

Command context

config-if
config-if-vlan
config-lag-if

Parameters

<DELAY-VALUE>

Specifies the propagation delay value in ms. Default: 500 ms. Range: 250-2000.

Authority

Administrators or local user group members with execution rights for this command.

Usage

The LAN Delay inserted by a router in the LAN Prune Delay option expresses the expected message
propagation delay on the link. When all routers on a link use the LAN Prune Delay Option, all routers on the
LAN MUST set Propagation Delay to the largest LAN Delay on the LAN.

Examples

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

240

Configuring and removing the propagation delay:

switch(config)# interface vlan40
switch(config-if-vlan)# ipv6 pim6-dense propagation-delay 400
switch(config-if-vlan)# no ipv6 pim6-dense propagation-delay

ipv6 pim6-dense ttl-threshold

Syntax

ipv6 pim6-dense ttl-threshold <THRESHOLD-VALUE>
no ipv6 pim6-dense ttl-threshold

Description

Configures the multicast datagram time-to-live (router hop-count) threshold for the interface. Any IP
multicast datagrams or state-refresh packets with a TTL less than this threshold will not be forwarded out
the interface.

The no form of this command removes the currently configured value and sets to the default of 3 attempts.

Command context

config-if

config-if-vlan

config-lag-if

Parameters

<THRESHOLD-VALUE>

Specifies the time to live threshold. Default: 3 attempts. Range: 0-255.

Authority

Administrators or local user group members with execution rights for this command.

Usage

The VLAN connected to the multicast source does not receive state refresh packets and thus is not state-
refresh capable. Downstream VLANs in the switches are state-refresh capable. This parameter provides a
method for containing multicast traffic within a network, or even within specific areas of a network. Initially,
the multicast traffic source sets a TTL value in the packets it transmits. Each time one of these packets
passes through a multicast routing device, the TTL setting decrements by 1. If the packet arrives with a TTL
lower than the ttl-threshold, the routing switch does not forward the packet. The following aspects of the
TTL setting of incoming multicast packets must be considered, before changing this parameter on a routing
switch:

n A value that is too high will allow multicast traffic to go beyond the internal network.

n A value that is too low may prevent some intended hosts from receiving the desired multicast traffic.

n A value of 0 will forward multicast traffic regardless of the packet TTL setting.

Example

Configuring and removing the time to live threshold:

Protocol Independent Multicast - Dense Mode (V4 and V6) | 241

| switch(config)# |     | interface | vlan40 |     |     |
| --------------- | --- | --------- | ------ | --- | --- |
switch(config-if-vlan)#
|                         |            |     | ipv6 pim6-dense    | ttl-threshold | 8   |
| ----------------------- | ---------- | --- | ------------------ | ------------- | --- |
| switch(config-if-vlan)# |            |     | no ipv6 pim6-dense | ttl-threshold |     |
| no ipv6                 | pim6-dense |     |                    |               |     |
Syntax
no ip pim-dense
Description
RemovesPIM-DMforallIPv6relatedconfigurationsfortheinterface.
Commandcontext
config-if
config-if-vlan
config-lag-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
RemovingallPIM-DMconfigurationsonaninterface:
| switch(config)#         |           | interface | vlan40             |     |     |
| ----------------------- | --------- | --------- | ------------------ | --- | --- |
| switch(config-if-vlan)# |           |           | no ipv6 pim6-dense |     |     |
| show                    | ipv6 pim6 |           |                    |     |     |
Syntax
| show ipv6 | pim6 [all-vrfs | |   | vrf <VRF-NAME>] | [vsx-peer] |     |
| --------- | -------------- | --- | --------------- | ---------- | --- |
Description
ShowsthePIMrouterinformation.Optionally,youcanspecifydisplayinformationbyVRF.Ifnooptionsare
specified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 242

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingtheIPv6PIMrouter:
| switch#    | show      | ipv6       | pim6      |            |     |
| ---------- | --------- | ---------- | --------- | ---------- | --- |
| PIM        | Global    | Parameters |           |            |     |
| VRF        |           |            |           | : default  |     |
| PIM        | Status    |            |           | : Enabled  |     |
| Join/Prune |           | Interval   | (sec)     | : 46       |     |
| SPT        | Threshold |            |           | : Disabled |     |
| show       | ipv6      | pim6       | interface |            |     |
Syntax
| show ipv6 | pim6 | interface | [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |
| --------- | ---- | --------- | --------- | ----------------- | ---------- |
Description
ShowstheinformationaboutPIMinterfacescurrentlyconfiguredintherouter.Optionally,youcanspecify
displayinformationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
Optional.ShowsPIMinterfaceinformationforallVRFs.
vrf <VRF-NAME>
Optional.ShowsPIMinterfaceinformationforaparticularVRF.Ifthe<VRF-NAME>isnotspecified,it
showsthedefaultVRFinformation.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMinterface:
| switch# | show       | ipv6 | pim6 interface |     |     |
| ------- | ---------- | ---- | -------------- | --- | --- |
| PIM     | Interfaces |      |                |     |     |
| VRF:    | default    |      |                |     |     |
ProtocolIndependentMulticast-DenseMode(V4andV6)|243

| Interface |     | IP Address |     |     |     |     |
| --------- | --- | ---------- | --- | --- | --- | --- |
mode
------------------ -------------------------------------------------------------- -
---------
| 1/1/1 |     | fe80::a00:9ff:feec:dc0e/64 |     |     |     |     |
| ----- | --- | -------------------------- | --- | --- | --- | --- |
dense
| show | ipv6 pim6 | interface | <INTERFACE-NAME> |     |     |     |
| ---- | --------- | --------- | ---------------- | --- | --- | --- |
Syntax
| show ipv6 | pim6 interface | <INTERFACE-NAME> | [vsx-peer] |     |     |     |
| --------- | -------------- | ---------------- | ---------- | --- | --- | --- |
Description
ShowsdetailedinformationaboutthePIMinterfacecurrentlyconfigured.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-NAME>
SpecifiesaninterfaceforshowingPIMinterfaceinformation.InterfacecanalsobeaLAGorVLAN.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingPIMinterfaceinformationforinterface1/1/1:
| switch#     | show ipv6      | pim6 interface               | 1/1/1 |               |         |       |
| ----------- | -------------- | ---------------------------- | ----- | ------------- | ------- | ----- |
| PIM         | Interfaces     |                              |       |               |         |       |
| VRF:        | default        |                              |       |               |         |       |
| Interface   |                | : 1/1/1                      |       |               |         |       |
| IPv6        | Address        | : fe80::a00:9ff:feec:dc0e/64 |       |               |         |       |
| Mode        |                | : dense                      |       |               |         |       |
| Designated  | Router         | : fe80::a00:9ff:febd:8364    |       |               |         |       |
| Hello       | Interval       | : 30 sec                     |       |               |         |       |
| Hello       | Delay          | : 4 sec                      |       |               |         |       |
| Override    | Interval       | : 500                        | msec  | LAN Prune     | Delay   | : Yes |
| Propagation | Delay          | : 350                        | msec  | DR Priority   |         | : 3   |
| Neighbor    | Timeout        | : 0                          |       | TTL Threshold |         | : 250 |
| Graft       | Retry Interval | : 9                          |       | Max Graft     | Retries | : 9   |
| show        | ipv6 mroute    |                              |       |               |         |       |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 244

Syntax
| show ipv6 | mroute [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |
| --------- | ---------------- | ----------------- | ---------- |
Description
Showsmulticastroutinginformation.Optionally,youcanshowspecificinformationbyVRF.Ifnooptions
arespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingIPv6mroute:
switch#
|          | show ipv6 mroute        | all-vrfs    |     |
| -------- | ----------------------- | ----------- | --- |
| IP       | Multicast Route Entries |             |     |
| VRF      | : blu                   |             |     |
| Total    | number of entries       | : 2         |     |
| Group    | Address                 | : ff08::1:3 |     |
| Source   | Address                 | : 2002::04  |     |
| Neighbor |                         | : 2001::04  |     |
| Incoming | interface               | : 1/1/2     |     |
| Outgoing | Interface List          | :           |     |
Interface State
--------- -----
1/1/3 pruned
1/1/4 forwarding
| Group    | Address        | : ff08::1:4 |     |
| -------- | -------------- | ----------- | --- |
| Source   | Address        | : 2003::04  |     |
| Neighbor |                | : 2001::04  |     |
| Incoming | interface      | : 1/1/2     |     |
| Outgoing | Interface List | :           |     |
Interface State
--------- -----
1/1/3 pruned
| VRF   | : default         |     |     |
| ----- | ----------------- | --- | --- |
| Total | number of entries | : 1 |     |
ProtocolIndependentMulticast-DenseMode(V4andV6)|245

| Group     | Address   |        | :      | ff08::1:5 |     |
| --------- | --------- | ------ | ------ | --------- | --- |
| Source    | Address   |        | :      | 2001::03  |     |
| Neighbor  |           |        | :      | 2003::04  |     |
| Incoming  | interface |        | :      | 1/1/1     |     |
| Outgoing  | Interface |        | List : |           |     |
| Interface |           | State  |        |           |     |
| --------- |           | -----  |        |           |     |
| 1/1/4     |           | pruned |        |           |     |
| show      | ipv6      | mroute | brief  |           |     |
Syntax
| show ipv6 | mroute | brief | [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |
| --------- | ------ | ----- | --------- | ----------------- | ---------- |
Description
Showsbriefversionofthemulticastroutinginformation.Optionally,youcanspecifythedisplay
informationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingtheIPv6mroutebrief:
| switch#   | show      | ipv6        | mroute brief | all-vrfs |     |
| --------- | --------- | ----------- | ------------ | -------- | --- |
| IP        | Multicast | Route       | Entries      |          |     |
| VRF       | : blu     |             |              |          |     |
| Total     | number    | of entries  | :            | 2        |     |
| Group     | Address   | : ff08::1:3 |              |          |     |
| Source    | Address   | : 2002::04  |              |          |     |
| Neighbor  |           | : 2003::04  |              |          |     |
| Interface |           | :           | 1/1/2        |          |     |
| Group     | Address   | : ff08::1:4 |              |          |     |
| Source    | Address   | : 2002::03  |              |          |     |
| Neighbor  |           | : 2003::05  |              |          |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 246

| Interface |           | :           | 1/1/3        |     |     |
| --------- | --------- | ----------- | ------------ | --- | --- |
| VRF       | : default |             |              |     |     |
| Total     | number    | of entries  | :            | 1   |     |
| Group     | Address   | : ff08::1:5 |              |     |     |
| Source    | Address   | : 2001::03  |              |     |     |
| Neighbor  |           | : 2002::01  |              |     |     |
| Interface |           | :           | 1/1/1        |     |     |
| show      | ipv6      | mroute      | <GROUP-ADDR> |     |     |
Syntax
| show ipv6 | mroute | <GROUP-ADDR>      |     | [<SOURCE-ADDR>] |     |
| --------- | ------ | ----------------- | --- | --------------- | --- |
| [all-vrfs |        | | vrf <vrf-name>] |     | [vsx-peer]      |     |
Description
Showsthemulticastroutinginformationforthegivengroupaddress.Optionally,youcanspecifydisplay
informationbyVRF.Ifnooptionsarespecified,itshowsinformationforthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
<GROUP-ADDR>
Specifiesshowinformationforthegroupaddress.Format:X:X::X:X
<SOURCE-ADDR>
Optional.Specifiesshowinformationforthegroupfromthissource.Format:X:X::X:X
all-vrfs
Optional.ShowsmrouteinformationforthegroupforallVRFs.
vrf <VRF-NAME>
Optional.ShowsmrouteinformationforthegroupforaparticularVRF.Ifthe<VRF-NAME>isnot
specified,itshowsinformationforthedefaultVRF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showinginformationforgroupff08::1:3andVRFgreen:
| switch# | show      | ipv6  | mroute  | ff08::1:3 | vrf green |
| ------- | --------- | ----- | ------- | --------- | --------- |
| IP      | Multicast | Route | Entries |           |           |
| VRF     | : green   |       |         |           |           |
ProtocolIndependentMulticast-DenseMode(V4andV6)|247

| Group Address |                  | : ff08::1:3 |     |
| ------------- | ---------------- | ----------- | --- |
| Source        | Address          | : 2001::03  |     |
| Neighbor      |                  | : 2003::04  |     |
| Incoming      | Interface        | : 1/1/1     |     |
| Multicast     | Routing Protocol | : PIM-DM    |     |
| Unicast       | Routing Protocol | : connected |     |
| Metric        |                  | : 0         |     |
| Metric        | Pref             | : 0         |     |
| Downstream    | Interface        |             |     |
| Interface     | State            |             |     |
| ---------     | -----            |             |     |
| 1/1/4         | pruned           |             |     |
Showinginformationforgroupff08::1:3fromsource2001::03andallVRFs:
| switch#      | show ipv6 mroute | ff08::1:3 | 2001::03 all-vrfs |
| ------------ | ---------------- | --------- | ----------------- |
| IP Multicast | Route Entries    |           |                   |
VRF : blue
| Group Address |                  | : ff08::1:3 |     |
| ------------- | ---------------- | ----------- | --- |
| Source        | Address          | : 2001::03  |     |
| Neighbor      |                  | : 2003::04  |     |
| Incoming      | Interface        | : 1/1/1     |     |
| Multicast     | Routing Protocol | : PIM-DM    |     |
| Unicast       | Routing Protocol | : connected |     |
| Metric        |                  | : 0         |     |
| Metric        | Pref             | : 0         |     |
| Downstream    | Interface        |             |     |
| Interface     | State            |             |     |
| ---------     | -----            |             |     |
| 1/1/4         | pruned           |             |     |
VRF : green
| Group Address |                  | : ff08::1:3 |     |
| ------------- | ---------------- | ----------- | --- |
| Source        | Address          | : 2001::03  |     |
| Neighbor      |                  | : 2003::04  |     |
| Incoming      | Interface        | : 1/1/2     |     |
| Multicast     | Routing Protocol | : PIM-DM    |     |
| Unicast       | Routing Protocol | : connected |     |
| Metric        |                  | : 0         |     |
| Metric        | Pref             | : 0         |     |
| Downstream    | Interface        |             |     |
| Interface     | State            |             |     |
| ---------     | -----            |             |     |
| 1/1/4         | pruned           |             |     |
VRF : red
| Group Address |                  | : ff08::1:6 |     |
| ------------- | ---------------- | ----------- | --- |
| Source        | Address          | : 2001::04  |     |
| Neighbor      |                  | : 2003::04  |     |
| Incoming      | Interface        | : 1/1/2     |     |
| Multicast     | Routing Protocol | : PIM-DM    |     |
| Unicast       | Routing Protocol | : connected |     |
| Metric        |                  | : 0         |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 248

| Metric     | Pref |            |          | : 0 |             |
| ---------- | ---- | ---------- | -------- | --- | ----------- |
| Downstream |      | Interface  |          |     |             |
| Interface  |      | State      |          |     | By_Proxy_Dr |
| ---------  |      | -----      |          |     | ----------- |
| vlan10     |      | forwarding |          |     | false       |
| show       | ipv6 | pim6       | neighbor |     |             |
Syntax
| show ipv6 | pim6 | neighbor | [<IPv6-ADDR>] |            |     |
| --------- | ---- | -------- | ------------- | ---------- | --- |
| [all-vrfs |      | | vrf    | <VRF-NAME>]   | [vsx-peer] |     |
Description
ShowsPIMneighborinformation.Optionally,youcanspecifydisplayinformationbyVRF.Ifnooptionsare
specified,itshowsinformationforthedefaultVRF.
Parameters
<IPv6-ADDR>
SpecifiesaneighboraddressinIPv6format(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
all-vrfs
ShowsinformationforallVRFs.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingPIMneighborinformation:
| switch#   | show       | ipv6  | pim6 neighbor |     |     |
| --------- | ---------- | ----- | ------------- | --- | --- |
| PIM       | Neighbor   |       |               |     |     |
| VRF       |            |       | : default     |     |     |
| IP        | Address    |       | : 2001::02    |     |     |
| Interface |            |       | : 1/1/1       |     |     |
| Up        | Time (sec) |       | : 0           |     |     |
| Expire    | Time       | (sec) | : 0           |     |     |
| DR        | Priority   |       | : 44          |     |     |
| router    | pim6       |       |               |     |     |
Syntax
ProtocolIndependentMulticast-DenseMode(V4andV6)|249

router pim6 [vrf <VRF-NAME>]
no router pim6 [vrf <VRF-NAME>]

Description

Changes the current context to the PIMv6 configuration context. If no VRF is specified, the default VRF is
assumed.

The no form of this command removes the PIM configuration from the specified context or the default VRF.

Command context

config

Parameters

vrf <VRF-NAME>

Specifies the name of a VRF. Default: default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring default router PIM:

switch(config)# router pim6
switch(config-pim6)#

Configuring specified router PIM:

switch(config)# router pim6 vrf Green
switch(config-pim6)#

Removing router PIM:

switch(config)# no router pim6

state-refresh-interval

Syntax

state-refresh <INTERVAL-VALUE>
no state-refresh

Description

Configures the interval between successive state-refresh messages originated by the routing switch. Only
the routing switch connected directly to the unicast source initiates state-refresh packets. All other PIM
routers in the network only propagate these state-refresh packets.

The no form of this command sets the interval to the default value of 60 seconds.

Command context

config-pim6

Parameters

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

250

<INTERVAL-VALUE>
Specifiesthestaterefreshintervalinseconds.Default:60seconds.Range10-100.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringthestaterefreshinterval:
| switch(config)# router | pim6             |     |
| ---------------------- | ---------------- | --- |
| switch(config-pim6)#   | state-refresh    | 30  |
| switch(config-pim6)#   | no state-refresh |     |
ProtocolIndependentMulticast-DenseMode(V4andV6)|251

Multicast Source Discovery Protocol
(MSDP)

Chapter 8

Multicast Source Discovery Protocol (MSDP)

Multicast Source Discovery Protocol (MSDP) is a mechanism to connect multiple Protocol Independent
Multicast sparse mode (PIM-SM) domains. MSDP allows multicast sources for a group to be known to all
rendezvous points (RPs) in different domains. An RP runs MSDP over TCP to discover multicast sources in
other domains. The main advantage of MSDP is that it reduces the complexity of interconnecting multiple
PIM-SM domains by allowing PIM-SM domains to use an interdomain source tree (rather than a common
shared tree).

Multicast Source Discovery Protocol (MSDP) overview

When MSDP is configured in a network, RPs running MSDP exchange source information with MSDP
enabled RPs in other domains. An RP can join the interdomain source tree for sources that are sending to
groups for which it has receivers. The RP can do that because it is the root of the shared tree within its
domain, which has branches to all points in the domain where there are active receivers. When a last-hop
device learns of a new source outside the PIM-SM domain (through the arrival of a multicast packet from the
source down the shared tree), it then can send a join toward the source and join the interdomain source tree,
which behaves similar to a local PIM register packet.

Benefits of Using MSDP to Interconnect Multiple PIM-SM Domains:

n Allows a rendezvous point (RP) to dynamically discover active sources outside of its domain.

n Introduces a more manageable approach for building multicast distribution trees between multiple

domains and thus provides administrative independence.

n Allows filtering.

PIM Anycast RP is supported with the help of MSDP mesh groups. The main purpose of an Anycast RP
implementation is that the downstream multicast routers will see just one address for an RP.

Currently, only intra-domain MSDP deployments are supported; inter-domain MSDP deployments are not

supported.

MSDP router config commands

disable

Syntax

disable

Description

Disables MSDP on the VRF.

Command context

config-msdp

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

252

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DisablingMSDP:
| switch(config)#      |     | router msdp |
| -------------------- | --- | ----------- |
| switch(config-msdp)# |     | disable     |
enable
Syntax
enable
Description
EnablesMSDPontheVRF.
Commandcontext
config-msdp
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
EnablingMSDP:
| switch(config)#      |      | router msdp |
| -------------------- | ---- | ----------- |
| switch(config-msdp)# |      | enable      |
| router               | msdp |             |
Syntax
| router    | msdp [vrf | <VRF-NAME>] |
| --------- | --------- | ----------- |
| no router | msdp [vrf | <VRF-NAME>] |
Description
ChangesthecurrentcontexttotheMSDProutercontext.IfnoVRFisspecified,thedefaultVRFMSDP
contextoftherouterisassumed.
ThenoformofthiscommandremovestheMSDPconfigurationfromthespecifiedcontextorthedefault
VRF.
Commandcontext
config
Parameters
vrf <VRF-NAME>
SpecifiesthecontexttothespecifiedVRF.
Authority
MulticastSourceDiscoveryProtocol(MSDP)|253

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringdefaultMSDProutercontext:
| switch(config)# | router | msdp |     |
| --------------- | ------ | ---- | --- |
switch(config-msdp)#
ConfiguringspecifiedrouterMSDP:
| switch(config-msdp)# |     | router msdp | vrf red |
| -------------------- | --- | ----------- | ------- |
sa-interval
Syntax
| sa-interval | <INTERVAL-VALUE> |     |     |
| ----------- | ---------------- | --- | --- |
no sa-interval
Description
Configuresthesa-intervalforthefrequencyatwhichMSDPsource-activemessagesaresent.
Thenoformofthiscommandsetstheintervaltothedefaultvalueof60seconds.
Commandcontext
config-msdp
Parameters
<INTERVAL-VALUE>
Specifiesthesa-intervalinseconds.Default:60seconds.Range60-65535.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringthesa-interval:
| switch(config)#      | router             | msdp           |          |
| -------------------- | ------------------ | -------------- | -------- |
| switch(config-msdp)# |                    | sa-interval    | 400      |
| switch(config-msdp)# |                    | no sa-interval |          |
| MSDP                 | peer configuration |                | commands |
connection-retry-interval
Syntax
| connection-retry-interval |     | <INTERVAL-VALUE> |     |
| ------------------------- | --- | ---------------- | --- |
no connection-retry-interval
Description
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 254

Configures the connection-retry-interval for which MSDP peers will wait after peering sessions are reset,
before attempting to re-establish the peering sessions.

The no form of this command removes the currently configured value and sets it to the default value of 30
seconds.

Command context

config-msdp-peer

Parameters

<INTERVAL-VALUE>

Specify connection-retry-interval in seconds. Range: 1-65535.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configuring the connection-retry-interval:

switch(config-msdp-peer)# connection-retry-interval 120
switch(config-msdp-peer)# no connection-retry-interval

connect-source

Syntax

connect-source <INTERFACE-NAME>

Description

Configures the connection source interface for the MSDP Peer.

The no form of this command removes the existing connection source interface and resets the peer
connection.

Command context

config-msdp-peer

Parameters

<INTERFACE-NAME>

Specifies the interface to use as a source.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configuring the connection source interface:

switch(config-msdp-peer)# connect-source 1/1/1
switch(config-msdp-peer)# no connect-source 1/1/1

description

Multicast Source Discovery Protocol (MSDP) | 255

Syntax

description <TEXT>
no description

Description

Configures a description for a specified MSDP peer to make it easier to identify in a configuration or show
command output.

The no form of this command removes the peer description.

Command context

config-msdp-peer

Parameters

<TEXT>

Specifies a description for the MSDP Peer.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configuring the MSDP peer description:

switch(config-msdp)# ip msdp peer 10.1.1.1
switch(config-msdp-peer)#
switch(config-msdp-peer)# description Peer_1
switch(config-msdp-peer)# no description

disable

Syntax

disable

Description

Disables MSDP peer on the L3 interface.

Command context

config-msdp-peer

Authority

Administrators or local user group members with execution rights for this command.

Example

Disabling MSDP peering:

switch(config)# router msdp
switch(config-msdp)#
switch(config-msdp)# ip msdp peer 10.1.1.1

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

256

switch(config-msdp-peer)#
switch(config-msdp-peer)# disable

enable

Syntax

enable

Description

Enables MSDP peer on the L3 interface.

Only one MSDP peering session per VRF should be configured between two routers to avoid loops.

Command context

config-msdp-peer

Authority

Administrators or local user group members with execution rights for this command.

Example

Enabling MSDP peering:

switch(config)# router msdp
switch(config-msdp)#
switch(config-msdp)# ip msdp peer 10.1.1.1
switch(config-msdp-peer)#
switch(config-msdp-peer)# enable

ip msdp peer

Syntax

ip msdp peer <IP-ADDR>
no ip msdp peer

Description

Changes the current context to the MSDP peer context.

The no form of this command removes the MSDP peer configuration from the specified context.

Command context

config-msdp

Parameters

<IP-ADDR>

Specifies the IPv4 address of the MSDP peer. Format: A.B.C.D

Authority

Administrators or local user group members with execution rights for this command.

Multicast Source Discovery Protocol (MSDP) | 257

Examples

Enabling the MSDP peer context:

switch(config)# router msdp
switch(config-msdp)#
switch(config-msdp)# ip msdp peer 10.1.1.1
switch(config-msdp-peer)#

keepalive

Syntax

keepalive <KEEPALIVE-INTERVAL> <HOLD-TIME>
no keepalive

Description

Configures the interval at which a MSDP peer will send keepalive messages, and the interval at which the
MSDP peer will wait for keepalive messages from other peers before declaring them down.

The no form of this command removes the currently configured value and sets it to the default value.

Command context

config-msdp-peer

Parameters

<KEEPALIVE-INTERVAL>

Specifies the value for the keepalive interval.

<HOLD-TIME>

Specifies the value for the hold time.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configuring the keepalive interval and the hold time for MSDP peer:

switch(config-msdp-peer)# keepalive 30 45
switch(config-msdp-peer)# no keepalive

mesh-group

Syntax

mesh-group <MESH-NAME>
no mesh-group <MESH-NAME>

Description

Associates the given mesh group with the MSDP peer. This feature is used to reduce the amount of SA
traffic in an intra-domain setting.

The no form of this command removes the peer from the currently configured mesh.

Command context

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

258

config-msdp-peer

Parameters

<MESH-NAME>

Specifies the MSDP mesh group name.

Authority

Administrators or local user group members with execution rights for this command.

Usage

All MSDP peers on the router that participate in the mesh group must be fully meshed with all other peers in
the mesh group. When MSDP mesh groups are used, SA messages are not flooded to other mesh group
peers. It also eliminates RPF checks on arriving SA messages. With MSDP mesh group configured, SA
messages are always accepted from mesh group peers.

Example

Associating a mesh group with an MSDP peer:

switch(config-msdp-peer)# mesh-group test-mesh-group

Removing the MSDP peer from the configured mesh:

switch(config-msdp-peer)# no mesh-group test-mesh-group

password

Syntax

password [{ciphertext | plaintext} <PASSWD>]
no password

Description

Enables MD5 password encryption for a TCP connection between two MSDP peers.

The no form of this command removes MD5 password encryption.

Command context

config-msdp-peer

Parameters

{ciphertext | plaintext}

Selects the password type.

<PASSWD>

Specifies the password.

When the password is not provided on the command line, plaintext password prompting occurs upon pressing

Enter. The entered password characters are masked with asterisks.

Authority

Administrators or local user group members with execution rights for this command.

Multicast Source Discovery Protocol (MSDP) | 259

Examples
ConfiguringMD5passwordencryptionwithaprovidedplaintextpassword:
switch(config)#
|     |     | router |     | msdp |     |     |
| --- | --- | ------ | --- | ---- | --- | --- |
switch(config-msdp)#
| switch(config-msdp)# |     |     | ip  | msdp peer | 10.1.1.1 |     |
| -------------------- | --- | --- | --- | --------- | -------- | --- |
switch(config-msdp-peer)#
| switch(config-msdp-peer)# |     |     |     | password | plaintext | F82#4eva |
| ------------------------- | --- | --- | --- | -------- | --------- | -------- |
ConfiguringMD5passwordencryptionwithapromptedplaintextpassword:
| switch(config)# |     | router |     | msdp |     |     |
| --------------- | --- | ------ | --- | ---- | --- | --- |
switch(config-msdp)#
| switch(config-msdp)# |     |     | ip  | msdp peer | 10.1.1.1 |     |
| -------------------- | --- | --- | --- | --------- | -------- | --- |
switch(config-msdp-peer)#
| switch(config-msdp-peer)# |     |               |     | password |     |     |
| ------------------------- | --- | ------------- | --- | -------- | --- | --- |
| Enter                     | the | MD5 password: |     | ******** |     |     |
| Re-Enter                  | the | MD5 password: |     | ******** |     |     |
RemovingMD5passwordencryption:
| switch(config)# |     | router |     | msdp |     |     |
| --------------- | --- | ------ | --- | ---- | --- | --- |
switch(config-msdp)#
| switch(config-msdp)# |     |     | ip  | msdp peer | 10.1.1.1 |     |
| -------------------- | --- | --- | --- | --------- | -------- | --- |
switch(config-msdp-peer)#
| switch(config-msdp-peer)# |             |     |     | no password |     |     |
| ------------------------- | ----------- | --- | --- | ----------- | --- | --- |
| sa-filter                 | access-list |     |     |             |     |     |
Syntax
| sa-filter    | {in|out} | access-list |             | <ACL-RULE> |            |     |
| ------------ | -------- | ----------- | ----------- | ---------- | ---------- | --- |
| no sa-filter |          | {in|out}    | access-list |            | <ACL-RULE> |     |
Description
AssociatesthegivenACLtofilterMSDPSAmessagesonthepeer.
ThenoformofthiscommandremovesthecurrentlyconfiguredACLentry.
Commandcontext
config-msdp-peer
Parameters
{in|out}
EnablesthefilterforincomingoroutgoingSAmessages.
<ACL-RULE>
SpecifiestheACLrulename.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 260

By default, the MSDP enabled router forwards all the SA messages, and the peer router processes all the
received messages. This command allows the user to configure an ACL on the MSDP peer to filter SA
messages. User can prevent the incoming/outgoing SA messages on MSDP router by creating
incoming/outgoing filter lists using an ACL.

Example

Filtering incoming SA messages on the MSDP peer for the specified ACL:

switch(config-msdp-peer)# sa-filter in access-list msdp_sa_filter1

Filtering outgoing SA messages on the MSDP peer for the specified ACL:

switch(config-msdp-peer)# sa-filter out access-list msdp_sa_filter2

Removing filter on the MSDP peer for the specified ACL:

switch(config-msdp-peer)# no sa-filter in access-list msdp_sa_filter2

MSDP show commands

show ip msdp count

Syntax

show ip msdp count [all-vrfs | vrf <VRF-NAME>]

Description

Shows MSDP Peer (S,G) learnt count for a given VRF. If no options are specified, it shows information for the
default VRF.

Command context

Operator (>) or Manager (#)

Parameters

all-vrfs

Shows MSDP (S,G) entries count for all VRFs. Optional.

vrf <VRF-NAME>

Shows MSDP (S,G) entries count for a particular VRF. If the <VRF-NAME> is not specified, it shows
information for the default VRF. Optional.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing the MSDP learnt count:

Multicast Source Discovery Protocol (MSDP) | 261

| switch#      | show ip  | msdp     | count |     |     |     |     |
| ------------ | -------- | -------- | ----- | --- | --- | --- | --- |
| VRF: default |          |          |       |     |     |     |     |
| SA state     | per Peer | counters |       |     |     |     |     |
| <Peer>:<#SA  | learned> |          |       |     |     |     |     |
| 10.1.1.1:    | 30       |          |       |     |     |     |     |
| 20.1.1.1:    | 100      |          |       |     |     |     |     |
| show ip      | msdp     | peer     |       |     |     |     |     |
Syntax
| show ip msdp | peer | [all-vrfs |     | | vrf | <VRF-NAME> | | <PEER-IP>] |     |
| ------------ | ---- | --------- | --- | ----- | ---------- | ------------ | --- |
Description
ShowsMSDPPeerinformationforthegivenVRF.Optionally,youcanshowspecificinformationbyVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsMSDPpeerinformationforallVRFs.Optional.
vrf <VRF-NAME>
ShowsMSDPpeerinformationforaparticularVRF.Ifthe<VRF-NAME>isnotspecified,itshows
informationforthedefaultVRF.Optional.
<PEER-IP>
ShowsMSDPPeerinformationforspecifiedPeerIP.Format:A.B.C.D.Optional.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShowingMSDPpeerinformationforVRFs:
| switch#           | show ip    | msdp | peer       |     |          |         |     |
| ----------------- | ---------- | ---- | ---------- | --- | -------- | ------- | --- |
| VRF: default      |            |      |            |     |          |         |     |
| MSDP Peer:        | 10.1.1.1   |      |            |     |          |         |     |
| Connection        | status     |      |            |     |          |         |     |
| State:            | up Resets: | 0    | Connection |     | Source:  | 1/1/1   |     |
| Uptime(Downtime): |            | 0m   | 25s        | SA  | Messages | sent: 0 |     |
| SA's learned      | from       | this | peer:      | 0   |          |         |     |
SA Filtering
| Input        | (S,G) filter:   |      | msdp_sa_filter1 |          |     | (S,G) entries | dropped: 0  |
| ------------ | --------------- | ---- | --------------- | -------- | --- | ------------- | ----------- |
| Output       | (S,G) filter:   |      | msdp_sa_filter2 |          |     | (S,G) entries | dropped: 30 |
| Mesh group:  | test-mesh-group |      |                 |          |     |               |             |
| switch#      | show ip         | msdp | peer            | 20.1.1.1 |     |               |             |
| VRF: default |                 |      |                 |          |     |               |             |
| MSDP Peer:   | 20.1.1.1        |      |                 |          |     |               |             |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 262

| Connection        | status       |      |              |             |               |     |
| ----------------- | ------------ | ---- | ------------ | ----------- | ------------- | --- |
| State:            | down Resets: |      | 0 Connection |             | Source: 1/1/2 |     |
| Uptime(Downtime): |              | 1m   | 25s          | SA Messages | sent: 0       |     |
| SA's learned      | from         | this | peer:        | 0           |               |     |
SA Filtering
| Input       | (S,G) filter:   | msdp_sa_filter1 |                 |     | (S,G) entries | dropped: 0  |
| ----------- | --------------- | --------------- | --------------- | --- | ------------- | ----------- |
| Output      | (S,G) filter:   |                 | msdp_sa_filter2 |     | (S,G) entries | dropped: 20 |
| Mesh group: | test-mesh-group |                 |                 |     |               |             |
| show ip     | msdp            | sa-cache        |                 |     |               |             |
Syntax
show ip msdp sa-cache [all-vrfs | vrf <VRF-NAME> | <SRC-OR-GRP-IP>]
Description
ShowsMSDPPeerSA-CacheinformationforthegivenVRF.Optionally,youcanshowspecificinformationby
VRF.TheSA-CacheoutputcanbefilteredbasedonthesourceorgroupIPv4address.
Parameters
all-vrfs
ShowsMSDPSA-CacheinformationforallVRFs.Optional.
vrf <VRF-NAME>
ShowsMSDPSA-CacheinformationforaparticularVRF.Ifthe<VRF-NAME>isnotspecified,itshows
informationforthedefaultVRF.Optional.
<SRC-OR-GRP-IP>
ShowsthefilteredSA-cacheoutputforthespecifiedsourceorgroupIPv4address.Format:A.B.C.D.
Optional.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShowingMSDPSA-CacheinformationforVRFs:
| switch#      | show ip    | msdp    | sa-cache |           |                |     |
| ------------ | ---------- | ------- | -------- | --------- | -------------- | --- |
| VRF: default |            |         |          |           |                |     |
| (30.0.0.1,   | 230.1.1.1) |         | RP:      | 10.1.1.1  | Peer: 10.1.1.2 |     |
| (20.0.0.1,   | 229.1.1.1) |         | RP:      | 10.1.1.1  | Peer: 10.1.1.2 |     |
| (10.0.0.1,   | 229.1.1.1) |         | RP:      | 10.1.1.1  | Peer: 10.1.1.2 |     |
| Total        | entries:   | 3       |          |           |                |     |
| switch#      | show ip    | msdp    | sa-cache | 229.1.1.1 |                |     |
| (20.0.0.1,   | 229.1.1.1) |         | RP:      | 10.1.1.1  | Peer: 10.1.1.2 |     |
| (10.0.0.1,   | 229.1.1.1) |         | RP:      | 10.1.1.1  | Peer: 10.1.1.2 |     |
| Total        | entries:   | 2       |          |           |                |     |
| show ip      | msdp       | summary |          |           |                |     |
Syntax
| show ip msdp | summary | [all-vrfs |     | | vrf | <VRF-NAME>] |     |
| ------------ | ------- | --------- | --- | ----- | ----------- | --- |
MulticastSourceDiscoveryProtocol(MSDP)|263

Description
ShowsMSDPpeersummaryforagivenVRF.Ifnooptionsarespecified,itshowsinformationforthedefault
VRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowstheMSDPpeersummaryforallVRFs.Optional.
vrf <VRF-NAME>
ShowstheMSDPpeersummaryforaparticularVRF.Ifthe<VRF-NAME>isnotspecified,itshows
informationforthedefaultVRF.Optional.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShowingtheMSDPpeersummary:
| switch# show | ip msdp summary |     |     |     |
| ------------ | --------------- | --- | --- | --- |
VRF: default
| MSDP Peer Status | Summary                |     |             |          |
| ---------------- | ---------------------- | --- | ----------- | -------- |
| Peer address     | State Uptime(Downtime) |     | Reset Count | SA Count |
| 10.1.1.1         | down 34m               | 34s | 0           | 0        |
| 20.1.1.1         | up 50m                 | 24s | 0           | 50       |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 264

Chapter 9

mDNS gateway

mDNS gateway

Multicast DNS (mDNS) gateway helps users to discover various servers such as printers and Apple TV, across
VLANs. mDNS gateway uses the reflection mechanism to achieve service discovery across VLANS.

This feature is supported on the 6300 and 6400 Switch Series only.

mDNS gateway overview

Reflection mechanism

With the reflection mechanism, the mDNS packets received in one VLAN are reflected to all the other mDNS
gateway-enabled VLANs based on filters. Only the packets containing the following records are supported
for reflection:

n PTR record—Contains service-name to service-instance-name mapping.

n SRV record—Contains service-instance-name to UDP/TCP port number and hostname mapping.

n TXT record—Contains more information about the service-instance, such as, vendor information.

n A record—Contains hostname to host IP address mapping.

Filters

Filters are used to control the service discovery both within and across VLANs. You can configure filter rules
in the service profiles based on service-name and service-instance-names. If a profile is configure for a VLAN,
then the filter rules in the profile will be used to filter packets transmitted out of the VLAN interface.

Filtering is performed based on parameters extracted from the first record.

Example of mDNS service discovery

The following figure shows an example topology where mDNS gateway is useful. Consider the following:

n Enable mDNS only on Switch 1 in VLAN 1, 2, and 3.

n Create a configuration rule in Switch 1 for VLAN 3—No host in VLAN 3 must discover any external

printers.

When Host 1 in VLAN 3 sends an mDNS query to Switch 1, the query is reflected in VLAN 1 and VLAN 2. The
Wireless Printer 1 in VLAN 1 generates a response that the Switch 1 receives and reflects to VLAN 2 and not
to VLAN 3, because a rule is configured for VLAN 3 to not allow any printer service.

However, Host 1 will still be able to access Wireless Printer 2, because it is present in the same VLAN 3.

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

265

Figure 1 Example of mDNS service discovery

Limitations

Following are a few limitations when configuring mDNS gateway:

n Filtering is performed only based on parameters extracted in the first mDNS record.

n Filtering is applied only on the egress mDNS packets.

n Only IPv4 mDNS packets are supported.

n mDNS gateway is recommended for deployments where mDNS is enabled on lesser VLANs. Because, the
switch allows the mDNS packets to be reflected in only 256 mDNS VLANs, in incremental order of VLAN
IDs, and in the VLAN from where the packet was initiated.

n mDNS packets are rate limited at 150 packets per second.

n When switches are connected directly with each other, you must enable mDNS only on one switch to

prevent a reflection loop.

n You must enable debug logging only for troubleshooting an issue. Enabling debug logging on a high scale

mDNS configuration might lead to high CPU utilization and the system may slow down.

Configuring mDNS gateway
Perform the following steps to configure mDNS gateway:

Procedure

1. Create a service for the mDNS gateway with the mdns-sd service command.

You can group multiple service IDs into a single service.

Add description to the service and create service IDs with the following commands:

mDNS gateway | 266

| a.  | Addadescriptiontotheservicewiththedescriptioncommand. |     |     |
| --- | ----------------------------------------------------- | --- | --- |
| b.  | CreateuniqueserviceIDswiththeidcommand.               |     |     |
2. CreateaprofiletobeappliedonaVLANwiththemdns-sd profilecommand.
Addrulestotheprofilewiththe<sequence-number>command.
3. EnablemDNSgatewayonaVLANwiththemdns-sdcommand.
4. ApplyaprofileontheVLANwiththemdns-sd apply-profile txcommand.
| 5. EnablemDNSgatewaygloballywiththemdns-sd |         |          | enablecommand. |
| ------------------------------------------ | ------- | -------- | -------------- |
| mDNS                                       | gateway | commands |                |
Supportedonthe6300and6400SwitchSeriesonly.
| debug | mdns |     |     |
| ----- | ---- | --- | --- |
Syntax
| debug mdns | {all | config | | init | packet | | timer} |
| ---------- | ------------- | --------------- | -------- |
Description
EnablesmDNSgatewaydebuglogsforallorspecificdebugmodules.
Commandcontext
Manager(#)
Parameters
all
EnablesdebuglogsforallmDNSgatewaymodules.
config
EnablesdebuglogstotracemDNSgatewayconfigurationchanges.
init
EnablesdebuglogstotracemDNSgatewayinitialization.
packet
EnablesdebuglogstotracemDNSgatewaypacketprocessing.
timer
EnablesdebuglogstotracemDNSgatewaytimerevents.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingdebuglogsforallmodules:
| switch# | debug mdns | all |     |
| ------- | ---------- | --- | --- |
Enablingdebuglogsforconfigmodule:
| switch# | debug mdns | config |     |
| ------- | ---------- | ------ | --- |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 267

description

Syntax

description <SERVICE-DESCRIPTION>
no description <SERVICE-DESCRIPTION>

Description

Adds description to a service.

The no form of this command deletes the description of a service.

Command context

config-mdns-sd-service

Parameters

<SERVICE-DESCRIPTION>

Specifies the service description. Maximum 128 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Add a service description:

switch(config-mdns-sd-service)# description students-airplay-service

Remove the service description from a service:

switch(config-mdns-sd-service)# no description students-airplay-service

id

Syntax

id <SERVICE-ID>
no id <SERVICE-ID>

Description

Adds a service identifier to a service. The service ID configured here must be same as the service ID that is
present in the packet.

The no form of this command removes a service ID from the service.

Command context

config-mdns-sd-service

Parameters

<SERVICE-ID>

Specifies the service ID. Maximum 128 characters.

Authority

mDNS gateway | 268

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
AddaserviceID:
| switch(config-mdns-sd-service)# |     |     |     | id _appletv-v2._tcp |
| ------------------------------- | --- | --- | --- | ------------------- |
RemoveaserviceIDfromaservice:
| switch(config-mdns-sd-service)# |     |     |     | no id _appletv-v2._tcp |
| ------------------------------- | --- | --- | --- | ---------------------- |
mdns-sd
Syntax
mdns-sd
no mdns-sd
Description
EnablesmDNSgatewayonaVLANinterface.
ThenoformofthiscommanddisablesmDNSgatewayonaVLANinterface.
ThiscommandisapplicableonlytoVLANinterfaces.
TheswitchwillnotprocessmDNSpacketsuntilthemDNSgatewayisenabledglobally.
Commandcontext
config-if-vlan
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingmDNSgatewayonVLAN10:
| switch(config)#         |     | interface | vlan    | 10  |
| ----------------------- | --- | --------- | ------- | --- |
| switch(config-if-vlan)# |     |           | mdns-sd |     |
DisablingmDNSgatewayonVLAN10:
| switch(config)#         |               | interface | vlan       | 10  |
| ----------------------- | ------------- | --------- | ---------- | --- |
| switch(config-if-vlan)# |               |           | no mdns-sd |     |
| mdns-sd                 | apply-profile |           | tx         |     |
Syntax
| mdns-sd    | apply-profile | <PROFILE-NAME> |     | tx  |
| ---------- | ------------- | -------------- | --- | --- |
| no mdns-sd | apply-profile | <PROFILE-NAME> |     | tx  |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 269

Description

Configures mDNS gateway profile on the VLAN interface. When a profile is applied in the transmit direction,
all the mDNS traffic transmitted on the VLAN interface will be filtered based on the rules specified in the
transmit profile.

The no form of this command deletes the profile configuration from the VLAN interface in the transmit
direction.

This command is applicable only to VLAN interfaces.

When no profile is configured on an interface then the default action is permit.

Command context

config-if-vlan

Parameters

<PROFILE-NAME>

Specifies the profile name. Maximum 32 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring mDNS gateway profile on VLAN 10:

switch(config)# interface vlan 10
switch(config-if-vlan)# mdns-sd
switch(config-if-vlan)# mdns-sd apply-profile student tx

Deleting mDNS gateway profile on VLAN 10:

switch(config)# interface vlan 10
switch(config-if-vlan)# no mdns-sd apply-profile student tx

mdns-sd enable

Syntax

mdns-sd enable
no mdns-sd enable

Description

Enables mDNS gateway.

The no form of this command disables mDNS gateway. Once the no form of this command is executed, all
the SVI VLANs, even though enabled with mDNS gateway, will stop reflecting mDNS packets to the enabled
VLANs.

Command context

config

Authority

mDNS gateway | 270

Administrators or local user group members with execution rights for this command.

Examples

Enable mDNS gateway:

switch(config)# mdns-sd enable

Disable mDNS gateway:

switch(config)# no mdns-sd enable

mdns-sd profile

Syntax

mdns-sd profile <PROFILE-NAME>

Description

Creates a profile that can be applied on one or more L3 VLAN interfaces.

The profile contains a set of rules that define various match parameters such as service-name and service-
instance-name.

Command context

config

Parameters

<PROFILE-NAME>

Specifies the name of the profile. Maximum 32 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating a profile:

switch(config)# mdns-sd profile student

mdns-sd service

Syntax

mdns-sd service <SERVICE-NAME>
no mdns-sd service

Description

Configures a service for mDNS gateway. You can group multiple service IDs into a single user-defined service
name.

The no form of this command deletes a service.

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

271

Aservicecannotbedeletedifitisbeingusedasamatchparameterinafilterruleinanyprofile.
Commandcontext
config
Parameters
<SERVICE-NAME>
Specifiesthenameoftheservice.Maximum32characters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfigureaserviceformDNSgateway:
| switch(config)# | mdns-sd | service | students |
| --------------- | ------- | ------- | -------- |
Deleteaservice:
| switch(config)# | no mdns-sd |     | service students |
| --------------- | ---------- | --- | ---------------- |
| clear mdns-sd   | statistics |     |                  |
Syntax
| clear mdns-sd statistics |     |     |     |
| ------------------------ | --- | --- | --- |
Description
ClearsallmDNSgatewaystatistics.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ClearmDNSgatewaystatistics:
| switch(config)# | clear | mdns-sd | statistics |
| --------------- | ----- | ------- | ---------- |
<sequence-number>
Syntax
| <sequence-number> | {permit | | deny} |     |
| ----------------- | ------- | ------- | --- |
{service-name <SERVICE-NAME> | service-instance-name <SERVICE-INSTANCE-NAME>}
| no <sequence-number> | {permit | |   | deny} |
| -------------------- | ------- | --- | ----- |
{service-name <SERVICE-NAME> | service-instance-name <SERVICE-INSTANCE-NAME>}
mDNSgateway|272

Description

Adds a filter rule to the service profile. The sequence number configured determines the priority with which
the rule is matched. Lower the sequence number, higher is the priority.

Following are the filter match parameters:

n Service-name: mDNS packets are matched against the service IDs configured under the service name.

n Service-instance-name: mDNS packets are matched against the service instance name present in the

mDNS packets.

When no match criteria is specified in the rule, then the rule can be matched against any mDNS packet. Once
the match is found then either the packet can be permitted or denied based on the action specified in the
rule.

The no form of this command deletes the filter configured in the service profile.

When an mDNS packet does not match any of the filters configured in the profile, then the packet is denied.

Command context

config-mdns-sd-profile

Parameters

<SERVICE-NAME>

Specifies the service name. Maximum 128 characters.

<SERVICE-INSTANCE-NAME>

Specifies the service instance name. Maximum 128 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Adding filter rules to a service profile:

switch(config)# mdns-sd profile student
switch(config-mdns-sd-profile)# 10 permit service-name default-appletv
switch(config-mdns-sd-profile)# 20 deny service-name default-appletv service-
instance-name instance-name office._pdl-datastream._tcp.local
switch(config-mdns-sd-profile)# 30 permit service-instance-name instance-name
library._pdl-datastream._tcp.local
switch(config-mdns-sd-profile)# 40 deny

Deleting filter rules to a service profile:

switch(config)# mdns-sd profile student
switch(config-mdns-sd-profile)# 10 permit service-name default-appletv
switch(config-mdns-sd-profile)# 20 deny service-name default-appletv service-
instance-name instance-name office._pdl-datastream._tcp.local
switch(config-mdns-sd-profile)# 30 permit service-instance-name instance-name
library._pdl-datastream._tcp.local
switch(config-mdns-sd-profile)# no 30 permit service-instance-name instance-name
library._pdl-datastream._tcp.local
switch(config-mdns-sd-profile)# 40 deny

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

273

show mdns-sd service-entries

Syntax

show mdns-sd service-entries {service-id <SERVICE-ID> | record-type <RECORD-TYPE>}

Description

Shows all the services exchanged in the mDNS gateway enabled VLANs.

Command context

Operator (>) or Manager (#)

Parameters

<SERVICE-ID>

Specifies the service ID. Maximum 128 characters.

<RECORD-TYPE>

Specifies the type of record. Record can be one of the following values:

n PTR

n SRV

n TXT

n A

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Displaying service entries learnt from mDNS gateway enabled VLANS:

switch# show mdns-sd service-entries
MAC-Address : 01:00:00:0e:21:23
VLAN Id
Record Name : _touch-able._tcp.local
Record Type : PTR
TTL

: 4500

: 10

MAC-Address : 01:00:00:0e:21:23
VLAN Id
Record Name : 523899E219D4C562._touch-able._tcp.local
Record Type : SRV
TTL

: 4500

: 10

MAC-Address : 01:00:00:0e:21:23
VLAN Id
Record Name : 523899E219D4C562._touch-able._tcp.local
Record Type : TXT
TTL

: 4500

: 10

Displaying service entries for a service and record type:

switch# show mdns-sd service-entries service-id _touch-able._tcp record-type ptr
MAC-Address : 01:00:00:0e:21:23

mDNS gateway | 274

| VLAN Id      | : 10                          |     |
| ------------ | ----------------------------- | --- |
| Record       | Name : _touch-able._tcp.local |     |
| Record       | Type : PTR                    |     |
| TTL          | : 4500                        |     |
| show mdns-sd | statistics                    |     |
Syntax
| show mdns-sd | statistics | [vlan [<VLAN-ID>]] |
| ------------ | ---------- | ------------------ |
Description
ShowsthemDNSpacketsreceivedandsentglobally,andperVLAN.
Commandcontext
Operator(>)orManager(#)
Parameters
<VLAN-ID>
SpecifiestheVLANID.Required.Range1to4094.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Displaystotalpackets:
| switch# | show mdns-sd | statistics |
| ------- | ------------ | ---------- |
| Packets | Recieved     | : 100      |
| Packets | Sent         | : 150      |
| Packets | Dropped      | : 50       |
DisplaystotalpacketsforallVLANs:
| switch#      | show mdns-sd | statistics |
| ------------ | ------------ | ---------- |
| VLAN 10      |              |            |
| Packets      | Recieved     | : 100      |
| Packets      | Sent         | : 100      |
| Packets      | Dropped      | : 0        |
| VLAN 20      |              |            |
| Packets      | Recieved     | : 0        |
| Packets      | Sent         | : 50       |
| Packets      | Dropped      | : 50       |
| show mdns-sd | statistics   | profile    |
Syntax
| show mdns-sd | statistics | profile <PROFILE-NAME> |
| ------------ | ---------- | ---------------------- |
Description
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 275

Displaysthenumberofpacketspermittedordeniedbyvariousfilterrulesinaprofile.
Commandcontext
Operator(>)orManager(#)
Parameters
<PROFILE-NAME>
Specifiestheprofilename.Maximum32characters.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Displayingstatisticsforaprofile:
| switch# show | mdns-sd | statistics | profile student |     |
| ------------ | ------- | ---------- | --------------- | --- |
--------------------------
| Sequence-Number | Hit-Count |     |     |     |
| --------------- | --------- | --- | --- | --- |
--------------------------
| 10           | 100        |           |                |       |
| ------------ | ---------- | --------- | -------------- | ----- |
| 20           | 25         |           |                |       |
| 30           | 150        |           |                |       |
| Total number | of packets | permitted | by the profile | : 250 |
| Total number | of packets | denied    | by the profile | : 50  |
| show mdns-sd | summary    |           |                |       |
Syntax
| show mdns-sd | summary |     |     |     |
| ------------ | ------- | --- | --- | --- |
Description
ShowswhethermDNSgatewayisenabledgloballyandattheVLANinterfacelevel.Italsoshowstheprofile
appliedonvariousVLANinterfaces.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
DisplayingmDNSgatewaysummary:
| switch# show   | mdns-sd | summary |     |     |
| -------------- | ------- | ------- | --- | --- |
| global mdns-sd | status: | enabled |     |     |
----------------------------
| VLAN-Id Status | Tx-Profile |     |     |     |
| -------------- | ---------- | --- | --- | --- |
mDNSgateway|276

----------------------------
| 1 enabled           | student  |           |     |     |
| ------------------- | -------- | --------- | --- | --- |
| 2 enabled           | employee |           |     |     |
| 3 disabled          | teacher  |           |     |     |
| show running-config |          | interface |     |     |
Syntax
| show running-config | interface | <INTERFACE-NAME> |     |     |
| ------------------- | --------- | ---------------- | --- | --- |
Description
Showstheconfigurationofprofilesforaninterface.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-NAME>
Specifiestheinterfacename.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
DisplayingconfigurationofprofileatVLAN10:
| switch# show | running-config | interface |     | vlan10 |
| ------------ | -------------- | --------- | --- | ------ |
| interface    | vlan10         |           |     |        |
mdns-sd
| mdns-sd | apply-profile | teacher | tx  |     |
| ------- | ------------- | ------- | --- | --- |
ip address 10.1.1.1/24
| show running-config |     | mdns-sd |     | profile |
| ------------------- | --- | ------- | --- | ------- |
Syntax
| show running-config | mdns-sd | profile | <PROFILE-NAME> |     |
| ------------------- | ------- | ------- | -------------- | --- |
Description
Showstheconfigurationofalloraspecificprofile.
Commandcontext
Operator(>)orManager(#)
Parameters
<PROFILE-NAME>
Specifiestheprofilename.Maximum32characters.
Authority
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 277

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Displayingconfigurationofallprofiles:
|     | switch# show    | running-config | mdns-sd | profile |
| --- | --------------- | -------------- | ------- | ------- |
|     | mdns-sd profile | student        |         |         |
10 deny service-type default-print service-instance-name office._pdl-datastream._
tcp.local
|     | 50 permit       | service-type | default-airplay |     |
| --- | --------------- | ------------ | --------------- | --- |
|     | 51 permit       | service-type | default-print   |     |
|     | mdns-sd profile | teacher      |                 |     |
10 deny service-type default-print service-instance-name office._pdl-datastream._
tcp.local
|      | 50 permit      | service-type | default-airplay |         |
| ---- | -------------- | ------------ | --------------- | ------- |
|      | 51 permit      | service-type | default-print   |         |
| show | running-config |              | mdns-sd         | service |
Syntax
| show | running-config | mdns-sd | service | <SERVICE-NAME> |
| ---- | -------------- | ------- | ------- | -------------- |
Description
ShowstherunningconfigurationofalloraspecificmDNSservice.
Commandcontext
Operator(>)orManager(#)
Parameters
<SERVICE-NAME>
Specifiestheservicename.Maximum32characters.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
DisplayingrunningconfigurationofallmDNSservices:
|     | switch# show          | running-config  | mdns-sd | service |
| --- | --------------------- | --------------- | ------- | ------- |
|     | mdns-sd service       | default-airplay |         |         |
|     | id _airplay._tcp      |                 |         |         |
|     | id _appletv-v2._tcp   |                 |         |         |
|     | id _roap._tcp         |                 |         |         |
|     | mdns-sd service       | itunes          |         |         |
|     | id _home-sharing._tcp |                 |         |         |
|     | id _apple-mobdev._dev |                 |         |         |
mDNSgateway|278

Chapter 10

Multicast VXLAN

Multicast VXLAN

The Aruba 8320 Switch Series does not support VXLAN.

IPv4 multicast forwarding for both L2 and L3 are supported with AOS-CX VXLAN/EVPN deployments. Refer
to the VXLAN Guide for more info on VXLAN/EVPN and overlays/underlays.

L2 multicast over VXLAN refers to deployments where the multicast sources/receivers are on the same L2
subnet/VLAN and bridging is required between switches that function as VXLAN Tunnel End Points (VTEPs),
as seen here:

L3 multicast over VXLAN refers to deployments where the multicast sources/receivers are on different
subnets/VLANs and routing is required between VTEPs as seen here:

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

279

IGMP
In a VXLAN deployment, enabling igmp snooping prevents flooding of unknown multicast packets to all the
VTEPs in the L2VNI. AHQ from the querier is sent to all the VTEPs in the L2VNI along with the regular ports in
the associated VLAN. Additionally, IGMP Membership Reports from local hosts are forwarded to all the
VTEPs in the L2VNI.

In a situation where a VSX pair is acting like a VTEP, IGMP Membership Reports from remote VTEPS are
synchronized among the VSX peers. Both the VSX peers will learn the join on the same VTEP. In order to
achieve this, redistribute local-svi or redistribute local-mac commands must be enabled under the
EVPN context. When running VSX on a pair of switches, only one device will get the packet on the VTEP.
IGMP snooping should be enabled on all devices in the fabric, otherwise all multicast traffic is flooded.

If the VTEP does not have any IGMP configurations, VXLAN encapsulated packets are copied to the CPU even

though there is no IGMP configuration; the packets are forwarded by the software to the other ports.

In a VXLAN-enabled topology where there are tunnel endpoints configured on different platforms, the scale

supported will be the lowest value among the different platforms. This is because the joins are synced across the

Tunnel Endpoints.

PIM-SM
In a VXLAN deployment, when PIM is configured on the tenant VRF, PIM is automatically enabled on the
L3VNI interface on that VRF. This interface is used to route multicast traffic across tunnels in a symmetric
IRB network. PIM neighbors will be learned on this interface and the remote VTEP neighbors will be listed
under this interface. Multicast traffic is forwarded through the same L3VNI interface to reach other VTEP
clients.

PIM uses the VXLAN source IP as the DR priority and it overrides the default DR priority. It is recommended
not to configure DR priorities. However, if you must configure the priority, the DR priority should be unique
in each of the leaf nodes. For a VSX VTEP, the VSX peers should have the same DR priority.

Multicast VXLAN | 280

PIM-DMwithVXLANisnotcurrentlysupported.
n
n MulticastoverstaticVXLANtunnelsiscurrentlynotsupported.
n PIMactive-activeisnotapplicableforMulticastoverVXLAN.
| Sample    | Multicast |              | over VXLAN |     | Config | of a VSX | Leaf in |
| --------- | --------- | ------------ | ---------- | --- | ------ | -------- | ------- |
| Symmetric |           | IRB topology |            |     |        |          |         |
Leaf-1AConfig:
| hostname | Leaf-1A |     |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- | --- |
| vrf      | Test1   |     |     |     |     |     |     |
rd 100.0.0.1:15000
|             | route-target      | export | 1234567:15000 | evpn |     |     |     |
| ----------- | ----------------- | ------ | ------------- | ---- | --- | --- | --- |
|             | route-target      | import | 1234567:15000 | evpn |     |     |     |
| vlan        | 1                 |        |               |      |     |     |     |
| vlan        | 101               |        |               |      |     |     |     |
| #Enable     | IGMP snooping     |        |               |      |     |     |     |
|             | ip igmp snooping  | enable |               |      |     |     |     |
| vlan        | 200               |        |               |      |     |     |     |
| virtual-mac | 00:00:00:0a:0a:0a |        |               |      |     |     |     |
| #evpn       | configuration     |        |               |      |     |     |     |
evpn
|     | redistribute | local-svi |     |     |     |     |     |
| --- | ------------ | --------- | --- | --- | --- | --- | --- |
vlan 101
rd 100.0.0.1:101
|     | route-target | export | 101:101 |     |     |     |     |
| --- | ------------ | ------ | ------- | --- | --- | --- | --- |
|     | route-target | import | 101:101 |     |     |     |     |
#L2vni svi configuration Enable IGMP and PIM on the L2 VNI mapped SVI
| interface  | vlan           | 101                  |                   |         |        |     |     |
| ---------- | -------------- | -------------------- | ----------------- | ------- | ------ | --- | --- |
|            | vrf attach     | Test1                |                   |         |        |     |     |
|            | ip address     | 101.1.1.2/24         |                   |         |        |     |     |
|            | active-gateway | ip mac               | 00:00:20:00:10:01 |         |        |     |     |
|            | active-gateway | ip 101.1.1.1         |                   |         |        |     |     |
|            | ip igmp enable |                      |                   |         |        |     |     |
|            | ip pim-sparse  | enable               |                   |         |        |     |     |
|            | ip pim-sparse  | vsx-virtual-neighbor |                   |         |        |     |     |
| #MC-LAG-AF | SVI            | Connection           | to device         | Outside | Fabric |     |     |
| interface  | vlan           | 200                  |                   |         |        |     |     |
|            | vrf attach     | Test1                |                   |         |        |     |     |
vsx active-forwarding
|           | ip address     | 101.2.1.2/24         |     |     |     |     |     |
| --------- | -------------- | -------------------- | --- | --- | --- | --- | --- |
|           | ip ospf 1      | area 0.0.0.0         |     |     |     |     |     |
|           | ip pim-sparse  | enable               |     |     |     |     |     |
|           | ip pim-sparse  | vsx-virtual-neighbor |     |     |     |     |     |
| #vxlan    | configuration  |                      |     |     |     |     |     |
| interface | vxlan          | 1                    |     |     |     |     |     |
|           | source ip      | 100.0.0.1            |     |     |     |     |     |
|           | vxlan-counters | aggregate            |     |     |     |     |     |
no shutdown
vni 101
|     | vlan 101 |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 281

vni 15001
| vrf | Test1 |     |     |     |
| --- | ----- | --- | --- | --- |
routing
vsx
| inter-switch-link |     | lag 1 |     |     |
| ----------------- | --- | ----- | --- | --- |
role primary
| keepalive   | peer        | 192.168.1.2 | source | 192.168.1.1 |
| ----------- | ----------- | ----------- | ------ | ----------- |
| router ospf | 1           |             |        |             |
| router-id   | 11.11.11.11 |             |        |             |
area 0.0.0.0
router bgp 1
| bgp router-id  |         | 1.1.1.1       |     |            |
| -------------- | ------- | ------------- | --- | ---------- |
| neighbor       | 3.3.3.3 | remote-as     | 1   |            |
| neighbor       | 3.3.3.3 | update-source |     | loopback 0 |
| neighbor       | 4.4.4.4 | remote-as     | 1   |            |
| neighbor       | 4.4.4.4 | update-source |     | loopback 0 |
| neighbor       | 5.5.5.5 | remote-as     | 1   |            |
| neighbor       | 5.5.5.5 | update-source |     | loopback 0 |
| address-family |         | ipv4 unicast  |     |            |
| redistribute   |         | connected     |     |            |
exit-address-family
| address-family |         | l2vpn evpn     |     |          |
| -------------- | ------- | -------------- | --- | -------- |
| neighbor       | 3.3.3.3 | activate       |     |          |
| neighbor       | 3.3.3.3 | send-community |     | extended |
| neighbor       | 4.4.4.4 | activate       |     |          |
| neighbor       | 4.4.4.4 | send-community |     | extended |
| neighbor       | 5.5.5.5 | activate       |     |          |
| neighbor       | 5.5.5.5 | send-community |     | extended |
exit-address-family
!
vrf Test1
| address-family |              | ipv4      | unicast |     |
| -------------- | ------------ | --------- | ------- | --- |
|                | redistribute | connected |         |     |
exit-address-family
!
#Enable PIM
| router pim | vrf Test1 |     |     |     |
| ---------- | --------- | --- | --- | --- |
enable
Leaf-1B Config:
hostname Leaf-1B
vrf Test1
rd 100.0.0.1:15000
| route-target | export | 1234567:15000 |     | evp  |
| ------------ | ------ | ------------- | --- | ---- |
| route-target | import | 1234567:15000 |     | evpn |
vlan 1
vlan 101
| #Enable | IGMP snooping |        |     |     |
| ------- | ------------- | ------ | --- | --- |
| ip igmp | snooping      | enable |     |     |
vlan 200
| virtual-mac | 00:00:00:0a:0a:0a |     |     |     |
| ----------- | ----------------- | --- | --- | --- |
#evpn configuration
evpn
| redistribute | local-svi |     |     |     |
| ------------ | --------- | --- | --- | --- |
vlan 101
rd 100.0.0.1:101
| route-target |     | export | 101:101 |     |
| ------------ | --- | ------ | ------- | --- |
| route-target |     | import | 101:101 |     |
MulticastVXLAN|282

#L2vni svi configuration. Configure IGMP and PIM on the L2 VNI mapped SVI
interface vlan 101

vrf attach Test1
ip address 101.1.1.3/24
active-gateway ip mac 00:00:20:00:10:01
active-gateway ip 101.1.1.1
ip igmp enable
ip pim-sparse enable
ip pim-sparse vsx-virtual-neighbor

#MC-LAG-AF SVI Connection to device Outside Fabric
interface vlan 200

vrf attach Test1
vsx active-forwarding
ip address 101.2.1.1/24
ip ospf 1 area 0.0.0.0
ip pim-sparse enable
ip pim-sparse vsx-virtual-neighbor

#vxlan configuration
interface vxlan 1

source ip 100.0.0.1
vxlan-counters aggregate
no shutdown
vni 101

vlan 101

vni 15001

vrf Test1
routing

vsx

inter-switch-link lag 1
role secondary
keepalive peer 192.168.1.1 source 192.168.1.2

router ospf 1

router-id 1.1.2.1
area 0.0.0.0

router bgp 1

bgp router-id 1.1.2.1
neighbor 3.3.3.3 remote-as 1
neighbor 3.3.3.3 update-source loopback 0
neighbor 4.4.4.4 remote-as 1
neighbor 4.4.4.4 update-source loopback 0
neighbor 5.5.5.5 remote-as 1
neighbor 5.5.5.5 update-source loopback 0
address-family ipv4 unicast

redistribute connected

exit-address-family
address-family l2vpn evpn

neighbor 3.3.3.3 activate
neighbor 3.3.3.3 send-community extended
neighbor 4.4.4.4 activate
neighbor 4.4.4.4 send-community extended
neighbor 5.5.5.5 activate
neighbor 5.5.5.5 send-community extended

exit-address-family

!

vrf Test1

address-family ipv4 unicast

redistribute connected

exit-address-family

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

283

!
#Enable PIM
router pim vrf Test1

enable

RP config on PIM router outside Fabric:

# SVI Connection to VxLAN VSX Leaf-1
interface vlan 200

ip address 101.2.1.3/24
ip ospf 1 area 0.0.0.0
ip pim-sparse enable

router ospf 1

router-id 7.7.7.7
area 0.0.0.0

router pim
enable
rp-candidate source-ip-interface loopback0
rp-candidate group-prefix 224.0.0.0/4
bsr-candidate source-ip-interface loopback0

Multicast VXLAN commands

ip pim-sparse vsx-virtual-neighbor
ip pim-sparse vsx-virtual-neighbor
no ip pim-sparse vsx-virtual-neighbor

Description

Once configured, the router processes IGMP/MLD and PIM joins received on this interface regardless of its
DR or Prime Neighbor role. The command must be enabled for VSX VXLAN leaf switches for both L2 and L3
extensions. This allows for the interface to be in the same multicast data path state on both the VSX peers.

The no form of the command disables the vsx-virtual-neighbor on the interface.

This command is applicable for normal SVI interfaces and L2 VNI mapped SVI interfaces. It is valid for VXLAN-

enabled VLANs only and has no effect on non-VXLAN-enabled VLANs.

Examples

switch(config)# interface vlan40
switch(config-if-vlan)# ip address 40.0.0.4/24
switch(config-if-vlan)# ip pim-sparse enable
switch(config-if-vlan)# ip pim-sparse vsx-virtual-neighbor

Command History

Release
10.07 or earlier

Command Information

Modification
--

Multicast VXLAN | 284

| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Administratorsorlocalusergroupmemberswithexecution
| Allplatforms | config-if-vlan |     |     |     |
| ------------ | -------------- | --- | --- | --- |
rightsforthiscommand.
| redistribute    | local-mac |     |     |     |
| --------------- | --------- | --- | --- | --- |
| redistribute    | local-mac |     |     |     |
| no redistribute | local-mac |     |     |     |
Description
EnablesType-2routeadvertisementforlocalMACaddressoftheSVIinterfacescorrespondingtotheEVPN-
enabledVLANs.
ThenoformofthiscommanddisablestheType-2routeadvertisement.
Examples
| switch(config)# | evpn         |     |           |     |
| --------------- | ------------ | --- | --------- | --- |
| switch(config)# | redistribute |     | local-mac |     |
| switch(config)# | vlan         | 20  |           |     |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Administratorsorlocalusergroupmemberswithexecution
| Allplatforms | config-evpn |     |     |     |
| ------------ | ----------- | --- | --- | --- |
rightsforthiscommand.
| show ip        | mroute    |       |             |            |
| -------------- | --------- | ----- | ----------- | ---------- |
| show ip mroute | [all-vrfs | | vrf | <VRF-NAME>] | [vsx-peer] |
Description
Showsmulticastroutinginformation.Optionally,youcanshowspecificinformationbyVRF.Ifnooptions
arespecified,itshowsinformationforthedefaultVRF.
Parameters
all-vrfs
ShowsallPIM neighborsinformation.
vrf <VRF-NAME>
ShowsPIM neighborinformationforaspecificVRF.
vsx-peer
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Examples
MulticastroutewithL3VNIinIncomingInterfaceList:
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 285

| switch#      | show | ip mroute     | all-vrfs |     |     |
| ------------ | ---- | ------------- | -------- | --- | --- |
| IP Multicast |      | Route Entries |          |     |     |
VRF : red
| Total        | number    | of entries    | : 1         |           |          |
| ------------ | --------- | ------------- | ----------- | --------- | -------- |
| Group        | Address   |               | : 225.1.1.1 |           |          |
| Source       | Address   |               | : 80.1.1.11 |           |          |
| Neighbor     |           |               | : 1.1.1.1   |           |          |
| Incoming     | interface |               | : vni2      |           |          |
| Outgoing     | Interface | List          | :           |           |          |
| Interface    |           | State         |             |           |          |
| -----------  |           | ----------    |             |           |          |
| vlan10       |           | forwarding    |             |           |          |
| switch#      | show      | ip mroute     | 225.1.1.1   | 80.1.1.11 | all-vrfs |
| IP Multicast |           | Route Entries |             |           |          |
VRF : red
| Group       | Address    |            |     | : 225.1.1.1 |     |
| ----------- | ---------- | ---------- | --- | ----------- | --- |
| Source      | Address    |            |     | : 80.1.1.11 |     |
| Neighbor    |            |            |     | : 1.1.1.1   |     |
| Incoming    | interface  |            |     | : vni2      |     |
| Multicast   | Routing    | Protocol   |     | : PIM-SM    |     |
| Unicast     | Routing    | Protocol   |     | : BGP       |     |
| Metric      |            |            |     | : 0         |     |
| Metric      | Pref       |            |     | : 200       |     |
| Uptime      | (HH:MM:SS) |            |     | : 00:07:23  |     |
| Downstream  | Interface  |            |     |             |     |
| Interface   |            | State      |     |             |     |
| ----------- |            | ---------- |     |             |     |
| vlan10      |            | forwarding |     |             |     |
MulticastroutewithL3VNIinOutgoingInterfaceList:
| switch#      | show | ip mroute     | all-vrfs |     |     |
| ------------ | ---- | ------------- | -------- | --- | --- |
| IP Multicast |      | Route Entries |          |     |     |
VRF : red
| Total       | number    | of entries | : 1         |     |     |
| ----------- | --------- | ---------- | ----------- | --- | --- |
| Group       | Address   |            | : 225.1.1.1 |     |     |
| Source      | Address   |            | : 80.1.1.11 |     |     |
| Neighbor    |           |            | :           |     |     |
| Incoming    | interface |            | : vlan20    |     |     |
| Outgoing    | Interface | List       | :           |     |     |
| Interface   |           | State      |             |     |     |
| ----------- |           | ---------- |             |     |     |
| vni2        |           | forwarding |             |     |     |
switch#
|              | show | ip mroute     | 225.1.1.1 | 80.1.1.11 | vrf red |
| ------------ | ---- | ------------- | --------- | --------- | ------- |
| IP Multicast |      | Route Entries |           |           |         |
VRF : red
| Total  | number  | of entries | : 1 |             |     |
| ------ | ------- | ---------- | --- | ----------- | --- |
| Group  | Address |            |     | : 225.1.1.1 |     |
| Source | Address |            |     | : 80.1.1.11 |     |
MulticastVXLAN|286

| Neighbor    |            |            |     | :           |
| ----------- | ---------- | ---------- | --- | ----------- |
| Incoming    | interface  |            |     | : vlan20    |
| Multicast   | Routing    | Protocol   |     | : PIM-SM    |
| Unicast     | Routing    | Protocol   |     | : connected |
| Metric      |            |            |     | : 0         |
| Metric      | Pref       |            |     | : 0         |
| Uptime      | (HH:MM:SS) |            |     | : 00:06:32  |
| Downstream  | Interface  |            |     |             |
| Interface   |            | State      |     |             |
| ----------- |            | ---------- |     |             |
| vni2        |            | forwarding |     |             |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
Allplatforms executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show ip     | pim      | neighbor    |           |                   |
| ----------- | -------- | ----------- | --------- | ----------------- |
| show ip pim | neighbor | [<IP-ADDR>] | [all-vrfs | | vrf <VRF-NAME>] |
Description
DisplaystheinformationaboutPIMinterfacescurrentlyconfiguredintherouterforthegivenVRF.IfVRFis
notgiven,itdisplaysfordefaultVRF.
Parameters
<IP-ADDR>
ShowsPIM neighborinformation.
all-vrfs
ShowsallPIM neighborsinformation.
vrf <VRF-NAME>
ShowsPIM neighborinformationforaspecificVRF.
Examples
ShowinformationforallVRFs:
| switch#      | show            | ip pim neighbor | all-vrfs      |     |
| ------------ | --------------- | --------------- | ------------- | --- |
| PIM Neighbor |                 |                 |               |     |
| VRF          |                 |                 | : Test_1      |     |
| Total        | number          | of neighbors    | : 2           |     |
| IP Address   |                 |                 | : 100.1.1.252 |     |
| Interface    |                 |                 | : vlan100     |     |
| Up Time      | (HH:MM:SS)      |                 | : 00:44:38    |     |
| Expire       | Time (HH:MM:SS) |                 | : 00:01:32    |     |
| DR Priority  |                 |                 | : 1           |     |
AOS-CX10.07MulticastGuide|(6300,6400,8xxxSwitchSeries) 287

| Hold Time   | (HH:MM:SS)      | : 00:01:45  |
| ----------- | --------------- | ----------- |
| IP Address  |                 | : 172.1.1.1 |
| Interface   |                 | : vni1000   |
| Up Time     | (HH:MM:SS)      | : 00:44:35  |
| Expire      | Time (HH:MM:SS) | : 00:03:25  |
| DR Priority |                 | : 1         |
| Hold Time   | (HH:MM:SS)      | : 00:03:30  |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
Allplatforms executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
MulticastVXLAN|288

Chapter 11

Support and other resources

Support and other resources

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

Accessing updates
You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

AOS-CX 10.07 Multicast Guide | (6300, 6400, 8xxx Switch Series)

289

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

Warranty information
To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Regulatory information
To view the regulatory information for your product, view the Safety and Compliance Information for Server,
Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs, product
recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For more
information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation feedback
Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

Support and other resources | 290