| AOS-CX |       | 10.16.xxxx |       |       | Feature |        |
| ------ | ----- | ---------- | ----- | ----- | ------- | ------ |
| Pack   |       | Deployment |       |       | Guide   |        |
| 5420,  | 6300, | 6400,      | 8xxx, | 93xx, | 100xx   | Switch |
Series
Published:August2025
Version:1

Copyright Information

© Copyright 2025 Hewlett Packard Enterprise Development LP.

This product includes code licensed under certain open source licenses which require source
compliance. The corresponding source for these components is available upon request. This
offer is valid to anyone in receipt of this information and shall expire three years following the
date of the final distribution of this product version by Hewlett Packard Enterprise Company. To
obtain such source code, please check if the code is available in the HPE Software Center at
https://myenterpriselicense.hpe.com/cwp-ui/software but, if not, send a written request for
specific software version and product for which you want the open source code. Along with the
request, please send a check or money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company
Attn: General Counsel
WW Corporate Headquarters
1701 E Mossy Oaks Rd Spring, TX 77389
United States of America.

Notices

The information contained herein is subject to change without notice. The only warranties for
Hewlett Packard Enterprise products and services are set forth in the express warranty
statements accompanying such products and services. Nothing herein should be construed as
constituting an additional warranty. Hewlett Packard Enterprise shall not be liable for technical or
editorial errors or omissions contained herein.

Confidential computer software. Valid license from Hewlett Packard Enterprise required for
possession, use, or copying. Consistent with FAR 12.211 and 12.212, Commercial Computer
Software, Computer Software Documentation, and Technical Data for Commercial Items are
licensed to the U.S. Government under vendor's standard commercial license.

Links to third-party websites take you outside the Hewlett Packard Enterprise website. Hewlett
Packard Enterprise has no control over and is not responsible for information outside the Hewlett
Packard Enterprise website.

Contents
| About                                                   | this document     |     |              |     |       |               |     | 6   |
| ------------------------------------------------------- | ----------------- | --- | ------------ | --- | ----- | ------------- | --- | --- |
| Applicableproducts                                      |                   |     |              |     |       |               |     | 6   |
| Latestversionavailableonline                            |                   |     |              |     |       |               |     | 6   |
| Commandsyntaxnotationconventions                        |                   |     |              |     |       |               |     | 6   |
| Abouttheexamples                                        |                   |     |              |     |       |               |     | 7   |
| HPE Aruba                                               | Networking        |     | CX Feature   |     | Pack  | Overview      |     | 9   |
| AOS-CXFeaturePackTypesandSupportedFeatures              |                   |     |              |     |       |               |     | 9   |
| FeaturePackModes                                        |                   |     |              |     |       |               |     | 11  |
|                                                         | Cloud-ManagedMode |     |              |     |       |               |     | 11  |
|                                                         | File-BasedMode    |     |              |     |       |               |     | 11  |
|                                                         | Honormode         |     |              |     |       |               |     | 12  |
| EvaluationvsSubscriptionFeaturePackKeys                 |                   |     |              |     |       |               |     | 12  |
| BestPracticesandLimitations                             |                   |     |              |     |       |               |     | 12  |
| Viewing                                                 | and Managing      |     | Subscription |     | Pools |               |     | 14  |
| ViewingFeaturePackSubscriptionPoolsandFeaturePackOrders |                   |     |              |     |       |               |     | 14  |
| AddingaSubscriptionPool                                 |                   |     |              |     |       |               |     | 16  |
| RenamingaSubscriptionPool                               |                   |     |              |     |       |               |     | 17  |
| DeletingaSubscriptionPool                               |                   |     |              |     |       |               |     | 17  |
| MovingaSubscriptionBlocktoaNewSubscriptionPool          |                   |     |              |     |       |               |     | 17  |
| AddingorEditingaSubscriptionBlockName                   |                   |     |              |     |       |               |     | 18  |
| Viewing                                                 | and Managing      |     | Feature      |     | Pack  | Subscriptions |     | 19  |
| ActivatingaTermFeaturePackSubscription                  |                   |     |              |     |       |               |     | 19  |
ActivatingaPerpetualFeaturePackSubscriptionfor10000or10040Switches 20
| MonitoringFeaturePackSubscriptions              |     |         |      |     |       |     |           | 21  |
| ----------------------------------------------- | --- | ------- | ---- | --- | ----- | --- | --------- | --- |
| RevokingaFeaturePackSubscription                |     |         |      |     |       |     |           | 22  |
| TransferFeaturePackSubscriptionsBetweenAccounts |     |         |      |     |       |     |           | 23  |
| Cloud-Managed                                   |     | Feature | Pack | Use | Cases | and | Workflows | 26  |
DeployingaCloud-managedFeaturePackSolutiononaStandaloneSwitch 26
RevokingandReinstallingaFeaturePackSubscriptiononaStandaloneSwitch 28
| DeployingaCloud-ManagedFeaturePackSolutiononaVSF Stack |     |     |     |     |     |     |     | 28  |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
ReplacingaVSFStackMemberUsingaCloud-ManagedFeaturePackSubscription 30
| File-based | Feature | Pack | Use | Cases | and | Workflows |     | 33  |
| ---------- | ------- | ---- | --- | ----- | --- | --------- | --- | --- |
DeployingaFile-BasedFeaturePackSolutiononaStandaloneSwitch 33
| SettingaFile-BasedSwitchtoHonorMode                |     |     |     |     |     |     |     | 36  |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| DeployingaFile-BasedFeaturePackSolutiononaVSFStack |     |     |     |     |     |     |     | 37  |
ReplacingaVSFStackMemberUsingaFile-BasedFeaturePacksubscription 40
ReplacingaVSFStackConductorUsingaFile-BasedFeaturePacksubscription 43
| Viewing           | Feature | Packs    | on  | Switches | Managed |     | by Central | 47  |
| ----------------- | ------- | -------- | --- | -------- | ------- | --- | ---------- | --- |
| Feature           | pack    | commands |     |          |         |     |            | 48  |
| erasefeature-pack |         |          |     |          |         |     |            | 48  |
| feature-packmode  |         |          |     |          |         |     |            | 49  |
4
AOS-CX10.16FeaturePackDeploymentGuide| (5420,6300,6400,8xxx,93xx,100xxSwitchSeries)

| feature-packserver                  |                                      |           |             | 51  |
| ----------------------------------- | ------------------------------------ | --------- | ----------- | --- |
| feature-packvalidate                |                                      |           |             | 53  |
| showfeature-pack                    |                                      |           |             | 53  |
| Frequently                          | Asked                                | Questions | (FAQs)      | 58  |
| GeneralFeaturePackFAQs              |                                      |           |             | 58  |
| AdvancedFeaturePackFAQs             |                                      |           |             | 59  |
| 10000SwitchSeriesFeaturePackFAQs    |                                      |           |             | 60  |
| SubscriptionManagementFAQs          |                                      |           |             | 61  |
| FeaturePackDomain/SubaccountFAQs    |                                      |           |             | 61  |
| FeaturePackRevocationFAQs           |                                      |           |             | 61  |
| FeaturePackExpirationandRenewalFAQs |                                      |           |             | 61  |
| VSFandVSXFAQs                       |                                      |           |             | 62  |
| Troubleshooting                     |                                      | Feature   | Pack Issues | 63  |
| HowdoIknowthereisafeaturepackissue? |                                      |           |             | 63  |
|                                     | WarningLogsfromSubscriptionFeatures  |           |             | 63  |
|                                     | Feature-PackShowCommands             |           |             | 63  |
| ReasonsforFeaturePackIssues         |                                      |           |             | 63  |
|                                     | Featureisblockedbymissingfeaturepack |           |             | 63  |
TheSwitchisOutofSyncwiththeHPEArubaNetworkingSupportPortal 64
HPEArubaNetworkingSupportPortalaccountislockedafterchangingthepassword64
|     | MissingFeaturePackProfileFields |     |     | 65  |
| --- | ------------------------------- | --- | --- | --- |
ConnectionFailuretotheHPEArubaNetworkingFeaturePackSupportPortalServer 65
|                                    | ModeMismatch                              |           |     | 66  |
| ---------------------------------- | ----------------------------------------- | --------- | --- | --- |
|                                    | InvalidBlock                              |           |     | 67  |
|                                    | NotEnoughFeaturePacks                     |           |     | 67  |
|                                    | FeaturePackAlreadyAssigned                |           |     | 68  |
|                                    | FeaturePackRevoked                        |           |     | 68  |
|                                    | FeaturePackRemoved                        |           |     | 69  |
|                                    | Serial/MACmismatch                        |           |     | 69  |
|                                    | ArubaCentralDisconnected                  |           |     | 70  |
|                                    | SomeFeaturesareAllowedbutOthersareBlocked |           |     | 70  |
|                                    | FeaturesareBlockedafterZeroization        |           |     | 71  |
| Feature                            | Pack events                               |           |     | 72  |
| FeaturePackAgentevents             |                                           |           |     | 76  |
| QueueMonitoringevents              |                                           |           |     | 77  |
| Support                            | and Other                                 | Resources |     | 79  |
| AccessingHPEArubaNetworkingSupport |                                           |           |     | 79  |
|5

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing HPE Aruba Networking switches on
a network.

Applicable products

This document applies to the following products:

n HPE Aruba Networking 5420 Switch Series (S0U67A, S0U55A, S0U63A, S0U64A, S0U65A, S0U75A,

S0U72A, S0U78A, S0U58A, S0U73A, S0U74A, S0U71A, S0U76A, S0U70A, S0U77A, S0U60A, S0U61A,
S0U62A, S0U66A, S0U68A)

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

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

6

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

{ }

[ ]

… or

...

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

About this document | 7

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

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

8

HPE Aruba Networking CX Feature Pack

Chapter 2

HPE Aruba Networking CX Feature Pack Overview

AOS-CX 6300, 6400, 8xxx, 9300, and 10000 Switch series running AOS-CX 10.13 or later support optional
add-on feature packs that enhance the base AOS-CX operating system and allow users to activate and
manage advanced features on the switches through a subscription. Depending upon the requirements
for their networks, network administrators may choose to purchase a subscription for these features
that provide enhanced traffic visibility and troubleshooting, and support advanced security.

This section includes the following information about HPE Aruba Networking CX feature packs.

n AOS-CX Feature Pack Types and Supported Features

n Feature Pack Modes

n Evaluation vs Subscription Feature Pack Keys

n Best Practices and Limitations

AOS-CX Feature Pack Types and Supported Features

The AOS-CX software preinstalled on all HPE Aruba Networking CX switches includes an active, perpetual
set of AOS-CX native enterprise features at no additional cost. The AOS-CX native enterprise features
include everything needed to deploy, connect, and troubleshoot an enterprise network. For those
networks that require enhanced visibility and assurance, the HPE Aruba Networking CX Advanced
feature pack enables Edge Insights for AOS-CX 6300 and 6400 Switch series, offering application-based
policies, from OSI Layer 2 to Layer 7. The HPE Aruba Networking CX Advanced feature pack for 5420
switches supports application-based policies, and the HPE Aruba Networking CX Advanced feature pack
for 8xxx, 9xxx and 10040 switches includes the ability to Host HPE certified applications for flexible and
reliable IT services. The HPE Aruba Networking CX premium feature pack is supported on 10000 Switch
Series only, and enables scalable Network Address Translation (NAT) and IPSec VPN services.

For networks managed by HPE Aruba Networking Central, the HPE Aruba Networking Central Advanced license

enables all features supported by the CX Advanced feature pack, so no additional purchase of an CX Advanced

feature pack is necessary. For more information on HPE Aruba Networking Central licensing, see the HPE Aruba

Networking Central SaaS Subscription Ordering Guide.

The following table describes the features supported by the different types of HPE Aruba Networking
feature packs.

Table 1: Features Supported by Each Feature Pack Type

Feature Pack Type

Availability

Supported Features

AOS-CX native
enterprise features

Automatically
included with AOS-
CX switch hardware)

While switch software features will vary per product
family, the following are generally included in the AOS-
CX native enterprise features:

switch series)

n Multiprotocol Label Switching (MPLS) (6400, 8360

Switch Series)

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

9

Feature Pack Type

Availability

Supported Features

n Basic and advanced routing, including static routes,

Routing Information Protocol (RIPv2 and RIPng),

Open Shortest Path First (OSPFv2 and OSPFv3),

Border Gateway Protocol (BGP), and IS-IS

n Protocol Independent Multicast (PIMv4, PIMv6)
n Software-Defined Environments: VXLAN, User-

Based Tunneling (UBT)

n IP Flow Information Export (IPFIX)
n Precision Time Protocol (PTP), Transparent Clocks

(TCs), and Boundary Clocks (BCs)

n High Availability, including In-Service Software

Upgrades (ISSU) and hot patching

n Full layer-2 support, including STP, VLANs, and

IGMP

