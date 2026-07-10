AOS-CX 10.14.1000 Hardening
Guide

All Switch Series

Published: April 2025

Version: 2

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

AOS-CX 10.14.1000 Hardening Guide | (All Switch Series)

3

Contents
| About this                          | document |     |     | 6   |
| ----------------------------------- | -------- | --- | --- | --- |
| Latestversionavailableonline        |          |     |     | 6   |
| Abouttheexamples                    |          |     |     | 6   |
| Identifyingswitchportsandinterfaces |          |     |     | 6   |
| Identifyingmodularswitchcomponents  |          |     |     | 7   |
| Overview                            |          |     |     | 9   |
| HardeningObjectives                 |          |     |     | 9   |
| OperationalAssumptions              |          |     |     | 10  |
| SyntaxandConventions                |          |     |     | 10  |
Software,Documentation,SecurityAdvisoriesandBugBountyProgram 10
| Hardening                             | the CX                                         | Management | plane | 11  |
| ------------------------------------- | ---------------------------------------------- | ---------- | ----- | --- |
| FactoryDefaults                       |                                                |            |       | 11  |
| PhysicalSecurity                      |                                                |            |       | 13  |
|                                       | FrontPanelSecurity                             |            |       | 13  |
|                                       | USBAuxiliaryPort                               |            |       | 14  |
| FirmwareValidation                    |                                                |            |       | 15  |
| Enhancedsecuritymode                  |                                                |            |       | 15  |
| ServiceOSpasswordauthentication       |                                                |            |       | 17  |
| SecuringSwitchManagementAccessControl |                                                |            |       | 17  |
|                                       | UserManagementandPasswordControl               |            |       | 17  |
|                                       | SecurityUserGroup                              |            |       | 18  |
|                                       | HardeningPasswordRules                         |            |       | 18  |
|                                       | PasswordComplexity                             |            |       | 19  |
|                                       | Authentication,AuthorizationandAccounting(AAA) |            |       | 21  |
|                                       | Authentication                                 |            |       | 22  |
|                                       | Authorization                                  |            |       | 26  |
|                                       | Accounting                                     |            |       | 27  |
|                                       | RadSecoverRADIUS                               |            |       | 28  |
|                                       | HardeningSSH                                   |            |       | 29  |
|                                       | PublicKeyAuthentication                        |            |       | 29  |
|                                       | AllowList                                      |            |       | 29  |
|                                       | RecommendedCiphers,MACs,andAlgorithms          |            |       | 30  |
|                                       | ServerPortCustomization                        |            |       | 30  |
|                                       | TwoFactorAuthenticationandAuthorization        |            |       | 31  |
|                                       | Summary                                        |            |       | 32  |
| SessionManagement                     |                                                |            |       | 32  |
| LimitingShellAccess                   |                                                |            |       | 33  |
| SecuringSNMPAccess                    |                                                |            |       | 33  |
| ControlPlaneACLs                      |                                                |            |       | 35  |
| TimeSynchronization                   |                                                |            |       | 35  |
| SecureCopy                            |                                                |            |       | 36  |
| HardeningPKI                          |                                                |            |       | 36  |
|                                       | Mandatorymatchingofpeerdevicehostname          |            |       | 38  |
|                                       | EST                                            |            |       | 39  |
|                                       | TLSEnforcements                                |            |       | 39  |
|                                       | SecureLogging                                  |            |       | 39  |
4
AOS-CX10.14.1000HardeningGuide| (AllSwitchSeries)

| Hardening                          | the                                            | Control         | Plane | 40  |
| ---------------------------------- | ---------------------------------------------- | --------------- | ----- | --- |
| ControlPlanePolicing               |                                                |                 |       | 40  |
| SecuringSpanningTree               |                                                |                 |       | 41  |
|                                    | BPDUProtection                                 |                 |       | 42  |
|                                    | RootProtection                                 |                 |       | 42  |
| DHCP Security                      |                                                |                 |       | 42  |
|                                    | DHCPSnooping                                   |                 |       | 43  |
|                                    | DHCPv6Guard                                    |                 |       | 44  |
| DynamicARPInspection               |                                                |                 |       | 45  |
| ND SnoopingAttackPrevention        |                                                |                 |       | 46  |
|                                    | RAGuard                                        |                 |       | 47  |
|                                    | IPv6DestinationGuard                           |                 |       | 48  |
|                                    | IPSourceLockdown                               |                 |       | 48  |
| SecuringRoutingProtocols           |                                                |                 |       | 49  |
|                                    | OSPFPassiveInterfaces                          |                 |       | 49  |
|                                    | OSPFNeighborAuthentication                     |                 |       | 50  |
|                                    | OSPFv3AreaAuthenticationandEncryptionwithIPsec |                 |       | 50  |
|                                    | BGP                                            |                 |       | 51  |
|                                    | ControlPlaneACLforBGPPeeringSessions           |                 |       | 52  |
|                                    | AuthenticateBGPPeersUsingMD5                   |                 |       | 52  |
|                                    | BGPTTLSecurity                                 |                 |       | 52  |
| MulticastSecurity                  |                                                |                 |       | 53  |
|                                    | SSDP                                           |                 |       | 53  |
|                                    | HardeningIGMPandMLD Snooping                   |                 |       | 54  |
|                                    | HardeningPIMandPIMv6                           |                 |       | 55  |
|                                    | PIMAccept-Register                             |                 |       | 55  |
|                                    | PIMAccept-RP                                   |                 |       | 55  |
|                                    | PIMSSM                                         |                 |       | 55  |
|                                    | SecuringMSDP                                   |                 |       | 56  |
| NAEScripts                         |                                                |                 |       | 57  |
| Trusted                            | Supply                                         | Chain           |       | 58  |
| Support                            | and                                            | Other Resources |       | 59  |
| AccessingHPEArubaNetworkingSupport |                                                |                 |       | 59  |
| AccessingUpdates                   |                                                |                 |       | 60  |
| WarrantyInformation                |                                                |                 |       | 60  |
| RegulatoryInformation              |                                                |                 |       | 60  |
| DocumentationFeedback              |                                                |                 |       | 60  |
|5

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

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

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

AOS-CX 10.14.1000 Hardening Guide | (All Switch Series)

6

On the 4100i Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the 6000 and 6100 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
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

About this document | 7

n Power supplies are on the front of the switch behind the bezel above the management modules.

Power supplies are labeled in software in the format: member/power supply:

o member: 1.

o power supply: 1 to 4.

n Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

o member: 1.

o tray: 1 to 4.

o fan: 1 to 4.

n Fabric modules are not labeled on the switch but are labeled in software in the format:

member/module:

o member: 1.

o member: 1 or 2.

n The display module on the rear of the switch is not labeled with a member or slot number.

AOS-CX 10.14.1000 Hardening Guide | (All Switch Series)

8

Chapter 2

Overview

Overview

Security is a growing concern in today’s all-digital enterprise infrastructure. Upper-level managers and IT
administrators alike are held to higher accountability for the integrity and availability of their critical data
and infrastructure. While clients and servers are often the focus of security discussions, the security of
network devices such as switches, routers, and wireless access points should not be ignored. Critical
enterprise data traverses these devices, and properly securing them is paramount to a stable and
secure infrastructure.

The HPE Aruba Networking CX switching platform, powered by the AOS-CX network operating system,
simplifies network operations by delivering automation, distributed analytics, security, and high
availability to campus and data center networks. The microservices architecture around which AOS-CX is
built delivers network-wide analytics and full programmability to enable complete network assurance.

The purpose of this document is to provide security guidelines and best practices for management
features and protocols provided by the AOS-CX software, and to present sample configurations to
illustrate these best practices in action. This document is not intended to be a comprehensive reference
guide to the features and commands listed; for additional information on configuration syntax and
advanced features referred to in this document, please obtain the latest software manual set from the
HPE Aruba Networking Support Portal.

Some of the features in this document are not be available on all switch platforms. Refer to
https://feature-navigator.arubanetworks.com for a list of features supported on each platform.

Hardening Objectives

IETF BCP 61 points to a few definitions that help us define our goals, which we can summarize into three
helpful points:

n Authentication: A security service that verifies an identity. This identity could be a user, a device, or a

process.

n Data Confidentiality: A security service that protects data against unauthorized disclosure to

unauthorized individuals or processes.

n Data Integrity: A security service that protects against unauthorized changes to data. Changes include

intentional change and accidental change.

The applications and procedures we use in this document leverage these summarized definitions above
and help to shape the following general guidelines:

n If there are methods, we can use to ensure the identities of the users and devices with which we

interact, we should prefer these over insecure alternatives.

n We should limit the exposure to the equipment from sources we cannot trust, whenever possible. We

should also make attempts to utilize encryption methods so that our data is not easily read by
anyone besides the trusted receiver of the data.

n Assume that eventually, an event will occur that causes a need for reliable information we know we

can trust. We need to make sure this data is safe, available for us to access, and unavailable to
anyone else.

AOS-CX 10.14.1000 Hardening Guide | (All Switch Series)

9

n This document helps you improve the overall network security by hardening the security of the

management and control plane.

Operational Assumptions

n One or more authorized administrators are assigned who are competent to manage the device and
the security of the information it contains, trained for the secure operation of the device, and who
can be trusted not to deliberately abuse their privileges to undermine security.

n Authorized users are trusted to correctly install, configure, and operate the device according to the

instructions provided by the device documentation.

n There will be no untrusted users and no untrusted software on component servers.

n The switch must be installed in a physically secure area where only authorized administrators have

access to the physical device.

n Users will protect their authentication data.

Syntax and Conventions

This document provides examples for each configurable feature discussed. These examples follow a
common format: commands and fixed options appear as fixed-width regular text, while configurable
parameters appear in italics, as in the following:

switch(config)# ssh server vrf default

For more details on command syntax, refer to the documentation referenced for each feature, or use
the built-in command syntax help on the switch by typing a partial command, then typing ? (a question
mark) to see possible options and parameters for that command.

Software, Documentation, Security Advisories and Bug
Bounty Program

HPE Aruba Networking CX switch software, release notes, and user documentation can be found at the
HPE Networking Support Portal.

Security advisories are published on the Aruba Security Advisory archive, and notification services are
provided by a Security Alerts mailing list, with subscriptions offered via the self-service portal . For more
information , refer to the Security Incident Response Policy.

HPE Aruba Networking also runs a Bug Bounty program for reporting security exploits and
vulnerabilities. HPE Aruba Networking handles and discloses vulnerabilities in accordance with ISO/IEC
30111. Refer to https://bugcrowd.com/aruba-product-public for more information on the Bug Bounty
program

Overview | 10

Chapter 3
|           |     |               |     |     | Hardening |     | the CX | Management | plane |
| --------- | --- | ------------- | --- | --- | --------- | --- | ------ | ---------- | ----- |
| Hardening | the | CX Management |     |     | plane     |     |        |            |       |
Thefollowingsectiondescribesstrategiestosecuretheswitchmanagementplane.
| Factory | Defaults |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Oncethedeviceboots,itisessentialforanadministratortoimmediatelyconnecttoitandconfigurea
passwordfortheadminaccount.CaliforniasignedintolawbillSB-327in2018,requiringmanufacturers
ofnetworkingequipmenttoforceuserstocreateapasswordwhentheyfirstconnecttoadevice.
Inafactorydefaultstate,AOS-CXdevicesareconfiguredwiththedefaultuseradminwithnopassword.
TheuserispromptedtocreateapasswordbeforeaccessisgiventotheCLI,WebUI,andRESTAPI:
| Please  | configure     | the | 'admin' |     | user account |     | password. |     |     |
| ------- | ------------- | --- | ------- | --- | ------------ | --- | --------- | --- | --- |
| Enter   | new password: |     | *****   |     |              |     |           |     |     |
| Confirm | new password: |     | ****    |     |              |     |           |     |     |
Thebuilt-inmanagementinterfaceprovidesawaytoaccessandmanagetheswitchthatissegregated
fromproductiontraffic.Internalnetworksseparatedfromproductiontrafficaretypicallyreferredtoas
Out-Of-Band-Managementnetworks(OOBM).Bylimitingtheclientsallowedtomanagedevicestoonly
thosewhoresideontheOOBMnetwork,wesharplylimitthelargesetofdevicesthatcanattemptto
controlthedevice.
InAOS-CX,themanagementinterfaceislogicallyseparatedfromtherestoftheswitchbymeansofa
uniquevirtualroutingandforwardingtable(VRF),namedthemgmtVRF.PleasenotethatthemgmtVRF
isuniqueinthatitispermanentlyassignedtothephysicalmanagementportandcannotbeassociated
withanyotherswitchinterface;themanagementportitselfcannotbeassociatedwithanyotherVRF.
ThemanagementinterfaceisenabledbydefaulttolearnanIPaddressviaDHCP.Toconfigurethe
managementinterfacewithastaticIPaddress,gateway,andDNS:
| switch(config)#         |     | interface |     | mgmt            |             |          |           |     |     |
| ----------------------- | --- | --------- | --- | --------------- | ----------- | -------- | --------- | --- | --- |
| switch(config-if-mgmt)# |     |           |     | ip static       | 10.1.1.5/24 |          |           |     |     |
| switch(config-if-mgmt)# |     |           |     | default-gateway |             | 10.1.1.1 |           |     |     |
| switch(config-if-mgmt)# |     |           |     | nameserver      | 10.0.1.10   |          | 10.0.1.11 |     |     |
Toshowthestatusofthemanagementinterface:
| switch#     | show                | interface         |     | mgmt          |                                |     |     |     |     |
| ----------- | ------------------- | ----------------- | --- | ------------- | ------------------------------ | --- | --- | --- | --- |
| Secondary   | Nameserver          |                   | :   | 10.0.1.11     |                                |     |     |     |     |
| Address     | Mode                | : static          |     |               |                                |     |     |     |     |
| Admin       | State :             | up                |     |               |                                |     |     |     |     |
| Mac Address | :                   | d0:67:26:11:11:11 |     |               |                                |     |     |     |     |
| IPv4        | address/subnet-mask |                   |     | : 10.1.1.5/24 |                                |     |     |     |     |
| Default     | gateway             | IPv4              | :   | 10.1.1.1      |                                |     |     |     |     |
| IPv6        | address/prefix      |                   | :   |               |                                |     |     |     |     |
| IPv6        | link local          | address/prefix    |     |               | : fe80::d267:2611:1111:1111/64 |     |     |     |     |
| Default     | gateway             | IPv6              | :   |               |                                |     |     |     |     |
11
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries)

Primary Nameserver : 10.0.1.10

The other VRFs available on an AOS-CX device upon first boot is the default VRF. The default VRF is
automatically associated with all non-management interfaces, including Layer 3 routed ports, non-
routed ports, and switched VLAN interfaces (SVIs) created on the switch, unless the interface is explicitly
attached to another VRF.

The following management services are enabled by default on an AOS-CX switch:

n SSH on TCP port 22

n WebUI and read/write REST API on TCP port 443. ( Any Connections to TCP port 80 will be

automatically redirected to TCP port 443)

The 10000, 8xxx and 9300 Switch series ship with these services enabled only on the mgmt VRF, while
6400, 6300 and 6200 switches ship with these services enabled on both the default and mgmt VRFs.

For optimal security, manage switches from a dedicated management network when possible, and
disable management services on all other VRFs.

To disable management services on all other VRFs :

switch(config)# no ssh server vrf <vrf-name>
switch(config)# no https-server vrf <vrf-name>

To view the configuration change :

switch # show ssh server vrf vrf1
SSH server is not enabled on VRF vrf1.

As the 6100, 6000 and 4100i Switch series does not have a dedicated management port or the
associated VRF, management services are enabled only on the default VRF. Therefore, disabling
management services is not a feasible solution for these platforms. For these switches, use other
alternatives, such as Control Plane ACLs , an SSH Allow list and Per-User management interface
enablement features to protect the management services.

Restoring the Switch to Factory Defaults

The recommended method to return an AOS-CX switch to factory default settings is to zeroize it. The
following occurs when the zeroization process is initiated:

n The switch reboots to ServiceOS

n Primary and secondary software image files are backed up to memory from flash storage

n The entire flash storage device is overwritten with zeroes to securely erase all stored data

n The flash storage device is reformatted with a factory default filesystem

n Backed up software image files are written to flash in their original locations

n The switch reboots to the primary software image with a default configuration

There are four methods that may be used to zeroize a switch. First, an admin user may use the erase all
zeroize command from the AOS-CX CLI:

switch# erase all zeroize
This will securely erase all customer data and reset the switch to factory

Hardening the CX Management plane | 12

defaults. This will initiate a reboot and render the switch unavailable until the
zeroization is complete.This should take several minutes to one hour to complete.
| Continue | (y/n)? |     |     |     |
| -------- | ------ | --- | --- | --- |
Second,anadminusermayusetheerasezeroizecommandfromtheServiceOSCLI:
| SVOS> erase | zeroize |     |     |     |
| ----------- | ------- | --- | --- | --- |
############################WARNIN
G##########################################################
This will securely erase all customer data and reset the switch to factory
defaults. This will initiate a reboot and render the switch unavailable until the
zeroization is complete.This should take several minutes to one hour to complete.
############################WARNI
G##########################################################
| Continue | (y/n)? |     |     |     |
| -------- | ------ | --- | --- | --- |
Third,auserwithphysicalaccesstotheswitchfrontpanelandaFAT32-formattedUSBstoragedevice
mayzeroizetheswitchfromtheServiceOSloginpromptbyenteringtheusernamezeroizeand
followingtheprovidedinstructions:
| ServiceOS | login: zeroize |     |     |     |
| --------- | -------------- | --- | --- | --- |
This will securely erase all customer data, including passwords, and reset the
| switch      | to factory defaults. |                   |            |              |
| ----------- | -------------------- | ----------------- | ---------- | ------------ |
| This action | requires             | proof of physical | access via | a USB drive. |
| * Create    | a FAT32 formatted    | USB               | drive      |              |
* Create a file in the root directory of the USB drive named zeroize.txt
* Type the following serial number into the zeroize.txt file: xxxxxxxxxx
| * Insert  | the USB drive | into the | target module |     |
| --------- | ------------- | -------- | ------------- | --- |
| * Confirm | the following | prompt   | to continue   |     |
| Continue  | (y/n)?        |          |               |     |
Finally,changingtheswitchsecuritymoderesultsintheswitchbeingzeroized;seetheEnhanced
securitymodesectionformoreinformation.
| Physical | Security |     |     |     |
| -------- | -------- | --- | --- | --- |
Thefollowingsectionsdescribephysicalsecurityhardeningworkflows.
| Front Panel | Security |     |     |     |
| ----------- | -------- | --- | --- | --- |
AOS-CXswitchesincludearesetbuttononthefrontpaneltoallowuserstoperformthefollowingreset
operations:
Reset
|     | Procedure |     |     | Outcome |
| --- | --------- | --- | --- | ------- |
Type
SoftReset Presstheresetbuttonandreleaseitbefore5 Theswitchoperatingsystemiscleared
|     | seconds. |     |     | gracefully.Theswitchthenrebootsand |
| --- | -------- | --- | --- | ---------------------------------- |
runsself-tests.
HardReset Presstheresetbuttonandreleaseitbetween5to20 Theswitchreboots,likeapowercycle.A
|     | seconds. |     |     | hardresetisused,forexample,whenthe |
| --- | -------- | --- | --- | ---------------------------------- |
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 13

