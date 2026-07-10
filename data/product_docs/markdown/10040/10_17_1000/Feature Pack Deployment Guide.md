AOS-CX 10.17.xxxx Feature Pack Deployment Guide

Published: February 2026

AOS-CX 10.17.xxxx Feature Pack Deployment Guide

Published: February 2026

© Copyright 2026 – Hewlett Packard Enterprise Development LP

Notices

The information provided here is subject to change without notice. Hewlett Packard Enterprise's products
and services are covered only by the express warranty statements that come with them. This document
does not constitute an additional warranty. Hewlett Packard Enterprise is not responsible for any technical
or editorial errors or omissions in this document.

Confidential computer software. You must have a valid license from Hewlett Packard Enterprise to possess,
use, or copy the software. In accordance with FAR 12.211 and 12.212, Commercial Computer Software,
Computer Software Documentation, and Technical Data for Commercial Items are licensed to the U.S.
Government under the vendor's standard commercial license.

Links to third-party websites will take you outside of the Hewlett Packard Enterprise website. Hewlett
Packard Enterprise has no control over and is not responsible for the information outside the Hewlett
Packard Enterprise website.

Open source code

This product includes code licensed under certain open source licenses which require source compliance.
The corresponding source for these components is available upon request. This offer is valid to anyone in
receipt of this information and shall expire three years following the date of the final distribution of this
product version by Hewlett Packard Enterprise Company. To obtain such source code, please check if the
code is available in the HPE Software Center at https://myenterpriselicense.hpe.com/cwp-ui/software
but, if not, send a written request for specific software version and product for which you want the open
source code. Along with the request, please send a check or money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company

Attn: General Counsel

WW Corporate Headquarters

1701 E Mossy Oaks Rd, Spring, TX 77389

United States of America.

Public

AOS-CX 10.17.xxxx Feature Pack Deployment Guide

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX 10.17.xxxx Feature Pack Deployment Guide

Table of contents

About this document..................................................................................................................................................................................6

Applicable products........................................................................................................................................................................6

Latest version available online.................................................................................................................................................7

Command syntax notation conventions.............................................................................................................................7

About the examples....................................................................................................................................................................... 8

HPE Aruba Networking CX Feature Pack Overview................................................................................................................ 9

AOS-CX Feature Pack Types and Supported Features..............................................................................................9

Feature Pack Modes....................................................................................................................................................................13

Evaluation vs Subscription Feature Pack Keys............................................................................................................14

Best Practices and Limitations..............................................................................................................................................14

Viewing and Managing Subscription Pools................................................................................................................................ 16

Viewing and Managing Feature Pack Subscriptions.............................................................................................................21

Activating a Term Feature Pack Subscription..............................................................................................................21

Activating a Perpetual Feature Pack Subscription for 10000 or 10040 Switches Switches........... 23

Monitoring Feature Pack Subscriptions...........................................................................................................................24

Revoking a Feature Pack Subscription.............................................................................................................................26

Transfer Feature Pack Subscriptions Between Accounts......................................................................................27

Cloud-Managed Feature Pack Use Cases and Workflows..................................................................................................30

Deploying a Cloud-managed Feature Pack Solution on a Standalone Switch.......................................... 30

Revoking and Reinstalling a Feature Pack Subscription on a Standalone Switch.................................. 33

Deploying a Cloud-Managed Feature Pack Solution on a VSF Stack.............................................................33

Replacing a VSF Stack Member Using a Cloud-Managed Feature Pack Subscription.........................35

File-based Feature Pack Use Cases and Workflows..............................................................................................................38

Deploying a File-Based Feature Pack Solution on a Standalone Switch...................................................... 38

Setting a File-Based Switch to Honor Mode.................................................................................................................42

Deploying a File-Based Feature Pack Solution on a VSF Stack.........................................................................43

Replacing a VSF Stack Member Using a File-Based Feature Pack subscription......................................48

Replacing a VSF Stack Conductor Using a File-Based Feature Pack subscription.................................52

Viewing Feature Packs on Switches Managed by Central................................................................................................. 55

Feature pack commands........................................................................................................................................................................57

erase feature-pack ...................................................................................................................................................................... 57

feature-pack mode ......................................................................................................................................................................58

feature-pack server .................................................................................................................................................................... 60

feature-pack validate ................................................................................................................................................................ 63

Public

Table of contents 4

show feature-pack ...................................................................................................................................................................... 64

Frequently Asked Questions (FAQs)..............................................................................................................................................70

Troubleshooting Feature Pack Issues............................................................................................................................................74

Feature Pack events.................................................................................................................................................................................84

feature pack events..................................................................................................................................................................... 91

Queue Monitoring events.........................................................................................................................................................96

Support and Other Resources............................................................................................................................................................97

Accessing HPE Aruba Networking Support..................................................................................................................98

Public

Table of contents 5

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing HPE Aruba Networking switches on a network.

Subtopics

Applicable products
Latest version available online
Command syntax notation conventions
About the examples

Applicable products

This document applies to the following products:

•  HPE Aruba Networking 5420 Switch Series (S0U67A, S0U55A, S0U63A, S0U64A, S0U65A, S0U75A,

S0U72A, S0U78A, S0U58A, S0U73A, S0U74A, S0U71A, S0U76A, S0U70A, S0U77A, S0U60A,
S0U61A, S0U62A, S0U66A, S0U68A)

•  HPE Aruba Networking 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A,
R8Q68A, R8Q69A, R8Q70A, R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A,
JL724B, JL725B, JL726B, JL727B, JL728B, S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,
S0M87A, S0M88A, S0M89A, S0M90A, S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

•  HPE Aruba Networking 8100 Switch Series (R9W94A, R9W95A, R9W96A, R9W97A)

•  HPE Aruba Networking 8320 Switch Series (JL479A, JL579A, JL581A)

•  HPE Aruba Networking 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

•  HPE Aruba Networking 8325H Switch Series (S4B20A, S4B21A, S4B22A, S4B23A, S2T42A, S2T46A,

S2T47A, S2T48A)

•  HPE Aruba Networking 8325P Switch Series (S0G12A, S4A48A)

•  HPE Aruba Networking 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A,
JL708A, JL709A, JL710A, JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C,
JL709C, JL710C, JL711C, JL704C, JL705C, JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

•  HPE Aruba Networking 8400 Switch Series (JL366A, JL363A, JL687A)

•  HPE Aruba Networking 9300 Switch Series (R9A29A, R9A30A, R8Z96A, S0F81A, S0F82A, S0F83A)

Public

About this document 6

•  HPE Aruba Networking 9300S Switch Series (S0F81A, S0F82A, S0F83A, S0F84A, S0F85A, S0F86A,

S0F88A, S0F95A, S0F96A)

•  HPE Aruba Networking 10000 Switch Series (R8P13A, R8P14A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

example‐text

example‐text

Any of the following:

•  <example‐text>
•  <example‐text>
•  example‐text
•  example‐text

|

Usage

Identifies commands and their options and operands
, code examples, filenames, pathnames, and output d
isplayed in a command window. Items that appear li
ke the example text in the previous column are to be
entered exactly as shown and are required unless en
closed in brackets ([ ]).

In code and screen examples, indicates text entered
by a user.

Identifies a placeholder—such as a parameter or a va
riable—that you must substitute with an actual valu
e in a command or in code:

•  For output formats where italic text cannot be di
splayed, variables are enclosed in angle brackets
(< >). Substitute the text—including the enclosin
g angle brackets—with an actual value.

•  For output formats where italic text can be displ
ayed, variables might or might not be enclosed i
n angle brackets. Substitute the text including th
e enclosing angle brackets, if any, with an actual
value.

Vertical bar. A logical OR that separates multiple ite
ms from which you can choose only one.

Public

Latest version available online 7

Convention

Usage

{ }

[ ]

… or

...

Any spaces that are on either side of the vertical bar
are included for readability and are not a required pa
rt of the command syntax.

Braces. Indicates that at least one of the enclosed ite
ms is required.

Brackets. Indicates that the enclosed item or items a
re optional.

Ellipsis:

•

•

In code and screen examples, a vertical or horizo
ntal ellipsis indicates an omission of information.
In syntax using brackets and braces, an ellipsis i
ndicates items that can be repeated. When an ite
m followed by ellipses is enclosed in brackets, ze
ro or more items can be specified.

About the examples

Examples in this document are representative and might not match your particular switch or environment.

The slot and port numbers in this document are for illustration only and might be unavailable on your switch.

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

Public

About the examples 8

Variable information in CLI prompts

In certain configuration contexts, the prompt may include variable information. For example, when in the
VLAN configuration context, a VLAN number appears in the prompt:

switch(config-vlan-100)#
When referring to this context, this document uses the syntax:

switch(config-vlan-<VLAN-ID>)#
Where <VLAN-ID> is a variable representing the VLAN number.

HPE Aruba Networking CX Feature Pack Overview

AOS-CX 5240, 6300, 6400, 8xxx, 93xx, and 100xx Switch series support optional add-on feature packs
that enhance the base AOS-CX operating system and allow users to activate and manage advanced features
on the switches through a subscription. Depending upon the requirements for their networks, network
administrators may choose to purchase a subscription for these features that provide enhanced traffic
visibility and troubleshooting, and support advanced security.

This section includes the following information about HPE Aruba Networking CX feature packs.

•  AOS-CX Feature Pack Types

•  Feature Pack Modes

•  Evaluation vs subscription Feature Pack Keys

•  Best Practices and Limitations

Subtopics

AOS-CX Feature Pack Types and Supported Features
Feature Pack Modes
Evaluation vs Subscription Feature Pack Keys
Best Practices and Limitations

AOS-CX Feature Pack Types and Supported Features

The AOS-CX software preinstalled on all HPE Aruba Networking CX switches includes an active, perpetual
set of AOS-CX native enterprise features at no additional cost. The AOS-CX native enterprise features
include everything needed to deploy, connect, and troubleshoot an enterprise network. For those networks
that require enhanced visibility and assurance, the HPE Aruba Networking CX Advanced feature pack
enables Edge Insights for AOS-CX 6300 and 6400 Switch series, offering application-based policies, from
OSI Layer 2 to Layer 7. The HPE Aruba Networking CX Advanced feature pack for 5420 switches supports
application-based policies, and the HPE Aruba Networking CX Advanced feature pack for 8xxx, 9xxx and
10040 switches includes the ability to Host HPE certified applications for flexible and reliable IT services.

Public

HPE Aruba Networking CX Feature Pack Overview 9

The HPE Aruba Networking CX premium feature pack is supported on 10000 Switch Series only, and
enables scalable Network Address Translation (NAT) and IPSec VPN services.

NOTE

For networks managed by HPE Aruba Networking Central, the HPE Aruba
Networking Central Advanced license enables all features supported by the CX
Advanced feature pack, so no additional purchase of an CX Advanced feature
pack is necessary. For more information on HPE Aruba Networking Central
licensing, see the HPE Aruba Networking Central SaaS Subscription Ordering
Guide.

The following table describes the features supported by the different types of HPE Aruba Networking
feature packs.

Table 1. Features Supported by Each Feature Pack Type
Feature Pack Type

Availability

AOS‐CX native enterprise feat
ures

Automatically included with AOS
‐CX switch hardware)

Supported Features

While switch software features wi
ll vary per product family, the foll
owing are generally included in th
e AOS‐CX native enterprise feat
ures:

switch series)

•  Multiprotocol Label Switching
(MPLS) (6400, 8360 Switch
Series)

•  Basic and advanced routing, i
ncluding static routes, Routing
Information Protocol (RIPv2 a
nd RIPng), Open Shortest Pat
h First (OSPFv2 and OSPFv3),
Border Gateway Protocol (BGP
), and IS‐IS

•  Protocol Independent Multica

st (PIMv4, PIMv6)

•  Software‐Defined Environme
nts: VXLAN, User‐Based Tun
neling (UBT)
IP Flow Information Export (IP
FIX)

•

•  Precision Time Protocol (PTP),
Transparent Clocks (TCs), and
Boundary Clocks (BCs)

Public

AOS-CX Feature Pack Types and Supported Features 10

