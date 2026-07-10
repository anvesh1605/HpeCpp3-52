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

# Important information

NOTE

Starting with AOS-CX 10.12.0001, the Administrative Distance (AD) for EBGP learned EVPN address family routes has been corrected to 20. This change in behavior could affect the best path selected. After upgrading the switches to AOS-CX 10.12.0001 or later versions, configurations that effect route selection for route-maps and route redistribution might require modifications.

NOTE

Aruba switches covered by this release note use eMMC or SSD storage. This is non-volatile memory for persistent storage of configuration, files, databases, scripts, and so forth.

To avoid damage to your equipment, do not interrupt power to the switch during a software update.

NOTE

Clear the browser cache after upgrading to this version of software before logging into the switch using a Web UI session. This will ensure the Web UI session downloads the latest changes. Do not upgrade to AOS-CX 10.14 using REST API or WebUI unless your switch is running AOS-CX 10.09.1060,10.10.1020 or later versions of these releases.

NOTE

Switch fans will run at full speed when a fault is detected with the temperature sensors in the switch. This is normal behavior to ensure overheating does not occur. Should the fans run at full speed at unexpected times, check the output of **show environment temperature** , then contact support for further assistance.

**AOS-CX 10.14 is a Short Supported Release (SSR).**

* SSRs are short lived releases where Aruba will introduce new features and new hardware. This release will not be the last major release supported for any hardware model.
* AOS-CX SSR support period: Initial Release + 1 year.
* The End of Maintenance (EOM\*) and End of Support (EOST) will be the same date.

For information about Short Supported Releases (SSRs) and Long Supported Releases (LSRs), see <https://www.arubanetworks.com/support-services/end-of-life/arubaos-software-release/>.

**Subtopics**

* **[Industry and Government Certifications](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007257en_us&page=GUID-CA452887-D9FB-441B-934B-187BD908CCEE_47.html)**
* **[License Written Offer](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007257en_us&page=GUID-3B42CABE-63D4-49EE-AC05-4301613A657B_47.html)**
* **[Version history](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007257en_us&page=GUID-7D4A9E7E-2091-488E-9163-4CAE9EE3EA49_14.html)**

Feedback

Recently Viewed

- [AOS-CX 9300 Release Notes | Products Supported](?docId=sd00007257en_us&page=GUID-D37E58AE-1783-4D00-9D6A-DD3B583955C8_22.html)
- [AOS-CX 9300 Release Notes | Upgrade information](?docId=sd00007257en_us&page=GUID-10C07EC7-78E1-4EA3-86AA-BEFFBAD60673_14.html)
- [AOS-CX 9300 Release Notes | Compatibility/interoperability](?docId=sd00007257en_us&page=GUID-9EEAE0B9-9C02-4BC9-843E-133035A2BC5D_23.html)

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