Reset
|     | Procedure |     |     | Outcome |
| --- | --------- | --- | --- | ------- |
Type
switchCPUisinanunknownstateornot
responding.
Factory Presstheresetbuttonandreleaseitbetween20to Theswitchwillundergothefactoryreset
| Reset | 25seconds. |     |     | process. |
| ----- | ---------- | --- | --- | -------- |
FactoryResetfunctionalityisavailablefrom10.13.1000releaseinHPEANWCX6000and6100seriesofswitches.
Thisfactoryresetcapabilitycreatesasecurityanddenial-of-serviceriskiftheswitchisinalocation
whereitisimpossibletopreventphysicalaccesstothefrontpanel.Itisdisabledbydefaultand
recommendedthatadministratorsdisablethisfeatureafteritsusagetopreventmalicioususebyan
attackerwithphysicalaccesstothedevice.
| switch(config)# |     | front-panel-security | factory-reset |     |
| --------------- | --- | -------------------- | ------------- | --- |
This command will enable front-panel factory reset capability, where user can
trigger factory-reset via reset button. This feature will remain enabled until
| it is    | disabled, | or a factory-reset | is performed. |     |
| -------- | --------- | ------------------ | ------------- | --- |
| Continue | (y/n)?    |                    |               |     |
Toviewtheconfigurationchange-
| switch#       | show          | front-panel-security | status        |            |
| ------------- | ------------- | -------------------- | ------------- | ---------- |
| Front         | panel factory | reset                |               | : disabled |
| First         | occurrence    | of front-panel       | factory reset | : N/A      |
| USB Auxiliary |               | Port                 |               |            |
TheAOS-CXswitchfront-panelincludesanUSBAuxiliaryportforthefollowingpurposes–
n USBMassstorage-flashdrivefordeploying,troubleshooting,backingupconfigurations,or
upgradingswitches
n BluetoothAdapter-allowsBluetoothenableddevicestoconnecttoandmanagetheswitchona
wirelessBluetoothPersonalAreaNetwork(PAN)
TheBluetoothfeaturehasbeenenabledbydefaultinAOS-CXswitchesanddesignedforoperational
simplicity.TheswitchprovidesanIPaddresstopaireddevicesthoughDHCPwhentheyjointhe
BluetoothPersonalAreaNetwork.Paireddevicescanthenmanagetheswitchthroughfollowing
methods
SSH
n
n WebUI
n RESTAPI
n ArubaCXMobileApp
RefertoSecuringSwitchManagementAccessControlfordetailsonsecuringthesemanagement
connections.
ThisUSBAuxiliaryportisenabledbydefaultsorecommendedtobedisabledwhennotinuse,andonly
temporarilyenabledwhenneeded.
HardeningtheCXManagementplane|14

TodisabletheUSBAuxiliaryportentirely(USBMassStorageandBluetoothAdapter),usethefollowing
command:
| switch(config)# |     | no usb |     |     |
| --------------- | --- | ------ | --- | --- |
Toviewtheconfigurationchange:
| switch   | # show | usb |     |     |
| -------- | ------ | --- | --- | --- |
| Enabled: | No     |     |     |     |
| Mounted: | No     |     |     |     |
AOS-CXswitchesalsohavethesupporttodisableonlythebluetoothfeatureratherthandisablingthe
USBAuxiliaryportcompletely,toperformthesamefollowingconfigurationcanbeexecutedwhichis
enabledbydefault:
| switch(config)# |            | bluetooth | disable         |     |
| --------------- | ---------- | --------- | --------------- | --- |
| switch          | # show     | bluetooth |                 |     |
| Enabled         |            | :         | No              |     |
| Device          | Name       | :         | 6300-SG9ZKN002Z |     |
| Adapter         | State      | :         | Absent          |     |
| Firmware        | Validation |           |                 |     |
AllAOS-CXswitchfirmwareissignedbyHPEatthetimethefirmwareiscreated.Thefirmwaresignature
isverifiedatthetimeofdownloadandverifiedateveryboot.Thepublickeysusedtoverifythe
firmwareisstoredwithinthebootloaderandfirmware.ThefirmwareisdigitallysignedwithRSA-3072
andSHA-256.
Iftheswitchfirmwarevalidationfailsatboot,theswitchwillfailtobootwithoneofthefollowingerror
messagesanddroptheuserintotheServiceOSloginscreen:
| Error: | Signature | verification |       | failed |
| ------ | --------- | ------------ | ----- | ------ |
| Error: | Signature | not          | found |        |
| Error: | Invalid   | signature    |       |        |
Alternatively,afterloadingthefirmwaretothebootbank–primaryorsecondary,administratorscan
verifythefirmwareintegrityusingbelowshowcommandbeforebootingtheswitch.
Theverifyoptionperformsanintegritycheckthattheimagehasavalidsignatureandiscompatiblewith
thissystem.Theswitchpreventsthedownloadoffirmwarewithoutavalidsignature.
| switch#     | show     | images verify |       | primary     |
| ----------- | -------- | ------------- | ----- | ----------- |
| The primary | image    | is            | valid |             |
| switch#     | show     | images verify |       | secondary   |
| The image   | does     | not contain   |       | a signature |
| Enhanced    | security |               | mode  |             |
AOS-CXprovidestwosecuritymodesthatcontrolaccesstocertainsystemmanagementfeatures—
standardandenhanced.AllAOS-CXswitchesoperateinstandardmodebydefault,withnosystem-level
restrictionsinplaceforanyfunctionality.Theenhancedsecuritymodedisablesaccesstothestart-shell
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 15

commandintheAOS-CXCLI,aswellastheServiceOScommandsconfig-clear,password,sh,and
update.
Inadualmanagementmoduleswitch,boththemanagementmodulesshouldbesettosamesecure
mode.
ChangingtheswitchsecuritymodeisperformedeitherthroughCLIorfromtheServiceOSshell.All
changestotheswitchsecuritymode(standardtoenhancedorenhancedtostandard)resultin
zeroizationofthefilesystemandaresettofactorydefaults.
| 6300-VSF(config)# |     | secure-mode | enhanced |     |
| ----------------- | --- | ----------- | -------- | --- |
This will set the switch into enhanced secure mode. Before enhanced secure mode is
enabled, the switch must securely erase all customer data and reset to factory
defaults. This will initiate a reboot and render the switch unavailable until the
| zeroization | is     | complete. |     |     |
| ----------- | ------ | --------- | --- | --- |
| Continue    | (y/n)? | y         |     |     |
ServiceOSbeusedasecondarymethodtoboottheswitchinenhancedsecure-mode.Reboottheswitch
toServiceOSusingthefollowingcommand:
| switch#  | boot system | serviceos     |            |             |
| -------- | ----------- | ------------- | ---------- | ----------- |
| One time | boot to     | ServiceOS     | initiated. |             |
| Checking | if the      | configuration | needs to   | be saved... |
This will reboot the system to ServiceOS and render the entire switch unavailable.
Access to ServiceOS is only available through the serial console.
| Continue | (y/n)? |     |     |     |
| -------- | ------ | --- | --- | --- |
OncetheswitchhasrebootedandtheServiceOSloginpromptisdisplayed,loginasadmin(no
passwordissetbydefault).Usethefollowingcommandtoenableenhancedsecuritymode:
| SVOS> secure-mode |     | enhanced |     |     |
| ----------------- | --- | -------- | --- | --- |
############################WARNING##########################################
This will set the switch into enhanced secure mode. Before enhanced secure mode
is enabled, the switch must securely erase all customer data and reset the switch
to factory defaults. This will initiate a reboot and render the switch unavailable
| until the | zeroization | is  | complete. |     |
| --------- | ----------- | --- | --------- | --- |
############################WARNING###############################
| Continue | (y/n)? |     |     |     |
| -------- | ------ | --- | --- | --- |
Enteringywillcausetheswitchtoreboot,zeroizethefilesystem,thenrebootanadditionaltime.
Toreverttothestandardsecuritymode,reboottoServiceOSasabove,loginasadmin,thenusethe
followingcommand:
| SVOS> secure-mode |     | standard |     |     |
| ----------------- | --- | -------- | --- | --- |
############################WARNING############################
This will set the switch into standard secure mode. Before standard secure mode
is rnabled, the switch must securely erase all customer data and reset the switch
to factory defaults. This will initiate a reboot and render the switch unavailable
| until the | zeroization | is  | complete. |     |
| --------- | ----------- | --- | --------- | --- |
############################WARNING############################
| Continue | (y/n)? |     |     |     |
| -------- | ------ | --- | --- | --- |
ServiceOSshalldefaulttostandardsecuremodeifZeroizationfailswhilesettingtostandardor
enhancedsecuremode.
HardeningtheCXManagementplane|16

ServiceOS password authentication

By default, the ServiceOS shell (accessible only from the local switch console port) requires no password
to login as admin; to enable password authentication for ServiceOS, use the following command from
the configuration context:

switch(config)# system serviceos password-prompt

When this setting is enabled, logging in to the ServiceOS shell with the admin user requires the same
password used to authenticate the admin user in the AOS-CX CLI or Web UI.

If this setting is enabled, a forgotten admin user password cannot be reset using ServiceOS; if there are
no other local or RADIUS/TACACS user accounts with administrator-level access, the switch must be
zeroized by entering the username zeroize at the ServiceOS login prompt to restore administrator
access. See password reset for more information.

Securing Switch Management Access Control

Use the following console, SSH, Telnet, and HTTPS server strategies to secure the switch management
access.

User Management and Password Control

User Groups

A factory-default switch comes with a single user named admin member of built-in administrators
group. Up to 63 local users can be added, for a total of 64 users including the default user admin. A user
can belong to only one group. The switch provides the following built-in user groups with corresponding
roles. Each of these roles comes with a set of privileges.

n Administrators—full access (privilege level 15)

o Perform firmware upgrades

o Make configuration changes

o View all switch configuration information, including sensitive data such as ciphertext passwords

o Add and remove local user accounts, and change user passwords

o All REST interface methods (GET, PUT, POST, PATCH, DELETE) can be used

n Operators – limited access (privilege level 1)

o Display-only CLI access

o View non-sensitive configuration information

o Only the REST interface GET method can be used

n Auditors – limited access (privilege level 19)

o Access to Commands in “auditor” context only

o Web-UI “system->Log Page” view only.

o REST Interface GET method available only for following resources only

l Audit log: /logs/audit

l Event log: /logs/event

AOS-CX 10.14.1000 Hardening Guide | (All Switch Series)

17

Apartfromthebuilt-ingroups,theswitchenablesyoutocreateupto29user-definedlocalusergroups,
forthepurposeofconfiguringlocalauthorization.Localauthorizationusesrole-basedaccesscontrol
(RBAC)toproviderole-basedprivilegelevelsplusoptionaluser-definedlocalusergroupswith
commandexecutionrules.Eachofthe29user-definedgroupssupportupto1024CLIcommand
authorizationrulesthatdefinewhatCLIcommandscanbeexecutedbymembersofthegroup.
SampleConfigurationtocreateuser-definedlocalusergroup:
| switch(config)# |     | user-group | sample-group |     |     |
| --------------- | --- | ---------- | ------------ | --- | --- |
switch(config-usr-grp-sample-group)# 10 comment Deny all show aaa commands
switch(config-usr-grp-sample-group)# 10 deny cli command "show aaa .*"
switch(config-usr-grp-sample-group)# 20 comment Permit all other show commands
switch(config-usr-grp-sample-group)# 20 permit cli command "show .*"
| switch(config-usr-grp-sample-group)# |      |            | exit           |        |          |
| ------------------------------------ | ---- | ---------- | -------------- | ------ | -------- |
| 6200(config)#                        | show | user-group |                |        |          |
| GROUP                                | NAME | GROUP TYPE | INCLUDED GROUP | NUMBER | OF RULES |
-------------- -------------- ------------------ -------------------
| administrators |            | built-in      | n/a | n/a |     |
| -------------- | ---------- | ------------- | --- | --- | --- |
| auditors       |            | built-in      | n/a | n/a |     |
| operators      |            | built-in      | n/a | n/a |     |
| sample-group   |            | configuration | --  | 2   |     |
| Security       | User Group |               |     |     |     |
Securitylogcommandsforshowing,clearing,andcopyingthesecuritylogscanbemadeavailabletoa
securityuser.Tohaveasecurityuser,theadminmustcreateasecurityusergroupandaddauserto
thegroup.Theadminmustalsograntpermissiontomembersofthesecurityusergroupforthethree
securitylogcommands.Onlyuserswhoaremembersofthesecuritygrouphavepermissiontoexecute
thesecuritylogcommands.Theadminuserwhocreatedthesecurityusergroupdoesnothave
permissiontousethesecuritylogcommands:
| switch(config)# |     | user-group | security-group |     |     |
| --------------- | --- | ---------- | -------------- | --- | --- |
switch(config-usr-grp-security-group)# permit cli command "show security-logs*"
switch(config-usr-grp-security-group)# permit cli command "clear security-logs"
switch(config-usr-grp-security-group)# permit cli command "copy security-log*"
switch(config-usr-grp-security-group)# exit
switch(config)# user security-user group security-group password
| Adding  | user security-user    |     |     |     |     |
| ------- | --------------------- | --- | --- | --- | --- |
| Enter   | password:************ |     |     |     |     |
| Confirm | password:************ |     |     |     |     |
Showingthesecuritylogs:
| switch# | show security-logs |     |     |     |     |
| ------- | ------------------ | --- | --- | --- | --- |
Copyingthesecuritylogs:
switch# copy security-log sftp://user1@99.99.99.99/coredump.xz vrf mgmt
| Hardening | Password | Rules |     |     |     |
| --------- | -------- | ----- | --- | --- | --- |
HardeningtheCXManagementplane|18

WhenmanaginganAOS-CXSwitches,settingupasecurenetworkisessential.Acrucialfactorinsecurity
istheselectionofastrongpassword.PasswordsareneverdisplayedinplaintextformatinCLIsand
configfiles.Passwordsareencryptedwhenstoredintheconfigfile.
Passwordsmust:
n ContainonlyASCIIcharactersfromdecimal33to126( Hexadecimal21to7E).Spacesarenotallowed
n Containatmost64characters.
Passwordsareportabletodifferentswitchusingdefaultorcustomerconfigurednon-defaultexportkey.
Thepasswordcomplexityfeaturewillhelporganizationtosetpasswordpolicyfortheiradministrators
Password Complexity
Thepasswordcomplexityfeaturehelpsinenforcementofcomplexityruleswhenconfiguringlocaluser
accountpasswords.Itisdisabledbydefault.Thepasswordcomplexityfeaturewillhelporganizationto
setpasswordpolicyfortheirusers.Remembertoenablethepasswordcomplexityfeatureafter
configuringitfortherulestobeenforced.Enablingorchangingpasswordcomplexitysettingsaffects
passwordcreationorpasswordchangeafterthepasswordcomplexityfeatureisenabledorchanged.
Thefollowingenforcementwillapplytonewusercreationorapasswordupdateoncethepassword
complexityfeatureisenabled:
Usercreation/Passwordupdatewith`ciphertext-password`isnotallowed,becausepassword
n
complexitycheckcannotbeperformedonciphertextpassword.
n Thefollowingpasswordcomplexitycheckwillbeenforced
| switch(config)#          |          | password            | complexity       |            |           |           |
| ------------------------ | -------- | ------------------- | ---------------- | ---------- | --------- | --------- |
| switch(config-pwd-cplx)# |          |                     | minimum-length   |            | 9         |           |
| switch(config-pwd-cplx)# |          |                     | history-count    |            | 4         |           |
| switch(config-pwd-cplx)# |          |                     | position-changes |            | 5         |           |
| switch(config-pwd-cplx)# |          |                     | enable           |            |           |           |
| switch(config-pwd-cplx)# |          |                     | exit             |            |           |           |
| switch                   | # show   | password-complexity |                  |            |           |           |
| Global                   | password | complexity          | checking         |            | criteria: |           |
|                          | Password | complexity          |                  |            |           | : Enabled |
|                          | Previous | passwords           | to               | check      |           | : 4       |
|                          | Minimum  | password            | length           |            |           | : 9       |
|                          | Minimum  | position            | changes          |            |           | : 5       |
|                          | Maximum  | adjacent            | characters       | count      |           | : 0       |
|                          | Password | composition         |                  |            |           |           |
|                          |          | Minimum             | lowercase        | characters |           | : 1       |
|                          |          | Minimum             | uppercase        | characters |           | : 1       |
|                          |          | Minimum             | special          | characters |           | : 1       |
|                          |          | Minimum             | numeric          | characters |           | : 1       |
| Non-Default              | Export   | Password            |                  |            |           |           |
Theexportpasswordisusedtotransformcriticalsensitiveinformationintociphertextsuitablefor
exportingandshowingbycommandssuchasshowrunning-config.Transformationenablessafeswitch
configurationimportandexport.Allfactory-defaultswitcheshaveidenticaldefaultexportpasswords.
Forsecurity,itisrecommendedthatyousetthesamenon-defaultexportpasswordoneveryswitchina
groupthatwillexchangesensitiveconfigurationinformation.Onlyswitcheswithidenticalexport
passwordscanexchangesensitiveconfigurationinformation.
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 19

| switch#         | show          | service export-password |                 |     |
| --------------- | ------------- | ----------------------- | --------------- | --- |
| Export          | password:     | default                 |                 |     |
| switch#         | config        | t                       |                 |     |
| switch(config)# |               | service export-password |                 |     |
| Enter           | password:     | ********                |                 |     |
| Confirm         | password:     | ********                |                 |     |
| switch(config)# |               | show service            | export-password |     |
| Export          | password:     | custom                  |                 |     |
| Built-in        | Admin Account | Password                | Reset           |     |
Whenadministratorsforgettheirswitchconsolepasswords,theymustendureatime-consumingreset
process,resultinginlossofproductivity.Iftherearemultipleadministratorsfortheswitch,itis
recommendedtoresetthepasswordusinganotheradministratoraccount.Therearetwowaystoreset
thepasswordincasethereissingleadminuseronlyfortheswitch:
| Reverting | the switch | to factory | defaults |     |
| --------- | ---------- | ---------- | -------- | --- |
1. Atthemanagercommandprompt,entererasestartup-config.
|     | switch(config)# | erase | startup-config |     |
| --- | --------------- | ----- | -------------- | --- |
2. Boottheswitchwithoutsavingthecurrentconfiguration
|     | switch# | boot system  |                           |          |
| --- | ------- | ------------ | ------------------------- | -------- |
|     | Do you  | want to save | the current configuration | (y/n)? n |
This will reboot the entire switch and render it unavailable until the
|     | process    | is complete. |                  |     |
| --- | ---------- | ------------ | ---------------- | --- |
|     | Continue   | (y/n)? y     |                  |     |
|     | The system | is going     | down for reboot. |     |
Resetting the switch admin password using the serviceOS console
Performthistaskonlywhentheswitchadminuserpasswordhasbeenforgotten:
HardeningtheCXManagementplane|20

Refer to the “Managing users and groups” section of the Security Guide for your switch model for more
information.

Authentication, Authorization and Accounting (AAA)

AOS-CX have following management interfaces for accessing the switch for configuration and
management -

n Console

n SSH

n Telnet

n https-server – Web UI and REST API

Telnet is not a recommended method to access the switch for configuration and management , as it is not a

secure communication. It is not enabled by default on any VRF.

User accounts for accessing these management interfaces can be stored locally or managed on remote
TACACS+ or RADIUS servers. AAA (Authentication, Authorization, and Accounting) is the security
framework to manage user access, enforce privileges, and log the user access records.

The following table describes supported AAA services based on the user account management
methods:

User Account
Management

Local

TACACS+

RADIUS

Authentication

Yes

Yes

Yes

AOS-CX 10.14.1000 Hardening Guide | (All Switch Series)

21

User Account
Management

Local

TACACS+

RADIUS

Authorization

Yes, RBAC

Yes, Per Command

No

Authorization and RBAC

Accounting

Yes

Yes

Yes

Authentication

Authentication is the process of identifying a user and granting them access to the network. Most of the
time, this is done through traditional username and password credential , but it could be extended to
SSH public key authentication. The following table describes supported authentication types based on
their user account management methods.

User Account
Management

Authentication Type

Local Authentication

Local

TACACS+

RADIUS

n Username/Password
n SSH Public Key
n SSH two-factor

Authentication

Username/Password

n Username/Password
n SSH two-factor

Authentication

Local user names and passwords are configured on a per-switch basis and provide the most basic form
of authentication. Local authentication is often used as the fallback login method. Local authentication
can provide a minimum-security level should the primary method fail, but does not completely disable
management access to the switch. To configure a local administrator-level user named localadmin with
interactive password entry:

switch(config)# user localadmin group administrators password
Enter password: **********
Confirm password: **********

To create an operator-level user named localoperator with a plaintext password:

switch(config)# user localoperator group operators password plaintext abcdefghij

An administrator can also enter a password as a ciphertext string rather than being entered in plaintext.
In AOS-CX, ciphertext passwords cannot be generated manually; they must be copied from another
switch with the same export password configured. By default all the switches will have same export
password. Refer to Non-Default Export Password for the configuration. Once the export passwords on
the source and destination switches are the same, copy the ciphertext password from the source switch
and apply it to the destination:

switch(config)# user localadmin group administrators password ciphertext
myCipherText

Hardening the CX Management plane | 22

