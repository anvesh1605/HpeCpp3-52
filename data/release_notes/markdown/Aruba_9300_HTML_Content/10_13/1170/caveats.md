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

English

0 result(s) found

No result found

AOS-CX 9300 Release Notes

Table of contents

# Feature Caveats

The following are feature caveats that should be taken into consideration when using this version of the software.

| Feature | Description |
| --- | --- |
| Central | When a switch is able to connect to Aruba Central but is not registered in the Aruba Central inventory or does not have a proper license, the switch will get disconnected. If the Aruba Central feature is enabled using this command, the switch will then reconnect back to Aruba Central and will get disconnected again. This connect/disconnect process will continue until the switch is properly registered in Aruba Central. To avoid this unnecessary reconnection cycle, best practices is to disable Aruba Central until the switch is registered in Aruba Central, or a license is obtained for that device. |
| Hot Patch | When a hot‐patch file download is triggered using the switch WebUI, log messages can incorrectly state that the file is added to the database with a **missing** status. This is a temporary state, and will correctly change to **Not applied** once the download is completed. |
| PIM‐SM | Pim Active‐Active is not supported on overlay VXLAN SVIs. |
| SNMP | When SNMP is enabled via the switch CLI, it can take between 1‐2 minutes for the SNMP daemon to be ready to respond to requests. If a local or external SNMP MIB walk is performed in the interval between when SNMP is first enabled and the SNMP daemon is ready, the MIB walk action will return an error. |
| Certificates | When a switch uses a certificate with a legacy certificate name that is not supported in 10.12 because it contains disallowed characters, the information will migrate properly in the upgrade, but that certificate can no longer be edited. For new certificate names, only alphanumeric characters, dots, dashes, and underscores are allowed. |
| Classifiers | For Classifier policy modifications to be secure, Aruba strongly encourages modifications be done as a three‐step process: Bring down the port, modify, and bring the port back up. |
| Classifiers | Policies containing both MAC and IPv6 classes are not allowed. |
| CMF | No other checkpoint besides "startup‐configuration" gets migrated during the upgrade process. |
| DHCP Server, DHCP Relay, and DHCP Snooping | DHCP Relay and DHCP Snooping can co‐exist on the same switch.  DHCP Snooping and DHCP Server cannot co‐exist on the same switch.  DHCP Snooping, DHCP Relay, and DHCP Server together cannot co‐exist on the same switch. |
| IP‐SLA | Reserved ports or ports used by other applications/services with in the system are not recommended to be used for other services. When two services use the same port there is chance of unexpected behaviors from these services. Best practices is to use unique port for each service across system. |
| IGMP/PIM on 6‐in‐6, Loopback and GRE interfaces | IGMP cannot be enabled on either Loopback or GRE interfaces. IGMP and PIM is not supported on a 6‐in‐6 Tunnel. |
| Multicast | Multicast traffic cannot be run under GRE, 6in4, or 6in6 tunnels. |
| Multicast and VXLAN | * VXLAN must be configured prior to configuring VSX. * Multicast support for static VXLAN in the overlay has limited support. Contact Aruba Support for details. |
| PFC | Priority‐based flow control (PFC) is not supported on a split port. |
| REST | REST supports the 'admin' and 'operator' roles but does not work with TACACS+ command authorization. |
| Tunnels | When configuring tunnels (VXLAN/IP tunnels) with the underlay as a static route, the next‐hop IP should be an SVI or ROP IP and not configured as the Active‐Gateway. |
| Traceroute | Issuing the **traceroute** command with the i**p‐option loosesourceroute** parameter fails inan overlay EVPN‐VxLAN deployment. |
| Traceroute | Traceroute v4/v6 over VXLAN fails to find intermediate next‐hop IP information from a source VTEP in Virtual Active Gateway environment (the SVI is the same as theActive Gateway IP). |
| GRE | A GRE tunnel in an access‐VLAN underlay is not supported in a non‐default VRF. |
| SNMP | Overlay/system partition information is included in HOST-RESOURCES-MIB polling. The overlay partition is a read-only partition and this is reflected in SNMP queries. hrFSAccess.3 = readOnly(2) is expected behavior for overlay partitions. Monitoring tools should not treat this as an error. |

AOS-CX 10.13.1170

Feedback

Related Products

- [HPE Aruba Networking CX 9300 Switch Series](https://support.hpe.com/connect/s/product?kmpmoid=1014667999)

Recently Viewed

- [AOS-CX 9300 Release Notes | Resolved Issues](?docId=sd00007257en_us&page=GUID-55F6E148-F33E-4B8F-AD31-DBB63790EB49.html)
- [AOS-CX 9300 Release Notes | Enhancements](?docId=sd00007257en_us&page=GUID-28A1C906-01D1-4F99-9C87-374EF16D9B3D.html)
- [AOS-CX 9300 Release Notes | Overview](?docId=sd00007257en_us&page=GUID-18C49221-BDBD-41EE-9455-4D60A0137399.html)

View more

Related Products

Recently Viewed

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