n Network Analytics Engine (NAE)
n Layer-2 MACsec Security (6300, 8360 Switch series

n Application-based policies

n Application-based policies
n Reflexive policies for port access GBP clients
n Reflexive policies for port access policy clients
n MACsec extensions for the WAN
n Drop Exceptions

n Application-based policies
n Reflexive policies for port access GBP clients
n Reflexive policies for port access policy clients
n MACsec extensions for the WAN

n Host HPE certified applications for flexible and

reliable IT services**

n MACsec extensions for the WAN (8360, 9300S

Switch series only)

n Queue Statistics Monitoring (8325, 8325H and 9xxx

Switch series only)

n Inband Flow Analyzer and Flow Telemetry (9xxx

Switch series only)

n Queue Congestion Monitoring (8325, 8325H and

8325P Switch series only)

HPE Aruba Networking CX Feature Pack Overview | 10

AOS-CX 5420 Switch
advanced feature pack

AOS-CX 6300 Switch
advanced feature pack

AOS-CX 6400 Switch
advanced feature pack

AOS-CX 8xxx/9xxx
Switch advanced
feature pack

Subscription:
1 year
3 year
5 year
7 year
10 year
90-day eval

Subscription:
1 year
3 year
5 year
7 year
10 year
90-day eval

Subscription:
1 year
3 year
5 year
7 year
10 year
90-day eval

Subscription:
1 year
3 year
5 year
7 year
10 year
90-day eval

Feature Pack Type

Availability

Supported Features

AOS-CX 10040 Switch
advanced feature pack

AOS-CX10000 Switch
advanced feature pack

Aruba 10000 Switch
premium feature pack

Subscription:
1 year
3 year
5 year
7 year
10 year
90-day eval

Subscription:
1 year
3 year
5 year
90-day eval
perpetual

1 year
3 year
5 year
90-day eval
perpetual

n Drop Exceptions (8325, 8325H and 8325P Switch

series only)

n Host HPE certified applications for flexible and

reliable IT services**

n MACsec extensions for the WAN

n Host HPE certified applications for flexible and

reliable IT services**

n Accelerated stateful firewall for east-west traffic
n Firewall logging and per-packet IPFIX telemetry

streaming

n Queue Statistics Monitoring

n All features included in the AOS-CX10000 Switch

advanced feature pack

n IPSec VPN services
n Scalable NAT, including stateful NAT for dual-stack

IPv4/IPv6 deployments
n Advanced DDoS protection

** AOS-CX does not enforce the requirement to own a feature pack prior to using the container feature to host HPE certified

applications.

Feature Pack Modes

CX Advanced and Premium feature packs can be managed in either cloud-managed mode, file-based
mode, or honor mode.

Cloud-Managed Mode

The centralized management of HPE Aruba Networking CX Advanced and Premium feature packs allows
a group of switches using feature pack subscriptions in cloud-managed mode to share a pool of one or
more feature pack subscriptions managed through the HPE Aruba Networking support portal. By
default, a switch using a CX feature pack in cloud mode will contact the HPE Aruba Networking support
portal once a day to automatically synchronize with the feature pack subscription management
database.

When you use a cloud-managed deployment type, the HPE Aruba Networking support site can
automatically distribute and manage feature pack subscriptions for all devices in a group, making it a
scalable solution for larger deployments and for global accounts across geographies.

File-Based Mode

Networks with a single switch or with multiple switches on isolated networks that cannot contact the
HPE Aruba Networking support site can use feature pack subscription keys in file-based mode, where a
feature pack is manually enabled on a switch using a non-sharable subscription key file tied to that
individual switch's serial number or MAC address. When a switch upgrades to 10.13.0001, existing

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

11

features that require feature packs in 10.13 will remain operational in honor mode, even if that feature
is not yet part of a feature pack. File-based mode is the default operation mode of feature pack
management for AOS-CX switches.

Honor mode

Honor mode is intended for cases where a valid feature pack for advanced features has been
purchased, but is not yet installed on the device. Advanced features on this device will be operational in
Honor mode, but a warning message may be seen until a valid feature pack is installed.

HPE Aruba Networking may remove support for honor mode in a future release. If support for honor mode is

removed, advanced features will only be operational if the applicable subscription fees are paid and a valid

feature pack is installed

Evaluation vs Subscription Feature Pack Keys

Each Aruba CX Advanced or Aruba CX Premium feature pack key is available as either a 90-day
evaluation subscription or a standard subscription that is valid for a term from 1-10 years. An evaluation
feature pack allows you to evaluate the functionality of a software feature pack for a period of 90 days.
Evaluation and standard subscription feature packs can added to and made sharable within a
subscription pool.

Feature pack subscription keys cannot be renewed. Once a feature pack subscription key expires, a new
feature pack subscription key must be generated and installed on the switch. To determine the
remaining time on an evaluation feature pack, issue the show feature-pack command in the switch
command-line interface. An expired feature pack will remain on the switch until it is removed using the
command erase feature-pack.

For more information on obtaining an evaluation subscription key, contact your authorized HPE Aruba
Networking reseller.

Best Practices and Limitations

The following best practices and limitations apply to Aruba CX Advanced and Premium feature pack
subscription keys.

n A single user account in the HPE Aruba Networking support portal can manage Aruba CX advanced

and premium feature packs in cloud mode (supporting cloud-managed mode on the AOS-CX switch)
or local mode (supporting file-based mode on the AOS-CX switch), but not in both modes
simultaneously. If your global deployment must support both file-based and cloud-managed feature
pack subscriptions, you must manage these subscription types separately using two different user
accounts.

n Feature pack keys in cloud mode can only be associated to a switch via the HPE Aruba Networking

support portal. Cloud-managed feature pack keys cannot be added directly to a switch via the switch
CLI.

n Multi-Factor Authentication (MFA) is supported on HPE user accounts and MFA is compatible with all

feature pack modes and management methods. MFA is both supported and recommended.

n 6300, 6400, 8xxx, and 9300 Switch series managed via HPE Aruba Networking Central and using an
HPE Aruba Networking Central Advanced license do not need HPE Aruba Networking CX Advanced
feature packs, as the HPE Aruba Networking Central Advanced license automatically enables all
advanced feature pack features on that switch. However, 10000 Switch series managed with an HPE

HPE Aruba Networking CX Feature Pack Overview | 12

Aruba Networking Central Advanced subscription does require a HPE Aruba Networking CX
Advanced Feature Pack when ordering the switch. For more information on HPE Aruba Networking
Central licenses, refer to the HPE Aruba Networking Central online help.

n When allocating feature pack subscriptions for a VSF stack, best practices is to keep subscriptions for

all members in dedicated subscription block.

n Subscriptions blocks cannot be split after activation. Consider creating subscription blocks with a

smaller number of subscriptions, as this provides greater flexibility in managing subscription blocks
and moving them across subscription pools.

n Rebooting the switch or removing a cloud-based feature pack subscription profile does not affect its

existing feature pack subscription. However, issuing the erase all zeroize command resets the
device to a factory default state and deletes all local or cloud-managed feature packs. If you reset a
switch to its factory default state, you must reinstall the previously-installed file-based feature pack.
To reinstall a cloud feature pack after zeroizing the switch, the former feature pack needs to be
revoked in the HPE Aruba Networking support portal, and the feature pack profile on the switch
needs to be re-configured to connect to the support portal.

n Tampering with a downloaded feature pack file in local mode will cause installation failure.

n If there is a possibility that a device may be added to a VSF stack sometime in future, consider

maintaining a buffer of additional feature pack subscriptions when creating a block.

n Setting the clock to past the expiration date will cause it to become expired.

n A file-based feature pack can be revoked and re-used on a different switch a limited number of times.
if this the limit has been exceeded, contact HPE Aruba Networking technical support for assistance in
revoking the feature pack.

CX feature pack management provides the ability to move a feature-pack from one switch to another, for

maximum flexibility in managing an organization’s network and to minimize an RMA impact. HPE Aruba

networking monitors and detects feature pack fraud. Abnormally high volumes of feature pack transfers for the
same feature pack subscription to multiple devices can indicate a breach of the HPE Aruba Networking end user

software license agreement and will be investigated.

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

13

Viewing and Managing Subscription

Chapter 3

Viewing and Managing Subscription Pools

Feature packs can be grouped into one or more feature pack subscription pools on the HPE Aruba
networking support portal. You can manage all of your feature pack orders using the single pre-existing
Default pool, but best practices is to create separate pools for different feature pack types or network
segments according to your feature pack deployment strategy. It is helpful to name pools in a standard
pattern for easy recognition, for example, by floors, buildings or departments.

The subscriptions in each pool are further grouped into individual subscription blocks, which are
comprised of a single type of subscription from a single order.

Each user account with the HPE Aruba Networking support portal can manage CX feature packs in cloud mode or

in local (file-based) mode, but not in both modes simultaneously. When you first access your CX feature pack

pools, you are asked if you want to manage feature packs in either Cloud mode or Local mode. Choose carefully,

as you will not be able to change your management mode. If you want to manage feature packs in both cloud-

managed and file-based modes, you must use two separate HPE Aruba Networking support accounts, one for

each mode. For more information on feature pack modes, see Feature Pack Modes

This section describes the following workflows:

n Viewing Feature Pack Subscription Pools and Feature Pack Orders

n Adding a Subscription Pool

n Viewing and Managing Subscription Pools

n Deleting a Subscription Pool

n Renaming a Subscription Pool

n Adding or Editing a Subscription Block Name

Viewing Feature Pack Subscription Pools and Feature Pack
Orders

The Orders page on the HPE Aruba Networking support portal displays your HPE Aruba Networking CX
subscription pools and information about all feature pack orders. To view your feature pack orders and
subscription pools:

1. Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking

support user name and password.

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

14

2. From the License Management page, select View Order.

Figure 1 Viewing Current Orders on the HPE Aruba Networking Support Portal

3. Select the AOS-CX Feature Pack tab at the top of the Orders page to display the Default

feature pack pool, and any user-created pools.

Figure 2 Viewing Aruba CX Feature Pack Orders

4. The first time you view this page, you will be prompted to select either local or cloud mode for

your CX feature pack management mode. Once selected, this mode cannot be changed, and will
display at the top of the Orders page.

Figure 3 CX feature pack management mode

The Orders page also displays the following information about the subscription orders in each
subscription pool.

n Order number

n Subscription key

Viewing and Managing Subscription Pools | 15

| n   | Blockname(optional)       |     |
| --- | ------------------------- | --- |
| n   | Subscriptiontermstartdate |     |
Subscriptiontermenddate
n
| n   | Subscriptionpackpartnumberdescription                      |     |
| --- | ---------------------------------------------------------- | --- |
| n   | Orderquantity(totalnumberofsubscriptionsinthefeatureblock) |     |
n Availablequantity(numberofsubscriptionsinthatfeatureblockthatarenotyetused)
| Figure4 | OrdersPageShowingCXFeaturePacks |      |
| ------- | ------------------------------- | ---- |
| Adding  | a Subscription                  | Pool |
AllnewfeaturepacksubscriptionordersautomaticallyappearintheDefaultsubscriptionpool.Youcan
createadditionalpoolstohelpyouidentifyandorganizeindividualsubscriptionsblocks.
Subscriptionsblockscannotbesplitafteractivation.Considercreatingsubscriptionblockswithasmallernumber
ofsubscriptions,asthisprovidesgreaterflexibilityinmanagingsubscriptionblocksandmovingthemacross
subscriptionpools.
Toaddanewsubscriptionpool:
1. NavigatetotheAOS-CXOrderspageasdescribedinViewingFeaturePackSubscriptionPoolsand
FeaturePackOrders.
| 2. Clickthe(+) | Add Subscription | Pooliconatthetopofthepage. |
| -------------- | ---------------- | -------------------------- |
3. Enteranameforthenewsubscriptionpool.
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 16

Figure 5 Adding a Subscription Pool

Renaming a Subscription Pool

You can assign a different name to any user-created subscription pool. The Default pool can not be
deleted.

1. Navigate to the AOS-CX Orders page as described in Viewing Feature Pack Subscription Pools and

Feature Pack Orders.

2. Click the green edit icon
3. Enter the new name for the pool, then click OK.

by the subscription pool you want to rename.

Deleting a Subscription Pool

If you delete a user-created subscription pool, any subscription blocks in that pool are automatically
transferred back to the Default pool. The Default pool cannot be deleted.

A pool cannot be deleted if switches are using feature pack subscriptions in that pool. All the feature
packs need to be revoked before the pool can be deleted. The switch can then be assigned feature
packs from a new pool.

For more information on revoking a feature pack subscription, see Revoking a Feature Pack Subscription

1. Navigate to the Aruba CX Orders page as described in Viewing Feature Pack Subscription Pools

and Feature Pack Orders.

2. Click the red delete icon

by the subscription pool you want to delete. A dialog box opens and

asks you to confirm that you want to delete that pool.

3. Click OK.

Moving a Subscription Block to a New Subscription Pool

To move a subscription block to a different subscription pool:

1. Navigate to the Aruba CX Orders page as described in Viewing Feature Pack Subscription Pools

and Feature Pack Orders.

Viewing and Managing Subscription Pools | 17

2. Clickthegreenactionsicon bythesubscriptionblocktobemoved,andselectMove.Adialog
boxopensthatallowsyoutoselectanewsubscriptionpoolforthatsubscriptionblock.
3. Selectthenewpoolforthesubscriptionblock,thenclickSubmit.
| Adding | or Editing | a Subscription | Block Name |
| ------ | ---------- | -------------- | ---------- |
Toaddorchangethenameofasubscriptionblock:
1. NavigatetotheAOS-CXOrderspageasdescribedinViewingFeaturePackSubscriptionPoolsand
FeaturePackOrders.
2. Clickinthe Block Namecolumnforanyordertoaddoreditablockname.
| Figure6 | EditingaBlockName |     |     |
| ------- | ----------------- | --- | --- |
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 18

Viewing and Managing Feature Pack

Chapter 4

Viewing and Managing Feature Pack Subscriptions

This chaptertopic describes how to activate a feature pack so it can be used by an AOS-CX switch, view
and monitor purchased feature packs, revoke a feature pack subscription so it can be assigned to
another switch, and transfer feature packs between user accounts on the HPE Aruba Networking
support portal.

n Monitoring Feature Pack Subscriptions

n Activating a Term Feature Pack Subscription

n Revoking a Feature Pack Subscription

n Transfer Feature Pack Subscriptions Between Accounts

Activating a Term Feature Pack Subscription

When you activate an evaluation or 1-year to 10-year term subscription feature pack subscription for
6xxx, 8xxx, 9xxx or 10000 switches:

n The subscription term for that feature pack begins.

n That feature pack subscription can be assigned to an AOS-CX switch.

The feature block for that feature pack order updates to show that one less subscription is available only
after a feature pack is generated for a specific switch. For feature packs in file-based mode, this happens
after a user downloads an feature pack from the HPE Aruba Networking support portal. For feature
packs in cloud-managed mode, this happens happen after a switch contacts the support portal to
reserve a feature pack.

A feature pack does not appear on the Subscription Monitoring page until it is both activated and assigned to a

switch. The feature block for that feature pack order update to show that one less subscription is available.

To activate a feature pack subscription:

1. Navigate to the AOS-CX Orders page as described in Viewing Feature Pack Subscription Pools and

Feature Pack Orders.

2.

Identify the feature pack order with the subscription to be activated. Orders with unactivated
subscriptions appear in the Orders table highlighted in green.

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

19

Figure 1 AOS-CX Orders Page Showing Unactivated Subscriptions

3. Click the green actions icon

by the order with a subscription to be activated, then click

Activate. A dialog box opens and displays the number of available subscriptions within that
feature pack order block.

4. Enter the number of feature pack subscriptions you want to activate.

5.

(Optional) Enter the name of a feature block for the activated feature packs.

6. Click Submit. Each activated feature pack subscription is now available to be associated to an

AOS-CX switch. For details on associating a feature pack to a switch, see also Deploying a Cloud-
managed Feature Pack Solution on a Standalone Switch and Deploying a File-Based Feature Pack
Solution on a Standalone Switch.

Activating a Perpetual Feature Pack Subscription for 10000
or 10040 Switches

When you activate a perpetual feature pack subscription:

n The subscription term for that feature pack begins.

n That feature pack subscription can be assigned to an AOS-CX switch.

n Other feature packs within the feature pack block cannot be split into different blocks.

The feature block for that feature pack order updates to show that one less subscription is available
only after a feature pack is generated for a specific switch. For feature packs in file-based mode, this
happens after a user downloads an feature pack from the HPE Aruba Networking support portal. For
feature packs in cloud-managed mode, this happens happen after a switch contacts the support portal
to reserve a feature pack.

A feature pack does not appear on the Subscription Monitoring page until it is both activated and assigned to a

switch. The feature block for that feature pack order update to show that one less subscription is available.

To activate a feature pack subscription:

1. Navigate to the Aruba CX Orders page as described in Viewing Feature Pack Subscription Pools

and Feature Pack Orders.

Viewing and Managing Feature Pack Subscriptions | 20

2. Click the All Products tab.

3. Click the green button on the right side labeled "Register New"

Figure 1 Aruba CX Orders Page

4.

Input the order number and confirmation number received from the order management system
into the pop-up window, then click Register.

5. Now click the AOS-CX Feature Pack tab. The order will be activated in the Default subscription

pool.

The activated feature pack subscription is now available to be associated to a 10000 or 10040 Switch.
For details on associating a feature pack to a switch, see also Deploying a Cloud-managed Feature Pack
Solution on a Standalone Switch and Deploying a File-Based Feature Pack Solution on a Standalone
Switch.

Monitoring Feature Pack Subscriptions

The Subscription Monitoring page of the HPE Aruba Networking support portal allows you to review
CX feature pack subscriptions that have been associated to an AOS-CX switch.

To view feature pack subscriptions currently in use by an AOS-CX switch:

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

21

1. Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking

support user name and password.

2. From the License Management page, select the AOS-CX Feature Pack icon to open the

Subscription Monitoring page.

Figure 1 Viewing Active CX feature Pack subscriptions

The Subscription Monitoring dashboard displays information for each feature pack subscription:

n Order ID: The order ID number is also sent in an email at the time of the feature pack subscription

purchase.

n Host Name: The host name of the switch using the feature pack subscription.

n Serial Number: Serial number unique to that feature pack.

n MAC Address: MAC address of the switch using the feature pack subscription

n UUID: A Universally Unique Device Identifier (UUID) for the feature pack subscription.

n Feature Pack Pool: Pool containing the feature pack subscription. By default, all new orders appear in
the Default feature pack pool, but feature pack blocks can be moved to other pools if desired. For
more information, see also Viewing and Managing Subscription Pools

n Block Name: This field displays any block name assigned to the feature pack when it was activated.

n Activation date: The date that the subscription order was activated.

n Expiry date: Date that the subscription term expires.

You can sort the feature pack subscriptions table on this page by clicking on any column heading to sort
the list by that column criteria, or enter an order ID, host name, serial number, UUID, or feature pack
pool name into the search bar at the top of the page.

Revoking a Feature Pack Subscription

Viewing and Managing Feature Pack Subscriptions | 22

You can use the HPE Aruba Networking support site remove a feature pack subscription from a switch
managing feature packs in cloud mode, and reuse that feature pack on another switch of the same
model.

When you revoke a feature pack subscription on the HPE Aruba Networking support site:

n The feature pack subscription appears as available on the CX Orders page, indicating that it can be

reassigned.

n The feature block for that feature pack order will update to show that an additional subscription is

available.

n A switch in cloud-managed mode will synchronize with the HPE Aruba Networking support site and

will go into honor mode.

n A switch in file-based mode is not notified that the subscription has been revoked. Manually remove

the subscription from the switch using the erase feature-pack CLI command.

Each HPE Aruba Networking support feature pack account domain managing feature packs in file-based mode

can revoke a feature pack up to 50 times per domain. If is limit is exceeded, the user will not be able to revoke the

feature pack and the system will display an error message.

1. Navigate to the Subscription Monitoring page as described in Monitoring Feature Pack

Subscriptions.

2.

Identify the feature pack subscription to be revoked. For large feature pack deployments, you can
use the search bar at the top of this page to search for the switch MAC address, the feature pack
subscription serial number or the feature pack pool.

3. Select the feature pack to be revoked, click the green actions icon

and select Revoke.

Figure 1 Revoking a Feature Pack Used by a Switch

Transfer Feature Pack Subscriptions Between Accounts

You can use the HPE Aruba Networking Support portal to transfer any unused feature pack
subscriptions orders to another HPE Aruba Networking Support account.

Any transfer between accounts must move all subscriptions within that feature pack subscription block. A single

order with multiple feature pack subscriptions cannot be split between two accounts.

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

23

1. Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking

support user name and password.

2. From the License Management page, select Transfer to Account. The Transfer to Account

page opens.

3.Figure 1 Transferring Feature Pack Subscriptions Between Accounts

4. Enter the email address of the account that currently contains the feature pack subscriptions you

want to transfer, then select Get Accounts.

5. Select the account that contains the feature pack subscriptions you want to transfer, and click

Get Licenses.

6. Click the CX-Switch button to list all CX feature pack subscriptions available for transfer.

7. Select the feature pack subscriptions to transfer and click Next.

Figure 2 Selecting feature pack subscriptions to be transferred

8. You will be prompted to verify your selection. Click Next again.

9. Now, enter the email address associated with the HPE Aruba Networking Support account to

receive the feature pack subscriptions and click Get Accounts.

Viewing and Managing Feature Pack Subscriptions | 24

10. Use the Select Accounts drop-down menu to select the account that should receive the feature

pack subscriptions.

11.

In the Enter reason for transfer field, specify why the feature pack subscriptions are being
transferred.

12. Click Next to display the transfer summary page. Validate all the information about the transfer,

then click Submit.

Figure 3 Validating the Feature Pack Transfer

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

25

Cloud-Managed Feature Pack Use Cases

Chapter 5

Cloud-Managed Feature Pack Use Cases and Workflows

This chaptersection describes the following workflows for deployments using feature pack subscriptions
in cloud-managed mode.

n Deploying a Feature Pack Solution on a Standalone Switch

n Removing a Feature Pack Subscription from a Standalone Switch

n Deploying a Feature Pack Solution on a VSF stack Switch

n Replacing a VSF Stack Member Using a Cloud-Managed Feature Pack Subscription

Deploying a Cloud-managed Feature Pack Solution on a
Standalone Switch

The following section describes the procedure to install an HPE Aruba Networking CX advanced feature
pack on a single standalone AOS-CX switch using feature pack subscriptions in cloud-managed mode.

Prerequisites

n The user has created a user account on the HPE Aruba Networking support portal.

n The user has already ordered their feature pack subscriptions from HPE Aruba Networking reseller.

n The Orders page on the HPE Aruba Networking support portal has been updated to indicate that the
subscriptions for the user account will be manged in cloud-managed mode. For details, see Viewing
Feature Pack Subscription Pools and Feature Pack Orders.

Procedure

1. Log on to the switch command-line interface.

2. Enter the feature pack server configuration sub-mode.

switch(config)# feature-pack server

3. Configure the location URL of the HPE Aruba Networking feature pack management server in the

corresponding VRF

switch(config-feature-pack-server)# location https://cx-feature-
pack.arubanetworks.com vrf mgmt

4. Configure the switch with the account credentials for your HPE Aruba Networking support

account.

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

26

switch (config-feature-pack-server)# credentials user <username> password
| plaintext | <password> |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
5. Configurethesubscriptionblockandsubscriptionpool,thenexitthefeaturepackservercontext
| switch(config-feature-pack-server)# |     |     |     |     | block | 6300_test_block_2 |     |     |
| ----------------------------------- | --- | --- | --- | --- | ----- | ----------------- | --- | --- |
| switch(config-feature-pack-server)# |     |     |     |     | pool  | default           |     |     |
| switch(config-feature-pack-server)# |     |     |     |     | exit  |                   |     |     |
6. Specifythattheswitchwillmanagefeaturepacksincloud-managedmode.
| switch | (config)# | feature-pack |     | mode | cloud-managed |     |     |     |
| ------ | --------- | ------------ | --- | ---- | ------------- | --- | --- | --- |
7. (Optional)Oncethefeaturepackisinstalledinthedevice,theshow feature-pack serverand
show feature-packcommandscanbeusedtoverifytheLMSconnectivityandfeaturepack
subscriptionstatus.
| switch# | show | feature-pack | server |     |     |     |     |     |
| ------- | ---- | ------------ | ------ | --- | --- | --- | --- | --- |
Profile
=======
| Location     | URL |       | : https://cx-feature-pack.arubanetworks.com |     |     |     |     |     |
| ------------ | --- | ----- | ------------------------------------------- | --- | --- | --- | --- | --- |
| Location     | VRF |       | : mgmt                                      |     |     |     |     |     |
| User account |     |       | : customer@example.com                      |     |     |     |     |     |
| Subscription |     | Pool  | : default                                   |     |     |     |     |     |
| Subscription |     | Block | : 6300_test_block_2                         |     |     |     |     |     |
Connection
==========
| Status          |            |              | : Validation |     | success     |     |          |     |
| --------------- | ---------- | ------------ | ------------ | --- | ----------- | --- | -------- | --- |
| Reason          |            |              | : --         |     |             |     |          |     |
| Last validation |            | time         | : Tue        | Sep | 12 09:27:42 |     | UTC 2023 |     |
| Success         | validation | time         | : Tue        | Sep | 12 09:27:42 |     | UTC 2023 |     |
| switch#         | show       | feature-pack |              |     |             |     |          |     |
| Feature         | Pack       | Summary      |              |     |             |     |          |     |
===============
| Name         |           | : CX                | Software | Advanced |           | Feature | Pack         |         |
| ------------ | --------- | ------------------- | -------- | -------- | --------- | ------- | ------------ | ------- |
| Expiration   | Date      | : Wed               | Aug      | 28 2024  |           |         |              |         |
| Serial       | Number(s) | : SG2ZL50166        |          |          |           |         |              |         |
| MAC Address  |           | : 18:7a:3b:1b:f6:40 |          |          |           |         |              |         |
| Hostname     |           | : 6300              |          |          |           |         |              |         |
| Mode         |           | : Cloud             | Managed  |          |           |         |              |         |
| State        |           | : Feature           |          | pack     | installed | and     | valid        |         |
| Error Reason |           | : none              |          |          |           |         |              |         |
|              |           |                     |          |          |           |         | Subscription | Feature |
| Feature      |           |                     |          |          |           |         | Status       | Status  |
---------------------------------------------------------------------
| Application | Based      | Policy |     |     |     |     | active | allowed |
| ----------- | ---------- | ------ | --- | --- | --- | --- | ------ | ------- |
| MACsec      | extensions | for    | WAN |     |     |     | active | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies | for | Port | Access | Clients |     | active | allowed |
| --------- | -------- | --- | ---- | ------ | ------- | --- | ------ | ------- |
Changing the password for your HPE Aruba Networking Support Portal account
Cloud-ManagedFeaturePackUseCasesandWorkflows|27

A network admin using feature packs in cloud mode may experience a lockout of their HPE account
after changing their password due to the switches syncing with the old password. When changing the
password of the user account credentials configured on switches for cloud-managed subscriptions, use
the following procedure to avoid unexpected account lockouts.

1. Configure all switches into file-mode using the command feature-pack mode file-based. This
will prevent the switches from syncing with the HPE Networking Support Portal during the
password change process.

Note: This will cause the switches to move into honor mode due to a mismatch between feature-pack type and

configured mode, but subscription features will remain operational.

2. Proceed with the password change on the HPE user account.

3. Configure the new password on each switch using the secure prompt or ciphertext options.

Using secure prompt:

switch (config-feature-pack-server)# credentials user <USER> password
<enter>”.

Using ciphertext :

switch (config-feature-pack-server)#
ciphertext <CIPHERTEXT>”

credentials user <USER> password

4. Configure each switch into cloud-managed mode using the command feature-pack mode

cloud-managed, then verify subscriptions are validated using show feature-pack server and
show feature-pack.

Revoking and Reinstalling a Feature Pack Subscription on a
Standalone Switch

Before you replace a standalone switch using a cloud-mode feature pack subscription, the feature pack
subscription needs to be revoked.

Procedure

1. Access the HPE Aruba Networking support portal and revoke the feature pack subscription from

the switch to be replaced. For details, see Revoking a Feature Pack Subscription

2. Once the replacement switch is installed on the network, use the feature-pack server

commands to reinstall the cloud-based feature pack on the new switch. For details, see Deploying
a Cloud-managed Feature Pack Solution on a Standalone Switch.

Deploying a Cloud-Managed Feature Pack Solution on a
VSF Stack

The following section describes the procedure to install an HPE Aruba Networking CX Advanced Feature
Pack on a VSF stack using feature pack subscriptions in cloud-managed mode.

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

28

Prerequisites

n The user has created a user account on the HPE Aruba Networking support portal.

n The user has already ordered their feature pack subscriptions from HPE Aruba Networking reseller.

n The HPE Aruba Networking support portal contains a subscription block activated with a number of

feature pack subscriptions equal to or greater than the number of devices in the VSF stack.

n The Orders page on the HPE Aruba Networking support portal has been updated to indicate that the
subscriptions for the user account will be managed in cloud-managed mode. For details, see Viewing
Feature Pack Subscription Pools and Feature Pack Orders.

Procedure

1. Log on to the switch command-line interface.

2. Enter the feature pack server configuration sub-mode.

switch(config)# feature-pack server

3. Configure the location URL of the feature pack management server in the corresponding VRF.

switch(config-feature-pack-server)# https://cx-feature-pack.arubanetworks.com vrf
mgmt

4. Configure the switch with the account credentials for your HPE Aruba Networking Support

account.

switch(config-feature-pack-server)#
plaintext <password>

credentials user <username> password

5. Configure the feature pack block and feature pack pool, then exit the feature pack server context.

switch(config-feature-pack-server)# block VSF_test
switch(config-feature-pack-server)# pool 6300_VSF
switch(config-feature-pack-server)# exit

6. Specify that the switch should manage feature packs in cloud-managed mode.

switch (config)#

feature-pack mode cloud-managed

7. Once the feature pack is installed in the device, the show feature-pack server and show
feature-pack commands can be used to verify the LMS connectivity and feature pack
subscription status. Note that the Serial Number(s) field in the output of the show feature-
pack command includes the serial numbers for all devices in the in the VSF stack.

switch# show feature-pack server
Profile
=======
Location URL

: https://cx-feature-pack.arubanetworks.com

Cloud-Managed Feature Pack Use Cases and Workflows | 29

| Location     | VRF |       | : mgmt                 |     |     |     |     |     |     |
| ------------ | --- | ----- | ---------------------- | --- | --- | --- | --- | --- | --- |
| User account |     |       | : customer@example.com |     |     |     |     |     |     |
| Subscription |     | Pool  | : 6300_VSF             |     |     |     |     |     |     |
| Subscription |     | Block | : VSF_test             |     |     |     |     |     |     |
Connection
==========
| Status          |              |         | :   | Validation | success     |     |          |     |     |
| --------------- | ------------ | ------- | --- | ---------- | ----------- | --- | -------- | --- | --- |
| Reason          |              |         | :   | --         |             |     |          |     |     |
| Last validation |              | time    | :   | Mon Sep    | 18 19:09:55 |     | UTC 2023 |     |     |
| Success         | validation   | time    | :   | Mon Sep    | 18 19:09:55 |     | UTC 2023 |     |     |
| 6300# show      | feature-pack |         |     |            |             |     |          |     |     |
| Feature         | Pack         | Summary |     |            |             |     |          |     |     |
===============
| Name         |           | : CX                | Software | Advanced   |           | feature    | pack         |     |         |
| ------------ | --------- | ------------------- | -------- | ---------- | --------- | ---------- | ------------ | --- | ------- |
| Expiration   | Date      | : Sat               | Sep      | 07 2024    |           |            |              |     |         |
| Serial       | Number(s) | : SG1ZL53061        |          | SG2ZL50131 |           | SG2ZL50145 |              |     |         |
| MAC Address  |           | : 18:7a:3b:1b:b6:c0 |          |            |           |            |              |     |         |
| Hostname     |           | : 6300              |          |            |           |            |              |     |         |
| Type         |           | : Floating          |          |            |           |            |              |     |         |
| Mode         |           | : Cloud             | Managed  |            |           |            |              |     |         |
| State        |           | : feature           |          | pack       | installed | and        | valid        |     |         |
| Error Reason |           | : none              |          |            |           |            |              |     |         |
|              |           |                     |          |            |           |            | Subscription |     | Feature |
| Feature      |           |                     |          |            |           |            | Status       |     | Status  |
---------------------------------------------------------------------
| Application | Based      | Policy |     |     |     |     | active |     | allowed |
| ----------- | ---------- | ------ | --- | --- | --- | --- | ------ | --- | ------- |
| MACsec      | extensions | for    | WAN |     |     |     | active |     | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies | for          | Port  | Access | Clients |     | active |                 | allowed |
| --------- | -------- | ------------ | ----- | ------ | ------- | --- | ------ | --------------- | ------- |
| Replacing | a        | VSF          | Stack | Member |         |     | Using  | a Cloud-Managed |         |
| Feature   | Pack     | Subscription |       |        |         |     |        |                 |         |
UsethefollowingworkflowtoreplaceaVSF stackmemberwithaswitchthatdoesnotyethavea
featurepacksubscription.
Procedure
1. Logontothecommand-lineinterfaceoftheVSFstackmember.
2. Verifythattheadvancedfeaturepackisbeingconsumedbyallswitchmembers.
switch#showfeature-pack
| Feature | Pack | Summary |     |     |     |     |     |     |     |
| ------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
===============
| Name         |           | : CX                | Software | Advanced   |           | Feature    | Pack         |     |         |
| ------------ | --------- | ------------------- | -------- | ---------- | --------- | ---------- | ------------ | --- | ------- |
| Expiration   | Date      | : Sat               | Sep      | 07 2024    |           |            |              |     |         |
| Serial       | Number(s) | : SG1ZL53061        |          | SG2ZL50131 |           | SG2ZL50145 |              |     |         |
| MAC Address  |           | : 18:7a:3b:1b:b6:c0 |          |            |           |            |              |     |         |
| Hostname     |           | : 6300              |          |            |           |            |              |     |         |
| Type         |           | : Floating          |          |            |           |            |              |     |         |
| Mode         |           | : Cloud             | Managed  |            |           |            |              |     |         |
| State        |           | : Feature           |          | Pack       | installed | and        | valid        |     |         |
| Error Reason |           | : none              |          |            |           |            |              |     |         |
|              |           |                     |          |            |           |            | Subscription |     | Feature |
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 30

| Feature |     |     |     |     |     | Status | Status |
| ------- | --- | --- | --- | --- | --- | ------ | ------ |
---------------------------------------------------------------------
| Application | Based      | Policy |     |     |     | active | allowed |
| ----------- | ---------- | ------ | --- | --- | --- | ------ | ------- |
| MACsec      | extensions | for    | WAN |     |     | active | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies | for | Port | Access Clients |     | active | allowed |
| --------- | -------- | --- | ---- | -------------- | --- | ------ | ------- |
3. RemovetheVSFstackmember.
| switch        | (config)#    | no           | vsf member | 3            |     |          |     |
| ------------- | ------------ | ------------ | ---------- | ------------ | --- | -------- | --- |
| The specified |              | switch       | will be    | unconfigured | and | rebooted |     |
| Do you        | want to      | continue     | (y/n)?     | y            |     |          |     |
| switch        | # show       | feature-pack |            |              |     |          |     |
| Feature       | Pack Summary |              |            |              |     |          |     |
===============
| Name       |      | : CX  | Software | Advanced | Feature | Pack |     |
| ---------- | ---- | ----- | -------- | -------- | ------- | ---- | --- |
| Expiration | Date | : Sat | Sep 07   | 2024     |         |      |     |
Serial Number(s) : SG2ZL50131 SG2ZL50145 << Member 3 serial number is gone
| MAC Address  |     | : 18:7a:3b:1b:b6:c0 |         |           |     |              |         |
| ------------ | --- | ------------------- | ------- | --------- | --- | ------------ | ------- |
| Hostname     |     | : 6300              |         |           |     |              |         |
| Type         |     | : Floating          |         |           |     |              |         |
| Mode         |     | : Cloud             | Managed |           |     |              |         |
| State        |     | : Feature           | Pack    | installed | and | valid        |         |
| Error Reason |     | : none              |         |           |     |              |         |
|              |     |                     |         |           |     | Subscription | Feature |
| Feature      |     |                     |         |           |     | Status       | Status  |
---------------------------------------------------------------------
| Application | Based      | Policy |     |     |     | active | allowed |
| ----------- | ---------- | ------ | --- | --- | --- | ------ | ------- |
| MACsec      | extensions | for    | WAN |     |     | active | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies | for | Port | Access Clients |     | active | allowed |
| --------- | -------- | --- | ---- | -------------- | --- | ------ | ------- |
4. IfyouarereplacingaVSFconductor,reboottheVSFstacksothatitnolongerusestheMAC
addressoftheformerconductor.Theformerconductor(nowastandaloneswitch)andthe
remainingVSFstackwillcontinuetousetheMACaddressuntiltheVSFstackreboots.Ifyou
attempttoaddafeaturepacktothestandaloneswitchbeforeyoureboottheVSFstack,youmay
getanerrorsayingthatisalreadyusingafeaturepacksubscription,becausetheMACaddressis
thesameastheexistingVSFstack.
5. WhenanewdeviceisaddedtotheVSFstack,thefeaturepackinformationforthatstackmember
isautomaticallyupdated.
| switch  | # show       | feature-pack |     |     |     |     |     |
| ------- | ------------ | ------------ | --- | --- | --- | --- | --- |
| Feature | Pack Summary |              |     |     |     |     |     |
===============
| Name       |      | : CX  | Software | Advanced | Feature | Pack |     |
| ---------- | ---- | ----- | -------- | -------- | ------- | ---- | --- |
| Expiration | Date | : Sat | Sep 07   | 2024     |         |      |     |
Serial Number(s) : SG2ZL50131 SG2ZL50145 SG1ZL78993 << New Stack Serial Number
| MAC Address  |     | : 18:7a:3b:1b:b6:c0 |         |           |     |              |         |
| ------------ | --- | ------------------- | ------- | --------- | --- | ------------ | ------- |
| Hostname     |     | : 6300              |         |           |     |              |         |
| Type         |     | : Floating          |         |           |     |              |         |
| Mode         |     | : Cloud             | Managed |           |     |              |         |
| State        |     | : Feature           | Pack    | installed | and | valid        |         |
| Error Reason |     | : none              |         |           |     |              |         |
|              |     |                     |         |           |     | Subscription | Feature |
| Feature      |     |                     |         |           |     | Status       | Status  |
---------------------------------------------------------------------
| Application | Based | Policy |     |     |     | active | allowed |
| ----------- | ----- | ------ | --- | --- | --- | ------ | ------- |
Cloud-ManagedFeaturePackUseCasesandWorkflows|31

| MACsec | extensions for | WAN |     | active | allowed |
| ------ | -------------- | --- | --- | ------ | ------- |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies for | Port Access | Clients | active | allowed |
| --------- | ------------ | ----------- | ------- | ------ | ------- |
IfyoureplaceaVSFstackmemberwithastandaloneswitchthatisalreadyusingacloud-managedfeaturepack
subscription,theHPEArubaNetworkingsupportportalwillautomaticallyextendtheexistingVSFfeaturepack
subscriptiontocoverthenewmember,butitwillnotrevoketheformerstandalonefeaturepack.Thisresultsin
anextrafeaturepackbeingconsumedbywhathasbecomesinglestandaloneswitchthatisnolongerbeing
used.Asaresult,youmustrevokethestandalonefeaturepacktomakeitavailableforotherswitchestouse.
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 32

File-based Feature Pack Use Cases and

Chapter 6

File-based Feature Pack Use Cases and Workflows

This chaptersection describes the following workflows for deployments using feature pack subscriptions
in file-based mode.

n Deploying a File-Based Feature Pack Solution on a Standalone Switch

n Setting a File-Based Switch to Honor Mode

n Deploying a File-Based Feature Pack Solution on a VSF Stack

n Replacing a VSF Stack Member Using a File-Based Feature Pack subscription

Deploying a File-Based Feature Pack Solution on a
Standalone Switch

The following section describes the procedure to install an HPE Aruba Networking CX Advanced feature
pack or a CX Premium feature pack on single standalone AOS-CX switches with feature pack
subscriptions in file -based mode.

Prerequisites

n The user has created a user account on the HPE Aruba Networking support portal.

n The user has already ordered their feature pack subscriptions from HPE Aruba Networking reseller.

n The Orders page on the HPE Aruba Networking support portal has been updated to indicate that the

subscriptions for the user account will be manged in file-based mode. For details, see Viewing
Feature Pack Subscription Pools and Feature Pack Orders.

Procedure

1. Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking

support user name and password.

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

33

2. From the License Management page, select View Order.

Figure 1 Viewing Current Orders on the HPE Aruba Networking Support Portal

3. On the Orders page, identify the feature pack you want to download and install on the switch.

4. Click the green actions icon

by the feature pack you want to download, and select Download.

The Download File window opens.

Figure 2 Downloading Feature Pack Subscriptions from the Orders Page

5.

In the Download File window, enter the host name, MAC address, and the serial number of the
device. Verify that the feature pack platform on this window matches the platform of the switch
that will use this feature pack.

File-based Feature Pack Use Cases and Workflows | 34

6. ClickDownload.
| Figure3 | DownloadingaFeaturePackFile |     |     |     |     |     |     |
| ------- | --------------------------- | --- | --- | --- | --- | --- | --- |
7. Accesstheswitchcommand-lineinterfaceandensurethatthedeviceisconfiguredtousefile-
basedmode.
| switch(config)# |     | feature-pack |     | mode file-based |     |     |     |
| --------------- | --- | ------------ | --- | --------------- | --- | --- | --- |
8. Usethecopycommandtocopythefeaturepackfiletotheswitch.
switch# copy tftp://192.168.1.1/feature-pack feature-pack vrf mgmt
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     | Dload | Upload | Total Spent | Left Speed |
| --- | --- | --- | --- | ----- | ------ | ----------- | ---------- |
100 21848 100 21848 0 0 7111k 0 --:--:-- --:--:-- --:--:-- 7111k
| writing | feature-pack |     |     |     |     |     |     |
| ------- | ------------ | --- | --- | --- | --- | --- | --- |
9. Usetheshow feature-packcommandtovalidatethethefeaturepackmodeisFile based,that
thefeaturepackstateshowsFeature pack installed and validandthatallfeaturesare
allowed.
| 6300# show | feature-pack |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- | --- | --- |
| Feature    | Pack Summary |     |     |     |     |     |     |
===============
| Name             |      | : CX                | Software | Advanced       | Feature | Pack         |         |
| ---------------- | ---- | ------------------- | -------- | -------------- | ------- | ------------ | ------- |
| Expiration       | Date | : Thu               | Jul      | 27 2028        |         |              |         |
| Serial Number(s) |      | : SG2ZL50171        |          |                |         |              |         |
| MAC Address      |      | : 18:7a:3b:1b:c6:80 |          |                |         |              |         |
| Hostname         |      | : Test_FP           |          |                |         |              |         |
| Type             |      | : Device            |          | specific       |         |              |         |
| Mode             |      | : File              | based    |                |         |              |         |
| State            |      | : Feature           |          | pack installed | and     | valid        |         |
| Error Reason     |      | : none              |          |                |         |              |         |
|                  |      |                     |          |                |         | Subscription | Feature |
| Feature          |      |                     |          |                |         | Status       | Status  |
---------------------------------------------------------------------
| Application       | Based | Policy |     |     |     | active | allowed |
| ----------------- | ----- | ------ | --- | --- | --- | ------ | ------- |
| MACsec extensions |       | for    | WAN |     |     | active | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 35

| Reflexive | Policies | for | Port | Access | Clients | active | allowed |
| --------- | -------- | --- | ---- | ------ | ------- | ------ | ------- |
10. Next,accesstheHPEArubaNetworkingSupportportalandverifythatthefeaturepackappears
tohavebeenactivated.
a. Navigatetohttps://licensemanagement.hpe.com,andloginwithyourHPEArubaNetworking
supportusernameandpassword.
b. FromtheLicense Managementpage,selecttheCX-SwitchicontoopentheSubscription
|     | Monitoring | page. |     |     |     |     |     |
| --- | ---------- | ----- | --- | --- | --- | --- | --- |
c. CheckthedetailsonthispagetoverifythattheHPEArubaNetworkingsupportportal
correctlyreflectsthatthefeaturepackisassociatedwiththecorrectdevice.
FormoredetailsonmonitoringfeaturePacks,refertoMonitoringFeaturePackSubscriptions.
| Setting | a File-Based |     |     | Switch | to Honor | Mode |     |
| ------- | ------------ | --- | --- | ------ | -------- | ---- | --- |
Inhonormode,thefeaturessupportedbyCXAdvancedorCXPremiumfeaturepacksareenabled
withoutthepresenceofaactivefeaturepack.Honormodeisintendedforcaseswhereavalidfeature
packforadvancedorpremiumfeatureshasbeenpurchased,butisnotyetinstalledonthedevice.A
warningmessagemayappearuntilavalidfeaturepackisinstalled.
Procedure
1. Accesstheswitchcommand-lineinterfaceandusethefeature-pack mode honorcommandto
settheswitchtohonormode.
| switch(config)# |     | feature-pack |     | mode | honor |     |     |
| --------------- | --- | ------------ | --- | ---- | ----- | --- | --- |
2. Oncehonormodeisconfigured,checktheswitchstateusingtheshowfeature-packcommand.
Theoutputofthiscommandshouldshowthatthefeaturepackmodeissettohonormode,and
thatfeaturesareallowedandthefeaturepacksubscriptionstatusismarkedhonormode.
| switch# | shpw | feature-pack |     |     |     |     |     |
| ------- | ---- | ------------ | --- | --- | --- | --- | --- |
| Feature | Pack | Summary      |     |     |     |     |     |
====================
| Name        |           | : --      |     |      |                       |              |         |
| ----------- | --------- | --------- | --- | ---- | --------------------- | ------------ | ------- |
| Expiration  | Date      | : --      |     |      |                       |              |         |
| Serial      | Number(s) | :         |     |      |                       |              |         |
| MAC Address |           | : --      |     |      |                       |              |         |
| Hostname    |           | : --      |     |      |                       |              |         |
| Type        |           | : --      |     |      |                       |              |         |
| Mode        |           | : Honor   |     |      |                       |              |         |
| State       |           | : Feature |     | pack | mode honor configured |              |         |
| Error       | Reason    | : none    |     |      |                       |              |         |
|             |           |           |     |      |                       | Subscription | Feature |
| Feature     |           |           |     |      |                       | Status       | Status  |
-----------------------------------------------------------------------
| Application | Based      | Policy |     |     |     | honor mode | allowed |
| ----------- | ---------- | ------ | --- | --- | --- | ---------- | ------- |
| MACsec      | extensions | for    | WAN |     |     | honor mode | allowed |
Reflexive Policies for Port Access GBP Clients honor mode allowed
File-basedFeaturePackUseCasesandWorkflows|36

Reflexive Policies for Port Access Clients

honor mode

allowed

Deploying a File-Based Feature Pack Solution on a VSF Stack

The following section describes the procedure to install an Aruba CX premium or advanced feature pack
on a VSF stack with feature pack subscriptions in file -based mode.

Prerequisites

n The user has created a user account on the HPE Aruba Networking support portal.

n The user has already ordered their feature pack subscriptions from HPE Aruba Networking reseller.

n The HPE Aruba Networking support portal contains a feature pack pool with a number of feature

pack subscriptions equal to or greater than the number of devices in the VSF stack.

n The Orders page on the HPE Aruba Networking support portal has been updated to indicate that the

subscriptions for the user account will be manged in file-based mode. For details, see Viewing
Feature Pack Subscription Pools and Feature Pack Orders.

Procedure

1. Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking

support user name and password.

2. From the License Management page, select View Order.

Figure 1 Viewing Current Orders on the HPE Aruba Networking Support Portal

3. On the Orders page, identify the feature pack you want to download and install on the switch.

Take care to verify that the available subscriptions in the block are equal or greater than the members in the VSF

stack.

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

37

4. Click the green actions icon

by the feature pack you want to download, and select Download.

The Download File window opens.

Figure 2 Downloading Feature Pack Subscriptions from the Orders page.

5.

In the Download File window, enter the VSF conductor MAC address (available in the output of
the show vsf command on the switch), the serial numbers of all the devices in the VSF stack in
comma-separated format. Verify that the feature pack platform displayed in this window matches
the platform of the switch that will use this feature pack.

6. Click Download.

Figure 3 Downloading a Feature Pack File

File-based Feature Pack Use Cases and Workflows | 38

7. Accesstheswitchcommand-lineinterfaceandensurethatthedeviceisconfiguredtousefile-
basedmode.
| switch(config)# |     |     | feature-pack |     | mode | file-based |     |     |     |
| --------------- | --- | --- | ------------ | --- | ---- | ---------- | --- | --- | --- |
8. Usethecopycommandtocopythefeaturepackfiletotheswitch.
switch# copy tftp://192.168.1.1/feature-pack feature-pack vrf mgmt
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     |     |     | Dload | Upload | Total Spent | Left Speed |
| --- | --- | --- | --- | --- | --- | ----- | ------ | ----------- | ---------- |
100 21848 100 21848 0 0 7111k 0 --:--:-- --:--:-- --:--:-- 7111k
| writing |     | feature-pack |     |     |     |     |     |     |     |
| ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
9. Usetheshow feature-packcommandtocheckthestatusofthefeaturepackontheconductor
orthestandbyswitch.VerifythatthefeaturepackmodeisFile Based,thefeaturepackis
installedandallfeaturesareallowed,andthattheserialnumberslistedrepresentallVSF
members.
| 6300#   | show | feature-pack |         |     |     |     |     |     |     |
| ------- | ---- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
| Feature |      | Pack         | Summary |     |     |     |     |     |     |
===============
| Name       |           |      | : CX                | Software |          | Advanced    | feature     | pack         |         |
| ---------- | --------- | ---- | ------------------- | -------- | -------- | ----------- | ----------- | ------------ | ------- |
| Expiration |           | Date | : Thu               | Sep      | 05 2024  |             |             |              |         |
| Serial     | Number(s) |      | : SG1ZL530661       |          |          | SG2ZL504146 | SG2ZL511853 |              |         |
| MAC        | Address   |      | : 18:7a:3b:1b:d7:80 |          |          |             |             |              |         |
| Hostname   |           |      | : VSF_demo          |          |          |             |             |              |         |
| Type       |           |      | : Device            |          | specific |             |             |              |         |
| Mode       |           |      | : File              | Based    |          |             |             |              |         |
| State      |           |      | :                   |          |          |             |             |              |         |
|            |           |      | feature             |          | pack     | installed   | and         | valid        |         |
| Error      | Reason    |      | : none              |          |          |             |             |              |         |
|            |           |      |                     |          |          |             |             | Subscription | Feature |
| Feature    |           |      |                     |          |          |             |             | Status       | Status  |
---------------------------------------------------------------------
| Application |            | Based | Policy |     |     |     |     | active | allowed |
| ----------- | ---------- | ----- | ------ | --- | --- | --- | --- | ------ | ------- |
| MACsec      | extensions |       | for    | WAN |     |     |     | active | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive |     | Policies | for | Port | Access | Clients |     | active |     |
| --------- | --- | -------- | --- | ---- | ------ | ------- | --- | ------ | --- |
allowed
10. Next,accesstheHPEArubaNetworkingSupportportalandverifythatthefeaturepackappears
tohavebeenactivated.
a. Navigatetohttps://licensemanagement.hpe.com,andloginwithyourHPEArubaNetworking
supportusernameandpassword.
b. FromtheLicense Managementpage,selecttheCX-SwitchicontoopentheSubscription
|     | Monitoring |     | page. |     |     |     |     |     |     |
| --- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- |
c. CheckthedetailsonthispagetoverifythattheHPEArubaNetworkingsupportportal
correctlyreflectsthatthefeaturepackisassociatedwithallserialnumbersintheVSF stack.
Formoredetailsonmonitoringfeaturepacks,refertoMonitoringFeaturePackSubscriptions.
| Adding | a Switch |     | with a | Feature | Pack | to  | a VSF Stack |     |     |
| ------ | -------- | --- | ------ | ------- | ---- | --- | ----------- | --- | --- |
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 39

WhenyouaddastandaloneswitchwithanexistingfloatingfeaturepacksubscriptiontoaVSFstack
withafloatingfeaturepacksubscription,theHPEArubaNetworkingsuportportalwillautomatically
extendtheexistingVSFfeaturepacktocoverthenewmember,butitwillnotrevoketheformer
standalonefeaturepack.Thiswillresultinanextrafeaturepacksubscriptionbeingconsumedinthe
HPEArubaNetworkingsupportportal,asthesinglestandalonesubscriptionthatisnolongerbeing
used.Youmustrevokethestandalonesubscriptioninthesupportportaltomakeitavailableforother
switchestouse.
| Replacing         | a   | VSF | Stack |     | Member | Using |     | a File-Based | Feature |
| ----------------- | --- | --- | ----- | --- | ------ | ----- | --- | ------------ | ------- |
| Pack subscription |     |     |       |     |        |       |     |              |         |
ThefollowingsectiondescribestheproceduretoreplaceaVSFstackmemberinaVSFstackwithafile-
basedfeaturepack.Thisexampleinstallsthefeaturepackforallmembersofthestack,
Procedure
1. Logontotheswitchcommand-lineinterface.
2. Usetheno vsf member <member>commandtoremovethememberyouwanttoreplacefrom
theVSFstack.Thefollowingexampleremovesthestackmemberwiththeserialnumber
SG2ZL50146.
| switch(config)# |     | no       | vsf  | member | 3            |     |          |     |     |
| --------------- | --- | -------- | ---- | ------ | ------------ | --- | -------- | --- | --- |
| The specified   |     | switch   | will | be     | unconfigured | and | rebooted |     |     |
| Do you want     | to  | continue |      | (y/n)? | y            |     |          |     |     |
3. AfteryouremovethedevicefromtheVSFstack,featuressupportedbythefeaturepacksarestill
active.Theshow feature-packcommandstillincludestheserialnumberofthedevicewhichwas
removed.ThefollowingexampleoutputshowsthattherearetwomembersintheVSFstack,but
threemembersarestillassociatedwiththefeaturepacksubscription.
| 6300(config)#   |             | show   | vsf     |      |                   |        |     |     |     |
| --------------- | ----------- | ------ | ------- | ---- | ----------------- | ------ | --- | --- | --- |
| Force Autojoin  |             |        |         | :    | Disabled          |        |     |     |     |
| Autojoin        | Eligibility |        | Status: |      | Not Eligible      |        |     |     |     |
| MAC Address     |             |        |         | :    | 18:7a:3b:1b:d7:80 |        |     |     |     |
| Secondary       |             |        |         | :    | 2                 |        |     |     |     |
| Topology        |             |        |         | :    | Chain             |        |     |     |     |
| Status          |             |        |         | :    | No Split          |        |     |     |     |
| Split Detection |             | Method |         | :    | None              |        |     |     |     |
| Mbr Mac         | Address     |        |         | type |                   | Status |     |     |     |
ID
| --- ------------------- |     |     |     | -------------- |     | --------------- |     |     |     |
| ----------------------- | --- | --- | --- | -------------- | --- | --------------- | --- | --- | --- |
| 1 18:7a:3b:1b:d7:80     |     |     |     | R8S90A         |     | Conductor       |     |     |     |
2 ec:02:73:f7:ec:c0 R8S92A Standby <<-Only 2 VSF Members in stack
| switch(config)# |      | show    | feature-pack |     |     |     |     |     |     |
| --------------- | ---- | ------- | ------------ | --- | --- | --- | --- | --- | --- |
| Feature         | Pack | Summary |              |     |     |     |     |     |     |
===============
| Name       |      | :   | CX Software |        | Advanced | Feature | Pack |     |     |
| ---------- | ---- | --- | ----------- | ------ | -------- | ------- | ---- | --- | --- |
| Expiration | Date | :   | Thu         | Sep 05 | 2024     |         |      |     |     |
Serial Number(s) : SG1ZL53061 SG2ZL50146 SG2ZL51153 <<-Old VSF Member still listed
File-basedFeaturePackUseCasesandWorkflows|40

| MAC Address  |     | : 18:7a:3b:1b:d7:80 |          |               |              |              |
| ------------ | --- | ------------------- | -------- | ------------- | ------------ | ------------ |
| Hostname     |     | : VSF_demo          |          |               |              |              |
| Type         |     | : Device            | specific |               |              |              |
| Mode         |     | : File              | Based    |               |              |              |
| State        |     | : Feature           | pack     | installed and | valid        |              |
| Error Reason |     | : none              |          |               |              |              |
|              |     |                     |          |               | Subscription | Subscription |
| Feature      |     |                     |          |               | Status       | Status       |
---------------------------------------------------------------------
| Application | Based      | Policy  |     |     | active | allowed |
| ----------- | ---------- | ------- | --- | --- | ------ | ------- |
| MACsec      | extensions | for WAN |     |     | active | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies | for Port | Access | Clients | active | allowed |
| --------- | -------- | -------- | ------ | ------- | ------ | ------- |
4. Beforeaddingthedevice,notetheserialnumberofthenewreplacementdevice.Next,navigate
tothesubscription MonitoringpageoftheHPEArubaNetworkingSupportportal,asdescribed
inMonitoringFeaturePackSubscriptions.
5. IntheSubscription Monitoringpage,locatethefeaturepacksubscriptionallocatedtothe VSF
stackbyenteringtheserialnumberoftheVSFstackconductorintothesearchbaratthetopof
thepage.
6. Clickthegreenactionsicon andselectModify.The Download Filewindowopens.
ModifyaFeaturePackSubscription
Figure1
7. ReplacetheserialnumberoftheoldVSF stackmemberwiththeserialnumberofthenewVSF
stackmember.
8. ClickDownloadtore-downloadtheupdatedfeaturepack.
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 41

Figure2 DownloadingtheFileforNewVSFSwitchMembers
9. Usethecopycommandtocopythefeaturepackfiletotheswitch.
switch# copy tftp://192.168.1.1/feature-pack feature-pack vrf mgmt
% Total % Received % Xferd Average Speed Time Time Time Current
|     |     |     |     | Dload | Upload | Total Spent | Left Speed |
| --- | --- | --- | --- | ----- | ------ | ----------- | ---------- |
100 21848 100 21848 0 0 7111k 0 --:--:-- --:--:-- --:--:-- 7111k
| writing | feature-pack |     |     |     |     |     |     |
| ------- | ------------ | --- | --- | --- | --- | --- | --- |
10. Usetheshow feature-packcommandtovalidatethatthenewswitchserialnumberispresentin
theupdatedfeaturepack.
| 6300# show | feature-pack |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- | --- | --- |
| Feature    | Pack Summary |     |     |     |     |     |     |
===============
| Name       |      | : CX  | Software | Advanced | Feature | Pack |     |
| ---------- | ---- | ----- | -------- | -------- | ------- | ---- | --- |
| Expiration | Date | : Thu | Sep 05   | 2024     |         |      |     |
Serial Number(s) : SG1ZL53061 SG2ZL50172 SG2ZL51153 << New member serial number
| MAC Address  |     | : 18:7a:3b:1b:d7:80 |          |           |     |              |         |
| ------------ | --- | ------------------- | -------- | --------- | --- | ------------ | ------- |
| Hostname     |     | : VSF_demo          |          |           |     |              |         |
| Type         |     | : Device            | specific |           |     |              |         |
| Mode         |     | : File              | Based    |           |     |              |         |
| State        |     | : Feature           | pack     | installed | and | valid        |         |
| Error Reason |     | : none              |          |           |     |              |         |
|              |     |                     |          |           |     | Subscription | Feature |
| Feature      |     |                     |          |           |     | Status       | Status  |
---------------------------------------------------------------------
| Application | Based      | Policy |     |     |     | active | allowed |
| ----------- | ---------- | ------ | --- | --- | --- | ------ | ------- |
| MACsec      | extensions | for    | WAN |     |     | active | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies | for | Port | Access Clients |     | active | allowed |
| --------- | -------- | --- | ---- | -------------- | --- | ------ | ------- |
11. AddthenewdevicetotheVSF stack.Thenewdeviceisautomaticiallyenabledwiththefeature
packsubscription.
File-basedFeaturePackUseCasesandWorkflows|42

12. (Optional)Issuetheshow vsfcommandandtheshow feature-packcommandasecondtimeto
verifythatthenewVSFmemberappearsinthestack,andtoverifythestatusofthefeaturepack
onthestack.
| switch#         | show        | vsf    |         |                     |          |        |     |     |     |     |
| --------------- | ----------- | ------ | ------- | ------------------- | -------- | ------ | --- | --- | --- | --- |
| Force Autojoin  |             |        |         | : Disabled          |          |        |     |     |     |     |
| Autojoin        | Eligibility |        | Status: | Not                 | Eligible |        |     |     |     |     |
| MAC Address     |             |        |         | : 18:7a:3b:1b:d7:80 |          |        |     |     |     |     |
| Secondary       |             |        |         | : 2                 |          |        |     |     |     |     |
| Topology        |             |        |         | : Ring              |          |        |     |     |     |     |
| Status          |             |        |         | : No                | Split    |        |     |     |     |     |
| Split Detection |             | Method |         | : None              |          |        |     |     |     |     |
| Mbr Mac         | Address     |        |         | type                |          | Status |     |     |     |     |
ID
| --- ------------------- |      |         |              | -------------- |     | --------------- |     |     |     |     |
| ----------------------- | ---- | ------- | ------------ | -------------- | --- | --------------- | --- | --- | --- | --- |
| 1 18:7a:3b:1b:d7:80     |      |         |              | R8S90A         |     | Conductor       |     |     |     |     |
| 2 ec:02:73:f7:ec:c0     |      |         |              | R8S92A         |     | Standby         |     |     |     |     |
| 3 18:7a:3b:1b:b6:40     |      |         |              | R8S89A         |     | Member          |     |     |     |     |
| switch(config)#         |      | show    | feature-pack |                |     |                 |     |     |     |     |
| Feature                 | Pack | Summary |              |                |     |                 |     |     |     |     |
===============
| Name       |      | :   | CX Software |     | Advanced | Feature | Pack |     |     |     |
| ---------- | ---- | --- | ----------- | --- | -------- | ------- | ---- | --- | --- | --- |
| Expiration | Date | :   | Thu Sep     | 05  | 2024     |         |      |     |     |     |
Serial Number(s) : SG1ZL53061 SG2ZL50172 SG2ZL51153 < New member serial number
| MAC Address  |     | :   | 18:7a:3b:1b:d7:80 |          |           |     |              |     |         |     |
| ------------ | --- | --- | ----------------- | -------- | --------- | --- | ------------ | --- | ------- | --- |
| Hostname     |     | :   | VSF_demo          |          |           |     |              |     |         |     |
| Type         |     | :   | Device            | specific |           |     |              |     |         |     |
| Mode         |     | :   | File              | Based    |           |     |              |     |         |     |
| State        |     | :   | Feature           | pack     | installed | and | valid        |     |         |     |
| Error Reason |     | :   | none              |          |           |     |              |     |         |     |
|              |     |     |                   |          |           |     | Subscription |     | Feature |     |
| Feature      |     |     |                   |          |           |     | Status       |     | Status  |     |
---------------------------------------------------------------------
| Application | Based      |     | Policy  |     |     |     | active |     | allowed |     |
| ----------- | ---------- | --- | ------- | --- | --- | --- | ------ | --- | ------- | --- |
| MACsec      | extensions |     | for WAN |     |     |     | active |     | allowed |     |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies |     | for Port | Access | Clients |     | active |     | allowed |     |
| --------- | -------- | --- | -------- | ------ | ------- | --- | ------ | --- | ------- | --- |
13. (Optional)ReturntotheFeature Pack MonitoringpageontheHPEArubaNetworkingsupport
portal,andverifythattheserialnumbersforthatorderreflectthecorrectserialnumbersforthat
stack.
| Replacing         | a   | VSF | Stack |     | Conductor |     | Using | a File-Based |     | Feature |
| ----------------- | --- | --- | ----- | --- | --------- | --- | ----- | ------------ | --- | ------- |
| Pack subscription |     |     |       |     |           |     |       |              |     |         |
ThefollowingsectiondescribestheproceduretoreplaceaVSFstackconductorinaVSFstackwithafile-
basedfeaturepack.Thisexampleinstallsthefeaturepackforallmembersofthestack,
Procedure
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 43

1. Logontotheswitchcommand-lineinterface.
2. Triggeraswitchoversomember1isnolongertheconductor.
| switch#   | vsf switchover |          |           |         |            |        |         |
| --------- | -------------- | -------- | --------- | ------- | ---------- | ------ | ------- |
| This will | cause          | an       | immediate |         | switchover | to the | standby |
| and the   | conductor      |          | will      | reboot. |            |        |         |
| Do you    | want to        | continue |           | (y/n)?  | y          |        |         |
switch#
1. Usetheno vsf member <member>commandtoremovetheconductorfromtheVSFstack.The
followingexampleremovesthestackmemberwiththeserialnumberSG2ZL50146.
| switch(config)# |         | no       | vsf  | member | 1            |     |          |
| --------------- | ------- | -------- | ---- | ------ | ------------ | --- | -------- |
| The specified   |         | switch   | will | be     | unconfigured | and | rebooted |
| Do you          | want to | continue |      | (y/n)? | y            |     |          |
2. AfteryouremovetheconductorfromtheVSFstack,featuressupportedbythefeaturepacksare
stillactive.Theshow feature-packcommandstillincludestheserialnumberofthedevicewhich
wasremoved.ThefollowingexampleoutputshowsthattherearetwomembersintheVSFstack,
butthreemembersarestillassociatedwiththefeaturepacksubscription.
| 6300(config)#   |             | show   | vsf     |      |                   |        |     |
| --------------- | ----------- | ------ | ------- | ---- | ----------------- | ------ | --- |
| Force Autojoin  |             |        |         | :    | Disabled          |        |     |
| Autojoin        | Eligibility |        | Status: |      | Not Eligible      |        |     |
| MAC Address     |             |        |         | :    | 18:7a:3b:1b:d7:80 |        |     |
| Secondary       |             |        |         | :    | 2                 |        |     |
| Topology        |             |        |         | :    | Chain             |        |     |
| Status          |             |        |         | :    | No Split          |        |     |
| Split Detection |             | Method |         | :    | None              |        |     |
| Mbr Mac         | Address     |        |         | type |                   | Status |     |
ID
| --- ------------------- |     |     |     | -------------- |     | --------------- |     |
| ----------------------- | --- | --- | --- | -------------- | --- | --------------- | --- |
| 1 18:7a:3b:1b:d7:80     |     |     |     | R8S90A         |     | Conductor       |     |
2 ec:02:73:f7:ec:c0 R8S92A Standby <<-Only 2 VSF Members in stack
| switch(config)# |      | show    | feature-pack |     |     |     |     |
| --------------- | ---- | ------- | ------------ | --- | --- | --- | --- |
| Feature         | Pack | Summary |              |     |     |     |     |
===============
| Name       |      | :   | CX Software |        | Advanced | Feature | Pack |
| ---------- | ---- | --- | ----------- | ------ | -------- | ------- | ---- |
| Expiration | Date | :   | Thu         | Sep 05 | 2024     |         |      |
Serial Number(s) : SG1ZL53061 SG2ZL50146 SG2ZL51153 <<-Old VSF Member still listed
| MAC Address  |     | :   | 18:7a:3b:1b:d7:80 |          |           |     |       |
| ------------ | --- | --- | ----------------- | -------- | --------- | --- | ----- |
| Hostname     |     | :   | VSF_demo          |          |           |     |       |
| Type         |     | :   | Device            | specific |           |     |       |
| Mode         |     | :   | File              | Based    |           |     |       |
| State        |     | :   | Feature           | pack     | installed | and | valid |
| Error Reason |     | :   | none              |          |           |     |       |
Subscription Subscription
File-basedFeaturePackUseCasesandWorkflows|44

| Feature |     |     |     |     |     | Status | Status |
| ------- | --- | --- | --- | --- | --- | ------ | ------ |
---------------------------------------------------------------------
| Application | Based      | Policy |     |     |     | active | allowed |
| ----------- | ---------- | ------ | --- | --- | --- | ------ | ------- |
| MACsec      | extensions | for    | WAN |     |     | active | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies | for | Port | Access Clients |     | active | allowed |
| --------- | -------- | --- | ---- | -------------- | --- | ------ | ------- |
3. AddthenewconductortotheVSF stack.
4. ReboottheVSFstacksothatitnolongerusestheMACaddressoftheformerconductor.The
formerconductor(nowastandaloneswitch)andtheremainingVSFstackwillcontinuetousethe
MACaddressuntiltheVSFstackreboots.Ifyouattempttoaddafeaturepacktothestandalone
switchbeforeyoureboottheVSFstack,youmaygetanerrorsayingthatitalreadyhasafeature
pack,becausetheMACaddressisthesameastheexistingVSFstack.
5. NotetheserialnumberofthereplacementdeviceandthenewMACaddressofthestack.
6. DownloadthenewfeaturepackusingtheproceduredescribedinDeployingaFile-BasedFeature
PackSolutiononaVSFStack.
7. Usetheshow feature-packcommandtovalidatethatthenewswitchserialnumberispresentin
theupdatedfeaturepack.
| 6300# show | feature-pack |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- | --- | --- |
| Feature    | Pack Summary |     |     |     |     |     |     |
===============
| Name       |      | : CX  | Software | Advanced | Feature | Pack |     |
| ---------- | ---- | ----- | -------- | -------- | ------- | ---- | --- |
| Expiration | Date | : Thu | Sep 05   | 2024     |         |      |     |
Serial Number(s) : SG1ZL53061 SG2ZL50172 SG2ZL51153 << New member serial number
| MAC Address  |     | : 18:7a:3b:1b:d7:80 |          |           |     |              |         |
| ------------ | --- | ------------------- | -------- | --------- | --- | ------------ | ------- |
| Hostname     |     | : VSF_demo          |          |           |     |              |         |
| Type         |     | : Device            | specific |           |     |              |         |
| Mode         |     | : File              | Based    |           |     |              |         |
| State        |     | : Feature           | pack     | installed | and | valid        |         |
| Error Reason |     | : none              |          |           |     |              |         |
|              |     |                     |          |           |     | Subscription | Feature |
| Feature      |     |                     |          |           |     | Status       | Status  |
---------------------------------------------------------------------
| Application | Based      | Policy |     |     |     | active | allowed |
| ----------- | ---------- | ------ | --- | --- | --- | ------ | ------- |
| MACsec      | extensions | for    | WAN |     |     | active | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies | for | Port | Access Clients |     | active | allowed |
| --------- | -------- | --- | ---- | -------------- | --- | ------ | ------- |
8. (Optional)Issuetheshow vsfcommandandtheshow feature-packcommandasecondtimeto
verifythatthenewVSFmemberappearsinthestack,andtoverifythestatusofthefeaturepack
onthestack.
| switch#        | show vsf    |     |         |                   |     |     |     |
| -------------- | ----------- | --- | ------- | ----------------- | --- | --- | --- |
| Force Autojoin |             |     | :       | Disabled          |     |     |     |
| Autojoin       | Eligibility |     | Status: | Not Eligible      |     |     |     |
| MAC Address    |             |     | :       | 18:7a:3b:1b:d7:80 |     |     |     |
| Secondary      |             |     | :       | 2                 |     |     |     |
| Topology       |             |     | :       | Ring              |     |     |     |
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 45

| Status          |         |        | :    | No Split |        |     |     |
| --------------- | ------- | ------ | ---- | -------- | ------ | --- | --- |
| Split Detection |         | Method | :    | None     |        |     |     |
| Mbr Mac         | Address |        | type |          | Status |     |     |
ID
| --- ------------------- |      |         | -------------- |     | --------------- |     |     |
| ----------------------- | ---- | ------- | -------------- | --- | --------------- | --- | --- |
| 1 18:7a:3b:1b:d7:80     |      |         | R8S90A         |     | Conductor       |     |     |
| 2 ec:02:73:f7:ec:c0     |      |         | R8S92A         |     | Standby         |     |     |
| 3 18:7a:3b:1b:b6:40     |      |         | R8S89A         |     | Member          |     |     |
| switch(config)#         |      | show    | feature-pack   |     |                 |     |     |
| Feature                 | Pack | Summary |                |     |                 |     |     |
===============
| Name       |      | : CX  | Software | Advanced | Feature | Pack |     |
| ---------- | ---- | ----- | -------- | -------- | ------- | ---- | --- |
| Expiration | Date | : Thu | Sep 05   | 2024     |         |      |     |
Serial Number(s) : SG1ZL53061 SG2ZL50172 SG2ZL51153 < New member serial number
| MAC Address  |     | : 18:7a:3b:1b:d7:80 |          |           |     |       |     |
| ------------ | --- | ------------------- | -------- | --------- | --- | ----- | --- |
| Hostname     |     | : VSF_demo          |          |           |     |       |     |
| Type         |     | : Device            | specific |           |     |       |     |
| Mode         |     | : File              | Based    |           |     |       |     |
| State        |     | : Feature           | pack     | installed | and | valid |     |
| Error Reason |     | : none              |          |           |     |       |     |
Subscription
| Feature |     |     |     |     |     | Status | Status |
| ------- | --- | --- | --- | --- | --- | ------ | ------ |
---------------------------------------------------------------------
| Application | Based      | Policy |     |     |     | active | allowed |
| ----------- | ---------- | ------ | --- | --- | --- | ------ | ------- |
| MACsec      | extensions | for    | WAN |     |     | active | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies | for | Port | Access Clients |     | active | allowed |
| --------- | -------- | --- | ---- | -------------- | --- | ------ | ------- |
9. (Optional)ReturntotheFeature Pack MonitoringpageontheHPEArubaNetworkingsupport
portal,andverifythattheserialnumbersforthatorderreflectthecorrectserialnumbersforthat
stack.
File-basedFeaturePackUseCasesandWorkflows|46

Chapter 7
|         |         |     |       |             |     | Viewing | Feature    | Packs | on Switches |
| ------- | ------- | --- | ----- | ----------- | --- | ------- | ---------- | ----- | ----------- |
| Viewing | Feature |     | Packs | on Switches |     | Managed | by Central |       |             |
YoudonotneedtoenablefeaturepacksonAOS-CXswitchesmanagedbyArubaCentral,asallfeatures
supportedbythesefeaturepacksareenabledwhentheswitchconnectstoArubaCentral.ArubaCentral
takesprecedenceoveranyotherfeaturepackconfiguredmode.
IfyouwanttousetheHPEArubaNetworkingsupportportalforfeaturepackmanagementinsteadofAruba
Central,disableCentralontheswitch.Thiswillallowyoutosetupanewcloudserverprofile​.
Issuetheshow feature-packcommandtoverifythattheswitchiscurrentlyconnectedtoAruba
Central.
| 6300#   | show | feature-pack |         |     |     |     |     |     |     |
| ------- | ---- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
| Feature |      | Pack         | Summary |     |     |     |     |     |     |
===============
| Name         |           |      | : CX                | Software | Advanced | Feature     | Pack      |        |     |
| ------------ | --------- | ---- | ------------------- | -------- | -------- | ----------- | --------- | ------ | --- |
| Expiration   |           | Date | : Fri               | Aug 12   | 2033     |             |           |        |     |
| Serial       | Number(s) |      | : SG2ZL50199        |          |          |             |           |        |     |
| MAC          | Address   |      | : 18:7a:3b:1b:c6:16 |          |          |             |           |        |     |
| Hostname     |           |      | : 6300M             |          |          |             |           |        |     |
| Type         |           |      | : Device            | specific |          |             |           |        |     |
| Mode         |           |      | : File              | Based    |          |             |           |        |     |
| State        |           |      | :                   |          |          |             |           |        |     |
|              |           |      | Aruba               | Central  |          | managed and | connected |        |     |
| Error        | Reason    |      | : none              |          |          |             |           |        |     |
| Subscription |           |      | Feature             |          |          |             | Status    | Status |     |
---------------------------------------------------------------------
| Application |            | Based | Policy |     |     |     | active | allowed |     |
| ----------- | ---------- | ----- | ------ | --- | --- | --- | ------ | ------- | --- |
| MACsec      | extensions |       | for    | WAN |     |     | active | allowed |     |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive |     | Policies | for | Port | Access | Clients | active | allowed |     |
| --------- | --- | -------- | --- | ---- | ------ | ------- | ------ | ------- | --- |
Thefeature-packontheswitchwilldisplaytheAruba Central managed and connectedstateonlyifall
thefollowingaretrue:
n TheswitchhasconnectiontoCentral.
n TheswitchisonboardedtotheGreenLakeforPrivateCloud(GLPC)deviceinventory.
n TheswitchisassignedtoCentralApplicationinGLPC.
n TheswitchhasavalidCentralLicenseassignedinGLPC.
IfaCentral-managedswitchisunabletoreachArubaCentral,featuressupportedbythefeaturepack
arestillallowedontheswitch,eventhoughtheoutputoftheshow feature-packcommandshowsthat
thefeaturepacksubscriptionisinactive.ThemodefielddisplaysadefaultstatusofFile-Based,butthe
modedoesnotapplyasswitchismanagedbyCentral.
| 6300#   | show | feature-pack |         |     |     |     |     |     |     |
| ------- | ---- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
| Feature |      | Pack         | Summary |     |     |     |     |     |     |
===============
47
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries)