Ifpasswordcomplexityisenabled,ciphertextpasswordconfigurationsarenotallowed.
| Local Authentication | Configuration | Task List |     |
| -------------------- | ------------- | --------- | --- |
Show
| Task | Configuration |     |     |
| ---- | ------------- | --- | --- |
Commands
Enablelocalauthentication aaaauthenticationlogin<console/default/ssh/telnet/https- showaaa
| fordesiredmanagement | server>local |     | authentication |
| -------------------- | ------------ | --- | -------------- |
interface
Default–Includesallthe
managementinterfaces
| Limittheloginattempts | Console: |     | showaaa |
| --------------------- | -------- | --- | ------- |
authentication
aaaauthenticationconsole-login-attempts<1-10>console-
|     | lockout-time<1-3600s> |     | show |
| --- | --------------------- | --- | ---- |
authentication
SSH/Telnet/https-Server:
locked-out-users
aaaauthenticationlogin-attempts<1-10>lockout-time<1-
3600s>
Remote Authentication
RemoteAuthenticationinvolvestheuseofremoteRADIUS,RadSecandTACACS+serversfor
authenticatingthemanagementusers.RemoteAAAserversareusedassinglepointofmanagementto
configureandstoreuseraccounts.Theyareoftencoupledwithdirectoriesandmanagement
repositories,simplifyingthesetupandmaintenanceoftheend-useraccounts.
| Remote Authentication | Configuration | Task List |     |
| --------------------- | ------------- | --------- | --- |
Show
| Task | Configuration |     |     |
| ---- | ------------- | --- | --- |
Commands
| Configuretheserver | RADIUSServer:                                             |     | showradius-  |
| ------------------ | --------------------------------------------------------- | --- | ------------ |
|                    | radius-serverhost<IPv4/IPv6/FQDN>keyplaintext<secret-key> |     | serverdetail |
|                    | vrf<vrf-name>                                             |     | showtacacs-  |
|                    | RadSecServer:                                             |     | serverdetail |
radius-serverhost<IPv4/IPv6/FQDN>keyplaintext<secret-key>
tlsvrf<vrf-name>
TACACS+Server:
tacacs-serverhost<IPv4/IPv6/FQDN>keyplaintext<secret-key>
vrf<vrf-name>
| ServerGroupCreation | RADIUSServer: |     | showaaaserver- |
| ------------------- | ------------- | --- | -------------- |
| andAssociation.     |               |     | groups         |
aaagroupserverradius<group-name>
| Theorderinwhich | server<IPv4/IPv6/FQDN>vrf<vrf-name> |     |     |
| --------------- | ----------------------------------- | --- | --- |
serversareaddedtoa
RadSecServer:
groupisimportant.The
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 23

Show
| Task |     | Configuration |     |
| ---- | --- | ------------- | --- |
Commands
| serveraddedfirstis |     | aaagroupserverradius<group-name>       |     |
| ------------------ | --- | -------------------------------------- | --- |
| accessedfirst,     |     | server<IPv4/IPv6/FQDN>tlsvrf<vrf-name> |     |
andifnecessary,the
TACACS+Server:
secondserverisaccessed
aaagroupservertacacs<group-name>
second,andsoon.
server<IPv4/IPv6/FQDN>vrf<vrf-name>
Enablelocal aaaauthenticationlogin<console/default/ssh/telnet/https- showaaa
| authenticationfor |     | server><group-name> | authentication |
| ----------------- | --- | ------------------- | -------------- |
desiredmanagement
interface
Default–Includesallthe
managementinterfaces
| Auth-Type“chap” |     | radius-serverauth-typechap | showradius- |
| --------------- | --- | -------------------------- | ----------- |
server
| BydefaultCXswitchuses |     | tacacs-serverauth-typechap |             |
| --------------------- | --- | -------------------------- | ----------- |
| “pap”asauth-type.     |     |                            | showtacacs- |
server
“Chap”isstronger
authenticationmethod
thanpap
SourceInterface ipsource-interface<radius/tacacs><ip-address> Showipsource-
interface
Toensurethatalltraffic ipv6source-interface<radius/tacacs><ipv6-address>
| sentfromtheswitchto |     |     | Showipv6         |
| ------------------- | --- | --- | ---------------- |
| theAAAserverusesthe |     |     | source-interface |
samesourceIPaddress
RoleAssignmentin n Aruba-Admin-RoleVSA-Maptheusertothematchinglocal
| RADIUS |     | user-groupname. |     |
| ------ | --- | --------------- | --- |
n Aruba-Priv-Admin-UserVSA-Extracttheprivilegelevel(1,
15,or19)andmaptheusertothelocaluser-group
correspondingtothisprivilegelevel
(1=operators,15=administrators,19=auditors).Privilege
levels2to14mayalsobeusedwithmatchinglocaluser
groupsnamed2to14.
n RADIUSService-Type-MapAdministrative-User(6)to
administratorsandmapNASPrompt-User(7)tooperators.
RoleAssignmentin n Aruba-Admin-RoleVSA-Maptheusertothematching
| TACACS+ |     | correspondinglocalusergroupName |     |
| ------- | --- | ------------------------------- | --- |
n TACACS+priv-lvlattribute-Extracttheprivilegelevel(1,15,
or19)andmaptheusertothelocaluser-group
correspondingtothisprivilegelevel
(1=operators,15=administrators,19=auditors).
n Privilegelevels2to14mayalsobeusedwithmatchinglocal
usergroupsnamed2to14.
| Authentication | Fallback and | Fail through |     |
| -------------- | ------------ | ------------ | --- |
HardeningtheCXManagementplane|24

TopreventauthenticationfailurebecauseofRemoteAAAServerfailure,itisrecommendedtoconfigure
morethanoneremoteAAAServer
Whendefiningtheserveraccesssequenceforauthenticationwithaaaaauthenticationlogindefault,
thereisanimpliedlocalincludedasthelastiteminthelist.IfnoremoteAAAserverscanbereached,
localauthenticationwillbeattempted.
Normally,authenticationsuccessorfailureisperformedbythefirstreachableAAAserver.Ararely
neededfeaturenamed"Authenticationfail-through"isavailable.Ifauthenticationfail-throughis
enabledandauthenticationfailsonthefirstreachableAAAserver,authenticationisattemptedonthe
secondAAAserver,andsoon,untilsuccessfulauthenticationortheserverlistisexhausted.Enabling
Authenticationfail-throughistypicallyunnecessarybecausetheusercredentialdatabasesshouldbe
consistentacrossallAAAservers.Authenticationfail-throughmightbehelpfulifyourAAAuser
credentialdatabasesarenotquicklysynchronizedacrossallAAAservers
Toconfigureandviewtheauthenticationfail-throughfeature:
| switch(config)#     |          | aaa authentication |          |     | allow-fail-through |     |
| ------------------- | -------- | ------------------ | -------- | --- | ------------------ | --- |
| switch#             | show     | aaa authentication |          |     |                    |     |
| AAA Authentication: |          |                    |          |     |                    |     |
| Fail-through        |          |                    |          |     | : Enabled          |     |
| Limit Login         | Attempts |                    |          |     | : Not set          |     |
| Lockout             | Time     |                    |          |     | : 300              |     |
| Console             | Login    | Attempts           |          |     | : Not set          |     |
| Console             | Lockout  | Time               |          |     | : 300              |     |
| Authentication      |          | for default        | channel: |     |                    |     |
----------------------------------------------------------------------------------
-----------
| GROUP NAME |     |     |     | |   | GROUP PRIORITY |     |
| ---------- | --- | --- | --- | --- | -------------- | --- |
----------------------------------------------------------------------------------
-----------
| local               |     |           |            | |   | 0   |     |
| ------------------- | --- | --------- | ---------- | --- | --- | --- |
| Per-User Management |     | Interface | Enablement |     |     |     |
Bydefault,switchusersareenabledforaccessingtheswitchthroughalltheseavailablemanagement
interfaces:ssh,telnet,https-server,console.Additionallyfine-grainedcommandauthorizationcanbe
performedusingRBAC,butitisapplicableonlyfortheCLIsnotforWeb-UI/RESTAPIrequests.Hence
HPEANWrecommendsenablingthespecificmanagementinterfacesfortheusersbasedontheuser
typeusingbelowways-
| Local Per-user | Management |     | Interface | Enablement |     |     |
| -------------- | ---------- | --- | --------- | ---------- | --- | --- |
Localper-usermanagementinterfaceenablementisperformedwithCLIcommand.Exampleof
disablingtheSSHmanagementinterfaceforlocaluseradmin1.
| switch(config)# |     | no user    | admin1       | management-interface |     | ssh |
| --------------- | --- | ---------- | ------------ | -------------------- | --- | --- |
| switch(config)# |     | show       | user-list    | management-interface |     |     |
| USER ENABLED    |     | MANAGEMENT | INTERFACE(S) |                      |     |     |
------------------------------------------------------------
| admin ssh,telnet,https-sever,console |                             |            |     |     |     |     |
| ------------------------------------ | --------------------------- | ---------- | --- | --- | --- | --- |
| admin1                               | telnet,https-server,console |            |     |     |     |     |
| Remote TACACS+                       |                             | and RADIUS |     |     |     |     |
ForremoteTACACS+andRADIUSservers,per-usermanagementinterfaceenablementisperformedby
configuringtheAOS-CXVSAAruba-User-Mgmt-Interface.OntheTACACS+orRADIUSserver,theAOS-CX
VSAAruba-User-Mgmt-Interfacemustbesettoacomma-separatedlistofmanagementinterfacenames
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 25

for which login is permitted by the associated user. Management interfaces omitted from the list are
disabled for the associated user. A maximum of four management interface names are allowed, with
each management interface name given once. Permitted management interface names (always
lowercase) are as follows:

n ssh

n telnet

n https-server

n console

The VSA has a maximum length of 32 characters. The VSA is ignored by the switch if longer than 32
characters. When a user login fails because of an attempt to use a management interface that is not
allowed, an event log is available indicating the enabled management interfaces as received in the
TACACS+ or RADIUS VSA.

When using a RADIUS server other than ClearPass Policy Manager (CPPM), before setting the Aruba-
User-Mgmt-Interface VSA, you must first define the VSA on the RADIUS server in file

ATTRIBUTE Aruba-User-Mgmt-Interface 69 string

Example RADIUS server VSA value that enables the two named management interfaces (ssh, telnet)
while disabling the two unnamed management interfaces (https-server, console):

Aruba-User-Mgmt-Interface = "ssh,telnet"

Example RADIUS server VSA value that enables all four management interfaces:

Aruba-User-Mgmt-Interface = "ssh,telnet,https-server,console"

Authorization

Authorization controls how authenticated users execute commands and interact with the switch.
Authorization uses role-based access control (RBAC) to provide role-based privilege levels plus optional
user-defined local user groups with command execution rules.

Switch(config)# aaa authorization commands <console | default | ssh | telnet >
group <tacacs | local |none > <tacacs | local | none>

n TACACS+ Authorization - Upon successful user authentication, the user is assigned their role by the
TACACS+ server. See also User role assignment using TACACS+ attributes .TACACS+ authorization
provides command filtering to allow/disallow individual command or command set execution. Each
command is sent to the TACACS+ server for approval, and the switch then allows/disallows command
execution according to the server response.TACACS+ authorization applies only to the CLI interface.

n RADIUS Authorization - Command authorization is not supported by RADIUS servers, however, user-
defined local user groups can be configured with command-authorization rules, providing locally
configured per command authorization for members of such groups.

n Fallback - Local authorization can be used as a fallback for the situation in which communication is

lost with all TACACS+ servers after a successful authentication.

Hardening the CX Management plane | 26

n Whendefiningtheserveraccesssequenceforauthorizationwithaboveaaaauthorization
commands,itisrecommendedtoalwaysincludeeitherlocalornoneasthelastiteminthelist
n Failthrough–Authorizationfail-throughisrecommendedonlyfordeploy.mentswherethereare
potentialsynchronizationissues,soauthorizationwillbefailinginoneserverbutsucceedingin
other.
| Switch(config)# |         | aaa               | authorization |          | allow-fail-through |
| --------------- | ------- | ----------------- | ------------- | -------- | ------------------ |
| switch#         | show    | aaa authorization |               |          |                    |
| *******         | Command | authorization     |               | *******  |                    |
| Fail-through    |         |                   |               |          | : Enabled          |
| Authorization   |         | for default       |               | channel: |                    |
---------------------------------------------------------------------------
| GROUP NAME |     |     |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | --- | --- | ---------------- |
---------------------------------------------------------------------------
| local |     |     |     |     | | 0 |
| ----- | --- | --- | --- | --- | --- |
Accounting
LocalAccountingrecordsalltheCLIandRESTaccessactivitiesbyusersfromallchannels.Itlogsand
helpstotrackalltheconfigurationchangesandshowcommandexecutionshappenedattheswitchfor
auditingoraccountingpurposes.Thisaccountinginformationiscapturedandmadeavailablelocally
(Enabledbydefaultandalwaysactive)and,ifdesired,forsendingtoremoteAAAservers:
n ExecAccounting:userlogin/logoutevents.
n Commandaccounting:commandsexecutedbyusers.
n Systemaccounting:remoteaccountingOn/Offevents.
n Interactionsonthenon-CLIinterfaces:RESTandWebUI.
Thefollowingisnotcapturedormadeavailableasaccountinginformation:
n CLIcommandsthatreboottheswitch.
n Iteractionsinthebashshell.( Ontheotherhand,loggingof“start-shell”CLIissupported.Ithelpsin
auditing)
Sampleaccountinginformation:
| Switch# | show | aaa accounting |     | log | all |
| ------- | ---- | -------------- | --- | --- | --- |
---------------------------------------------------
| Command | logs | from previous |     | boots |     |
| ------- | ---- | ------------- | --- | ----- | --- |
---------------------------------------------------
2023-06-09T05:50:27.765+00:00 acctsyslogd[2788]: AUDIT|CLI "enable" executed
by user 'admin' from address '0.0.0.0' through CONSOLE session which resulted
| in success | at  | timezone | UTC. |     |     |
| ---------- | --- | -------- | ---- | --- | --- |
Remote Accounting
Forremoteaccounting,theinformationissenttothefirstreachableremoteserverthatwasconfigured
withthiscommandforremoteaccounting.Ifnoremoteserverisreachable,localaccountingremains
availablebydefault
Toenableandviewtheaccountingconfiguration:
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 27

Switch(config)# aaa accounting all-mgmt <console|default|https-server|ssh|telnet>
| start-stop | <group|local> |                |     |     |     |     |     |
| ---------- | ------------- | -------------- | --- | --- | --- | --- | --- |
| switch#    | show          | aaa accounting |     |     |     |     |     |
AAA Accounting:
| Accounting |     | Type         |          |     |     |     | : all        |
| ---------- | --- | ------------ | -------- | --- | --- | --- | ------------ |
| Accounting |     | Mode         |          |     |     |     | : start-stop |
| Accounting |     | Fail-through |          |     |     |     | : Disabled   |
| Accounting | for | default      | channel: |     |     |     |              |
----------------------------------------------------------------------------------
----------------------------------------------------------
| GROUP NAME |     |     |     |     | | GROUP | PRIORITY |     |
| ---------- | --- | --- | --- | --- | ------- | -------- | --- |
----------------------------------------------------------------------------------
-----------
| local       |     |        |     |     | | 0 |     |     |
| ----------- | --- | ------ | --- | --- | --- | --- | --- |
| RadSec over |     | RADIUS |     |     |     |     |     |
TheRADIUSprotocolusesUDPasunderlyingtransportlayerprotocol.RadSecisaprotocolthat
supportsRADIUSoverTCPandTLS.InconventionalRADIUSrequests,securityisaconcernasthe
confidentialdataissentusingweakencryptionalgorithms.Theaccessrequestsareinplaintext
includesinformationsuchasusername,IPaddressandsoon.Theuserpasswordisanencrypted
sharedsecret.Asaresult,eavesdropperscanlistentotheseRADIUSrequestsandcollectconfidential
information.DataprotectionisnecessaryinroamingenvironmentswheretheRADIUSpacketstravel
acrossmultipleadministrativedomainsanduntrustednetworks.TheRadSecmodulesecuresthe
communicationbetweentheswitchandRADIUSserverusingaTLSconnection.UsingRADIUSoverTLS
providesuserswiththeflexibilitytohostRADIUSserversacrossgeographiesandWANnetworks.
HPEArubaNetworkingrecommendstheusageofRadSecoverRADIUS.BothIPv4andIPv6RadSec
serversaresupported.
ToenableRADIUSsecurity,usethetlsparameterwiththefollowingcommand.
RefertotheSecurityGuideforyourswitchfordetailedstepstoassociatetheTLScertificateformutual
authentication.
| Switch(config)# |     | radius-server |     | host | <FQDN/ipv4/ipv6> |     | tls |
| --------------- | --- | ------------- | --- | ---- | ---------------- | --- | --- |
ToviewtheRadSecserverconfiguration:
| switch#        | show           | radius-server |                      |            |     |         |     |
| -------------- | -------------- | ------------- | -------------------- | ---------- | --- | ------- | --- |
| Unreachable    | servers        |               | are preceded         |            | by  | *       |     |
| *******        | Global         | RADIUS        | Configuration        |            |     | ******* |     |
| Shared-Secret: |                | None          |                      |            |     |         |     |
| Timeout:       | 10             |               |                      |            |     |         |     |
| Auth-Type:     | pap            |               |                      |            |     |         |     |
| Retries:       | 3              |               |                      |            |     |         |     |
| Initial        | TLS Connection |               | Timeout:             |            | 30  |         |     |
| TLS Timeout:   |                | 5             |                      |            |     |         |     |
| Tracking       | Time           | Interval      | (seconds):           |            | 300 |         |     |
| Tracking       | Retries:       | 3             |                      |            |     |         |     |
| Tracking       | User-name:     |               | radius-tracking-user |            |     |         |     |
| Tracking       | Password:      | None          |                      |            |     |         |     |
| Status-Server  |                | Time Interval |                      | (seconds): |     | 300     |     |
| Number of      | Servers:       | 1             |                      |            |     |         |     |
HardeningtheCXManagementplane|28

| AAA Server | Status Trap: | Disabled |     |     |
| ---------- | ------------ | -------- | --- | --- |
----------------------------------------------------------------------------------
| SERVER NAME |     |     | | TLS | | PORT | VRF |
| ----------- | --- | --- | ----- | ------------ |
----------------------------------------------------------------------------------
| cppm.abcd.net |     |     | | Yes | | 1812 | mgmt |
| ------------- | --- | --- | ----- | ------------- |
----------------------------------------------------------------------------------
| Hardening | SSH |     |     |     |
| --------- | --- | --- | --- | --- |
ThefollowingsectionsdescribesecurityandhardeningworkflowsforSSH.
| Public Key | Authentication |     |     |     |
| ---------- | -------------- | --- | --- | --- |
Passwordsareeasytouseandremember,buttheyarevulnerabletoattacksandhumanerrors.Keys
aremoresecureandefficientcomparedtopasswords.SSHPublickeyauthenticationisenabledby
defaultandtakesprecedenceoverpassword-basedauthentication.ValidateusersidentifiedwithSSH
publickeysstoredinthelocaluserdatabaseusingthefollowingcommands.
Switch(config)# user admin authorized-key ecdsa-sha2-nistp256 E2VjZH...QUiCAk=
root@switch
| Switch#          | Show user <username> | authorized-key |     |     |
| ---------------- | -------------------- | -------------- | --- | --- |
| E2VjZH...QUiCAk= | root@switch          |                |     |     |
Allow List
TheSSHserveraccesscontrolcanbeimplementedwithanACLappliedtothecontrolplaneperVRF.A
mistakeintheconfigurationofthecontrol-planeACLappliedtothedefaultVRFmightblockother
networkprotocolssincetheACLinvolvesruleorderingandcandenyincomingpackets.TheSSHallow-
listfeatureenhancementsimplifiestheconfigurationandprotectsagainstunauthorizedSSHaccess.To
usethisfeature,configurealistofaddressesorprefixesthatwillbetheonlyhostsallowedtoconnectto
theSSHserversrunningonallVRFsoftheswitch.Bydefault,theallow-listisdisabledandanyhostis
allowedtoconnectgiventhecorrectauthenticationcriteria.Whentheallow-listisenabled,onlythe
hoststhatfallunderoneofthelistentriesmayconnectwiththecorrectauthenticationcriteria;allother
hostswillbedeniedtoattemptauthentication.
| switch(config)#        | ssh server    | allow-list      |     |     |
| ---------------------- | ------------- | --------------- | --- | --- |
| switch(config-ssh-al)# |               | ip 10.10.0.0/16 |     |     |
| switch(config-ssh-al)# |               | ipv6 fd10::0/64 |     |     |
| switch(config-ssh-al)# |               | enable          |     |     |
| Active SSH             | sessions will | be terminated.  |     |     |
| Do you want            | to continue   | (y/n)? y        |     |     |
switch(config-ssh-al)#exit
| switch(config)# | show        | ssh server allow-list |     |     |
| --------------- | ----------- | --------------------- | --- | --- |
| SSH server      | allow-list: |                       |     |     |
| Status:         | Enabled     |                       |     |     |
| Allowed         | host IPs:   |                       |     |     |
10.10.0.0/16
fd10::0/64
IftheACLisappliedtothecontrol-planeandtheSSHallow-listisalsoenabled,thecontrol-planeACLhaspre-
emptionovertheSSHallow-list.
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 29

