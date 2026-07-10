AOS-CX 10.18.xxxx Maintenance mode Guide

Part Number:
Published: May 2026
Edition:

AOS-CX 10.18.xxxx Maintenance mode Guide (Internal use only)

Part Number:
Published: May 2026
Edition:

© Copyright 2026– Hewlett Packard Enterprise Development LP

Public

AOS-CX 10.18.xxxx Maintenance mode Guide (Internal...

A
O
S
-
C
X

1
0
.
1
8
.
x
x
x
x

M
a
i
n
t
e
n
a
n
c
e

m
o
d
e

G
u
i
d
e

(
I
n
t
e
r
n
a
l
.
.
.

Table of contents

Maintenance Mode

Aruba Maintenance Mode...........................................................................................................................................................5

Design Principles and Traffic Impact....................................................................................................................................5

Critical Network Topology Requirements..........................................................................................................................6

Traffic Impact Expectations....................................................................................................................................................... 7

Configuration Examples...............................................................................................................................................................9

Alternative Profile Configurations..........................................................................................................................10

Example 1: Complete Maintenance Configuration....................................................................................... 10

Example 2: Layer-Separated Feature-Sets Configuration....................................................................... 14

Operational Behavior and Recommendations............................................................................................................. 18

Configuration Change Guidelines........................................................................................................................................20

VSX/MCLAG-Specific Behavior and Scope....................................................................................................................21

High Availability (HA) Behavior...........................................................................................................................................22

Known Issues and Limitations...............................................................................................................................................24

Maintenance Mode Scope and Traffic Impact Analysis..........................................................................................26

Show Events.....................................................................................................................................................................................28

REST API Terminology and Data Model Reference..................................................................................................29

Key REST API Concepts...............................................................................................................................................31

REST API Base Paths.....................................................................................................................................................32

Maintenance mode commands.............................................................................................................................................34

maintenance-mode activate [profile <PROFILE_NAME>] ......................................................................35

maintenance-mode profile <PROFILE_NAME>..............................................................................................38

maintenance-unit apply <FEATURE_SET_NAME>......................................................................................41

maintenance-unit bgp <FEATURE_SET_NAME>..........................................................................................43

maintenance-unit ospfv2 <FEATURE_SET_NAME>...................................................................................46

maintenance-unit ospfv3 <FEATURE_SET_NAME>...................................................................................48

maintenance-unit ospfv3-af-ipv4 <FEATURE_SET_NAME>.................................................................50

maintenance-unit ospfv3-af-ipv6 <FEATURE_SET_NAME>.................................................................51

neighbor <IP_ADDRESS> vrf <VRF_NAME>...................................................................................................53

process <PROCESS_ID>...............................................................................................................................................56

show events -d gshut-daemon................................................................................................................................ 62

show maintenance-mode profile.............................................................................................................................63

show maintenance-mode............................................................................................................................................ 68

show maintenance-unit................................................................................................................................................71

Public

Table of contents 3

shutdown-delay-timer <SECONDS>.....................................................................................................................75

Support and other resources.............................................................................................................................................................. 78

Accessing Hewlett Packard Enterprise Support.........................................................................................................78

HPE product registration......................................................................................................................................................... 79

Accessing updates....................................................................................................................................................................... 79

Remote support............................................................................................................................................................................. 80

Warranty information................................................................................................................................................................. 80

Regulatory information............................................................................................................................................................. 80

Documentation feedback......................................................................................................................................................... 81

Public

Table of contents 4

Aruba Maintenance Mode

This section provides comprehensive documentation for the Aruba Maintenance Mode feature CLI
commands and REST API. Aruba Maintenance Mode is a feature designed to enable network operators
to perform maintenance tasks, such as hardware replacements, EOS upgrades, re-cabling, or configuration
changes, while minimizing disruption to live network traffic. When activated, maintenance mode uses
protocols like OSPF and BGP to gracefully reroute traffic away from the switch or its components, ensuring
minimal traffic impact and service continuity.

We will focus on CLI commands and operations, however, commands include corresponding REST API
examples. For REST API developers, a comprehensive REST API terminology mapping and data model
reference section is available in the NAME OF SECTION.

Design Principles and Traffic Impact

This section describes the underlying mechanisms, network requirements, and expected traffic behavior
during maintenance mode operations. Understanding these principles is essential for proper deployment
planning and setting appropriate expectations for traffic impact.

Underlying Protocol Mechanisms

Maintenance mode leverages standard protocol mechanisms to signal maintenance state to the network and
gracefully redirect traffic away from the switch:

OSPF Max-Metric

BGP Graceful Shutdown (GSHUT)

Mechanism

Maximum metric values (0xFFFF) are app
lied to OSPF interface costs in Link State
Advertisements (LSAs).

BGP Graceful Shutdown (GSHUT) communi
ty (GRACEFUL_SHUTDOWN 65535:0) is ad
vertised with BGP routes, followed by BGP n
eighbor session shutdown after a configurab
le shutdown-delay-timer.

Behavior

•  OSPF neighbors receive LSAs adverti
sing maximum metric paths through t
he switch

•  Neighboring routers recalculate SPF (
Shortest Path First) with the new met
ric values

•  Traffic is redirected through alternate

lower-cost paths if available

•  GSHUT community (65535:0) is added

to all advertised BGP routes

•

•

IBGP peers receive routes with GSHUT c
ommunity and lower route preference
IBGP Peers select alternate paths if avail
able, avoiding routes through the mainte
nance switch

•  EBGP peer receive routes with only GSH

UT community

Public

Aruba Maintenance Mode 5

OSPF Max-Metric

BGP Graceful Shutdown (GSHUT)

•  OSPF neighbor relationships remain a

•  EBGP peers should be configured with

ctive; only metric values change

Timing

OSPF reconvergence depends on LSA fl
ooding, SPF calculation, and RIB/FIB upd
ates across the network.

route-map actions as, when GSHUT com
munity is received route preference need
to be altered

•  After GSHUT community advertisemen
t, the configurable shutdown-delay-time
r (default 120 seconds) begins

•  BGP neighbor sessions are brought dow
n gracefully after the shutdown-delay-ti
mer expires

•  Session teardown allows peers to immed
iately remove routes and complete reco
nvergence

Two-phase process:

1.  GSHUT community advertisement trigg
ers peer-side route preference changes
2.  Shutdown-delay-timer expiration (confi
gurable, default 120 seconds) triggers s
ession teardown and final route removal

Critical Network Topology Requirements

Redundant Path Requirement

Maintenance mode requires redundant network paths for traffic redirection. The network topology must
provide alternate paths for traffic to avoid the maintenance switch.

NOTE
Why redundancy is essential?

•  Maintenance mode signals protocols to deprioritize paths through the switch

•  Without alternate paths, traffic has nowhere to redirect

•  Protocol mechanisms (max-metric, GSHUT) make the switch less preferred,

not unreachable

Public

Critical Network Topology Requirements 6

Topology Planning:

1.  OSPF Networks: Ensure mesh or redundant ring topologies with multiple paths between endpoints

2.  BGP Networks: Verify multiple BGP paths exist for critical prefixes before maintenance

3.  Validation: Use network simulation or pre-maintenance path analysis to confirm redundancy

Single Point of Failure Warning: If the maintenance switch is a single point of failure (no alternate path),
maintenance mode cannot prevent traffic disruption. Traffic loss will occur regardless of protocol signaling.
While OSPF routes will advertise max-metric and BGP neighbor sessions will be shut down, the switch itself
remains reachable for management and control plane operations. Maintenance mode affects only the routing
protocols, not the underlying switch management accessibility.

Traffic Impact Expectations

Activation impact on traffic

When maintenance mode is activated, the switch signals protocols to redirect traffic. Traffic loss is minimized
but not eliminated.

Traffic loss considerations:

•  Not Guaranteed Zero Loss: Brief traffic disruption may occur during protocol reconvergence

•  Convergence Windows: OSPF SPF recalculation and BGP path selection take time

•  Micro-Outages: Sub-second to few-second interruptions possible during switchover

•  Flow Disruption: Existing flows may experience packet loss during path transition

•  New Flows: New flows are immediately redirected once protocols converge

Factors affecting traffic Loss:

1.  Protocol Convergence Speed: Faster OSPF timers and BGP PIC (Prefix Independent Convergence)

reduce loss

2.  Network Topology: More alternate paths and better-meshed networks converge faster

3.  Traffic Patterns: Elephant flows and stateful connections experience more disruption

4.  Hardware Capabilities: Switch forwarding plane performance during reconvergence

Best-Effort Traffic Minimization: Maintenance mode uses industry-standard graceful mechanisms, but
cannot guarantee hitless operation. Plan maintenance windows during low-traffic periods.

Public

Traffic Impact Expectations 7

Deactivation impact on traffic

NOTE
Deactivating maintenance mode with the  no maintenance-mode activ
ate  command can cause traffic loss during BGP neighbor reconvergence.

Why does deactivation cause traffic loss?:

•  BGP Session Restoration: BGP neighbors were shut down during maintenance mode

•  Session Re-establishment: TCP sessions must reconnect, BGP FSM transitions through states

•  Route Re-advertisement: All routes must be re-exchanged and processed

•  RIB/FIB Updates: Routing tables and forwarding tables are updated with new paths

•  Reconvergence Window: Significant time (seconds to minutes) for full BGP reconvergence

Traffic Disruption During Deactivation:

•  Traffic that would use BGP routes through the switch experiences loss until BGP reconverges

•  Existing flows through alternate paths may shift back, causing brief interruption

•  OSPF reconvergence (max-metric removal) is typically faster than BGP

Deactivation Best Practices:

1.  Plan Deactivation Windows: Schedule deactivation during maintenance windows, not production hours

2.  Monitor Reconvergence: Watch BGP session states, route counts, and traffic flows during deactivation

3.  Staged Deactivation: For large networks, consider deactivating in stages if supported by topology

4.  Avoid Rapid Cycling: Do not repeatedly activate/deactivate; each cycle causes reconvergence disruption

The following table summarizes the impact on traffic:

Operation

Activation

Deactivation

Traffic Impact

Primary Cause

Duration

Minimized, not eliminated Protocol reconvergence

Expected loss during BG
P reconvergence

to alternate paths

BGP session re-establish
ment and route re-advert
isement

Sub-second to few secon
ds

Seconds to minutes

Steady State (Active)

Minimal, traffic on altern
ate paths

Normal forwarding throu
gh alternate topology

N/A (stable)

Deployment Planning Checklist

Public

Traffic Impact Expectations 8

Before activating maintenance mode in production networks:

•  Verify Redundant Paths: Confirm alternate paths exist for all critical traffic flows

•  Test in Lab: Validate maintenance mode behavior in lab topology matching production

•  Plan Maintenance Windows: Schedule activation and deactivation during low-traffic periods

•  Monitor Protocols: Prepare monitoring for OSPF metrics and BGP paths during operation

•  Document Expectations: Set stakeholder expectations about potential micro-outages during activation

•  Plan Deactivation Carefully: Treat deactivation as a potentially disruptive event requiring monitoring

•  Have Rollback Plan: Prepare to quickly deactivate if unexpected traffic loss occurs

Configuration Examples

This section provides comprehensive examples showing how to configure and use maintenance mode with
protocol-specific maintenance-units.

Protocol-Specific maintenance-units Architecture

Maintenance mode uses protocol-specific maintenance-units where each maintenance-unit is dedicated to a
single protocol type:

Protocol

Description

BGP maintenance-units

Configure BGP graceful shutdown behavior.

OSPFv2/OSPFv3/OSPFv3-AF maintenance-units

Configure OSPF max-metric behavior for specific OS
PF variants.

Key Design Principle: Maintenance-units are protocol-specific and cannot contain multiple protocols. To
affect multiple protocols during maintenance, create separate protocol-specific maintenance-units and apply
all of them to a maintenance mode profile.

Organizational Flexibility: You can organize maintenance-units by function, such as, "campus-bgp",
"campus-ospfv2" or by network layer, for example, "underlay-ospfv2", "overlay-bgp". Both approaches run
identically; the choice is purely organizational for configuration clarity.

Subtopics

Alternative Profile Configurations
Example 1: Complete Maintenance Configuration
Example 2: Layer-Separated Feature-Sets Configuration

Public

Configuration Examples 9

Alternative Profile Configurations

This example demonstrates how to use protocol-specific maintenance-units organized by network layer for
maintenance operations that require coordinated traffic redirection across underlay and overlay protocols.

Since only one profile can exist at a time, you can reconfigure for different maintenance scenarios:

For Underlay-Only Maintenance

switch(config)# no maintenance-mode profile complete-profile

switch(config)# maintenance-mode profile underlay-profile

switch(config-maint-mode-underlay-profile)# maintenance-unit apply underlay-

ospfv2

switch(config-maint-mode-underlay-profile)# maintenance-unit apply underlay-

ospfv3

switch(config-maint-mode-underlay-profile)# exit

switch(config)# maintenance-mode activate profile underlay-profile
For Overlay-Only Maintenance

switch(config)# no maintenance-mode profile underlay-profile

switch(config)# maintenance-mode profile overlay-profile

switch(config-maint-mode-overlay-profile)# maintenance-unit apply overlay-

bgp

switch(config-maint-mode-overlay-profile)# exit

switch(config)# maintenance-mode activate profile overlay-profile

Example 1: Complete Maintenance Configuration

Configuration Overview

This example demonstrates configuring maintenance mode with protocol-specific maintenance-unit. We
create separate BGP, OSPFv2, and OSPFv3 maintenance-units, then apply all of them to a single
maintenance mode profile for coordinated maintenance affecting all network layers.

Complete Configuration Example

Create BGP maintenance-unit for overlay services:

switch(config)# maintenance-unit bgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# shutdown-delay-timer 120
switch(config-maintenance-unit-bgp-campus-bgp)# neighbor 10.1.1.1 vrf red

switch(config-maintenance-unit-bgp-campus-bgp)# neighbor 10.1.1.2 vrf red

switch(config-maintenance-unit-bgp-campus-bgp)# exit
Create OSPFv2 maintenance-unit for IPv4 underlay routing:

Public

Alternative Profile Configurations 10

switch(config)# maintenance-unit ospfv2 campus-ospfv2

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# process 1 vrf red

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# process 2 vrf red

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# exit
Create OSPFv3 maintenance-unit for IPv6 underlay routing:

switch(config)# maintenance-unit ospfv3 campus-ospfv3

switch(config-maintenance-unit-ospfv3-campus-ospfv3)# process 1 vrf red

switch(config-maintenance-unit-ospfv3-campus-ospfv3)# exit
Create maintenance mode profile and apply all maintenance-units:

switch(config)# maintenance-mode profile campus-profile

switch(config-maint-mode-campus-profile)# maintenance-unit apply campus-bgp

switch(config-maint-mode-campus-profile)# maintenance-unit apply campus-

ospfv2

switch(config-maint-mode-campus-profile)# maintenance-unit apply campus-

ospfv3

switch(config-maint-mode-campus-profile)# exit
Activate maintenance mode with the campus-profile:

switch(config)# maintenance-mode activate profile campus-profile
Show Running Configuration

switch# show running-config maintenance-mode

# Feature-set definitions

maintenance-unit bgp campus-bgp

   shutdown-delay-timer 120

   neighbor 10.1.1.1 vrf red

   neighbor 10.1.1.2 vrf red

maintenance-unit ospfv2 campus-ospfv2

   process 1 vrf red

   process 2 vrf red

maintenance-unit ospfv3 campus-ospfv3

   process 1 vrf red

# Maintenance mode configuration

maintenance-mode profile campus-profile

   maintenance-unit apply campus-bgp

   maintenance-unit apply campus-ospfv2

Public

Example 1: Complete Maintenance Configuration 11

maintenance-unit apply campus-ospfv3

maintenance-mode activate profile campus-profile

NOTE
When viewing the complete switch configuration with show running-config
command (without the maintenance-mode filter), the maintenance-mode section
appears toward the end of the output, after most other configuration sections.

Execution Flow Explanation

Activation Flow

When maintenance mode is activated, all protocols from the applied maintenance-units are executed:

Feature-Set

Purpose

Action

Result

BGP (campus-bgp)

Gracefully remove the sw
itch from BGP overlay ser
vices.

BGP neighbors 10.1.1.1
and 10.1.1.2 in VRF red
are put into maintenance
mode.

OSPFv2 (campus-ospfv2
)

Signal maintenance state
for OSPFv2 IPv4 underl
ay routing.

OSPFv2 processes 1 and
2 in VRF red are put into
maintenance mode.

OSPFv3 (campus-ospfv3
)

Signal maintenance state
for OSPFv3 IPv6 underl
ay routing.

OSPFv3 process 1 in VRF
red is put into maintenan
ce mode.

BGP graceful shutdown c
ommunity is sent to pee
rs and sessions are broug
ht down to redirect overl
ay traffic.

OSPFv2 max-metric is a
pplied to gracefully rem
ove the switch from IPv4
underlay routing.

OSPFv3 max-metric is a
pplied to gracefully rem
ove the switch from IPv6
underlay routing.

Deactivation Flow

When maintenance mode is deactivated using no maintenance-mode activate, normal operation is restored
for all protocols from all applied maintenance-units. All maintenance mode configurations including the
profile and maintenance-units remain configured and can be reactivated later.

REST API Configuration Example

This example demonstrates how to configure maintenance mode with protocol-specific maintenance-units
that provide clear separation by protocol type, enabling granular control and reusability of configurations.

CLI protocol-specific maintenance-units map to two separate REST tables:

•  maintenance-unit bgp → Feature_Set_BGP table

•  maintenance-unit ospfv2/ospfv3/ospfv3-af → Feature_Set_OSPF table (one table for all OSPF variants)

Step 1: Create OSPFv2 maintenance-unit

Public

Example 1: Complete Maintenance Configuration 12

curl -X POST "/rest/latest/system/feature_set_bgps" \

  -H "Content-Type: application/json" \

  -d '{

    "name": "campus-bgp",

    "bgp_peer_vrfs": {

      "10.1.1.1": "/rest/latest/system/vrfs/red",

      "10.1.1.2": "/rest/latest/system/vrfs/red"

    },

    "shutdown_delay_timer": 120,

    "description": "BGP overlay services"

  }'
Step 2: Create OSPFv2 maintenance-unit:

curl -X POST "/rest/latest/system/feature_set_ospfs" \

  -H "Content-Type: application/json" \

  -d '{

    "name": "campus-ospfv2",

    "protocol_type": "ospfv2",

    "ospf_process_vrfs": {

      "1": "/rest/latest/system/vrfs/red",

      "2": "/rest/latest/system/vrfs/red"

    },

    "description": "OSPFv2 IPv4 underlay routing"

  }'