| Name         |           | : CX                | Software | Advanced Feature | Pack         |         |
| ------------ | --------- | ------------------- | -------- | ---------------- | ------------ | ------- |
| Expiration   | Date      | : Fri               | Aug 12   | 2033             |              |         |
| Serial       | Number(s) | : SG2ZL50199        |          |                  |              |         |
| MAC Address  |           | : 18:7a:3b:1b:c6:16 |          |                  |              |         |
| Hostname     |           | : 6300M             |          |                  |              |         |
| Type         |           | : Device            | specific |                  |              |         |
| Mode         |           | : File              | Based    |                  |              |         |
| State        |           | : Aruba             | Central  | managed and      | disconnected |         |
| Error Reason |           | : none              |          |                  |              |         |
|              |           |                     |          |                  | Subcription  | Feature |
| Feature      |           |                     |          |                  | Status       | Status  |
---------------------------------------------------------------------
| Application | Based      | Policy |     |     | inactive | allowed |
| ----------- | ---------- | ------ | --- | --- | -------- | ------- |
| MACsec      | extensions | for    | WAN |     | inactive | allowed |
Reflexive Policies for Port Access GBP Clients inactive allowed
| Reflexive | Policies | for | Port | Access Clients | inactive | allowed |
| --------- | -------- | --- | ---- | -------------- | -------- | ------- |
Inaddition,thefollowingmessageisloggedwhentheswitchconnectstoArubaCentral.
2023-09-20T07:04:03.172885+00:00 6300 feature-pack-mgrd[4077]: Event|14407|LOG_
INFO|CDTR|1|Feature pack subscription through Aruba Central is connected
Formorelogmessagesrelatedtofeaturepackevents,seeFeaturePackevents.
| Feature | pack | commands |     |     |     |     |
| ------- | ---- | -------- | --- | --- | --- | --- |
erase feature-pack
erasefeature-pack[reset]
Description
Removetheinstalledfeaturepackanddeletethefeaturepackfile.
| Parameter |     |     |     | Description                                      |     |     |
| --------- | --- | --- | --- | ------------------------------------------------ | --- | --- |
| reset     |     |     |     | Optional.Includethisparameterifyoudonotwanttouse |     |     |
subscriptionfeaturesanymoreandwanttostopreceivinghonor
modewarninglogsmessages.Runningthiscommandwill
disableallsubscriptionfeaturesandstophonorwarnings.
Example
Removethefeaturepack.Theswitchwillcontinuetooperateinhonormode.
| switch# | erase | feature-pack |     |     |     |     |
| ------- | ----- | ------------ | --- | --- | --- | --- |
Removethefeaturepackanddisableallsubscriptionfeatures.
| switch# | erase | feature-pack | reset |     |     |     |
| ------- | ----- | ------------ | ----- | --- | --- | --- |
Featurepackcommands|48