| Feature Pack Type |     | Availability |     | Supported Features |     |
| ----------------- | --- | ------------ | --- | ------------------ | --- |
•  High Availability, including In
‐Service Software Upgrades
(ISSU) and hot patching
•  Full layer‐2 support, includin
g STP, VLANs, and IGMP
•  Network Analytics Engine (NA
E)
•  Layer‐2 MACsec Security (6
300, 8360 Switch series
| AOS‐CX 5420 Switch advanced |     | Subscription: |     |     |     |
| --------------------------- | --- | ------------- | --- | --- | --- |
•  Application‐based policies
feature pack
1 year
•  Drop Exceptions
3 year
•  MACsec extensions for the WA
N
5 year
7 year
10 year
90‐day eval
| AOS‐CX 6300 Switch advanced |     | Subscription: |     |                               |     |
| --------------------------- | --- | ------------- | --- | ----------------------------- | --- |
| feature pack                |     |               |     | •  Application‐based policies |     |
1 year
•  Reflexive policies for port acc
|     |     | 3 year |     | ess GBP clients                    |     |
| --- | --- | ------ | --- | ---------------------------------- | --- |
|     |     | 5 year |     | •  Reflexive policies for port acc |     |
ess policy clients
7 year
•  MACsec extensions for the WA
10 year
N
|     |     | 90‐day eval |     | •  Drop Exceptions |     |
| --- | --- | ----------- | --- | ------------------ | --- |
AOS‐CX 6400 Switch advanced
Subscription:
Application‐based policies
| feature pack |     |     |     | •   |     |
| ------------ | --- | --- | --- | --- | --- |
1 year
•  Reflexive policies for port acc
|     |     | 3 year |     | ess GBP clients                    |     |
| --- | --- | ------ | --- | ---------------------------------- | --- |
|     |     | 5 year |     | •  Reflexive policies for port acc |     |
ess policy clients
7 year
•  MACsec extensions for the WA
|     |        | 10 year     |                                                  | N                  |     |
| --- | ------ | ----------- | ------------------------------------------------ | ------------------ | --- |
|     |        | 90‐day eval |                                                  | •  Drop Exceptions |     |
|     | Public |             | AOS-CX Feature Pack Types and Supported Features |                    | 11  |

| Feature Pack Type         |     | Availability  |     | Supported Features |     |
| ------------------------- | --- | ------------- | --- | ------------------ | --- |
| AOS‐CX 8xxx/9xxxSwitch ad |     | Subscription: |     |                    |     |
•  Host HPE certified application
vanced feature pack
1 year
s for flexible and reliable IT ser
|     |     | 3 year |     | vices** |     |
| --- | --- | ------ | --- | ------- | --- |
•  MACsec extensions for the WA
5 year
N (8360, 9300S Switch series
7 year
only)
10 year
•  Queue Statistics Monitoring (8
90‐day eval
325, 8325H and 9xxx Switch
series only)
•  Inband Flow Analyzer and Flo
w Telemetry (9xxx Switch seri
es only)
•  Queue Congestion Monitoring
(8325, 8325H and 8325P Swi
tch series only)
•  Drop Exceptions (not suppor
ted on 8320 Switch series)
•  Audio-Video Bridging (AVB) o
n the 8360 Switch series JL71
7C, JL718C, JL721C, JL722C
| AOS-CX 10040 Switch advanced |     | Subscription: |     |                                   |     |
| ---------------------------- | --- | ------------- | --- | --------------------------------- | --- |
| feature pack                 |     |               |     | •  Host HPE certified application |     |
1 year
s for flexible and reliable IT ser
|     |     | 3 year |     | vices**                         |     |
| --- | --- | ------ | --- | ------------------------------- | --- |
|     |     | 5 year |     | •  MACsec extensions for the WA |     |
N.
7 year
10 year
90‐day eval
perpetual
| AOS‐CX 10000 Switch advanc |     | Subscription: |     |                                   |     |
| -------------------------- | --- | ------------- | --- | --------------------------------- | --- |
| ed feature pack            |     |               |     | •  Host HPE certified application |     |
1 year
s for flexible and reliable IT ser
|     |     | 3 year |     | vices** |     |
| --- | --- | ------ | --- | ------- | --- |
•  Accelerated stateful firewall fo
5 year
r east‐west traffic
7 year
•  Firewall logging and per‐pac
10 year
ket IPFIX telemetry streaming
|     |        | 90‐day eval |                                                  | •  Queue Statistics Monitoring |     |
| --- | ------ | ----------- | ------------------------------------------------ | ------------------------------ | --- |
|     | Public |             | AOS-CX Feature Pack Types and Supported Features |                                | 12  |

Feature Pack Type

AOS‐CX 10000 Switch premium
feature pack

Availability

perpetual

1 year

3 year

5 year

90‐day eval

perpetual

Supported Features

•  Drop Exceptions

•  All features included in the AO
S‐CX 10000 Switch advance
d feature pack
IPSec VPN services

•
•  Scalable NAT, including statef
ul NAT for dual‐stack IPv4/I
Pv6 deployments

•  Advanced DDoS protection

** AOS-CX does not enforce the requirement to own a feature pack prior to using the container feature to
host HPE certified applications.

Feature Pack Modes

CX Advanced and Premium feature packs can be managed in either cloud-managed mode, file-based
mode, or honor mode.

Cloud-Managed Mode

The centralized management of HPE Aruba Networking CX Advanced and Premium feature packs allows a
group of switches using feature pack subscriptions in cloud-managed mode to share a pool of one or more
feature pack subscriptions managed through the HPE Aruba Networking support portal. By default, a switch
using a CX feature pack in cloud mode will contact the HPE Aruba Networking support portal once a day to
automatically synchronize with the feature pack subscription management database.

When you use a cloud-managed deployment type, the HPE Aruba Networking support site can automatically
distribute and manage feature pack subscriptions for all devices in a group, making it a scalable solution for
larger deployments and for global accounts across geographies.

File-Based Mode

Networks with a single switch or with multiple switches on isolated networks that cannot contact the HPE
Aruba Networking support site can use feature pack subscription keys in file-based mode, where a feature
pack is manually enabled on a switch using a non-sharable subscription key file tied to that individual
switch's serial number or MAC address. When a switch upgrades to 10.13.0001, existing features that
require feature packs in 10.13 will remain operational in honor mode, even if that feature is not yet part
of a feature pack. File-based mode is the default operation mode of feature pack management for AOS-CX
switches.

Honor mode

Public

Feature Pack Modes 13

Honor mode is intended for cases where a valid feature pack for advanced features has been purchased, but
is not yet installed on the device. Advanced features on this device will be operational in Honor mode, but a
warning message may be seen until a valid feature pack is installed.

NOTE

HPE Aruba Networking may remove support for honor mode in a future release.
If support for honor mode is removed, advanced features will only be operational
if the applicable subscription fees are paid and a valid feature pack is installed

Evaluation vs Subscription Feature Pack Keys

Each Aruba CX Advanced or Aruba CX Premium feature pack key is available as either a 90-day evaluation
subscription or a standard subscription that is valid for a term from 1-10 years. An evaluation feature pack
allows you to evaluate the functionality of a software feature pack for a period of 90 days. Evaluation and
standard subscription feature packs can added to and made sharable within a subscription pool.

Feature pack subscription keys cannot be renewed. Once a feature pack subscription key expires, a new
feature pack subscription key must be generated and installed on the switch. To determine the remaining
time on an evaluation feature pack, issue the show feature-pack command in the switch command-line
interface. An expired feature pack will remain on the switch until it is removed using the command erase
feature-pack.

For more information on obtaining an evaluation subscription key, contact your authorized HPE Aruba
Networking reseller.

Best Practices and Limitations

The following best practices and limitations apply to Aruba CX Advanced and Premium feature pack
subscription keys.

•  A single user account in the HPE Aruba Networking support portal can manage Aruba CX advanced

and premium feature packs in cloud mode (supporting cloud-managed mode on the AOS-CX switch) or
local mode (supporting file-based mode on the AOS-CX switch), but not in both modes simultaneously.
If your global deployment must support both file-based and cloud-managed feature pack subscriptions,
you must manage these subscription types separately using two different user accounts.

•  Feature pack keys in cloud mode can only be associated to a switch via the HPE Aruba Networking

support portal. Cloud-managed feature pack keys cannot be added directly to a switch via the switch
CLI.

•  Multi-Factor Authentication (MFA) is supported on HPE user accounts and MFA is compatible with all

feature pack modes and management methods. MFA is both supported and recommended.

Public

Evaluation vs Subscription Feature Pack Keys 14

•  6300, 6400, 8xxx, and 9300 Switch series managed via HPE Aruba Networking Central and using an
HPE Aruba Networking Central Advanced license do not need HPE Aruba Networking CX Advanced
feature packs, as the HPE Aruba Networking Central Advanced license automatically enables all
advanced feature pack features on that switch. However, 10000 Switch series managed with an HPE
Aruba Networking Central Advanced subscription does require a HPE Aruba Networking CX Advanced
Feature Pack when ordering the switch. For more information on HPE Aruba Networking Central
licenses, refer to the .

•  When allocating feature pack subscriptions for a VSF stack, best practices is to keep subscriptions for all

members in dedicated subscription block.

•  Subscriptions blocks cannot be split after activation. Consider creating subscription blocks with a smaller
number of subscriptions, as this provides greater flexibility in managing subscription blocks and moving
them across subscription pools.

•  Rebooting the switch or removing a cloud-based feature pack subscription profile does not affect its
existing feature pack subscription. However, issuing the erase all zeroize command resets the device
to a factory default state and deletes all local or cloud-managed feature packs. If you reset a switch to
its factory default state, you must reinstall the previously-installed file-based feature pack. To reinstall a
cloud feature pack after zeroizing the switch, the former feature pack needs to be revoked in the HPE
Aruba Networking support portal, and the feature pack profile on the switch needs to be re-configured
to connect to the support portal.

•  Tampering with a downloaded feature pack file in local mode will cause installation failure.

•

If there is a possibility that a device may be added to a VSF stack sometime in future, consider
maintaining a buffer of additional feature pack subscriptions when creating a block.

•  Setting the clock to past the expiration date will cause it to become expired.

•  A file-based feature pack can be revoked and re-used on a different switch a limited number of times.
if this the limit has been exceeded, contact HPE Aruba Networking technical support for assistance in
revoking the feature pack.

NOTE
CX feature pack management provides the ability to move a feature-pack from
one switch to another, for maximum flexibility in managing an organization’s
network and to minimize an RMA impact. HPE Aruba networking monitors and
detects feature pack fraud. Abnormally high volumes of feature pack transfers
for the same feature pack subscription to multiple devices can indicate a breach
of the HPE Aruba Networking end user software license agreement and will be
investigated.

Public

Best Practices and Limitations 15

Viewing and Managing Subscription Pools

Feature packs can be grouped into one or more feature pack subscription pools on the HPE Aruba
networking support portal. You can manage all of your feature pack orders using the single pre-existing
Default pool, but best practices is to create separate pools for different feature pack types or network
segments according to your feature pack deployment strategy. It is helpful to name pools in a standard
pattern for easy recognition, for example, by floors, buildings or departments.

The subscriptions in each pool are further grouped into individual subscription blocks, which are comprised
of a single type of subscription from a single order.

NOTE

Each user account with the HPE Aruba Networking support portal can manage
CX feature packs in cloud mode or in local (file-based) mode, but not in both
modes simultaneously. When you first access your CX feature pack pools, you are
asked if you want to manage feature packs in either Cloud mode or Local mode.
Choose carefully, as you will not be able to change your management mode.
If you want to manage feature packs in both cloud-managed and file-based
modes, you must use two separate HPE Aruba Networking support accounts, one
for each mode. For more information on feature pack modes, see Feature Pack
Modes

This section describes the following workflows:

•  Viewing Feature Pack Subscription Pools and Feature Pack Orders

•  Adding a Subscription Pool

•  Renaming a Subscription Pool

•  Deleting a Subscription Pool

•  Moving a Subscription Block to a New Subscription Pool

•  Adding or Editing a Subscription Block Name

Viewing Feature Pack Subscription Pools and Feature Pack Orders

The Orders page on the HPE Aruba Networking support portal displays your HPE Aruba Networking CX
subscription pools and information about all feature pack orders. To view your feature pack orders and
subscription pools:

1.  Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking support

user name and password.

2.  From the License Management page, select View Order.

Figure 1. Viewing Current Orders on the HPE Aruba Networking Support Portal

Public

Viewing and Managing Subscription Pools 16

3.  Select the AOS-CX Feature Pack tab at the top of the Orders page to display the Default feature pack

pool, and any user-created pools.

Figure 2. Viewing Aruba CX Feature Pack Orders

4.  The first time you view this page, you will be prompted to select either local or cloud mode for your CX
feature pack management mode. Once selected, this mode cannot be changed, and will display at the
top of the Orders page.

Figure 3. CX feature pack management mode

Public

Viewing and Managing Subscription Pools 17

The Orders page also displays the following information about the subscription orders in each subscription
pool.

•  Order number

•  Subscription key

•  Block name (optional)

•  Subscription term start date

•  Subscription term end date

•  Subscription pack part number description

•  Order quantity (total number of subscriptions in the feature block)

•  Available quantity (number of subscriptions in that feature block that are not yet used)

Figure 4. Orders Page Showing CX Feature Packs

Public

Viewing and Managing Subscription Pools 18

Adding a Subscription Pool

All new feature pack subscription orders automatically appear in the Default subscription pool. You can
create additional pools to help you identify and organize individual subscriptions blocks.

NOTE

Subscriptions blocks cannot be split after activation. Consider creating
subscription blocks with a smaller number of subscriptions, as this provides
greater flexibility in managing subscription blocks and moving them across
subscription pools.

To add a new subscription pool:

1.  Navigate to the AOS-CX Orders page as described in .

2.  Click the (+) Add Subscription Pool icon at the top of the page.

3.  Enter a name for the new subscription pool.

Figure 5. Adding a Subscription Pool

Renaming a Subscription Pool

You can assign a different name to any user-created subscription pool. The Default pool can not be deleted.

1.  Navigate to the AOS-CX Orders page as described in .

2.  Click the green edit icon

 by the subscription pool you want to rename.

3.  Enter the new name for the pool, then click OK.

Public

Viewing and Managing Subscription Pools 19

Deleting a Subscription Pool

If you delete a user-created subscription pool, any subscription blocks in that pool are automatically
transferred back to the Default pool. The Default pool cannot be deleted.

A pool cannot be deleted if switches are using feature pack subscriptions in that pool. All the feature packs
need to be revoked before the pool can be deleted. The switch can then be assigned feature packs from a
new pool.

NOTE
For more information on revoking a feature pack subscription, see Revoking a
Feature Pack Subscription

1.  Navigate to the Aruba CX Orders page as described in .

2.  Click the red delete icon

 by the subscription pool you want to delete. A dialog box opens and asks

you to confirm that you want to delete that pool.

3.  Click OK.

Moving a Subscription Block to a New Subscription Pool

To move a subscription block to a different subscription pool:

1.  Navigate to the Aruba CX Orders page as described in .

2.  Click the green actions icon

 by the subscription block to be moved, and select Move. A dialog box

opens that allows you to select a new subscription pool for that subscription block.

3.  Select the new pool for the subscription block, then click Submit.

Adding or Editing a Subscription Block Name

To add or change the name of a subscription block:

1.  Navigate to the AOS-CX Orders page as described in .

2.  Click in the Block Name column for any order to add or edit a block name.

Figure 6. Editing a Block Name

Public

Viewing and Managing Subscription Pools 20

Viewing and Managing Feature Pack Subscriptions

This chapter describes how to activate a feature pack so it can be used by an AOS-CX switch, view and
monitor purchased feature packs, revoke a feature pack subscription so it can be assigned to another switch,
and transfer feature packs between user accounts on the HPE Aruba Networking support portal.

Subtopics

Activating a Term Feature Pack Subscription
Activating a Perpetual Feature Pack Subscription for 10000 or 10040 Switches Switches
Monitoring Feature Pack Subscriptions
Revoking a Feature Pack Subscription
Transfer Feature Pack Subscriptions Between Accounts

Activating a Term Feature Pack Subscription

About this task

When you activate an evaluation or 1-year to 10-year term subscription feature pack subscription for 6xxx,
8xxx, 9xxx or 10000 switches:

•  The subscription term for that feature pack begins.

•  That feature pack subscription can be assigned to an AOS-CX switch.

Public

Viewing and Managing Feature Pack Subscriptions 21

The feature block for that feature pack order updates to show that one less subscription is available only
after a feature pack is generated for a specific switch. For feature packs in file-based mode, this happens
after a user downloads an feature pack from the HPE Aruba Networking support portal. For feature packs in
cloud-managed mode, this happens happen after a switch contacts the support portal to reserve a feature
pack.

NOTE
A feature pack does not appear on the Subscription Monitoring page until it is
both activated and assigned to a switch. The feature block for that feature pack
order update to show that one less subscription is available.

To activate a feature pack subscription:

Procedure

1.  Navigate to the AOS-CX Orders page as described in Viewing Aruba CX Feature Subscription Pools and

Feature Pack Orders.

2.

Identify the feature pack order with the subscription to be activated. Orders with unactivated
subscriptions appear in the Orders table highlighted in green.

Figure 1. AOS-CX Orders Page Showing Unactivated Subscriptions

3.  Click the green actions icon by the order with a subscription to be activated, then click Activate. A
dialog box opens and displays the number of available subscriptions within that feature pack order
block.

4.  Enter the number of feature pack subscriptions you want to activate.

5.  (Optional) Enter the name of a feature block for the activated feature packs.

Public

Activating a Term Feature Pack Subscription 22

6.  Click Submit. Each activated feature pack subscription is now available to be associated to an AOS-CX
switch. For details on associating a feature pack to a switch, see also Deploying a Cloud-managed
Feature Pack Solution on a Standalone Switch and Deploying a File-Based Feature Pack Solution on a
Standalone Switch.

Activating a Perpetual Feature Pack Subscription for 10000 or
10040 Switches Switches

About this task

When you activate a perpetual feature pack subscription:

•  The subscription term for that feature pack begins.

•  That feature pack subscription can be assigned to an AOS-CX switch.

•  Other feature packs within the feature pack block cannot be split into different blocks.

The feature block for that feature pack order updates to show that one less subscription is available only
after a feature pack is generated for a specific switch. For feature packs in file-based mode, this happens
after a user downloads an feature pack from the HPE Aruba Networking support portal. For feature packs in
cloud-managed mode, this happens happen after a switch contacts the support portal to reserve a feature
pack.

NOTE
A feature pack does not appear on the Subscription Monitoring page until it is
both activated and assigned to a switch. The feature block for that feature pack
order update to show that one less subscription is available.

To activate a feature pack subscription:

Procedure

1.  Navigate to the Aruba CX Orders page as described in Viewing Aruba CX Feature Subscription Pools

and Feature Pack Orders.

2.  Click the All Products tab.

3.  Click the green button on the right side labeled "Register New"

Figure 1. Aruba CX Orders Page

Public

Activating a Perpetual Feature Pack Subscription f... 23

A
c
t
i
v
a
t
i
n
g

a

P
e
r
p
e
t
u
a
l

F
e
a
t
u
r
e

P
a
c
k

S
u
b
s
c
r
i
p
t
i
o
n

f
.
.
.

4.

Input the order number and confirmation number received from the order management system into the
pop-up window, then click Register.

5.  Now click the AOS-CX Feature Pack tab. The order will be activated in the Default subscription pool.

Results

The activated feature pack subscription is now available to be associated to a 10000 or 10040 switch. For
details on associating a feature pack to a switch, see also Deploying a Cloud-managed Feature Pack Solution
on a Standalone Switch and Deploying a File-Based Feature Pack Solution on a Standalone Switch.

Monitoring Feature Pack Subscriptions

About this task

The Subscription Monitoring page of the HPE Aruba Networking support portal allows you to review CX
feature pack subscriptions that have been associated to an AOS-CX switch.

Public

Monitoring Feature Pack Subscriptions 24

To view feature pack subscriptions currently in use by an AOS-CX switch:

Procedure

1.  Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking support

user name and password.

2.  From the License Management page, select the AOS-CX Feature Pack icon to open the Subscription

Monitoring page.

Figure 1. Viewing Active CX feature Pack subscriptions

Results

The Subscription Monitoring dashboard displays information for each feature pack subscription:

•  Order ID: The order ID number is also sent in an email at the time of the feature pack subscription

purchase.

•  Host Name: The host name of the switch using the feature pack subscription.

•  Serial Number: Serial number unique to that feature pack.

•  MAC Address: MAC address of the switch using the feature pack subscription

•  UUID: A Universally Unique Device Identifier (UUID) for the feature pack subscription.

Public

Monitoring Feature Pack Subscriptions 25

•  Feature Pack Pool: Pool containing the feature pack subscription. By default, all new orders appear in

the Default feature pack pool, but feature pack blocks can be moved to other pools if desired. For more
information, see also Viewing and Managing Subscription Pools .

•  Block Name: This field displays any block name assigned to the feature pack when it was activated.

•  Activation date: The date that the subscription order was activated.

•  Expiry date: Date that the subscription term expires.

You can sort the feature pack subscriptions table on this page by clicking on any column heading to sort the
list by that column criteria, or enter an order ID, host name, serial number, UUID, or feature pack pool name
into the search bar at the top of the page.

Revoking a Feature Pack Subscription

About this task

You can use the HPE Aruba Networking support site remove a feature pack subscription from a switch
managing feature packs in cloud mode, and reuse that feature pack on another switch of the same model.

When you revoke a feature pack subscription on the HPE Aruba Networking support site:

•  The feature pack subscription appears as available on the CX Orders page, indicating that it can be

reassigned.

•  The feature block for that feature pack order will update to show that an additional subscription is

available.

•  A switch in cloud-managed mode will synchronize with the HPE Aruba Networking support site and will

go into honor mode.

•  A switch in file-based mode is not notified that the subscription has been revoked. Manually remove the

subscription from the switch using the erase feature-pack CLI command.

NOTE
Each HPE Aruba Networking support feature pack account domain managing
feature packs in file-based mode can revoke a feature pack up to 50 times per
domain. If is limit is exceeded, the user will not be able to revoke the feature pack
and the system will display an error message.

Procedure

1.  Navigate to the Subscription Monitoring page as described in Monitoring Feature Pack Subscriptions.

Public

Revoking a Feature Pack Subscription 26

2.

Identify the feature pack subscription to be revoked. For large feature pack deployments, you can
use the search bar at the top of this page to search for the switch MAC address, the feature pack
subscription serial number or the feature pack pool.

3.  Select the feature pack to be revoked, click the green actions icon and select Revoke.

Results

Figure 1. Revoking a Feature Pack Used by a Switch

Transfer Feature Pack Subscriptions Between Accounts

About this task

You can use the HPE Aruba Networking Support portal to transfer any unused feature pack subscriptions
orders to another HPE Aruba Networking Support account.

NOTE
Any transfer between accounts must move all subscriptions within that feature
pack subscription block. A single order with multiple feature pack subscriptions
cannot be split between two accounts.

Procedure

1.  Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking support

user name and password.

2.  From the License Management page, select Transfer to Account. The Transfer to Account page opens.

Public

Transfer Feature Pack Subscriptions Between Accoun... 27

T
r
a
n
s
f
e
r

F
e
a
t
u
r
e

P
a
c
k

S
u
b
s
c
r
i
p
t
i
o
n
s

B
e
t
w
e
e
n

A
c
c
o
u
n
.
.
.

3.

Figure 1. Transferring Feature Pack Subscriptions Between Accounts

4.  Enter the email address of the account that currently contains the feature pack subscriptions you want

to transfer, then select Get Accounts.

5.  Select the account that contains the feature pack subscriptions you want to transfer, and click Get

Licenses.

6.  Click the CX-Switch button to list all CX feature pack subscriptions available for transfer.

7.  Select the feature pack subscriptions to transfer and click Next.

Figure 2. Selecting feature pack subscriptions to be transferred

Public

Transfer Feature Pack Subscriptions Between Accoun... 28

8.  You will be prompted to verify your selection. Click Next again.

9.  Now, enter the email address associated with the HPE Aruba Networking Support account to receive the

feature pack subscriptions and click Get Accounts

.

10.  Use the Select Accounts drop-down menu to select the account that should receive the feature pack

subscriptions.

11.

In the Enter reason for transfer field, specify why the feature pack subscriptions are being transferred.

12.  Click Next to display the transfer summary page. Validate all the information about the transfer, then

click Submit.

Results

Figure 3. Validating the Feature Pack Transfer

Public

Transfer Feature Pack Subscriptions Between Accoun... 29

Cloud-Managed Feature Pack Use Cases and Workflows

This chapter section describes the following workflows for deployments using feature pack subscriptions in
cloud-managed mode.

•  Deploying a Feature Pack Solution on a Standalone Switch

•  Removing a Feature Pack Subscription from a Standalone Switch

•  Deploying a Feature Pack Solution on a VSF stack Switch

•  Replacing a VSF Stack Member with a Feature Pack Subscription

Subtopics

Deploying a Cloud-managed Feature Pack Solution on a Standalone Switch
Revoking and Reinstalling a Feature Pack Subscription on a Standalone Switch
Deploying a Cloud-Managed Feature Pack Solution on a VSF Stack
Replacing a VSF Stack Member Using a Cloud-Managed Feature Pack Subscription

Deploying a Cloud-managed Feature Pack Solution on a Standalone
Switch

The following section describes the procedure to install an HPE Aruba Networking CX advanced feature
pack on a single standalone AOS-CX switch using feature pack subscriptions in cloud-managed mode.

Public

Cloud-Managed Feature Pack Use Cases and Workflows 30

D
e
p
l
o
y
i
n
g

a

C
l
o
u
d
-
m
a
n
a
g
e
d

F
e
a
t
u
r
e

P
a
c
k

S
o
l
u
t
i
o
n

o
n
.
.
.

Prerequisites

•  The user has created a user account on the HPE Aruba Networking support portal.

•  The user has already ordered their feature pack subscriptions from HPE Aruba Networking reseller.

•  The Orders page on the HPE Aruba Networking support portal has been updated to indicate that the
subscriptions for the user account will be manged in cloud-managed mode. For details, see Viewing
Aruba CX Feature Subscription Pools and Feature Pack Orders.

Procedure

1.  Log on to the switch command-line interface.

2.  Enter the feature pack server configuration sub-mode.

switch(config)# feature-pack server

3.  Configure the location URL of the HPE Aruba Networking feature pack management server in the

corresponding VRF

switch(config-feature-pack-server)# location https://cx-feature-

pack.arubanetworks.com vrf mgmt

4.  Configure the switch with the account credentials for your HPE Aruba Networking support account.

switch (config-feature-pack-server)#  credentials user <username>

password plaintext <password>

5.  Configure the subscription block and subscription pool, then exit the feature pack server context

switch(config-feature-pack-server)# block 6300_test_block_2

switch(config-feature-pack-server)# pool default

switch(config-feature-pack-server)# exit

6.  Specify that the switch will manage feature packs in cloud-managed mode.

switch (config)#  feature-pack mode cloud-managed

7.  (Optional) Once the feature pack is installed in the device, the show feature-pack server and show
feature-pack commands can be used to verify the LMS connectivity and feature pack subscription
status.

switch# show feature-pack server

Profile

=======
Location URL           : https://cx-feature-pack.arubanetworks.com

Location VRF           : mgmt

User account           : customer@example.com

Subscription Pool      : default

Public

Deploying a Cloud-managed Feature Pack Solution on... 31

Subscription Block     : 6300_test_block_2

Connection

==========

Status                  : Validation success

Reason                  : --

Last validation time    : Tue Sep 12 09:27:42 UTC 2023

Success validation time : Tue Sep 12 09:27:42 UTC 2023

switch# show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Wed Aug 28 2024

Serial Number(s) : SG2ZL50166

MAC Address      : 18:7a:3b:1b:f6:40

Hostname         : 6300

Mode             : Cloud Managed

State            : Feature pack installed and valid

Error Reason     : none

                                                Subscription   Feature

Feature                                         Status         Status

---------------------------------------------------------------------

Application Based Policy                        active          allowed

MACsec extensions for WAN                       active          allowed

Reflexive Policies for Port Access GBP Clients  active          allowed

Reflexive Policies for Port Access Clients      active          allowed
Changing the password for your HPE Aruba Networking Support Portal account

A network admin using feature packs in cloud mode may experience a lockout of their HPE account
after changing their password due to the switches syncing with the old password. When changing the
password of the user account credentials configured on switches for cloud-managed subscriptions, use
the following procedure to avoid unexpected account lockouts. Federated SSO (such as SAML SSO) is
not supported on the HPE user account used by the switch for cloud feature-pack.

8.  Configure all switches into file-mode using the command feature-pack mode file-based. This will
prevent the switches from syncing with the HPE Networking Support Portal during the password
change process.

NOTE

This will cause the switches to move into honor mode due to a mismatch
between feature-pack type and configured mode, but subscription features
will remain operational.

9.  Proceed with the password change on the HPE user account.

Public

Deploying a Cloud-managed Feature Pack Solution on... 32

10.  Configure the new password on each switch using the secure prompt or ciphertext options.

Using secure prompt:

switch (config-feature-pack-server)# credentials user <USER> password

<enter>”.
Using ciphertext :

switch (config-feature-pack-server)#  credentials user <USER> password

ciphertext <CIPHERTEXT>”

11.  Configure each switch into cloud-managed mode using the command feature-pack mode cloud-

managed, then verify subscriptions are validated using show feature-pack server and show feature-
pack.

Configure a non-default export password

Best practices is to use the service export-password command on the switch to configure a nondefault
export password. The export password is used to transform critical security parameters (such as
password hashes) into ciphertext suitable for exporting and showing commands such as show running-
config. This transformation enables safe switch configuration import and export.

Revoking and Reinstalling a Feature Pack Subscription on a
Standalone Switch

Before you replace a standalone switch using a cloud-mode feature pack subscription, the feature pack
subscription needs to be revoked.

Procedure

1.  Access the HPE Aruba Networking support portal and revoke the feature pack subscription from the

switch to be replaced. For details, see Revoking a Feature Pack Subscription

2.  Once the replacement switch is installed on the network, use the feature-pack server commands to

reinstall the cloud-based feature pack on the new switch. For details, see Deploying a Cloud-managed
Feature Pack Solution on a Standalone Switch.

Deploying a Cloud-Managed Feature Pack Solution on a VSF Stack

The following section describes the procedure to install an HPE Aruba Networking CX Advanced Feature
Pack on a VSF stack using feature pack subscriptions in cloud-managed mode.

Public

Revoking and Reinstalling a Feature Pack Subscript... 33

R
e
v
o
k
i
n
g

a
n
d

R
e
i
n
s
t
a
l
l
i
n
g

a

F
e
a
t
u
r
e

P
a
c
k

S
u
b
s
c
r
i
p
t
.
.
.

D
e
p
l
o
y
i
n
g

a

C
l
o
u
d
-
M
a
n
a
g
e
d

F
e
a
t
u
r
e

P
a
c
k

S
o
l
u
t
i
o
n

o
n
.
.
.

Prerequisites

•  The user has created a user account on the HPE Aruba Networking support portal.

•  The user has already ordered their feature pack subscriptions from HPE Aruba Networking reseller.

•  The HPE Aruba Networking support portal contains a subscription block activated with a number of

feature pack subscriptions equal to or greater than the number of devices in the VSF stack.

•  The Orders page on the HPE Aruba Networking support portal has been updated to indicate that the

subscriptions for the user account will be managed in cloud-managed mode. For details, see Viewing CX
Feature Subscription Pools and Feature Pack Orders.

Procedure

1.  Log on to the switch command-line interface.

2.  Enter the feature pack server configuration sub-mode.

switch(config)# feature-pack server

3.  Configure the location URL of the feature pack management server in the corresponding VRF.

switch(config-feature-pack-server)# https://cx-feature-

pack.arubanetworks.com vrf mgmt

4.  Configure the switch with the account credentials for your HPE Aruba Networking Support account.

switch(config-feature-pack-server)#  credentials user <username>

password plaintext <password>

5.  Configure the feature pack block and feature pack pool, then exit the feature pack server context.

switch(config-feature-pack-server)# block VSF_test

switch(config-feature-pack-server)# pool 6300_VSF

switch(config-feature-pack-server)# exit

6.  Specify that the switch should manage feature packs in cloud-managed mode.

switch (config)#  feature-pack mode cloud-managed

7.  Once the feature pack is installed in the device, the show feature-pack server and show feature-pack
commands can be used to verify the LMS connectivity and feature pack subscription status. Note
that the Serial Number(s) field in the output of the show feature-pack command includes the serial
numbers for all devices in the in the VSF stack.

switch# show feature-pack server

Profile

=======

Location URL           : https://cx-feature-pack.arubanetworks.com

Public

Deploying a Cloud-Managed Feature Pack Solution on... 34

Location VRF           : mgmt

User account           : customer@example.com

Subscription Pool      : 6300_VSF

Subscription Block     : VSF_test

Connection

==========

Status                  : Validation success

Reason                  : --

Last validation time    : Mon Sep 18 19:09:55 UTC 2023

Success validation time : Mon Sep 18 19:09:55 UTC 2023

6300# show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced feature pack

Expiration Date  : Sat Sep 07 2024

Serial Number(s) : SG1ZL53061 SG2ZL50131 SG2ZL50145

MAC Address      : 18:7a:3b:1b:b6:c0

Hostname         : 6300

Type             : Floating

Mode             : Cloud Managed

State            : feature pack installed and valid

Error Reason     : none

                                                Subscription   Feature

Feature                                         Status         Status

---------------------------------------------------------------------

Application Based Policy                        active          allowed

MACsec extensions for WAN                       active          allowed

Reflexive Policies for Port Access GBP Clients  active          allowed

Reflexive Policies for Port Access Clients      active          allowed
Configure a non-default export password

Best practices is to use the service export-password command on each switch to configure a
nondefault export password. The export password is used to transform critical security parameters
(such as password hashes) into ciphertext suitable for exporting and showing commands such as show
running-config. This transformation enables safe switch configuration import and export.

Replacing a VSF Stack Member Using a Cloud-Managed Feature Pack
Subscription

Use the following workflow to replace a VSF stack member with a switch that does not yet have a feature
pack subscription.

Public

Replacing a VSF Stack Member Using a Cloud-Managed... 35

R
e
p
l
a
c
i
n
g

a

V
S
F

S
t
a
c
k

M
e
m
b
e
r

U
s
i
n
g

a

C
l
o
u
d
-
M
a
n
a
g
e
d
.
.
.

Procedure

1.  Log on to the command-line interface of the VSF stack member.

2.  Verify that the advanced feature pack is being consumed by all switch members.

switch # show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Sat Sep 07 2024

Serial Number(s) : SG1ZL53061 SG2ZL50131 SG2ZL50145

MAC Address      : 18:7a:3b:1b:b6:c0

Hostname         : 6300

Type             : Floating

Mode             : Cloud Managed

State            : Feature Pack installed and valid

Error Reason     : none

                                                Subscription   Feature

Feature                                         Status         Status

---------------------------------------------------------------------

Application Based Policy                        active          allowed

MACsec extensions for WAN                       active          allowed

Reflexive Policies for Port Access GBP Clients  active          allowed

Reflexive Policies for Port Access Clients      active          allowed

3.  Remove the VSF stack member.

switch (config)# no vsf member 3

The specified switch will be unconfigured and rebooted

Do you want to continue (y/n)? y

switch # show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Sat Sep 07 2024

Serial Number(s) : SG2ZL50131 SG2ZL50145   << Member 3 serial number is

gone

MAC Address      : 18:7a:3b:1b:b6:c0

Hostname         : 6300

Type             : Floating

Mode             : Cloud Managed

State            : Feature Pack installed and valid

Error Reason     : none

                                                Subscription   Feature

Public

Replacing a VSF Stack Member Using a Cloud-Managed... 36

Feature                                         Status         Status

---------------------------------------------------------------------

Application Based Policy                        active          allowed

MACsec extensions for WAN                       active          allowed

Reflexive Policies for Port Access GBP Clients  active          allowed

Reflexive Policies for Port Access Clients      active          allowed

4.

If you are replacing a VSF conductor, reboot the VSF stack so that it no longer uses the MAC address of
the former conductor. The former conductor (now a standalone switch) and the remaining VSF stack will
continue to use the MAC address until the VSF stack reboots. If you attempt to add a feature pack to the
standalone switch before you reboot the VSF stack, you may get an error saying that is already using a
feature pack subscription, because the MAC address is the same as the existing VSF stack.

5.  When a new device is added to the VSF stack, the feature pack information for that stack member is

automatically updated.

switch # show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Sat Sep 07 2024

Serial Number(s) : SG2ZL50131 SG2ZL50145 SG1ZL78993 << New Stack Serial

Number

MAC Address      : 18:7a:3b:1b:b6:c0

Hostname         : 6300

Type             : Floating

Mode             : Cloud Managed

State            : Feature Pack installed and valid

Error Reason     : none

                                                Subscription   Feature

Feature                                         Status         Status

---------------------------------------------------------------------

Application Based Policy                        active          allowed
MACsec extensions for WAN                       active          allowed

Public

Replacing a VSF Stack Member Using a Cloud-Managed... 37

Reflexive Policies for Port Access GBP Clients  active          allowed

Reflexive Policies for Port Access Clients      active          allowed

NOTE

If you replace a VSF stack member with a standalone switch that is already
using a cloud-managed feature pack subscription, the HPE Aruba Networking
support portal will automatically extend the existing VSF feature pack
subscription to cover the new member, but it will not revoke the former
standalone feature pack. This results in an extra feature pack being consumed
by what has become single standalone switch that is no longer being used. As
a result, you must revoke the standalone feature pack to make it available for
other switches to use.

File-based Feature Pack Use Cases and Workflows

This chapter section describes the following workflows for deployments using feature pack subscriptions in
file-based mode.

•  Deploying a Feature Pack Solution on a Standalone Switch

•  Setting a File-Based Switch to Honor Mode

•  Deploying a Feature Pack Solution on a Standalone Switch

•  Replacing a VSF Stack Member using a Feature Pack Subscription

Subtopics

Deploying a File-Based Feature Pack Solution on a Standalone Switch
Setting a File-Based Switch to Honor Mode
Deploying a File-Based Feature Pack Solution on a VSF Stack
Replacing a VSF Stack Member Using a File-Based Feature Pack subscription
Replacing a VSF Stack Conductor Using a File-Based Feature Pack subscription

Deploying a File-Based Feature Pack Solution on a Standalone
Switch

The following section describes the procedure to install an HPE Aruba Networking CX Advanced feature
pack or a CX Premium feature pack on single standalone AOS-CX switches with feature pack subscriptions in
file -based mode.

Public

File-based Feature Pack Use Cases and Workflows 38

D
e
p
l
o
y
i
n
g

a

F
i
l
e
-
B
a
s
e
d

F
e
a
t
u
r
e

P
a
c
k

S
o
l
u
t
i
o
n

o
n

a

.
.
.

Prerequisites

•  The user has created a user account on the HPE Aruba Networking support portal.

•  The user has already ordered their feature pack subscriptions from HPE Aruba Networking reseller.

•  The Orders page on the HPE Aruba Networking support portal has been updated to indicate that the

subscriptions for the user account will be manged in file-based mode. For details, see Viewing Aruba CX
Feature Subscription Pools and Feature Pack Orders.

Procedure

1.  Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking support

user name and password.

2.  From the License Management page, select View Order.

Figure 1. Viewing Current Orders on the HPE Aruba Networking Support Portal

3.  On the Orders page, identify the feature pack you want to download and install on the switch.

4.  Click the green actions icon

 by the feature pack you want to download, and select Download. The

Download File window opens.

Figure 2. Downloading Feature Pack Subscriptions from the Orders Page

Public

Deploying a File-Based Feature Pack Solution on a ... 39

5.

In the Download File window, enter the host name, MAC address, and the serial number of the device.
Verify that the feature pack platform on this window matches the platform of the switch that will use
this feature pack.

6.  Click Download.

Figure 3. Downloading a Feature Pack File

7.  Access the switch command-line interface and ensure that the device is configured to use file-based

mode.

switch(config)# feature-pack mode file-based

8.  Use the copy command to copy the feature pack file to the switch.

Public

Deploying a File-Based Feature Pack Solution on a ... 40

switch# copy tftp://192.168.1.1/feature-pack feature-pack vrf mgmt

  % Total    % Received % Xferd  Average Speed   Time    Time     Time

Current

                                  Dload  Upload  Total   Spent    Left

Speed

100 21848  100 21848    0     0  7111k      0 --:--:-- --:--:-- --:--:--

7111k

writing feature-pack

9.  Use the show feature-pack command to validate the the feature pack mode is File based, that the
feature pack state shows Feature pack installed and valid and that all features are allowed.

6300# show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Thu Jul 27 2028

Serial Number(s) : SG2ZL50171

MAC Address      : 18:7a:3b:1b:c6:80

Hostname         : Test_FP

Type             : Device specific

Mode             : File based

State            : Feature pack installed and valid

Error Reason     : none

Subscription   Feature

Feature                                         Status         Status

---------------------------------------------------------------------

Application Based Policy                        active          allowed

MACsec extensions for WAN                       active          allowed

Reflexive Policies for Port Access GBP Clients  active          allowed

Reflexive Policies for Port Access Clients      active          allowed

10.  Next, access the HPE Aruba Networking Support portal and verify that the feature pack appears to have

been activated.

Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking support
user name and password.

From the License Management page, select the CX-Switch icon to open the Subscription Monitoring
page.

Public

Deploying a File-Based Feature Pack Solution on a ... 41

Check the details on this page to verify that the HPE Aruba Networking support portal correctly reflects
that the feature pack is associated with the correct device.

NOTE

For more details on monitoring feature Packs, refer to Monitoring Feature
Pack Subscriptions .

Setting a File-Based Switch to Honor Mode

In honor mode, the features supported by CX Advanced or CX Premium feature packs are enabled without
the presence of a active feature pack. Honor mode is intended for cases where a valid feature pack for
advanced or premium features has been purchased, but is not yet installed on the device. A warning
message may appear until a valid feature pack is installed.

Procedure

1.  Access the switch command-line interface and use the feature-pack mode honor command to set the

switch to honor mode.

switch(config)# feature-pack mode honor

2.  Once honor mode is configured, check the switch state using the show feature-pack command. The
output of this command should show that the feature pack mode is set to honor mode, and that
features are allowed and the feature pack subscription status is marked honor mode.

switch# shpw feature-pack

Feature Pack Summary

====================

Name             : --

Expiration Date  : --
Serial Number(s) :

MAC Address      : --

Hostname         : --

Type             : --

Mode             : Honor

State            : Feature pack mode honor configured

Error Reason     : none

                                              Subscription  Feature

Feature                                        Status        Status

-----------------------------------------------------------------------

Application Based Policy                        honor mode    allowed

MACsec extensions for WAN                       honor mode    allowed

Public

Setting a File-Based Switch to Honor Mode 42

Reflexive Policies for Port Access GBP Clients  honor mode    allowed

Reflexive Policies for Port Access Clients      honor mode    allowed

Deploying a File-Based Feature Pack Solution on a VSF Stack

The following section describes the procedure to install an Aruba CX premium or advanced feature pack on a
VSF stack with feature pack subscriptions in file -based mode.

Prerequisites

•  The user has created a user account on the HPE Aruba Networking support portal.

•  The user has already ordered their feature pack subscriptions from HPE Aruba Networking reseller.

•  The HPE Aruba Networking support portal contains a feature pack pool with a number of feature pack

subscriptions equal to or greater than the number of devices in the VSF stack.

•  The Orders page on the HPE Aruba Networking support portal has been updated to indicate that the
subscriptions for the user account will be manged in file-based mode. For details, see Viewing HPE
Aruba Networking CX Feature Subscription Pools and Feature Pack Orders.

Procedure

1.  Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking support

user name and password.

2.  From the License Management page, select View Order.

Figure 1. Viewing Current Orders on the HPE Aruba Networking Support Portal

Public

Deploying a File-Based Feature Pack Solution on a ... 43

D
e
p
l
o
y
i
n
g

a

F
i
l
e
-
B
a
s
e
d

F
e
a
t
u
r
e

P
a
c
k

S
o
l
u
t
i
o
n

o
n

a

.
.
.

3.  On the Orders page, identify the feature pack you want to download and install on the switch.

NOTE

Take care to verify that the available subscriptions in the block are equal or
greater than the members in the VSF stack.

4.  Click the green actions icon

 by the feature pack you want to download, and select Download. The

Download File window opens.

Figure 2. Downloading Feature Pack Subscriptions from the Orders page.

Public

Deploying a File-Based Feature Pack Solution on a ... 44

5.

In the Download File window, enter the VSF conductor MAC address (available in the output of
the show vsf command on the switch), the serial numbers of all the devices in the VSF stack in
comma-separated format. Verify that the feature pack platform displayed in this window matches the
platform of the switch that will use this feature pack.

6.  Click Download.

Figure 3. Downloading a Feature Pack File

Public

Deploying a File-Based Feature Pack Solution on a ... 45

7.  Access the switch command-line interface and ensure that the device is configured to use file-based

mode.

switch(config)# feature-pack mode file-based

8.  Use the copy command to copy the feature pack file to the switch.

switch# copy tftp://192.168.1.1/feature-pack feature-pack vrf mgmt

  % Total    % Received % Xferd  Average Speed   Time    Time     Time

Current

                                  Dload  Upload  Total   Spent    Left

Speed

100 21848  100 21848    0     0  7111k      0 --:--:-- --:--:-- --:--:--
7111k

writing feature-pack

9.  Use the show feature-pack command to check the status of the feature pack on the conductor or the
standby switch. Verify that the feature pack mode is File Based, the feature pack is installed and all
features are allowed, and that the serial numbers listed represent all VSF members.

6300# show feature-pack
Feature Pack Summary
===============

Name             : CX Software Advanced feature pack

Expiration Date  : Thu Sep 05 2024

Public

Deploying a File-Based Feature Pack Solution on a ... 46

Serial Number(s) : SG1ZL530661 SG2ZL504146 SG2ZL511853

MAC Address      : 18:7a:3b:1b:d7:80

Hostname         : VSF_demo

Type             : Device specific

Mode             : File Based

State            : feature pack installed and valid

Error Reason     : none

                                                Subscription   Feature

Feature                                         Status         Status

---------------------------------------------------------------------

Application Based Policy                        active          allowed

MACsec extensions for WAN                       active          allowed

Reflexive Policies for Port Access GBP Clients  active          allowed

Reflexive Policies for Port Access Clients      active          allowed

10.  Next, access the HPE Aruba Networking Support portal and verify that the feature pack appears to have

been activated.

Navigate to https://licensemanagement.hpe.com, and log in with your HPE Aruba Networking support
user name and password.

From the License Management page, select the CX-Switch icon to open the Subscription Monitoring
page.

Check the details on this page to verify that the HPE Aruba Networking support portal correctly reflects
that the feature pack is associated with all serial numbers in the VSF stack.

NOTE

For more details on monitoring feature packs, refer to Monitoring Feature
Pack Subscriptions .

Adding a Switch with a Feature Pack to a VSF Stack

When you add a standalone switch with an existing floating feature pack subscription to a VSF stack
with a floating feature pack subscription, the HPE Aruba Networking suport portal will automatically
extend the existing VSF feature pack to cover the new member, but it will not revoke the former
standalone feature pack. This will result in an extra feature pack subscription being consumed in the
HPE Aruba Networking support portal, as the single standalone subscription that is no longer being
used. You must revoke the standalone subscription in the support portal to make it available for other
switches to use.

Public

Replacing a VSF Stack Member Using a File-Based Fe... 47

R
e
p
l
a
c
i
n
g

a

V
S
F

S
t
a
c
k

M
e
m
b
e
r

U
s
i
n
g

a

F
i
l
e
-
B
a
s
e
d

F
e
.
.
.

Replacing a VSF Stack Member Using a File-Based Feature Pack
subscription

The following section describes the procedure to replace a VSF stack member in a VSF stack with a
file-based feature pack. This example installs the feature pack for all members of the stack,

Procedure

1.  Log on to the switch command-line interface.

2.  Use the no vsf member <member> command to remove the member you want to replace from the VSF

stack. The following example removes the stack member with the serial number SG2ZL50146.

switch(config)# no vsf member 3

The specified switch will be unconfigured and rebooted

Do you want to continue (y/n)? y

3.  After you remove the device from the VSF stack, features supported by the feature packs are still active.
The show feature-pack command still includes the serial number of the device which was removed. The
following example output shows that there are two members in the VSF stack, but three members are
still associated with the feature pack subscription.

6300(config)# show vsf

Force Autojoin             : Disabled

Autojoin Eligibility Status: Not Eligible

MAC Address                : 18:7a:3b:1b:d7:80

Secondary                  : 2

Topology                   : Chain

Status                     : No Split

Split Detection Method     : None

Mbr Mac Address         type           Status

ID

--- ------------------- -------------- ---------------
1   18:7a:3b:1b:d7:80   R8S90A         Conductor

2   ec:02:73:f7:ec:c0   R8S92A         Standby   <<-Only 2 VSF Members

in stack

switch(config)# show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Thu Sep 05 2024

Serial Number(s) : SG1ZL53061 SG2ZL50146 SG2ZL51153 <<-Old VSF Member

still listed

MAC Address      : 18:7a:3b:1b:d7:80

Hostname         : VSF_demo

Public

Replacing a VSF Stack Member Using a File-Based Fe... 48

Type             : Device specific

Mode             : File Based

State            : Feature pack installed and valid

Error Reason     : none

                                                Subscription

Subscription

Feature                                         Status          Status

---------------------------------------------------------------------

Application Based Policy                        active         allowed

MACsec extensions for WAN                       active         allowed

Reflexive Policies for Port Access GBP Clients  active         allowed

Reflexive Policies for Port Access Clients      active         allowed

4.  Before adding the device, note the serial number of the new replacement device. Next, navigate to the

subscription Monitoring page of the HPE Aruba Networking Support portal, as described in Monitoring
Feature Pack Subscriptions.

5.

In the Subscription Monitoring page, locate the feature pack subscription allocated to the VSF stack by
entering the serial number of the VSF stack conductor into the search bar at the top of the page.

6.  Click the green actions icon

 and select Modify. The Download File window opens.

Figure 1. Modify a Feature Pack Subscription

7.  Replace the serial number of the old VSF stack member with the serial number of the new VSF stack

member.

8.  Click Download to re-download the updated feature pack.

Figure 2. Downloading the File for New VSF Switch Members

Public

Replacing a VSF Stack Member Using a File-Based Fe... 49

9.  Use the copy command to copy the feature pack file to the switch.

switch# copy tftp://192.168.1.1/feature-pack feature-pack vrf mgmt

  % Total    % Received % Xferd  Average Speed   Time    Time     Time

Current

                                  Dload  Upload  Total   Spent    Left

Speed

100 21848  100 21848    0     0  7111k      0 --:--:-- --:--:-- --:--:--

7111k

writing feature-pack

10.  Use the show feature-pack command to validate that the new switch serial number is present in the

updated feature pack.

6300# show feature-pack

Feature Pack Summary

===============
Name             : CX Software Advanced Feature Pack

Expiration Date  : Thu Sep 05 2024

Serial Number(s) : SG1ZL53061 SG2ZL50172 SG2ZL51153  << New member

serial number

MAC Address      : 18:7a:3b:1b:d7:80

Hostname         : VSF_demo

Type             : Device specific

Mode             : File Based

State            : Feature pack installed and valid

Error Reason     : none

                                                Subscription   Feature

Public

Replacing a VSF Stack Member Using a File-Based Fe... 50

Feature                                         Status         Status

---------------------------------------------------------------------

Application Based Policy                        active          allowed

MACsec extensions for WAN                       active          allowed

Reflexive Policies for Port Access GBP Clients  active          allowed

Reflexive Policies for Port Access Clients      active          allowed

11.  Add the new device to the VSF stack. The new device is automaticially enabled with the feature pack

subscription.

12.  (Optional) Issue the show vsf command and the show feature-pack command a second time to verify

that the new VSF member appears in the stack, and to verify the status of the feature pack on the stack.

switch# show vsf

Force Autojoin             : Disabled

Autojoin Eligibility Status: Not Eligible

MAC Address                : 18:7a:3b:1b:d7:80

Secondary                  : 2

Topology                   : Ring

Status                     : No Split

Split Detection Method     : None

Mbr Mac Address         type           Status

ID

--- ------------------- -------------- ---------------

1   18:7a:3b:1b:d7:80   R8S90A         Conductor

2   ec:02:73:f7:ec:c0   R8S92A         Standby

3   18:7a:3b:1b:b6:40   R8S89A         Member

switch(config)# show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Thu Sep 05 2024

Serial Number(s) : SG1ZL53061 SG2ZL50172 SG2ZL51153 < New member serial
number

MAC Address      : 18:7a:3b:1b:d7:80

Hostname         : VSF_demo

Type             : Device specific

Mode             : File Based

State            : Feature pack installed and valid

Error Reason     : none

                                               Subscription    Feature

Feature                                        Status          Status

---------------------------------------------------------------------

Application Based Policy                        active         allowed

MACsec extensions for WAN                       active         allowed

Public

Replacing a VSF Stack Member Using a File-Based Fe... 51

Reflexive Policies for Port Access GBP Clients  active         allowed

Reflexive Policies for Port Access Clients      active         allowed

13.  (Optional) Return to the Feature Pack Monitoring page on the HPE Aruba Networking support portal,
and verify that the serial numbers for that order reflect the correct serial numbers for that stack.

Replacing a VSF Stack Conductor Using a File-Based Feature Pack
subscription

The following section describes the procedure to replace a VSF stack conductor in a VSF stack with a
file-based feature pack. This example installs the feature pack for all members of the stack,

Procedure

1.  Log on to the switch command-line interface.

2.  Trigger a switchover so member 1 is no longer the conductor.

switch# vsf switchover

This will cause an immediate switchover to the standby

and the conductor will reboot.

Do you want to continue (y/n)? y

switch#

3.  Use the no vsf member <member> command to remove the conductor from the VSF stack. The

following example removes the stack member with the serial number SG2ZL50146.

switch(config)# no vsf member 1

The specified switch will be unconfigured and rebooted

Do you want to continue (y/n)? y

4.  After you remove the conductor from the VSF stack, features supported by the feature packs are

still active. The show feature-pack command still includes the serial number of the device which was
removed. The following example output shows that there are two members in the VSF stack, but three
members are still associated with the feature pack subscription.

6300(config)# show vsf

Force Autojoin             : Disabled

Autojoin Eligibility Status: Not Eligible

MAC Address                : 18:7a:3b:1b:d7:80
Secondary                  : 2

Topology                   : Chain

Status                     : No Split

Split Detection Method     : None

Public

Replacing a VSF Stack Conductor Using a File-Based... 52

R
e
p
l
a
c
i
n
g

a

V
S
F

S
t
a
c
k

C
o
n
d
u
c
t
o
r

U
s
i
n
g

a

F
i
l
e
-
B
a
s
e
d
.
.
.

Mbr Mac Address         type           Status

ID

--- ------------------- -------------- ---------------

1   18:7a:3b:1b:d7:80   R8S90A         Conductor

2   ec:02:73:f7:ec:c0   R8S92A         Standby   <<-Only 2 VSF Members

in stack

switch(config)# show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Thu Sep 05 2024

Serial Number(s) : SG1ZL53061 SG2ZL50146 SG2ZL51153 <<-Old VSF Member

still listed

MAC Address      : 18:7a:3b:1b:d7:80

Hostname         : VSF_demo

Type             : Device specific

Mode             : File Based

State            : Feature pack installed and valid

Error Reason     : none

                                                Subscription

Subscription

Feature                                         Status          Status

---------------------------------------------------------------------

Application Based Policy                        active         allowed

MACsec extensions for WAN                       active         allowed

Reflexive Policies for Port Access GBP Clients  active         allowed

Reflexive Policies for Port Access Clients      active         allowed

5.  Add the new conductor to the VSF stack.

6.  Reboot the VSF stack so that it no longer uses the MAC address of the former conductor. The former

conductor (now a standalone switch) and the remaining VSF stack will continue to use the MAC address
until the VSF stack reboots. If you attempt to add a feature pack to the standalone switch before you
reboot the VSF stack, you may get an error saying that it already has a feature pack, because the MAC
address is the same as the existing VSF stack.

7.  Note the serial number of the replacement device and the new MAC address of the stack.

8.  Download the new feature pack using the procedure described in Deploying a File-Based Feature Pack

Solution on a VSF Stack.

9.  Use the show feature-pack command to validate that the new switch serial number is present in the

updated feature pack.

6300# show feature-pack

Feature Pack Summary

Public

Replacing a VSF Stack Conductor Using a File-Based... 53

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Thu Sep 05 2024

Serial Number(s) : SG1ZL53061 SG2ZL50172 SG2ZL51153  << New member

serial number

MAC Address      : 18:7a:3b:1b:d7:80

Hostname         : VSF_demo

Type             : Device specific

Mode             : File Based

State            : Feature pack installed and valid

Error Reason     : none

                                                Subscription   Feature

Feature                                         Status         Status

---------------------------------------------------------------------

Application Based Policy                        active          allowed

MACsec extensions for WAN                       active          allowed

Reflexive Policies for Port Access GBP Clients  active          allowed

Reflexive Policies for Port Access Clients      active          allowed

10.  (Optional) Issue the show vsf command and the show feature-pack command a second time to verify

that the new VSF member appears in the stack, and to verify the status of the feature pack on the stack.

switch# show vsf

Force Autojoin             : Disabled

Autojoin Eligibility Status: Not Eligible

MAC Address                : 18:7a:3b:1b:d7:80

Secondary                  : 2

Topology                   : Ring

Status                     : No Split

Split Detection Method     : None

Mbr Mac Address         type           Status

ID

--- ------------------- -------------- ---------------

1   18:7a:3b:1b:d7:80   R8S90A         Conductor

2   ec:02:73:f7:ec:c0   R8S92A         Standby

3   18:7a:3b:1b:b6:40   R8S89A         Member

switch(config)# show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Thu Sep 05 2024

Serial Number(s) : SG1ZL53061 SG2ZL50172 SG2ZL51153 < New member serial

number

MAC Address      : 18:7a:3b:1b:d7:80

Public

Replacing a VSF Stack Conductor Using a File-Based... 54

Hostname         : VSF_demo

Type             : Device specific

Mode             : File Based

State            : Feature pack installed and valid

Error Reason     : none

                                               Subscription

Feature                                        Status          Status

---------------------------------------------------------------------

Application Based Policy                        active         allowed

MACsec extensions for WAN                       active         allowed

Reflexive Policies for Port Access GBP Clients  active         allowed

Reflexive Policies for Port Access Clients      active         allowed

11.  (Optional) Return to the Feature Pack Monitoring page on the HPE Aruba Networking support portal,
and verify that the serial numbers for that order reflect the correct serial numbers for that stack.

Viewing Feature Packs on Switches Managed by Central

You do not need to enable feature packs on AOS-CX switches managed by Aruba Central, as all features
supported by these feature packs are enabled when the switch connects to Aruba Central. Aruba Central
takes precedence over any other feature pack configured mode.

NOTE

If you want to use the HPE Aruba Networking support portal for feature pack
management instead of Aruba Central, disable Central on the switch. This will
allow you to set up a new cloud server profile.

Issue the show feature-pack command to verify that the switch is currently connected to Aruba Central.

6300# show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Fri Aug 12 2033

Serial Number(s) : SG2ZL50199

MAC Address      : 18:7a:3b:1b:c6:16

Hostname         : 6300M

Type             : Device specific

Mode             : File Based

State            : Aruba Central managed and connected

Error Reason     : none

Subscription    Feature                        Status          Status

Public

Viewing Feature Packs on Switches Managed by Centr... 55

V
i
e
w
i
n
g

F
e
a
t
u
r
e

P
a
c
k
s

o
n

S
w
i
t
c
h
e
s

M
a
n
a
g
e
d

b
y

C
e
n
t
r
.
.
.

---------------------------------------------------------------------

Application Based Policy                        active          allowed

MACsec extensions for WAN                       active          allowed

Reflexive Policies for Port Access GBP Clients  active          allowed

Reflexive Policies for Port Access Clients      active          allowed
The feature-pack on the switch will display the Aruba Central managed and connected state only if all the
following are true:

•  The switch has connection to Central.

•  The switch is onboarded to the GreenLake for PrivateCloud (GLPC) device inventory .

•  The switch is assigned to Central Application in GLPC.

•  The switch has a valid Central License assigned in GLPC .

If a Central-managed switch is unable to reach Aruba Central, features supported by the feature pack are still
allowed on the switch, even though the output of the show feature-pack command shows that the feature
pack subscription is inactive. The mode field displays a default status of File-Based, but the mode does not
apply as switch is managed by Central.

6300# show feature-pack

Feature Pack Summary

===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Fri Aug 12 2033

Serial Number(s) : SG2ZL50199

MAC Address      : 18:7a:3b:1b:c6:16

Hostname         : 6300M

Type             : Device specific

Mode             : File Based

State            : Aruba Central managed and disconnected

Error Reason     : none

Subcription     Feature

Feature
---------------------------------------------------------------------

Status          Status

Application Based Policy                        inactive        allowed

MACsec extensions for WAN                       inactive        allowed

Reflexive Policies for Port Access GBP Clients  inactive        allowed

Reflexive Policies for Port Access Clients      inactive        allowed
In addition, the following message is logged when the switch connects to Aruba Central.

2023-09-20T07:04:03.172885+00:00 6300 feature-pack-mgrd[4077]: Event|14407|
LOG_INFO|CDTR|1|Feature pack subscription through Aruba Central is connected
For more log messages related to feature pack events, see Feature Pack events.

Public

Viewing Feature Packs on Switches Managed by Centr... 56

Feature pack commands

Select a command from the list in the left navigation menu.

Subtopics

erase feature-pack
feature-pack mode
feature-pack server
feature-pack validate
show feature-pack

erase feature-pack

Syntax

erase feature-pack [reset]

Description

Remove the installed feature pack and delete the feature pack file.

Parameter

reset

Example

Description

Optional. Include this parameter if you do not want to use subsc
ription features anymore and want to stop receiving honor mod
e warning logs messages. Running this command will disable
all subscription features and stop honor warnings.

Remove the feature pack. The switch will continue to operate in honor mode.

switch# erase feature-pack

Remove the feature pack and disable all subscription features.

switch# erase feature-pack reset

This operation will delete the feature pack subscription key and reset

feature pack enforcement to a factory default state. This will disable
advanced features that require a subscription to operate and may impact
network operation if those features are in use.

After running this command, advanced features can only be re-enabled

through one of the following:

Public

Feature pack commands 57

1. Installing a new feature-pack subscription key.

2. Connecting to HPE Aruba Networking Central.

3. Configuring honor mode.

Continue (y/n)?

Command History

Release

10.14

10.13

Modification

The reset parameter is introduced.

Command introduced.

Command Information

Platforms

Command context

Authority

manager

Administrators or local user group members with execution righ
ts for this command.

6300

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

feature-pack mode

Public

feature-pack mode 58

Syntax

feature-pack mode

   cloud-managed

   file-based

   honor

   no ...

Description

Set the operation mode for a feature pack deployment.

HPE Aruba Networking provides three modes for feature pack management: cloud-managed, file-based,
and honor. In the event of a mismatch between the installed feature pack and the feature pack mode, the
device will operate in honor mode.

Parameter

Description

  cloud‐managed

  file‐managed

honor

no ...

Usage

The device uses cloud‐based feature pack management

The device uses a manually installed feature pack file. This is th
e default feature pack mode.

A valid feature pack has been obtained, but is not yet installed.

Resets the configuration back to the default file‐based feature
pack mode.

Switches using feature pack subscription keys in cloud mode share a pool of one or more feature pack
subscription keys managed using the HPE Networking support portal. By default, a switch using an HPE
Aruba Networking CX feature pack in cloud mode will contact the HPE Networking support portal once a
day to automatically synchronize with the feature pack subscription key management database. With this
deployment type, the HPE Networking support site can automatically distribute and manage feature packs
for all devices in a group, making it a scalable solution for larger deployments and for global accounts across
geographies.

Networks with a single switch, or with multiple switches on isolated networks that cannot contact the HPE
Networking support site should use feature pack subscription keys in file-based mode, where a feature pack
is manually enabled on a switch using a non-sharable subscription key tied to that individual switch's serial
number or MAC address.

Honor mode is intended for cases where a valid feature pack for advanced features has been purchased, but
is not yet installed on the device. Advanced features on this device will be operational in Honor mode, but a
warning message may be seen until a valid feature pack is installed. Please note that HPE Aruba Networking
will remove support for Honor mode in a future release and advanced features will only be operational if the
applicable subscription fees are paid and a valid feature pack is installed.

Public

feature-pack mode 59

Examples

switch(config)# feature pack mode cloud-managed

Command History

Release

10.13

Modification

Command introduced

Command Information

Platforms

Command context

Authority

config

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

6300

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

feature-pack server

Syntax

feature-pack server

   block <block>

   credentials user <USER> password [{plaintext <PASSWORD>}|{ciphertext

Public

feature-pack server 60

<PASSWORD>}]

   location <LOCATION> [vrf <VRF>]

   pool <pool>

Description

If the switch is in cloud-managed feature pack mode, use this command to define the switch's feature pack
profile. A switch in cloud-managed mode uses the information in this profile to contact the feature pack
management server and download and install any allocated feature packs.

Parameter

block <block>

credentials

Description

If the subscription pool for the profile contains more than on
e subscription block, specify the subscription block within that
pool to be assigned.

Configures the credentials used by the device to contact and au
thenticate to the feature pack server.

   user <USER>

The user name of a feature pack server account.

   password

plaintext <PASSWORD>

Select a mode for entering the feature pack server password. If
you press <enter> after the password parameter, you will enter
a secure prompt that allows you to securely enter a hidden pass
word. This is the recommended method for entering a plaintext
password.

You can include the optional plaintext parameter to configure a
plain text password (not recommended), or use the optional cip
hertext parameter to enter previously encrypted ciphertext pas
sword.

Optional. Enter a password in plain text without the secure pro
mpt. This option does not hide the password in the CLI, and is n
ot recommended.

ciphertext <PASSWORD>

Optional. Enter a password as previously encrypted text. This is
the recommended method for entering an encrypted password.

location <LOCATION>

The FQDN of the feature pack server;

   [vrf <VRF>]

pool <pool>

https://cx‐feature‐pack.arubanetworks.com

(Optional) Specify the VRF used to contact the feature pack ser
ver.

Configures the feature pack server subscription pool. This infor
mation is used by the feature pack server to properly identify th
e subscription to be assigned to the device.

Public

feature-pack server 61

Examples

Defining a feature pack server by entering a hidden plain text user password.

switch(config)# feature-pack server

switch(config-feature-pack-server)# location https://cx-feature-

pack.arubanetworks.com vrf mgmt

switch(config-feature-pack-server)# credentials user myLMSUser1234 password

Enter password: *****

Confirm password: *****
Defining a feature pack server with an encrypted ciphertext user password.

switch(config)# feature-pack server

switch(config-feature-pack-server)# location https://cx-feature-

pack.arubanetworks.com vrf mgmt

switch(config-feature-pack-server)# credentials user myLMSUser1234 password

ciphertext

AQBapcmUTsCVdaTGkLA3mN2sslLgsNOdqFUP0j+CaCxVdz7oEwAA2OmsmBmgPHavS+6Gkgm2twE4

NU1Y=

Command History

Release

10.13.1000

Modification

Plaintext passwords should now be configured using the secure prompt, which
can be accessed by pressing <enter> after the password keyword. This makes t
he plaintext and ciphertext keywords optional. It is recommended to use either
the secure prompt or the ciphertext option.

10.13

Command introduced

Command Information

Platforms

Command context

Authority

config
config‐feature‐
pack‐server

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

6300

6400

8100

8320

8325

8325H

8325P

Public

feature-pack server 62

Platforms

Command context

Authority

8360

8400

9300

9300S

10000

10040

feature-pack validate

Syntax

feature-pack validate

Description

Manually trigger a feature pack validation on the HPE Networking support portal. (By default, automatic
validation happens once every day.) This command is only applicable for feature packs in cloud-managed
mode.

Examples

switch# feature-pack validate

Command History

Release

10.13

Modification

Command introduced

Command Information

Platforms

Command context

Authority

manager

Administrators or local user group members with execution righ
ts for this command.

6300

6400

8100

Public

feature-pack validate 63

Platforms

Command context

Authority

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

Syntax

show feature-pack [server]

Description

Display the current feature pack summary and status, and feature status of features that require a feature
pack.

Parameter

Description

(Optional) For feature packs in cloud‐managed mode, Include
this parameter to display configuration settings used to conne
ct to the feature pack management server, and display the conn
ection status information.

server

Examples

switch# show feature-pack

Feature Pack Summary
===============

Name             : CX Software Advanced Feature Pack

Expiration Date  : Thu May 4 2025

Serial Number(s) : TW13KM304V

Public

show feature-pack 64

MAC Address      : 90:20:c2:c4:98:00

Hostname         : 6405

Mode             : File based

Status           : feature pack installed and valid

Error Reason     : None

Subscription   Feature

Feature                                         Status         Status

---------------------------------------------------------------------

Application Based Policy                        active          allowed

MACsec extensions for WAN                       active          allowed

Reflexive Policies for Port Access GBP Clients  active          allowed

Reflexive Policies for Port Access Clients      active          allowed

switch# switch# show feature-pack server

Profile

=======

Location URL           : https://cx-feature-pack.arubanetworks.com

Location VRF           : mgmt

User account           : customer@example.com

Subscription Pool      : default

Subscription Block     : 6300_test_block_2

Connection

==========

Status                  : Validation success

Reason                  : --

Last validation time    : Tue Sep 12 09:27:42 UTC 2023

Success validation time : Tue Sep 12 09:27:42 UTC 2023
The output of the show feature-pack command include the following information:

Value

Name

Expiration Date

Serial Numbers

MAC address

Hostname

Type

Description

Name of the feature pack

The date that the feature pack subscription expires

Serial numbers for that feature pack. If the feature pack is used
by multiple switches (for example, in a VSF deployment) then t
he Serial Number(s) field displays all the switch serial numbers
for that feature pack.

MAC address of the switch using the feature pack

Host name of the switch using the feature pack

Shows the feature pack file type:

Public

show feature-pack 65

Value

Description

•  Device specific: Feature pack was manually downloaded fro
m a feature pack server account in local mode. Use this feat
ure pack with a switch in file‐based mode..

•  Floating: The feature pack was automatically downloaded f
rom a cloud mode feature pack account on the HPE Networ
king support portal. This feature pack should be used with t
he switch in cloud‐managed mode.

Mode

Shows the feature pack configuration mode:

•  Cloud management: Switches using feature pack subscript
ions in cloud‐managed mode share a pool of one or more
feature pack subscriptions. These subscriptions are manage
d through the HPE Networking support portal.

•  File Based: If a switch is using a feature pack in file‐ba

sed mode, you must manually upload the feature pack usin
g the copy command and enable it on a switch using a non
‐sharable subscription file tied to that individual switch's s
erial number or MAC address.

•  Honor: Honor mode is intended for cases where a valid feat
ure pack for advanced features has been purchased, but is
not yet installed on the device. Advanced features on this d
evice will be operational in honor mode, but a warning mes
sage may be seen until a valid feature pack is installed. Plea
se note that HPE Aruba Networking will remove support fo
r Honor mode in a future release and advanced features wi
ll only be operational if the applicable subscription fees are
paid and a valid feature pack is installed. This message is s
hown when the switch is configured to use a cloud‐manag
ed feature pack profile using the feature pack mode cloud
‐managed command.

Status

This message displays the current status of the feature pack:

•  No feature pack installed: No feature pack is detected on t

he switch.

•  Feature pack installed and valid: Feature pack installed wi

th no errors.

•  Feature pack install error: The feature pack has invalid d

ata.

•  Feature pack expired: The feature pack subscription has

expired.

Public

show feature-pack 66

Value

Description

•  Feature pack removed: The feature pack was erased from t

he switch using the erase command.

•  Subscription through HPE Aruba Networking Central is
connected: Switch is actively connected to HPE Aruba Net
working Central. Subscription features are operational. The
feature‐pack on the switch will display this state only if all
the following are true:

◦  The switch has a connection to HPE Aruba Networking

Central.

◦  The switch is onboarded to the GreenLake for PrivateCl

oud (GLPC) device inventory .

◦  The switch is assigned to HPE Aruba Networking Cent

ral Application.

◦  The switch has a valid HPE Aruba Networking Central

License assigned.

•  Subscription through HPE Aruba Networking Central is
disconnected: Switch is disconnected from HPE Aruba Net
working Central. Subscription features are still operational.
The switch will appear in this state if any of the requiremen
ts for the status is not currently true, A switch may also dis
play this feature pack status if the switch has connection to
HPE Aruba Networking Central, is assigned to the Central a
pplication, but has no Central License attached. In this case
the switch will be in disconnected state even if it never was
previously in connected state.

•  Feature pack mode honor configured: The switch does n
ot have a valid feature pack. Subscription features are ope
rational, and is operating in honor mode until the feature pa
ck is installed.

•  Cloud managed server is disconnected: The switch is man
aging feature packs in cloud mode, but the switch is no lon
ger able to reach the HPE Networking support portal. The s
witch will continue to operate in honor mode.

•  Cloud managed and subscription revoked from server: T
he switch is managing the feature pack in cloud mode, but
feature pack has been revoked from the switch through the
HPE Networking support portal.The switch will continue to
operate in honor mode until the feature pack is removed fro
m the switch.

Public

show feature-pack 67

Value

Description

Error Reason

•  Cloud managed server validation error: Server validation
failed. Issue the command show feature pack server for m
ore information.

•  Unexpected VSF member in stack: A feature pack intende
d for a VSF stack is installed on a VSF member whose serial
number is not covered under the current feature pack.
•  Mode does not match installed feature pack type: The fe
ature pack type (device‐locked or floating) does not matc
h the configured mode. Device‐locked feature packs shou
ld be used in file‐based deployments only, and floating fe
ature packs should be used by cloud‐managed deployme
nts.

If the feature pack Status field displays an error status, this fiel
d displays details about possible causes for the issue.

•  Serial number mismatch: The serial number in the installe
d feature pack does not match the switch's serial number.
•  MAC address mismatch: The MAC address in the installed
feature pack does not match the switch's serial number.
•  Feature pack file parsing error: The feature pack file has a

n invalid format.

•  Feature pack file signature invalid: The feature pack file

was modified.

Feature

Name of the feature supported by the feature pack.

Subscription Status

Current subscription status;

inactive: Subscription is inactive or has expired.

•  active: Subscrition is active.
•
•  honor: Installed feature pack has expired or cloud managed
feature pack has encountered an error. Warnings will be log
ged periodically.

Feature Pack Status

Current status of the feature pack:

•  allowed: Feature is functional.
•  blocked: Feature is not functional and will require a valid fe

ature pack to be functional.

•  not running: Feature is not configured on switch and daem

on is not running

•  unsupported on SKU: Feature is not supported on product

SKU.

Public

show feature-pack 68

Value

Description

•  unsupported with VSF: Feature is not supported on a VSF

stack.

The output of the show feature-pack server command include the following information:

Location URL

Location VRF

User Account

Subscription Pool

Fully qualified domain name of the feature pack subscription se
rver, for example, https://cx‐feature‐pack.arubanetworks.c
om

VRF used to access the feature pack subscription server.

User name of the user account at the HPE Networking support
portal associated with the feature pack.

Name of the subcription pool associated with the feature pack.
This can be the Default subscription pool, or a user‐defined s
ubscription pool.

Subscription Block

Subscription block associated with the feature pack.

Indicates whether the switch was able to contact the feature pa
ck server.

If the switch is unable to contact the feature pack server, this fie
ld can display information about the cause for the connection fa
ilure.

Timestamp showing the date and time the switch last contacte
d the feature pack server.

Timestamp showing the date and time of the last successful fe
ature pack installation or validation against the feature pack ser
ver

Status

Reason

Last validation time

Success Validation time

Command History

Command Information

Platforms

Command context

Authority

6300

6400

manager

Administrators or local user group members with execution righ
ts for this command.

Public

show feature-pack 69

Platforms

Command context

Authority

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

Frequently Asked Questions (FAQs)

The following sections of this document answer frequently asked questions (FAQs) about AOS-CX feature
packs and feature pack management. Select any category below to few FAQs and answers for that category
type.

•  General Feature Pack FAQs

•  Advanced Feature Pack FAQs

•  10000 Switch Series Feature Pack FAQs

•  Subscription Management FAQs

•  Feature Pack Domain/Subaccount FAQs

•  Feature Pack Expiration and Renewal FAQs

•  VSF and VSX FAQs

General Feature Pack FAQs

What type of feature packs do I need?

The choice of feature pack depends on your desired features. AOS-CX features are organized into a set of
native enterprise features available in every CX switch at no cost, and an optional, term-based Advanced
Feature Pack for 6300, 6400, 8xxx, and 9300 Switch series. Feature packs can be consumed standalone or

Public

Frequently Asked Questions (FAQs) 70

combined with a Central Advanced subscription. The 10000 Switch series require a Advanced Feature Pack,
which can be optionally replaced by a Premium Feature Pack to support additional features.

Will I receive switch software updates even if I do not purchase a Feature Pack?

AOS-CX software updates are not contingent upon whether a customer has purchased a feature pack. HPE
Aruba Networking will continue to maintain and enhance the native functionalities of the AOS-CX operating
system, making them available to customers through the regular AOS-CX software release cycle.

At any point of time, how many feature packs can a CX switch have?

A switch can have one single feature pack, or can operate with no feature pack installed. A switch cannot
have more than one feature pack.

Does switch platform define the required type of feature packs for product?

The software feature set drives the requirement for Feature Pack. There is only one Advanced Feature Pack
for 6300, 6400, 8xxx, and 9300 Switch series. Only 10000 switch series offers two options: an Advanced
Feature Pack and a Premium Feature Pack.

How I know which features are strictly enforced and cannot be used without a subscription?

The output of the show feature-pack provides this information per switch platform.

Advanced Feature Pack FAQs

What will happen when I configure an advanced feature without a Feature Pack?

When a user configures an advanced feature the CLI will display a warning. In honor-based enforcement the
user is warned that an advanced feature is in use, and it will operate normally. In Strict enforcement mode,
the user is warned that a feature is advanced, and the feature will not operate until a valid feature pack is
installed. Note: all configurations are accepted with warnings. Features become operational depending on
the enforcement mode.

Can I upgrade to the CX Advanced Feature Pack once I have purchased a switch?

Yes. You can upgrade to a CX Advanced Feature Pack after a switch purchase.

If I already own an HPE Aruba Networking Central Advanced subscription, is there any need to
purchase CX Software Advanced feature pack subscription?

If you have a Central Advanced subscription for6300, 6400, 8xxx, and 9300 Switch series, there is no need
to purchase a CX Advanced Feature Pack.

A Central Advanced subscription automatically enables CX features included in the CX Advanced Feature
Pack. Note that the 10000 Switch series does require a feature pack, even if you already own a Central
Advanced subscription for a CX 10000 switch.

If I purchased a 1-year CX Advanced Feature Pack for a switch, after one year can I alter my plan to
3-year subscription?

Yes. HPE Aruba Networking does allow you to alter subscription plans.

Public

Frequently Asked Questions (FAQs) 71

If I purchased 3-year CX Advanced Feature Pack for a 10000 Switch, can I upgrade after one year from
the current CX Advanced subscription to the CX Premium Feature Pack?

Currently there is no automated upgrade option, but HPE Aruba Networking sales can provide a manual
upgrade option.

Can I purchase an Advanced Feature Pack subscription for all the HPE Aruba Networking CX switch
series?

No. The Advanced Feature Pack is only available for the 6300, 6400, 8100, 8320, 8325, 8360, 8400, 9300,
and 10000 Series switches. There is no requirement or option to purchase any feature pack for 4100i, 6000,
and 6100 platforms.

What features are supported in each CX series with purchase of CX Advanced and Premium feature
packs?

For platform-specific advanced feature support, refer to the HPE Aruba Networking Switch Feature
Navigator.

How do I can get a temporary CX Advanced Feature Pack subscription to perform a demo for new
advanced features?

Contact your HPE Aruba Networking sales representative for more information about a 90-day CX
Advanced Feature Pack Eval subscription. Eval feature packs are intended for evaluation purposes only
and are not meant for production deployments.

10000 Switch Series Feature Pack FAQs

Is there any Evaluation feature pack for the 10000 Switch series ?

Yes. There is a CX Advanced Feature Pack Eval subscription and a CX Premium Feature Pack Eval
subscription for 10000 Switch series.

How are feature pack enforced on the 10000 Switch series platform, considering that some features
are deployed from AMD Pensando PSM, and strict enforcement cannot be applied to them?

Since the policy features are deployed from AMD Pensando Policy and Services Manager (PSM), PSM-
specific features on the 10000 Switch series are not enforced. Non-PSM features like Container are subject
to enforcement in AOS-CX.

Are all AOS-CX 10000 features available under the CX Premium Feature Pack?

Yes. Several 10000 Switch series features are available in both the CX Advanced Feature Pack and the CX
Premium Feature Pack, but some select features will only be available with CX Premium.

How do the feature pack warning message on 10000 Switch series differ from other CX platforms?

•  All platforms log a warning message when an advanced feature is used without a valid feature pack

while in honor mode. However, 10000 Switch series will also log a warning message if no feature pack is
found, regardless of whether advanced features are used.

•  A 10000 Switch series displays warning messages if a user configures advanced features while no

feature pack file is installed.

Public

Frequently Asked Questions (FAQs) 72

Subscription Management FAQs

How do I place an order for the CX Software feature packs?

Orders are processed by an HPE Aruba Networking representative. You must have an account on the HPE
Aruba networking licensing management portal to activate your orders.

Does the HPE Aruba Networking licensing management portal support Multi-Factor Authentication
(MFA) for feature packs in cloud-managed mode?

Multi-Factor Authentication (MFA) is supported on HPE user accounts and MFA is compatible with all
feature pack modes and management methods. MFA is both supported and recommended.

Feature Pack Domain/Subaccount FAQs

Can users with access to a subaccount of a feature pack domain view or access feature packs within
another user account of that domain?

No. A user cannot create a feature pack pool in any domain or user account other than their own. However,
if a user account is added to multiple domains in the HPE Aruba Networking support portal then that user
account can view and access feature-packs in those multiple domains. It is important to note that a user
account can only have one domain as its “primary account”. If a user account is part of multiple domains,
then when that user account’s credentials are configured on the switch for cloud-managed feature-packs,
the HPE Aruba Networking support portal will connect that switch to the domain assigned as the user’s
primary account.

If I already created a subaccount for a feature pack domain, can I create another subaccount within the
first subaccount?

No. You cannot create a subaccount within another subaccount.

Feature Pack Revocation FAQs

What user roles within a feature pack domain account have access to this view or revoke a feature
pack?

Both Admin and standard users can view feature pack details, but only Admin users will be able to revoke a
feature pack.

Feature Pack Expiration and Renewal FAQs

What happens if a feature pack expires? Do services stop?

When a feature pack expires, advanced features are not out of service immediately. These features will
continue to work in honor mode. This mode provides a warning message that reminds users to renew, yet
avoids strict enforcement that can disable a feature and potentially cause network disruptions.

How can I track feature pack expirations and renewals?

Feature pack renewal can be automated or done manually. The HPE Aruba Networking support portal allows
users to monitor feature packs they have generated, and order a new feature pack to replace one about to
expire. With automated renewal, if a feature pack has expired, the Support Portal will trigger an auto-renewal

Public

Frequently Asked Questions (FAQs) 73

order available for the number of feature packs that must be renewed, if available. The Support Portal will
then activate the new feature packs to allow the switch to undergo auto-renewal of its feature pack.

VSF and VSX FAQs

If I want to enable advanced features on a 6300 Switch series VSF stack, then how many feature packs
do I need to purchase?

Stacked switches are required to have one feature pack per member,

I have a VSF stack of five members, each having its own feature pack. If I add a new member and there
is no feature pack available in feature pack pool within LMS, then does entire stack stop working?

No, the stack continues to work. One of the key benefits of the HPE Aruba Networking subscription model
is that a network is not impacted by a feature pack going invalid – this includes a feature pack expiring, or a
scenario where a valid, subscribed stack is changed to include an unsubscribed member.

What happens if the MAC/serial of a device added to a VSF stack is not included in the feature pack
file?

The feature pack file contains the MAC/serial of each subscribed member, so any MAC/serial in the stack but
not present in the feature pack file is considered an unsubscribed device.

How frequently are critical event messages logged when a switch operates without a valid feature pack
for a specific feature?

Critical event messages will be logged to indicate that the system is operating with an invalid feature pack.
These messages will be generated twice a day for each feature used without a valid feature pack.

Can I manage a subscription from the conductor in a VSF stack?

Yes. The VSF stack conductor is responsible for all the feature pack management for that stack, and the
feature pack is installed as a bundle for all the members.

Can I manage a subscription from primary device in a VSX cluster?

Feature packs on a VSX cluster are not managed only from the VSX primary node. In a VSX cluster, both
nodes, primary and secondary, must manage their own feature packs independently.

Troubleshooting Feature Pack Issues

Use the following workflows to identify and fix problems with your Aruba CX feature pack deployment.

How do I know there is a feature pack issue?

Warning Logs from Subscription Features

Features that require a CX feature pack will generate warning event logs if a valid feature pack is missing.

Public

Troubleshooting Feature Pack Issues 74

For example, the Application Based Policy feature will generate the following log message if the feature is
missing a valid feature pack, even though the feature is still operational. This log message can be triggered
by scenarios such as feature pack expiration, or a loss of connection to the HPE Aruba Networking support
portal.

Event|10536|LOG_WARN|CDTR|1|Policy policy1 is of type ABP and a valid

feature pack is required to use the policy. The policy is currently in use

without a valid feature pack.
If the Application Based Policy feature is blocked due to a missing or invalid feature pack, then the switch
will generate the following log message. This issue can occur if the feature has never had a valid feature
pack, or if the switch has been zeroized.

Event|10535|LOG_ERR|CDTR|1|Policy policy1 is of type ABP and a valid

feature pack is required to use the policy. All clients associated with

this policy will be unauthorized until a valid feature pack is installed.
If the switch displays warning logs for a subscription feature, refer to Reasons for Feature Pack Issues for
help with identifying and resolving the issue.

Feature-Pack Show Commands

The switch command-line interface includes feature-pack show commands to display the status of the
feature pack and subscription features on the switch. The show feature-pack and show feature-pack server
commands will display an error message if there is a feature-pack related issue.

Reasons for Feature Pack Issues

If the event logs or show commands are showing errors on the switch. These commands will display an error
message if there is a feature pack related issue.

Feature is blocked by missing feature pack

When a feature is blocked due to an invalid or missing feature pack, the show feature-pack command will
display the Subscription Status as inactive and Feature Status as blocked. To resolve this issue, install
a valid feature pack onto the switch. For more information, see Deploying a Cloud-managed Feature Pack
Solution on a Standalone Switch or Deploying a File-Based Feature Pack Solution on a Standalone Switch.

6300# show feature-pack

Feature Pack Summary

====================

Name             : --

Expiration Date  : --

Serial Number(s) : --

MAC Address      : --

Hostname         : --

Type             : --

Mode             : File Based

State            : No feature pack installed

Error Reason     : --

Subscription  Feature

Public

Troubleshooting Feature Pack Issues 75

Feature                                         Status        Status

-----------------------------------------------------------------------

Application Based Policy                        inactive      blocked

MACsec extensions for WAN                       inactive      blocked

Reflexive Policies for Port Access GBP Clients  inactive      blocked

Reflexive Policies for Port Access Clients      inactive      blocked

The Switch is Out of Sync with the HPE Aruba Networking Support Portal

If changes have been made on the switch or the HPE Aruba Networking support portal, and the
switch feature pack state is out-of-date, issue the feature-pack validate command to force the switch to
immediately synchronize with the support portal.

HPE Aruba Networking Support Portal account is locked after changing the password

About this task

A network admin using feature packs in cloud mode may experience a lockout of their HPE account after
changing their password due to the switches syncing with the old password. When changing the password
of the user account credentials configured on switches for cloud-managed subscriptions, use the following to
avoid unexpected account lockouts:

Procedure

1.  Configure all switches into file-mode using the command feature-pack mode file-based. This will
prevent the switches from syncing with the HPE Networking Support Portal during the password
change process.

NOTE

This will cause the switches to move into honor mode due to a mismatch
between feature-pack type and configured mode, but subscription features
will remain operational.

2.  Proceed with the password change on the HPE user account.

3.  Configure the new password on each switch using the secure prompt or ciphertext options.

Using secure prompt:

switch (config-feature-pack-server)# credentials user <USER> password

<enter>”.
Using ciphertext :

switch (config-feature-pack-server)#  credentials user <USER> password

ciphertext <CIPHERTEXT>”

4.  Configure each switch into cloud-managed mode using the command feature-pack mode cloud-

managed, then verify subscriptions are validated using show feature-pack server and show feature-
pack.

Public

Troubleshooting Feature Pack Issues 76

Missing Feature Pack Profile Fields

The feature pack profile on the switch requires a location, user account credentials, and subscription pool
information. If any of those fields are missing, the output of the show feature-pack server command will
indicate that there are missing profile fields. Configure the missing fields to resolve the error and connect to
the support portal.

6405# show feature-pack server

Profile

=======

Location URL       : --

Location VRF       : default

User account       : --

Subscription Pool  : --

Subscription Block : --

Connection

==========

Status                  : Invalid profile configuration

Reason                  : missing fields for profile configuration

Last validation time    : Wed Oct 18 22:06:09 UTC 2023

Success validation time : --

Connection Failure to the HPE Aruba Networking Feature Pack Support Portal Server

When the switch cannot connect to the support portal server, the show feature-pack server command
displays the following output. Verify that the switch has internet access and DNS can resolve the HPE Aruba
Networking support portal FQDN (https://cx-feature-pack.arubanetworks.com).

6405# show feature-pack server

Profile

=======

Location URL       : https://cx-feature-pack.arubanetworks.com

Location VRF       : mgmt

User account       : customer@example.com

Subscription Pool  : Default
Subscription Block : 6300_block_4

Connection

==========

Status                  : Connection failed

Reason                  : connection to the feature pack server was

attempted, but failed

Last validation time    : Wed Oct 18 22:16:34 UTC 2023

Success validation time : --
Connectivity issues can also be caused by internet access security rules, web-proxy issues, or DNS name
resolution failures. Check your security settings and ensure that DNS is configured on the switch.

Mode Mismatch

Public

Troubleshooting Feature Pack Issues 77

About this task

The feature pack mode configured on the switch profile (cloud-managed or file-based) must match the
feature pack type that is installed on the switch. If you configure the switch with the command feature-pack
mode cloud-managed, the switch must use a floating feature pack. If you configure the switch with the
command feature-pack mode file-based, the switch must use a device specific feature pack.

if the switch has a floating feature pack installed while in file-based mode, the switch will display the
following error in the output of the show feature-pack command.

6300# show feature-pack

Feature Pack Summary

====================

Name             : CX Advanced Feature Pack

Expiration Date  : Sat Oct 12 2024

Serial Number(s) : SG2Zxxxxx1 SG9Zxxxxx2 SG9Zxxxxx3

MAC Address      : 38:21:c7:00:00:00

Hostname         : 6300

Type             : Floating

Mode             : File Based

State            : Mode does not match installed feature pack type

Error Reason     : none

Subscription  Feature

Feature                                         Status        Status

-----------------------------------------------------------------------

Application Based Policy                        honor mode    allowed

MACsec extensions for WAN                       honor mode    allowed

Reflexive Policies for Port Access GBP Clients  honor mode    allowed

Reflexive Policies for Port Access Clients      honor mode    allowed
if the switch has a device-specific feature pack installed while in cloud-managed mode, the switch will display
the following error in the output of the show feature-pack command.

6300# show feature-pack server

Profile

=======
Location URL       : https://cx-feature-pack.arubanetworks.com

Location VRF       : mgmt

User account       : customer@example.com

Subscription Pool  : Default

Subscription Block : 6300_block_7

Connection

==========

Status                  : File based feature pack installed

Reason                  : file based feature packs are not validated

against the feature pack server

Public

Troubleshooting Feature Pack Issues 78

Last validation time    : Mon Oct 16 21:24:49 UTC 2023

Success validation time : --
To resolve these errors:

Procedure

1.  Change the mode configuration to match the current installed feature type.

2.  Erase the feature pack and reinstall a new feature pack of the correct type.

Invalid Block

When the block configured on the switch does not exist in the specified pool on the HPE Aruba Networking
support portal, the output of the Reasons for Feature Pack Issues command will display a Server invalid
block status.

6300# show feature-pack server

Profile

=======

Location URL       : https://cx-feature-pack.arubanetworks.com

Location VRF       : mgmt

User account       : plmtest@example.com

Subscription Pool  : Default

Subscription Block : 6300_block_7

Connection

==========

Status                  : Server invalid block

Reason                  : the feature pack block is not valid

Last validation time    : Mon Oct 16 21:33:59 UTC 2023

Success validation time : --
To correct this issue, update the block configured on the switch to match a valid block in the configured pool.

Not Enough Feature Packs

If the subscription pool or block does not have enough feature packs for the switch after the switch
synchronizes with the HPE Aruba Networking support portal, then the output of the show feature-pack
server command displays the Server not enough feature packs status. To resolve this issue, change the
configured block and/or pool on the switch to connect to a block that has feature packs available.

6300# show feature-pack server

Profile

=======

Location URL       : https://cx-feature-pack.arubanetworks.com

Location VRF       : mgmt
User account       : customer@example.com

Subscription Pool  : Default

Subscription Block : 6300_block_4

Connection

Public

Troubleshooting Feature Pack Issues 79

==========

Status                  : Server not enough feature packs

Reason                  : there are not enough feature packs for the device

and/or device stack

Last validation time    : Thu Oct 12 18:20:59 UTC 2023

Success validation time : Thu Oct 12 18:15:15 UTC 2023

Feature Pack Already Assigned

If a switch that is already assigned a feature pack in the HPE Aruba Networking support portal, requests a
new feature pack, the output of the show feature-pack server command on the switch will display the Server
feature pack already assigned to device error after the switch connects to the portal. This issue can occur
if a feature pack is erased from the switch but not revoked in the support portal. To resolve this issue and
install a feature pack on the switch, revoke the existing feature pack in the support portal, then trigger a
manual synchronization with the portal using the feature-pack validate CLI command.

6405# show feature-pack server

Profile

=======

Location URL       : https://cx-feature-pack.arubanetworks.com

Location VRF       : mgmt

User account       : customer@example.com

Subscription Pool  : Test1

Subscription Block : 6400_test_block_1

Connection

==========

Status                  : Server feature pack already assigned to device

Reason                  : the feature pack server has already assigned a

feature pack for this device

Last validation time    : Wed Oct 18 23:11:36 UTC 2023

Success validation time : --

Feature Pack Revoked

If a cloud feature pack for a switch is revoked in the HPE Aruba Networking support portal, then the switch
will display the following errors will operate with subscription features enabled in honor mode. To reinstall a
feature pack on the switch, issue the erase feature-pack command to erase the existing feature-pack, verify
that the feature-pack profile is configured as desired, and trigger a sync with the support portal using the
command feature-pack server-validate.

6300# show feature-pack

Feature Pack Summary

====================

Name             : CX Advanced Feature Pack
Expiration Date  : Wed Aug 28 2024

Serial Number(s) : SG2xxxxx1 SG9Zxxxx2

MAC Address      : 38:21:c7:5a:00:00

Hostname         : 6300

Public

Troubleshooting Feature Pack Issues 80

Type             : Floating

Mode             : Cloud Managed

State            : Cloud managed subscription revoked from server

Error Reason     : none

Subscription  Feature

Feature                                         Status        Status

-----------------------------------------------------------------------

Application Based Policy                        honor mode    allowed

MACsec extensions for WAN                       honor mode    allowed

Reflexive Policies for Port Access GBP Clients  honor mode    allowed

Reflexive Policies for Port Access Clients      honor mode    allowed

6300# show feature-pack server

Profile

=======

Location URL           : https://cx-feature-pack.arubanetworks.com

Location VRF           : mgmt

User account           : customer@example.com

Subscription Pool      : Default

Subscription Block     : 6300_test1

Connection

==========

Status                  : Server feature pack revoked

Reason                  : the device feature pack was revoked from the

feature pack server

Last validation time    : Fri Oct  6 16:48:24 UTC 2023

Success validation time : Fri Oct  6 16:36:04 UTC 2023

Feature Pack Removed

If a feature-pack is erased from the switch using the erase feature-pack command, then the switch will
display the following message and will operate with subscription features enabled in honor mode. The
feature-pack can be reinstalled by following the same steps as the initial installation. See Deploying a
Cloud-managed Feature Pack Solution on a Standalone Switch or Deploying a File-Based Feature Pack
Solution on a Standalone Switch.

6300# show feature-pack

Feature Pack Summary

====================

Name             : --

Expiration Date  : --

Serial Number(s) :
MAC Address      : --
Hostname         : --

Type             : --

Mode             : File Based

State            : Feature pack removed

Public

Troubleshooting Feature Pack Issues 81

Error Reason     : none

Subscription  Feature

Feature                                         Status        Status

-----------------------------------------------------------------------

Application Based Policy                        honor mode    allowed

MACsec extensions for WAN                       honor mode    allowed

Reflexive Policies for Port Access GBP Clients  honor mode    allowed

Reflexive Policies for Port Access Clients      honor mode    allowed

Serial/MAC mismatch

When using device-specific feature packs, if the serial number or MAC address in the feature pack does not
match the switch, then the output of the show feature-pack command displays the following error:

6300# show feature-pack

Feature Pack Summary

====================

Name             : CX Advanced Feature Pack

Expiration Date  : Fri Jul 19 2024

Serial Number(s) : SG2Zxxxx9 SG9ZxxxxG SG9Zxxxx5X

MAC Address      : 38:21:c7:00:00:00

Hostname         : 6300

Type             : Device specific

Mode             : File Based

State            : Feature pack install error

Error Reason     : Serial number mismatch

Subscription  Feature

Feature                                         Status        Status

-----------------------------------------------------------------------

Application Based Policy                        inactive      blocked

MACsec extensions for WAN                       inactive      blocked

Reflexive Policies for Port Access GBP Clients  inactive      blocked

Reflexive Policies for Port Access Clients      inactive      blocked
To resolve, install a feature-pack with the correct serial number and MAC address. The serial number of a
feature pack can be edited in the HPE Aruba Networking support portal in the Monitoring page. The MAC
address cannot be edited. If a MAC address must be changed for a feature pack, revoke the feature pack and
re-downloaded it with the correct MAC address.

Aruba Central Disconnected

If a switch was previously managed by Aruba Central but is no longer managed by Central, subscription
features will be operational in honor mode and the output of the show feature-pack command will display
the following message:

(switch)# show feature-pack

Feature Pack Summary

====================

Public

Troubleshooting Feature Pack Issues 82

Name             : --

Expiration Date  : --

Serial Number(s) : --

MAC Address      : --

Hostname         : --

Type             : --

Mode             : File Based

State            : No feature pack installed

Error Reason     : --

                                                Subscription  Feature

Feature                                         Status        Status

-----------------------------------------------------------------------

Application Based Policy                        inactive      blocked

MACsec extensions for WAN                       inactive      blocked

Reflexive Policies for Port Access GBP Clients  inactive      blocked

Reflexive Policies for Port Access Clients      inactive      blocked
The switch may be in this state for the below reasons:

•  The switch lost connectivity to the Aruba Central server. Check that the switch’s uplink has connectivity

to Central.

•  The Aruba Central subscription or Aruba Central application assignment for the switch was removed in
GLCP. Check that the switch is assigned to Central and has a valid Central license attached in GLCP.

Some Features are Allowed but Others are Blocked

The following example output of show feature-pack shows that some features are allowed in honor mode
while some are blocked in strict mode. This will happen in a deployment where the feature was not used until
after the switch upgraded to AOS-CX 10.13 or later releases. If a subscription feature was in use before an
upgrade to 10.13, then the feature will default to being allowed instead of blocked.

6300# show feature-pack

Feature Pack Summary

====================

Name             : --

Expiration Date  : --

Serial Number(s) : --

MAC Address      : --

Hostname         : --

Type             : --

Mode             : File Based

State            : No feature pack installed

Error Reason     : --

Subscription  Feature

Feature                                         Status        Status

-----------------------------------------------------------------------

Public

Troubleshooting Feature Pack Issues 83

Application Based Policy                        inactive      blocked

MACsec extensions for WAN                       inactive      blocked

Reflexive Policies for Port Access GBP Clients  inactive      blocked

Reflexive Policies for Port Access Clients      inactive      blocked

Features are Blocked after Zeroization

After zeroizing a switch, any installed feature pack is erased and all subscription features become blocked.
The output of show feature-pack will look like the following example:

6300# show feature-pack

switch(config)# sh feature-pack

Feature Pack Summary

====================

Name             : --

Expiration Date  : --

Serial Number(s) : --

MAC Address      : --

Hostname         : --

Type             : --

Mode             : File Based

State            : No feature pack installed

Error Reason     : none

                                                Subscription  Feature

Feature                                         Status        Status

-----------------------------------------------------------------------

Application Based Policy                        inactive      blocked

Audio Video Bridging                            inactive      --

MACsec extensions for WAN                       inactive      blocked

Reflexive Policies for Port Access GBP Clients  inactive      blocked

Reflexive Policies for Port Access Clients      inactive      blocked
To re-enable features, reinstall the feature pack. If a device-specific feature pack was being used, then
the feature pack can be re-downloaded from the Monitoring page in the HPE Aruba Networking support
portal. If a floating feature pack was being used, revoke the existing feature pack in the support portal ,
then re-configure the feature-pack server profile on the switch. Afterwards, the switch will reach out to the
support portal and install a new feature pack.

Feature Pack events

The following are the events related to CX Advanced and CX Premium feature packs.

Public

Feature Pack events 84

Event ID: 14401

Message

Category

Severity

Description

Event ID: 14402

Message

Category

Severity

Description

Event ID: 14403

Message

Category

Severity

Description

Event ID: 14404

Message

Category

Severity

{feature_pack_name} installed

Feature Pack

Info

Event raised when a feature pack is installed

{feature_pack_name} erased.

Feature Pack

Info

Event raised when a feature pack is erased.

{feature_pack_name} expired on {expiry_date}.

Feature Pack

Warning

Event raised when a feature pack expires

Feature pack {parameter_type} {subscription_param
eter} does not match device {parameter_type} {devic
e_parameter}

Feature Pack

Warning

Public

Feature Pack events 85

Description

Event ID: 14405

Message

Category

Severity

Description

Event ID: 14406

Message

Category

Severity

Description

Event ID: 14407

Message

Category

Severity

Description

Event raised when a feature pack serial number or M
AC address does not match that of the device

Event raised when a feature pack file downloads suc
cessfully

Feature Pack

Info

Feature pack file download success

Feature pack file download failure

Feature Pack

Warning

Event raised when a feature pack file download fails

Feature pack subscription through HPE Aruba Netw
orking Central is {connection_state}

Feature Pack

Info

Event raised when a feature pack subscription thro
ugh HPE Aruba Networking Central becomes conne
cted or disconnected

Public

Feature Pack events 86

Event ID: 14408

Message

Category

Severity

Description

Event ID: 14409

Message

Category

Severity

Description

Event ID: 14410

Message

Category

Severity

Description

VSF member serial number {device_serial} not subsc
ribed as part of installed feature pack

Feature Pack

Warning

Event raised when a VSF member is not subscribed a
s part of the installed feature pack

Feature {feature_name} is operating in honor mode
without a valid feature pack.

Feature Pack

Warning

Periodic event raised to indicate that a feature is ope
rating in honor mode

Connection to feature pack server lost and subscript
ion for {feature_pack_name} cannot be validated. Su
bscribed features will continue to operate in honor m
ode.

Feature Pack

Warning

Event raised when a connection to the feature pack s
erver has been lost and the feature pack subscriptio
n cannot be validated

Public

Feature Pack events 87

Event ID: 14411

Message

Category

Severity

Description

Event ID: 14412

Message

Category

Severity

Description

Event ID: 14413

Message

Category

Severity

Description

No feature pack is installed. This device requires an
Advanced or Premium feature pack to use advanced
or premium features.

Feature Pack

Warning

Event raised to indicate that the device requires a fe
ature pack

Advanced feature pack installed. This system requi
res a Premium feature pack to use all features.

Feature Pack

Warning

Event raised to indicate that a higher feature pack ti
er is available and necessary to enable higher tier fe
atures

Software feature pack {feature_pack_name} revoked
by the server.

Feature Pack

Info

Event raised when a feature pack is revoked by the
feature pack server.

Public

Feature Pack events 88

Event ID: 14414

Message

Category

Severity

Description

Event ID: 14415

Message

Category

Severity

Description

Event ID: 14416

Message

Category

Severity

Description

Feature pack mode {feature_pack_mode} does not m
atch installed feature pack type {feature_pack_type}.

Feature Pack

Warning

Event raised when the feature pack mode configured
does not match the feature pack type installed on th
e device.

Cloud‐managed mode is enabled. A feature pack s
erver will be used for feature pack management.

Feature Pack

Info

Event raised when the feature pack management m
ode is set to cloud‐managed

Cloud‐managed mode is disabled. A feature pack s
erver will no longer be used for feature pack manage
ment.

Feature Pack

Info

Event raised when the management mode is differen
t than cloud‐managed

Public

Feature Pack events 89

Event ID: 14417

Message

Category

Severity

Description

Event ID: 14418

Message

Category

Severity

Description

Event ID: 14419

Message

Category

Severity

Description

Subtopics

The feature pack has been successfully validated by
the server

Feature Pack

Info

Event raised when the feature pack was successfully
validated by the server

Feature pack server failed to validate the installed fe
ature pack

Feature Pack

Error

Event raised when there is an error validating a featu
re pack by the server

One or more advanced features have been blocked d
ue to an invalid or missing feature‐pack. Check sho
w feature‐pack for details.

Feature Pack

Warning

Event raised when an invalid or missing feature pack
blocks one or more features from operating

feature pack events
Queue Monitoring events

Public

Feature Pack events 90

feature pack events

Event ID: 14401

Message

Category

Severity

Description

Event ID: 14402

Message

Category

Severity

Description

Event ID: 14403

Message

Category

Severity

Description

Event ID: 14404

Message

{feature_pack_name} installed

Feature Pack

Info

Event raised when a feature pack is installed

{feature_pack_name} erased.

Feature Pack

Info

Event raised when a feature pack is erased.

{feature_pack_name} expired on {expiry_date}.

Feature Pack

Warning

Event raised when a feature pack expires

Feature pack {parameter_type} {subscription_param
eter} does not match device {parameter_type} {devic
e_parameter}

Public

feature pack events 91

Category

Severity

Description

Event ID: 14405

Message

Category

Severity

Description

Event ID: 14406

Message

Category

Severity

Description

Event ID: 14407

Message

Category

Severity

Description

Feature Pack

Warning

Event raised when a feature pack serial number or M
AC address does not match that of the device

Event raised when a feature pack file downloads suc
cessfully

Feature Pack

Info

Feature pack file download success

Feature pack file download failure

Feature Pack

Warning

Event raised when a feature pack file download fails

Feature pack subscription through HPE Aruba Netw
orking Central is {connection_state}

Feature Pack

Info

Event raised when a feature pack subscription thro
ugh HPE Aruba Networking Central becomes conne
cted or disconnected

Public

feature pack events 92

Event ID: 14408

Message

Category

Severity

Description

Event ID: 14409

Message

Category

Severity

Description

Event ID: 14410

Message

Category

Severity

Description

VSF member serial number {device_serial} not subsc
ribed as part of installed feature pack

Feature Pack

Warning

Event raised when a VSF member is not subscribed a
s part of the installed feature pack

Feature {feature_name} is operating in honor mode
without a valid feature pack.

Feature Pack

Warning

Periodic event raised to indicate that a feature is ope
rating in honor mode

Connection to feature pack server lost and subscript
ion for {feature_pack_name} cannot be validated. Su
bscribed features will continue to operate in honor m
ode.

Feature Pack

Warning

Event raised when a connection to the feature pack s
erver has been lost and the feature pack subscriptio
n cannot be validated

Public

feature pack events 93

Event ID: 14411

Message

Category

Severity

Description

Event ID: 14412

Message

Category

Severity

Description

Event ID: 14413

Message

Category

Severity

Description

No feature pack is installed. This device requires an
Advanced or Premium feature pack to use advanced
or premium features.

Feature Pack

Warning

Event raised to indicate that the device requires a fe
ature pack

Advanced feature pack installed. This system requi
res a Premium feature pack to use all features.

Feature Pack

Warning

Event raised to indicate that a higher feature pack ti
er is available and necessary to enable higher tier fe
atures

Software feature pack {feature_pack_name} revoked
by the server.

Feature Pack

Info

Event raised when a feature pack is revoked by the
feature pack server.

Public

feature pack events 94

Event ID: 14414

Message

Category

Severity

Description

Event ID: 14415

Message

Category

Severity

Description

Event ID: 14416

Message

Category

Severity

Description

Feature pack mode {feature_pack_mode} does not m
atch installed feature pack type {feature_pack_type}.

Feature Pack

Warning

Event raised when the feature pack mode configured
does not match the feature pack type installed on th
e device.

Cloud‐managed mode is enabled. A feature pack s
erver will be used for feature pack management.

Feature Pack

Info

Event raised when the feature pack management m
ode is set to cloud‐managed

Cloud‐managed mode is disabled. A feature pack s
erver will no longer be used for feature pack manage
ment.

Feature Pack

Info

Event raised when the management mode is differen
t than cloud‐managed

Public

feature pack events 95

Event ID: 14417

Message

Category

Severity

Description

Event ID: 14418

Message

Category

Severity

Description

Event ID: 14419

Message

Category

Severity

Description

The feature pack has been successfully validated by
the server

Feature Pack

Info

Event raised when the feature pack was successfully
validated by the server

Feature pack server failed to validate the installed fe
ature pack

Feature Pack

Error

Event raised when there is an error validating a featu
re pack by the server

One or more advanced features have been blocked d
ue to an invalid or missing feature‐pack. Check sho
w feature‐pack for details.

Feature Pack

Warning

Event raised when an invalid or missing feature pack
blocks one or more features from operating

Queue Monitoring events

Public

Queue Monitoring events 96

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

Description

HONOR_MODE: Queue Monitoring is operating with
out a valid feature pack.

QTP

Info

Log event to indicate that the Queue Monitor feature
is operating without a valid feature pack

STRICT_MODE: Queue Monitoring is blocked due to i
nvalid or missing feature pack.

QTP

Info

Log event to indicate that the Queue Monitoring feat
ure is blocked due to invalid or missing feature pack

Log event to indicate that the Queue Monitoring feat
ure is operational for valid feature pack

QTP

Info

ACTIVE_MODE: Queue Monitoring is operating with
valid feature pack.

Support and Other Resources

Access HPE Aruba Networking support and updates, and view warranty and regulatory information

Public

Support and Other Resources 97

Subtopics

Accessing HPE Aruba Networking Support

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

AOS‐CX Switch Software Documentation Portal

https://www.hpe.com/us/en/networking/hpe‐aru
ba‐networking‐support‐services.html

https://arubanetworking.hpe.com/techdocs/Aruba
DocPortal/content/new-portal/aoscx.html

HPE Aruba Networking Support Portal

https://networkingsupport.hpe.com/home

North America telephone

1‐800‐943‐4526 (US & Canada Toll‐Free Nu
mber)

+1‐650‐750‐0350 (Backup—Toll Number)

International telephone

https://www.hpe.com/psnow/doc/a50011948enw

Be sure to collect the following information before contacting Support:

•  Technical support registration number (if applicable)

•  Product name, model or version, and serial number

•  Operating system name and version

•  Firmware version

•  Error messages

•  Product-specific reports and logs

•  Add-on products or components

•  Third-party products or components

Other useful sites

Other websites that can be used to find information:

Public

Accessing HPE Aruba Networking Support 98

HPE Aruba Networking Developer Hub

https://developer.arubanetworks.com/hpe‐aruba
‐networking‐aoscx/docs/about

Airheads social forums and Knowledge Base

https://community.arubanetworks.com/

AOS‐CX Software Technical Update channel on You
Tube.

Videos on new features introduced in this release
: https://www.youtube.com/playlist?list=PLsYGHu
NuBZcbWPEjjHuVMqP‐Q_UL3CskS

HPE Aruba Networking Hardware Documentation an
d Translations Portal

HPE Aruba Networking software

https://networkingsupport.hpe.com/downloads h
ttps://networkingsupport.hpe.com/downloads

Software licensing and Feature Packs

https://licensemanagement.hpe.com/

End‐of‐Life information

https://networkingsupport.hpe.com/end‐of‐life

Public

Accessing HPE Aruba Networking Support 99