Step 3: Create OSPFv3 maintenance-unit

curl -X POST "/rest/latest/system/feature_set_ospfs" \

  -H "Content-Type: application/json" \

  -d '{

    "name": "campus-ospfv3",

    "protocol_type": "ospfv3",

    "ospf_process_vrfs": {

      "1": "/rest/latest/system/vrfs/red"
    },

    "description": "OSPFv3 IPv6 underlay routing"

  }'
Step 4: Create maintenance mode profile:

curl -X POST "/rest/latest/system/maintenance_mode_profiles" \

  -H "Content-Type: application/json" \

  -d '{
    "name": "campus-mode-profile",

    "description": "Campus network maintenance orchestration"

  }'
Step 5: Create stage and link all maintenance-units to mode profile:

Public

Example 1: Complete Maintenance Configuration 13

curl -X POST "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile/stages" \

  -H "Content-Type: application/json" \

  -d '{

    "stage_id": 1,

    "feature_set_bgp": ["/rest/latest/system/feature_set_bgps/campus-bgp"],

    "feature_set_ospf": [

      "/rest/latest/system/feature_set_ospfs/campus-ospfv2",

      "/rest/latest/system/feature_set_ospfs/campus-ospfv3"

    ]

  }'
Step 6: Activate maintenance mode:

curl -X PATCH "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile" \

  -H "Content-Type: application/json" \

  -d '{"activated": true}'
Step 7: Monitor status:

curl -X GET "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile"
Step 8: Deactivate when maintenance complete:

curl -X PATCH "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile" \

  -H "Content-Type: application/json" \

  -d '{"activated": false}'

Example 2: Layer-Separated Feature-Sets Configuration

Configuration Overview

This example demonstrates organizing maintenance-units by network layer. We create separate "underlay"
OSPFv2/OSPFv3 maintenance-units and an "overlay" BGP maintenance-unit, then apply them to a single
profile for coordinated maintenance affecting all network layers.

Complete Configuration Example

Create underlay OSPFv2 maintenance-unit for IPv4 routing:

switch(config)# maintenance-unit ospfv2 underlay-ospfv2

switch(config-maintenance-unit-ospfv2-underlay-ospfv2)# process 1 vrf red
switch(config-maintenance-unit-ospfv2-underlay-ospfv2)# process 2 vrf red

switch(config-maintenance-unit-ospfv2-underlay-ospfv2)# exit
Create underlay OSPFv3 maintenance-unit for IPv6 routing:

Public

Example 2: Layer-Separated Feature-Sets Configurat... 14

E
x
a
m
p
l
e

2
:

L
a
y
e
r
-
S
e
p
a
r
a
t
e
d

F
e
a
t
u
r
e
-
S
e
t
s

C
o
n
fi
g
u
r
a
t
.
.
.

switch(config)# maintenance-unit ospfv3 underlay-ospfv3

switch(config-maintenance-unit-ospfv3-underlay-ospfv3)# process 1 vrf red

switch(config-maintenance-unit-ospfv3-underlay-ospfv3)# exit
Create overlay BGP maintenance-unit for services:

switch(config)# maintenance-unit bgp overlay-bgp

switch(config-maintenance-unit-bgp-overlay-bgp)# shutdown-delay-timer 120

switch(config-maintenance-unit-bgp-overlay-bgp)# neighbor 10.1.1.1 vrf red

switch(config-maintenance-unit-bgp-overlay-bgp)# neighbor 10.1.1.2 vrf red

switch(config-maintenance-unit-bgp-overlay-bgp)# exit
Create profile applying all maintenance-units for complete maintenance

switch(config)# maintenance-mode profile complete-profile

switch(config-maint-mode-complete-profile)# maintenance-unit apply underlay-

ospfv2

switch(config-maint-mode-complete-profile)# maintenance-unit apply underlay-

ospfv3

switch(config-maint-mode-complete-profile)# maintenance-unit apply overlay-

bgp

switch(config-maint-mode-complete-profile)# exit
Activate maintenance mode with the complete profile

switch(config)# maintenance-mode activate profile complete-profile
Show Running Configuration

switch# show running-config maintenance-mode

# Feature-set definitions

maintenance-unit ospfv2 underlay-ospfv2

   process 1 vrf red

   process 2 vrf red

maintenance-unit ospfv3 underlay-ospfv3

   process 1 vrf red

maintenance-unit bgp overlay-bgp

   shutdown-delay-timer 120

   neighbor 10.1.1.1 vrf red

   neighbor 10.1.1.2 vrf red

# Maintenance mode profile configuration

maintenance-mode profile complete-profile

   maintenance-unit apply underlay-ospfv2

   maintenance-unit apply underlay-ospfv3

Public

Example 2: Layer-Separated Feature-Sets Configurat... 15

maintenance-unit apply overlay-bgp

maintenance-mode activate profile complete-profile

NOTE
When viewing the complete switch configuration with show running-config
(without the maintenance-mode filter), the maintenance-mode section appears
toward the end of the output, after most other configuration sections.

Activation Flow Explanation

When maintenance mode is activated with complete-profile, all underlay and overlay maintenance-units are
applied simultaneously:

Feature-Set

Purpose

Action

Result

Underlay OSPFv2 (underl
ay-ospfv2)

Signal maintenance state
for OSPFv2 IPv4 underl
ay routing.

OSPFv2 processes 1 and
2 in VRF red are put into
maintenance mode.

Underlay OSPFv3 (underl
ay-ospfv3)

Signal maintenance state
for OSPFv3 IPv6 underl
ay routing.

OSPFv3 process 1 in VRF
red is put into maintenan
ce mode.

OSPFv2 max-metric is ap
plied to gracefully redire
ct IPv4 underlay routing t
raffic away from the switc
h.

OSPFv3 max-metric is ap
plied to gracefully redire
ct IPv6 underlay routing t
raffic away from the switc
h.

All configured routing protocols (underlay OSPF and overlay BGP) signal maintenance state simultaneously,
providing coordinated traffic redirection across all network layers.

Deactivation Flow

When maintenance mode is deactivated using no maintenance-mode activate, normal operation is restored
for all protocols in all maintenance-units. The profile and maintenance-units remain configured and can be
reactivated later.

REST API Configuration Example

CLI protocol-specific maintenance-units map to two separate REST tables:

•  maintenance-unit ospfv2/ospfv3 → Feature_Set_OSPF table (one table for all OSPF variants)

•  maintenance-unit bgp → Feature_Set_BGP table

Step 1: Create underlay OSPFv2 maintenance-unit

curl -X POST "/rest/latest/system/feature_set_ospfs" \

  -H "Content-Type: application/json" \

  -d '{

Public

Example 2: Layer-Separated Feature-Sets Configurat... 16

"name": "underlay-ospfv2",

    "protocol_type": "ospfv2",

    "ospf_process_vrfs": {

      "1": "/rest/latest/system/vrfs/red",

      "2": "/rest/latest/system/vrfs/red"

    },

    "description": "Underlay OSPFv2 IPv4 routing"

  }'
Step 2: Create underlay OSPFv3 maintenance-unit

curl -X POST "/rest/latest/system/feature_set_ospfs" \

  -H "Content-Type: application/json" \

  -d '{

    "name": "underlay-ospfv3",

    "protocol_type": "ospfv3",

    "ospf_process_vrfs": {

      "1": "/rest/latest/system/vrfs/red"

    },

    "description": "Underlay OSPFv3 IPv6 routing"

  }'
Step 3: Create overlay BGP maintenance-unit

curl -X POST "/rest/latest/system/feature_set_bgps" \

  -H "Content-Type: application/json" \

  -d '{

    "name": "overlay-bgp",

    "bgp_peer_vrfs": {

      "10.1.1.1": "/rest/latest/system/vrfs/red",

      "10.1.1.2": "/rest/latest/system/vrfs/red"

    },

    "shutdown_delay_timer": 120,

    "description": "Overlay BGP services"

  }'
Step 4: Create maintenance mode profile

curl -X POST "/rest/latest/system/maintenance_mode_profiles" \

  -H "Content-Type: application/json" \

  -d '{

    "name": "complete-mode-profile",

    "description": "Complete maintenance with underlay and overlay"

  }'
Step 5: Create stage and link all maintenance-units to mode profile

curl -X POST "/rest/latest/system/maintenance_mode_profiles/complete-mode-

profile/stages" \

  -H "Content-Type: application/json" \

Public

Example 2: Layer-Separated Feature-Sets Configurat... 17

-d '{

    "stage_id": 1,

    "feature_set_bgp": ["/rest/latest/system/feature_set_bgps/overlay-bgp"],

    "feature_set_ospf": [

      "/rest/latest/system/feature_set_ospfs/underlay-ospfv2",

      "/rest/latest/system/feature_set_ospfs/underlay-ospfv3"

    ]
Step 6: Activate maintenance mode

Ocurl -X PATCH "/rest/latest/system/maintenance_mode_profiles/complete-mode-

profile" \

  -H "Content-Type: application/json" \

  -d '{"activated": true}'
Step 7: Step 7: Deactivate when complete

curl -X PATCH "/rest/latest/system/maintenance_mode_profiles/complete-mode-

profile" \

  -H "Content-Type: application/json" \

  -d '{"activated": false}'
Configuration Notes

This layer-separated approach demonstrates:

1. Layer Separation: Protocol configurations organized by network layer (underlay OSPF vs. overlay BGP)

2. Independent Protocol maintenance-units: Each protocol has its own dedicated maintenance-unit

3. Profile Flexibility: Profile can be deleted and recreated with different maintenance-units combinations for
different maintenance scenarios

Operational Behavior and Recommendations

This section provides important information about maintenance mode operational behavior, default
configurations, feature interactions, and best practices for safe operation.

Default Profile Behavior

When no custom maintenance mode profile is configured, the system automatically applies a comprehensive
default profile that affects all network protocols. This default profile uses protocol-specific default
maintenance-units that are automatically created and applied, though they do not appear in the device
configuration database.

Equivalent default profile configuration (not stored in DB)

maintenance-unit bgp default-bgp

   all-neighbor

maintenance-unit ospfv2 default-ospfv2

   all-process

Public

Operational Behavior and Recommendations 18

maintenance-unit ospfv3 default-ospfv3

   all-process

maintenance-mode profile default-profile

   maintenance-unit apply default-bgp

   maintenance-unit apply default-ospfv2

   maintenance-unit apply default-ospfv3
Default Profile Feature-Sets