| Recommended | Ciphers, | MACs, | and Algorithms |     |     |     |
| ----------- | -------- | ----- | -------------- | --- | --- | --- |
AOS-CXswitchesbydefaultsupportsthefollowingSSHCiphers,MACs,andAlgorithms:
| switch #    | show ssh      | server |                |               |       |           |
| ----------- | ------------- | ------ | -------------- | ------------- | ----- | --------- |
| SSH server  | configuration |        | on VRF default | :             |       |           |
| IP Version  |               | : IPv4 | and IPv6       | SSH Version   |       | : 2.0     |
| TCP Port    |               | : 22   |                | Grace Timeout | (sec) | : 60      |
| Max Auth    | Attempts      | : 6    |                | Server Status |       | : running |
| Allow-list: | disabled      |        |                |               |       |           |
Ciphers:
chacha20-poly1305@openssh.com, aes128-ctr, aes192-ctr, aes256-ctr,
| aes128-gcm@openssh.com, |               |                      | aes256-gcm@openssh.co |                      |     |     |
| ----------------------- | ------------- | -------------------- | --------------------- | -------------------- | --- | --- |
| Host Key                | Algorithms    |                      |                       |                      |     |     |
| ecdsa-sha2-nistp256,    |               | ecdsa-sha2-nistp384, |                       | ecdsa-sha2-nistp521, |     |     |
| ssh-ed25519,            | rsa-sha2-256, |                      | rsa-sha2-512,         | ssh-rsa              |     |     |
| Key Exchange            | Algorithms:   |                      |                       |                      |     |     |
curve25519-sha256, curve25519-sha256@libssh.org, ecdh-sha2-nistp256,
| ecdh-sha2-nistp384, |     | ecdh-sha2-nistp521 |     |     |     |     |
| ------------------- | --- | ------------------ | --- | --- | --- | --- |
MACs:
| hmac-sha2-256-etm@openssh.com, |     |     | hmac-sha2-512-etm@openssh.com, |     |     |     |
| ------------------------------ | --- | --- | ------------------------------ | --- | --- | --- |
hmac-sha1-etm@openssh.com, hmac-sha2-256, hmac-sha2-512, hmac-sha1
| Public Key                  | Algorithms:   |                      |                             |                      |     |     |
| --------------------------- | ------------- | -------------------- | --------------------------- | -------------------- | --- | --- |
| rsa-sha2-256,               | rsa-sha2-512, |                      | ssh-rsa,                    | ecdsa-sha2-nistp256, |     |     |
| ecdsa-sha2-nistp384,        |               | ecdsa-sha2-nistp521, |                             | ssh-ed25519,         |     |     |
| x509v3-rsa2048-sha256,      |               | x509v3-ssh-rsa,      |                             | x509v3-sign-rsa,     |     |     |
| x509v3-ecdsa-sha2-nistp256, |               |                      | x509v3-ecdsa-sha2-nistp384, |                      |     |     |
x509v3-ecdsa-sha2-nistp521
Thepreviouslymentioneddefaultciphers,messageauthenticationcodes(MACs),andalgorithmsare
basedonOpenSSH'sdefaultsettingsandaredeemedsecurebythecommunity.
ForhighlysecuredeploymentslikeFederalAccountswhichmandatesthecomplianceofNDcPP
(CommonCriteriaProtectionProfile),itisrecommendedtoconfigurethefollwoinglistofciphers,
MACs,andalgorithmsaspertheNDcPPevaluationcriteria.
switch(config)# ssh ciphers aes128-ctr, aes256-ctr, aes128-cbc, aes256-cbc
switch(config)# ssh macs hmac-sha2-256, hmac-sha2-512, hmac-sha1
switch(config)# ssh key-exchange-algorithms ecdh-sha2-nistp256, ecdh-sha2-
| nistp384, | diffie-hellman-group14-sha1 |     |     |     |     |     |
| --------- | --------------------------- | --- | --- | --- | --- | --- |
switch(config)# ssh host-key-algorithms ecdsa-sha2-nistp256, ecdsa-sha2-
nistp384,ecdsa-sha2-nistp521
switch(config)# ssh public-key-algorithms ecdsa-sha2-nistp256, ecdsa-sha2-
| nistp384, | ecdsa-sha2-nistp521 |     |     |     |     |     |
| --------- | ------------------- | --- | --- | --- | --- | --- |
IndividualalgorithmsareorderedandadvertisedtothepeerSSHdeviceasconfigured.Pleaseorderthe
algorithmsappropriatelytoensurethatdesiredpreferenceofalgorithms
| Server Port | Customization |     |     |     |     |     |
| ----------- | ------------- | --- | --- | --- | --- | --- |
Bydefault,SSHserverlistensonTCPport22.ThisportwillbeusedforallVRFsthathaveSSHserver
enabled.OptionallyAOS-CXswitchesprovidestheabilitytomodifythedefaultSSHserverporttoadd
extraprotectiontotheserver.SupportedPortnumberrangefrom1to65535.Althoughitispossibleto
useallports,itmightcauseanetworkconflict.Thus,itissafertochooseaportnumberwhichisnot
HardeningtheCXManagementplane|30

reservedforanyotherservice.Additionallyensurethefirewallisnotblockingtheportyouwanttouse
forSSH.
SampleconfigurationtomodifytheSSHserverport:
| switch(config)# |     | ssh server port | 19222 |     |
| --------------- | --- | --------------- | ----- | --- |
ThisportwillbeusedforallVRFsthathaveanSSHserverenabled.Ifthenewportiscurrentlyopenedbyanother
serviceonaVRF,theSSHserverwillgointoanerrorstateforthatVRF,andaneventlogmessagewillbelogged.
| Two Factor | Authentication |     | and Authorization |     |
| ---------- | -------------- | --- | ----------------- | --- |
TwofactorAuthenticationisanextralayerofprotectionusedtoguaranteethesecureaccessofswitch
managementinterfaceslikeSSHandHTTPS-Server.Intwo-factorauthentication,X.509certificate-based
authenticationiscombinedwithRadSecauthentication.Two-factorauthenticationcanbeperformed
locallyorremoteRadSecserver.Refersecurityguidefordetailedsteps.
FollowingtablesummarizestheTwofactorAuthenticationandAuthorizationsupportacrossdifferent
authenticationmethods–LocalandRemote-
Local +
| Task/Methods |     | Local Only |     | Remote Only |
| ------------ | --- | ---------- | --- | ----------- |
Remote
| SupportedManagement |     | SSH | SSH | SSHandHTTPS-Server |
| ------------------- | --- | --- | --- | ------------------ |
Interfaces
X.509Certificate Validatedusing Validated ValidatedusinglocallyconfiguredTAprofile
| Authentication |     | locallyconfiguredTA | usinglocally | inswitch |
| -------------- | --- | ------------------- | ------------ | -------- |
|                |     | profileinswitch     | configured   |          |
TAprofilein
switch
ValidationofUsername LocaluserAccounts Localuser RemoteRADIUSAuthorizeonlyrequest
| presentincertificate's |     |     | Accounts |     |
| ---------------------- | --- | --- | -------- | --- |
CommonNameor
SubjectAlternative
Name-UserPrincipal
Name
| Validationof-Username |     | LocaluserAccounts | Remote | NoValidation. |
| --------------------- | --- | ----------------- | ------ | ------------- |
| andPassword           |     |                   | Server |               |
| Authorization         |     | LocaluserAccount  | Remote | RemoteServer  |
Server
n AuthorizationrequestsaresentoverTLSandthereforeRADIUSauthorize-onlyrequiresaRadSec
RADIUSserver.ItshouldbesupportingAuthorizeonlyrequest.
n ForRemoteonlyauthentication,passwordisnotrequiredatthetimeofauthentication.
n YourswitchmanagementcomputerhasaccesstotheRESTAPIusinganappropriateHTTPSclient.
Thiscanbedonewithawebbrowser,usingtheWebUI,orotherHTTPsrequesttoolssuchas
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 31

Postman.UsageofFirefoxisnotrecommended,asitrequiresadditionalconfigurationtoworkwith
thisfeature.
Summary
ThefollowingtablesummarizesthemanagementaccessmethodsavailableonanAOS-CXSwitch,how
theyaresecuredbydefault,andthewaysinwhichtheycanbesecured.
| Access | Secured by |     | Other Hardening |
| ------ | ---------- | --- | --------------- |
Ways to Secure
| Method  | Default |                             | Recommendations          |
| ------- | ------- | --------------------------- | ------------------------ |
| Console | No      | EnableAAAthroughExternal    | •    LimitingShellAccess |
|         |         | TACACS+/RADIUS/RadSecserver | •    SessionManagement   |
orLocal(MandatoryFallback)
| Telnet | No  | EnableAAAthroughExternal | •    LimitingShellAccess |
| ------ | --- | ------------------------ | ------------------------ |
TACACS+/RADIUS/RadSecserver
•    SessionManagement
orLocal
•    ControlPlaneACLs
| SSH | No  | EnableAAAthroughExternal | •    LimitingShellAccess |
| --- | --- | ------------------------ | ------------------------ |
TACACS+/RADIUS/RadSecserver
•    SessionManagement
orLocal
•    HardeningSSH
•    ControlPlaneACLs
| WebUI | No  | EnableAuthenticationand | •    HardeningPKI |
| ----- | --- | ----------------------- | ----------------- |
AccountingthroughExternal
•    TLSEnforcements
TACACS+/RADIUS/RadSecserver
•    ControlPlaneACLs
orLocal.Authorizationis
supportedviaRBAC.
| RESTAPI | No  | EnableAuthenticationand | ControlPlaneACLs |
| ------- | --- | ----------------------- | ---------------- |
AccountingthroughExternal
TACACS+/RADIUS/RadSecserver
orLocal.Authorizationis
supportedviaRBAC
| SNMP               | No  | RefertoSecuringSNMPAccess | ControlPlaneACLs |
| ------------------ | --- | ------------------------- | ---------------- |
| Session Management |     |                           |                  |
SessionmanagementenhancessecuritybyenforcingspecificCLIusersessionrequirementsfor
console,SSHandtelnetconnections.Thefollowinginformationisprovidedatthetimeofasuccessful
login:
n Whenapplicable,thenumberoffailedloginattemptssincethemostrecentsuccessfullogin.
n Thedate,time,andlocation(consoleorIPaddressorhostname)ofthemostrecentprevious
successfullogin.
n Thecountofsuccessfulloginswithinthepast(configurable)timeperiod.
HardeningtheCXManagementplane|32

ThefollowingexampleconfiguresCLIusersessionsettingsforamaximumofoneconcurrentsession
witha15-minutetimeout,andtrackingforamaximumof25days
| switch(config)#             |      | cli-session    |     |
| --------------------------- | ---- | -------------- | --- |
| switch(config-cli-session)# |      | max-per-user   | 1   |
| switch(config-cli-session)# |      | timeout        | 15  |
| switch(config-cli-session)# |      | tracking-range | 25  |
| switch#                     | exit |                |     |
Itisrecommendedtoconfigureatleastfivetotenminutesoftimeoutforsensitivenetworks.Fornon-
sensitivenetworks,a15minutetimeoutisrecommended.
Whenthesameusernameisusedforbothlocalandremoteauthentication,bothusers,regardlessof
privilegelevel,areconsideredtobethesameuserforthepurposeofcountingconcurrentCLIsessions.
Forexample,withmax-per-uservaluesetto1anduseradmin1configuredforlocalandremote
authentication,onlythelocaluseradmin1ortheremoteuseradmin1canbeloggedinatanygiven
moment.Bothadmin1userscannotbeloggedinsimultaneouslyunlessthemax-per-uservalueis
increasedtoatleast2.
| Limiting | Shell | Access |     |
| -------- | ----- | ------ | --- |
TheAOS-CXoperatingsystemprovidesaccesstotheunderlyingLinuxsystem,allowingadministrators
tolaunchabashshellsessionfromtheswitchcommand-lineinterface.Misuseofshellaccesscould
exposesensitivenetworktraffictoanunauthorizedthirdpartyviapacketmirroringtoaremotedevice
orcouldcauseadenialofservicebymodifyingorremovingsystemfiles.Thisfilemodificationcould
renderthedeviceunbootable,andrequiresoftwarerestorationthroughtheServiceOSconsole..
Thefollowingarebestpracticesforlimitingshellaccess:
n DisableaccesstotheBashshellbychangingtheswitchsecuritymodetoenhancedfromServiceOS.
n LimitshellaccessbyusingRBACoranexternalTACACS+authorizationservertodenyaccesstothe
start-shellcommandtoallusersexceptthosewhospecificallyrequireit.
| Securing | SNMP | Access |     |
| -------- | ---- | ------ | --- |
SNMPisusedtomanageandmonitornetworkeddevicesfromacentralizedplatform.Therearethree
versionsoftheSNMPprotocol:v1,v2c,andv3.SNMPv1andv2cusecommunitynamesforreadand
writeaccess.Muchlikepasswordsareusedforauthentication,thesecommunitynamesaresentacross
thewireascleartext.Ifamalicioususerweretocapturethesecommunitynames,theycouldpotentially
issueSNMPsetcommandstomakeunauthorizedandpotentiallyharmfulconfigurationchangestoa
networkdevice.SNMPv3,bycomparison,utilizesauser-basedsecuritymodelwithbothauthentication
andprivacyprotocolstopreventunauthorizedaccessoreavesdroppingofmanagementtraffic.
SNMPisdisabledbydefaultonallAOS-CXdevices.Whenenabled,SNMPprovideslimitedwritesupport
inadditiontoread-onlyaccessandtrapsupportforSNMPv1,v2c,andv3.
ThedefaultSNMPcommunitystringispublic,acommonsettingforSNMP-capabledevices.Replacethe
publiccommunitystringwithanothervaluethatishardtoguess,butnotethatthisdoesn’tfully
preventagainstattacksasthisstringisincleartextformatinpacketcaptures:
| Switch(config)# |     | snmp-server community | zerotrust |
| --------------- | --- | --------------------- | --------- |
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 33

ThedefaultaccesslevelforSNMPcommunitiesisread-only;ifread-writesupportisrequired,setthe
accesslevelforthecommunitytorwfromthecommunitycontext.IPv4and/orIPv6ACLsmaybeused
tolimitaccesstoallowedmanagementstationsorsubnets;onlyoneACL(IPv4orIPv6)maybeapplied
toacommunityatatime.ApplyanIPv4orIPv6ACLfromtheSNMPconfig-communitycontext.
| switch(config)#           | snmp-server |           | community    | zerotrust |     |     |
| ------------------------- | ----------- | --------- | ------------ | --------- | --- | --- |
| switch(config-community)# |             |           | access-level | rw        |     |     |
| switch(config-community)# |             |           | access-list  | snmp_acl  |     |     |
| switch # show             | snmp        | community |              |           |     |     |
----------------------------------------------------------------------------------
| Community |     |     | Access-level | ACL Name | ACL Type | View |
| --------- | --- | --- | ------------ | -------- | -------- | ---- |
----------------------------------------------------------------------------------
| zerotrust |     |     | rw  | snmp_acl | ipv4 | none |
| --------- | --- | --- | --- | -------- | ---- | ---- |
BestpracticesistouseSNMPv3insteadofolderversionsofSNMP.OlderversionsofSNMPare
unauthenticatedandunencrypted,withthecommunitystringactingasapassword,transmittedin
plaintext.SNMPv3,offerssupportfordifferentusers,authentication,andstrongencryption.AOS-CX
supportsstrongerauthenticationprotocols(SHA224,SHA256,SHA384,andSHA512)andprivacy
protocols(AES192andAES256).
TocreateanSNMPv3userusingSHAforauthenticationandDESforprivacy:
switch(config)# snmpv3 user myUser auth sha auth-pass plaintext myAuthPswrd priv
| des priv-pass | plaintext |     | myPrivPswrd |     |     |     |
| ------------- | --------- | --- | ----------- | --- | --- | --- |
ThefollowingexamplecreatesanSNMPv3contextwiththecommunitynamecreatedaboveand
assignedtothemgmtVRF:
switch(config)# snmpv3 context snmpv3mgmt vrf mgmt community zerotrust
DisablesupportforSNMPv1andSNMPv2candonlyacceptSNMPv3messagesusingthefollowing
command:
| switch(config)# | snmp-server |     | snmpv3-only |     |     |     |
| --------------- | ----------- | --- | ----------- | --- | --- | --- |
ToenableSNMPonthemgmtVRF:
| switch(config)# | snmp-server |         | vrf mgmt |     |     |     |
| --------------- | ----------- | ------- | -------- | --- | --- | --- |
| switch# show    | snmpv3      | context |          |     |     |     |
----------------------------------------------------------------------------------
| Name |     | vrf |     | Community | Type[Instance_id] |     |
| ---- | --- | --- | --- | --------- | ----------------- | --- |
----------------------------------------------------------------------------------
| snmpv3mgmt   |        | mgmt  |     | zerotrust | vrf |     |
| ------------ | ------ | ----- | --- | --------- | --- | --- |
| switch# show | snmpv3 | users |     |           |     |     |
----------------------------------------------------------------------------------
| User |     | AuthMode | PrivMode | Status Context | Access-level | View |
| ---- | --- | -------- | -------- | -------------- | ------------ | ---- |
----------------------------------------------------------------------------------
HardeningtheCXManagementplane|34

| myUser        |      | sha | des | Enabled | none | ro  | none |
| ------------- | ---- | --- | --- | ------- | ---- | --- | ---- |
| Control Plane | ACLs |     |     |         |      |     |      |
OnceanIPaddressisboundtoaninterfaceassociatedwithaVRF,theswitchmaybecomeexposedto
managementaccessfromuntrustedusersordevices.Thispotentialpointofvulnerabilitycanbe
mitigatedbybindinganAccessControlList(ACL)tothecontrolplaneforthatVRF.Thecontrolplane
handlesthedevice'smanagementandroutingfunctionality.
OnceacontrolplaneACLisappliedtoaVRF,itfilterspacketstoallIPv4/IPv6addressesboundtothe
deviceonthatVRF.ItispossibletocreateacontrolplaneACLforeachexistingVRF,includingthemgmt
VRF.
ThefollowingcommandsareanexampleofanACLanadministratorcanapplythatlimitsSSHand
SNMPcontrolplaneaccesstosourcedeviceswithIPaddressesinthe10.10.0.0/24subnet,withcounters
fordeniedSSHandSNMPpackets.
| switch(config)# | access-list | ip  | CONTROLPLANE |     |     |     |     |
| --------------- | ----------- | --- | ------------ | --- | --- | --- | --- |
switch(config-acl-ip)# 05 comment ALLOW SSH AND SNMP ON ADMIN SUBNET, BLOCK ALL
OTHERS
| switch(config-acl-ip)# |     | 10 permit   | tcp     | 10.10.0.0/24 | any eq 22  |     |     |
| ---------------------- | --- | ----------- | ------- | ------------ | ---------- | --- | --- |
| switch(config-acl-ip)# |     | 20 permit   | udp     | 10.10.0.0/24 | any eq 161 |     |     |
| switch(config-acl-ip)# |     | 30 permit   | udp     | 10.10.0.0/24 | any eq 162 |     |     |
| switch(config-acl-ip)# |     | 40 deny     | tcp any | any eq 22    | log count  |     |     |
| switch(config-acl-ip)# |     | 50 deny     | udp any | any eq 161   | log count  |     |     |
| switch(config-acl-ip)# |     | 60 deny     | udp any | any eq 162   | log count  |     |     |
| switch(config-acl-ip)# |     | 990 comment | ALLOW   | ANYTHING     | ELSE       |     |     |
| switch(config-acl-ip)# |     | 1000 permit | any     | any any      |            |     |     |
EventlogsforControlPlaneACEissupportedusingthelogkeyword.Thisoptionoffersbettertroubleshooting
andvisibilityofanACLappliedtothecontrolplane.
ToapplythisACLtothedefaultVRF:
switch(config)# apply access-list ip CONTROLPLANE control-plane vrf default
AllACLsinAOS-CXhaveanimplicitdeny anyruleattheendoftheruleslist.Thisrequiresthatallowed
trafficbeexplicitlypermittedtopassthroughanappliedACL.Intheaboveexample,SSHandSNMP
trafficonports22isallowedfrom10.10.0.0/24.TheSSHandSNMPtrafficisthenblockedfromany
othersubnets.ThefinalACLentry(permit any any any)permitsallothertraffic.
Time Synchronization
Manysecureprotocolsandauditingfunctionsrelyonsystemtimesbeingsynchronizedwithareliable
timesource,eitherwithinor(wheresecurityconsiderationspermit)externaltothemanagednetwork.
Oneofthemostcommonly-usedprotocolstoaccomplishthisistheNetworkTimeProtocol(NTP),which
canusebothlocalandInternet-hostedserverstosynchronizesystemtimeacrossanetwork.
Recommendation-NTPshouldbeconfiguredandenabledonthedevicepriortoenablingsecure
managementprotocols.
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 35

