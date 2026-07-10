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

0 result(s) found

No result found

AOS-CX 10000 Release Notes

Table of contents

# Known Issues

The following are known open issues with this branch of the software. The **Symptom** statement describes what a user might experience if this is seen on the network. The **Scenario** statement provides additional environment details and trigger summaries. When available, the **Workaround** statement provides a workaround to the issue.

| Category | Bug ID | Description |
| --- | --- | --- |
| IGMP | 341085 | **Symptom**: Multicast traffic is being blocked after upgrading from AOS‐CX 10.12.0006 or earlier versions of AOS‐CX.  **Scenario**: If the switch has a control plane ACL configured AND has IGMP or PIM configured on a pre‐10.12.1000 build and upgrades to 10.12.1000 or a later release, the implicit **deny** in the control plane ACL will block multicast traffic thus inhibiting functionality of those features.  **Workaround**: Manually add an ACE to the control plane ACL to explicitly permit multicast traffic. |
| VXLAN | T‐1223 | **Symptom**: North‐South or South‐North traffic cannot be inspected.  **Scenario**: This issue occurs on 10000 Series switches that support VRF to VRF traffic with firewall inspection.  **Workaround**: Leak the inter‐vrf traffic on borders (without firewall enabled) and inspect them on non‐border VTEPs. |
| **VXLAN** | **T‐1244** | **Symptom**: There is no support for application ALG for the firewall.  **Scenario**: Applications that use multiple ports (UDP/TCP) and ports are dynamically negotiated will be affected. |
| VXLAN | T‐1245 | **Symptom**; fLocal proxy ARP cannot be disabled per VLAN.  **Scenario**: Deployments that require local proxy ARP. |
| IPFIX | T‐3801 | **Symptom**: External collectors that consume the **InputInt** field from IPFIX data packets will display an input interface value of **0**.  **Scenario**: For routed traffic that is monitored by Ipfix, the exported data packets will contain a value of zero (**0**) in the **InputInt** field.  **Workaround**: Switched traffic that is monitored by IPFIX observes the correct InputInt value in exported data collections. |
| Port | T‐1013 | **Symptom**: A port with AOC15 SFP might not link up after a link flap.  **Scenario**: If AOC15 SFP is used, and there are multiple port flaps, then there is a chance that the port might not link up.  **Workaround**: Recover from this issue by issuing the commands **shut** and **no shut** on the port. |
| IPSEC | T‐3412 | **Symptom**: DSCP classification will not work with IPSec.  Scenario: This issue is observed in a deloyment with anIPSec tunnel is configured between two 10000 Switch series in no\_ha mode. |
| L3 addressing | T‐3012 | **Syymptom**: There may be a delay in the programming of IPsec tunnels after a switch reboot.  **Scenario**: A Higher SVI scale with IPsec tunnel may increase traffic convergence time upon system reboot. |

AOS-CX 10.13.0010

Feedback

Recently Viewed

- [AOS-CX 10000 Release Notes | Feature Caveats](?docId=sd00007259en_us&page=GUID-80D84EE7-58C7-4460-AF44-22A699F6D5C0.html)
- [AOS-CX 10000 Release Notes | Resolved Issues](?docId=sd00007259en_us&page=GUID-57A54A58-0FF9-4B59-A1E4-37C5352C3FFD.html)
- [AOS-CX 10000 Release Notes | Enhancements](?docId=sd00007259en_us&page=GUID-AE92B0EB-57CD-41B7-BDF1-1A67CFA97788.html)

View more

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