The default profile applies maintenance operations to the following protocols using protocol-specific
maintenance-units:

1.  BGP - All neighbor sessions (default-bgp maintenance-unit)

•  All BGP neighbor sessions across all VRFs are put into maintenance mode.

•  BGP graceful shutdown community is sent and sessions are brought down.

2.  OSPF - All processes (default-ospfv2 and default-ospfv3 maintenance-units)

•  All OSPFv2 and OSPFv3 processes across all VRFs are put into maintenance mode using max-metric

approach.

•  This gracefully removes the switch from routing.

Default Profile Recommendations

It is strongly recommended to create and configure a custom maintenance mode profile before activating
maintenance mode. This approach provides several advantages:

•  Administrative Control: Explicit control over which protocols and interfaces are affected

•  Selective Maintenance: Ability to affect only specific network components rather than everything

•  Visibility: Clear documentation of maintenance procedures in the device configuration

•  Predictability: Consistent behavior across maintenance operations

Feature Interaction and Dependencies

Maintenance mode is designed to take precedence over other similar network features to ensure consistent
and predictable behavior during maintenance operations.

Feature Precedence Behavior

When maintenance mode is active, it supersedes the following features:

•  OSPF max-metric commands: Maintenance mode's max-metric implementation takes priority over

manually configured max-metric settings

•  BGP neighbor shutdown commands: Maintenance mode's graceful shutdown process overrides

individual neighbor shutdown configurations

Conflict Avoidance Recommendations

Public

Operational Behavior and Recommendations 19

It is strongly recommended to avoid configuring or modifying conflicting features while maintenance mode is
active or configured. Specifically:

•  Do not configure OSPF max-metric commands while maintenance mode profiles reference those OSPF

processes.

•  Do not issue BGP neighbor shutdown commands for neighbors included in maintenance mode

maintenance-units.

These precautions prevent operational confusion and ensure that maintenance mode behavior remains
predictable and consistent.

Configuration Change Guidelines

Maintenance mode requires configuration stability to ensure reliable and predictable operation throughout
the maintenance window.

Feature-Set and Profile Modification

Feature-sets and profiles can be modified at any time. You can add or remove processes, neighbors, or other
parameters within existing maintenance-units. However, changes made after maintenance mode is activated
have indeterminate behavior and should be avoided.

Configuration Stability Requirements

It is critical not to perform configuration changes to maintenance mode profiles, maintenance-units, or
referenced network protocols while maintenance mode is active. Configuration modifications during active
maintenance can result in:

•

Inconsistent State: Partial application of changes that may not align with the current maintenance stage

•  Unexpected Behavior: Protocol behavior that differs from the configured maintenance profile

•  Traffic Disruption: Unplanned traffic impact due to configuration timing conflicts

•  Operational Complexity: Difficulty troubleshooting issues that arise from configuration changes during

maintenance

Safe Configuration Practices

Follow these guidelines for safe maintenance mode operation:

1.  Pre-Maintenance Planning: Complete all maintenance mode profile and maintenance-unit

configurations before activating maintenance mode.

2.  Configuration Lock: Treat maintenance mode activation as a configuration change freeze period.

3.  Emergency Changes: If emergency configuration changes are absolutely necessary, deactivate

maintenance mode first, make the changes, then reactivate if needed.

Public

Configuration Change Guidelines 20

4.  Post-Maintenance Updates: Schedule any routine configuration changes for after maintenance mode

deactivation and normal operation verification.

Recommended Workflow

1.  Plan maintenance requirements and timeline

2.  Configure maintenance-units and maintenance mode profile

3.  Verify configuration with show commands

4.  Activate maintenance mode (configuration freeze begins)

5.  Perform physical maintenance tasks

6.  Deactivate maintenance mode

7.  Verify normal operation restoration

8.  Resume normal configuration management activities

This workflow ensures that maintenance mode operates in a stable configuration environment, maximizing
the reliability and predictability of the maintenance process.

VSX/MCLAG-Specific Behavior and Scope

What Maintenance Mode does not Include for VSX

•

Important Distinction: Maintenance mode on a VSX peer is not equivalent to VSX software upgrade
procedures or comprehensive VSX maintenance workflows.

•  VSX-Specific Operations NOT Handled by Maintenance Mode.

Maintenance mode does not perform the following VSX-specific operations:

•  VSX ISL (Inter-Switch Link) Maintenance: Maintenance mode does not affect VSX ISL link states or

perform ISL-specific maintenance procedures.

•  VSX Keepalive Management: VSX keepalive link state and keepalive protocol operation are not

modified by maintenance mode.

•  VSX Split-Brain Prevention: Maintenance mode does not alter VSX split-brain detection or prevention

mechanisms.

•  VSX Configuration Synchronization: Maintenance mode configurations (maintenance-units, profiles,
and activation state) are **not synchronized** via VSX config-sync between VSX peers. Each VSX peer
must have its maintenance mode configuration independently configured. Config-sync pause or control
is not part of maintenance mode operations.

Public

VSX/MCLAG-Specific Behavior and Scope 21

•  VSX Role Sequencing: Maintenance mode does not enforce or recommend specific VSX primary/

secondary role sequencing for maintenance.

•  VSX Device Parameter Management: VSX device-specific parameters (system-mac, isl-port, keepalive-

peer, device-role) are not affected.

•  VSX Software Upgrade Distinction: Maintenance mode is not a substitute for VSX software upgrade
procedures. VSX software upgrades have specific workflows, sequencing requirements, and safety
mechanisms that are separate from maintenance mode protocol signaling.

When to use Maintenance Mode on VSX Peers

Selective Protocol Maintenance: Maintenance targeting specific OSPF processes or BGP neighbors.

VSX Maintenance Mode Behavior Details

Traffic redirection in VSX environments:

•  OSPF max-metric causes routing traffic to prefer the non-maintenance VSX peer if available.

•  BGP graceful shutdown redirects BGP traffic to alternate paths, potentially including the other VSX peer.

Maintenance mode on VSX peers provides protocol-level traffic redirection for BGP and OSPF but does not
replace VSX-specific maintenance or upgrade procedures.

High Availability (HA) Behavior

Maintenance mode has specific behaviors and restrictions in High Availability (HA) configurations that
network operators must understand when planning maintenance.

Activation Restrictions

•  Active Switch Only: Maintenance mode can only be activated on the active switch in an HA pair. The

standby switch does not accept maintenance mode activation commands.

•  Command Behavior:

◦  On Active Switch: maintenance-mode activate command executes successfully and puts the active

switch into maintenance mode.

◦  On Standby Switch: maintenance-mode activate command returns an error indicating that

maintenance mode cannot be activated on standby.

This restriction ensures that:

1.  Only the switch actively forwarding traffic can signal maintenance state to the network.

2.  Configuration changes that affect active traffic flows are controlled from the active switch.

Public

High Availability (HA) Behavior 22

3.  Standby switch remains in ready state to assume active role if needed.

Failover Behavior

Ephemeral State: Maintenance mode state is not maintained across HA failover events. When an HA failover
occurs:

1.  Previous Active Switch: Maintenance mode state is lost when the switch transitions to standby role.

2.  New Active Switch: Assumes active role in normal operation mode (not in maintenance mode).

3.  Network Operation: Network protocols on the new active switch begin normal operation immediately.

Post-Failover Actions: After an HA failover, if maintenance operations still need to continue:

1.  Verify that the new active switch has stabilized and is forwarding traffic normally.

2.

If maintenance mode is still needed, run maintenance-mode activate [profile <PROFILE_NAME>] on
the new active switch.

3.  All maintenance mode configurations (profiles and maintenance-units) remain in the device

configuration and can be reactivated.

HA Maintenance Planning

Recommended Approach for maintenance in HA environments:

1.  Pre-Maintenance Verification:

•  Verify HA status and identify the active switch

•  Ensure HA synchronization is complete

•  Verify both switches are healthy

2.  Maintenance Execution:

•  Activate maintenance mode on the active switch only

•  Perform maintenance tasks on the active switch

•  Monitor HA status throughout maintenance

3.  Failover Scenarios:

•  If unplanned failover occurs during maintenance, maintenance mode is automatically cleared

•  Assess whether to reactivate maintenance mode on the new active switch

•  Consider completing maintenance on the original switch after it returns to service

4.  Planned Failover:

•  Deactivate maintenance mode before initiating planned failover

Public

High Availability (HA) Behavior 23

•  Allow network to stabilize in normal operation

•  If needed, activate maintenance mode on the new active switch after failover completes

Configuration Synchronization:

Maintenance mode profiles and maintenance-units are synchronized between HA peers as part of normal
configuration synchronization. However, the active/inactive state of maintenance mode itself is not
synchronized and remains local to the active switch.

Known Issues and Limitations

This section documents current limitations and known issues with the maintenance mode implementation
that network operators should be aware of when planning maintenance operations.

BGP Address Family Limitations

Supported Address Famili
es

Maintenance mode BGP maintenance-units currently support only the followin
g address families:

•

•

IPv4 Unicast: Fully supported for graceful shutdown and maintenance ope
rations.

IPv6 Unicast: Fully supported for graceful shutdown and maintenance ope
rations.

Unsupported Address Fam
ilies

The following BGP address families are not qualified for maintenance mode o
perations:

Impact

Recommended Workaroun
d

•  EVPN Route-Type 2 (MAC/IP Advertisement Routes): EVPN MAC/IP routes
are not included in maintenance mode graceful shutdown procedures.

•  EVPN Route-Type 5 (IP Prefix Routes): EVPN IP prefix routes are not inclu

ded in maintenance mode graceful shutdown procedures.

BGP neighbors configured with EVPN address families will not receive graceful
shutdown treatment for EVPN routes during maintenance mode activation. Onl
y IPv4 and IPv6 unicast routes will be gracefully withdrawn.

For networks heavily dependent on EVPN services, consider:

1.  Manual EVPN neighbor shutdown before activating maintenance mode.

2.  Coordinating maintenance windows with EVPN convergence timelines.

3.  Monitoring EVPN route convergence separately from maintenance mode o

perations.

Public

Known Issues and Limitations 24

OSPF Standards Compliance Limitations

RFC 8379 not supported Maintenance mode OSPF implementation does not include support for RFC 83

Impact

Current Behavior

79 (OSPF Graceful Link Shutdown).

Current Implementation:

The maintenance mode OSPF maintenance-units use the traditional max-metri
c approach rather than the newer graceful link shutdown mechanisms defined i
n RFC 8379.

Networks expecting RFC 8379 compliant graceful link shutdown behavior will
experience traditional max-metric behavior instead.

•  OSPF processes use maximum metric values (0xFFFF) in LSA advertiseme

nts.

•  Standard OSPF convergence procedures apply.

•  No RFC 8379 specific graceful shutdown signaling.

Planning Considerations

1.  Factor traditional OSPF convergence times into maintenance windows.

2.  Monitor OSPF neighbor states and LSA propagation during maintenance o

perations.

Supportability and Diagnostics Limitations

SAINT Integration

SAINT (Service Availability Insight) is not supported in this release.

General Recommendations

Given these limitations, network operators should:

1.  Pre-Maintenance Testing: Validate maintenance mode behavior in lab environments that match

production network characteristics.

2.  Selective Application

: Consider creating maintenance-units that exclude problematic address families or routing protocols.

3.  Manual Coordination:

: Plan manual intervention for unsupported protocol features during maintenance windows.

4.  Monitoring Strategy:

Public

Known Issues and Limitations 25

Implement comprehensive monitoring for both supported and unsupported protocol behaviors during
maintenance.

These limitations are documented to ensure proper maintenance planning and to set appropriate
expectations for maintenance mode behavior in complex network environments.

Maintenance Mode Scope and Traffic Impact Analysis

This section provides a comprehensive analysis of what maintenance mode addresses in the current release
and clearly identifies scenarios that are out of scope. This compartmentalized view helps network operators
understand the specific traffic impact of maintenance mode operations.

Current Release Scope

Maintenance mode in this release is specifically designed to address *3 Unicast dynamic routing protocols:

Supported Protocols

Traffic Types

OSPF (OSPFv2, OSPFv3, OSPFv3-AF)

IPv4 and IPv6 unicast routing via OSPF max-metric

BGP IPv4 Unicast

BGP IPv6 Unicast

IPv4 unicast prefix advertisement and neighbor sess
ion management

IPv6 unicast prefix advertisement and neighbor sess
ion management

Traffic Impact: When maintenance mode is activated, these protocols gracefully redirect L3 unicast routing
traffic away from the switch undergoing maintenance, minimizing disruption to unicast IP forwarding.

L3 Unicast Out-of-Scope Features

The following L3 unicast routing features and scenarios are not addressed by maintenance mode in the
current release:

Routing Protocols and Features

Description

Static Routes

Maintenance mode does not modify or disable static route c
onfigurations

Policy-Based Routing (PBR)

PBR configurations remain active and unchanged during mai
ntenance

VRRP

First-hop redundancy protocol is not affected by maintenanc
e mode

Public

Maintenance Mode Scope and Traffic Impact Analysis 26

Routing Protocols and Features

Description

Route Maps and Filters

Multicast Routing Protocols

BGP Advanced Features:

BGP EVPN Address Family

Existing route manipulation policies continue to operate nor
mally

PIM, IGMP, and MLD are not in scope (see L2/L3 Multicast s
ection below).

EVPN Route-Type 2 (MAC/IP) and Route-Type 5 (IP Prefix)
routes are not qualified for maintenance mode.

BGP VPNv4/VPNv6

MPLS L3VPN address families are not in scope.

BGP Multicast Address Family

BGP multicast prefixes are not affected.

These out-of-scope L3 features continue normal operation during maintenance mode. Static routes, PBR,
and VRRP will continue to forward traffic, potentially preventing complete traffic redirection if they provide
active paths to destinations.

L2 Unicast Out-of-Scope Features

All L2 unicast forwarding mechanisms and protocols are out of scope for maintenance mode in the current
release:

L2 Protocols and Features

Description

Spanning Tree Protocol (STP/RSTP/MSTP)

STP states and bridge priorities are not modified.

Link Aggregation (LAG/LACP)

Interface Draining feature is currently out of scope.

MAC Address Learning

Dynamic MAC learning continues normally.

VLAN Forwarding

Layer 2 VLAN forwarding behavior is unchanged.

Multicast Routing Protocols

PIM, IGMP, and MLD are not in scope (see L2/L3 Multicast s
ection below).

L2 unicast traffic forwarding continues normally during maintenance mode. Switches remain active
participants in STP topology, LAG bundles remain operational, and MAC learning continues. This means
L2-switched traffic is not redirected during maintenance operations. LACP/LAG maintenance capabilities are
planned in a future release, which will provide graceful L2 link shutdown mechanisms.

