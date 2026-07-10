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

AOS-CX 4100i Release Notes

Table of contents

# Resolved Issues

This section describes the issues resolved in this release.

| Category | Bug ID | Description |
| --- | --- | --- |
| PIM‐SM | 338339 | **Symptom:** PIM RPF override with nexthop IP address is not working as expected.  **Scenario:** When RPF override is configured, the route for the nexthop must be resolved. After a Route Resolver (RR) succeeds, the system was supposed to check the routes for the nexthop IP. However, route entries were not being updated correctly. |
| SNMP | 336872 | **Symptom:** Incorrect **sysDescr** displayed in snmpwalk/get output.  **Scenario:** When a non‐default system description is configured and then reverted to the default, performing an SNMP walk or get operation may display the wrong **sysDescr**.  **Workaround:** The System Description can still be viewed using the CLI. |
| SNMP | 336469 | **Symptom:** A core dump occurs when attempting to snmpget the **dot1qPortGvrpLastPduOrigin** object.  **Scenario:** The issue occurs during the execution of an snmpget operation on the **dot1qPortGvrpLastPduOrigin** object. |
| Port Access | 333709 | **Symptom:** Interface remains down post a CoA port bounce, with interface details reason showing as **Authorization Change**.  **Scenario:** On doing a admin shut on the port during the Port‐Bounce duration, the interface continues to remain in the down state even after the port‐bounce duration.  **Workaround:** Reset the configuration to default by using the default interface <IFNAME> command. This brings the interface back up. |
| VLANS | 333372 | **Symptom:** When trying to snmpset **VlanStaticName** object, customer will see the vlan name briefly change and then change back to the old name. The name is also never updated in DB or CLI.  **Scenario:** When trying to snmpset dot1q/ieee **VlanStaticName**.  **Workaround:** Change vlan name via CLI instead of through snmpset. |
| 801.1X | 330413 | **Symptom:** The access‐clients won't be authenticated successfully via 802.1x Auth.  **Scenario:** If MAC‐Authentication is successful first and MBV is applied for client, then 802.1x EAPOL packet sent by clients won't be processed by Port‐Access daemon, as a result the 802.1x‐Auth process won't be completed.  **Workaround:** 802.1x Auth has to be triggered first before MAC‐Auth gets triggered, which can be achieved by applying appropriate auth precedence & priority and disabling concurrent auth. |
| Routing | 328738 | **Symptom:** The **Maximum 1 nexthops per route** error is displayed.  **Scenario:** When a client tried to configure more than 1 nexthop. |
| PIM‐SM | 328568 | **Symptom:** Kernel panic occurred while collecting support files at switch.  **Scenario:** When multicast traffic passing through the switch. The logs piled up over a period of time, which can result in an increased system memory consumption.  **Workaround:** Disable or enable PIM, or restart PIM daemon. |

AOS-CX 10.14.1030

Feedback

Related Products

- [HPE Aruba Networking CX 4100i Switch Series](https://support.hpe.com/connect/s/product?kmpmoid=1013625614)

Recently Viewed

- [AOS-CX 4100i Release Notes | Enhancements](?docId=sd00007142en_us&page=GUID-F993C61C-6863-43A3-B89B-F91F139C0326.html)
- [AOS-CX 4100i Release Notes | AOS-CX 10.14 Overview](?docId=sd00007142en_us&page=GUID-4D8399EE-118A-4573-9450-50A73FE1CF83_5.html)
- [AOS-CX 4100i Release Notes | 10.14.1030](?docId=sd00007142en_us&page=GUID-9AAEEB4F-0226-4A7D-BC64-CE23862B9B6E.html)

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