This operation will delete the feature pack subscription key and reset
feature pack enforcement to a factory default state. This will disable
advanced features that require a subscription to operate and may impact
| network operation |     | if those | features | are in | use. |
| ----------------- | --- | -------- | -------- | ------ | ---- |
After running this command, advanced features can only be re-enabled
| through one         | of      | the following:   |            |                                |      |
| ------------------- | ------- | ---------------- | ---------- | ------------------------------ | ---- |
| 1. Installing       | a       | new feature-pack |            | subscription                   | key. |
| 2. Connecting       | to      | HPE Aruba        | Networking | Central.                       |      |
| 3. Configuring      |         | honor mode.      |            |                                |      |
| Continue            | (y/n)?  |                  |            |                                |      |
| Command History     |         |                  |            |                                |      |
| Release             |         |                  |            | Modification                   |      |
| 10.14               |         |                  |            | Theresetparameterisintroduced. |      |
| 10.13               |         |                  |            | Commandintroduced.             |      |
| Command Information |         |                  |            |                                |      |
| Platforms           | Command | context          |            | Authority                      |      |
manager
| 6300 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- |
| 6400 |     |     |     | rightsforthiscommand.                              |     |
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| feature-pack |      | mode |     |     |     |
| ------------ | ---- | ---- | --- | --- | --- |
| feature-pack | mode |      |     |     |     |
cloud-managed
file-based
honor
no ...
Description
Settheoperationmodeforafeaturepackdeployment.
HPEArubaNetworkingprovidesthreemodesforfeaturepackmanagement:cloud-managed,file-
based,andhonor.Intheeventofamismatchbetweentheinstalledfeaturepackandthefeaturepack
mode,thedevicewilloperateinhonormode.
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 49