L2/L3 Multicast Out-of-Scope Features

All multicast routing and forwarding features are out of scope for maintenance mode in the current release:

Public

Maintenance Mode Scope and Traffic Impact Analysis 27

L2 Protocols and Features

Description

PIM (Protocol Independent Multicast)

PIM-SM, PIM-DM, and PIM-SSM operations are not affected.

IGMP (Internet Group Management Protocol) IGMP snooping and IGMP querier functions continue normal

ly.

MAC Address Learning

MLD for IPv6 multicast operates unchanged.

MLD (Multicast Listener Discovery)

Layer 2 VLAN forwarding behavior is unchanged.

Multicast VPN

L3 multicast VPN services are not in scope.

MVR (Multicast VLAN Registration):

MVR configurations remain active.

Multicast traffic (both L2 and L3) continues to flow normally through the switch during maintenance mode.
The switch remains an active participant in multicast distribution trees, continues to process IGMP/MLD
reports, and forwards multicast traffic based on existing state. Multicast maintenance capabilities are under
consideration for future releases, which will provide graceful multicast traffic redirection mechanisms.

Key Principle

Maintenance mode is narrowly scoped to L3 unicast dynamic routing protocols (OSPF and BGP unicast) only.

All other traffic types, forwarding mechanisms, and protocols continue normal operation during maintenance.
Network operators must plan maintenance procedures accounting for traffic that is not redirected by
maintenance mode, including L2 switched traffic, multicast traffic, and traffic forwarded via static routes or
other out-of-scope mechanisms.

For comprehensive traffic redirection during physical switch maintenance, operators may need to combine
maintenance mode activation with additional manual procedures for out-of-scope features.

Show Events

Monitor the progress of maintenance mode activation, deactivation and diagnose graceful shutdown
sequencing for BGP and OSPF protocols. The show events -d gshut-daemon command displays the event
logs generated by gshut-daemon:

Event Name

GSHUT_PROFILE_ACTIVATED

GSHUT_PROFILE_DEACTIVATED

Description

Logs event when a maintenance mode profile is
activated

Logs event when a maintenance mode profile is
deactivated

Public

Show Events 28

| Event Name |     | Description |     |     |
| ---------- | --- | ----------- | --- | --- |
GSHUT_FEATURE_SET_STATUS_CHANGE Logs event when a routing process completes i
ts graceful shutdown during maintenance
GSHUT_BGP_COORDINATION_CHANGE Logs event when BGP graceful shutdown prog
resses to a new phase
GSHUT_BGP_TIMER_STARTED Logs event when BGP graceful shutdown timer
starts
GSHUT_BGP_TIMER_EXPIRED Logs event when BGP graceful shutdown timer
expires and triggers neighbor session shutdown

REST API Terminology and Data Model Reference
This section provides comprehensive mapping between CLI terminology and REST API data structures
for maintenance mode configuration. This reference is intended for REST API developers and automation
engineers who need to understand how CLI concepts translate to REST API operations.
CLI to REST API Terminology Mapping
| CLI Terminology | REST API Schema | Yang Path | Description |     |
| --------------- | --------------- | --------- | ----------- | --- |
maintenance-unit bgp Feature_Set_BGP /system/feature_ BGP-specific maintenanc
|     |     | set_bgps | e configurations |     |
| --- | --- | -------- | ---------------- | --- |
maintenance-unit ospfv2 Feature_Set_OSPF /system/feature_ OSPF-specific maintenan
| /ospfv3/ospfv3-af |     | set_ospfs | ce configurations (all vari |     |
| ----------------- | --- | --------- | --------------------------- | --- |
ants share one table)
maintenance-mode profil Maintenance_Mode_Profil /system/maintenance_mo Top-level orchestration li
| e   | e   | de_profiles | nking maintenance-units |     |
| --- | --- | ----------- | ----------------------- | --- |
to stages
Not visible in CLI Maintenance_Stage /system/maintenance_mo System-managed contain
|     |     | de_profiles/stages | er grouping maintenanc |     |
| --- | --- | ------------------ | ---------------------- | --- |
e-units
Key Architecture Change:
The REST API uses two separate protocol-specific tables (Feature_Set_BGP, Feature_Set_OSPF) instead of
a single multi-protocol table. This aligns with the CLI's protocol-specific maintenance-unit model. Stages link
to feature-sets via URI references in separate typed arrays.
|     | Public | REST API Terminology and Data Model Reference |     | 29  |
| --- | ------ | --------------------------------------------- | --- | --- |

Data Model Hierarchy

The REST API uses a 3-tier hierarchy with protocol-specific tables:

Subtopics

Public

REST API Terminology and Data Model Reference 30

Key REST API Concepts
REST API Base Paths

Key REST API Concepts

Protocol-Specific Tables

By design, feature-sets are stored in two separate protocol-specific tables:

Feature-set

Table

Fields

Feature_Set_BGP

/rest/latest/system/feature_set_bgps

bgp_peer_vrfs

Contains only BGP-related fields

shutdown_delay_timer

all_instances

Feature_Set_OSPF

/rest/latest/system/feature_set_ospfs

protocol_type

Handles ALL OSPF variants (OSPFv2, OSP
Fv3, OSPFv3-AF-IPv4, OSPFv3-AF-IPv6)

ospf_process_vrfs

ospf_all_vrfs_process_ids

all_instances

Typed Feature-Set Arrays in Stages

Stages use separate typed arrays with URI references for each protocol:

{

  "feature_set_bgp": ["/rest/latest/system/feature_set_bgps/campus-bgp"],

  "feature_set_ospf": [

    "/rest/latest/system/feature_set_ospfs/campus-ospfv2",

    "/rest/latest/system/feature_set_ospfs/campus-ospfv3"
  ]

}
Each protocol has its own array, using URI references (not UUIDs) to identify feature-sets.

VRF Name to URI Reference Resolution

CLI uses VRF names, but REST API uses VRF URI references:

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv2" \
  -H "Content-Type: application/json" \

  -d '{"ospf_process_vrfs": {"1": "/rest/latest/system/vrfs/red"}}'
Stage Creation:

Public

Key REST API Concepts 31

When you create a Maintenance_Mode_Profile, stages start empty. You must explicitly create stages via
POST to link feature-sets:

Create mode profile (starts with empty stages):

curl -X POST "/rest/latest/system/maintenance_mode_profiles" \

  -H "Content-Type: application/json" \

  -d '{"name": "campus-mode-profile"}'
Create stage and link feature-sets:

curl -X POST "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile/stages" \

  -H "Content-Type: application/json" \

  -d '{

    "stage_id": 1,

    "feature_set_bgp": ["/rest/latest/system/feature_set_bgps/campus-bgp"],

    "feature_set_ospf": ["/rest/latest/system/feature_set_ospfs/campus-

ospfv2"]

  }'
Activation Control

Maintenance mode is activated or deactivated by setting the activated boolean on the
Maintenance_Mode_Profile:

Activate maintenance mode:

curl -X PATCH "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile" \

  -H "Content-Type: application/json" \

  -d '{"activated": true}'
Deactivate maintenance mode:

curl -X PATCH "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile" \

  -H "Content-Type: application/json" \

  -d '{"activated": false}'

REST API Base Paths

All maintenance mode REST APIs use the following base path:

/rest/latest/system/feature_set_bgps
(Feature_Set_BGP)
/rest/latest/system/feature_set_ospfs

(Feature_Set_OSPF)

/rest/latest/system/maintenance_mode_profiles

(Maintenance_Mode_Profile)

Public

REST API Base Paths 32

/rest/latest/system/maintenance_mode_profiles/{name}/stages

(Maintenance_Stage - POST to create)

/rest/latest/system/maintenance_mode_profiles/{name}/stages/{stage_id}

(GET/DELETE)

Complete REST API Workflow Example

1. Create BGP maintenance-unit:

curl -X POST "/rest/latest/system/feature_set_bgps" \

  -H "Content-Type: application/json" \

  -d '{

    "name": "campus-bgp",

    "bgp_peer_vrfs": {"10.1.1.1": "/rest/latest/system/vrfs/red",

"10.1.1.2": "/rest/latest/system/vrfs/red"},

    "shutdown_delay_timer": 120

  }'
2. Create OSPF maintenance-unit:

curl -X POST "/rest/latest/system/feature_set_ospfs" \

  -H "Content-Type: application/json" \

  -d '{

    "name": "campus-ospfv2",

    "protocol_type": "ospfv2",

    "ospf_process_vrfs": {"1": "/rest/latest/system/vrfs/red", "2": "/rest/

latest/system/vrfs/red"}

  }'
3. Create mode profile:

curl -X POST "/rest/latest/system/maintenance_mode_profiles" \

  -H "Content-Type: application/json" \

  -d '{"name": "campus-mode-profile"}'
4. Create stage and link feature-sets via URI references:

curl -X POST "/rest/latest/system/maintenance_mode_profiles/campus-mode-
profile/stages" \

  -H "Content-Type: application/json" \

  -d '{

    "stage_id": 1,

    "feature_set_bgp": ["/rest/latest/system/feature_set_bgps/campus-bgp"],

    "feature_set_ospf": ["/rest/latest/system/feature_set_ospfs/campus-

ospfv2"]

  }'
5. Activate maintenance mode:

curl -X PATCH "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile" \

Public

REST API Base Paths 33

-H "Content-Type: application/json" \

  -d '{"activated": true}'
6. Check status:

curl -X GET "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile"
7. Deactivate when complete

curl -X PATCH "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile" \

  -H "Content-Type: application/json" \

  -d '{"activated": false}'

NOTE

REST API Usage Notes for REST API developers:

•  Protocol-specific maintenance-units are stored in two separate tables

•  Stages use separate feature_set_bgp and feature_set_ospf arrays with URI

references

•  VRF references use URI paths directly, for example /rest/latest/system/

vrfs/red) — no UUID lookup needed

•  Stages must be explicitly created via POST after creating the mode profile

•  PATCH on stages is additive only; use DELETE + POST to replace stage

content

•  Activation state is controlled at the Maintenance_Mode_Profile level, not

individual maintenance-units

One Feature_Set_OSPF table handles all OSPF variants (v2, v3, v3-AF-IPv4,
v3-AF-IPv6)

•  OSPF POST requires protocol_type field to specify the variant

Maintenance mode commands

Subtopics

maintenance-mode activate [profile <PROFILE_NAME>]
maintenance-mode profile <PROFILE_NAME>
maintenance-unit apply <FEATURE_SET_NAME>
maintenance-unit bgp <FEATURE_SET_NAME>

Public

Maintenance mode commands 34

maintenance-unit ospfv2 <FEATURE_SET_NAME>
maintenance-unit ospfv3 <FEATURE_SET_NAME>
maintenance-unit ospfv3-af-ipv4 <FEATURE_SET_NAME>
maintenance-unit ospfv3-af-ipv6 <FEATURE_SET_NAME>
neighbor <IP_ADDRESS> vrf <VRF_NAME>
process <PROCESS_ID>
show events -d gshut-daemon
show maintenance-mode profile
show maintenance-mode
show maintenance-unit
shutdown-delay-timer <SECONDS>

maintenance-mode activate [profile <PROFILE_N
AME>]

Syntax

[no] maintenance-mode activate [profile <PROFILE_NAME>]

Description

Activates maintenance mode on the Aruba switch. This command puts the switch into maintenance mode,
allowing network operators to perform maintenance tasks while minimizing disruption to live network traffic.
The command uses protocol mechanisms (OSPF max-metric, BGP GSHUT community with shutdown timer)
to gracefully reroute traffic away from the switch.

The no form of this command seactivates maintenance mode on the Aruba switch. This command takes the
switch out of maintenance mode and restores normal operation, regardless of whether maintenance mode
was activated with the default profile or a custom profile. All maintenance mode configurations including
profiles and feature-sets remain configured and can be reactivated later.

NOTE
Deactivation can cause traffic loss during BGP neighbor reconvergence. BGP
sessions that were shut down during maintenance mode must re-establish, re-
exchange routes, and update routing tables. This reconvergence process takes
time (seconds to minutes) and may disrupt traffic. Plan deactivation during
appropriate maintenance windows. See the "Design Principles and Traffic Impact"
section for detailed information.

Parameter

activate

Description

Activates maintenance mode state.

Public

maintenance-mode activate [profile <PROFILE_NAME>] 35

Parameter

Description

Required

profile <PROFILE_NAME>

Name of the pre-configured profile.

Optional

Usage

Traffic Impact Warning: Activation minimizes but does not eliminate traffic loss. Brief disruption may
occur during protocol reconvergence to alternate paths. Redundant network paths are required for proper
operation. See the Design Principles and Traffic Impact section for detailed information.

Default Profile Activation: When executed without the profile parameter, maintenance-mode activate
uses the built-in default profile which affects all OSPF processes, all BGP neighbors, and all VSX/MCLAG LAG
ports across all VRFs.

Custom Profile Activation: When executed with profile <PROFILE_NAME>, maintenance mode uses the
specified custom profile. The profile must be pre-configured. If the specified profile does not exist, the
command returns an error.

High Availability (HA) Restriction: Maintenance mode can only be activated on the active switch in an HA
configuration. Attempting to activate maintenance mode on the standby switch will result in an error.

Configuration Freeze During Activation: Once maintenance mode is activated, any modifications to
maintenance-units (BGP or OSPF) or custom maintenance-mode profiles will not be applied dynamically
at runtime. Changes to maintenance-unit configurations or profile associations made after activation will
only take effect after deactivating and reactivating maintenance mode. To apply updated configurations,
deactivate maintenance mode first using no maintenance-mode activate, make the necessary changes, and
then reactivate maintenance mode.

Maintenance mode is active until manually deactivated or system reboot. After reboot or HA failover, the
system returns to normal operation.

Examples

Activating maintenance mode with default profile:

switch(config)# maintenance-mode activate
Activating maintenance mode with a custom profile:

switch(config)# maintenance-mode activate profile campus-profile
Activating maintenance mode when no profile is configured (shows default behavior note):

switch(config)# maintenance-mode activate

Note: No maintenance profile configured, using default behavior (all OSPF,

BGP)
Activating maintenance mode with a profile that has no stages configured (shows warning):

Public

maintenance-mode activate [profile <PROFILE_NAME>] 36

switch(config)# maintenance-mode activate profile empty-profile

Warning: Maintenance mode profile has no stages configured.

Using default behavior (all OSPF, BGP).
Attempting to activate when maintenance mode is already active with same profile:

switch(config)# maintenance-mode activate profile campus-profile

Maintenance mode is already activated
Attempting to activate when maintenance mode is already active with different profile

switch(config)# maintenance-mode activate profile other-profile

Error: Maintenance mode is already activated for profile 'campus-profile'.

Only one profile can be activated at a time.

Please deactivate the current profile first using 'no maintenance-mode

activate'
Activating with non-existent profile (error)

switch(config)# maintenance-mode activate profile nonexistent

Profile 'nonexistent' not found
Deactivating maintenance mode :

switch(config)# no maintenance-mode activate

REST API Examples

Activating maintenance mode on node profile:

curl -X PATCH "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile" \

  -H "Content-Type: application/json" \

  -d '{"activated": true}'
Deactivating maintenance mode:

curl -X PATCH "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile" \

  -H "Content-Type: application/json" \

  -d '{"activated": false}'

Release

10.18

Modification

Command introduced.

Public

maintenance-mode activate [profile <PROFILE_NAME>] 37

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

8400

9300

9300-32D

10000

maintenance-mode profile <PROFILE_NAME>

Syntax

[no] maintenance-mode profile <PROFILE_NAME>

Description

Creates or enters into the maintenance mode profile context. This command allows you to define a custom
maintenance mode profile that references pre-created BGP and OSPF maintenance-units. The profile can
reference one or multiple maintenance-units depending on maintenance requirements. To use a configured
profile, it must be explicitly specified in the maintenance-mode activate profile <PROFILE_NAME>
command.

The no form of this command deletes a maintenance-mode profile from the configuration. This command
removes the entire maintenance-mode profile including all maintenance-unit application references. The
profile cannot be deleted while maintenance mode is active using that profile. You must first deactivate
maintenance mode using no maintenance-mode activate before deleting the profile. Maintenance-units
referenced by the profile remain configured and can be applied to other profiles. Only one maintenance-

Public

maintenance-mode profile <PROFILE_NAME> 38

mode profile can exist at a time, so deleting the current profile allows the creation of a different profile
configuration.

NOTE

Only one custom maintenance-mode profile can be configured at a time in this
release. Attempting to create a second profile while one already exists will be
rejected by the system. However, multiple maintenance-units can coexist and be
reused. To create a different maintenance-mode profile configuration, you must
first delete the existing maintenance-mode profile using no maintenance-mode
profile <PROFILE_NAME>, then create the new maintenance-mode profile.
Feature-sets remain configured and can be reused when creating different
maintenance-mode profile configurations.

.

Parameter

Description

<PROFILE_NAME>

Name of the maintenance mode profile.

Required

Examples

Creating and entering maintenance mode profile named campus-profile

switch(config)# maintenance-mode profile campus-profile

switch(config-maint-mode-campus-profile)#
In this example, a custom maintenance-mode profile already exists and another profile is created. This will be
rejected.

switch(config)# maintenance-mode profile ospf

switch(config-maint-mode-ospf)# exit

switch(config)# maintenance-mode profile ospf1

% Only one custom maintenance-mode profile is allowed, delete existing one
to create a new maintenance-mode profile.
To resolve this, delete the existing profile using no maintenance-mode profile
<EXISTING_PROFILE_NAME>before creating a new one.

Deleting maintenance-mode profile named campus-profile

switch(config)# no maintenance-mode profile campus-profile
Deleting an active profile will fail:

switch(config)# no maintenance-mode profile campus-profile
Error: Cannot delete profile 'campus-profile' - maintenance mode is

currently active
To achieve this deactivate first, then delete:

Public

maintenance-mode profile <PROFILE_NAME> 39

switch(config)# no maintenance-mode activate

switch(config)# no maintenance-mode profile campus-profile

REST API Examples

Creating maintenance mode profile (stages start empty; create via POST separately)

curl -X POST "/rest/latest/system/maintenance_mode_profiles" \

  -H "Content-Type: application/json" \

  -d '{

    "name": "campus-mode-profile",

    "description": "Campus network maintenance orchestration"

  }'
Delete maintenance node profile (CLI maintenance-mode profile maps to Maintenance_Mode_Profile in
REST):
curl -X DELETE "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile"
REST API will fail if node profile is currently activated. First deactivate, then delete:

curl -X DELETE "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile"

  -H "Content-Type: application/json" \

  -d '{"activated": false}'

curl -X DELETE "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile"

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

config-feature-set-bgp-c
ampus-bgp

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

Public

maintenance-mode profile <PROFILE_NAME> 40

Platforms

Command context

Authority

8400

9300

9300-32D

10000

maintenance-unit apply <FEATURE_SET_NAME>

Syntax

[no] maintenance-unit apply <FEATURE_SET_NAME>

Description

Applies a pre-created maintenance-unit within a maintenance mode profile. This command references a
protocol-specific maintenance-unit that was previously created at the global configuration level and applies
it to the profile. Each feature-set is dedicated to a single protocol (BGP or OSPF), and multiple maintenance-
units can be applied within the same profile to affect multiple protocols during maintenance.

The no form removes a maintenance-unit application from a maintenance-mode profile. This command
unlinks the specified maintenance-unit from the profile without deleting the maintenance-unit itself. The
maintenance-unit remains configured at the global level and can be applied to other profiles or reapplied
later. This removal can be performed regardless of whether maintenance mode is active, but will affect
maintenance operations if performed while the profile is active. If you remove all maintenance-units from a
profile, the profile becomes empty but still exists.

Parameter

Description

<FEATURE_SET_NAME>

BGP neighbor IP address (when using specific neighbor).

Examples

Applying BGP maintenance-unit within a profile:

switch(config)# maintenance-mode profile campus-profile

switch(config-maint-mode-campus-profile)# maintenance-mode apply campus-bgp
Applying multiple protocol-specific maintenance-units within a profile:

switch(config-maint-mode-campus-profile)# maintenance-mode apply campus-bgp

switch(config-maint-mode-campus-profile)# maintenance-mode apply campus-

ospfv2
Removing BGP maintenance-unit from a profile:

Public

maintenance-unit apply <FEATURE_SET_NAME> 41

switch(config)# maintenance-mode profile campus-profile

switch(config-maint-mode-campus-profile)# no maintenance-unit apply campus-

bgp
Removing one of multiple maintenance-units from a profile:

switch(config)# maintenance-mode profile campus-profile

switch(config-maint-mode-campus-profile)# no maintenance-mode apply

underlay-ospfv2

REST API Examples

Linking maintenance-units to mode profile by creating a stage with feature-set references. Custom profiles
start with empty stages; create stage via POST with feature-set URI references

curl -X POST "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile/stages" \

  -H "Content-Type: application/json" \

  -d '{

    "stage_id": 1,

    "feature_set_bgp": ["/rest/latest/system/feature_set_bgps/campus-bgp"],

    "feature_set_ospf": ["/rest/latest/system/feature_set_ospfs/campus-

ospfv2"]

  }'
Removing maintenance-unit from profile by replacing stage content:

NOTE

PATCH on stages is additive only (cannot remove feature-sets). Use DELETE +
POST to replace.

Delete existing stage and recreate with only the desired feature-sets.

curl -X DELETE "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile/stages/1"
Recreate stage with only campus-ospfv2 (campus-bgp removed):

curl -X POST "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile/stages" \

  -H "Content-Type: application/json" \

  -d '{

    "stage_id": 1,

    "feature_set_ospf": ["/rest/latest/system/feature_set_ospfs/campus-

ospfv2"]
  }'
Remove all maintenance-units from profile (delete stage entirely)

curl -X DELETE "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile/stages/1"

Public

maintenance-unit apply <FEATURE_SET_NAME> 42

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

8400

9300

9300-32D

10000

maintenance-unit bgp <FEATURE_SET_NAME>

Syntax

[no] maintenance-unit bgp <FEATURE_SET_NAME>

Description

Creates and enters a BGP maintenance-unit context at the global configuration level. This command
allows you to define reusable BGP- specific maintenance-units for maintenance mode operations. BGP
maintenance-units configure graceful shutdown behavior for BGP neighbor sessions including shutdown
delay timers and neighbor selection. Once created, you can configure BGP- specific parameters directly
(no sub-context). These BGPmaintenance-units can be referenced and applied within maintenance mode
profiles.

The no form of this command deletes a BGP maintenance-unit from the global configuration. It also
removes the entire BGP maintenance-unit including all BGP neighbor and timer configurations. The BGP

Public

maintenance-unit bgp <FEATURE_SET_NAME> 43

maintenance-unit cannot be deleted if it is currently applied to a maintenance-mode profile. You must
first remove the maintenance-unit from any profiles using no maintenance-unit <FEATURE_SET_NAME>
before deletion. The maintenance-unit can be deleted regardless of whether maintenance mode is active, as
long as it is not applied to the active profile.

Parameter

Description

<FEATURE_SET_NAME>

Name of the BGP maintenance-unit.

Required

Examples

Creating BGP maintenance-unit named campus-bgp with neighbor configuration:

switch(config)# maintenance-unit bgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# neighbor 10.1.1.1 vrf red
Creating a BGP maintenance-unit with all-neighbor configuration:

switch(config)# maintenance-unit bgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# all-neighbor
Deleting a BGP maintenance-unit named campus-bgp:

switch(config)# no maintenance-unit bgp campus-bgp
Attempting to delete BGP maintenance-unit that is applied to a profile. This will fail:

switch(config)# no maintenance-unit bgp campus-bgp

Error: Cannot delete maintenance-unit 'campus-bgp' - currently applied to

maintenance-mode profile 'campus-profile'
The correct sequence is to remove from profile first, then delete the maintenance-unit:

switch(config)# maintenance-mode profile campus-profile

switch(config-maint-mode-campus-profile)# no maintenance-unit apply campus-

bgp

switch(config-maint-mode-campus-profile)# exit
switch(config)# no maintenance-unit bgp campus-bgp

REST API Examples

Creating a BGP maintenance-unit with specific neighbor:

(CLI maintenance-unit bgp maps to Feature_Set_BGP table in REST)

curl -X POST "/rest/latest/system/feature_set_bgps" \
  -H "Content-Type: application/json" \
  -d '{

    "name": "campus-bgp",

    "bgp_peer_vrfs": {"10.1.1.1": "/rest/latest/system/vrfs/red"},

Public

maintenance-unit bgp <FEATURE_SET_NAME> 44

"shutdown_delay_timer": 120

  }'
Creating a BGP maintenance-unit with all neighbors:

curl -X POST "/rest/latest/system/feature_set_bgps" \

  -H "Content-Type: application/json" \

  -d '{

    "name": "campus-bgp",

    "all_instances": true,

    "shutdown_delay_timer": 120

  }'
Attempting to delete BGP maintenance-unit that is applied to a profile. REST API will fail if maintenance-unit
is referenced by any node profile stage. First, remove the reference from the stage:

curl -X DELETE "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile/stages/1"
Then delete the maintenance-unit:

curl -X DELETE "/rest/latest/system/feature_set_bgps/campus-bgp"

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

8400

9300

9300-32D

10000

Public

maintenance-unit bgp <FEATURE_SET_NAME> 45

maintenance-unit ospfv2 <FEATURE_SET_NAME>

Syntax

[no] maintenance-unit ospfv2 <FEATURE_SET_NAME>

Description

Creates and enters an OSPFv2 maintenance-unit context at the global configuration level. This command
allows you to define reusable OSPFv2-specific maintenance-unit for maintenance mode operations. OSPFv2
maintenance-unit configure max-metric behavior for OSPFv2 processes supporting IPv4 routing. Once
created, you can configure OSPFv2 process IDs and VRFs directly (no sub-context). These OSPFv2
maintenance-unit can be referenced and applied within maintenance mode profiles.

The no form of this command deletes an OSPF maintenance-unit from the global configuration. It also
removes the entire OSPF maintenance-unit including all OSPF process and VRF configurations. The OSPF
maintenance-unit cannot be deleted if it is currently applied to a maintenance-mode profile.

NOTE

You must first remove the maintenance-unit from any profiles using
no maintenance-unit apply <FEATURE_SET_NAME> before deletion. The
maintenance-unit can be deleted regardless of whether maintenance mode is
active, as long as it is not applied to the active profile.

Parameter

Description

<FEATURE_SET_NAME>

Name of the OSPFv2 maintenance-unit.

Required

Examples

Creating OSPFv2 maintenance-unit named campus-ospfv2:

switch(config)# maintenance-unit ospfv2  campus-ospfv2

switch(config-maintenance-unit-ospfv2-campus-ospfv2)#
Creating OSPFv2 maintenance-unit named campus-ospfv2 with REST API:

(CLI maintenance-unit ospfv2 maps to Feature_Set_OSPF table in REST)

Public

maintenance-unit ospfv2 <FEATURE_SET_NAME> 46

curl -X POST "/rest/latest/network/maintenance/feature_set_ospf" \

  -H "Content-Type: application/json" \

  -d '{"name": "campus-ospfv2"}'

NOTE
One Feature_Set_OSPF table handles all OSPF variants (v2, v3, v3-AF-IPv4,
v3-AF-IPv6)

Delete OSPFv2 maintenance-unit named campus-ospfv2

switch(config)# no maintenance-unit ospfv2 campus-ospfv2
Attempting to delete OSPF maintenance-unit that is applied to a profile will fail:

switch(config)# no maintenance-unit ospfv2 campus-ospfv2

Error: Cannot delete maintenance-unit 'campus-ospfv2' - currently applied

to maintenance-mode profile 'campus-profile'
Remove from profile first, then delete the maintenance-unit:

switch(config)# maintenance-mode profile campus-profile

switch(config-maint-mode-campus-profile)# no maintenance-unit apply campus-

ospfv2

switch(config-maint-mode-campus-profile)# exit

switch(config)# no  maintenance-unit ospfv2 campus-ospfv2

REST API Examples

Removing OSPFv2 maintenance-unit:

curl -X DELETE "/rest/latest/system/feature_set_ospfs/campus-ospfv2"

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

Public

maintenance-unit ospfv2 <FEATURE_SET_NAME> 47

Platforms

Command context

Authority

8325H

8360

8400

9300

9300-32D

10000

maintenance-unit ospfv3 <FEATURE_SET_NAME>

Syntax

[no] maintenance-unit ospfv3 <FEATURE_SET_NAME>

Description

Creates and enters an OSPFv3 feature-set context at the global configuration level. This command
allows you to define reusable OSPFv3-specific feature-sets for maintenance mode operations. OSPFv3
maintenance-unit configure max-metric behavior for OSPFv3 processes supporting IPv6 routing. Once
created, you can configure OSPFv3 process IDs and VRFs directly (no sub-context). These OSPFv3
maintenance-units can be referenced and applied within maintenance mode profiles.