AcommonpracticeamongorganizationsthatspanmultipletimezonesistouseNTPtosynchronize
timeclocksandsetthelocaltimezoneonallequipmenttoUTC.Thispracticeaidsintroubleshooting
andsecurityauditsfordevicesthatmightbecontinentsapart.BothIPv4andIPv6Serversare
supported.
ToconfigureaswitchtouseNTPauthenticationandconnecttoalocalNTPserverat10.100.1.254using
theswitchmanagementport:
| switch(config)# |          | ntp authentication     |              |        |            |     |
| --------------- | -------- | ---------------------- | ------------ | ------ | ---------- | --- |
| switch(config)# |          | ntp authentication-key |              | 1 md5  | ntpauthkey |     |
| switch(config)# |          | ntp server             | 10.100.1.254 | prefer |            |     |
| switch(config)# |          | ntp vrf                | mgmt         |        |            |     |
| switch#         | show ntp | servers                |              |        |            |     |
------------------------------------------------
| NTP SERVER |     | KEYID | MINPOLL | MAXPOLL OPTION | VER |     |
| ---------- | --- | ----- | ------- | -------------- | --- | --- |
------------------------------------------------
| 10.100.1.254 |     | --  | 6   | 10 none   | 4 prefer       |     |
| ------------ | --- | --- | --- | --------- | -------------- | --- |
| 10.80.2.219  |     | --  | 6   | 10 iburst | 4 prefer(auto) |     |
| pool.ntp.org |     | --  | 4   | 4 iburst  | 4              |     |
------------------------------------------------
| switch# | show ntp | authentication-keys |     |     |     |     |
| ------- | -------- | ------------------- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
| Key ID | Trusted | Type | Encrypted | Key |     |     |
| ------ | ------- | ---- | --------- | --- | --- | --- |
----------------------------------------------------------------------------------
| 1   | No  | MD5 | AQBapUtt1YTjZS2PH4+J7G5OKJG0GuZ2WxmD0339TNg6nfGXY= |     |     |     |
| --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
-------------------------------------------------------------------------------
| switch#            | show ntp    | status  |             |                |             |            |
| ------------------ | ----------- | ------- | ----------- | -------------- | ----------- | ---------- |
| NTP Status         | Information |         |             |                |             |            |
| NTP                |             |         | : Enabled   |                |             |            |
| NTP DHCP           |             |         | : Enabled   |                |             |            |
| NTP Authentication |             |         | : Enabled   |                |             |            |
| NTP Server         | Connections |         | : Using     | the mgmt       | VRF         |            |
| System time        |             |         | : Fri       | Mar 8 03:51:46 | PST 2024    |            |
| NTP uptime         |             |         | : 8 days,   | 15 hours,      | 24 minutes, | 37 seconds |
| Not synchronized   |             | with an | NTP server. |                |             |            |
Secure Copy
ThecopycommandiswidelyusedinAOS-CXswitchestotransferfiles,configurationsandlog
messages.ThecommonlyusedfiletransferprotocolTFTPtransfersfilesinplaintext,soattackerscan
easilycapturetransferredpackets.Toprotectthedeviceagainstsecuritythreats,itisrecommendedto
useSFTPandSCPtoperformthecopyoperations.
| Hardening | PKI |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- |
ThePublicKeyInfrastructure(PKI)featureenablesadministratorstomanagedigitalcertificatesonthe
switch.Theswitchusescertificatestovalidateclientswhenactingasaserver,andwhencommunicating
withserverswhenTLSencryptionisused.
TheAOS-CXSwitchSeriessupportstheinstallationofcertificateauthority(CA)certificatesandthe
generationandinstallationofleafcertificates.Theswitchsupports64trustanchor(TA)profiles.EachTA
HardeningtheCXManagementplane|36

profile stores a trusted CA certificate. The certificate can be either a root CA certificate, which must be
self-signed, or an intermediate CA certificate that is issued by another CA. The TA profile also enables
configuration of real-time checking of certificate revocation (through OCSP).

Leaf certificates can be installed on the switch for use by applications such as:

n RadSec Client

n dot1x-supplicant

n EST Client

n captive-portal

n syslog client

n https-server - Web UI or REST API

AOS-CX switches by default supports the following preinstalled leaf certificates:

n local-cert: A self-signed certificate that switch automatically generated at first boot, as the default

certificate for any application when the application's associated certificate is not configured

n device-identity: A device-identity certificate built into a switch at manufacturing and resident for the
life of the product. The identity is a combination of an RSA key pair with physical information such as
the unit's model, chassis/PCA serial number, and base MAC ID. Device Identity will be used for
following purposes:

o Allow 801.2X-2010 to perform peer authentication without the need for certificate or pre-shared
key installation to automate the formation of MACsec secure channels between neighbor devices.

o Authentication with HPE Aruba Networking cloud services.

switch # show crypto pki certificate
Certificate Name
Cert Status
------------------------ ---------------- ----------- --------------------
local-cert
captive-portal, dot1x
supplicant, est-client, https-server, radsec-client, syslog-client
device-identity

EST Status

installed

installed

none

n/a

n/a

Associated Applications

AOS-CX recommends the usage of trusted CA signed certificate over the self-signed certificate for all the

applications to avoid potential security risks.

If you are purchasing a certificate from a trusted CA, the switch can generate the certificate signing
request (CSR) that is used to request the certificate. The switch can also directly generate self-signed
certificates. Alternatively, the certificate and private key can be generated outside the switch and then
imported. X509 certificate management software such as OpenSSL can be used to generate the private
key and CSR and then combine the certificate and private key into one PEM or PKCS#12 file suitable for
import into the switch.

The following procedure describes how to create and install an X.509 leaf certificate that is initiated
inside the switch but signed outside the switch by a Certificate Authority.

switch(config)# crypto pki ta-profile root-cert
switch(config-ta-root-cert)# revocation-check ocsp
switch(config-ta-root-cert)# ocsp url primary http://ocsp-server.site.com
switch(config-ta-root-cert)# ocsp url secondary http://ocsp-server2.site.com
switch(config-ta-root-cert)# ta-certificate import terminal
Paste the certificate in PEM format below, then hit enter and ctrl-D:
switch(config-ta-cert)# -----BEGIN CERTIFICATE-----

AOS-CX 10.14.1000 Hardening Guide | (All Switch Series)

37

switch(config-ta-cert)# MIIDuTCCAqECCQCuoxeJ2ZNYcjANBgkqhkiG9w0BAQsFADCBqzELMAEBh
switch(config-ta-cert)# VVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEDAOBgNVBAcMB1JvY2tsDAKBg
switch(config-ta-cert)# BAoMA0hQTjEVMBMGA1UECwwMSFBOUm9zZXZpbGxlMSowKAYDVQocG5zdz
switch(config-ta-cert)# x3WFf3dFZ8o9sd5LVAHneH/ztb9MP34z+le1V346r12L2kpxmTOVJVyTO
switch(config-ta-cert)# BIzD/ST/HaWI+0S+S80rm93PSscEbb9GWk7vshh5EnW/moehBKcE4O1zy
switch(config-ta-cert)# 3LvMLZcssSe5J2Ca2XIhfDme8UaNZ7syGYMsAW0nG7yYHWkEOQu9s
| switch(config-ta-cert)# |     |     |     | -----END | CERTIFICATE----- |     |     |     |
| ----------------------- | --- | --- | --- | -------- | ---------------- | --- | --- | --- |
switch(config-ta-cert)#
The certificate you are importing has the following attributes:
| Issuer: | C=US, | ST=CA, | L=Rocklin, |     | O=Company, |     | OU=Site, |     |
| ------- | ----- | ------ | ---------- | --- | ---------- | --- | -------- | --- |
CN=site.com/emailAddress=test.ca@site.com
| Subject: | C=US, | ST=CA, | L=Rocklin, |     | O=Company, |     | OU=Site, |     |
| -------- | ----- | ------ | ---------- | --- | ---------- | --- | -------- | --- |
CN=8400/emailAddress=test.ca@site.com
| Serial Number:               |     | 12121221634631568498 |      |             |      | (0xaea51217d5945772) |     |              |
| ---------------------------- | --- | -------------------- | ---- | ----------- | ---- | -------------------- | --- | ------------ |
| TA certificate               |     | import               | is   | allowed     | only | once                 | for | a TA profile |
| Do you want                  | to  | accept               | this | certificate |      | (y/n)?               |     | y            |
| TA certificate               |     | accepted.            |      |             |      |                      |     |              |
| switch(config-ta-root-cert)# |     |                      |      |             | exit |                      |     |              |
| switch(config)#              |     | crypto               | pki  | certificate |      | lcert                |     |              |
switch(config-cert-lcert)# subject common-name Leaf country US state CA
| locality                   | Rocklin   | org    | Company     |          | org-unit   | Site |           |             |
| -------------------------- | --------- | ------ | ----------- | -------- | ---------- | ---- | --------- | ----------- |
| switch(config-cert-lcert)# |           |        |             | key-type |            | rsa  | key-size  | 3072        |
| switch(config-cert-lcert)# |           |        |             | enroll   | terminal   |      |           |             |
| You are                    | enrolling | a      | certificate |          | with       | the  | following | attributes: |
| Subject:                   | C=US,     | ST=CA, | L=Rocklin,  |          | O=Company, |      | OU=Site   |             |
CN=Leaf
| Key Type:  | RSA         | (2048) |              |     |     |     |     |     |
| ---------- | ----------- | ------ | ------------ | --- | --- | --- | --- | --- |
| Continue   | (y/n)?      | y      |              |     |     |     |     |     |
| -----BEGIN | CERTIFICATE |        | REQUEST----- |     |     |     |     |     |
MIIBozCCAQwCAQAwYzEVMBMGA1UEAxMMcG9kMDEtODQwMC0xMQ4wDAYDV
nViYTEMMAoGA1UEChMDSFBFMRIwEAYDVQQHEwlSb3NldmlsbGUxCzAJBg
NBMQswCQYDVQQGEwJVUzCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYE
...
GBAJ4L3lFFfWBEL+KAKpOGjZcVmwlBMqSKFtOFNF9nzmUmONmU3SKy6dz
7Au22mf3lWDxzrtCC/dj5RtWJeJekxp2LCIK/3eRXUwbYveQDKcxH7j9Z
ace+2tA68F2vlgRCQ/hcQH0YmNuaq4Ne3w0dhm7HlUrx
| -----END | CERTIFICATE |     | REQUEST----- |     |     |     |     |     |
| -------- | ----------- | --- | ------------ | --- | --- | --- | --- | --- |
switch(config-cert-lcert)# import terminal ta-profile root-cert
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-cert-import)# |     |     |     | -----BEGIN |     | CERTIFICATE----- |     |     |
| --------------------------- | --- | --- | --- | ---------- | --- | ---------------- | --- | --- |
switch(config-cert-import)# MIIFRDCCAyygwIBAgIQPnnS2Vp5u07XMdktDJzANBgkqhkiG9w0Bv
switch(config-cert-import)# MQswCQYDVQGEwJVEOMAwG1UECgwFJ1YmxDAOgNBMMB1Jvb3QgQ0Ew
switch(config-cert-import)# HhcNMTkNDEwMjIwNTWcjIwMTA0MjwNE1WBzQswQYDVQQGEwJVUzEL
...
switch(config-cert-import)# 1fIYZYGQyla0AwFuTTxBXYwRxPbUYU5tumrfwRPmE4OVY8S9DQgcr
switch(config-cert-import)# 1NGNm3NG03GqPcs/T9bVyF5BOrS5lmm7kNfRYl8D/kMTfRreSdxis
| switch(config-cert-import)# |     |     |     | YQ1u1NqShps= |     |                  |     |     |
| --------------------------- | --- | --- | --- | ------------ | --- | ---------------- | --- | --- |
| switch(config-cert-import)# |     |     |     | -----END     |     | CERTIFICATE----- |     |     |
switch(config-cert-import)#
Leaf certificate is validated with root-cert and imported successfully.
| switch(config-cert-lcert)# |     |     |     | exit |     |     |     |     |
| -------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- |
switch(config)# crypto pki application syslog-client certificate lcert
| Mandatory | matching |     |     | of peer |     | device | hostname |     |
| --------- | -------- | --- | --- | ------- | --- | ------ | -------- | --- |
Toenhancetheserver-sidecertificateverification,theAOS-CXswitchchecksthatthepeerdevice
configuredhostnamematcheseithertheSubjectAlternativeName(SAN)fieldortheCommonName
HardeningtheCXManagementplane|38

(CN) within the certificate Subject field. If the SAN field is present and matches the hostname, validation
succeeds, otherwise it fails. If the SAN field is not present, and the CN matches the hostname, validation
succeeds, otherwise it fails.

EST

EST stands for Enrolment over Secure Transport; An EST client is implemented as a part of the PKI
infrastructure in the AOS-CX switches. Switches can be configured to request the trusted CA certificates
and to request enrolment/reenrolment of leaf certificates automatically, without the need for
administrator intervention, while maintaining the security and integrity of the whole enrolment process.

Refer the PKI EST section in Security Guide for more information.

TLS Enforcements

Minimum TLS version supported in AOS-CX switches is TLS1.2. The following are recommended cipher
suites for TLS Applications/Protocols

n TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

n TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

n TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256

n TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384

The Extended Key Usage X.509 v3 extension defines one or more purposes for which the public key can
be used. This is in addition to or in place of the basic purposes specified by the Key Usage extension. As
per NDcPP recommendation , that a peer certificate being used to establish TLS connection must have
its extended key usage field set as client-auth or server-auth, depending on its role of the peer device.
This configuration enables the checking of key usage during TLS handshake. It is disabled by default

switch(config)# tls check-key-usage

switch# show tls
TLS crypto algorithms state:
:
TLS key usage checking

default
on

Secure Logging

AOS-CX Switch provides both locally stored event and security logs, as well as using the syslog protocol
to forward events to a remote IPv4/IPv6 syslog server for auditing purposes. Logged events can be
filtered by severity level, originating system modules, or using regular expressions to match against
message text.

When configuring AOS-CX to send logs to a remote server, it is common practice to set a facility value.
This value acts as a label that the remote server can use to determine which file the syslog message
should get appended.

Below is an example of how to configure AOS-CX to send event log messages via syslog to a remote
server. This example uses the default facility of local7 and sends event messages marked informational
and higher:

switch(config)# logging 10.100.1.250 vrf mgmt

AOS-CX 10.14.1000 Hardening Guide | (All Switch Series)

39

Toincludesecurity-relatedaccountinglogsinadditiontotheeventlogs,thenaddtheinclude-auditable-
eventsoptiontotheconfiguration:
switch(config)# logging 10.100.1.250 include-auditable-events vrf mgmt
ThesyslogclientcanconnecttoaserverusingUDP(default),TCP,orTLSprotocols.TLSisthe
recommendedprotocol,asitprovidesanencryptedconnectiontothesyslogreceiver.Thisrequiresthe
switchtopossessasignedTLSclientcertificate,andthereceivertopossessasignedTLSserver
certificate.TheprocessofrequestingandinstallingasignedTLSclientcertificateforsyslogissimilarto
thatforrequestingandinstallinganSSL/TLScertificateforweb-management.
| Hardening | the | Control | Plane |     |     |     |
| --------- | --- | ------- | ----- | --- | --- | --- |
Thefollowingsectionsdescribestrategiesforsecuringandhardeningtheswitchcontrolplane
| Control Plane | Policing |     |     |     |     |     |
| ------------- | -------- | --- | --- | --- | --- | --- |
ControlPlanePolicingpreventsfloodingofcertaintypesofpacketsfromoverloadingtheswitchor
moduleCPUbyeitherrate-limitingordroppingpackets.
Theswitchsoftwareprovidesseveralconfigurableclassesofpacketsthatcanberate-limited,including
(butnotlimitedto)ARPbroadcasts,multicast,routingprotocols(BGP,OSPF),andspanningtree.CoPPis
alwaysactiveandcannotbedisabled.
ThefollowingdefaultCoPPpolicyappliesthefollowingtrafficclassdefinitionsandratelimits(inpackets
persecond)on6300seriesswitchseries:
| switch# show | copp-policy | default       |          |            |          |          |
| ------------ | ----------- | ------------- | -------- | ---------- | -------- | -------- |
| class        |             | drop priority | rate pps | burst pkts | hardware | rate pps |
--------------------- ---- -------- -------- ---------- -----------------
| acl-logging         |     | 0   | 25   | 25   | 25   |     |
| ------------------- | --- | --- | ---- | ---- | ---- | --- |
| arp-broadcast       |     | 2   | 1250 | 1250 | 1250 |     |
| arp-protect         |     | 2   | 2075 | 2075 | 2075 |     |
| arp-unicast         |     | 3   | 825  | 825  | 825  |     |
| bfd-control         |     | 5   | 850  | 850  | 850  |     |
| bgp                 |     | 5   | 750  | 750  | 750  |     |
| captive-portal      |     | 2   | 2075 | 259  | 2075 |     |
| client-onboard      |     | 5   | 1024 | 1024 | 1000 |     |
| dfp-collector       |     | 0   | 512  | 512  | 500  |     |
| dhcp                |     | 2   | 750  | 750  | 750  |     |
| erps                |     | 6   | 225  | 225  | 225  |     |
| fib-optimization    |     | 0   | 100  | 200  | 100  |     |
| icmp-broadcast-ipv4 |     | 2   | 325  | 325  | 325  |     |
| icmp-multicast-ipv6 |     | 2   | 475  | 475  | 475  |     |
| icmp-security-ipv6  |     | 2   | 325  | 325  | 325  |     |
| icmp-unicast-ipv4   |     | 3   | 225  | 225  | 225  |     |
| icmp-unicast-ipv6   |     | 3   | 400  | 400  | 400  |     |
| ieee-8021x          |     | 2   | 2075 | 259  | 2075 |     |
| igmp                |     | 4   | 1600 | 450  | 1600 |     |
| ip-exceptions       |     | 0   | 100  | 100  | 100  |     |
| ip-lockdown         |     | 0   | 100  | 100  | 100  |     |
| ip-tracker          |     | 0   | 256  | 256  | 250  |     |
| ipfix               |     | 0   | 2500 | 2500 | 2500 |     |
| ipsec               |     | 5   | 1025 | 128  | 1025 |     |
| ipv4-options        |     | 1   | 100  | 100  | 100  |     |
| lacp                |     | 5   | 2050 | 2050 | 2050 |     |
HardeningtheControlPlane|40