| Parameter     |     |     | Description                                   |
| ------------- | --- | --- | --------------------------------------------- |
| cloud-managed |     |     | Thedeviceusescloud-basedfeaturepackmanagement |
file-managed Thedeviceusesamanuallyinstalledfeaturepackfile.Thisisthe
defaultfeaturepackmode.
| honor |     |     | Avalidfeaturepackhasbeenobtained,butisnotyetinstalled. |
| ----- | --- | --- | ------------------------------------------------------ |
no ...
Resetstheconfigurationbacktothedefaultfile-basedfeature
packmode.
Usage
Switchesusingfeaturepacksubscriptionkeysincloudmodeshareapoolofoneormorefeaturepack
subscriptionkeysmanagedusingtheHPENetworkingsupportportal.Bydefault,aswitchusinganHPE
ArubaNetworkingCXfeaturepackincloudmodewillcontactthe HPENetworkingsupportportaloncea
daytoautomaticallysynchronizewiththefeaturepacksubscriptionkeymanagementdatabase.With
thisdeploymenttype,theHPENetworkingsupportsitecanautomaticallydistributeandmanage
featurepacksforalldevicesinagroup,makingitascalablesolutionforlargerdeploymentsandfor
globalaccountsacrossgeographies.
Networkswithasingleswitch,orwithmultipleswitchesonisolatednetworksthatcannotcontactthe
HPENetworkingsupportsiteshouldusefeaturepacksubscriptionkeysinfile-basedmode,wherea
featurepackismanuallyenabledonaswitchusinganon-sharablesubscriptionkeytiedtothat
individualswitch'sserialnumberorMACaddress.
Honormodeisintendedforcaseswhereavalidfeaturepackforadvancedfeatureshasbeen
purchased,butisnotyetinstalledonthedevice.Advancedfeaturesonthisdevicewillbeoperationalin
Honormode,butawarningmessagemaybeseenuntilavalidfeaturepackisinstalled.Pleasenotethat
HPEArubaNetworkingwillremovesupportforHonormodeinafuturereleaseandadvancedfeatures
willonlybeoperationaliftheapplicablesubscriptionfeesarepaidandavalidfeaturepackisinstalled.
Examples
| switch(config)#     | feature | pack mode | cloud-managed     |
| ------------------- | ------- | --------- | ----------------- |
| Command History     |         |           |                   |
| Release             |         |           | Modification      |
| 10.13               |         |           | Commandintroduced |
| Command Information |         |           |                   |
| Platforms           | Command | context   | Authority         |
config
| 6300 |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith  |
| ---- | --- | --- | ----------------------------------------------------- |
| 6400 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| 8100 |     |     | commandfromtheoperatorcontext(>)only.                 |
8320
8325
8325H
8325P
Featurepackcommands|50

Platforms

Command context

Authority

8360
8400
9300
9300S
10000
10040

feature-pack server
feature-pack server
block <block>
credentials user <USER> password [{plaintext <PASSWORD>}|{ciphertext <PASSWORD>}]
location <LOCATION> [vrf <VRF>]
pool <pool>

Description

If the switch is in cloud-managed feature pack mode, use this command to define the switch's feature
pack profile. A switch in cloud-managed mode uses the information in this profile to contact the feature
pack management server and download and install any allocated feature packs.

Parameter

block <block>

credentials

user <USER>

password

plaintext <PASSWORD>

Description

If the subscription pool for the profile contains more than one
subscription block, specify the subscription block within that pool
to be assigned.

Configures the credentials used by the device to contact and
authenticate to the feature pack server.

The user name of a feature pack server account.

Select a mode for entering the feature pack server password. If
you press <enter> after the password parameter, you will enter a
secure prompt that allows you to securely enter a hidden
password. This is the recommended method for entering a plaintext
password.

You can include the optional plaintext parameter to configure a
plain text password (not recommended), or use the optional
ciphertext parameter to enter previously encrypted ciphertext
password.

Optional. Enter a password in plain text without the secure
prompt. This option does not hide the password in the CLI, and is not
recommended.

ciphertext <PASSWORD>

Optional. Enter a password as previously encrypted text. This is the
recommended method for entering an encrypted password.

location <LOCATION>

The FQDN of the feature pack server;
https://cx-feature-pack.arubanetworks.com

[vrf <VRF>]

(Optional) Specify the VRF used to contact the feature pack server.

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

51

Parameter Description
pool <pool> Configuresthefeaturepackserversubscriptionpool.This
informationisusedbythefeaturepackservertoproperlyidentify
thesubscriptiontobeassignedtothedevice.
Examples
Definingafeaturepackserverbyenteringahiddenplaintextuserpassword.
| switch(config)# | feature-pack | server |     |
| --------------- | ------------ | ------ | --- |
switch(config-feature-pack-server)# location https://cx-feature-
| pack.arubanetworks.com |     | vrf mgmt |     |
| ---------------------- | --- | -------- | --- |
switch(config-feature-pack-server)# credentials user myLMSUser1234 password
| Enter password:   | ***** |     |     |
| ----------------- | ----- | --- | --- |
| Confirm password: | ***** |     |     |
Definingafeaturepackserverwithanencryptedciphertextuserpassword.
| switch(config)# | feature-pack | server |     |
| --------------- | ------------ | ------ | --- |
switch(config-feature-pack-server)# location https://cx-feature-
| pack.arubanetworks.com |     | vrf mgmt |     |
| ---------------------- | --- | -------- | --- |
switch(config-feature-pack-server)# credentials user myLMSUser1234 password
ciphertext
AQBapcmUTsCVdaTGkLA3mN2sslLgsNOdqFUP0j+CaCxVdz7oEwAA2OmsmBmgPHavS+6Gkgm2twE4NU1Y=
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Release Modification
10.13.1000 Plaintextpasswordsshouldnowbeconfiguredusingthesecure
prompt,whichcanbeaccessedbypressing<enter>afterthe
passwordkeyword.Thismakestheplaintextandciphertext
keywordsoptional.Itisrecommendedtouseeitherthesecure
promptortheciphertextoption.
10.13 Commandintroduced
| Command Information |         |         |                                           |
| ------------------- | ------- | ------- | ----------------------------------------- |
| Platforms           | Command | context | Authority                                 |
| 6300                | config  |         | OperatorsorAdministratorsorlocalusergroup |
6400 config-feature-pack-server memberswithexecutionrightsforthiscommand.
| 8100 |     |     | Operatorscanexecutethiscommandfromthe |
| ---- | --- | --- | ------------------------------------- |
operatorcontext(>)only.
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
Featurepackcommands|52

