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

# Performing the software upgrade

## About this task

For additional upgrade and downgrade scenarios, including limitations of automatic upgrade and downgrade scenarios provided by the Configuration Migration Framework (CMF), refer to the [AOS-CX 10.14 Fundamentals Guide](https://arubanetworking.hpe.com/techdocs/AOS-CX/help_portal/Content/home.htm).

CAUTION

This version may contain a change of BootROM from the current running version. A BootROM update is a non-failsafe update. Do not interrupt power to the switch during the update process or the update could permanently damage the device.

## Procedure

1. Copy the new image into the non-current boot bank on the switch using your preferred method.
2. Depending on the version being updated, there may be device component updates needed. Preview any devices updates needed using the `boot system <BOOT-BANK>`  command and entering `n` when asked to continue.

   For example, if you copied the new image to the secondary boot bank and no device component updates are needed, you will see this:

   ```
   Copy

   switch# boot system secondary
   Default boot image set to secondary.
   Checking if the configuration needs to be saved...
   Checking for updates needed to programmable devices...
   Done checking for updates.
   This will reboot the entire switch and render it unavailable
   until the process is complete.
   Continue (y/n)? n
   ```

   In this example, three device updates will be made upon reboot, one of which is a non-failsafe device:

   ```
   Copy

   switch# boot system secondary
   Default boot image set to secondary.
   Checking if the configuration needs to be saved...
   Checking for updates needed to programmable devices...
   Done checking for updates.
   2 device(s) need to be updated during the boot process.
   The estimated update time is between 2 and 3 minute(s).
   There may be multiple reboots during the update process.
   1 non-failsafe device(s) also need to be updated.
   Please run the 'allow-non-failsafe-updates' command to enable these updates.
   This will reboot the entire switch and render it unavailable
   until the process is complete.
   Continue (y/n)? n
   ```
3. When ready to update the system, if a non-failsafe device update is needed, make sure the system will not have any power interruption during the process. Invoke the `allow non-failsafe updates` command to allow updates to proceed after a switch reboot. Proceed to step 4 within the configured time.

   ```
   Copy

   switch# config
   switch(config)# allow-non-failsafe-updates 30
   This command will enable non-failsafe updates of programmable devices for
   the next 30 minutes.  You will first need to wait for all line and fabric
   modules to reach the ready state, and then reboot the switch to begin
   applying any needed updates.  Ensure that the switch will not lose power,
   be rebooted again, or have any modules removed until all updates have
   finished and all line and fabric modules have returned to the ready state.
   WARNING: Interrupting these updates may make the product unusable!
   Continue (y/n)? y
       non-failsafe updates      : allowed (less than 30 minute(s) remaining)
   ```
4. Use the boot system <BOOT-BANK> command to initiate the upgrade. On the switch console port an output similar to the following will be displayed as various components are being updated:

   ```
   Copy

   switch# boot system secondary
   Default boot image set to secondary.
   Checking if the configuration needs to be saved...
   Checking for updates needed to programmable devices...
   Done checking for updates.
   3 device(s) need to be updated during the boot process.
   The estimated update time is between 2 and 3 minute(s).
   There may be multiple reboots during the update process.
   This will reboot the entire switch and render it unavailable
   until the process is complete.
   Continue (y/n)? y
   The system is going down for reboot.
   Looking for SVOS.
   Primary SVOS:  Checking...Loading...Finding...Verifying...Booting...
   ServiceOS Information:
       Version:          <serviceOS_number>
       Build Date:       yyyy-mm-dd hh:mm:ss PDT
       Build ID:         ServiceOS:<serviceOS_number>:6303a2a501ba:202006171659
       SHA:              6303a2a501bad91100d9e71780813c59f19c12fe
   Boot Profiles:
   0. Service OS Console
   1. Primary Software Image [xx.10.13.1000]
   2. Secondary Software Image [xx.10.14.0001]
   Select profile(secondary):
   ISP configuration:
       Auto updates        : enabled
       Version comparisons : match (upgrade or downgrade)
       non-failsafe updates      : allowed (less than 29 minute(s) remaining)
   Advanced:
       Config path         : /fs/nos/isp/config [DEFAULT]
       Log-file path       : /fs/logs/isp [DEFAULT]
       Write-protection    : disabled [DEFAULT]
       Package selection   : 0 [DEFAULT]
   3 device(s) need to be updated by the ServiceOS during the boot process.
   The estimated update time by the ServiceOS is 2 minute(s).
   There may be multiple reboots during the update process.
   MODULE 'mc' DEVICE 'svos_primary' :
       Current version  : '<serviceOS_number>'
       Write-protected  : NO
       Packaged version : '<version>'
       Package name     : '<svos_package_name>'
       Image filename   : '<filename>.svos'
       Image timestamp  : 'Day Mon dd hh:mm:ss yyyy'
       Image size       : 22248723
       Version upgrade needed
   Starting update...
   Writing...    Done.
   Erasing...    Done.
   Reading...    Done.
   Verifying...  Done.
   Reading...    Done.
   Verifying...  Done.
   Update successful (0.5 seconds).
   reboot: Restarting system
   ```

## Results

Multiple components may be updated and several reboots will be triggered during these updates. When all component updates are completed, the switch console port will arrive at the login prompt with a display similar to following:

```
Copy

(C) Copyright 2017-2024 Hewlett Packard Enterprise Development LP
                      RESTRICTED RIGHTS LEGEND
 Confidential computer software. Valid license from Hewlett Packard Enterprise
 Development LP required for possession, use or copying. Consistent with FAR
 12.211 and 12.212, Commercial Computer Software, Computer Software
 Documentation, and Technical Data for Commercial Items are licensed to the
 U.S. Government under vendor's standard commercial license.
We'd like to keep you up to date about:
  * Software feature updates
  * New product announcements
  * Special events
Please register your products now at: https://asp.arubanetworks.com
switch login:
```

NOTE

Aruba recommends waiting until all upgrades have completed before making any configuration changes.

AOS-CX 10.14.xx

Feedback

Related Products

- [HPE Aruba Networking CX 9300 Switch Series](https://support.hpe.com/connect/s/product?kmpmoid=1014667999)

Recently Viewed

- [AOS-CX 9300 Release Notes | Manual configuration restore for software downgrade](?docId=sd00007257en_us&page=GUID-310C66DC-0837-4821-98DE-3CF7D44B9EDB_30.html)
- [AOS-CX and NetEdit Compatibility Matrix | AOS-CX and NetEdit Compatibility](?docId=sd00007737en_us&page=GUID-4B0F6B97-9F0B-4027-B4A4-CC86BDDE4920.html)
- [AOS-CX 9300 Release Notes | Important information](?docId=sd00007257en_us&page=GUID-A419327A-EB91-4071-A47C-36CF2B4A0FFA_6.html)

View more

On This Page

* [Performing the software upgrade](#ariaid-title1)
  + [About this task](#about-this-task-1)
  + [Procedure](#procedure-2)
  + [Results](#results-3)

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