| lldp                  |     |     | 5   |     | 100  | 100  | 100  |     |
| --------------------- | --- | --- | --- | --- | ---- | ---- | ---- | --- |
| loop-protect          |     |     | 6   |     | 225  | 225  | 225  |     |
| mac-lockout           |     |     | 0   |     | 100  | 100  | 100  |     |
| manageability         |     |     | 4   |     | 4218 | 4218 | 4200 |     |
| mdns                  |     |     | 2   |     | 150  | 150  | 150  |     |
| mirror-to-cpu         |     |     | 0   |     | 100  | 100  | 100  |     |
| mld                   |     |     | 4   |     | 1600 | 450  | 1600 |     |
| mvrp                  |     |     | 5   |     | 225  | 225  | 225  |     |
| nae-packet-monitor    |     |     | 0   |     | 100  | 200  | 0    |     |
| ntp                   |     |     | 4   |     | 100  | 100  | 100  |     |
| ospf-multicast        |     |     | 5   |     | 1025 | 1025 | 1025 |     |
| ospf-unicast          |     |     | 5   |     | 1025 | 1025 | 1025 |     |
| pim                   |     |     | 5   |     | 1700 | 1700 | 1700 |     |
| ptp                   |     |     | 5   |     | 1000 | 250  | 1000 |     |
| secure-learn          |     |     | 2   |     | 2075 | 259  | 2075 |     |
| sflow                 |     |     | 1   |     | 1000 | 125  | 1000 |     |
| stp                   |     |     | 6   |     | 2000 | 2000 | 2000 |     |
| udld                  |     |     | 6   |     | 450  | 450  | 450  |     |
| unknown-multicast     |     |     | 1   |     | 1025 | 128  | 1025 |     |
| unresolved-ip-unicast |     |     | 1   |     | 325  | 325  | 325  |     |
| vrrp                  |     |     | 4   |     | 400  | 400  | 400  |     |
| default               |     |     | 2   |     | 4225 | 528  | 4225 |     |
ThedefaultCoPPpolicycanbemodifiedbutcannotbedeleted.
TorevertamodifieddefaultCoPPpolicytofactorydefaultsettings:
| switch(config)# |     | copp-policy |     | default | revert |     |     |     |
| --------------- | --- | ----------- | --- | ------- | ------ | --- | --- | --- |
Administratorsmaycreateupto32customCoPPpolicies,thoughonlyonecanbeactiveatanygiven
time.
TocreateandapplyasimplecustomCoPPpolicy:
| switch(config)# |     | copp-policy |     | copp_policy_01 |     |     |     |     |
| --------------- | --- | ----------- | --- | -------------- | --- | --- | --- | --- |
switch(config-copp)#
|     |     |     | class arp-broadcast |     | priority |     | 2 rate 1000 | burst 1000 |
| --- | --- | --- | ------------------- | --- | -------- | --- | ----------- | ---------- |
switch(config-copp)# class unknown-multicast priority 2 rate 1000 burst 1000
switch(config-copp)# class unresolved-ip-unicast priority 2 rate 1000 burst 1000
switch(config-copp)# default-class priority 1 rate 3000 burst 3000
| switch(config-copp)# |     |       | exit        |     |                |     |     |     |
| -------------------- | --- | ----- | ----------- | --- | -------------- | --- | --- | --- |
| switch(config)#      |     | apply | copp-policy |     | copp_policy_01 |     |     |     |
ToremoveacustomCoPPpolicyfromserviceandautomaticallyapplythedefaultpolicy
| switch(config)# |     | no apply | copp-policy |     | copp_policy_01 |     |     |     |
| --------------- | --- | -------- | ----------- | --- | -------------- | --- | --- | --- |
TodeleteacustomCoPPpolicy:
| switch(config)# |     | no copp-policy |     | copp_policy_01 |     |     |     |     |
| --------------- | --- | -------------- | --- | -------------- | --- | --- | --- | --- |
AnactivecustomCoPPpolicycannotbedeleted;itmustfirstberemovedfromserviceusingtheabove
command.
| Securing | Spanning |     | Tree |     |     |     |     |     |
| -------- | -------- | --- | ---- | --- | --- | --- | --- | --- |
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 41

ThefollowingsectionsdescribesecurityandhardeningworkflowsforSpanningTree.
BPDU Protection
Varioussecuritymechanismsareinplacetoprotectspanningtrueconfigurationsfrominterferenceand
roguedevicesorunwarrantedchangestothenetwork.BPDUprotectionsecurestheactivetopologyby
preventingspoofedBPDUpacketsfromenteringthenetwork.Typically,BPDUprotectionisappliedon
edgeportsconnectedtoenduserdevicesthatdonotrunSTP.IfSTPBPDUpacketsarereceivedona
protectedport,BPDUguarddisablestheportandanalertissent.HencerecommendedtoenableBPDU
guardonenduser/deviceconnectedportstopreventanyinadvertentspanningtreeormaliciousattack.
| switch(config)#    |     | interface   | 1/1/8 |     |     |
| ------------------ | --- | ----------- | ----- | --- | --- |
| switch(config-if)# |     | no shutdown |       |     |     |
switch(config-if)#
no routing
| switch(config-if)# |     | vlan          | access | 10         |     |
| ------------------ | --- | ------------- | ------ | ---------- | --- |
| switch(config-if)# |     | spanning-tree |        | bpdu-guard |     |
| switch(config-if)# |     | exit          |        |            |     |
Root Protection
Rootprotectionsecurestheactivetopologybypreventingotherswitchesfromdeclaringtheirabilityto
propagatesuperiorBPDUs,containingbothbetterinformationontherootbridgeandpathcosttothe
rootbridgewhichwouldnormallyreplacethecurrentrootbridgeselection.Thisistypicallycarriedout
betweenthecorethatisrequiredtobetherootandaccessswitchestopreventportsthatarenot
expectedtooriginaterootinformationsuchasserverportsandaccessswitchports.
| switch(config)#    |     | interface   | 1/1/8 |     |     |
| ------------------ | --- | ----------- | ----- | --- | --- |
| switch(config-if)# |     | no shutdown |       |     |     |
switch(config-if)#
no routing
| switch(config-if)# |     | vlan          | access | 10         |     |
| ------------------ | --- | ------------- | ------ | ---------- | --- |
| switch(config-if)# |     | spanning-tree |        | root-guard |     |
| switch(config-if)# |     | exit          |        |            |     |
Viewingtheconfigurationchange:
| switch#      | show  | spanning-tree | interface |               | 1/1/3    |
| ------------ | ----- | ------------- | --------- | ------------- | -------- |
| Port         |       |               | :         | 1/1/3         |          |
| Admin State  |       |               | :         | up            |          |
| BPDU Guard   |       |               | :         | enabled       |          |
| BPDU Filter  |       |               | :         | disabled      |          |
| RPVST Guard  |       |               | :         | disabled      |          |
| RPVST Filter |       |               | :         | disabled      |          |
| Loop Guard   |       |               | :         | disabled      |          |
| Root Guard   |       |               | :         | enabled       |          |
| TCN Guard    |       |               | :         | disabled      |          |
| Admin Edge   | Port  |               | :         | admin-network |          |
| Link Type    |       |               | :         | Point         | to Point |
| BPDU Tx      | Count |               | :         | 31            |          |
| BPDU Rx      | Count |               | :         | 0             |          |
| TCN Tx Count |       |               | :         | 0             |          |
| TCN Rx Count |       |               | :         | 0             |          |
DHCP Security
ThefollowingsectionsdescribesecurityandhardeningworkflowsforDHCP.
HardeningtheControlPlane|42

DHCP Snooping
DHCPsnoopingprotectsthenetworkfromcommonDHCPattacks,includingaddressspoofingresulting
fromarogueDHCPserveroperatingonthenetworkorexhaustionofaddressesonaDHCPserver
causedbymassaddressrequestsbyanattackeronthenetwork.DHCP snoopingdesignatestrusted
DHCPserversandportsonwhichDHCPrequestsandresponsesareaccepted.
RefertotheIP ServicesGuideformoreinformation.
ThefollowingisaDHCPv4-snoopingsampleconfiguration:
| switch(config)#          | dhcpv4-snooping |                 |     |     |     |     |     |     |     |     |     |
| ------------------------ | --------------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| switch(config)#          | vlan            | 100             |     |     |     |     |     |     |     |     |     |
| switch(config-vlan-100)# |                 | dhcpv4-snooping |     |     |     |     |     |     |     |     |     |
| switch(config-vlan-100)# |                 | exit            |     |     |     |     |     |     |     |     |     |
switch(config)#
| switch(config)#    | interface       | 1/1/1 |       |     |     |     |     |     |     |     |     |
| ------------------ | --------------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| switch(config-if)# | dhcpv4-snooping |       | trust |     |     |     |     |     |     |     |     |
| switch(config-if)# | exi             |       |       |     |     |     |     |     |     |     |     |
switch(config)# dhcpv4-snooping authorized-server 192.168.2.10 vrf default
ToviewtheconfigurationchangewithDHCPv4-snooping:
| switch# show | dhcpv4-snooping |                     |                |         |       |              |                    |           |         |         |       |
| ------------ | --------------- | ------------------- | -------------- | ------- | ----- | ------------ | ------------------ | --------- | ------- | ------- | ----- |
|              | DHCPv4-Snooping |                     | Information    |         |       |              |                    |           |         |         |       |
|              |                 | DHCPv4-Snooping     |                |         |       | : Yes        |                    | Verify    | MAC     | Address | : Yes |
|              |                 | Allow Overwrite     |                | Binding |       | : No         |                    | Enabled   | VLANs   |         | : 100 |
|              |                 | IP Binding          | Disabled       |         | VLANs | :            |                    |           |         |         |       |
|              |                 | Static              | Attributes     |         | : No  |              |                    |           |         |         |       |
|              |                 | Client              | Event          | Logs    | : No  |              |                    |           |         |         |       |
|              |                 | Trust VxLAN         | Tunnels        |         |       | : Yes        |                    |           |         |         |       |
|              | Option          | 82 Configurations   |                |         |       |              |                    |           |         |         |       |
|              |                 | Untrusted           | Policy         |         | :     | drop         |                    | Insertion |         |         | : Yes |
|              |                 | Option              | 82 Remote-id   |         | :     | mac          |                    |           |         |         |       |
|              | External        | Storage             | Information    |         |       |              |                    |           |         |         |       |
|              |                 | Volume              | Name           |         | :     | --           |                    |           |         |         |       |
|              |                 | File Name           |                |         | :     | --           |                    |           |         |         |       |
|              |                 | Inactive            | Since          |         | :     | --           |                    |           |         |         |       |
|              |                 | Error               |                |         | :     | --           |                    |           |         |         |       |
|              | Flash           | Storage Information |                |         |       |              |                    |           |         |         |       |
|              |                 | File Write          | Delay          | :       | --    |              |                    |           |         |         |       |
|              | Active          | Storage             | : --           |         |       |              |                    |           |         |         |       |
|              | Authorized      | Server              | Configurations |         |       |              |                    |           |         |         |       |
|              |                 | VRF                 |                |         |       |              | Authorized         |           | Servers |         |       |
|              |                 | ------------        |                |         |       |              | ------------------ |           |         |         |       |
|              |                 | default             |                |         |       | 192.168.2.10 |                    |           |         |         |       |
Port Information
|     |     |     |     | Max |     | Static |     | Dynamic |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | ------- | --- | --- | --- |
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 43

|     |     |     | Port     |     | Trust | Bindings |     | Bindings | Bindings |
| --- | --- | --- | -------- | --- | ----- | -------- | --- | -------- | -------- |
|     |     |     | -------- |     | ----- | -------- |     | -------- | -------- |
|     |     |     | 1/1/1    |     | Yes   | 0        | 0   |          | 0        |
ThefollowingisaDHCPv6-snoopingsampleconfiguration:
| switch(config)#          |     | dhcpv6-snooping |     |                 |     |     |     |     |     |
| ------------------------ | --- | --------------- | --- | --------------- | --- | --- | --- | --- | --- |
| switch(config)#          |     | vlan            | 100 |                 |     |     |     |     |     |
| switch(config-vlan-100)# |     |                 |     | dhcpv6-snooping |     |     |     |     |     |
| switch(config-vlan-100)# |     |                 |     | exit            |     |     |     |     |     |
switch(config)#
| switch(config)# |     | interface |     | 1/1/1 |     |     |     |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- | --- | --- | --- |
switch(config-if)#
|                    |     | dhcpv6-snooping |     |     | trust |     |     |     |     |
| ------------------ | --- | --------------- | --- | --- | ----- | --- | --- | --- | --- |
| switch(config-if)# |     | exit            |     |     |       |     |     |     |     |
switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default
ToviewtheconfigurationchangewithDHCPv6-snooping:
| 6200(config)#   |                 | show           | dhcpv6-snooping |         |             |                    |       |         |       |
| --------------- | --------------- | -------------- | --------------- | ------- | ----------- | ------------------ | ----- | ------- | ----- |
| DHCPv6-Snooping |                 | Information    |                 |         |             |                    |       |         |       |
|                 | DHCPv6-Snooping |                |                 | :       | Yes Enabled |                    | VLANs |         | : 100 |
|                 | IP Binding      | Disabled       |                 | VLANs   |             | :                  |       |         |       |
|                 | Trusted         | Port           | Bindings        | Enabled | VLANs       | :                  |       |         |       |
|                 | Client          | Event          | Logs            |         |             | :                  | No    |         |       |
|                 | Trust           | VxLAN Tunnels  |                 |         |             | :                  | Yes   |         |       |
| External        | Storage         | Information    |                 |         |             |                    |       |         |       |
|                 | Volume          | Name           |                 | :       | --          |                    |       |         |       |
|                 | File Name       |                |                 | :       | --          |                    |       |         |       |
|                 | Inactive        | Since          |                 | :       | --          |                    |       |         |       |
|                 | Error           |                |                 | :       | --          |                    |       |         |       |
| Flash           | Storage         | Information    |                 |         |             |                    |       |         |       |
|                 | File Write      | Delay          | :               | --      |             |                    |       |         |       |
| Active          | Storage         | : --           |                 |         |             |                    |       |         |       |
| Authorized      | Server          | Configurations |                 |         |             |                    |       |         |       |
|                 | VRF             |                |                 |         |             | Authorized         |       | Servers |       |
|                 | ------------    |                |                 |         |             | ------------------ |       |         |       |
|                 | default         |                |                 |         |             | ABCD:5ACD::2000    |       |         |       |
Port Information
|     |          |       | Max      |     | Static   |     | Dynamic  |     |     |
| --- | -------- | ----- | -------- | --- | -------- | --- | -------- | --- | --- |
|     | Port     | Trust | Bindings |     | Bindings |     | Bindings |     |     |
|     | -------- | ----- | -------- |     | -------- |     | -------- |     |     |
|     | 1/1/1    | Yes   |          | 0   | 0        |     | 0        |     |     |
DHCPv6 Guard
DHCPv6guardisanextensionofDHCPv6snooping.WhentheDHCPv6snoopingfeatureisconfigured
globallyandontheVLAN,theportsareconfiguredastrustedanduntrustedports.DHCPv6guard
enhancesthisbycreatingapolicyandapplyingitonaportandontheVLAN.Thispolicycontains
multipleattributeswhicharecomparedagainstthepacketthatisreceivedontrustedports.Ifthe
HardeningtheControlPlane|44

packetcomplieswiththeattributesofthepolicy,itisforwardedtothedestinationport;otherwisethe
packetisdropped.
ThefollowingaresampleconfigurationsofDHCPv6guard:
| switch(config)# | dhcpv6-snooping |     | guard-policy | pol1 |     |
| --------------- | --------------- | --- | ------------ | ---- | --- |
switch(config-dhcpv6-guard-policy)# match server access-list acl1
| switch(config-dhcpv6-guard-policy)# |     |     | preference | min | 6   |
| ----------------------------------- | --- | --- | ---------- | --- | --- |
| switch(config-dhcpv6-guard-policy)# |     |     | preference | max | 250 |
switch(config-dhcpv6-guard-policy)# match client prefix-list pref1
| switch(config)#          | vlan 5 |                 |     |              |      |
| ------------------------ | ------ | --------------- | --- | ------------ | ---- |
| switch(config-vlan-100)# |        | dhcpv6-snooping |     | guard-policy | pol1 |
ToviewtheconfigurationchangewithDHCPv6guard:
| switch# show    | dhcpv6-snooping |        | guard-policy |     |     |
| --------------- | --------------- | ------ | ------------ | --- | --- |
| DHCPv6-Snooping | guard-policy    |        | Information  |     |     |
| DHCPV6 Guard    | Policy name     | : POL1 |              |     |     |
| Attached Access | List :          | ACL1   |              |     |     |
| Attached Prefix | List :          | PRF1   |              |     |     |
| Preference      | Range : 6-250   |        |              |     |     |
| Applied on      | VLAN : 5        |        |              |     |     |
| Applied on      | Port            |        |              |     |     |
| Dynamic         | ARP Inspection  |        |              |     |     |
DynamicARPInspectionprovidesadditionalsecurityforARP.DynamicARPresolvesIP addresses
againstMAC addressesonabroadcastnetworksegmentsuchasEthernet,originallydefinedbyInternet
StandardRFC826.ARPdoesnotsupportanyinherentsecuritymechanismandassuch,dependson
simpledatagramexchangesfortheresolution,withmanyofthesebeingbroadcast.Becauseitisan
unreliableandnon-secureprotocol,ARPisvulnerabletoattacks.
Someattacksmaybetargetedtowardthenetworkswhereasotherattacksmaybetargetedtowardthe
switchitself.Theattacksprimarilyintendtocreatedenialofservice(DoS)fortheotherentitiespresent
inthenetwork.Mostoftheattacksarecarriedoutinoneofthefollowingthreeforms:
n OverwhelmingtheswitchcontrolplanewithtoomanyARPpackets.
n Overwhelmingtheswitchcontrolplanewithtoomanyunresolveddatapackets.
n Posingasatrustedgateway/serverbywronglyadvertisingARPs.
Thefollowingdefensemechanismscanbeputinplaceonaswitchtoprotectagainstattacks:
n LimitingtheamountofARPactivityallowedfromahostoronaport.
n EnsuringthatallARPpacketsareconsistentwithoneormorebindingdatabases.
EnforcingintegritychecksontheARPpacketstocheckagainstdifferentMACorIPaddressesinthe
n
EthernetorIPandARPheader.
Thefollowingaresupported:
n EnablinganddisablingofDynamicARPInspectiononaVLANlevel(itdoesnothavetobeSVI).
n DefiningthememberportsofaVLANaseithertrustedoruntrusted.OnlyARPtrafficonuntrusted
portssubjectedtochecks.
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 45

n Routedports(RoPs)alwaystreatedastrusted.
n ListeningtotheDHCPBindingstableandcheckingeveryARPpackettomatchagainstthebinding.
Prerequisites
DynamicARPInspectionisenforcedusingDHCP Snooping bindingandStatic IP Binding.Refertothe
DHCPSnoopingsectionfortheDHCPsnoopingconfigurationtoenabletheStatic IP Binding.
| switch(config)#         | interface | vlan 10          |                       |
| ----------------------- | --------- | ---------------- | --------------------- |
| switch(config-if-vlan)# |           | arp ipv4 2.2.2.2 | mac 01:00:5e:00:00:01 |
| switch# configure       | terminal  |                  |                       |
| switch(config)#         | vlan      | 1                |                       |
| switch(config-vlan)#    |           | arp inspection   |                       |
Toconfiguretheinterfaceastrusted:
| switch# configure | terminal  |       |     |
| ----------------- | --------- | ----- | --- |
| switch(config)#   | interface | 1/1/1 |     |
switch(config-if)#
|              | arp            | inspection trust |       |
| ------------ | -------------- | ---------------- | ----- |
| switch# show | arp inspection | interface        | 1/1/1 |
---------------------------------------------------------------------------
| Interface | Trust-State |     |     |
| --------- | ----------- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1 Trusted |     |     |     |
| ------------- | --- | --- | --- |
---------------------------------------------------------------------------
Allinterfacesareuntrustedbydefault.
| ND Snooping | Attack | Prevention |     |
| ----------- | ------ | ---------- | --- |
NDsnoopingisusedinLayer2switchingnetworksandpreventsNDattacks.NDsnoopingdropsinvalid
NDpackets,andcombinedwithDIPLDv6(DynamicIPLockdownforIPv6),blocksdatatrafficfrom
invalidhosts.NDsnoopinglearnsthesourceMACaddresses,sourceIPv6addresses,inputinterfaces,
andVLANsofincomingNDmessagesanddatapacketstobuildIPbindingentries.
NDsnoopingdropsNDpacketsforthefollowingreasons:
n IftheEthernetsourceMACaddressdoesnotmatchtheaddressintheICMPv6Targetlinklayer
addressfieldoftheNDpacket.
n IftheglobalIPv6addressinthesourceaddressfielddoesnotmatchtheNDsnoopingprefixfilter
table.
n IftheglobalIPv6addressorthelink-localIPv6addressinthesourceIPaddressfielddoesnotmatch
theNDsnoopingbindingtable
ThefollowingaresampleVLANconfigurationsofgloballyenabledND snooping:
HardeningtheControlPlane|46