| feature-pack | validate |     |     |
| ------------ | -------- | --- | --- |
| feature-pack | validate |     |     |
Description
ManuallytriggerafeaturepackvalidationontheHPENetworkingsupportportal.(Bydefault,automatic
validationhappensonceeveryday.)Thiscommandisonlyapplicableforfeaturepacksincloud-
managedmode.
Examples
| switch# feature-pack |         | validate |                   |
| -------------------- | ------- | -------- | ----------------- |
| Command History      |         |          |                   |
| Release              |         |          | Modification      |
| 10.13                |         |          | Commandintroduced |
| Command Information  |         |          |                   |
| Platforms            | Command | context  | Authority         |
6300 manager Administratorsorlocalusergroupmemberswithexecution
| 6400 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
show feature-pack
| show feature-pack | [server] |     |     |
| ----------------- | -------- | --- | --- |
Description
Displaythecurrentfeaturepacksummaryandstatus,andfeaturestatusoffeaturesthatrequirea
featurepack.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
server (Optional)Forfeaturepacksincloud-managedmode,Includethis
parametertodisplayconfigurationsettingsusedtoconnecttothe
featurepackmanagementserver,anddisplaytheconnection
statusinformation.
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 53

Examples
| switch# | show | feature-pack |     |     |     |     |     |     |
| ------- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
| Feature | Pack | Summary      |     |     |     |     |     |     |
===============
| Name         |           | : CX                | Software | Advanced |           | Feature | Pack         |         |
| ------------ | --------- | ------------------- | -------- | -------- | --------- | ------- | ------------ | ------- |
| Expiration   | Date      | : Thu               | May      | 4 2025   |           |         |              |         |
| Serial       | Number(s) | : TW13KM304V        |          |          |           |         |              |         |
| MAC Address  |           | : 90:20:c2:c4:98:00 |          |          |           |         |              |         |
| Hostname     |           | : 6405              |          |          |           |         |              |         |
| Mode         |           | : File              | based    |          |           |         |              |         |
| Status       |           | : feature           |          | pack     | installed | and     | valid        |         |
| Error Reason |           | : None              |          |          |           |         |              |         |
|              |           |                     |          |          |           |         | Subscription | Feature |
| Feature      |           |                     |          |          |           |         | Status       | Status  |
---------------------------------------------------------------------
| Application | Based      | Policy |     |     |     |     | active | allowed |
| ----------- | ---------- | ------ | --- | --- | --- | --- | ------ | ------- |
| MACsec      | extensions | for    | WAN |     |     |     | active | allowed |
Reflexive Policies for Port Access GBP Clients active allowed
| Reflexive | Policies | for  | Port         | Access | Clients |     | active | allowed |
| --------- | -------- | ---- | ------------ | ------ | ------- | --- | ------ | ------- |
| switch#   | switch#  | show | feature-pack |        | server  |     |        |         |
Profile
=======
| Location     | URL |       | : https://cx-feature-pack.arubanetworks.com |     |     |     |     |     |
| ------------ | --- | ----- | ------------------------------------------- | --- | --- | --- | --- | --- |
| Location     | VRF |       | : mgmt                                      |     |     |     |     |     |
| User account |     |       | : customer@example.com                      |     |     |     |     |     |
| Subscription |     | Pool  | : default                                   |     |     |     |     |     |
| Subscription |     | Block | : 6300_test_block_2                         |     |     |     |     |     |
Connection
==========
| Status          |            |      | : Validation |     | success     |     |          |     |
| --------------- | ---------- | ---- | ------------ | --- | ----------- | --- | -------- | --- |
| Reason          |            |      | : --         |     |             |     |          |     |
| Last validation |            | time | : Tue        | Sep | 12 09:27:42 |     | UTC 2023 |     |
| Success         | validation | time | : Tue        | Sep | 12 09:27:42 |     | UTC 2023 |     |
Theoutputoftheshow feature-packcommandincludethefollowinginformation:
| Value          |     |     |     |     | Description                                  |     |     |     |
| -------------- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- |
| Name           |     |     |     |     | Nameofthefeaturepack                         |     |     |     |
| ExpirationDate |     |     |     |     | Thedatethatthefeaturepacksubscriptionexpires |     |     |     |
SerialNumbers Serialnumbersforthatfeaturepack.Ifthefeaturepackisusedby
multipleswitches(forexample,inaVSFdeployment)thenthe
SerialNumber(s)fielddisplaysalltheswitchserialnumbersfor
thatfeaturepack.
| MACaddress |     |     |     |     | MACaddressoftheswitchusingthefeaturepack |     |     |     |
| ---------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
| Hostname   |     |     |     |     | Hostnameoftheswitchusingthefeaturepack   |     |     |     |
| Type       |     |     |     |     | Showsthefeaturepackfiletype:             |     |     |     |
n Devicespecific:Featurepackwasmanuallydownloadedfrom
afeaturepackserveraccountinlocalmode.Usethisfeature
Featurepackcommands|54

Value

Description

Mode

Status

pack with a switch in file-based mode..

n Floating: The feature pack was automatically downloaded

from a cloud mode feature pack account on the HPE

Networking support portal. This feature pack should be used

with the switch in cloud-managed mode.

Shows the feature pack configuration mode:

n Cloud management: Switches using feature pack

subscriptions in cloud-managed mode share a pool of one or

more feature pack subscriptions. These subscriptions are

managed through the HPE Networking support portal.
n File Based: If a switch is using a feature pack in file-based

mode, you must manually upload the feature pack using the

copy command and enable it on a switch using a non-sharable

subscription file tied to that individual switch's serial number

or MAC address.

n Honor: Honor mode is intended for cases where a valid

feature pack for advanced features has been purchased, but is

not yet installed on the device. Advanced features on this

device will be operational in honor mode, but a warning

message may be seen until a valid feature pack is installed.

Please note that HPE Aruba Networking will remove support

for Honor mode in a future release and advanced features will

only be operational if the applicable subscription fees are paid

and a valid feature pack is installed. This message is shown
when the switch is configured to use a cloud-managed feature

pack profile using the feature pack mode cloud-managed

command.

This message displays the current status of the feature pack:

n No feature pack installed: No feature pack is detected on the

switch.

n Feature pack installed and valid: Feature pack installed with

no errors.

n Feature pack install error: The feature pack has invalid data.
n Feature pack expired: The feature pack subscription has

expired.

n Feature pack removed: The feature pack was erased from

the switch using the erase command.

n Subscription through HPE Aruba Networking Central is

connected: Switch is actively connected to HPE Aruba

Networking Central. Subscription features are operational. The

feature-pack on the switch will display this state only if all the

following are true:

o The switch has a connection to HPE Aruba Networking

Central.

o The switch is onboarded to the GreenLake for PrivateCloud

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

55

Value

Description

(GLPC) device inventory .

o The switch is assigned to HPE Aruba Networking Central

Application.

o The switch has a valid HPE Aruba Networking Central

License assigned.

n Subscription through HPE Aruba Networking Central is

disconnected: Switch is disconnected from HPE Aruba

Networking Central. Subscription features are still operational.

The switch will appear in this state if any of the requirements

for the status is not currently true, A switch may also display

this feature pack status if the switch has connection to HPE

Aruba Networking Central, is assigned to the Central

application, but has no Central License attached. In this case

the switch will be in disconnected state even if it never was

previously in connected state.

n Feature pack mode honor configured: The switch does not

have a valid feature pack. Subscription features are

operational, and is operating in honor mode until the feature

pack is installed.

n Cloud managed server is disconnected: The switch is

managing feature packs in cloud mode, but the switch is no

longer able to reach the HPE Networking support portal. The

switch will continue to operate in honor mode.

n Cloud managed and subscription revoked from server:

The switch is managing the feature pack in cloud mode, but
feature pack has been revoked from the switch through the

HPE Networking support portal.The switch will continue to

operate in honor mode until the feature pack is removed from

the switch.

n Cloud managed server validation error: Server validation

failed. Issue the command show feature pack server for

more information.

n Unexpected VSF member in stack: A feature pack intended

for a VSF stack is installed on a VSF member whose serial

number is not covered under the current feature pack.
n Mode does not match installed feature pack type: The

feature pack type (device-locked or floating) does not match

the configured mode. Device-locked feature packs should be

used in file-based deployments only, and floating feature

packs should be used by cloud-managed deployments.

If the feature pack Status field displays an error status, this field
displays details about possible causes for the issue.

n Serial number mismatch: The serial number in the installed

feature pack does not match the switch's serial number.
n MAC address mismatch: The MAC address in the installed

feature pack does not match the switch's serial number.

Feature pack commands | 56

Error Reason

Value

Description

n Feature pack file parsing error: The feature pack file has an

invalid format.

n Feature pack file signature invalid: The feature pack file was

modified.

Feature

Name of the feature supported by the feature pack.

Subscription Status

Current subscription status;

n active: Subscrition is active.
n inactive: Subscription is inactive or has expired.
n honor: Installed feature pack has expired or cloud managed

feature pack has encountered an error. Warnings will be

logged periodically.

Feature Pack Status

Current status of the feature pack:

n allowed: Feature is functional.
n blocked: Feature is not functional and will require a valid

feature pack to be functional.

n not running: Feature is not configured on switch and daemon

is not running

n unsupported on SKU: Feature is not supported on product

SKU.

n unsupported with VSF: Feature is not supported on a VSF

stack.

The output of the show feature-pack server command include the following information:

Location URL

Location VRF

User Account

Subscription Pool

Fully qualified domain name of the feature pack subscription
server, for example, https://cx-feature-
pack.arubanetworks.com

VRF used to access the feature pack subscription server.

User name of the user account at the HPE Networking support
portal associated with the feature pack.

Name of the subcription pool associated with the feature pack.
This can be the Default subscription pool, or a user-defined
subscription pool.

Subscription Block

Subscription block associated with the feature pack.

Status

Reason

Indicates whether the switch was able to contact the feature pack
server.

If the switch is unable to contact the feature pack server, this field
can display information about the cause for the connection
failure.

Last validation time

Timestamp showing the date and time the switch last contacted
the feature pack server.

Success Validation time

Timestamp showing the date and time of the last successful

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

57

featurepackinstallationorvalidationagainstthefeaturepack
server
| Command | History |     |     |     |                                                       |     |
| ------- | ------- | --- | --- | --- | ----------------------------------------------------- | --- |
| Release |         |     |     |     | Modification                                          |     |
| 10.16   |         |     |     |     | Theoutputofthiscommandnolongerdisplaysthesubscription |     |
statusoftheApplicationRecognitionfeature,asthisfeatureno
longerrequiresafeaturepacksubscription.
| 10.13     |             |     |         |     | Commandintroduced |     |
| --------- | ----------- | --- | ------- | --- | ----------------- | --- |
| Command   | Information |     |         |     |                   |     |
| Platforms | Command     |     | context |     | Authority         |     |
6300 manager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6400
8100
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
10040
| Frequently |     | Asked |     | Questions |     | (FAQs) |
| ---------- | --- | ----- | --- | --------- | --- | ------ |
Thefollowingsectionsofthisdocumentanswerfrequentlyaskedquestions(FAQs)aboutAOS-CX
featurepacksandfeaturepackmanagement.SelectanycategorybelowtofewFAQsandanswersfor
thatcategorytype.
n GeneralFeaturePackFAQs
n AdvancedFeaturePackFAQs
n 10000SwitchSeriesFeaturePackFAQs
n SubscriptionManagementFAQs
FeaturePackDomain/SubaccountFAQs
n
n FeaturePackExpirationandRenewalFAQs
n VSFandVSXFAQs
| General   | Feature    |     | Pack  | FAQs       |     |     |
| --------- | ---------- | --- | ----- | ---------- | --- | --- |
| What type | of feature |     | packs | do I need? |     |     |
FrequentlyAskedQuestions(FAQs)|58

The choice of feature pack depends on your desired features. AOS-CX features are organized into a set
of native enterprise features available in every CX switch at no cost, and an optional, term-based
Advanced Feature Pack for 6300, 6400, 8xxx, and 9300 Switch series. Feature packs can be consumed
standalone or combined with a Central Advanced subscription. The 10000 Switch series require a
Advanced Feature Pack, which can be optionally replaced by a Premium Feature Pack to support
additional features.

Will I receive switch software updates even if I do not purchase a Feature Pack?

AOS-CX software updates are not contingent upon whether a customer has purchased a feature pack.
HPE Aruba Networking will continue to maintain and enhance the native functionalities of the AOS-CX
operating system, making them available to customers through the regular AOS-CX software release
cycle.

At any point of time, how many feature packs can a CX switch have?

A switch can have one single feature pack, or can operate with no feature pack installed. A switch cannot
have more than one feature pack.

Does switch platform define the required type of feature packs for product?

The software feature set drives the requirement for Feature Pack. There is only one Advanced Feature
Pack for 6300, 6400, 8xxx, and 9300 Switch series. Only 10000 switch series offers two options: an
Advanced Feature Pack and a Premium Feature Pack.

How I know which features are strictly enforced and cannot be used without a
subscription?

The output of the show feature-pack provides this information per switch platform.

Advanced Feature Pack FAQs

What will happen when I configure an advanced feature without a Feature Pack?

When a user configures an advanced feature the CLI will display a warning. In honor-based enforcement
the user is warned that an advanced feature is in use, and it will operate normally. In Strict enforcement
mode, the user is warned that a feature is advanced, and the feature will not operate until a valid
feature pack is installed. Note: all configurations are accepted with warnings. Features become
operational depending on the enforcement mode.

Can I upgrade to the CX Advanced Feature Pack once I have purchased a switch?

Yes. You can upgrade to a CX Advanced Feature Pack after a switch purchase.

If I already own an HPE Aruba Networking Central Advanced subscription, is there any
need to purchase CX Software Advanced feature pack subscription?

If you have a Central Advanced subscription for6300, 6400, 8xxx, and 9300 Switch series, there is no
need to purchase a CX Advanced Feature Pack.

A Central Advanced subscription automatically enables CX features included in the CX Advanced Feature
Pack. Note that the 10000 Switch series does require a feature pack, even if you already own a Central
Advanced subscription for a CX 10000 switch.

If I purchased a 1-year CX Advanced Feature Pack for a switch, after one year can I
alter my plan to 3-year subscription?

Yes. HPE Aruba Networking does allow you to alter subscription plans.

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

59

If I purchased 3-year CX Advanced Feature Pack for a 10000 Switch, can I upgrade after
one year from the current CX Advanced subscription to the CX Premium Feature Pack?

Currently there is no automated upgrade option, but HPE Aruba Networking sales can provide a manual
upgrade option.

Can I purchase an Advanced Feature Pack subscription for all the HPE Aruba
Networking CX switch series?

No. The Advanced Feature Pack is only available for the 6300, 6400, 8100, 8320, 8325, 8360, 8400, 9300,
and 10000 Series switches. There is no requirement or option to purchase any feature pack for 4100i,
6000, and 6100 platforms.

What features are supported in each CX series with purchase of CX Advanced and
Premium feature packs?

For platform-specific advanced feature support, refer to the HPE Aruba Networking Switch Feature
Navigator.

How do I can get a temporary CX Advanced Feature Pack subscription to perform a
demo for new advanced features?

Contact your HPE Aruba Networking sales representative for more information about a 90-day CX
Advanced Feature Pack Eval subscription. Eval feature packs are intended for evaluation purposes only
and are not meant for production deployments.

10000 Switch Series Feature Pack FAQs

Is there any Evaluation feature pack for the 10000 Switch series ?

Yes. There is a CX Advanced Feature Pack Eval subscription and a CX Premium Feature Pack Eval
subscription for 10000 Switch series.

How are feature pack enforced on the 10000 Switch series platform, considering that
some features are deployed from AMD Pensando PSM, and strict enforcement cannot
be applied to them?

Since the policy features are deployed from AMD Pensando Policy and Services Manager (PSM), PSM-
specific features on the 10000 Switch series are not enforced. Non-PSM features like Container are
subject to enforcement in AOS-CX.

Are all AOS-CX 10000 features available under the CX Premium Feature Pack?

Yes. Several 10000 Switch series features are available in both the CX Advanced Feature Pack and the CX
Premium Feature Pack, but some select features will only be available with CX Premium.

How do the feature pack warning message on 10000 Switch series differ from other CX
platforms?

n All platforms log a warning message when an advanced feature is used without a valid feature pack
while in honor mode. However, 10000 Switch series will also log a warning message if no feature
pack is found, regardless of whether advanced features are used.

n A 10000 Switch series displays warning messages if a user configures advanced features while no

feature pack file is installed.

Frequently Asked Questions (FAQs) | 60

| Subscription |         | Management |         |             | FAQs    |     |        |
| ------------ | ------- | ---------- | ------- | ----------- | ------- | --- | ------ |
| How do       | I place | an order   | for the | CX Software | feature |     | packs? |
OrdersareprocessedbyanHPEArubaNetworkingrepresentative.Youmusthaveanaccountonthe
HPEArubanetworkinglicensingmanagementportaltoactivateyourorders.
Does the HPE Aruba Networking licensing management portal support Multi-Factor
Authentication (MFA) for feature packs in cloud-managed mode?
Multi-FactorAuthentication(MFA)issupportedonHPEuseraccountsandMFAiscompatiblewithall
featurepackmodesandmanagementmethods.MFAisbothsupportedandrecommended.
| Feature |     | Pack | Domain/Subaccount |     |     | FAQs |     |
| ------- | --- | ---- | ----------------- | --- | --- | ---- | --- |
Can users with access to a subaccount of a feature pack domain view or access feature
| packs | within | another | user account | of  | that domain? |     |     |
| ----- | ------ | ------- | ------------ | --- | ------------ | --- | --- |
No.Ausercannotcreateafeaturepackpoolinanydomainoruseraccountotherthantheirown.
However,ifauseraccountisaddedtomultipledomainsintheHPEArubaNetworkingsupportportal
thenthatuseraccountcanviewandaccessfeature-packsinthosemultipledomains.Itisimportantto
notethatauseraccountcanonlyhaveonedomainasits“primaryaccount”.Ifauseraccountispartof
multipledomains,thenwhenthatuseraccount’scredentialsareconfiguredontheswitchforcloud-
managedfeature-packs,theHPEArubaNetworkingsupportportalwillconnectthatswitchtothe
domainassignedastheuser’sprimaryaccount.
If I already created a subaccount for a feature pack domain, can I create another
| subaccount |     | within the | first subaccount? |     |     |     |     |
| ---------- | --- | ---------- | ----------------- | --- | --- | --- | --- |
No.Youcannotcreateasubaccountwithinanothersubaccount.
| Feature |     | Pack | Revocation | FAQs |     |     |     |
| ------- | --- | ---- | ---------- | ---- | --- | --- | --- |
What user roles within a feature pack domain account have access to this view or
| revoke | a feature | pack? |     |     |     |     |     |
| ------ | --------- | ----- | --- | --- | --- | --- | --- |
BothAdminandstandarduserscanviewfeaturepackdetails,butonlyAdminuserswillbeableto
revokeafeaturepack.
| Feature |         | Pack         | Expiration | and      | Renewal     |     | FAQs  |
| ------- | ------- | ------------ | ---------- | -------- | ----------- | --- | ----- |
| What    | happens | if a feature | pack       | expires? | Do services |     | stop? |
Whenafeaturepackexpires,advancedfeaturesarenotoutofserviceimmediately.Thesefeatureswill
continuetoworkinhonormode.Thismodeprovidesawarningmessagethatremindsuserstorenew,
yetavoidsstrictenforcementthatcandisableafeatureandpotentiallycausenetworkdisruptions.
| How can | I track | feature | pack expirations |     | and renewals? |     |     |
| ------- | ------- | ------- | ---------------- | --- | ------------- | --- | --- |
Featurepackrenewalcanbeautomatedordonemanually.TheHPEArubaNetworkingsupportportal
allowsuserstomonitorfeaturepackstheyhavegenerated,andorderanewfeaturepacktoreplace
oneabouttoexpire.Withautomatedrenewal,ifafeaturepackhasexpired,theSupportPortalwill
triggeranauto-renewalorderavailableforthenumberoffeaturepacksthatmustberenewed,if
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 61

