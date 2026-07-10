Cookie PreferencesDo Not Sell or Share My Personal Information

Close

* [GreenLake](https://common.cloud.hpe.com/)
* [My services](https://common.cloud.hpe.com/services/my-services)

GreenLake Administration

* [Manage workspace](https://common.cloud.hpe.com/manage-account)
* [Manage devices](https://common.cloud.hpe.com/devices/inventory-list)

HPE Resources

* [HPE Support Center](https://support.hpe.com/connect/s/)
* [HPE Developer Community](https://developer.hpe.com/)
* [HPE Communities](https://www.hpe.com/us/en/communities.html)

Legal & financial

* [Privacy statement](https://www.hpe.com/us/en/legal/privacy.html)
* [Cookies](https://www.hpe.com/us/en/legal/privacy.html#datacollection)
* [Terms of use](https://www.hpe.com/us/en/about/legal/terms-of-use.html)
* [Do not sell my personal info](https://www.hpe.com/us/en/privacy/personal-information.html)
* [Financial Services](https://www.hpe.com/us/en/financing-asset-management-services.html)

Close

* [HPE Account Details](https://auth.hpe.com/profile)
* [GreenLake Preferences](https://common.cloud.hpe.com/preferences-only)
* [Visit hpe.com](https://www.hpe.com/)
* Sign out of HPE

[My HPE Account](https://www.hpe.com/us/en/my-account/overview.html)

* Sign Out

Close

* [HPE Home](https://www.hpe.com/us/en/home.html)
* [GreenLake](https://www.hpe.com/us/en/greenlake.html)
* [Products and Solutions](https://www.hpe.com/us/en/products.html)
* [Services](https://www.hpe.com/us/en/services.html)
* [Company](https://www.hpe.com/us/en/about.html)
* [Support](https://support.hpe.com/connect/s/)

* [Dashboard](https://common.cloud.hpe.com/home)
* [Applications](https://common.cloud.hpe.com/applications/my-apps)
* [Devices](https://common.cloud.hpe.com/devices/inventory)
* [Manage](https://common.cloud.hpe.com/manage-account)

[**Support Center**](/connect/s/)

[Skip to main content](#dceContent)

Menu toggle

* Home

  Home

  + [HPE Support Center](/connect/s/)
  + [Workspace](/hpesc/public/home/signin?TARGET=https%3A%2F%2Fsupport.hpe.com%2Fhpesc%2Fpublic%2FdocDisplay%3FdocId%3Dsd00007259en_us%26page%3DGUID-AC7107A1-C6DF-4B39-A3E5-F94855670074.html)
* Manage

  Manage

  + [Create Case](/connect/s/createcase?client=navMenu)
  + [My Cases](/connect/s/viewcases)
  + [Parts](/connect/s/?card=parts)
  + [My Contracts](/connect/s/contracts)
  + [My Contracts Dashboard](/connect/s/contractsdashboard)
  + [Service Credits](/hpsc/credits/dash)
  + [My Groups](/connect/s/groups)
  + [My Remote Support Connections](/connect/s/myremotesupportconnections)
* Products

  Products

  + [Browse All Products](/connect/s/product)
  + [My Products](/connect/s/assets)
  + [HPE InfoSight](https://infosight.hpe.com/)
  + [HPE GreenLake Central](https://client.greenlake.hpe.com/login)
  + [Sign up for Product Alerts](https://h41360.www4.hpe.com/?country=us&language=en)
* Downloads

  Downloads

  + [Find Drivers and Software](/connect/s/search#t=DriversandSoftware)
  + [My HPE Software Center](https://myenterpriselicense.hpe.com/)
  + [Patch Management](/hpsc/patch/content?action=home)
* Knowledge

  Knowledge

  + [Find Documents](/connect/s/search#t=Documents)
  + [Tech Tips](/connect/s/search#t=Videos&f:@kmvideomarketinglabel=[Tech%20Tips])
  + [QuickSpecs](/connect/s/search#t=Documents&f:@kmdoctypedetails=[cv66000043])
  + [Manuals](/connect/s/search#t=Documents&f:@kmdoctype=[cv60000003,cv60000006])
  + [Security Bulletins](/connect/s/securitybulletinlibrary)
  + [Videos](/connect/s/search#t=Videos)
  + [Forums](/connect/s/search#t=Forums)
* Resources

  Resources

  + [My Insights Dashboards](/connect/s/insights)
  + [Warranty Check](/connect/s/warrantycheck)
  + [HPE Networking Support Portal](https://networkingsupport.hpe.com/)
  + [Import/Export Classification Data](https://wwclass-ext.it.hpe.com/wwclass_ext2/)
  + [HPE Community Forums](https://community.hpe.com/)
  + [Validate Equipment Parts](https://www.hpe.com/us/en/validate.html)
  + [Return Parts](https://hpereturn.agoraportal.com)
  + [iLO Amplifier Pack](/hpesc/ilo-amp-entitlement)
  + [HPE NonStop Registration](/connect/s/nonstopregistration)

[Support Center](/connect/s/)

You have no new notifications.

Help

* Light Mode[ ]
* United States - English
* [Sign In](/hpesc/public/home/signin?TARGET=https%3A%2F%2Fsupport.hpe.com%2Fhpesc%2Fpublic%2FdocDisplay%3FdocId%3Dsd00007259en_us%26page%3DGUID-AC7107A1-C6DF-4B39-A3E5-F94855670074.html)

Search HPE Support

Manage privacy and data collection on HPE.com

English

0 result(s) found

No result found

AOS-CX 10000 Release Notes

Table of contents

# Feature Caveats

The following are feature caveats that should be taken into consideration when using this version of the software.

| Feature | Description |
| --- | --- |
| BGP | When configuring the same BGP neighbor under both IPv4 and IPv6 address families on a router, if a maximum prefix limit is set on one address family (like IPv4), exceeding that limit can potentially impact the BGP session for the other address family (IPv6) as well. |
| Activate | If there is no user configuration for DNS servers and HPE Aruba Networking Central is configured, the switch defaults to using Google's DNS server at 8.8.8.8. HPE Aruba Networking Central is enabled by default across all switch platforms. |
| BGP | The **next‐hop‐unchanged** option needs to be explicitly configured to preserve nexthop while advertising routes to eBGP peers, in the L2VPN EVPN address‐family. For example:   ```  Copy  router bgp  neighbor 1.1.1.1 remote‐as 2 address‐family l2vpn evpn neighbor 1.1.1.1 activate neighbor 1.1.1.1 next‐hop‐unchange neighbor 1.1.1.1 send‐community extended ```  exit‐address‐family |
| Central | When a switch can connect to HPE Aruba Networking Central but is not registered in the inventory or lacks a proper license, it will repeatedly disconnect and reconnect. This cycle will continue until the switch is properly registered or a license is obtained. To avoid this unnecessary reconnection cycle, it is best practice to disable HPE Aruba Networking Central until the switch is registered or a license is obtained. |
| Certificates | When a switch uses a certificate with a legacy certificate name that is not supported in 10.12 because it contains disallowed characters, the information will migrate properly in the upgrade, but that certificate can no longer be edited. For new certificate names, only alphanumeric characters, dots, dashes, and underscores are allowed. |
| Classifiers | Policies containing both MAC and IPv6 classes are not allowed. |
| Classifiers | For secure classifier policy modifications, HPE Aruba Networking strongly encourages a three‐step process: bring down the port, make the modifications, and then bring the port back up. |
| Classifiers | Egress ACL logging is not supported. |
| Classifiers | IPv4 egress ACLs can be applied only to route‐only ports. |
| Classifiers | Classifier policies, IPv6 and MAC ACLs are not supported on egress. |
| CMF | No other checkpoint besides "startup‐configuration" gets migrated during the upgrade process. |
| Counters | Layer 3 Route‐only port counters are not enabled by default. Enabling them will reduce ipv4 route scale to 80K. |
| DHCP Server, DHCP Relay, and DHCP Snooping | DHCP Relay and DHCP Snooping can co‐exist on the same switch. DHCP Snooping and DHCP Server cannot co‐exist on the same switch. DHCP Snooping, DHCP Relay, and DHCP Server together cannot co‐exist on the same switch. |
| Hot Patch | When downloading a hot‐patch file using the switch WebUI, log messages may incorrectly state that the file is added to the database with a **missing** status. This is a temporary state, and will correctly change to **Not applied** once the download is completed. |
| ICMP Redirect | The switch may incorrectly duplicate an IP frame that triggers ICMP redirect. |
| IGMP/PIM on 6‐in‐6, Loopback and GRE interfaces | IGMP cannot be enabled on either Loopback or GRE interfaces. IGMP and PIM is not supported on a 6‐in‐6 Tunnel. |
| IP‐SLA | Do not use reserved ports or ports used by other applications/services for different services. When two services use the same port, unexpected behaviors may occur. Best practice is to assign a unique port for each service across the system. |
| Multicast | Multicast traffic cannot be run under GRE, 6in4, or 6in6 tunnels. |
| MVRP and VSX | MVRP is mutually exclusive with VSX. |
| Network Analytics Engine (NAE) | Network Analects Engine (NAE) agents execute Command Line Interface (CLI) actions as 'admin' user, so they have permission to run any command by default. However, when the authentication, authorization and accounting (AAA) feature is enabled, the same restrictions applied to 'admin' will also apply to NAE agents. When using AAA, make sure to give the admin user the permissions to run all commands needed by enabled NAE agents. Otherwise, some CLI commands may be denied and their outputs won't be available. Actions other than CLI won't be affected and will execute normally. Also, NAE agents won't authenticate, thus the AAA service configuration must not block authorization for unauthenticated 'admin' user. ClearPass doesn't support such configuration, so it cannot be used as a TACACS+ server. |
| Network Analytics Engine (NAE) | The following tables are not supported for NAE scripts: OSPF\_Route, OSPF\_LSA, OSPF\_Neighbor, BGP\_Route. |
| Network Analytics Engine (NAE) | Agents monitoring a resource that has column type enum with a list of strings (as opposed to a single string enum) is not supported. |
| OSPF | OSPFv2 and OSPFv3 do not support detailed LSA **show** commands. |
| PIM‐SM | Pim Active‐Active is not supported on overlay VXLAN SVIs. |
| Port Access | Port Access (802.1x, MAC Authentication, Device Profile), Port Security, IPv4/v6 Source Lockdown, Dynamic ARP Inspection and/or DHCPv4/v6 Snooping configurations are mutually exclusive with PSM stateful firewall policies. |
| REST | REST supports the 'admin' and 'operator' roles but does not work with TACACS+ command authorization. |
| RIP/RIPng | Redistribute RIP/RIPng is not supported in BGP/BGP+. |
| RPVST+ and MSTP | Spanning Tree can only run in MSTP or RPVST+ mode. |
| RPVST+ and MVRP | RPVST+ is mutually exclusive with MVRP. |
| SNMP | When SNMP is enabled via the switch CLI, it can take between 1‐2 minutes for the SNMP daemon to be ready to respond to requests. If a local or external SNMP MIB walk is performed in the interval between when SNMP is first enabled and the SNMP daemon is ready, the MIB walk action will return an error. |
| Stateful L4 firewall | Stateful services for VRFs, where route leaking is enabled, are not supported. |
| Stateful L4 firewall | Port‐access (802.1x, MAC authentication, Device Profile), Port‐security, DHCP v4/v6 snooping, Dynamic ARP Inspection and/or IPv4/v6 Source Lockdown configurations are mutually exclusive with PSM Stateful firewall policies |
| Stateful L4 firewall | For locally‐switched and routed flows on the switch, the traffic from the host is subject to policy processing only once and only egress policy is enforced on the traffic egressing the workload and entering the switch. |
| Sub‐interface | BFD is not supported on a sub‐interface. A sub‐interface as underlay for EVPN‐VXLAN is not supported |
| Traceroute | Issuing the **traceroute** command with the i**p‐option loosesourceroute** parameter fails in an overlay EVPN‐VXLAN deployment. |
| Traceroute | Traceroute v4/v6 over VXLAN fails to find intermediate next‐hop IP information from a source VTEP in Virtual Active Gateway environment (the SVI is the same as theActive Gateway IP). |
| VRF | VRF names are limited to 31 characters. |
| VRRP‐MD5 authentication interop | Not supported with Comware‐based switches |
| VRRP and VXLAN | VRRP and VXLAN are mutually exclusive. |
| VRRP | VRRP Preemption Delay Timer (preempt delay minimum) may be ignored after a switch reboot or power cycle. |
| VxLAN‐Underlay‐Mcast‐Replication | Overlay flood and overlay multicast traffic loss may occur in underlay multicast VxLAN replication mode.  In a 3‐clos data center design when there is link failure between the VTEP and the spine, the underlay multicast routing path towards the RP picks up a leaf VTEP as a transit router, which can cause traffic loss. |
| VxLAN‐Underlay‐Mcast‐Replication | Overlay flood and overlay multicast traffic loss may occur in underlay multicast VxLAN replication mode.  In a medium and small campus deployment with Underlay RP placement at any VTEP or Aggregate with PIM‐BIDIR, traffic loss will be observed due to a bud node scenario. |
| VxLAN‐Underlay‐Mcast‐Replication | Overlay flood and overlay multicast traffic loss may occur in underlay multicast VxLAN replication mode.  In a 3‐clos data center design when there is link failure between the VTEP and the spine, the underlay multicast routing path towards the RP picks up a leaf VTEP as a transit router, which can cause traffic loss. |
| VXLAN | IPV6 vxlan Tunnels on 8325/8325P and 10000 Switch series are supported with only ROP ports as an underlay. MCLAG or LAG as an underlay is not supported. |
| VXLAN | VXLAN must be configured prior to configuring VSX. |
| ZTP | The Vendor Class Identifier (VCI) for the switch can be obtained using the command **show dhcp client vendor‐class‐identifier**. There is a change in the VCI output of the 10000 switch from 10.15 onwards:   * **10.14 VCI**: Aruba R8S96A Aruba * **10.15 VCI**:Aruba R8S96A 10000   If ZTP is used by customers on 10000 platform, then the new VCI needs to be updated in the DHCP server configurations from 10.15 release onwards. |

## Client Insights Supportability Matrix

The Client Insights information available on each switch varies by model type. The following features can share information with Client Insights.

| Platform | Port‐Access support | DHCP‐Snooping support | ARP‐GW onboarding support | Traffic Insight ‐‐ DNS Onboarding | Traffic Insight ‐‐ DNS avg latency |
| --- | --- | --- | --- | --- | --- |
| 8400 | No | Yes | No | No | No |
| 10000 | Yes | Yes | No | No | No |
| 10040 | Yes | Yes | No | No | No |
| 6000 | Yes | Yes | No | No | No |
| 6100 | Yes | Yes | No | No | No |
| 6200 | Yes | Yes | No | No | No |
| 4100i | Yes | Yes | No | No | No |
| 6300M/F | Yes | Yes | Yes | Yes | Yes |
| 6300L | Yes | Yes | No | No | No |
| 6400 | Yes | Yes | Yes | Yes | Yes |
| 8325/8325H/8325P | Yes | Yes | No | No | No |
| 8360 | Yes | Yes | No | No | Yes |
| 8100 | Yes | Yes | No | No | No |
| 5420 | Yes | Yes | No | No | No |

AOS-CX 10.16.1006

Feedback

Related Products

- [HPE Aruba Networking CX 10000 Switch Series](https://support.hpe.com/connect/s/product?kmpmoid=1014368376)

Recently Viewed

- [AOS-CX 10000 Release Notes | Resolved Issues](?docId=sd00007259en_us&page=GUID-0C33B4D7-8518-47DA-BF19-1E6405577FF2.html)
- [AOS-CX 10000 Release Notes | Enhancements](?docId=sd00007259en_us&page=GUID-A6855702-7C15-4CB0-91D8-02005DCE04F7.html)
- [AOS-CX 10000 Release Notes | Overview](?docId=sd00007259en_us&page=GUID-9CADAF31-BE45-4D8B-A55D-071F31256652_5.html)

View more

On This Page

* [Feature Caveats](#ariaid-title1)
  + [Client Insights Supportability Matrix](#client-insights-supportability-matrix-1)

Related Products

Recently Viewed

On This Page

**Legal Disclaimer:** Products sold prior to the November 1, 2015 separation of Hewlett-Packard Company into Hewlett Packard Enterprise Company and HP Inc. may have older product names and model numbers that differ from current models.Hewlett Packard Enterprise believes in being unconditionally inclusive. Efforts to replace noninclusive terms in our active products are ongoing.

[How to buy](https://www.hpe.com/us/en/buy-parts-products.html)[Product support](https://support.hpe.com/connect/s/)[Email sales](https://www.hpe.com/us/en/contact-hpe.html)

Follow HPE on

Company

[About HPE](https://www.hpe.com/us/en/about.html)[Accessibility](https://www.hpe.com/us/en/about/accessibility-aging.html)[Careers](https://careers.hpe.com/us/en)[Corporate responsibility](https://www.hpe.com/us/en/living-progress.html)[HPE Labs](https://www.hpe.com/us/en/hpe-labs.html)[HPE Modern Slavery Transparency Statement (PDF)](https://www.hpe.com/psnow/doc/a00005807enw?jumpid=in_pdfviewer-psnow)[Investor relations](https://investors.hpe.com/)[Leadership](https://www.hpe.com/us/en/leadership.html)[Public policy](https://www.hpe.com/us/en/living-progress/political-engagement-advocacy.html)

Support

[OEM Solutions](https://www.hpe.com/us/en/oem.html)[Product return and recycling](https://www.hpe.com/us/en/about/environment/product-recycling.html)[Product support](https://support.hpe.com/hpesc/public/home)[Software and drivers](https://myenterpriselicense.hpe.com/cwp-ui/auth/login)[Warranty check](https://support.hpe.com/connect/s/warrantycheck)

Events and news

[Events](https://www.hpe.com/us/en/events.html)[HPE Discover](https://www.hpe.com/us/en/events/discover-events.html)[Local events](https://www.hpe.com/h22166/Calendar_hpe.aspx?cc=us&lang=en)[Newsroom](https://www.hpe.com/us/en/newsroom.html)

Customer resources

[Contact Us](https://www.hpe.com/us/en/contact-hpe.html)[Education and training](https://education.hpe.com/us/en/training/index.html)[Email signup](https://explore.hpe.com/email-preference-center.html?language=en)[Enterprise glossary](https://www.hpe.com/us/en/what-is.html)[Financial services](https://www.hpe.com/us/en/financing-asset-management-services.html)[HPE communities](https://community.hpe.com/)[HPE customer centers](https://www.hpe.com/us/en/about/customer-centers.html)[HPE sign in](https://auth.hpe.com/)[Voice of the Customer signup](https://www.hpe.com/h41268/live/index_e.aspx?qid=29244)

Partners

[Alliances](https://www.hpe.com/us/en/alliance.html)[Certifications](https://certification-learning.hpe.com/TR/Index.html)[Find a partner](https://partnerconnect.hpe.com/partners)[Partner programs](https://www.hpe.com/us/en/partners/partner-ready-vantage.html)

© Copyright 2026 Hewlett Packard Enterprise Development LP

* [Privacy](https://www.hpe.com/us/en/legal/privacy.html)
* [Terms of Use](https://www.hpe.com/us/en/about/legal/terms-of-use.html)
* [Ad Choices & Cookies](https://www.hpe.com/us/en/legal/privacy.html#datacollection)
* [Do not Sell my Personal Information](https://www.hpe.com/us/en/privacy/personal-information.html)