AOS-CX 10.10 Security Guide

8320, 8325, 8400, 9300, 10000 Switch Series

Published: April 2023

Version: 4

Copyright Information

© Copyright 2024 Hewlett Packard Enterprise Development LP.

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

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

3

Contents
| About this                                              | document                               |            | 9   |
| ------------------------------------------------------- | -------------------------------------- | ---------- | --- |
| Applicableproducts                                      |                                        |            | 9   |
| Latestversionavailableonline                            |                                        |            | 9   |
| Commandsyntaxnotationconventions                        |                                        |            | 9   |
| Abouttheexamples                                        |                                        |            | 10  |
| Identifyingswitchportsandinterfaces                     |                                        |            | 10  |
| Identifyingmodularswitchcomponents                      |                                        |            | 11  |
| About security                                          |                                        |            | 12  |
| AboutAuthentication,Authorization,andAccounting(AAA)    |                                        |            | 12  |
| Managing                                                | local users                            | and groups | 13  |
| Defaultuseradmin                                        |                                        |            | 13  |
|                                                         | Exampleoffirstloginwithpasswordsetting |            | 13  |
| Built-inusergroupsandtheirprivileges                    |                                        |            | 13  |
| User-definedusergroups                                  |                                        |            | 14  |
| Usernamerequirements                                    |                                        |            | 14  |
| Passwordrequirements                                    |                                        |            | 15  |
| Userandusergroupmanagementtasks                         |                                        |            | 15  |
| ResettingtheswitchadminpasswordusingtheServiceOSconsole |                                        |            | 16  |
Resettingtheadminpasswordbyrevertingtheswitchtofactorydefaults 17
| Userandgroupcommands |                            |     | 18  |
| -------------------- | -------------------------- | --- | --- |
|                      | user                       |     | 18  |
|                      | user-group                 |     | 20  |
|                      | userpassword               |     | 24  |
|                      | serviceexport-password     |     | 26  |
|                      | showuser-group             |     | 27  |
|                      | showuserinformation        |     | 28  |
|                      | showuser-list              |     | 29  |
| SSH server           |                            |     | 32  |
| SSHdefaults          |                            |     | 32  |
| SSHservertasks       |                            |     | 32  |
| SSHservercommands    |                            |     | 33  |
|                      | showsshhost-key            |     | 33  |
|                      | showsshserver              |     | 34  |
|                      | showsshserversessions      |     | 37  |
|                      | sshciphers                 |     | 39  |
|                      | sshhost-key                |     | 40  |
|                      | sshhost-key-algorithms     |     | 41  |
|                      | sshkey-exchange-algorithms |     | 42  |
|                      | sshknown-hostremove        |     | 43  |
|                      | sshmacs                    |     | 44  |
|                      | sshmaximum-auth-attempts   |     | 45  |
|                      | sshpublic-key-algorithms   |     | 46  |
|                      | sshservervrf               |     | 47  |
| SSH client           |                            |     | 49  |
| SSHclientcommands    |                            |     | 49  |
4
AOS-CX10.10SecurityGuide| (832x,8400,9300,10000SwitchSeries)

|                                                           | ssh(clientlogin)                         |         | 49  |
| --------------------------------------------------------- | ---------------------------------------- | ------- | --- |
| Local                                                     | AAA                                      |         | 51  |
| LocalAAAdefaultsandlimits                                 |                                          |         | 51  |
| Localauthentication                                       |                                          |         | 51  |
|                                                           | Password-basedlocalauthentication        |         | 51  |
|                                                           | SSHpublickey-basedlocalauthentication    |         | 52  |
|                                                           | Localauthenticationtasks                 |         | 52  |
| Localauthorization                                        |                                          |         | 54  |
|                                                           | Localauthorizationtasks                  |         | 54  |
| Localaccounting                                           |                                          |         | 54  |
|                                                           | Localaccountingtasks                     |         | 55  |
| Local                                                     | AAA commands                             |         | 56  |
| aaaaccountingall-mgmt                                     |                                          |         | 56  |
| aaaauthenticationconsole-login-attempts                   |                                          |         | 57  |
| aaaauthenticationlimit-login-attempts                     |                                          |         | 59  |
| aaaauthenticationlogin                                    |                                          |         | 60  |
| aaaauthenticationminimum-password-length                  |                                          |         | 61  |
| aaaauthorizationcommands(local)                           |                                          |         | 62  |
| showaaaaccounting                                         |                                          |         | 64  |
| showaaaauthentication                                     |                                          |         | 65  |
| showaaaauthorization                                      |                                          |         | 66  |
| showsshauthentication-method                              |                                          |         | 68  |
| showuser                                                  |                                          |         | 68  |
| sshpassword-authentication                                |                                          |         | 69  |
| sshpublic-key-authentication                              |                                          |         | 70  |
| userauthorized-key                                        |                                          |         | 71  |
| Remote                                                    | AAA with                                 | TACACS+ | 73  |
| Defaultservergroups                                       |                                          |         | 73  |
| RemoteAAA(TACACS+)defaultsandlimits                       |                                          |         | 73  |
| Aboutglobalversusper-TACACS+serverpasskeys(sharedsecrets) |                                          |         | 74  |
| RemoteAAATACACS+serverconfigurationrequirements           |                                          |         | 74  |
|                                                           | UserroleassignmentusingTACACS+attributes |         | 74  |
|                                                           | TACACS+serverredundancyandaccesssequence |         | 75  |
SinglesourceIPaddressforconsistentsourceidentificationtoAAAservers 75
| TACACS+generaltasks                                      |                                                           |        | 76  |
| -------------------------------------------------------- | --------------------------------------------------------- | ------ | --- |
| TACACS+authentication                                    |                                                           |        | 76  |
|                                                          | Aboutauthenticationfail-through                           |        | 76  |
|                                                          | TACACS+authenticationtasks                                |        | 77  |
| TACACS+authorization                                     |                                                           |        | 77  |
|                                                          | UsinglocalauthorizationasfallbackfromTACACS+authorization |        | 78  |
|                                                          | Aboutauthenticationfail-throughandauthorization           |        | 78  |
|                                                          | TACACS+authorizationtasks                                 |        | 78  |
| TACACS+accounting                                        |                                                           |        | 79  |
|                                                          | SampleaccountinginformationonaTACACS+server               |        | 79  |
|                                                          | SampleRESTaccountinginformationonaTACACS+server           |        | 80  |
|                                                          | TACACS+accountingtasks                                    |        | 80  |
| Example:ConfiguringtheswitchforRemoteAAAwithTACACS+      |                                                           |        | 81  |
| Remote                                                   | AAA with                                                  | RADIUS | 84  |
| Defaultservergroups                                      |                                                           |        | 84  |
| RemoteAAA(RADIUS)defaultsandlimits                       |                                                           |        | 84  |
| Aboutglobalversusper-RADIUSserverpasskeys(sharedsecrets) |                                                           |        | 85  |
| RemoteAAARADIUSserverconfigurationrequirements           |                                                           |        | 85  |
|5

|     | UserroleassignmentusingRADIUSattributes |     |     | 86  |
| --- | --------------------------------------- | --- | --- | --- |
|     | RADIUSserverredundancyandaccesssequence |     |     | 86  |
SinglesourceIPaddressforconsistentsourceidentificationtoAAAservers 87
| RADIUSgeneraltasks                                 |                                     |         |          | 87  |
| -------------------------------------------------- | ----------------------------------- | ------- | -------- | --- |
| RADIUSauthentication                               |                                     |         |          | 88  |
|                                                    | Aboutauthenticationfail-through     |         |          | 88  |
|                                                    | RADIUSauthenticationtasks           |         |          | 88  |
|                                                    | Configuringtwo-factorauthentication |         |          | 89  |
| SecureRADIUS(RadSec)                               |                                     |         |          | 90  |
|                                                    | RadSecconfiguration                 |         |          | 91  |
|                                                    | Deploymentscenarios                 |         |          | 91  |
|                                                    | RadSecexampleconfiguration          |         |          | 92  |
| RADIUSaccounting                                   |                                     |         |          | 94  |
|                                                    | Samplegeneralaccountinginformation  |         |          | 94  |
|                                                    | RADIUSaccountingtasks               |         |          | 96  |
| Example:ConfiguringtheswitchforRemoteAAAwithRADIUS |                                     |         |          | 97  |
| Remote                                             | AAA (TACACS+,                       | RADIUS) | commands | 99  |
| aaaaccountingall-mgmt                              |                                     |         |          | 99  |
| aaaauthenticationallow-fail-through                |                                     |         |          | 101 |
| aaaauthenticationlogin                             |                                     |         |          | 102 |
| aaaauthorizationcommands(remote)                   |                                     |         |          | 104 |
| aaagroupserver                                     |                                     |         |          | 106 |
| radius-serverauth-type                             |                                     |         |          | 107 |
| radius-serverhost                                  |                                     |         |          | 108 |
| radius-serverhostsecureipsec                       |                                     |         |          | 112 |
| radius-serverhosttls(RadSec)                       |                                     |         |          | 117 |
| radius-serverhosttlsport-access                    |                                     |         |          | 120 |
| radius-serverhosttlstracking-method                |                                     |         |          | 121 |
| radius-serverkey                                   |                                     |         |          | 122 |
| radius-serverretries                               |                                     |         |          | 123 |
| radius-serverstatus-serverinterval                 |                                     |         |          | 124 |
| radius-servertimeout                               |                                     |         |          | 125 |
| radius-servertlstimeout(RadSec)                    |                                     |         |          | 126 |
| radius-servertracking                              |                                     |         |          | 127 |
| server                                             |                                     |         |          | 128 |
| showaaaaccounting                                  |                                     |         |          | 130 |
| showaaaauthentication                              |                                     |         |          | 132 |
| showaaaauthorization                               |                                     |         |          | 135 |
| showaaaserver-groups                               |                                     |         |          | 136 |
| showaccountinglog                                  |                                     |         |          | 138 |
| showradius-server                                  |                                     |         |          | 140 |
| showradius-serversecureipsec                       |                                     |         |          | 146 |
| showradius-serverstatisticsauthentication          |                                     |         |          | 147 |
| showtacacs-server                                  |                                     |         |          | 149 |
| showtacacs-serverstatistics                        |                                     |         |          | 151 |
| showtechaaa                                        |                                     |         |          | 152 |
| tacacs-serverauth-type                             |                                     |         |          | 155 |
| tacacs-serverhost                                  |                                     |         |          | 156 |
| tacacs-serverkey                                   |                                     |         |          | 158 |
| tacacs-servertimeout                               |                                     |         |          | 159 |
| tacacs-servertracking                              |                                     |         |          | 160 |
| PKI                                                |                                     |         |          | 163 |
| PKIconcepts                                        |                                     |         |          | 163 |
|                                                    | Digitalcertificate                  |         |          | 163 |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 6

Certificate authority
Root certificate
Leaf certificate
Intermediate certificate
Trust anchor
OCSP
PKI on the switch

Trust anchor profiles
Leaf certificates
Mandatory matching of peer device hostname

PKI EST

EST usage overview
Prerequisites for using EST for certificate enrollment
EST profile configuration
Certificate enrollment
Certificate re-enrollment
Checking EST profile and certificate configuration
EST best practices

Example using EST for certificate enrollment
Example including the use of an intermediate certificate
Installing a self-signed leaf certificate (created inside the switch)
Installing a self-signed leaf certificate (created outside the switch)
Installing a certificate of a root CA
Installing a downloadable user role certificate
Installing a CA-signed leaf certificate (initiated in the switch)
Installing a CA-signed leaf certificate (created outside the switch)
PKI commands

crypto pki application
crypto pki certificate
crypto pki ta-profile
enroll self-signed
enroll terminal
import (CA-signed leaf certificate)
import (self-signed leaf certificate)
key-type
ocsp disable-nonce
ocsp enforcement-level
ocsp url
ocsp vrf
revocation-check ocsp
show crypto pki application
show crypto pki certificate
show crypto pki ta-profile
ta-certificate
subject
PKI EST commands

arbitrary-label
arbitrary-label-enrollment
arbitrary-label-reenrollment
crypto pki est-profile
enroll est-profile
reenrollment-lead-time
retry-count
retry-interval
show crypto pki est-profile
url

163
164
164
164
164
164
164
164
165
165
165
165
166
166
166
166
167
167
167
173
175
176
177
178
179
180
181
181
183
184
185
185
186
188
190
191
192
193
194
195
195
196
198
200
201
203
203
204
205
206
207
208
209
209
210
211

| 7

|                                               | username                          |           | 212 |
| --------------------------------------------- | --------------------------------- | --------- | --- |
|                                               | vrf                               |           | 214 |
| Fault Monitor                                 |                                   |           | 216 |
| Faultmonitoringconditions                     |                                   |           | 216 |
|                                               | ExcessiveCRCerrors                |           | 216 |
|                                               | Excessiveoversizepackets          |           | 216 |
|                                               | Excessivefragments                |           | 216 |
|                                               | ExcessiveTXdrops                  |           | 216 |
|                                               | Excessivecollisions               |           | 216 |
|                                               | ExcessiveLateCollisions           |           | 216 |
|                                               | Excessivealignmenterrors          |           | 217 |
|                                               | Excessivelinkflaps                |           | 217 |
|                                               | Excessivebroadcasts               |           | 217 |
|                                               | Excessivemulticasts               |           | 217 |
| Faultmonitorcommands                          |                                   |           | 217 |
|                                               | (Faultenabling/disabling)         |           | 217 |
|                                               | action                            |           | 218 |
|                                               | applyfault-monitorprofile         |           | 220 |
|                                               | fault-monitorprofile              |           | 221 |
|                                               | showfault-monitorprofile          |           | 223 |
|                                               | showinterfacefault-monitorprofile |           | 224 |
|                                               | showinterfacefault-monitorstatus  |           | 225 |
|                                               | showrunning-config                |           | 226 |
|                                               | showrunning-configall             |           | 228 |
|                                               | threshold                         |           | 229 |
|                                               | vsx-sync(faultmonitor)            |           | 230 |
| Configuring                                   | enhanced                          | security  | 232 |
| Configuringenhancedsecurity                   |                                   |           | 232 |
| passwordcomplexity                            |                                   |           | 233 |
| ConfiguringremoteloggingusingSSHreversetunnel |                                   |           | 236 |
| CLIusersessionmanagementcommands              |                                   |           | 237 |
|                                               | cli-session                       |           | 237 |
| Auditors                                      | and auditing                      | tasks     | 240 |
| Auditingtasks(CLI)                            |                                   |           | 240 |
| Auditingtasks(WebUI)                          |                                   |           | 240 |
| RESTrequestsandaccountinglogs                 |                                   |           | 241 |
| Support                                       | and Other                         | Resources | 242 |
| AccessingHPEArubaNetworkingSupport            |                                   |           | 242 |
| AccessingUpdates                              |                                   |           | 243 |
|                                               | ArubaSupportPortal                |           | 243 |
|                                               | MyNetworking                      |           | 243 |
| WarrantyInformation                           |                                   |           | 243 |
| RegulatoryInformation                         |                                   |           | 244 |
| DocumentationFeedback                         |                                   |           | 244 |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 8

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8400 Switch Series (JL375A, JL376A)

n Aruba 9300 Switch Series (R9A29A, R9A30A, R8Z96A)

n Aruba 10000 Switch Series (R8P13A, R8P14A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

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

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables
are enclosed in angle brackets (< >). Substitute the text—including
the enclosing angle brackets—with an actual value.

n For output formats where italic text can be displayed, variables

might or might not be enclosed in angle brackets. Substitute the
text including the enclosing angle brackets, if any, with an actual
value.

|

Vertical bar. A logical OR that separates multiple items from which you can
choose only one.
Any spaces that are on either side of the vertical bar are included for

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

9

Convention

Usage

{ }

[ ]

… or

...

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

On the 83xx, 9300, and 10000 Switch Series

About this document | 10

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

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

11

Chapter 2

About security

About security

This AOS-CX Switch provides the following security features:

n Local user and group management.

n Authentication, Authorization, and Accounting (AAA), either local (password or SSH public key-based),

or remote password-based TACACS+ or RADIUS.

n SSH server. SSH is a cryptographic protocol that encrypts all communication between devices.

n Ability to use enhanced security as described in Configuring enhanced security .

n Making sensitive switch configuration information available for secure export/import between

switches. For information, see service export-password.

About Authentication, Authorization, and Accounting (AAA)

n Authentication: identifies users, validates their credentials, and grants switch access.

n Authorization: controls authenticated users command execution and switch interaction privileges.

n Accounting: collects and manages user session activity logs for auditing and reporting purposes.

Local AAA on your Aruba switch provides:

n Authentication using local password or SSH public key.

n Authorization using role-based access control (RBAC), and optionally, using user-defined local user

groups with command authorization rules defined per group.

n Accounting of user activity on the switch using accounting logs.

Remote AAA provides the following for your Aruba switch:

n Authentication using remote AAA servers with either TACACS+ or RADIUS.

n Authorization using remote AAA servers with TACACS+ fine-grained command authorization. Local

RBAC or local rule-based authorization is also possible.

n Transmission of locally collected accounting information to remote TACACS+ and RADIUS servers.

TACACS+ (Terminal Access Controller Access-Control System Plus) and RADIUS (Remote Authentication Dial-In

User Service) server software is readily available as either open source or from various vendors.

For switches that support multiple management modules such as the Aruba 8400, all AAA functionality discussed

only applies to the active management module. See also AAA on switches with multiple management modules in the

High Availability Guide.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

12

Chapter 3
|          |       |           |        | Managing |     | local users | and groups |
| -------- | ----- | --------- | ------ | -------- | --- | ----------- | ---------- |
| Managing | local | users and | groups |          |     |             |            |
| Default  | user  | admin     |        |          |     |             |            |
Afactory-defaultswitchcomeswithasingleusernamedadmin.
Theadminuser:
n Hasanemptypassword.PressEnterinresponsetotheadminpasswordprompt.Atinitialboot,you
arepromptedtodefineapasswordfortheadminuser.Althoughempty(blank)passwordsare
allowed,itisrecommendedthatyouusestrongpasswordsforallproductionswitches.
n Isamemberoftheadministratorsgroup.
Cannotberemovedfromtheswitch.
n
TheswitchadminuserisdistinctfromtheServiceOSadminuser.TheServiceOSactsasthebootloaderand
recoveryoperatingsystem.TheServiceOShasitsownCLI.
| Example | of first | login | with password |     | setting |     |     |
| ------- | -------- | ----- | ------------- | --- | ------- | --- | --- |
| switch  | login:   | admin |               |     |         |     |     |
Password:
| Please  | configure     | the 'admin' | user account |     | password. |     |     |
| ------- | ------------- | ----------- | ------------ | --- | --------- | --- | --- |
| Enter   | new password: | ********    |              |     |           |     |     |
| Confirm | new password: | ********    |              |     |           |     |     |
switch#
| Built-in | user | groups | and their |     | privileges |     |     |
| -------- | ---- | ------ | --------- | --- | ---------- | --- | --- |
Theswitchprovidesthefollowingbuilt-inusergroupswithcorrespondingroles.Eachoftheseroles
comeswithasetofprivileges.
| Group/Role     |     | Privileges                                  |     |     |     |     |     |
| -------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
| administrators |     | Administratorshavefullprivileges,including: |     |     |     |     |     |
n FullCLIaccess.
n Performingfirmwareupgrades.
n Viewingswitchconfigurationinformation,includingsensitiveinformationsuchas
passwordswhicharedisplayedasciphertext.
n Performingswitchconfiguration.
n Adding/removinguseraccounts.
n Configuringusersaccounts,includingpasswords.Onceset,apasswordcannotbe
deletedorsettoempty.
13
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries)

Group/Role

Privileges

n REST API: All methods (GET, PUT, POST, DELETE) and switch resources are available.

The privilege level for administrators is 15.

operators

Operators have no switch configuration privileges. Operators are restricted to:

n Basic display-only CLI access.
n Viewing of nonsensitive switch configuration information.
n REST API: Other than the \login and \logout resources, only the GET method is

available.

The privilege level for operators is 1.

auditors

Auditors are restricted to functions related to auditing only:

n CLI: Access to commands in the auditor context (auditor>) only.
n Web UI: Access to the System > Log page only.
n REST API: POST method available for the \login and \logout resources. GET

method available for the following resources only:

o Audit log: /logs/audit

o Event log: /logs/event

The privilege level for auditors is 19.

User-defined user groups

The switch enables you to create up to 29 user-defined local user groups, for the purpose of configuring
local authorization. Each of the 29 user-defined groups support up to 1024 CLI command authorization
rules that define what CLI commands can be executed by members of the group.

The local user groups with their command execution rules are useful for the following:

n Providing authorization for use with RADIUS servers.

n Providing fallback authorization for use with TACACS+ servers.

n Providing authorization when neither RADIUS or TACACS+ servers are used.

User name requirements
Specifies the user name. Requirements:

n Must start with a lowercase letter.

n Can contain numbers and lowercase letters.

n Can include only these three special characters: hyphens ( - ), dots ( . ), and underscores ( _ ).

n Can have a maximum of 32 characters.

n Cannot be empty.

n Cannot contain uppercase letters.

n Cannot be: admin, root, or remote_user.

n Cannot be Linux reserved names such as:

daemon, bin, sys, sync, proxy, www-data, backup, list, irc, gnats, nobody, systemd-bus-proxy,
sshd, messagebus, rpc, systemd-journal-gateway, systemd-journal-remote, systemd-journal-

Managing local users and groups | 14

upload,systemd-timesync,systemd-coredump,systemd-resolve,rpcuser,vagrant,opsd,
rdanet,_lldpd,rdaadmin,rdaweb,docker_container,tss.
| Password | requirements |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- |
Passwordsmust:
n ContainonlyASCIIcharactersfromhexadecimal21tohexadecimal7E[\x21-\x7E](decimal33to126).
Spacesarenotallowed.Whenthepasswordisentereddirectlywithoutprompting,the"?"symbol
(hexadecimal3F[\x3F](decimal63))isnotpermitted.
n Containatmost32characters.
n Containatleastthenumberofcharactersconfigured(optionally)forminimum-password-length.
Althoughemptypasswordsaresupported,itisrecommendedthatyouusestrongpasswordsforallproduction
switches.
Onlyanadministratorcanchangethepasswordofauserassignedtotheoperatorsrole.
| User and | user group | management |     | tasks |     |
| -------- | ---------- | ---------- | --- | ----- | --- |
Userandusergroupmanagementcommontasksareasfollows:
Command or
| Task |     |     | Example |     |     |
| ---- | --- | --- | ------- | --- | --- |
procedure
| Creatingauser | user          |     | user jamie | group administrators | password |
| ------------- | ------------- | --- | ---------- | -------------------- | -------- |
| Changingauser | user password |     | user jamie | password             |          |
password
| Removingauser       | user          |     | no user    | jamie    |     |
| ------------------- | ------------- | --- | ---------- | -------- | --- |
| Settingauseraccount | user password |     | user admin | password |     |
password
Resettingtheadmin (procedure)
passwordusingthe
ServiceOS
| Resettingtheadmin   | (procedure) |     | erase startup-config |     |     |
| ------------------- | ----------- | --- | -------------------- | --- | --- |
| passwordbyreverting |             |     | boot system          |     |     |
theswitchtofactory
defaults
| Showingalistofall | show user-list |     | show user-list |     |     |
| ----------------- | -------------- | --- | -------------- | --- | --- |
users
| Showinginformation | show user |     | show user | information |     |
| ------------------ | --------- | --- | --------- | ----------- | --- |
forthelogged-inuser information
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 15

|      |     | Command | or  |     |         |     |     |     |
| ---- | --- | ------- | --- | --- | ------- | --- | --- | --- |
| Task |     |         |     |     | Example |     |     |     |
procedure
| Creatingausergroup |     | user-group |     |     | user-group | admuser2 |     |     |
| ------------------ | --- | ---------- | --- | --- | ---------- | -------- | --- | --- |
Addingcommand permitordeny(within 10 deny cli command "show aaa .*"
| authorizationrulestoa |     |     |     |     | 20 permit | cli command | "show .*" |     |
| --------------------- | --- | --- | --- | --- | --------- | ----------- | --------- | --- |
user-group)
usergroup
Addingcommentsto comment(withinuser- 10 comment Deny all show aaa commands.
rulesinausergroup group) 20 comment Permit all other show commands.
| Resequencingrulesin |     | resequence(within |     |     | resequence | 100 20 |     |     |
| ------------------- | --- | ----------------- | --- | --- | ---------- | ------ | --- | --- |
ausergroup
user-group)
| Showingalistofall |     | show user-group |     |     | show user-group |     |     |     |
| ----------------- | --- | --------------- | --- | --- | --------------- | --- | --- | --- |
usergroups
| Resetting | the | switch | admin |     | password | using | the Service | OS  |
| --------- | --- | ------ | ----- | --- | -------- | ----- | ----------- | --- |
console
Performthistaskonlywhentheswitch(ProductOS)adminuserpasswordhasbeenforgotten.
Prerequisites
n Youareconnectedtotheswitchthroughtheconsoleport.
n YouknowtheServiceOSpassword(ifconfigured).
IfyouforgettheServiceOSpassword,theonlyrecourseistozerioizetheswitch,revertingittofactorydefaults.
Formoreinformation,seeZeroizationintheDiagnosticsandSupportabilityGuide.
Procedure
1. Reboottheswitch.
| 2.  | Atthebootprompt,select0. |            | Service | OS              | Console. |     |     |     |
| --- | ------------------------ | ---------- | ------- | --------------- | -------- | --- | --- | --- |
|     | 0. Service               | OS Console |         |                 |          |     |     |     |
|     | 1. Primary               | Software   | Image   | [XL.01.01.0001] |          |     |     |     |
|     | 2. Secondary             | Software   | Image   | [XL.01.01.0002] |          |     |     |     |
3. AttheSwitch Loginprompt,enteradminandpressEnter.IfpromptedforaServiceOS
password,enteritandpressEnter.
|     | Switch login: | admin              |     |     |     |     |     |     |
| --- | ------------- | ------------------ | --- | --- | --- | --- | --- | --- |
|     | Password:     | **********         |     |     |     |     |     |     |
|     | Hewlett       | Packard Enterprise |     |     |     |     |     |     |
SVOS>
Managinglocalusersandgroups|16

4. AttheSVOS>prompt,enterpasswordandpressEnter.
5. Enterthenewswitch(ProductOS)passwordatbothpasswordprompts.
SVOS> password
| Enter   | password: ************ |              |     |     |     |
| ------- | ---------------------- | ------------ | --- | --- | --- |
| Confirm | password:              | ************ |     |     |     |
SVOS>
6. EnterbootandpressEnter.
| SVOS> boot |              |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- |
| ServiceOS  | Information: |     |     |     |     |
Version: **.10.06.0001
| Build | Date: 2020-12-01 | 14:52:31 PDT |     |     |     |
| ----- | ---------------- | ------------ | --- | --- | --- |
Build ID: ServiceOS:**.01.01.0001:461519208911:20180301452
SHA: 46151920891195cdb2267ea6889a3c6cbc3d4193
| Boot Profiles: |                   |                 |     |     |     |
| -------------- | ----------------- | --------------- | --- | --- | --- |
| 0. Service     | OS Console        |                 |     |     |     |
| 1. Primary     | Software Image    | [**.10.06.0001] |     |     |     |
| 2. Secondary   | Software Image    | [**.10.06.0001] |     |     |     |
| Select         | profile(primary): |                 |     |     |     |
7. Tobootwiththeprimaryswitchimagepress1andthenEnter.Tobootwiththesecondaryswitch
image,press2andthenEnter.Ifyoumakenoselectionforapproximately10seconds,theswitch
bootsthedefaultimage.ThedefaultisshowninparenthesestotherightofSelect profile,for
| example:Select | profile(primary):. |     |     |     |     |
| -------------- | ------------------ | --- | --- | --- | --- |
8. OnceinAOS-CX,savetheconfigurationtomaketheadminloginuseraccountpasswordsetting
persistent.
| Resetting | the admin | password | by reverting | the switch | to  |
| --------- | --------- | -------- | ------------ | ---------- | --- |
| factory   | defaults  |          |              |            |     |
Thistaskerasesallswitchconfiguration,revertingtheswitchtoitsfactorydefaultstate.Considerusingotherless-
impactingtechniquesforadminpasswordreset.Forexample,anotheradministratorusercanresettheadmin
userpasswordtoaknownvalue.SeealsoResettingtheswitchadminpasswordusingtheServiceOSconsole.
Prerequisites
Ifwanted,youhavesavedacopyoftheswitchconfiguration.
Procedure
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 17

| 1.  | Atthemanagercommandprompt,entererase |     |     | startup-config. |     |
| --- | ------------------------------------ | --- | --- | --------------- | --- |
switch#
erase startup-config
2. Enterboot system,respondingntotheDo you want to save the current configuration
promptandthenrespondingytotheContinueprompt.
|     | switch#    | boot system  |                  |               |                |
| --- | ---------- | ------------ | ---------------- | ------------- | -------------- |
|     | Do you     | want to save | the current      | configuration | (y/n)? n       |
|     | This will  | reboot the   | entire switch    | and render    | it unavailable |
|     | until the  | process      | is complete.     |               |                |
|     | Continue   | (y/n)? y     |                  |               |                |
|     | The system | is going     | down for reboot. |               |                |
3. Attheloginprompt,enteradminandpressEnter.Theadminpasswordremainsemptyuntilitis
set.
| User | and group | commands |     |     |     |
| ---- | --------- | -------- | --- | --- | --- |
user
user <USERNAME> group {administrators | operators | auditors | <USER-GROUP>}
password [ciphertext <CIPHERTEXT-PASSWORD> | plaintext <PLAINTEXT-PASSWORD>]
| no user | <USERNAME> |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- |
Description
Createsauserandaddstheusertooneoftheusergroups.Usersaregiventheprivilegesoftheir
group.Forthethreebuilt-inusergroups(administrators,operators,auditors),theprivilegesare
fixed.Foruser-definedlocalusergroups,theprivilegesaredefinedbytheCLIcommandauthorization
rulesofthegroup.
Whenenteredwithouteitheroptionalciphertextorplaintextparameters,thecleartextpasswordis
promptedfortwice,withthecharactersenteredmaskedwith"*"symbols.
Thenoformofthiscommandremovesauseraccountfromtheswitch.Theadministratorcannotdelete
theuseraccountfromwhichtheyareloggedin.Theadminusercannotbedeleted.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<USERNAME>
Specifiestheusername.Requirements:
Muststartwithalowercaseletter.
Cancontainnumbersandlowercaseletters.
Canincludeonlythesethreespecialcharacters:
hyphens( -),dots( .),andunderscores( _).
Canhaveamaximumof32characters.
Cannotbeempty.
Cannotcontainuppercaseletters.
Cannotbe:admin,root,orremote_user.
CannotbeLinuxreservednamessuchas:
daemon,bin,sys,sync,proxy,www-data,backup,
list,irc,gnats,nobody,systemd-bus-proxy,
Managinglocalusersandgroups|18

Parameter

Description

group

sshd, messagebus, rpc, systemd-journal-gateway,
systemd-journal-remote, systemd-journal-
upload, systemd-timesync, systemd-coredump,
systemd-resolve, rpcuser, vagrant, opsd, rdanet,
_lldpd, rdaadmin, rdaweb, docker_container, tss.

Selects the local user group to which the new user will be
assigned.

administrators | operators | auditors

Selects one of three built-in local user groups.

<USER-GROUP>

Specifies an existing user-defined local user group.

ciphertext <CIPHERTEXT-PASSWORD>

plaintext <PLAINTEXT-PASSWORD>

Specifies a ciphertext password. No password prompts are
provided and the ciphertext password is validated before
the configuration is applied for the user. The variable
<CIPHERTEXT-PASSWORD> is Base64 and is typically
copied from another switch using the show running-
config command output and then pasted into this
command.

NOTE: The administrator cannot construct ciphertext
passwords themselves. The ciphertext is only created by
an AOS-CX switch. The ciphertext is created by setting a
password for a user with the user command. The
ciphertext is available for copying from the show
running-config output and pasting into the
configuration on any other AOS-CX switch. The target
switch must have the same export password (default or
otherwise) as the source switch.

Specifies the password without prompting. The password
is visible as cleartext when entered but is encrypted
thereafter. Command history does show the password as
cleartext.

Usage

n Up to 63 local users can be added, for a total of 64 users including the default user admin. A user can

belong to only one group.

n The switch ships with the admin user account and three built-in local user groups: administrators,
operators, and auditors. The admin account belongs to the administrators group. The Service OS
also includes the administrator user admin. The two admin users are entirely distinct.

n When a local user account is removed, the user loses all active login/SSH sessions. Any calls on the

existing REST session with that local user account fail with a permissions issue as soon as the user is
deleted. Soon afterwards, the existing REST sessions with the deleted local user account become
invalidated. If a user is viewing the GUI while their account is deleted, the user is redirected to the
login page within 60 seconds. The home directory associated with the user is also removed from the
switch.

n Cleartext passwords (whether entered with prompting or entered directly) must:

o Contain only ASCII characters from hexadecimal 21 to hexadecimal 7E [\x21-\x7E] (decimal 33 to
126). Spaces are not allowed. When the password is entered directly without prompting, the "?"
symbol (hexadecimal 3F [\x3F] (decimal 63)) is not permitted.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

19

o Containatmost32characters.
o Containatleastthenumberofcharactersconfigured(optionally)forminimum-password-length.
Althoughemptypasswordsaresupported,itisrecommendedthatyouusestrongpasswordsfor
allproductionswitches.
Onlyanadministratorcanchangethepasswordofauserassignedtotheoperatorsrole.
Examples
Creatinglocaluserjamieintheadministratorsgroupwithapromptedpassword:
| switch(config)#               | user  | jamie group | administrators | password |
| ----------------------------- | ----- | ----------- | -------------- | -------- |
| Adding user                   | jamie |             |                |          |
| Enter password:************   |       |             |                |          |
| Confirm password:************ |       |             |                |          |
Creatinguserchrisintheexistinguser-definedlocalusergroupadmuser2withacleartextpassword,
usingdirectentrywithoutprompting:
switch(config)# user chris group admuser2 password plaintext passWORDxJ|989
Creatinguseralexintheoperatorsgroupwithaciphertextpassword(theciphertextshownisa
placeholderthatmustbereplacedwithactualciphertext):
switch(config)# user alex group operators password ciphertext NDcDI2...8igJfA=
Removinguserjamie:
| switch(config)# | no  | user jamie |     |     |
| --------------- | --- | ---------- | --- | --- |
User jamie's home directory and active sessions will be deleted.
| Do you want         | to continue | [y/n]?y |              |     |
| ------------------- | ----------- | ------- | ------------ | --- |
| Command History     |             |         |              |     |
| Release             |             |         | Modification |     |
| 10.07orearlier      |             |         | --           |     |
| Command Information |             |         |              |     |
| Platforms           | Command     | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
user-group
Managinglocalusersandgroups|20

user-group <GROUP-NAME>
no user-group <GROUP-NAME>

Description

If <GROUP-NAME> does not exist, this command creates a local user group and then enters its context. If
<GROUP-NAME> exists, this command enters the context for the specified <GROUP-NAME>. Within the
<GROUP-NAME> context, several subcommands are available for working with rules that specify what CLI
commands are permitted or denied for all members of the local group.

In addition to the three built-in user groups administrators, operators, and auditors, up to 29 user-
defined local user groups can be defined. All users can be members of only one of the up to 32 groups.

The no form of this command deletes the specified user group. All members of the deleted group lose
all command authorization privilege.

Parameter

<GROUP-NAME>

Description

Specifies the user group name. A new group is created if the
specified group does not exist and then the group context is
entered. If the group name exists, its context is entered.

Do not causally delete user-defined local user groups without understanding the implications. Although user-

defined local user groups can be deleted with the respective members losing all privileges, the three built-in
groups administrators, operators, and auditors are always available and their privileges are unchangeable.

Subcommands

These subcommands are available within the user-defined local user group context (shown in the switch
prompt as config-usr-grp-<GROUP-NAME>).
[<SEQ-NUM>] {permit | deny} cli command "<REGEX>"
no <SEQ-NUM>

Defines a CLI command privilege permit or deny rule. There is an implicit "deny .*" rule at the end
of every user-defined group rule list. Members of a user-defined group without any permit rules
have no CLI command privileges.

The no form of this subcommand deletes the specified (by sequence number) rule from the group.

Rule evaluation proceeds from lowest to highest sequence number until the first successful match, resulting in

either CLI command permission or denial. Rule evaluation ceases upon first match. Therefore, rules for related

CLI commands must be defined in most restrictive to least restrictive order.

<SEQ-NUM>

Specifies the CLI command rule sequence number. When omitted, a sequence number that is 10
greater the highest existing sequence number is auto-assigned. When no rules exist, the first auto-
assigned sequence number is 10.

{permit | deny}

Sets the rule type as either permit or deny. Rule order is important. For example, these two related
rules together authorize all show commands except for the show aaa commands.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

21

switch(config-usr-grp-admuser2)#10 deny cli command "show aaa .*"
switch(config-usr-grp-admuser2)#20
|     |     |     |     |     | permit cli | command | "show | .*" |
| --- | --- | --- | --- | --- | ---------- | ------- | ----- | --- |
Toachievethewantedeffectinthisexample,thedenyrulemustprecedethepermitrule.Thesetwo
rulestogetherachievethefollowing:
n Allshow aaacommandsmatchonrule10,triggeringcommanddenial,andtheimmediate
cessationoffurtherruleevaluation.Matchingonrule20isneverattempted.
n Allothershowcommands(excludingshow aaacommands)matchonrule20andaretherefore
permitted.
<REGEX>
SpecifiestheCLIcommandmatchingcriteriaoftherule.Thecriteriacanbeexpressedas".*"which
matchesallcommands.Otherwise,thecriteriaisexpressedasaPOSIX-compliantregularexpression
(regex)stringstartingwithanexactmatchcommandtoken(forexampleshow)followedbyaregex
representingcommandarguments.Thefirstwordmustbeastringthatcontainsonlyalphanumeric
orhyphencharacters.
Forexample,toallowallcommandsstartingwiththewordinterface,theregexmustbe"interface
.*"orjust"interface".Using"interface.*"(withoutthespace)isnotsupported.Forexample,
"show .*"matcheseveryshowcommand.ConsulttheExtendedregularexpressioninformation
availableat:https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_
09_04.
|              |                |               | Sample    | matched    | CLI          |     |                            |     |
| ------------ | -------------- | ------------- | --------- | ---------- | ------------ | --- | -------------------------- | --- |
| Sample       | matching       | criteria      |           |            |              |     | Matches                    |     |
|              |                |               | command   |            | or specifier |     |                            |     |
| show         | .*             |               | show      | accounting | log          |     | Allshowcommands            |     |
| bgp          | .*             |               | bgp       | router-id  | 1.1.1.1      |     | Allbgpcommands             |     |
| interface    | .*             |               | interface |            | 1/1/1        |     | Allinterfacespecifiers     |     |
| vlan         | (3|4)          |               | vlan      | 3          |              |     | VLAN3or4                   |     |
| vlan         | [1-9]          |               | vlan      | 5          |              |     | AsingleVLANintherange1to9  |     |
| vlan         | ([1-9]|1[0-9]) |               | vlan      | 19         |              |     | AsingleVLANintherange1to19 |     |
| [<SEQ-NUM>]  | comment        | <TEXT-STRING> |           |            |              |     |                            |     |
| no <SEQ-NUM> | comment        |               |           |            |              |     |                            |     |
Addsacommenttoanexistingrule.Thenoformofthissubcommandremovesanexisting
comment.
switch(config-usr-grp-admuser2)# 10 comment Deny all show aaa commands.
switch(config-usr-grp-admuser2)# 20 comment Permit all other show commands.
switch(config-usr-grp-admuser2)#
switch(config-usr-grp-admuser2)# show running-config current-context
| user-group |              | admuser2    |           |               |           |     |     |     |
| ---------- | ------------ | ----------- | --------- | ------------- | --------- | --- | --- | --- |
|            | 10 comment   | Deny all    | show      | aaa commands. |           |     |     |     |
|            | 10 deny      | cli command | "show     | aaa           | .*"       |     |     |     |
|            | 20 comment   | Permit      | all other | show          | commands. |     |     |     |
|            | 20 permit    | cli command | "show     | .*"           |           |     |     |     |
| include    | <GROUP-NAME> | [no]        | include   | <GROUP-NAME>  |           |     |     |     |
Managinglocalusersandgroups|22

Includeallrulesfromthespecifieduser-defined<GROUP-NAME>.Onlyonegroupcanbeincludedin
thedefinitionofanothergroup.Thecontentoftheincludedgroupiseffectivelyplacedatthetopof
theruleslistinthecurrentgroup.Ifthespecified<GROUP-NAME>doesnotexist,itiscreated.
Thenoformofthissubcommandremovesthespecifiedincludedgroupfromthecurrentgroup.The
specifiedincludedgroupmustexistandmustbeincludedinthecurrentgrouporelseanerror
messageisshown.
Thenameoftheincludedgroupisshownatthetopoftheshow user-groupcommandforthegroup
withtheinclude.
Inthisexample,groupadmuser1isincludedingroupadmuser2.Sotheadmuser1rulesareevaluated
firstandthentherulesintheadmuser2groupareonlyevaluatedifnoCLIcommandmatchoccurs
fortherulesingroupadmuser1.
| switch(config-usr-grp-admuser2)# |       |         |     | include |            | admuser1 |     |     |
| -------------------------------- | ----- | ------- | --- | ------- | ---------- | -------- | --- | --- |
| switch(config-usr-grp-admuser2)# |       |         |     | show    | user-group | admuser2 |     |     |
| User                             | Group | Summary |     |         |            |          |     |     |
==================
| Name     |          | : admuser2      |     |     |     |     |     |     |
| -------- | -------- | --------------- | --- | --- | --- | --- | --- | --- |
| Type     |          | : configuration |     |     |     |     |     |     |
| Included | Group    | : admuser1      |     |     |     |     |     |     |
| Number   | of Rules | : 2             |     |     |     |     |     |     |
| User     | Group    | Rules           |     |     |     |     |     |     |
================
| SEQUENCE | NUM | ACTION | COMMAND |     |     |     | COMMENT |     |
| -------- | --- | ------ | ------- | --- | --- | --- | ------- | --- |
------------- ---------- ----------------------------- ---------------------------
-----
| 10  |     | deny   | show | aaa .* |     |     | Deny all   | show aaa commands. |
| --- | --- | ------ | ---- | ------ | --- | --- | ---------- | ------------------ |
| 20  |     | permit | show | .*     |     |     | Permit all | other show         |
commands.
| resequence | [<STARTING-SEQ-NUM> |     |     | <INCREMENT>] |     |     |     |     |
| ---------- | ------------------- | --- | --- | ------------ | --- | --- | --- | --- |
ResequencestheCLIcommandauthorizationrules.Whenenteredwithouttheoptionalparameters
therulesareresequencedwitha<STARTING-SEQ-NUM>of10andan<INCREMENT>of10.
<STARTING-SEQ-NUM>
Specifiesthestartingsequencenumber.
<INCREMENT>
Specifiesthesequencenumberincrement.
Resequencingtherulestostartat100withanincrementof20:
| switch(config-usr-grp-admuser2)# |     |     |     | resequence |     | 100 20 |     |     |
| -------------------------------- | --- | --- | --- | ---------- | --- | ------ | --- | --- |
switch(config-usr-grp-admuser2)# show running-config current-context
| user-group |             | admuser2    |       |               |           |     |     |     |
| ---------- | ----------- | ----------- | ----- | ------------- | --------- | --- | --- | --- |
|            | 100 comment | Deny all    | show  | aaa commands. |           |     |     |     |
|            | 100 deny    | cli command | "show | aaa           | .*"       |     |     |     |
|            | 120 comment | Permit      | all   | other show    | commands. |     |     |     |
|            | 120 permit  | cli command |       | "show .*"     |           |     |     |     |
Resequencingtherulestothedefaultofstartingat10withanincrementof10:
| switch(config-usr-grp-admuser2)# |     |     |     | resequence |     |     |     |     |
| -------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
switch(config-usr-grp-admuser2)# show running-config current-context
| user-group |            | admuser2    |       |               |     |     |     |     |
| ---------- | ---------- | ----------- | ----- | ------------- | --- | --- | --- | --- |
|            | 10 comment | Deny all    | show  | aaa commands. |     |     |     |     |
|            | 10 deny    | cli command | "show | aaa .*"       |     |     |     |     |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 23

|      | 20 comment     | Permit          | all other |     | show commands. |
| ---- | -------------- | --------------- | --------- | --- | -------------- |
|      | 20 permit      | cli command     | "show     |     | .*"            |
| show | running-config | current-context |           |     |                |
Showsallthecommandsusedtoconfiguretherulesinthecurrentgroupcontext.
switch(config-usr-grp-admuser2)# show running-config current-context
| user-group |            | admuser2    |          |       |                |
| ---------- | ---------- | ----------- | -------- | ----- | -------------- |
|            | 10 comment | Deny        | all show | aaa   | commands.      |
|            | 10 deny    | cli command | "show    | aaa   | .*"            |
|            | 20 comment | Permit      | all      | other | show commands. |
|            | 20 permit  | cli command |          | "show | .*"            |
list
Listthesubcommandsavailablewithintheuser-definedgroupcontext.
exit
Exitstheuser-definedgroupcontext.
end
Exitstheuser-definedgroupcontextandthentheconfigcontext.
| Command        | History     |         |         |     |              |
| -------------- | ----------- | ------- | ------- | --- | ------------ |
| Release        |             |         |         |     | Modification |
| 10.07orearlier |             |         |         |     | --           |
| Command        | Information |         |         |     |              |
| Platforms      |             | Command | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
user password
user <USERNAME> password [ciphertext <CIPHERTEXT-PASSWORD> | plaintext <PLAINTEXT-
PASSWORD>]
Description
Changesapasswordforanaccountorenablesthepasswordfortheadminaccount.Whenentered
withouteitheroptionalciphertextorplaintextparameters,thecleartextpasswordispromptedfor
twice,withthecharactersenteredmaskedwith"*"symbols.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<USERNAME> Specifiesthecorrespondingusernameforthepasswordyou
wanttochange.
| ciphertext |     | <CIPHERTEXT-PASSWORD> |     |     |     |
| ---------- | --- | --------------------- | --- | --- | --- |
Specifiesaciphertextpassword.Nopasswordpromptsare
providedandtheciphertextpasswordisvalidatedbeforethe
configurationisappliedfortheuser.Thevariable<CIPHERTEXT-
Managinglocalusersandgroups|24

Parameter

Description

PASSWORD> is Base64 and is typically copied from another switch
using the show running-config command output and then
pasted into this command.

NOTE: The administrator cannot construct ciphertext passwords
themselves. The ciphertext is only created by an AOS-CX switch.
The ciphertext is created by setting a password for a user with
the user command. The ciphertext is available for copying from
the show running-config output and pasting into the
configuration on any other AOS-CX switch. The target switch
must have the same export password (default or otherwise) as
the source switch.

plaintext <PLAINTEXT-PASSWORD>

Specifies the password without prompting. The password is
visible as cleartext when entered but is encrypted thereafter.
Command history does show the password as cleartext.

Usage

The admin account is available on the switch without a password by default.

Cleartext passwords (whether entered with prompting or entered directly) must:

n Contain only ASCII characters from hexadecimal 21 to hexadecimal 7E [\x21-\x7E] (decimal 33 to 126).
Spaces are not allowed. When the password is entered directly without prompting, the "?" symbol
(hexadecimal 3F [\x3F] (decimal 63)) is not permitted.

n Contain at most 32 characters.

n Contain at least the number of characters configured (optionally) for minimum-password-length.

Although empty passwords are supported, it is recommended that you use strong passwords for all

production switches.

Only an administrator can change the password of a user assigned to the operators role.

Examples

Enabling (or changing) a cleartext password for admin:

switch(config)# user admin password
Changing password for user admin
Enter password:************
Confirm password:************

Changing the cleartext password for user chris, using direct entry without prompting:

switch(config)# user chris password plaintext PASSwordZQ#@67

Changing the ciphertext password for user alex (the ciphertext shown is a placeholder that must be
replaced with actual ciphertext):

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

25

| switch(config)#     | user    | alex password | ciphertext   | XqYJ36...W83D4Y= |
| ------------------- | ------- | ------------- | ------------ | ---------------- |
| Command History     |         |               |              |                  |
| Release             |         |               | Modification |                  |
| 10.07orearlier      |         |               | --           |                  |
| Command Information |         |               |              |                  |
| Platforms           | Command | context       | Authority    |                  |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| service export-password |     |     |     |     |
| ----------------------- | --- | --- | --- | --- |
service export-password
| no service export-password |     |     |     |     |
| -------------------------- | --- | --- | --- | --- |
Description
Configuresanondefaultexportpassword.Theexportpasswordisusedtotransformcriticalsecurity
parameters(suchaspasswordhashes)intociphertextsuitableforexportingandshowingby
commandssuchasshow running-config.Thistransformationenablessafeswitchconfiguration
importandexport.
Thenoformofthiscommandrevertstheexportpasswordtoitsfactorydefault.
Allfactory-defaultswitcheshaveidenticaldefaultexportpasswords.Forsecurity,itisrecommendedthatyouset
thesamenondefaultexportpasswordoneveryswitchinagroupthatwillexchangeconfigurationinformation.
Onlyswitcheswithidenticalexportpasswordscanexchangeconfigurationinformation.
Usage
Promptsyoutwiceforthenewexportpassword.
Theexportpasswordmust:
n ContainonlyASCIIcharactersfromhexadecimal21tohexadecimal7E[\x21-\x7E](decimal33to
126).Spacesarenotallowed.
n Containatmost32characters.
n Notbeblank.
Examples
Configuringanewexportpassword:
| switch(config)#               | service | export-password |     |     |
| ----------------------------- | ------- | --------------- | --- | --- |
| Enter password:************   |         |                 |     |     |
| Confirm password:************ |         |                 |     |     |
Revertingtheexportpasswordtoitsfactorydefault:
Managinglocalusersandgroups|26

| switch(config)#     | no      | service | export-password |     |     |
| ------------------- | ------- | ------- | --------------- | --- | --- |
| Command History     |         |         |                 |     |     |
| Release             |         |         | Modification    |     |     |
| 10.07orearlier      |         |         | --              |     |     |
| Command Information |         |         |                 |     |     |
| Platforms           | Command | context | Authority       |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show user-group
| show user-group | [<GROUP-NAME>] |     | [vsx-peer] |     |     |
| --------------- | -------------- | --- | ---------- | --- | --- |
Description
Showsusergroupinformationforthebuilt-ingroupsplusanyuser-definedlocalusergroups.When
enteredwithout<GROUP-NAME>,summaryinformationisshownforallgroups.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<GROUP-NAME> Narrowstheshowcommandoutputtothatofthespecifiedgroup,
andforlocalusergroups,addstheUser Group Ruleslist.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showthelistofallusergroups,includingbuilt-ingroupsandlocalusergroups.
| switch# show | user-group |      |                |        |          |
| ------------ | ---------- | ---- | -------------- | ------ | -------- |
| GROUP NAME   | GROUP      | TYPE | INCLUDED GROUP | NUMBER | OF RULES |
-------------- -------------- ----------------- -------------------
| administrators | built-in      |     | n/a      | n/a |     |
| -------------- | ------------- | --- | -------- | --- | --- |
| admuser1       | configuration |     | --       | 5   |     |
| admuser2       | configuration |     | admuser1 | 2   |     |
| auditors       | built-in      |     | n/a      | n/a |     |
| operators      | built-in      |     | n/a      | n/a |     |
Showdetailedinformationforlocalusergroupadmuser2.
| switch(config-usr-grp-admuser2)# |         |     | show user-group | admuser2 |     |
| -------------------------------- | ------- | --- | --------------- | -------- | --- |
| User Group                       | Summary |     |                 |          |     |
==================
| Name | : admuser2 |     |     |     |     |
| ---- | ---------- | --- | --- | --- | --- |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 27

| Type       | : configuration  |     |     |     |     |
| ---------- | ---------------- | --- | --- | --- | --- |
| Included   | Group : admuser1 |     |     |     |     |
| Number of  | Rules : 2        |     |     |     |     |
| User Group | Rules            |     |     |     |     |
================
| SEQUENCE | NUM ACTION | COMMAND |     | COMMENT |     |
| -------- | ---------- | ------- | --- | ------- | --- |
------------- ---------- ----------------------------- ---------------------------
-----
| 10  | deny   | show aaa | .*  | Deny all   | show aaa commands. |
| --- | ------ | -------- | --- | ---------- | ------------------ |
| 20  | permit | show .*  |     | Permit all | other show         |
commands.
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show user             | information |     |     |     |     |
| --------------------- | ----------- | --- | --- | --- | --- |
| show user information |             |     |     |     |     |
Description
Showsthefollowinginformationforthelogged-inuser:
n Username.
n Userauthenticationtype:local,RADIUS,orTACACS+.
n Usergroup:administrators,operators,or<GROUP-NAME>.
n Userprivilegelevel:Forthebuilt-inusergroupsandRADIUSorTACACS+,theroleprivilegelevelvalue
isshown.Foruser-definedusergroups,N/Aisshown.
Examples
Showinginformationfortheadminuser:
| switch# show   | user information |                  |     |     |     |
| -------------- | ---------------- | ---------------- | --- | --- | --- |
| Username       |                  | : admin          |     |     |     |
| Authentication | type             | : Local          |     |     |     |
| User group     |                  | : administrators |     |     |     |
| User privilege | level            | : 15             |     |     |     |
Showinginformationforamemberoftheuser-definedlocalusergroupadmuser2:
| switch# show   | user information |            |     |     |     |
| -------------- | ---------------- | ---------- | --- | --- | --- |
| Username       |                  | : admin2-b |     |     |     |
| Authentication | type             | : Local    |     |     |     |
Managinglocalusersandgroups|28

| User group     |       | : admuser2 |     |
| -------------- | ----- | ---------- | --- |
| User privilege | level | : N/A      |     |
Showinginformationforamemberofoperators:
| switch# show   | user information |             |     |
| -------------- | ---------------- | ----------- | --- |
| Username       |                  | : operator  |     |
| Authentication | type             | : Local     |     |
| User group     |                  | : operators |     |
| User privilege | level            | : 1         |     |
ShowinginformationforremoteRADIUSuserrad_user1mappedtolocalusergroupadministrators:
switch#
show user information
| Username       |       | : rad_user1      |     |
| -------------- | ----- | ---------------- | --- |
| Authentication | type  | : RADIUS         |     |
| User group     |       | : administrators |     |
| User privilege | level | : 15             |     |
ShowinginformationforremoteRADIUSuserrad_user2mappedtolocalusergroupoperators:
| switch# show   | user information |             |     |
| -------------- | ---------------- | ----------- | --- |
| Username       |                  | : rad_user2 |     |
| Authentication | type             | : RADIUS    |     |
| User group     |                  | : operators |     |
| User privilege | level            | : 1         |     |
ShowinginformationforremoteTACACS+tac_user1loggedinwithpriv-lvl15(mappedtousergroup
administrators):
| switch# show        | user information |                  |              |
| ------------------- | ---------------- | ---------------- | ------------ |
| Username            |                  | : tac_user1      |              |
| Authentication      | type             | : TACACS+        |              |
| User group          |                  | : administrators |              |
| User privilege      | level            | : 15             |              |
| Command History     |                  |                  |              |
| Release             |                  |                  | Modification |
| 10.07orearlier      |                  |                  | --           |
| Command Information |                  |                  |              |
| Platforms           | Command          | context          | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
show user-list
| show user-list | [vsx-peer] |     |     |
| -------------- | ---------- | --- | --- |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 29

Description

Shows all configured users and their corresponding group names.

Parameter

vsx-peer

Examples

Description

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

Show the user list from a switch with only the admin user defined.

switch# show user-list

USER
---------------------------------------------
admin

administrators

GROUP

Show the user list after adding a user to the operators built-in group.

switch# show user-list

USER
---------------------------------------------
admin
oper1

administrators
operators

GROUP

Show the user list after adding a user to the auditors built-in group.

switch# show user-list

USER
---------------------------------------------
admin
oper1
audit1

administrators
operators
auditors

GROUP

Show the user list after adding a total of three users to two user-defined user groups.

switch# show user-list

GROUP

USER
---------------------------------------------
admin
oper1
audit1
adm1a
admin2-a
admin2-b

administrators
operators
auditors
admuser1
admuser2
admuser2

Command History

Managing local users and groups | 30

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 31

Chapter 4
SSH server
SSH server
SSH(SecureShell)isacryptographicprotocolthatencryptsallcommunicationbetweendevices.
EachswitchVRFincludesanSSHserver.TheSSHserveronthemgmtVRFisenabledbydefaultin
softwareversion10.02andhigher,anddisabledinversion10.01andlower.OnlytheSSHservers
includedintheswitcharesupported.
TheSSHserverprovidesSSHclienttoswitchcommunications,enablingSSHclients(atleastSSHv2.0)to
connecttotheswitchforthepurposeofmanagingit.TheSSHserverinterfaceswiththeauthentication
servicethatprovideslocaland/orremoteAAA.
TheSSHserverwillperformarekeyoperationforallopenSSHsessionsateveryhourorafter1GBofdata
transferred,whicheveroccursfirst.Therekeyisperformedtoaddressacommonsecurityconcernthat
encryption/decryptionkeysnotbeusedforlongperiodsoftime.Thislimitstheamountofdataexposedinthe
unfortunatecasewhereakeyisexposedorrefactored.
SSHpublickeyauthenticationisseparatefromSSHserver.LookforinformationonSSHpublickeyunderLocal
authentication.
SSH defaults
| Setting                       |     | Default value     |     |     |
| ----------------------------- | --- | ----------------- | --- | --- |
| MaximumSSHpasswordretries     |     | 3passwordretries. |     |     |
| Password-based(withSSHclient) |     | Enabled.          |     |     |
authentication
| SSHpassword-basedlogingrace |     | 120seconds. |     |     |
| --------------------------- | --- | ----------- | --- | --- |
periodtimeout
| SSHpublickeyauthentication |     | Enabled.   |     |     |
| -------------------------- | --- | ---------- | --- | --- |
| SSHidlesessiontimeout      |     | 60seconds. |     |     |
| SSH server tasks           |     |            |     |     |
SSHservertasksareasfollows:
| Task                 | Command    | name | Example    |             |
| -------------------- | ---------- | ---- | ---------- | ----------- |
| EnablingtheSSHserver | ssh server | vrf  | ssh server | vrf default |
32
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries)

| Task | Command | name | Example |     |     |
| ---- | ------- | ---- | ------- | --- | --- |
DisablingtheSSHserver no ssh server vrf no ssh server vrf default
| GeneratinganSSHhost- | ssh host-key |     | ssh host-key | rsa bits 2048 |     |
| -------------------- | ------------ | --- | ------------ | ------------- | --- |
keypair
Clearingthelistoftrusted ssh known-host ssh known-host remove 1.1.1.1
SSHserversforyouruser
remove
account
ConfiguringSSHtousea ssh ciphers ssh ciphers chacha20-poly1305@openssh.com
| setofciphers |     |     | aes256-ctr | aes256-cbc |     |
| ------------ | --- | --- | ---------- | ---------- | --- |
ConfiguringSSHtousea ssh host-key- ssh host-key-algorithms ssh-rsa ssh-ed25519
setofhostkeyalgorithms
|     | algorithms |     | ecdsa-sha2-nistp521 |     |     |
| --- | ---------- | --- | ------------------- | --- | --- |
ConfiguringSSHtousea ssh macs ssh macs hmac-sha2-256 hmac-sha2-512
setofMACs
ConfiguringSSHtousea ssh key-exchange- ssh key-exchange-algorithms ecdh-sha2-
| setofkeyexchange | algorithms |     | nistp256 |     |     |
| ---------------- | ---------- | --- | -------- | --- | --- |
algorithms
ConfiguringSSHtousea ssh public-key- ssh public-key-algorithms x509v3-ssh-rsa
| setofpublickey | algorithms |     | ssh-rsa | rsa-sha2-256 |     |
| -------------- | ---------- | --- | ------- | ------------ | --- |
algorithms
| ConfiguringSSHidle  | cli-session |        | switch(config)#             | cli-session     |            |
| ------------------- | ----------- | ------ | --------------------------- | --------------- | ---------- |
| sessiontimeout      |             |        | switch(config-cli-session)# |                 | timeout 20 |
| ShowingtheSSHserver | show ssh    | server | show ssh                    | server all-vrfs |            |
configuration
ShowingtheactiveSSH show ssh server show ssh server sessions all-vrfs
| sessions | sessions |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- |
ShowingtheSSHserver show ssh host-key show ssh host-key ecdsa
hostkeys
| SSH server        | commands         |        |     |     |     |
| ----------------- | ---------------- | ------ | --- | --- | --- |
| show ssh host-key |                  |        |     |     |     |
| show ssh host-key | [ecdsa | ed25519 | | rsa] |     |     |     |
Description
ShowsthepublichostkeysfortheSSHserver.Ifthekeytypeisnotprovided,allavailablehost-keysare
shown.
| Parameter |     | Description                  |     |     |     |
| --------- | --- | ---------------------------- | --- | --- | --- |
| ecdsa     |     | SelectstheECDSAhost-keypair. |     |     |     |
SSHserver|33

| Parameter |     |     | Description                    |     |
| --------- | --- | --- | ------------------------------ | --- |
| ed25519   |     |     | SelectstheED25519host-keypair. |     |
| rsa       |     |     | SelectstheRSAhost-keypair.     |     |
Examples
ShowingtheECDSApublichost-key:
| switch#  | show ssh host-key |       | ecdsa                 |     |
| -------- | ----------------- | ----- | --------------------- | --- |
| Key Type | : ECDSA           | Curve | : ecdsa-sha2-nistp256 |     |
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAhtuv5rABBBGs
...
O4mjVFGMVKZ87RWkyrxeQa2fAGZZEp1902K33/k3q17fA4EivRzC75YvjDu8=
Showingallpublichostkeys:
| switch#  | show ssh host-key |       |                       |     |
| -------- | ----------------- | ----- | --------------------- | --- |
| Key Type | : ECDSA           | Curve | : ecdsa-sha2-nistp256 |     |
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAhtuv5rABBBGs
...
O4mjVFGMVKZ87RWkyrxeQa2fAGZZEp1902K33/k3q17fA4EivRzC75YvjDu8=
| Key Type | : ED25519 |     |     |     |
| -------- | --------- | --- | --- | --- |
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGb6910Jwoe8Hkl9K5YhqijrWI3yovNbiJVq6tw4WjJr4
| Key Type | : RSA | Key | Size : 2048 |     |
| -------- | ----- | --- | ----------- | --- |
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDdVCXlw43h4n1bwg9jI6DSBMngymCdPD0JUG42Sn9IS
...
nGSXtrNy6OmlFDJTAy+zz5Kd8d21ZLuhf07IHNgF3pff65Xc8qNJBv
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ssh        | server |            |             |            |
| --------------- | ------ | ---------- | ----------- | ---------- |
| show ssh server | [vrf   | <VRF-NAME> | | all-vrfs] | [vsx-peer] |
Description
ShowstheSSHserverconfigurationforthespecifiedVRF.Administratorscanshowtheserver
configurationofallVRFsbyusingtheall-vrfsparameter.IfnoVRFnameisprovidedinthiscommand,
thecommandshowstheSSHserverconfigurationonthedefaultVRF.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 34

| Parameter      |     |     |     |     |     | Description          |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
| vrf <VRF-NAME> |     |     |     |     |     | SpecifiestheVRFname. |     |     |     |     |     |
| all-vrfs       |     |     |     |     |     | SelectsallVRFs.      |     |     |     |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheSSHserverconfigurationonthedefaultVRF:
| switch#    | show          | ssh server |     |      |             |     |       |         |       |     |     |
| ---------- | ------------- | ---------- | --- | ---- | ----------- | --- | ----- | ------- | ----- | --- | --- |
| SSH server | configuration |            |     | on   | VRF default |     | :     |         |       |     |     |
| IP Version |               |            | :   | IPv4 | and IPv6    |     | SSH   | Version |       | :   | 2.0 |
| TCP Port   |               |            | :   | 22   |             |     | Grace | Timeout | (sec) | :   | 120 |
| Max Auth   | Attempts      |            | :   |      | 6           |     |       |         |       |     |     |
Ciphers:
| chacha20-poly1305@openssh.com,         |                 |               |                               |                         |               | aes128-ctr, | aes192-cbc,          |     |     |     |     |
| -------------------------------------- | --------------- | ------------- | ----------------------------- | ----------------------- | ------------- | ----------- | -------------------- | --- | --- | --- | --- |
| aes128-cbc,                            |                 | aes192-ctr,   |                               | aes256-gcm@openssh.com, |               |             |                      |     |     |     |     |
| aes128-gcm@openssh.com,                |                 |               |                               | aes256-ctr,             |               |             | aes256-cbc           |     |     |     |     |
| Host                                   | Key Algorithms: |               |                               |                         |               |             |                      |     |     |     |     |
| ecdsa-sha2-nistp256,                   |                 |               |                               | ecdsa-sha2-nistp384,    |               |             | ecdsa-sha2-nistp521, |     |     |     |     |
| ssh-ed25519,                           |                 | rsa-sha2-256, |                               |                         | rsa-sha2-512, |             | ssh-rsa              |     |     |     |     |
| Key Exchange                           |                 | Algorithms:   |                               |                         |               |             |                      |     |     |     |     |
| curve25519-sha256,                     |                 |               | curve25519-sha256@libssh.org, |                         |               |             |                      |     |     |     |     |
| ecdh-sha2-nistp256,ecdh-sha2-nistp384, |                 |               |                               |                         |               |             | ecdh-sha2-nistp521,  |     |     |     |     |
diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,
diffie-hellman-group18-sha512,diffie-hellman-group14-sha256,
diffie-hellman-group14-sha1
MACs:
| hmac-sha1-etm@openssh.com,  |     |                      |     |                                       | umac-64@openssh.com,        |                      |                  |     |     |     |     |
| --------------------------- | --- | -------------------- | --- | ------------------------------------- | --------------------------- | -------------------- | ---------------- | --- | --- | --- | --- |
| umac-128@openssh.com,       |     |                      |     | hmac-sha2-256,hmac-sha2-512,hmac-sha1 |                             |                      |                  |     |     |     |     |
| Public                      | Key | Algorithms:          |     |                                       |                             |                      |                  |     |     |     |     |
| rsa-sha2-256,               |     | rsa-sha2-512ssh-rsa, |     |                                       |                             | ecdsa-sha2-nistp256, |                  |     |     |     |     |
| ecdsa-sha2-nistp384,        |     |                      |     | ecdsa-sha2-nistp521,                  |                             |                      | ssh-ed25519,     |     |     |     |     |
| x509v3-rsa2048-sha256,      |     |                      |     | x509v3-ssh-rsa,                       |                             |                      | x509v3-sign-rsa, |     |     |     |     |
| x509v3-ecdsa-sha2-nistp256, |     |                      |     |                                       | x509v3-ecdsa-sha2-nistp384, |                      |                  |     |     |     |     |
x509v3-ecdsa-sha2-nistp521
ShowingtheSSHserverconfigurationonthemanagementVRF:
| switch#    | show          | ssh server |     | vrf | mgmt     |          |     |             |         |       |       |
| ---------- | ------------- | ---------- | --- | --- | -------- | -------- | --- | ----------- | ------- | ----- | ----- |
| SSH server | configuration |            |     | on  | VRF mgmt | :        |     |             |         |       |       |
| IP Version |               |            |     | :   | IPv4     | and IPv6 |     | SSH Version |         |       | : 2.0 |
| TCP        | Port          |            |     | :   | 22       |          |     | Grace       | Timeout | (sec) | : 120 |
| Max        | Auth          | Attempts   |     | :   | 6        |          |     |             |         |       |       |
SSHserver|35

Ciphers:
| chacha20-poly1305@openssh.com,         |          |               |                               | aes128-ctr,             |            | aes192-cbc,          |     |     |     |
| -------------------------------------- | -------- | ------------- | ----------------------------- | ----------------------- | ---------- | -------------------- | --- | --- | --- |
| aes128-cbc,                            |          | aes192-ctr,   |                               | aes256-gcm@openssh.com, |            |                      |     |     |     |
| aes128-gcm@openssh.com,                |          |               |                               | aes256-ctr,             | aes256-cbc |                      |     |     |     |
| Host                                   | Key      | Algorithms:   |                               |                         |            |                      |     |     |     |
| ecdsa-sha2-nistp256,                   |          |               | ecdsa-sha2-nistp384,          |                         |            | ecdsa-sha2-nistp521, |     |     |     |
| ssh-ed25519,                           |          | rsa-sha2-256, |                               | rsa-sha2-512,           |            | ssh-rsa              |     |     |     |
| Key                                    | Exchange | Algorithms:   |                               |                         |            |                      |     |     |     |
| curve25519-sha256,                     |          |               | curve25519-sha256@libssh.org, |                         |            |                      |     |     |     |
| ecdh-sha2-nistp256,ecdh-sha2-nistp384, |          |               |                               |                         |            | ecdh-sha2-nistp521,  |     |     |     |
diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,
diffie-hellman-group18-sha512,diffie-hellman-group14-sha256,
diffie-hellman-group14-sha1
MACs:
| hmac-sha1-etm@openssh.com,  |     |                      |                                       | umac-64@openssh.com,        |                      |                  |     |     |     |
| --------------------------- | --- | -------------------- | ------------------------------------- | --------------------------- | -------------------- | ---------------- | --- | --- | --- |
| umac-128@openssh.com,       |     |                      | hmac-sha2-256,hmac-sha2-512,hmac-sha1 |                             |                      |                  |     |     |     |
| Public                      | Key | Algorithms:          |                                       |                             |                      |                  |     |     |     |
| rsa-sha2-256,               |     | rsa-sha2-512ssh-rsa, |                                       |                             | ecdsa-sha2-nistp256, |                  |     |     |     |
| ecdsa-sha2-nistp384,        |     |                      | ecdsa-sha2-nistp521,                  |                             |                      | ssh-ed25519,     |     |     |     |
| x509v3-rsa2048-sha256,      |     |                      | x509v3-ssh-rsa,                       |                             |                      | x509v3-sign-rsa, |     |     |     |
| x509v3-ecdsa-sha2-nistp256, |     |                      |                                       | x509v3-ecdsa-sha2-nistp384, |                      |                  |     |     |     |
ShowingtheSSHserverconfigurationforallVRFs:
| switch#    | show          | ssh server | all-vrfs |             |      |     |               |       |       |
| ---------- | ------------- | ---------- | -------- | ----------- | ---- | --- | ------------- | ----- | ----- |
| SSH server | configuration |            | on       | VRF default | :    |     |               |       |       |
| IP Version |               |            | :        | IPv4 and    | IPv6 |     | SSH Version   |       | : 2.0 |
| TCP        | Port          |            | :        | 22          |      |     | Grace Timeout | (sec) | : 120 |
| Max        | Auth          | Attempts   | :        | 6           |      |     |               |       |       |
Ciphers:
| chacha20-poly1305@openssh.com,         |          |               |                               | aes128-ctr,             |            | aes192-cbc,          |     |     |     |
| -------------------------------------- | -------- | ------------- | ----------------------------- | ----------------------- | ---------- | -------------------- | --- | --- | --- |
| aes128-cbc,                            |          | aes192-ctr,   |                               | aes256-gcm@openssh.com, |            |                      |     |     |     |
| aes128-gcm@openssh.com,                |          |               |                               | aes256-ctr,             | aes256-cbc |                      |     |     |     |
| Host                                   | Key      | Algorithms:   |                               |                         |            |                      |     |     |     |
| ecdsa-sha2-nistp256,                   |          |               | ecdsa-sha2-nistp384,          |                         |            | ecdsa-sha2-nistp521, |     |     |     |
| ssh-ed25519,                           |          | rsa-sha2-256, |                               | rsa-sha2-512,           |            | ssh-rsa              |     |     |     |
| Key                                    | Exchange | Algorithms:   |                               |                         |            |                      |     |     |     |
| curve25519-sha256,                     |          |               | curve25519-sha256@libssh.org, |                         |            |                      |     |     |     |
| ecdh-sha2-nistp256,ecdh-sha2-nistp384, |          |               |                               |                         |            | ecdh-sha2-nistp521,  |     |     |     |
diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,
diffie-hellman-group18-sha512,diffie-hellman-group14-sha256,
MACs:
| hmac-sha1-etm@openssh.com, |     |                      |                                       | umac-64@openssh.com, |                      |              |     |     |     |
| -------------------------- | --- | -------------------- | ------------------------------------- | -------------------- | -------------------- | ------------ | --- | --- | --- |
| umac-128@openssh.com,      |     |                      | hmac-sha2-256,hmac-sha2-512,hmac-sha1 |                      |                      |              |     |     |     |
| Public                     | Key | Algorithms:          |                                       |                      |                      |              |     |     |     |
| rsa-sha2-256,              |     | rsa-sha2-512ssh-rsa, |                                       |                      | ecdsa-sha2-nistp256, |              |     |     |     |
| ecdsa-sha2-nistp384,       |     |                      | ecdsa-sha2-nistp521,                  |                      |                      | ssh-ed25519, |     |     |     |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 36

|     | x509v3-rsa2048-sha256,      |     |     |     | x509v3-ssh-rsa, |                             |     | x509v3-sign-rsa, |     |     |     |
| --- | --------------------------- | --- | --- | --- | --------------- | --------------------------- | --- | ---------------- | --- | --- | --- |
|     | x509v3-ecdsa-sha2-nistp256, |     |     |     |                 | x509v3-ecdsa-sha2-nistp384, |     |                  |     |     |     |
x509v3-ecdsa-sha2-nistp521
| SSH | server     | configuration |          |     | on VRF | mgmt | :    |     |               |       |       |
| --- | ---------- | ------------- | -------- | --- | ------ | ---- | ---- | --- | ------------- | ----- | ----- |
|     | IP Version |               |          |     | : IPv4 | and  | IPv6 |     | SSH Version   |       | : 2.0 |
|     | TCP        | Port          |          |     | : 22   |      |      |     | Grace Timeout | (sec) | : 120 |
|     | Max        | Auth          | Attempts |     | : 6    |      |      |     |               |       |       |
Ciphers:
|     | chacha20-poly1305@openssh.com,         |          |               |                               |                         | aes128-ctr,   |            |                      | aes192-cbc, |     |     |
| --- | -------------------------------------- | -------- | ------------- | ----------------------------- | ----------------------- | ------------- | ---------- | -------------------- | ----------- | --- | --- |
|     | aes128-cbc,                            |          | aes192-ctr,   |                               | aes256-gcm@openssh.com, |               |            |                      |             |     |     |
|     | aes128-gcm@openssh.com,                |          |               |                               | aes256-ctr,             |               | aes256-cbc |                      |             |     |     |
|     | Host                                   | Key      | Algorithms:   |                               |                         |               |            |                      |             |     |     |
|     | ecdsa-sha2-nistp256,                   |          |               |                               | ecdsa-sha2-nistp384,    |               |            | ecdsa-sha2-nistp521, |             |     |     |
|     | ssh-ed25519,                           |          | rsa-sha2-256, |                               |                         | rsa-sha2-512, |            | ssh-rsa              |             |     |     |
|     | Key                                    | Exchange | Algorithms:   |                               |                         |               |            |                      |             |     |     |
|     | curve25519-sha256,                     |          |               | curve25519-sha256@libssh.org, |                         |               |            |                      |             |     |     |
|     | ecdh-sha2-nistp256,ecdh-sha2-nistp384, |          |               |                               |                         |               |            | ecdh-sha2-nistp521,  |             |     |     |
diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,
diffie-hellman-group18-sha512,diffie-hellman-group14-sha256,
diffie-hellman-group14-sha1
MACs:
|                | hmac-sha1-etm@openssh.com,  |             |                      |         |                                       | umac-64@openssh.com,        |                      |                  |     |     |     |
| -------------- | --------------------------- | ----------- | -------------------- | ------- | ------------------------------------- | --------------------------- | -------------------- | ---------------- | --- | --- | --- |
|                | umac-128@openssh.com,       |             |                      |         | hmac-sha2-256,hmac-sha2-512,hmac-sha1 |                             |                      |                  |     |     |     |
|                | Public                      | Key         | Algorithms:          |         |                                       |                             |                      |                  |     |     |     |
|                | rsa-sha2-256,               |             | rsa-sha2-512ssh-rsa, |         |                                       |                             | ecdsa-sha2-nistp256, |                  |     |     |     |
|                | ecdsa-sha2-nistp384,        |             |                      |         | ecdsa-sha2-nistp521,                  |                             |                      | ssh-ed25519,     |     |     |     |
|                | x509v3-rsa2048-sha256,      |             |                      |         | x509v3-ssh-rsa,                       |                             |                      | x509v3-sign-rsa, |     |     |     |
|                | x509v3-ecdsa-sha2-nistp256, |             |                      |         |                                       | x509v3-ecdsa-sha2-nistp384, |                      |                  |     |     |     |
| Command        |                             | History     |                      |         |                                       |                             |                      |                  |     |     |     |
| Release        |                             |             |                      |         |                                       | Modification                |                      |                  |     |     |     |
| 10.07orearlier |                             |             |                      |         |                                       | --                          |                      |                  |     |     |     |
| Command        |                             | Information |                      |         |                                       |                             |                      |                  |     |     |     |
| Platforms      |                             | Command     |                      | context |                                       | Authority                   |                      |                  |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show | ssh | server | sessions |     |     |     |     |     |     |     |     |
| ---- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
show ssh server sessions [vrf <VRF-NAME> | all-vrfs] [vsx-peer]
Description
ShowstheactiveSSHsessionsonaspecifiedVRForonallVRFs.IfnoVRFisspecified,theactive
sessionsonthedefaultVRFareshown.
SSHserver|37

Parameter Description
vrf <VRF-NAME> SpecifiestheVRFname.
all-vrfs SelectsallVRFs.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
IfyouprovidethecommandwithaVRFname,thecommandshowstheactiveSSHsessionforthe
specifiedVRF.AnyusercanshowsessionsofallVRFsbyusingtheall-vrfsparameter.Themaximum
numberofsessionsperVRFisfive.ThemaximumSSHidlesessiontimeoutis60seconds.
Examples
ShowingtheactiveSSHsessionsonthedefaultVRF:
| switch# show | ssh server     | sessions              |
| ------------ | -------------- | --------------------- |
| SSH sessions | on VRF default |                       |
| IPv4 SSH     | Sessions       |                       |
| Server       | IP             | : 10.1.1.1            |
| Client       | IP             | : 10.1.1.2            |
| Client       | Port           | : 58835               |
| IPv6 SSH     | Sessions       |                       |
| Server       | IP             | : FF01:0:0:0:0:0:0:FB |
| Client       | IP             | : FF01:0:0:0:0:0:0:FC |
| Client       | Port           | : 58836               |
ShowingtheSSHserverconfigurationforallVRFs:
| switch# show | ssh server     | sessions all-vrf      |
| ------------ | -------------- | --------------------- |
| SSH sessions | on VRF mgmt    |                       |
| IPv4 SSH     | Sessions       |                       |
| Server       | IP             | : 10.1.1.1            |
| Client       | IP             | : 10.1.1.2            |
| Client       | Port           | : 58835               |
| IPv6 SSH     | Sessions       |                       |
| Server       | IP             | : FF01:0:0:0:0:0:0:FB |
| Client       | IP             | : FF01:0:0:0:0:0:0:FC |
| Client       | Port           | : 58836               |
| SSH sessions | on VRF default |                       |
| IPv4 SSH     | Sessions       |                       |
| Server       | IP             | : 20.1.1.1            |
| Client       | IP             | : 20.1.1.2            |
| Client       | Port           | : 58837               |
| IPv6 SSH     | Sessions       |                       |
| Server       | IP             | : FF01:0:0:0:0:0:0:FD |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 38

| Client              | IP      | : FF01:0:0:0:0:0:0:FE |              |
| ------------------- | ------- | --------------------- | ------------ |
| Client              | Port    | : 58838               |              |
| Command History     |         |                       |              |
| Release             |         |                       | Modification |
| 10.07orearlier      |         |                       | --           |
| Command Information |         |                       |              |
| Platforms           | Command | context               | Authority    |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
(#)
ssh ciphers
| ssh ciphers | <CIPHERS-LIST> |     |     |
| ----------- | -------------- | --- | --- |
no ssh ciphers
Description
ConfiguresSSHtouseasetofciphersinthespecifiedpriorityorder.CiphersinSSHareusedforprivacy
ofdatabeingtransportedovertheconnection.ThefirstciphertypeenteredintheCLIisconsidereda
firstpriority.Eachoptionisanalgorithmthatisusedtoencryptthelinkandeachnameindicatesthe
algorithmandcryptographicparametersthatareused.Onlyciphersthatareenteredbytheuserare
configured.
ThenoformofthiscommandremovestheconfigurationofciphersandrevertsSSHtousethedefault
setofciphers.
| Parameter      |     |     | Description   |
| -------------- | --- | --- | ------------- |
| <CIPHERS-LIST> |     |     | Validciphers: |
aes128-cbc
n
n aes192-cbc
aes256-cbc
n
n aes128-ctr
aes192-ctr
n
n aes256-ctr
n aes128-gcm@openssh.com
n aes256-gcm@openssh.com
n chacha20-poly1305@openssh.com
Defaultsetofciphersinpriorityorder(highestattop):
n chacha20-1305@openssh.com
n aes128-ctr
n aes192-ctr
n aes256-ctr
aes128-gcm@openssh.com
n
n aes256-gcUm@openssh.com
SSHserver|39

Examples
ConfiguringSSHtouseonlyspecifiedciphersinthepriorityorder:
switch(config)#
ssh ciphers chacha20-poly1305@openssh.com aes256-ctr aes256-cbc
RevertingSSHtousethedefaultsetofciphers:
| switch(config)# | no          | ssh ciphers |              |     |     |
| --------------- | ----------- | ----------- | ------------ | --- | --- |
| Command         | History     |             |              |     |     |
| Release         |             |             | Modification |     |     |
| 10.07orearlier  |             |             | --           |     |     |
| Command         | Information |             |              |     |     |
| Platforms       | Command     | context     | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ssh host-key
ssh host-key {ecdsa [ecdsa-sha2-nistp256 | ecdsa-sha2-nistp384 | ecdsa-sha2-nistp521] |
| ed25519 | | rsa [bits | {2048 | 4096}] | }   |     |     |
| ------- | ----------- | -------------- | --- | --- | --- |
Description
GeneratesanSSHhost-keypair.
| Parameter |     |     | Description                                          |     |     |
| --------- | --- | --- | ---------------------------------------------------- | --- | --- |
| ecdsa     |     |     | SelectstheECDSAhost-keypairtypeasecdsa-sha2-nistp256 |     |     |
(thedefault),ecdsa-sha2-nistp384,orecdsa-sha2-
nistp521.
| ed25519 |     |     | SelectstheED25519host-keypair.                         |                        |       |
| ------- | --- | --- | ------------------------------------------------------ | ---------------------- | ----- |
| rsa     |     |     | SelectstheRSAhost-keypair.Optionally,thekeybitlengthis |                        |       |
|         |     |     | selectedwitheitherbits                                 | 2048(thedefault)orbits | 4096. |
Usage
WhenanSSHserverisenabledonaVRFforthefirsttime,host-keysaregenerated.
Ifthehost-keyofthegiventypeexists,awarningmessageisdisplayedwitharequesttooverwritethe
previoushost-keywiththenewkey.
Examples
OverwritinganoldECDSAhost-keywithanewecdsa-sha2-nistp384host-key:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 40

| switch(config)# | ssh         | host-key        | ecdsa ecdsa-sha2-nistp384 |
| --------------- | ----------- | --------------- | ------------------------- |
| ecdsa host-key  | will        | be overwritten. |                           |
| Do you want     | to continue | (y/n)?          |                           |
OverwritinganoldRSAhost-keywithanewRSAhost-keywith2048bits:
| switch(config)# | ssh         | host-key     | rsa bits 2048 |
| --------------- | ----------- | ------------ | ------------- |
| rsa host-key    | will be     | overwritten. |               |
| Do you want     | to continue | (y/n)?       |               |
OverwritinganECDSAhost-keywithanED25519host-keypair:
| switch(config)#     | ssh         | host-key        | ed25519      |
| ------------------- | ----------- | --------------- | ------------ |
| ed25519 host-key    | will        | be overwritten. |              |
| Do you want         | to continue | (y/n)?          |              |
| Command History     |             |                 |              |
| Release             |             |                 | Modification |
| 10.07orearlier      |             |                 | --           |
| Command Information |             |                 |              |
| Platforms           | Command     | context         | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ssh host-key-algorithms
| ssh host-key-algorithms |     | <HOST-KEY-ALGORITHMS-LIST> |     |
| ----------------------- | --- | -------------------------- | --- |
no ssh host-key-algorithms
Description
ConfiguresSSHtouseasetofhostkeyalgorithmsinthespecifiedpriorityorder.Hostkeyalgorithms
specifywhichhostkeytypesareallowedtobeusedfortheSSHconnection.Thefirsthostkeyenteredin
theCLIisconsideredafirstpriority.Eachoptionrepresentsatypeofkeythatcanbeused.Hostkeys
areusedtoverifythehostthatyouareconnectingto.Thisconfigurationallowsyoutocontrolwhich
hostkeytypesarepresentedtoincomingclients,orwhichhostkeytypestoreceivefirstfromhosts.
Onlythehostkeyalgorithmsthatarespecifiedbytheuserareconfigured.
ThenoformofthiscommandremovestheconfigurationofhostkeyalgorithmsandrevertsSSHtouse
thedefaultsetofalgorithms.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<HOST-KEY-ALGORITHMS-LIST> Defaultsetofpublickeyalgorithmsinpriorityorder(highestat
top),comprisedofallpossiblevalidalgorithms:
n ecdsa-sha2-nistp256
n ecdsa-sha2-nistp384
SSHserver|41

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
n ecdsa-sha2-nistp521
ssh-ed25519
n
n rsa-sha2-256
n rsa-sha2-512
n ssh-rsa
Examples
ConfiguringSSHtouseonlyspecifiedhostkeyalgorithms:
switch(config)# ssh host-key-algorithms ssh-rsa ssh-ed25519 ecdsa-sha2-nistp521
RevertingSSHtousethedefaultsetofhostkeyalgorithms:
| switch(config)#     | no      | host-key-algorithms |              |
| ------------------- | ------- | ------------------- | ------------ |
| Command History     |         |                     |              |
| Release             |         |                     | Modification |
| 10.07orearlier      |         |                     | --           |
| Command Information |         |                     |              |
| Platforms           | Command | context             | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ssh key-exchange-algorithms
| ssh key-exchange-algorithms |     | <KEY-EXCHANGE-ALGORITHMS-LIST> |     |
| --------------------------- | --- | ------------------------------ | --- |
no ssh key-exchange-algorithms
Description
ConfiguresSSHtouseasetofkeyexchangealgorithmtypesinthespecifiedpriorityorder.Thefirstkey
exchangetypeenteredintheCLIisconsideredafirstpriority.Keyexchangealgorithmsareusedto
exchangeasharedsessionkeywithapeersecurely.Eachoptionrepresentsanalgorithmthatisusedto
distributeasharedkeyinawaythatpreventsoutsideinterference,manipulation,orrecovery.Onlythe
keyexchangealgorithmsthatarespecifiedbytheuserareconfigured.
ThenoformofthiscommandremovestheconfigurationofkeyexchangealgorithmsandrevertsSSHto
usethedefaultsetofalgorithms.
| Parameter                      |     |     | Description                 |
| ------------------------------ | --- | --- | --------------------------- |
| <KEY-EXCHANGE-ALGORITHMS-LIST> |     |     | Validkeyexchangealgorithms: |
n curve25519-sha256
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 42

Parameter

Description

n curve25519-sha256@libssh.org
n diffie-hellman-group-exchange-sha1
n diffie-hellman-group-exchange-sha256
n diffie-hellman-group14-sha1
n diffie-hellman-group14-sha256
n diffie-hellman-group16-sha512
n diffie-hellman-group18-sha512
n ecdh-sha2-nistp256
n ecdh-sha2-nistp384
n ecdh-sha2-nistp521

Default set of key exchange algorithms in priority order (highest at
top):
n curve25519-sha256
n curve25519-sha256@libssh.org
n ecdh-sha2-nistp256
n ecdh-sha2-nistp384
n ecdh-sha2-nistp521
n diffie-hellman-group-exchange-sha256
n diffie-hellman-group16-sha512
n diffie-hellman-group18-sha512
n diffie-hellman-group14-sha256
n diffie-hellman-group-exchange-sha1

Examples

Configuring SSH to use a set of specified key exchange algorithms:

switch(config)# ssh key-exchange-algorithms ecdh-sha2-nistp256 curve25519-sha256

diffie-hellman-group-exchange-sha256

Reverting SSH to use the default set of key-exchange-algorithms:

switch(config)# no key-exchange-algorithms

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution
rights for this command.

ssh known-host remove

SSH server | 43

ssh known-host remove {all | {<IPv4-ADDRESS> | <HOSTNAME> | <IPv6-ADDRESS>} }
Description
ClearsthelistoftrustedSSHserversforyouruseraccount.Whenyoudownloadoruploadafiletoor
fromaserverusingSFTP,youestablishatrustedSSHrelationshipwiththatserver.Eachuseraccount
maintainsitsownsetofSSHserverhost-keysforeveryservertowhichtheuserpreviouslyconnected.
| Parameter      |     |     | Description                               |
| -------------- | --- | --- | ----------------------------------------- |
| all            |     |     | Clearsthetrustedserverslist.              |
| <IPv4-ADDRESS> |     |     | SpecifiestheIPv4addressoftheremotedevice. |
<HOSTNAME> Specifiesthehostnameoftheremotedevice.Range:upto255
characters.
| <IPv6-ADDRESS> |     |     | SpecifiestheIPv6addressoftheremotedevice. |
| -------------- | --- | --- | ----------------------------------------- |
Examples
Clearingthetrustedserverlist:
| switch(config)# | ssh | known-host | remove all |
| --------------- | --- | ---------- | ---------- |
Removingaspecifiedserverfromthetrustedserverlist:
| switch(config)#     | ssh     | known-host | remove 1.1.1.1 |
| ------------------- | ------- | ---------- | -------------- |
| Command History     |         |            |                |
| Release             |         |            | Modification   |
| 10.07orearlier      |         |            | --             |
| Command Information |         |            |                |
| Platforms           | Command | context    | Authority      |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ssh macs
ssh macs <MACS-LIST>
no ssh macs
Description
ConfiguresSSHtouseasetofmessageauthenticationcodes(MACs)inthespecifiedpriorityorder.The
firstMACenteredintheCLIisconsideredafirstpriority.MACsmaintaintheintegrityofeachmessage
sentacrossanSSHconnection.Eachoptionrepresentsanalgorithmthatcanbeusedtoprovide
integritybetweenpeers.OnlytheMACtypesthatarespecifiedbytheuserareconfigured.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 44

ThenoformofthiscommandremovestheconfigurationofMACsandrevertsSSHtousethedefaultset
ofMACs.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<MACS-LIST>
ValidMACs:
n hmac-sha1
hmac-sha1-96
n
n hmac-sha1-etm@openssh.com
hmac-sha2-256
n
n hmac-sha2-512
n hmac-sha2-256-etm@openssh.com
n hmac-sha2-512-etm@openssh.com
DefaultsetofMACsinpriorityorder(highestattop):
hmac-sha2-256-etm@openssh.com
n
n hmac-sha2-512-etm@openssh.com
n hmac-sha1-etm@openssh.com
n hmac-sha2-256
n hmac-sha2-512
hmac-sha1
n
Examples
ConfiguringSSHtouseasetofspecifiedMACs:
| switch(config)# | ssh | macs hmac-sha2-256 | hmac-sha2-512 |
| --------------- | --- | ------------------ | ------------- |
RevertingSSHtousethedefaultsetofMACs:
| switch(config)#     | no      | ssh macs |              |
| ------------------- | ------- | -------- | ------------ |
| Command History     |         |          |              |
| Release             |         |          | Modification |
| 10.07orearlier      |         |          | --           |
| Command Information |         |          |              |
| Platforms           | Command | context  | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ssh maximum-auth-attempts
| ssh maximum-auth-attempts |     | <ATTEMPTS> |     |
| ------------------------- | --- | ---------- | --- |
no maximum-auth-attempts
Description
SetstheSSHmaximumnumberofauthenticationattempts.
SSHserver|45

Thenoformofthecommandresetsthemaximumtoitsdefaultof6.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<ATTEMPTS> SpecifiesthemaximumnumberofSSHauthenticationattempts.
Range:1to10.Default:6.
Examples
Settingthemaximumnumberofauthenticationattempts:
| switch(config)# | ssh | maximum-auth-attempts | 3   |
| --------------- | --- | --------------------- | --- |
Resettingthemaximumnumberofauthenticationattemptstoitsdefaultof6:
| switch(config)#     | no      | maximum-auth-attempts |              |
| ------------------- | ------- | --------------------- | ------------ |
| Command History     |         |                       |              |
| Release             |         |                       | Modification |
| 10.07orearlier      |         |                       | --           |
| Command Information |         |                       |              |
| Platforms           | Command | context               | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ssh public-key-algorithms
| ssh public-key-algorithms |     | <PUBLIC-KEY-ALGORITHMS-LIST> |     |
| ------------------------- | --- | ---------------------------- | --- |
no ssh public-key-algorithms
Description
ConfiguresSSHtouseasetofpublickeyalgorithmsinthespecifiedpriorityorder.Thefirstpublickey
typeenteredintheCLIisconsideredafirstpriority.Publickeyalgorithmsspecifywhichpublickeytypes
canbeusedforpublickeyauthenticationinSSH.EachoptionrepresentsapublickeytypethattheSSH
servercanacceptorthattheSSHclientcanpresenttoaserver.Onlythepublickeyalgorithmsthatare
chosenbytheuserareconfigured.
ThenoformofthiscommandremovestheconfigurationofpublickeyalgorithmsandrevertsSSHtouse
thedefaultset.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<PUBLIC-KEY-ALGORITHMS-LIST> Defaultsetofpublickeyalgorithmsinpriorityorder(highestat
top),comprisedofallpossiblevalidalgorithms:
rsa-sha2-256
n
n rsa-sha2-512
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 46

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
n ssh-rsa
ecdsa-sha2-nistp256
n
n ecdsa-sha2-nistp384
n ecdsa-sha2-nistp521
n ssh-ed25519
n x509v3-rsa2048-sha256
x509v3-ssh-rsa
n
n x509v3-sign-rsa
x509v3-ecdsa-sha2-nistp256
n
n x509v3-ecdsa-sha2-nistp384
x509v3-ecdsa-sha2-nistp521
n
Examples
ConfiguringSSHtouseasetofspecifiedpublickeyalgorithms:
switch(config)# ssh public-key-algorithms x509v3-ssh-rsa ssh-rsa rsa-sha2-256
RevertingSSHtousethedefaultsetofpublickeyalgorithms:
| switch(config)#     | no      | ssh public-key-algorithms |              |
| ------------------- | ------- | ------------------------- | ------------ |
| Command History     |         |                           |              |
| Release             |         |                           | Modification |
| 10.07orearlier      |         |                           | --           |
| Command Information |         |                           |              |
| Platforms           | Command | context                   | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ssh server     | vrf            |     |     |
| -------------- | -------------- | --- | --- |
| ssh server vrf | <VRF-NAME>     |     |     |
| no ssh server  | vrf <VRF-NAME> |     |     |
Description
EnablestheSSHserveronthespecifiedVRF.
ThenoformofthecommanddisablestheSSHserveronthespecifiedVRF.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vrf <VRF-NAME>
SpecifiestheVRFname.
SSHserver|47

Examples
EnablingtheSSHserveronthemanagementVRF:
switch(config)#
|     | ssh | server vrf | mgmt |
| --- | --- | ---------- | ---- |
DisablingtheSSHserveronthemanagementVRF:
| switch(config)#     | no      | ssh server vrf | mgmt         |
| ------------------- | ------- | -------------- | ------------ |
| Command History     |         |                |              |
| Release             |         |                | Modification |
| 10.07orearlier      |         |                | --           |
| Command Information |         |                |              |
| Platforms           | Command | context        | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 48

Chapter 5

SSH client

SSH client

The switch provides an SSH client that enables the switch to log in to an SSH server such as another
switch, typically for command execution purposes. The SSH client provides secure encrypted
communications between the switch and the SSH server over any network.

SSH client commands

ssh (client login)
ssh [<USERNAME>@]{<IPV4> | <HOSTNAME>} [vrf <VRF-NAME>] [port <PORT-NUMBER>]

Description

Establishes a client session with an SSH server which is typically another switch.

Parameter

<USERNAME>

<IPV4>

<HOSTNAME>

vrf <VRF-NAME>

port <PORT-NUMBER>

Examples

Description

Specifies the username that the client uses to log in to an SSH
server. When omitted, the username of the current session is
used.

Specifies the SSH server to which the SSH client will connect as an
IPv4 address.

Specifies the SSH server to which the SSH client will connect as a
host name.

Specifies the VRF to be used for the SSH client session. When
omitted, the default VRF named default is used.

Specifies the SSH server TCP port number. When omitted, the
default TCP port 22 is used.

Establishing an SSH client session (using the management VRF) with an SSH server:

switch# ssh admin@10.0.11.180 vrf mgmt

Establishing an SSH client session (using the default VRF and a specific port) with an SSH server:

switch# ssh admin@10.0.11.175 port 223

Configuring a test user on switch 1 and then connecting to switch 1 from switch 2 using the SSH client on
the mgmt VRF:

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

49

| ** Configuring | a test | user | on switch | 1 ** |     |     |
| -------------- | ------ | ---- | --------- | ---- | --- | --- |
switch(config)#
|                              | user-group |     | test   |             |      |     |
| ---------------------------- | ---------- | --- | ------ | ----------- | ---- | --- |
| switch(config-usr-grp-test)# |            |     | permit | cli command | ".*" |     |
| switch(config)#              | exit       |     |        |             |      |     |
switch(config)# user test-user group test password plaintext tst#9J
| ** On switch        | 2, connecting         |         | to switch | 1 using the  | SSH client | **  |
| ------------------- | --------------------- | ------- | --------- | ------------ | ---------- | --- |
| switch# ssh         | test-user@10.0.11.177 |         |           | vrf mgmt     |            |     |
| Command History     |                       |         |           |              |            |     |
| Release             |                       |         |           | Modification |            |     |
| 10.07orearlier      |                       |         |           | --           |            |     |
| Command Information |                       |         |           |              |            |     |
| Platforms           | Command               | context |           | Authority    |            |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
SSHclient|50

Chapter 6

Local AAA

Local AAA

Local AAA on your Aruba switch provides:

n Authentication using local password or SSH public key.

n Authorization using local role-based access control (RBAC). Optional per-command authorization is

possible through configuration of user-defined local user groups, with command authorization rules
applied to respective group members.

n Accounting of user activity on the switch using accounting logs.

For switches that support multiple management modules such as the Aruba 8400, all AAA functionality discussed

only applies to the active management module. See also AAA on switches with multiple management modules in the
High Availability Guide.

Local AAA defaults and limits

Setting

Default value / limit

Local authentication

Enabled by default for all connection types: console, SSH, and REST.

Local role-based access control (RBAC)
authorization

Enabled by default for all connection types: console, SSH, and REST.

Local accounting

Enabled.

Maximum number of local users

64 users, including the default admin user.

Maximum number of user-defined local
user groups

32 groups, including the three built-in groups administrators,
operators, auditors.

Password for default admin account

The password is empty by default.

SSH public key authentication

Enabled.

Local authentication

Authentication identifies users, validates their credentials, and grants switch access. Local authentication
is either password-based or SSH public key-based.

Password-based local authentication

n Validates users with local user name and password credentials

n Is supported on all interfaces/channels (SSH, WebUI, Console, REST)

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

51

n IsenabledbydefaultbutcanbesupersededbyremoteauthenticationorwithSSHclientusingSSH
publickeyauthentication
| SSH public | key-based | local authentication |     |     |     |
| ---------- | --------- | -------------------- | --- | --- | --- |
n ValidatesusersidentifiedwithSSHpublickeysstoredinthelocaluserdatabase
n IssupportedontheSSHinterface/channelwithSSHclient
n Takesprecedenceoverpassword-basedauthenticationwhetherlocalorremote
n Isenabledbydefault(alsorequireskeyconfigurationtowork)
| Local authentication |     | tasks |     |     |     |
| -------------------- | --- | ----- | --- | --- | --- |
Thelocalauthentication(localpasswordandSSHpublickey)tasksareasfollows:
Command
| Task |     | Example |     |     |     |
| ---- | --- | ------- | --- | --- | --- |
name
Enable aaa Enablelocalauthenticationforthedefaultandconsoleconnectiontypes:
authenticati authenticati aaa authentication login default local
| onaslocal |     | aaa authentication | login console | local |     |
| --------- | --- | ------------------ | ------------- | ----- | --- |
on login
forthe
specified
connection
types
| Show         | show aaa     | show aaa authentication |     |     |     |
| ------------ | ------------ | ----------------------- | --- | --- | --- |
| authenticati | authenticati |                         |     |     |     |
on
on
configuratio
n
| Enable    | aaa          | aaa authentication | minimum-password-length |     | 12  |
| --------- | ------------ | ------------------ | ----------------------- | --- | --- |
| password- | authenticati |                    |                         |     |     |
based
on minimum-
authenticati
password-
onminimum
| password | length |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- |
length
checking
| Disable | aaa | no aaa authentication | minimum-password-length |     |     |
| ------- | --- | --------------------- | ----------------------- | --- | --- |
password-
authenticati
based
on minimum-
authenticati
password-
onminimum
length
password
length
checking
Enablelocal aaa aaa authentication limit-login-attempts 4 lockout-time 20
password-
authenticati
| based | on limit- |     |     |     |     |
| ----- | --------- | --- | --- | --- | --- |
authenticati
login-
onlogin
attempts
attempt
limiting
| Disablelocal | aaa | no aaa authentication | limit-login-attempts |     |     |
| ------------ | --- | --------------------- | -------------------- | --- | --- |
LocalAAA|52

Command
| Task |     | Example |     |     |
| ---- | --- | ------- | --- | --- |
name
| password-    | authenticati |     |     |     |
| ------------ | ------------ | --- | --- | --- |
| based        | on limit-    |     |     |     |
| authenticati | login-       |     |     |     |
onlogin
attempts
attempt
limiting
| Enablelocal | ssh password- | ssh password-authentication |     |     |
| ----------- | ------------- | --------------------------- | --- | --- |
| password-   | authenticati  |                             |     |     |
| based       | on            |                             |     |     |
authenticati
onforuse
withSSH
clients
(enabledby
default)
| Disablelocal | ssh password- | no ssh password-authentication |     |     |
| ------------ | ------------- | ------------------------------ | --- | --- |
| password-    | authenticati  |                                |     |     |
based
on
authenticati
onforuse
withSSH
clients
| EnableSSH | ssh public- | ssh public-key-authentication |     |     |
| --------- | ----------- | ----------------------------- | --- | --- |
| publickey | key-        |                               |     |     |
authenticati
authenticati
on(enabled
on
bydefault)
| DisableSSH | ssh public- | no ssh public-key-authentication |     |     |
| ---------- | ----------- | -------------------------------- | --- | --- |
| publickey  | key-        |                                  |     |     |
authenticati
authenticati
on
on
| Showstate | show ssh     | show ssh authentication-method |     |     |
| --------- | ------------ | ------------------------------ | --- | --- |
| oflocal   | authenticati |                                |     |     |
password-
on-method
based(for
SSH)and
SSHpublic
key
authenticati
on
Copyingthe user user admin authorized-key ecdsa-sha2-nistp256
| clientSSH | authorized- | E2VjZH...QUiCAk= | root@switch |     |
| --------- | ----------- | ---------------- | ----------- | --- |
publickey
key
intothekey
list
| Removing  | user        | no user admin | authorized-key | 2   |
| --------- | ----------- | ------------- | -------------- | --- |
| SSHpublic | authorized- |               |                |     |
keysfrom
key
thekeylist
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 53

Command
| Task |     | Example |     |     |     |
| ---- | --- | ------- | --- | --- | --- |
name
| Showingthe | show user | show user | admin authorized-key |     |     |
| ---------- | --------- | --------- | -------------------- | --- | --- |
SSHclient
publickey
list
Local authorization
Authorizationcontrolsauthenticateduserscommandexecutionandswitchinteractionprivileges.Local
authorizationusesrole-basedaccesscontrol(RBAC)toproviderole-basedprivilegelevelsplusoptional
user-definedlocalusergroupswithcommandexecutionrules.Authorizationoccursonlyafter
successfulauthentication.
Administratorshavefullcommandexecutionandswitchinteractionprivilege.
n
n Operatorsarelimitedtotheuseofseveralnonsensitiveshowcommands.
n Auditorsarelimitedtoafewauditing-relatedcommands.
Optionalper-commandauthorizationisavailablethroughconfigurationofuser-definedlocaluser
groupswithcommandauthorizationrulesappliedtorespectivegroupmembers.seeUser-defineduser
groups .
| Local authorization |     | tasks |     |     |     |
| ------------------- | --- | ----- | --- | --- | --- |
Thelocalauthorizationtasksareasfollows:
| Task | Command | name | Example |     |     |
| ---- | ------- | ---- | ------- | --- | --- |
Enableauthorization aaa authorization Enablelocalauthorizationforthedefaultandconsole
| aslocalRBACforthe   | commands      |     | connectiontypes:       |                  |       |
| ------------------- | ------------- | --- | ---------------------- | ---------------- | ----- |
| specifiedconnection |               |     | aaa authorization      | commands default | local |
| types               |               |     | aaa authorization      | commands console | local |
| Showauthorization   | show aaa      |     | show aaa authorization |                  |       |
| configuration       | authorization |     |                        |                  |       |
Local accounting
Localaccountingisalwaysactive.Itcannotbeturnedoff.
Thisaccountinginformationiscapturedandmadeavailablelocally(usingshow accounting log)and,if
desired,forsendingtoremoteAAAservers:
n ExecAccounting:userlogin/logoutevents.
n Commandaccounting:commandsexecutedbyusers.
n Systemaccounting:remoteaccountingOn/Offevents.
n CLIshowcommands.
Interactionsonthenon-CLIinterfaces:RESTandWebUI.
n
Thefollowingisnotcapturedormadeavailableasaccountinginformation:
LocalAAA|54

n CLIcommandsthatreboottheswitch.
n Interactionsinthebashshell.
| Seealsotheshow   | accounting | logcommand. |     |     |     |     |
| ---------------- | ---------- | ----------- | --- | --- | --- | --- |
| Local accounting |            | tasks       |     |     |     |     |
Thelocalaccountingtasksareasfollows:
Command
| Task |     |     | Example |     |     |     |
| ---- | --- | --- | ------- | --- | --- | --- |
name
Enableaccounting aaa accounting Enablelocalaccountingforthedefaultandconsoleconnection
| aslocalforthe | all-mgmt |     | types:         |                  |            |       |
| ------------- | -------- | --- | -------------- | ---------------- | ---------- | ----- |
| specified     |          |     | aaa accounting | all-mgmt default | start-stop | local |
connectiontypes aaa accounting all-mgmt console start-stop local
| Showaccounting | show | aaa | show aaa accounting |     |     |     |
| -------------- | ---- | --- | ------------------- | --- | --- | --- |
configuration
accounting
|               |            |     | show accounting | log last 10 |     |     |
| ------------- | ---------- | --- | --------------- | ----------- | --- | --- |
| Showlocal     | show       |     |                 |             |     |     |
| accountinglog | accounting | log |                 |             |     |     |
contents
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 55

Chapter 7

Local AAA commands

Local AAA commands

aaa accounting all-mgmt
aaa accounting all-mgmt <CONNECTION-TYPE> start-stop {local | group <GROUP-LIST>}
no aaa accounting all-mgmt <CONNECTION-TYPE>

Description

Defines accounting as being local (with the name local) (the default). Or defines a sequence of remote
AAA server groups to be accessed for accounting purposes.

For remote accounting, the information is sent to the first reachable remote server that was configured
with this command for remote accounting. If no remote server is reachable, local accounting remains
available. Each available connection type (channel) can be configured individually as either local or using
remote AAA server groups. All server groups named in your command, must exist. This command can
be issued multiple times, once for each connection type. Local is always available for any connection
type not configured for remote accounting.

The system accounting log is not associated with any connection type (channel) and is therefore sent to the

accounting method configured on the default connection type (channel) only.

The no form of this command removes for the specified connection type, any defined remote AAA server
group accounting sequence. Local accounting is available for connection types without a configured
remote AAA server group list (whether default or for the specific connection type).

Parameter

Description

<CONNECTION-TYPE>

One of these connection types (channels):
default

Defines a list of accounting server groups to be used for the
default connection type. This configuration applies to all
other connection types (console, https-server, ssh) that
are not explicitly configured with this command. For example,
if you do not use aaa accounting all-mgmt console...
to define the console accounting list, then this default
configuration is used for console.

console

Defines a list of accounting server groups to be used for the
console connection type.

https-server

Defines a list of accounting server groups to be used for the
https-server (REST, Web UI) connection type.

ssh

Defines a list of accounting server groups to be used for the
ssh connection type.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

56

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
start-stop Selectsaccountinginformationcaptureatboththebeginningand
endofaprocess.
local
Selectslocal-onlyaccountingwhenusedwithoutthegroup
parameter.
group <GROUP-LIST> SpecifiesthelistofremoteAAAservergroupnames.Eachname
canbespecifiedonetime.PredefinedremoteAAAgroupnames
tacacsandradiusareavailable.Althoughnotagroupname,
predefinednamelocalisavailable.User-definedTACACS+and
RADIUSservergroupnamesmayalsobeused.
TheremoteAAAservergroupsareaccessedintheorderthatthe
groupnamesarelistedinthiscommand.Withineachgroup,the
serversareaccessedintheorderinwhichtheserverswereadded
tothegroup.Servergroupsaredefinedusingcommandaaa
group serverandserversareaddedtoaservergroupwiththe
commandserver.
Usage
Localaccountingisalwaysactive.Itcannotbeturnedoff.
Examples
Settinglocalaccountingforthedefaultconnectiontype:
switch(config)#
|     | aaa | accounting | all-mgmt default | start-stop | local |
| --- | --- | ---------- | ---------------- | ---------- | ----- |
Settinglocalaccountingfortheconsoleconnectiontype:
switch(config)# aaa accounting all-mgmt console start-stop local
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| aaa authentication |     | console-login-attempts |     |     |     |
| ------------------ | --- | ---------------------- | --- | --- | --- |
aaa authentication console-login-attempts <ATTEMPTS> console-lockout-time <LOCKOUT-TIME>
| no aaa authentication |     | console-login-attempts |     |     |     |
| --------------------- | --- | ---------------------- | --- | --- | --- |
Description
LocalAAAcommands|57

Fortheconsoleinterfaceonly(notSSHorREST),enablesconsoleloginattemptlimiting.Ifthenumberof
failedconsoleloginattemptsequalstheconfiguredthreshold,theuserislockedoutfortheconfigured
duration..
Thenoformofthiscommanddisablesconsoleloginattemptlimits.
Important:IfyouenablethelockoutusingthiscommandandalsoenabletheSSHandRESTlockoutusing
commandaaa authentication limit-login-attempts,andthenentertoomanyconsecutivewrong
passwords,youwillbecomelockedout,andwillhavetowaitfortheconfiguredlockouttimetoelapsebefore
logginginonanyinterface.
ThisconsoleloginattemptlimitingfeatureisonlyavailablewhennotusingremoteauthenticationthroughAAA
servers(TACACS+orRADIUS)onanyinterface.RemoteauthenticationthroughAAAservers(TACACS+orRADIUS)
isnotpossiblewhenlimitloginattemptsisconfiguredonanyinterface.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<ATTEMPTS> Specifiesthethresholdoffailedconsoleloginattemptsthat
triggersuserlockout.Range:1to10.Forexample,if<ATTEMPTS>
issetto1,asinglefailedloginattempttriggersimmediateuser
lockout.
<LOCKOUT-TIME> Specifiestheamountoftimeauserislockedout.Range:1to3600
seconds.
Examples
Enablingconsoleloginattemptfailurelimitingwitha60secondlockoutbeingtriggereduponthethird
consecutiveloginattemptfailure.
switch(config)# aaa authentication console-login-attempts 3 console-lockout-time
60
Disablingconsoleloginattemptfailurelimiting:
| switch(config)#     | no      | aaa authentication | console-login-attempts |
| ------------------- | ------- | ------------------ | ---------------------- |
| Command History     |         |                    |                        |
| Release             |         |                    | Modification           |
| 10.07orearlier      |         |                    | --                     |
| Command Information |         |                    |                        |
| Platforms           | Command | context            | Authority              |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 58

aaa authentication limit-login-attempts
aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>
no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>

Description

For the SSH and REST interface, enables local login attempt limiting. If the number of failed local login
attempts equals the configured threshold, the user is locked out for the configured duration.

The no form of this command disables local login attempt limits.

Important: If you enable the lockout using this command and also enable the console lockout using command
aaa authentication console-login-attempts, and then enter too many consecutive wrong passwords,
you will become locked out, and will have to wait for the configured lockout time to elapse before logging in on

any interface.

This local login attempt limiting feature is only available when not using remote authentication through AAA

servers (TACACS+ or RADIUS) on any interface. Remote authentication through AAA servers (TACACS+ or RADIUS)

is not possible when limit login attempts is configured on any interface.

Parameter

<ATTEMPTS>

<LOCKOUT-TIME>

Examples

Description

Specifies the threshold of failed local login attempts that triggers
user lockout. Range: 1 to 10. For example, if <ATTEMPTS> is set to
1, a single failed login attempt triggers immediate user lockout.

Specifies the amount of time a user is locked out. Range: 1 to
3600 seconds.

Enabling local login attempt failure limiting with a 20 second lockout being triggered upon the fourth
consecutive login attempt failure.

switch(config)# aaa authentication limit-login-attempts 4 lockout-time 20

Disabling login attempt failure limiting:

switch(config)# no aaa authentication limit-login-attempts

Command History

Release

10.07 or earlier

Command Information

Modification

--

Local AAA commands | 59

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution
rights for this command.

aaa authentication login
aaa authentication login <CONNECTION-TYPE> {local | group <GROUP-LIST>}
no aaa authentication login <CONNECTION-TYPE> {local | group <GROUP-LIST>}

Description

Defines authentication as being local (with the name local) (the default). Or defines a sequence of
remote AAA server groups to be accessed for authentication purposes. Each available connection type
(channel) can be configured individually as either local or using remote AAA server groups. All server
groups named in your command, must exist. This command can be issued multiple times, once for each
connection type. Local is always available for any connection type not configured for remote AAA
authentication.

The no form of this command removes for the specified connection type, any defined remote AAA
server group authentication sequence. Local authentication is available for connection types without a
configured remote AAA server group list (whether default or for the specific connection type).

Parameter

Description

<CONNECTION-TYPE>

local

group <GROUP-LIST>

One of these connection types (channels):
default

Defines a list of accounting server groups to be used for the
default connection type. This configuration applies to all
other connection types (console, https-server, ssh) that
are not explicitly configured with this command. For example,
if you do not use aaa accounting all-mgmt console...
to define the console accounting list, then this default
configuration is used for console.

console

Defines a list of accounting server groups to be used for the
console connection type.

https-server

Defines a list of accounting server groups to be used for the
https-server (REST, Web UI) connection type.

ssh

Defines a list of accounting server groups to be used for the
ssh connection type.

Selects local-only accounting when used without the group
parameter.

Specifies the list of remote AAA server group names. Each name
can be specified one time. Predefined remote AAA group names
tacacs and radius are available. Although not a group name,
predefined name local is available. User-defined TACACS+ and
RADIUS server group names may also be used.
The remote AAA server groups are accessed in the order that the
group names are listed in this command. Within each group, the
servers are accessed in the order in which the servers were added

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

60

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
tothegroup.Servergroupsaredefinedusingcommandaaa
group serverandserversareaddedtoaservergroupwiththe
commandserver.IfnoAAAserverisreachable,local
authenticationisattempted.
Examples
Settinglocalauthenticationforthedefaultconnectiontype:
| switch(config)# |     | aaa authentication | login | default | local |
| --------------- | --- | ------------------ | ----- | ------- | ----- |
Settinglocalauthenticationfortheconsoleconnectiontype:
| switch(config)#     |         | aaa authentication | login        | console | local |
| ------------------- | ------- | ------------------ | ------------ | ------- | ----- |
| Command History     |         |                    |              |         |       |
| Release             |         |                    | Modification |         |       |
| 10.07orearlier      |         |                    | --           |         |       |
| Command Information |         |                    |              |         |       |
| Platforms           | Command | context            | Authority    |         |       |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| aaa authentication    |     | minimum-password-length |     |          |     |
| --------------------- | --- | ----------------------- | --- | -------- | --- |
| aaa authentication    |     | minimum-password-length |     | <LENGTH> |     |
| no aaa authentication |     | minimum-password-length |     | <LENGTH> |     |
Description
Enablesminimumpasswordlengthchecking.Existingpasswordsshorterthantheminimumlengthare
unaffected.Lengthcheckingdoesnotapplytociphertextpasswords.Lengthcheckingappliesbothto
localandremoteauthentication.
Thenoformofthiscommanddisablesminimumpasswordlengthchecking.
| Parameter |     |     | Description                                    |     |     |
| --------- | --- | --- | ---------------------------------------------- | --- | --- |
| <LENGTH>  |     |     | Specifiestheminimumpasswordlength.Range:1to32. |     |     |
Examples
Enablingpasswordlengthchecking,withaminimumlengthof12.
LocalAAAcommands|61

| switch(config)# |     | aaa authentication |     | minimum-password-length |     | 12  |     |
| --------------- | --- | ------------------ | --- | ----------------------- | --- | --- | --- |
Disablingminimumpasswordlengthchecking:
| switch(config)#     |         | no aaa | authentication |              | minimum-password-length |     |     |
| ------------------- | ------- | ------ | -------------- | ------------ | ----------------------- | --- | --- |
| Command History     |         |        |                |              |                         |     |     |
| Release             |         |        |                | Modification |                         |     |     |
| 10.07orearlier      |         |        |                | --           |                         |     |     |
| Command Information |         |        |                |              |                         |     |     |
| Platforms           | Command |        | context        | Authority    |                         |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| aaa authorization    |     |          | commands          |     | (local)        |     |     |
| -------------------- | --- | -------- | ----------------- | --- | -------------- | --- | --- |
| aaa authorization    |     | commands | <CONNECTION-TYPE> |     | {local | none} |     |     |
| no aaa authorization |     | commands | <CONNECTION-TYPE> |     | {local | none} |     |     |
aaa authorization commands <CONNECTION-TYPE> group <GROUP-LIST>
no aaa authorization commands <CONNECTION-TYPE> group <GROUP-LIST>
Description
DefinesauthorizationasbeingbasiclocalRBAC(specifiedasnone),orasfull-fledgedlocalRBAC
specifiedaslocal(thedefault),orasremoteTACACS+(specifiedwithgroup <GROUP-LIST>).Each
availableconnectiontype(channel)canbeconfiguredindividually.Allservergroupsnamedinthe
command,mustexist.Thiscommandcanbeissuedmultipletimes,onceforeachconnectiontype.
Thenoformofthiscommandunconfiguresauthorizationforthespecifiedconnectiontype,revertingto
thedefaultoflocal.
AlthoughonlyTACACS+serversaresupportedforremoteauthorization,localauthorization(basicorfull-fledged)
canbeusedwithremoteRADIUSauthentication.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<CONNECTION-TYPE>
Oneoftheseconnectiontypes(channels):
default
Selectsthedefaultconnectiontypeforconfiguration.This
configurationappliestoallotherconnectiontypes(console,
ssh)thatarenotexplicitlyconfiguredwiththiscommand.For
|     |     |     |     | example,ifyoudonotuseaaa |     | authorization | commands |
| --- | --- | --- | --- | ------------------------ | --- | ------------- | -------- |
console...todefinetheconsoleauthorizationlist,thenthis
defaultconfigurationisusedforconsole.
console
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 62

Parameter

Description

local

none

group <GROUP-LIST>

Selects the console connection type for configuration.

ssh

Selects the ssh connection type for configuration.

When used alone without group <GROUP-LIST>, selects local
authorization which can be used to provide authorization for a
purely local setup without any remote AAA servers and also for
when RADIUS is used for remote Authentication and Accounting
but Authorization is local. When used after group, provides for
fallback (to full-fledged local authorization) when every server in
every specified TACACS+ server group cannot be reached.

NOTE: If any TACACS+ server in the specified groups is reachable,
but the command fails to be authorized by that server, the
command is rejected and local authorization is never attempted.
Local authorization is only attempted if every TACACS+ server
cannot be reached.

When used alone without group <GROUP-LIST>, selects basic
local RBAC authorization, for use with the built-in user groups
(administrators, operators, auditors). When used after
group, provides for fallback (to basic local RBAC authorization)
when every server in every specified TACACS+ server group
cannot be reached.

NOTE: With none, for users belonging to user-defined user
groups, all commands can be executed regardless of what
authorization rules are defined in such groups. For per-command
local authorization, use local instead.

Specifies the list of remote AAA server group names. Predefined
remote AAA group name tacacs is available. User-defined
TACACS+ server group names may also be used. The remote AAA
server groups are accessed in the order that the group names are
listed in this command. Within each group, the servers are
accessed in the order in which the servers were added to the
group. Server groups are defined using command aaa server
group and servers are added to a server group using command
server.
It is recommended to always include either the special name
local or none as the last name in the group list. If both local
and none are omitted, and no remote AAA server is reachable (or
the first reachable server cannot authorize the command),
command execution for the current user will not be possible.

Examples

Setting the authorization for default to local:

switch(config)# aaa authorization commands default local

Setting the authorization for the SSH interface to none:

switch(config)# aaa authorization commands ssh none

Local AAA commands | 63

| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show aaa            | accounting |     |     |     |     |
| ------------------- | ---------- | --- | --- | --- | --- |
| show aaa accounting | [vsx-peer] |     |     |     |     |
Description
Showstheaccountingconfigurationperconnectiontype(channel).
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Configuringandthenshowinglocalaccountingforthedefaultandconsoleconnectiontypes:
| switch(config)# | aaa                 | accounting | all default | start-stop | local |
| --------------- | ------------------- | ---------- | ----------- | ---------- | ----- |
| switch(config)# | aaa                 | accounting | all console | start-stop | local |
| switch(config)# | exit                |            |             |            |       |
| switch#         | show aaa accounting |            |             |            |       |
AAA Accounting:
| Accounting | Type        |          |     | : all        |     |
| ---------- | ----------- | -------- | --- | ------------ | --- |
| Accounting | Mode        |          |     | : start-stop |     |
| Accounting | for default | channel: |     |              |     |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP | PRIORITY |     |
| ---------- | --- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| local |     |     | | 0 |     |     |
| ----- | --- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Accounting | for console | channel: |     |     |     |
| ---------- | ----------- | -------- | --- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP | PRIORITY |     |
| ---------- | --- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| local |     |     | | 0 |     |     |
| ----- | --- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Command | History |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 64

| Release             |         |         |     | Modification |     |     |
| ------------------- | ------- | ------- | --- | ------------ | --- | --- |
| 10.07orearlier      |         |         |     | --           |     |     |
| Command Information |         |         |     |              |     |     |
| Platforms           | Command | context |     | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show aaa                | authentication |            |     |     |     |     |
| ----------------------- | -------------- | ---------- | --- | --- | --- | --- |
| show aaa authentication |                | [vsx-peer] |     |     |     |     |
Description
Showstheauthenticationconfigurationperconnectiontype(channel).
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Configuringandthenshowinglocalauthenticationforthedefaultandconsoleconnectiontypes
(channels):
| switch(config)# |     | aaa authentication |     | login | default | local |
| --------------- | --- | ------------------ | --- | ----- | ------- | ----- |
| switch(config)# |     | aaa authentication |     | login | console | local |
| switch(config)# |     | exit               |     |       |         |       |
| switch# show    | aaa | authentication     |     |       |         |       |
AAA Authentication:
| Fail-through   |          |         |          |     | : Disabled |     |
| -------------- | -------- | ------- | -------- | --- | ---------- | --- |
| Limit Login    | Attempts |         |          |     | : Not      | set |
| Lockout        | Time     |         |          |     | : 300      |     |
| Minimum        | Password | Length  |          |     | : Not      | set |
| Authentication | for      | default | channel: |     |            |     |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP | PRIORITY |     |
| ---------- | --- | --- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| local |     |     |     | | 0 |     |     |
| ----- | --- | --- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authentication | for | console | channel: |     |     |     |
| -------------- | --- | ------- | -------- | --- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP | PRIORITY |     |
| ---------- | --- | --- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| local |     |     |     | | 0 |     |     |
| ----- | --- | --- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
LocalAAAcommands|65

| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show aaa               | authorization |            |     |     |
| ---------------------- | ------------- | ---------- | --- | --- |
| show aaa authorization |               | [vsx-peer] |     |     |
Description
Showstheauthorizationconfigurationperconnectiontype(channel).
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Configuringandthenshowingfull-fledgedlocalRBACauthorizationforthedefaultandconsole
connectiontypes(channels):
| switch(config)# | aaa | authorization | commands default | none |
| --------------- | --- | ------------- | ---------------- | ---- |
switch(config)#
| switch(config)# | aaa  | authorization | commands console | none |
| --------------- | ---- | ------------- | ---------------- | ---- |
| switch(config)# | exit |               |                  |      |
switch#
| switch# show  | aaa authorization |          |     |     |
| ------------- | ----------------- | -------- | --- | --- |
| Authorization | for default       | channel: |     |     |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |     |
| ---------- | --- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
| none |     |     | | 0 |     |
| ---- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authorization | for console | channel: |     |     |
| ------------- | ----------- | -------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |     |
| ---------- | --- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
| none |     |     | | 0 |     |
| ---- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Command History |     |     |     |     |
| --------------- | --- | --- | --- | --- |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 66

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
LocalAAAcommands|67

| show     | ssh                   | authentication-method |     |     |     |
| -------- | --------------------- | --------------------- | --- | --- | --- |
| show ssh | authentication-method |                       |     |     |     |
Description
ShowsthestatusoftheSSHpublickeymethodandthelocalpassword-based(throughSSHclient)
authenticationmethod.
Example
Showingtheauthenticationmethods.
| switch#        | show        | ssh            | authentication-method |           |              |
| -------------- | ----------- | -------------- | --------------------- | --------- | ------------ |
| SSH            | publickey   |                | authentication        | :         | Enabled      |
| SSH            | password    | authentication |                       | : Enabled |              |
| Command        | History     |                |                       |           |              |
| Release        |             |                |                       |           | Modification |
| 10.07orearlier |             |                |                       |           | --           |
| Command        | Information |                |                       |           |              |
| Platforms      |             | Command        | context               |           | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show      | user       |     |                |     |     |
| --------- | ---------- | --- | -------------- | --- | --- |
| show user | <USERNAME> |     | authorized-key |     |     |
Description
ShowstheSSHclientpublickeylistforaspecifieduser.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<USERNAME> SpecifiestheusernameforwhichyouwanttoshowtheSSHclient
publickeylist.
Usage
Anyusercanshowtheirownpublickeylist;however,administratorscanalsoshowapublickeylistof
otherusers.
Examples
Showingaclientpublickey:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 68

| switch# show | user admin | authorized-key |        |
| ------------ | ---------- | -------------- | ------ |
| 1. Key Type  | : RSA      | Key size       | : 2048 |
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMtyMBmmAaF6r1zxf3DZNHSYVHBJhlbBlyAIqQ8DSHK
...
U+aE14UW/ifIukmK67sIHwK+FhhRYwPztQc5pjyOPk128a4pgKQaHCcOF169Z admin@switch
Showingtwoclientpublickeys:
| switch# show | user admin | authorized-key |            |
| ------------ | ---------- | -------------- | ---------- |
| 1. Key Type  | : ECDSA    | Curve          | : nistp256 |
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEqEFevZ0
...
l76V+D0svdCJ9Wo32zqI9OeAdTJw/eZYp5qknhNgS81HjAI6J/4/kAqdZAjbqQUiCAk= admin@switch
| 2. Key Type | : RSA | Key size | : 2048 |
| ----------- | ----- | -------- | ------ |
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDXQHrqV7+/GcMdOhr//IRjJkX7TQKupW89j80bL7xq8
...
j8qKuHWSN0/h/HxjzQJuYDVmZN5vG3DhpXbBZUlZNnchVod13QLCesqA3VLKN admin@switch
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
ssh password-authentication
ssh password-authentication
no ssh password-authentication
Description
Enablesthepassword-basedauthenticationmethodforusewithSSHclients.
Thenoformofthiscommanddisablesthepassword-basedauthenticationmethodforusewithSSH
clients.
Usage
Theswitchshipswithpassword-basedauthentication(forSSHclients)enabled.Themaximumnumber
ofpasswordretriesisthree.
Examples
EnablingpasswordauthenticationforusewithSSHclients:
LocalAAAcommands|69

| switch(config)# | ssh | password-authentication |     |
| --------------- | --- | ----------------------- | --- |
DisablingpasswordauthenticationforusewithSSHclients:
| switch(config)#     | no      | ssh password-authentication |              |
| ------------------- | ------- | --------------------------- | ------------ |
| Command History     |         |                             |              |
| Release             |         |                             | Modification |
| 10.07orearlier      |         |                             | --           |
| Command Information |         |                             |              |
| Platforms           | Command | context                     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ssh public-key-authentication
ssh public-key-authentication
no ssh public-key-authentication
Description
EnablestheSSHpublickeyauthenticationmethod.TheswitchshipswithSSHpublickeyauthentication
enabled.
ThenoformofthiscommanddisablestheSSHpublickeyauthenticationmethod.
AlthoughSSHpublickeyauthenticationisenabledbydefault,itcannotbeuseduntilSSHpublickeysareadded
| withtheuser | authorized-keycommand. |     |     |
| ----------- | ---------------------- | --- | --- |
Examples
EnablingSSHpublickeyauthentication:
| switch(config)# | ssh | public-key-authentication |     |
| --------------- | --- | ------------------------- | --- |
DisablingSSHpublickeyauthentication:
| switch(config)# | no  | ssh public-key-authentication |              |
| --------------- | --- | ----------------------------- | ------------ |
| Command History |     |                               |              |
| Release         |     |                               | Modification |
| 10.07orearlier  |     |                               | --           |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 70

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution
rights for this command.

user authorized-key
user <USERNAME> authorized-key <PUBKEY>
no user <USERNAME> authorized-key [<KEYNUM>]

Description

Copies an SSH client public key into the key list. If the key list and the public key do not exist, it creates a
list with the public key. If the SSH client public key exists, the command appends the new key to the
existing list. The client public key list holds a maximum of 32 client keys.

The no form of the command removes either one or all SSH public keys from the key list.

Parameter

<USERNAME>

<PUBKEY>

<KEYNUM>

Usage

Description

Specifies the name of the user.

Specifies the SSH client public key to be copied into the key list.

Specifies the key number. The range is 1 to 32. Use the show
user <USERNAME> authorized-key command to find the key
number associated with the key.

Each key on the key list has a key identifier. The show user <USERNAME> authorized-key command
displays the key identifier associated with the key.

Administrators can add and remove the public keys of themselves and other users. Operators can add
and remove only their own public keys. If the public key authentication method is enabled, the client
public key present is used by the SSH server to authenticate the client. The authentication method
reverts to the password authentication method and prompts for a client password when one of the
following occurs:

n The client public keys are not present.

n The server does not have the keys enabled.

n The public key method is disabled.

You can either remove all keys or a specific key. Each key on the key list has a key identifier. If you
provide the key identifier in this command, the command removes the corresponding key from the list.
If you provide no key identifier, the command removes all keys from the key list.

Examples

Adding a public key:

Local AAA commands | 71

switch(config)#user admin authorized-key ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTIt
bmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEqEFevZ0l76V+D0svdCJ9Wo32zqI9OeAIdTJwT/eZYp50qkA
| nhZNgS81HBjAI6QJ/4/kAyqdZ9oAjbiqQUiCAk= |     |     | root@switch |     |
| --------------------------------------- | --- | --- | ----------- | --- |
RemovingallSSHpublickeysfromthelist:
| switch(config)# | no  | user admin authorized-key |     |     |
| --------------- | --- | ------------------------- | --- | --- |
RemovingthespecifiedSSHpublickeyfromthelist:
| switch(config)#     | no      | user admin authorized-key |              | 2   |
| ------------------- | ------- | ------------------------- | ------------ | --- |
| Command History     |         |                           |              |     |
| Release             |         |                           | Modification |     |
| 10.07orearlier      |         |                           | --           |     |
| Command Information |         |                           |              |     |
| Platforms           | Command | context                   | Authority    |     |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 72

Chapter 8
|        |          |         |     | Remote | AAA with | TACACS+ |
| ------ | -------- | ------- | --- | ------ | -------- | ------- |
| Remote | AAA with | TACACS+ |     |        |          |         |
RemoteAAAprovidesthefollowingforyourArubaswitch:
n AuthenticationusingremoteTACACS+AAAservers.
n AuthorizationusingremoteTACACS+AAAservers,providingfine-grainedcommandauthorization.
Optionaluser-definedlocalusergroupswithconfiguredcommandauthorizationrulescanbeusedto
provideauthorizationfallbackprotectionforwhenTACACS+serversbecometemporarilyunavailable.
n TransmissionoflocallycollectedaccountinginformationtoremoteTACACS+servers.
ForswitchesthatsupportmultiplemanagementmodulessuchastheAruba8400,allAAAfunctionalitydiscussed
onlyappliestotheactivemanagementmodule.SeealsoAAAonswitcheswithmultiplemanagementmodulesinthe
HighAvailabilityGuide.
| Default | server | groups |     |     |     |     |
| ------- | ------ | ------ | --- | --- | --- | --- |
Theswitchalwayshasthesefourdefaultgroups:
n tacacs:forremoteAAA,alwayscontainseveryconfiguredTACACS+server.
n radius:forremoteAAA,alwayscontainseveryconfiguredRADIUSserver.
n local:forlocalauthentication.
n none:forlocal(RBAC)authorization.
User-definedAAAserversarealwaysaddedtothematchingdefaultgroup,eithertacacsorradius.
Optionally,eachservercanalsobeaddedtoexactlyoneadditionaluser-defined(custom)group.A
maximumof28user-definedgroupscanbecreated.
Theorderinwhichserversareaddedtoagroupisimportant.Theserveraddedfirstisaccessedfirst,
andifnecessary,thesecondserverisaccessedsecond,andsoon.
| Remote                                           | AAA | (TACACS+) | defaults | and limits |          |               |
| ------------------------------------------------ | --- | --------- | -------- | ---------- | -------- | ------------- |
| Setting                                          |     |           |          |            | Default  | value / limit |
| AuthenticationofRESTsessionswithTACACS+          |     |           |          |            | Disabled |               |
| MaximumnumberofTACACS+serversinanAAAgroup        |     |           |          |            | 16       |               |
| MaximumnumberofTACACS+serversthatcanbeconfigured |     |           |          |            | 16       |               |
Maximumnumberofuser-definedAAAservergroupsthatcanbeconfigured 28
| TACACS+authentication |     |     |     |     | Disabled |     |
| --------------------- | --- | --- | --- | --- | -------- | --- |
73
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries)

| Setting                                    |     |     |     |     | Default    | value / limit |
| ------------------------------------------ | --- | --- | --- | --- | ---------- | ------------- |
| TACACS+authenticationglobaltimeout         |     |     |     |     | 5seconds   |               |
| TACACS+authenticationpasskey(sharedsecret) |     |     |     |     | None       |               |
| TACACS+authenticationtcp-port              |     |     |     |     | 49         |               |
| TACACS+globalauthenticationprotocol        |     |     |     |     | PAP        |               |
| TACACS+servertrackingdefaultinterval       |     |     |     |     | 300seconds |               |
| TACACS+serveraccessthroughthedefaultVRF    |     |     |     |     | default*   |               |
*Thedefaultvalueisdefault,unlessanotherVRFisspecifiedduringtheserverconfiguration.
| About | global | versus | per-TACACS+ | server | passkeys | (shared |
| ----- | ------ | ------ | ----------- | ------ | -------- | ------- |
secrets)
TocommunicatewithaTACACS+AAAserver,theswitchmusthaveapasskey(sharedsecret)configured
thatmatcheswhatisconfiguredontheserver.Useoneofthesecommandstoachievethedesired
configuration:
n ForaglobalpasskeycommontoeveryTACACS+server,usetacacs-server key.
n Foraper-TACACS+serverpasskey,usetacacs-server hostwiththekeyparameter.
Ifbothpasskeysareconfiguredontheswitch,theper-TACACS+serverpasskeyisused.
| Remote | AAA | TACACS+ | server | configuration | requirements |     |
| ------ | --- | ------- | ------ | ------------- | ------------ | --- |
Theuser-suppliedTACACS+servermust:
n HaveanIPv4/IPv6addressorfullyqualifieddomainname(FQDN)thatisvisibletotheswitch.
n Haveapasskey(sharedsecret)thatmatcheswhatisconfiguredontheswitch.
n Provideusernameandpassworddefinitionsforeveryswitchuser.Remoteusersdonotrequire
definitionontheswitch.
n ConfigureuserroleassignmentusingTACACS+attributes.
n Haveanyneededcommandauthorizationconfiguredtocontrolwhatcommands(peruseroruser
role)willbeexecutableontheswitch.
ConsultyourTACACS+serverdocumentationforinstallationandgeneralconfigurationdetails.
IfSSHpublickeyauthenticationisused,thekeyinformationisstoredlocallyontheswitch,makingusernameand
passworddefinitionontheTACACS+serverunnecessary.
| User | role assignment |     | using TACACS+ | attributes |     |     |
| ---- | --------------- | --- | ------------- | ---------- | --- | --- |
RemoteAAAwithTACACS+|74

UserroleassignmentisconfiguredontheTACACS+serverusingVSAs(vendor-specificattributes)and
TACACS+specifiedattributes.
TACACS+serverscanreturnmultipleattributevaluepairs(AVPs)inresponsetoanauthentication
request.Theattributesareprocessedinthisorderofprecedencetodeterminetheuserroleassigned:
n IftheAruba-Admin-RoleVSAispresent,maptheusertothematchingcorrespondinglocaluser-
groupname.
o Elseifthepriv-lvlTACACS+specifiedattributeispresent,extracttheprivilegelevel(1,15,or19)
andmaptheusertothelocaluser-groupcorrespondingtothisprivilegelevel(1=operators,
15=administrators,19=auditors).Privilegelevels2to14mayalsobeusedwithmatchinglocal
usergroupsnamed2to14.
Otherwise,theuserrolecannotbedetermined,andauthenticationfails.
l
| This information | is summarized     | as         | follows:   |                                   |
| ---------------- | ----------------- | ---------- | ---------- | --------------------------------- |
| Aruba-Admin-Role |                   | priv-lvl   |            | User role assigned                |
| <GROUP-NAME>     |                   | Donotcare  |            | Matchinglocaluser<GROUP-NAME>     |
| Notpresent       |                   | 1          |            | Operators                         |
| Notpresent       |                   | 15         |            | Administrators                    |
| Notpresent       |                   | 19         |            | Auditors                          |
| Notpresent       |                   | 2to14      |            | Matchinglocalusergroupsnamed2to14 |
| Notpresent       |                   | Notpresent |            | None(notauthenticated)            |
| TACACS+          | server redundancy |            | and access | sequence                          |
Topreventauthenticationandauthorizationinterruption,itiscommonpracticetoconfiguremorethan
oneTACACS+server.WhenidentifyingTACACS+serverstotheswitch,servergrouporder(andserver
orderwithinthegroup),determinesserveraccessorder.
Whendefiningtheserveraccesssequenceforauthenticationwithaaa authentication login default,
thereisanimpliedlocalincludedasthelastiteminthelist.IfnoTACACS+servercanbereached,local
authenticationwillbeattempted.
Whendefiningtheserveraccesssequenceforauthorizationwithaaa authorization commands,itis
recommendedtoalwaysincludeeitherlocalornoneasthelastiteminthelist.
Single source IP address for consistent source identification
| to AAA | servers |     |     |     |
| ------ | ------- | --- | --- | --- |
Ifapplicabletoyourinstallation,itisrecommendedthatyouperformtheoptionalconfigurationmentionedin
thissection.
IfyourtopologyallowstheAAAservertobereachedthroughmultiplepaths,theserverinterpretsthe
incomingpacketstobefromdifferentswitcheseventhoughtheyareallcomingfromthesameswitch.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 75

HavingaswitchassociatedwithmultipleIPaddressesmakesitmoredifficulttointerpretsystemlogs
andaccountingdata.
ToensurethatalltrafficsentfromtheswitchtotheAAAserverusesthesamesourceIPaddress,useip
source-interfaceoripv6 source-interface.Thesetwocommandsplustherelatedcommandsshow
ip source-interfaceandshow ipv6 source-interfacearedescribedunderLayer2/3Interface
commandsintheCommand-LineInterfaceGuide.
| TACACS+ | general | tasks |     |     |     |     |     |
| ------- | ------- | ----- | --- | --- | --- | --- | --- |
GeneralTACACS+tasks,notspecifictoauthentication,authorization,oraccounting,areasfollows:
| Task |     | Command | name | Example |     |     |     |
| ---- | --- | ------- | ---- | ------- | --- | --- | --- |
ConfiguringaTACACS+ tacacs-server tacacs-server host 1.1.1.1 vrf default
| server           |     | host         |     | no tacacs-server   |     | host   | 1.1.1.1 vrf default |
| ---------------- | --- | ------------ | --- | ------------------ | --- | ------ | ------------------- |
| Showingglobaland |     | show tacacs- |     | show tacacs-server |     | detail |                     |
| TACACS+server    |     | server       |     |                    |     |        |                     |
configurations
|                     |     |           |         | aaa group | server        | tacacs | sg1 |
| ------------------- | --- | --------- | ------- | --------- | ------------- | ------ | --- |
| ConfiguringaTACACS+ |     | aaa group | server  |           |               |        |     |
| servergroup         |     |           |         | no aaa    | group server  | tacacs | sg1 |
| Showingservergroups |     | show aaa  | server- | show aaa  | server-groups |        |     |
groups
| AddingaTACACSserver |     | server |     | aaa group | server  | tacacs  | sg1         |
| ------------------- | --- | ------ | --- | --------- | ------- | ------- | ----------- |
|                     |     |        |     | server    | 1.1.1.2 | port 32 | vrf default |
toaserver-group
| DeletingaTACACS    |     | server |     | aaa group | server  | tacacs | sg1            |
| ------------------ | --- | ------ | --- | --------- | ------- | ------ | -------------- |
| serverfromaserver- |     |        |     | no server | 1.1.1.2 | port   | 32 vrf default |
group
ConfiguringaTACACS+ tacacs-server key tacacs-server key plaintext mypasskey123
globalpasskey
| ConfiguringPAPor |     | tacacs-server |     | tacacs-server    |     | auth-type | chap |
| ---------------- | --- | ------------- | --- | ---------------- | --- | --------- | ---- |
| CHAPforTACACS+   |     |               |     | no tacacs-server |     | auth-type |      |
auth-type
|                      |                |               |     | tacacs-server    |     | timeout | 20  |
| -------------------- | -------------- | ------------- | --- | ---------------- | --- | ------- | --- |
| Configuringthe       |                | tacacs-server |     |                  |     |         |     |
|                      |                |               |     | no tacacs-server |     | timeout |     |
| TACACS+globaltimeout |                | timeout       |     |                  |     |         |     |
| TACACS+              | authentication |               |     |                  |     |         |     |
TACACS+authenticationoccursasfollows:
n UsercredentialsaresentfromtheswitchtoTACACS+serverusingthePAPorCHAPauthentication
protocol.
n Ifauserisauthenticated,theirroleiscommunicatedtotheswitchasAdministrator,Operator,or
Auditor.
n Anunknownuserorauserwhoenteredaninvalidpasswordisidentifiedassuchtotheswitch,
whichthenrejectsuserlogin.
| About authentication |     |     | fail-through |     |     |     |     |
| -------------------- | --- | --- | ------------ | --- | --- | --- | --- |
RemoteAAAwithTACACS+|76

Normally,authenticationisperformedbythefirstAAAserverreached.Ararelyneededfeaturenamed
"Authenticationfail-through"isavailable.IfAuthenticationfail-throughisenabledandauthentication
failsonthefirstreachableAAAserver,authenticationisattemptedonthesecondAAAserver,andsoon,
untilsuccessfulauthenticationortheserverlistisexhausted.
EnablingAuthenticationfail-throughistypicallyunnecessarybecausetheusercredentialdatabases
shouldbeconsistentacrossallAAAservers.Authenticationfail-throughmightbehelpfulifyourAAA
usercredentialdatabasesarenotquicklysynchronizedacrossallAAAservers.
| TACACS+ | authentication | tasks |     |
| ------- | -------------- | ----- | --- |
TheTACACS+authentication-relatedtasksareasfollows:
Command
| Task |     | Example |     |
| ---- | --- | ------- | --- |
name
Configuringthe aaa aaa authentication login default group tg1 tg2 tacacs
| authentication | authentication | local |     |
| -------------- | -------------- | ----- | --- |
sequencefor
login
thedefault
connection
type
Configuringthe aaa aaa authentication login console group tg2 tg3 tacacs
| authentication | authentication | local |     |
| -------------- | -------------- | ----- | --- |
sequencefor
login
theconsole
connection
type
Configuringthe aaa aaa authentication login ssh group tg2 tacacs local
| authentication | authentication |     |     |
| -------------- | -------------- | --- | --- |
sequencefor
login
thessh
connection
type
| Removing     | aaa            | no aaa authentication | login default |
| ------------ | -------------- | --------------------- | ------------- |
| remoteAAAfor | authentication |                       |               |
thedefault
login
connection
type
| Configuring | aaa | aaa authentication | allow-fail-through |
| ----------- | --- | ------------------ | ------------------ |
authentication authentication no aaa authentication allow-fail-through
fail-through
allow-fail-
through
| Showingthe     | show aaa       | show aaa authentication |     |
| -------------- | -------------- | ----------------------- | --- |
| authentication | authentication |                         |     |
sequence
| TACACS+ | authorization |     |     |
| ------- | ------------- | --- | --- |
Uponsuccessfuluserauthentication,theuserisassignedtheirrolebytheTACACS+server.Seealso
UserroleassignmentusingTACACS+attributes.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 77

TACACS+ authorization provides command filtering to allow/disallow individual command or command
set execution. Each command is sent to the TACACS+ server for approval, and the switch then
allows/disallows command execution according to the server response.

TACACS+ authorization applies only to the CLI interface.

Using local authorization as fallback from TACACS+ authorization

Local authorization can be used for the situation in which communication is lost with all TACACS+
servers after a successful authentication. Users that are members of the built-in local user groups
(administrators, operators, or auditors) are authorized according to the fixed roles and privilege
levels of those groups. Optionally, local user-defined user groups can be configured with specific
command execution rules per group. Users that are members of such groups, are authorized according
to the command execution rules of the group to which they belong. For configuring local user groups,
see user-group.

About authentication fail-through and authorization

For authorization, there is no equivalent of the authentication fail-through feature. Therefore, if the first
reachable TACACS+ server responds with "Authorization Denied," no additional TACACS+ servers are
interrogated.

Rare potential out-of-synchronization situation when using authentication fail-through: Successful authentication

on one server can be followed by authorization denial on another. The user is known on the server doing the

authentication but unknown on the server attempting the authorization. This situation typically arises only during

brief periods in which user credential databases are not synchronized across all TACACS+ servers. See also

TACACS+ server authorization considerations in aaa authorization commands (remote) .

TACACS+ authorization tasks

The TACACS+ authorization-related tasks are as follows:

Command
name

aaa
authorization
commands

aaa
authorization
commands

Task

Configuring
the
authorization
sequence for
the default
connection
type

Configuring
the
authorization
sequence for
the console
connection
type

Example

aaa authorization commands default group tg1 tacacs local

aaa authorization commands console group tg1 tg2 tacacs
none

Removing
remote AAA

aaa
authorization

no aaa authorization commands default

Remote AAA with TACACS+ | 78

Command
| Task |     | Example |     |     |
| ---- | --- | ------- | --- | --- |
name
| forthedefault | commands |     |     |     |
| ------------- | -------- | --- | --- | --- |
connection
type
| Showingthe | show aaa | show aaa | authorization |     |
| ---------- | -------- | -------- | ------------- | --- |
TACACS+
authorization
authorization
sequence
| TACACS+ | accounting |     |     |     |
| ------- | ---------- | --- | --- | --- |
Thisaccountinginformationiscapturedandmadeavailableforsendingtoremoteaccountingservers:
n ExecAccounting:userlogin/logoutevents.
n Commandaccounting:commandsexecutedbyusers.
n Systemaccounting:remoteaccountingOn/Offevents.
n CLIshowcommands.
n Interactionsonthenon-CLIinterfaces:RESTandWebUI.
Thefollowingisnotcapturedormadeavailableasaccountinginformation:
n CLIcommandsthatreboottheswitch.
n Interactionsinthebashshell.
Localaccounting(alwaysenabled)mustbefunctioningproperlyforremoteAccountingtowork.
TheaccountinginformationissenttothefirstreachableremoteTACACS+AAAserver(configuredforremote
accounting).IfnoremoteTACACS+serverisreachable,localaccountingremainsavailable.
| Sample | accounting | information | on a TACACS+ | server |
| ------ | ---------- | ----------- | ------------ | ------ |
Mon May 9 17:52:32 10.10.11.1 UNKNOWN tty 0.0.0.0 start task_id=1525899775430
timezone=UTC start_time=1525913552.428 service=system event=sys_acct
| reason="System-accounting-ON" |     | result=success |     |     |
| ----------------------------- | --- | -------------- | --- | --- |
Mon May 9 17:52:48 10.10.11.1 admin tty 192.168.1.20 start task_id=1525899775431
timezone=UTC start_time=1525913567.611 service=shell priv_lvl=15 result=success
Mon May 9 17:52:48 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775432
timezone=UTC stop_time=1525913567.614 service=shell priv_lvl=15 cmd="enable"
result=success
Mon May 9 17:52:51 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775433
timezone=UTC stop_time=1525913570.851 service=shell priv_lvl=15
| cmd="configure" | result=success |     |     |     |
| --------------- | -------------- | --- | --- | --- |
Mon May 9 17:52:53 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775434
timezone=UTC stop_time=1525913573.427 service=shell priv_lvl=15 cmd="interface
| 1/1/3" | result=success |     |     |     |
| ------ | -------------- | --- | --- | --- |
Mon May 9 17:52:54 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775435
timezone=UTC stop_time=1525913574.447 service=shell priv_lvl=15 cmd="no
| shutdown" | result=success |     |     |     |
| --------- | -------------- | --- | --- | --- |
Mon May 9 17:52:58 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775436
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 79

timezone=UTC stop_time=1525913578.131 service=shell priv_lvl=15 cmd="ip
| address | 10.10.13.1/24" | result=success |     |     |     |     |
| ------- | -------------- | -------------- | --- | --- | --- | --- |
Mon May 9 17:52:59 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775437
timezone=UTC stop_time=1525913579.468 service=shell priv_lvl=15 cmd="exit"
result=success
Mon May 9 17:53:10 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775442
timezone=UTC stop_time=1525913590.204 service=shell priv_lvl=15 cmd="exit"
result=success
Mon May 9 17:53:10 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775431
timezone=UTC stop_time=1525913590.205 service=shell priv_lvl=15 result=success
Mon May 9 17:53:44 10.10.11.1 UNKNOWN tty 0.0.0.0 stop task_id=1525899775430
timezone=UTC stop_time=1525913624.473 service=system event=sys_acct
| reason="System-accounting-OFF" |     | result=success |     |     |     |     |
| ------------------------------ | --- | -------------- | --- | --- | --- | --- |
ThissampleisrepresentativeandnotfromanyparticularTACACS+serverimplementation.
| Sample | REST accounting | information |     | on a TACACS+ | server |     |
| ------ | --------------- | ----------- | --- | ------------ | ------ | --- |
Oct 30 16:31:56 10.10.10.1 admin tty 127.0.0.1 start task_id=1540942055868
timezone=UTC start_time=1540942316.36 service=https-server priv_lvl=15
| cmd="http-method=POST |     | http-uri=/rest/v1/login" |     | result=success |     |     |
| --------------------- | --- | ------------------------ | --- | -------------- | --- | --- |
ThissampleisrepresentativeandnotfromanyparticularTACACS+serverimplementation.
| TACACS+ | accounting | tasks |     |     |     |     |
| ------- | ---------- | ----- | --- | --- | --- | --- |
TheTACACS+accounting-relatedtasksareasfollows:
Command
| Task |     | Example |     |     |     |     |
| ---- | --- | ------- | --- | --- | --- | --- |
name
Configuring aaa aaa accounting all-mgmt default start-stop group tg1 tg2
| the |     | tacacs local |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- |
accounting
| accounting | all-mgmt |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- |
sequencefor
thedefault
connection
type
|             |            | aaa accounting | all-mgmt | console start-stop | group tg2 | tg3 |
| ----------- | ---------- | -------------- | -------- | ------------------ | --------- | --- |
| Configuring | aaa        |                |          |                    |           |     |
| the         | accounting | tacacs local   |          |                    |           |     |
| accounting  | all-mgmt   |                |          |                    |           |     |
sequencefor
theconsole
connection
type
Configuring aaa aaa accounting all-mgmt ssh start-stop group tg2 tacacs local
| the | accounting |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- |
accounting
all-mgmt
sequencefor
thessh
RemoteAAAwithTACACS+|80

Command
| Task |     | Example |     |     |     |     |
| ---- | --- | ------- | --- | --- | --- | --- |
name
connection
type
| Removing  | aaa        | no  | aaa accounting | all-mgmt | default | start-stop |
| --------- | ---------- | --- | -------------- | -------- | ------- | ---------- |
| remoteAAA | accounting |     |                |          |         |            |
forthe
all-mgmt
default
connection
type
| Showingthe | show aaa   | show | aaa accounting |     |     |     |
| ---------- | ---------- | ---- | -------------- | --- | --- | --- |
| accounting | accounting |      |                |     |     |     |
configuration
| Example: | Configuring |     | the switch |     | for Remote | AAA with |
| -------- | ----------- | --- | ---------- | --- | ---------- | -------- |
TACACS+
Prerequisites
n TACACS+serversconfiguredingeneralaccordingtotheinformationinRemoteAAATACACS+server
configurationrequirements.Theexactsettingsappropriatetoyourenvironmentwillvary.
n LoggedintotheswitchwithAdministratorprivilegeandintheconfigcontext.
Procedure
1. ConfiguretheglobalTACACS+passkey(sharedsecret)as"xjkW74932qX3j_$"
|     | switch(config)# | tacacs-server | key | plaintext | xjkW74932qX3j_$ |     |
| --- | --------------- | ------------- | --- | --------- | --------------- | --- |
switch(config)#
2. AddtheseconfigurationdetailsfortworemoteTACACS+servers:
n Server1withIPv4address10.0.0.2,onthemanagementinterface(belongingtoVRF“mgmt”),
usingthedefaultPAPprotocol.
n Server2withIPv4address4.0.0.2,onthedatainterface(belongingtoVRF“default”),usingthe
CHAPprotocol.
|     | switch(config)# | tacacs-server | host | 10.0.0.2 | vrf mgmt  |      |
| --- | --------------- | ------------- | ---- | -------- | --------- | ---- |
|     | switch(config)# | tacacs-server | host | 4.0.0.2  | auth-type | chap |
switch(config)#
3. CreateaTACACS+groupnamedtac_grp1,assignTACACS+server10.0.0.2tothegroup,showthe
groupinformation.
ThedefaultTACACS+groupnamedtacacsincludeseveryTACACS+serverregardlessof
whetheranyTACACS+serversarealsoassignedtoauser-definedTACACS+group.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 81

| switch(config)# |     | aaa | group | server | tacacs | tac_grp1 |     |     |
| --------------- | --- | --- | ----- | ------ | ------ | -------- | --- | --- |
switch(config-sg)#
|                    |     |     | server | 10.0.0.2 | vrf | mgmt |     |     |
| ------------------ | --- | --- | ------ | -------- | --- | ---- | --- | --- |
| switch(config-sg)# |     |     | exit   |          |     |      |     |     |
switch(config)#
| switch(config)# |           | do  | show aaa | server-groups |     | tacacs |     |     |
| --------------- | --------- | --- | -------- | ------------- | --- | ------ | --- | --- |
| ******* AAA     | Mechanism |     | TACACS+  | *******       |     |        |     |     |
-------------------------------------------------------------------------
| GROUP NAME |     | |   | SERVER | NAME |     |     | | PORT | VRF | | PRIORITY |
| ---------- | --- | --- | ------ | ---- | --- | --- | ------------ | ---------- |
-------------------------------------------------------------------------
| tac_grp1 |     | |   | 10.0.0.2 |     |     |     | | 49 | mgmt | | 1 |
| -------- | --- | --- | -------- | --- | --- | --- | ----------- | --- |
-------------------------------------------------------------------------
| tacacs (default) |     | |   | 10.0.0.2 |     |     |     | | 49 | mgmt    | | 1 |
| ---------------- | --- | --- | -------- | --- | --- | --- | -------------- | --- |
| tacacs (default) |     | |   | 4.0.0.2  |     |     |     | | 49 | default | | 2 |
-------------------------------------------------------------------------
switch(config)#
4. DefinetheauthenticationsequencelistsothatthenewTACACS+groupisfirst,thedefault
TACACS+groupissecond,andlocalisthird.Showtheauthenticationsequence.
switch(config)#
|     |     | aaa | authentication |     | login | default | group tac_grp1 | tacacs local |
| --- | --- | --- | -------------- | --- | ----- | ------- | -------------- | ------------ |
switch(config)#
| switch(config)# |     | do  | show aaa | authentication |     |     |     |     |
| --------------- | --- | --- | -------- | -------------- | --- | --- | --- | --- |
AAA Authentication:
| Fail-through           |          |          |        |               |     | : Disabled |     |     |
| ---------------------- | -------- | -------- | ------ | ------------- | --- | ---------- | --- | --- |
| Limit Login            |          | Attempts |        |               |     | : Not      | set |     |
| Lockout                | Time     |          |        |               |     | : 300      |     |     |
| Minimum                | Password |          | Length |               |     | : Not      | set |     |
| Default Authentication |          |          | for    | All Channels: |     |            |     |     |
----------------------------------------------------------------------------
-----
| GROUP NAME |     |     |     |     | | GROUP | PRIORITY |     |     |
| ---------- | --- | --- | --- | --- | ------- | -------- | --- | --- |
----------------------------------------------------------------------------
-----
| tac_grp1 |     |     |     |     | | 0 |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| tacacs   |     |     |     |     | | 1 |     |     |     |
| local    |     |     |     |     | | 2 |     |     |     |
----------------------------------------------------------------------------
-----
switch(config)#
5. DefinetheauthorizationsequencelistwithtwoTACACS+servergroupspluslocalRBAC.Showthe
authorizationsequence.
switch(config)# aaa authorization commands default group tac_grp1 tacacs
local
switch(config)#
| switch(config)# |     | do            | show aaa | authorization |     |           |     |     |
| --------------- | --- | ------------- | -------- | ------------- | --- | --------- | --- | --- |
| Default command |     | Authorization |          | for           | All | Channels: |     |     |
----------------------------------------------------------------------------
-----
| GROUP NAME |     |     |     |     | | GROUP | PRIORITY |     |     |
| ---------- | --- | --- | --- | --- | ------- | -------- | --- | --- |
----------------------------------------------------------------------------
-----
RemoteAAAwithTACACS+|82

| tac_grp1 |     | | 0 |     |     |     |
| -------- | --- | --- | --- | --- | --- |
| tacacs   |     | | 1 |     |     |     |
| local    |     | | 2 |     |     |     |
----------------------------------------------------------------------------
-----
switch(config)#
6. DefinetheaccountingsequencelistwithtwoTACACS+servergroups.Showtheaccounting
sequence.
switch(config)#
|     | aaa accounting | all default | start-stop | group tac_grp1 | tacacs |
| --- | -------------- | ----------- | ---------- | -------------- | ------ |
switch(config)#
| switch(config)# | do show aaa | accounting |     |     |     |
| --------------- | ----------- | ---------- | --- | --- | --- |
AAA Accounting:
| Accounting         | Type    |           | : all        |     |     |
| ------------------ | ------- | --------- | ------------ | --- | --- |
| Accounting         | Mode    |           | : start-stop |     |     |
| Default Accounting | for All | Channels: |              |     |     |
----------------------------------------------------------------------------
-----
| GROUP NAME |     | | GROUP | PRIORITY |     |     |
| ---------- | --- | ------- | -------- | --- | --- |
----------------------------------------------------------------------------
-----
| tac_grp1 |     | | 0 |     |     |     |
| -------- | --- | --- | --- | --- | --- |
| tacas    |     | | 1 |     |     |     |
----------------------------------------------------------------------------
-----
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 83

Chapter 9

Remote AAA with RADIUS

Remote AAA with RADIUS

Remote AAA provides the following for your Aruba switch:

n Authentication using remote RADIUS AAA servers. For added security, two-factor authentication may

be used. In two-factor authentication, X.509 certificate-based authentication is combined with RADIUS
authentication.

n Command authorization is not supported by RADIUS servers, however, user-defined local user
groups can be configured with command-authorization rules, providing locally configured per-
command authorization for members of such groups. See User-defined user groups .

In the switch default state (without user-defined local groups), basic role-based authorization is
available with the three built-in roles (administrators, operators, auditors).

n Transmission of locally collected accounting information to remote RADIUS servers.

For switches that support multiple management modules, all AAA functionality discussed only applies to the

active management module. See also AAA on switches with multiple management modules in the High Availability

Guide.

AOS-CX supports IPv4/IPv6 Radius over the VXLAN overlay network​ without additional configuration
from the user.

Default server groups

The switch always has these four default groups:

n tacacs: for remote AAA, always contains every configured TACACS+ server.

n radius: for remote AAA, always contains every configured RADIUS server.

n local: for local authentication.

n none: for local (RBAC) authorization.

User-defined AAA servers are always added to the matching default group, either tacacs or radius.
Optionally, each server can also be added to exactly one additional user-defined (custom) group. A
maximum of 28 user-defined groups can be created.

The order in which servers are added to a group is important. The server added first is accessed first,
and if necessary, the second server is accessed second, and so on.

Remote AAA (RADIUS) defaults and limits

Setting

Default value / limit

Maximum number of RADIUS servers in
an AAA group

16

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

84

| Setting                      |     |     | Default | value / limit |     |     |
| ---------------------------- | --- | --- | ------- | ------------- | --- | --- |
| MaximumnumberofRADIUSservers |     |     | 16      |               |     |     |
thatcanbeconfigured
| Maximumnumberofuser-definedAAA |     |     | 28  |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- |
servergroupsthatcanbeconfigured
| RADIUSauthentication               |     |     | Disabled |     |     |     |
| ---------------------------------- | --- | --- | -------- | --- | --- | --- |
| RADIUSauthenticationglobaltimeout  |     |     | 5seconds |     |     |     |
| RADIUSauthenticationpasskey(shared |     |     | None     |     |     |     |
secret)
| RADIUSauthenticationudp-port        |     |     | 1812       |     |     |     |
| ----------------------------------- | --- | --- | ---------- | --- | --- | --- |
| RADIUSglobalauthenticationprotocol  |     |     | PAP        |     |     |     |
| RADIUSglobalretries                 |     |     | 1retry     |     |     |     |
| RADIUSservertrackingdefaultinterval |     |     | 300seconds |     |     |     |
RADIUSserveraccessthroughthe
default*
defaultVRF
*Thedefaultvalueisdefault,unlessanotherVRFisspecifiedduringtheserverconfiguration.
| About | global | versus | per-RADIUS | server | passkeys | (shared |
| ----- | ------ | ------ | ---------- | ------ | -------- | ------- |
secrets)
TocommunicatewithaRADIUSAAAserver,theswitchmusthaveapasskey(sharedsecret)configured
thatmatcheswhatisconfiguredontheserver.Useoneofthesecommandstoachievethedesired
configuration:
n ForaglobalpasskeycommontoeveryRADIUSserver,useradius-server key.
n Foraper-RADIUSserverpasskey,useradius-server hostwiththekeyparameter.
Ifbothpasskeysareconfiguredontheswitch,theper-RADIUSserverpasskeyisused.
| Remote | AAA | RADIUS | server | configuration | requirements |     |
| ------ | --- | ------ | ------ | ------------- | ------------ | --- |
Theuser-suppliedRADIUSservermust:
n HaveanIPv4/IPv6addressorfullyqualifieddomainname(FQDN)thatisvisibletotheswitch.
n Haveapasskey(sharedsecret)thatmatcheswhatisconfiguredontheswitch.
Provideusernameandpassworddefinitionsforeveryswitchuser.Remoteusersdonotrequire
n
definitionontheswitch.
n ConfigureuserroleassignmentusingRADIUSattributes.
RemoteAAAwithRADIUS|85

ConsultyourRADIUSserverdocumentationforinstallationandgeneralconfigurationdetails.
IfSSHpublickeyauthenticationisused,thekeyinformationisstoredlocallyontheswitch,makingusernameand
passworddefinitionontheRADIUSserverunnecessary.
| User role | assignment | using | RADIUS | attributes |     |
| --------- | ---------- | ----- | ------ | ---------- | --- |
UserroleassignmentisconfiguredontheRADIUSserverusingVSAs(vendor-specificattributes).
RADIUSserverscanreturnmultipleattributevaluepairs(AVPs)inresponsetoanauthentication
request.Theattributesareprocessedinthisorderofprecedencetodeterminetheuserroleassigned:
n IftheAruba-Admin-RoleVSAispresent,maptheusertothematchinglocaluser-groupname.
o ElseiftheAruba-Priv-Admin-UserVSAispresent,extracttheprivilegelevel(1,15,or19)andmap
theusertothelocaluser-groupcorrespondingtothisprivilegelevel(1=operators,
15=administrators,19=auditors).Privilegelevels2to14mayalsobeusedwithmatchinglocal
usergroupsnamed2to14.
ElseIfService-TypeAVPispresent,mapAdministrative-User(6)toadministratorsandmap
l
NAS-Prompt-User(7)tooperators.
Otherwise,theuserrolecannotbedetermined,andtheauthenticationfails.
l
| This is      | summarized | as follows:       |              |     |                    |
| ------------ | ---------- | ----------------- | ------------ | --- | ------------------ |
| Aruba-Admin- |            | Aruba-Priv-Admin- |              |     |                    |
|              |            |                   | service-type |     | User role assigned |
| Role         |            | User              |              |     |                    |
| <GROUP-NAME> |            | Donotcare         | Donotcare    |     | Matchinglocaluser  |
<GROUP-NAME>
| Notpresent |     | privilegelevel=1     | Donotcare |     | Operators         |
| ---------- | --- | -------------------- | --------- | --- | ----------------- |
| Notpresent |     | privilegelevel=15    | Donotcare |     | Administrators    |
| Notpresent |     | privilegelevel=19    | Donotcare |     | Auditors          |
| Notpresent |     | privilegelevel=2to14 | Donotcare |     | Matchinglocaluser |
groupsnamed2to14
| Notpresent |     | Notpresent | Administrative- |     | Administrators |
| ---------- | --- | ---------- | --------------- | --- | -------------- |
User(6)
| Notpresent |     | Notpresent | NAS-Prompt-User |     | Operators |
| ---------- | --- | ---------- | --------------- | --- | --------- |
(7)
| Notpresent |     | Notpresent | Notpresent(or=any |     | None(not       |
| ---------- | --- | ---------- | ----------------- | --- | -------------- |
|            |     |            | othervalue)       |     | authenticated) |
TheService-Typeattributeisretainedonlyforbackwardcompatibility.Itisrecommendedthatyouinsteaduse
theAruba-Admin-RoleorAruba-Priv-Admin-UserVSA.
| RADIUS | server | redundancy | and access | sequence |     |
| ------ | ------ | ---------- | ---------- | -------- | --- |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 86

Topreventauthenticationinterruption,itiscommonpracticetoconfiguremorethanoneRADIUS
server.WhenidentifyingRADIUSserverstotheswitch,servergrouporder(andserverorderwithinthe
group),determinesserveraccessorder.
Whendefiningtheserveraccesssequenceforauthenticationwithaaa authentication login default,
thereisanimpliedlocalincludedasthelastiteminthelist.IfnoRADIUSservercanbereached,local
authenticationwillbeattempted.
Single source IP address for consistent source identification
| to AAA | servers |     |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- | --- |
Ifapplicabletoyourinstallation,itisrecommendedthatyouperformtheoptionalconfigurationmentionedin
thissection.
IfyourtopologyallowstheAAAservertobereachedthroughmultiplepaths,theserverinterpretsthe
incomingpacketstobefromdifferentswitcheseventhoughtheyareallcomingfromthesameswitch.
HavingaswitchassociatedwithmultipleIPaddressesmakesitmoredifficulttointerpretsystemlogs
andaccountingdata.
ToensurethatalltrafficsentfromtheswitchtotheAAAserverusesthesamesourceIPaddress,useip
source-interfaceoripv6 source-interface.Thesetwocommandsplustherelatedcommandsshow
ip source-interfaceandshow ipv6 source-interfacearedescribedunderLayer2/3Interface
commandsintheCommand-LineInterfaceGuide.
| RADIUS | general | tasks |     |     |     |     |     |
| ------ | ------- | ----- | --- | --- | --- | --- | --- |
GeneralRADIUStasks,notspecifictoauthentication,areasfollows:
| Task |     | Command | name | Example |     |     |     |
| ---- | --- | ------- | ---- | ------- | --- | --- | --- |
ConfiguringaRADIUS radius-server radius-server host 1.1.1.1 vrf default
| server |     |     |     | no radius-server |     | host 1.1.1.1 | vrf default |
| ------ | --- | --- | --- | ---------------- | --- | ------------ | ----------- |
host
| Showingglobaland |     | show radius- |     | show radius-server |     | detail |     |
| ---------------- | --- | ------------ | --- | ------------------ | --- | ------ | --- |
| RADIUSserver     |     | server       |     |                    |     |        |     |
configurations
ConfiguringaRADIUS aaa group server aaa group server radius sg3
| servergroup         |     |          |         | no aaa   | group server  | radius | sg3 |
| ------------------- | --- | -------- | ------- | -------- | ------------- | ------ | --- |
| Showingservergroups |     | show aaa | server- | show aaa | server-groups |        |     |
groups
| AddingaRADIUSserver |     | server |     | aaa group | server       | radius sg3  |         |
| ------------------- | --- | ------ | --- | --------- | ------------ | ----------- | ------- |
| toaserver-group     |     |        |     | server    | 1.1.1.4 port | 32 vrf      | default |
|                     |     |        |     | aaa group | server       | tacacs sg3  |         |
| DeletingaRADIUS     |     | server |     |           |              |             |         |
|                     |     |        |     | no server | 1.1.1.4      | port 32 vrf | default |
serverfromaserver-
group
ConfiguringaRADIUS radius-server key radius-server key plaintext mypasskey123
globalpasskey
RemoteAAAwithRADIUS|87

| Task                 |     | Command       | name Example     |           |      |
| -------------------- | --- | ------------- | ---------------- | --------- | ---- |
| ConfiguringPAPor     |     | radius-server | radius-server    | auth-type | chap |
| CHAPforRADIUS        |     | auth-type     | no radius-server | auth-type |      |
| ConfiguringtheRADIUS |     | radius-server | radius-server    | timeout   | 15   |
| globaltimeout        |     | timeout       | no radius-server | timeout   |      |
| ConfiguringtheRADIUS |     | radius-server | radius-server    | retries   | 3    |
| globalretries        |     |               | no radius-server | retries   |      |
retries
Overridingtheglobal radius-server radius-server host 1.1.1.1 retries 2
| retriesforaRADIUS |     | host |     |     |     |
| ----------------- | --- | ---- | --- | --- | --- |
server
| RADIUS | authentication |     |     |     |     |
| ------ | -------------- | --- | --- | --- | --- |
RADIUSauthenticationoccursasfollows:
n UsercredentialsaresentfromtheswitchtoRADIUSserverusingthePAPorCHAPauthentication
protocol.
n Ifauserisauthenticated,theirroleiscommunicatedtotheswitchasAdministrator,Operator,or
Auditor.
n Anunknownuserorauserwhoenteredaninvalidpasswordisidentifiedassuchtotheswitch,which
thenrejectsuserlogin.
| About | authentication | fail-through |     |     |     |
| ----- | -------------- | ------------ | --- | --- | --- |
Normally,authenticationisperformedbythefirstAAAserverreached.Ararelyneededfeaturenamed
"Authenticationfail-through"isavailable.IfAuthenticationfail-throughisenabledandauthentication
failsonthefirstreachableAAAserver,authenticationisattemptedonthesecondAAAserver,andsoon,
untilsuccessfulauthenticationortheserverlistisexhausted.
EnablingAuthenticationfail-throughistypicallyunnecessarybecausetheusercredentialdatabases
shouldbeconsistentacrossallAAAservers.Authenticationfail-throughmightbehelpfulifyourAAA
usercredentialdatabasesarenotquicklysynchronizedacrossallAAAservers.
| RADIUS | authentication |     | tasks |     |     |
| ------ | -------------- | --- | ----- | --- | --- |
TheRADIUSauthentication-relatedtasksareasfollows:
Command
| Task |     |     | Example |     |     |
| ---- | --- | --- | ------- | --- | --- |
name
Configuringthe aaa aaa authentication login default group rg1 rg2 radius
| authentication |     |     | local |     |     |
| -------------- | --- | --- | ----- | --- | --- |
authentication
sequencefor
login
thedefault
connection
type
Configuringthe aaa aaa authentication login https-server group rg1 radius
| authentication |     |     | local |     |     |
| -------------- | --- | --- | ----- | --- | --- |
authentication
sequencefor
login
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 88

Task

the https-
server
connection
type

Removing
remote AAA for
the default
connection
type

Configuring
authentication
fail-through

Showing the
authentication
sequence

Command
name

Example

aaa
authentication
login

aaa
authentication
allow-fail-
through

show aaa
authentication

no aaa authentication login default

aaa authentication allow-fail-through
no aaa authentication allow-fail-through

show aaa authentication

Configuring two-factor authentication

Two-factor authentication is available for added security. In two-factor authentication, X.509 certificate-
based authentication is combined with RADIUS authentication. When a user establishes an SSH
connection to the switch, two factor-authentication occurs as follows:

n The username in the user's X.509 certificate is validated against the local user accounts on the

switch.

n The username and password are validated against the accounts on the RADIUS server and the

configured trust anchors.

Prerequisites

n The switch SSH server is enabled.

n Your switch management computer, though its SSH client, is connected to the switch.

n A remote RADIUS server is available to authenticate switch users and is configured on the switch.

n Every user that will use two-factor authentication is configured both on the RADIUS server and locally

on the switch using identical usernames. Users are added locally on the switch with the user
command. These usernames must precisely match the usernames identified by the X.509 user
certificates.

n The X.509 CA certificate is both installed on your switch management computer and is also visible to
your computer's SSH client. The X.509 CA certificate is the root of trust for the client certificate being
used.

n One X.509 certificate per user is available on your switch management computer and is visible to

your computer's SSH client. The usernames identified by these user certificates must be the same as
the usernames already defined on the RADIUS server and locally on the switch.

Procedure

1. Create a TA profile with the command crypto pki ta-profile. This command switches to the TA

configuration context. The TA profile is where the switch stores the root certificate of the CA that

Remote AAA with RADIUS | 89

isusedtovalidatethecertificatesofclientscommunicatingwiththeSSHserver.
2. Althoughoptional,itisrecommendedthatyouenablecertificaterevocationcheckingwiththe
| commandrevocation-check |     |     |     |     | ocsp. |     |     |
| ----------------------- | --- | --- | --- | --- | ----- | --- | --- |
3. ImporttherootcertificateoftheCAwiththecommandta-certificate.
4. ExittheTAconfigurationcontextwiththecommandexit.
5. Foreachuserthatwillbeusingtwo-factorauthentication,importthepublickeyfromthe
individualX.509usercertificatewiththecommanduser <USERNAME> authorized-key <PUBKEY>.
Eachuseridentifiedby<USERNAME>mustexistlocallyontheswitchandontheRADIUS
authenticationserver.
6. Enabletwo-factorauthenticationwiththecommandssh two-factor-authentication.
Example
Thisexampleinstallstherootcertificateroot-certandenablestwo-factorauthenticationforuser
admin:
| switch(config)#              |     |     | crypto | pki | ta-profile       | root-cert |      |
| ---------------------------- | --- | --- | ------ | --- | ---------------- | --------- | ---- |
| switch(config-ta-root-cert)# |     |     |        |     | revocation-check |           | ocsp |
switch(config-ta-root-cert)#
ta-certificate
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-ta-cert)# |     |     |     | -----BEGIN |     | CERTIFICATE----- |     |
| ----------------------- | --- | --- | --- | ---------- | --- | ---------------- | --- |
switch(config-ta-cert)# MIIDuTCCAqECCQCuoxeJ2ZNYcjANBgkqhkiG9w0BAQsFADCBq
switch(config-ta-cert)# VVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEDAOBgNVBAcMB1JvY
switch(config-ta-cert)# BAoMA0hQTjEVMBMGA1UECwwMSFBOUm9zZXZpbGxlMSowKAYDV
...
switch(config-ta-cert)# x3WFf3dFZ8o9sd5LVAHneH/ztb9MP34z+le1V346r12L2MDL8
switch(config-ta-cert)# BIzD/ST/HaWI+0S+S80rm93PSscEbb9GWk7vshh5E8DH73nW/
switch(config-ta-cert)# 3LvMLZcssSe5J2Ca2XIhfDme8UaNZ7syGYoCD/TMsAW0nG7yY
| switch(config-ta-cert)# |     |     |     | -----END |     | CERTIFICATE----- |     |
| ----------------------- | --- | --- | --- | -------- | --- | ---------------- | --- |
switch(config-ta-cert)#
The certificate you are importing has the following attributes:
| Issuer: |     | C=US, ST=CA, |     | L=Rocklin, |     | O=Company, | OU=Site, |
| ------- | --- | ------------ | --- | ---------- | --- | ---------- | -------- |
CN=site.com/emailAddress=test.ca@site.com
| Subject: |     | C=US, ST=CA, |     | L=Rocklin, |     | O=Company, | OU=Site, |
| -------- | --- | ------------ | --- | ---------- | --- | ---------- | -------- |
CN=8400/emailAddress=test.ca@site.com
| Serial                       | Number: | 12121221634631568498 |     |      |             | (0xaea51217d5945772) |          |
| ---------------------------- | ------- | -------------------- | --- | ---- | ----------- | -------------------- | -------- |
| Do you                       | want    | to accept            |     | this | certificate |                      | (y/n)? y |
| TA certificate               |         | accepted.            |     |      |             |                      |          |
| switch(config-ta-root-cert)# |         |                      |     |      | exit        |                      |          |
switch(config)#
| switch(config)# |     |     | user | admin | authorized-key |     | ssh-rsa |
| --------------- | --- | --- | ---- | ----- | -------------- | --- | ------- |
AAAAB3NzaC1yc2EAAAADAQABAAACAQC6krLTrFTnzg3YjLiZKTZEYnh4cUiuOK+cjduxFnZUa
...
iAfcGvqvWtWWBSoWd011DeEZNKnOO8uEKeTEcAjfrnRHeOk2QJmw== "sv1@site.net"
switch(config)#
| switch(config)# |        |     | ssh two-factor-authentication |     |     |     |     |
| --------------- | ------ | --- | ----------------------------- | --- | --- | --- | --- |
| Secure          | RADIUS |     | (RadSec)                      |     |     |     |     |
RADIUSprotocolusesUDPasunderlyingtransportlayerprotocol.RadSecisaprotocolthatsupports
RADIUSoverTCPandTLS.InconventionalRADIUSrequests,securityisaconcernastheconfidential
dataissentusingweakencryptionalgorithms.Theaccessrequestsareinplaintextincludes
informationsuchasusername,IPaddressandsoon.Theuserpasswordisanencryptedsharedsecret.
Asaresult,eavesdropperscanlistentotheseRADIUSrequestsandcollectconfidentialinformation.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 90

Data protection is necessary in roaming environments where the RADIUS packets travel across multiple
administrative domains and untrusted networks.

RadSec module secures the communication between the switch and RADIUS server using TLS
connection. Using RADIUS over TLS provides users with the flexibility to host RADIUS servers across
geographies and WAN networks.

For enabling RADIUS security, a CLI option tls is provided with the command radius-server host,
where tls stands for Transport Layer Security.

Advantages:

n Secures the communication between the switch and RADIUS server using a TLS session.

n Provides flexibility and enhances security to host RADIUS servers across geographies and WAN

networks.

n Uses digital certificates to authenticate both client and server connection.

RadSec over VXLAN

CX supports IPv4/IPv6 RadSec over the VXLAN overlay network​ and requires additional configuration
from the user. The RadSec connection between the switch and RadSec server requires TLS with mutual
authentication. The switch and RadSec servers exchange digital certificates as a part of TLS mutual
authentication. These digital certificates often contain certificate chains which can increase the packet
sizes to over 1500 bytes. If the MTU size is set to default on all interfaces between the switch and
RadSec server then the packets that are carrying digital certificates will be dropped and the RadSec
connection will fail.

To successfully establish RadSec connection between the switch and RadSec server, MTU configuration
of all the interfaces in the path should be set to higher values based on the switch and RadSec server's
certificate size. With this configuration change the RadSec connection will be established successfully
and can be used for authentication of network clients and management users.

RadSec configuration

To configure RadSec protocol, use the following commands:

n Configure TLS using the command radius-server host tls.

n Associate the leaf certificate with RadSec feature (radsec-client) using the command crypto pki
application. To use switch inbuilt IDEVID certificate, add device-identity with the command
crypto pki application. By default, switch uses the local certificate for Radsec application. For
more information on installing certificates, see PKI chapter.

RadSec mandates validating server certificates SAN/CN while establishing connections.

Deployment scenarios

You can deploy the RADIUS/TLS servers in any of the following scenarios:

n Scenario 1: Switch establishes TLS connection with the RADIUS server.

n Scenario 2: Switch establishes TLS connection with the proxy server, which communicates with the

RADIUS server.

Remote AAA with RADIUS | 91

Figure 1 Scenario 1: Switch establishes TLS connection with the RADIUS server

In this scenario, the RADIUS server is across WAN. The RADIUS/TLS secures the user data by creating an
encrypted TLS tunnel between the switch and authentication server.

Figure 2 Scenario 2: Switch establishes TLS connection with the proxy server, which communicates with the
RADIUS server

In this scenario, multiple RADIUS servers are distributed over WAN (untrusted networks). RADIUS proxy
directs the RADIUS requests to the RADIUS server, which listens on UDP. The proxy server uses the
switch certificates to authenticate the client-server credentials. As a result, all RADIUS communications
across the network are TLS encrypted.

RadSec example configuration

Prerequisite

n ClearPass version is 6.7.4 or higher.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

92

ClearPass as RadSec server

Following are the steps to configure ClearPass as RadSec server:

1. From the ClearPass Web UI, navigate to Administration > Certificates >Certificate store and
click Import Certificate to import the Root CA certificate to the ClearPass certificate store.

2. The Import Certificate window opens. In the Certificate Type field, select Server Certificate.

Specify the server and upload method. In the Usage field, you must select Radsec Server
Certificate.

3. Click Import.

4. next, click Create Certificate Signing Request. In the Common Name field, enter the IP address

of the ClearPass server. For configuring radius-server host , enter the hostname.

5. Click Submit. You can download the CSR or copy and paste the displayed CSR content into the

web form in the enrollment process.

6. Sign the created CSR with the CA.

Remote AAA with RADIUS | 93

7. Select Enable RadSec while adding devices.The IP address is used as the source IP of the switch.

RADIUS accounting

This accounting information is captured and made available for sending to remote accounting servers:

n Port access accounting

n Exec Accounting: user login/logout events

n Command accounting: commands executed by users. The Vendor-Specific Attribute (VSA) Aruba_

Command_String with a value of 46 is available.

n System accounting: remote accounting On/Off events.

n CLI show commands.

n Interactions on the non-CLI interfaces: REST and WebUI.

With RADIUS, command accounting logs a maximum of 247 characters per command entered by the user.

The following is not captured or made available as accounting information:

n CLI commands that reboot the switch.

n Interactions in the bash shell.

Local accounting (always enabled) must be functioning properly for remote Accounting to work.

The accounting information is sent to the first reachable remote RADIUS AAA server (configured for remote

accounting). If no remote RADIUS server is reachable, local accounting remains available.

Sample general accounting information

~~~~~~~~ EXEC ~~~~~~~~~~

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

94

| Mon Jul 16 | 16:25:27 2018 |     |     |     |
| ---------- | ------------- | --- | --- | --- |
User-Name = "admin"
| NAS-Identifier |     | = "switchx" |     |     |
| -------------- | --- | ----------- | --- | --- |
NAS-Port = 331
| NAS-Port-Type          |     | = Virtual         |                      |      |
| ---------------------- | --- | ----------------- | -------------------- | ---- |
| Acct-Status-Type       |     | = Start           |                      |      |
| Acct-Session-Id        |     | = "1531769192494" |                      |      |
| Acct-Authentic         |     | = Local           |                      |      |
| Calling-Station-Id     |     | = "0.0.0.0"       |                      |      |
| Event-Timestamp        |     | = "Jul            | 16 2018 16:25:22     | PDT" |
| Acct-Delay-Time        |     | = 0               |                      |      |
| NAS-IP-Address         |     | = 10.10.10.1      |                      |      |
| Acct-Unique-Session-Id |     |                   | = "b83e29f4140c17b1" |      |
Timestamp = 1531783527
| ~~~ EXEC stop | ~~~           |     |     |     |
| ------------- | ------------- | --- | --- | --- |
| Mon Jul 16    | 16:26:42 2018 |     |     |     |
User-Name = "admin"
| NAS-Identifier |     | = "switchx" |     |     |
| -------------- | --- | ----------- | --- | --- |
NAS-Port = 331
| NAS-Port-Type          |     | = Virtual         |                      |      |
| ---------------------- | --- | ----------------- | -------------------- | ---- |
| Acct-Status-Type       |     | = Stop            |                      |      |
| Acct-Session-Id        |     | = "1531769192494" |                      |      |
| Acct-Authentic         |     | = Local           |                      |      |
| Calling-Station-Id     |     | = "0.0.0.0"       |                      |      |
| Event-Timestamp        |     | = "Jul            | 16 2018 16:26:37     | PDT" |
| Acct-Delay-Time        |     | = 0               |                      |      |
| Acct-Session-Time      |     | = 75              |                      |      |
| NAS-IP-Address         |     | = 10.10.10.1      |                      |      |
| Acct-Unique-Session-Id |     |                   | = "b83e29f4140c17b1" |      |
Timestamp = 1531783602
| ~~~~~~~~ CMD | ACCOUNTING    | ~~~~~~~~~~~~ |     |     |
| ------------ | ------------- | ------------ | --- | --- |
| Mon Jul 16   | 16:26:42 2018 |              |     |     |
User-Name = "admin"
| NAS-Identifier |     | = "switchx" |     |     |
| -------------- | --- | ----------- | --- | --- |
NAS-Port = 331
| NAS-Port-Type          |     | = Virtual         |                      |      |
| ---------------------- | --- | ----------------- | -------------------- | ---- |
| Acct-Status-Type       |     | = Stop            |                      |      |
| Acct-Session-Id        |     | = "1531769192496" |                      |      |
| Acct-Authentic         |     | = Local           |                      |      |
| Aruba-Command-String   |     | =                 | "exit"               |      |
| Calling-Station-Id     |     | = "0.0.0.0"       |                      |      |
| Event-Timestamp        |     | = "Jul            | 16 2018 16:26:37     | PDT" |
| Acct-Delay-Time        |     | = 0               |                      |      |
| NAS-IP-Address         |     | = 10.10.10.1      |                      |      |
| Acct-Unique-Session-Id |     |                   | = "280710992629128c" |      |
Timestamp = 1531783602
| ~~~~~~~~~~~~~ | SYSTEM        | ACCOUNTING | ~~~~~~~~~~~~ |     |
| ------------- | ------------- | ---------- | ------------ | --- |
| Mon Jul 16    | 17:13:02 2018 |            |              |     |
User-Name = "UNKNOWN"
| NAS-Identifier |     | = "UNKNOWN" |     |     |
| -------------- | --- | ----------- | --- | --- |
NAS-Port = 331
| NAS-Port-Type      |     | = Virtual         |     |     |
| ------------------ | --- | ----------------- | --- | --- |
| Acct-Status-Type   |     | = Accounting-On   |     |     |
| Acct-Session-Id    |     | = "1531769192506" |     |     |
| Acct-Authentic     |     | = Local           |     |     |
| Calling-Station-Id |     | = "0.0.0.0"       |     |     |
RemoteAAAwithRADIUS|95

|     | Event-Timestamp        | = "Jul            | 16 2018 17:12:56     | PDT" |     |     |
| --- | ---------------------- | ----------------- | -------------------- | ---- | --- | --- |
|     | Acct-Delay-Time        | = 0               |                      |      |     |     |
|     | NAS-IP-Address         | = 10.10.10.1      |                      |      |     |     |
|     | Acct-Unique-Session-Id |                   | = "b478e6402c86933e" |      |     |     |
|     | Timestamp =            | 1531786382        |                      |      |     |     |
| Mon | Jul 16 17:12:55        | 2018              |                      |      |     |     |
|     | User-Name =            | "UNKNOWN"         |                      |      |     |     |
|     | NAS-Identifier         | = "UNKNOWN"       |                      |      |     |     |
|     | NAS-Port =             | 331               |                      |      |     |     |
|     | NAS-Port-Type          | = Virtual         |                      |      |     |     |
|     | Acct-Status-Type       | = Accounting-Off  |                      |      |     |     |
|     | Acct-Session-Id        | = "1531769192491" |                      |      |     |     |
|     | Acct-Authentic         | = Local           |                      |      |     |     |
|     | Calling-Station-Id     | = "0.0.0.0"       |                      |      |     |     |
|     | Event-Timestamp        | = "Jul            | 16 2018 17:12:49     | PDT" |     |     |
|     | Acct-Delay-Time        | = 0               |                      |      |     |     |
|     | NAS-IP-Address         | = 10.10.10.1      |                      |      |     |     |
|     | Acct-Unique-Session-Id |                   | = "93da1f094121f2ee" |      |     |     |
|     | Timestamp =            | 1531786375        |                      |      |     |     |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ThissampleisrepresentativeandnotfromanyparticularRADIUSserverimplementation.
| RADIUS | accounting | tasks |     |     |     |     |
| ------ | ---------- | ----- | --- | --- | --- | --- |
TheRADIUSaccounting-relatedtasksareasfollows:
Command
| Task |     | Example |     |     |     |     |
| ---- | --- | ------- | --- | --- | --- | --- |
name
Configuring aaa aaa accounting all-mgmt default start-stop group rg1 rg2
|            |            | radius local |     |     |     |     |
| ---------- | ---------- | ------------ | --- | --- | --- | --- |
| the        | accounting |              |     |     |     |     |
| accounting | all-mgmt   |              |     |     |     |     |
sequencefor
thedefault
connection
type
|             |            | aaa accounting | all-mgmt | https-server | start-stop | group rg1 |
| ----------- | ---------- | -------------- | -------- | ------------ | ---------- | --------- |
| Configuring | aaa        |                |          |              |            |           |
|             |            | radius local   |          |              |            |           |
| the         | accounting |                |          |              |            |           |
| accounting  | all-mgmt   |                |          |              |            |           |
sequencefor
thehttps-
server
connection
type
| Removing  | aaa        | no aaa accounting | all-mgmt | default | start-stop |     |
| --------- | ---------- | ----------------- | -------- | ------- | ---------- | --- |
| remoteAAA | accounting |                   |          |         |            |     |
forthe
all-mgmt
default
connection
type
| Showingthe | show aaa | show aaa | accounting |     |     |     |
| ---------- | -------- | -------- | ---------- | --- | --- | --- |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 96

Command
| Task |     |     |     | Example |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
name
| accounting |     | accounting |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
configuration
| Example: |     | Configuring |     |     | the | switch |     | for | Remote | AAA | with |
| -------- | --- | ----------- | --- | --- | --- | ------ | --- | --- | ------ | --- | ---- |
RADIUS
Prerequisites
n RADIUSserversconfiguredingeneralaccordingtotheinformationinRemoteAAARADIUSserver
configurationrequirements.Theexactsettingsappropriatetoyourenvironmentwillvary.
n LoggedintotheswitchwithAdministratorprivilegeandintheconfigcontext.
Procedure
1. ConfiguretheglobalRADIUSpasskey(sharedsecret)as"xjkW74932qX3j_$"
|     | switch(config)# |     |     | radius-server |     | key | plaintext |     | xjkW74932qX3j_$ |     |     |
| --- | --------------- | --- | --- | ------------- | --- | --- | --------- | --- | --------------- | --- | --- |
switch(config)#
2. AddtheseconfigurationdetailsfortworemoteRADIUSservers.
n Server1withIPv4address10.0.0.2,onthemanagementinterface(belongingtoVRF“mgmt”),
usingthedefaultPAPprotocol.
n Server2withIPv4address4.0.0.2,onthedatainterface(belongingtoVRF“default”),usingthe
CHAPprotocol.
|     | switch(config)# |     |     | radius-server |     | host | 10.0.0.2 |     | vrf mgmt  |      |     |
| --- | --------------- | --- | --- | ------------- | --- | ---- | -------- | --- | --------- | ---- | --- |
|     | switch(config)# |     |     | radius-server |     | host | 4.0.0.2  |     | auth-type | chap |     |
switch(config)#
3. CreateaRADIUSgroupnamedrad_grp1,assignRADIUSserver10.0.0.2tothegroup,showthe
groupinformation.
ThedefaultRADIUSgroupnamedradiusincludeseveryRADIUSserverregardlessofwhether
anyRADIUSserversarealsoassignedtoauser-definedRADIUSgroup.
|     | switch(config)#    |     |     | aaa | group  | server   | radius | rad_grp1 |     |     |     |
| --- | ------------------ | --- | --- | --- | ------ | -------- | ------ | -------- | --- | --- | --- |
|     | switch(config-sg)# |     |     |     | server | 10.0.0.2 | vrf    | mgmt     |     |     |     |
|     | switch(config-sg)# |     |     |     | exit   |          |        |          |     |     |     |
switch(config)#
|     | switch(config)# |     |           | do  | show aaa | server-groups |     | radius |     |     |     |
| --- | --------------- | --- | --------- | --- | -------- | ------------- | --- | ------ | --- | --- | --- |
|     | *******         | AAA | Mechanism |     | RADIUS   | *******       |     |        |     |     |     |
-------------------------------------------------------------------------
|     | GROUP | NAME |     | |   | SERVER | NAME |     |     | | PORT | | VRF | | PRIORITY |
| --- | ----- | ---- | --- | --- | ------ | ---- | --- | --- | ------ | ----- | ---------- |
-------------------------------------------------------------------------
RemoteAAAwithRADIUS|97

| rad_grp1 |     | | 10.0.0.2 |     |     | | 1812 | mgmt | | 1 |
| -------- | --- | ---------- | --- | --- | ------------- | --- |
-------------------------------------------------------------------------
| radius (default) |     | | 10.0.0.2 |     |     | | 1812 | mgmt    | | 1 |
| ---------------- | --- | ---------- | --- | --- | ---------------- | --- |
| radius (default) |     | | 4.0.0.2  |     |     | | 1812 | default | | 2 |
-------------------------------------------------------------------------
switch(config)#
4. DefinetheauthenticationsequencelistsothatthenewRADIUSgroupisfirst,thedefaultRADIUS
groupissecond,andlocalisthird.Showtheauthenticationsequence.
switch(config)#
|     |     | aaa authentication |     | login default | group rad_grp1 | radius local |
| --- | --- | ------------------ | --- | ------------- | -------------- | ------------ |
switch(config)#
| switch(config)# |     | do show aaa | authentication |     |     |     |
| --------------- | --- | ----------- | -------------- | --- | --- | --- |
AAA Authentication:
| Fail-through           |          |        |               | : Disabled |     |     |
| ---------------------- | -------- | ------ | ------------- | ---------- | --- | --- |
| Limit Login            | Attempts |        |               | : Not      | set |     |
| Lockout                | Time     |        |               | : 300      |     |     |
| Minimum                | Password | Length |               | : Not      | set |     |
| Default Authentication |          | for    | All Channels: |            |     |     |
----------------------------------------------------------------------------
---
| GROUP NAME |     |     |     | | GROUP PRIORITY |     |     |
| ---------- | --- | --- | --- | ---------------- | --- | --- |
----------------------------------------------------------------------------
---
| rad_grp1 |     |     |     | | 0 |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
| radius   |     |     |     | | 1 |     |     |
| local    |     |     |     | | 2 |     |     |
----------------------------------------------------------------------------
---
switch(config)#
5. DefinetheaccountingsequencelistwithtwoRADIUSservergroups.Showtheaccounting
sequence.
switch(config)# aaa accounting all default start-stop group rad_grp1 radius
switch(config)#
| switch(config)# |     | do show aaa | accounting |     |     |     |
| --------------- | --- | ----------- | ---------- | --- | --- | --- |
AAA Accounting:
| Accounting         | Type |         |           |     | : all        |     |
| ------------------ | ---- | ------- | --------- | --- | ------------ | --- |
| Accounting         | Mode |         |           |     | : start-stop |     |
| Default Accounting |      | for All | Channels: |     |              |     |
----------------------------------------------------------------------------
--
| GROUP NAME |     |     |     | | GROUP PRIORITY |     |     |
| ---------- | --- | --- | --- | ---------------- | --- | --- |
----------------------------------------------------------------------------
--
| rad_grp1 |     |     |     | | 0 |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
| radius   |     |     |     | | 1 |     |     |
----------------------------------------------------------------------------
--
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 98

Remote AAA (TACACS+, RADIUS) commands

Chapter 10

Remote AAA (TACACS+, RADIUS) commands

aaa accounting all-mgmt
aaa accounting all-mgmt <CONNECTION-TYPE> start-stop {local | group <GROUP-LIST>}
no aaa accounting all-mgmt <CONNECTION-TYPE> start-stop {local | group <GROUP-LIST>}

Description

Defines accounting as being local (with the name local) (the default). Or defines a sequence of remote
AAA server groups to be accessed for accounting purposes.

For remote accounting, the information is sent to the first reachable remote server that was configured
with this command for remote accounting. If no remote server is reachable, local accounting remains
available. Each available connection type (channel) can be configured individually as either local or using
remote AAA server groups. All server groups named in your command, must exist. This command can
be issued multiple times, once for each connection type. Local is always available for any connection
type not configured for remote accounting.

The system accounting log is not associated with any connection type (channel) and is therefore sent to the

accounting method configured on the default connection type (channel) only.

The no form of this command removes for the specified connection type, any defined remote AAA server
group accounting sequence. Local accounting is available for connection types without a configured
remote AAA server group list (whether default or for the specific connection type).

Parameter

Description

<CONNECTION-TYPE>

One of these connection types (channels):
default

Defines a list of accounting server groups to be used for the
default connection type. This configuration applies to all
other connection types (console, https-server, ssh) that
are not explicitly configured with this command. For example,
if you do not use aaa accounting all-mgmt console...
to define the console accounting list, then this default
configuration is used for console.

console

Defines a list of accounting server groups to be used for the
console connection type.

https-server

Defines a list of accounting server groups to be used for the
https-server (REST, Web UI) connection type.

ssh

Defines a list of accounting server groups to be used for the
ssh connection type.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

99

Parameter

start-stop

local

group <GROUP-LIST>

Description

Selects accounting information capture at both the beginning and
end of a process.

Selects local-only accounting when used without the group
parameter.

Specifies the list of remote AAA server group names. Each name
can be specified one time. Predefined remote AAA group names
tacacs and radius are available. Although not a group name,
predefined name local is available. User-defined TACACS+ and
RADIUS server group names may also be used.
The remote AAA server groups are accessed in the order that the
group names are listed in this command. Within each group, the
servers are accessed in the order in which the servers were added
to the group. Server groups are defined using command aaa
group server and servers are added to a server group with the
command server.

Usage

Local accounting is always active. It cannot be turned off.

Examples

Defining the default accounting sequence based on two user-defined TACACS+ server groups, then the
default TACACS+ server group, and finally (if needed), local accounting.

switch(config)# aaa accounting all-mgmt default start-stop group tg1 tg2 tacacs
local

Defining the console accounting sequence based on two user-defined TACACS+ server groups, then the
default TACACS+ server group, and finally (if needed), local accounting.

switch(config)# aaa accounting all-mgmt console start-stop group tg2 tg3 tacacs
local

Defining the ssh accounting sequence based on one user-defined TACACS+ server group and then the
default TACACS+ server group.

switch(config)# aaa accounting all-mgmt ssh start-stop group tg2 tacacs

Defining the default accounting sequence based on two user-defined RADIUS server groups, then the
default RADIUS server group, and finally (if needed), local accounting.

switch(config)# aaa accounting all-mgmt default start-stop group rg1 rg2 radius
local

Defining the https-server accounting sequence based on one user-defined RADIUS server group and
then the default RADIUS server group.

Remote AAA (TACACS+, RADIUS) commands | 100

switch(config)# aaa accounting all-mgmt https-server start-stop group rg1 radius
Settinglocalaccountingforthedefaultconnectiontype:
switch(config)# aaa accounting all-mgmt default start-stop local
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| aaa authentication    |                    | allow-fail-through |     |
| --------------------- | ------------------ | ------------------ | --- |
| aaa authentication    | allow-fail-through |                    |     |
| no aaa authentication |                    | allow-fail-through |     |
Description
Enablesauthenticationfail-through.Whenthisoptionisenabled,thenextserver/authentication
methodistriedafteranauthenticationfailure.
Thenoformofthiscommanddisablesauthenticationfail-through.Ifthesystemfailstoauthenticate
withareachableTACACS+orRADIUSserver,thesystemdoesnotattempttoauthenticatewiththenext
TACACS+/RADIUSserver.
Example
Enablingauthenticationfail-through:
| switch(config)#     | aaa     | authentication | allow-fail-through |
| ------------------- | ------- | -------------- | ------------------ |
| Command History     |         |                |                    |
| Release             |         |                | Modification       |
| 10.07orearlier      |         |                | --                 |
| Command Information |         |                |                    |
| Platforms           | Command | context        | Authority          |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 101

aaa authentication login
aaa authentication login <CONNECTION-TYPE> {local | group <GROUP-LIST>}
no aaa authentication login <CONNECTION-TYPE> {local | group <GROUP-LIST>}

Description

Defines authentication as being local (with the name local) (the default). Or defines a sequence of
remote AAA server groups to be accessed for authentication purposes. Each available connection type
(channel) can be configured individually as either local or using remote AAA server groups. All server
groups named in your command, must exist. This command can be issued multiple times, once for each
connection type. Local is always available for any connection type not configured for remote AAA
authentication.

If you do not want local authentication to occur in cases where all AAA servers contacted reject the user's
credentials, do not enable authentication fail-through (command aaa authentication allow-fail-
through).

The no form of this command removes for the specified connection type, any defined remote AAA
server group authentication sequence. Local authentication is available for connection types without a
configured remote AAA server group list (whether default or for the specific connection type).

Parameter

Description

<CONNECTION-TYPE>

local

group <GROUP-LIST>

One of these connection types (channels):
default

Defines a list of accounting server groups to be used for the
default connection type. This configuration applies to all
other connection types (console, https-server, ssh) that
are not explicitly configured with this command. For example,
if you do not use aaa accounting all-mgmt console...
to define the console accounting list, then this default
configuration is used for console.

console

Defines a list of accounting server groups to be used for the
console connection type.

https-server

Defines a list of accounting server groups to be used for the
https-server (REST, Web UI) connection type.

ssh

Defines a list of accounting server groups to be used for the
ssh connection type.

Selects local-only accounting when used without the group
parameter.

Specifies the list of remote AAA server group names. Each name
can be specified one time. Predefined remote AAA group names
tacacs and radius are available. Although not a group name,
predefined name local is available. User-defined TACACS+ and
RADIUS server group names may also be used.
The remote AAA server groups are accessed in the order that the
group names are listed in this command. Within each group, the
servers are accessed in the order in which the servers were added
to the group. Server groups are defined using command aaa

Remote AAA (TACACS+, RADIUS) commands | 102

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
group serverandserversareaddedtoaservergroupwiththe
commandserver.
Examples
Definingthedefaultauthenticationsequencebasedontwouser-definedTACACS+servergroups,then
thedefaultTACACS+servergroup,andfinally(ifneeded),localauthentication.
switch(config)# aaa authentication login default group tg1 tg2 tacacs local
Definingtheconsoleauthenticationsequencebasedontwouser-definedTACACS+servergroups,then
thedefaultTACACS+servergroup,andfinally(ifneeded),localauthentication.
switch(config)# aaa authentication login console group tg2 tg3 tacacs local
Definingthesshauthenticationsequencebasedononeuser-definedTACACS+servergroupandthen
thedefaultTACACS+servergroup.
| switch(config)# | aaa | authentication | login ssh | group tg2 | tacacs |
| --------------- | --- | -------------- | --------- | --------- | ------ |
Definingthedefaultauthenticationsequencebasedontwouser-definedRADIUSservergroups,then
thedefaultRADIUSservergroup,andfinally(ifneeded),localauthentication.
switch(config)# aaa authentication login default group rg1 rg2 radius local
Definingthehttps-serverauthenticationsequencebasedononeuser-definedRADIUSservergroupand
thenthedefaultRADIUSservergroup.
switch(config)# aaa authentication login https-server group rg1 radius
Settinglocalauthenticationforthedefaultconnectiontype:
switch(config)#
|                     | aaa     | authentication | login default | local |     |
| ------------------- | ------- | -------------- | ------------- | ----- | --- |
| Command History     |         |                |               |       |     |
| Release             |         |                | Modification  |       |     |
| 10.07orearlier      |         |                | --            |       |     |
| Command Information |         |                |               |       |     |
| Platforms           | Command | context        | Authority     |       |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 103

aaa authorization commands (remote)
aaa authorization commands <CONNECTION-TYPE> {local | none}
no aaa authorization commands <CONNECTION-TYPE> {local | none}
aaa authorization commands <CONNECTION-TYPE> group <GROUP-LIST>
no aaa authorization commands <CONNECTION-TYPE> group <GROUP-LIST>

Description

Defines authorization as being basic local RBAC (specified as none), or as full-fledged local RBAC
specified as local (the default), or as remote TACACS+ (specified with group <GROUP-LIST>). Each
available connection type (channel) can be configured individually. All server groups named in the
command, must exist. This command can be issued multiple times, once for each connection type.

The no form of this command unconfigures authorization for the specified connection type, reverting to
the default of local.

Although only TACACS+ servers are supported for remote authorization, local authorization (basic or full-fledged)

can be used with remote RADIUS authentication.

Parameter

Description

<CONNECTION-TYPE>

One of these connection types (channels):
default

local

none

Selects the default connection type for configuration. This
configuration applies to all other connection types (console,
ssh) that are not explicitly configured with this command. For
example, if you do not use aaa authorization commands
console... to define the console authorization list, then this
default configuration is used for console.

console

Selects the console connection type for configuration.

ssh

Selects the ssh connection type for configuration.

When used alone without group <GROUP-LIST>, selects local
authorization which can be used to provide authorization for a
purely local setup without any remote AAA servers and also for
when RADIUS is used for remote Authentication and Accounting
but Authorization is local. When used after group, provides for
fallback (to full-fledged local authorization) when every server in
every specified TACACS+ server group cannot be reached.

NOTE: If any TACACS+ server in the specified groups is reachable,
but the command fails to be authorized by that server, the
command is rejected and local authorization is never attempted.
Local authorization is only attempted if every TACACS+ server
cannot be reached.

When used alone without group <GROUP-LIST>, selects basic
local RBAC authorization, for use with the built-in user groups
(administrators, operators, auditors). When used after
group, provides for fallback (to basic local RBAC authorization)
when every server in every specified TACACS+ server group
cannot be reached.

Remote AAA (TACACS+, RADIUS) commands | 104

Parameter

Description

group <GROUP-LIST>

NOTE: With none, for users belonging to user-defined user
groups, all commands can be executed regardless of what
authorization rules are defined in such groups. For per-command
local authorization, use local instead.

Specifies the list of remote AAA server group names. Predefined
remote AAA group name tacacs is available. User-defined
TACACS+ server group names may also be used. The remote AAA
server groups are accessed in the order that the group names are
listed in this command. Within each group, the servers are
accessed in the order in which the servers were added to the
group. Server groups are defined using command aaa server
group and servers are added to a server group using command
server.
It is recommended to always include either the special name
local or none as the last name in the group list. If both local
and none are omitted, and no remote AAA server is reachable (or
the first reachable server cannot authorize the command),
command execution for the current user will not be possible.

Usage

TACACS+ server authorization considerations

Use caution when configuring authorization, as it has no fail through. If the switch is not configured properly, the

switch might get into an unusable state in which all command execution is prohibited.

To prevent authorization difficulties:

n Make sure that all listed TACACS+ servers can authorize users for command execution.

n Make sure that credential database changes are promptly synchronized across all TACACS+ servers.

n Make sure either local or none is included as the last name in the group list. If both local and none

are omitted, and no remote TACACS+ server is reachable (or the first reachable server cannot
authorize), authorization will not be possible.

n Although not recommended, if you choose to omit both local and none from the list, and are

manipulating configuration files, special caution is necessary. If the source configuration includes
TACACS⁠+ authorization and you are copying configuration from an existing switch into the running
configuration of a new switch, and you have not yet configured the interface or routing information
to reach the TACACS+ server, the switch will enter an unusable state, requiring hard reboot.

To avoid getting into this situation that can occur when local and none have been omitted, do either
of the following:

o In the configuration source, delete or comment-out the line configuring remote authorization. Then,

after the configuration copy and paste, manually configure authorization.

o Move the line configuring the authorization to the end of the source configuration before copying

and pasting.

Examples

Defining the default authorization sequence based on a user-defined TACACS+ server group, then the
default TACACS+ server group, and finally (as a precaution), local authorization:

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

105

switch(config)# aaa authorization commands default group tg1 tacacs local
All commands will fail if none of the servers in the group list are reachable.
| Continue | (y/n)? | y   |     |     |     |
| -------- | ------ | --- | --- | --- | --- |
Definingtheconsoleauthorizationsequencebasedontwouser-definedTACACS+servergroups,and
finally(asaprecaution),localauthorization:
switch(config)# aaa authorization commands console group tg1 tg2 local
All commands will fail if none of the servers in the group list are reachable.
| Continue | (y/n)? | y   |     |     |     |
| -------- | ------ | --- | --- | --- | --- |
Settingtheauthorizationfordefaulttolocal:
| switch(config)# |     | aaa | authorization | commands default | local |
| --------------- | --- | --- | ------------- | ---------------- | ----- |
SettingtheauthorizationfortheSSHinterfacetonone:
| switch(config)# |             | aaa | authorization | commands ssh | none |
| --------------- | ----------- | --- | ------------- | ------------ | ---- |
| Command         | History     |     |               |              |      |
| Release         |             |     |               | Modification |      |
| 10.07orearlier  |             |     |               | --           |      |
| Command         | Information |     |               |              |      |
| Platforms       | Command     |     | context       | Authority    |      |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| aaa group | server       |         |           |                     |     |
| --------- | ------------ | ------- | --------- | ------------------- | --- |
| aaa group | server       | {tacacs | | radius} | <SERVER-GROUP-NAME> |     |
| no aaa    | group server | {tacacs | | radius} | <SERVER-GROUP-NAME> |     |
Description
CreatesanAAAservergroupthatiseitheremptyorcontainspreconfiguredRADIUS/TACACS+servers.
Youcancreateamaximumof28servergroups.
Thenoformofthiscommanddeletesaservergroup.Onlyapreconfigureduser-defined
RADIUS/TACACS+servergroupcanbedeleted.RADIUSorTACACS+serversthatwereinadeleted
servergroupremainapartoftheirdefaultservergroup.ThedefaultservergroupforTACACS+servers
istacacs.ThedefaultservergroupforRADIUSserversisradius.
RemoteAAA(TACACS+,RADIUS)commands|106

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
server {tacacs | radius} Selecteithertacacsorradiusfortheservertype.
<SERVER-GROUP-NAME> Specifiesthenameoftheservergrouptobecreated.Thenameof
theservergroupcanhaveamaximumof32characters.
Examples
CreatingTACACS+servergroupsg1:
| switch(config)# |     | aaa | group | server | tacacs | sg1 |
| --------------- | --- | --- | ----- | ------ | ------ | --- |
CreatingRADIUSservergroupsg3:
| switch(config)# |     | aaa | group | server | radius | sg3 |
| --------------- | --- | --- | ----- | ------ | ------ | --- |
DeletingTACACS+servergroupsg1:
| switch(config)# |     | no  | aaa group | server | tacacs | sg1 |
| --------------- | --- | --- | --------- | ------ | ------ | --- |
DeletingRADIUSservergroupsg3:
| switch(config)# |             | no  | aaa group | server | radius       | sg3 |
| --------------- | ----------- | --- | --------- | ------ | ------------ | --- |
| Command         | History     |     |           |        |              |     |
| Release         |             |     |           |        | Modification |     |
| 10.07orearlier  |             |     |           |        | --           |     |
| Command         | Information |     |           |        |              |     |
| Platforms       | Command     |     | context   |        | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| radius-server    |           | auth-type |      |         |       |     |
| ---------------- | --------- | --------- | ---- | ------- | ----- | --- |
| radius-server    | auth-type |           | {pap | | chap} |       |     |
| no radius-server |           | auth-type | {pap | |       | chap} |     |
Description
EnablestheCHAPorPAPauthenticationprotocol,whichisusedforcommunicationwiththeRADIUS
servers,atthegloballevel.Youcanoverridethiscommandwithafine-grainedperserverauth-type
configuration.
ThenoformofthiscommandresetstheglobalauthenticationmechanismforRADIUStoPAPorCHAP.
PAP isthedefaultauthenticationmechanismforRADIUS.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 107

| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
auth-type {pap | chap} SelectseitherthePAPorCHAPauthenticationprotocol.
Examples
AuthenticatingCHAP:
| switch(config)# |     | radius-server |     | auth-type |     | chap |
| --------------- | --- | ------------- | --- | --------- | --- | ---- |
AuthenticatingPAP:
| switch(config)# |     | radius-server |     | auth-type |     | pap |
| --------------- | --- | ------------- | --- | --------- | --- | --- |
RemovingCHAP authentication:
| switch(config)# |             | no      | radius-server | auth-type    |           | chap |
| --------------- | ----------- | ------- | ------------- | ------------ | --------- | ---- |
| Command         | History     |         |               |              |           |      |
| Release         |             |         |               | Modification |           |      |
| 10.07orearlier  |             |         |               | --           |           |      |
| Command         | Information |         |               |              |           |      |
| Platforms       |             | Command | context       |              | Authority |      |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| radius-server   |                    | host      |          |                      |             |     |
| --------------- | ------------------ | --------- | -------- | -------------------- | ----------- | --- |
| radius-server   | host               | {<FQDN>   | | <IPV4> | |                    | <IPV6>}     |     |
| [key [plaintext |                    | <PASSKEY> | |        | ciphertext           | <PASSKEY>]] |     |
| [timeout        | <TIMEOUT-SECONDS>] |           |          | [port <PORT-NUMBER>] |             |     |
[auth-type {pap | chap}] [acct-port <ACCT-PORT>] [retries <RETRY-COUNT>]
[tracking {enable | disable}] [tracking-mode {any | dead-only}][vrf <VRF-NAME>]
| no radius-server |                    | host      | {<FQDN> | | <IPV4>             | | <IPV6>}   |     |
| ---------------- | ------------------ | --------- | ------- | -------------------- | ----------- | --- |
| [key [plaintext  |                    | <PASSKEY> | |       | ciphertext           | <PASSKEY>]] |     |
| [timeout         | <TIMEOUT-SECONDS>] |           |         | [port <PORT-NUMBER>] |             |     |
[auth-type {pap | chap}] [acct-port <ACCT-PORT>] [retries <RETRY-COUNT>]
[tracking {enable | disable}] [tracking-mode {any | dead-only}][vrf <VRF-NAME>]
Description
AddsaRADIUSserver.Bydefault,theRADIUSserverisassociatedwiththeservergroupnamedradius.
ThenoformofthiscommandremovesapreviouslyaddedRADIUSserver.
RemoteAAA(TACACS+,RADIUS)commands|108

For enhanced security with IPsec, the alternative command radius-server host secure ipsec is available.
The standard non-IPsec radius-server host command does not modify any existing IPsec configuration. If
IPsec is already configured for the RADIUS server, then IPsec will remain enabled for the server.

Parameter

Description

{<FQDN> | <IPV4> | <IPv6>}

key [plaintext
ciphertext

<PASSKEY> |
<PASSKEY>]

Specifies the RADIUS server as:
n <FQDN>: a fully qualified domain name.
n <IPV4>: an IPv4 address.
n <IPV6>: an IPv6 address.

Selects either a plaintext or an encrypted local shared-secret
passkey for the server. As per RFC 2865, shared-secret can be a
mix of alphanumeric and special characters. Plaintext passkeys
are between 1 and 32 alphanumeric and special characters.

NOTE: When key is entered without either sub-parameter,
plaintext passkey prompting occurs upon pressing Enter. Enter
must be pressed immediately after the key parameter without
entering other parameters. The entered passkey characters are
masked with asterisks. When key is omitted, the server uses the
global passkey. This command requires either the global or local
passkey to be set; otherwise the server will not be contacted.
Command radius-server key is available for setting the global
passkey.

timeout

<TIMEOUT-SECONDS>

Specifies the timeout. Range: 1 to 60 seconds. If a timeout is not
specified, the value from the global timeout for RADIUS is used.

port <PORT-NUMBER>

auth-type {pap | chap}

acct-port <ACCT-PORT>

retries <RETRY-COUNT>

tracking {enable | disable}

Specifies the authentication port number. Range: 1 to 65535.
Default: 1812.

Selects either the PAP (the default) or CHAP authentication types.
If this parameter is not specified, the RADIUS global default is
used.

Specifies the UDP accounting port number. Range: 1 to 65535.
Default: 1813.

Specifies the number of retry attempts for contacting the specified
RADIUS server. Range is 0 to 5 attempts. If no retry value is
provided, the default value of 1 is used.

Enables or disables server tracking for the RADIUS server. Tracked
servers are probed at the start of each server tracking interval to
check if they are reachable.
Use command radius-server tracking to configure RADIUS
server tracking globally.

NOTE: Server tracking uses authentication request and response
packets to determine server reachability status. The server
tracking user name and password are used to form the request
packet which is sent to the server with tracking enabled. Upon
receiving a response to the request packet, the server is
considered to be reachable.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

109

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
tracking-mode {any | dead-only} ConfigurestrackingmodefortheRADIUSserverthathastracking
enabledwiththeserver.Thetrackingmodeisusedtomonitorthe
statusofRADIUSserverreachabilityThedefaulttrackingmodeis
any.
any
TracktheRADIUSserverirrespectiveofitsserverreachability.
dead-only
TracktheRADIUSserveronlywhentheserverismarkedas
unreachable.
vrf <VRF-NAME> SpecifiestheVRFnametobeusedforcommunicatingwiththe
server.IfnoVRFnameisprovided,thedefaultVRFnamed
defaultisused.
Usage
IfthefullyqualifieddomainnameisprovidedfortheRADIUSserver,aDNSservermustbeconfigured
andaccessiblethroughthesameVRFwhichisconfiguredfortheRADIUSserver.Thisconfigurationis
requiredfortheresolutionoftheRADIUSserverhostnametoitsIPaddress.IfaDNSserverisnot
availableforthisVRF,theRADIUSserversreachablethroughthisVRFmustbeconfiguredbymeansof
theirIPaddressesonly.
Examples
AddingaRADIUSserverwithanIPv4addressandapromptedpasskey:
| switch(config)# | radius-server     |                | host 1.1.1.5 | key |     |
| --------------- | ----------------- | -------------- | ------------ | --- | --- |
| Enter the       | RADIUS server     | key: ********* |              |     |     |
| Re-Enter        | the RADIUS server | key:           | *********    |     |     |
DeletingaRADIUSserverwithanIPv4addressandapromptedpasskey:
| switch(config)# | no radius-server  |                | host 1.1.1.5 | key |     |
| --------------- | ----------------- | -------------- | ------------ | --- | --- |
| Enter the       | RADIUS server     | key: ********* |              |     |     |
| Re-Enter        | the RADIUS server | key:           | *********    |     |     |
AddingaRADIUSserverwithanIPv4addressandanamedVRF:
| switch(config)# | radius-server |     | host 1.1.1.1 | vrf mgmt |     |
| --------------- | ------------- | --- | ------------ | -------- | --- |
DeletingaRADIUSserverwithanIPv4addressandanamedVRF:
| switch(config)# | no radius-server |     | host 1.1.1.1 | vrf mgmt |     |
| --------------- | ---------------- | --- | ------------ | -------- | --- |
AddingaRADIUSserverwithanIPv4address,aport,andanamedVRF:
| switch(config)# | radius-server |     | host 1.1.1.2 | port 32 vrf | mgmt |
| --------------- | ------------- | --- | ------------ | ----------- | ---- |
DeletingaRADIUSserverwithanIPv4address,aport,andanamedVRF:
RemoteAAA(TACACS+,RADIUS)commands|110

switch(config)# no radius-server host 1.1.1.2 port 32 vrf mgmt

Adding a RADIUS server with an FQDN, a timeout, port number, and a named VRF:

switch(config)# radius-server host abc.com timeout 15 port 32 vrf vrf_blue

Deleting a RADIUS server with an FQDN, a timeout, port number, and a named VRF:

switch(config)# no radius-server host abc.com timeout 15 port 32 vrf vrf_blue

Adding a RADIUS server with an IPv6 address:

switch(config)# radius-server host 2001:0db8:85a3:0000:0000:8a2e:0370:7334

Deleting a RADIUS server with an IPv6 address:

switch(config)# no radius-server host 2001:0db8:85a3:0000:0000:8a2e:0370:7334

Adding a RADIUS server with tracking enabled and tracking mode is set to dead-only:

switch(config)# radius-server host 1.1.1.1 tracking enable tracking-mode dead-only

Deleting a RADIUS server with tracking enabled and tracking mode is set to dead-only:

switch(config)# no radius-server host 1.1.1.1 tracking enable tracking-mode dead-
only

Adding a RADIUS server with tracking disabled:

switch(config)# radius-server host 1.1.1.1 tracking disable

Deleting a RADIUS server with tracking disabled:

switch(config)# no radius-server host 1.1.1.1 tracking disable

Adding a RADIUS server with an IPv4 address, key, encrypted passkey, number of retries, and VRF name:

switch(config)# radius-server host 1.1.1.6 key ciphertext AQBapStbgHt1X2JlbcEcQl
xbbzWjrFr9UsfH3+00x5Qj0qcQBAAAAJ5WZBQ= retries 3 vrf vrf_red

Deleting a RADIUS server with an IPv4 address, key, encrypted passkey, number of retries, and VRF
name:

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

111

| switch(config)# |     | no  | radius-server |     | host | 1.1.1.6 | key ciphertext |
| --------------- | --- | --- | ------------- | --- | ---- | ------- | -------------- |
AQBapStbgHt1X2JlbcEcQl
| xbbzWjrFr9UsfH3+00x5Qj0qcQBAAAAJ5WZBQ= |     |     |     |     |     | retries | 3 vrf vrf_red |
| -------------------------------------- | --- | --- | --- | --- | --- | ------- | ------------- |
DeletingaRADIUSserverwithanIPv4addressandspecifiedVRF:
| switch(config)# |     | no  | radius-server |     | host | 1.1.1.1 | vrf mgmt |
| --------------- | --- | --- | ------------- | --- | ---- | ------- | -------- |
DeletingaRADIUSserverwithanFQDN,port,andspecifiedVRF:
switch(config)# no radius-server host abc.com port 32 vrf vrf_blue
| Command        | History     |         |         |     |              |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- |
| Release        |             |         |         |     | Modification |     |     |
| 10.07orearlier |             |         |         |     | --           |     |     |
| Command        | Information |         |         |     |              |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| radius-server |     | host |     | secure |     | ipsec |     |
| ------------- | --- | ---- | --- | ------ | --- | ----- | --- |
SyntaxforaRADIUSserverthatusesIPsecforauthentication:
| radius-server   | host               | {<FQDN>   | |   | <IPV4>       | | <IPV6>}      |             |     |
| --------------- | ------------------ | --------- | --- | ------------ | -------------- | ----------- | --- |
| [key [plaintext |                    | <PASSKEY> |     | | ciphertext |                | <PASSKEY>]] |     |
| [timeout        | <TIMEOUT-SECONDS>] |           |     | [port        | <PORT-NUMBER>] |             |     |
[auth-type {pap | chap}] [acct-port <ACCT-PORT>] [retries <RETRY-COUNT>]
[tracking {enable | disable}] [tracking-mode {any | dead-only}] [vrf <VRF-NAME>]
secure ipsec authentication spi <SPI-INDEX> <AUTH-TYPE> <AUTH-KEY-TYPE> [<AUTH-KEY>]
| no radius-server |                    | host      | {<FQDN> | | <IPV4>     |                | | <IPV6>}   |     |
| ---------------- | ------------------ | --------- | ------- | ------------ | -------------- | ----------- | --- |
| [key [plaintext  |                    | <PASSKEY> |         | | ciphertext |                | <PASSKEY>]] |     |
| [timeout         | <TIMEOUT-SECONDS>] |           |         | [port        | <PORT-NUMBER>] |             |     |
[auth-type {pap | chap}] [acct-port <ACCT-PORT>] [retries <RETRY-COUNT>]
[tracking {enable | disable}] [tracking-mode {any | dead-only}] [vrf <VRF-NAME>]
secure ipsec authentication spi <SPI-INDEX><AUTH-TYPE><AUTH-KEY-TYPE> [<AUTH-KEY>]
SyntaxforaRADIUSserverthatusesIPsecforbothauthenticationandencryption:
| radius-server   | host               | {<FQDN>   | |   | <IPV4>       | | <IPV6>}      |             |     |
| --------------- | ------------------ | --------- | --- | ------------ | -------------- | ----------- | --- |
| [key [plaintext |                    | <PASSKEY> |     | | ciphertext |                | <PASSKEY>]] |     |
| [timeout        | <TIMEOUT-SECONDS>] |           |     | [port        | <PORT-NUMBER>] |             |     |
[auth-type {pap | chap}] [acct-port <ACCT-PORT>] [retries <RETRY-COUNT>]
[tracking {enable | disable}] [tracking-mode {any | dead-only}] [vrf <VRF-NAME>]
secure ipsec encryption spi <SPI-INDEX> <AUTH-TYPE> <AUTH-KEY-TYPE>
| [<AUTH-KEY>]     |                    | <ENCRYPT-TYPE> |         | <ENCRYPT-KEY-TYPE> |                |             | [<ENCRYPT-KEY>] |
| ---------------- | ------------------ | -------------- | ------- | ------------------ | -------------- | ----------- | --------------- |
| no radius-server |                    | host           | {<FQDN> | | <IPV4>           |                | | <IPV6>}   |                 |
| [key [plaintext  |                    | <PASSKEY>      |         | | ciphertext       |                | <PASSKEY>]] |                 |
| [timeout         | <TIMEOUT-SECONDS>] |                |         | [port              | <PORT-NUMBER>] |             |                 |
[auth-type {pap | chap}] [acct-port <ACCT-PORT>] [retries <RETRY-COUNT>]
RemoteAAA(TACACS+,RADIUS)commands|112

[tracking {enable | disable}] [tracking-mode {any | dead-only}] [vrf <VRF-NAME>]
secure ipsec encryption spi <SPI-INDEX><AUTH-TYPE><AUTH-KEY-TYPE>
[<AUTH-KEY>] <ENCRYPT-TYPE><ENCRYPT-KEY-TYPE> [<ENCRYPT-KEY>]

Description

Adds a RADIUS server that uses IPsec for enhanced security (authentication and possibly encryption). By
default, the RADIUS server is associated with the server group named radius.

The no form of this command removes a previously added RADIUS (with IPsec) server.

Unless enhanced security with IPsec is required, use the radius-server host command instead.

Parameter

Description

{<FQDN> | <IPV4> | <IPv6>}

key [plaintext
ciphertext

<PASSKEY> |
<PASSKEY>]

Specifies the RADIUS server as:
n <FQDN>: a fully qualified domain name.
n <IPV4>: an IPv4 address.
n <IPV6>: an IPv6 address.

Selects either a plaintext or an encrypted local shared-secret
passkey for the server. As per RFC 2865, shared-secret can be a
mix of alphanumeric and special characters. Plaintext passkeys
are between 1 and 32 alphanumeric and special characters.

NOTE: When key is entered without either sub-parameter,
plaintext passkey prompting occurs upon pressing Enter. Enter
must be pressed immediately after the key parameter without
entering other parameters. The entered passkey characters are
masked with asterisks. When key is omitted, the server uses the
global passkey. This command requires either the global or local
passkey to be set; otherwise the server will not be contacted.
Command radius-server key is available for setting the global
passkey.

timeout

<TIMEOUT-SECONDS>

Specifies the timeout. Range: 1 to 60 seconds. If a timeout is not
specified, the value from the global timeout for RADIUS is used.

port <PORT-NUMBER>

auth-type {pap | chap}

acct-port <ACCT-PORT>

retries <RETRY-COUNT>

tracking {enable | disable}

Specifies the authentication port number. Range: 1 to 65535.
Default: 1812.

Selects either the PAP (the default) or CHAP authentication types.
If this parameter is not specified, the RADIUS global default is
used.

Specifies the UDP accounting port number. Range: 1 to 65535.
Default: 1813.

Specifies the number of retry attempts for contacting the specified
RADIUS server. Range is 0 to 5 attempts. If no retry value is
provided, the default value of 1 is used.

Enables or disables server tracking for the RADIUS server. Tracked
servers are probed at the start of each server tracking interval to
check if they are reachable.
Use command radius-server tracking to configure RADIUS
server tracking globally.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

113

Parameter

Description

tracking-mode {any | dead-only}

vrf <VRF-NAME>

spi

<SPI-INDEX>

<AUTH-TYPE>

<AUTH-KEY-TYPE>

[<AUTH-KEY>]

NOTE: Server tracking uses authentication request and response
packets to determine server reachability status. The server
tracking user name and password are used to form the request
packet which is sent to the server with tracking enabled. Upon
receiving a response to the request packet, the server is
considered to be reachable.

Configures tracking mode for the RADIUS server that has tracking
enabled with the server. The tracking mode is used to monitor the
status of RADIUS server reachability The default tracking mode is
any.
any

Track the RADIUS server irrespective of its server reachability.

dead-only

Track the RADIUS server only when the server is marked as
unreachable.

Specifies the VRF name to be used for communicating with the
server. If no VRF name is provided, the default VRF named
default is used.

Specifies the Security Parameters Index. The SPI is an
identification tag carried in the IPsec AH header. The SPI must be
unique on the switch. Range: 256 to 4294967295.

Specifies the authentication algorithm: md5, sha1, or sha256.

Specifies the authentication key type: plaintext, hex-string,
or ciphertext.

Specifies the authentication key. For <AUTH-TYPE> of
ciphertext, this is the ciphertext string.
For <AUTH-TYPE> of plaintext or hex-string:
n md5 (plaintext): 1 to 16 characters, (hex-string): 2 to 32

hexadecimal digits.

n sha1 (plaintext): 1 to 20 characters, (hex-string): 2 to

40 hexadecimal digits.

n sha256 (plaintext): 1 to 32 characters, (hex-string): 2

to 64 hexadecimal digits.

NOTE: When <AUTH-KEY-TYPE> is not followed by <AUTH-KEY>,
plaintext authentication key prompting occurs upon pressing
Enter. Enter must be pressed immediately after the <AUTH-KEY-
TYPE> parameter without entering other parameters. The entered
authentication key characters are masked with asterisks.

<ENCRYPT-TYPE>

<ENCRYPT-KEY-TYPE>

Specifies the encryption algorithm: 3des, aes, des, or null.

Specifies the encryption key type: plaintext, hex-string, or
ciphertext.

[<ENCRYPT-KEY>]

Specifies the encryption key. For <ENCRYPT-TYPE> of

Remote AAA (TACACS+, RADIUS) commands | 114

Parameter

Description

ciphertext, this is the ciphertext string.
For <ENCRYPT-TYPE> of plaintext or hex-string:
n 3des (plaintext): 24 characters, (hex-string): 48

hexadecimal digits.

n aes (plaintext): 16, 24, or 32 characters, (hex-string):

32, 48, or 64 hexadecimal digits.

n des (plaintext): 8 characters, (hex-string): 16

hexadecimal digits.

NOTE: When <ENCRYPT-KEY-TYPE> is not followed by
<ENCRYPT-KEY>, plaintext encryption key prompting occurs upon
pressing Enter. Enter must be pressed immediately after the
<ENCRYPT-KEY-TYPE> parameter without entering other
parameters. The entered encryption key characters are masked
with asterisks.

Usage

If the fully qualified domain name is provided for the RADIUS server host, a DNS server must be
configured and accessible through the same VRF as mentioned for the server host. This configuration is
required for the resolution of the RADIUS server hostname to its IP address. If a DNS server is not
available for this VRF, the RADIUS servers reachable through this VRF must be configured by means of
their IP addresses only.

Examples

Adding a RADIUS server with an IPv4 address, a plaintext passkey, and IPsec authentication (md5
plaintext).

switch(config)# radius-server host 1.1.1.1 key plaintext 98ab vrf mgmt secure

ipsec authentication spi 261 md5 plaintext 1abc

Deleting a RADIUS server with an IPv4 address, a plaintext passkey, and IPsec authentication (md5
plaintext).

switch(config)# no radius-server host 1.1.1.1 key plaintext 98ab vrf mgmt secure

ipsec authentication spi 261 md5 plaintext 1abc

Adding a RADIUS server with an IPv4 address and a prompted IPsec authentication (md5) plaintext
authentication key.

switch(config)# radius-server host 1.1.1.1
md5
Enter the IPsec authentication key: ********
Re-Enter the IPsec authentication key: ********

secure ipsec authentication spi 261

Deleting a RADIUS server with an IPv4 address and a prompted IPsec authentication (md5) plaintext
authentication key.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

115

switch(config)# no radius-server host 1.1.1.1 secure ipsec authentication spi 261
md5
| Enter the | IPsec | authentication       |     | key: ******** |     |     |     |
| --------- | ----- | -------------------- | --- | ------------- | --- | --- | --- |
| Re-Enter  | the   | IPsec authentication |     | key: ******** |     |     |     |
AddingaRADIUSserverwithanIPv4address,IPsecauthentication(MD5plaintext),andIPsec
encryption(AESplaintext):
| switch(config)# |     | radius-server |     | host 1.1.1.2 | vrf | mgmt secure |     |
| --------------- | --- | ------------- | --- | ------------ | --- | ----------- | --- |
ipsec encryption spi 262 md5 plaintext 9xyz aes plaintext 1234567890abcdef
DeletingaRADIUSserverwithanIPv4address,IPsecauthentication(MD5plaintext),andIPsec
encryption(AESplaintext):
| switch(config)# |     | no radius-server |     | host 1.1.1.2 |     | vrf mgmt | secure |
| --------------- | --- | ---------------- | --- | ------------ | --- | -------- | ------ |
ipsec encryption spi 262 md5 plaintext 9xyz aes plaintext 1234567890abcdef
AddingaRADIUSserverbyprovidinganIPv4addressandIPsecMD5authenticationtype,andthen
respondingtopromptsforthekeysandencryptiontype:
switch(config)# radius-server host 1.1.1.6 secure ipsec encryption spi 262 md5
| Enter the | IPsec | authentication       |      | key: ********        |     |     |     |
| --------- | ----- | -------------------- | ---- | -------------------- | --- | --- | --- |
| Re-Enter  | the   | IPsec authentication |      | key: ********        |     |     |     |
| Enter the | IPsec | encryption           | type | (3des/aes/des/null)? |     | aes |     |
| Enter the | IPsec | encryption           | key: |                      |     |     |     |
********
| Re-Enter | the | IPsec encryption |     | key: ******** |     |     |     |
| -------- | --- | ---------------- | --- | ------------- | --- | --- | --- |
DeletingaRADIUSserverbyprovidinganIPv4addressandIPsecMD5authenticationtype,andthen
respondingtopromptsforthekeysandencryptiontype:
switch(config)# no radius-server host 1.1.1.6 secure ipsec encryption spi 262 md5
| Enter the | IPsec | authentication       |      | key: ********        |     |     |     |
| --------- | ----- | -------------------- | ---- | -------------------- | --- | --- | --- |
| Re-Enter  | the   | IPsec authentication |      | key: ********        |     |     |     |
| Enter the | IPsec | encryption           | type | (3des/aes/des/null)? |     | aes |     |
| Enter the | IPsec | encryption           | key: | ********             |     |     |     |
| Re-Enter  | the   | IPsec encryption     |      | key: ********        |     |     |     |
AddingaRADIUSserverwithanIPv4address,trackingenabled,trackingmode,IPsecauthentication
(MD5plaintext),IPsecencryption(AESplaintext)issettodead-only:
switch(config)# radius-server host 1.1.1.1 tracking enable tracking-mode dead-only
| vrf | mgmt secure | ipsec            | encryption | spi | 262 md5 | plaintext | 9xyz |
| --- | ----------- | ---------------- | ---------- | --- | ------- | --------- | ---- |
| aes | plaintext   | 1234567890abcdef |            |     |         |           |      |
DeletingaRADIUSserverwithanIPv4address,trackingenabled,trackingmode,IPsecauthentication
(MD5plaintext),IPsecencryption(AESplaintext)issettodead-only:
RemoteAAA(TACACS+,RADIUS)commands|116

switch(config)# no radius-server host 1.1.1.1 tracking enable tracking-mode dead-
only
|     | vrf | mgmt secure |                  | ipsec encryption |     | spi 262 | md5 plaintext | 9xyz |
| --- | --- | ----------- | ---------------- | ---------------- | --- | ------- | ------------- | ---- |
|     | aes | plaintext   | 1234567890abcdef |                  |     |         |               |      |
RemovingaRADIUSserver:
|     | switch(config)# |     | no  | radius-server |     | host 1.1.1.1 | vrf mgmt |     |
| --- | --------------- | --- | --- | ------------- | --- | ------------ | -------- | --- |
RemovingtheipsecconfigurationfromaRADIUSserver:
switch(config)# no radius-server host 1.1.1.2 vrf mgmt secure ipsec encryption
| Command        |     | History     |     |         |     |              |     |     |
| -------------- | --- | ----------- | --- | ------- | --- | ------------ | --- | --- |
| Release        |     |             |     |         |     | Modification |     |     |
| 10.07orearlier |     |             |     |         |     | --           |     |     |
| Command        |     | Information |     |         |     |              |     |     |
| Platforms      |     | Command     |     | context |     | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| radius-server |     |     | host | tls | (RadSec) |     |     |     |
| ------------- | --- | --- | ---- | --- | -------- | --- | --- | --- |
radius-server host {<FQDN> | <IPV4> | <IPV6>}tls [timeout <TIMEOUT-SECONDS>] [port <PORT-
NUMBER>][auth-type {pap | chap}] [tracking {enable | disable}] [tracking-mode {any |
dead-
| only}] |     | [vrf <VRF-NAME>] |     |     |     |     |     |     |
| ------ | --- | ---------------- | --- | --- | --- | --- | --- | --- |
no radius-server host {<FQDN> | <IPV4> | <IPV6>}tls [timeout <TIMEOUT-SECONDS>] [port
<PORT-
NUMBER>][auth-type {pap | chap}] [tracking {enable | disable}] [tracking-mode {any |
dead-
| only}] |     | [vrf <VRF-NAME>] |     |     |     |     |     |     |
| ------ | --- | ---------------- | --- | --- | --- | --- | --- | --- |
Description
AddsaRadSecserver.Bydefault,theRADIUSserverisassociatedwiththeservergroupnamedradius.
RadSecisusedtosecurethecommunicationbetweenRADIUSserverandRADIUSclientusingTLS.
ThenoformofthiscommandremovesapreviouslyaddedRadSecserver.
Thesharedkeywillbeaddedasradsecforconnectionestablishment.
| Parameter |     |          |           |     |     | Description                 |     |     |
| --------- | --- | -------- | --------- | --- | --- | --------------------------- | --- | --- |
| {<FQDN>   |     | | <IPV4> | | <IPv6>} |     |     | SpecifiestheRADIUSserveras: |     |     |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 117

Parameter

Description

n <FQDN>: a fully qualified domain name.
n <IPV4>: an IPv4 address.
n <IPV6>: an IPv6 address.

tls

Establishes RADIUS connection over TLS.

timeout

<TIMEOUT-SECONDS>

Specifies the timeout. Range: 1 to 60 seconds. If a timeout is not
specified, the value from the global timeout for RADIUS is used.

port <PORT-NUMBER>

auth-type {pap | chap}

Specifies the authentication port number. Range: 1 to 65535.
Default: 1812.

Selects either the PAP (the default) or CHAP authentication types.
If this parameter is not specified, the RADIUS global default is
used.

acct-port <ACCT-PORT>

Specifies the UDP accounting port number. Range: 1 to 65535.
Default: 1813.

tracking {enable | disable}

tracking-mode {any | dead-only}

vrf <VRF-NAME>

Examples

Enables or disables server tracking for the RADIUS server. Tracked
servers are probed at the start of each server tracking interval to
check if they are reachable.
Use command radius-server tracking to configure RADIUS
server tracking globally.

NOTE: Server tracking uses authentication request and response
packets to determine server reachability status. The server
tracking user name and password are used to form the request
packet which is sent to the server with tracking enabled. Upon
receiving a response to the request packet, the server is
considered to be reachable.

Configures tracking mode for the RADIUS server that has tracking
enabled with the server. The tracking mode is used to monitor the
status of RADIUS server reachability The default tracking mode is
any.
any

Track the RADIUS server irrespective of its server reachability.

dead-only

Track the RADIUS server only when the server is marked as
unreachable.

Specifies the VRF name to be used for communicating with the
server. If no VRF name is provided, the default VRF named
default is used.

Adding a RADIUS server over TLS with an IPv4 address and a named VRF:

switch(config)# radius-server host 1.1.1.1 tls vrf mgmt

Deleting a RADIUS server over TLS with an IPv4 address and a named VRF:

switch(config)# no radius-server host 1.1.1.1 tls vrf mgmt

Remote AAA (TACACS+, RADIUS) commands | 118

AddingaRADIUSserveroverTLSwithanIPv4addressanddefaultport:
| switch(config)# | radius-server |     | host 1.1.1.1 | tls port |
| --------------- | ------------- | --- | ------------ | -------- |
DeletingaRADIUSserveroverTLSwithanIPv4addressanddefaultport:
| switch(config)# | no  | radius-server | host 1.1.1.1 | tls port |
| --------------- | --- | ------------- | ------------ | -------- |
AddingaRADIUSserveroverTLSwithtrackingenabledandtrackingmodeissettodead-only:
switch(config)#
radius-server host 1.1.1.1 tls tracking enable tracking-mode dead-
only
DeletingaRADIUSserveroverTLSwithtrackingenabledandtrackingmodeissettodead-only:
switch(config)# no radius-server host 1.1.1.1 tls tracking enable tracking-mode
dead-only
AddingaRADIUSserveroverTLSwithanIPv4address,aport,andanamedVRF:
switch(config)# radius-server host 1.1.1.2 tls port 32 vrf mgmt
DeletingaRADIUSserveroverTLSwithanIPv4address,aport,andanamedVRF:
switch(config)# no radius-server host 1.1.1.2 tls port 32 vrf mgmt
AddingaRADIUSserveroverTLSwithanIPv6address:
switch(config)# radius-server host 2001:0db8:85a3:0000:0000:8a2e:0370:7334 tls
DeletingaRADIUSserveroverTLSwithanIPv6address:
switch(config)# no radius-server host 2001:0db8:85a3:0000:0000:8a2e:0370:7334 tls
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 119

radius-server host tls port-access
radius-server host {<FQDN> | <IPV4> | <IPV6>} tls port-access {status-server | keep-
alive}
no radius-server host {<FQDN> | <IPV4> | <IPV6>} tls port-access {status-server | keep-
alive}

Description

Configures the type of messages to be sent inside RadSec sessions for port access authentication.
Default message type for port access authentication sessions is status-server.

The no form of this command removes the message type configured for port access authentication
sessions and sets the default, status-server.

Parameter

Description

{<FQDN> | <IPV4> | <IPv6>}

Specifies the RADIUS server as:
n <FQDN>: a fully qualified domain name.
n <IPV4>: an IPv4 address.
n <IPV6>: an IPv6 address.

port-access
{status-server | keep-alive}

Specifies the message type to be used for port access authentication
in RadSec sessions. Following message types are supported:

n status-server: Sets status server message type for

authentication.

n keep-alive: Sets keep-alive message type for authentication.

NOTE: Keep-alive as tracking method and for port access sessions is
recommended in networks where a RadSec server is connected to
more number of RadSec clients. The server requires additional
resources to process status-server and access-request messages
when compared to keep-alive messages. This is because status-server
and access-request messages are RADIUS protocol packets. However,
keep-alive packets are TCP control packets that does not require any
additional resources for processing by the RadSec server.

Examples

Configuring the keep-alive messages for port access authentication in RadSec session on host

1.1.1.1:

switch(config)# radius-server host 1.1.1.1 tls port-access keep-alive

Deleting the message type configured on host 1.1.1.1 for port access authentication session and

setting the method to the default, status-server:

switch(config)# no radius-server host 1.1.1.1 tls port-access status-server

Command History

Remote AAA (TACACS+, RADIUS) commands | 120

| Release   |             |         | Modification                                       |     |
| --------- | ----------- | ------- | -------------------------------------------------- | --- |
| 10.10     |             |         | Commandintroduced                                  |     |
| Command   | Information |         |                                                    |     |
| Platforms | Command     | context | Authority                                          |     |
|           | config      |         | Administratorsorlocalusergroupmemberswithexecution |     |
rightsforthiscommand.
| radius-server |     | host tls | tracking-method |     |
| ------------- | --- | -------- | --------------- | --- |
radius-server host {<FQDN> | <IPV4> | <IPV6>} tls tracking-method {status-server | keep-
| alive | | access-request} |     |     |     |
| ------- | --------------- | --- | --- | --- |
no radius-server host {<FQDN> | <IPV4> | <IPV6>} tls tracking-method {status-server |
| keep-alive | | access-request} |     |     |     |
| ---------- | ----------------- | --- | --- | --- |
Description
ConfiguresthetrackingmethodtobeusedforRADIUSservertracking.RADIUSservertrackingmustbe
configuredforenablingthetrackingmethod.Defaulttrackingmethodisaccess-request.
Thenoformofthiscommandsetsthetrackingmethodtothedefaultoption,access-request.
| Parameter |          |           |     | Description                 |
| --------- | -------- | --------- | --- | --------------------------- |
| {<FQDN>   | | <IPV4> | | <IPv6>} |     | SpecifiestheRADIUSserveras: |
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
n <IPV6>:anIPv6address.
tracking-method
SpecifiesthetrackingmethodforRadSec
{status-server | keep-alive | access-request} tracking.Followingmethodsaresupported:
status-server:Statusserverresponses
n
areusedtoupdatethereachabilitystatusof
theRadSecserver.
n keep-alive:Serversocketstatusisverified
toupdatethereachabilitystatusofthe
RadSecserver.
NOTE:keep-aliveastrackingmethodand
forportaccesssessionsisrecommendedin
networkswhereaRadSecserveris
connectedtomorenumberofRadSec
clients.Theserverrequiresadditional
resourcestoprocessstatus-serverand
access-requestmessageswhencompared
tokeep-alivemessages.Thisisbecause
status-serverandaccess-request
messagesareRADIUSprotocolpackets.
However,keep-alive packetsareTCP
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 121

Parameter

Description

control packets that does not require any
additional resources for processing by the
RadSec server.

n access-request: Access response

messages are used to update the reachability

status of the RadSec server.

Usage

n If the network has a RADIUS proxy, then it is recommended to use the access-request tracking

method to track the RadSec server.

n If keep-alive is the tracking method, then make sure to check whether the server has the capability

to treat the keep-alive messages sent in RadSec sessions as valid RadSec messages to keep the
session active.

Examples

Configuring the RADIUS server tracking method on host 1.1.1.1:

switch(config)# radius-server host 1.1.1.1 tls tracking-method status-server

Deleting the RADIUS server tracking method on host 1.1.1.1 and setting the method to the default,

access-request:

switch(config)# no radius-server host 1.1.1.1 tls tracking-method access-request

Command History

Release

10.10

Command Information

Modification

Command introduced

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution
rights for this command.

radius-server key
radius-server key [plaintext <GLOBAL-PASSKEY> | ciphertext <GLOBAL-PASSKEY>]
no radius-server key [plaintext <GLOBAL-PASSKEY> | ciphertext <GLOBAL-PASSKEY>]

Description

Creates or modifies a RADIUS global passkey. The RADIUS global passkey is used as a shared-secret for
encrypting the communication between all RADIUS servers and the switch. The RADIUS global passkey

Remote AAA (TACACS+, RADIUS) commands | 122

isrequiredforauthenticationunlesslocalpasskeyshavebeenset.Bydefault,theRADIUSglobal
passkeyisempty.Iftheadministratorhasnotsetthiskey,theswitchwillnotbeabletoperformRADIUS
authentication.Theswitchwillinsteadrelyontheauthenticationmechanismconfiguredwithaaa
| authentication | login. |     |     |     |     |     |
| -------------- | ------ | --- | --- | --- | --- | --- |
Whenthiscommandisenteredwithoutparameters,plaintextpasskeypromptingoccursuponpressingEnter.
Theenteredpasskeycharactersaremaskedwithasterisks.
Thenoformofthecommandremovestheglobalpasskey.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
plaintext <GLOBAL-PASSKEY> SpecifiestheRADIUSglobalpasskeyinplaintextformatwitha
lengthof1to31characters.AsperRFC2865,ashared-secretcan
beamixofalphanumericandspecialcharacters.
ciphertext <GLOBAL-PASSKEY> SpecifiestheRADIUSglobalpasskeyinencryptedformat.
Examples
Addingtheglobalpasskey:
| switch(config)# |     | radius-server |     |     | key plaintext | mypasskey123 |
| --------------- | --- | ------------- | --- | --- | ------------- | ------------ |
Addingtheglobalpasskeywithprompting:
| switch(config)# |        | radius-server |        |                | key       |     |
| --------------- | ------ | ------------- | ------ | -------------- | --------- | --- |
| Enter the       | RADIUS | server        |        | key: ********* |           |     |
| Re-Enter        | the    | RADIUS        | server | key:           | ********* |     |
Removingtheglobalpasskey:
| switch(config)# |             | no  | radius-server |     | key          |     |
| --------------- | ----------- | --- | ------------- | --- | ------------ | --- |
| Command         | History     |     |               |     |              |     |
| Release         |             |     |               |     | Modification |     |
| 10.07orearlier  |             |     |               |     | --           |     |
| Command         | Information |     |               |     |              |     |
| Platforms       | Command     |     | context       |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| radius-server |     | retries |     |     |     |     |
| ------------- | --- | ------- | --- | --- | --- | --- |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 123

| radius-server    | retries |         | <0-5> |     |     |
| ---------------- | ------- | ------- | ----- | --- | --- |
| no radius-server |         | retries | <0-5> |     |     |
Description
SetsatthegloballevelthenumberofretriestheswitchmakesbeforeconcludingthattheRADIUS
serverisunreachable.
Youcanoverridethissettingwithafine-grainedperRADIUSserverretriesconfiguration.
ThenoformofthiscommandresetstheRADIUSglobalretriestothedefaultretriesvalueof1.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
retries <0-5> SpecifiesthenumberofretryattemptsforcontactingRADIUS
servers.Rangeis0to5retries.
Example
| switch(config)# |             | radius-server |         | retries | 3            |
| --------------- | ----------- | ------------- | ------- | ------- | ------------ |
| Command         | History     |               |         |         |              |
| Release         |             |               |         |         | Modification |
| 10.07orearlier  |             |               |         |         | --           |
| Command         | Information |               |         |         |              |
| Platforms       | Command     |               | context |         | Authority    |
Allplatforms config OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| radius-server    |               | status-server |     |          | interval   |
| ---------------- | ------------- | ------------- | --- | -------- | ---------- |
| radius-server    | status-server |               |     | interval | <10-86400> |
| no radius-server |               | status-server |     | interval | <10-86400> |
Description
ConfiguresthetimeintervalinsecondstosendthestatusserverrequeststotheRADIUSserver.
Thenoformofthiscommandconfiguresthedefaulttimeinterval,300seconds.
| Parameter |     | Description |     |     |     |
| --------- | --- | ----------- | --- | --- | --- |
<10-86400>
Specifiesthestatusservertimeintervalinseconds.Default: 300.
Examples
Configuringthestatusservertimeintervalof200seconds:
RemoteAAA(TACACS+,RADIUS)commands|124

| switch(config)# | radius-server |     | status-server | interval 200 |
| --------------- | ------------- | --- | ------------- | ------------ |
Resettingthestatusservertimeintervaltothedefault,300seconds:
| switch(config)#     | no      | radius-server | status-server     | interval 200 |
| ------------------- | ------- | ------------- | ----------------- | ------------ |
| Command History     |         |               |                   |              |
| Release             |         |               | Modification      |              |
| 10.10               |         |               | Commandintroduced |              |
| Command Information |         |               |                   |              |
| Platforms           | Command | context       | Authority         |              |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| radius-server    | timeout |          |     |     |
| ---------------- | ------- | -------- | --- | --- |
| radius-server    | timeout | [<1-60>] |     |     |
| no radius-server | timeout | [<1-60>] |     |     |
Description
SpecifiesthenumberofsecondstowaitforaresponsefromtheRADIUSserverbeforetryingthenext
RADIUSserver.Ifavalueisnotspecified,adefaultvalueof5secondsisused.Youcanoverridethis
valuewithafine-grainedperservertimeoutconfiguredforindividualservers.
ThenoformofthiscommandresetstheRADIUSglobalauthenticationtimeouttothedefaultof5
seconds.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
timeout <1-60> Specifiesthetimeoutintervalof1to60seconds.Default:5
seconds.
Examples
SettingtheRADIUSservertimeout:
| switch(config)# | radius-server |     | timeout 10 |     |
| --------------- | ------------- | --- | ---------- | --- |
ResettingthetimeoutfortheRADIUSservertothedefault:
| switch(config)# | no  | radius-server | timeout |     |
| --------------- | --- | ------------- | ------- | --- |
| Command History |     |               |         |     |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 125

| Release        |             |     |         | Modification |     |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| radius-server    |     | tls         | timeout  | (RadSec) |     |
| ---------------- | --- | ----------- | -------- | -------- | --- |
| radius-server    | tls | timeout     | [<1-60>] |          |     |
| no radius-server |     | tls timeout | [<1-60>] |          |     |
Description
SpecifiesthenumberofsecondstowaitforaresponsefromtheRadSecserverbeforetryingthenext
RADIUSorRadSecserver.Ifavalueisnotspecified,adefaultvalueof5secondsisused.Youcan
overridethisvaluewithafine-grainedperservertimeoutconfiguredforindividualservers.
ThenoformofthiscommandresetstheRadSecglobalauthenticationtimeouttothedefaultof5
seconds.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
timeout <1-60> Specifiesthetimeoutintervalof1to60seconds.Default:5
seconds.
Examples
SettingtheRadSecservertimeout:
| switch(config)# |     | radius-server |     | tls timeout | 10  |
| --------------- | --- | ------------- | --- | ----------- | --- |
ResettingthetimeoutfortheRadSectothedefault:
| switch(config)# |             | no  | radius-server | tls timeout  |     |
| --------------- | ----------- | --- | ------------- | ------------ | --- |
| Command         | History     |     |               |              |     |
| Release         |             |     |               | Modification |     |
| Command         | Information |     |               |              |     |
| Platforms       | Command     |     | context       | Authority    |     |
config
allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
RemoteAAA(TACACS+,RADIUS)commands|126

| radius-server    |            | tracking   |              |     |              |
| ---------------- | ---------- | ---------- | ------------ | --- | ------------ |
| radius-server    | tracking   | interval   | <INTERVAL>   |     |              |
| no radius-server | tracking   | interval   |              |     |              |
| radius-server    | tracking   | retries    | <RETRIES>    |     |              |
| no radius-server | tracking   | retries    |              |     |              |
| radius-server    | tracking   | user-name  | <NAME>       |     |              |
| [password        | [plaintext | <PASSWORD> | | ciphertext |     | <PASSWORD>]] |
| no radius-server | tracking   | user-name  | <NAME>       |     |              |
| [password        | [plaintext | <PASSWORD> | | ciphertext |     | <PASSWORD>]] |
Description
ConfiguresRADIUSservertrackingsettingsgloballyforallconfiguredRADIUSserversthathavetracking
| enabledwiththeradius-server |     |     | hostcommandonindividualservers. |     |     |
| --------------------------- | --- | --- | ------------------------------- | --- | --- |
Thenoformofthecommandremovesthespecifiedconfiguration,revertingittoitsdefault.Theno
formwithuser-namealsoclearsthepassword(resetsittoempty).
| Parameter |            |     |     | Description |     |
| --------- | ---------- | --- | --- | ----------- | --- |
| interval  | <INTERVAL> |     |     |             |     |
Specifiesthetimeinterval,inseconds,towaitbefore
checkingtheserverreachabilitystatus.Default:300.Range
60to84600.
retries <RETRIES> Specifiesthenumberofserverretries.Default:Global
RADIUSretries.Range:0to5.
user-name <NAME> Specifiestheusername(andoptionallyapassword)tobe
[password [plaintext <PASSWORD> | usedforserverchecking.Thedefaultusernameisradius-
| ciphertext | <PASSWORD>]] |     |     | tracking-userwithanemptypassword. |     |
| ---------- | ------------ | --- | --- | --------------------------------- | --- |
Thepasswordisoptionalandmaybeenteredasplaintext
orpastedinasciphertext.Theplaintextpasswordisvisible
ascleartextwhenenteredbutisencryptedthereafter.
Commandhistorydoesshowthepasswordascleartext.
NOTE:Whenpasswordisenteredwithoutafollowingsub-
parameter,plaintextpasswordpromptingoccursupon
pressingEnter.Theenteredpasswordcharactersaremasked
withasterisks.
NOTE:Theuserdoesnothavetobeconfiguredonthe
server.Servertrackingcanstillbeperformedwithauser
whichisnotconfiguredontheserverbecauseauthentication
failureontheserverachievesconfirmationthattheserveris
reachable.
NOTE:Servertrackingusesauthenticationrequestand
responsepacketstodetermineserverreachabilitystatus.The
servertrackingusernameandpasswordareusedtoform
therequestpacketwhichissenttotheserverwithtracking
enabled.Uponreceivingaresponsetotherequestpacket,
theserverisconsideredtobereachable.
Examples
Configuringatrackingintervalof120seconds:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 127

| switch(config)# |     | radius-server |     |     | tracking interval |     | 120 |
| --------------- | --- | ------------- | --- | --- | ----------------- | --- | --- |
Revertingthetrackingintervaltoitsdefaultof300seconds:
| switch(config)# |     | no  | radius-server |     | tracking | interval |     |
| --------------- | --- | --- | ------------- | --- | -------- | -------- | --- |
Configuringthreeretries:
| switch(config)# |     | radius-server |     |     | tracking retries |     | 3   |
| --------------- | --- | ------------- | --- | --- | ---------------- | --- | --- |
Configuringuserradius-trackerwithaplaintextpassword.
switch(config)# radius-server tracking user-name radius-tracker
| password |     | plaintext | track$1 |     |     |     |     |
| -------- | --- | --------- | ------- | --- | --- | --- | --- |
Configuringuserradius-trackerwithapromptedplaintextpassword.
switch(config)# radius-server tracking user-name radius-tracker password
| Enter the | RADIUS | server |        | tracking | password: | ******* |         |
| --------- | ------ | ------ | ------ | -------- | --------- | ------- | ------- |
| Re-Enter  | the    | RADIUS | server | tracking | password: |         | ******* |
Revertingthetrackingusernametoitsdefaultofradius-tracking-user:
| switch(config)# |             | no  | radius-server |     | tracking     | user-name |     |
| --------------- | ----------- | --- | ------------- | --- | ------------ | --------- | --- |
| Command         | History     |     |               |     |              |           |     |
| Release         |             |     |               |     | Modification |           |     |
| 10.07orearlier  |             |     |               |     | --           |           |     |
| Command         | Information |     |               |     |              |           |     |
| Platforms       | Command     |     | context       |     | Authority    |           |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
server
server {<FQDN> | <IPV4> | <IPV6>} [tls] [port <PORT-NUMBER>] [vrf <VRF-NAME>]
no server {<FQDN> | <IPV4> | <IPV6>} [tls] [port <PORT-NUMBER>] [vrf <VRF-NAME>]
Description
AddsaTACACS+/RADIUSservertoaserver-group.OnlytheconfiguredTACACS+/RADIUSserversare
allowedtobeaddedwithintheservergroup.Ifthesameservernameexistswithmultipleportsor
multipleVRFs,specifytheservername,port,andVRFwhenaddingtheservertotheserver-group.
ThenoformofthiscommandremovesaTACACS+/RADIUSserverfromaserver-group.
RemoteAAA(TACACS+,RADIUS)commands|128

| Parameter |          |           |     | Description                 |     |
| --------- | -------- | --------- | --- | --------------------------- | --- |
| {<FQDN>   | | <IPV4> | | <IPv6>} |     | SpecifiestheRADIUSserveras: |     |
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
n <IPV6>:anIPv6address.
| tls |     |     |     | SpecifiestheTLSprotectionfortheRADIUSserver. |     |
| --- | --- | --- | --- | -------------------------------------------- | --- |
IfTLSisconfiguredwithoutaportnumber,thesystemsearches
theRADIUSserverbyhostnameandsetsthedefault
authenticationport(2083).Groupserverpriorityisassignedbased
onthesequenceinwhichtheserversareadded.
port <PORT-NUMBER> Specifiestheauthenticationportnumber.Range:1to65535.
DefaultTACACS+(TCP):49,RADIUS(UDP):1812andRadSec:2083.
Ifaportnumberisnotprovided,thesystemsearchesthe
TACACS+/RADIUSserverbyhostnameandsetsthedefault
authenticationport.Groupserverpriorityisassignedbasedon
thesequenceinwhichtheserversareadded.
vrf <VRF-NAME>
SpecifiestheVRFnametobeusedforcommunicatingwiththe
server.IfnoVRFnameisprovided,thedefaultVRFnamed
defaultisused.
Examples
AddingaservertoTACACS+servergroupsg1byprovidinganIPv4address,portnumber,andVRF
name:
| switch(config)#    |     | aaa group | server  | tacacs sg1  |         |
| ------------------ | --- | --------- | ------- | ----------- | ------- |
| switch(config-sg)# |     | server    | 1.1.1.2 | port 32 vrf | default |
AddingaservertoTACACS+servergroupsg2byprovidinganIPv6addressanddefaultVRF:
| switch(config)# |     | aaa group | server | tacacs sg2 |     |
| --------------- | --- | --------- | ------ | ---------- | --- |
switch(config-sg)# server 2001:0db8:85a3:0000:0000:8a2e:0370:7334 vrf default
AddingaservertoRADIUSservergroupsg3byprovidinganIPv4address,portnumber,andVRFname:
| switch(config)#    |     | aaa group | server  | radius sg3  |         |
| ------------------ | --- | --------- | ------- | ----------- | ------- |
| switch(config-sg)# |     | server    | 1.1.1.5 | port 12 vrf | default |
AddingaservertoRADIUSservergroupsg3withTLSprotectionbyprovidinganIPv4address,port
number,andVRFname:
| switch(config)#    |     | aaa group | server  | radius sg3 |                |
| ------------------ | --- | --------- | ------- | ---------- | -------------- |
| switch(config-sg)# |     | server    | 1.1.1.5 | tls port   | 12 vrf default |
AddingaservertoRADIUSservergroupsg4byprovidinganIPv6addressanddefaultVRF:
| switch(config)# |     | aaa group | server | radius sg4 |     |
| --------------- | --- | --------- | ------ | ---------- | --- |
switch(config-sg)# server 2001:0db8:85a3:0000:0000:8a2e:0371:7334 vrf default
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 129

AddingaservertoRADIUSservergroupsg4byprovidinganIPv4address,portnumber,andVRFname:
| switch(config)#    |     | aaa group | server  | radius | sg4    |         |     |
| ------------------ | --- | --------- | ------- | ------ | ------ | ------- | --- |
| switch(config-sg)# |     | server    | 1.1.1.6 | port   | 32 vrf | vrf_red |     |
SpecifyinganIPv4addresswhenremovingaTACACS+serverfromservergroupsg1:
| switch(config)#    |     | aaa group | server  | tacacs | sg1     |             |     |
| ------------------ | --- | --------- | ------- | ------ | ------- | ----------- | --- |
| switch(config-sg)# |     | no server | 1.1.1.2 |        | port 12 | vrf default |     |
SpecifyinganIPv6addresswhenremovingaTACACS+serverfromservergroupsg2withthedefault
VRF:
| switch(config)# |     | aaa group | server | tacacs | sg2 |     |     |
| --------------- | --- | --------- | ------ | ------ | --- | --- | --- |
switch(config-sg)#
|                     |         | no server | 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |              |     |     | vrf default |
| ------------------- | ------- | --------- | --------------------------------------- | ------------ | --- | --- | ----------- |
| Command History     |         |           |                                         |              |     |     |             |
| Release             |         |           |                                         | Modification |     |     |             |
| 10.07orearlier      |         |           |                                         | --           |     |     |             |
| Command Information |         |           |                                         |              |     |     |             |
| Platforms           | Command | context   |                                         | Authority    |     |     |             |
Allplatforms config-sg Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show aaa            | accounting |            |     |     |     |     |     |
| ------------------- | ---------- | ---------- | --- | --- | --- | --- | --- |
| show aaa accounting |            | [vsx-peer] |     |     |     |     |     |
Description
Showstheaccountingconfigurationperconnectiontype(channel).
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ConfiguringandthenshowingtheaccountingsequenceforTACACS+groupsandlocal:
switch(config)# aaa accounting all default start-stop group tg1 tg2 tacacs local
switch(config)# aaa accounting all ssh start-stop group tg1 tg2
switch(config)# aaa accounting all console start-stop group tg4 tacacs local
RemoteAAA(TACACS+,RADIUS)commands|130

switch(config)# aaa accounting all https-server start-stop local group tacacs tg3
switch(config)#
exit
| switch# | show aaa accounting |     |     |
| ------- | ------------------- | --- | --- |
AAA Accounting:
| Accounting | Type        |          | : all        |
| ---------- | ----------- | -------- | ------------ |
| Accounting | Mode        |          | : start-stop |
| Accounting | for default | channel: |              |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |
| ---------- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
tg1 | 0
tg2 | 1
tacacs | 2
local | 3
---------------------------------------------------------------------------------
| Accounting | for ssh channel: |     |     |
| ---------- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |
| ---------- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
tg1 | 0
tg2 | 1
---------------------------------------------------------------------------------
| Accounting | for console | channel: |     |
| ---------- | ----------- | -------- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |
| ---------- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
tg4 | 0
tacacs | 1
local | 2
---------------------------------------------------------------------------------
| Accounting | for https-server | channel: |     |
| ---------- | ---------------- | -------- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |
| ---------- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
local | 0
tacacs | 1
tg3 | 2
---------------------------------------------------------------------------------
ConfiguringandthenshowingtheaccountingsequenceforRADIUSgroupsandlocal:
switch(config)# aaa accounting all default start-stop group rg1 rg2 radius local
switch(config)# aaa accounting all console start-stop group rg4 radius local
| switch(config)# | exit                |     |     |
| --------------- | ------------------- | --- | --- |
| switch#         | show aaa accounting |     |     |
AAA Accounting:
| Accounting | Type        |          | : all        |
| ---------- | ----------- | -------- | ------------ |
| Accounting | Mode        |          | : start-stop |
| Accounting | for default | channel: |              |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |
| ---------- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
rg1 | 0
rg2 | 1
radius | 2
local | 3
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 131

---------------------------------------------------------------------------------
| Accounting | for console | channel: |     |     |     |
| ---------- | ----------- | -------- | --- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP | PRIORITY |     |
| ---------- | --- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| tg4    |     |     | | 0 |     |     |
| ------ | --- | --- | --- | --- | --- |
| radius |     |     | | 1 |     |     |
| local  |     |     | | 2 |     |     |
---------------------------------------------------------------------------------
Configuringandthenshowingonlylocalaccountingfordefault:
| switch(config)# | aaa                 | accounting | all default | start-stop | local |
| --------------- | ------------------- | ---------- | ----------- | ---------- | ----- |
| switch(config)# | exit                |            |             |            |       |
| switch#         | show aaa accounting |            |             |            |       |
AAA Accounting:
| Accounting | Type        |          |     | : all        |     |
| ---------- | ----------- | -------- | --- | ------------ | --- |
| Accounting | Mode        |          |     | : start-stop |     |
| Accounting | for default | channel: |     |              |     |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP | PRIORITY |     |
| ---------- | --- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| local |     |     | | 0 |     |     |
| ----- | --- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show aaa                | authentication |            |     |     |     |
| ----------------------- | -------------- | ---------- | --- | --- | --- |
| show aaa authentication |                | [vsx-peer] |     |     |     |
Description
Showstheauthenticationconfigurationperconnectiontype(channel).
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
RemoteAAA(TACACS+,RADIUS)commands|132

Example
ConfiguringTACACS+authenticationsequencesandthenshowingtheconfigurationperconnection
type(channel):
switch(config)# aaa authentication login default group tg1 tg2 tg3 tg4 tacacs
local
| switch(config)# |     | aaa authentication |     | login ssh | group tg1 | tg2 |
| --------------- | --- | ------------------ | --- | --------- | --------- | --- |
switch(config)#
|     |     | aaa authentication |     | login console | group | tg4 tacacs local |
| --- | --- | ------------------ | --- | ------------- | ----- | ---------------- |
switch(config)# aaa authentication login https-server local group tacacs tg3
| switch(config)# |     | exit           |     |     |     |     |
| --------------- | --- | -------------- | --- | --- | --- | --- |
| switch# show    | aaa | authentication |     |     |     |     |
AAA Authentication:
| Fail-through     |          |         | :        | Enabled |     |     |
| ---------------- | -------- | ------- | -------- | ------- | --- | --- |
| Limit Login      | Attempts |         | :        | Not set |     |     |
| Lockout Time     |          |         | :        | 300     |     |     |
| Minimum Password |          | Length  | :        | Not set |     |     |
| Authentication   | for      | default | channel: |         |     |     |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP PRIORITY |     |     |
| ---------- | --- | --- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| tg1    |     |     |     | | 0 |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
| tg2    |     |     |     | | 1 |     |     |
| tg3    |     |     |     | | 2 |     |     |
| tg4    |     |     |     | | 3 |     |     |
| tacacs |     |     |     | | 4 |     |     |
| local  |     |     |     | | 5 |     |     |
---------------------------------------------------------------------------------
| Authentication | for | ssh channel: |     |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP PRIORITY |     |     |
| ---------- | --- | --- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| tg1 |     |     |     | | 0 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| tg2 |     |     |     | | 1 |     |     |
---------------------------------------------------------------------------------
| Authentication | for | console | channel: |     |     |     |
| -------------- | --- | ------- | -------- | --- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP PRIORITY |     |     |
| ---------- | --- | --- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| tg4    |     |     |     | | 0 |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
| tacacs |     |     |     | | 1 |     |     |
| local  |     |     |     | | 2 |     |     |
---------------------------------------------------------------------------------
| Authentication | for | https-server |     | channel: |     |     |
| -------------- | --- | ------------ | --- | -------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP PRIORITY |     |     |
| ---------- | --- | --- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| local  |     |     |     | | 0 |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
| tacacs |     |     |     | | 1 |     |     |
| tg3    |     |     |     | | 2 |     |     |
---------------------------------------------------------------------------------
ConfiguringRADIUSauthenticationsequencesandthenshowingtheconfigurationperconnectiontype
(channel):
switch(config)# aaa authentication login default group rg1 rg2 rg3 rg4 radius
local
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 133

switch(config)# aaa authentication login console group rg4 radius local
switch(config)#
exit
| switch# show | aaa authentication |     |     |     |
| ------------ | ------------------ | --- | --- | --- |
AAA Authentication:
| Fail-through     |             | : Enabled |     |     |
| ---------------- | ----------- | --------- | --- | --- |
| Limit Login      | Attempts    | : Not     | set |     |
| Lockout Time     |             | : 300     |     |     |
| Minimum Password | Length      | : Not     | set |     |
| Authentication   | for default | channel:  |     |     |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |     |
| ---------- | --- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
| rg1    |     |     | | 0 |     |
| ------ | --- | --- | --- | --- |
| rg2    |     |     | | 1 |     |
| rg3    |     |     | | 2 |     |
| rg4    |     |     | | 3 |     |
| radius |     |     | | 4 |     |
| local  |     |     | | 5 |     |
---------------------------------------------------------------------------------
| Authentication | for console | channel: |     |     |
| -------------- | ----------- | -------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |     |
| ---------- | --- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
| rg4    |     |     | | 0 |     |
| ------ | --- | --- | --- | --- |
| radius |     |     | | 1 |     |
| local  |     |     | | 2 |     |
---------------------------------------------------------------------------------
Configuringonlydefaultauthenticationandthenshowingthedefaultconnectiontype(channel):
switch(config)#
|                 | aaa authentication |     | login default | local |
| --------------- | ------------------ | --- | ------------- | ----- |
| switch(config)# | exit               |     |               |       |
| switch# show    | aaa authentication |     |               |       |
AAA Authentication:
| Fail-through     |             |          | : Disabled |     |
| ---------------- | ----------- | -------- | ---------- | --- |
| Limit Login      | Attempts    |          | : Not      | set |
| Lockout Time     |             |          | : 300      |     |
| Minimum Password | Length      |          | : Not      | set |
| Authentication   | for default | channel: |            |     |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |     |
| ---------- | --- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
| local |     |     | | 0 |     |
| ----- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Command History     |     |     |              |     |
| ------------------- | --- | --- | ------------ | --- |
| Release             |     |     | Modification |     |
| 10.07orearlier      |     |     | --           |     |
| Command Information |     |     |              |     |
RemoteAAA(TACACS+,RADIUS)commands|134

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show aaa               | authorization |            |     |
| ---------------------- | ------------- | ---------- | --- |
| show aaa authorization |               | [vsx-peer] |     |
Description
Showstheauthorizationconfigurationperconnectiontype(channel).
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Configuringandthenshowingtheauthorizationsequencefordefaultandconsoleconnectiontypes
(channels):
switch(config)# aaa authorization commands default group tg1 tacacs none
All commands will fail if none of the servers in the group list are reachable.
| Continue | (y/n)? y |     |     |
| -------- | -------- | --- | --- |
switch(config)#
switch(config)# aaa authorization commands console group tg1 tg2 tacacs none
All commands will fail if none of the servers in the group list are reachable.
| Continue        | (y/n)? y |     |     |
| --------------- | -------- | --- | --- |
| switch(config)# | exit     |     |     |
switch#
| switch# show  | aaa authorization |          |     |
| ------------- | ----------------- | -------- | --- |
| Authorization | for default       | channel: |     |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| tg1    |     |     | | 0 |
| ------ | --- | --- | --- |
| tacacs |     |     | | 1 |
| none   |     |     | | 2 |
---------------------------------------------------------------------------------
| Authorization | for console | channel: |     |
| ------------- | ----------- | -------- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| tg1    |     |     | | 0 |
| ------ | --- | --- | --- |
| tg2    |     |     | | 1 |
| tacacs |     |     | | 2 |
| none   |     |     | | 3 |
---------------------------------------------------------------------------------
| Command History |     |     |     |
| --------------- | --- | --- | --- |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 135

| Release             |         |         | Modification |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show aaa               | server-groups |         |                      |     |     |
| ---------------------- | ------------- | ------- | -------------------- | --- | --- |
| show aaa server-groups |               | [tacacs | | radius] [vsx-peer] |     |     |
Description
ShowsTACACS+andRADIUSAAAservergroupinformationforallservertypesorforthespecified
servertype.
| Parameter |     |     | Description                                  |     |     |
| --------- | --- | --- | -------------------------------------------- | --- | --- |
| tacacs    |     |     | NarrowsthecommandoutputtoonlyTACACS+servers. |     |     |
| radius    |     |     | NarrowsthecommandoutputtoonlyRADIUSservers.  |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
ShowingallAAAservergroupinformation:
| switch# show | aaa       | server-groups |         |     |     |
| ------------ | --------- | ------------- | ------- | --- | --- |
| ******* AAA  | Mechanism | TACACS+       | ******* |     |     |
--------------------------------------------------------------------------------
| GROUP NAME |     | | SERVER | NAME | | PORT | VRF | | PRIORITY |
| ---------- | --- | -------- | ---- | ------------ | ---------- |
--------------------------------------------------------------------------------
| sg2 |     | | 2001:0db8:85a3:0000:0000:8a2e: |     |                |     |
| --- | --- | -------------------------------- | --- | -------------- | --- |
|     |     | 0370:7334                        |     | | 49 | default | | 1 |
--------------------------------------------------------------------------------
| sg1 |     | | 1.1.1.2 |     | | 12 | mgmt | | 1 |
| --- | --- | --------- | --- | ----------- | --- |
--------------------------------------------------------------------------------
| tacacs (default) |     | | FQDN.com                       |     | | 32 | mgmt      | | 1 |
| ---------------- | --- | -------------------------------- | --- | ---------------- | --- |
| tacacs (default) |     | | 1.1.1.1                        |     | | 49 | mgmt      | | 2 |
| tacacs (default) |     | | 1.1.1.2                        |     | | 12 | mgmt      | | 3 |
| tacacs (default) |     | | abc.com                        |     | | 32 | vrf_red   | | 4 |
| tacacs (default) |     | | 2001:0db8:85a3:0000:0000:8a2e: |     |                  |     |
|                  |     | 0370:7334                        |     | | 49 | default   | | 5 |
| tacacs (default) |     | | 1.1.1.3                        |     | | 32 | vrf_blue| | 6   |
--------------------------------------------------------------------------------
| ******* AAA | Mechanism | RADIUS | ******* |     |     |
| ----------- | --------- | ------ | ------- | --- | --- |
RemoteAAA(TACACS+,RADIUS)commands|136

--------------------------------------------------------------------------------
| GROUP NAME | |   | SERVER NAME | | PORT | VRF | | PRIORITY |
| ---------- | --- | ----------- | ------------ | ---------- |
--------------------------------------------------------------------------------
| sg4 | |   | 2001:0db8:85a3:0000:0000:8a2e: |                  |     |
| --- | --- | ------------------------------ | ---------------- | --- |
|     |     | 0370:7334                      | | 1812 | default | | 1 |
--------------------------------------------------------------------------------
| sg3 | |   | 1.1.1.5 | | 12 | mgmt | | 1 |
| --- | --- | ------- | ----------- | --- |
--------------------------------------------------------------------------------
| radius (default) | |   | 1.1.1.4                        | | 1812 | mgmt    | | 1 |
| ---------------- | --- | ------------------------------ | ---------------- | --- |
| radius (default) | |   | 1.1.1.5                        | | 12 | mgmt      | | 2 |
| radius (default) | |   | abc1.com                       | | 32 | mgmt      | | 3 |
| radius (default) | |   | 2001:0db8:85a3:0000:0000:8a2e: |                  |     |
|                  |     | 0370:7334                      | | 1812 | default | | 4 |
| radius (default) | |   | 1.1.1.6                        | | 32 | vrf_red   | | 5 |
| radius (default) | |   | 1.1.1.7                        | | 32 | vrf_blue| | 6   |
--------------------------------------------------------------------------------
ShowingTACACS+servergroupinformation:
| switch# show | aaa server-groups | tacacs          |     |     |
| ------------ | ----------------- | --------------- | --- | --- |
| ******* AAA  | Mechanism         | TACACS+ ******* |     |     |
--------------------------------------------------------------------------------
| GROUP NAME | |   | SERVER NAME | | PORT | VRF | | PRIORITY |
| ---------- | --- | ----------- | ------------ | ---------- |
--------------------------------------------------------------------------------
| sg2 | |   | 2001:0db8:85a3:0000:0000:8a2e: |                |     |
| --- | --- | ------------------------------ | -------------- | --- |
|     |     | 0370:7334                      | | 49 | default | | 1 |
--------------------------------------------------------------------------------
| sg1 | |   | 1.1.1.2 | | 12 | mgmt | | 1 |
| --- | --- | ------- | ----------- | --- |
--------------------------------------------------------------------------------
| tacacs (default) | |   | FQDN.com                       | | 32 | mgmt      | | 1 |
| ---------------- | --- | ------------------------------ | ---------------- | --- |
| tacacs (default) | |   | 1.1.1.1                        | | 49 | mgmt      | | 2 |
| tacacs (default) | |   | 1.1.1.2                        | | 12 | mgmt      | | 3 |
| tacacs (default) | |   | abc.com                        | | 32 | vrf_red   | | 4 |
| tacacs (default) | |   | 2001:0db8:85a3:0000:0000:8a2e: |                  |     |
|                  |     | 0370:7334                      | | 49 | default   | | 5 |
| tacacs (default) | |   | 1.1.1.3                        | | 32 | vrf_blue| | 6   |
--------------------------------------------------------------------------------
ShowingRADIUSservergroupinformation:
| switch# show | aaa server-groups | radius         |     |     |
| ------------ | ----------------- | -------------- | --- | --- |
| ******* AAA  | Mechanism         | RADIUS ******* |     |     |
--------------------------------------------------------------------------------
| GROUP NAME | |   | SERVER NAME | | PORT | VRF | | PRIORITY |
| ---------- | --- | ----------- | ------------ | ---------- |
--------------------------------------------------------------------------------
| sg4 | |   | 2001:0db8:85a3:0000:0000:8a2e: |                  |     |
| --- | --- | ------------------------------ | ---------------- | --- |
|     |     | 0370:7334                      | | 1812 | default | | 1 |
--------------------------------------------------------------------------------
| sg3 | |   | 1.1.1.5 | | 12 | mgmt | | 1 |
| --- | --- | ------- | ----------- | --- |
--------------------------------------------------------------------------------
| radius (default) | |   | 1.1.1.4                        | | 1812 | mgmt    | | 1 |
| ---------------- | --- | ------------------------------ | ---------------- | --- |
| radius (default) | |   | 1.1.1.5                        | | 12 | mgmt      | | 2 |
| radius (default) | |   | abc1.com                       | | 32 | mgmt      | | 3 |
| radius (default) | |   | 2001:0db8:85a3:0000:0000:8a2e: |                  |     |
|                  |     | 0370:7334                      | | 1812 | default | | 4 |
| radius (default) | |   | 1.1.1.6                        | | 32 | vrf_red   | | 5 |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 137

| radius (default) | | 1.1.1.7 |     |     | | 32 | vrf_blue| | 6   |
| ---------------- | --------- | --- | --- | ---------------- | --- |
--------------------------------------------------------------------------------
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show accounting |           | log           |        |     |     |
| --------------- | --------- | ------------- | ------ | --- | --- |
| show accounting | log [last | <QTY-TO-SHOW> | | all] |     |     |
Description
Enteredwithoutoptionalparameters,thiscommandshowsallaccountinglogrecordsforthecurrent
boot.Sensitiveinformationismaskedfromthelog,bybeingrepresentedasasterisks.
Thisshow accounting logcommandreplacestheshow audit-logcommandthatissupportedonlyin10.00
releases.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
last <QTY-TO-SHOW> Specifieshowmanymost-recentaccountinglogrecordstoshow
forthecurrentboot.Range:1to1000.
| all |     |     | Selectsforshowing,allaccountingrecordsfromthecurrentboot |     |     |
| --- | --- | --- | -------------------------------------------------------- | --- | --- |
andthepreviousboot.
Usage
Thelogmessagestartswiththerecordtype,whichisspecifictoAOS-CX.Valuesarethefollowing:
USER_START
Recordofauserloginaction.
USER_END
Recordofauserlogoutaction.
USYS_CONFIG
Recordofacommandexecutedbytheuser.
Thethreetypesofaccountingloginformationareidentifiedbythemsg=elementstartingwiththe
rec=itemasfollows:
n Execisidentifiedwith:msg='rec=ACCT_EXEC
n Commandisidentifiedwith:msg='rec=ACCT_CMD
RemoteAAA(TACACS+,RADIUS)commands|138

n Systemisidentifiedwith:msg='rec=ACCT_SYSTEM
Theusergroupisindicatedbypriv-lvl,whichisspecifictoAOS-CX.Valuesarethefollowing:
Privilege
User group
level
| 1   | operators |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- |
administrators
15
auditors
19
Thevalueofserviceindicateswhichuserinterfacewasused:
service=shell
IndicatesthatthelogentryisaresultofaCLIcommand.
service=https-server
IndicatesthatthelogentryisaresultofaRESTAPIrequestoraWebUIaction.
ThestringvalueofdataidentifiestheCLIcommandorRESTAPIrequestthatwasexecuted.
TheseelementsareshownincontextunderExamples.
Examples
Showingtheaccountinglogforthepreviousandcurrentboot.Linebreakshavebeenaddedfor
readability.
| switch# show | accounting |     | log | all |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Local accounting |     | logs | from | previous | boot |     |     |     |
| ---------------- | --- | ---- | ---- | -------- | ---- | --- | --- | --- |
---------------------------------------------------------------------------------
----
| type=DAEMON_START |     | msg=audit(Nov |     | 05  | 2018 | 23:00:58.607:9057) |     | :   |
| ----------------- | --- | ------------- | --- | --- | ---- | ------------------ | --- | --- |
auditd start, ver=2.4.3 format=raw kernel=4.9.119-yocto-standard res=success
----
| type=USER_START |     | msg=audit(Nov |     | 05  | 2018 | 23:06:42.398:42) |     | :   |
| --------------- | --- | ------------- | --- | --- | ---- | ---------------- | --- | --- |
msg='rec=ACCT_EXEC op=start session=CONSOLE timezone=UTC user=user1 priv-lvl=15
| auth-method=LOCAL |              | auth-type=LOCAL |     |              | service=shell |     | isconfig=no |     |
| ----------------- | ------------ | --------------- | --- | ------------ | ------------- | --- | ----------- | --- |
| hostname=8xxx     | addr=0.0.0.0 |                 |     | res=success' |               |     |             |     |
----
| type=USYS_CONFIG |     | msg=audit(Nov |     | 05  | 2018 | 23:06:42.399:43) |     | :   |
| ---------------- | --- | ------------- | --- | --- | ---- | ---------------- | --- | --- |
msg='rec=ACCT_CMD op=stop session=CONSOLE timezone=UTC user=user1 priv-lvl=15
| auth-method=LOCAL |               | auth-type=LOCAL |     |              | service=shell |              | isconfig=no |     |
| ----------------- | ------------- | --------------- | --- | ------------ | ------------- | ------------ | ----------- | --- |
| data="enable"     | hostname=8xxx |                 |     | addr=0.0.0.0 |               | res=success' |             |     |
----
| type=USYS_CONFIG |     | msg=audit(Nov |     | 05  | 2018 | 23:08:24.693:51) |     | :   |
| ---------------- | --- | ------------- | --- | --- | ---- | ---------------- | --- | --- |
msg='rec=ACCT_CMD op=stop session=CONSOLE timezone=UTC user=user1 priv-lvl=1
| auth-method=LOCAL |     | auth-type=LOCAL |     |     | service=shell |     | isconfig=no |     |
| ----------------- | --- | --------------- | --- | --- | ------------- | --- | ----------- | --- |
data="configure terminal" hostname=8xxx addr=0.0.0.0 res=success'
----
| type=USYS_CONFIG |     | msg=audit(Nov |     | 05  | 2018 | 23:08:39.108:52) |     | :   |
| ---------------- | --- | ------------- | --- | --- | ---- | ---------------- | --- | --- |
msg='rec=ACCT_CMD op=stop session=CONSOLE timezone=UTC user=user1 priv-lvl=15
| auth-method=LOCAL  |              | auth-type=LOCAL |             |              | service=shell |     | isconfig=yes |     |
| ------------------ | ------------ | --------------- | ----------- | ------------ | ------------- | --- | ------------ | --- |
| data="https-server |              | rest            | access-mode |              | read-write"   |     |              |     |
| hostname=8xxx      | addr=0.0.0.0 |                 |             | res=success' |               |     |              |     |
----
| type=USER_START |     | msg=audit(Nov |     | 05  | 2018 | 23:10:57.238:58) |     | :   |
| --------------- | --- | ------------- | --- | --- | ---- | ---------------- | --- | --- |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 139

msg='rec=ACCT_EXEC op=start session=REST timezone=UTC user=admin priv-lvl=15
| auth-method=LOCAL      |     | auth-type=LOCAL |                          |     | service=https-server |     |     |     |
| ---------------------- | --- | --------------- | ------------------------ | --- | -------------------- | --- | --- | --- |
| data="http-method=POST |     |                 | http-uri=/rest/v1/login" |     |                      |     |     |     |
| hostname=8xxx          |     | addr=127.0.0.1  |                          |     | res=success'         |     |     |     |
----
| type=USYS_CONFIG |     | msg=audit(Nov |     |     | 05 2018 23:15:11.958:75) |     |     | :   |
| ---------------- | --- | ------------- | --- | --- | ------------------------ | --- | --- | --- |
msg='rec=ACCT_CMD op=stop session=CONSOLE timezone=UTC user=user1 priv-lvl=15
| auth-method=LOCAL |     | auth-type=LOCAL |     |     | service=shell | isconfig=yes |     |     |
| ----------------- | --- | --------------- | --- | --- | ------------- | ------------ | --- | --- |
data="tacacs-server host 2.2.2.2" hostname=8xxx addr=0.0.0.0 res=success'
----
| type=USYS_CONFIG |     | msg=audit(Nov |     |     | 05 2018 23:15:37.090:76) |     |     | :   |
| ---------------- | --- | ------------- | --- | --- | ------------------------ | --- | --- | --- |
msg='rec=ACCT_CMD op=stop session=REST timezone=UTC user=admin priv-lvl=15
| auth-method=LOCAL |     | auth-type=LOCAL |     |     | service=https-server |     |     |     |
| ----------------- | --- | --------------- | --- | --- | -------------------- | --- | --- | --- |
data="http-method=GET http-uri=/rest/v1/system/vrfs/mgmt/tacacs_servers"
| hostname=8xxx |     | addr=127.0.0.1 |     |     | res=success' |     |     |     |
| ------------- | --- | -------------- | --- | --- | ------------ | --- | --- | --- |
----
| type=USER_END |     | msg=audit(Nov |     | 05  | 2018 23:26:59.207:90) |     | :   |     |
| ------------- | --- | ------------- | --- | --- | --------------------- | --- | --- | --- |
msg='rec=ACCT_EXEC op=stop session=REST timezone=UTC user=admin priv-lvl=15
| auth-method=LOCAL      |     | auth-type=LOCAL |                           |     | service=https-server |     |     |     |
| ---------------------- | --- | --------------- | ------------------------- | --- | -------------------- | --- | --- | --- |
| data="http-method=POST |     |                 | http-uri=/rest/v1/logout" |     |                      |     |     |     |
| hostname=8xxx          |     | addr=127.0.0.1  |                           |     | res=success'         |     |     |     |
----
| type=USER_END |     | msg=audit(Nov |     | 05  | 2018 23:27:49.164:93) |     | :   |     |
| ------------- | --- | ------------- | --- | --- | --------------------- | --- | --- | --- |
msg='rec=ACCT_EXEC op=stop session=CONSOLE timezone=UTC user=user1 priv-lvl=15
| auth-method=LOCAL |     | auth-type=LOCAL |     |              | service=shell | isconfig=no |     |     |
| ----------------- | --- | --------------- | --- | ------------ | ------------- | ----------- | --- | --- |
| hostname=8xxx     |     | addr=0.0.0.0    |     | res=success' |               |             |     |     |
---------------------------------------------------------------------------------
| Local accounting |     | logs | from | current | boot |     |     |     |
| ---------------- | --- | ---- | ---- | ------- | ---- | --- | --- | --- |
---------------------------------------------------------------------------------
----
| type=DAEMON_START |     | msg=audit(Nov |     |     | 05 2018 23:32:05.642:626) |     |     | :   |
| ----------------- | --- | ------------- | --- | --- | ------------------------- | --- | --- | --- |
auditd start, ver=2.4.3 format=raw kernel=4.9.119-yocto-standard res=success
----
| type=USER_START |     | msg=audit(Nov |     |     | 05 2018 23:35:52.915:11) |     |     | :   |
| --------------- | --- | ------------- | --- | --- | ------------------------ | --- | --- | --- |
msg='rec=ACCT_EXEC op=start session=CONSOLE timezone=UTC user=admin priv-lvl=15
| auth-method=LOCAL |     | auth-type=LOCAL |     |              | service=shell | isconfig=no |     |     |
| ----------------- | --- | --------------- | --- | ------------ | ------------- | ----------- | --- | --- |
| hostname=8xxx     |     | addr=0.0.0.0    |     | res=success' |               |             |     |     |
----
| type=USYS_CONFIG |     | msg=audit(Nov |     |     | 05 2018 23:35:52.917:12) |     |     | :   |
| ---------------- | --- | ------------- | --- | --- | ------------------------ | --- | --- | --- |
msg='rec=ACCT_CMD op=stop session=CONSOLE timezone=UTC user=admin priv-lvl=15
auth-method=LOCAL auth-type=LOCAL service=shell isconfig=no data="enable"
| hostname=8xxx       |         | addr=0.0.0.0 |         | res=success' |              |     |     |     |
| ------------------- | ------- | ------------ | ------- | ------------ | ------------ | --- | --- | --- |
| Command History     |         |              |         |              |              |     |     |     |
| Release             |         |              |         |              | Modification |     |     |     |
| 10.07orearlier      |         |              |         |              | --           |     |     |     |
| Command Information |         |              |         |              |              |     |     |     |
| Platforms           | Command |              | context |              | Authority    |     |     |     |
Allplatforms Manager(#)orAuditor AuditorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Auditorscanexecutethis
(auditor)
commandfromtheauditorcontext(auditor>)only.
show radius-server
RemoteAAA(TACACS+,RADIUS)commands|140

| show radius-server | [detail] [vsx-peer] |     |     |     |
| ------------------ | ------------------- | --- | --- | --- |
Description
ShowsconfiguredRADIUSserversinformation.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
detail SelectsadditionalRADIUSserverdetailsandglobalparametersfor
showing.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
n Whentheshow radius-servercommandshowsNonefortheshared-secret,thepasskeyismissing.
n TheTracking-Last-AttemptedandNext-Tracking-Requestfieldsareapplicableonlywhenthe
RADIUS servertrackingmethodisaccess-request.
ForinformationaboutRADIUS servertrackingmethods,seetheradius-server host tls tracking-
method.command.
Examples
ShowingasummaryoftheglobalRADIUSconfiguration:
| switch# show   | radius-server        |         |     |     |
| -------------- | -------------------- | ------- | --- | --- |
| ******* Global | RADIUS Configuration | ******* |     |     |
Shared-Secret:
AQBapRIb1nyfO/CyTOjj/lPIihQKoTcZWzPxlPwazapMPFKOCwAAAGJtiSZsV9EM/HZq
| Timeout: 60         |                      |     |     |     |
| ------------------- | -------------------- | --- | --- | --- |
| Auth-Type:          | pap                  |     |     |     |
| Retries: 5          |                      |     |     |     |
| TLS Timeout:        | 60                   |     |     |     |
| Tracking Time       | Interval (seconds):  | 60  |     |     |
| Tracking Retries:   | 5                    |     |     |     |
| Tracking User-name: | radius-tracking-user |     |     |     |
| Tracking Password:  | None                 |     |     |     |
| Number of Servers:  | 1                    |     |     |     |
---------------------------------------------------------------------------
| SERVER NAME |     |     | | TLS | PORT | | VRF |
| ----------- | --- | --- | ------------ | ----- |
---------------------------------------------------------------------------
| 20.1.1.129                              |     |     | | | 1812 | | default  |
| --------------------------------------- | --- | --- | -------- | ---------- |
| 1.1.1.4                                 |     |     | | | 1812 | | mgmt     |
| 1.1.1.5                                 |     |     | | | 12   | | mgmt     |
| abc1.com                                |     |     | | | 32   | | mgmt     |
| 2001:0db8:85a3:0000:0000:8a2e:0371:7334 |     |     | | | 1812 | | default  |
| 1.1.1.6                                 |     |     | | | 32   | | vrf_red  |
| 1.1.1.7                                 |     |     | | | 32   | | vrf_blue |
---------------------------------------------------------------------------
ShowingasummaryofaRADIUSserverwhenthestatusservertimeintervalisconfigured:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 141

| switch# show   | radius-server                   |               |     |         |     |
| -------------- | ------------------------------- | ------------- | --- | ------- | --- |
| Unreachable    | servers are                     | preceded      | by  | *       |     |
| ******* Global | RADIUS                          | Configuration |     | ******* |     |
| Shared-Secret: | None                            |               |     |         |     |
| Timeout:       | 5                               |               |     |         |     |
| Auth-Type:     | pap                             |               |     |         |     |
| Retries:       | 1                               |               |     |         |     |
| TLS Timeout:   | 5                               |               |     |         |     |
| Tracking       | Time Interval                   | (seconds):    | 300 |         |     |
| Tracking       | Retries: 1                      |               |     |         |     |
| Tracking       | User-name: radius-tracking-user |               |     |         |     |
| Tracking       | Password: None                  |               |     |         |     |
| Status-Server  | Time Interval                   | (seconds):    |     | 400     |     |
| Number of      | Servers: 2                      |               |     |         |     |
--------------------------------------------------------------------------------
| SERVER NAME |     |     |     | | TLS | PORT | | VRF |
| ----------- | --- | --- | --- | ------------ | ----- |
--------------------------------------------------------------------------------
| 1.1.1.1 |     |     |     | | Yes | 2083 | | default |
| ------- | --- | --- | --- | ------------ | --------- |
| 2.2.2.2 |     |     |     | | | 1812     | | default |
--------------------------------------------------------------------------------
ShowingdetailsofaglobalRADIUSconfiguration:
| switch# show   | radius-server | detail        |     |         |     |
| -------------- | ------------- | ------------- | --- | ------- | --- |
| ******* Global | RADIUS        | Configuration |     | ******* |     |
Shared-Secret: AQBapb+HsdpqV1QcA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout:            | 5                               |              |        |     |     |
| ------------------- | ------------------------------- | ------------ | ------ | --- | --- |
| Auth-Type:          | pap                             |              |        |     |     |
| Retries:            | 5                               |              |        |     |     |
| TLS Timeout:        | 60                              |              |        |     |     |
| Tracking            | Time Interval                   | (seconds):   | 60     |     |     |
| Tracking            | Retries: 5                      |              |        |     |     |
| Tracking            | User-name: radius-tracking-user |              |        |     |     |
| Tracking            | Password: None                  |              |        |     |     |
| Number of           | Servers: 1                      |              |        |     |     |
| ****** RADIUS       | Server                          | Information  | ****** |     |     |
| Server-Name         |                                 | : 20.1.1.129 |        |     |     |
| Auth-Port           |                                 | : 1812       |        |     |     |
| Accounting-Port     |                                 | : 1813       |        |     |     |
| VRF                 |                                 | : default    |        |     |     |
| TLS Enabled         |                                 | : No         |        |     |     |
| Shared-Secret       |                                 | : None       |        |     |     |
| Timeout             |                                 | : 60         |        |     |     |
| Retries             |                                 | : 5          |        |     |     |
| Auth-Type           |                                 | : pap        |        |     |     |
| Server-Group        |                                 | : radius     |        |     |     |
| Default-Priority    |                                 | : 4          |        |     |     |
| Tracking            |                                 | : disabled   |        |     |     |
| Tracking-Mode       |                                 | : any        |        |     |     |
| Reachability-Status |                                 | : N/A        |        |     |     |
| ClearPass-Username  |                                 | :            |        |     |     |
| ClearPass-Password  |                                 | : None       |        |     |     |
ShowingdetailsofaRADIUSserverwhentheper-serversharedkeyandtheglobalRADIUSsharedkey
arenotset:
RemoteAAA(TACACS+,RADIUS)commands|142

| switch#          | show radius-server        | detail        |         |
| ---------------- | ------------------------- | ------------- | ------- |
| *******          | Global RADIUS             | Configuration | ******* |
| Shared-Secret:   | None                      |               |         |
| Timeout:         | 5                         |               |         |
| Auth-Type:       | pap                       |               |         |
| Retries:         | 1                         |               |         |
| TLS Timeout      | : 5                       |               |         |
| Number           | of Servers: 1             |               |         |
| ******           | RADIUS Server Information |               | ******  |
| Server-Name      |                           | : 1.1.1.1     |         |
| Auth-Port        |                           | : 2083        |         |
| VRF              |                           | : default     |         |
| Shared-Secret    | (default)                 | : None        |         |
| Timeout          | (default)                 | : 5           |         |
| Retries          | (default)                 | : 1           |         |
| Auth-Type        | (default)                 | : pap         |         |
| Server-Group     | (default)                 | : radius      |         |
| Default-Priority |                           | : 1           |         |
ShowingdetailsofaRADIUSserverwithTLS:
| switch#        | show radius-server | detail        |         |
| -------------- | ------------------ | ------------- | ------- |
| *******        | Global RADIUS      | Configuration | ******* |
| Shared-Secret: | None               |               |         |
| Timeout:       | 5                  |               |         |
| Auth-Type:     | pap                |               |         |
| Retries:       | 1                  |               |         |
| TLS Timeout:   | 5                  |               |         |
| TLS Connection | Timeout:           | 5             |         |
| TLS Connection | Retries:           | 1             |         |
| Tracking       | Time Interval      | (seconds):    | 60      |
| Tracking       | Retries: 1         |               |         |
| Tracking       | User-name: jim     |               |         |
| Tracking       | Password:          |               |         |
AQBapcPi5GR2MGH5WCuYW0ZRtLrFgGT/pAcp0JqFFpndkMwYCwAAADsYv787vMdnbSBZ
| Number              | of Servers: 1             |                              |        |
| ------------------- | ------------------------- | ---------------------------- | ------ |
| ******              | RADIUS Server Information |                              | ****** |
| Server-Name         |                           | : 172.20.30.30               |        |
| Auth-Port           |                           | : 2083                       |        |
| Accounting-Port     |                           | : 2083                       |        |
| VRF                 |                           | : default                    |        |
| TLS Enabled         |                           | : Yes                        |        |
| TLS Connection      | Timeout                   | (default):                   | 5      |
| TLS Connection      | Retries                   | (default):                   | 1      |
| TLS Connection      | Status                    | : tls_connection_established |        |
| Timeout             | (default)                 | : 5                          |        |
| Auth-Type           | (default)                 | : pap                        |        |
| Server-Group        | (default)                 | : radius                     |        |
| Default-Priority    |                           | : 1                          |        |
| Tracking            |                           | : enabled                    |        |
| Tracking-Mode       |                           | : any                        |        |
| Reachability-Status |                           | : reachable                  |        |
| ClearPass-Username  |                           | : admin                      |        |
| ClearPass-Password  |                           | :                            |        |
AQBapcPi5GR2MGH5WCuYW0ZRtLrFgGT/pAcp0JqFFpndkMwYCwAAADsYv787vMdnbSBZ
ShowingdetailsofaRADIUSserverwhenthestatus-servertrackingmethodisconfigured:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 143

| switch# show   | radius-server                   | detail    |         |
| -------------- | ------------------------------- | --------- | ------- |
| ******* Global | RADIUS Configuration            |           | ******* |
| Shared-Secret: | None                            |           |         |
| Timeout:       | 5                               |           |         |
| Auth-Type:     | pap                             |           |         |
| Retries:       | 1                               |           |         |
| TLS Timeout:   | 5                               |           |         |
| Tracking       | Time Interval (seconds):        |           | 300     |
| Tracking       | Retries: 1                      |           |         |
| Tracking       | User-name: radius-tracking-user |           |         |
| Tracking       | Password: None                  |           |         |
| Status-Server  | Time Interval                   | (seconds) | : 600   |
| Number of      | Servers: 1                      |           |         |
| ****** RADIUS  | Server Information              |           | ******  |
Server-Name : 2.2.2.2
Auth-Port : 2083
Accounting-Port : 2083
VRF : default
TLS Enabled : Yes
| TLS Connection | Status |     | : tls_connection_established |
| -------------- | ------ | --- | ---------------------------- |
Timeout : 5
Auth-Type : pap
Server-Group : radius
Default-Priority : 1
ClearPass-Username :
ClearPass-Password : None
Tracking : disabled
Tracking-Mode : any
Tracking-Method : status-server
Reachability-Status : unknown
Tracking-Last-Attempted : N/A
Next-Tracking-Request : N/A
| Port-Access | session |     | : status-server |
| ----------- | ------- | --- | --------------- |
ShowingdetailsofaRADIUSserverwhenthekeep-alivetrackingmethodisconfigured:
| switch# show   | radius-server                   | detail    |         |
| -------------- | ------------------------------- | --------- | ------- |
| ******* Global | RADIUS Configuration            |           | ******* |
| Shared-Secret: | None                            |           |         |
| Timeout:       | 5                               |           |         |
| Auth-Type:     | pap                             |           |         |
| Retries:       | 1                               |           |         |
| TLS Timeout:   | 5                               |           |         |
| Tracking       | Time Interval (seconds):        |           | 300     |
| Tracking       | Retries: 1                      |           |         |
| Tracking       | User-name: radius-tracking-user |           |         |
| Tracking       | Password: None                  |           |         |
| Status-Server  | Time Interval                   | (seconds) | : 400   |
| Number of      | Servers: 1                      |           |         |
| ****** RADIUS  | Server Information              |           | ******  |
Server-Name : 1.1.1.1
Auth-Port : 2083
Accounting-Port : 2083
VRF : default
TLS Enabled : Yes
| TLS Connection | Status |     | : tcp_connection_failed |
| -------------- | ------ | --- | ----------------------- |
Timeout : 5
RemoteAAA(TACACS+,RADIUS)commands|144

Auth-Type : pap
Server-Group : radius
Default-Priority : 1
ClearPass-Username :
ClearPass-Password : None
Tracking : disabled
Tracking-Mode : any
Tracking-Method : keep-alive
Reachability-Status : unknown
Tracking-Last-Attempted : N/A
Next-Tracking-Request : N/A
| Port-Access | session |     | : status-server |
| ----------- | ------- | --- | --------------- |
ShowingdetailsofaRADIUSserverwhentheaccess-requesttrackingmethodisconfigured:
| switch# show   | radius-server                   | detail    |         |
| -------------- | ------------------------------- | --------- | ------- |
| ******* Global | RADIUS Configuration            |           | ******* |
| Shared-Secret: | None                            |           |         |
| Timeout:       | 5                               |           |         |
| Auth-Type:     | pap                             |           |         |
| Retries:       | 1                               |           |         |
| TLS Timeout:   | 5                               |           |         |
| Tracking       | Time Interval (seconds):        |           | 300     |
| Tracking       | Retries: 1                      |           |         |
| Tracking       | User-name: radius-tracking-user |           |         |
| Tracking       | Password: None                  |           |         |
| Status-Server  | Time Interval                   | (seconds) | : 500   |
| Number of      | Servers: 1                      |           |         |
| ****** RADIUS  | Server Information              |           | ******  |
Server-Name : 4.4.4.4
Auth-Port : 2083
Accounting-Port : 2083
VRF : default
TLS Enabled : Yes
| TLS Connection | Status |     | : tcp_connection_failed |
| -------------- | ------ | --- | ----------------------- |
Timeout : 5
Auth-Type : pap
Server-Group : radius
Default-Priority : 1
ClearPass-Username :
ClearPass-Password : None
Tracking : disabled
Tracking-Mode : any
Tracking-Method : access-request
Reachability-Status : unknown
Tracking-Last-Attempted : N/A
Next-Tracking-Request : N/A
| Port-Access         | session |     | : keep-alive |
| ------------------- | ------- | --- | ------------ |
| Command History     |         |     |              |
| Release             |         |     | Modification |
| 10.07orearlier      |         |     | --           |
| Command Information |         |     |              |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 145

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show | radius-server | secure | ipsec |     |
| ---- | ------------- | ------ | ----- | --- |
show radius-server secure ipsec { server-list | host {<FQDN> | <IPV4> | <IPv6>}
| [port | <PORT-NUMBER>] | [vrf <VRF-NAME>] | [vsx-peer] | }   |
| ----- | -------------- | ---------------- | ---------- | --- |
Description
ShowsinformationforoneorallRADIUSserversconfiguredwithIPsec.
| Parameter   |                    |     | Description                  |     |
| ----------- | ------------------ | --- | ---------------------------- | --- |
| server-list |                    |     | Selectsallserversforshowing. |     |
| {<FQDN>     | | <IPV4> | <IPv6>} |     | SpecifiestheRADIUSserveras:  |     |
<FQDN>:afullyqualifieddomainname.
n
n <IPV4>:anIPv4address.
<IPV6>:anIPv6address.
n
port <PORT-NUMBER> Specifiestheauthenticationportnumber.Range:1to65535.
Default:1812.
vrf <VRF-NAME> SpecifiestheVRFnametobeusedforcommunicatingwiththe
server.IfnoVRFnameisprovided,thedefaultVRFnamed
defaultisused.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
TheIPseckeyisshowninanexportableciphertextformat.
Examples
ShowinginformationforRADIUSserver1.1.1.1securedwithIPsec:
| switch#        | show radius-server | secure    | ipsec host 1.1.1.1 |     |
| -------------- | ------------------ | --------- | ------------------ | --- |
| IPsec          |                    | : enabled |                    |     |
| Protocol       |                    | : ESP     |                    |     |
| Authentication |                    | : MD5     |                    |     |
| Encryption     |                    | : AES     |                    |     |
| SPI            |                    | : 1234    |                    |     |
ShowinginformationforallRADIUSserverssecuredwithIPsec:
| switch# | show radius-server | secure    | ipsec server-list |     |
| ------- | ------------------ | --------- | ----------------- | --- |
| Server  |                    | : 1.1.1.1 |                   |     |
RemoteAAA(TACACS+,RADIUS)commands|146

| IPsec          |             |         |         | : enabled |              |     |
| -------------- | ----------- | ------- | ------- | --------- | ------------ | --- |
| Protocol       |             |         |         | : ESP     |              |     |
| Authentication |             |         |         | : MD5     |              |     |
| Encryption     |             |         |         | : AES     |              |     |
| SPI            |             |         |         | : 1234    |              |     |
| Server         |             |         |         | : 1.1.1.2 |              |     |
| IPsec          |             |         |         | : enabled |              |     |
| Protocol       |             |         |         | : ESP     |              |     |
| Authentication |             |         |         | : MD5     |              |     |
| Encryption     |             |         |         | : AES     |              |     |
| SPI            |             |         |         | : 12341   |              |     |
| Command        | History     |         |         |           |              |     |
| Release        |             |         |         |           | Modification |     |
| 10.07orearlier |             |         |         |           | --           |     |
| Command        | Information |         |         |           |              |     |
| Platforms      |             | Command | context |           | Authority    |     |
Allplatorms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show | radius-server |     |     | statistics |     | authentication |
| ---- | ------------- | --- | --- | ---------- | --- | -------------- |
show radius-server statistics authentication host {<FQDN> | <IPV4> | <IPv6>}
| [tls] | [port | <PORT-NUMBER>] |     | [vrf | <VRF-NAME>] | [vsx-peer] |
| ----- | ----- | -------------- | --- | ---- | ----------- | ---------- |
Description
ShowsauthenticationstatisticsforthespecifiedRADIUSserver.
| Parameter |          |           |     |     | Description                         |     |
| --------- | -------- | --------- | --- | --- | ----------------------------------- | --- |
| {<FQDN>   | | <IPV4> | | <IPv6>} |     |     | SpecifiestheRADIUSserveras:         |     |
|           |          |           |     |     | n <FQDN>:afullyqualifieddomainname. |     |
|           |          |           |     |     | n <IPV4>:anIPv4address.             |     |
|           |          |           |     |     | n <IPV6>:anIPv6address.             |     |
| tls       |          |           |     |     | SelectsTLS.                         |     |
port <PORT-NUMBER> Specifiestheauthenticationportnumber.Range:1to65535.
Default:1812.
vrf <VRF-NAME> SpecifiestheVRFnametobeusedforcommunicatingwiththe
server.IfnoVRFnameisprovided,thedefaultVRFnamed
defaultisused.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 147

Examples
ShowingRADIUSserverauthenticationstatistics:
switch#
|                 | show    | radius-server | statistics | authentication | host 20.1.1.49 |
| --------------- | ------- | ------------- | ---------- | -------------- | -------------- |
| Server          | Name    | : 20.1.1.49   |            |                |                |
| Auth-Port       |         | : 2083        |            |                |                |
| Accounting-Port |         | : 2083        |            |                |                |
| VRF             |         | : default     |            |                |                |
| TLS             | Enabled | : No          |            |                |                |
| Authentication  |         | Statistics    |            |                |                |
-------------------------
| Round    | Trip           | Time      | : 3  |     |     |
| -------- | -------------- | --------- | ---- | --- | --- |
| Pending  |                | Requests  | : 0  |     |     |
| Timeouts |                |           | : 0  |     |     |
| Bad      | Authenticators |           | : 0  |     |     |
| Packets  |                | Dropped   | : 0  |     |     |
| Access   | Requests       |           | : 13 |     |     |
| Access   | challenge      |           | : 6  |     |     |
| Access   | Accepts        |           | : 3  |     |     |
| Access   | Rejects        |           | : 4  |     |     |
| Access   | Response       | Malformed | : 0  |     |     |
ShowingRADIUSserverauthenticationstatisticswhenRADIUSservertrackingmethodisconfigured:
| switch#         | show    | radius-server  | statistics | authentication |     |
| --------------- | ------- | -------------- | ---------- | -------------- | --- |
| Server          | Name    | : 10.93.48.200 |            |                |     |
| Auth-Port       |         | : 2083         |            |                |     |
| Accounting-Port |         | : 2083         |            |                |     |
| VRF             |         | : mgmt         |            |                |     |
| TLS             | Enabled | : yes          |            |                |     |
| Authentication  |         | Statistics     |            |                |     |
-------------------------
| Round          | Trip           | Time          |              |          | : 101 |
| -------------- | -------------- | ------------- | ------------ | -------- | ----- |
| Pending        |                | Requests      |              |          | : 0   |
| Timeouts       |                |               |              |          | : 342 |
| Bad            | Authenticators |               |              |          | : 0   |
| Packets        |                | Dropped       |              |          | : 0   |
| Access         | Requests       |               |              |          | : 779 |
| Access         | challenge      |               |              |          | : 182 |
| Access         | Accepts        |               |              |          | : 4   |
| Access         | Rejects        |               |              |          | : 251 |
| Access         | Response       | Malformed     |              |          | : 0   |
| Access         | Retransmits    |               |              |          | : 200 |
| Tracking       |                | Requests      |              |          | : 280 |
| Tracking       |                | Responses     |              |          | : 142 |
| Status-Server  |                | Requests      | (Tracking    | session) | : 280 |
| Status-Server  |                | Responses     | (Tracking    | session) | : 280 |
| Status-Server  |                | Requests      | (port-access | session) | : 280 |
| Status-Server  |                | Responses     | (port-access | session) | : 280 |
| Unknown        |                | Response Code |              |          |       |
| Command        | History        |               |              |          |       |
| Release        |                |               | Modification |          |       |
| 10.07orearlier |                |               | --           |          |       |
RemoteAAA(TACACS+,RADIUS)commands|148

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
show tacacs-server
| show tacacs-server | [detail] | [vsx-peer] |     |
| ------------------ | -------- | ---------- | --- |
Description
ShowstheconfiguredTACACS+servers.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
detail SelectsadditionalTACACS+serverdetailsandglobalparameters
forshowing.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingasummaryofaglobalTACACS+configurationwithashared-secret:
| switch# show   | tacacs-server |               |         |
| -------------- | ------------- | ------------- | ------- |
| ******* Global | TACACS+       | Configuration | ******* |
Shared-Secret: AQBapb+HsdpqV1Q3CPCBMQTG8e1cA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout:   | 5        |     |     |
| ---------- | -------- | --- | --- |
| Auth-Type: | pap      |     |     |
| Number of  | Servers: | 5   |     |
-------------------------------------------------------------------------------
| SERVER NAME |     |     | | PORT | VRF |
| ----------- | --- | --- | ------------ |
-------------------------------------------------------------------------------
1.1.1.1 | 49 | mgmt
1.1.1.2 | 12 | mgmt
abc.com | 32 | vrf_blue
2001:0db8:85a3:0000:0000:8a2e:0370:7334 | 49 | default
1.1.1.3 | 32 | vrf_red
-------------------------------------------------------------------------------
ShowingdetailsofaglobalTACACS+configuration:
| switch# show   | tacacs-server | detail        |         |
| -------------- | ------------- | ------------- | ------- |
| ******* Global | TACACS+       | Configuration | ******* |
Shared-Secret: AQBapb+HsdpqV1Q3CPCBMQTG8e1cA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout:   | 5   |     |     |
| ---------- | --- | --- | --- |
| Auth-Type: | pap |     |     |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 149

| Number      | of Servers: 5  |             |        |
| ----------- | -------------- | ----------- | ------ |
| ******      | TACACS+ Server | Information | ****** |
| Server-Name |                | : 1.1.1.2   |        |
| Auth-Port   |                | : 12        |        |
| VRF         |                | : mgmt      |        |
Shared-Secret (default) : AQBapb+HsdpqV1Q3CPCBMQTG8eeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout        | (default) | : 5                                       |     |
| -------------- | --------- | ----------------------------------------- | --- |
| Auth-Type      | (default) | : pap                                     |     |
| Server-Group   |           | : sg1                                     |     |
| Group-Priority |           | : 1                                       |     |
| Server-Name    |           | : 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |     |
| Auth-Port      |           | : 49                                      |     |
| VRF            |           | : default                                 |     |
Shared-Secret (default) : AQBapb+HsdpqV1Q3CPCBMQTG8eeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout        | (default) | : 5       |     |
| -------------- | --------- | --------- | --- |
| Auth-Type      | (default) | : pap     |     |
| Server-Group   |           | : sg2     |     |
| Group-Priority |           | : 1       |     |
| Server-Name    |           | : 1.1.1.1 |     |
| Auth-Port      |           | : 49      |     |
| VRF            |           | : mgmt    |     |
Shared-Secret (default) : AQBapb+HsdpqV1Q3CPCBMQTG8eeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout          | (default) | : 5       |     |
| ---------------- | --------- | --------- | --- |
| Auth-Type        | (default) | : pap     |     |
| Server-Group     | (default) | : tacacs  |     |
| Default-Priority |           | : 1       |     |
| Server-Name      |           | : abc.com |     |
| Auth-Port        |           | : 32      |     |
| VRF              |           | : vrf_red |     |
Shared-Secret (default) : AQBapb+HsdpqV1Q3CPCBMQTG8eeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout          |           | : 15       |     |
| ---------------- | --------- | ---------- | --- |
| Auth-Type        | (default) | : pap      |     |
| Server-Group     | (default) | : tacacs   |     |
| Default-Priority |           | : 3        |     |
| Server-Name      |           | : 1.1.1.3  |     |
| Auth-Port        |           | : 32       |     |
| VRF              |           | : vrf_blue |     |
Shared-Secret : AQBapfnqbSswqKC476tdUFZ+AncIRY92hDTYkQCAAAAFEAaHn43vNC
| Timeout          |           | : 15     |     |
| ---------------- | --------- | -------- | --- |
| Auth-Type        |           | : chap   |     |
| Server-Group     | (default) | : tacacs |     |
| Default-Priority |           | : 5      |     |
ShowingTACACS+serverwhenper-serversharedkeyandglobalTACACS+sharedkeyisnotset:
| switch#        | show tacacs-server |               |         |
| -------------- | ------------------ | ------------- | ------- |
| *******        | Global TACACS+     | Configuration | ******* |
| Shared-Secret: | None               |               |         |
| Timeout:       | 5                  |               |         |
| Auth-Type:     | pap                |               |         |
| Number         | of Servers: 1      |               |         |
-------------------------------------------------------------------------------
SERVER NAME | PORT | VRF
-------------------------------------------------------------------------------
RemoteAAA(TACACS+,RADIUS)commands|150

1.1.1.1 | 49 | default
-------------------------------------------------------------------------------
ShowingTACACS+serverdetailswhenper-serversharedkeyandglobalTACACS+sharedkeyisnotset:
| switch#          | show        | tacacs-server |               | detail    |              |
| ---------------- | ----------- | ------------- | ------------- | --------- | ------------ |
| *******          | Global      | TACACS+       | Configuration |           | *******      |
| Shared-Secret:   |             | None          |               |           |              |
| Timeout:         | 5           |               |               |           |              |
| Auth-Type:       | pap         |               |               |           |              |
| Number           | of Servers: |               | 1             |           |              |
| ******           | TACACS+     | Server        | Information   |           | ******       |
| Server-Name      |             |               |               | : 1.1.1.1 |              |
| Auth-Port        |             |               |               | : 49      |              |
| VRF              |             |               |               | : default |              |
| Shared-Secret    |             | (default)     |               | : None    |              |
| Timeout          | (default)   |               |               | : 5       |              |
| Auth-Type        | (default)   |               |               | : pap     |              |
| Server-Group     |             | (default)     |               | : tacacs  |              |
| Default-Priority |             |               |               | : 1       |              |
| Command          | History     |               |               |           |              |
| Release          |             |               |               |           | Modification |
| 10.07orearlier   |             |               |               |           | --           |
| Command          | Information |               |               |           |              |
| Platforms        |             | Command       | context       |           | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show tacacs-server |     |            |     | statistics |     |
| ------------------ | --- | ---------- | --- | ---------- | --- |
| show tacacs-server |     | statistics |     | [vsx-peer] |     |
Description
ShowsauthenticationstatisticsforallconfiguredTACACS+servers.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingTACACS+serverauthenticationstatistics:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 151

| switch#        | show tacacs-server | statistics |     |
| -------------- | ------------------ | ---------- | --- |
| Server         | Name : tac1        |            |     |
| Auth-Port      | : 49               |            |     |
| VRF            | : mgmt             |            |     |
| Authentication | Statistics         |            |     |
----------------------------------------------
| Round Trip     | Time        | : 1     |              |
| -------------- | ----------- | ------- | ------------ |
| Pending        | Requests    | : 0     |              |
| Timeout        |             | : 0     |              |
| Unknown        | Types       | : 0     |              |
| Packet         | Dropped     | : 0     |              |
| Auth Start     |             | : 8     |              |
| Auth challenge |             | : 0     |              |
| Auth Accepts   |             | : 4     |              |
| Auth Rejects   |             | : 4     |              |
| Auth reply     | malformed   | : 0     |              |
| Tracking       | Requests    | : 0     |              |
| Tracking       | Responses   | : 0     |              |
| Command        | History     |         |              |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show tech | aaa |     |     |
| --------- | --- | --- | --- |
| show tech | aaa |     |     |
Description
ShowstheAAAconfigurationsettings.
Example
ShowingtheAAAconfigurationsettings:
| switch# | show tech aaa |     |     |
| ------- | ------------- | --- | --- |
====================================================
| Show Tech | executed | on Tue Feb | 14 02:19:11 2017 |
| --------- | -------- | ---------- | ---------------- |
====================================================
====================================================
| [Begin] | Feature aaa |     |     |
| ------- | ----------- | --- | --- |
====================================================
*********************************
| Command | : show aaa | authentication |     |
| ------- | ---------- | -------------- | --- |
*********************************
AAA Authentication:
RemoteAAA(TACACS+,RADIUS)commands|152

| Fail-through   |                |              | :   | Enabled |
| -------------- | -------------- | ------------ | --- | ------- |
| Limit          | Login Attempts |              | :   | Not set |
| Lockout        | Time           |              | :   | 300     |
| Minimum        | Password       | Length       | :   | Not set |
| Authentication | for            | ssh channel: |     |         |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| local |     |     |     | | 0 |
| ----- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authentication | for | https-server |     | channel: |
| -------------- | --- | ------------ | --- | -------- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| local |     |     |     | | 0 |
| ----- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authentication | for | console | channel: |     |
| -------------- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| local |     |     |     | | 0 |
| ----- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authentication | for | default | channel: |     |
| -------------- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| tacacs |     |     |     | | 0 |
| ------ | --- | --- | --- | --- |
| local  |     |     |     | | 1 |
---------------------------------------------------------------------------------
*********************************
| Command | : show aaa | accounting |     |     |
| ------- | ---------- | ---------- | --- | --- |
*********************************
AAA Accounting:
| Accounting | Type        |          |     | : all        |
| ---------- | ----------- | -------- | --- | ------------ |
| Accounting | Mode        |          |     | : start-stop |
| Accounting | for default | channel: |     |              |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| local |     |     |     | | 0 |
| ----- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Accounting | for ssh | channel: |     |     |
| ---------- | ------- | -------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| tacacs |     |     |     | | 0 |
| ------ | --- | --- | --- | --- |
| local  |     |     |     | | 1 |
---------------------------------------------------------------------------------
| Accounting | for https-server |     | channel: |     |
| ---------- | ---------------- | --- | -------- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| tacacs |     |     |     | | 0 |
| ------ | --- | --- | --- | --- |
---------------------------------------------------------------------------------
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 153

*********************************
| Command | : show aaa | authorization |     |     |     |
| ------- | ---------- | ------------- | --- | --- | --- |
*********************************
| Authorization | for default | channel: |     |     |     |
| ------------- | ----------- | -------- | --- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |     |     |
| ---------- | --- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| none |     |     | | 0 |     |     |
| ---- | --- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authorization | for console | channel: |     |     |     |
| ------------- | ----------- | -------- | --- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |     |     |
| ---------- | --- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| none |     |     | | 0 |     |     |
| ---- | --- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authorization | for ssh | channel: |     |     |     |
| ------------- | ------- | -------- | --- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |     |     |
| ---------- | --- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| tacacs |     |     | | 0 |     |     |
| ------ | --- | --- | --- | --- | --- |
| none   |     |     | | 1 |     |     |
---------------------------------------------------------------------------------
*********************************
| Command | : show aaa | server-groups |     |     |     |
| ------- | ---------- | ------------- | --- | --- | --- |
*********************************
| ******* | AAA Mechanism | TACACS+ | ******* |     |     |
| ------- | ------------- | ------- | ------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | SERVER NAME | | PORT | PRIORITY | | VRF |
| ---------- | --- | --- | ------------- | ----------------- | ----- |
---------------------------------------------------------------------------------
| tacacs | (default) |     | | 1.1.1.1 | | 49 | 1 | | mgmt |
| ------ | --------- | --- | --------- | -------- | ------ |
---------------------------------------------------------------------------------
| ******* | AAA Mechanism | RADIUS | ******* |     |     |
| ------- | ------------- | ------ | ------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | SERVER NAME | | PORT | PRIORITY | | VRF |
| ---------- | --- | --- | ------------- | ----------------- | ----- |
---------------------------------------------------------------------------------
***********************************
| Command | : show tacacs-server |     | detail |     |     |
| ------- | -------------------- | --- | ------ | --- | --- |
***********************************
| *******        | Global TACACS+                                | Configuration        | ******* |     |     |
| -------------- | --------------------------------------------- | -------------------- | ------- | --- | --- |
| Shared-Secret: | G8ekK1cA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA= |                      |         |     |     |
| Timeout:       | 5                                             |                      |         |     |     |
| Auth-Type:     | pap                                           |                      |         |     |     |
| Tracking:      | disabled                                      |                      |         |     |     |
| Tracking       | Time Interval                                 | (seconds):           | 300     |     |     |
| Tracking       | User-name:                                    | tacacs-tracking-user |         |     |     |
| Tracking       | Password:                                     | None                 |         |     |     |
| Number         | of Servers:                                   | 1                    |         |     |     |
| ******         | TACACS+ Server                                | Information          | ******  |     |     |
| Server-Name    |                                               | : 1.1.1.1            |         |     |     |
| Auth-Port      |                                               | : 49                 |         |     |     |
| VRF            |                                               | : mgmt               |         |     |     |
Shared-Secret : KCdmOMxMD26T0fQoXfJbtj9j2AUxlGn6eCAAAAF2MkfMTojqX
RemoteAAA(TACACS+,RADIUS)commands|154

| Timeout             | (default) |           |     | : 5        |     |
| ------------------- | --------- | --------- | --- | ---------- | --- |
| Auth-Type           | (default) |           |     | : pap      |     |
| Server-Group        |           | (default) |     | : tacacs   |     |
| Default-Priority    |           |           |     | : 1        |     |
| Tracking            |           |           |     | : disabled |     |
| Reachability-Status |           |           |     | : N/A      |     |
***********************************
| Command | : show | radius-server |     | detail |     |
| ------- | ------ | ------------- | --- | ------ | --- |
***********************************
| ******* | Global | RADIUS | Configuration |     | ******* |
| ------- | ------ | ------ | ------------- | --- | ------- |
Shared-Secret: CPCBMQTG8ekK1cA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout:   | 5           |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- |
| Auth-Type: | pap         |     |     |     |     |
| Retries:   | 1           |     |     |     |     |
| Number     | of Servers: |     | 0   |     |     |
====================================================
| [End] Feature |     | aaa |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
====================================================
====================================================
| Show Tech | commands |     | executed | successfully |     |
| --------- | -------- | --- | -------- | ------------ | --- |
====================================================
| Command        | History     |         |         |     |              |
| -------------- | ----------- | ------- | ------- | --- | ------------ |
| Release        |             |         |         |     | Modification |
| 10.07orearlier |             |         |         |     | --           |
| Command        | Information |         |         |     |              |
| Platforms      |             | Command | context |     | Authority    |
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
| tacacs-server    |           |           | auth-type |         |       |
| ---------------- | --------- | --------- | --------- | ------- | ----- |
| tacacs-server    | auth-type |           | {pap      | | chap} |       |
| no tacacs-server |           | auth-type | [pap      | |       | chap] |
Description
EnablestheCHAPorPAPauthenticationprotocol,whichisusedforcommunicationwiththeTACACS+
servers,atthegloballevel.Youcanoverridethiscommandwithafine-grainedperserverauth-type
configuration.
ThenoformofthiscommandresetstheglobalauthenticationmechanismforTACACS+toPAP,whichis
thedefaultauthenticationmechanismforTACACS+.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
auth-type {pap | chap} SelectseitherthePAPorCHAPauthenticationprotocol.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 155

Examples
EnablingcommandforCHAPauthentication:
switch(config)#
|     |     | tacacs-server |     | auth-type | chap |
| --- | --- | ------------- | --- | --------- | ---- |
EnablingcommandforPAPauthentication:
| switch(config)# |             | tacacs-server |         | auth-type    | pap       |
| --------------- | ----------- | ------------- | ------- | ------------ | --------- |
| Command         | History     |               |         |              |           |
| Release         |             |               |         | Modification |           |
| 10.07orearlier  |             |               |         | --           |           |
| Command         | Information |               |         |              |           |
| Platforms       |             | Command       | context |              | Authority |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| tacacs-server   |                    | host      |          |                      |             |
| --------------- | ------------------ | --------- | -------- | -------------------- | ----------- |
| tacacs-server   | host               | {<FQDN>   | | <IPV4> | |                    | <IPV6>}     |
| [key [plaintext |                    | <PASSKEY> | |        | ciphertext           | <PASSKEY>]] |
| [timeout        | <TIMEOUT-SECONDS>] |           |          | [port <PORT-NUMBER>] |             |
[auth-type {pap | chap}] [tracking {enable | disable}] [vrf <VRF-NAME>]
| no tacacs-server |                    | host      | {<FQDN> | | <IPV4>             | | <IPV6>}   |
| ---------------- | ------------------ | --------- | ------- | -------------------- | ----------- |
| [key [plaintext  |                    | <PASSKEY> | |       | ciphertext           | <PASSKEY>]] |
| [timeout         | <TIMEOUT-SECONDS>] |           |         | [port <PORT-NUMBER>] |             |
[auth-type {pap | chap}] [tracking {enable | disable}] [vrf <VRF-NAME>]
Description
AddsaTACACS+server.Bydefault,theTACACS+serverisassociatedwiththeservergroupnamed
tacacs.
ThenoformofthiscommandremovesapreviouslyaddedTACACS+server.
| Parameter |        |           |     | Description |     |
| --------- | ------ | --------- | --- | ----------- | --- |
| {<FQDN> | | <IPV4> | | <IPv6>} |     |             |     |
SpecifiestheTACACS+serveras:
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
n <IPV6>:anIPv6address.
key [plaintext <PASSKEY> | Selectseitheraplaintextoranencryptedlocalshared-secret
ciphertext <PASSKEY>] passkeyfortheserver.AsperRFC2865,shared-secretcanbea
mixofalphanumericandspecialcharacters.Plaintextpasskeys
arebetween1and32alphanumericandspecialcharacters.
RemoteAAA(TACACS+,RADIUS)commands|156

Parameter

Description

NOTE: When key is entered without either sub-parameter,
plaintext passkey prompting occurs upon pressing Enter. Enter
must be pressed immediately after the key parameter without
entering other parameters. The entered passkey characters are
masked with asterisks. When key is omitted, the server uses the
global passkey. This command requires either the global or local
passkey to be set; otherwise the server will not be contacted.
Command tacacs-server key is available for setting the global
passkey.

timeout

<TIMEOUT-SECONDS>

Specifies the timeout. Range: 1 to 60 seconds. Default : 5 seconds.

port <PORT-NUMBER>

auth-type {pap | chap}

tracking {enable | disable}

vrf <VRF-NAME>

Usage

Specifies the TCP authentication port number. Range: 1 to 65535.
Default: 49.

Selects either the PAP (the default) or CHAP authentication types.
If this parameter is not specified, the TACACS+ global default is
used.

Enables or disables server tracking for the RADIUS server. Tracked
servers are probed at the start of each server tracking interval to
check if they are reachable.
Use command tacacs-server tracking to configure TACACS+
server tracking globally.

Specifies the VRF name to be used for communicating with the
server. If no VRF name is provided, the default VRF named
default is used.

If the fully qualified domain name is provided for the TACACS+ server, a DNS server must be configured
and accessible through the same VRF which is configured for the TACACS+ server. This configuration is
required for the resolution of the TACACS+ server hostname to its IP address. If a DNS server is not
available for this VRF, the TACACS+ servers reachable through this VRF must be configured by means of
their IP addresses only.

Examples

Adding a TACACS+ server with an IPv4 address, plaintext passkey, timeout, port, authentication type,
and VRF name:

switch(config)# tacacs-server host 1.1.1.3 key plaintext test-123 timeout 15 port
32 auth-type chap vrf vrf_red

Adding a TACACS+ server with an IPv4 address and prompted plaintext passkey:

switch(config)# tacacs-server host 1.1.1.5 key
Enter the TACACS server key: *********
Re-Enter the TACACS server key: *********

Adding a TACACS+ server with an IPv4 address and a named VRF:

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

157

| switch(config)# | tacacs-server |     | host 1.1.1.1 | vrf mgmt |     |
| --------------- | ------------- | --- | ------------ | -------- | --- |
AddingaTACACS+serverwithanIPv4address,aport,andanamedVRF:
| switch(config)# | tacacs-server |     | host 1.1.1.2 | port 32 vrf | mgmt |
| --------------- | ------------- | --- | ------------ | ----------- | ---- |
AddingaTACACS+serverwithanFQDN,atimeout,portnumber,andanamedVRF:
switch(config)# tacacs-server host abc.com timeout 15 port 32 vrf vrf_blue
AddingaTACACS+serverwithanIPv6address:
switch(config)# tacacs-server host 2001:0db8:85a3:0000:0000:8a2e:0370:7334
DeletingaTACACS+serverwithanIPv4addressandspecifiedVRF:
| switch(config)# | no  | tacacs-server | host 1.1.1.1 | vrf mgmt |     |
| --------------- | --- | ------------- | ------------ | -------- | --- |
DeletingaTACACS+serverwithanFQDN,port,andspecifiedVRF:
switch(config)# no tacacs-server host abc.com port 32 vrf vrf_blue
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| tacacs-server | key |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
tacacs-server key [plaintext <GLOBAL-PASSKEY> | ciphertext <GLOBAL-PASSKEY>]
no tacacs-server key [plaintext <GLOBAL-PASSKEY> | ciphertext <GLOBAL-PASSKEY>]
Description
CreatesormodifiesaTACACS+globalpasskey.TheTACACS+globalpasskeyisusedasashared-secret
forencryptingthecommunicationbetweenallTACACS+serversandtheswitch.TheTACACS+global
passkeyisrequiredforauthenticationunlesslocalpasskeyshavebeenset.Bydefault,theTACACS+
globalpasskeyisempty.Iftheadministratorhasnotsetthiskey,theswitchwillnotbeabletoperform
TACACS+authentication.Theswitchwillinsteadrelyontheauthenticationmechanismconfiguredwith
login.
aaa authentication
RemoteAAA(TACACS+,RADIUS)commands|158

Whenthiscommandisenteredwithoutparameters,plaintextpasskeypromptingoccursuponpressingEnter.
Theenteredpasskeycharactersaremaskedwithasterisks.
Thenoformofthecommandremovestheglobalpasskey.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
plaintext <GLOBAL-PASSKEY> SpecifiestheTACACS+globalpasskeyinplaintextformatwitha
lengthof1to31characters.AsperRFC2865,ashared-secretcan
beamixofalphanumericandspecialcharacters.
ciphertext <GLOBAL-PASSKEY> SpecifiestheTACACS+globalpasskeyinencryptedformat.
Examples
Addingtheglobalpasskey:
| switch(config)# |     | tacacs-server |     |     | key plaintext | mypasskey123 |
| --------------- | --- | ------------- | --- | --- | ------------- | ------------ |
Addingtheglobalpasskeywithprompting:
| switch(config)# |        | tacacs-server |        |                | key       |     |
| --------------- | ------ | ------------- | ------ | -------------- | --------- | --- |
| Enter the       | TACACS | server        |        | key: ********* |           |     |
| Re-Enter        | the    | TACACS        | server | key:           | ********* |     |
Removingtheglobalpasskey:
| switch(config)# |             | no  | tacacs-server |     | key          |     |
| --------------- | ----------- | --- | ------------- | --- | ------------ | --- |
| Command         | History     |     |               |     |              |     |
| Release         |             |     |               |     | Modification |     |
| 10.07orearlier  |             |     |               |     | --           |     |
| Command         | Information |     |               |     |              |     |
| Platforms       | Command     |     | context       |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| tacacs-server    |         | timeout |          |     |     |     |
| ---------------- | ------- | ------- | -------- | --- | --- | --- |
| tacacs-server    | timeout |         | [<1-60>] |     |     |     |
| no tacacs-server |         | timeout | [<1-60>] |     |     |     |
Description
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 159

SpecifiesthenumberofsecondstowaitforaresponsefromtheTACACS+serverbeforetryingthenext
TACACS+server.Ifavalueisnotspecified,adefaultvalueof5secondsisused.Youcanoverridethis
valuewithafine-grainedperservertimeoutconfiguredforindividualservers.
ThenoformofthiscommandresetstheTACACS+globalauthenticationtimeouttothedefaultof5
seconds.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
timeout <1-60> Specifiesthetimeoutintervalof1to60seconds.Default:5
seconds.
Examples
SpecifyingtheTACACS+servertimeout:
| switch(config)# |     | tacacs-server |     | timeout | 10  |     |
| --------------- | --- | ------------- | --- | ------- | --- | --- |
ResettingthetimeoutfortheTACACS+servertothedefault:
| switch(config)# |             | no  | tacacs-server |     | timeout      |     |
| --------------- | ----------- | --- | ------------- | --- | ------------ | --- |
| Command         | History     |     |               |     |              |     |
| Release         |             |     |               |     | Modification |     |
| 10.07orearlier  |             |     |               |     | --           |     |
| Command         | Information |     |               |     |              |     |
| Platforms       | Command     |     | context       |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| tacacs-server    |            | tracking |            |            |              |              |
| ---------------- | ---------- | -------- | ---------- | ---------- | ------------ | ------------ |
| tacacs-server    | tracking   |          | interval   | <INTERVAL> |              |              |
| no tacacs-server |            | tracking | interval   |            | [<INTERVAL>] |              |
| tacacs-server    | tracking   |          | user-name  | <NAME>     |              |              |
| [password        | [plaintext |          | <PASSWORD> |            | | ciphertext | <PASSWORD>]] |
no tacacs-server tracking [user-name [<NAME>] [ciphertext <PASSWORD>]]
Description
ConfiguresTACACS+servertrackingsettingsgloballyforallconfiguredTACACS+serversthathave
trackingenabledwiththetacacs-server hostcommandonindividualservers.
Thenoformofthecommandremovesthespecifiedconfiguration,revertingittoitsdefault.Theno
formwithuser-namealsoclearsthepassword(resetsittoempty).
RemoteAAA(TACACS+,RADIUS)commands|160

Parameter

Description

interval <INTERVAL>

user-name <NAME>

[password [plaintext <PASSWORD> |
ciphertext <PASSWORD>]]

Specifies the time interval, in seconds, to wait before
checking the server reachability status. Default: 300. Range
60 to 84600.

Specifies the user name (and optionally a password) to be
used for server checking. The default user name is tacacs-
tracking-user with an empty password.
The password is optional and may be entered as plaintext
or pasted in as ciphertext. The plaintext password is visible
as cleartext when entered but is encrypted thereafter.
Command history does show the password as cleartext.

NOTE: When password is entered without a following sub-
parameter, plaintext password prompting occurs upon
pressing Enter. The entered password characters are masked
with asterisks.

NOTE: The user does not have to be configured on the
server. Server tracking can still be performed with a user
which is not configured on the server because authentication
failure on the server achieves confirmation that the server is
reachable.

NOTE: Server tracking uses authentication request and
response packets to determine server reachability status. The
server tracking user name and password are used to form
the request packet which is sent to the server with tracking
enabled. Upon receiving a response to the request packet,
the server is considered to be reachable.

Examples

Configuring a tracking interval of 120 seconds:

switch(config)# tacacs-server tracking interval 120

Reverting the tracking interval to its default of 300 seconds:

switch(config)# no tacacs-server tracking interval

Configuring user tacacs-tracker with a plaintext password.

switch(config)# tacacs-server tracking user-name tacacs-tracker password plaintext
track$1

Configuring user tacacs-tracker with a prompted plaintext password.

switch(config)# tacacs-server tracking user-name tacacs-tracker password
Enter the TACACS server tracking password: *******
Re-Enter the TACACS server tracking password: *******

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

161

Revertingthetrackingusernametoitsdefaultoftacacs-tracking-user:
| switch(config)#     | no      | tacacs-server | tracking user-name |
| ------------------- | ------- | ------------- | ------------------ |
| Command History     |         |               |                    |
| Release             |         |               | Modification       |
| 10.07orearlier      |         |               | --                 |
| Command Information |         |               |                    |
| Platforms           | Command | context       | Authority          |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
RemoteAAA(TACACS+,RADIUS)commands|162

Chapter 11

PKI

PKI

The public key infrastructure (PKI) feature enables administrators to manage digital certificates on the
switch. The switch uses certificates to validate SSH clients when acting as an SSH server, and when
communicating with syslog servers when TLS encryption is used.

PKI concepts

Digital certificate

A digital certificate is an electronic form of identification that stores important information about an
entity (such as a computer, program, or website). Certificates help secure digital transactions by
enabling the end parties to validate each other's identity. Digital certificates are issued by a certificate
authority (CA) and are composed of an encoded string of characters (usually stored in a file). For
example:
-----BEGIN CERTIFICATE-----
MIIDsDCCApgCCQDJotuPPj9GCDANBgkqhkiG9w0BAQsAADCBqzELMAkGA1UEBh
VVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEDAOBgNVBAcBM1JvY2tsaW4xDDAKBg
BAoMA0hQTjEVMBMGA1UECwwMSFBOUm9zZXZpbGxlMSokwAYDVQQDDCFocG5zdz
...
MioDy0096DvSMPsnOaI+jnZ3AozN8y+nLgotXUsg36pO/Ncc51oQhyUdcAbgA1
rzSLgyTnpXZKumvlaoTk3pzrIf7m5V103GTbgHGSFCzgO6QWxVxu9d7ju1o59S
aOIT7JSsYI5LsLpVz9ZqS599rj/lLoH+rLNlRDVXpS+J51
-----END CERTIFICATE-----

The switch can import PEM encoded ITU-T X.509 v3 certificates. (Certificates can be converted to human-
readable form using a software decoder.)

An X.509 digital certificate typically includes the following information:

n Signature algorithm: The cryptographic algorithm used to generate the digital signature.

n Signature value: Digital signature of the certificate generated using the CA's private key.

n Version number: X.509 version number.

n Serial number: Certificate serial number.

n Issuer name: Name of the certificate authority (CA) that issued the certificate.

n Validity period: Beginning and ending dates.

n Subject name: Name of the entity to which the certificate is issued.

n Subject public key and key algorithm.

n Key usage extension: Purpose of the certificate.

Certificate authority

A certificate authority (CA) is an entity that can issue and sign digital certificates. A CA can be a well-
known, trusted commercial company, or a private entity controlled by your organization. For a
commercial CA, the CA validates the credentials of a user before issuing a certificate and signing it,
guaranteeing a certificate holder's identity. For a private CA, self-signed certificates can be generated as
needed for devices on your network without paying a commercial company.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

163

Root certificate

A root certificate is a self-signed certificate that is deemed the root of trust for a certificate chain. This is
the certificate that identifies a CA, and is used by the CA to sign any certificates that it issues. When two
peers attempt to establish a secure connection, they use the CA's public key to verify that each other's
certificates were indeed signed by a trusted certificate authority.

Each root CA certificate has a unique fingerprint, which is the hash value of the certificate content. The
fingerprint of a root CA certificate can be used to authenticate the validity of the root CA.

In a certificate chain, the root CA generates a self-signed certificate, and each lower level CA holds a CA
certificate (intermediate certificate) issued by the CA immediately above it. The hierarchy of these
certificates forms a chain of trust.

Leaf certificate

This is the certificate used by a software entity, such as a syslog client, to identify itself to a peer when
establishing a secure connection.

Intermediate certificate

An intermediate certificate is a CA which has been issued by the root certificate or by another
intermediate certificate. Intermediate CAs can issue leaf certificates and sit in between the root and leaf
certificates. The use of an intermediate CA allows administrators to segregate their PKI groups.

Trust anchor

This is the certificate that acts as the base of trust for the validation of other certificates. A trust anchor
can be a root or intermediate certificate issued by a CA.

OCSP

The online certificate status protocol (OCSP) is a real-time method for determining the revocation status
of a certificate. When two peers attempt to establish a secure connection, they can query an OCSP
responder to determine the status (valid or revoked) of each other's certificates. The OCSP responder
for a certificate is typically provided by a server managed by the CA that issued the certificate.

PKI on the switch

The AOS-CX Switch Series switches provides for installation of certificate authority (CA) certificates and
the generation and installation of leaf certificates.

Trust anchor profiles

The switch supports 64 trust anchor (TA) profiles. Each TA profile stores a trusted CA certificate. The
certificate can be either a root CA certificate, which must be self-signed, or an intermediate CA
certificate that is issued by another CA.

The certificate must have its BasicConstraints field with CA key set to true, and its KeyUsage extension field
set with keyCertSign and/or cRLSign.

CA certificates are used to:

PKI | 164

n Validate the certificates that remote peers present when attempting to establish a secure connection

with a service on the switch, for example, the SSH server.

n Validate leaf certificates installed on the switch that are used, for example, by the syslog client, the

Web UI, or REST API.

The TA profile also enables configuration of real-time checking of certificate revocation (through OCSP).

Leaf certificates

Leaf certificates can be installed on the switch for use by features such as the syslog client, the Web UI,
or REST API. If you are purchasing a certificate from a trusted CA, the switch can generate the certificate
signing request (CSR) that is used to obtain the certificate. The switch can also directly generate self-
signed certificates. Alternatively, the certificate and private key can be generated outside the switch and
then imported. X509 certificate management software such as OpenSSL can be used to generate the
private key and CSR and then combine the certificate and private key into one PEM or PKCS#12 file
suitable for importation into the switch.

Mandatory matching of peer device hostname

While validating the peer device certificates, the switch checks that the peer device configured
hostname matches either the Subject Alternative Name (SAN) field or the Common Name (CN) within
the certificate Subject field. If the SAN field is present and matches the hostname, validation succeeds,
otherwise it fails. If the SAN field is not present, and the CN matches the hostname, validation succeeds,
otherwise it fails.

PKI EST

EST (Enrollment over Secure Transport) (RFC 7030) defines the protocol that devices use to request
trusted certificate authority (CA) certificates and to enroll / re-enroll device certificates from CA services
using secure channels, specifically HTTP over TLS.

Devices can be configured to request the trusted CA certificates and to request enrollment, and re-
enrollment of device certificates automatically, without the need for administrator intervention, while
maintaining the security and integrity of the whole enrollment process.

The switch includes an EST client implemented as a part of the PKI infrastructure.

For detailed CLI command descriptions, see:

n PKI commands

n PKI EST commands

EST usage overview

n The EST client on the switch requires EST profile configuration, including EST server URL and the VRF

providing HTTP connection to the EST server.

n At the time the URL is set in the EST profile, the switch connects to the EST server and downloads the

trusted CA certificate chain. To accommodate CA certificate updates, the certificate chain is also
downloaded before a certificate enrollment or re-enrollment is attempted.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

165

n ESTsupportsupto:
o 16ESTprofiles
o 63trustedCAcertificatesdownloadedfromESTservers.
o 18devicecertificatesenrolledthroughESTservices.
n ESTprofileconfigurationissupportedthroughtheCLIandtheRESTAPIPKI_EST_Profile.
n CAcertificaterequestanddevicecertificateenrollmentissupportedthroughtheCLIandtheREST
customAPICertificateManager /certificate.
| Prerequisites | for | using EST for | certificate | enrollment |
| ------------- | --- | ------------- | ----------- | ---------- |
n EstablishthePKIinfrastructureforyouorganization,withtheCAchainandservicereadytoissue
certificates.IssueaservicecertificatefortheESTserver.
n InstalltherootCAcertificateinaTAprofileontheswitchthatwillvalidatetheESTservercertificate
usingCLIcommandscryptopki ta-profileandta-certificate.
n Optionally,preconfigureanESTclientcertificateontheswitch.
n MaketheESTserverreachablefromtheswitch.ConnecttheCAservice(s)totheESTserver.Ifthereis
aclientcertificatefortheESTclient,installtherootCAcertificateontheserverthatwillvalidatethe
clientcertificate.
| EST profile | configuration |     |     |     |
| ----------- | ------------- | --- | --- | --- |
Intheglobalconfigurationcontext,createanESTprofileandenteritscontext:
| crypto pki | est-profile | <EST-NAME> |     |     |
| ---------- | ----------- | ---------- | --- | --- |
InanESTprofilecontext,configuretheESTprofileparametersusingthesecommands:
url <URL>
vrf <VRF-NAME>
username <USERNAME> password [ciphertext <CIPHERTEXT-PASSWORD> |
|                              |            | plaintext   | <PLAINTEXT-PASSWORD>] |     |
| ---------------------------- | ---------- | ----------- | --------------------- | --- |
| retry-interval               | <INTERVAL> |             |                       |     |
| retry-count                  | <RETRIES>  |             |                       |     |
| arbitrary-label              | <LABEL>    |             |                       |     |
| arbitrary-label-enrollment   |            | <LABEL>     |                       |     |
| arbitrary-label-reenrollment |            | <LABEL>     |                       |     |
| reenrollment-lead-time       |            | <LEAD-TIME> |                       |     |
| Certificate                  | enrollment |             |                       |     |
Intheglobalconfigurationcontext,createacertificateandenteritscontext:
| crypto pki | certificate | <CERT-NAME> |     |     |
| ---------- | ----------- | ----------- | --- | --- |
Inacertificateconfigurationcontext,configurethecertificateparameters:
key-type {rsa [key-size <K-SIZE>] | ecdsa [curve-size <C-SIZE>]}
| subject | [common-name | <COMMON-NAME>] |     |     |
| ------- | ------------ | -------------- | --- | --- |
|         | [country     | <COUNTRY>]     |     |     |
|         | [locality    | <LOCALITY>]    |     |     |
[org <ORG-NAME>]
|     | [org-unit       | <ORG-UNIT>] |     |     |
| --- | --------------- | ----------- | --- | --- |
|     | [state <STATE>] |             |     |     |
Inacertificateconfigurationcontext,enrollthecertificateusinganESTservice:
| enroll est-profile | <EST-NAME>    |     |     |     |
| ------------------ | ------------- | --- | --- | --- |
| Certificate        | re-enrollment |     |     |     |
PKI|166

n The re-enrollment request is sent automatically to the same EST server that was used for the original

enrollment.

n The switch presents the enrolled certificate being re-enrolled to the EST server for authentication. If

the certificate has expired or authentication fails for any reason, the switch falls back to using the EST
client certificate or the username and password in the EST profile, whichever is configured, and
performs a new certificate enrollment.

n Re-enrollment lead-time is configurable in the EST profile using CLI command reenrollment-lead-
time. It sets the number of days before certificate expiry date that certificate re-enrollment will be
initiated.

Checking EST profile and certificate configuration

Show the list of EST profiles or details of a specific EST profile:
show crypto pki est-profile [<EST-NAME>]

Show a list of TA profiles whether directly configured or EST-enrolled, or details of a specific TA profile:
show crypto pki ta-profile [<TA-NAME>]

Show the list of certificates whether directly configured or EST-enrolled, or details of a specific
certificate:
show crypto pki certificate [<CERT-NAME> [plaintext | pem]]

Show all certificates assigned to the switch EST client as well as certificates that are assigned to other
applications on the switch.:
show crypto pki application

EST best practices

Ensure the following:

n A time synchronization service is used on both the switch (the EST client) and the EST server.

n In all CA certificates, the Basic Constraints field has CA set to true, pathlen is set appropriately, and

Key Usage is set with keyCertSign.

n In all leaf certificates, the Extended Key Usage field is set with the appropriate purpose as follows:

o For server certificates, set with serverAuth. The Key Usage field has at least one of

digitalSignature, keyEncipherment, or keyAgreement.

o For client certificates, set with clientAuth. The Key Usage field has at least one of

digitalSignature, or keyAgreement.

n The EST server is configured to include the intermediate issuer CA certificates in the trusted CA

certificate chain that the EST server sends to the switch (the EST client) upon request.

Example using EST for certificate enrollment

This example illustrates the configuration of an EST profile and enrolling application certificates using an
EST server.

Prerequisites:

n An EST server is reachable from the switch management port.

n Availability of the root CA certificate used to validate the server certificate.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

167

Thisexampleshowsthefollowing:
n InstallingtherootCAcertificateasaTAprofileforvalidationoftheESTservercertificate.
n ConfiguringanESTprofilewiththeESTserverinformation,includingtheusernameandpasswordfor
clientauthenticationandtheESTserverURL.
n IssuingarequesttoenrollaleafcertificateusingtheESTserver.
n AssigningtheenrolledcertificatetotheESTclientandsyslogclientontheswitch.
Eachsectioninthebelowexampleisprecededbydescriptivetext.
Example
================================================================================
| The switch | in its default | configuration | state. |
| ---------- | -------------- | ------------- | ------ |
================================================================================
| switch# | show running-config |     |     |
| ------- | ------------------- | --- | --- |
| Current | configuration:      |     |     |
!
| !Version          | AOS-CX FL.10.06.0001CM |     |     |
| ----------------- | ---------------------- | --- | --- |
| !export-password: | default                |     |     |
user admin group administrators password ciphertext AQBapTLgcT+DNrtd0bmdXIP2L0AY
NUpwwyQEIZX4oMKtwlXcYgAAAOmKlfxH+ugf3Fe2JuWar2uKG7A/R6bqMO/ZHS364NOmpXV/Ko37ZhCq
cFpaOJsk01+IJPRUkbpigCeEObM67Od8/vrASJaO6EAj+RBnWCrifwdChcUUS3XpbCUl7dmxYHNg
!
!
| ssh server | vrf default |     |     |
| ---------- | ----------- | --- | --- |
| ssh server | vrf mgmt    |     |     |
| vsf member | 1           |     |     |
| type       | jl668a      |     |     |
vlan 1
spanning-tree
| interface | mgmt |     |     |
| --------- | ---- | --- | --- |
no shutdown
ip dhcp
| interface | 1/1/1 |     |     |
| --------- | ----- | --- | --- |
no shutdown
no routing
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/2    |     |     |
no shutdown
no routing
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/3    |     |     |
no shutdown
no routing
| vlan | access 1 |     |     |
| ---- | -------- | --- | --- |
...
| interface | 1/1/26 |     |     |
| --------- | ------ | --- | --- |
no shutdown
no routing
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/27   |     |     |
no shutdown
no routing
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | 1/1/28   |     |     |
no shutdown
no routing
| vlan      | access 1 |     |     |
| --------- | -------- | --- | --- |
| interface | vlan 1   |     |     |
PKI|168

ip dhcp
!
!
| https-server |     | vrf default |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| https-server |     | vrf mgmt    |     |     |     |     |     |     |     |     |
switch#
================================================================================
The mgmt port is connected to a network with DNS available and the
| EST server | reachable. |     |     |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
================================================================================
| switch#                  | show       | interface       | mgmt |     |                              |     |     |     |     |     |
| ------------------------ | ---------- | --------------- | ---- | --- | ---------------------------- | --- | --- | --- | --- | --- |
| Address                  | Mode       |                 |      |     | : dhcp                       |     |     |     |     |     |
| Admin                    | State      |                 |      |     | : up                         |     |     |     |     |     |
| Mac Address              |            |                 |      |     | : 38:21:c7:59:cd:81          |     |     |     |     |     |
| IPv4 address/subnet-mask |            |                 |      |     | : 999.100.205.146/24         |     |     |     |     |     |
| Default                  | gateway    | IPv4            |      |     | : 999.100.205.1              |     |     |     |     |     |
| IPv6 address/prefix      |            |                 |      |     | :                            |     |     |     |     |     |
| IPv6 link                | local      | address/prefix: |      |     | fe80::3a21:c7ff:fe59:cd81/64 |     |     |     |     |     |
| Default                  | gateway    | IPv6            |      |     | :                            |     |     |     |     |     |
| Primary                  | Nameserver |                 |      |     | :                            |     |     |     |     |     |
| Secondary                | Nameserver |                 |      |     | :                            |     |     |     |     |     |
switch#
================================================================================
Configure the root CA cert as a TA profile that will validate the server cert.
================================================================================
| switch# | config |     |     |     |     |     |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
switch(config)#
| switch(config)# |     | crypto | pki | ta-profile |     | root-ca-for-est-server |     |     |     |     |
| --------------- | --- | ------ | --- | ---------- | --- | ---------------------- | --- | --- | --- | --- |
switch(config-ta-root-ca-for-est-server)#
switch(config-ta-root-ca-for-est-server)# ta-certificate import terminal
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-ta-cert)# |     |     |     | -----BEGIN |     | CERTIFICATE----- |     |     |     |     |
| ----------------------- | --- | --- | --- | ---------- | --- | ---------------- | --- | --- | --- | --- |
NVBAYTonfig-ta-cert)# MIIB2DCCAX6gAwIBAgIJAKtmJvZZy9RdMAoGCCqGSM49BAMCMGIxCzAJBg
QKEwNIonfig-ta-cert)# AlVTMQswCQYDVQQIEwJDQTESMBAGA1UEBxMJUm9zZXZpbGxlMQwwCgYDVQ
0yMDA1onfig-ta-cert)# UEUxDjAMBgNVBAsTBUFydWJhMRQwEgYDVQQDEwtkYW5lc3Qtcm9vdDAeFw
...
YDVR0Ponfig-ta-cert)# VCnKTlhxfmV72nfxYpI979UsopuP5nCjHTAbMAwGA1UdEwQFMAMBAf8wCw
eo6yN0onfig-ta-cert)# BAQDAgEGMAoGCCqGSM49BAMCA0gAMEUCIQDb/uHvU8DFRTyfnP9wk1i6sd
c=00(config-ta-cert)# UvUO5t7/rrVxRQIgMHGjHhaN1nkjYBG8Ei3C1UDILiKlO7McMTCWVo4Ik5
| switch(config-ta-cert)# |     |     |     | -----END | CERTIFICATE----- |     |     |     |     |     |
| ----------------------- | --- | --- | --- | -------- | ---------------- | --- | --- | --- | --- | --- |
switch(config-ta-cert)#
The certificate you are importing has the following attributes:
Subject: C = US, ST = CA, L = Roseville, O = HPE, OU = Aruba, CN = danest-root
Issuer: C = US, ST = CA, L = Roseville, O = HPE, OU = Aruba, CN = danest-root
| Serial Number: |     | 0xAB6626FXXXXD45D |      |             |      |        |     |      |         |     |
| -------------- | --- | ----------------- | ---- | ----------- | ---- | ------ | --- | ---- | ------- | --- |
| TA certificate |     | import            | is   | allowed     | only | once   | for | a TA | profile |     |
| Do you want    | to  | accept            | this | certificate |      | (y/n)? |     | y    |         |     |
switch(config-ta-root-ca-for-est-server)#
| switch(config-ta-root-ca-for-est-server)# |     |     |     |     |     |     | exit |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
switch(config)#
| switch(config)# |      | show | crypto | pki | ta-profile |             |     |     |            |       |
| --------------- | ---- | ---- | ------ | --- | ---------- | ----------- | --- | --- | ---------- | ----- |
| TA Profile      | Name |      |        |     | TA         | Certificate |     |     | Revocation | Check |
-------------------------------- -------------------- ----------------
| root-ca-for-est-server |     |     |     |     | Installed, |     | valid |     | disabled |     |
| ---------------------- | --- | --- | --- | --- | ---------- | --- | ----- | --- | -------- | --- |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 169

switch(config)#
================================================================================
Configure the EST profile with the EST server URL, username/password.
================================================================================
| switch(config)# |     | crypto | pki | est-profile |     | test-est-server |     |     |     |
| --------------- | --- | ------ | --- | ----------- | --- | --------------- | --- | --- | --- |
switch(config-est-test-est-server)#
switch(config-est-test-est-server)# user fred password plaintext barney
switch(config-est-test-est-server)#
switch(config-est-test-est-server)#
url https://999.0.10.229:8443/.well-known/est
switch(config-est-test-est-server)#
| switch(config-est-test-est-server)# |     |     |     |     |     | exit |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
switch(config)#
================================================================================
At the time the EST URL is set, the switch sends a request to the EST server to
get the set of trusted CA certs. If that is successful, TA profiles will be
| auto-created |          | for those | CA          | certs. |     |             |          |     |     |
| ------------ | -------- | --------- | ----------- | ------ | --- | ----------- | -------- | --- | --- |
| Display      | the list | of        | TA profiles |        | and | EST profile | details. |     |     |
================================================================================
| switch(config)# |      | show | crypto | pki | ta-profile |             |     |            |       |
| --------------- | ---- | ---- | ------ | --- | ---------- | ----------- | --- | ---------- | ----- |
| TA Profile      | Name |      |        |     | TA         | Certificate |     | Revocation | Check |
-------------------------------- -------------------- ----------------
| test-est-server-est-ta00         |      |          |              |     | Installed,                                |                | valid           | OCSP     |     |
| -------------------------------- | ---- | -------- | ------------ | --- | ----------------------------------------- | -------------- | --------------- | -------- | --- |
| test-est-server-est-ta02         |      |          |              |     | Installed,                                |                | valid           | OCSP     |     |
| test-est-server-est-ta05         |      |          |              |     | Installed,                                |                | valid           | OCSP     |     |
| test-est-server-est-ta01         |      |          |              |     | Installed,                                |                | valid           | OCSP     |     |
| root-ca-for-est-server           |      |          |              |     | Installed,                                |                | valid           | disabled |     |
| test-est-server-est-ta04         |      |          |              |     | Installed,                                |                | valid           | OCSP     |     |
| test-est-server-est-ta03         |      |          |              |     | Installed,                                |                | valid           | OCSP     |     |
| switch(config)#                  |      | show     | crypto       | pki | est-profile                               |                |                 |          |     |
|                                  |      |          |              |     | Downloaded                                |                | Enrolled        |          |     |
| Profile                          | Name |          |              |     | TA                                        | Profiles       | Certificates    |          |     |
| -------------------------------- |      |          |              |     | -----------                               |                | ------------    |          |     |
| test-est-server                  |      |          |              |     |                                           |                | 6               | 1        |     |
| switch(config)#                  |      | show     | crypto       | pki | est-profile                               |                | test-est-server |          |     |
| Profile                          | Name |          |              | :   | test-est-server                           |                |                 |          |     |
| Service                          | VRF  |          |              | :   | mgmt                                      |                |                 |          |     |
| Service                          | URL  |          |              | :   | https://999.0.10.229:8443/.well-known/est |                |                 |          |     |
| Arbitrary                        |      | Label    |              |     | :                                         | not configured |                 |          |     |
| Arbitrary                        |      | Label    | Enrollment   |     | :                                         | not configured |                 |          |     |
| Arbitrary                        |      | Label    | Reenrollment |     | :                                         | not configured |                 |          |     |
| Authentication                   |      | Username |              | :   | fred                                      |                |                 |          |     |
| Authentication                   |      | Password |              | :   |                                           |                |                 |          |     |
AQBapR7ndgoxkMlWQUQvK+Dvd3S6m+s9fdaPQwdkMbIYEMnMBgAAAHRhhliYwA==
| Retry        | Interval     |             |      | :   | 30 seconds |     |     |     |     |
| ------------ | ------------ | ----------- | ---- | --- | ---------- | --- | --- | --- | --- |
| Retry        | Count        |             |      | :   | 3 times    |     |     |     |     |
| Reenrollment |              | Lead        | Time | :   | 2 days     |     |     |     |     |
| Downloaded   |              | TA Profiles |      | :   | 6          |     |     |     |     |
| Enrolled     | Certificates |             |      | :   |            |     |     |     |     |
cert-for-app
switch(config)#
PKI|170

================================================================================
| Originally, | the | switch | only | has | two | built-in | certificates. |     |     |     |
| ----------- | --- | ------ | ---- | --- | --- | -------- | ------------- | --- | --- | --- |
================================================================================
| switch(config)# |     | show | crypto | pki | certificate |     |     |     |     |     |
| --------------- | --- | ---- | ------ | --- | ----------- | --- | --- | --- | --- | --- |
Certificate Name Cert Status EST Status Associated Applications
---------------------- -------------- ----------------- --------------------------
----
| local-cert |     |     | installed |     |     | n/a |     |     | captive-portal, | est- |
| ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --------------- | ---- |
client,
|     |     |     |     |     |     |     |     |     | https-server, | radsec- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- |
client,
syslog-client
| device-identity |     |     | installed |     |     | n/a |     |     | none |     |
| --------------- | --- | --- | --------- | --- | --- | --- | --- | --- | ---- | --- |
switch(config)#
================================================================================
fields.
Create a new certificate, configure its key type, key size, and subject
================================================================================
| switch(config)# |     | crypto | pki | certificate |     | cert-for-app |     |     |     |     |
| --------------- | --- | ------ | --- | ----------- | --- | ------------ | --- | --- | --- | --- |
switch(config-cert-cert-for-app)#
switch(config-cert-cert-for-app)# key-type ecdsa curve-size 521
switch(config-cert-cert-for-app)#
| switch(config-cert-cert-for-app)# |     |     |     |     | subject |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
Do you want to use the switch serial number as the common name (y/n)? n
| Common Name: |     | 999.100.205.146 |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Org Unit:
Aruba-Roseville
| Org Name: | HPE       |     |     |     |     |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Locality: | Roseville |     |     |     |     |     |     |     |     |     |
State: CA
| Country: | US  |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
switch(config-cert-cert-for-app)#
================================================================================
| Request | to enroll | the | certificate |     | through | the | EST | server. |     |     |
| ------- | --------- | --- | ----------- | --- | ------- | --- | --- | ------- | --- | --- |
================================================================================
switch(config-cert-cert-for-app)# enroll est-profile test-est-server
| You are  | enrolling | a      | certificate  |     | with | the following       |     | attributes: |        |     |
| -------- | --------- | ------ | ------------ | --- | ---- | ------------------- | --- | ----------- | ------ | --- |
| Subject: | C=US,     | ST=CA, | L=Roseville, |     |      | OU=Aruba-Roseville, |     |             | O=HPE, |     |
CN=999.100.205.146
| Key Type: | ECDSA  | (521) |     |     |     |     |     |     |     |     |
| --------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| Continue  | (y/n)? | y     |     |     |     |     |     |     |     |     |
Certificate enrollment via test-est-server has been initiated. Please use
'show crypto pki certificate cert-for-app' to check its status.
switch(config-cert-cert-for-app)#
================================================================================
Check the cert status to see if enrollment is successful. It is.
================================================================================
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 171

| switch(config-cert-cert-for-app)# |     |     | show | crypto pki | certificate |     |
| --------------------------------- | --- | --- | ---- | ---------- | ----------- | --- |
Certificate Name Cert Status EST Status Associated Applications
---------------------- -------------- ----------------- --------------------------
----
| local-cert |     | installed |     | n/a | captive-portal, | est- |
| ---------- | --- | --------- | --- | --- | --------------- | ---- |
client,
|     |     |     |     |     | https-server, | radsec- |
| --- | --- | --- | --- | --- | ------------- | ------- |
client,
syslog-client
| device-identity |     | installed |     | n/a            | none |     |
| --------------- | --- | --------- | --- | -------------- | ---- | --- |
| cert-for-app    |     | installed |     | enroll success | none |     |
switch(config-cert-cert-for-app)#
| switch(config-cert-cert-for-app)# |     |     | exit |     |     |     |
| --------------------------------- | --- | --- | ---- | --- | --- | --- |
switch(config)#
| switch(config)# | show          | crypto pki   | certificate | cert-for-app | pem |     |
| --------------- | ------------- | ------------ | ----------- | ------------ | --- | --- |
| Certificate     | Name:         | cert-for-app |             |              |     |     |
| Associated      | Applications: |              |             |              |     |     |
est-client
| Certificate | Status: | installed |     |     |     |     |
| ----------- | ------- | --------- | --- | --- | --- | --- |
| EST Status: | enroll  | success   |     |     |     |     |
| Certificate | Type:   | regular   |     |     |     |     |
Intermediates:
Subject: C = US, ST = CA, O = HPE, OU = Aruba, CN = danest-int2
| Issuer: | C = US, | ST = CA, | O = HPE, | OU = Aruba, | CN = danest-int1 |     |
| ------- | ------- | -------- | -------- | ----------- | ---------------- | --- |
| Serial  | Number: | 0x02     |          |             |                  |     |
Subject: C = US, ST = CA, O = HPE, OU = Aruba, CN = danest-int1
Issuer: C = US, ST = CA, L = Roseville, O = HPE, OU = Aruba, CN = danest-
root
| Serial | Number: | 0x01 |     |     |     |     |
| ------ | ------- | ---- | --- | --- | --- | --- |
Subject: C = US, ST = CA, L = Roseville, O = HPE, OU = Aruba, CN = danest-root
Issuer: C = US, ST = CA, L = Roseville, O = HPE, OU = Aruba, CN = danest-
root
| Serial     | Number:          | 0xAB6626FXXXXD45D |     |     |     |     |
| ---------- | ---------------- | ----------------- | --- | --- | --- | --- |
| -----BEGIN | CERTIFICATE----- |                   |     |     |     |     |
MIICizCCAjKgAwIBAgICAIgwCQYHKoZIzj0EATBOMQswCQYDVQQGEwJVUzELMAkG
A1UECBMCQ0ExDDAKBgNVBAoTA0hQRTEOMAwGA1UECxMFQXJ1YmExFDASBgNVBAMT
C2RhbmVzdC1pbnQyMB4XDTIwMTAyODE5NTczOVoXDTIwMTEyNTE5NTczOVowbzEL
...
RTEOMAwGA1UECxMFQXJ1YmExFDASBgNVBAMTC2RhbmVzdC1pbnQxggECMAkGByqG
SM49BAEDSAAwRQIgVC1kVIewXhpBSQVqVsQ36MbzrhR4XsaGbQeu7+O8gbUCIQCH
cS17gcLbNxJ1WVr2jnZpPBxy9vID38FjirJiGZ5cZw==
| -----END   | CERTIFICATE----- |     |     |     |     |     |
| ---------- | ---------------- | --- | --- | --- | --- | --- |
| -----BEGIN | CERTIFICATE----- |     |     |     |     |     |
MIIBpzCCAU2gAwIBAgIBAjAJBgcqhkjOPQQBME4xCzAJBgNVBAYTAlVTMQswCQYD
VQQIEwJDQTEMMAoGA1UEChMDSFBFMQ4wDAYDVQQLEwVBcnViYTEUMBIGA1UEAxML
ZGFuZXN0LWludDEwHhcNMjAwNTIwMDUyNDExWhcNMzAwNTE4MDUyNDExWjBOMQsw
...
7ovbXodgN8lqDvBl1VTJYlLBSzl9FKMdMBswDAYDVR0TBAUwAwEB/zALBgNVHQ8E
BAMCAQYwCQYHKoZIzj0EAQNJADBGAiEA+i3x7KEZsxObVruM1kwqWe+QXiLKbgNL
fL077jsSMhYCIQD/dFBkH/yN0NFzb3wI7OaooO83HY2p/47t2pIBk/JNfg==
| -----END   | CERTIFICATE----- |     |     |     |     |     |
| ---------- | ---------------- | --- | --- | --- | --- | --- |
| -----BEGIN | CERTIFICATE----- |     |     |     |     |     |
MIIBuTCCAWGgAwIBAgIBATAJBgcqhkjOPQQBMGIxCzAJBgNVBAYTAlVTMQswCQYD
VQQIEwJDQTESMBAGA1UEBxMJUm9zZXZpbGxlMQwwCgYDVQQKEwNIUEUxDjAMBgNV
BAsTBUFydWJhMRQwEgYDVQQDEwtkYW5lc3Qtcm9vdDAeFw0yMDA1MjAwNTE1MjNa
...
BgNVHRMEBTADAQH/MAsGA1UdDwQEAwIBBjAJBgcqhkjOPQQBA0cAMEQCIGrlZmBX
SmbhDvG9pRiXG0YMqVbvZd37jRQdE+mEk2jfAiBFGhzMjUadhQbuPUTNs9A7bdYk
PKI|172

wej0mJe5bRpd7sqwRQ==
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIB2DCCAX6gAwIBAgIJAKtmJvZZy9RdMAoGCCqGSM49BAMCMGIxCzAJBgNVBAYT
AlVTMQswCQYDVQQIEwJDQTESMBAGA1UEBxMJUm9zZXZpbGxlMQwwCgYDVQQKEwNI
UEUxDjAMBgNVBAsTBUFydWJhMRQwEgYDVQQDEwtkYW5lc3Qtcm9vdDAeFw0yMDA1
...
VCnKTlhxfmV72nfxYpI979UsopuP5nCjHTAbMAwGA1UdEwQFMAMBAf8wCwYDVR0P
BAQDAgEGMAoGCCqGSM49BAMCA0gAMEUCIQDb/uHvU8DFRTyfnP9wk1i6sdeo6yN0
UvUO5t7/rrVxRQIgMHGjHhaN1nkjYBG8Ei3C1UDILiKlO7McMTCWVo4Ik5c=
-----END CERTIFICATE-----
switch(config)#
================================================================================
| Initially, | all | applications | use the | default | local-cert. |     |     |
| ---------- | --- | ------------ | ------- | ------- | ----------- | --- | --- |
================================================================================
| switch(config)# |              | show | crypto pki application |      |     |             |     |
| --------------- | ------------ | ---- | ---------------------- | ---- | --- | ----------- | --- |
| Associated      | Applications |      | Certificate            | Name |     | Cert Status |     |
-------------------------- ------------------- ---------------------------------
| captive-portal |     |     |     |     | not | configured, | using local-cert |
| -------------- | --- | --- | --- | --- | --- | ----------- | ---------------- |
| est-client     |     |     |     |     | not | configured, | using local-cert |
| https-server   |     |     |     |     | not | configured, | using local-cert |
| radsec-client  |     |     |     |     | not | configured, | using local-cert |
| syslog-client  |     |     |     |     | not | configured, | using local-cert |
switch(config)#
================================================================================
| Assign | the newly | enrolled | cert to | applications | as  | desired. |     |
| ------ | --------- | -------- | ------- | ------------ | --- | -------- | --- |
In this example, the cert is assigned to the est-client and syslog.
================================================================================
switch(config)# crypto pki application est-client certificate cert-for-app
switch(config)# crypto pki application syslog-client certificate cert-for-app
switch(config)#
switch(config)#
|            |              | show | crypto pki application |      |      |        |     |
| ---------- | ------------ | ---- | ---------------------- | ---- | ---- | ------ | --- |
| Associated | Applications |      | Certificate            | Name | Cert | Status |     |
-------------------------- ------------------- ------------------------------
| captive-portal |     |     |              |     | not   | configured, | using local-cert |
| -------------- | --- | --- | ------------ | --- | ----- | ----------- | ---------------- |
| est-client     |     |     | cert-for-app |     | valid |             |                  |
| https-server   |     |     |              |     | not   | configured, | using local-cert |
| radsec-client  |     |     |              |     | not   | configured, | using local-cert |
| syslog-client  |     |     | cert-for-app |     | valid |             |                  |
switch(config)#
| Example | including |     | the use | of an | intermediate |     | certificate |
| ------- | --------- | --- | ------- | ----- | ------------ | --- | ----------- |
Thisexampleshowsthefollowing:
n InstallingarootCAasaTAprofile.
n CreatingaCSRforaleafcertificate.
n InstallingthesignedleafcertificateissuedbyanintermediateCA.TheintermediateCAcertificateis
includedafterthesignedleafcertificate.
Eachsectioninthebelowexampleisprecededbydescriptivetext.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 173

Example
================================================================================
| Install | root | CA as | a TA | profile |     |     |     |
| ------- | ---- | ----- | ---- | ------- | --- | --- | --- |
================================================================================
| switch(config)#         |     | crypto | pki | ta-profile     |     | root   |          |
| ----------------------- | --- | ------ | --- | -------------- | --- | ------ | -------- |
| switch(config-ta-root)# |     |        |     | ta-certificate |     | import | terminal |
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-ta-cert)# |     |     |     | -----BEGIN |     | CERTIFICATE----- |     |
| ----------------------- | --- | --- | --- | ---------- | --- | ---------------- | --- |
switch(config-ta-cert)# MIIGATCCA+mgAwIBAgIJAL/JIZfJ0GpcMA0GCSqGSIUAMIGOMQswCQYD
switch(config-ta-cert)# VQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESBwwJUm9zZXZpbGxl
switch(config-ta-cert)# MQwwCgYDVQQKDANIUEUxEzARBgNVBAsMCk5ldmcxFTATBgNVBAMMDFRl
...
switch(config-ta-cert)# rvadRXSAsUlevJRNNOyINrEJyOfUX2hAfLaiBYP+In6gKTAwVh1xLiXn
switch(config-ta-cert)# LlryAb2/go4BTYjil3eJyXxweUHheuBeesEslBawLv0cPCQPTTdbc97O
switch(config-ta-cert)# iWbyAmfSpD/TS3AgCLnBFPKEKsms0f0LF3/C9dRUXjIHT/LDBr+lgzY3
| switch(config-ta-cert)# |     |     |     | m2NCvxY= |                  |     |     |
| ----------------------- | --- | --- | --- | -------- | ---------------- | --- | --- |
| switch(config-ta-cert)# |     |     |     | -----END | CERTIFICATE----- |     |     |
switch(config-ta-cert)#
The certificate you are importing has the following attributes:
Subject: C = US, ST = California, L = Roseville, O = HPE, OU = Networking,
| CN = Test | CA  | root, | emailAddress |     | =   | generic@corp.com |     |
| --------- | --- | ----- | ------------ | --- | --- | ---------------- | --- |
Issuer: C = US, ST = California, L = Roseville, O = HPE, OU = Networking,
| CN =Test                | CA root, | emailAddress       |      |             | = generic@corp.com |          |              |
| ----------------------- | -------- | ------------------ | ---- | ----------- | ------------------ | -------- | ------------ |
| Serial Number:          |          | 0xBFC92197xxxxxxxx |      |             |                    |          |              |
| TA certificate          |          | import             | is   | allowed     | only               | once for | a TA profile |
| Do you want             | to       | accept             | this | certificate |                    | (y/n)?   | y            |
| switch(config-ta-root)# |          |                    |      | exit        |                    |          |              |
================================================================================
| Create a | CSR | for a | leaf | certificate |     |     |     |
| -------- | --- | ----- | ---- | ----------- | --- | --- | --- |
================================================================================
| switch(config)#           |     | crypto | pki | certificate |     | leaf |     |
| ------------------------- | --- | ------ | --- | ----------- | --- | ---- | --- |
| switch(config-cert-leaf)# |     |        |     | subject     |     |      |     |
Do you want to use the switch serial number as the common name (y/n)? y
| Common Name: |     | SG9Zxxxxxx |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | --- | --- |
Org Unit:
Org Name:
Locality:
State:
Country:
| switch(config-cert-leaf)# |           |     |             | enroll | terminal |               |             |
| ------------------------- | --------- | --- | ----------- | ------ | -------- | ------------- | ----------- |
| You are                   | enrolling | a   | certificate |        | with     | the following | attributes: |
Subject: C=<empty>, ST=<empty>, L=<empty>, OU=<empty>, O=<empty>,
CN=SG9Zxxxxxx
| Key Type:  | RSA         | (2048) |              |     |     |     |     |
| ---------- | ----------- | ------ | ------------ | --- | --- | --- | --- |
| Continue   | (y/n)?      | y      |              |     |     |     |     |
| -----BEGIN | CERTIFICATE |        | REQUEST----- |     |     |     |     |
MIICWjCCAUICAQIwFTETMBEGA1UEAwwKU0c5WktONDAwSoZIhvcN
AQEBBQADggEPADCCAQoCggEBAMKdtoucDEMeuZjPGvCcWTm4D39A
WBA8K/bduJvM1E2B/uirU2TX7mF6lN30akClSxZOoofZAmBPCzI3
...
wZtb5c8fYCSR+TpLwZAdoXrvGJqJ1aGzV6/kVfb7rM6ulBksfBo/
JwO+7x8Vn5h1dGCrsl9CPJienni/fq24+1CJzspMbY9BKu9EIL+P
5ND9BmN0IzEmDO26F+Ip74DqFCIYjXtl3uPJk4cwJkXq121hlcrG
UlatpvjNEpZOtfoEryDJSs0pHXky7VjltYABIuDy
| -----END | CERTIFICATE |     | REQUEST----- |     |     |     |     |
| -------- | ----------- | --- | ------------ | --- | --- | --- | --- |
PKI|174

================================================================================
Install the signed leaf certificate issued by an intermediate CA. The
1intermediate CA certificate is included after the signed leaf certificate.
================================================================================

switch(config-cert-leaf)# import terminal ta-profile root
Paste the certificate in PEM format below, then hit enter and ctrl-D:
switch(config-cert-import)# -----BEGIN CERTIFICATE-----
switch(config-cert-import)# MIIEKTCCAhGgAwIBAgIJAO1LSoBmKxtbMA0GCSqGSIYxCzAJBgNV
switch(config-cert-import)# BAYTAkFVMRUwEwYDVQQIDAxJbnRlcm1lZGNVBAoMGEludGVybmV0
switch(config-cert-import)# IFdpZGdpdHMgUHR5IEx0ZDENMAsGA1UEAw0yMDA1MTQyMDI3MTla
...
switch(config-cert-import)# axnZcIaNp4eNi95in+TvckXA0eMLScNyR7IF+Wjn56H0fQKYsHp/
switch(config-cert-import)# jllbCkyB1xKnn6IpzIj/hvAx3NpA0jXx/qJA+V/cltaAL6+QPZmI
switch(config-cert-import)# vr5GZsoV72BHFOXxoteZlmWMUdVldYXXP2DzEUbttr9zojwz0MyK
switch(config-cert-import)# Qz5tc0BlGfJAtghykw==
switch(config-cert-import)# -----END CERTIFICATE-----
switch(config-cert-import)# -----BEGIN CERTIFICATE-----
switch(config-cert-import)# MIIFyzCCA7OgAwIBAgIJAO1LSoBmKxtwMA0GCSqGCIGOMQswCQYD
switch(config-cert-import)# VQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvc1UEBwwJUm9zZXZpbGxl
switch(config-cert-import)# MQwwCgYDVQQKDANIUEUxEzARBgNVBAsMCmcxFTATBgNVBAMMDFRl
...
switch(config-cert-import)# LM9DV3YNWOM4UMMP2HXaDDfqxZPX9Zsj6Gl/stRCh8SVfsF2duYR
switch(config-cert-import)# 5brLfEpiDhXrZVXxF9lljRABO2JPLSUufg7xr6M/K5aCujxVYzK7
switch(config-cert-import)# DQaCEw5NlmC1vpYlY2TG3dlUQPZDeQOAHwuBd4HewqDHWfp/T04=
switch(config-cert-import)# -----END CERTIFICATE-----
switch(config-cert-import)#
Leaf certificate is validated with root and imported successfully.
switch(config-cert-leaf)#

Installing a self-signed leaf certificate (created inside the
switch)

This procedure describes how to create (wholly inside the switch) and install a self-signed X.509 leaf
certificate. And associate it with one of the following switch features: syslog client, RadSec client, captive-
portal, HTTPS server, or HSC (hardware switch controller).

Procedure

1. Create a leaf certificate context with the command crypto pki certificate. This switches to the

leaf certificate configuration context.

2. Define leaf certificate properties with the command subject.

3. Set the encryption key type for the leaf certificate with the command key-type.

4. Generate and install the self-signed certificate with the command enroll self-signed.

5. Exit the leaf certificate context with the command exit.

6. Associate the leaf certificate with a switch feature (syslog client, RadSec client, captive-portal,

HTTPS server, or HSC) with the command crypto pki application.

Example

This example:

n Creates the leaf certificate context.

n Defines the leaf certificate characteristics.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

175

n Createsandinstallstheself-signedleafcertificate.
n Associatestheleafcertificatewiththesyslogclient(application)ontheswitch.
| switch(config)# |     | crypto | pki | cert | SS_LC |     |     |     |
| --------------- | --- | ------ | --- | ---- | ----- | --- | --- | --- |
8400X(config-cert-SS_LC)# subject common-name SSLeaf country US
| state CA                  | locality | Rocklin       | org        | Company | org-unit     |            | Site        |     |
| ------------------------- | -------- | ------------- | ---------- | ------- | ------------ | ---------- | ----------- | --- |
| 8400X(config-cert-SS_LC)# |          |               | key-type   |         | rsa key-size |            | 3072        |     |
| 8400X(config-cert-SS_LC)# |          |               | enroll     |         | self-signed  |            |             |     |
| You are enrolling         |          | a certificate |            |         | with the     | following  | attributes: |     |
| Subject:                  | C=US,    | ST=CA,        | L=Rocklin, |         | OU=Site,     | O=Company, |             |     |
CN=SSLeaf
| Key Type:                 | RSA (3072)  |     |      |         |              |     |               |     |
| ------------------------- | ----------- | --- | ---- | ------- | ------------ | --- | ------------- | --- |
| Continue                  | (y/n)?      | y   |      |         |              |     |               |     |
| Self-signed               | certificate |     | is   | created | and enrolled |     | successfully. |     |
| 8400X(config-cert-SS_LC)# |             |     | exit |         |              |     |               |     |
switch(config)# crypto pki application syslog-client certificate SS_LC
Installing a self-signed leaf certificate (created outside the
switch)
Thisproceduredescribeshowtoinstallaself-signedX.509leafcertificate(thatwascreatedoutsidethe
switch).Andthenassociatethecertificatewithoneofthefollowingswitchfeatures:syslogclient,RadSec
client,captive-portal,HTTPSserver,orHSC(hardwareswitchcontroller).
Prerequisites
Aself-signedleafcertificate(includingprivate-keydata)mustbecreatedoutsidetheswitch.
Procedure
1. Createtheleafcertificatecontextwiththecommandcrypto pki certificatewhichthen
switchestothecreatedleafcertificatecontext.
2. Importtheleafcertificatedataintotheswitchwiththecommandimport(self-signed
leaf
certificate).
3. Exittheleafcertificatecontextwiththecommandexit.
4. Associatetheleafcertificatewithaswitchfeature(syslogclient,RadSecclient,captive-portal,
| HTTPSserver,orHSC)withthecommandcrypto |     |     |     |     |     |     | pki application. |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
Example
Thisexample:
Createstheleafcertificatecontext.
n
n Importstheself-signedleafcertificate.
n Associatestheleafcertificatewiththesyslogclient(application)ontheswitch.
| switch(config)# |     | switch(config)# |     |     | crypto pki | certificate |     | SS_LC2 |
| --------------- | --- | --------------- | --- | --- | ---------- | ----------- | --- | ------ |
switch(config)# switch(config-cert-SS_LC)# import terminal self-signed
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-cert-import)# |     |     |     | -----BEGIN | CERTIFICATE----- |     |     |     |
| --------------------------- | --- | --- | --- | ---------- | ---------------- | --- | --- | --- |
switch(config-cert-import)# MIIFRDCCAyygAwIBAgIQP8nnS2Vp15u07xXMdktDJzANBgkqhkiG9
switch(config-cert-import)# MQswCQYDVQGEwJVUEOMAwGA1UECgwFXJ1YmxDAOgNBAMMB1Jvb3gw
PKI|176

switch(config-cert-import)# HhcNMTkNDEwMjIwNT1WhcjIwMTA0MjIwNE1WjBzQswQYDVQQGEwJV
...
switch(config-cert-import)# 1fIYZYGQyla0AwFuPTTxBXHYwRxTPbUYU5tumJrfwRPmE4OVY8S9D
switch(config-cert-import)# 1NGNm3NG03GqPScs/TF9bVyFA5BOrS5lmm7kNfRYlK8D/kMTfRreS
| switch(config-cert-import)# |     |     | YQ1u1NqShps= |                  |     |
| --------------------------- | --- | --- | ------------ | ---------------- | --- |
| switch(config-cert-import)# |     |     | -----END     | CERTIFICATE----- |     |
switch(config-cert-import)# -----BEGIN ENCRYPTED PRIVATE KEY-----
switch(config-cert-import)# MIIFDjBABgkqhkiG9wBBQ0wMzAbBgkqkiw0QwwDQImNpJMN7sVGwC
switch(config-cert-import)# MBQGCCqGSIb3DQMHAit+2qadNAASCMg5LYJ4AFm3EffhH5p51Ggr8
switch(config-cert-import)# IJ6L/UhEtH523nUkdV6gvoAWgoYaeD83PeswToAGv5VS8OMFTPttr
...
switch(config-cert-import)# OgSecqZsG6arbx0ESaYBir1c/6rPs1pcjbDxw283DiD1MWOpeoS2a
switch(config-cert-import)# iKnXnUMpVPfLc74ty2S41DtH0X9Sgf6aa1LjiStg+N7cND9XfGtj/
| switch(config-cert-import)# |     |     | cb4= |     |     |
| --------------------------- | --- | --- | ---- | --- | --- |
switch(config-cert-import)# -----END ENCRYPTED PRIVATE KEY-----
switch(config-cert-import)#
| Enter import | password: | ******* |     |     |     |
| ------------ | --------- | ------- | --- | --- | --- |
Leaf certificate is validated as self-signed certificate and imported
successfully.
| switch(config-cert-SS_LC2)# |     |     | exit |     |     |
| --------------------------- | --- | --- | ---- | --- | --- |
switch(config)# crypto pki application syslog-client certificate SS_LC2
| Installing | a certificate |     | of  | a root | CA  |
| ---------- | ------------- | --- | --- | ------ | --- |
Prerequisites
n AcertificateofarootCA(thatisusedasthesigner).
n RevocationcheckingURLsfortheCA(optional).
Procedure
1. CreateaTAprofilewiththecommandcrypto pki ta-profilewhichthenswitchestothe
createdTAprofilecontext.
Step2isoptionalandsuggestedonlyforadvancedusers.
2. Optionallyenablecertificaterevocationcheckingwiththecommandrevocation-check ocsp.
MostcertificatescontainrevocationcheckingURLsforOCSP.IfyouwanttooverridetheseURLs,
configurecustomrevocationcheckingURLswiththecommandocsp url.
3. ImportthecertificateoftherootCAwiththecommandta-certificate.
Example
Thisexampleinstallsthecertificateroot-certanddefinescustomrevocationcheckingURLs:
| switch(config)# | crypto | pki | ta-profile | root-cert |     |
| --------------- | ------ | --- | ---------- | --------- | --- |
switch(config-ta-root-cert)#
|     |     |     | revocation-check |     | ocsp |
| --- | --- | --- | ---------------- | --- | ---- |
switch(config-ta-root-cert)# ocsp url primary http://ocsp-server.site.com
switch(config-ta-root-cert)# ocsp url secondary http://ocsp-server2.site.com
| switch(config-ta-root-cert)# |     |     | ta-certificate |     | import terminal |
| ---------------------------- | --- | --- | -------------- | --- | --------------- |
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-ta-cert)# |     | -----BEGIN |     | CERTIFICATE----- |     |
| ----------------------- | --- | ---------- | --- | ---------------- | --- |
switch(config-ta-cert)# MIIDuTCCAqECCQCuoxeJ2ZNYcjANBgkqhkiG9w0BAQsFADCBqzELMAEBh
switch(config-ta-cert)# VVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEDAOBgNVBAcMB1JvY2tsDAKBg
switch(config-ta-cert)# BAoMA0hQTjEVMBMGA1UECwwMSFBOUm9zZXZpbGxlMSowKAYDVQocG5zdz
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 177

...
switch(config-ta-cert)# x3WFf3dFZ8o9sd5LVAHneH/ztb9MP34z+le1V346r12L2kpxmTOVJVyTO
switch(config-ta-cert)# BIzD/ST/HaWI+0S+S80rm93PSscEbb9GWk7vshh5EnW/moehBKcE4O1zy
switch(config-ta-cert)# 3LvMLZcssSe5J2Ca2XIhfDme8UaNZ7syGYMsAW0nG7yYHWkEOQu9s
| switch(config-ta-cert)# |     | -----END | CERTIFICATE----- |     |     |
| ----------------------- | --- | -------- | ---------------- | --- | --- |
switch(config-ta-cert)#
The certificate you are importing has the following attributes:
| Issuer: | C=US, ST=CA, | L=Rocklin, | O=Company, | OU=Site, |     |
| ------- | ------------ | ---------- | ---------- | -------- | --- |
CN=site.com/emailAddress=test.ca@site.com
| Subject: | C=US, ST=CA, | L=Rocklin, | O=Company, | OU=Site, |     |
| -------- | ------------ | ---------- | ---------- | -------- | --- |
CN=8400/emailAddress=test.ca@site.com
| Serial Number: | 12121221634631568498 |                  |      | (0xaea51217d5945772) |              |
| -------------- | -------------------- | ---------------- | ---- | -------------------- | ------------ |
| TA certificate | import               | is allowed       | only | once for             | a TA profile |
| Do you want    | to accept            | this certificate |      | (y/n)?               | y            |
| TA certificate | accepted.            |                  |      |                      |              |
switch(config-ta-root-cert)#
| Installing | a downloadable |     |     | user role | certificate |
| ---------- | -------------- | --- | --- | --------- | ----------- |
Thisproceduredescribeshowtocreateandinstalladownloadableuserrole(DUR)certificate.
Prerequisites
n AcertificateofarootCA(thatisusedasthesigner).
Procedure
1. CreateaTAprofilewiththecommandcrypto pki ta-profilewhichthenswitchestothe
createdTAprofilecontext.
2. ImportthecertificateoftherootCAwiththecommandta-certificate.
Example
switch(config)#
|                             | crypto | pki ta-profile |                  | DUR-cert |     |
| --------------------------- | ------ | -------------- | ---------------- | -------- | --- |
| switch(config-ta-DUR-cert)# |        | ta-profile     |                  |          |     |
| switch(config-ta-cert)#     |        | -----BEGIN     | CERTIFICATE----- |          |     |
switch(config-ta-cert)#
MIIGFjCCA/6gAwIBAgIJAMtlKN7Gy9GCMA0GCSqGSIb3DQEBCwUAMIGWMQswCQYD
VQQGEwJJTjESMBAGA1UECAwJS2FybmF0YWdhMRIwEAYDVQQHDAlCYW5nYWxvcmUx
DDAKBgNVBAoMA0hQRTEMMAoGA1UECwwDSFBOMRcwFQYDVQQDDA4xNS4yMTIuMjIx
LjE5NDEqMCgGCSqGSIb3DQEJARYbcmFkaGFrcmlzaG5hbi5nb3BhbEBocGUuY29t
MCAXDTIwMDExNTA5MzgwM1oYDzQxODMxMDIyMDkzODAzWjCBljELMAkGA1UEBhMC
SU4xEjAQBgNVBAgMCUthcm5hdGFnYTESMBAGA1UEBwwJQmFuZ2Fsb3JlMQwwCgYD
VQQKDANIUEUxDDAKBgNVBAsMA0hQTjEXMBUGA1UEAwwOMTUuMjEyLjIyMS4xOTQx
KjAoBgkqhkiG9w0BCQEWG3JhZGhha3Jpc2huYW4uZ29wYWxAaHBlLmNvbTCCAiIw
DQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBALs99p/xrJHXgYTAiV4WjwgHgJJt
aRwisIoA8iKBZN3zmc1HKJNeGHYXJl0QNC7xfAFSptwgmQ+bhawLuGLNWWMlzQdP
68GmJS1Ojn1xkQ1VIwjrDCfk5t7RAMY/bZKPRjPnfzbZ03Nv3tqp9h/bWTP1y17S
SzYdDF9SiEVfx/4EWicXIDx2ie44kE+9CGB817Q/kovALiIjREJxtv2WJLvE4g/X
2pBu2WMMKhxU95JX2WdIrbHLM1sETUMvb6itg6jfhnPDIzWF5Xbb0c22HsJ6Ynvy
FylHqkN5QjTBaWo9UpvVeeNEAl2tm8D7UsRGJO5u0Y01j4Xp1bQgDf/S6b6LHYQZ
4TLZIEjBn9tH1hXoPd0wXAdpXnYqBZ0UO4ZHaRxvG5wEsvZ3LOyJXNU1J2Z5osC+
HkJRr5tMKV9Dc0gON81LPXj4+JmubyWi7ABM8+ktNyDqTeGqMaUZaB+NvGwQyMUr
Ntgvam9ntI+/njW0ViKYEwQJ4OB9D+0sWXJHFrqfZpbVYTQjZktDDnVhSL9Z5Fce
5+AIBBlCCFcNc933fv29jC0oVWjZ2RHt/8B0DdPY/hDPb0epy+WEosxIQzQ++D+M
s9aBPYVgwCKE2mkT6lnqBhAaNNiSK7wiUU92rHvYhRr2W6Zib+wU9BFWZIzFKbXd
PKI|178

D8I7P0Zm0hf/j0wVAgMBAAGjYzBhMB0GA1UdDgQWBBRV0riw2MVuuc/Y9VtGgstN
PTrm+DAfBgNVHSMEGDAWgBRV0riw2MVuuc/Y9VtGgstNPTrm+DAPBgNVHRMBAf8E
BTADAQH/MA4GA1UdDwEB/wQEAwIBhjANBgkqhkiG9w0BAQsFAAOCAgEAU7fff1Ci
lyA7yq37jlxzdnGXiuR+00xiuZ62xBcu6F/p2SwsieesQCJ2odiOcaqeYXIAIiI2
EAHpesan7OQap2KQ/Xw/00H3/q+SQo47LiGiZjWLeGjaJ5NXBBra6MhZXjli1EEG
70Qn0dehM7am5bsLRhYvRR+TesWEceNoFQN11yiqpGWCPII8Q4eL4MsSTEMl6Qki
yaVDzQko2FW9P3sDV7RGwKrxJIYT8HqPrU6WZUaT7+C0G5EwqP8peg7HOaInKM6Z
lsmFXaSlTvHGbgjJm8uReWr1wNr+V3nugzOCUFspy32OexP90fJ873K1glIbEfxw
bmWMq6za1KQ9rzyNVI2ucp9F7oyXz0vy/6/Fagu1Kkv2BoUxExU9AVwCkDsdVnun
IuQMly2CVGpj+5bhcDRS3ZUmKWAMw0uBwky0BiE1A48LN7R/OYbOmr4QkmveAJAD
MOZIGK4KbutsrIGsT0vs+lU9wrfdiG2TiZ1hsWIT47EYg/C9ZkeDtQUuilob6uaO
Wt/2il/ePUbsSZn9YX9jLBNEsNWbW9B5wyqhAh1AwOpC5KVkHPOsXPOLJZPNO2RI
UKVv7wqGQMMFwKVnn4MoNEdQCYwRsTt6l0+yY1C1dA6xsG0LUXa2SpuX/gpovaNW
6VA2QAAIJIcSFB4Ky1gncPvV2gUr+GbD0lM=
switch(config-ta-cert)# -----END CERTIFICATE-----
switch(config-ta-cert)#

Installing a CA-signed leaf certificate (initiated in the
switch)

This procedure describes how to create and install an X.509 leaf certificate that is initiated inside the
switch but signed outside the switch by a CA. And then associate the certificate with one of the following
switch features: syslog client, RadSec client, HTTPS server, or HSC (hardware switch controller).

Prerequisites

Root CA certificate root-cert must be installed as described in Installing a certificate of a root CA.

Procedure

1. Create a leaf certificate context with the command crypto pki certificate which then switches

to the created leaf certificate configuration context.

2. Define leaf certificate properties with the command subject.

3. Set the encryption key type for the leaf certificate with the command key-type.

4. Generate the certificate signing request (CSR) with the command enroll terminal.

5. Use the CSR to obtain a leaf certificate from the root CA, using the root CA directly as the signer

CA.

6.

Import the leaf certificate into the switch with the command import(CA-signed leaf
certificate).

7. Exit the leaf certificate context with the command exit.

8. Associate the leaf certificate with a switch feature (syslog client, RadSec client, HTTPS server, or

HSC) with the command crypto pki application.

Example

This example:

n Creates the leaf certificate context.

n Defines the leaf certificate characteristics.

n Generates the leaf certificate signing request in the switch for getting signed outside the switch by a

CA.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

179

n ImportstheCA-signedleafcertificateintotheswitch.
n Associatestheleafcertificatewiththesyslogclient(application)ontheswitch.
| switch(config)# |     | crypto pki | certificate |     | lcert |     |     |     |
| --------------- | --- | ---------- | ----------- | --- | ----- | --- | --- | --- |
switch(config-cert-lcert)# subject common-name Leaf country US state CA
| locality                   | Rocklin   | org Company       |          | org-unit   | Site          |             |     |     |
| -------------------------- | --------- | ----------------- | -------- | ---------- | ------------- | ----------- | --- | --- |
| switch(config-cert-lcert)# |           |                   | key-type |            | rsa key-size  | 3072        |     |     |
| switch(config-cert-lcert)# |           |                   | enroll   | terminal   |               |             |     |     |
| You are                    | enrolling | a certificate     |          | with       | the following | attributes: |     |     |
| Subject:                   | C=US,     | ST=CA, L=Rocklin, |          | O=Company, | OU=Site       |             |     |     |
CN=Leaf
| Key Type:  | RSA (2048)  |              |     |     |     |     |     |     |
| ---------- | ----------- | ------------ | --- | --- | --- | --- | --- | --- |
| Continue   | (y/n)?      | y            |     |     |     |     |     |     |
| -----BEGIN | CERTIFICATE | REQUEST----- |     |     |     |     |     |     |
MIIBozCCAQwCAQAwYzEVMBMGA1UEAxMMcG9kMDEtODQwMC0xMQ4wDAYDV
nViYTEMMAoGA1UEChMDSFBFMRIwEAYDVQQHEwlSb3NldmlsbGUxCzAJBg
NBMQswCQYDVQQGEwJVUzCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYE
...
GBAJ4L3lFFfWBEL+KAKpOGjZcVmwlBMqSKFtOFNF9nzmUmONmU3SKy6dz
7Au22mf3lWDxzrtCC/dj5RtWJeJekxp2LCIK/3eRXUwbYveQDKcxH7j9Z
ace+2tA68F2vlgRCQ/hcQH0YmNuaq4Ne3w0dhm7HlUrx
| -----END | CERTIFICATE | REQUEST----- |     |     |     |     |     |     |
| -------- | ----------- | ------------ | --- | --- | --- | --- | --- | --- |
switch(config-cert-lcert)# import terminal ta-profile root-cert
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-cert-import)# |     |     | -----BEGIN |     | CERTIFICATE----- |     |     |     |
| --------------------------- | --- | --- | ---------- | --- | ---------------- | --- | --- | --- |
switch(config-cert-import)# MIIFRDCCAyygwIBAgIQPnnS2Vp5u07XMdktDJzANBgkqhkiG9w0Bv
switch(config-cert-import)# MQswCQYDVQGEwJVEOMAwG1UECgwFJ1YmxDAOgNBMMB1Jvb3QgQ0Ew
switch(config-cert-import)# HhcNMTkNDEwMjIwNTWcjIwMTA0MjwNE1WBzQswQYDVQQGEwJVUzEL
...
switch(config-cert-import)# 1fIYZYGQyla0AwFuTTxBXYwRxPbUYU5tumrfwRPmE4OVY8S9DQgcr
switch(config-cert-import)# 1NGNm3NG03GqPcs/T9bVyF5BOrS5lmm7kNfRYl8D/kMTfRreSdxis
| switch(config-cert-import)# |     |     | YQ1u1NqShps= |     |                  |     |     |     |
| --------------------------- | --- | --- | ------------ | --- | ---------------- | --- | --- | --- |
| switch(config-cert-import)# |     |     | -----END     |     | CERTIFICATE----- |     |     |     |
switch(config-cert-import)#
Leaf certificate is validated with root-cert and imported successfully.
| switch(config-cert-lcert)# |     |     | exit |     |     |     |     |     |
| -------------------------- | --- | --- | ---- | --- | --- | --- | --- | --- |
switch(config)# crypto pki application syslog-client certificate lcert
| Installing | a CA-signed |     | leaf |     | certificate | (created | outside | the |
| ---------- | ----------- | --- | ---- | --- | ----------- | -------- | ------- | --- |
switch)
ThisproceduredescribeshowtoinstallanX.509leafcertificatethatwascreatedandsigned(byaCA)
outsidetheswitch.Andthenassociatethecertificatewithoneofthefollowingswitchfeatures:syslog
client,RadSecclient,captive-portal,HTTPSserver,orHSC(hardwareswitchcontroller).
Prerequisites
n RootCAcertificateroot-certinstalledasdescribedinInstalling a certificate of a root CA.
ACA-signedleafcertificate(includingprivate-keydata)createdoutsidetheswitch.
n
Procedure
1. Createtheleafcertificatecontextwiththecommandcrypto pki certificatewhichthen
switchestothecreatedleafcertificatecontext.
PKI|180

2. Importtheleafcertificateintotheswitchwiththecommandimport (CA-signed leaf
certificate).
3. Exittheleafcertificatecontextwiththecommandexit.
4. Associatetheleafcertificatewithaswitchfeature(syslogclient,RadSecclient,captive-portal,
| HTTPSserver,orHSC)withthecommandcrypto |     |     |     |     |     |     | pki application. |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
Example
Thisexample:
n Createstheleafcertificatecontext.
n importstheCA-signedleafcertificate.
n Associatestheleafcertificatewiththesyslogclient(application)ontheswitch.
| switch(config)# |     |     | switch(config)# |     | crypto | pki | certificate | CA_LC |
| --------------- | --- | --- | --------------- | --- | ------ | --- | ----------- | ----- |
switch(config)# switch(config-cert-CA_LC)# import terminal ta-profile root-cert
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-cert-import)# |     |     |     | -----BEGIN |     | CERTIFICATE----- |     |     |
| --------------------------- | --- | --- | --- | ---------- | --- | ---------------- | --- | --- |
switch(config-cert-import)# MIIFRDCCAyygAwIBAgIQP8nn2Vp15u07XMktDJANBgkqhkiG9w0Bv
switch(config-cert-import)# MQswCQYDVQGEwJVUEOMAw1UECgwFX1YmxDOgNBAMMB1Jvb3QgQ0Ew
switch(config-cert-import)# HhcNMTkNDEwMjIwNT1WhjIMTA0MjIwNE1jBzQswYDVQQGEwJVUzEL
...
switch(config-cert-import)# 1fIYZYGQyla0AwFuPTTxBXHYRxTPbUYUtmJrwRPmE4OVY8S9DQgcr
switch(config-cert-import)# 1NGNm3NG03GqPScs/TF9bVyFABOrlmm7kNfRlK8D/kMTfRreSdxis
| switch(config-cert-import)# |     |     |     | YQ1u1NqShps= |     |                  |     |     |
| --------------------------- | --- | --- | --- | ------------ | --- | ---------------- | --- | --- |
| switch(config-cert-import)# |     |     |     | -----END     |     | CERTIFICATE----- |     |     |
switch(config-cert-import)# -----BEGIN ENCRYPTED PRIVATE KEY-----
switch(config-cert-import)# MIIFDjBABgkqhkiG9wBBQ0wMzAbBgkiwQwwQImNpJMN7sVGwCAggA
switch(config-cert-import)# MBQGCCqGSIb3DQMHAit+2qadNAASCMgLYJ4AFEfhH5p51Ggr86VqS
switch(config-cert-import)# IJ6L/UhEtH523nUkdV6gvoAWgoYaeD8eswAGv5VS8OMFTPttrn5/K
...
switch(config-cert-import)# OgSecqZsG6arbx0ESaYBir1c6rPs1pcbDx283DD1MWOpeoS2aEmOX
switch(config-cert-import)# iKnXnUMpVPfLc74ty2S41tH0X9gfaa1LiStg+N7cND9XfGtjaV2+/
| switch(config-cert-import)# |     |     |     | cb4= |     |     |     |     |
| --------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- |
switch(config-cert-import)# -----END ENCRYPTED PRIVATE KEY-----
switch(config-cert-import)#
| Enter | import | password: | ******* |     |     |     |     |     |
| ----- | ------ | --------- | ------- | --- | --- | --- | --- | --- |
Leaf certificate is validated with root-cert and imported successfully.
| switch(config-cert-CA_LC)# |     |     |     | exit |     |     |     |     |
| -------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- |
switch(config)# crypto pki application syslog-client certificate CA_LC
PKI commands
| crypto    | pki             | application |            |     |             |     |             |     |
| --------- | --------------- | ----------- | ---------- | --- | ----------- | --- | ----------- | --- |
| crypto    | pki application |             | <APP-NAME> |     | certificate |     | <CERT-NAME> |     |
| no crypto | pki             | application | <APP-NAME> |     | certificate |     | <CERT-NAME> |     |
Description
Associatesaleafcertificatewithafeature(application)ontheswitch.Bydefault,allfeaturesare
associatedwiththedefault,self-signedcertificatelocal-cert.Thiscertificateiscreatedbytheswitch
thefirsttimeitstarts.
Thenoformofthiscommandassociatesthespecifiedfeaturewiththedefaultcertificate.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 181

Parameter

<APP-NAME>

Description

Specifies the name of a feature on the switch:
n captive-portal: Captive portal
n est-client: EST client
n hsc: Hardware switch controller
n https-server: HTTPS server
n radsec-client: RadSec client
n syslog-client: Syslog client
syslog-client communicates with syslog server over TLS.
You can associate a certificate with the syslog-client
application by enrolling the certificate manually or through EST.

<CERT-NAME>

Specifies the name of an installed leaf certificate.

Examples

Associating the EST client with leaf certificate leaf-cert1:

switch(config)# crypto pki application est-client certificate leaf-cert1

Associating the syslog client with leaf certificate leaf-cert:

switch(config)# crypto pki application syslog-client certificate leaf-cert

Setting the syslog client to use the default certificate:

switch(config)# no crypto pki application syslog-client certificate

Setting the RadSec client to use the default certificate:

switch(config)# no crypto pki application radsec-client certificate

Associating the RadSec client with leaf certificate leaf-cert:

switch(config)# crypto pki application radsec-client certificate leaf-cert

Associating the HTTPS server with leaf certificate leaf-cert2:

switch(config)# crypto pki application https-server certificate leaf-cert2

Associating the 802.1X supplicant with leaf certificate cert1:

switch(config)# crypto pki application dot1x-supplicant certificate cert1

Command History

PKI | 182

| Release        |             |         |         |     | Modification |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| crypto    | pki             | certificate |             |             |     |     |
| --------- | --------------- | ----------- | ----------- | ----------- | --- | --- |
| crypto    | pki certificate |             | <CERT-NAME> |             |     |     |
| no crypto | pki             | certificate |             | <CERT-NAME> |     |     |
Description
Createsaleafcertificateandchangestoitscontextconfig-cert-<CERT-NAME>.Ifthespecifiedleaf
certificateexists,thiscommandchangestoitscontext.
Thefirsttimetheswitchstartsitcreatesaself-signed,defaultleafcertificatecalledlocal-cert.This
certificateisusedbyanyswitchapplicationthatdoesnothaveanassociatedleafcertificate.
Thenoformofthiscommanddeletesthespecifiedleafcertificate.Thedefaultleafcertificatelocal-
certcannotbedeleted.
| Parameter   |     |     |     |     | Description                                    |     |
| ----------- | --- | --- | --- | --- | ---------------------------------------------- | --- |
| <CERT-NAME> |     |     |     |     | Specifiesthenameofaleafcertificate.Range:1to32 |     |
alphanumericcharacters(excluding").
Examples
Creatingleafcertificateleaf-cert:
| switch(config)# |     |     | crypto | pki certificate |     | leaf-cert |
| --------------- | --- | --- | ------ | --------------- | --- | --------- |
switch(config-cert-leaf-cert)#
Deletingleafcertificateleaf-cert:
switch(config)#
|     |     |     | no crypto | pki certificate |     | leaf-cert |
| --- | --- | --- | --------- | --------------- | --- | --------- |
The leaf certificate has associated applications. Deleting the certificate
will make the applications use the default certificate local-cert.
| Continue |     | (y/n)? | y   |     |     |     |
| -------- | --- | ------ | --- | --- | --- | --- |
switch(config)#
| Command        | History     |     |     |     |              |     |
| -------------- | ----------- | --- | --- | --- | ------------ | --- |
| Release        |             |     |     |     | Modification |     |
| 10.07orearlier |             |     |     |     | --           |     |
| Command        | Information |     |     |     |              |     |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 183

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| crypto    | pki            | ta-profile |           |     |     |     |
| --------- | -------------- | ---------- | --------- | --- | --- | --- |
| crypto    | pki ta-profile |            | <TA-NAME> |     |     |     |
| no crypto | pki            | ta-profile | <TA-NAME> |     |     |     |
Description
Createsatrustanchor(TA)profileandchangestotheconfig-ta-<TA-NAME>contextfortheprofile.
EachTAprofilestoresthecertificateforatrustedCA.Upto64profilescanbedefined.
IfthespecifiedTAprofileexists,thiscommandchangestotheconfig-ta-<TA-NAME>contextforthe
profile.
ThenoformofthiscommandremovesthespecifiedTAprofile.
Whencreatinganewprofile,Ifyouexittheconfig-ta-<TA-NAME>contextwithoutimportingtheTAcertificate,
theprofileisdiscarded.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<TA-NAME>
SpecifiestheTAprofilename.Range:1to48alphanumeric
charactersexcluding".
NOTE:TheTAprofilenamecannotendwithest-ta<nn>where
<nn>is00to99.Forexample,company-trust-anchor-est-
ta01isnotallowed.ThisTAprofilenamesuffixisreservedforTA
profilesthatarecreatedforCAcertificatesfromESTservers.
Examples
CreatingtheTAprofileroot-cert:
| switch(config)# |     |     | crypto | pki ta-profile |     | root-cert |
| --------------- | --- | --- | ------ | -------------- | --- | --------- |
switch(config-ta-root-cert)#
RemovingTAprofileroot-cert:
| switch(config)# |             |     | no crypto | pki ta-profile |              | root-cert |
| --------------- | ----------- | --- | --------- | -------------- | ------------ | --------- |
| Command         | History     |     |           |                |              |           |
| Release         |             |     |           |                | Modification |           |
| 10.07orearlier  |             |     |           |                | --           |           |
| Command         | Information |     |           |                |              |           |
PKI|184

| Platforms | Command |     | context | Authority |     |     |
| --------- | ------- | --- | ------- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
enroll self-signed
enroll self-signed
Description
Generatesakeypairandgeneratesaself-signedcertificatewithit.
Thesubjectfieldsandkeytypeofthecurrentleafcertificatemustbedefinedbeforerunningthis
command.Ifnot,youarepromptedtofillinthesubjectfields,andthekeytypeissettoRSA 2048.
Example
Enrollingtheleafcertificateleaf-cert:
| switch(config-cert-leaf-cert)# |       |               |            | enroll   | self-signed   |             |
| ------------------------------ | ----- | ------------- | ---------- | -------- | ------------- | ----------- |
| You are enrolling              |       | a certificate |            | with     | the following | attributes: |
| Subject:                       | C=US, | ST=CA,        | L=Rocklin, | OU=Site, | O=Comp,       |             |
CN=Leaf01
| Key Type:   | RSA (2048)  |     |            |     |          |               |
| ----------- | ----------- | --- | ---------- | --- | -------- | ------------- |
| Continue    | (y/n)?      | y   |            |     |          |               |
| Self-signed | certificate |     | is created | and | enrolled | successfully. |
switch(config-cert-leaf-cert)#
| Command History     |         |     |         |              |           |     |
| ------------------- | ------- | --- | ------- | ------------ | --------- | --- |
| Release             |         |     |         | Modification |           |     |
| 10.07orearlier      |         |     |         | --           |           |     |
| Command Information |         |     |         |              |           |     |
| Platforms           | Command |     | context |              | Authority |     |
Allplatforms config-cert-<CERT-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
enroll terminal
enroll terminal
Description
Generatesakeypairandcertificatesigningrequest(CSR)forthecurrentleafcertificate.UsetheCSRto
obtainasignedcertificatefromacertificateauthority(CA),andthenimportthecertificateontothe
| switchwiththecommandimport |     |     | terminal. |     |     |     |
| -------------------------- | --- | --- | --------- | --- | --- | --- |
Thekeytype,andthecertificatecommonnameinthesubjectfieldsofthecurrentleafcertificatemust
becompletedbeforerunningthiscommand.
Example
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 185

Enrolling the leaf certificate leaf-cert:

switch(config-cert-leaf-cert)# enroll terminal
You are enrolling a certificate with the following attributes:
Subject: C=US, ST=CA, L=Rocklin, OU=Site, O=Comp,

CN=Leaf01

Key Type: RSA (2048)

Continue (y/n)? y

-----BEGIN CERTIFICATE REQUEST-----
MIIBozCCAQwCAQAwYzEVMBMGA1UEAxMMcG9kMDEtODQwMC0xMQ4wDAYDVQQLEwV
nViYTEMMAoGA1UEChMDSFBFMRIwEAYDVQQHEwlSb3NldmlsbGUxCzAJBgNVBAgT
NBMQswCQYDVQQGEwJVUzCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAtKcLS
...
GBAJ4L3lFFfWBEL+KAKpOGjZcVmwlBMqSKFtOFNF9nzmUmONmU3SKy6dzQ+6ynR
7Au22mf3lWDxzrtCC/dj5RtWJeJekxp2LCIK/3eRXUwbYveQDKcxH7j9ZB+BAp2
ace+2tA68F2vlgRCQ/hcQH0YmNuaq4Ne3w0dhm7HlUrx
-----END CERTIFICATE REQUEST-----
switch(config-cert-leaf-cert)#

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

All platforms

config-cert-<CERT-NAME>

Administrators or local user group members with
execution rights for this command.

import (CA-signed leaf certificate)
import terminal ta-profile <TA-NAME> [password <PW>]
import <REMOTE-URL> ta-profile <TA-NAME> [password <PW>][vrf <VRF-NAME>]
import <STORAGE-URL> ta-profile <TA-NAME> [password <PW>]

Description

Imports a CA-signed leaf certificate and then validates the certificate against the specified TA profile. If
the imported data includes a private key, the private key must match the leaf certificate being imported.
If the imported data does not include a private key, the certificate must match a CSR that was previously
generated with the command enroll terminal and must be signed by the CA whose root certificate is
installed in the specified TA profile. The TA profile must exist and have a TA certificate configured.

Parameter

terminal

Description

Import the certificate by pasting PEM-format data at the console.
Upon execution, the config-cert-import context is entered for
certificate pasting. To complete certificate data entry press
Control-D in your terminal program. Alternatively, the pasted
certificate data can include at its end the delimiter END_OF_

PKI | 186

| Parameter |     |     | Description                  |     |                        |
| --------- | --- | --- | ---------------------------- | --- | ---------------------- |
|           |     |     | CERTIFICATE(afterthe-----END |     | CERTIFICATE-----line), |
makingentryofControl-Dunnecessary.
ta-profile <TA-NAME> SpecifiestheTAprofilename.Range:1to48alphanumeric
charactersexcluding".
password <PW> Specifiestheplaintextpasswordusedtodecrypttheprivatekeyin
theimportedcertificatedata.Whenthisparameterisomitted,the
passwordispromptedforasrequired.Range:1to32
alphanumericcharacters.
<REMOTE-URL> SpecifiesacertificatedatafileonaremoteTFTPorSFTPserver.
TheURLsyntaxis:
|     |     |     | {tftp://  | | sftp://<USER>@}          | {<IP>|<HOST>} |
| --- | --- | --- | --------- | -------------------------- | ------------- |
|     |     |     | [:<PORT>] | [;blocksize=<SIZE>]/<FILE> |               |
vrf <VRF-NAME> SpecifiesthenameoftheVRFtousefortheremoteURLfile
transfer.Thedefaultismgmt.
<STORAGE-URL>
AvailableonswitchfamiliesthatprovideUSBdevicefileimport
capability,specifiesacertificatedatafileonaUSBstoragedevice
insertedintheswitchUSBport.TheURLsyntaxisusb:/<FILE>.
Usage
n TheimporteddatamustincludealltheintermediateCAcertificatesinthecertificatechainleadingto
thecertificateimportedintothespecifiedTAprofile.
n Thiscommandcannotbeusedwiththedefaultcertificatelocal-cert.
n ThePEMdataformatissupportedforallimportsources.ThePKCS#12dataformatissupportedfor
<REMOTE-URL>and<STORAGE-URL>.
n ThePEMdatamustbedelimitedwiththeselinesforthecertificatedata:
| -----BEGIN | CERTIFICATE----- |     |     |     |     |
| ---------- | ---------------- | --- | --- | --- | --- |
| -----END   | CERTIFICATE----- |     |     |     |     |
AndthePEMdatamustbedelimitedwitheitheroftheselinepairsfortheprivatekeydata:
| -----BEGIN | PRIVATE          | KEY----- |          |     |     |
| ---------- | ---------------- | -------- | -------- | --- | --- |
| -----END   | PRIVATE KEY----- |          |          |     |     |
| -----BEGIN | ENCRYPTED        | PRIVATE  | KEY----- |     |     |
| -----END   | ENCRYPTED        | PRIVATE  | KEY----- |     |     |
Examples
Importingaleafcertificatefromtheconsole:
| switch(config)# |     | crypto pki | certificate | leaf-cert |     |
| --------------- | --- | ---------- | ----------- | --------- | --- |
switch(config-cert-leaf-cert1)# import terminal ta-profile root-cert
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-cert-import)# |     |     | -----BEGIN | CERTIFICATE----- |     |
| --------------------------- | --- | --- | ---------- | ---------------- | --- |
switch(config-cert-import)# MIIFRDCCAyygAwIBAgQP8nS2Vp15u0xXMdkDJzANBgkqhkiG9w0Bv
switch(config-cert-import)# MQswCQYDVQGEwJVUEOMAwGA1UCgwFXJ1YmDAgNBAMM1Jvb3QgQ0Ew
switch(config-cert-import)# HhcNMTkNDEwMjIwNT1WhcjIwMT0MjwNE1WjzQswQDVQQGEwJVUzEL
...
switch(config-cert-import)# 1fIYZYGQyla0AwFuPTTxBXHYwRxTPbUYU5umJfRPmE4VY8S9DQgcr
switch(config-cert-import)# 1NGNm3NG03GqPScs/TF9bVyFA5BOS5lmmkfRYK8D/kMTfRreSdxis
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 187

| switch(config-cert-import)# |     |     |     |     | YQ1u1NqShps= |     |                  |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | ------------ | --- | ---------------- | --- | --- | --- | --- |
| switch(config-cert-import)# |     |     |     |     | -----END     |     | CERTIFICATE----- |     |     |     |     |
switch(config-cert-import)# -----BEGIN ENCRYPTED PRIVATE KEY-----
switch(config-cert-import)# MIIFDjBABgkqhkiG9wBBQ0wMzAbBgqkw0QwwDQIpJMN7sVGwCAggA
switch(config-cert-import)# MBQGCCqGSIb3DQMHAit+2qadNAASCgLYJ4Am3EfhH5p51Ggr86VqS
switch(config-cert-import)# IJ6L/UhEtH523nUkdV6gvAgoYaD83PswToAGv5VS8OMFTPttrn5/K
...
switch(config-cert-import)# OgSecqZsG6arbx0ESaYBir1c/6rPspcjbx283iD1MWOpeoS2aEmOX
switch(config-cert-import)# iKnXnUMpVPfLc74ty2S41DtH0X9gf6aa1jStg+7cND9XfGtjaV2+/
| switch(config-cert-import)# |     |     |     |     | cb4= |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
switch(config-cert-import)# -----END ENCRYPTED PRIVATE KEY-----
switch(config-cert-import)#
| Enter | import | password: |     | ******* |     |     |     |     |     |     |     |
| ----- | ------ | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Leaf certificate is validated with root-cert and imported successfully.
switch(config-cert-leaf-cert)#
Importingaleafcertificatefromaremotefile:
| switch(config)# |     |     | crypto | pki | certificate |     | leaf-cert2 |     |     |     |     |
| --------------- | --- | --- | ------ | --- | ----------- | --- | ---------- | --- | --- | --- | --- |
switch(config-cert-leaf-cert2)# import tftp://1.1.1.2/c2.p12 ta-profile root-cert
% Total % Received % Xferd Average Speed Time Time Time Current
|       |        |           |      |         |     | Dload | Upload | Total    | Spent    | Left     | Speed |
| ----- | ------ | --------- | ---- | ------- | --- | ----- | ------ | -------- | -------- | -------- | ----- |
| 100   | 3722   | 100       | 3722 | 0       | 0   | 391k  | 0      | --:--:-- | --:--:-- | --:--:-- | 391k  |
| 100   | 3722   | 100       | 3722 | 0       | 0   | 376k  | 0      | --:--:-- | --:--:-- | --:--:-- | 376k  |
| Enter | import | password: |      | ******* |     |       |        |          |          |          |       |
Leaf certificate is validated with root-cert and imported successfully.
switch(config-cert-leaf-cert2)#
| Command        | History     |         |     |         |     |              |           |     |     |     |     |
| -------------- | ----------- | ------- | --- | ------- | --- | ------------ | --------- | --- | --- | --- | --- |
| Release        |             |         |     |         |     | Modification |           |     |     |     |     |
| 10.07orearlier |             |         |     |         |     | --           |           |     |     |     |     |
| Command        | Information |         |     |         |     |              |           |     |     |     |     |
| Platforms      |             | Command |     | context |     |              | Authority |     |     |     |     |
Allplatforms config-cert-<CERT-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| import | (self-signed |             |     | leaf      | certificate) |       |     |     |     |     |     |
| ------ | ------------ | ----------- | --- | --------- | ------------ | ----- | --- | --- | --- | --- | --- |
| import | terminal     | self-signed |     | [password |              | <PW>] |     |     |     |     |     |
import <REMOTE-URL> self-signed [password <PW>][vrf <VRF-NAME>]
| import | <STORAGE-URL> |     | self-signed |     | [password |     | <PW>] |     |     |     |     |
| ------ | ------------- | --- | ----------- | --- | --------- | --- | ----- | --- | --- | --- | --- |
Description
Importsaself-signedleafcertificateincludingitsmatchingprivatekey.
| Parameter |     |     |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
terminal ImportthecertificatebypastingPEM-formatdataattheconsole.
Uponexecution,theconfig-cert-importcontextisenteredfor
PKI|188

| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
certificatepasting.Tocompletecertificatedataentrypress
Control-Dinyourterminalprogram.Alternatively,thepasted
certificatedatacanincludeatitsendthedelimiterEND_OF_
|     |     |     | CERTIFICATE(afterthe-----END |     |     | CERTIFICATE-----line), |
| --- | --- | --- | ---------------------------- | --- | --- | ---------------------- |
makingentryofControl-Dunnecessary.
password <PW> Specifiestheplaintextpasswordusedtodecrypttheprivatekeyin
theimportedcertificatedata.Whenthisparameterisomitted,the
passwordispromptedforasrequired.Range:1to32
alphanumericcharacters.
<REMOTE-URL> SpecifiesacertificatedatafileonaremoteTFTPorSFTPserver.
TheURLsyntaxis:
|     |     |     | {tftp://  | | sftp://<USER>@}          |     | {<IP>|<HOST>} |
| --- | --- | --- | --------- | -------------------------- | --- | ------------- |
|     |     |     | [:<PORT>] | [;blocksize=<SIZE>]/<FILE> |     |               |
vrf <VRF-NAME> SpecifiesthenameoftheVRFtousefortheremoteURLfile
transfer.Thedefaultismgmt.
<STORAGE-URL>
AvailableonswitchfamiliesthatprovideUSBdevicefileimport
capability,specifiesacertificatedatafileonaUSBstoragedevice
insertedintheswitchUSBport.TheURLsyntaxisusb:/<FILE>.
Usage
n Thiscommandcannotbeusedwiththedefaultcertificatelocal-cert.
n ThePEMdataformatissupportedforallimportsources.ThePKCS#12dataformatissupportedfor
<REMOTE-URL>and<STORAGE-URL>.
n ThePEMdatamustbedelimitedwiththeselinesforthecertificatedata:
| -----BEGIN | CERTIFICATE----- |     |     |     |     |     |
| ---------- | ---------------- | --- | --- | --- | --- | --- |
| -----END   | CERTIFICATE----- |     |     |     |     |     |
AndthePEMdatamustbedelimitedwitheitheroftheselinepairsfortheprivatekeydata:
| -----BEGIN | PRIVATE   | KEY----- |          |     |     |     |
| ---------- | --------- | -------- | -------- | --- | --- | --- |
| -----END   | PRIVATE   | KEY----- |          |     |     |     |
| -----BEGIN | ENCRYPTED | PRIVATE  | KEY----- |     |     |     |
| -----END   | ENCRYPTED | PRIVATE  | KEY----- |     |     |     |
Example
Importingaself-signedleafcertificatefromtheconsole:
| switch(config)#                   |     | crypto pki | certificate | ss-leaf-cert |             |     |
| --------------------------------- | --- | ---------- | ----------- | ------------ | ----------- | --- |
| switch(config-cert-ss-leaf-cert)# |     |            | import      | terminal     | self-signed |     |
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-cert-import)# |     |     | -----BEGIN | CERTIFICATE----- |     |     |
| --------------------------- | --- | --- | ---------- | ---------------- | --- | --- |
switch(config-cert-import)# MIID2TCCAsGgAwIBAgIJAKcrqokm6p9GMA0GCSqGSIb3DQEBCwUAM
switch(config-cert-import)# tDCCA5ygAwIBAgICEAEwDQYJKoZIhvcNAQELBQAwgYgxCzABAYTAl
switch(config-cert-import)# VQQGEwJVUzELMAkGA1UECAwCQ0ExDTALBgNVBAcMBFJvc2UxDDAKB
...
switch(config-cert-import)# +fWQLxhp+jKJGZGOZz/FENt2uSfZHzlXiu8n3g+EgqExenY1pBRJr
switch(config-cert-import)# VuEEoNb/YfkPXHHva4Zfx223q+f694wlVsHkENSzqr2goHpa2fOzq
switch(config-cert-import)# alewwdmVqCES+x8bvhf3C/6IB6ePkEsnMlHNTeM=
| switch(config-cert-import)# |     |     | -----END | CERTIFICATE----- |     |     |
| --------------------------- | --- | --- | -------- | ---------------- | --- | --- |
switch(config-cert-import)# -----BEGIN ENCRYPTED PRIVATE KEY-----
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 189

switch(config-cert-import)# MIIFDjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBQwwDgQIt8Ni3
switch(config-cert-import)# MBQGCCqGSIb3DQMHBAiBHrejkcdpdASCBMjVxrrYYPNt3V1abr9k8
switch(config-cert-import)# 5GE0U99awh9ys4360WR95xOFGThvjkTyRWG511nGwVeLZs/7TPXWI
...
switch(config-cert-import)# hzc5ZT/w2F08icRI5mFbGoTAAw9IIWMOXGweaWQJDyKGrhg89GrnV
switch(config-cert-import)# M2UuP/tYuuO328QcenKZEJmZKCbx78oFRR+pgma4oeMaFTIyXE6Pr
switch(config-cert-import)# GAdCK8tkDiJ9DKbqdM5W0/nTJfqwUQlfl27dNrBAodsHdrw3UR99H
| switch(config-cert-import)# |     | SPo= |     |     |     |     |     |
| --------------------------- | --- | ---- | --- | --- | --- | --- | --- |
switch(config-cert-import)# -----END ENCRYPTED PRIVATE KEY-----
switch(config-cert-import)#
| Enter import | password: | ******* |     |     |     |     |     |
| ------------ | --------- | ------- | --- | --- | --- | --- | --- |
Leaf certificate is validated as self-signed certificate and imported
successfully.
switch(config-cert-ss-leaf-cert)#
Importingaleafcertificatefromaremotefile:
| switch(config)# | crypto | pki certificate |     | ss-leaf-cert2 |     |     |     |
| --------------- | ------ | --------------- | --- | ------------- | --- | --- | --- |
switch(config-cert-ss-leaf-cert2)# import tftp://1.1.1.2/ss2.p12 self-signed
% Total % Received % Xferd Average Speed Time Time Time Current
|              |           |         | Dload  | Upload | Total Spent       | Left     | Speed |
| ------------ | --------- | ------- | ------ | ------ | ----------------- | -------- | ----- |
| 100 3230     | 100 3230  | 0       | 0 875k | 0      | --:--:-- --:--:-- | --:--:-- | 875k  |
| 100 3230     | 100 3230  | 0       | 0 831k | 0      | --:--:-- --:--:-- | --:--:-- | 831k  |
| Enter import | password: | ******* |        |        |                   |          |       |
Leaf certificate is validated as self-signed certificate and imported
successfully.
switch(config-cert-ss-leaf-cert2)#
| Command        | History     |         |              |           |     |     |     |
| -------------- | ----------- | ------- | ------------ | --------- | --- | --- | --- |
| Release        |             |         | Modification |           |     |     |     |
| 10.07orearlier |             |         | --           |           |     |     |     |
| Command        | Information |         |              |           |     |     |     |
| Platforms      | Command     | context |              | Authority |     |     |     |
Allplatforms config-cert-<CERT-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
key-type
key-type {rsa [key-size <K-SIZE>] | ecdsa [curve-size <C-SIZE>]}
Description
Setsthekeytypeandkeysizeforthecurrentleafcertificate.Thekeytypeofthedefaultcertificate
local-certcannotbechanged.
| Parameter |     |     | Description           |     |     |     |     |
| --------- | --- | --- | --------------------- | --- | --- | --- | --- |
| rsa       |     |     | SelectstheRSAkeytype. |     |     |     |     |
key-size <K-SIZE> SpecifiestheRSAkeysizeinbits.Supportedvalues:2048,3072,
PKI|190

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
4096.Default:2048
| ecdsa |     |     | SelectstheECDSAkeytype. |     |     |
| ----- | --- | --- | ----------------------- | --- | --- |
curve-size <C-SIZE> SpecifiestheECDSAellipticcurvesizeinbits.Supportedvalues:
256,348,521.Default:256
Examples
SettingRSAencryptionontheleafcertificateleaf-cert:
| switch(config)#                | crypto | pki certificate |          | leaf-cert         |     |
| ------------------------------ | ------ | --------------- | -------- | ----------------- | --- |
| switch(config-cert-leaf-cert)# |        |                 | key-type | rsa key-size 3072 |     |
SettingECDSAencryptionontheleafcertificateleaf-cert:
| switch(config)#                | crypto  | pki certificate |              | leaf-cert        |     |
| ------------------------------ | ------- | --------------- | ------------ | ---------------- | --- |
| switch(config-cert-leaf-cert)# |         |                 | key-type     | ecdsa curve-size | 521 |
| Command History                |         |                 |              |                  |     |
| Release                        |         |                 | Modification |                  |     |
| 10.07orearlier                 |         |                 | --           |                  |     |
| Command Information            |         |                 |              |                  |     |
| Platforms                      | Command | context         |              | Authority        |     |
Allplatforms config-cert-<CERT-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
ocsp disable-nonce
ocsp disable-nonce
no ocsp disable-nonce
Description
ConfiguresexclusionofthenoncefromOCSPrequests.AnonceisauniqueidentifierthatanOCSP
clientinsertsinanOCSPrequestandexpectstheOCSPrespondertoincludeitinthecorresponding
OCSPresponse.Thenoncemechanismhelpspreventreplayattacksinwhichamaliciousplayer
attemptstomasqueradeastheOCSPresponder.Althoughthenonceisincludedbydefault,itcanbe
excluded.SomeOCSPresponderschoosetonotsupporttheuseofthenonceduetoperformance
considerations.
Thenoformofthiscommandre-enablesnonceinclusioninOCSPrequests.
Examples
DisableinclusionofthenonceinOCSPrequestsforTAprofileroot-cert:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 191

| switch(config)# |     | crypto pki | ta-profile | root-cert |
| --------------- | --- | ---------- | ---------- | --------- |
switch(config-ta-root-cert)#
ocsp disable-nonce
EnableinclusionofthenonceinOCSPrequestsforTAprofileroot-cert:
| switch(config)#              |         | crypto pki | ta-profile | root-cert          |
| ---------------------------- | ------- | ---------- | ---------- | ------------------ |
| switch(config-ta-root-cert)# |         |            | no         | ocsp disable-nonce |
| Command History              |         |            |            |                    |
| Release                      |         |            |            | Modification       |
| 10.07orearlier               |         |            |            | --                 |
| Command Information          |         |            |            |                    |
| Platforms                    | Command | context    |            | Authority          |
Allplatforms config-ta-<TA-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ocsp enforcement-level
| ocsp enforcement-level |     | {strict | | optional} |     |
| ---------------------- | --- | ------- | ----------- | --- |
no enforcement-level
Description
SetseitherstrictorreducedenforcementoftheOCSPcheckofcertificates.Strictenforcementis
enabledbydefault.
Thenoformofthiscommandresetsenforcementtoitsdefaultofstrict.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
strict SetsstrictOCSPcheckingofcertificates.Thecertificateisaccepted
onlyifallpossiblechecking(includingvalidationfailures,software
systemerrors,configurationerrors,transactionalerrors)is
successful.
optional SetsreducedOCSPcheckingofcertificates.Thecertificateis
acceptedunlessoneormoreofthesevalidationerrorsoccur:
|     |     |     |     | n Responsesignatureinvalid.                          |
| --- | --- | --- | --- | ---------------------------------------------------- |
|     |     |     |     | n Nonceinresponsemismatch.                           |
|     |     |     |     | n Certificaterevoked,butonlywhenrevocationcheckingis |
possible.ifrevocationcheckisnotpossible,thecertificateis
stillacceptediftherearenoothervalidationerrors.
Examples
SettingreducedOCSPcheckingofcertificates:
PKI|192

| switch(config)# |     | crypto | pki | ta-profile | root-cert |     |     |
| --------------- | --- | ------ | --- | ---------- | --------- | --- | --- |
switch(config-ta-root-cert)#
|     |     |     |     | ocsp | enforcement-level |     | optional |
| --- | --- | --- | --- | ---- | ----------------- | --- | -------- |
SettingstrictOCSPcheckingofcertificates:
| switch(config)#              |             | crypto  | pki     | ta-profile | root-cert         |     |        |
| ---------------------------- | ----------- | ------- | ------- | ---------- | ----------------- | --- | ------ |
| switch(config-ta-root-cert)# |             |         |         | ocsp       | enforcement-level |     | strict |
| Command                      | History     |         |         |            |                   |     |        |
| Release                      |             |         |         |            | Modification      |     |        |
| 10.07orearlier               |             |         |         |            | --                |     |        |
| Command                      | Information |         |         |            |                   |     |        |
| Platforms                    |             | Command | context |            | Authority         |     |        |
Allplatforms config-ta-<TA-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ocsp url
| ocsp url    | {primary | | secondary} |            | <URL> |     |     |     |
| ----------- | -------- | ------------ | ---------- | ----- | --- | --- | --- |
| no ocsp url | {primary | |            | secondary} |       |     |     |     |
Description
ConfigurestheOCSPresponderURLsthatthecurrentTAprofileusestoverifytherevocationstatusof
anX.509digitalcertificate.TheseURLsoverridetheOCSPresponderURLcontainedwithinthepeer
certificatebeingverified(aswellasURLsdefinedinanyintermediateCAsinthechainoftrust).
IfnoOCSPresponderURLsaredefinedforaTAprofile(defaultsetting),thentheOCSPresponderURL
inthepeercertificateisusedforrevocationstatuschecking.(TheOCSPresponderURLiscontainedina
certificate'sAuthorityInformationAccessfield,whichisanX.509v3certificateextension.)
ThenoformofthiscommanddeletesthespecifiedOCSPresponderURL(primaryorsecondary)from
thecurrentTAprofile.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
{primary | secondary} <URL> SpecifytheHTTPURLoftheprimaryorsecondaryOCSP
responderusingeitherafullyqualifieddomainnameorIPv4
address.
Examples
DefiningtheprimaryOCSPURLfortheTAprofileroot-cert:
| switch(config)#              |     | crypto | pki | ta-profile       | root-cert |      |     |
| ---------------------------- | --- | ------ | --- | ---------------- | --------- | ---- | --- |
| switch(config-ta-root-cert)# |     |        |     | revocation-check |           | ocsp |     |
switch(config-ta-root-cert)# ocsp url primary http://ocsp-server.site.com
RemovingtheprimaryOCSPURLfromtheTAprofileroot-cert:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 193

| switch(config)# | crypto | pki | ta-profile | oot-cert |
| --------------- | ------ | --- | ---------- | -------- |
switch(config-ta-root-cert)#
revocation-check ocsp
| switch(config-ta-root-cert)# |         |         | no  | ocsp url primary |
| ---------------------------- | ------- | ------- | --- | ---------------- |
| Command History              |         |         |     |                  |
| Release                      |         |         |     | Modification     |
| 10.07orearlier               |         |         |     | --               |
| Command Information          |         |         |     |                  |
| Platforms                    | Command | context |     | Authority        |
Allplatforms config-ta-<TA-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ocsp vrf
ocsp vrf <VRF-NAME>
no ocsp vrf
Description
SetstheVRFthattheswitchusestocommunicatewithOCSPrespondersforOCSPchecking.VRFmgmt
isusedbydefault.
ThenoformofthiscommandresetstheVRFtoitsdefaultmgmt.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<VRF-NAME>
SpecifiesthenameoftheVRFtheswitchusestocommunicate
withOCSPresponders.Default:mgmt.
Examples
SettingtheOCSPresponderVRFtocorp1:
| switch(config)#              | crypto | pki | ta-profile | root-cert |
| ---------------------------- | ------ | --- | ---------- | --------- |
| switch(config-ta-root-cert)# |        |     | ocsp       | vrf corp1 |
RevertingtheOCSPresponderVRFtoitsdefault:
| switch(config)#              | crypto | pki | ta-profile | root-cert    |
| ---------------------------- | ------ | --- | ---------- | ------------ |
| switch(config-ta-root-cert)# |        |     | no         | ocsp vrf     |
| Command History              |        |     |            |              |
| Release                      |        |     |            | Modification |
| 10.07orearlier               |        |     |            | --           |
| Command Information          |        |     |            |              |
PKI|194

| Platforms | Command | context |     | Authority |     |
| --------- | ------- | ------- | --- | --------- | --- |
Allplatforms config-ta-<TA-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| revocation-check |      | ocsp |     |     |     |
| ---------------- | ---- | ---- | --- | --- | --- |
| revocation-check | ocsp |      |     |     |     |
no revocation-check
Description
Enablescertificaterevocationcheckingforthecurrentprofileusingtheonlinecertificatestatusprotocol
(OCSP).
Thenoformofthiscommanddisablescertificaterevocationcheckingforthecurrentprofile.
Examples
EnablingrevocationcheckingfortheTAprofileroot-cert:
| switch(config)#              | crypto | pki | ta-profile       | root-cert |      |
| ---------------------------- | ------ | --- | ---------------- | --------- | ---- |
| switch(config-ta-root-cert)# |        |     | revocation-check |           | ocsp |
DisablingrevocationcheckingfortheTAprofileroot-cert:
| switch(config)#              | crypto  | pki     | ta-profile          | root-cert |     |
| ---------------------------- | ------- | ------- | ------------------- | --------- | --- |
| switch(config-ta-root-cert)# |         |         | no revocation-check |           |     |
| Command History              |         |         |                     |           |     |
| Release                      |         |         | Modification        |           |     |
| 10.07orearlier               |         |         | --                  |           |     |
| Command Information          |         |         |                     |           |     |
| Platforms                    | Command | context |                     | Authority |     |
Allplatforms config-ta-<TA-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show crypto | pki application |     |     |     |     |
| ----------- | --------------- | --- | --- | --- | --- |
| show crypto | pki application |     |     |     |     |
Description
Showscertificateinformationforallfeatures(applications)usingleafcertificatesthataremanagedby
PKI.
Examples
Showingcertificateinformationforallfeatures(applications)usingleafcertificates:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 195

| switch#    | show crypto  | pki application1 |      |             |     |
| ---------- | ------------ | ---------------- | ---- | ----------- | --- |
| Associated | Applications | Certificate      | Name | Cert Status |     |
------------------------ ---------------------- --------------------------------
| https-server   |             |                 |              | not configured, | using local-cert |
| -------------- | ----------- | --------------- | ------------ | --------------- | ---------------- |
| syslog-client  |             | local-cert      |              | valid           |                  |
| hsc            |             | xhsccert        |              | invalid, using  | local-cert       |
| radsec-client  |             | device-identity |              | valid           |                  |
| Command        | History     |                 |              |                 |                  |
| Release        |             |                 | Modification |                 |                  |
| 10.07orearlier |             |                 | --           |                 |                  |
| Command        | Information |                 |              |                 |                  |
| Platforms      | Command     | context         | Authority    |                 |                  |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show crypto | pki             | certificate  |            |         |     |
| ----------- | --------------- | ------------ | ---------- | ------- | --- |
| show crypto | pki certificate | [<CERT-NAME> | [plaintext | | pem]] |     |
Description
Showsalistofallconfiguredleafcertificates,ordetailedinformationforaspecificleafcertificate.
PossiblevaluesforCertStatusare:CSR pending,expired,expires soon,installed,malformed,not
yet known.
PossiblevaluesforESTStatusare:enroll failed, enroll pending,enroll retrying,enroll success,
n/a(certificateisnotEST-enrolled),reenroll failed,reenroll pending,reenroll retrying.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<CERT-NAME> Specifiestheleafcertificatename.Range:1to32alphanumeric
charactersexcluding"
plaintext
Showscertificateinformationinplaintext.
| pem |     |     | ShowscertificateinformationinPEMformat. |     |     |
| --- | --- | --- | --------------------------------------- | --- | --- |
Examples
Showingalistofallconfiguredleafcertificates:
| switch# | show crypto | pki certificate |     |     |     |
| ------- | ----------- | --------------- | --- | --- | --- |
Certificate Name Cert Status EST Status Associated Applications
-------------------- -------------- ----------------- ----------------------------
--
| local-cert |     | installed | n/a | radsec-client, | captive- |
| ---------- | --- | --------- | --- | -------------- | -------- |
portal
PKI|196

| device-identity |     |     | installed |         | n/a    |          |     |     | none          |            |
| --------------- | --- | --- | --------- | ------- | ------ | -------- | --- | --- | ------------- | ---------- |
| pod01-99-1      |     |     | installed |         | n/a    |          |     |     | https-server, | est-client |
| syslog-1        |     |     | CSR       | pending | enroll | retrying |     |     | syslog-client |            |
| leaf-cert1      |     |     | installed |         | enroll | success  |     |     | none          |            |
| leaf-cert2      |     |     | CSR       | pending | enroll | failed   |     |     | none          |            |
Showingdetailedinformation(inplaintextformat)forleafcertificatepod01-99-1:
| switch#     | show          | crypto        | pki        | certificate | pod01-99-1 |     | plaintext |     |     |     |
| ----------- | ------------- | ------------- | ---------- | ----------- | ---------- | --- | --------- | --- | --- | --- |
| Certificate |               | Name:         | pod01-99-1 |             |            |     |           |     |     |     |
| Associated  |               | Applications: |            |             |            |     |           |     |     |     |
|             | https-server, |               | est-client |             |            |     |           |     |     |     |
| Certificate |               | Status:       | installed  |             |            |     |           |     |     |     |
| EST         | Status:       | n/a           |            |             |            |     |           |     |     |     |
| Certificate |               | Type:         | regular    |             |            |     |           |     |     |     |
Intermediates:
Subject: C = US, ST = CA, O = Company, OU = Lab-IT, CN = DeviceCA
|     | Issuer: | C =     | US, ST | = CA, | O = Company, |     | OU = | Lab-IT, | CN = Lab-CA |     |
| --- | ------- | ------- | ------ | ----- | ------------ | --- | ---- | ------- | ----------- | --- |
|     | Serial  | Number: | 0x02   |       |              |     |      |         |             |     |
Subject: C = US, ST = CA, O = Company, OU = Lab-IT, CN = Lab-CA
Issuer: C = US, ST = CA, O = Company, OU = Lab-IT, CN = Lab-Root
|     | Serial | Number: | 0x01 |     |     |     |     |     |     |     |
| --- | ------ | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Certificate:
Data:
|     | Version:  | 1          | (0x0)                |                         |     |            |                      |             |     |     |
| --- | --------- | ---------- | -------------------- | ----------------------- | --- | ---------- | -------------------- | ----------- | --- | --- |
|     | Serial    | Number:    | 14529416756121781768 |                         |     |            | (0xc9a2db8f3e3f4608) |             |     |     |
|     | Signature | Algorithm: |                      | sha256WithRSAEncryption |     |            |                      |             |     |     |
|     | Issuer:   | C=US,      | ST=CA,               | OU=Lab-IT,              |     | O=Company, |                      | CN=DeviceCA |     |     |
Validity
|     |          | Not Before: |                | Jan 12     | 23:36:57      | 2018       | GMT |               |     |     |
| --- | -------- | ----------- | -------------- | ---------- | ------------- | ---------- | --- | ------------- | --- | --- |
|     |          | Not After   | :              | Nov 1      | 23:36:57      | 2020       | GMT |               |     |     |
|     | Subject: | C=US,       | ST=CA,         | OU=Lab-IT, |               | O=Company, |     | CN=pod01-99-1 |     |     |
|     | Subject  | Public      | Key            | Info:      |               |            |     |               |     |     |
|     |          | Public      | Key Algorithm: |            | rsaEncryption |            |     |               |     |     |
|     |          | Public-Key: |                | (2048      | bit)          |            |     |               |     |     |
Modulus:
00:a0:cd:ef:1b:f9:b8:bd:39:fc:7a:0e:00:17:ff:
2b:72:d8:4e:d4:df:49:36:ca:3a:f9:05:05:d7:e3:
d1:97:29:71:e6:33:b8:bb:8e:f0:ee:a6:e4:4a:f8:
...
fe:dd:d9:a0:af:59:47:25:b4:34:06:af:03:1d:33:
30:c3:85:fe:5c:e7:19:7f:ff:3a:b2:21:b8:e8:ed:
83:09
|     |           | Exponent:  |     | 65537                   | (0x10001) |     |     |     |     |     |
| --- | --------- | ---------- | --- | ----------------------- | --------- | --- | --- | --- | --- | --- |
|     | Signature | Algorithm: |     | sha256WithRSAEncryption |           |     |     |     |     |     |
39:f6:03:86:03:d9:05:61:39:25:5f:0d:75:cc:05:ae:04:7e:
4c:a3:13:0b:f0:1e:af:68:0e:40:9f:ed:48:b6:5e:56:8c:53:
46:5b:c9:a4:e0:b0:bc:31:4b:a7:5d:0a:ed:7c:9c:f6:bf:1e:
...
39:f5:26:58:68:e2:13:ec:94:ac:60:8e:4b:b0:ba:45:cf:d6:
6a:4b:9f:7d:ae:3f:e5:2e:81:fe:ac:b3:65:44:35:47:a5:2f:
89:e7:58:a0
Showingdetailedinformation(inPEMformat)forleafcertificateleaf-cert1withastatusofCSR
pending:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 197

|     | switch#     | show | crypto        | pki        | certificate | leaf-cert1 | pem |
| --- | ----------- | ---- | ------------- | ---------- | ----------- | ---------- | --- |
|     | Certificate |      | Name:         | leaf-cert1 |             |            |     |
|     | Associated  |      | Applications: |            |             |            |     |
syslog-client
|     | Certificate |         | Status:     | CSR      | pending      |     |     |
| --- | ----------- | ------- | ----------- | -------- | ------------ | --- | --- |
|     | EST         | Status: | enroll      | retrying |              |     |     |
|     | Certificate |         | Type:       | regular  |              |     |     |
|     | -----BEGIN  |         | CERTIFICATE |          | REQUEST----- |     |     |
MIICtTCCAZ0CAQAwcDEWMBQGA1UEAxMNc3lzbG9nLTg0MBYGA1UECxMPQ
XJ1YmEtUm9zZXZpbGxlMQ4wDAYDVQQKEYTESMBAGA1EBxMJUm9zZXZpbG
xlMQswCQYDVQQIEwJDQTELMAGA1UEBhMCVVMwggEiMSIb3DQEBAQUAA4I
...
cw2ytN6Idgh81k59x6DH7V/eORaKd5lq+oO7nkr6+QBf5L3f5Kb+TOFio
lei+EdCHMxxc07MK0n3dkziSW25HFUGsyEXVMK+BID3zbKDoUe6XVhvqI
mamXyghigLYDcbsn6WVw==
|                | -----END |             | CERTIFICATE |         | REQUEST----- |              |     |
| -------------- | -------- | ----------- | ----------- | ------- | ------------ | ------------ | --- |
| Command        |          | History     |             |         |              |              |     |
| Release        |          |             |             |         |              | Modification |     |
| 10.07orearlier |          |             |             |         |              | --           |     |
| Command        |          | Information |             |         |              |              |     |
| Platforms      |          |             | Command     | context |              | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show | crypto |     | pki ta-profile |     |             |     |     |
| ---- | ------ | --- | -------------- | --- | ----------- | --- | --- |
| show | crypto | pki | ta-profile     |     | [<TA-NAME>] |     |     |
Description
ShowsalistofallconfiguredTAprofiles,ordetailedinformationforaspecificprofile.
Thiscommandshowsinformationforbothdirectly-configuredTAprofilesandTAprofilesthatweredynamically
downloadedfromESTservers.
| Parameter |     |     |     |     |     | Description                                       |     |
| --------- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- |
| <TA-NAME> |     |     |     |     |     | SpecifiestheTAprofilename.Range:1to48alphanumeric |     |
charactersexcluding".
Examples
ShowingalistofallconfiguredTAprofiles:
PKI|198

| switch# | show | crypto | pki | ta-profile |     |                |     |            |       |
| ------- | ---- | ------ | --- | ---------- | --- | -------------- | --- | ---------- | ----- |
| Profile | Name |        |     |            |     | TA Certificate |     | Revocation | Check |
-------------------------------- ------------------ ----------------
| BASE_CA      |     |     |     |     |     | Installed,valid   |     | disabled |     |
| ------------ | --- | --- | --- | --- | --- | ----------------- | --- | -------- | --- |
| BASE02_CA    |     |     |     |     |     | Installed,expired |     | disabled |     |
| root-cert    |     |     |     |     |     | Installed,valid   |     | OCSP     |     |
| ROOT-A_CA    |     |     |     |     |     | Not Installed     |     | OCSP     |     |
| EST-Service1 |     |     |     |     |     | Installed,valid   |     | None     |     |
| EST-Service2 |     |     |     |     |     | Installed,valid   |     | None     |     |
ShowingdetailedinformationforTAprofileroot-cert:
| switch#    | show         | crypto        | pki       | ta-profile |                           | root-cert  |     |     |     |
| ---------- | ------------ | ------------- | --------- | ---------- | ------------------------- | ---------- | --- | --- | --- |
| TA         | Profile      | Name          |           |            | : root-cert               |            |     |     |     |
| Revocation |              | Check         |           |            | : OCSP                    |            |     |     |     |
|            | OSCP         | Primary       | URL       |            | : http://ocsp1.domain.com |            |     |     |     |
|            | OCSP         | Secondary     | URL       |            | : Not                     | Configured |     |     |     |
|            | OCSP         | Disable-nonce |           |            | : false                   |            |     |     |     |
|            | OCSP         | Enforcement   |           | Level:     | strict                    |            |     |     |     |
|            | OCSP         | VRF           |           |            | : mgmt                    |            |     |     |     |
| TA         | Certificate: |               | Installed |            | and                       | valid      |     |     |     |
|            | Version:     | 3             | (0x2)     |            |                           |            |     |     |     |
|            | Serial       | Number:       |           |            |                           |            |     |     |     |
74:e6:6d:22:3f:52:cc:94:43:41:ab:66:a8:8d:47:b1
|     | Signature |                 | Algorithm: | sha1withRSAEncryption |                |     |             |       |     |
| --- | --------- | --------------- | ---------- | --------------------- | -------------- | --- | ----------- | ----- | --- |
|     | Issuer:   | OU=DeviceTrust, |            |                       | OU=Operations, |     | O=Site,     | C=US, |     |
|     |           | CN=Site         | Trusted    |                       | Computing      |     | Root CA 1.0 |       |     |
Validity
|     | Not      | Before:         | Sep            | 14      | 03:12:06       | 2007 | GMT         |       |     |
| --- | -------- | --------------- | -------------- | ------- | -------------- | ---- | ----------- | ----- | --- |
|     | Not      | After           | : Sep          | 14      | 03:21:14       | 2032 | GMT         |       |     |
|     | Subject: | OU=DeviceTrust, |                |         | OU=Operations, |      | O=Site,     | C=US, |     |
|     |          | CN=Site         |                | Trusted | Computing      |      | Root CA 1.0 |       |     |
|     | Subject  | Public          | Key            | Info:   |                |      |             |       |     |
|     | Public   |                 | Key Algorithm: |         | rsaEncryption  |      |             |       |     |
|     |          | RSA             | Public         | Key:    | (2048          | bit) |             |       |     |
|     |          | Modulus         | (2048          | bit):   |                |      |             |       |     |
30:0d:06:09:2a:86:48:86:f7:0d:01:01:01:05:33:
03:82:01:0f:00:30:82:01:3a:02:82:01:01:00:ac:
3d:60:3a:2e:ca:a4:34:db:5c:3b:6b:07:df:73:62:
...
20:c8:df:63:14:5a:e8:d3:ea:83:d8:47:a3:b5:2e:
bb:64:51:f0:be:13:b6:91:e4:32:45:58:5e:1f:0d:
02:03:01:00:01
|     |        | Exponent:   | 65537              |     | (0x10001)   |     |          |             |     |
| --- | ------ | ----------- | ------------------ | --- | ----------- | --- | -------- | ----------- | --- |
|     | X509v3 | extensions: |                    |     |             |     |          |             |     |
|     | X509v3 |             | Key Usage:         |     |             |     |          |             |     |
|     |        | Digital     | Signature,         |     | Certificate |     | Signing, | CRL Signing |     |
|     | X509v3 |             | Basic Constraints: |     |             |     |          |             |     |
|     |        | CA:TRUE,    | pathlen:4          |     |             |     |          |             |     |
|     | X509v3 |             | Subject            | Key | Identifier: |     |          |             |     |
eb:d7:ec:db:8a:cb:f2:51:d5:06:e1:42:7b:39:a7:d0:1e:31:6e:bf
|     | Signature |     | Algorithm: | sha1withRSAEncryption |     |     |     |     |     |
| --- | --------- | --- | ---------- | --------------------- | --- | --- | --- | --- | --- |
1c:90:f3:a4:f0:0d:e2:e3:e9:ae:01:e1:7d:a7:13:e2:cc:0b:
17:31:26:92:a2:5d:1d:19:60:54:03:13:9b:e1:73:6c:e4:b3:
01:4f:4e:ae:61:bd:ae:b6:12:d3:ab:08:ae:8c:47:92:d7:0d:
...
ca:cf:11:78:55:6d:06:49:fa:d4:8d:f3:ef:7f:79:38:35:5d:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 199

16:5a:57:7f:a8:dc:b0:f8:a2:04:0d:17:0b:bb:58:32:30:e0:
2d:a8:37:a2
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ta-certificate
ta-certificate { [import [terminal]] | import {<REMOTE-URL> | <STORAGE-URL>} }
Description
ImportsaCAcertificateforuseinthecurrentTAprofile.ThecertificatemustbeinPEMformat.ThePEM
datamustbedelimitedwiththeselines:
| -----BEGIN CERTIFICATE----- |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- |
-----END CERTIFICATE-----
OnlythefirstcertificateinthePEMdataisimported.Anyadditionalcertificatesareignored.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
[import [terminal]] ImportthecertificatebypastingPEM-formatdataattheconsole.
Uponexecution,theconfig-cert-importcontextisenteredfor
certificatepasting.Tocompletecertificatedataentrypress
Control-Dinyourterminalprogram.Alternatively,thepasted
certificatedatacanincludeatitsendthedelimiterEND_OF_
|     |     |     | CERTIFICATE(afterthe-----END |     | CERTIFICATE-----line), |
| --- | --- | --- | ---------------------------- | --- | ---------------------- |
makingentryofControl-Dunnecessary.
import <REMOTE-URL> ImportthecertificatefromafileonaremoteTFTPorSFTPserver.
TheURLsyntaxis:
|     |     |     | {tftp://  | | sftp://<USER>@}          | {<IP>|<HOST>} |
| --- | --- | --- | --------- | -------------------------- | ------------- |
|     |     |     | [:<PORT>] | [;blocksize=<SIZE>]/<FILE> |               |
import <STORAGE-URL> AvailableonswitchfamiliesthatprovideUSBdevicefileimport
capability,importthecertificatefromafileonaUSBstorage
deviceinsertedintheswitchUSBport.TheURLsyntaxis
usb:/<FILE>.
Example
ImportingacertificateintotheTAprofileroot-certbypastingPEM-formatcertificatedataatthe
console:
PKI|200

| switch(config)# |     | crypto | pki | ta-profile |     | root-cert |     |     |
| --------------- | --- | ------ | --- | ---------- | --- | --------- | --- | --- |
switch(config-ta-root-cert)#
|     |     |     |     | ta-certificate |     |     | import | terminal |
| --- | --- | --- | --- | -------------- | --- | --- | ------ | -------- |
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-ta-cert)# |     |     |     | -----BEGIN |     | CERTIFICATE----- |     |     |
| ----------------------- | --- | --- | --- | ---------- | --- | ---------------- | --- | --- |
switch(config-ta-cert)# MIIDuTCCAqECCQCuoxeJ2ZNYcjANBgkqhkiG9w0BAQsFADCBqzELMAEBh
switch(config-ta-cert)# VVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEDAOBgNVBAcMB1JvY2tsDAKBg
switch(config-ta-cert)# BAoMA0hQTjEVMBMGA1UECwwMSFBOUm9zZXZpbGxlMSowKAYDVQocG5zdz
...
switch(config-ta-cert)# x3WFf3dFZ8o9sd5LVAHneH/ztb9MP34z+le1V346r12L2kpxmTOVJVyTO
switch(config-ta-cert)# BIzD/ST/HaWI+0S+S80rm93PSscEbb9GWk7vshh5EnW/moehBKcE4O1zy
switch(config-ta-cert)# 3LvMLZcssSe5J2Ca2XIhfDme8UaNZ7syGYMsAW0nG7yYHWkEOQu9s
| switch(config-ta-cert)# |     |     |     | -----END | CERTIFICATE----- |     |     |     |
| ----------------------- | --- | --- | --- | -------- | ---------------- | --- | --- | --- |
switch(config-ta-cert)#
The certificate you are importing has the following attributes:
| Issuer: |     | C=US, ST=CA, | L=Rocklin, |     | O=Company, |     | OU=Site, |     |
| ------- | --- | ------------ | ---------- | --- | ---------- | --- | -------- | --- |
CN=site.com/emailAddress=test.ca@site.com
| Subject: |     | C=US, ST=CA, | L=Rocklin, |     | O=Company, |     | OU=Site, |     |
| -------- | --- | ------------ | ---------- | --- | ---------- | --- | -------- | --- |
CN=9000/emailAddress=test.ca@site.com
| Serial | Number:     | 12121221634631568498 |      |             |      | (0xaea51217d5945772) |     |              |
| ------ | ----------- | -------------------- | ---- | ----------- | ---- | -------------------- | --- | ------------ |
| TA     | certificate | import               | is   | allowed     | only | once                 | for | a TA profile |
| Do     | you want    | to accept            | this | certificate |      | (y/n)?               |     |              |
y
| TA  | certificate | accepted. |     |     |     |     |     |     |
| --- | ----------- | --------- | --- | --- | --- | --- | --- | --- |
switch(config-ta-root-cert)#
ImportingacertificateintotheTAprofileroot-cert2fromfilercert2-dataontheUSBdevice:
| switch(config)# |     | crypto | pki | ta-profile |     | root-cert2 |     |     |
| --------------- | --- | ------ | --- | ---------- | --- | ---------- | --- | --- |
switch(config-ta-root-cert2)# ta-certificate import usb:/rcert2-data
The certificate you are importing has the following attributes:
| Issuer: | C=US, | ST=California, |     | L=Rocklin, |     |     | O=Company, | OU=Site, |
| ------- | ----- | -------------- | --- | ---------- | --- | --- | ---------- | -------- |
CN=site.com/emailAddress=test.ca@site.com
| Subject: |     | C=US, ST=California, |     |     | L=Rocklin, |     | O=Company, | OU=Site, |
| -------- | --- | -------------------- | --- | --- | ---------- | --- | ---------- | -------- |
CN=9000/emailAddress=test.ca@site.com
| Serial | Number:     | 12121221634631568498 |      |             |      | (0xaea51217d5945772) |     |              |
| ------ | ----------- | -------------------- | ---- | ----------- | ---- | -------------------- | --- | ------------ |
| TA     | certificate | import               | is   | allowed     | only | once                 | for | a TA profile |
| Do     | you want    | to accept            | this | certificate |      | (y/n)?               |     | y            |
| TA     | certificate | accepted.            |      |             |      |                      |     |              |
switch(config-ta-root-cert2)#
| Command        | History     |         |         |     |              |           |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --------- | --- | --- |
| Release        |             |         |         |     | Modification |           |     |     |
| 10.07orearlier |             |         |         |     | --           |           |     |     |
| Command        | Information |         |         |     |              |           |     |     |
| Platforms      |             | Command | context |     |              | Authority |     |     |
Allplatforms config-ta-<TA-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
subject
subject [common-name <COMMON-NAME>] [country <COUNTRY>] [locality <LOCALITY>]
|     | [org | <ORG-NAME>] | [org-unit |     | <ORG-UNIT>] |     | [state | <STATE>] |
| --- | ---- | ----------- | --------- | --- | ----------- | --- | ------ | -------- |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 201

Description
Setsthesubjectfieldsforthecurrentleafcertificate.Ifthecommon-nameparameterisnotspecified,then
youarepromptedtodefineavalueforeachfield.Ifaconfiguredvalueexistsforanyfield,itis
presentedasthedefault.
Thesubjectfieldsofthedefaultcertificatelocal-certcannotbechanged.
| Parameter         |               |     | Description             |
| ----------------- | ------------- | --- | ----------------------- |
| common-name       | <COMMON-NAME> |     | Specifiesthecommonname. |
| country <COUNTRY> |               |     |                         |
Specifiesthecountryorregion.
| locality | <LOCALITY> |     | Specifiesthelocalitysuchascity. |
| -------- | ---------- | --- | ------------------------------- |
org <ORG-NAME>
Specifiestheorganization.
| org-unit | <ORG-UNIT> |     | Specifiestheorganizationalunit. |
| -------- | ---------- | --- | ------------------------------- |
state <STATE>
Specifiesthestate.
Examples
Settingsubjectfieldsfortheleafcertificateleaf-cert:
switch(config-cert-leaf-cert)# subject common-name Leaf01 country US
| locality | CA org Company | org-unit | Site state CA |
| -------- | -------------- | -------- | ------------- |
Settingsubjectfieldsfortheleafcertificateleaf-certinteractively:
| switch(config-cert-leaf-cert)# |     |     | subject |
| ------------------------------ | --- | --- | ------- |
Do you want to use the switch serial number as the common name (y/n)? n
| Enter Common   | Name :         | Leaf01 |     |
| -------------- | -------------- | ------ | --- |
| Enter Org      | Unit : Site    |        |     |
| Enter Org      | Name : Company |        |     |
| Enter Locality | : Rocklin      |        |     |
| Enter State    | : CA           |        |     |
| Enter Country  | : US           |        |     |
switch(config-cert-leaf-cert)#
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms config-cert-<CERT-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
PKI|202

PKI EST commands
arbitrary-label
| arbitrary-label | <LABEL> |     |     |     |
| --------------- | ------- | --- | --- | --- |
no arbitrary-label
Description
WithintheESTprofilecontext,configuresthegenericoptionallabel(alsoknownasarbitrarylabel)tobe
concatenatedtotheESTserverURLthatisconfiguredwiththeurlcommand.Thereisnoarbitrarylabel
configuredbydefault.Anyexistingarbitrarylabelisreplacedbythiscommand.Theuseofarbitrary
labelsisoptional.
RFC7030allowstheuseofarbitrarylabelssothatoneESTservermayservemultipleCAswiththesame
serverURLthatgetsconcatenatedwithdifferentarbitrarylabels.Thesamelabelisusedforevery
requestmadeunderaparticularESTprofile.
SomeESTschemesusearbitrarylabelsinamoresophisticatedway,definingdifferentlabelsfor
differenttypesofrequestsunderthesameESTprofile.Forexample,theCAcertificaterequestcoulduse
thegenericlabel(configuredwiththisarbitrary-labelcommand),thecertificateenrollmentrequest
couldusetheenrollmentlabel(configuredwiththearbitrary-label-enrollmentcommand),andthe
re-enrollmentrequestcouldusethere-enrollmentlabel(configuredwiththearbitrary-label-
reenrollmentcommand).Notethatonlyonelabelofeachofthethreeavailabletypescanbe
configuredinanyESTprofile.
Thenoformofthiscommandremovesthegenericarbitrarylabel.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<LABEL>
Specifiesthegenericarbitrarylabel.Range:Upto64characters.
Examples
ConfiguringtheURLandgenericarbitrarylabel.NotethatwiththeURLandarbitrarylabelconfiguredin
thisexample,thefinalURLtheswitchusestorequestCAcertificatesfromtheESTserveris
https://est-service999.com/.well-known/est/rsa2048/cacerts.
| switch(config)#                  | crypto pki                                     | est-profile     | EST-service1 |         |
| -------------------------------- | ---------------------------------------------- | --------------- | ------------ | ------- |
| switch(config)#                  | url https://est-service999.com/.well-known/est |                 |              |         |
| switch(config-est-EST-service1)# |                                                | arbitrary-label |              | rsa2048 |
Removingthegenericarbitrarylabel:
| switch(config)# | crypto pki | est-profile | EST-service1 |     |
| --------------- | ---------- | ----------- | ------------ | --- |
switch(config-est-EST-service1)#
|     |     | no  | arbitrary-label |     |
| --- | --- | --- | --------------- | --- |
Command History
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
Command Information
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 203

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-est-<EST-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
arbitrary-label-enrollment
| arbitrary-label-enrollment |     | <LABEL> |     |
| -------------------------- | --- | ------- | --- |
no arbitrary-label-enrollment
Description
WithintheESTprofilecontext,configuresthearbitraryenrollmentlabeltobeconcatenatedtotheEST
serverURLthatisconfiguredwiththeurlcommand.Thislabelisspecifictotheenrollmentoperation.
Thereisnoarbitraryenrollmentlabelconfiguredbydefault.Anyexistingarbitraryenrollmentlabelis
replacedbythiscommand.Theuseofarbitraryenrollmentlabelsisoptional.
Whentheenrollmentlabelisnotconfigured,thegenericarbitrarylabel(createdwiththearbitrary-
labelcommand)isused(ifconfigured)forenrollment.
RFC7030allowstheuseofarbitrarylabelssothatoneESTservermayservemultipleCAswiththesame
serverURLthatgetsconcatenatedwithdifferentarbitrarylabels.Thesamelabelisusedforevery
requestmadeunderaparticularESTprofile.
SomeESTschemesusearbitrarylabelsinamoresophisticatedway,definingdifferentlabelsfor
differenttypesofrequestsunderthesameESTprofile.Forexample,theCAcertificaterequestcould
usethegenericlabel(configuredwiththearbitrary-labelcommand),thecertificateenrollment
requestcouldusetheenrollmentlabel(configuredwiththisarbitrary-label-enrollmentcommand),
andthere-enrollmentrequestcouldusethere-enrollmentlabel(configuredwiththearbitrary-label-
reenrollmentcommand).Notethatonlyonelabelofeachofthethreeavailabletypescanbe
configuredinanyESTprofile.
Thenoformofthiscommandremovesthearbitraryenrollmentlabel.
| Parameter |     | Description                                       |     |
| --------- | --- | ------------------------------------------------- | --- |
| <LABEL>   |     | Specifiesthearbitraryenrollmentlabel.Range:Upto64 |     |
characters.
Examples
Configuringthearbitraryenrollmentlabel:
| switch(config)# | crypto | pki est-profile | EST-service1 |
| --------------- | ------ | --------------- | ------------ |
switch(config-est-EST-service1)# arbitrary-label-enrollment ipsec-v7
Removingthearbitraryenrollmentlabel:
| switch(config)#                  | crypto | pki est-profile | EST-service1               |
| -------------------------------- | ------ | --------------- | -------------------------- |
| switch(config-est-EST-service1)# |        | no              | arbitrary-label-enrollment |
| Command History                  |        |                 |                            |
PKI|204

| Release             |         | Modification |           |
| ------------------- | ------- | ------------ | --------- |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
Allplatforms config-est-<EST-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
arbitrary-label-reenrollment
| arbitrary-label-reenrollment |     | <LABEL> |     |
| ---------------------------- | --- | ------- | --- |
no arbitrary-label-reenrollment
Description
WithintheESTprofilecontext,configuresthearbitraryre-enrollmentlabeltobeconcatenatedtothe
ESTserverURLthatisconfiguredwiththeurlcommand.Thislabelisspecifictothere-enrollment
operation.Thereisnoarbitraryre-enrollmentlabelconfiguredbydefault.Anyexistingarbitraryre-
enrollmentlabelisreplacedbythiscommand.Theuseofarbitraryre-enrollmentlabelsisoptional.
Whenthere-enrollmentlabelisnotconfigured,thegenericarbitrarylabel(createdwiththearbitrary-
labelcommand)isused(ifconfigured)forre-enrollment.
RFC7030allowstheuseofarbitrarylabelssothatoneESTservermayservemultipleCAswiththesame
serverURLthatgetsconcatenatedwithdifferentarbitrarylabels.Thesamelabelisusedforevery
requestmadeunderaparticularESTprofile.
SomeESTschemesusearbitrarylabelsinamoresophisticatedway,definingdifferentlabelsfor
differenttypesofrequestsunderthesameESTprofile.Forexample,theCAcertificaterequestcoulduse
thegenericlabel(configuredwiththearbitrary-labelcommand),thecertificateenrollmentrequest
couldusetheenrollmentlabel(configuredwiththearbitrary-label-enrollmentcommand),andthe
re-enrollmentrequestcouldusethere-enrollmentlabel(configuredwiththisarbitrary-label-
reenrollmentcommand).Notethatonlyonelabelofeachofthethreeavailabletypescanbe
configuredinanyESTprofile.
Thenoformofthiscommandremovesthearbitraryre-enrollmentlabel.
| Parameter |     | Description                                          |     |
| --------- | --- | ---------------------------------------------------- | --- |
| <LABEL>   |     | Specifiesthearbitraryre-enrollmentlabel.Range:Upto64 |     |
characters.
Examples
Configuringthearbitraryre-enrollmentlabel:
| switch(config)# | crypto | pki est-profile | EST-service1 |
| --------------- | ------ | --------------- | ------------ |
switch(config-est-EST-service1)# arbitrary-label-reenrollment ipsec-v7
Removingthearbitraryre-enrollmentlabel:
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 205

| switch(config)# |     |     | crypto pki | est-profile | EST-service1 |
| --------------- | --- | --- | ---------- | ----------- | ------------ |
switch(config-est-EST-service1)#
|                |             |         |         | no           | arbitrary-label-reenrollment |
| -------------- | ----------- | ------- | ------- | ------------ | ---------------------------- |
| Command        | History     |         |         |              |                              |
| Release        |             |         |         | Modification |                              |
| 10.07orearlier |             |         |         | --           |                              |
| Command        | Information |         |         |              |                              |
| Platforms      |             | Command | context |              | Authority                    |
Allplatforms config-est-<EST-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| crypto    | pki             | est-profile |            |     |     |
| --------- | --------------- | ----------- | ---------- | --- | --- |
| crypto    | pki est-profile |             | <EST-NAME> |     |     |
| no crypto | pki             | est-profile | <EST-NAME> |     |     |
Description
CreatesacertificateEnrollmentoverSecureTransport(EST)profileandchangestotheconfig-est-
<EST-NAME>contextfortheprofile.EachESTprofilestoresinformationabouttheESTservice,including
ESTserverURLUpto16profilescanbecreated.
IfthespecifiedESTprofileexists,thiscommandchangestotheconfig-est-<EST-NAME>contextforthe
profile.
ThenoformofthiscommanddeletesthespecifiedESTprofile.ItalsodeletestheTAprofileswhoseCA
certificatesweredownloadedfromthecorrespondingESTserver,andtheleafcertificatesthatwere
enrolledusingthisESTprofile.
ThedeletionoftherelatedTAprofilesandenrolledcertificatesispermanent.IftheESTprofileisinthestartup
configurationandtheESTprofileisdeletedbutthisdeletionisnotupdatedinthestartupconfigurationbeforea
switchreboot,theESTprofilewillstillexistaftertherebootbuttherelatedTAprofilesandenrolledcertificates
willnotexist.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<EST-NAME> SpecifiestheESTprofilename.Range:Upto32alphanumeric
characters(excluding").
Examples
CreatingESTprofileEST-Service1:
| switch(config)# |     |     | crypto pki | est-profile | EST-Service1 |
| --------------- | --- | --- | ---------- | ----------- | ------------ |
switch(config-est-service1)#
RemovingESTprofileservice1:
PKI|206

| switch(config)#     |         | no crypto | pki est-profile |              | EST-Service1 |     |
| ------------------- | ------- | --------- | --------------- | ------------ | ------------ | --- |
| Command History     |         |           |                 |              |              |     |
| Release             |         |           |                 | Modification |              |     |
| 10.07orearlier      |         |           |                 | --           |              |     |
| Command Information |         |           |                 |              |              |     |
| Platforms           | Command | context   |                 | Authority    |              |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
enroll est-profile
| enroll est-profile |     | <EST-NAME> |     |     |     |     |
| ------------------ | --- | ---------- | --- | --- | --- | --- |
Description
EnrollsaleafcertificatethrougharemoteEST(EnrollmentoverSecureTransport)server.
PerRFC7030,ESTenablesclientstorequestcertificatesigningservicesoversecureTLSconnections.
TheswitchgeneratesakeypairandthecorrespondingCSR.TheCSRissenttotheESTservertorequest
signing,andthesignedcertificateisbereturnedtotheswitchwhereitisvalidated.Ifthewholeprocess
succeeds,thecertificatecanbeusedasaleafcertificateontheswitch.Whentheleafcertificate
approachesitsexpirydate,itwillberenewedautomaticallythroughthesameESTserver.
Eachenrollmentorre-enrollmentattemptstartswitha/cacertsrequestsenttotheESTservertoget
thelatestchainofCAcertificates.Aftertheenrollmentorre-enrollmentsucceeds,thischainofCA
certificateswillbecomparedwiththosedownloadedpreviouslyfromthesameESTserver.Updateswill
bemadeasappropriate.
Thesubjectfieldsofthecurrentleafcertificatemustbedefinedbeforerunningthiscommand.Ifthe
commonnamesubjectfieldisnotconfigured,thiscommandisrejected.
Thiscommandcannotbeusedtoenrollorrenewthedefaultcertificate"local-cert."
| Parameter  |     |     |     | Description                                    |     |     |
| ---------- | --- | --- | --- | ---------------------------------------------- | --- | --- |
| <EST-NAME> |     |     |     | SpecifiesanexistingESTprofilename.Range:Upto32 |     |     |
alphanumericcharacters(excluding").
Example
Enrollingleafcertificateleaf-cert1throughtheESTserveridentifiedinESTprofileEST-service1:
switch(config-cert-leaf-cert1)# enroll est-profile EST-service1
| You are enrolling |     | a certificate |     | with the | following | attributes: |
| ----------------- | --- | ------------- | --- | -------- | --------- | ----------- |
Subject: C=US, ST=CA, L=Roseville, OU=Aruba-Roseville, O=Aruba,
CN=leaf-cert1
| Key Type: | RSA    | (2048 bits) |     |     |     |     |
| --------- | ------ | ----------- | --- | --- | --- | --- |
| Continue  | (y/n)? | y           |     |     |     |     |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 207

| Certificate | enrollment | via EST-service1 |     | has been initiated. |     |
| ----------- | ---------- | ---------------- | --- | ------------------- | --- |
Please use `show crypto pki certificate leaf-cert1` to check its status.
switch(config-cert-leaf-cert1)#
| Command History     |         |         |              |           |     |
| ------------------- | ------- | ------- | ------------ | --------- | --- |
| Release             |         |         | Modification |           |     |
| 10.07orearlier      |         |         | --           |           |     |
| Command Information |         |         |              |           |     |
| Platforms           | Command | context |              | Authority |     |
Allplatforms config-cert-<CERT-NAME> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
reenrollment-lead-time
| reenrollment-lead-time |     | <LEAD-TIME> |     |     |     |
| ---------------------- | --- | ----------- | --- | --- | --- |
no reenrollment-lead-time
Description
WithintheESTprofilecontext,setsthecertificatere-enrollmentleadtimewhichisthenumberofdays
beforecertificateexpirydatethatcertificatere-enrollmentwillbeinitiated.
ThenoformofthiscommandresetstheESTserverre-enrollmentleadtimetoitsdefaultof2days.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<LEAD-TIME> Specifiesthecertificatere-enrollmentleadtimeindays.Range:0
to30days.Default:2days.
Examples
Settingthecertificatere-enrollmentleadtimeto15days:
| switch(config)#                  | crypto | pki est-profile |                        | EST-service1 |     |
| -------------------------------- | ------ | --------------- | ---------------------- | ------------ | --- |
| switch(config-est-EST-service1)# |        |                 | reenrollment-lead-time |              | 15  |
Resettingthecertificatere-enrollmentleadtimetoitsdefaultof2days:
| switch(config)#                  | crypto | pki est-profile |              | EST-service1           |     |
| -------------------------------- | ------ | --------------- | ------------ | ---------------------- | --- |
| switch(config-est-EST-service1)# |        |                 | no           | reenrollment-lead-time |     |
| Command History                  |        |                 |              |                        |     |
| Release                          |        |                 | Modification |                        |     |
| 10.07orearlier                   |        |                 | --           |                        |     |
PKI|208

| Command Information |         |         |     |           |
| ------------------- | ------- | ------- | --- | --------- |
| Platforms           | Command | context |     | Authority |
config-est-<EST-NAME>
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
retry-count
| retry-count | <RETRIES> |     |     |     |
| ----------- | --------- | --- | --- | --- |
no retry-count
Description
WithintheESTprofilecontext,setsthemaximumnumberofretirestobeattemptedaftertheinitial
certificateenrollmentrequestfails.
Thenoformofthiscommandresetsthemaximumnumberofcertificateenrollmentrequestretriesto
itsdefaultof3.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<RETRIES> Specifiesthemaximumnumberofcertificateenrollmentrequest
retries.Range:0to32retries.Default:3retries.
Examples
Settingtheretrycountto5retries:
| switch(config)#                  | crypto | pki est-profile |             | EST-service1 |
| -------------------------------- | ------ | --------------- | ----------- | ------------ |
| switch(config-est-EST-service1)# |        |                 | retry-count | 5            |
Resettingtheretrycounttoitsdefaultof3retries:
| switch(config)#                  | crypto  | pki est-profile |              | EST-service1 |
| -------------------------------- | ------- | --------------- | ------------ | ------------ |
| switch(config-est-EST-service1)# |         |                 | no           | retry-count  |
| Command History                  |         |                 |              |              |
| Release                          |         |                 | Modification |              |
| 10.07orearlier                   |         |                 | --           |              |
| Command Information              |         |                 |              |              |
| Platforms                        | Command | context         |              | Authority    |
Allplatforms config-est-<EST-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
retry-interval
| retry-interval | <INTERVAL> |     |     |     |
| -------------- | ---------- | --- | --- | --- |
no retry-interval
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 209

Description
WithintheESTprofilecontext,setstheintervalatwhichafailedcertificateenrollmentrequestisretried.
Thenoformofthiscommandresetstheenrollmentrequestretryintervaltoitsdefaultof30seconds.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<INTERVAL> Specifiestheenrollmentrequestretryintervalinseconds.Range:
30to600seconds.Default:30seconds.
Examples
Settingthecertificateenrollmentrequestretryintervalto45seconds:
| switch(config)#                  |     | crypto | pki est-profile |                | EST-service1 |     |
| -------------------------------- | --- | ------ | --------------- | -------------- | ------------ | --- |
| switch(config-est-EST-service1)# |     |        |                 | retry-interval |              | 45  |
Resettingtheretryintervaltoitsdefaultof30seconds:
| switch(config)#                  |             | crypto | pki est-profile |              | EST-service1   |     |
| -------------------------------- | ----------- | ------ | --------------- | ------------ | -------------- | --- |
| switch(config-est-EST-service1)# |             |        |                 | no           | retry-interval |     |
| Command                          | History     |        |                 |              |                |     |
| Release                          |             |        |                 | Modification |                |     |
| 10.07orearlier                   |             |        |                 | --           |                |     |
| Command                          | Information |        |                 |              |                |     |
| Platforms                        | Command     |        | context         |              | Authority      |     |
Allplatforms config-est-<EST-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show crypto |     | pki est-profile |              |     |     |     |
| ----------- | --- | --------------- | ------------ | --- | --- | --- |
| show crypto | pki | est-profile     | [<EST-NAME>] |     |     |     |
Description
ShowsalistofallconfiguredESTprofiles,ordetailedinformationforaspecificprofile.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<EST-NAME> SpecifiestheESTprofilename.Range:Upto32alphanumeric
characters(excluding").
Examples
ShowingalistofallconfiguredESTprofiles:
PKI|210

| switch#                          | show | crypto |     | pki | est-profile |             |              |
| -------------------------------- | ---- | ------ | --- | --- | ----------- | ----------- | ------------ |
|                                  |      |        |     |     |             | Downloaded  | Enrolled     |
| Profile                          | Name |        |     |     |             | TA Profiles | Certificates |
| -------------------------------- |      |        |     |     |             | ----------- | ------------ |
| EST-service1                     |      |        |     |     |             | 2           | 3            |
| EST-service2                     |      |        |     |     |             | 1           | 2            |
| EST-service3                     |      |        |     |     |             | 2           | 0            |
ShowingdetailedinformationforESTprofileEST-service1:
| switch# | show           | crypto |          | pki          | est-profile                  | EST-service1     |     |
| ------- | -------------- | ------ | -------- | ------------ | ---------------------------- | ---------------- | --- |
|         | Profile        | Name   |          |              | : EST-service1               |                  |     |
|         | Service        | VRF    |          |              | : mgmt                       |                  |     |
|         | Service        | URL    |          |              | : https://est-service999.com |                  |     |
|         | Arbitrary      |        | Label    |              |                              | : not configured |     |
|         | Arbitrary      |        | Label    | Enrollment   |                              | : /ipsec-VP7     |     |
|         | Arbitrary      |        | Label    | Reenrollment |                              | : not configured |     |
|         | Authentication |        | Username |              | : est1                       |                  |     |
|         | Authentication |        | Password |              | :                            |                  |     |
AQBapREALpWYm2z7L1LanOtR3vGkqhBN1hBUU2CuvQXUF/ggYgAAnAnGTnKq49P4c
dNQ6UqPbjHL4XzCO0T04djkhSUxPKGfnsWuFEONveh+JbEobqKImfwJjc3eWHiaUb
eNpPx2zN2Q1DdyxAAQi4rmKr8LITMTTMd7qr
|     | Retry Interval |              |          |      | : 45 | seconds |     |
| --- | -------------- | ------------ | -------- | ---- | ---- | ------- | --- |
|     | Retry Count    |              |          |      | : 5  | times   |     |
|     | Reenrollment   |              | Lead     | Time | : 2  | days    |     |
|     | Downloaded     | TA           | Profiles |      | : 2  |         |     |
|     | Enrolled       | Certificates |          |      | :    |         |     |
leaf-cert1
leaf-cert2
leaf-cert3
| Command        | History     |         |     |         |     |              |     |
| -------------- | ----------- | ------- | --- | ------- | --- | ------------ | --- |
| Release        |             |         |     |         |     | Modification |     |
| 10.07orearlier |             |         |     |         |     | --           |     |
| Command        | Information |         |     |         |     |              |     |
| Platforms      |             | Command |     | context |     | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
url
url <URL>
no url
Description
WithintheESTprofilecontext,configurestheURLofthecertificateenrollmentESTserver.Thisisnot
configuredbydefault.AnyexistingURLisreplacedbythiscommand.
ThenoformofthiscommandremovestheESTserverURLwithintheselectedESTprofile.Theremoval
oftheURLdoesnotaffecttheTAprofilesandenrolledcertificatesfromtheESTserver.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 211

| Parameter |     | Description                                       |     |
| --------- | --- | ------------------------------------------------- | --- |
| <URL>     |     | SpecifiestheESTserverURL.Range:Upto192characters. |     |
Usage
n TheconfigurationandupdateoftheESTprofileURLtriggersthesendingofa/cacertsrequestto
theESTserver.AsuccessfulrequestwillresultinachainoftrustedCAcertificatesbeingdownloaded
fromtheESTserver.EachCAcertificate,eitherrootCAcertificatesorintermediateCAcertificates,will
besavedasaTAprofile,withTAprofilename<est-name>-est-taNNwithNNrepresentingtwo
numericaldigits.ThisTAprofilenamingschemewiththe-est-taNNsuffixisreservedforTAprofiles
downloadedfromESTservers.
n UponconnectionwithanESTserver,theswitchauthenticatestheserverbyvalidatingtheserver
certificate.Forthisvalidationtosucceed,aTAprofileneedstopre-existintheswitchwithaCA
certificatefromtheissuerchainoftheservercertificate.Oncetheserverisauthenticated,allCA
certificatesinits/cacertsresponsewillbetrusted,withnofurthervalidationoccurringforthem.
TheTAprofileswithCAcertificatesdownloadedfromanESTserverwillhavetheirrevocationcheck
n
settoOCSP,enforcementsettooptional,andtheOCSPVRFsettothesameasthatoftheEST
profile.
Examples
ConfiguringtheESTserverURL:
| switch(config)# | crypto | pki est-profile | EST-service1 |
| --------------- | ------ | --------------- | ------------ |
switch(config-est-EST-service1)# url https://est-service999.com/.well-known/est
RemovingtheESTserverURL:
| switch(config)#                  | crypto  | pki est-profile | EST-service1 |
| -------------------------------- | ------- | --------------- | ------------ |
| switch(config-est-EST-service1)# |         | no              | url          |
| Command History                  |         |                 |              |
| Release                          |         | Modification    |              |
| 10.07orearlier                   |         | --              |              |
| Command Information              |         |                 |              |
| Platforms                        | Command | context         | Authority    |
Allplatforms config-est-<EST-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
username
username <USERNAME> password [ciphertext <CIPHERTEXT-PASSWORD> |
| plaintext | <PLAINTEXT-PASSWORD>] |     |     |
| --------- | --------------------- | --- | --- |
no username
Description
PKI|212

Within the EST profile context, configures the user account information for the EST server that is used to
authenticate the switch before accepting requests from the switch. This is not configured by default. Any
existing username and password is replaced by this command.

When entered without either optional ciphertext or plaintext parameters, the plaintext password is
prompted for twice, with the characters entered masked with "*" symbols.

The no form of this command removes the user account information within the selected EST profile.

There are two ways the EST client on a CX switch can prove itself to an EST server: a certificate, and/or
username and password. At least one of the two must be configured for the EST request to succeed. If
both are configured, certificate authentication will be used. If a certificate is not configured or certificate
authentication fails, and username and password is configured, the username and password will be
sent to the EST server for authentication.

Parameter

<USERNAME>

ciphertext <CIPHERTEXT-PASSWORD>

plaintext <PLAINTEXT-PASSWORD>

Description

Specifies the EST server account user name. The exact user
name requirements are set by the chosen EST service. Range:
Up to 32 alphanumeric characters.

Specifies the EST server account password as Base64
ciphertext. No password prompts are provided and the
ciphertext password is validated before the configuration is
applied for the user.

NOTE: The ciphertext password must be gotten from the EST
service.

Specifies the password without prompting. The password is
visible as cleartext when entered but is encrypted thereafter.
The exact password requirements are set by the chosen EST
service. Range: Up to 64 alphanumeric characters.

Examples

Configuring an EST user with prompted cleartext password entry :

switch(config)# crypto pki est-profile EST-service1
switch(config-est-EST-service1)# username est1 password
Enter password: ********
Confirm password: ********
switch(config-est-EST-service1)#

Configuring an EST user with direct cleartext password entry:

switch(config)# crypto pki est-profile EST-service2
switch(config-est-EST-service2)# username est1 password plaintext concept_leap739

Configuring an EST user with ciphertext password entry :

switch(config)# crypto pki est-profile EST-service3
switch(config-est-EST-service3)# username est1 password ciphertext
AQBpRALpWYm2z7L1LanOtR3vGkqhN1hBU2CuvQXUF/ggYgAAAHWaPqxU6nAnGTnKq49P4cdNQ6U

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

213

qPbjHL4XzO0T04djkUPKGfnsWuFEONveh+JbEobq63+1k80qBKImfwJjc3eWHiaUbeNpPx2zN2Q
1DdyxAAQi4rmKr8LITMTTMd7qr
RemovingtheESTuseraccountinformationforESTprofileEST-service2:
| switch(config)#                  | crypto  | pki est-profile | EST-service2 |
| -------------------------------- | ------- | --------------- | ------------ |
| switch(config-est-EST-service2)# |         | no              | username     |
| Command History                  |         |                 |              |
| Release                          |         | Modification    |              |
| 10.07orearlier                   |         | --              |              |
| Command Information              |         |                 |              |
| Platforms                        | Command | context         | Authority    |
Allplatforms config-est-<EST-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
vrf
vrf <VRF-NAME>
no vrf
Description
WithintheESTprofilecontext,selectstheVRFthroughwhichtheESTservercanbereached.Any
existingVRFselectionisreplacedbythiscommand.Whenthiscommandisnotused,VRFmgmtisused
bydefaultonswitchfamiliessupportingthemgmtVRF,otherwisethedefaultVRFnameddefaultis
used.
ThenoformofthiscommandselectsthedefaultVRFeithermgmtordefault.
| Parameter  |     | Description                               |     |
| ---------- | --- | ----------------------------------------- | --- |
| <VRF-NAME> |     | SpecifiesthenameoftheVRFtouseforESTserver |     |
communication
Examples
SelectingVRFit-servicesforESTservercommunications:
| switch(config)#                  | crypto | pki est-profile | EST-service1 |
| -------------------------------- | ------ | --------------- | ------------ |
| switch(config-est-EST-service1)# |        | vrf             | it-services  |
ResettingtheVRFtoitsdefaultofmgmtforESTservercommunications:
| switch(config)#                  | crypto | pki est-profile | EST-service1 |
| -------------------------------- | ------ | --------------- | ------------ |
| switch(config-est-EST-service1)# |        | no              | vrf          |
PKI|214

| Command History     |         |              |           |
| ------------------- | ------- | ------------ | --------- |
| Release             |         | Modification |           |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
Allplatforms config-est-<EST-NAME> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 215

Chapter 12
Fault Monitor
Fault Monitor
AppliestotheAruba8400SwitchSeriesonly,whichmustberunninganyofCPEormajorversionsreleasedafter
AOS-CX10.06.0150.
AOS-CXswitchesincludeautomaticdetectionandcontrolforcertainlinkerrorsandexcessivetraffic
conditions.FaultmonitorcanbeusedtologaneventorsendSNMPtrapsfortheseconditionsand
temporarilydisabletheporttoprotectthenetwork.Monitoringcanbeenabledforallrecognizedfaults
orforindividualfaults,andactionsandthresholdsforeachfaultcanbeconfigured.
FaultmonitorappliesonlytophysicalportsandnottoLAGs,tunnels,VSFlinks,orothertypesof
interfaces.FaultmonitoringcanbeappliedtotheindividualmembersofaLAG.
| Fault monitoring |     | conditions |
| ---------------- | --- | ---------- |
Thefollowingfaultconditionsaremonitored:
| Excessive | CRC errors |     |
| --------- | ---------- | --- |
AnexcessiveCRCerrorfaultisreportedwhenthenumberofingresscrc-errorframesper10,000
receivedframesexceedstheconfiguredthresholdvalueinatwentysecondinterval.
| Excessive | oversize | packets |
| --------- | -------- | ------- |
Anexcessiveoversizedpacketfaultisreportedwhenthenumberofingressoversizedframesper10,000
receivedframesexceedstheconfiguredthresholdvalueinatwentysecondinterval.Inoversizepacket
fault,thepacketssizeismorethantheconfiguredMTUontheinterfacewithgoodcyclicredundancy
check(CRC).
| Excessive | fragments |     |
| --------- | --------- | --- |
Anexcessivefragmentfaultisreportedwhenthenumberofingressfragmentframesper10,000
receivedframesexceedstheconfiguredthresholdvalueinatwentysecondinterval.Infragmentsfault,
thepacketsizeislesserthantheconfiguredMTUontheinterfacewithbadCRC.
| Excessive | TX drops |     |
| --------- | -------- | --- |
ExcessiveTXdropsfaultisanexampleofoverbandwidth.Itisreportedwhenegressdroppedpackets
per10,000transmittedframesexceedstheconfiguredthresholdvalueinatwentysecondinterval.
| Excessive | collisions |     |
| --------- | ---------- | --- |
Anexcessivecollisionfaultisanexampleofoverbandwidth,itgetsreportedwhenegresscollision
framesper10,000transmittedframesexceedstheconfiguredthresholdvalueina20secondinterval.
| Excessive | Late Collisions |     |
| --------- | --------------- | --- |
216
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries)

Anexcessivelatecollisionfaultisreportedwheningresslate-collisionframesper10,000received
framesexceedstheconfiguredthresholdvalueina300secondinterval.
| Excessive | alignment | errors |
| --------- | --------- | ------ |
Afullduplexmismatchfaultisreportedwheningressalignment-errorframesper10,000received
framesexceedstheconfiguredthresholdvalueina20secondinterval.
| Excessive | link flaps |     |
| --------- | ---------- | --- |
Alinkflapfaultisreportedwhenthecountoftransitionsbetweenlink-upandlink-downstateexceeds
theconfiguredthresholdinatensecondinterval.
| Excessive | broadcasts |     |
| --------- | ---------- | --- |
Abroadcaststormfaultisreportedwhentheaverageingresstrafficrateofbroadcastpacketsexceeds
theconfiguredthresholdinatwentysecondinterval.
Thedefaultthresholdlevelisconfiguredasapercentageofthebandwidthoftheport.Largertheframe
size,smallertheconvertedthresholdvalueinPPS.Hencelargerframesrequirelowerthresholdpercent
configurationstohitthefault.
| Excessive | multicasts |     |
| --------- | ---------- | --- |
Amulticaststormfaultisreportedwhentheaverageingresstrafficrateofmulticastpacketsexceeds
theconfiguredthresholdinatwentysecondinterval.
| Fault monitor              | commands |     |
| -------------------------- | -------- | --- |
| (Fault enabling/disabling) |          |     |
{all | <FAULT>}
| no {all | | <FAULT>} |     |
| --------- | -------- | --- |
Description
Withintheselectedfaultmonitorprofilecontext,enablesallfaultsorspecificfaultsformonitoring.
Faultsenabledwiththiscommandusedefaultactionsandthresholdsunlesstheactionsandthresholdsare
configuredwithrespectivecommandsactionandthreshold.
Bydefault,allfaultsaredisabledinaprofileandremaindisableduntilenabledasdescribedhere.Configuring
theactionandthresholddoesnotenablethefault.
Thenoformofthiscommanddisablesfaultsformonitoring.
Parameter Description
all Selectsallfaults.
<FAULT> Selectsaspecificfault.Availablefaultnames:
excessive-crc-errors
excessive-oversize-packets
FaultMonitor|217

Parameter Description
excessive-fragments
excessive-tx-drops
excessive-collisions
excessive-late-collisions
excessive-alignment-errors
excessive-link-flaps
excessive-broadcasts
excessive-multicasts
Examples
Enablingfaults:
| switch(config-fault-monitor-profile)# |     | all |     |
| ------------------------------------- | --- | --- | --- |
switch(config-fault-monitor-profile)# excessive-oversize-packets
| switch(config-fault-monitor-profile)# |     | excessive-fragments  |     |
| ------------------------------------- | --- | -------------------- | --- |
| switch(config-fault-monitor-profile)# |     | excessive-crc-errors |     |
| switch(config-fault-monitor-profile)# |     | excessive-tx-drops   |     |
| switch(config-fault-monitor-profile)# |     | excessive-link-flaps |     |
| switch(config-fault-monitor-profile)# |     | excessive-broadcasts |     |
| switch(config-fault-monitor-profile)# |     | excessive-multicasts |     |
| switch(config-fault-monitor-profile)# |     | excessive-collisions |     |
switch(config-fault-monitor-profile)# excessive-late-collisions
switch(config-fault-monitor-profile)# excessive-alignment-errors
Disablingfaults:
| switch(config-fault-monitor-profile)# |     | no  | all |
| ------------------------------------- | --- | --- | --- |
switch(config-fault-monitor-profile)# no excessive-oversize-packets
| switch(config-fault-monitor-profile)# |     | no  | excessive-fragments  |
| ------------------------------------- | --- | --- | -------------------- |
| switch(config-fault-monitor-profile)# |     | no  | excessive-crc-errors |
| switch(config-fault-monitor-profile)# |     | no  | excessive-tx-drops   |
| switch(config-fault-monitor-profile)# |     | no  | excessive-link-flaps |
| switch(config-fault-monitor-profile)# |     | no  | excessive-broadcasts |
| switch(config-fault-monitor-profile)# |     | no  | excessive-multicasts |
| switch(config-fault-monitor-profile)# |     | no  | excessive-collisions |
switch(config-fault-monitor-profile)# no excessive-late-collisions
switch(config-fault-monitor-profile)# no excessive-alignment-errors
| Command History |     |     |     |
| --------------- | --- | --- | --- |
Release Modification
10.08.1010 Commandintroduced
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8400 config-fault-monitor-profile Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
action
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 218

{all | <FAULT>} action {notify | notify-and-disable [auto-enable <TIMEOUT>]}
no {all | <FAULT>} action {notify | notify-and-disable [auto-enable <TIMEOUT>]}

Description

Within the selected fault monitor profile context, configures the fault monitoring action for the specified
fault. Default action: notify with auto-enable disabled.

The no form of this command removes the action and disables auto-enable.

Parameter

all

<FAULT>

Description

Selects all faults.

Selects a specific fault. Available fault names:
excessive-crc-errors
excessive-oversize-packets
excessive-fragments
excessive-tx-drops
excessive-collisions
excessive-late-collisions
excessive-alignment-errors
excessive-link-flaps
excessive-broadcasts
excessive-multicasts

notify

notify-and-disable

auto-enable <TIMEOUT>

Selects the notify action. Notifies through events, DLOGs, and
SNMP trap. This action is enabled by default.

Selects the action as notify-and-disable. Notifies through
events, DLOGs, and SNMP trap, and then disables the port.

Sets the number of seconds after which a port disabled by the
notify-and-disable action is automatically re-enabled. Range:
1 to 604800 seconds.

The fault parameter values are saved even after a fault is disabled in the profile. The saved values will be used

if the fault is later re-enabled in the profile again.

Examples

Configuring the notify fault action:

switch(config-fault-monitor-profile)# all action notify
switch(config-fault-monitor-profile)# excessive-oversize-packets action notify
switch(config-fault-monitor-profile)# excessive-collisions action notify

Configuring the notify-and-disable fault action:

switch(config-fault-monitor-profile)# all action notify-and-disable
switch(config-fault-monitor-profile)# excessive-oversize-packets action notify-
and-disable
switch(config-fault-monitor-profile)# excessive-late-collisions action notify-and-
disable

Fault Monitor | 219

switch(config-fault-monitor-profile)# excessive-alignment-errors action notify-
and-disable
Configuringthenotify-and-disableactionwithauto-enable:
switch(config-fault-monitor-profile)# excessive-oversize-packets action notify-
| and-disable | auto-enable | 80  |     |
| ----------- | ----------- | --- | --- |
switch(config-fault-monitor-profile)# excessive-collisions action notify-and-
| disable auto-enable |     | 70  |     |
| ------------------- | --- | --- | --- |
Resettingthefaultactiontodefault:
switch(config-fault-monitor-profile)# no excessive-oversize-packets action
switch(config-fault-monitor-profile)#
no excessive-alignment-errors action
switch(config-fault-monitor-profile)# no excessive-oversize-packets action notify-
and-disable
Disablingauto-enable:
switch(config-fault-monitor-profile)# no all action notify-and-disable auto-enable
switch(config-fault-monitor-profile)# no excessive-collisions action notify-and-
| disable auto-enable |     | 70  |     |
| ------------------- | --- | --- | --- |
| Command History     |     |     |     |
Release Modification
10.08.1010 Commandintroduced
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8400 config-fault-monitor-profile Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| apply fault-monitor    |         | profile                  |     |
| ---------------------- | ------- | ------------------------ | --- |
| apply fault-monitor    | profile | <PROFILE-NAME>           |     |
| no apply fault-monitor |         | profile [<PROFILE-NAME>] |     |
Description
Appliesafaultmonitoringprofiletotheselectedinterfaceorinterfacerange.
Thenoformofthiscommandremovesthefaultmonitoringprofilefromtheselectedinterfaceor
interfacerange.
Parameter Description
<PROFILE-NAME> Specifiesthefaultmonitorprofilename.Range:Upto64
alphanumericandspecialcharacters.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 220

Examples
Applyingthefaultmonitoringprofiletoainterface:
switch(config)#
|                    |     | interface | 1/1/1         |                     |
| ------------------ | --- | --------- | ------------- | ------------------- |
| switch(config-if)# |     | apply     | fault-monitor | profile noisy-ports |
Applyingthefaultmonitoringprofiletoainterfacerange:
| switch(config)#     |         | interface | 1/1/2-1/1/24  |                     |
| ------------------- | ------- | --------- | ------------- | ------------------- |
| switch(config-if)#  |         | apply     | fault-monitor | profile quiet-ports |
| Command History     |         |           |               |                     |
| Release             |         |           |               | Modification        |
| 10.08.1010          |         |           |               | Commandintroduced.  |
| Command Information |         |           |               |                     |
| Platforms           | Command | context   |               | Authority           |
config-if
| 8400 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
| fault-monitor   | profile |                |     |     |
| --------------- | ------- | -------------- | --- | --- |
| fault-monitor   | profile | <PROFILE-NAME> |     |     |
| {all | <FAULT>} |         |                |     |     |
no ..
Description
Createsafaultmonitoringprofileandentersitscontext.Iftheprofilealreadyexists,thiscommand
enterstheprofilecontext.Amaximumof16faultmonitoringprofilesaresupported.
Thenoformofthiscommanddeletesthefaultmonitoringprofile.
Faultsenabledwiththiscommandusedefaultactionsandthresholdsunlesstheactionsandthresholdsare
configuredwithrespectivecommandsactionandthreshold.
Bydefault,allfaultsaredisabledinaprofileandremaindisableduntilenabledasdescribedhere.Configuring
theactionandthresholddoesnotenablethefault.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<PROFILE-NAME> Specifiesthefaultmonitorprofilename.Range:Upto64
alphanumericandspecialcharacters.
all
Withintheselectedfaultmonitorprofilecontext,enablesall
faults.
FaultMonitor|221

Parameter

<FAULT>

Description

Within the selected fault monitor profile context, enables a
specific fault. Available fault names:
excessive-crc-errors
excessive-oversize-packets
excessive-fragments
excessive-tx-drops
excessive-collisions
excessive-late-collisions
excessive-alignment-errors
excessive-link-flaps
excessive-broadcasts
excessive-multicasts

Examples

Creating a fault monitor profile:

switch(config)# fault-monitor profile noisy-ports
switch(config-fault-monitor-profile)#

Deleting a fault monitor profile:

switch(config)# no fault-monitor profile noisy-ports
switch(config)#

Enabling all faults in the fault monitor profile noisy-ports:

switch(config)# fault-monitor profile noisy-ports
switch(config-fault-monitor-profile)# all

Enabling individual faults in the fault monitor profile noisy-ports:

switch(config)# fault-monitor profile noisy-ports
switch(config-fault-monitor-profile)# excessive-oversize-packets
switch(config-fault-monitor-profile)# excessive-fragments
switch(config-fault-monitor-profile)# excessive-crc-errors
switch(config-fault-monitor-profile)# excessive-tx-drops
switch(config-fault-monitor-profile)# excessive-link-flaps
switch(config-fault-monitor-profile)# excessive-broadcasts
switch(config-fault-monitor-profile)# excessive-multicasts
switch(config-fault-monitor-profile)# excessive-collisions
switch(config-fault-monitor-profile)# excessive-late-collisions
switch(config-fault-monitor-profile)# excessive-alignment-errors

Disabling faults:

switch(config-fault-monitor-profile)# no excessive-oversize-packets
switch(config-fault-monitor-profile)# no excessive-fragments
switch(config-fault-monitor-profile)# no excessive-crc-errors
switch(config-fault-monitor-profile)# no excessive-tx-drops

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

222

| switch(config-fault-monitor-profile)# |     |     | no excessive-link-flaps |     |     |
| ------------------------------------- | --- | --- | ----------------------- | --- | --- |
switch(config-fault-monitor-profile)#
no excessive-broadcasts
| switch(config-fault-monitor-profile)# |     |     | no excessive-multicasts |     |     |
| ------------------------------------- | --- | --- | ----------------------- | --- | --- |
| switch(config-fault-monitor-profile)# |     |     | no excessive-collisions |     |     |
switch(config-fault-monitor-profile)# no excessive-late-collisions
switch(config-fault-monitor-profile)# no excessive-alignment-errors
| Command History     |         |         |                   |     |     |
| ------------------- | ------- | ------- | ----------------- | --- | --- |
| Release             |         |         | Modification      |     |     |
| 10.08.1010          |         |         | Commandintroduced |     |     |
| Command Information |         |         |                   |     |     |
| Platforms           | Command | context | Authority         |     |     |
8400 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show fault-monitor |         | profile        |     |     |     |
| ------------------ | ------- | -------------- | --- | --- | --- |
| show fault-monitor | profile | <PROFILE-NAME> |     |     |     |
Description
Showsfaultmonitoringprofileinformationforallprofilesoraspecificprofile.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<PROFILE-NAME> Specifiesthefaultmonitorprofilename.Range:Upto64
alphanumericandspecialcharacters.
Example
Showinginformationforallfaultmonitoringprofiles:
| switch# show | fault-monitor | profile |     |     |     |
| ------------ | ------------- | ------- | --- | --- | --- |
-------------------------------------------------------------------------------
| Fault monitor | profile: | noisy-ports |     |     |     |
| ------------- | -------- | ----------- | --- | --- | --- |
-------------------------------------------------------------------------------
Auto
| Fault |     | Enabled | Threshold | Action | Enable |
| ----- | --- | ------- | --------- | ------ | ------ |
-------------------------------------------------------------------------------
| excessive-broadcasts       |     | yes | 5%       | notify-and-disable | --  |
| -------------------------- | --- | --- | -------- | ------------------ | --- |
| excessive-multicasts       |     | yes | 1000 pps | notify-and-disable | --  |
| excessive-link-flaps       |     | yes | 7        | notify-and-disable | --  |
| excessive-oversize-packets |     | yes | 25       | notify-and-disable | --  |
| excessive-fragments        |     | yes | 25       | notify-and-disable | --  |
| excessive-crc-errors       |     | yes | 25       | notify-and-disable | --  |
| excessive-late-collisions  |     | yes | 25       | notify-and-disable | --  |
| excessive-collisions       |     | yes | 25       | notify-and-disable | --  |
| excessive-tx-drops         |     | yes | 25       | notify-and-disable | --  |
| excessive-alignment-errors |     | yes | 25       | notify-and-disable | --  |
-------------------------------------------------------------------------------
| Fault monitor | profile: | quiet-ports |     |     |     |
| ------------- | -------- | ----------- | --- | --- | --- |
FaultMonitor|223

-------------------------------------------------------------------------------
Auto
| Fault |     |     | Enabled | Threshold |     | Action | Enable |
| ----- | --- | --- | ------- | --------- | --- | ------ | ------ |
-------------------------------------------------------------------------------
| excessive-broadcasts       |     |     | yes | 20%   |     | notify-and-disable | --  |
| -------------------------- | --- | --- | --- | ----- | --- | ------------------ | --- |
| excessive-multicasts       |     |     | yes | 25000 | pps | notify-and-disable | 40  |
| excessive-link-flaps       |     |     | yes | 7     |     | notify             | --  |
| excessive-oversize-packets |     |     | yes | 30    |     | notify-and-disable | --  |
| excessive-fragments        |     |     | yes | 30    |     | notify-and-disable | --  |
| excessive-crc-errors       |     |     | yes | 30    |     | notify-and-disable | --  |
| excessive-late-collisions  |     |     | yes | 30    |     | notify-and-disable | --  |
| excessive-collisions       |     |     | yes | 30    |     | notify-and-disable | --  |
| excessive-tx-drops         |     |     | yes | 30    |     | notify-and-disable | --  |
| excessive-alignment-errors |     |     | yes | 30    |     | notify-and-disable | --  |
Showinginformationforaparticularfaultmonitoringprofile:
| switch# | show fault-monitor |     | profile | noisy-ports |     |     |     |
| ------- | ------------------ | --- | ------- | ----------- | --- | --- | --- |
-------------------------------------------------------------------------------
| Fault monitor | profile: | noisy-ports |     |     |     |     |     |
| ------------- | -------- | ----------- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------------
Auto
| Fault |     |     | Enabled | Threshold |     | Action | Enable |
| ----- | --- | --- | ------- | --------- | --- | ------ | ------ |
-------------------------------------------------------------------------------
| excessive-broadcasts       |         |         | yes | 5%                |     | notify-and-disable | --  |
| -------------------------- | ------- | ------- | --- | ----------------- | --- | ------------------ | --- |
| excessive-multicasts       |         |         | yes | 1000              | pps | notify-and-disable | --  |
| excessive-link-flaps       |         |         | yes | 7                 |     | notify-and-disable | --  |
| excessive-oversize-packets |         |         | yes | 25                |     | notify-and-disable | --  |
| excessive-fragments        |         |         | yes | 25                |     | notify-and-disable | --  |
| excessive-crc-errors       |         |         | yes | 25                |     | notify-and-disable | --  |
| excessive-late-collisions  |         |         | yes | 25                |     | notify-and-disable | --  |
| excessive-collisions       |         |         | yes | 25                |     | notify-and-disable | --  |
| excessive-tx-drops         |         |         | yes | 25                |     | notify-and-disable | --  |
| excessive-alignment-errors |         |         | yes | 25                |     | notify-and-disable | --  |
| Command History            |         |         |     |                   |     |                    |     |
| Release                    |         |         |     | Modification      |     |                    |     |
| 10.08.1010                 |         |         |     | Commandintroduced |     |                    |     |
| Command Information        |         |         |     |                   |     |                    |     |
| Platforms                  | Command | context |     | Authority         |     |                    |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show interface | fault-monitor            |     |     | profile       |     |         |     |
| -------------- | ------------------------ | --- | --- | ------------- | --- | ------- | --- |
| show interface | [<INTERFACE>|<IF-RANGE>] |     |     | fault-monitor |     | profile |     |
Description
Showsfaultmonitoringprofileconfigurationinformationforallorspecificinterfaces.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 224

| Parameter   |     |     | Description                |     |     |
| ----------- | --- | --- | -------------------------- | --- | --- |
| <INTERFACE> |     |     | Specifiesasingleinterface. |     |     |
<IF-RANGE>
Specifiesainterfacerange,
Example
Showingallinterfaceswithappliedfaultmonitoringprofiles:
| switch# | show interface | fault-monitor | profile |     |     |
| ------- | -------------- | ------------- | ------- | --- | --- |
--------------------------------------------------------------------------
| Port | Fault Monitor | Profile |     |     |     |
| ---- | ------------- | ------- | --- | --- | --- |
--------------------------------------------------------------------------
| 1/1/1 | noisy-ports |     |     |     |     |
| ----- | ----------- | --- | --- | --- | --- |
| 1/1/2 | quiet-ports |     |     |     |     |
| 1/1/4 | quiet-ports |     |     |     |     |
| 1/1/5 | noisy-ports |     |     |     |     |
| 1/1/6 | noisy-ports |     |     |     |     |
| 1/1/7 | quiet-ports |     |     |     |     |
Showingarangeofinterfaceswithappliedfaultmonitoringprofiles:
| switch# | show interface | 1/1/1-1/1/2,1/1/6 |     | fault-monitor | profile |
| ------- | -------------- | ----------------- | --- | ------------- | ------- |
--------------------------------------------------------------------------
| Port | Fault Monitor | Profile |     |     |     |
| ---- | ------------- | ------- | --- | --- | --- |
--------------------------------------------------------------------------
| 1/1/1               | noisy-ports |         |                   |     |     |
| ------------------- | ----------- | ------- | ----------------- | --- | --- |
| 1/1/2               | quiet-ports |         |                   |     |     |
| 1/1/6               | noisy-ports |         |                   |     |     |
| Command History     |             |         |                   |     |     |
| Release             |             |         | Modification      |     |     |
| 10.08.1010          |             |         | Commandintroduced |     |     |
| Command Information |             |         |                   |     |     |
| Platforms           | Command     | context | Authority         |     |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show interface | fault-monitor            |     | status        |     |        |
| -------------- | ------------------------ | --- | ------------- | --- | ------ |
| show interface | [<INTERFACE>|<IF-RANGE>] |     | fault-monitor |     | status |
Description
Showsactivefaultinformationforallorspecificinterfaces.
FaultMonitor|225

| Parameter   |     |     | Description                |     |     |
| ----------- | --- | --- | -------------------------- | --- | --- |
| <INTERFACE> |     |     | Specifiesasingleinterface. |     |     |
| <IF-RANGE>  |     |     | Specifiesainterfacerange,  |     |     |
Example
Showingactivefaultinformationforallinterfaceswithappliedfaultmonitoringprofiles:
| switch# | show interface | fault-monitor | status |     |     |
| ------- | -------------- | ------------- | ------ | --- | --- |
Port Time
| Port | Fault |     | Fault Elapsed | Time | State Left |
| ---- | ----- | --- | ------------- | ---- | ---------- |
--------------------------------------------------------------------------------
1/1/1 excessive-broadcasts Tue Apr 14 14:29:09 UTC 2020 down 60
1/1/2 excessive-oversize-packets Tue Apr 16 14:29:09 UTC 2020 down --
Showingactivefaultinformationforarangeofinterfaceswithappliedfaultmonitoringprofiles:
| switch# | show interface | 1/3/1,1/3/3 | fault-monitor | status |     |
| ------- | -------------- | ----------- | ------------- | ------ | --- |
Port Time
| Port | Fault |     | Occurring | Since | State Left |
| ---- | ----- | --- | --------- | ----- | ---------- |
--------------------------------------------------------------------------------
1/1/4 excessive-broadcasts Tue Apr 14 14:29:09 UTC 2020 down 60
| Command    | History     |         |                   |     |     |
| ---------- | ----------- | ------- | ----------------- | --- | --- |
| Release    |             |         | Modification      |     |     |
| 10.08.1010 |             |         | Commandintroduced |     |     |
| Command    | Information |         |                   |     |     |
| Platforms  | Command     | context | Authority         |     |     |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show running-config
show running-config [interface <IFNAME> | current-context | all]
Description
Displaysthefault-monitorprofileconfigurationsandprofile-nameappliedtoaninterface.
| Parameter       |          |     | Description                            |     |     |
| --------------- | -------- | --- | -------------------------------------- | --- | --- |
| interface       | <IFNAME> |     | Specifiesasingleinterface.             |     |     |
| current-context |          |     | Displaysonlycurrentcontextinformation. |     |     |
| all             |          |     | Displaysalloptionsintherunningconfig.  |     |     |
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 226

Example
Showingtherunningconfigurationforthefaultmonitoringprofiles:
switch#
show running-config
| fault-monitor | profile | noisy-ports |     |     |     |
| ------------- | ------- | ----------- | --- | --- | --- |
excessive-broadcasts
| excessive-broadcasts |     |     | threshold | pps | 10000 |
| -------------------- | --- | --- | --------- | --- | ----- |
excessive-broadcasts action notify-and-disable auto-enable 2000
excessive-multicasts
| excessive-multicasts |     |     | threshold | pps | 10000 |
| -------------------- | --- | --- | --------- | --- | ----- |
excessive-link-flaps
excessive-link-flaps action notify-and-disable auto-enable 2000
| interface | 1/1/1         |         |     |             |     |
| --------- | ------------- | ------- | --- | ----------- | --- |
| apply     | fault-monitor | profile |     | noisy-ports |     |
Showingtherunningconfigurationwiththealloption:
| switch# show  | running-config |             | all |     |     |
| ------------- | -------------- | ----------- | --- | --- | --- |
| fault-monitor | profile        | noisy-ports |     |     |     |
excessive-broadcasts
| excessive-broadcasts |     |     | threshold | pps | 10000 |
| -------------------- | --- | --- | --------- | --- | ----- |
excessive-broadcasts action notify-and-disable auto-enable 2000
excessive-multicasts
| excessive-multicasts |     |     | threshold | pps    | 10000 |
| -------------------- | --- | --- | --------- | ------ | ----- |
| excessive-multicasts |     |     | action    | notify |       |
excessive-link-flaps
| excessive-link-flaps |     |     | threshold | count | 7   |
| -------------------- | --- | --- | --------- | ----- | --- |
excessive-link-flaps action notify-and-disable auto-enable 2000
no excessive-oversize-packets
| excessive-oversize-packets |     |     |     | threshold | value 25 |
| -------------------------- | --- | --- | --- | --------- | -------- |
| excessive-oversize-packets |     |     |     | action    | notify   |
no excessive-fragments
| excessive-fragments |     | threshold |     | value  | 25  |
| ------------------- | --- | --------- | --- | ------ | --- |
| excessive-fragments |     | action    |     | notify |     |
no excessive-crc-errors
| excessive-crc-errors |     |     | threshold | value  | 25  |
| -------------------- | --- | --- | --------- | ------ | --- |
| excessive-crc-errors |     |     | action    | notify |     |
no excessive-late-collisions
| excessive-late-collisions |     |     |     | threshold | value 25 |
| ------------------------- | --- | --- | --- | --------- | -------- |
| excessive-late-collisions |     |     |     | action    | notify   |
no excessive-collisions
| excessive-collisions |     |     | threshold | value  | 25  |
| -------------------- | --- | --- | --------- | ------ | --- |
| excessive-collisions |     |     | action    | notify |     |
no excessive-tx-drops
| excessive-tx-drops |     | threshold |     | value  | 25  |
| ------------------ | --- | --------- | --- | ------ | --- |
| excessive-tx-drops |     | action    |     | notify |     |
no excessive-alignment-errors
| excessive-alignment-errors |     |     |     | threshold         | value 25 |
| -------------------------- | --- | --- | --- | ----------------- | -------- |
| excessive-alignment-errors |     |     |     | action            | notify   |
| Command History            |     |     |     |                   |          |
| Release                    |     |     |     | Modification      |          |
| 10.08.1010                 |     |     |     | Commandintroduced |          |
| Command Information        |     |     |     |                   |          |
FaultMonitor|227

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show | running-config |     | all |     |     |     |
| ---- | -------------- | --- | --- | --- | --- | --- |
| show | running-config | all |     |     |     |     |
Description
Showstherunningconfigurationwithallfaultmonitoringprofileoptions.
Example
Showingtherunningconfigurationwithallfaultmonitoringprofileoptions:
| switch#       | show | running-config |             | all |     |     |
| ------------- | ---- | -------------- | ----------- | --- | --- | --- |
| fault-monitor |      | profile        | noisy-ports |     |     |     |
excessive-broadcasts
|     | excessive-broadcasts |     |     | threshold | pps | 10000 |
| --- | -------------------- | --- | --- | --------- | --- | ----- |
excessive-broadcasts action notify-and-disable auto-enable 2000
excessive-multicasts
|     | excessive-multicasts |     |     | threshold | pps    | 10000 |
| --- | -------------------- | --- | --- | --------- | ------ | ----- |
|     | excessive-multicasts |     |     | action    | notify |       |
excessive-link-flaps
|     | excessive-link-flaps |     |     | threshold | count | 7   |
| --- | -------------------- | --- | --- | --------- | ----- | --- |
excessive-link-flaps action notify-and-disable auto-enable 2000
|            | no excessive-oversize-packets |         |           |           |                   |          |
| ---------- | ----------------------------- | ------- | --------- | --------- | ----------------- | -------- |
|            | excessive-oversize-packets    |         |           |           | threshold         | value 40 |
|            | excessive-oversize-packets    |         |           |           | action            | notify   |
|            | no excessive-fragments        |         |           |           |                   |          |
|            | excessive-fragments           |         | threshold |           | value             | 50       |
|            | excessive-fragments           |         | action    |           | notify            |          |
|            | no excessive-crc-errors       |         |           |           |                   |          |
|            | excessive-crc-errors          |         |           | threshold | value             | 35       |
|            | excessive-crc-errors          |         |           | action    | notify            |          |
|            | no excessive-late-collisions  |         |           |           |                   |          |
|            | excessive-late-collisions     |         |           |           | threshold         | value 30 |
|            | excessive-late-collisions     |         |           |           | action            | notify   |
|            | no excessive-collisions       |         |           |           |                   |          |
|            | excessive-collisions          |         |           | threshold | value             | 40       |
|            | excessive-collisions          |         |           | action    | notify            |          |
|            | no excessive-tx-drops         |         |           |           |                   |          |
|            | excessive-tx-drops            |         | threshold |           | value             | 20       |
|            | excessive-tx-drops            |         | action    |           | notify            |          |
| Command    | History                       |         |           |           |                   |          |
| Release    |                               |         |           |           | Modification      |          |
| 10.08.1010 |                               |         |           |           | Commandintroduced |          |
| Command    | Information                   |         |           |           |                   |          |
| Platforms  |                               | Command | context   |           | Authority         |          |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 228

threshold
| <FAULT>                  | threshold | value <VALUE>           |               |
| ------------------------ | --------- | ----------------------- | ------------- |
| no <FAULT>               | threshold | value <VALUE>           |               |
| excessive-link-flaps     |           | threshold               | count <COUNT> |
| no excessive-link-flaps  |           | threshold               | count <COUNT> |
| {excessive-broadcasts    |           | | excessive-multicasts} |               |
| threshold                | {percent  | <BW-PERCENT>            | | pps <PPS>}  |
| no {excessive-broadcasts |           | | excessive-multicasts} |               |
| threshold                | {percent  | <BW-PERCENT>            | | pps <PPS>}  |
no all threshold
Description
Withintheselectedfaultmonitorprofilecontext,configuresthefaultthresholdvaluefortheprofile.
Thenoformofthiscommandsetsthethresholdtoitsdefaultvalue.
| Parameter |     |     | Description          |
| --------- | --- | --- | -------------------- |
| <FAULT>   |     |     | Availablefaultnames: |
excessive-crc-errors
excessive-oversize-packets
excessive-fragments
excessive-tx-drops
excessive-collisions
excessive-late-collisions
excessive-alignment-errors
| threshold | value | <VALUE> |     |
| --------- | ----- | ------- | --- |
Specifiesthefaultthresholdvalue.Default:25.
threshold count <COUNT> Specifiesthefaultthresholdcount.Defaultthresholdcount:7.
| threshold | percent | <BW-PERCENT> |     |
| --------- | ------- | ------------ | --- |
Specifiesthefaultthresholdbandwidthpercentage.Range:1to
100.Default:5.
threshold pps <PPS> SpecifiesthefaultthresholdPPS(packetspersecond).Range:1to
195312500.
Ifexcessive-broadcastorexcessive-multicastfaultsareconfiguredwiththethresholdhigherthantherate-
limitthreshold,thefollowingoccurs:
n Faultreportingstillhappensastheporthasactuallyreceivedpacketsataratethatviolateditsthreshold.
n Trafficgetsshapedasperrate-limitconfigurationandanypacketexceedingtherate-limitthreshold
getsdropped.
Examples
Configuringwiththresholdvalues:
switch(config-fault-monitor-profile)# excessive-oversize-packets threshold value
40
FaultMonitor|229

switch(config-fault-monitor-profile)# excessive-crc-errors threshold value 35
switch(config-fault-monitor-profile)#
|     |     |     | excessive-fragments | threshold | value 50 |
| --- | --- | --- | ------------------- | --------- | -------- |
switch(config-fault-monitor-profile)# excessive-tx-drops threshold value 20
switch(config-fault-monitor-profile)# excessive-collisions threshold value 40
switch(config-fault-monitor-profile)# excessive-late-collisions threshold value 30
switch(config-fault-monitor-profile)# excessive-alignment-errors threshold value
50
Configuringwithathresholdcount:
switch(config-fault-monitor-profile)# excessive-link-flaps threshold count 10
ConfiguringwiththresholdpercentsandPPS:
switch(config-fault-monitor-profile)# excessive-broadcasts threshold percent 40
switch(config-fault-monitor-profile)# excessive-multicasts threshold pps 10000
Removingtheconfiguredthresholdtodefaultthresholdforthefaults:
switch(config-fault-monitor-profile)# no excessive-oversize-packets threshold
| value 40 |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
switch(config-fault-monitor-profile)# no excessive-crc-errors threshold value 35
switch(config-fault-monitor-profile)# no excessive-fragments threshold value 50
switch(config-fault-monitor-profile)# no excessive-tx-drops threshold value 20
switch(config-fault-monitor-profile)#
|     |     |     | no excessive-collisions | threshold | value 40 |
| --- | --- | --- | ----------------------- | --------- | -------- |
switch(config-fault-monitor-profile)# no excessive-late-collisions threshold value
30
switch(config-fault-monitor-profile)# no excessive-alignment-errors threshold
| value 50 |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
switch(config-fault-monitor-profile)# no excessive-link-flaps threshold count 10
switch(config-fault-monitor-profile)# no excessive-broadcasts threshold percent 40
switch(config-fault-monitor-profile)# no excessive-multicasts threshold pps 10000
| switch(config-fault-monitor-profile)# |         |                                          | no all threshold |     |     |
| ------------------------------------- | ------- | ---------------------------------------- | ---------------- | --- | --- |
| Command History                       |         |                                          |                  |     |     |
| Release                               |         | Modification                             |                  |     |     |
| 10.09                                 |         | Addedparameterstothenoformofthecommands. |                  |     |     |
| 10.08.1010                            |         | Commandintroduced.                       |                  |     |     |
| Command Information                   |         |                                          |                  |     |     |
| Platforms                             | Command | context                                  | Authority        |     |     |
config-fault-monitor-profile
| 8400 |     |     | Administratorsorlocalusergroupmemberswith |     |     |
| ---- | --- | --- | ----------------------------------------- | --- | --- |
executionrightsforthiscommand.
| vsx-sync | (fault monitor) |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
vsx-sync
no vsx-sync
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 230

Description
Withintheselectedfaultmonitorprofilecontext,configuresVSXsynchronizationfortheselectedfault
monitoringprofile.
ThenoformofthiscommandremovestheVSXsynchronizationforafaultmonitoringprofile.
Example
ConfiguringVSXsynchronizationforafaultmonitoringprofile:
| switch(config-fault-monitor-profile)# |     | vsx-sync |     |
| ------------------------------------- | --- | -------- | --- |
| Command History                       |     |          |     |
Release Modification
10.08.1010 Commandintroduced
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-fault-monitor-profile
| 8400 |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | ----------------------------------------- |
executionrightsforthiscommand.
FaultMonitor|231

Chapter 13

Configuring enhanced security

Configuring enhanced security

Several measures can be taken to enhance switch security, including setting secure mode to enhanced
in the Service OS. For maximum security, perform all the configuration described in this chapter.

Configuring enhanced security

Prerequisites

If you have switch configuration that you want to retain, create a backup. This procedure erases all
configuration, including the current running configuration, the startup configuration, and all historical
configuration checkpoints.

Procedure

1. Set enhanced security mode:

a. Reboot the switch into the Service OS with command boot system serviceos. If on an 8400

Switch with both Management Modules:

i.

Issue the boot command only on the active Management Module. This command ensures
that both Management Modules are booted into the Service OS.

ii. Perform steps b to e on both modules starting with the active module.

b. Log in to the Service OS as admin.
c. Enter command secure-mode enhanced.
d. When prompted about the mode change, respond with y for "yes."
e. Wait for the reboot and zeroization to complete. The switch firmware boots automatically.

2. Ensure adequate password requirements:

a. Before adding users, enable and configure password complexity as described in password

complexity. To maintain enhanced security, configure the password complexity
subcommand settings no smaller than their defaults.

b. Configure passwords for all users, including admin. To make your password complexity

settings applicable to the default admin user, change the admin password after enabling
password complexity. The new admin password must respect your password complexity
settings.

3. Ensure proper login management as follows:

a. Configure local user session management as described in CLI user session management

commands using cli-session and its subcommands max-per-user, timeout, and tracking-
range to achieve the wanted configuration. To maintain enhanced security, configure cli-
session subcommand settings no smaller than their defaults.

b. Restrict remote SSH connections to only use certified crypto algorithms using ssh certified-

algorithms-only.

c. Configure pre- and post-login banners using respectively, banner motd, and banner exec.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

232

4. Ensure that the switch date and time is accurately set using clock datetime <DATE> <TIME>.

5. When logging to a remote syslog server is required, ensure that the connection to the server is

cryptographically secure. See Configuring remote logging using SSH reverse tunnel.

To ensure that enhanced security is maintained, also respect these requirements:

n Do not configure remote logging with a remote server directly without setting up an SSH tunnel.

n Do not configure passwords and secret keys using the plaintext option.

When in enhanced security mode, the switch (Product OS) start-shell command is disabled for security
purpose. If you attempt to use this command while in enhanced security mode, it is rejected and the following

error message is displayed:

The start-shell command is not available in enhanced secure mode.

When in enhanced security mode, the following Service OS commands are disabled for security purposes:
config-clear, password, sh, and update. If you attempt to use any of these Service OS commands while in
enhanced security mode, the command is rejected and an error message is displayed.

password complexity

Syntax

password complexity
no password complexity

Description

Enters the password-complexity context (shown in the switch prompt as config-pwd-cplx) for the
purpose of enabling and configuring password complexity. Password complexity enhances security by
enforcing specific password complexity requirements. Password complexity is disabled by default and
must be enabled by execution of the enable command.

The no form of this command reverts all settings to their default values and disables password
complexity enforcement.

To ensure that enhanced security is maintained, it is recommended that you do not set any values to less than

their defaults.

Password complexity apples only to local authentication. For remote authentication, you may choose to set up an

equivalent of password complexity according to whatever is supported on your particular TACACS+ or RADIUS

server.

Command context

config

Subcommands

These subcommands are available within the password complexity context (shown in the switch prompt
as config-pwd-cplx).
enable

Configuring enhanced security | 233

Enables password complexity enforcement. The enforcement only applies to passwords created
after this enabling. Existing passwords are not checked against password complexity.

disable

Disables password complexity enforcement.

[no] history-count <COUNT>

Specifies the number of previous passwords checked to prevent excessive reuse. Not applicable
when adding new users. The no form of this subcommand resets the value to its default. Default: 5.
Range: 1 to 5.

[no] minimum-length <LENGTH>

Specifies the minimum password length. The no form of this subcommand resets the value to its
default. Default: 8. Range: 1 to 32.
[no] position-changes <POSITIONS>

Specifies the minimum number of characters that must change in the new password compared to
the previous password. Not applicable if no previous password exists, including when adding new
users. The no form of this subcommand resets the value to its default. Default: 8. Range: 1 to 32.

The number of password position changes is based on the number of simple character insertions,
deletions, or replacements. For example:

Old password: abCD4$ New password: abCD$    Position changes=1 ("4" deleted) Old password:
abCD4$ New password: abCDEF4$ Position changes=2 ("EF" inserted) Old password: abCD4$ New
password: ebCD4$1 Position changes=2 ("a"replaced with "e," "1" added) Old password: abCD4$ New
password: abC$# Position changes=3 ("D4" deleted, "#" added)

[no] lowercase-count

<COUNT>

Specifies the minimum lowercase character count for new passwords. The no form of this
subcommand resets the value to its default. Default: 1. Range: 0 to 32.

[no] uppercase-count

<COUNT>

Specifies the minimum uppercase character count for new passwords. The no form of this
subcommand resets the value to its default. Default: 1. Range: 0 to 32.

[no] numeric-count <COUNT>

Specifies the minimum numeric digit count for new passwords. The no form of this subcommand
resets the value to its default. Default: 1. Range: 0 to 32.

[no] special-char-count <COUNT>

Specifies the minimum special character count for new passwords. The no form of this subcommand
resets the value to its default. Default: 1. Range: 0 to 32.

list

List the subcommands available within the password complexity context.

exit

Exits the password complexity context.

end

Exits the password complexity context and then the config context.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n Password complexity is only for use with plaintext passwords. With password complexity enabled,

existing ciphertext passwords will continue working until a password is changed. All new passwords
must be entered in plaintext form and be compliant with your password complexity configuration.

n The effective minimum password length may be larger than the configured minimum-length value.

The effective minimum password length is calculated as follows:

LARGEST-of:(minimum-length, position-changes,(SUM-of:lowercase-count+uppercase-
count+numeric-count+special-char-count))

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

234

Forexample,withminimum-length=8,andposition-changes=10(andthesumoftheotherfourcount
settings<=9),theeffective minimum-length is 10(becauseposition-changesislargest).Similarity,
withaminimum-length=12,position-changes=8,lowercase-count=8,uppercase-count=4,numeric-
count=1,special-char-count=1,the effective minimum-length is 14(8+4+1+1=14)(becausesumoff
thefourcountsislargest).
Examples
Configuringpasswordcomplexitysettingswithaneffectiveminimumlengthof10(becauseposition-
changesis10):
| switch(config)#          | password | complexity         |     |
| ------------------------ | -------- | ------------------ | --- |
| switch(config-pwd-cplx)# |          | history-count      | 3   |
| switch(config-pwd-cplx)# |          | minimum-length     | 8   |
| switch(config-pwd-cplx)# |          | position-changes   | 10  |
| switch(config-pwd-cplx)# |          | lowercase-count    | 2   |
| switch(config-pwd-cplx)# |          | uppercase-count    | 2   |
| switch(config-pwd-cplx)# |          | numeric-count      | 2   |
| switch(config-pwd-cplx)# |          | special-char-count | 2   |
| switch(config-pwd-cplx)# |          | enable             |     |
switch# exit
Configuringpasswordcomplexitysettingswithaneffectiveminimumlengthof14(becausethesumof
thefourcountitemsis14):
| switch(config)#          | password | complexity         |     |
| ------------------------ | -------- | ------------------ | --- |
| switch(config-pwd-cplx)# |          | history-count      | 4   |
| switch(config-pwd-cplx)# |          | minimum-length     | 12  |
| switch(config-pwd-cplx)# |          | position-changes   | 8   |
| switch(config-pwd-cplx)# |          | lowercase-count    | 8   |
| switch(config-pwd-cplx)# |          | uppercase-count    | 4   |
| switch(config-pwd-cplx)# |          | numeric-count      | 1   |
| switch(config-pwd-cplx)# |          | special-char-count | 1   |
| switch(config-pwd-cplx)# |          | enable             |     |
switch# exit
Enablingpasswordcomplexity(withdefaultsettings)andchangingauser(admin1)password
successfullybutfailingtochangeanotheruser(admin2)passwordduetonotmeetingcomplexity
requirements:
| switch(config)#          | password | complexity |     |
| ------------------------ | -------- | ---------- | --- |
| switch(config-pwd-cplx)# |          | enable     |     |
| switch(config-pwd-cplx)# |          | exit       |     |
switch(config)#
| switch(config)#                   | user admin1 | password |     |
| --------------------------------- | ----------- | -------- | --- |
| Changing password                 | for user    | admin1   |     |
| Enter old password:************   |             |          |     |
| Enter new password:************   |             |          |     |
| Confirm new password:************ |             |          |     |
switch(config)#
| switch(config)#                   | user admin2  | password |     |
| --------------------------------- | ------------ | -------- | --- |
| Changing password                 | for user     | admin2   |     |
| Enter old password:************   |              |          |     |
| Enter new password:************   |              |          |     |
| Confirm new password:************ |              |          |     |
| User password                     | not changed. |          |     |
The new password does not meet one or more of the following complexity
Configuringenhancedsecurity|235

requirements:
| Minimum   | length    |       | : 8 |     |     |     |
| --------- | --------- | ----- | --- | --- | --- | --- |
| Position  | changes   |       | : 8 |     |     |     |
| Numeric   | count     |       | : 1 |     |     |     |
| Lowercase | count     |       | : 1 |     |     |     |
| Uppercase | count     |       | : 1 |     |     |     |
| Special   | character | count | : 1 |     |     |     |
switch(config)#
Withpasswordcomplexityalreadyenabled,attemptingtochangeanexistinguserpasswordbutfailing
becausethenewpasswordisidenticaltoarecentlyusedone(history-count).
| switch(config)# |                           | user         | admin1 password    |      |           |     |
| --------------- | ------------------------- | ------------ | ------------------ | ---- | --------- | --- |
| Changing        | password                  | for          | user admin1        |      |           |     |
| Enter old       | password:************     |              |                    |      |           |     |
| Enter new       | password:************     |              |                    |      |           |     |
| Confirm         | new password:************ |              |                    |      |           |     |
| User password   |                           | not changed. |                    |      |           |     |
| The new         | password                  | is the       | same as a recently | used | password. |     |
switch(config)#
Withpasswordcomplexityalreadyenabled,creatinganewadminuser(admin3)withaplaintext
passwordthatmeetscomplexityrequirements.
| switch(config)#             |                       | user | admin3 group administrators |     | password |     |
| --------------------------- | --------------------- | ---- | --------------------------- | --- | -------- | --- |
| Adding                      | user admin3           |      |                             |     |          |     |
| Enter password:************ |                       |      |                             |     |          |     |
| Confirm                     | password:************ |      |                             |     |          |     |
switch(config)#
Withpasswordcomplexityalreadyenabled,attemptingtocreateanewadminuser(admin4)witha
ciphertextpasswordbutfailingbecauseciphertextpasswordsarenotsupportedwithpassword
complexityenabled.
switch(config)# user admin4 group administrators password ciphertext AQBapPd...==
Ciphertext passwords cannot be used when password complexity is enabled.
switch(config)#
| Configuring |     | remote | logging | using | SSH reverse | tunnel |
| ----------- | --- | ------ | ------- | ----- | ----------- | ------ |
LoggingtoaremotesyslogservercanbemadecryptographicallysecurebyusingSSHreversetunnel.
ThesyslogdaemonontheswitchforwardslogmessagestotheSSHtunnel,andtheSSHtunnel
endpointontheremoteserverhostforwardsmessagestothelisteningsyslogserver.
Thisprocedureincludessampleconfigurationcommandsforauser-suppliedsyslogserverbasedonUbuntu
14.04.5LTSwithrsyslog.Itisuptotheusertochecktheirserverdocumentationandadjustthesample
commandsasrequired.Optionallyseeyourserverdocumentationforinformationonhowtousethesystemd
andautosshservicestoautomaticallyrestoretheSSHtunnelaftersystemreboot.
Prerequisites
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 236

Theuser-suppliedremotesyslogservermustbeonanetworkthatcanreachtheswitchmanagement
interface.
Procedure
1. ConfigureSSHserverontheswitch.
a. Enterthesecommands(althoughthisexampleusesthemgmtVRF,otherVRFscanbeused):
|     | switch(config)#         | interface | mgmt            |                  |     |
| --- | ----------------------- | --------- | --------------- | ---------------- | --- |
|     | switch(config-if-mgmt)# |           | no shutdown     |                  |     |
|     | switch(config-if-mgmt)# |           | ip address      | <switch_mgmt_IP> |     |
|     | switch(config-if-mgmt)# |           | exit            |                  |     |
|     | switch(config)#         | ssh       | server vrf mgmt |                  |     |
b. IfpublickeyauthenticationisdesiredforremoteSSHusers,configureitontheswitch:
|     | switch(config)# | user | admin authorized-key |     | <PUBKEY> |
| --- | --------------- | ---- | -------------------- | --- | -------- |
2. Configureloggingontheswitchtoforwardtolocalhost:
switch(config)# logging localhost tcp <switch_tcp_port> vrf mgmtinclude-auditable-
events
3. Configurethersyslogserverontheremotehost:
a. MakersyslogacceptTCPconnectionsandspecifythelogfile,byaddingthefollowingto
/etc/rsyslog.conf:
|     | $ModLoad imtcp                             |                   |     |     |     |
| --- | ------------------------------------------ | ----------------- | --- | --- | --- |
|     | $InputTCPServerRun                         | <server_tcp_port> |     |     |     |
|     | $template RemoteLogs,"/var/log/remote.log" |                   |     |     |     |
*.* ?RemoteLogs
|     | b. Toactivatetheaddedconfiguration,restartthersyslogserver: |     |                 |     |         |
| --- | ----------------------------------------------------------- | --- | --------------- | --- | ------- |
|     | root@Ubuntu4479:~#sudo                                      |     | service rsyslog |     | restart |
4. EstablishanSSHreversetunnelfromtheremotehosttotheswitch:
|     | root@Ubuntu4479:~#ssh | -nNTx | –R  |     |     |
| --- | --------------------- | ----- | --- | --- | --- |
<switch_tcp_port>:127.0.0.1:<server_tcp_port>
admin@<switch_mgmt_IP>
| CLI | user session | management |     | commands |     |
| --- | ------------ | ---------- | --- | -------- | --- |
cli-session
cli-session
no cli-session
Description
EnterstheCLIsessioncontext(shownintheswitchpromptasconfig-cli-session)forthepurposeof
configuringCLIusersessionmanagement.Sessionmanagementenhancessecuritybyenforcing
specificCLIusersessionrequirements.Thefollowinginformationisprovidedattimeofsuccessfullogin:
n Whenapplicable,thenumberoffailedloginattemptssincethemostrecentsuccessfullogin.
n Thedate,time,andlocation(consoleorIPaddressorhostname)ofthemostrecentprevious
successfullogin.
n Thecountofsuccessfulloginswithinthepast(configurable)timeperiod.
Forexample:
| switch | login: admin |     |     |     |     |
| ------ | ------------ | --- | --- | --- | --- |
Password:
There were 3 failed login attempts since the last successful login
Configuringenhancedsecurity|237

| Last login:  | 2019-04-20 | 08:51:33 | from the     | console      |
| ------------ | ---------- | -------- | ------------ | ------------ |
| User "admin" | has logged | in 73    | times in the | past 30 days |
ThenoformofthiscommanddisablesconcurrentCLIusersessionrestrictionsandrevertstimeoutand
tracking-rangetotheirdefaultvalues.
Toensurethatenhancedsecurityismaintained,itisrecommendedthatyoukeepCLIusersessionmanagement
| fullyenabledbysetting |     | max-per-usertoanondefaultvalue. |     |     |
| --------------------- | --- | ------------------------------- | --- | --- |
Thecli-sessioncommandappliesonlytoSSH/consoleloginconnectiontypes.Itdoesnotapplytoother
connectiontypessuchasREST.
Subcommands
ThesesubcommandsareavailablewithintheCLIsessioncontext.
| [no] max-per-user | <SESSIONS> |     |     |     |
| ----------------- | ---------- | --- | --- | --- |
SpecifiesthemaximumnumberofconcurrentCLIsessionsperuser.Thenoformofthis
subcommanddisablesconcurrentCLIusersessionrestrictions.Default:Disabled(novalue).Range:1
to5.
Whenthesameusernameisconfiguredforbothlocalandremoteauthentication,bothusers,regardlessof
privilegelevel,areconsideredtobethesameuserforthepurposeofcountingconcurrentCLIsessions.For
example,withmax-per-usersetto1anduseradmin1configuredforlocalandremoteauthentication,onlythe
localuseradmin1ortheremoteuseradmin1canbeloggedinatanygivenmoment.Bothadmin1userscannot
beloggedinsimultaneouslyunlessmax-per-userisincreasedtoatleast2.
| [no] timeout | <MINUTES> |     |     |     |
| ------------ | --------- | --- | --- | --- |
SpecifiesthenumberofminutesaCLIsessioncanbeidlebeforethesessionisautomatically
terminatedandtheuserisloggedout.Avalueof0minutesdisablesthesessiontimeout.Theno
formofthissubcommandsetsthetimeoutvaluetothedefault.Default30:Range0to4320.
Thissubcommandistherecommendedreplacementforthesession-timeoutcommand.
| [no] tracking-range |     | <DAYS> |     |     |
| ------------------- | --- | ------ | --- | --- |
SpecifiesthemaximumnumberofdaystotrackCLIusersessionlogins.Thenoformofthis
subcommandresetsthevaluetoitsdefault.Default30:Range1to30.
exit
ExitstheCLIsessioncontext.
end
ExitstheCLIsessioncontextandthentheconfigcontext.
Examples
ConfiguringCLIusersessionsettingsforamaximumofoneconcurrentsession,a20-minutetimeout,
andtrackingforamaximumof25days.
| switch(config)#             |      | cli-session |                |     |
| --------------------------- | ---- | ----------- | -------------- | --- |
| switch(config-cli-session)# |      |             | max-per-user   | 1   |
| switch(config-cli-session)# |      |             | timeout 20     |     |
| switch(config-cli-session)# |      |             | tracking-range | 25  |
| switch#                     | exit |             |                |     |
Aftersuccessfulearlierlogins,logginginfromtheconsolewithoutanyinterveningunsuccessfullogins.
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries) 238

| switch login: | admin1 |     |     |     |
| ------------- | ------ | --- | --- | --- |
Password:
| Last login:   | 2019-04-15 | 14:10:21 | from the console  |         |
| ------------- | ---------- | -------- | ----------------- | ------- |
| User 'admin1' | has logged | in 65    | times in the past | 25 days |
Attemptingtologinasadmin1whenalreadyloggedinasadmin1fromelsewhere.
| switch login: | admin1 |     |     |     |
| ------------- | ------ | --- | --- | --- |
Password:
| Too many | logins for | 'admin1' |     |     |
| -------- | ---------- | -------- | --- | --- |
Aftersuccessfulearlierlogins,attemptingtologintwicewithaninvalidpassword,followedbya
successfullogin.
| switch login: | admin1 |     |     |     |
| ------------- | ------ | --- | --- | --- |
Password:
| Login incorrect |        |     |     |     |
| --------------- | ------ | --- | --- | --- |
| switch login:   | admin1 |     |     |     |
Password:
| Login incorrect |        |     |     |     |
| --------------- | ------ | --- | --- | --- |
| switch login:   | admin1 |     |     |     |
Password:
There were 2 failed login attempts since the last successful login
| Last login:         | 2019-04-15 | 17:22:45 | from 192.168.1.1  |         |
| ------------------- | ---------- | -------- | ----------------- | ------- |
| User 'admin1'       | has logged | in 72    | times in the past | 25 days |
| Command History     |            |          |                   |         |
| Release             |            |          | Modification      |         |
| 10.07orearlier      |            |          | --                |         |
| Command Information |            |          |                   |         |
| Platforms           | Command    | context  | Authority         |         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
Configuringenhancedsecurity|239

Chapter 14
|          |              |       |     | Auditors | and auditing | tasks |
| -------- | ------------ | ----- | --- | -------- | ------------ | ----- |
| Auditors | and auditing | tasks |     |          |              |       |
Theauditorsgroupenablesadministratorstocreateusersthatcanperformauditingtaskswithout
allowingthoseuserstheauthoritytovieworchangetheswitchconfiguration.
Asisthecaseforotherusers,auditorscanaccesstheswitchusingtheWebUI,RESTAPI,ortheCLI.
| Auditing | tasks | (CLI) |     |     |     |     |
| -------- | ----- | ----- | --- | --- | --- | --- |
WhenyoulogontotheswitchCLIasauserwithauditorrights,youhaveaccesstotheauditorcommand
contextonly.
auditor>
Thetasksthatcanbeperformedbyauditorsareasfollows.Thecommandslistedaretheonly
commandsauditorscanexecuteotherthansessioncommandslikeprint,list,andexit.However,
auditorscanuseallcommandoptionsexceptasnoted.Seethecommanddescriptionforeach
commandforcompleteinformationaboutthecommand.
| Task                   |     | Command         | name | Example                 |             |     |
| ---------------------- | --- | --------------- | ---- | ----------------------- | ----------- | --- |
| Showeventlogcontents   |     | show events     |      | show events             | -a -r       |     |
|                        |     |                 |      | show accounting         | log last 10 |     |
| Showlocalaccountinglog |     | show accounting |      |                         |             |     |
| contents               |     | log             |      |                         |             |     |
| Copycommandoutputto    |     | copy command-   |      | copy command-output     |             |     |
| aremoteserverortoa     |     | output          |      | "show events            | -a -r"      |     |
| localUSBdrive.         |     |                 |      | tftp://10.100.0.12/file |             |     |
Whenusingthecopy command-output command,userswithauditorrightscanspecifythefollowingcommands
only:
| show accounting | log |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
show events
| Auditing | tasks | (Web | UI) |     |     |     |
| -------- | ----- | ---- | --- | --- | --- | --- |
AuditorshaveaccesstotheLogpageonly.WhenyoulogontotheswitchWebUIasauserwithauditor
rights,theLogpageisdisplayed.
FromtheLogpage,youcanviewandexporteventlogentries.
TheWebUIdoesnotprovideaccesstotheaccountinglogs.
240
AOS-CX10.10SecurityGuide|(832x,8400,9300,10000SwitchSeries)

REST requests and accounting logs

All REST requests—including GET requests—are logged to the accounting (audit) log.

The URI of the REST API resource for accounting logs is the following:
/rest/v10.04/logs/audit

In an accounting log entry for a REST request:

n service=https-server indicates that the log entry is a result of a REST API request or a Web UI

action.

n The string value of data identifies the REST API request that was executed.

For more information about accounting log entries, see the description of the show accounting log CLI
command.

Auditors and auditing tasks | 241

Chapter 15

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

HPE Aruba
Networking
Developer Hub

Airheads social
forums and
Knowledge Base

https://developer.arubanetworks.com/hpe-aruba-networking-aoscx/docs/about

https://community.arubanetworks.com/

AOS-CX Software

Videos on new features introduced in this release:

Technical Update

https://www.youtube.com/playlist?list=PLsYGHuNuBZcbWPEjjHuVMqP-Q_UL3CskS

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

242

channel on

YouTube.

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

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

https://networkingsupport.hpe.com/downloads

https://licensemanagement.hpe.com/

https://www.arubanetworks.com/support-services/end-of-life/

Accessing Updates

You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

https://asp.arubanetworks.com/downloads

If you are unable to find your product in the Aruba Support Portal, you may need to search My
Networking, where older networking products can be found:

My Networking

https://www.hpe.com/networking/support

To view and update your entitlements, and to link your contracts and warranties with your profile, go to
the Hewlett Packard Enterprise Support Center More Information on Access to Support Materials
page:

https://support.hpe.com/portal/site/hpsc/aae/home/

Access to some updates might require product entitlement when accessed through the Hewlett Packard
Enterprise Support Center. You must have an HP Passport set up with relevant entitlements.

Some software products provide a mechanism for accessing software updates through the product
interface. Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://asp.arubanetworks.com/notifications/subscriptions (requires an active Aruba Support Portal
(ASP) account to manage subscriptions). Security notices are viewable without an ASP account.

Warranty Information

To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Support and Other Resources | 243

Regulatory Information

To view the regulatory information for your product, view the Safety and Compliance Information for
Server, Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs,
product recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For
more information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation Feedback

Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

AOS-CX 10.10 Security Guide | (832x, 8400, 9300, 10000 Switch Series)

244