available. The Support Portal will then activate the new feature packs to allow the switch to undergo
auto-renewal of its feature pack.

VSF and VSX FAQs

If I want to enable advanced features on a 6300 Switch series VSF stack, then how
many feature packs do I need to purchase?

Stacked switches are required to have one feature pack per member,

I have a VSF stack of five members, each having its own feature pack. If I add a new
member and there is no feature pack available in feature pack pool within LMS, then
does entire stack stop working?

No, the stack continues to work. One of the key benefits of the HPE Aruba Networking subscription
model is that a network is not impacted by a feature pack going invalid – this includes a feature pack
expiring, or a scenario where a valid, subscribed stack is changed to include an unsubscribed member.

What happens if the MAC/serial of a device added to a VSF stack is not included in the
feature pack file?

The feature pack file contains the MAC/serial of each subscribed member, so any MAC/serial in the
stack but not present in the feature pack file is considered an unsubscribed device.

How frequently are critical event messages logged when a switch operates without a
valid feature pack for a specific feature?

Critical event messages will be logged to indicate that the system is operating with an invalid feature
pack. These messages will be generated twice a day for each feature used without a valid feature pack.

Can I manage a subscription from the conductor in a VSF stack?

Yes. The VSF stack conductor is responsible for all the feature pack management for that stack, and the
feature pack is installed as a bundle for all the members.

Can I manage a subscription from primary device in a VSX cluster?

Feature packs on a VSX cluster are not managed only from the VSX primary node. In a VSX cluster, both
nodes, primary and secondary, must manage their own feature packs independently.

Frequently Asked Questions (FAQs) | 62

Chapter 8
|                 |     |     |         | Troubleshooting |        | Feature | Pack Issues |
| --------------- | --- | --- | ------- | --------------- | ------ | ------- | ----------- |
| Troubleshooting |     |     | Feature | Pack            | Issues |         |             |
UsethefollowingworkflowstoidentifyandfixproblemswithyourArubaCXfeaturepackdeployment.
| How     | do I know | there        | is a | feature  | pack issue? |     |     |
| ------- | --------- | ------------ | ---- | -------- | ----------- | --- | --- |
| Warning | Logs from | Subscription |      | Features |             |     |     |
FeaturesthatrequireaCXfeaturepackwillgeneratewarningeventlogsifavalidfeaturepackis
missing.
Forexample,theApplicationBasedPolicyfeaturewillgeneratethefollowinglogmessageifthefeature
ismissingavalidfeaturepack,eventhoughthefeatureisstilloperational.Thislogmessagecanbe
triggeredbyscenariossuchasfeaturepackexpiration,oralossofconnectiontotheHPEAruba
Networkingsupportportal.
Event|10536|LOG_WARN|CDTR|1|Policy policy1 is of type ABP and a valid feature pack
is required to use the policy. The policy is currently in use without a valid
| feature | pack. |     |     |     |     |     |     |
| ------- | ----- | --- | --- | --- | --- | --- | --- |
IftheApplicationBasedPolicyfeatureisblockedduetoamissingorinvalidfeaturepack,thenthe
switchwillgeneratethefollowinglogmessage.Thisissuecanoccurifthefeaturehasneverhadavalid
featurepack,oriftheswitchhasbeenzeroized.
Event|10535|LOG_ERR|CDTR|1|Policy policy1 is of type ABP and a valid feature pack
is required to use the policy. All clients associated with this policy will be
| unauthorized | until | a valid | feature | pack is | installed. |     |     |
| ------------ | ----- | ------- | ------- | ------- | ---------- | --- | --- |
Iftheswitchdisplayswarninglogsforasubscriptionfeature,refertoReasonsforFeaturePackIssuesfor
helpwithidentifyingandresolvingtheissue.
| Feature-Pack | Show | Commands |     |     |     |     |     |
| ------------ | ---- | -------- | --- | --- | --- | --- | --- |
Theswitchcommand-lineinterfaceincludesfeature-packshowcommandstodisplaythestatusofthe
featurepackandsubscriptionfeaturesontheswitch.Theshowfeature-packandshowfeature-pack
servercommandswilldisplayanerrormessageifthereisafeature-packrelatedissue.
| Reasons | for Feature |     | Pack | Issues |     |     |     |
| ------- | ----------- | --- | ---- | ------ | --- | --- | --- |
Iftheeventlogsorshowcommandsareshowingerrorsontheswitch.Thesecommandswilldisplayan
errormessageifthereisafeaturepackrelatedissue.
| Feature | is blocked | by  | missing | feature | pack |     |     |
| ------- | ---------- | --- | ------- | ------- | ---- | --- | --- |
63
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries)

Whenafeatureisblockedduetoaninvalidormissingfeaturepack,theshow feature-packcommand
willdisplaytheSubscription StatusasinactiveandFeature Statusasblocked.Toresolvethisissue,
installavalidfeaturepackontotheswitch.Formoreinformation,seeDeployingaCloud-managed
FeaturePackSolutiononaStandaloneSwitchorDeployingaFile-BasedFeaturePackSolutionona
StandaloneSwitch.
| 6300# show | feature-pack |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| Feature    | Pack Summary |     |     |     |     |     |     |     |
====================
| Name         |           | : --   |         |      |           |              |         |     |
| ------------ | --------- | ------ | ------- | ---- | --------- | ------------ | ------- | --- |
| Expiration   | Date      | : --   |         |      |           |              |         |     |
| Serial       | Number(s) | : --   |         |      |           |              |         |     |
| MAC Address  |           | : --   |         |      |           |              |         |     |
| Hostname     |           | : --   |         |      |           |              |         |     |
| Type         |           | : --   |         |      |           |              |         |     |
| Mode         |           | : File | Based   |      |           |              |         |     |
| State        |           | : No   | feature | pack | installed |              |         |     |
| Error Reason |           | : --   |         |      |           |              |         |     |
|              |           |        |         |      |           | Subscription | Feature |     |
| Feature      |           |        |         |      |           | Status       | Status  |     |
-----------------------------------------------------------------------
| Application | Based      | Policy |     |     |     | inactive | blocked |     |
| ----------- | ---------- | ------ | --- | --- | --- | -------- | ------- | --- |
| MACsec      | extensions | for    | WAN |     |     | inactive | blocked |     |
Reflexive Policies for Port Access GBP Clients inactive blocked
| Reflexive | Policies | for | Port | Access | Clients | inactive | blocked |     |
| --------- | -------- | --- | ---- | ------ | ------- | -------- | ------- | --- |
The Switch is Out of Sync with the HPE Aruba Networking Support
Portal
IfchangeshavebeenmadeontheswitchortheHPEArubaNetworkingsupportportal,andtheswitch
featurepackstateisout-of-date,issuethefeature-packvalidatecommandtoforcetheswitchto
immediatelysynchronizewiththesupportportal.
| HPE Aruba | Networking |          |     | Support | Portal | account | is locked | after |
| --------- | ---------- | -------- | --- | ------- | ------ | ------- | --------- | ----- |
| changing  | the        | password |     |         |        |         |           |       |
AnetworkadminusingfeaturepacksincloudmodemayexperiencealockoutoftheirHPEaccount
afterchangingtheirpasswordduetotheswitchessyncingwiththeoldpassword.Whenchangingthe
passwordoftheuseraccountcredentialsconfiguredonswitchesforcloud-managedsubscriptions,use
thefollowingtoavoidunexpectedaccountlockouts:
1. Configureallswitchesintofile-modeusingthecommandfeature-pack mode file-based.This
willpreventtheswitchesfromsyncingwiththeHPENetworkingSupportPortalduringthe
passwordchangeprocess.
Note:Thiswillcausetheswitchestomoveintohonormodeduetoamismatchbetweenfeature-packtypeand
configuredmode,butsubscriptionfeatureswillremainoperational.
2. ProceedwiththepasswordchangeontheHPEuseraccount.
3. Configurethenewpasswordoneachswitchusingthesecurepromptorciphertextoptions.
Usingsecureprompt:
TroubleshootingFeaturePackIssues|64