The no form of this command deletes an OSPF maintenance-unit from the global configuration. It also
removes the entire OSPF maintenance-unit including all OSPF process and VRF configurations. The OSPF
maintenance-unit cannot be deleted if it is currently applied to a maintenance-mode profile.

NOTE
You must first remove the maintenance-unit from any profiles using no
maintenance-unit apply <FEATURE_SET_NAME> before deletion. The feature-
set can be deleted regardless of whether maintenance mode is active, as long as
it is not applied to the active profile.

Parameter

Description

<FEATURE_SET_NAME>

Name of the OSPFv3 maintenance-unit.

Required

Public

maintenance-unit ospfv3 <FEATURE_SET_NAME> 48

Examples

Creating OSPFv3 maintenance-unit named campus-ospfv3:

switch(config)# maintenance-unit ospfv3  campus-ospfv3

switch(config-maintenance-unit-ospfv3-campus-ospfv3)#
Deleting OSPFv3 feature-set named campus-ospfv3

switch(config)# no maintenance-unit ospfv3 campus-ospfv3

REST API Examples

Creating OSPFv3 maintenance-unit named campus-ospfv3 with REST API:

(CLI maintenance-unit ospfv3 maps to Feature_Set_OSPF table in REST)

curl -X POST "/rest/latest/system/feature_set_ospfs" \

  -H "Content-Type: application/json" \

  -d '{"name": "campus-ospfv3", "protocol_type": "ospfv3"}'
Removing OSPFv3 maintenance-unit

curl -X DELETE "/rest/latest/system/feature_set_ospfs/campus-ospfv3"

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

8400

9300

9300-32D

10000

Public

maintenance-unit ospfv3 <FEATURE_SET_NAME> 49

maintenance-unit ospfv3-af-ipv4 <FEATURE_SET_
NAME>

Syntax

[no] maintenance-unit ospfv3-af-ipv4 <FEATURE_SET_NAME>

Description

Creates and enters an OSPFv3-AF-IPv4 maintenance-unit context at the global configuration level. This
command allows you to define reusable OSPFv3-AF-IPv4-specific maintenance-units for maintenance mode
operations. OSPFv3-AF-IPv4 maintenance-units configure max-metric behavior for OSPFv3 processes using
the IPv4 address family. Once created, you can configure OSPFv3-AF-IPv4 process IDs and VRFs directly (no
sub-context). These OSPFv3-AF-IPv4 maintenance-units can be referenced and applied within maintenance
mode profiles.

The no form of this command deletes an OSPF maintenance-unit from the global configuration. It also
removes the entire OSPF maintenance-unit including all OSPF process and VRF configurations. The OSPF
maintenance-unit cannot be deleted if it is currently applied to a maintenance-mode profile.

NOTE
You must first remove the feature-set from any profiles using no maintenance-
unit apply <FEATURE_SET_NAME> before deletion. The maintenance-unit can
be deleted regardless of whether maintenance mode is active, as long as it is not
applied to the active profile.

Parameter

Description

<FEATURE_SET_NAME>

Name of the OSPFv3-AF-IPv4 maintenance-unit.

Required

Examples

Creating OSPFv3 maintenance-unit named campus-ospfv3-af-ipv4:

switch(config)# maintenance-unit ospfv3-af-ipv4  campus-ospfv3-af-ipv4

switch(config-maintenance-unit-ospfv3-af-ipv4-campus-ospfv3-af-ipv4)#
Creating OSPFv3-AF-IPv4 maintenance-unit named campus-ospfv3-af-ipv4 with REST API:

(CLI maintenance-unit ospfv3-af-ipv4 maps to Feature_Set_OSPF table in REST)

Public

maintenance-unit ospfv3-af-ipv4 <FEATURE_SET_NAME> 50

curl -X POST "/rest/latest/system/feature_set_ospfs" \

  -H "Content-Type: application/json" \

  -d '{"name": "campus-ospfv3-af-ipv4", "protocol_type": "ospfv3-af-ipv4"}'

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

8400

9300

9300-32D

10000

maintenance-unit ospfv3-af-ipv6 <FEATURE_SET_
NAME>

Syntax

[no] maintenance-unit ospfv3-af-ipv6 <FEATURE_SET_NAME>

Description

Creates and enters an OSPFv3-AF-IPv6 maintenance-unit context at the global configuration level. This
command allows you to define reusable OSPFv3-AF-IPv6-specific maintenance-units for maintenance mode
operations. OSPFv3-AF-IPv6 maintenance-units configure max-metric behavior for OSPFv3 processes using

Public

maintenance-unit ospfv3-af-ipv6 <FEATURE_SET_NAME> 51

the IPv6 address family. Once created, you can configure OSPFv3-AF-IPv6 process IDs and VRFs directly (no
sub-context). These OSPFv3-AF-IPv6 maintenance-units can be referenced and applied within maintenance
mode profiles.

The no form of this command deletes an OSPF maintenance-unit from the global configuration. It also
removes the entire OSPF maintenance-unit including all OSPF process and VRF configurations. The OSPF
maintenance-unit cannot be deleted if it is currently applied to a maintenance-mode profile.

NOTE

You must first remove the maintenance-unit from any profiles using
no maintenance-unit apply <FEATURE_SET_NAME> before deletion. The
maintenance-unit can be deleted regardless of whether maintenance mode is
active, as long as it is not applied to the active profile.

Parameter

Description

<FEATURE_SET_NAME>

Name of the OSPFv3-AF-IPv6 maintenance-unit.

Required

Examples

Creating OSPFv3-AF-IPv6 feature-set named campus-ospfv3-af-ipv6:

switch(config)# maintenance-unitospfv3-af-ipv6  campus-ospfv3-af-ipv6

switch(config-feature-set-ospfv3-af-ipv6-campus-ospfv3-af-ipv6)#
Creating OSPFv3-AF-IPv6 maintenance-unit named campus-ospfv3-af-ipv6 with REST API:

(CLI maintenance-unit ospfv3-af-ipv6 maps to Feature_Set_OSPF table in REST)

curl -X POST "/rest/latest/system/feature_set_ospfs" \

  -H "Content-Type: application/json" \

  -d '{"name": "campus-ospfv3-af-ipv6", "protocol_type": "ospfv3-af-ipv6"}'

Release

10.18

Modification

Command introduced.

Public

maintenance-unit ospfv3-af-ipv6 <FEATURE_SET_NAME> 52

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

8400

9300

9300-32D

10000

neighbor <IP_ADDRESS> vrf <VRF_NAME>

Syntax

[no] {neighbor <IP_ADDRESS> vrf <VRF_NAME> | all-neighbor}

Description

Specifies the BGP neighbor IP address and VRF within a BGP maintenance-unit, or configures all BGP
neighbors from all VRFs. You can specify individual neighbor IP addresses with specific VRF names, or
use all-neighbor to include all BGP neighbors from all VRFs. Multiple individual neighbor commands can
be configured within the same BGP maintenance-unit. The all-neighbor command overrides any specific
neighbor configurations since it includes everything. When applied during maintenance mode, BGP graceful
shutdown (GSHUT) community is sent to peers and BGP neighbor sessions are brought down.

The no form removes specific BGP configurations from a BGP maintenance-unit. The no neighbor command
removes a specific BGP neighbor and VRF combination. The no all-neighbor command removes the
configuration that affects all BGP neighbors across all VRFs. These provide granular control without deleting
the entire BGP maintenance-unit.

Parameter

Description

neighbor <IP_ADDRESS>

BGP neighbor IP address (when using specific neighbor).

Public

neighbor <IP_ADDRESS> vrf <VRF_NAME> 53

Parameter

Description

vrf <VRF_NAME>

Specific VRF name (only with specific neighbor IP.

all-neighbor

All BGP neighbors from all VRFs (alternative to specific neighbo
r).

Examples

Configuring BGP neighbor 10.1.1.1 in VRF red in the maintenance-unit

switch(config)# maintenance-unit bgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# neighbor 10.1.1.1 vrf red
Configuring multiple BGP neighbors in different VRFs in the maintenance-unit:

switch(config)# maintenance-unit bgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# neighbor 10.1.1.1 vrf red

switch(config-maintenance-unit-bgp-campus-bgp)# neighbor 10.1.1.2 vrf red

switch(config-maintenance-unit-bgp-campus-bgp)# neighbor 10.2.1.1 vrf blue
Configuring all BGP neighbors from all VRFs in the maintenance-unit:

switch(config)# maintenance-unit bgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# all-neighbor
Removing specific BGP neighbor 10.1.1.1 from VRF red

switch(config)# maintenance-unit bgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# no neighbor 10.1.1.1 vrf red
Removing all-neighbor configuration

switch(config)# maintenance-unitbgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# no all-neighbor

REST API Examples

Configuring specific BGP neighbors with VRFs (using VRF URI references):

curl -X PATCH "/rest/latest/system/feature_set_bgps/campus-bgp" \

  -H "Content-Type: application/json" \

  -d '{

    "bgp_peer_vrfs": {

      "10.1.1.1": "/rest/latest/system/vrfs/red",

      "10.1.1.2": "/rest/latest/system/vrfs/red"

    },

    "shutdown_delay_timer": 120

  }'
Configuring BGP to affect all neighbors across all VRFs:

curl -X PATCH "/rest/latest/system/feature_set_bgps/campus-bgp" \

  -H "Content-Type: application/json" \

Public

neighbor <IP_ADDRESS> vrf <VRF_NAME> 54

-d '{

    "all_instances": true,

    "shutdown_delay_timer": 120

  }'
Configuring specific peer addresses that apply to all VRFs:

curl -X PATCH "/rest/latest/network/maintenance/feature_set_bgp/campus-bgp"

\

  -H "Content-Type: application/json" \

  -d '{

    "bgp_all_vrfs_peer_addresses": ["10.1.1.1", "10.1.1.2"],

    "shutdown_delay_timer": 120

  }'
Removing specific BGP neighbor/VRF combination. Get current configuration, modify, then update:

curl -X GET "/rest/latest/system/feature_set_bgps/campus-bgp" > current.json
Edit current.json to remove specific neighbor/VRF entry from bgp_peer_vrfs map

curl -X PATCH "/rest/latest/system/feature_set_bgps/campus-bgp" \

  -H "Content-Type: application/json" \

  -d '{

    "bgp_peer_vrfs": {

      "10.1.1.2": "/rest/latest/system/vrfs/red"

    }

  }'
Removing all-neighbor configuration:

curl -X PATCH "/rest/latest/system/feature_set_bgps/campus-bgp" \

  -H "Content-Type: application/json" \

  -d '{"all_instances": false}'

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

Public

neighbor <IP_ADDRESS> vrf <VRF_NAME> 55

Platforms

Command context

Authority

8325

8325H

8360

8400

9300

9300-32D

10000

process <PROCESS_ID>

Syntax

[no] process <PROCESS_ID> {vrf <VRF_NAME> | all-vrfs | all-process }

Description

Specifies the OSPF process ID (OSPFv2, OSPFv3, OSPFv3-AF-IPv4 or OSPFv3-AF-IPv6) and VRF within an
OSPF maintenance-unit, or configures all OSPF processes from all VRFs. You can specify individual process
IDs with specific VRF names, configure a specific process ID across all VRFs using all-vrfs, or use all-process
to include all OSPF processes from all VRFs.

NOTE

OSPFv3-AF-IPv4 and uses OSPFv3 with the IPv4 address family. OSPFv3-AF-
IPv6 uses OSPFv3 with the IPv6 address family.

The no form of this command removes a specific OSPF process and VRF combination from an OSPF
maintenance-unit, removes a process configured with all-vrfs, or removes the all-process configuration.
This provides granular control to remove individual OSPF processes without deleting the entire OSPF
maintenance-unit. Multiple process commands can be removed individually. The no process <ID> all-vrfs
command removes the all-VRFs configuration for a specific process ID. The no all-process command
removes the configuration that affects all OSPF processes across all VRFs.

Usage

Configuration Options:

Public

process <PROCESS_ID> 56

Option

Command

Description

Specific Process + Specific VRF

process vrf <VRF_NAME>

Specific Process + All VRFs

process <ID> all-vrfs

All Processes

process <ID> all-process

Targets a single process in a single
VRF

Applies the specified process ID ac
ross all VRFs (including default VR
F)

Includes all process IDs from all V
RFs

Multiple individual process commands can be configured within the same OSPF maintenance-unit. When
both specific VRF and all-vrfs configurations exist for the same process ID, the all-vrfs configuration
takes precedence as it is a superset. The all-process command includes all process IDs from all VRFs and
represents the broadest scope.

NOTE
Important Configuration Timing: Configuration changes made before
maintenance-mode activate take effect immediately. Configuration changes
made after maintenance mode is activated have indeterminate behavior and
should be avoided.

When applied during maintenance mode, OSPF processes use the max-metric
approach to signal maintenance state to neighboring routers.

Parameter

<PROCESS_ID>

Description

OSPF process ID (when using specific process).

Required

Range: 1-65535

Specific VRF name (only with specific process ID and specific V
RF).

All OSPF processes from all VRFs (alternative to specific proces
s).

Apply process ID to all VRFs including default VRF (alternative
to specific VRF).

vrf <VRF_NAME>

all-process

all-vrfs

Examples

Configuring OSPFv2 process 1 in VRF red:

Public

process <PROCESS_ID> 57

switch(config)# maintenance-unit ospfv2 campus-ospfv2

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# process 1 vrf red
Configuring OSPFv3 process 1 in VRF red:

switch(config)# maintenance-unit ospfv3 campus-ospfv3

switch(config-maintenance-unit-ospfv3-campus-ospfv3)# process 1 vrf red
Configuring OSPFv3-AF-IPv4 process 1 in VRF red:

switch(config)# maintenance-unitospfv3-af-ipv4 campus-ospfv3-af-ipv4

switch(config-maintenance-unit-ospfv3-af-ipv4-campus-ospfv3-af-ipv4)#

process 1 vrf red
Configuring OSPFv3-AF-IPv6 process 1 in VRF red:

switch(config)# maintenance-unitospfv3-af-ipv6 campus-ospfv3-af-ipv6

switch(config-maintenance-unit-ospfv3-af-ipv6-campus-ospfv3-af-ipv6)#

process 1 vrf red
For the following examples, replace OSPFv2 with OSPFv3, OSPFv3-af-ipv4 or OSPFv3-af-ipv6 as needed.

Configuring multiple OSPFv2 processes in different VRFs:

switch(config)# maintenance-unit ospfv2 campus-ospfv2

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# process 1 vrf red

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# process 2 vrf red

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# process 3 vrf blue
Configuring OSPFv2 process 1 across all VRFs:

switch(config)# maintenance-unit ospfv2 campus-ospfv2

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# process 1 all-vrfs
Configuring multiple OSPFv2 processes across all VRFs:

switch(config)# maintenance-unit ospfv2 campus-ospfv2

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# process 1 all-vrfs

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# process 2 all-vrfs
Configuring all OSPFv2 processes from all VRFs

switch(config)# maintenance-unitospfv2 campus-ospfv2

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# all-process
Removing OSPFv2 process 1 from VRF red:

switch(config)# maintenance-unitospfv2 campus-ospfv2

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# no process 1 vrf red
Removing OSPFv2 process 1 all-vrfs configuration:

switch(config)# maintenance-unit ospfv2 campus-ospfv2

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# no process 1 all-vrfs
Removing all-process configuration

switch(config)# maintenance-unit ospfv2 campus-ospfv2

switch(config-maintenance-unit-ospfv2-campus-ospfv2)# no all-process

Public

process <PROCESS_ID> 58

REST API Examples

NOTE
The OSPFv2 examples also apply to OSPFv3. Replace campus-ospfv2 with
campus-ospfv3.

Configuring OSPFv2 processes with specific VRFs (using VRF URI references):

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv2" \

  -H "Content-Type: application/json" \

  -d '{

    "ospf_process_vrfs": {

      "1": "/rest/latest/system/vrfs/red",

      "2": "/rest/latest/system/vrfs/red"

    }

  }'
Configuring OSPFv2 process 1 to apply across all VRFs (including default):

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv2" \

  -H "Content-Type: application/json" \

  -d '{

    "ospf_all_vrfs_process_ids": [1]

  }'
Configuring multiple OSPFv2 processes to apply across all VRFs:

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv2" \

  -H "Content-Type: application/json" \

  -d '{

    "ospf_all_vrfs_process_ids": [1, 2]

  }'
Configuring OSPFv2 to affect all processes across all VRFs:

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv2" \

  -H "Content-Type: application/json" \
  -d '{"all_instances": true}'
Configuring specific OSPFv2 process IDs that apply to all VRFs:

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv2" \

  -H "Content-Type: application/json" \

  -d '{

    "ospf_all_vrfs_process_ids": [1, 2, 3]

  }'
Configuring specific OSPFv3-AF-IPv4 processes with specific VRF:

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv3-af-ipv4"

\

  -H "Content-Type: application/json" \

Public

process <PROCESS_ID> 59

-d '{

    "ospf_process_vrfs": {

      "1": "/rest/latest/system/vrfs/red"

    }

  }'
Configuring OSPFv3-AF-IPv4 process 1 to apply across all VRFs (including default)

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv3-af-ipv4"

\

  -H "Content-Type: application/json" \

  -d '{

    "ospf_all_vrfs_process_ids": [1]

  }'
Configuring specific OSPFv3-AF-IPv6 process/VRF combination:

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv3-af-ipv6"

\

  -H "Content-Type: application/json" \

  -d '{

    "ospf_process_vrfs": {

      "1": "/rest/latest/system/vrfs/red"

    }

  }'
Configuring multiple OSPFv3-AF-IPv6 processes:

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv3-af-ipv6"

\

  -H "Content-Type: application/json" \

  -d '{

    "ospf_process_vrfs": {

      "1": "/rest/latest/system/vrfs/red",

      "2": "/rest/latest/system/vrfs/red"

    }

  }'
Configuring OSPFv3-AF-IPv6 process 1 to apply across all VRFs (including default)

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv3-af-ipv6"

\

  -H "Content-Type: application/json" \

  -d '{

    "ospf_all_vrfs_process_ids": [1]

  }'
Configuring OSPFv3-AF-IPv6 to affect all processes across all VRFs:

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv3-af-ipv6"

\

Public

process <PROCESS_ID> 60

-H "Content-Type: application/json" \

  -d '{"all_instances": true}'
To remove specific OSPF process/VRF combination using REST API, get current configuration, modify, then
update:

curl -X GET "/rest/latest/system/feature_set_ospfs/campus-ospfv2" >

current.json
Edit current.json to remove specific process/VRF entry from ospf_process_vrfs map, then update:

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv2" \

  -H "Content-Type: application/json" \

  -d '{

    "ospf_process_vrfs": {

      "2": "/rest/latest/system/vrfs/red"

    }

  }'
Removing process all-vrfs configuration:

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv2" \

  -H "Content-Type: application/json" \

  -d '{

    "ospf_process_vrfs": {

      "1": []

    }

  }'
Removing all-process configuration:

curl -X PATCH "/rest/latest/system/feature_set_ospfs/campus-ospfv2" \

  -H "Content-Type: application/json" \

  -d '{"all_instances": false}'

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

Public

process <PROCESS_ID> 61

Platforms

Command context

Authority

8325

8325H

8360

8400

9300

9300-32D

10000

show events -d gshut-daemon

Syntax

show events -d gshut-daemon

Description

Displays event logs generated by gshut-daemon for maintenance mode operations. Use this command to
monitor the progress of maintenance mode activation and deactivation, and to diagnose graceful shutdown
sequencing for BGP and OSPF protocols.

Example

Displaying event logs during a BGP and OSPF maintenance mode activation:

switch# show events -d gshut-daemon

---------------------------------------------------

show event logs

---------------------------------------------------

2026-03-08:10:00:01.000000|gshut-daemon|17601|LOG_INFO|UKWN|-|Maintenance

mode activated using profile 'campus-maintenance-profile'

2026-03-08:10:00:01.050000|gshut-daemon|17604|LOG_INFO|UKWN|-|BGP 'bgp-

campus-fs': graceful shutdown community advertised to all neighbors

2026-03-08:10:00:01.100000|gshut-daemon|17605|LOG_INFO|UKWN|-|BGP graceful

shutdown timer started for 'bgp-campus-fs' (120 seconds)

2026-03-08:10:02:01.150000|gshut-daemon|17606|LOG_INFO|UKWN|-|BGP graceful

shutdown timer for 'bgp-campus-fs' expired (timer elapsed), triggering

neighbor session shutdown

2026-03-08:10:02:01.200000|gshut-daemon|17604|LOG_INFO|UKWN|-|BGP 'bgp-

Public

show events -d gshut-daemon 62

campus-fs': all neighbors gracefully shutdown

2026-03-08:10:02:01.300000|gshut-daemon|17603|LOG_INFO|UKWN|-|BGP process

'bgp-campus-fs' graceful shutdown executed, neighbors in maintenance state

2026-03-08:10:02:01.400000|gshut-daemon|17603|LOG_INFO|UKWN|-|OSPF process

'ospf-campus-fs' graceful shutdown executed, neighbors in maintenance state

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

8400

9300

9300-32D

10000

show maintenance-mode profile

Syntax

show maintenance-mode profile

Description

Displays the configuration details of the maintenance mode profile including maintenance-unit breakdown
and protocol-specific settings. This command shows what is configured, not runtime state. Use this
command to review the maintenance mode configuration including BGP shutdown timers and OSPF process
selections. The output clearly distinguishes between default (built-in) and custom profiles.

Public

show maintenance-mode profile 63

Parameter

profile

Examples

Description

Command to show profile configuration.

Required

Displaying maintenance mode profile when default profile is used:

switch# show maintenance-mode profile

Maintenance Mode Profile: default (built-in)

Applied Feature-Sets:

  - default-feature

    BGP Configuration:

      Shutdown Delay Timer: 120 seconds

      Neighbor Scope: All neighbors from all VRFs

    OSPF Configuration:

      OSPFv2: All processes from all VRFs

      OSPFv3: All processes from all VRFs

      OSPFv3-AF-IPv4: All processes from all VRFs

      OSPFv3-AF-IPv6: All processes from all VRFs

NOTE

Default profile does not appear in running-config

Displaying custom maintenance mode profile configuration:

switch# show maintenance-mode profile

=== ACTIVE PROFILE (Custom) ===
Maintenance Mode Profile: campus-profile

Applied Feature-Sets:

  - campus-feature

    BGP Configuration:

      Shutdown Delay Timer: 120 seconds

      Neighbors:

        - 10.1.1.1 (VRF: red)

        - 10.1.1.2 (VRF: red)

Public

show maintenance-mode profile 64

OSPF Configuration:

      OSPFv2 Processes:

        - Process 1 (VRF: red)

        - Process 2 (VRF: red)

      OSPFv3 Processes:

        - Process 1 (VRF: red)

=== DEFAULT PROFILE (Reference) ===

Note: This built-in profile would be used if custom profile is deleted

Applied Feature-Sets:

  - default-feature

    BGP Configuration:

      Shutdown Delay Timer: 120 seconds

      Neighbor Scope: All neighbors from all VRFs

    OSPF Configuration:

      OSPFv2: All processes from all VRFs

      OSPFv3: All processes from all VRFs

      OSPFv3-AF-IPv4: All processes from all VRFs

      OSPFv3-AF-IPv6: All processes from all VRFs
Displaying profile with multiple maintenance-units:

switch# show maintenance-mode profile

=== ACTIVE PROFILE (Custom) ===

Maintenance Mode Profile: complete-profile

Applied Feature-Sets:

  - underlay-feature

    OSPF Configuration:

      OSPFv2 Processes:

        - Process 1 (VRF: red)

        - Process 2 (VRF: red)

      OSPFv3 Processes:

        - Process 1 (VRF: red)

  - overlay-feature

    BGP Configuration:

      Shutdown Delay Timer: 120 seconds

      Neighbors:

        - 10.1.1.1 (VRF: red)

Public

show maintenance-mode profile 65

- 10.1.1.2 (VRF: red)

=== DEFAULT PROFILE (Reference) ===

Note: This built-in profile would be used if custom profile is deleted

Applied Feature-Sets:

  - default-feature

    BGP Configuration:

      Shutdown Delay Timer: 120 seconds

      Neighbor Scope: All neighbors from all VRFs

    OSPF Configuration:

      OSPFv2: All processes from all VRFs

      OSPFv3: All processes from all VRFs

      OSPFv3-AF-IPv4: All processes from all VRFs

      OSPFv3-AF-IPv6: All processes from all VRFs
Displaying profile when no profile is configured

switch# show maintenance-mode profile

No custom maintenance mode profile configured

NOTE

By default, when maintenance mode is activated without a profile, the built-in
default profile will be applied, affecting all OSPF processes and all BGP neighbors.
To view default profile details run maintenance-mode activate without profile
parameter to apply default, then run show maintenance-mode profile to see
active default configuration.

REST API Examples

Step 1: Get mode profile with all details:

curl -X GET "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile"
Step 2: Get all BGP maintenance-units:

curl -X GET "/rest/latest/system/feature_set_bgps"
Step 3: Get all OSPF maintenance-units

curl -X GET "/rest/latest/system/feature_set_ospfs"
Step 4: Get specific maintenance-unit configuration:

curl -X GET "/rest/latest/system/feature_set_bgps/campus-bgp"

curl -X GET "/rest/latest/system/feature_set_ospfs/campus-ospfv2"
Step 5: Get stage configuration with linked maintenance-units:

Public

show maintenance-mode profile 66

curl -X GET "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile/stages/1"

NOTE
The maintenance-unit {bgp | ospfv2 | ospfv3} command maps to two separate
REST tables:

Command

REST table

Feature_Set_BGP

/rest/latest/system/feature_set_
bgps

Feature_Set_OSPF

'/rest/latest/system/feature_set_ospfs'

(handles all OSPF variants)

The maintenance-mode profile command maps to Maintenance_Mode_Profile
in REST API.
Feature-sets are referenced by URI paths in separate feature_set_bgp and
feature_set_ospf arrays on the stage
VRF references use URI paths. For example /rest/latest/system/vrfs/red.
Stages must be explicitly created via POST after creating the mode profile

Each protocol has its own dedicated table with protocol-specific fields.

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

Public

show maintenance-mode profile 67

Platforms

Command context

Authority

8400

9300

9300-32D

10000

show maintenance-mode

Syntax

show maintenance-mode

Description

Displays comprehensive maintenance mode operational status including current state and protocol
execution details. This command provides real-time visibility into maintenance mode operations including
protocol-specific status information. Use this command to monitor the operational state of an active
maintenance session.

Examples

Displaying maintenance mode status when active with custom profile:

switch# show maintenance-mode

Maintenance Mode Status: Active

Active Profile: campus-profile

Activation Time: 14:32:15

Duration: 00:15:42

Protocol Status:

  BGP:

    Status: GSHUT community advertised

    Shutdown Timer: 42 seconds remaining (of 120 configured)

    Neighbors Affected: 2 (VRF red)

  OSPF:

    OSPFv2: max-metric active (2 processes in VRF red)

    OSPFv3: max-metric active (1 process in VRF red)

Applied Feature-Sets:

  - campus-feature (Active)

Public

show maintenance-mode 68

Displaying maintenance mode status when active with default profile:

switch# show maintenance-mode

Maintenance Mode Status: Active

Active Profile: default

Activation Time: 14:32:15

Duration: 00:15:42

Protocol Status:

  BGP:

    Status: GSHUT community advertised

    Shutdown Timer: 42 seconds remaining (of 120 configured)

    Neighbors Affected: All neighbors from all VRFs

  OSPF:

    OSPFv2: max-metric active (all processes from all VRFs)

    OSPFv3: max-metric active (all processes from all VRFs)

Applied Feature-Sets:

  - default-feature (Active)
Displaying maintenance mode status during deactivation:

switch# show maintenance-mode

Maintenance Mode Status: Deactivating

Active Profile: campus-profile

Deactivation Started: 15:45:10

Deactivation Duration: 00:02:15

Protocol Restoration Status:

  BGP: Restoring neighbor sessions (2 neighbors)

  OSPF: Removing max-metric (3 processes)

Applied Feature-Sets:
  - campus-feature (Restoring)

Displaying maintenance mode status when not active:

switch# show maintenance-mode

Maintenance Mode Status: Inactive

Active Profile: None

REST API Examples

Step 1: Get mode profile status (includes activated state, maintenance_status):

Public

show maintenance-mode 69

curl -X GET "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile"
Step 2: Get all BGP maintenance-units:

curl -X GET "/rest/latest/system/feature_set_bgps"
Step 3: Get all OSPF maintenance-units:

curl -X GET "/rest/latest/system/feature_set_ospfs"
Step 4: Get specific BGP maintenance-unit details:

curl -X GET "/rest/latest/system/feature_set_bgps/campus-bgp"
Step 5: Get stage details with maintenance-unit references:

curl -X GET "/rest/latest/system/maintenance_mode_profiles/campus-mode-

profile/stages/1"

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

8400

9300

9300-32D

10000

Public

show maintenance-mode 70

show maintenance-unit

Syntax

show maintenance-unit {bgp | ospf}

Description

Displays all configured maintenance-units with optional filtering by protocol type. This command shows both
default (built-in) and user-configured maintenance-units along with their key configuration parameters. Use
this command to review all available maintenance-units that can be applied to maintenance-mode profiles.
When run without a protocol filter, both BGP and OSPF maintenance-units are displayed. Use the bgp
keyword to display only BGP maintenance-units. Use the ospf keyword to display only OSPF maintenance-
units (including OSPFv2, OSPFv3, OSPFv3-AF-IPv4, and OSPFv3-AF-IPv6).

Parameter

{bgp | ospf}

Examples

Description

Name of the protocol to filter the output.

Optional

Displaying all maintenance-units when no custom maintenance-units are configured:

switch# show maintenance-unit

Maintenance Units:

==================

Default Maintenance-Units:

  - default-bgp (Default, BGP)

      Shutdown Delay Timer: 120 seconds

      Neighbor Scope: All neighbors from all VRFs

  - default-ospfv2 (Default, OSPFv2)
      Process Scope: All processes from all VRFs

  - default-ospfv3-af-ipv6 (Default, OSPFv3-AF-IPv6)

      Process Scope: All processes from all VRFs

  - default-ospfv3-af-ipv4 (Default, OSPFv3-AF-IPv4)

      Process Scope: All processes from all VRFs

  - default-ospfv3 (Default, OSPFv3)

      Process Scope: All processes from all VRFs
Displaying only BGP maintenance-units when no custom BGP maintenance-units are configured

switch# show maintenance-unit bgp

Maintenance Units:

==================

Public

show maintenance-unit 71

Default Maintenance-Units:

  - default-bgp (Default, BGP)

      Shutdown Delay Timer: 120 seconds

      Neighbor Scope: All neighbors from all VRFs

User-configured Maintenance-Units:

  No custom BGP maintenance-unit configured.
Displaying only OSPF maintenance-units when no custom OSPF maintenance-units are configured:

switch# show maintenance-unit ospf

Maintenance Units:

==================

Default Maintenance-Units:

  - default-ospfv2 (Default, OSPFv2)

      Process Scope: All processes from all VRFs

  - default-ospfv3-af-ipv6 (Default, OSPFv3-AF-IPv6)

      Process Scope: All processes from all VRFs

  - default-ospfv3-af-ipv4 (Default, OSPFv3-AF-IPv4)

      Process Scope: All processes from all VRFs

  - default-ospfv3 (Default, OSPFv3)

      Process Scope: All processes from all VRFs

User-configured Maintenance-Units:

  No custom OSPF maintenance-unit configured.
Displaying all maintenance-units with custom maintenance-units configured:

switch# show maintenance-unit

Maintenance Units:

==================

Default Maintenance-Units:
  - default-bgp (Default, BGP)

      Shutdown Delay Timer: 120 seconds

      Neighbor Scope: All neighbors from all VRFs

  - default-ospfv2 (Default, OSPFv2)

      Process Scope: All processes from all VRFs

  - default-ospfv3-af-ipv6 (Default, OSPFv3-AF-IPv6)

      Process Scope: All processes from all VRFs

  - default-ospfv3-af-ipv4 (Default, OSPFv3-AF-IPv4)

      Process Scope: All processes from all VRFs

  - default-ospfv3 (Default, OSPFv3)

      Process Scope: All processes from all VRFs

Public

show maintenance-unit 72

User-configured Maintenance-Units:

  - campus-bgp (Custom, BGP)

      Shutdown Delay Timer: 180 seconds

      Neighbors:

        - 10.1.1.1 (VRF: red)

        - 10.1.1.2 (VRF: red)

  - campus-ospfv2 (Custom, OSPFv2)

      Processes:

        - Process 1 (VRF: red)

        - Process 2 (VRF: red)
Displaying only BGP maintenance-units with custom BGP maintenance-unit configured:

switch# show maintenance-unit bgp

Maintenance Units:

==================

Default Maintenance-Units:

  - default-bgp (Default, BGP)

      Shutdown Delay Timer: 120 seconds

      Neighbor Scope: All neighbors from all VRFs

User-configured Maintenance-Units:

  - campus-bgp (Custom, BGP)

      Shutdown Delay Timer: 180 seconds

      Neighbors:

        - 10.1.1.1 (VRF: red)

        - 10.1.1.2 (VRF: red)
Displaying only OSPF maintenance-units with custom OSPF maintenance-unit configured:

switch# show maintenance-unit ospf

Maintenance Units:

==================

Default Maintenance-Units:

  - default-ospfv2 (Default, OSPFv2)

      Process Scope: All processes from all VRFs

  - default-ospfv3-af-ipv6 (Default, OSPFv3-AF-IPv6)

      Process Scope: All processes from all VRFs

  - default-ospfv3-af-ipv4 (Default, OSPFv3-AF-IPv4)

      Process Scope: All processes from all VRFs

  - default-ospfv3 (Default, OSPFv3)

      Process Scope: All processes from all VRFs

User-configured Maintenance-Units:

  - campus-ospfv2 (Custom, OSPFv2)

Public

show maintenance-unit 73

Processes:

        - Process 1 (VRF: red)

        - Process 2 (VRF: red)
Display when no maintenance-units are configured:

switch# show maintenance-unit

No maintenance-units configured
Display when only user-configured maintenance-units exist for a protocol:

switch# show maintenance-unit bgp

Maintenance Units:

==================

User-configured Maintenance-Units:

  - campus-bgp (User-configured, BGP)

      Shutdown Delay Timer: 120 seconds (default)

      Neighbor Scope: All neighbors from all VRFs

REST API Example

Get all BGP maintenance-units (equivalent to show maintenance-unit bgp):

curl -X GET "/rest/latest/network/maintenance/feature_set_bgp"
Get all OSPF maintenance-units (equivalent to show maintenance-unit ospf):

curl -X GET "/rest/latest/network/maintenance/feature_set_ospf"
Get specific BGP maintenance-unit details:

curl -X GET "/rest/latest/network/maintenance/feature_set_bgp/campus-bgp"
Get specific OSPF maintenance-unit details:

curl -X GET "/rest/latest/network/maintenance/feature_set_ospf/campus-

ospfv2"

NOTE

The response includes origin field to distinguish built-in from configured profiles:

Table 1.
Origin field

built-in

configuration

maintenance-unit

Default maintenance-unit

User-configured maintenance-unit

Public

show maintenance-unit 74

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

8400

9300

9300-32D

10000

shutdown-delay-timer <SECONDS>

Syntax

[no] shutdown-delay-timer <SECONDS>

Description

Configures the BGP shutdown delay timer within a BGP maintenance-unit. This timer controls the delay
between GSHUT community advertisement and actual BGP neighbor session shutdown during maintenance
mode activation. The timer allows BGP peers sufficient time to reconverge and select alternate paths before
sessions are brought down. the default value is 120 seconds.

Timer Behavior: When maintenance mode is activated, BGP first advertises the GSHUT community
(65535:0) with all routes. After the configured shutdown-delay-timer expires, BGP neighbor sessions
are gracefully brought down. This two-phase approach minimizes traffic disruption by allowing peers to
preemptively select alternate paths before session teardown.

Public

shutdown-delay-timer <SECONDS> 75

Timer Range: The shutdown-delay-timer can be configured from 0 to 3600 seconds (1 hour). A value of
0 causes immediate session shutdown without delay after GSHUT community advertisement. Higher values
provide more time for network reconvergence but extend the maintenance mode activation duration.

Scope: The shutdown-delay-timer applies to all BGP neighbors configured within the same BGP
maintenance-unit. Different maintenance-units can have different shutdown-delay-timer values for different
maintenance scenarios.

The no form resets the timer to the default value of 120 seconds. This provides granular control without
deleting the entire BGP maintenance-unit.

Parameter

<SECONDS>

Examples

Description

Delay in seconds.

Range: 0-3600

Default: 120

Required

Configuring BGP shutdown-delay-timer to 180 seconds with specific neighbors:

switch(config)# maintenance-unit bgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# shutdown-delay-timer 180

switch(config-maintenance-unit-bgp-campus-bgp)# neighbor 10.1.1.1 vrf red
Configuring BGP shutdown-delay-timer to default 120 seconds with all neighbors:

switch(config)# maintenance-unitbgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# shutdown-delay-timer 120

switch(config-maintenance-unit-bgp-campus-bgp)# all-neighbor
Configuring BGP with custom timer and neighbors:

switch(config)# maintenance-unitbgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# shutdown-delay-timer 300
switch(config-maintenance-unit-bgp-campus-bgp)# neighbor 10.1.1.1 vrf red

switch(config-maintenance-unit-bgp-campus-bgp)# neighbor 10.1.1.2 vrf red
Configuring immediate BGP shutdown (0 second delay)

switch(config)# maintenance-unit bgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# shutdown-delay-timer 0

switch(config-maintenance-unit-bgp-campus-bgp)# all-neighbor
Resetting BGP shutdown-delay-timer to default:

switch(config)# maintenance-unit bgp campus-bgp

switch(config-maintenance-unit-bgp-campus-bgp)# no shutdown-delay-timer

Public

shutdown-delay-timer <SECONDS> 76

REST API Examples

Configuring BGP shutdown-delay-timer to 180 seconds with specific neighbors:

curl -X PATCH "/rest/latest/system/feature_set_bgps/campus-bgp" \

  -H "Content-Type: application/json" \

  -d '{"shutdown_delay_timer": 180}'
Configuring BGP shutdown-delay-timer to default 120 seconds with all neighbors:

curl -X PATCH "/rest/latest/system/feature_set_bgps/campus-bgp" \

  -H "Content-Type: application/json" \

  -d '{"shutdown_delay_timer": 120}'
Configuring BGP with custom timer:

curl -X PATCH "/rest/latest/system/feature_set_bgps/campus-bgp" \

  -H "Content-Type: application/json" \

  -d '{"shutdown_delay_timer": 300}'
Resetting BGP shutdown-delay-timer to default:

curl -X PATCH "/rest/latest/system/feature_set_bgps/campus-bgp" \

  -H "Content-Type: application/json" \

  -d '{"shutdown_delay_timer": 120}'

Release

10.18

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

config

config-feature-set-bgp-c
ampus-bgp

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

8325

8325H

8360

8400

9300

9300-32D

Public

shutdown-delay-timer <SECONDS> 77

Platforms

Command context

Authority

10000

Support and other resources

Subtopics

Accessing Hewlett Packard Enterprise Support
HPE product registration
Accessing updates
Remote support
Warranty information
Regulatory information
Documentation feedback

Accessing Hewlett Packard Enterprise Support

•  For live assistance, go to the Contact Hewlett Packard Enterprise Worldwide website:

https://www.hpe.com/info/assistance

•  To access documentation and support services, go to the Hewlett Packard Enterprise Support Center

website:

https://www.hpe.com/support/hpesc

Information to collect

•  Technical support registration number (if applicable)

•  Product name, model or version, and serial number

•  Operating system name and version

•  Firmware version

•  Error messages

•  Product-specific reports and logs

•  Add-on products or components

Public

Support and other resources 78

•  Third-party products or components

HPE product registration

To gain the full benefits of the Hewlett Packard Enterprise Support Center and your purchased support
services, add your contracts and products to your account on the HPESC.

•  When you add your contracts and products, you receive enhanced personalization, workspace alerts,

insights through the dashboards, and easier management of your environment.

•  You will also receive recommendations and tailored product knowledge to self-solve any issues, as well

as streamlined case creation for faster time to resolution when you must create a case.

To learn how to add your contracts and products, see https://www.hpe.com/info/add-products-contracts.

Accessing updates

•  Some software products provide a mechanism for accessing software updates through the product

interface. Review your product documentation to identify the recommended software update method.

•  To download product updates:

Hewlett Packard Enterprise Support Center

https://www.hpe.com/support/hpesc

My HPE Software Center

https://www.hpe.com/software/hpesoftwarecenter

•  To subscribe to eNewsletters and alerts:

https://www.hpe.com/support/e-updates

•  To view and update your entitlements, and to link your contracts and warranties with your profile, go to

the Hewlett Packard Enterprise Support Center More Information on Access to Support Materials page:

Public

HPE product registration 79

https://www.hpe.com/support/AccessToSupportMaterials

IMPORTANT

Access to some updates might require product entitlement when accessed
through the Hewlett Packard Enterprise Support Center. You must have an HPE
Account set up with relevant entitlements.

Remote support

Remote support is available with supported devices as part of your warranty or contractual support
agreement. It provides intelligent event diagnosis, and automatic, secure submission of hardware event
notifications to Hewlett Packard Enterprise, which initiates a fast and accurate resolution based on the
service level of your product. Hewlett Packard Enterprise strongly recommends that you register your device
for remote support.

If your product includes additional remote support details, use search to locate that information.

HPE Get Connected

https://www.hpe.com/services/getconnected

HPE Tech Care Service

https://www.hpe.com/services/techcare

HPE Complete Care Service

https://www.hpe.com/services/completecare

Warranty information

To view the warranty information for your product, see the warranty check tool.

Regulatory information

To view the regulatory information for your product, view the Safety and Compliance Information for Server,
Storage, Power, Networking, and Rack Products, available at the Hewlett Packard Enterprise Support Center:

Public

Remote support 80

https://www.hpe.com/support/Safety-Compliance-EnterpriseProducts

Additional regulatory information

Hewlett Packard Enterprise is committed to providing our customers with information about the chemical
substances in our products as needed to comply with legal requirements such as REACH (Regulation EC No
1907/2006 of the European Parliament and the Council). A chemical information report for this product can
be found at:

https://www.hpe.com/info/reach

For Hewlett Packard Enterprise product environmental and safety information and compliance data,
including RoHS and REACH, see:

https://www.hpe.com/info/ecodata

For Hewlett Packard Enterprise environmental information, including company programs, product recycling,
and energy efficiency, see:

https://www.hpe.com/info/environment

Documentation feedback

Hewlett Packard Enterprise is committed to providing documentation that meets your needs. To help us
improve the documentation, click the Feedback button on the page of an opened document on the Hewlett
Packard Enterprise Support Center portal (https://www.hpe.com/support/hpesc). Use this feature to send
any errors, suggestions, or comments. This process captures all document information.

Public

Documentation feedback 81