| switch#                  | configure | terminal    |             |     |     |
| ------------------------ | --------- | ----------- | ----------- | --- | --- |
| switch(config)#          |           | nd-snooping |             |     |     |
| switch(config)#          |           | vlan        | 100         |     |     |
| switch(config-vlan-100)# |           |             | nd-snooping |     |     |
| switch(config-vlan-100)# |           |             | exit        |     |     |
switch(config)#
| switch(config)# |             | show | nd-snooping |     |     |
| --------------- | ----------- | ---- | ----------- | --- | --- |
| ND Snooping     | Information |      |             |     |     |
========================
| ND Snooping | :            | Enabled       |                  |                   |     |
| ----------- | ------------ | ------------- | ---------------- | ----------------- | --- |
| ND Snooping | Enabled      | VLANs         |                  | : 100             |     |
| Trusted     | Port         | Bindings      | Enabled          | VLANs : 100       |     |
| ND Guard    | Enabled      | VLANs         | : 100            |                   |     |
| RA Guard    | Enabled      | VLANs         | : 100            |                   |     |
| RA Drop     | Enabled      | VLANs         | :                |                   |     |
| MAC Address | Check        | : Disabled    |                  |                   |     |
| PORT TRUST  | MAX-BINDINGS |               | CURRENT-BINDINGS |                   |     |
| -------     | ------       | ------------- |                  | ----------------- |     |
1/1/1 Yes
1/1/2 Yes
FormoreinformationonNDsnoopingrefertheAOS-CXIPServicesGuide.
RA Guard
RouterAdvertisement(RA)guardblocksunwanted,forgedRAmessagesonaLayer2acessdevice.ND
snoopingdropsbothRAandRRpacketsonuntrustedports.ToblockonlyRApacketsonVLANswithND
| snoopingenabled,usend-snooping |     |     |     | ra-drop. |     |
| ------------------------------ | --- | --- | --- | -------- | --- |
RAdropisdisabledbydefaultonVLANs.Whenenabled(withnd-snooping ra-drop),NDsnooping
blocksRApacketsonbothtrustedanduntrustedports.WhenRAdropisdisabled,NDsnoopingallows
RApacketsontrustedportsandblocksthemonuntrustedports.
WhenRAguardpolicyisenabled(withipv6 nd-snooping ra-guard policy),RApacketsreceivedon
trustedportsarevalidatedagainstasetofparametersconfiguredonthepolicyandassignedtoaport
orVLAN.RAGuardpolicyoptionsinclude:
n HopLimit
n ManagedConfigFlag
n OtherConfigFlag
n RouterPreference
n ACL
AdvertisedPrefixLists
n
| switch(config)#                             |     | ipv6 | nd-snooping | ra-guard policy    | <POLICY-NAME> |
| ------------------------------------------- | --- | ---- | ----------- | ------------------ | ------------- |
| switch(config-raguard-policy)#-------Policy |     |      |             | Parameters-------- |               |
| switch(config)#                             |     | vlan | 10          |                    |               |
switch(config-vlan-10)# nd-snooping ra-guard attach-policy POLICY_NAME
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 47

| switch#  | show   | nd-snooping |     | ra-guard | interface | 1/1/1 |
| -------- | ------ | ----------- | --- | -------- | --------- | ----- |
| RA Guard | Policy | Counters    |     |          |           |       |
========================
| RA Guard          | Policy    | Applied |          | : POLICY_2 |     |     |
| ----------------- | --------- | ------- | -------- | ---------- | --- | --- |
| RA Packets        | Received  |         | : 10     |            |     |     |
| RA Packets        | Forwarded |         | :        | 5          |     |     |
| RA Packets        | Dropped   |         | : 5      | [Total]    |     |     |
| reason :          | Managed   | flag    | error    | [0]        |     |     |
| Other flag        | error     | [0]     |          |            |     |     |
| Access list       | error     |         | [0]      |            |     |     |
| Prefix list       | error     |         | [0]      |            |     |     |
| Router preference |           |         | error[0] |            |     |     |
| Hop limit         | error     | [5]     |          |            |     |     |
| IPv6 Destination  |           |         | Guard    |            |     |     |
EnablingIPv6destinationguardonaswitchpreventsNDcachedepletionissuesandhelpsinminimizing
Denial-of-Service(DoS)attacks.WhenIPv6destinationguardisenabled,addressresolutionis
performedonlyforthedestinationaddressesthatareactiveonthelink.Thisfeaturerequiresthe
bindingtabletobepopulatedwiththehelpofDHCPv6snooping,NDsnooping,orstatic-ip-bindings.
DestinationguardenablesthedestinationaddressbasedfilteringofIPv6trafficandblocksthe
NeighborDiscovery(ND)protocolresolutionfordestinationaddressesthatarenotfoundinthebinding
table.
| switch(config)#         |          | vlan | 10                |                        |            |     |
| ----------------------- | -------- | ---- | ----------------- | ---------------------- | ---------- | --- |
| switch(config-vlan-10)# |          |      |                   | ipv6 destination-guard |            |     |
| switch#                 | show     | ipv6 | destination-guard |                        | statistics |     |
| Packets                 | dropped  | for  | VLAN              | 10 : 25467             |            |     |
| Packets                 | dropped  | for  | VLAN              | 30 : 434               |            |     |
| Packets                 | dropped  | for  | VLAN              | 50 : 8767              |            |     |
| IP Source               | Lockdown |      |                   |                        |            |     |
IPsourcelockdownprovidesaddedsecuritybypreventingIPsourceaddressspoofingonaper-port
basis.Everypacketisinspectedforthispurposeinhardware.WhenIPsourcelockdownisenabled,IP
trafficreceivedonaninterface(port)isforwardedonlyiftheVLAN,IPaddress,MACaddress,and
interface(port)matchetheIPbindingdatabaseentry.
TouseIPsourcelockdown,theIPbindingdatabasemustbepopulated.Thebindingdatabaseis
dynamicallypopulatedbyDHCPsnoopingthatlearnsandsavesthebindinginformation.Alternatively,
theIPbindingdatabasecanbestaticallypopulatedwiththeiPsource-bindingcommand.
ToenableIPsourcelockdownresourceextendedonthedevice(supportsdynamicallysharinghardware
resourcesofIPsourcelockdownwithotherfeatures):
| switch(config)# |     | ip       | source-lockdown |          | resource-extended |     |
| --------------- | --- | -------- | --------------- | -------- | ----------------- | --- |
| Do you want     | to  | continue |                 | (y/n)? y |                   |     |
ToenableIPv4/IPv6sourcelockdownforallVLANsontheselectedinterface(port):
HardeningtheControlPlane|48

| switch(config)#    |          | interface |                 | 1/1/1           |     |     |     |     |
| ------------------ | -------- | --------- | --------------- | --------------- | --- | --- | --- | --- |
| switch(config-if)# |          |           | ipv4            | source-lockdown |     |     |     |     |
| switch(config-if)# |          |           | ipv6            | source-lockdown |     |     |     |     |
| switch#            | show     | ipv4      | source-lockdown |                 |     |     |     |     |
| INTERFACE          | LOCKDOWN |           | HW-STATUS       |                 |     |     |     |     |
| ---------          | -------- |           | ---------       |                 |     |     |     |     |
| 1/1/1              | Yes      | Yes       |                 |                 |     |     |     |     |
| switch#            | show     | ipv6      | source-lockdown |                 |     |     |     |     |
| INTERFACE          | LOCKDOWN |           | HW-STATUS       |                 |     |     |     |     |
| ---------          | -------- |           | ---------       |                 |     |     |     |     |
| 1/1/1              | Yes      | Yes       |                 |                 |     |     |     |     |
ToaddstaticIPv4/IPv6clientsourcebindinginformationtotheswitchIPv4/IPv6bindingdatabase:
| Ipv4 source-binding |      |             | <VLAN-ID>      |     | <IPV4-ADDR> | <MAC-ADDR> |     | <IFNAME>     |
| ------------------- | ---- | ----------- | -------------- | --- | ----------- | ---------- | --- | ------------ |
| ipv6 source-binding |      |             | <VLAN-ID>      |     | <IPV6-ADDR> | <MAC-ADDR> |     | <IFNAME>     |
| switch#             | show | ipv4        | source-binding |     |             |            |     |              |
| PORT                | VLAN | MAC-ADDRESS |                |     | HW-STATUS   | FROM       |     | IPv4-ADDRESS |
-------------- --------- ----------------- --------- -------- ----------
| 1/1/1   | 2    | aa:bb:cc:dd:ee:ff |                |     | Yes       | static |      | 1.2.3.4      |
| ------- | ---- | ----------------- | -------------- | --- | --------- | ------ | ---- | ------------ |
| 1/1/2   | 12   | aa:ab:cc:dd:ee:ff |                |     | Yes       | static |      | 10.20.30.40  |
| switch# | show | ipv6              | source-binding |     |           |        |      |              |
| PORT    | VLAN | MAC-ADDRESS       |                |     | HW-STATUS |        | FROM | IPv6-ADDRESS |
-------------- --------- ----------------- --------- -------- -------------
| 1/1/1    | 1234    | 00:50:56:96:e4:cf |     |           |     | Yes/No |     | static 3000::1 |
| -------- | ------- | ----------------- | --- | --------- | --- | ------ | --- | -------------- |
| Securing | Routing |                   |     | Protocols |     |        |     |                |
ThefollowingsectionsdescribetheworkflowsforsecuringOSPF andBGProutingprotocols.
| OSPF Passive |     | Interfaces |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
UnlikeBGP,mostroutingprotocolstendtodiscoverneighborsviathesendingandreceivingHello
packets.Sincetheseneighborrelationshipsbuilddynamically,theadministratorshouldcontrolwhich
neighborrelationshipscanbeformedandadministratorsshouldensurethatthepotentialneighbors
areknownandtrusted.
TolimitwhereOSPFcanlearnneighbors,AOS-CXsupportsthepassiveOSPFinterfaces.ApassiveOSPF
interfacehasitsIPsubnetsannounced,butitdoesnotestablishneighborrelationshipswithotherOSPF
devicesontheinterface.
YoumustmakeallOSPFenabledinterfacespassive.SettingtheOSPFenabledinterfacestofromdefault
topassiveisdoneintheOSPFrouterinstancecontext.
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 49

| switch(config)#        |     |     | router | ospf 1            |     |         |     |
| ---------------------- | --- | --- | ------ | ----------------- | --- | ------- | --- |
| switch(config-ospf-1)# |     |     |        | passive-interface |     | default |     |
ThepassiveinterfaceisthenremovedfromeachinterfacewhereOSPFneighborrelationshipsare
allowed.Sincethisisaninterface-levelconfigurationchange,itcanbedonefromtheinterfacecontext:
| switch(config)#    |          |     | interface      | 1/1/1        |     |     |     |
| ------------------ | -------- | --- | -------------- | ------------ | --- | --- | --- |
| switch(config-if)# |          |     | no ip          | ospf passive |     |     |     |
| OSPF               | Neighbor |     | Authentication |              |     |     |     |
AllOSPFexchangesareauthenticated.However,thedefaultauthenticationusedbynetworkvendorsis
"null,"meaningemptyorzero.OSPFalsosupportsuseofasimpleplaintextpasswordand
cryptographicauthentication.AOS-CXsupportsseveralOSPFv2authenticationmethods,includingSHA
cryptographichashesupto512bits,toauthenticatemessagesbetweenOSPFneighbors.
WhenconfiguringauthenticationbetweenOSPFneighbors,theauthenticationmethodand
authenticationkeymustbethesameontheinterfacesconnectedonthebothdevices.
ToconfigureSHA-512authentication,changethedefaultauthenticationmethodfromnulltohmac-sha-
512fromtheinterfacecontext:switch
| (config-if)# |     | ip  | ospf authentication |     |     | hmac-sha-512 |     |
| ------------ | --- | --- | ------------------- | --- | --- | ------------ | --- |
ThenconfigureaSHAkeytobeusedfortheconnection,thekeycanbeenteredasplaintextorasa
hashedciphertextstring:
switch(config-if)# ip ospf sha-key 1 plaintext ospfshakeystring
Alternatively,theAOS-CXkeychainfeaturemaybeusedtospecifyasystem-levelcryptographic
authenticationkeywhichcanbeusedbymultipleOSPFinterfaces:
| switch(config)#          |     |     | keychain | ospf-keychain |     |     |     |
| ------------------------ | --- | --- | -------- | ------------- | --- | --- | --- |
| switch(config-keychain)# |     |     |          | key 1         |     |     |     |
switch(config-keychain-key)# cryptographic-algorithm hmac-sha-512
switch(config-keychain-key)# key-string plaintext ospfshakeystring
| switch(config-keychain-key)# |      |                |         | interface      |     | 1/1/49        |            |
| ---------------------------- | ---- | -------------- | ------- | -------------- | --- | ------------- | ---------- |
| switch(config-if)#           |      |                | ip ospf | authentication |     | keychain      |            |
| switch(config-if)#           |      |                | ip ospf | keychain       |     | ospf-keychain |            |
| OSPFv3                       | Area | Authentication |         |                | and | Encryption    | with IPsec |
OSPFv3neighborsmayuseinterface-levelauthentication.Analternativemethodmightbeusedto
provideencryption,orauthentication,orbothforanentireOSPFv3areausingtheIPsecprotocol,which
automaticallyappliestheconfiguredmethodstoallmemberinterfaces.TherearetwoIPsec
encapsulationtypessupportedonAOS-CXtosecureOSPFv3areas:
n IPv6authenticationheader(AH),whichaddsanIPv6authenticationheadertoOSPFv3packets.
EncryptedSecurityPayload(ESP),whichprovidesbothauthenticationandencryptionforOSPFv3
n
packets.
HardeningtheControlPlane|50

IPsecauthenticationandencryptionareconfiguredfromtheOSPFv3routerprocesscontext.Both
authenticationandencryptionrequireaspecifiedSecurityPolicyIndex(SPI),whichisanintegervalue
between256and4,294,967,295;thisvalueisusedoneachOSPFv3routerinthesecuredareatomatch
aconfiguredIPsecauthenticationand/orencryptionpolicy.EachOSPFv3IPsecpolicyonaswitchmust
useadifferentSPIvalue,andtheSPIvalue(aswellasauthentication,orencryptionkeys,orboth)must
matchacrossallOSPFv3neighborinterfacesusingthatpolicywithinthesecuredarea.
ToconfigureAHauthenticationforOSPFv3area1,specifytheSPI,authenticationmethod(md5orsha1),
keytype(plaintext,hex-string,orciphertext)andthekeystringitself.Ifakeytypeandstringarenot
specified,theuserispromptedtoenteraplaintextkeyinteractively:
switch(config-ospfv3-1)# area 1 authentication ipsec spi 1024 sha1
| Enter the | IPsec authentication     | key: *******  |     |     |
| --------- | ------------------------ | ------------- | --- | --- |
| Re-Enter  | the IPsec authentication | key: ******** |     |     |
ToconfigureESPencryptionforarea1,specifytheSPI,authenticationmethod,authenticationkeytype
andstring,encryptiontype(3des,aes,des,ornull),keytype,andencryptionkeystring.Iftheencryption
typeandkeystringarenotspecified,youarepromptedtoenteraplaintextkeyinteractively.Ifthe
authenticationkeytypeandstringarenotspecified,youarepromptedtoenterbothaplaintext
authenticationkeyaswellasthedesiredencryptiontypeandplaintextkey.
| switch(config-ospfv3-1)# |                          | area 1 encryption         | ipsec spi | 1024 sha1 |
| ------------------------ | ------------------------ | ------------------------- | --------- | --------- |
| Enter the                | IPsec authentication     | key: *******              |           |           |
| Re-Enter                 | the IPsec authentication | key: *******              |           |           |
| Enter the                | IPsec encryption         | type (3des/aes/des/null)? |           | aes       |
| Enter the                | IPsec encryption         | key: ****************     |           |           |
| Re-Enter                 | the IPsec encryption     | key: ****************     |           |           |
Dependingontheselectedencryptiontype,aplaintextorhexadecimalencryptionkeymustbesettoa
specificlengthasmentionedbelow:
n 3DES:
o Hexadecimal:48digits
o Plaintext:24characters
n DES:
o Hexadecimal:16digits
o Plaintext:8characters
n AES:
o Hexadecimal:32,48,or64digits
o Plaintext:16,24,or32characters
ForAESencryption,thespecifiedkeylengthscorrespondtoAES128,AES192,orAES256,respectively;
thetypeofthekeythatwillbeusedisautomaticallydeterminedbythelengthoftheenteredencryption
key.AOS-CXrecommendsusingAESoverDESor3DESasitisstronger.
| switch(config)# | show run | ospf   |     |     |
| --------------- | -------- | ------ | --- | --- |
| switch(config)# | show run | ospfv3 |     |     |
BGP
TheIETFBestCurrentPracticesforBGPSecurity(BCP194)focusesonthefollowingthreeitems:
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 51

n Utilizingthecontrol-placeACLfunctionalitytolimitBGPcommunicationtoconfiguredBGPpeers.
n SecuringBGPsessionsbetweenpeersbyusingauthentication.
UseTTLSecurityMechanismstopreventspoofingattacksfromthirdparties.
n
| Control Plane | ACL for | BGP Peering |     | Sessions |     |     |
| ------------- | ------- | ----------- | --- | -------- | --- | --- |
DevicesrunningBGPlistenforconnectionsonTCPport179.WhenestablishingaBGPpeersession,one
deviceactivelyestablishesarelationshipwiththeotherpeerbysendingthefirstTCPSYNpacket.This
deviceisattheoutgoingsideoftheconnection.Theotherpeer,hearingtheTCPSYN,respondswitha
SYNorACKattheincomingconnection.Aseachpeercanassumeeitherrole,ACLentriesneedtobe
configuredforBGPinbothdirections.
BuildingonthesameControlPlaneACLexampleasbefore,thebelowentriespermittrafficfrom
10.20.0.10sothatitcanestablishaBGPpeeringsessionwiththedevice.Eithersidecouldplaythe
outgoingorincomingroleintheconnection,sotheACLrequirestwoentriesperpeer:
| switch(config)#        | access-list |     | ip CONTROLPLANE |          |              |     |
| ---------------------- | ----------- | --- | --------------- | -------- | ------------ | --- |
| switch(config-acl-ip)# |             | 800 | comment         | LOCKDOWN | BGP SESSIONS |     |
switch(config-acl-ip)# 805 permit tcp 10.20.0.10 gt 1023 any eq 179
switch(config-acl-ip)# 810 permit tcp 10.20.0.10 eq 179 any gt 1023
After allowing traffic from all configured peers, block all other devices from
establishing a BGP peering session by denying all other traffic to or from TCP
| port 179.              |           |       |      |                 |             |     |
| ---------------------- | --------- | ----- | ---- | --------------- | ----------- | --- |
| switch(config-acl-ip)# |           | 890   | deny | tcp any gt 1023 | any eq      | 179 |
| switch(config-acl-ip)# |           | 895   | deny | tcp any eq 179  | any gt 1023 |     |
| Authenticate           | BGP Peers | Using | MD5  |                 |             |     |
TheTCPsessionsbetweenthetwopeerscanbesecuredbyaddingMD5protectiontotheTCPsession
header.TheMD5digestactslikeapasswordbetweenpeers.ThisconfigurationisdonewithintheBGP
configurationcontext,andbothpeersneedtoconfigurethesamepassword.
switch(config-bgp)# neighbor 10.20.0.10 password plaintext meatballs4me!
| BGP TTL Security |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- |
Assumingmostroutingneighborsaretypicallydirectlyconnected,asimplemethodtoblockremote
spoofingfromremotedevicesistochecktheTTLofthepacketssentfromthepeeranddropped
packetswhoseTTLislessthantheexpectedamount.FollowingexampleusestheBGPpeerspecified
above.AssumingthemaximumTTLvalueis255,thepacketssentfromthepeerarecomparedagainst
thehop-count,enteredbelowasavalueof1.
| switch(config-bgp)# |     | neighbor | 10.20.0.10 | ttl-security-hops |     | 1   |
| ------------------- | --- | -------- | ---------- | ----------------- | --- | --- |
WithamaximumTTLvalueof255andaconfiguredhopcountvalueof1,thepacketswithaTTLbelow
254willbedropped.
| switch | # show run | bgp |     |     |     |     |
| ------ | ---------- | --- | --- | --- | --- | --- |
HardeningtheControlPlane|52