switch (config-feature-pack-server)# credentials user <USER> password
<enter>”.
Usingciphertext:
switch (config-feature-pack-server)# credentials user <USER> password
|     | ciphertext | <CIPHERTEXT>” |     |     |     |     |     |
| --- | ---------- | ------------- | --- | --- | --- | --- | --- |
4. Configureeachswitchintocloud-managedmodeusingthecommandfeature-pack mode
cloud-managed,thenverifysubscriptionsarevalidatedusingshow feature-pack serverand
| show    | feature-pack. |      |         |        |     |     |     |
| ------- | ------------- | ---- | ------- | ------ | --- | --- | --- |
| Missing | Feature       | Pack | Profile | Fields |     |     |     |
Thefeaturepackprofileontheswitchrequiresalocation,useraccountcredentials,andsubscription
poolinformation.Ifanyofthosefieldsaremissing,theoutputoftheshow feature-pack server
commandwillindicatethattherearemissingprofilefields.Configurethemissingfieldstoresolvethe
errorandconnecttothesupportportal.
| 6405# | show feature-pack |     | server |     |     |     |     |
| ----- | ----------------- | --- | ------ | --- | --- | --- | --- |
Profile
=======
| Location     | URL     | :       | --      |     |     |     |     |
| ------------ | ------- | ------- | ------- | --- | --- | --- | --- |
| Location     | VRF     | :       | default |     |     |     |     |
| User         | account | :       | --      |     |     |     |     |
| Subscription |         | Pool :  | --      |     |     |     |     |
| Subscription |         | Block : | --      |     |     |     |     |
Connection
==========
| Status     |            |        | : Invalid | profile     | configuration         |         |      |
| ---------- | ---------- | ------ | --------- | ----------- | --------------------- | ------- | ---- |
| Reason     |            |        | : missing | fields for  | profile configuration |         |      |
| Last       | validation | time   | : Wed Oct | 18 22:06:09 | UTC 2023              |         |      |
| Success    | validation | time   | : --      |             |                       |         |      |
| Connection | Failure    |        | to the    | HPE Aruba   | Networking            | Feature | Pack |
| Support    | Portal     | Server |           |             |                       |         |      |
Whentheswitchcannotconnecttothesupportportalserver,theshow feature-pack servercommand
displaysthefollowingoutput.VerifythattheswitchhasinternetaccessandDNScanresolvetheHPE
ArubaNetworkingsupportportalFQDN(https://cx-feature-pack.arubanetworks.com).
| 6405# | show feature-pack |     | server |     |     |     |     |
| ----- | ----------------- | --- | ------ | --- | --- | --- | --- |
Profile
=======
| Location     | URL     | :       | https://cx-feature-pack.arubanetworks.com |     |     |     |     |
| ------------ | ------- | ------- | ----------------------------------------- | --- | --- | --- | --- |
| Location     | VRF     | :       | mgmt                                      |     |     |     |     |
| User         | account | :       | customer@example.com                      |     |     |     |     |
| Subscription |         | Pool :  | Default                                   |     |     |     |     |
| Subscription |         | Block : | 6300_block_4                              |     |     |     |     |
Connection
==========
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 65

| Status |     |     | :   | Connection | failed |     |     |
| ------ | --- | --- | --- | ---------- | ------ | --- | --- |
Reason : connection to the feature pack server was attempted, but
failed
| Last validation |            | time | :   | Wed Oct | 18 22:16:34 | UTC 2023 |     |
| --------------- | ---------- | ---- | --- | ------- | ----------- | -------- | --- |
| Success         | validation | time | :   | --      |             |          |     |
Connectivityissuescanalsobecausedbyinternetaccesssecurityrules,web-proxyissues,orDNSname
resolutionfailures.CheckyoursecuritysettingsandensurethatDNSisconfiguredontheswitch.
Mode Mismatch
Thefeaturepackmodeconfiguredontheswitchprofile(cloud-managedorfile-based)mustmatchthe
featurepacktypethatisinstalledontheswitch.Ifyouconfiguretheswitchwiththecommandfeature-
pack mode cloud-managed,theswitchmustuseafloatingfeaturepack.Ifyouconfiguretheswitch
withthecommandfeature-pack mode file-based,theswitchmustuseadevice specificfeaturepack.
iftheswitchhasafloatingfeaturepackinstalledwhileinfile-basedmode,theswitchwilldisplaythe
| followingerrorintheoutputoftheshow |              |         |     | feature-packcommand. |     |     |     |
| ---------------------------------- | ------------ | ------- | --- | -------------------- | --- | --- | --- |
| 6300# show                         | feature-pack |         |     |                      |     |     |     |
| Feature                            | Pack         | Summary |     |                      |     |     |     |
====================
| Name             |      | : CX                | Advanced | Feature    | Pack       |              |         |
| ---------------- | ---- | ------------------- | -------- | ---------- | ---------- | ------------ | ------- |
| Expiration       | Date | : Sat               | Oct      | 12 2024    |            |              |         |
| Serial Number(s) |      | : SG2Zxxxxx1        |          | SG9Zxxxxx2 | SG9Zxxxxx3 |              |         |
| MAC Address      |      | : 38:21:c7:00:00:00 |          |            |            |              |         |
| Hostname         |      | : 6300              |          |            |            |              |         |
| Type             |      | : Floating          |          |            |            |              |         |
| Mode             |      | : File              | Based    |            |            |              |         |
| State            |      | : Mode              | does     | not match  | installed  | feature pack | type    |
| Error Reason     |      | : none              |          |            |            |              |         |
|                  |      |                     |          |            |            | Subscription | Feature |
| Feature          |      |                     |          |            |            | Status       | Status  |
-----------------------------------------------------------------------
| Application       | Based | Policy |     |     |     | honor mode | allowed |
| ----------------- | ----- | ------ | --- | --- | --- | ---------- | ------- |
| MACsec extensions |       | for    | WAN |     |     | honor mode | allowed |
Reflexive Policies for Port Access GBP Clients honor mode allowed
Reflexive Policies for Port Access Clients honor mode allowed
iftheswitchhasadevice-specificfeaturepackinstalledwhileincloud-managedmode,theswitchwill
displaythefollowingerrorintheoutputoftheshow feature-packcommand.
| 6300# show | feature-pack |     | server |     |     |     |     |
| ---------- | ------------ | --- | ------ | --- | --- | --- | --- |
Profile
=======
| Location     | URL | :       | https://cx-feature-pack.arubanetworks.com |     |     |     |     |
| ------------ | --- | ------- | ----------------------------------------- | --- | --- | --- | --- |
| Location     | VRF | :       | mgmt                                      |     |     |     |     |
| User account |     | :       | customer@example.com                      |     |     |     |     |
| Subscription |     | Pool :  | Default                                   |     |     |     |     |
| Subscription |     | Block : | 6300_block_7                              |     |     |     |     |
Connection
==========
| Status |     |     | :   | File based | feature | pack installed |     |
| ------ | --- | --- | --- | ---------- | ------- | -------------- | --- |
Reason : file based feature packs are not validated against the
| feature         | pack | server |     |         |             |          |     |
| --------------- | ---- | ------ | --- | ------- | ----------- | -------- | --- |
| Last validation |      | time   | :   | Mon Oct | 16 21:24:49 | UTC 2023 |     |
TroubleshootingFeaturePackIssues|66

| Success | validation | time | : -- |     |     |     |     |
| ------- | ---------- | ---- | ---- | --- | --- | --- | --- |
Toresolvetheseerrors:
1. Changethemodeconfigurationtomatchthecurrentinstalledfeaturetype.
2. Erasethefeaturepackandreinstallanewfeaturepackofthecorrecttype.
| Invalid Block |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- |
WhentheblockconfiguredontheswitchdoesnotexistinthespecifiedpoolontheHPEAruba
Networkingsupportportal,theoutputoftheReasonsforFeaturePackIssuescommandwilldisplaya
| Server invalid | blockstatus. |     |        |     |     |     |     |
| -------------- | ------------ | --- | ------ | --- | --- | --- | --- |
| 6300# show     | feature-pack |     | server |     |     |     |     |
Profile
=======
| Location     | URL | :       | https://cx-feature-pack.arubanetworks.com |     |     |     |     |
| ------------ | --- | ------- | ----------------------------------------- | --- | --- | --- | --- |
| Location     | VRF | :       | mgmt                                      |     |     |     |     |
| User account |     | :       | plmtest@example.com                       |     |     |     |     |
| Subscription |     | Pool :  | Default                                   |     |     |     |     |
| Subscription |     | Block : | 6300_block_7                              |     |     |     |     |
Connection
==========
| Status          |            |      | : Server | invalid | block       |       |              |
| --------------- | ---------- | ---- | -------- | ------- | ----------- | ----- | ------------ |
| Reason          |            |      | : the    | feature | pack        | block | is not valid |
| Last validation |            | time | : Mon    | Oct     | 16 21:33:59 | UTC   | 2023         |
| Success         | validation | time | : --     |         |             |       |              |
Tocorrectthisissue,updatetheblockconfiguredontheswitchtomatchavalidblockintheconfigured
pool.
| Not Enough |     | Feature | Packs |     |     |     |     |
| ---------- | --- | ------- | ----- | --- | --- | --- | --- |
Ifthesubscriptionpoolorblockdoesnothaveenoughfeaturepacksfortheswitchaftertheswitch
synchronizeswiththeHPEArubaNetworkingsupportportal,thentheoutputoftheshowfeature-pack
servercommanddisplaystheServer not enough feature packsstatus.Toresolvethisissue,change
theconfiguredblockand/orpoolontheswitchtoconnecttoablockthathasfeaturepacksavailable.
| 6300# show | feature-pack |     | server |     |     |     |     |
| ---------- | ------------ | --- | ------ | --- | --- | --- | --- |
Profile
=======
| Location     | URL | :       | https://cx-feature-pack.arubanetworks.com |     |     |     |     |
| ------------ | --- | ------- | ----------------------------------------- | --- | --- | --- | --- |
| Location     | VRF | :       | mgmt                                      |     |     |     |     |
| User account |     | :       | customer@example.com                      |     |     |     |     |
| Subscription |     | Pool :  | Default                                   |     |     |     |     |
| Subscription |     | Block : | 6300_block_4                              |     |     |     |     |
Connection
==========
| Status |     |     | : Server | not | enough | feature | packs |
| ------ | --- | --- | -------- | --- | ------ | ------- | ----- |
Reason : there are not enough feature packs for the device and/or
| device stack    |            |      |       |     |             |     |      |
| --------------- | ---------- | ---- | ----- | --- | ----------- | --- | ---- |
| Last validation |            | time | : Thu | Oct | 12 18:20:59 | UTC | 2023 |
| Success         | validation | time | : Thu | Oct | 12 18:15:15 | UTC | 2023 |
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 67

| Feature | Pack |     | Already | Assigned |     |     |     |     |     |     |
| ------- | ---- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- |
IfaswitchthatisalreadyassignedafeaturepackintheHPEArubaNetworkingsupportportal,requests
anewfeaturepack,theoutputoftheshowfeature-packservercommandontheswitchwilldisplaythe
Server feature pack already assigned to deviceerroraftertheswitchconnectstotheportal.This
issuecanoccurifafeaturepackiserasedfromtheswitchbutnotrevokedinthesupportportal.To
resolvethisissueandinstallafeaturepackontheswitch,revoketheexistingfeaturepackinthe
supportportal,thentriggeramanualsynchronizationwiththeportalusingthefeature-pack validate
CLIcommand.
| 6405# | show | feature-pack |     | server |     |     |     |     |     |     |
| ----- | ---- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- |
Profile
=======
| Location     |         | URL   | :   | https://cx-feature-pack.arubanetworks.com |     |     |     |     |     |     |
| ------------ | ------- | ----- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
| Location     |         | VRF   | :   | mgmt                                      |     |     |     |     |     |     |
| User         | account |       | :   | customer@example.com                      |     |     |     |     |     |     |
| Subscription |         | Pool  | :   | Test1                                     |     |     |     |     |     |     |
| Subscription |         | Block | :   | 6400_test_block_1                         |     |     |     |     |     |     |
Connection
==========
| Status |     |     |     | :   | Server feature | pack | already | assigned |     | to device |
| ------ | --- | --- | --- | --- | -------------- | ---- | ------- | -------- | --- | --------- |
Reason : the feature pack server has already assigned a feature
| pack    | for        | this | device  |     |         |             |          |     |     |     |
| ------- | ---------- | ---- | ------- | --- | ------- | ----------- | -------- | --- | --- | --- |
| Last    | validation |      | time    | :   | Wed Oct | 18 23:11:36 | UTC 2023 |     |     |     |
| Success | validation |      | time    | :   | --      |             |          |     |     |     |
| Feature | Pack       |      | Revoked |     |         |             |          |     |     |     |
IfacloudfeaturepackforaswitchisrevokedintheHPEArubaNetworkingsupportportal,thenthe
switchwilldisplaythefollowingerrorswilloperatewithsubscriptionfeaturesenabledinhonormode.
Toreinstallafeaturepackontheswitch,issuetheerasefeature-packcommandtoerasetheexisting
feature-pack,verifythatthefeature-packprofileisconfiguredasdesired,andtriggerasyncwiththe
supportportalusingthecommandfeature-packvalidate.
| 6300#   | show | feature-pack |     |     |     |     |     |     |     |     |
| ------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Feature | Pack | Summary      |     |     |     |     |     |     |     |     |
====================
| Name       |           |      | : CX                | Advanced | Feature      | Pack |              |      |         |     |
| ---------- | --------- | ---- | ------------------- | -------- | ------------ | ---- | ------------ | ---- | ------- | --- |
| Expiration |           | Date | : Wed               | Aug      | 28 2024      |      |              |      |         |     |
| Serial     | Number(s) |      | : SG2xxxxx1         |          | SG9Zxxxx2    |      |              |      |         |     |
| MAC        | Address   |      | : 38:21:c7:5a:00:00 |          |              |      |              |      |         |     |
| Hostname   |           |      | : 6300              |          |              |      |              |      |         |     |
| Type       |           |      | : Floating          |          |              |      |              |      |         |     |
| Mode       |           |      | : Cloud             | Managed  |              |      |              |      |         |     |
| State      |           |      | : Cloud             | managed  | subscription |      | revoked      | from | server  |     |
| Error      | Reason    |      | : none              |          |              |      |              |      |         |     |
|            |           |      |                     |          |              |      | Subscription |      | Feature |     |
| Feature    |           |      |                     |          |              |      | Status       |      | Status  |     |
-----------------------------------------------------------------------
| Application |            | Based | Policy |     |     |     | honor | mode | allowed |     |
| ----------- | ---------- | ----- | ------ | --- | --- | --- | ----- | ---- | ------- | --- |
| MACsec      | extensions |       | for    | WAN |     |     | honor | mode | allowed |     |
Reflexive Policies for Port Access GBP Clients honor mode allowed
Reflexive Policies for Port Access Clients honor mode allowed
TroubleshootingFeaturePackIssues|68

| 6300# show | feature-pack |     | server |     |     |     |     |
| ---------- | ------------ | --- | ------ | --- | --- | --- | --- |
Profile
=======
| Location     | URL |       | : https://cx-feature-pack.arubanetworks.com |     |     |     |     |
| ------------ | --- | ----- | ------------------------------------------- | --- | --- | --- | --- |
| Location     | VRF |       | : mgmt                                      |     |     |     |     |
| User account |     |       | : customer@example.com                      |     |     |     |     |
| Subscription |     | Pool  | : Default                                   |     |     |     |     |
| Subscription |     | Block | : 6300_test1                                |     |     |     |     |
Connection
==========
| Status |     |     | :   | Server feature | pack | revoked |     |
| ------ | --- | --- | --- | -------------- | ---- | ------- | --- |
Reason : the device feature pack was revoked from the feature
pack server
| Last validation |            | time    | :   | Fri Oct | 6 16:48:24 | UTC 2023 |     |
| --------------- | ---------- | ------- | --- | ------- | ---------- | -------- | --- |
| Success         | validation | time    | :   | Fri Oct | 6 16:36:04 | UTC 2023 |     |
| Feature Pack    |            | Removed |     |         |            |          |     |
Ifafeature-packiserasedfromtheswitchusingtheerasefeature-packcommand,thentheswitchwill
displaythefollowingmessageandwilloperatewithsubscriptionfeaturesenabledinhonormode.The
feature-packcanbereinstalledbyfollowingthesamestepsastheinitialinstallation.SeeDeployinga
Cloud-managedFeaturePackSolutiononaStandaloneSwitchorDeployingaFile-BasedFeaturePack
SolutiononaStandaloneSwitch.
| 6300# show | feature-pack |         |     |     |     |     |     |
| ---------- | ------------ | ------- | --- | --- | --- | --- | --- |
| Feature    | Pack         | Summary |     |     |     |     |     |
====================
| Name             |      | : --      |       |              |     |              |         |
| ---------------- | ---- | --------- | ----- | ------------ | --- | ------------ | ------- |
| Expiration       | Date | : --      |       |              |     |              |         |
| Serial Number(s) |      | :         |       |              |     |              |         |
| MAC Address      |      | : --      |       |              |     |              |         |
| Hostname         |      | : --      |       |              |     |              |         |
| Type             |      | : --      |       |              |     |              |         |
| Mode             |      | : File    | Based |              |     |              |         |
| State            |      | : Feature |       | pack removed |     |              |         |
| Error Reason     |      | : none    |       |              |     |              |         |
|                  |      |           |       |              |     | Subscription | Feature |
| Feature          |      |           |       |              |     | Status       | Status  |
-----------------------------------------------------------------------
| Application       | Based | Policy |     |     |     | honor mode | allowed |
| ----------------- | ----- | ------ | --- | --- | --- | ---------- | ------- |
| MACsec extensions |       | for    | WAN |     |     | honor mode | allowed |
Reflexive Policies for Port Access GBP Clients honor mode allowed
Reflexive Policies for Port Access Clients honor mode allowed
| Serial/MAC | mismatch |     |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- | --- |
Whenusingdevice-specificfeaturepacks,iftheserialnumberorMACaddressinthefeaturepackdoes
notmatchtheswitch,thentheoutputoftheshowfeature-packcommanddisplaysthefollowingerror:
| 6300# show | feature-pack |         |     |     |     |     |     |
| ---------- | ------------ | ------- | --- | --- | --- | --- | --- |
| Feature    | Pack         | Summary |     |     |     |     |     |
====================
| Name             |      | : CX        | Advanced | Feature   | Pack       |     |     |
| ---------------- | ---- | ----------- | -------- | --------- | ---------- | --- | --- |
| Expiration       | Date | : Fri       | Jul      | 19 2024   |            |     |     |
| Serial Number(s) |      | : SG2Zxxxx9 |          | SG9ZxxxxG | SG9Zxxxx5X |     |     |
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 69

| MAC Address  |     | : 38:21:c7:00:00:00 |          |              |       |              |         |
| ------------ | --- | ------------------- | -------- | ------------ | ----- | ------------ | ------- |
| Hostname     |     | : 6300              |          |              |       |              |         |
| Type         |     | : Device            | specific |              |       |              |         |
| Mode         |     | : File              | Based    |              |       |              |         |
| State        |     | : Feature           |          | pack install | error |              |         |
| Error Reason |     | : Serial            | number   | mismatch     |       |              |         |
|              |     |                     |          |              |       | Subscription | Feature |
| Feature      |     |                     |          |              |       | Status       | Status  |
-----------------------------------------------------------------------
| Application | Based      | Policy |     |     |     | inactive | blocked |
| ----------- | ---------- | ------ | --- | --- | --- | -------- | ------- |
| MACsec      | extensions | for    | WAN |     |     | inactive | blocked |
Reflexive Policies for Port Access GBP Clients inactive blocked
| Reflexive | Policies | for | Port | Access Clients |     | inactive | blocked |
| --------- | -------- | --- | ---- | -------------- | --- | -------- | ------- |
Toresolve,installafeature-packwiththecorrectserialnumberandMACaddress.Theserialnumberof
afeaturepackcanbeeditedintheHPEArubaNetworkingsupportportalintheMonitoringpage.The
MACaddresscannotbeedited.IfaMACaddressmustbechangedforafeaturepack,revokethe
featurepackandre-downloadeditwiththecorrectMACaddress.
| Aruba Central |     | Disconnected |     |     |     |     |     |
| ------------- | --- | ------------ | --- | --- | --- | --- | --- |
IfaswitchwaspreviouslymanagedbyArubaCentralbutisnolongermanagedbyCentral,subscription
featureswillbeoperationalinhonormodeandtheoutputoftheshowfeature-packcommandwill
displaythefollowingmessage:
| (switch)# | show | feature-pack |     |     |     |     |     |
| --------- | ---- | ------------ | --- | --- | --- | --- | --- |
| Feature   | Pack | Summary      |     |     |     |     |     |
====================
| Name         |           | : --   |         |                |     |              |         |
| ------------ | --------- | ------ | ------- | -------------- | --- | ------------ | ------- |
| Expiration   | Date      | : --   |         |                |     |              |         |
| Serial       | Number(s) | : --   |         |                |     |              |         |
| MAC Address  |           | : --   |         |                |     |              |         |
| Hostname     |           | : --   |         |                |     |              |         |
| Type         |           | : --   |         |                |     |              |         |
| Mode         |           | : File | Based   |                |     |              |         |
| State        |           | : No   | feature | pack installed |     |              |         |
| Error Reason |           | : --   |         |                |     |              |         |
|              |           |        |         |                |     | Subscription | Feature |
| Feature      |           |        |         |                |     | Status       | Status  |
-----------------------------------------------------------------------
| Application | Based      | Policy |     |     |     | inactive | blocked |
| ----------- | ---------- | ------ | --- | --- | --- | -------- | ------- |
| MACsec      | extensions | for    | WAN |     |     | inactive | blocked |
Reflexive Policies for Port Access GBP Clients inactive blocked
| Reflexive | Policies | for | Port | Access Clients |     | inactive | blocked |
| --------- | -------- | --- | ---- | -------------- | --- | -------- | ------- |
Theswitchmaybeinthisstateforthebelowreasons:
n TheswitchlostconnectivitytotheArubaCentralserver.Checkthattheswitch’suplinkhas
connectivitytoCentral.
n TheArubaCentralsubscriptionorArubaCentralapplicationassignmentfortheswitchwasremoved
inGLCP.CheckthattheswitchisassignedtoCentralandhasavalidCentrallicenseattachedinGLCP.
| Some Features |     | are | Allowed | but | Others | are Blocked |     |
| ------------- | --- | --- | ------- | --- | ------ | ----------- | --- |
Thefollowingexampleoutputofshowfeature-packshowsthatsomefeaturesareallowedinhonor
modewhilesomeareblockedinstrictmode.Thiswillhappeninadeploymentwherethefeaturewas
TroubleshootingFeaturePackIssues|70

notuseduntilaftertheswitchupgradedtoAOS-CX10.13orlaterreleases.Ifasubscriptionfeaturewas
inusebeforeanupgradeto10.13,thenthefeaturewilldefaulttobeingallowedinsteadofblocked.
| 6300#   | show feature-pack |     |     |     |     |     |
| ------- | ----------------- | --- | --- | --- | --- | --- |
| Feature | Pack Summary      |     |     |     |     |     |
====================
| Name        |           | : --   |         |                |              |         |
| ----------- | --------- | ------ | ------- | -------------- | ------------ | ------- |
| Expiration  | Date      | : --   |         |                |              |         |
| Serial      | Number(s) | : --   |         |                |              |         |
| MAC Address |           | : --   |         |                |              |         |
| Hostname    |           | : --   |         |                |              |         |
| Type        |           | : --   |         |                |              |         |
| Mode        |           | : File | Based   |                |              |         |
| State       |           | : No   | feature | pack installed |              |         |
| Error       | Reason    | : --   |         |                |              |         |
|             |           |        |         |                | Subscription | Feature |
| Feature     |           |        |         |                | Status       | Status  |
-----------------------------------------------------------------------
| Application | Based      | Policy |     |     | inactive | blocked |
| ----------- | ---------- | ------ | --- | --- | -------- | ------- |
| MACsec      | extensions | for    | WAN |     | inactive | blocked |
Reflexive Policies for Port Access GBP Clients inactive blocked
| Reflexive | Policies | for     | Port  | Access Clients | inactive | blocked |
| --------- | -------- | ------- | ----- | -------------- | -------- | ------- |
| Features  | are      | Blocked | after | Zeroization    |          |         |
Afterzeroizingaswitch,anyinstalledfeaturepackiserasedandallsubscriptionfeaturesbecome
blocked.Theoutputofshow feature-packwilllooklikethefollowingexample:
| 6300#           | show feature-pack |                 |     |     |     |     |
| --------------- | ----------------- | --------------- | --- | --- | --- | --- |
| switch(config)# |                   | sh feature-pack |     |     |     |     |
| Feature         | Pack Summary      |                 |     |     |     |     |
====================
| Name        |           | : --   |         |                |              |         |
| ----------- | --------- | ------ | ------- | -------------- | ------------ | ------- |
| Expiration  | Date      | : --   |         |                |              |         |
| Serial      | Number(s) | : --   |         |                |              |         |
| MAC Address |           | : --   |         |                |              |         |
| Hostname    |           | : --   |         |                |              |         |
| Type        |           | : --   |         |                |              |         |
| Mode        |           | : File | Based   |                |              |         |
| State       |           | : No   | feature | pack installed |              |         |
| Error       | Reason    | : none |         |                |              |         |
|             |           |        |         |                | Subscription | Feature |
| Feature     |           |        |         |                | Status       | Status  |
-----------------------------------------------------------------------
| Application | Based          | Policy |     |     | inactive | blocked |
| ----------- | -------------- | ------ | --- | --- | -------- | ------- |
| Audio       | Video Bridging |        |     |     | inactive | --      |
| MACsec      | extensions     | for    | WAN |     | inactive | blocked |
Reflexive Policies for Port Access GBP Clients inactive blocked
| Reflexive | Policies | for | Port | Access Clients | inactive | blocked |
| --------- | -------- | --- | ---- | -------------- | -------- | ------- |
Tore-enablefeatures,reinstallthefeaturepack.Ifadevice-specificfeaturepackwasbeingused,then
thefeaturepackcanbere-downloadedfromtheMonitoringpageintheHPEArubaNetworkingsupport
portal.Ifafloatingfeaturepackwasbeingused,revoketheexistingfeaturepackinthesupportportal,
thenre-configurethefeature-packserverprofileontheswitch.Afterwards,theswitchwillreachoutto
thesupportportalandinstallanewfeaturepack.
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 71

Chapter 9

Feature Pack events

Feature Pack events

The following are the events related to CX Advanced and CX Premium feature packs.

Event ID: 14401

Message

{feature_pack_name} installed

Category

Feature Pack

Severity

Info

Description

Event raised when a feature pack is installed

Event ID: 14402

Message

{feature_pack_name} erased.

Category

Feature Pack

Severity

Info

Description

Event raised when a feature pack is erased.

Event ID: 14403

Message

{feature_pack_name} expired on {expiry_date}.

Category

Feature Pack

Severity

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

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

72

Message

Event raised when a feature pack file downloads successfully

Category

Feature Pack

Severity

Info

Description

Feature pack file download success

Event ID: 14406

Message

Feature pack file download failure

Category

Feature Pack

Severity

Warning

Description

Event raised when a feature pack file download fails

Event ID: 14407

Message

Feature pack subscription through HPE Aruba Networking Central is {connection_state}

Category

Feature Pack

Severity

Info

Description

Event raised when a feature pack subscription through HPE Aruba Networking Central

becomes connected or disconnected

Event ID: 14408

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

Feature {feature_name} is operating in honor mode without a valid feature pack.

Category

Feature Pack

Severity

Warning

Description

Periodic event raised to indicate that a feature is operating in honor mode

Event ID: 14410

Feature Pack events | 73

Message

Connection to feature pack server lost and subscription for {feature_pack_name} cannot

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

Software feature pack {feature_pack_name} revoked by the server.

Category

Feature Pack

Severity

Info

Description

Event raised when a feature pack is revoked by the feature pack server.

Event ID: 14414

Message

Feature pack mode {feature_pack_mode} does not match installed feature pack type

{feature_pack_type}.

Category

Feature Pack

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

74

Severity

Warning

Description

Event raised when the feature pack mode configured does not match the feature pack

type installed on the device.

Event ID: 14415

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

The feature pack has been successfully validated by the server

Category

Feature Pack

Severity

Info

Description

Event raised when the feature pack was successfully validated by the server

Event ID: 14418

Message

Feature pack server failed to validate the installed feature pack

Category

Feature Pack

Severity

Error

Description

Event raised when there is an error validating a feature pack by the server

Event ID: 14419

Message

One or more advanced features have been blocked due to an invalid or missing feature-

Feature Pack events | 75

pack.Checkshowfeature-packfordetails.
| Category | FeaturePack |     |
| -------- | ----------- | --- |
| Severity | Warning     |     |
Description Eventraisedwhenaninvalidormissingfeaturepackblocksoneormorefeaturesfrom
operating
| Feature | Pack Agent | events |
| ------- | ---------- | ------ |
ThefollowingaretheeventsrelatedtoCXAdvancedandCXPremiumfeaturepackagents.
| Event ID: | 15001 |     |
| --------- | ----- | --- |
Message
'Thecloud-managedmodeisenabled,afeaturepackserverwillbeusedforfeaturepack
management'
| Category | FeaturePackAgent |     |
| -------- | ---------------- | --- |
| Severity | Info             |     |
Description
Eventraisedwhenthefeaturepackmanagamentmodeissettocloud-managed'
| Event ID: | 15002 |     |
| --------- | ----- | --- |
Message Thecloud-managedmodeisdisabled,afeaturepackserverwillnolongerbeusedfor
featurepackmanagement
| Category | FeaturePack |     |
| -------- | ----------- | --- |
| Severity | Info        |     |
Description
Eventraisedwhenthemanagementmodeisdifferentthancloud-managed
| Event ID: | 15003                                              |     |
| --------- | -------------------------------------------------- | --- |
| Message   | Featurepackvalidationwithanexternalservertriggered |     |
| Category  | FeaturePackAgent                                   |     |
| Severity  | Info                                               |     |
Description Eventraisedwhenafeaturepackvalidationprocessusinganexternalserveristriggered
| Event ID: | 15004 |     |
| --------- | ----- | --- |
Message
Anewfeaturepackhasbeensuccessfullyinstalledonthesystem
| Category | FeaturePackAgent |     |
| -------- | ---------------- | --- |
AOS-CX10.16FeaturePackDeploymentGuide|(5420,6300,6400,8xxx,93xx,100xxSwitchSeries) 76

Severity

Info

Description

Event raised when a new feature pack was successfully installed on the switch

Event ID: 15005

Message

The feature pack has been successfully validated on the system

Category

Feature Pack Agent

Severity

Info

Description

Software feature pack file successfully downloaded

Event ID: 15006

Message

Failed to validate the system feature pack

Category

Feature Pack Agent

Severity

Error

Description

Event raised when there is an error validating a feature pack for the switch

Queue Monitoring events

The following are the events related to queue monitoring (QTP).

Event ID: 16101

Message

HONOR_MODE: Queue Monitoring is operating without a valid feature pack.

Category

QTP

Severity

Information

Description

Log event to indicate that the Queue Monitor feature is operating without a valid feature
pack

Event ID: 16102

Message

STRICT_MODE: Queue Monitoring is blocked due to invalid or missing feature pack.

Category

QTP

Severity

Information

Description

Log event to indicate that the Queue Monitoring feature is blocked due to invalid or

missing feature pack

Event ID: 16103

Feature Pack events | 77

Message

Log event to indicate that the Queue Monitoring feature is operational for valid feature
pack

Category

QTP

Severity

Information

Description

ACTIVE_MODE: Queue Monitoring is operating with valid feature pack.

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

78

Chapter 10

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

AOS-CX 10.16 Feature Pack Deployment Guide | (5420, 6300, 6400, 8xxx, 93xx, 100xx Switch Series)

79

HPE Aruba
Networking
Hardware
Documentation
and Translations
Portal

HPE Aruba
Networking
software

Software
licensing and
Feature Packs

End-of-Life
information

https://arubanetworking.hpe.com/techdocs/hardware/DocumentationPortal/Content/home.
htmm

https://networkingsupport.hpe.com/downloads

https://licensemanagement.hpe.com/

https://networkingsupport.hpe.com/end-of-life

Support and Other Resources | 80