| Multicast | Security |     |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- | --- |
Thefollowingsectionsdescribesecurityandhardeningworkflowsformulticasttraffic.
SSDP
TheSimpleServiceDiscoveryProtocol(SSDP)isanapplicationlayerprotocolandoneofthekey
protocolsthatimplementUniversalPlugandPlay(UPnP).SSDPenablesnetworkdevicestodiscoverand
advertisenetworkservicesbysendingmulticastdiscoveryandadvertisementmessagestomulticast
IPv4groupaddress239.255.255.250:1900ormulticastIPv6groupaddressFF0x::C.WithUPnP,each
devicegeneratesauniquemulticastflow(SourceIP,SSDPGroupIP).Inamulticastnetworkwithmany
enduserdevices,thiscanconsumealargeamountofmulticasthardwareandsoftwareresourcesas
eachdevicecreatesaunique(S,G)flowandtheresourcesarelimited.Innetworkswherethereisa
needtocontrol,drop,orminimizeSSDPtraffic,summarizedstaticmulticastroutescanbeconfiguredto
savenetworkresourcesandtoavoiddenialofservices.
Thefollowingexampleshowsatypicalstaticmulticastroute:[Incominginterface,Source,Group]>[Set
ofdownstreaminterfaces]:
switch(config)# ip multicast-static-route vlan10 any 239.250.255.250 1/1/2
| switch# show | ip  | multicast-static-route |     |     | all-vrfs |     |     |
| ------------ | --- | ---------------------- | --- | --- | -------- | --- | --- |
VRF : default
| Group Address      | :        | 239.250.255.250 |       |     |     |     |     |
| ------------------ | -------- | --------------- | ----- | --- | --- | --- | --- |
| Source Address     | :        | any             |       |     |     |     |     |
| Route type         | : Static |                 |       |     |     |     |     |
| Incoming interface |          | :               | 1/1/2 |     |     |     |     |
| Outgoing Interface |          | List            | :     |     |     |     |     |
| Interface          | State    |                 |       |     |     |     |     |
| ---------          | -----    |                 |       |     |     |     |     |
vlan10 forwarding
IftheSSDPserviceisnotenabledinthenetwork,bestpracticesistodisableSSDPeitherthroughVLAN
ACLsorthroughapolicy,asshowninthefollowingexamples:
| switch(config)#          |     | access-list |               | ip drop_ssdp |                     |           |         |
| ------------------------ | --- | ----------- | ------------- | ------------ | ------------------- | --------- | ------- |
| switch(config-acl-ip)#10 |     |             | deny          | udp any      | 239.255.255.250     |           | eq 1900 |
| switch(config)#          |     | vlan        | 10            |              |                     |           |         |
| switch(config-vlan-10)#  |     |             | apply         | access-list  | ip                  | drop_ssdp | in      |
| switch(config)#          |     | interface   | 1/1/1         |              |                     |           |         |
| switch(config-if)#       |     | no          | shutdown      |              |                     |           |         |
| switch(config-if)#       |     | no          | routing       |              |                     |           |         |
| switch(config-if)#       |     | vlan        | access        | 10           |                     |           |         |
| switch(config)#          |     | interface   | vlan          | 10           |                     |           |         |
| switch(config-if-vlan)#  |     |             | ip address    |              | 192.168.1.2/24      |           |         |
| switch(config-if-vlan)#  |     |             | ip igmp       | enable       |                     |           |         |
| switch(config-if-vlan)#  |     |             | ip pim-sparse |              | enable              |           |         |
| switch(config)#          |     | router      | pim           |              |                     |           |         |
| switch(config-pim)#      |     | enable      |               |              |                     |           |         |
| switch(config)#          |     | class       | ip drop_class |              |                     |           |         |
| switch(config-class-ip)# |     |             | 10            | match any    | any 239.255.255.250 |           |         |
| switch(config)#          |     | policy      | drop_ssdp     |              |                     |           |         |
| switch(config-policy)#   |     |             | 10 class      | ip           | drop_class          | action    | drop    |
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 53

| switch(config)#                                  |      | vlan      | 10            |        |                |          |
| ------------------------------------------------ | ---- | --------- | ------------- | ------ | -------------- | -------- |
| switch(config-vlan-10)#                          |      |           | apply         | policy | drop_ssdp      | in       |
| switch(config)#                                  |      | interface | 1/1/1         |        |                |          |
| switch(config-if)#                               |      | no        | shutdown      |        |                |          |
| switch(config-if)#                               |      | no        | routing       |        |                |          |
| switch(config-if)#                               |      | vlan      | access        | 10     |                |          |
| switch(config)#                                  |      | interface | vlan          | 10     |                |          |
| switch(config-if-vlan)#                          |      |           | ip address    |        | 192.168.1.2/24 |          |
| switch(config-if-vlan)#                          |      |           | ip igmp       | enable |                |          |
| switch(config-if-vlan)#                          |      |           | ip pim-sparse |        | enable         |          |
| switch(config)#                                  |      | router    | pim           |        |                |          |
| switch(config-pim)#                              |      | enable    |               |        |                |          |
| Toviewtheconfigurationchange,issuethecommandshow |      |           |               |        |                | run pim. |
| Hardening                                        | IGMP | and       | MLD Snooping  |        |                |          |
IGMPsnoopingrunsonaLayer2deviceasamulticastconstrainingmechanismtoimprovemulticast
forwardingefficiency.ItcreatesLayer2multicastforwardingentriesfromIGMPpacketsthatare
exchangedbetweenthehostsandtherouter.IfIGMPsnoopingisnotenabled,thesnoopingswitch
floodsmulticastpacketstoallhostsinaVLAN.IGMPL2snoopingswitchprovidesthebenefitof
conservingbandwidthonthosesegmentsofthenetworkwherenonodehasexpressedinterestin
receivingpacketsaddressedtothegroupaddress.WhenIGMPsnoopingisenabled,theL2snooping
switchforwardsmulticastpacketsofknownmulticastgroupstoonlythereceivers.
MulticastListenerDiscovery(MLD)snoopingoptimizesmulticasttrafficacrossthenetworktoprevent
trafficfromfloodingportsonaVLAN.Forexample,oneofthefeaturesofMLDsnoopingletsyou
configurethenetworksothattrafficisforwardedonlytoportsthatinitiateanMLDrequestfor
multicast.AnotherfeatureofMLDletsyouenableasettingsothatpacketsthatdonotmatchthe
configuredversionaredropped.Portscanbeblockedfromtraffic.
Thedevicecannotprovidemulticastservicestolegaluserswhenithasmanyinvalidmulticastentries
thatarecreatedbasedonIGMPorMLDreportsfrommalicioususers.Tocontrolthemulticastgroups
thathostscanjoin,configureamulticastgrouppolicyontheLayer2devicethatisenabledwithIGMP
snoopingorMLDsnooping.WhenahostsendsanIGMPorMLDreporttorequestamulticastprogram,
theLayer2deviceusesthemulticastgrouppolicytofilterthereport.TheLayer2deviceaddstheport
ofthehosttotheoutgoingportlistonlyifthereportispermittedbythemulticastgrouppolicy.
| switch(config)# |     | ip igmp | snooping     | apply | access       | list <ACL-NAME> |
| --------------- | --- | ------- | ------------ | ----- | ------------ | --------------- |
| switch(config)# |     | ipv6    | mld snooping |       | apply access | list <ACL-NAME> |
n ExistingclassifiercommandsareusedtoconfiguretheACL.
n IfanIGMPv3packetwithmultiplegroupaddressesisreceived,theswitchonlyprocessesthe
permittedgroupaddressesfromtheACLruleset.ThepacketisforwardedtothequerierandPIM
routereventhoughoneofthegroupspresentinthepacketisblockedbyACL.Thisavoidsadelayin
learningthepermittedgroups.SincetheaccessswitchconfiguredwithACLblocksthetrafficforthe
groupswhicharedenied,theforwardingofjoinmessageshasnoimpact.Ifallthegroupsinthe
packetaredeniedbytheACLrule,thepacketisnotforwardedtothequerierandPIMrouter.Existing
joinmessageswilltimeout.
n InadeploymentwithIGMPv2,ifthereisnomatchorifthereisadenyrulematch,thepacketis
dropped.
HardeningtheControlPlane|54

| Hardening | PIM | and | PIMv6 |     |     |     |
| --------- | --- | --- | ----- | --- | --- | --- |
InanetworkwhereIPmulticasttrafficistransmittedformultimediaapplications,thistrafficisblocked
atroutedinterface(VLAN)boundariesunlessamulticastroutingprotocolisrunning.Protocol
IndependentMulticast(PIM)isafamilyofroutingprotocolsthatformmulticasttreestoforwardtraffic
frommulticastsourcestosubnetsthathaveusedaprotocolsuchasIGMPtorequestthetraffic.
PIM Accept-Register
PIMAccept-registerisasecurityfeaturethatallowscontroloverwhichsourcesandgroupscanregister
withtheRendezvousPoint(RP).ThecommandisconfiguredinadditiontotheRPconfigurationand
includesanaccesslistoptionthatcontrolssourcesandgroupsbasedonthefollowingaccesslist
configuration:
| switch(config)#          |     | access-list |                 | ip        | pim_reg_acl   |               |
| ------------------------ | --- | ----------- | --------------- | --------- | ------------- | ------------- |
| switch(config-acl-ip)#   |     |             | 10              | permit    | any 20.1.1.1  | 225.1.1.2     |
| switch(config-acl-ip)#   |     |             | 20              | deny      | any 30.1.1.1  | 225.1.1.3     |
| switch(config)#          |     | router      | pim             |           |               |               |
| switch(config-pim)#      |     |             | accept-register |           | access-list   | pim_reg_acl   |
| switch(config)#          |     | access-list |                 | ipv6      | pim_regv6_acl |               |
| switch(config-acl-ipv6)# |     |             |                 | 10 permit | any 20.::1    | ff1e::1       |
| switch(config-acl-ipv6)# |     |             |                 | 20 deny   | any 30::1     | ff1e::3       |
| switch(config)#          |     | router      | pim6            |           |               |               |
| switch(config-pim6)#     |     |             | accept-register |           | access-list   | pim_regv6_acl |
WhenaregisterACLisassociatedwithaPIMRouter,thePIMprotocolwillstorethesourceand
destinationaddressdetailsalongwiththeaction(permitordeny).Ifthereareanyexistingflows,the
userwillneedtodisableandenablePIMontheinterfacetoapplytheACL.Uponreceivingtheregister
messages,alookupisperformedtocheckiftheSandGinthepacketisinthepermittedlist.Ifthereis
nomatchorifthereisadenyrulematch,aregisterstopmessageisimmediatelysentandthepacketis
droppedandnofurtheractionistaken.Permittedpacketswillgothroughthenormalflow.
PIM Accept-RP
PIMAccept-RPpreventsunwantedrendezvouspointsinthePIMsparsemodedomain.Bydefault,an
RPwillacceptallmulticastgroupsinthe224.0.0.0/4range(theentireclassDrange),butifrequired,you
canconfiguretheroutertoallowonlyPIMjoin/prunemessagestowardthewantedgroups.
| switch(config)# |     | access-list |     | ip  | pim_rp_grp_acl |     |
| --------------- | --- | ----------- | --- | --- | -------------- | --- |
switch(config-acl-ip)# 10 permit any any 225.1.1.2/255.255.255.0
switch(config-acl-ip)# 20 permit any any 239.1.1.2/255.255.255.0
| switch(config)-acl-ip# |     |     | router |     | pim |     |
| ---------------------- | --- | --- | ------ | --- | --- | --- |
switch(config-pim)# accept-rp 30.1.1.1 access-list pim_rp_grp_acl
| switch(config-pim)#      |     |     | access-list |           | ip pim_rpv6_grp_acl |            |
| ------------------------ | --- | --- | ----------- | --------- | ------------------- | ---------- |
| switch(config-acl-ipv6)# |     |     |             | 10 permit | any any             | ff2e::2/64 |
| switch(config-acl-ipv6)# |     |     |             | 20 permit | any any             | ff1e::1/64 |
| switch(config-acl-ipv6)# |     |     |             | router    | pim6                |            |
switch(config-pim6)# accept-rp 30::1 access-list pim_rpv6_grp_acl
PIM SSM
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries) 55

ProtocolIndependentMulticast-Source-SpecificMulticast(PIM-SSM)usesasubsetofPIMsparsemode
andIGMPversion3(IGMPv3)/MLDversion2(MLDv2)toallowmulticastreceiverstoreceivetrafficfrom
specifiedsourceaddresses.
ThedefaultPIMSSMgrouprangeisIPv4-232.0.0.0/8andIPv6-FF3x::/32.Arangeaccesslistallowsthe
PIMroutertomodifythedefaultSSMrange
n IntheACLusedtospecifythePIM-SSMrange,ACEsshouldcontainonlymulticastgroupaddressesin
thedestinationIPfield,elsetheACEwillbeignored.
n ModifyingthePIM-SSMrangecanleadtomomentarytrafficlossuntilPIMrebuildsthestates.
n ItisrecommendedtokeeptheSSMrangethesameacrossthenetwork.
| switch(config)# |     | access-list | ip  | pim_ssm_grp_range_acl |
| --------------- | --- | ----------- | --- | --------------------- |
switch(config-acl-ip)# 10 permit any any 225.1.1.2/255.255.255.0
switch(config-acl-ip)# 20 permit any any 239.1.1.2/255.255.255.0
| switch(config)# |     | router | pim |     |
| --------------- | --- | ------ | --- | --- |
switch(config-pim)# pim-ssm range-access-list pim_ssm_grp_range_acl
| switch(config)#          |     | access-list | ipv6      | pim_ssm_v6grp_range_acl |
| ------------------------ | --- | ----------- | --------- | ----------------------- |
| switch(config-acl-ipv6)# |     |             | 10 permit | any any ff2e::2/64      |
| switch(config-acl-ipv6)# |     |             | 20 permit | any any ff1e::1/64      |
| switch(config)#          |     | router      | pim6      |                         |
switch(config-pim6)# pim-ssm range-access-list pim_ssm_v6grp_range_acl
Toviewtheconfigurationchanges,issuethecommandsshow run pimorshow run pim6.
| Securing | MSDP |     |     |     |
| -------- | ---- | --- | --- | --- |
MulticastSourceDiscoveryProtocol(MSDP)isamechanismtoconnectmultipleProtocolIndependent
Multicastsparsemode(PIM-SM)domains.MSDPallowsmulticastsourcesforagrouptobeknowntoall
rendezvouspoints(RPs)indifferentdomains.AnRPrunsMSDPoverTCPtodiscovermulticastsources
inotherdomains.ThemainadvantageofMSDPisthatitreducesthecomplexityofinterconnecting
multiplePIM-SMdomainsbyallowingPIM-SMdomainstouseaninterdomainsourcetree(ratherthana
commonsharedtree).
ToenhanceMSDPsecurity,enableMD5authenticationforbothMSDPpeerstoestablishaTCP
connection.IftheMD5authenticationfails,theTCPconnectioncannotbeestablished.
| switch(config)#      |     | router | msdp         |          |
| -------------------- | --- | ------ | ------------ | -------- |
| switch(config-msdp)# |     |        | ip msdp peer | 10.1.1.1 |
switch(config-msdp-peer)#
| switch(config-msdp-peer)# |     |               | password |     |
| ------------------------- | --- | ------------- | -------- | --- |
| Enter the                 | MD5 | password:     | ******** |     |
| Re-Enter                  | the | MD5 password: | ******** |     |
MSDPusesSA(SourceActive)messagesthatcontainS,G(SourceGroup)informationforRPs
(RendezvousPoints)inPIMsparsedomains.
Bydefault,theMSDPenabledrouterforwardsalltheSAmessages,andthepeerrouterprocessesall
thereceivedmessages.ThiscommandallowstheusertoconfigureanACLontheMSDPpeertofilterSA
messages.UsercanpreventtheincomingandoutgoingSAmessagesonMSDProuterbycreating
incomingandoutgoingfilterlistsusinganACL.
HardeningtheControlPlane|56

switch(config-msdp-peer)# sa-filter in access-list msdp_sa_filter1
switch(config-msdp-peer)# sa-filter out access-list msdp_sa_filter2

To view the configuration changes, issue the command show run msdp.

NAE Scripts

The Network Analytics Engine is a first-of-its-kind built-in framework for network assurance and
remediation. Combining the full automation and deep visibility capabilities of the AOS-CX operating
system, this unique framework enables monitoring, collecting network data, evaluating conditions, and
taking corrective actions through simple scripting agents. This engine is integrated with the AOS-CX
system configuration and time series databases, enabling to examine historical trends and predict
future problems due to scale, security, and performance bottlenecks. With that information,
administrators can create software modules that automatically detect such issues and take appropriate
action.

The following list describes the HPE Aruba Networking certified NAE scripts hosted on the Aruba
Solution Exchange. These scripts can help in hardening the switch control plane.
Table 1: HPE Aruba Networking certified NAE scripts

Module

Objective

Control Plane Policing

Spanning Tree

ARP

The purpose of this script is to
detect anomalous traffic that
is getting dropped by Control
Plane Policing.

This script monitors the STP
BPDU counters, Topology
Change Notifications (TCN)
and raise an alert if the rate of
TCN exceeds a certain
threshold value for a specified
time. It also monitors the
number of STP packets
dropped at CoPP.

The purpose of this script is to
help in monitoring the
number of ARP requests
coming to the switch CPU.

Script

copp.5.1

tp_bpdu_tcn_rate_monitor.2.0

arp_request_monitor.2.0

AOS-CX 10.14.1000 Hardening Guide | (All Switch Series)

57

|                      |     |     |     |         | Chapter | 4     |
| -------------------- | --- | --- | --- | ------- | ------- | ----- |
|                      |     |     |     | Trusted | Supply  | Chain |
| Trusted Supply Chain |     |     |     |         |         |       |
HPEisaleaderintheICT(InformationandCommunicationTechnology)industryforsupplychain
cybersecurity.HPErecognizestheimportanceofsecuresoftwareandhardwaredevelopment,enabling
theavailabilityofpartsfromtrustedsources,buildingproductswithadvancedsecurityfeatures,and
accessingdatathatisprotectedwithinsecureenvironments.
Ascybersecuritythreatsevolve,HPEcontinuestoidentifyandmitigatecybersecurityriskswithinthe
supplychainandprovidesecureproductssoyoucanconcentrateonyourbusinessgoals.
Supplychainattackscausedbymaliciousactorsinfiltratingsystemsthroughpartnersortechnology
vendorswithaccesstodataandresourcesareontherise.Mitigatingcybersecurityrisksandpreventing
attacksinthesupplychainisessentialtoprovidesecureproductsandservices.Followingarethelistof
securitybestpracticesthatcanbefollowedfromAOS-CXswitchingperspective.
n BoottheswitchinEnhancedSecureMode.
n DisabletheUSBAuxiliaryportwhennotinuse.
n DisableallphysicalinterfacesandtheOOBMportusingthefollowingcommands:
| switch(config)# | interface | <physical | interface | range> |     |     |
| --------------- | --------- | --------- | --------- | ------ | --- | --- |
| switch(config)# | disable   |           |           |        |     |     |
| switch(config)# | exit      |           |           |        |     |     |
| switch(config)# | interface | mgmt      |           |        |     |     |
| switch(config)# | shutdown  |           |           |        |     |     |
| switch(config)# | exit      |           |           |        |     |     |
n Disableallmanagementprotocols(https-server,SSH,SNMP)andforcetheconsoleintothedevice
configurationtodisablethemanagementprotocolsonalltheenabledVRFsusingthefollowing
commands:
| switch(config)# | no ssh          | server vrf | <vrf-name> |     |     |     |
| --------------- | --------------- | ---------- | ---------- | --- | --- | --- |
| switch(config)# | no https-server | vrf        | <vrf-name> |     |     |     |
| switch(config)# | no snmp-server  | vrf        | <vrf-name> |     |     |     |
n Enablepasswordcomplexitywithastrictsetofrequirements.
n EnabletheServiceOSpasswordprompt.
DisabletheCentralclientusingthefollowingcommands:
n
switch(config)#
aruba-central
| switch(config-aruba-central)# |     | disable |     |     |     |     |
| ----------------------------- | --- | ------- | --- | --- | --- | --- |
| switch(config-aruba-central)# |     | exit    |     |     |     |     |
n EnableonlyNDcPPapprovedSSHalgorithms.
58
AOS-CX10.14.1000HardeningGuide|(AllSwitchSeries)

Chapter 5

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

AOS-CX 10.14.1000 Hardening Guide | (All Switch Series)

59

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
SupportandOtherResources|60

content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.14.1000 Hardening Guide | (All Switch Series)

61