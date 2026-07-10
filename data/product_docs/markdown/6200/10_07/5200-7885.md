AOS-CX 10.07 Security Guide

6200, 6300, 6400 Switch Series

Part Number: 5200-7885
Published: April 2021
Edition: 1

Copyright Information

© Copyright 2021 Hewlett Packard Enterprise Development LP.

Open Source Code

This product includes code licensed under the GNU General Public License, the GNU Lesser General Public
License, and/or certain other open source licenses. A complete machine-readable copy of the source code
corresponding to such code is available upon request. This offer is valid to anyone in receipt of this
information and shall expire three years following the date of the final distribution of this product version
by Hewlett Packard Enterprise Company. To obtain such source code, send a check or money order in the
amount of US $10.00 to:

Hewlett Packard Enterprise Company
6280 America Center Drive
San Jose, CA 95002
USA

Notices

The information contained herein is subject to change without notice. The only warranties for Hewlett
Packard Enterprise products and services are set forth in the express warranty statements accompanying
such products and services. Nothing herein should be construed as constituting an additional warranty.
Hewlett Packard Enterprise shall not be liable for technical or editorial errors or omissions contained herein.

Confidential computer software. Valid license from Hewlett Packard Enterprise required for possession, use,
or copying. Consistent with FAR 12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the U.S. Government under
vendor's standard commercial license.

Links to third-party websites take you outside the Hewlett Packard Enterprise website. Hewlett Packard
Enterprise has no control over and is not responsible for information outside the Hewlett Packard
Enterprise website.

| 2

Contents
Contents
| Contents                                                |                                        |            | 3   |
| ------------------------------------------------------- | -------------------------------------- | ---------- | --- |
| About this                                              | document                               |            | 12  |
| Applicableproducts                                      |                                        |            | 12  |
| Latestversionavailableonline                            |                                        |            | 12  |
| Commandsyntaxnotationconventions                        |                                        |            | 12  |
| Abouttheexamples                                        |                                        |            | 13  |
| Identifyingswitchportsandinterfaces                     |                                        |            | 13  |
| Identifyingmodularswitchcomponents                      |                                        |            | 14  |
| About security                                          |                                        |            | 15  |
| AboutAuthentication,Authorization,andAccounting(AAA)    |                                        |            | 15  |
| Managing                                                | local users                            | and groups | 16  |
| Defaultuseradmin                                        |                                        |            | 16  |
|                                                         | Exampleoffirstloginwithpasswordsetting |            | 16  |
| Built-inusergroupsandtheirprivileges                    |                                        |            | 16  |
| User-definedusergroups                                  |                                        |            | 17  |
| Usernamerequirements                                    |                                        |            | 17  |
| Passwordrequirements                                    |                                        |            | 18  |
| Userandusergroupmanagementtasks                         |                                        |            | 18  |
| ResettingtheswitchadminpasswordusingtheServiceOSconsole |                                        |            | 19  |
|                                                         | Prerequisites                          |            | 19  |
|                                                         | Procedure                              |            | 19  |
Resettingtheadminpasswordbyrevertingtheswitchtofactorydefaults 20
|                      | Prerequisites              |     | 20  |
| -------------------- | -------------------------- | --- | --- |
|                      | Procedure                  |     | 20  |
| Userandgroupcommands |                            |     | 21  |
|                      | user                       |     | 21  |
|                      | user-group                 |     | 23  |
|                      | userpassword               |     | 27  |
|                      | serviceexport-password     |     | 28  |
|                      | showuser-group             |     | 29  |
|                      | showuserinformation        |     | 30  |
|                      | showuser-list              |     | 31  |
| SSH server           |                            |     | 34  |
| SSHdefaults          |                            |     | 34  |
| SSHservertasks       |                            |     | 34  |
| SSHservercommands    |                            |     | 35  |
|                      | showsshhost-key            |     | 35  |
|                      | showsshserver              |     | 36  |
|                      | showsshserversessions      |     | 39  |
|                      | sshciphers                 |     | 40  |
|                      | sshhost-key                |     | 42  |
|                      | sshhost-key-algorithms     |     | 42  |
|                      | sshkey-exchange-algorithms |     | 44  |
|                      | sshknown-hostremove        |     | 45  |
|                      | sshmacs                    |     | 46  |
3
AOS-CX10.07SecurityGuide| (6200,6300,6400SwitchSeries)

|                                                           | sshmaximum-auth-attempts                 |         | 47  |
| --------------------------------------------------------- | ---------------------------------------- | ------- | --- |
|                                                           | sshpublic-key-algorithms                 |         | 47  |
|                                                           | sshservervrf                             |         | 49  |
| SSH client                                                |                                          |         | 50  |
| SSHclientcommands                                         |                                          |         | 50  |
|                                                           | ssh(clientlogin)                         |         | 50  |
| Local                                                     | AAA                                      |         | 52  |
| LocalAAAdefaultsandlimits                                 |                                          |         | 52  |
| Localauthentication                                       |                                          |         | 52  |
|                                                           | Password-basedlocalauthentication        |         | 52  |
|                                                           | SSHpublickey-basedlocalauthentication    |         | 53  |
|                                                           | Localauthenticationtasks                 |         | 53  |
| Localauthorization                                        |                                          |         | 55  |
|                                                           | Localauthorizationtasks                  |         | 55  |
| Localaccounting                                           |                                          |         | 56  |
|                                                           | Localaccountingtasks                     |         | 56  |
| Local                                                     | AAA commands                             |         | 57  |
| aaaaccountingall-mgmt                                     |                                          |         | 57  |
| aaaauthenticationconsole-login-attempts                   |                                          |         | 58  |
| aaaauthenticationlimit-login-attempts                     |                                          |         | 59  |
| aaaauthenticationlogin                                    |                                          |         | 60  |
| aaaauthenticationminimum-password-length                  |                                          |         | 61  |
| aaaauthorizationcommands                                  |                                          |         | 62  |
| showaaaaccounting                                         |                                          |         | 64  |
| showaaaauthentication                                     |                                          |         | 64  |
| showaaaauthorization                                      |                                          |         | 65  |
| showsshauthentication-method                              |                                          |         | 66  |
| showuser                                                  |                                          |         | 67  |
| sshpassword-authentication                                |                                          |         | 68  |
| sshpublic-key-authentication                              |                                          |         | 68  |
| userauthorized-key                                        |                                          |         | 69  |
| Remote                                                    | AAA with                                 | TACACS+ | 71  |
| Defaultservergroups                                       |                                          |         | 71  |
| RemoteAAA(TACACS+)defaultsandlimits                       |                                          |         | 71  |
| Aboutglobalversusper-TACACS+serverpasskeys(sharedsecrets) |                                          |         | 72  |
| RemoteAAATACACS+serverconfigurationrequirements           |                                          |         | 72  |
|                                                           | UserroleassignmentusingTACACS+attributes |         | 72  |
|                                                           | TACACS+serverredundancyandaccesssequence |         | 73  |
SinglesourceIPaddressforconsistentsourceidentificationtoAAAservers 73
| TACACS+generaltasks                                 |                                                           |     | 74  |
| --------------------------------------------------- | --------------------------------------------------------- | --- | --- |
| TACACS+authentication                               |                                                           |     | 74  |
|                                                     | Aboutauthenticationfail-through                           |     | 74  |
|                                                     | TACACS+authenticationtasks                                |     | 75  |
| TACACS+authorization                                |                                                           |     | 75  |
|                                                     | UsinglocalauthorizationasfallbackfromTACACS+authorization |     | 76  |
|                                                     | Aboutauthenticationfail-throughandauthorization           |     | 76  |
|                                                     | TACACS+authorizationtasks                                 |     | 76  |
| TACACS+accounting                                   |                                                           |     | 77  |
|                                                     | SampleaccountinginformationonaTACACS+server               |     | 77  |
|                                                     | SampleRESTaccountinginformationonaTACACS+server           |     | 78  |
|                                                     | TACACS+accountingtasks                                    |     | 78  |
| Example:ConfiguringtheswitchforRemoteAAAwithTACACS+ |                                                           |     | 79  |
Contents|4

|                                                          | Prerequisites                           |        |     | 79  |
| -------------------------------------------------------- | --------------------------------------- | ------ | --- | --- |
|                                                          | Procedure                               |        |     | 79  |
| Remote                                                   | AAA with                                | RADIUS |     | 82  |
| Defaultservergroups                                      |                                         |        |     | 82  |
| RemoteAAA(RADIUS)defaultsandlimits                       |                                         |        |     | 82  |
| Aboutglobalversusper-RADIUSserverpasskeys(sharedsecrets) |                                         |        |     | 83  |
| RemoteAAARADIUSserverconfigurationrequirements           |                                         |        |     | 83  |
|                                                          | UserroleassignmentusingRADIUSattributes |        |     | 84  |
|                                                          | RADIUSserverredundancyandaccesssequence |        |     | 84  |
SinglesourceIPaddressforconsistentsourceidentificationtoAAAservers 85
| RADIUSgeneraltasks                                 |                                       |         |          | 85  |
| -------------------------------------------------- | ------------------------------------- | ------- | -------- | --- |
| RADIUSauthentication                               |                                       |         |          | 86  |
|                                                    | Aboutauthenticationfail-through       |         |          | 86  |
|                                                    | RADIUSauthenticationtasks             |         |          | 86  |
|                                                    | Configuringtwo-factorauthentication   |         |          | 87  |
|                                                    | Prerequisites                         |         |          | 87  |
|                                                    | Procedure                             |         |          | 87  |
| SecureRADIUS(RadSec)                               |                                       |         |          | 88  |
|                                                    | RadSecconfiguration                   |         |          | 89  |
|                                                    | Deploymentscenarios                   |         |          | 89  |
|                                                    | ExampleofRadSecconfiguration          |         |          | 90  |
| RADIUSaccounting                                   |                                       |         |          | 91  |
|                                                    | Sampleportaccessaccountinginformation |         |          | 92  |
|                                                    | Samplegeneralaccountinginformation    |         |          | 92  |
|                                                    | RADIUSaccountingtasks                 |         |          | 94  |
| Example:ConfiguringtheswitchforRemoteAAAwithRADIUS |                                       |         |          | 94  |
|                                                    | Prerequisites                         |         |          | 94  |
|                                                    | Procedure                             |         |          | 95  |
| Remote                                             | AAA (TACACS+,                         | RADIUS) | commands | 97  |
| aaaaccountingall-mgmt                              |                                       |         |          | 97  |
| aaaaccountingport-access(RADIUSonly)               |                                       |         |          | 99  |
| aaaauthenticationallow-fail-through                |                                       |         |          | 100 |
| aaaauthenticationlogin                             |                                       |         |          | 101 |
| aaaauthorizationcommands                           |                                       |         |          | 102 |
| aaagroupserver                                     |                                       |         |          | 105 |
| radius-serverauth-type                             |                                       |         |          | 106 |
| radius-serverhost                                  |                                       |         |          | 106 |
| radius-serverhost(ClearPass)                       |                                       |         |          | 109 |
| radius-serverhostsecureipsec                       |                                       |         |          | 110 |
| radius-serverhosttls(RadSec)                       |                                       |         |          | 114 |
| radius-serverkey                                   |                                       |         |          | 116 |
| radius-serverretries                               |                                       |         |          | 117 |
| radius-servertimeout                               |                                       |         |          | 117 |
| radius-servertlstimeout(RadSec)                    |                                       |         |          | 118 |
| radius-servertracking                              |                                       |         |          | 118 |
| server                                             |                                       |         |          | 120 |
| showaaaaccounting                                  |                                       |         |          | 122 |
| showaaaaccountingport-access(RADIUSonly)           |                                       |         |          | 124 |
| showaaaauthentication                              |                                       |         |          | 125 |
| showaaaauthorization                               |                                       |         |          | 127 |
| showaaaserver-groups                               |                                       |         |          | 128 |
| showaccountinglog                                  |                                       |         |          | 130 |
| showaccountinglogport-access                       |                                       |         |          | 133 |
| showradius-server                                  |                                       |         |          | 134 |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 5

| showradius-serversecureipsec       |               | 137 |
| ---------------------------------- | ------------- | --- |
| showradius-serverstatistics        |               | 138 |
| showradius-serverstatisticshost    |               | 139 |
| showtacacs-server                  |               | 140 |
| showtacacs-serverstatistics        |               | 143 |
| showtechaaa                        |               | 144 |
| tacacs-serverauth-type             |               | 147 |
| tacacs-serverhost                  |               | 147 |
| tacacs-serverkey                   |               | 149 |
| tacacs-servertimeout               |               | 150 |
| tacacs-servertracking              |               | 151 |
| RADIUS dynamic                     | authorization | 153 |
| Requirementsandtips                |               | 153 |
| RADIUSdynamicauthorizationcommands |               | 153 |
radiusdyn-authorizationenable 153
radiusdyn-authorizationclient 154
radiusdyn-authorizationclienttls(RadSec) 155
radiusdyn-authorizationport 156
showradiusdyn-authorization 157
showradiusdyn-authorizationclient 158
showradiusdyn-authorizationclienttls(RadSec) 160
| PKI         |     | 162 |
| ----------- | --- | --- |
| PKIconcepts |     | 162 |
Digitalcertificate 162
Certificateauthority 162
Rootcertificate 162
Leafcertificate 163
Intermediatecertificate 163
Trustanchor 163
OCSP 163
| PKIontheswitch |     | 163 |
| -------------- | --- | --- |
Trustanchorprofiles 163
Leafcertificates 164
Mandatorymatchingofpeerdevicehostname 164
| PKIEST |     | 164 |
| ------ | --- | --- |
ESTusageoverview 164
PrerequisitesforusingESTforcertificateenrollment 165
ESTprofileconfiguration 165
Certificateenrollment 165
Certificatere-enrollment 165
CheckingESTprofileandcertificateconfiguration 166
ESTbestpractices 166
| ExampleusingESTforcertificateenrollment           |     | 166 |
| ------------------------------------------------- | --- | --- |
| Exampleincludingtheuseofanintermediatecertificate |     | 172 |
Installingaself-signedleafcertificate(createdinsidetheswitch) 174
Procedure 174
Installingaself-signedleafcertificate(createdoutsidetheswitch) 175
Prerequisites 175
Procedure 175
| InstallingacertificateofarootCA |     | 176 |
| ------------------------------- | --- | --- |
Prerequisites 176
Procedure 176
InstallingaCA-signedleafcertificate(initiatedintheswitch) 177
Prerequisites 177
Contents|6

|     | Procedure |     | 177 |
| --- | --------- | --- | --- |
InstallingaCA-signedleafcertificate(createdoutsidetheswitch) 178
|                                               | Prerequisites                      |          | 178 |
| --------------------------------------------- | ---------------------------------- | -------- | --- |
|                                               | Procedure                          |          | 178 |
| PKIcommands                                   |                                    |          | 179 |
|                                               | cryptopkiapplication               |          | 179 |
|                                               | cryptopkicertificate               |          | 180 |
|                                               | cryptopkita-profile                |          | 181 |
|                                               | enrollself-signed                  |          | 182 |
|                                               | enrollterminal                     |          | 183 |
|                                               | import(CA-signedleafcertificate)   |          | 183 |
|                                               | import(self-signedleafcertificate) |          | 185 |
|                                               | key-type                           |          | 187 |
|                                               | ocspdisable-nonce                  |          | 188 |
|                                               | ocspenforcement-level              |          | 188 |
|                                               | ocspurl                            |          | 189 |
|                                               | ocspvrf                            |          | 190 |
|                                               | revocation-checkocsp               |          | 191 |
|                                               | showcryptopkiapplication           |          | 191 |
|                                               | showcryptopkicertificate           |          | 192 |
|                                               | showcryptopkita-profile            |          | 194 |
|                                               | ta-certificate                     |          | 195 |
|                                               | subject                            |          | 197 |
| PKIESTcommands                                |                                    |          | 198 |
|                                               | arbitrary-label                    |          | 198 |
|                                               | arbitrary-label-enrollment         |          | 199 |
|                                               | arbitrary-label-reenrollment       |          | 200 |
|                                               | cryptopkiest-profile               |          | 201 |
|                                               | enrollest-profile                  |          | 201 |
|                                               | reenrollment-lead-time             |          | 202 |
|                                               | retry-count                        |          | 203 |
|                                               | retry-interval                     |          | 204 |
|                                               | showcryptopkiest-profile           |          | 204 |
|                                               | url                                |          | 205 |
|                                               | username                           |          | 206 |
|                                               | vrf                                |          | 208 |
| Configuring                                   | enhanced                           | security | 209 |
| Configuringenhancedsecurity                   |                                    |          | 209 |
|                                               | Prerequisites                      |          | 209 |
|                                               | Procedure                          |          | 209 |
| passwordcomplexity                            |                                    |          | 210 |
| ConfiguringremoteloggingusingSSHreversetunnel |                                    |          | 213 |
|                                               | Prerequisites                      |          | 213 |
|                                               | Procedure                          |          | 214 |
| CLIusersessionmanagementcommands              |                                    |          | 214 |
|                                               | cli-session                        |          | 214 |
| Captive portal                                | (RADIUS)                           |          | 217 |
| Aboutcaptiveportal(RADIUS)                    |                                    |          | 217 |
| IPv4Captiveportalexampleconfiguration         |                                    |          | 218 |
|                                               | Policyconfiguration                |          | 218 |
|                                               | Captiveportalconfiguration         |          | 218 |
|                                               | Userroleconfiguration              |          | 218 |
| IPv6Captiveportalexampleconfiguration         |                                    |          | 219 |
| Captiveportal(RADIUS)commands                 |                                    |          | 219 |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 7

Port access

Port access general commands

Port access 802.1X authentication

aaa authentication port-access captive-portal-profile
show port-access captive-portal-profile
url
url-hash-key

219
220
222
222

Port access 802.1X authentication commands

aaa authentication port-access auth-mode
aaa authentication port-access auth-precedence
aaa authentication port-access auth-priority
aaa authentication port-access client-limit
aaa authentication port-access (role)
port-access allow-flood-traffic
port-access client-move
port-access fallback-role
port-access log-off client
port-access onboarding-method precedence
port-access onboarding-method concurrent
port-access reauthenticate interface
port-access security violation action
port-access security violation action shutdown auto-recovery
port-access security violation action shutdown recovery-timer
show aaa authentication port-access interface client-status
show port-access clients
show port-access clients detail
show port-access clients onboarding-method
show port-access security violation client-limit-exceeded interface

224
224
224
224
225
226
227
228
228
229
229
230
231
232
233
234
234
235
236
237
241
241
242
243
243
aaa authentication port-access dot1x authenticator
244
aaa authentication port-access dot1x authenticator auth-method
244
aaa authentication port-access dot1x authenticator cached-reauth
245
aaa authentication port-access dot1x authenticator cached-reauth-period
246
aaa authentication port-access dot1x authenticator discovery-period
246
aaa authentication port-access dot1x authenticator eapol-timeout
247
aaa authentication port-access dot1x authenticator max-eapol-requests
248
port-access dot1x authenticator max-retries
248
aaa authentication port-access dot1x authenticator quiet-period
249
aaa authentication port-access dot1x authenticator radius server-group
250
aaa authentication port-access dot1x authenticator reauth
250
aaa authentication port-access dot1x authenticator reauth-period
251
clear dot1x authenticator statistics interface
show aaa authentication port-access dot1x authenticator interface client-status
252
show aaa authentication port-access dot1x authenticator interface port-statistics 253
254
255
255
255
255
256
257
258
258
259
259
260

aaa authentication port-access mac-auth
aaa authentication port-access mac-auth addr-format
aaa authentication port-access mac-auth auth-method
aaa authentication port-access mac-auth cached-reauth
aaa authentication port-access mac-auth cached-reauth-period
aaa authentication port-access mac-auth quiet-period
aaa authentication port-access mac-auth radius server-group
aaa authentication port-access mac-auth reauth

How RADIUS server is used in MAC authentication

Port access MAC authentication commands

How MAC authentication works

Port access MAC authentication

Contents | 8

|     | aaaauthenticationport-accessmac-authreauth-period |     | 261 |
| --- | ------------------------------------------------- | --- | --- |
|     | clearmac-authstatistics                           |     | 261 |
showaaaauthenticationport-accessmac-authinterfaceclient-status 262
showaaaauthenticationport-accessmac-authinterfaceport-statistics 264
| Portaccesspolicy                               |                                                        |               | 265 |
| ---------------------------------------------- | ------------------------------------------------------ | ------------- | --- |
| Classesandactionssupportedbyportaccesspolicies |                                                        |               | 265 |
| Portaccesspolicycommands                       |                                                        |               | 265 |
|                                                | port-accesspolicy                                      |               | 265 |
|                                                | port-accesspolicycopy                                  |               | 269 |
|                                                | port-accesspolicyresequence                            |               | 270 |
|                                                | port-accesspolicyreset                                 |               | 271 |
|                                                | clearport-accesspolicyhitcounts                        |               | 272 |
|                                                | showport-accesspolicy                                  |               | 274 |
|                                                | showport-accesspolicyhitcounts                         |               | 276 |
| Portaccessrole                                 |                                                        |               | 277 |
| Operationalnotes                               |                                                        |               | 278 |
| Downloadableuserroles                          |                                                        |               | 278 |
| Specialroles                                   |                                                        |               | 279 |
|                                                | Criticalrole                                           |               | 279 |
|                                                | Rejectrole                                             |               | 279 |
|                                                | Pre-authenticationrole                                 |               | 279 |
|                                                | Auth-role                                              |               | 280 |
|                                                | Fallbackrole                                           |               | 280 |
| Portaccessrolecommands                         |                                                        |               | 281 |
|                                                | associatecaptive-portal-profile                        |               | 281 |
|                                                | associatepolicy                                        |               | 281 |
|                                                | auth-mode                                              |               | 282 |
|                                                | cached-reauth-period                                   |               | 283 |
|                                                | client-inactivitytimeout                               |               | 283 |
|                                                | description                                            |               | 284 |
|                                                | gateway-zonezonegateway-role                           |               | 285 |
|                                                | mtu                                                    |               | 285 |
|                                                | poe-priority                                           |               | 286 |
|                                                | port-accessrole                                        |               | 286 |
|                                                | reauth-period                                          |               | 287 |
|                                                | sessiontimeout                                         |               | 288 |
|                                                | showaaaauthenticationport-accessinterfaceclient-status |               | 288 |
|                                                | showport-accessrole                                    |               | 289 |
|                                                | stp-admin-edge-port                                    |               | 291 |
|                                                | trust-mode                                             |               | 292 |
|                                                | vlan                                                   |               | 292 |
| PortaccessVLANgroups                           |                                                        |               | 294 |
| VLANgroupinglimitations                        |                                                        |               | 294 |
| VLANgrouploadbalancing                         |                                                        |               | 294 |
| PortaccessVLANgroupcommands                    |                                                        |               | 295 |
|                                                | associate-vlan                                         |               | 295 |
|                                                | port-accessvlan-group                                  |               | 296 |
|                                                | showrunning-configport-accessvlan-group                |               | 297 |
| Configurable                                   | RADIUS attributes                                      | (port access) | 298 |
| ConfigurableRADIUSattributecommands            |                                                        |               | 298 |
| aaaradius-attributegroup                       |                                                        |               | 298 |
| nas-idrequest-type                             |                                                        |               | 299 |
| nas-idvalue                                    |                                                        |               | 299 |
| tunnel-private-group-idrequest-type            |                                                        |               | 300 |
| tunnel-private-group-idvalue                   |                                                        |               | 301 |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 9

| Supported                                 | RADIUS attributes |     | 303 |
| ----------------------------------------- | ----------------- | --- | --- |
| Attributessupportedin802.1Xauthentication |                   |     | 303 |
| AttributessupportedinMACauthentication    |                   |     | 303 |
| Attributessupportedindynamicauthorization |                   |     | 304 |
Sessionauthorizationattributessupportedin802.1XandMACauthentication,andCoA 304
|                                              | Standardsessionattributessupported                       |     | 304 |
| -------------------------------------------- | -------------------------------------------------------- | --- | --- |
|                                              | Vendor-SpecificAttributessupportedinsessionauthorization |     | 305 |
|                                              | DescriptionofVSAs                                        |     | 305 |
| AttributessupportedinRADIUSnetworkaccounting |                                                          |     | 306 |
| AttributessupportedinRADIUSservertracking    |                                                          |     | 307 |
| Port security                                |                                                          |     | 308 |
| Port-securitystickyMAC                       |                                                          |     | 308 |
| Basicoperation                               |                                                          |     | 308 |
|                                              | Defaultportsecurityoperation                             |     | 308 |
|                                              | Intruderprotection                                       |     | 309 |
|                                              | Generaloperationforportsecurity                          |     | 309 |
| Blockingunauthorizedtraffic                  |                                                          |     | 309 |
| Trunkgroupexclusion                          |                                                          |     | 310 |
| Portsecuritycommands                         |                                                          |     | 310 |
|                                              | port-accessport-security                                 |     | 310 |
|                                              | port-accessport-securityclient-limit                     |     | 311 |
|                                              | port-accessport-securitymac-address                      |     | 312 |
|                                              | showport-accessport-securityinterfaceclient-status       |     | 312 |
|                                              | showport-accessport-securityinterfaceport-statistics     |     | 314 |
|                                              | sticky-learnenable                                       |     | 314 |
|                                              | sticky-learnmac                                          |     | 315 |
showport-accesssecurityviolationsticky-mac-client-moveinterface 316
| Fault Monitor             |                                           |     | 318 |
| ------------------------- | ----------------------------------------- | --- | --- |
| Faultmonitoringconditions |                                           |     | 318 |
|                           | Excessiveoversizepackets                  |     | 318 |
|                           | Excessivejabbers                          |     | 318 |
|                           | Excessivefragments                        |     | 318 |
|                           | ExcessiveCRCerrors                        |     | 318 |
|                           | ExcessiveTXdrops                          |     | 318 |
|                           | Excessivelinkflaps                        |     | 318 |
|                           | Excessivebroadcasts                       |     | 318 |
|                           | Excessivemulticasts                       |     | 319 |
|                           | Excessivecollisions                       |     | 319 |
|                           | ExcessiveLateCollisions                   |     | 319 |
| Faultmonitorcommands      |                                           |     | 319 |
|                           | Commandforcreatingafaultmonitoringprofile |     | 319 |
|                           | Commandsforenablinganddisablingthefaults  |     | 320 |
Commandsforapplyingorchangingtheactionandconfiguringauto-enableforafault 321
|     | Commandsforconfiguringthethresholdforthefault    |     | 323 |
| --- | ------------------------------------------------ | --- | --- |
|     | Commandforapplyingafaultmonitoringprofiletoaport |     | 324 |
CommandforconfiguringVSXsynchronizationforafaultmonitoringprofile 325
|                    | showfault-monitorprofile          |       | 325 |
| ------------------ | --------------------------------- | ----- | --- |
|                    | showinterfacefault-monitorprofile |       | 327 |
|                    | showinterfacefault-monitorstatus  |       | 327 |
|                    | showrunning-config                |       | 328 |
|                    | showrunning-configall             |       | 329 |
| Auditors           | and auditing                      | tasks | 331 |
| Auditingtasks(CLI) |                                   |       | 331 |
Contents|10

| Auditingtasks(WebUI)          |                    |           | 331 |
| ----------------------------- | ------------------ | --------- | --- |
| RESTrequestsandaccountinglogs |                    |           | 332 |
| Support                       | and Other          | Resources | 333 |
| AccessingArubaSupport         |                    |           | 333 |
| AccessingUpdates              |                    |           | 333 |
|                               | ArubaSupportPortal |           | 333 |
|                               | MyNetworking       |           | 334 |
| WarrantyInformation           |                    |           | 334 |
| RegulatoryInformation         |                    |           | 334 |
| DocumentationFeedback         |                    |           | 334 |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 11

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

Usage

example-text

Identifies commands and their options and operands, code examples,
filenames, pathnames, and output displayed in a command window. Items that
appear like the example text in the previous column are to be entered exactly
as shown and are required unless enclosed in brackets ([ ]).

example-text

In code and screen examples, indicates text entered by a user.

Any of the following:
n <example-text>
n <example-text>
n example-text

n example-text

|

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables are
enclosed in angle brackets (< >). Substitute the text—including the
enclosing angle brackets—with an actual value.

n For output formats where italic text can be displayed, variables might

or might not be enclosed in angle brackets. Substitute the text
including the enclosing angle brackets, if any, with an actual value.

Vertical bar. A logical OR that separates multiple items from which you can
choose only one.
Any spaces that are on either side of the vertical bar are included for
readability and are not a required part of the command syntax.

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

12

Convention

Usage

{ }

[ ]

… or

...

Braces. Indicates that at least one of the enclosed items is required.

Brackets. Indicates that the enclosed item or items are optional.

Ellipsis:

n In code and screen examples, a vertical or horizontal ellipsis indicates an

omission of information.

n In syntax using brackets and braces, an ellipsis indicates items that can be

repeated. When an item followed by ellipses is enclosed in brackets, zero

or more items can be specified.

About the examples
Examples in this document are representative and might not match your particular switch or environment.

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

In certain configuration contexts, the prompt may include variable information. For example, when in the
VLAN configuration context, a VLAN number appears in the prompt:
switch(config-vlan-100)#

When referring to this context, this document uses the syntax:
switch(config-vlan-<VLAN-ID>)#

Where <VLAN-ID> is a variable representing the VLAN number.

Identifying switch ports and interfaces
Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 6200 Switch Series

About this document | 13

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

Identifying modular switch components

n Power supplies are on the front of the switch behind the bezel above the management modules. Power

supplies are labeled in software in the format: member/power supply:

o member: 1.

o power supply: 1 to 4.

n Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

o member: 1.

o tray: 1 to 4.

o fan: 1 to 4.

n Fabric modules are not labeled on the switch but are labeled in software in the format: member/module:

o member: 1.

o member: 1 or 2.

n The display module on the rear of the switch is not labeled with a member or slot number.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

14

Chapter 2

About security

About security

This AOS-CX Switch provides the following security features:

n Local user and group management.

n Authentication, Authorization, and Accounting (AAA), either local (password or SSH public key-based), or

remote password-based TACACS+ or RADIUS.

n SSH server. SSH is a cryptographic protocol that encrypts all communication between devices.

n Ability to use enhanced security as described in Configuring enhanced security .

n Making sensitive switch configuration information available for secure export/import between switches.

For information, see service export-password.

About Authentication, Authorization, and Accounting (AAA)

n Authentication: identifies users, validates their credentials, and grants switch access.

n Authorization: controls authenticated users command execution and switch interaction privileges.

n Accounting: collects and manages user session activity logs for auditing and reporting purposes.

Local AAA on your Aruba switch provides:

n Authentication using local password or SSH public key.

n Authorization using role-based access control (RBAC), and optionally, using user-defined local user groups

with command authorization rules defined per group.

n Accounting of user activity on the switch using accounting logs.

Remote AAA provides the following for your Aruba switch:

n Authentication using remote AAA servers with either TACACS+ or RADIUS.

n Authorization using remote AAA servers with TACACS+ fine-grained command authorization. Local RBAC

or local rule-based authorization is also possible.

n Transmission of locally collected accounting information to remote TACACS+ and RADIUS servers.

TACACS+ (Terminal Access Controller Access-Control System Plus) and RADIUS (Remote Authentication Dial-In

User Service) server software is readily available as either open source or from various vendors.

For switches that support multiple management modules such as the Aruba 8400, all AAA functionality discussed

only applies to the active management module. See also AAA on switches with multiple management modules in the

High Availability Guide.

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

15

Chapter 3
|          |       |           |        | Managing |     | local users | and groups |
| -------- | ----- | --------- | ------ | -------- | --- | ----------- | ---------- |
| Managing | local | users and | groups |          |     |             |            |
| Default  | user  | admin     |        |          |     |             |            |
Afactory-defaultswitchcomeswithasingleusernamedadmin.
Theadminuser:
Hasanemptypassword.PressEnterinresponsetotheadminpasswordprompt.Atinitialboot,youare
n
promptedtodefineapasswordfortheadminuser.Althoughempty(blank)passwordsareallowed,itis
recommendedthatyouusestrongpasswordsforallproductionswitches.
n Isamemberoftheadministratorsgroup.
n Cannotberemovedfromtheswitch.
TheswitchadminuserisdistinctfromtheServiceOSadminuser.TheServiceOSactsasthebootloaderand
recoveryoperatingsystem.TheServiceOShasitsownCLI.
| Example | of first | login | with password |     | setting |     |     |
| ------- | -------- | ----- | ------------- | --- | ------- | --- | --- |
| switch  | login:   | admin |               |     |         |     |     |
Password:
| Please  | configure     | the 'admin' | user account | password. |     |     |     |
| ------- | ------------- | ----------- | ------------ | --------- | --- | --- | --- |
| Enter   | new password: | ********    |              |           |     |     |     |
| Confirm | new password: | ********    |              |           |     |     |     |
switch#
| Built-in | user | groups | and their |     | privileges |     |     |
| -------- | ---- | ------ | --------- | --- | ---------- | --- | --- |
Theswitchprovidesthefollowingbuilt-inusergroupswithcorrespondingroles.Eachoftheserolescomes
withasetofprivileges.
| Group/Role |     | Privileges |     |     |     |     |     |
| ---------- | --- | ---------- | --- | --- | --- | --- | --- |
administrators
Administratorshavefullprivileges,including:
FullCLIaccess.
n
|     |     | n Performingfirmwareupgrades. |     |     |     |     |     |
| --- | --- | ----------------------------- | --- | --- | --- | --- | --- |
n Viewingswitchconfigurationinformation,includingsensitiveinformationsuchas
passwordswhicharedisplayedasciphertext.
|     |     | n Performingswitchconfiguration. |     |     |     |     |     |
| --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
Adding/removinguseraccounts.
n
n Configuringusersaccounts,includingpasswords.Onceset,apasswordcannotbe
deletedorsettoempty.
16
| AOS-CX10.07SecurityGuide| | (6200,6300,6400SwitchSeries) |     |     |     |     |     |     |
| ------------------------- | ---------------------------- | --- | --- | --- | --- | --- | --- |

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
n REST API: POST method available for the \login and \logout resources. GET method

available for the following resources only:

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
<USERNAME>

Specifies the user name. Requirements:

n Must start with a lowercase letter.

n Can contain numbers and lowercase letters.

n Can include only these three special characters: hyphens ( - ), dots ( . ), and underscores ( _ ).

n Can have a maximum of 32 characters.

n Cannot be empty.

n Cannot contain uppercase letters.

n Cannot be: admin, root, or remote_user.

n Cannot be Linux reserved names such as:

daemon, bin, sys, sync, proxy, www-data, backup, list, irc, gnats, nobody, systemd-bus-proxy, sshd,
messagebus, rpc, systemd-journal-gateway, systemd-journal-remote, systemd-journal-upload,

Managing local users and groups | 17

systemd-timesync,systemd-coredump,systemd-resolve,rpcuser,vagrant,opsd,rdanet,_lldpd,
rdaadmin,rdaweb,docker_container,tss.
| Password | requirements |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- |
Passwordsmust:
ContainonlyASCIIcharactersfromhexadecimal21tohexadecimal7E[\x21-\x7E](decimal33to126).
n
Spacesarenotallowed.Whenthepasswordisentereddirectlywithoutprompting,the"?"symbol
(hexadecimal3F[\x3F](decimal63))isnotpermitted.
n Containatmost32characters.
Containatleastthenumberofcharactersconfigured(optionally)forminimum-password-length.
n
Althoughemptypasswordsaresupported,itisrecommendedthatyouusestrongpasswordsforallproduction
switches.
Onlyanadministratorcanchangethepasswordofauserassignedtotheoperatorsrole.
| User and | user group | management | tasks |     |     |
| -------- | ---------- | ---------- | ----- | --- | --- |
Userandusergroupmanagementcommontasksareasfollows:
| Task          | Commandorprocedure |     | Example    |                      |          |
| ------------- | ------------------ | --- | ---------- | -------------------- | -------- |
| Creatingauser | user               |     | user jamie | group administrators | password |
| Changingauser | user password      |     | user jamie | password             |          |
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
| Showingalistofallusers | show user-list |     | show user-list |     |     |
| ---------------------- | -------------- | --- | -------------- | --- | --- |
Showinginformationfor show user information show user information
thelogged-inuser
| Creatingausergroup | user-group |     | user-group | admuser2 |     |
| ------------------ | ---------- | --- | ---------- | -------- | --- |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 18

| Task          |     | Commandorprocedure |     |     | Example |             |           |     |
| ------------- | --- | ------------------ | --- | --- | ------- | ----------- | --------- | --- |
| Addingcommand |     |                    |     |     | 10 deny | cli command | "show aaa | .*" |
permitordeny(within
|                       |     |             |     |     | 20 permit | cli command | "show .*" |     |
| --------------------- | --- | ----------- | --- | --- | --------- | ----------- | --------- | --- |
| authorizationrulestoa |     | user-group) |     |     |           |             |           |     |
usergroup
Addingcommentsto comment(withinuser- 10 comment Deny all show aaa commands.
| rulesinausergroup |     |     |     |     | 20 comment | Permit all | other show | commands. |
| ----------------- | --- | --- | --- | --- | ---------- | ---------- | ---------- | --------- |
group)
Resequencingrulesina resequence(withinuser- resequence 100 20
usergroup
group)
| Showingalistofalluser |     | show | user-group |     | show user-group |     |     |     |
| --------------------- | --- | ---- | ---------- | --- | --------------- | --- | --- | --- |
groups
| Resetting | the | switch | admin | password |     | using | the Service | OS  |
| --------- | --- | ------ | ----- | -------- | --- | ----- | ----------- | --- |
console
Performthistaskonlywhentheswitch(ProductOS)adminuserpasswordhasbeenforgotten.
Prerequisites
n Youareconnectedtotheswitchthroughtheconsoleport.
YouknowtheServiceOSpassword(ifconfigured).
n
IfyouforgettheServiceOSpassword,theonlyrecourseistozerioizetheswitch,revertingittofactorydefaults.
Formoreinformation,seeZeroizationintheDiagnosticsandSupportabilityGuide.
Procedure
1. Reboottheswitch.
| 2.  | Atthebootprompt,select0. |            | Service               | OS Console. |     |     |     |     |
| --- | ------------------------ | ---------- | --------------------- | ----------- | --- | --- | --- | --- |
|     | 0. Service               | OS Console |                       |             |     |     |     |     |
|     | 1. Primary               | Software   | Image [XL.01.01.0001] |             |     |     |     |     |
|     | 2. Secondary             | Software   | Image [XL.01.01.0002] |             |     |     |     |     |
3. AttheSwitch Loginprompt,enteradminandpressEnter.IfpromptedforaServiceOSpassword,
enteritandpressEnter.
|     | Switch login: | admin              |     |     |     |     |     |     |
| --- | ------------- | ------------------ | --- | --- | --- | --- | --- | --- |
|     | Password:     | **********         |     |     |     |     |     |     |
|     | Hewlett       | Packard Enterprise |     |     |     |     |     |     |
SVOS>
4. AttheSVOS>prompt,enterpasswordandpressEnter.
5. Enterthenewswitch(ProductOS)passwordatbothpasswordprompts.
Managinglocalusersandgroups|19

SVOS> password
Enter password:
************
| Confirm | password: | ************ |     |     |     |     |
| ------- | --------- | ------------ | --- | --- | --- | --- |
SVOS>
6. EnterbootandpressEnter.
SVOS> boot
ServiceOS Information:
|     | Version:    | **.10.06.0001                                    |          |     |     |     |
| --- | ----------- | ------------------------------------------------ | -------- | --- | --- | --- |
|     | Build Date: | 2020-12-01                                       | 14:52:31 | PDT |     |     |
|     | Build ID:   | ServiceOS:**.01.01.0001:461519208911:20180301452 |          |     |     |     |
SHA: 46151920891195cdb2267ea6889a3c6cbc3d4193
Boot Profiles:
| 0.  | Service OS       | Console        |                 |     |     |     |
| --- | ---------------- | -------------- | --------------- | --- | --- | --- |
| 1.  | Primary Software | Image          | [**.10.06.0001] |     |     |     |
| 2.  | Secondary        | Software Image | [**.10.06.0001] |     |     |     |
Select profile(primary):
7. Tobootwiththeprimaryswitchimagepress1andthenEnter.Tobootwiththesecondaryswitch
image,press2andthenEnter.Ifyoumakenoselectionforapproximately10seconds,theswitch
bootsthedefaultimage.ThedefaultisshowninparenthesestotherightofSelect profile,for
| example:Select | profile(primary):. |     |     |     |     |     |
| -------------- | ------------------ | --- | --- | --- | --- | --- |
8. OnceinAOS-CX,savetheconfigurationtomaketheadminloginuseraccountpasswordsetting
persistent.
| Resetting | the      | admin | password | by reverting | the switch | to  |
| --------- | -------- | ----- | -------- | ------------ | ---------- | --- |
| factory   | defaults |       |          |              |            |     |
Thistaskerasesallswitchconfiguration,revertingtheswitchtoitsfactorydefaultstate.Considerusingotherless-
impactingtechniquesforadminpasswordreset.Forexample,anotheradministratorusercanresettheadminuser
passwordtoaknownvalue.SeealsoResettingtheswitchadminpasswordusingtheServiceOSconsole.
Prerequisites
Ifwanted,youhavesavedacopyoftheswitchconfiguration.
Procedure
| 1. Atthemanagercommandprompt,entererase |       |                |     | startup-config. |     |     |
| --------------------------------------- | ----- | -------------- | --- | --------------- | --- | --- |
| switch#                                 | erase | startup-config |     |                 |     |     |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 20

2. Enter boot system, responding n to the Do you want to save the current configuration prompt

and then responding y to the Continue prompt.

switch# boot system
Do you want to save the current configuration (y/n)? n

This will reboot the entire switch and render it unavailable
until the process is complete.
Continue (y/n)? y
The system is going down for reboot.

3. At the login prompt, enter admin and press Enter. The admin password remains empty until it is set.

User and group commands

user

Syntax

user <USERNAME> group {administrators | operators | auditors | <USER-GROUP>}

password [ciphertext <CIPHERTEXT-PASSWORD> | plaintext <PLAINTEXT-PASSWORD>]

no user <USERNAME>

Description

Creates a user and adds the user to one of the user groups. Users are given the privileges of their group. For
the three built-in user groups (administrators, operators, auditors), the privileges are fixed. For user-
defined local user groups, the privileges are defined by the CLI command authorization rules of the group.

When entered without either optional ciphertext or plaintext parameters, the cleartext password is
prompted for twice, with the characters entered masked with "*" symbols.

The no form of this command removes a user account from the switch. The administrator cannot delete the
user account from which they are logged in. The admin user cannot be deleted.

Command context

config

Parameters

<USERNAME>

Specifies the user name. Requirements:

n Must start with a lowercase letter.

n Can contain numbers and lowercase letters.

n Can include only these three special characters: hyphens ( - ), dots ( . ), and underscores ( _ ).

n Can have a maximum of 32 characters.

n Cannot be empty.

n Cannot contain uppercase letters.

n Cannot be: admin, root, or remote_user.

n Cannot be Linux reserved names such as:

daemon, bin, sys, sync, proxy, www-data, backup, list, irc, gnats, nobody, systemd-bus-proxy, sshd,
messagebus, rpc, systemd-journal-gateway, systemd-journal-remote, systemd-journal-upload,

Managing local users and groups | 21

systemd-timesync, systemd-coredump, systemd-resolve, rpcuser, vagrant, opsd, rdanet, _lldpd,
rdaadmin, rdaweb, docker_container, tss.

group

Selects the local user group to which the new user will be assigned.

administrators | operators | auditors

Selects one of three built-in local user groups.

<USER-GROUP>

Specifies an existing user-defined local user group.

ciphertext <CIPHERTEXT-PASSWORD>

Specifies a ciphertext password. No password prompts are provided and the ciphertext password is
validated before the configuration is applied for the user. The variable <CIPHERTEXT-PASSWORD> is Base64
and is typically copied from another switch using the show running-config command output and then
pasted into this command.

The administrator cannot construct ciphertext passwords themselves. The ciphertext is only created by an
AOS-CX switch. The ciphertext is created by setting a password for a user with the user command. The
ciphertext is available for copying from the show running-config output and pasting into the configuration
on any other AOS-CX switch. The target switch must have the same export password (default or otherwise) as
the source switch.

plaintext <PLAINTEXT-PASSWORD>

Specifies the password without prompting. The password is visible as cleartext when entered but is
encrypted thereafter. Command history does show the password as cleartext.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n Up to 63 local users can be added, for a total of 64 users including the default user admin. A user can

belong to only one group.

n The switch ships with the admin user account and three built-in local user groups: administrators,

operators, and auditors. The admin account belongs to the administrators group. The Service OS also
includes the administrator user admin. The two admin users are entirely distinct.

n When a local user account is removed, the user loses all active login/SSH sessions. Any calls on the

existing REST session with that local user account fail with a permissions issue as soon as the user is
deleted. Soon afterwards, the existing REST sessions with the deleted local user account become
invalidated. If a user is viewing the GUI while their account is deleted, the user is redirected to the login
page within 60 seconds. The home directory associated with the user is also removed from the switch.

n Cleartext passwords (whether entered with prompting or entered directly) must:

o Contain only ASCII characters from hexadecimal 21 to hexadecimal 7E [\x21-\x7E] (decimal 33 to
126). Spaces are not allowed. When the password is entered directly without prompting, the "?"
symbol (hexadecimal 3F [\x3F] (decimal 63)) is not permitted.

o Contain at most 32 characters.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

22

o Containatleastthenumberofcharactersconfigured(optionally)forminimum-password-length.
Althoughemptypasswordsaresupported,itisrecommendedthatyouusestrongpasswordsfor
allproductionswitches.
Onlyanadministratorcanchangethepasswordofauserassignedtotheoperatorsrole.
Examples
Creatinglocaluserjamieintheadministratorsgroupwithapromptedpassword:
| switch(config)# | user  | jamie group administrators | password |     |
| --------------- | ----- | -------------------------- | -------- | --- |
| Adding user     | jamie |                            |          |     |
Enter password:************
| Confirm password:************ |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- |
Creatinguserchrisintheexistinguser-definedlocalusergroupadmuser2withacleartextpassword,using
directentrywithoutprompting:
switch(config)# user chris group admuser2 password plaintext passWORDxJ|989
Creatinguseralexintheoperatorsgroupwithaciphertextpassword(theciphertextshownisa
placeholderthatmustbereplacedwithactualciphertext):
switch(config)# user alex group operators password ciphertext NDcDI2...8igJfA=
Removinguserjamie:
| switch(config)# | no user        | jamie      |               |             |
| --------------- | -------------- | ---------- | ------------- | ----------- |
| User jamie's    | home directory | and active | sessions will | be deleted. |
| Do you want     | to continue    | [y/n]?y    |               |             |
user-group
Syntax
user-group <GROUP-NAME>
| no user-group | <GROUP-NAME> |     |     |     |
| ------------- | ------------ | --- | --- | --- |
Description
If<GROUP-NAME>doesnotexist,thiscommandcreatesalocalusergroupandthenentersitscontext.If
<GROUP-NAME>exists,thiscommandentersthecontextforthespecified<GROUP-NAME>.Withinthe<GROUP-
NAME>context,severalsubcommandsareavailableforworkingwithrulesthatspecifywhatCLIcommands
arepermittedordeniedforallmembersofthelocalgroup.
Inadditiontothethreebuilt-inusergroupsadministrators,operators,andauditors,upto29user-
definedlocalusergroupscanbedefined.Alluserscanbemembersofonlyoneoftheupto32groups.
Managinglocalusersandgroups|23

The no form of this command deletes the specified user group. All members of the deleted group lose all
command authorization privilege.

Do not causally delete user-defined local user groups without understanding the implications. Although user-

defined local user groups can be deleted with the respective members losing all privileges, the three built-in
groups administrators, operators, and auditors are always available and their privileges are unchangeable.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Subcommands

These subcommands are available within the user-defined local user group context (shown in the switch
prompt as config-usr-grp-<GROUP-NAME>).
[<SEQ-NUM>] {permit | deny} cli command "<REGEX>"
no <SEQ-NUM>

Defines a CLI command privilege permit or deny rule. There is an implicit "deny .*" rule at the end of
every user-defined group rule list. Members of a user-defined group without any permit rules have no
CLI command privileges.

The no form of this subcommand deletes the specified (by sequence number) rule from the group.

Rule evaluation proceeds from lowest to highest sequence number until the first successful match, resulting in
either CLI command permission or denial. Rule evaluation ceases upon first match. Therefore, rules for related

CLI commands must be defined in most restrictive to least restrictive order.

<SEQ-NUM>

Specifies the CLI command rule sequence number. When omitted, a sequence number that is 10 greater
the highest existing sequence number is auto-assigned. When no rules exist, the first auto-assigned
sequence number is 10.

{permit | deny}

Sets the rule type as either permit or deny. Rule order is important. For example, these two related rules
together authorize all show commands except for the show aaa commands.

switch(config-usr-grp-admuser2)#10 deny cli command "show aaa .*"
switch(config-usr-grp-admuser2)#20 permit cli command "show .*"

To achieve the wanted effect in this example, the deny rule must precede the permit rule. These two
rules together achieve the following:

n All show aaa commands match on rule 10, triggering command denial, and the immediate cessation of

further rule evaluation. Matching on rule 20 is never attempted.

n All other show commands (excluding show aaa commands) match on rule 20 and are therefore

permitted.

<REGEX>

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

24

SpecifiestheCLIcommandmatchingcriteriaoftherule.Thecriteriacanbeexpressedas".*"which
matchesallcommands.Otherwise,thecriteriaisexpressedasaPOSIX-compliantregularexpression
(regex)stringstartingwithanexactmatchcommandtoken(forexampleshow)followedbyaregex
representingcommandarguments.Thefirstwordmustbeastringthatcontainsonlyalphanumericor
hyphencharacters.
Forexample,toallowallcommandsstartingwiththewordinterface,theregexmustbe"interface .*"
orjust"interface".Using"interface.*"(withoutthespace)isnotsupported.Forexample,"show .*"
matcheseveryshowcommand.ConsulttheExtendedregularexpressioninformationavailableat:
https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_04.
Sample matchedCLI
| Sample | matching | criteria |     |     |     |     | Matches |
| ------ | -------- | -------- | --- | --- | --- | --- | ------- |
commandorspecifier
| show         | .*             |               | show      | accounting |       | log     | Allshowcommands            |
| ------------ | -------------- | ------------- | --------- | ---------- | ----- | ------- | -------------------------- |
| bgp          | .*             |               | bgp       | router-id  |       | 1.1.1.1 | Allbgpcommands             |
| interface    | .*             |               | interface |            | 1/1/1 |         | Allinterfacespecifiers     |
| vlan         | (3|4)          |               | vlan      | 3          |       |         | VLAN3or4                   |
| vlan         | [1-9]          |               | vlan      | 5          |       |         | AsingleVLANintherange1to9  |
| vlan         | ([1-9]|1[0-9]) |               | vlan      | 19         |       |         | AsingleVLANintherange1to19 |
| [<SEQ-NUM>]  | comment        | <TEXT-STRING> |           |            |       |         |                            |
| no <SEQ-NUM> | comment        |               |           |            |       |         |                            |
Addsacommenttoanexistingrule.Thenoformofthissubcommandremovesanexistingcomment.
switch(config-usr-grp-admuser2)# 10 comment Deny all show aaa commands.
switch(config-usr-grp-admuser2)# 20 comment Permit all other show commands.
switch(config-usr-grp-admuser2)#
switch(config-usr-grp-admuser2)#
|            |              |             |           |              | show           | running-config | current-context |
| ---------- | ------------ | ----------- | --------- | ------------ | -------------- | -------------- | --------------- |
| user-group |              | admuser2    |           |              |                |                |                 |
|            | 10 comment   | Deny all    | show      | aaa          | commands.      |                |                 |
|            | 10 deny      | cli command | "show     | aaa          | .*"            |                |                 |
|            | 20 comment   | Permit      | all other |              | show commands. |                |                 |
|            | 20 permit    | cli command | "show     |              | .*"            |                |                 |
| include    | <GROUP-NAME> | [no]        | include   | <GROUP-NAME> |                |                |                 |
Includeallrulesfromthespecifieduser-defined<GROUP-NAME>.Onlyonegroupcanbeincludedinthe
definitionofanothergroup.Thecontentoftheincludedgroupiseffectivelyplacedatthetopofthe
ruleslistinthecurrentgroup.Ifthespecified<GROUP-NAME>doesnotexist,itiscreated.
Thenoformofthissubcommandremovesthespecifiedincludedgroupfromthecurrentgroup.The
specifiedincludedgroupmustexistandmustbeincludedinthecurrentgrouporelseanerrormessage
isshown.
Thenameoftheincludedgroupisshownatthetopoftheshow user-groupcommandforthegroup
withtheinclude.
Inthisexample,groupadmuser1isincludedingroupadmuser2.Sotheadmuser1rulesareevaluatedfirst
andthentherulesintheadmuser2groupareonlyevaluatedifnoCLIcommandmatchoccursforthe
rulesingroupadmuser1.
Managinglocalusersandgroups|25

| switch(config-usr-grp-admuser2)# |     |     |     | include |     | admuser1 |     |     |
| -------------------------------- | --- | --- | --- | ------- | --- | -------- | --- | --- |
switch(config-usr-grp-admuser2)#
|      |       |         |     | show | user-group | admuser2 |     |     |
| ---- | ----- | ------- | --- | ---- | ---------- | -------- | --- | --- |
| User | Group | Summary |     |      |            |          |     |     |
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
------------- ---------- ----------------------------- -----------------------------
---
| 10  |     | deny   | show | aaa | .*  |     | Deny all   | show aaa commands. |
| --- | --- | ------ | ---- | --- | --- | --- | ---------- | ------------------ |
| 20  |     | permit | show | .*  |     |     | Permit all | other show         |
commands.
| resequence | [<STARTING-SEQ-NUM> |     |     | <INCREMENT>] |     |     |     |     |
| ---------- | ------------------- | --- | --- | ------------ | --- | --- | --- | --- |
ResequencestheCLIcommandauthorizationrules.Whenenteredwithouttheoptionalparametersthe
rulesareresequencedwitha<STARTING-SEQ-NUM>of10andan<INCREMENT>of10.
<STARTING-SEQ-NUM>
Specifiesthestartingsequencenumber.
<INCREMENT>
Specifiesthesequencenumberincrement.
Resequencingtherulestostartat100withanincrementof20:
| switch(config-usr-grp-admuser2)# |     |     |     | resequence |     | 100 20 |     |     |
| -------------------------------- | --- | --- | --- | ---------- | --- | ------ | --- | --- |
switch(config-usr-grp-admuser2)# show running-config current-context
| user-group |             | admuser2    |       |            |           |     |     |     |
| ---------- | ----------- | ----------- | ----- | ---------- | --------- | --- | --- | --- |
|            | 100 comment | Deny all    | show  | aaa        | commands. |     |     |     |
|            | 100 deny    | cli command | "show | aaa        | .*"       |     |     |     |
|            | 120 comment | Permit      | all   | other show | commands. |     |     |     |
|            | 120 permit  | cli command |       | "show .*"  |           |     |     |     |
Resequencingtherulestothedefaultofstartingat10withanincrementof10:
| switch(config-usr-grp-admuser2)# |     |     |     | resequence |     |     |     |     |
| -------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
switch(config-usr-grp-admuser2)# show running-config current-context
| user-group |                | admuser2        |           |               |           |     |     |     |
| ---------- | -------------- | --------------- | --------- | ------------- | --------- | --- | --- | --- |
|            | 10 comment     | Deny all        | show      | aaa commands. |           |     |     |     |
|            | 10 deny        | cli command     | "show     | aaa           | .*"       |     |     |     |
|            | 20 comment     | Permit          | all other | show          | commands. |     |     |     |
|            | 20 permit      | cli command     | "show     | .*"           |           |     |     |     |
| show       | running-config | current-context |           |               |           |     |     |     |
Showsallthecommandsusedtoconfiguretherulesinthecurrentgroupcontext.
switch(config-usr-grp-admuser2)# show running-config current-context
| user-group |            | admuser2    |           |               |           |     |     |     |
| ---------- | ---------- | ----------- | --------- | ------------- | --------- | --- | --- | --- |
|            | 10 comment | Deny all    | show      | aaa commands. |           |     |     |     |
|            | 10 deny    | cli command | "show     | aaa           | .*"       |     |     |     |
|            | 20 comment | Permit      | all other | show          | commands. |     |     |     |
|            | 20 permit  | cli command | "show     | .*"           |           |     |     |     |
list
Listthesubcommandsavailablewithintheuser-definedgroupcontext.
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 26

exit

Exits the user-defined group context.

end

Exits the user-defined group context and then the config context.

user password

Syntax

user <USERNAME> password [ciphertext <CIPHERTEXT-PASSWORD> | plaintext <PLAINTEXT-PASSWORD>]

Description

Changes a password for an account or enables the password for the admin account. When entered without
either optional ciphertext or plaintext parameters, the cleartext password is prompted for twice, with the
characters entered masked with "*" symbols.

Command context

config

Parameters

<USERNAME>

Specifies the corresponding user name for the password you want to change.
ciphertext <CIPHERTEXT-PASSWORD>

Specifies a ciphertext password. No password prompts are provided and the ciphertext password is
validated before the configuration is applied for the user. The variable <CIPHERTEXT-PASSWORD> is
Base64 and is typically copied from another switch using the show running-config command output
and then pasted into this command.

The administrator cannot construct ciphertext passwords themselves. The ciphertext is only created by an
AOS-CX switch. The ciphertext is created by setting a password for a user with the user command. The
ciphertext is available for copying from the show running-config output and pasting into the configuration
on any other AOS-CX switch. The target switch must have the same export password (default or otherwise) as

the source switch.

plaintext <PLAINTEXT-PASSWORD>

Specifies the password without prompting. The password is visible as cleartext when entered but is
encrypted thereafter. Command history does show the password as cleartext.

Authority

Administrators or local user group members with execution rights for this command.

Usage

The admin account is available on the switch without a password by default.

Cleartext passwords (whether entered with prompting or entered directly) must:

n Contain only ASCII characters from hexadecimal 21 to hexadecimal 7E [\x21-\x7E] (decimal 33 to 126).
Spaces are not allowed. When the password is entered directly without prompting, the "?" symbol
(hexadecimal 3F [\x3F] (decimal 63)) is not permitted.

n Contain at most 32 characters.

Managing local users and groups | 27

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

switch(config)# user alex password ciphertext XqYJ36...W83D4Y=

service export-password

Syntax

service export-password
no service export-password

Description

Configures a nondefault export password. The export password is used to transform critical security
parameters (such as password hashes) into ciphertext suitable for exporting and showing by commands
such as show running-config. This transformation enables safe switch configuration import and export.

The no form of this command reverts the export password to its factory default.

All factory-default switches have identical default export passwords. For security, it is recommended that you set

the same nondefault export password on every switch in a group that will exchange configuration information.

Only switches with identical export passwords can exchange configuration information.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

28

Usage

Prompts you twice for the new export password.

The export password must:

n Contain only ASCII characters from hexadecimal 21 to hexadecimal 7E [\x21-\x7E] (decimal 33 to 126).

Spaces are not allowed.

n Contain at most 32 characters.

n Not be blank.

Examples

Configuring a new export password:

switch(config)# service export-password
Enter password:************
Confirm password:************

Reverting the export password to its factory default:

switch(config)# no service export-password

show user-group

Syntax

show user-group [<GROUP-NAME>] [vsx-peer]

Description

Shows user group information for the built-in groups plus any user-defined local user groups. When entered
without <GROUP-NAME>, summary information is shown for all groups.

Command context

Manager (#)

Parameters

<GROUP-NAME>

Narrows the show command output to that of the specified group, and for local user groups, adds the
User Group Rules list.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Show the list of all user groups, including built-in groups and local user groups.

Managing local users and groups | 29

| switch# show | user-group |                |        |          |     |
| ------------ | ---------- | -------------- | ------ | -------- | --- |
| GROUP NAME   | GROUP TYPE | INCLUDED GROUP | NUMBER | OF RULES |     |
-------------- -------------- ----------------- -------------------
| administrators | built-in      | n/a      | n/a |     |     |
| -------------- | ------------- | -------- | --- | --- | --- |
| admuser1       | configuration | --       | 5   |     |     |
| admuser2       | configuration | admuser1 | 2   |     |     |
| auditors       | built-in      | n/a      | n/a |     |     |
| operators      | built-in      | n/a      | n/a |     |     |
Showdetailedinformationforlocalusergroupadmuser2.
| switch(config-usr-grp-admuser2)# |         | show user-group | admuser2 |     |     |
| -------------------------------- | ------- | --------------- | -------- | --- | --- |
| User Group                       | Summary |                 |          |     |     |
==================
| Name            | : admuser2      |     |     |     |     |
| --------------- | --------------- | --- | --- | --- | --- |
| Type            | : configuration |     |     |     |     |
| Included Group  | : admuser1      |     |     |     |     |
| Number of Rules | : 2             |     |     |     |     |
| User Group      | Rules           |     |     |     |     |
================
| SEQUENCE NUM | ACTION | COMMAND |     | COMMENT |     |
| ------------ | ------ | ------- | --- | ------- | --- |
------------- ---------- ----------------------------- -----------------------------
---
| 10  | deny   | show aaa .* |     | Deny all show | aaa commands. |
| --- | ------ | ----------- | --- | ------------- | ------------- |
| 20  | permit | show .*     |     | Permit all    | other show    |
commands.
| show user | information |     |     |     |     |
| --------- | ----------- | --- | --- | --- | --- |
Syntax
show user information
Description
Showsthefollowinginformationforthelogged-inuser:
Username.
n
n Userauthenticationtype:local,RADIUS,orTACACS+.
n Usergroup:administrators,operators,or<GROUP-NAME>.
n Userprivilegelevel:Forthebuilt-inusergroupsandRADIUSorTACACS+,theroleprivilegelevelvalueis
shown.Foruser-definedusergroups,N/Aisshown.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showinginformationfortheadminuser:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 30

switch# show user information
Username
: admin
Authentication type : Local
User group
User privilege level : 15

: administrators

Showing information for a member of the user-defined local user group admuser2:

switch# show user information
Username
Authentication type : Local
User group
User privilege level : N/A

: admuser2

: admin2-b

Showing information for a member of operators:

switch# show user information
Username
Authentication type : Local
User group
User privilege level : 1

: operator

: operators

Showing information for remote RADIUS user rad_user1 mapped to local user group administrators:

switch# show user information
Username
Authentication type : RADIUS
User group
User privilege level : 15

: rad_user1

: administrators

Showing information for remote RADIUS user rad_user2 mapped to local user group operators:

switch# show user information
Username
Authentication type : RADIUS
User group
User privilege level : 1

: operators

: rad_user2

Showing information for remote TACACS+ tac_user1 logged in with priv-lvl 15 (mapped to user group
administrators):

switch# show user information
Username
Authentication type : TACACS+
User group
User privilege level : 15

: tac_user1

: administrators

show user-list

Syntax

show user-list [vsx-peer]

Description

Managing local users and groups | 31

Shows all configured users and their corresponding group names.

Command context

Manager (#)

Parameters

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Administrators or local user group members with execution rights for this command.

Examples

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

administrators
operators
auditors
admuser1

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

32

admin2-a
admin2-b

admuser2
admuser2

Managing local users and groups | 33

Chapter 4
SSH server
SSH server
SSH(SecureShell)isacryptographicprotocolthatencryptsallcommunicationbetweendevices.
EachswitchVRFincludesanSSHserver.TheSSHserveronthemgmtVRFisenabledbydefaultinsoftware
version10.02andhigher,anddisabledinversion10.01andlower.OnlytheSSHserversincludedinthe
switcharesupported.
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
| Task                 | Commandname |     | Example    |             |
| -------------------- | ----------- | --- | ---------- | ----------- |
| EnablingtheSSHserver | ssh server  | vrf | ssh server | vrf default |
34
AOS-CX10.07SecurityGuide| (6200,6300,6400SwitchSeries)

| Task | Commandname |     | Example |     |     |
| ---- | ----------- | --- | ------- | --- | --- |
DisablingtheSSHserver no ssh server vrf no ssh server vrf default
| GeneratinganSSHhost- | ssh host-key |     | ssh host-key | rsa bits 2048 |     |
| -------------------- | ------------ | --- | ------------ | ------------- | --- |
keypair
Clearingthelistoftrusted ssh known-host ssh known-host remove 1.1.1.1
| SSHserversforyouruser | remove |     |     |     |     |
| --------------------- | ------ | --- | --- | --- | --- |
account
ConfiguringSSHtousea ssh ciphers ssh ciphers chacha20-poly1305@openssh.com
| setofciphers |     |     | aes256-ctr | aes256-cbc |     |
| ------------ | --- | --- | ---------- | ---------- | --- |
ConfiguringSSHtousea ssh host-key- ssh host-key-algorithms ssh-rsa ssh-ed25519
| setofhostkeyalgorithms | algorithms |     | ecdsa-sha2-nistp521 |     |     |
| ---------------------- | ---------- | --- | ------------------- | --- | --- |
ConfiguringSSHtousea ssh macs ssh macs hmac-sha2-256 hmac-sha2-512
setofMACs
ConfiguringSSHtousea ssh key-exchange- ssh key-exchange-algorithms ecdh-sha2-
| setofkeyexchange | algorithms |     | nistp256 |     |     |
| ---------------- | ---------- | --- | -------- | --- | --- |
algorithms
ConfiguringSSHtousea ssh public-key- ssh public-key-algorithms x509v3-ssh-rsa
setofpublickey
|     | algorithms |     | ssh-rsa | rsa-sha2-256 |     |
| --- | ---------- | --- | ------- | ------------ | --- |
algorithms
| ConfiguringSSHidle  | cli-session |        | switch(config)#             | cli-session     |            |
| ------------------- | ----------- | ------ | --------------------------- | --------------- | ---------- |
| sessiontimeout      |             |        | switch(config-cli-session)# |                 | timeout 20 |
| ShowingtheSSHserver | show ssh    | server | show ssh                    | server all-vrfs |            |
configuration
ShowingtheactiveSSH show ssh server show ssh server sessions all-vrfs
sessions
sessions
ShowingtheSSHserver show ssh host-key show ssh host-key ecdsa
hostkeys
| SSH server        | commands |     |     |     |     |
| ----------------- | -------- | --- | --- | --- | --- |
| show ssh host-key |          |     |     |     |     |
Syntax
| show ssh host-key | [ecdsa | ed25519 | | rsa] |     |     |     |
| ----------------- | ---------------- | ------ | --- | --- | --- |
Description
ShowsthepublichostkeysfortheSSHserver.Ifthekeytypeisnotprovided,allavailablehost-keysare
shown.
Commandcontext
Manager(#)
Parameters
SSHserver|35

ecdsa
SelectstheECDSAhost-keypair.
ed25519
SelectstheED25519host-keypair.
rsa
SelectstheRSAhost-keypair.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShowingtheECDSApublichost-key:
| switch#  | show ssh host-key | ecdsa   |                     |     |
| -------- | ----------------- | ------- | ------------------- | --- |
| Key Type | : ECDSA           | Curve : | ecdsa-sha2-nistp256 |     |
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAhtuv5rABBBGs
...
O4mjVFGMVKZ87RWkyrxeQa2fAGZZEp1902K33/k3q17fA4EivRzC75YvjDu8=
Showingallpublichostkeys:
| switch#  | show ssh host-key |         |                     |     |
| -------- | ----------------- | ------- | ------------------- | --- |
| Key Type | : ECDSA           | Curve : | ecdsa-sha2-nistp256 |     |
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAhtuv5rABBBGs
...
O4mjVFGMVKZ87RWkyrxeQa2fAGZZEp1902K33/k3q17fA4EivRzC75YvjDu8=
| Key Type | : ED25519 |     |     |     |
| -------- | --------- | --- | --- | --- |
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGb6910Jwoe8Hkl9K5YhqijrWI3yovNbiJVq6tw4WjJr4
| Key Type | : RSA | Key Size | : 2048 |     |
| -------- | ----- | -------- | ------ | --- |
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDdVCXlw43h4n1bwg9jI6DSBMngymCdPD0JUG42Sn9IS
...
nGSXtrNy6OmlFDJTAy+zz5Kd8d21ZLuhf07IHNgF3pff65Xc8qNJBv
| show ssh | server |     |     |     |
| -------- | ------ | --- | --- | --- |
Syntax
| show ssh server | [vrf | <VRF-NAME> | | all-vrfs] | [vsx-peer] |
| --------------- | ---- | ---------- | ----------- | ---------- |
Description
ShowstheSSHserverconfigurationforthespecifiedVRF.Administratorscanshowtheserverconfiguration
ofallVRFsbyusingtheall-vrfsparameter.IfnoVRFnameisprovidedinthiscommand,thecommand
showstheSSHserverconfigurationonthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
SelectsallVRFs.
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 36

vrf VRF-NAME>
SpecifiestheVRFname.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
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
SSHserver|37

| Max | Auth | Attempts | :   | 6   |     |     |     |     |     |
| --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
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
| hmac-sha1-etm@openssh.com, |     |                      |                                       | umac-64@openssh.com, |                      |     |     |     |     |
| -------------------------- | --- | -------------------- | ------------------------------------- | -------------------- | -------------------- | --- | --- | --- | --- |
| umac-128@openssh.com,      |     |                      | hmac-sha2-256,hmac-sha2-512,hmac-sha1 |                      |                      |     |     |     |     |
| Public                     | Key | Algorithms:          |                                       |                      |                      |     |     |     |     |
| rsa-sha2-256,              |     | rsa-sha2-512ssh-rsa, |                                       |                      | ecdsa-sha2-nistp256, |     |     |     |     |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 38

|     | ecdsa-sha2-nistp384,        |     |     | ecdsa-sha2-nistp521, |                             |     |                  | ssh-ed25519, |     |     |
| --- | --------------------------- | --- | --- | -------------------- | --------------------------- | --- | ---------------- | ------------ | --- | --- |
|     | x509v3-rsa2048-sha256,      |     |     | x509v3-ssh-rsa,      |                             |     | x509v3-sign-rsa, |              |     |     |
|     | x509v3-ecdsa-sha2-nistp256, |     |     |                      | x509v3-ecdsa-sha2-nistp384, |     |                  |              |     |     |
x509v3-ecdsa-sha2-nistp521
| SSH | server     | configuration |          | on  | VRF mgmt | :        |     |               |       |       |
| --- | ---------- | ------------- | -------- | --- | -------- | -------- | --- | ------------- | ----- | ----- |
|     | IP Version |               |          | :   | IPv4     | and IPv6 |     | SSH Version   |       | : 2.0 |
|     | TCP        | Port          |          | :   | 22       |          |     | Grace Timeout | (sec) | : 120 |
|     | Max        | Auth          | Attempts | :   | 6        |          |     |               |       |       |
Ciphers:
|     | chacha20-poly1305@openssh.com,         |          |               |                               |                         | aes128-ctr, |                     | aes192-cbc,          |     |     |
| --- | -------------------------------------- | -------- | ------------- | ----------------------------- | ----------------------- | ----------- | ------------------- | -------------------- | --- | --- |
|     | aes128-cbc,                            |          | aes192-ctr,   |                               | aes256-gcm@openssh.com, |             |                     |                      |     |     |
|     | aes128-gcm@openssh.com,                |          |               |                               | aes256-ctr,             |             | aes256-cbc          |                      |     |     |
|     | Host                                   | Key      | Algorithms:   |                               |                         |             |                     |                      |     |     |
|     | ecdsa-sha2-nistp256,                   |          |               | ecdsa-sha2-nistp384,          |                         |             |                     | ecdsa-sha2-nistp521, |     |     |
|     | ssh-ed25519,                           |          | rsa-sha2-256, |                               | rsa-sha2-512,           |             | ssh-rsa             |                      |     |     |
|     | Key                                    | Exchange | Algorithms:   |                               |                         |             |                     |                      |     |     |
|     | curve25519-sha256,                     |          |               | curve25519-sha256@libssh.org, |                         |             |                     |                      |     |     |
|     | ecdh-sha2-nistp256,ecdh-sha2-nistp384, |          |               |                               |                         |             | ecdh-sha2-nistp521, |                      |     |     |
diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,
diffie-hellman-group18-sha512,diffie-hellman-group14-sha256,
diffie-hellman-group14-sha1
MACs:
|      | hmac-sha1-etm@openssh.com,  |        |                      |                                       | umac-64@openssh.com,        |                      |                  |              |     |     |
| ---- | --------------------------- | ------ | -------------------- | ------------------------------------- | --------------------------- | -------------------- | ---------------- | ------------ | --- | --- |
|      | umac-128@openssh.com,       |        |                      | hmac-sha2-256,hmac-sha2-512,hmac-sha1 |                             |                      |                  |              |     |     |
|      | Public                      | Key    | Algorithms:          |                                       |                             |                      |                  |              |     |     |
|      | rsa-sha2-256,               |        | rsa-sha2-512ssh-rsa, |                                       |                             | ecdsa-sha2-nistp256, |                  |              |     |     |
|      | ecdsa-sha2-nistp384,        |        |                      | ecdsa-sha2-nistp521,                  |                             |                      |                  | ssh-ed25519, |     |     |
|      | x509v3-rsa2048-sha256,      |        |                      | x509v3-ssh-rsa,                       |                             |                      | x509v3-sign-rsa, |              |     |     |
|      | x509v3-ecdsa-sha2-nistp256, |        |                      |                                       | x509v3-ecdsa-sha2-nistp384, |                      |                  |              |     |     |
| show | ssh                         | server | sessions             |                                       |                             |                      |                  |              |     |     |
Syntax
| show | ssh server |     | sessions | [vrf <VRF-NAME> |     | |   | all-vrfs] | [vsx-peer] |     |     |
| ---- | ---------- | --- | -------- | --------------- | --- | --- | --------- | ---------- | --- | --- |
Description
ShowstheactiveSSHsessionsonaspecifiedVRForonallVRFs.IfnoVRFisspecified,theactivesessionson
thedefaultVRFareshown.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
SelectsallVRFs.
vrf <VRF-NAME>
SpecifiestheVRFname.
[vsx-peer]
SSHserver|39

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
IfyouprovidethecommandwithaVRFname,thecommandshowstheactiveSSHsessionforthespecified
VRF.AnyusercanshowsessionsofallVRFsbyusingtheall-vrfsparameter.Themaximumnumberof
sessionsperVRFisfive.ThemaximumSSHidlesessiontimeoutis60seconds.
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
| Client       | IP             | : FF01:0:0:0:0:0:0:FE |
| Client       | Port           | : 58838               |
ssh ciphers
Syntax
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 40

ssh ciphers <CIPHERS-LIST>
no ssh ciphers

Description

Configures SSH to use a set of ciphers in the specified priority order. Ciphers in SSH are used for privacy of
data being transported over the connection. The first cipher type entered in the CLI is considered a first
priority. Each option is an algorithm that is used to encrypt the link and each name indicates the algorithm
and cryptographic parameters that are used. Only ciphers that are entered by the user are configured.

The no form of this command removes the configuration of ciphers and reverts SSH to use the default set
of ciphers.

Command context

config

Parameters

<CIPHERS-LIST>

Valid cipher types are:

n aes128-cbc

n aes192-cbc

n aes256-cbc

n aes128-ctr

n aes192-ctr

n aes256-ctr

n aes128-gcm@openssh.com

n aes256-gcm@openssh.com

n chacha20-poly1305@openssh.com

Default set of ciphers in priority order:

1. chacha20-1305@openssh.com

2. aes128-ctr

3. aes192-ctr

4. aes256-ctr

5. aes128-gcm@openssh.com

6. aes256-gcUm@openssh.com

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring SSH to use only specified ciphers in the priority order:

switch(config)# ssh ciphers chacha20-poly1305@openssh.com aes256-ctr aes256-cbc

Reverting SSH to use the default set of ciphers:

switch(config)# no ssh ciphers

SSH server | 41

ssh host-key
Syntax
ssh host-key {ecdsa [ecdsa-sha2-nistp256 | ecdsa-sha2-nistp384 | ecdsa-sha2-nistp521] |
| ed25519 | | rsa [bits | {2048 | | 4096}] | }   |
| ------- | ----------- | ----- | -------- | --- |
Description
GeneratesanSSHhost-keypair.
Commandcontext
config
Parameters
ecdsa
SelectstheECDSAhost-keypairtypeasecdsa-sha2-nistp256(thedefault),ecdsa-sha2-nistp384,or
ecdsa-sha2-nistp521.
ed25519
SelectstheED25519host-keypair.
rsa
SelectstheRSAhost-keypair.Optionally,thekeybitlengthisselectedwitheitherbits 2048(thedefault)
| orbits | 4096. |     |     |     |
| ------ | ----- | --- | --- | --- |
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
WhenanSSHserverisenabledonaVRFforthefirsttime,host-keysaregenerated.
Ifthehost-keyofthegiventypeexists,awarningmessageisdisplayedwitharequesttooverwritethe
previoushost-keywiththenewkey.
Examples
OverwritinganoldECDSAhost-keywithanewecdsa-sha2-nistp384host-key:
| switch(config)# |             | ssh host-key |              | ecdsa ecdsa-sha2-nistp384 |
| --------------- | ----------- | ------------ | ------------ | ------------------------- |
| ecdsa           | host-key    | will be      | overwritten. |                           |
| Do              | you want to | continue     | (y/n)?       |                           |
OverwritinganoldRSAhost-keywithanewRSAhost-keywith2048bits:
| switch(config)# |             | ssh host-key |              | rsa bits 2048 |
| --------------- | ----------- | ------------ | ------------ | ------------- |
| rsa             | host-key    | will be      | overwritten. |               |
| Do              | you want to | continue     | (y/n)?       |               |
OverwritinganECDSAhost-keywithanED25519host-keypair:
| switch(config)# |             | ssh host-key |                 | ed25519 |
| --------------- | ----------- | ------------ | --------------- | ------- |
| ed25519         | host-key    | will         | be overwritten. |         |
| Do              | you want to | continue     | (y/n)?          |         |
ssh host-key-algorithms
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 42

Syntax

ssh host-key-algorithms <HOST-KEY-ALGORITHMS-LIST>
no ssh host-key-algorithms

Description

Configures SSH to use a set of host key algorithms in the specified priority order. Host key algorithms
specify which host key types are allowed to be used for the SSH connection. The first host key entered in
the CLI is considered a first priority. Each option represents a type of key that can be used. Host keys are
used to verify the host that you are connecting to. This configuration allows you to control which host key
types are presented to incoming clients, or which host key types to receive first from hosts. Only the host
key algorithms that are specified by the user are configured.

The no form of this command removes the configuration of host key algorithms and reverts SSH to use the
default set of algorithms.

Command context

config

Parameters

<HOST-KEY-ALGORITHMS-LIST>

Valid host key algorithms are:

n ecdsa-sha2-nistp256

n ecdsa-sha2-nistp384

n ecdsa-sha2-nistp521

n rsa-sha2-256

n rsa-sha2-512

n ssh-ed25519

n ssh-rsa

Default set of host key algorithms in priority order:

1. ecdsa-sha2-nistp256

2. ecdsa-sha2-nistp384

3. ecdsa-sha2-nistp521

4. ssh-ed25519

5. rsa-sha2-256

6. rsa-sha2-512

7. ssh-rsa

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring SSH to use only specified host key algorithms:

switch(config)# ssh host-key-algorithms ssh-rsa ssh-ed25519 ecdsa-sha2-nistp521

Reverting SSH to use the default set of host key algorithms:

SSH server | 43

switch(config)# no host-key-algorithms

ssh key-exchange-algorithms

Syntax

ssh key-exchange-algorithms <KEY-EXCHANGE-ALGORITHMS-LIST>
no ssh key-exchange-algorithms

Description

Configures SSH to use a set of key exchange algorithm types in the specified priority order. The first key
exchange type entered in the CLI is considered a first priority. Key exchange algorithms are used to
exchange a shared session key with a peer securely. Each option represents an algorithm that is used to
distribute a shared key in a way that prevents outside interference, manipulation, or recovery. Only the key
exchange algorithms that are specified by the user are configured.

The no form of this command removes the configuration of key exchange algorithms and reverts SSH to use
the default set of algorithms.

Command context

config

Parameters

<KEY-EXCHANGE-ALGORITHMS-LIST>

Valid key exchange algorithms are:

n curve25519-sha256

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

Default set of key exchange algorithms in priority order:

1. curve25519-sha256

2. curve25519-sha256@libssh.org

3. ecdh-sha2-nistp256

4. ecdh-sha2-nistp384

5. ecdh-sha2-nistp521

6. diffie-hellman-group-exchange-sha256

7. diffie-hellman-group16-sha512

8. diffie-hellman-group18-sha512

9. diffie-hellman-group14-sha256

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

44

10. diffie-hellman-group-exchange-sha1

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring SSH to use a set of specified key exchange algorithms:

switch(config)# ssh key-exchange-algorithms ecdh-sha2-nistp256 curve25519-sha256

diffie-hellman-group-exchange-sha256

Reverting SSH to use the default set of key-exchange-algorithms:

switch(config)# no key-exchange-algorithms

ssh known-host remove

Syntax

ssh known-host remove {all | {<IPv4-ADDRESS> | <HOSTNAME> | <IPv6-ADDRESS>} }

Description

Clears the list of trusted SSH servers for your user account. When you download or upload a file to or from
a server using SFTP, you establish a trusted SSH relationship with that server. Each user account maintains
its own set of SSH server host-keys for every server to which the user previously connected.

Command context

config

Parameters

all

Clears the trusted servers list.

<IPv4-ADDRESS>

Specifies the IPv4 address of the remote device.

<HOSTNAME>

Specifies the host name of the remote device. The length of the host name can be up to 255 characters.

<IPv6-ADDRESS>

Specifies the IPv6 address of the remote device.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Clearing the trusted server list:

switch(config)# ssh known-host remove all

Removing a specified server from the trusted server list:

SSH server | 45

switch(config)# ssh known-host remove 1.1.1.1

ssh macs

Syntax

ssh macs <MACS-LIST>
no ssh macs

Description

Configures SSH to use a set of message authentication codes (MACs) in the specified priority order. The first
MAC entered in the CLI is considered a first priority. MACs maintain the integrity of each message sent
across an SSH connection. Each option represents an algorithm that can be used to provide integrity
between peers. Only the MAC types that are specified by the user are configured.

The no form of this command removes the configuration of MACs and reverts SSH to use the default set of
MACs.

Command context

config

Parameters

<MACS-LIST>

Valid MAC types are:

n hmac-sha1

n hmac-sha1-96

n hmac-sha1-etm@openssh.com

n hmac-sha2-256

n hmac-sha2-512

n hmac-sha2-256-etm@openssh.com

n hmac-sha2-512-etm@openssh.com

Default set of MACs in priority order:

1. hmac-sha2-256-etm@openssh.com

2. hmac-sha2-512-etm@openssh.com

3. hmac-sha1-etm@openssh.com

4. hmac-sha2-256

5. hmac-sha2-512

6. hmac-sha1

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring SSH to use a set of specified MACs:

switch(config)# ssh macs hmac-sha2-256 hmac-sha2-512

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

46

Reverting SSH to use the default set of MACs:

switch(config)# no ssh macs

ssh maximum-auth-attempts

Syntax

ssh maximum-auth-attempts <ATTEMPTS>
no maximum-auth-attempts

Description

Sets the SSH maximum number of authentication attempts.

The no form of the command resets the maximum to its default of 6.

Command context

config

Parameters

<ATTEMPTS>

Specifies the maximum number of SSH authentication attempts. Range: 1 to 10. Default: 6.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the maximum number of authentication attempts:

switch(config)# ssh maximum-auth-attempts 3

Resetting the maximum number of authentication attempts to its default of 6:

switch(config)# no maximum-auth-attempts

ssh public-key-algorithms

Syntax

ssh public-key-algorithms <PUBLIC-KEY-ALGORITHMS-LIST>
no ssh public-key-algorithms

Description

Configures SSH to use a set of public key algorithms in the specified priority order. The first public key type
entered in the CLI is considered a first priority. Public key algorithms specify which public key types can be
used for public key authentication in SSH. Each option represents a public key type that the SSH server can
accept or that the SSH client can present to a server. Only the public key algorithms that are chosen by the
user are configured.

The no form of this command removes the configuration of public key algorithms and reverts SSH to use
the default set.

SSH server | 47

Command context

config

Parameters

<PUBLIC-KEY-ALGORITHMS-LIST>

Valid public key algorithm types are:

n ecdsa-sha2-nistp256

n ecdsa-sha2-nistp384

n

ecdsa-sha2-nistp521

n ssh-ed25519

n ssh-rsa

n rsa-sha2-256

n rsa-sha2-512

n x509v3-ecdsa-sha2-nistp256

n x509v3-ecdsa-sha2-nistp384

n x509v3-ecdsa-sha2-nistp521

n x509v3-rsa2048-sha256

n x509v3-sign-rsa

n x509v3-ssh-rsa

Default set of public key algorithms in priority order:

1. rsa-sha2-256
2. rsa-sha2-512

3. ssh-rsa

4. ecdsa-sha2-nistp256

5. ecdsa-sha2-nistp384

6. ecdsa-sha2-nistp521

7. ssh-ed25519

8. x509v3-rsa2048-sha256

9. x509v3-ssh-rsa

10. x509v3-sign-rsa

11. x509v3-ecdsa-sha2-nistp256

12. x509v3-ecdsa-sha2-nistp384

13. x509v3-ecdsa-sha2-nistp521

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring SSH to use a set of specified public key algorithms:

switch(config)# ssh public-key-algorithms x509v3-ssh-rsa ssh-rsa rsa-sha2-256

Reverting SSH to use the default set of public key algorithms:

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

48

| switch(config)# | no ssh public-key-algorithms |     |
| --------------- | ---------------------------- | --- |
| ssh server vrf  |                              |     |
Syntax
| ssh server vrf <VRF-NAME> |            |     |
| ------------------------- | ---------- | --- |
| no ssh server vrf         | <VRF-NAME> |     |
Description
EnablestheSSHserveronthespecifiedVRF.
ThenoformofthecommanddisablestheSSHserveronthespecifiedVRF.
Commandcontext
config
Parameters
vrf <VRF-NAME>
SpecifiestheVRFname.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingtheSSHserveronthemanagementVRF:
| switch(config)# | ssh server | vrf mgmt |
| --------------- | ---------- | -------- |
DisablingtheSSHserveronthemanagementVRF:
| switch(config)# | no ssh server | vrf mgmt |
| --------------- | ------------- | -------- |
SSHserver|49

Chapter 5

SSH client

SSH client

The switch provides an SSH client that enables the switch to log in to an SSH server such as another switch,
typically for command execution purposes. The SSH client provides secure encrypted communications
between the switch and the SSH server over any network.

SSH client commands

ssh (client login)

Syntax

ssh [<USERNAME>@]{<IPV4> | <HOSTNAME>} [vrf <VRF-NAME>] [port <PORT-NUMBER>]

Description

Establishes a client session with an SSH server which is typically another switch.

Command context

Manager (#)

Parameters

<USERNAME>

Specifies the username that the client uses to log in to an SSH server. When omitted, the username of the
current session is used.

{<IPV4> | <HOSTNAME>}

Specifies the SSH server to which the SSH client will connect.

n <IPV4>: The IPv4 address.

n <HOSTNAME>: The host name.

vrf <VRF-NAME>

Specifies the VRF to be used for the SSH client session. When omitted, the default VRF named default is
used.

port <PORT-NUMBER>

Specifies the SSH server TCP port number. When omitted, the default TCP port 22 is used.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Establishing an SSH client session (using the management VRF) with an SSH server:

switch# ssh admin@10.0.11.180 vrf mgmt

Establishing an SSH client session (using the default VRF and a specific port) with an SSH server:

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

50

| switch# | ssh admin@10.0.11.175 |     |     | port 223 |     |
| ------- | --------------------- | --- | --- | -------- | --- |
Configuringatestuseronswitch1andthenconnectingtoswitch1fromswitch2usingtheSSHclienton
themgmtVRF:
| ** Configuring | a test | user | on  | switch | 1 ** |
| -------------- | ------ | ---- | --- | ------ | ---- |
switch(config)#
|                              | user-group |     | test   |     |              |
| ---------------------------- | ---------- | --- | ------ | --- | ------------ |
| switch(config-usr-grp-test)# |            |     | permit | cli | command ".*" |
| switch(config)#              | exit       |     |        |     |              |
switch(config)# user test-user group test password plaintext tst#9J%** On switch 2,
| connecting | to switch                 | 1 using | the | SSH | client ** |
| ---------- | ------------------------- | ------- | --- | --- | --------- |
| switch#    | ssh test-user@10.0.11.177 |         |     | vrf | mgmt      |
SSHclient|51

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
Authentication identifies users, validates their credentials, and grants switch access. Local authentication is
either password-based or SSH public key-based.

Password-based local authentication

n Validates users with local user name and password credentials

n Is supported on all interfaces/channels (SSH, WebUI, Console, REST)

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

52

IsenabledbydefaultbutcanbesupersededbyremoteauthenticationorwithSSHclientusingSSH
n
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
authenticat authenticati aaa authentication login default local
| ionaslocal |     | aaa authentication | login console | local |     |
| ---------- | --- | ------------------ | ------------- | ----- | --- |
on login
forthe
specified
connection
types
| Show        | show aaa     | show aaa authentication |     |     |     |
| ----------- | ------------ | ----------------------- | --- | --- | --- |
| authenticat | authenticati |                         |     |     |     |
ion
on
configurati
on
| Enable    | aaa          | aaa authentication | minimum-password-length |     | 12  |
| --------- | ------------ | ------------------ | ----------------------- | --- | --- |
| password- | authenticati |                    |                         |     |     |
based
on minimum-
authenticat
password-
ion
| minimum | length |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- |
password
length
checking
| Disable | aaa | no aaa authentication | minimum-password-length |     |     |
| ------- | --- | --------------------- | ----------------------- | --- | --- |
password-
authenticati
based
on minimum-
| authenticat | password- |     |     |     |     |
| ----------- | --------- | --- | --- | --- | --- |
ion
length
minimum
password
length
checking
LocalAAA|53

Command
| Task |     | Example |     |
| ---- | --- | ------- | --- |
name
Enable aaa aaa authentication limit-login-attempts 4 lockout-time 20
| local | authenticati |     |     |
| ----- | ------------ | --- | --- |
password-
on limit-
based
login-
authenticat
attempts
ionlogin
attempt
limiting
| Disable | aaa | no aaa authentication | limit-login-attempts |
| ------- | --- | --------------------- | -------------------- |
local
authenticati
password-
on limit-
| based | login- |     |     |
| ----- | ------ | --- | --- |
authenticat
attempts
ionlogin
attempt
limiting
| Enable    | ssh          | ssh password-authentication |     |
| --------- | ------------ | --------------------------- | --- |
| local     | password-    |                             |     |
| password- | authenticati |                             |     |
based
on
authenticat
ionforuse
withSSH
clients
(enabledby
default)
| Disable | ssh       | no ssh password-authentication |     |
| ------- | --------- | ------------------------------ | --- |
| local   | password- |                                |     |
password-
authenticati
based
on
authenticat
ionforuse
withSSH
clients
| EnableSSH | ssh public- | ssh public-key-authentication |     |
| --------- | ----------- | ----------------------------- | --- |
| publickey | key-        |                               |     |
authenticat
authenticati
ion
on
(enabledby
default)
| Disable   | ssh public- | no ssh public-key-authentication |     |
| --------- | ----------- | -------------------------------- | --- |
| SSHpublic | key-        |                                  |     |
key
authenticati
authenticat
on
ion
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 54

Command
| Task |     | Example |     |     |     |
| ---- | --- | ------- | --- | --- | --- |
name
| Showstate | show ssh     | show ssh | authentication-method |     |     |
| --------- | ------------ | -------- | --------------------- | --- | --- |
| oflocal   | authenticati |          |                       |     |     |
password-
on-method
based(for
SSH)and
SSHpublic
key
authenticat
ion
Copyingthe user user admin authorized-key ecdsa-sha2-nistp256 E2VjZH...QUiCAk=
| clientSSH |     | root@switch |     |     |     |
| --------- | --- | ----------- | --- | --- | --- |
authorized-
| publickey | key |     |     |     |     |
| --------- | --- | --- | --- | --- | --- |
intothekey
list
| Removing | user | no user | admin authorized-key | 2   |     |
| -------- | ---- | ------- | -------------------- | --- | --- |
SSHpublic
authorized-
keysfrom
key
thekeylist
| Showing | show user | show user | admin authorized-key |     |     |
| ------- | --------- | --------- | -------------------- | --- | --- |
theSSH
clientpublic
keylist
Local authorization
Authorizationcontrolsauthenticateduserscommandexecutionandswitchinteractionprivileges.Local
authorizationusesrole-basedaccesscontrol(RBAC)toproviderole-basedprivilegelevelsplusoptionaluser-
definedlocalusergroupswithcommandexecutionrules.Authorizationoccursonlyaftersuccessful
authentication.
n Administratorshavefullcommandexecutionandswitchinteractionprivilege.
n Operatorsarelimitedtotheuseofseveralnonsensitiveshowcommands.
n Auditorsarelimitedtoafewauditing-relatedcommands.
Optionalper-commandauthorizationisavailablethroughconfigurationofuser-definedlocalusergroups
withcommandauthorizationrulesappliedtorespectivegroupmembers.seeUser-definedusergroups .
| Local authorization |     | tasks |     |     |     |
| ------------------- | --- | ----- | --- | --- | --- |
Thelocalauthorizationtasksareasfollows:
| Task | Commandname |     | Example |     |     |
| ---- | ----------- | --- | ------- | --- | --- |
Enableauthorization aaa authorization Enablelocalauthorizationforthedefaultandconsole
| aslocalRBACforthe |     |     | connectiontypes: |     |     |
| ----------------- | --- | --- | ---------------- | --- | --- |
commands
| specifiedconnection |      |     | aaa authorization      | commands default | local |
| ------------------- | ---- | --- | ---------------------- | ---------------- | ----- |
| types               |      |     | aaa authorization      | commands console | local |
| Showauthorization   | show | aaa | show aaa authorization |                  |       |
configuration
authorization
LocalAAA|55

| Local accounting |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- |
Localaccountingisalwaysactive.Itcannotbeturnedoff.
Thisaccountinginformationiscapturedandmadeavailablelocally(usingshow accounting log)and,if
desired,forsendingtoremoteAAAservers:
n ExecAccounting:userlogin/logoutevents.
n Commandaccounting:commandsexecutedbyusers.
n Systemaccounting:remoteaccountingOn/Offevents.
CLIshowcommands.
n
Interactionsonthenon-CLIinterfaces:RESTandWebUI.
n
Thefollowingisnotcapturedormadeavailableasaccountinginformation:
CLIcommandsthatreboottheswitch.
n
Interactionsinthebashshell.
n
| Seealsotheshow   | accounting | logcommand. |     |     |     |     |
| ---------------- | ---------- | ----------- | --- | --- | --- | --- |
| Local accounting |            | tasks       |     |     |     |     |
Thelocalaccountingtasksareasfollows:
Commandname
| Task |     |     | Example |     |     |     |
| ---- | --- | --- | ------- | --- | --- | --- |
Enableaccounting aaa accounting Enablelocalaccountingforthedefaultandconsoleconnection
| aslocalforthe | all-mgmt |     | types:         |                  |            |       |
| ------------- | -------- | --- | -------------- | ---------------- | ---------- | ----- |
| specified     |          |     | aaa accounting | all-mgmt default | start-stop | local |
connectiontypes aaa accounting all-mgmt console start-stop local
| Showaccounting | show       | aaa        | show aaa accounting |             |     |     |
| -------------- | ---------- | ---------- | ------------------- | ----------- | --- | --- |
| configuration  | accounting |            |                     |             |     |     |
| Showlocal      | show       | accounting | show accounting     | log last 10 |     |     |
| accountinglog  | log        |            |                     |             |     |     |
contents
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 56

Chapter 7

Local AAA commands

Local AAA commands

aaa accounting all-mgmt

Syntax

aaa accounting all-mgmt <CONNECTION-TYPE> start-stop {local | group <GROUP-LIST>}
no aaa accounting all-mgmt <CONNECTION-TYPE>

Description

Defines accounting as being local (with the name local) (the default). Or defines a sequence of remote AAA
server groups to be accessed for accounting purposes.

For remote accounting, the information is sent to the first reachable remote server that was configured with
this command for remote accounting. If no remote server is reachable, local accounting remains available.
Each available connection type (channel) can be configured individually as either local or using remote AAA
server groups. All server groups named in your command, must exist. This command can be issued multiple
times, once for each connection type. Local is always available for any connection type not configured for
remote accounting.

The system accounting log is not associated with any connection type (channel) and is therefore sent to the

accounting method configured on the default connection type (channel) only.

The no form of this command removes for the specified connection type, any defined remote AAA server
group accounting sequence. Local accounting is available for connection types without a configured remote
AAA server group list (whether default or for the specific connection type).

Command context

config

Parameters

<CONNECTION-TYPE>

One of these connection types (channels):

default

Defines a list of accounting server groups to be used for the default connection type. This
configuration applies to all other connection types (console, https-server, ssh) that are not explicitly
configured with this command. For example, if you do not use aaa accounting all-mgmt
console... to define the console accounting list, then this default configuration is used for console.

console

Defines a list of accounting server groups to be used for the console connection type.

https-server

Defines a list of accounting server groups to be used for the https-server (REST, Web UI) connection
type.
ssh

Defines a list of accounting server groups to be used for the ssh connection type.

start-stop

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

57

Selects accounting information capture at both the beginning and end of a process.

local

Selects local-only accounting when used without the group parameter.

group <GROUP-LIST>

Specifies the list of remote AAA server group names. Each name can be specified one time. Predefined
remote AAA group names tacacs and radius are available. Although not a group name, predefined
name local is available. User-defined TACACS+ and RADIUS server group names may also be used. The
remote AAA server groups are accessed in the order that the group names are listed in this command.
Within each group, the servers are accessed in the order in which the servers were added to the group.
Server groups are defined using command aaa group server and servers are added to a server group
with the command server.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Local accounting is always active. It cannot be turned off.

Examples

Setting local accounting for the default connection type:

switch(config)# aaa accounting all-mgmt default start-stop local

Setting local accounting for the console connection type:

switch(config)# aaa accounting all-mgmt console start-stop local

aaa authentication console-login-attempts

Syntax

aaa authentication console-login-attempts <ATTEMPTS> console-lockout-time <LOCKOUT-TIME>
no aaa authentication console-login-attempts

Description

For the console interface only (not SSH or REST), enables console login attempt limiting. If the number of
failed console login attempts equals the configured threshold, the user is locked out for the configured
duration..

The no form of this command disables console login attempt limits.

Important: If you enable the lockout using this command and also enable the SSH and REST lockout using
command aaa authentication limit-login-attempts, and then enter too many consecutive wrong
passwords, you will become locked out, and will have to wait for the configured lockout time to elapse before

logging in on any interface.

Local AAA commands | 58

This console login attempt limiting feature is only available when not using remote authentication through AAA

servers (TACACS+ or RADIUS) on any interface. Remote authentication through AAA servers (TACACS+ or

RADIUS) is not possible when limit login attempts is configured on any interface.

Command context

config

Parameters

<ATTEMPTS>

Specifies the threshold of failed console login attempts that triggers user lockout. Range: 1 to 10. For
example, if <ATTEMPTS> is set to 1, a single failed login attempt triggers immediate user lockout.

<LOCKOUT-TIME>

Specifies the amount of time a user is locked out. Range: 1 to 3600 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling console login attempt failure limiting with a 60 second lockout being triggered upon the third
consecutive login attempt failure.

switch(config)# aaa authentication console-login-attempts 3 console-lockout-time 60

Disabling console login attempt failure limiting:

switch(config)# no aaa authentication console-login-attempts

aaa authentication limit-login-attempts

Syntax

aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>
no aaa authentication limit-login-attempts

Description

For the SSH and REST interface, enables local login attempt limiting. If the number of failed local login
attempts equals the configured threshold, the user is locked out for the configured duration.

The no form of this command disables local login attempt limits.

Important: If you enable the lockout using this command and also enable the console lockout using command
aaa authentication console-login-attempts, and then enter too many consecutive wrong passwords, you
will become locked out, and will have to wait for the configured lockout time to elapse before logging in on any

interface.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

59

This local login attempt limiting feature is only available when not using remote authentication through AAA

servers (TACACS+ or RADIUS) on any interface. Remote authentication through AAA servers (TACACS+ or

RADIUS) is not possible when limit login attempts is configured on any interface.

Command context

config

Parameters

<ATTEMPTS>

Specifies the threshold of failed local login attempts that triggers user lockout. Range: 1 to 10. For
example, if <ATTEMPTS> is set to 1, a single failed login attempt triggers immediate user lockout.

<LOCKOUT-TIME>

Specifies the amount of time a user is locked out. Range: 1 to 3600 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling local login attempt failure limiting with a 20 second lockout being triggered upon the fourth
consecutive login attempt failure.

switch(config)# aaa authentication limit-login-attempts 4 lockout-time 20

Disabling login attempt failure limiting:

switch(config)# no aaa authentication limit-login-attempts

aaa authentication login

Syntax

aaa authentication login <CONNECTION-TYPE> {local | group <GROUP-LIST>}
no aaa authentication login <CONNECTION-TYPE>

Description

Defines authentication as being local (with the name local) (the default). Or defines a sequence of remote
AAA server groups to be accessed for authentication purposes. Each available connection type (channel) can
be configured individually as either local or using remote AAA server groups. All server groups named in your
command, must exist. This command can be issued multiple times, once for each connection type. Local is
always available for any connection type not configured for remote AAA authentication.

The no form of this command removes for the specified connection type, any defined remote AAA server
group authentication sequence. Local authentication is available for connection types without a configured
remote AAA server group list (whether default or for the specific connection type).

Command context

config

Parameters

Local AAA commands | 60

<CONNECTION-TYPE>

One of these connection types (channels):

default

Defines a list of authentication server groups to be used for the default connection type. This
configuration applies to all other connection types (console, https-server, ssh) that are not
explicitly configured with this command. For example, if you do not use aaa authentication
login console... to define the console authentication list, then this default configuration is used
for console.

console

Defines a list of authentication server groups to be used for the console connection type.

https-server

Defines a list of authentication server groups to be used for the https-server (REST, Web UI)
connection type.

ssh

Defines a list of authentication server groups to be used for the ssh connection type.

local

Selects local-only authentication when used without the group parameter.

group <GROUP-LIST>

Specifies the list of remote AAA server group names. Each name can be specified one time. Predefined
remote AAA group names tacacs and radius are available. Although not a group name, predefined
name local is available. User-defined TACACS+ and RADIUS server group names may also be used. The
remote AAA server groups are accessed in the order that the group names are listed in this command.
Within each group, the servers are accessed in the order in which the servers were added to the group.
Server groups are defined using command aaa group server and servers are added to a server group
with the command server.

If no AAA server is reachable, local authentication is attempted.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting local authentication for the default connection type:

switch(config)# aaa authentication login default local

Setting local authentication for the console connection type:

switch(config)# aaa authentication login console local

aaa authentication minimum-password-length

Syntax

aaa authentication minimum-password-length <LENGTH>
no aaa authentication minimum-password-length

Description

Enables minimum password length checking. Existing passwords shorter than the minimum length are
unaffected. Length checking does not apply to ciphertext passwords. Length checking applies both to local
and remote authentication.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

61

The no form of this command disables minimum password length checking.

Command context

config

Parameters

<LENGTH>

Specifies the minimum password length. Range: 1 to 32.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling password length checking, with a minimum length of 12.

switch(config)# aaa authentication minimum-password-length 12

Disabling minimum password length checking:

switch(config)# no aaa authentication minimum-password-length

aaa authorization commands

Syntax

aaa authorization commands <CONNECTION-TYPE> {local | none}
aaa authorization commands <CONNECTION-TYPE> group <GROUP-LIST>

no aaa authorization commands <CONNECTION-TYPE>

Description

Defines authorization as being basic local RBAC (specified as none), or as full-fledged local RBAC specified as
local (the default), or as remote TACACS+ (specified with group <GROUP-LIST>). Each available connection
type (channel) can be configured individually. All server groups named in the command, must exist. This
command can be issued multiple times, once for each connection type.

The no form of this command unconfigures authorization for the specified connection type, reverting to the
default of local.

Although only TACACS+ servers are supported for remote authorization, local authorization (basic or full-fledged)

can be used with remote RADIUS authentication.

Command context

config

Parameters

<CONNECTION-TYPE>

One of these connection types (channels):
default

Local AAA commands | 62

Selects the default connection type for configuration. This configuration applies to all other
connection types (console, ssh) that are not explicitly configured with this command. For example, if
you do not use aaa authorization commands console... to define the console authorization list,
then this default configuration is used for console.

console

Selects the console connection type for configuration.

ssh

Selects the ssh connection type for configuration.

local (the default)

When used alone without group <GROUP-LIST>, selects local authorization which can be used to provide
authorization for a purely local setup without any remote AAA servers and also for when RADIUS is used
for remote Authentication and Accounting but Authorization is local.

When used after group, provides for fallback (to full-fledged local authorization) when every server in
every specified TACACS+ server group cannot be reached.

If any TACACS+ server in the specified groups is reachable, but the command fails to be authorized by that

server, the command is rejected and local authorization is never attempted. Local authorization is only

attempted if every TACACS+ server cannot be reached.

none

When used alone without group <GROUP-LIST>, selects basic local RBAC authorization, for use with the
built-in user groups (administrators, operators, auditors).

When used after group, provides for fallback (to basic local RBAC authorization) when every server in
every specified TACACS+ server group cannot be reached.

With none, for users belonging to user-defined user groups, all commands can be executed regardless of what
authorization rules are defined in such groups. For per-command local authorization, use local instead.

group <GROUP-LIST>

Specifies the list of remote AAA server group names. Predefined remote AAA group name tacacs is
available. User-defined TACACS+ server group names may also be used. The remote AAA server groups
are accessed in the order that the group names are listed in this command. Within each group, the
servers are accessed in the order in which the servers were added to the group. Server groups are
defined using command aaa server group and servers are added to a server group using command
server.

It is recommended to always include either the special name local or none as the last name in the group
list. If both local and none are omitted, and no remote AAA server is reachable (or the first reachable
server cannot authorize the command), command execution for the current user will not be possible.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the authorization for default to local:

switch(config)# aaa authorization commands default local

Setting the authorization for the SSH interface to none:

switch(config)# aaa authorization commands ssh none

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

63

| show aaa | accounting |     |     |     |
| -------- | ---------- | --- | --- | --- |
Syntax
| show aaa accounting | [vsx-peer] |     |     |     |
| ------------------- | ---------- | --- | --- | --- |
Description
Showstheaccountingconfigurationperconnectiontype(channel).
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Configuringandthenshowinglocalaccountingforthedefaultandconsoleconnectiontypes:
| switch(config)# | aaa                 | accounting all default | start-stop | local |
| --------------- | ------------------- | ---------------------- | ---------- | ----- |
| switch(config)# | aaa                 | accounting all console | start-stop | local |
| switch(config)# | exit                |                        |            |       |
| switch#         | show aaa accounting |                        |            |       |
AAA Accounting:
| Accounting | Type        |          | : all        |     |
| ---------- | ----------- | -------- | ------------ | --- |
| Accounting | Mode        |          | : start-stop |     |
| Accounting | for default | channel: |              |     |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP | PRIORITY |     |
| ---------- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
local | 0
---------------------------------------------------------------------------------
| Accounting | for console | channel: |     |     |
| ---------- | ----------- | -------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP | PRIORITY |     |
| ---------- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
local | 0
---------------------------------------------------------------------------------
| show aaa | authentication |     |     |     |
| -------- | -------------- | --- | --- | --- |
Syntax
| show aaa authentication |     | [vsx-peer] |     |     |
| ----------------------- | --- | ---------- | --- | --- |
Description
Showstheauthenticationconfigurationperconnectiontype(channel).
LocalAAAcommands|64

Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Configuringandthenshowinglocalauthenticationforthedefaultandconsoleconnectiontypes(channels):
switch(config)#
|                 | aaa authentication | login | default | local |
| --------------- | ------------------ | ----- | ------- | ----- |
| switch(config)# | aaa authentication | login | console | local |
| switch(config)# | exit               |       |         |       |
| switch# show    | aaa authentication |       |         |       |
AAA Authentication:
| Fail-through     |             |          | : Disabled |     |
| ---------------- | ----------- | -------- | ---------- | --- |
| Limit Login      | Attempts    |          | : Not      | set |
| Lockout Time     |             |          | : 300      |     |
| Minimum Password | Length      |          | : Not      | set |
| Authentication   | for default | channel: |            |     |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP | PRIORITY |     |
| ---------- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| local |     | | 0 |     |     |
| ----- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authentication | for console | channel: |     |     |
| -------------- | ----------- | -------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP | PRIORITY |     |
| ---------- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| local |     | | 0 |     |     |
| ----- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| show aaa | authorization |     |     |     |
| -------- | ------------- | --- | --- | --- |
Syntax
show aaa authorization
[vsx-peer]
Description
Showstheauthorizationconfigurationperconnectiontype(channel).
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 65

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Configuringandthenshowingfull-fledgedlocalRBACauthorizationforthedefaultandconsoleconnection
types(channels):
| switch(config)# | aaa authorization | commands default | none |
| --------------- | ----------------- | ---------------- | ---- |
switch(config)#
| switch(config)# | aaa authorization | commands console | none |
| --------------- | ----------------- | ---------------- | ---- |
| switch(config)# | exit              |                  |      |
switch#
| switch# show  | aaa authorization |          |     |
| ------------- | ----------------- | -------- | --- |
| Authorization | for default       | channel: |     |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |
| ---------- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
| none |     | | 0 |     |
| ---- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authorization | for console | channel: |     |
| ------------- | ----------- | -------- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |
| ---------- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
| none |     | | 0 |     |
| ---- | --- | --- | --- |
---------------------------------------------------------------------------------
| show ssh | authentication-method |     |     |
| -------- | --------------------- | --- | --- |
Syntax
show ssh authentication-method
Description
ShowsthestatusoftheSSHpublickeymethodandthelocalpassword-based(throughSSHclient)
authenticationmethod.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Showingtheauthenticationmethods.
LocalAAAcommands|66

switch# show ssh authentication-method
SSH publickey authentication : Enabled
SSH password authentication : Enabled

show user

Syntax

show user <USERNAME> authorized-key

Description

Shows the SSH client public key list for a specified user.

Command context

Operator (>) or Manager (#)

Parameters

<USERNAME>

Specifies the username for which you want to show the SSH client public key list.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

Any user can show their own public key list; however, administrators can also show a public key list of other
users.

Examples

Showing a client public key:

switch# show user admin authorized-key

1. Key Type : RSA
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMtyMBmmAaF6r1zxf3DZNHSYVHBJhlbBlyAIqQ8DSHK
...
U+aE14UW/ifIukmK67sIHwK+FhhRYwPztQc5pjyOPk128a4pgKQaHCcOF169Z admin@switch

Key size : 2048

Showing two client public keys:

switch# show user admin authorized-key
1. Key Type : ECDSA
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEqEFevZ0
...
l76V+D0svdCJ9Wo32zqI9OeAdTJw/eZYp5qknhNgS81HjAI6J/4/kAqdZAjbqQUiCAk= admin@switch

Curve : nistp256

2. Key Type : RSA
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDXQHrqV7+/GcMdOhr//IRjJkX7TQKupW89j80bL7xq8
...
j8qKuHWSN0/h/HxjzQJuYDVmZN5vG3DhpXbBZUlZNnchVod13QLCesqA3VLKN admin@switch

Key size : 2048

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

67

ssh password-authentication

Syntax

ssh password-authentication

no ssh password-authentication

Description

Enables the password-based authentication method for use with SSH clients.

The no form of this command disables the password-based authentication method for use with SSH clients.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Usage

The switch ships with password-based authentication (for SSH clients) enabled. The maximum number of
password retries is three.

Examples

Enabling password authentication for use with SSH clients:

switch(config)# ssh password-authentication

Disabling password authentication for use with SSH clients:

switch(config)# no ssh password-authentication

ssh public-key-authentication

Syntax

ssh public-key-authentication

no ssh public-key-authentication

Description

Enables the SSH public key authentication method. The switch ships with SSH public key authentication
enabled.

The no form of this command disables the SSH public key authentication method.

Although SSH public key authentication is enabled by default, it cannot be used until SSH public keys are added
with the user authorized-key command.

Command context

config

Local AAA commands | 68

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling SSH public key authentication:

switch(config)# ssh public-key-authentication

Disabling SSH public key authentication:

switch(config)# no ssh public-key-authentication

user authorized-key

Syntax

user <USERNAME> authorized-key <PUBKEY>
no user <USERNAME> authorized-key [<KEYNUM>]

Description

Copies an SSH client public key into the key list. If the key list and the public key do not exist, it creates a list
with the public key. If the SSH client public key exists, the command appends the new key to the existing list.
The client public key list holds a maximum of 32 client keys.

The no form of the command removes either one or all SSH public keys from the key list.

Command context

config

Parameters

<USERNAME>

Specifies the name of the user.

<PUBKEY>

Specifies the SSH client public key to be copied into the key list.

<KEYNUM>

Specifies the key number. The range is 1 to 32. Use the show user <USERNAME> authorized-key
command to find the key number associated with the key.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

Each key on the key list has a key identifier. The show user <USERNAME> authorized-key command displays
the key identifier associated with the key.

Administrators can add and remove the public keys of themselves and other users. Operators can add and
remove only their own public keys. If the public key authentication method is enabled, the client public key
present is used by the SSH server to authenticate the client. The authentication method reverts to the
password authentication method and prompts for a client password when one of the following occurs:

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

69

n The client public keys are not present.

n The server does not have the keys enabled.

n The public key method is disabled.

You can either remove all keys or a specific key. Each key on the key list has a key identifier. If you provide
the key identifier in this command, the command removes the corresponding key from the list. If you
provide no key identifier, the command removes all keys from the key list.

Examples

Adding a public key:

switch(config)#user admin authorized-key ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTIt
bmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEqEFevZ0l76V+D0svdCJ9Wo32zqI9OeAIdTJwT/eZYp50qkA
nhZNgS81HBjAI6QJ/4/kAyqdZ9oAjbiqQUiCAk= root@switch

Removing all SSH public keys from the list:

switch(config)# no user admin authorized-key

Removing the specified SSH public key from the list:

switch(config)# no user admin authorized-key 2

Local AAA commands | 70

Chapter 8
|        |          |         |     | Remote | AAA with | TACACS+ |
| ------ | -------- | ------- | --- | ------ | -------- | ------- |
| Remote | AAA with | TACACS+ |     |        |          |         |
RemoteAAAprovidesthefollowingforyourArubaswitch:
AuthenticationusingremoteTACACS+AAAservers.
n
AuthorizationusingremoteTACACS+AAAservers,providingfine-grainedcommandauthorization.
n
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
local:forlocalauthentication.
n
none:forlocal(RBAC)authorization.
n
User-definedAAAserversarealwaysaddedtothematchingdefaultgroup,eithertacacsorradius.
Optionally,eachservercanalsobeaddedtoexactlyoneadditionaluser-defined(custom)group.A
maximumof28user-definedgroupscanbecreated.
Theorderinwhichserversareaddedtoagroupisimportant.Theserveraddedfirstisaccessedfirst,andif
necessary,thesecondserverisaccessedsecond,andsoon.
| Remote                                           | AAA | (TACACS+) | defaults | and limits |               |         |
| ------------------------------------------------ | --- | --------- | -------- | ---------- | ------------- | ------- |
| Setting                                          |     |           |          |            | Default value | / limit |
| AuthenticationofRESTsessionswithTACACS+          |     |           |          |            | Disabled      |         |
| MaximumnumberofTACACS+serversinanAAAgroup        |     |           |          |            | 16            |         |
| MaximumnumberofTACACS+serversthatcanbeconfigured |     |           |          |            | 16            |         |
Maximumnumberofuser-definedAAAservergroupsthatcanbeconfigured 28
| TACACS+authentication |     |     |     |     | Disabled |     |
| --------------------- | --- | --- | --- | --- | -------- | --- |
71
| AOS-CX10.07SecurityGuide| | (6200,6300,6400SwitchSeries) |     |     |     |     |     |
| ------------------------- | ---------------------------- | --- | --- | --- | --- | --- |

| Setting                                    |     |     |     |     | Default  | value / limit |
| ------------------------------------------ | --- | --- | --- | --- | -------- | ------------- |
| TACACS+authenticationglobaltimeout         |     |     |     |     | 5seconds |               |
| TACACS+authenticationpasskey(sharedsecret) |     |     |     |     | None     |               |
49
TACACS+authenticationtcp-port
| TACACS+globalauthenticationprotocol     |     |     |     |     | PAP        |     |
| --------------------------------------- | --- | --- | --- | --- | ---------- | --- |
| TACACS+servertrackingdefaultinterval    |     |     |     |     | 300seconds |     |
| TACACS+serveraccessthroughthedefaultVRF |     |     |     |     | default*   |     |
*Thedefaultvalueisdefault,unlessanotherVRFisspecifiedduringtheserverconfiguration.
| About | global | versus | per-TACACS+ | server | passkeys | (shared |
| ----- | ------ | ------ | ----------- | ------ | -------- | ------- |
secrets)
TocommunicatewithaTACACS+AAAserver,theswitchmusthaveapasskey(sharedsecret)configuredthat
matcheswhatisconfiguredontheserver.Useoneofthesecommandstoachievethedesired
configuration:
ForaglobalpasskeycommontoeveryTACACS+server,usetacacs-server key.
n
n Foraper-TACACS+serverpasskey,usetacacs-server hostwiththekeyparameter.
Ifbothpasskeysareconfiguredontheswitch,theper-TACACS+serverpasskeyisused.
| Remote | AAA | TACACS+ | server | configuration | requirements |     |
| ------ | --- | ------- | ------ | ------------- | ------------ | --- |
Theuser-suppliedTACACS+servermust:
HaveanIPv4/IPv6addressorfullyqualifieddomainname(FQDN)thatisvisibletotheswitch.
n
Haveapasskey(sharedsecret)thatmatcheswhatisconfiguredontheswitch.
n
Provideusernameandpassworddefinitionsforeveryswitchuser.Remoteusersdonotrequire
n
definitionontheswitch.
ConfigureuserroleassignmentusingTACACS+attributes.
n
Haveanyneededcommandauthorizationconfiguredtocontrolwhatcommands(peruseroruserrole)
n
willbeexecutableontheswitch.
ConsultyourTACACS+serverdocumentationforinstallationandgeneralconfigurationdetails.
IfSSHpublickeyauthenticationisused,thekeyinformationisstoredlocallyontheswitch,makingusernameand
passworddefinitionontheTACACS+serverunnecessary.
| User | role assignment |     | using TACACS+ | attributes |     |     |
| ---- | --------------- | --- | ------------- | ---------- | --- | --- |
RemoteAAAwithTACACS+|72

UserroleassignmentisconfiguredontheTACACS+serverusingVSAs(vendor-specificattributes)and
TACACS+specifiedattributes.
TACACS+serverscanreturnmultipleattributevaluepairs(AVPs)inresponsetoanauthenticationrequest.
Theattributesareprocessedinthisorderofprecedencetodeterminetheuserroleassigned:
n IftheAruba-Admin-RoleVSAispresent,maptheusertothematchingcorrespondinglocaluser-group
name.
o Elseifthepriv-lvlTACACS+specifiedattributeispresent,extracttheprivilegelevel(1,15,or19)and
maptheusertothelocaluser-groupcorrespondingtothisprivilegelevel(1=operators,
15=administrators,19=auditors).Privilegelevels2to14mayalsobeusedwithmatchinglocaluser
groupsnamed2to14.
Otherwise,theuserrolecannotbedetermined,andauthenticationfails.
l
| This information |        | is summarized |            | as follows: |                                   |          |
| ---------------- | ------ | ------------- | ---------- | ----------- | --------------------------------- | -------- |
| Aruba-Admin-Role |        |               | priv-lvl   |             | Userrole                          | assigned |
| <GROUP-NAME>     |        |               | Donotcare  |             | Matchinglocaluser<GROUP-NAME>     |          |
| Notpresent       |        |               | 1          |             | Operators                         |          |
| Notpresent       |        |               | 15         |             | Administrators                    |          |
| Notpresent       |        |               | 19         |             | Auditors                          |          |
| Notpresent       |        |               | 2to14      |             | Matchinglocalusergroupsnamed2to14 |          |
| Notpresent       |        |               | Notpresent |             | None(notauthenticated)            |          |
| TACACS+          | server | redundancy    |            | and access  | sequence                          |          |
Topreventauthenticationandauthorizationinterruption,itiscommonpracticetoconfiguremorethanone
TACACS+server.WhenidentifyingTACACS+serverstotheswitch,servergrouporder(andserverorder
withinthegroup),determinesserveraccessorder.
Whendefiningtheserveraccesssequenceforauthenticationwithaaa authentication login default,there
isanimpliedlocalincludedasthelastiteminthelist.IfnoTACACS+servercanbereached,localauthentication
willbeattempted.
Whendefiningtheserveraccesssequenceforauthorizationwithaaa authorization commands,itis
recommendedtoalwaysincludeeitherlocalornoneasthelastiteminthelist.
| Single         | source | IP  | address | for consistent |     | source |
| -------------- | ------ | --- | ------- | -------------- | --- | ------ |
| identification |        | to  | AAA     | servers        |     |        |
Ifapplicabletoyourinstallation,itisrecommendedthatyouperformtheoptionalconfigurationmentionedinthis
section.
IfyourtopologyallowstheAAAservertobereachedthroughmultiplepaths,theserverinterpretsthe
incomingpacketstobefromdifferentswitcheseventhoughtheyareallcomingfromthesameswitch.
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 73

HavingaswitchassociatedwithmultipleIPaddressesmakesitmoredifficulttointerpretsystemlogsand
accountingdata.
ToensurethatalltrafficsentfromtheswitchtotheAAAserverusesthesamesourceIPaddress,useip
source-interfaceoripv6 source-interface.Thesetwocommandsplustherelatedcommandsshow ip
source-interfaceandshow ipv6 source-interfacearedescribedunderLayer2/3Interfacecommandsin
theCommand-LineInterfaceGuide.
| TACACS+ | general | tasks |     |     |     |     |
| ------- | ------- | ----- | --- | --- | --- | --- |
GeneralTACACS+tasks,notspecifictoauthentication,authorization,oraccounting,areasfollows:
| Task |     | Commandname | Example |     |     |     |
| ---- | --- | ----------- | ------- | --- | --- | --- |
ConfiguringaTACACS+ tacacs-server host tacacs-server host 1.1.1.1 vrf default
| server           |     |                    | no tacacs-server   |     | host   | 1.1.1.1 vrf default |
| ---------------- | --- | ------------------ | ------------------ | --- | ------ | ------------------- |
|                  |     |                    | show tacacs-server |     | detail |                     |
| Showingglobaland |     | show tacacs-server |                    |     |        |                     |
TACACS+server
configurations
ConfiguringaTACACS+ aaa group server aaa group server tacacs sg1
| servergroup         |     |                  | no aaa   | group server  | tacacs | sg1 |
| ------------------- | --- | ---------------- | -------- | ------------- | ------ | --- |
| Showingservergroups |     | show aaa server- | show aaa | server-groups |        |     |
groups
| AddingaTACACS         |     | server | aaa group | server  | tacacs  | sg1            |
| --------------------- | --- | ------ | --------- | ------- | ------- | -------------- |
| servertoaserver-group |     |        | server    | 1.1.1.2 | port 32 | vrf default    |
|                       |     |        | aaa group | server  | tacacs  | sg1            |
| DeletingaTACACS       |     | server |           |         |         |                |
| serverfromaserver-    |     |        | no server | 1.1.1.2 | port    | 32 vrf default |
group
ConfiguringaTACACS+ tacacs-server key tacacs-server key plaintext mypasskey123
globalpasskey
| ConfiguringPAPor     |     | tacacs-server | tacacs-server    |     | auth-type | chap |
| -------------------- | --- | ------------- | ---------------- | --- | --------- | ---- |
| CHAPforTACACS+       |     | auth-type     | no tacacs-server |     | auth-type |      |
| Configuringthe       |     | tacacs-server | tacacs-server    |     | timeout   | 20   |
| TACACS+globaltimeout |     |               | no tacacs-server |     | timeout   |      |
timeout
| TACACS+ | authentication |     |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- |
TACACS+authenticationoccursasfollows:
n UsercredentialsaresentfromtheswitchtoTACACS+serverusingthePAPorCHAPauthentication
protocol.
n Ifauserisauthenticated,theirroleiscommunicatedtotheswitchasAdministrator,Operator,orAuditor.
n Anunknownuserorauserwhoenteredaninvalidpasswordisidentifiedassuchtotheswitch,which
thenrejectsuserlogin.
| About authentication |     | fail-through |     |     |     |     |
| -------------------- | --- | ------------ | --- | --- | --- | --- |
RemoteAAAwithTACACS+|74

Normally,authenticationisperformedbythefirstAAAserverreached.Ararelyneededfeaturenamed
"Authenticationfail-through"isavailable.IfAuthenticationfail-throughisenabledandauthenticationfails
onthefirstreachableAAAserver,authenticationisattemptedonthesecondAAAserver,andsoon,until
successfulauthenticationortheserverlistisexhausted.
EnablingAuthenticationfail-throughistypicallyunnecessarybecausetheusercredentialdatabasesshould
beconsistentacrossallAAAservers.Authenticationfail-throughmightbehelpfulifyourAAAusercredential
databasesarenotquicklysynchronizedacrossallAAAservers.
| TACACS+ | authentication | tasks |     |     |     |
| ------- | -------------- | ----- | --- | --- | --- |
TheTACACS+authentication-relatedtasksareasfollows:
Command
| Task |     | Example |     |     |     |
| ---- | --- | ------- | --- | --- | --- |
name
Configuring aaa aaa authentication login default group tg1 tg2 tacacs local
the
authentication
| authentication | login |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- |
sequencefor
thedefault
connection
type
Configuring aaa aaa authentication login console group tg2 tg3 tacacs local
| the            | authentication |     |     |     |     |
| -------------- | -------------- | --- | --- | --- | --- |
| authentication | login          |     |     |     |     |
sequencefor
theconsole
connection
type
|                |                | aaa authentication | login ssh | group tg2 | tacacs local |
| -------------- | -------------- | ------------------ | --------- | --------- | ------------ |
| Configuring    | aaa            |                    |           |           |              |
| the            | authentication |                    |           |           |              |
| authentication | login          |                    |           |           |              |
sequencefor
thessh
connection
type
|               |                | no aaa authentication | login | default |     |
| ------------- | -------------- | --------------------- | ----- | ------- | --- |
| Removing      | aaa            |                       |       |         |     |
| remoteAAA     | authentication |                       |       |         |     |
| forthedefault | login          |                       |       |         |     |
connection
type
|                |                | aaa authentication    | allow-fail-through |     |     |
| -------------- | -------------- | --------------------- | ------------------ | --- | --- |
| Configuring    | aaa            |                       |                    |     |     |
|                |                | no aaa authentication | allow-fail-through |     |     |
| authentication | authentication |                       |                    |     |     |
| fail-through   | allow-fail-    |                       |                    |     |     |
through
show aaa authentication
| Showingthe     | show aaa       |     |     |     |     |
| -------------- | -------------- | --- | --- | --- | --- |
| authentication | authentication |     |     |     |     |
sequence
| TACACS+ | authorization |     |     |     |     |
| ------- | ------------- | --- | --- | --- | --- |
Uponsuccessfuluserauthentication,theuserisassignedtheirrolebytheTACACS+server.SeealsoUser
roleassignmentusingTACACS+attributes.
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 75

TACACS+ authorization provides command filtering to allow/disallow individual command or command set
execution. Each command is sent to the TACACS+ server for approval, and the switch then allows/disallows
command execution according to the server response.

TACACS+ authorization applies only to the CLI interface.

Using local authorization as fallback from TACACS+ authorization

Local authorization can be used for the situation in which communication is lost with all TACACS+ servers
after a successful authentication. Users that are members of the built-in local user groups (administrators,
operators, or auditors) are authorized according to the fixed roles and privilege levels of those groups.
Optionally, local user-defined user groups can be configured with specific command execution rules per
group. Users that are members of such groups, are authorized according to the command execution rules
of the group to which they belong. For configuring local user groups, see user-group.

About authentication fail-through and authorization

For authorization, there is no equivalent of the authentication fail-through feature. Therefore, if the first
reachable TACACS+ server responds with "Authorization Denied," no additional TACACS+ servers are
interrogated.

Rare potential out-of-synchronization situation when using authentication fail-through: Successful authentication

on one server can be followed by authorization denial on another. The user is known on the server doing the

authentication but unknown on the server attempting the authorization. This situation typically arises only during

brief periods in which user credential databases are not synchronized across all TACACS+ servers. See also

TACACS+ server authorization considerations in aaa authorization commands .

TACACS+ authorization tasks

The TACACS+ authorization-related tasks are as follows:

Task

Command
name

Example

aaa authorization commands default group tg1 tacacs local

aaa authorization commands console group tg1 tg2 tacacs none

aaa
authorization
commands

aaa
authorization
commands

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

Remote AAA with TACACS+ | 76

Task

Command
name

Example

Removing
remote AAA
for the
default
connection
type

Showing the
TACACS+
authorization
sequence

aaa
authorization
commands

no aaa authorization commands default

show aaa
authorization

show aaa authorization

TACACS+ accounting
This accounting information is captured and made available for sending to remote accounting servers:

n Exec Accounting: user login/logout events.

n Command accounting: commands executed by users.

n System accounting: remote accounting On/Off events.

n CLI show commands.

n Interactions on the non-CLI interfaces: REST and WebUI.

The following is not captured or made available as accounting information:

n CLI commands that reboot the switch.

n Interactions in the bash shell.

Local accounting (always enabled) must be functioning properly for remote Accounting to work.

The accounting information is sent to the first reachable remote TACACS+ AAA server (configured for remote

accounting). If no remote TACACS+ server is reachable, local accounting remains available.

Sample accounting information on a TACACS+ server

Mon May 9 17:52:32 10.10.11.1 UNKNOWN tty 0.0.0.0 start task_id=1525899775430
timezone=UTC start_time=1525913552.428 service=system event=sys_acct
reason="System-accounting-ON" result=success
Mon May 9 17:52:48 10.10.11.1 admin tty 192.168.1.20 start task_id=1525899775431
timezone=UTC start_time=1525913567.611 service=shell priv_lvl=15 result=success
Mon May 9 17:52:48 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775432
timezone=UTC stop_time=1525913567.614 service=shell priv_lvl=15 cmd="enable"
result=success
Mon May 9 17:52:51 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775433
timezone=UTC stop_time=1525913570.851 service=shell priv_lvl=15 cmd="configure"
result=success
Mon May 9 17:52:53 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775434
timezone=UTC stop_time=1525913573.427 service=shell priv_lvl=15 cmd="interface
1/1/3" result=success
Mon May 9 17:52:54 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775435

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

77

timezone=UTC stop_time=1525913574.447 service=shell priv_lvl=15 cmd="no shutdown"
result=success
Mon May 9 17:52:58 10.10.11.1 admin tty 192.168.1.20 stop task_id=1525899775436
timezone=UTC stop_time=1525913578.131 service=shell priv_lvl=15 cmd="ip address
| 10.10.13.1/24" | result=success |     |     |     |     |     |     |
| -------------- | -------------- | --- | --- | --- | --- | --- | --- |
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
| reason="System-accounting-OFF" |     |     | result=success |     |     |     |     |
| ------------------------------ | --- | --- | -------------- | --- | --- | --- | --- |
ThissampleisrepresentativeandnotfromanyparticularTACACS+serverimplementation.
| Sample | REST accounting |     | information | on  | a TACACS+ | server |     |
| ------ | --------------- | --- | ----------- | --- | --------- | ------ | --- |
Oct 30 16:31:56 10.10.10.1 admin tty 127.0.0.1 start task_id=1540942055868
timezone=UTC start_time=1540942316.36 service=https-server priv_lvl=15
| cmd="http-method=POST |     | http-uri=/rest/v1/login" |     | result=success |     |     |     |
| --------------------- | --- | ------------------------ | --- | -------------- | --- | --- | --- |
ThissampleisrepresentativeandnotfromanyparticularTACACS+serverimplementation.
| TACACS+ | accounting | tasks |     |     |     |     |     |
| ------- | ---------- | ----- | --- | --- | --- | --- | --- |
TheTACACS+accounting-relatedtasksareasfollows:
Comman
| Task |     | Example |     |     |     |     |     |
| ---- | --- | ------- | --- | --- | --- | --- | --- |
dname
|             |           | aaa   | accounting all-mgmt | default | start-stop | group tg1 | tg2 tacacs |
| ----------- | --------- | ----- | ------------------- | ------- | ---------- | --------- | ---------- |
| Configuring | aaa       |       |                     |         |            |           |            |
| the         | accountin | local |                     |         |            |           |            |
| accounting  | g all-    |       |                     |         |            |           |            |
sequence
mgmt
forthe
default
connection
type
Configuring aaa aaa accounting all-mgmt console start-stop group tg2 tg3 tacacs
| the | accountin | local |     |     |     |     |     |
| --- | --------- | ----- | --- | --- | --- | --- | --- |
accounting
g all-
sequence
mgmt
forthe
console
connection
type
RemoteAAAwithTACACS+|78

Task

Configuring
the
accounting
sequence
for the ssh
connection
type

Removing
remote AAA
for the
default
connection
type

Showing the
accounting
configuratio
n

Comman
d name

aaa
accountin
g all-
mgmt

aaa
accountin
g all-
mgmt

show aaa
accountin
g

Example

aaa accounting all-mgmt ssh start-stop group tg2 tacacs local

no aaa accounting all-mgmt default start-stop

show aaa accounting

Example: Configuring the switch for Remote AAA with
TACACS+

Prerequisites

n TACACS+ servers configured in general according to the information in Remote AAA TACACS+ server

configuration requirements . The exact settings appropriate to your environment will vary.

n Logged in to the switch with Administrator privilege and in the config context.

Procedure

1. Configure the global TACACS+ passkey (shared secret) as "xjkW74932qX3j_$"

switch(config)# tacacs-server key plaintext xjkW74932qX3j_$
switch(config)#

2. Add these configuration details for two remote TACACS+ servers:

n Server 1 with IPv4 address 10.0.0.2, on the management interface (belonging to VRF “mgmt”),

using the default PAP protocol.

n Server 2 with IPv4 address 4.0.0.2, on the data interface (belonging to VRF “default”), using the

CHAP protocol.

switch(config)# tacacs-server host 10.0.0.2 vrf mgmt
switch(config)# tacacs-server host 4.0.0.2 auth-type chap
switch(config)#

3. Create a TACACS+ group named tac_grp1, assign TACACS+ server 10.0.0.2 to the group, show the

group information.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

79

ThedefaultTACACS+groupnamedtacacsincludeseveryTACACS+serverregardlessof
whetheranyTACACS+serversarealsoassignedtoauser-definedTACACS+group.
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
4. DefinetheauthenticationsequencelistsothatthenewTACACS+groupisfirst,thedefaultTACACS+
groupissecond,andlocalisthird.Showtheauthenticationsequence.
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
------------------------------------------------------------------------------
---
| GROUP NAME |     |     |     |     | | GROUP | PRIORITY |     |     |
| ---------- | --- | --- | --- | --- | ------- | -------- | --- | --- |
------------------------------------------------------------------------------
---
| tac_grp1 |     |     |     |     | | 0 |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| tacacs   |     |     |     |     | | 1 |     |     |     |
| local    |     |     |     |     | | 2 |     |     |     |
------------------------------------------------------------------------------
---
switch(config)#
5. DefinetheauthorizationsequencelistwithtwoTACACS+servergroupspluslocalRBAC.Showthe
authorizationsequence.
switch(config)# aaa authorization commands default group tac_grp1 tacacs local
switch(config)#
| switch(config)# |     | do            | show aaa | authorization |     |           |     |     |
| --------------- | --- | ------------- | -------- | ------------- | --- | --------- | --- | --- |
| Default command |     | Authorization |          | for           | All | Channels: |     |     |
------------------------------------------------------------------------------
RemoteAAAwithTACACS+|80

---
| GROUP NAME |     | | GROUP PRIORITY |     |
| ---------- | --- | ---------------- | --- |
-------------------------------------------------------------------------------
--
| tac_grp1 |     | | 0 |     |
| -------- | --- | --- | --- |
| tacacs   |     | | 1 |     |
| local    |     | | 2 |     |
-------------------------------------------------------------------------------
--
switch(config)#
6. DefinetheaccountingsequencelistwithtwoTACACS+servergroups.Showtheaccountingsequence.
switch(config)# aaa accounting all default start-stop group tac_grp1 tacacs
switch(config)#
| switch(config)# | do show aaa | accounting |     |
| --------------- | ----------- | ---------- | --- |
AAA Accounting:
| Accounting         | Type    |           | : all        |
| ------------------ | ------- | --------- | ------------ |
| Accounting         | Mode    |           | : start-stop |
| Default Accounting | for All | Channels: |              |
-------------------------------------------------------------------------------
--
| GROUP NAME |     | | GROUP PRIORITY |     |
| ---------- | --- | ---------------- | --- |
-------------------------------------------------------------------------------
--
| tac_grp1 |     | | 0 |     |
| -------- | --- | --- | --- |
| tacas    |     | | 1 |     |
-------------------------------------------------------------------------------
--
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 81

Chapter 9
|        |          |        |     | Remote | AAA with | RADIUS |
| ------ | -------- | ------ | --- | ------ | -------- | ------ |
| Remote | AAA with | RADIUS |     |        |          |        |
RemoteAAAprovidesthefollowingforyourArubaswitch:
AuthenticationusingremoteRADIUSAAAservers.Foraddedsecurity,two-factorauthenticationmaybe
n
used.Intwo-factorauthentication,X.509certificate-basedauthenticationiscombinedwithRADIUS
authentication.
n CommandauthorizationisnotsupportedbyRADIUSservers,however,user-definedlocalusergroups
canbeconfiguredwithcommand-authorizationrules,providinglocallyconfiguredper-command
authorizationformembersofsuchgroups.SeeUser-definedusergroups.
Intheswitchdefaultstate(withoutuser-definedlocalgroups),basicrole-basedauthorizationisavailable
withthethreebuilt-inroles(administrators,operators,auditors).
TransmissionoflocallycollectedaccountinginformationtoremoteRADIUSservers.
n
Forswitchesthatsupportmultiplemanagementmodules,allAAAfunctionalitydiscussedonlyappliestotheactive
managementmodule.SeealsoAAAonswitcheswithmultiplemanagementmodulesintheHighAvailabilityGuide.
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
Theorderinwhichserversareaddedtoagroupisimportant.Theserveraddedfirstisaccessedfirst,andif
necessary,thesecondserverisaccessedsecond,andsoon.
| Remote                       | AAA | (RADIUS) | defaults      | and limits |     |     |
| ---------------------------- | --- | -------- | ------------- | ---------- | --- | --- |
| Setting                      |     |          | Default value | / limit    |     |     |
| MaximumnumberofRADIUSservers |     |          | 16            |            |     |     |
inanAAAgroup
| MaximumnumberofRADIUSservers |     |     | 16  |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- |
thatcanbeconfigured
82
| AOS-CX10.07SecurityGuide| | (6200,6300,6400SwitchSeries) |     |     |     |     |     |
| ------------------------- | ---------------------------- | --- | --- | --- | --- | --- |

| Setting                     |     |     | Default | value / limit |     |     |
| --------------------------- | --- | --- | ------- | ------------- | --- | --- |
| Maximumnumberofuser-defined |     |     | 28      |               |     |     |
AAAservergroupsthatcanbe
configured
| RADIUSauthentication              |     |     | Disabled |     |     |     |
| --------------------------------- | --- | --- | -------- | --- | --- | --- |
| RADIUSauthenticationglobaltimeout |     |     | 5seconds |     |     |     |
| RADIUSauthenticationpasskey       |     |     | None     |     |     |     |
(sharedsecret)
| RADIUSauthenticationudp-port       |     |     | 1812       |     |     |     |
| ---------------------------------- | --- | --- | ---------- | --- | --- | --- |
| RADIUSglobalauthenticationprotocol |     |     | PAP        |     |     |     |
| RADIUSglobalretries                |     |     | 1retry     |     |     |     |
| RADIUSservertrackingdefault        |     |     | 300seconds |     |     |     |
interval
RADIUSserveraccessthroughthe
default*
defaultVRF
*Thedefaultvalueisdefault,unlessanotherVRFisspecifiedduringtheserverconfiguration.
| About | global | versus | per-RADIUS | server | passkeys | (shared |
| ----- | ------ | ------ | ---------- | ------ | -------- | ------- |
secrets)
TocommunicatewithaRADIUSAAAserver,theswitchmusthaveapasskey(sharedsecret)configuredthat
matcheswhatisconfiguredontheserver.Useoneofthesecommandstoachievethedesired
configuration:
ForaglobalpasskeycommontoeveryRADIUSserver,useradius-server key.
n
Foraper-RADIUSserverpasskey,useradius-server hostwiththekeyparameter.
n
Ifbothpasskeysareconfiguredontheswitch,theper-RADIUSserverpasskeyisused.
| Remote | AAA | RADIUS | server | configuration | requirements |     |
| ------ | --- | ------ | ------ | ------------- | ------------ | --- |
Theuser-suppliedRADIUSservermust:
n HaveanIPv4/IPv6addressorfullyqualifieddomainname(FQDN)thatisvisibletotheswitch.
Haveapasskey(sharedsecret)thatmatcheswhatisconfiguredontheswitch.
n
Provideusernameandpassworddefinitionsforeveryswitchuser.Remoteusersdonotrequire
n
definitionontheswitch.
ConfigureuserroleassignmentusingRADIUSattributes.
n
ConsultyourRADIUSserverdocumentationforinstallationandgeneralconfigurationdetails.
RemoteAAAwithRADIUS|83

IfSSHpublickeyauthenticationisused,thekeyinformationisstoredlocallyontheswitch,makingusernameand
passworddefinitionontheRADIUSserverunnecessary.
| User role | assignment | using | RADIUS | attributes |     |
| --------- | ---------- | ----- | ------ | ---------- | --- |
UserroleassignmentisconfiguredontheRADIUSserverusingVSAs(vendor-specificattributes).
RADIUSserverscanreturnmultipleattributevaluepairs(AVPs)inresponsetoanauthenticationrequest.
Theattributesareprocessedinthisorderofprecedencetodeterminetheuserroleassigned:
n IftheAruba-Admin-RoleVSAispresent,maptheusertothematchinglocaluser-groupname.
o ElseiftheAruba-Priv-Admin-UserVSAispresent,extracttheprivilegelevel(1,15,or19)andmapthe
usertothelocaluser-groupcorrespondingtothisprivilegelevel(1=operators,15=administrators,
19=auditors).Privilegelevels2to14mayalsobeusedwithmatchinglocalusergroupsnamed2to
14.
l ElseIfService-TypeAVPispresent,mapAdministrative-User(6)toadministratorsandmap
NAS-Prompt-User(7)tooperators.
l Otherwise,theuserrolecannotbedetermined,andtheauthenticationfails.
| This is      | summarized | as follows:       |              |     |                   |
| ------------ | ---------- | ----------------- | ------------ | --- | ----------------- |
| Aruba-Admin- |            | Aruba-Priv-Admin- |              |     |                   |
|              |            |                   | service-type |     | Userrole assigned |
| Role         |            | User              |              |     |                   |
| <GROUP-NAME> |            | Donotcare         | Donotcare    |     | Matchinglocaluser |
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
| Notpresent |     | Notpresent | NAS-Prompt-User(7) |     | Operators      |
| ---------- | --- | ---------- | ------------------ | --- | -------------- |
| Notpresent |     | Notpresent | Notpresent(or=any  |     | None(not       |
|            |     |            | othervalue)        |     | authenticated) |
TheService-Typeattributeisretainedonlyforbackwardcompatibility.Itisrecommendedthatyouinsteaduse
theAruba-Admin-RoleorAruba-Priv-Admin-UserVSA.
| RADIUS | server | redundancy | and access | sequence |     |
| ------ | ------ | ---------- | ---------- | -------- | --- |
Topreventauthenticationinterruption,itiscommonpracticetoconfiguremorethanoneRADIUSserver.
WhenidentifyingRADIUSserverstotheswitch,servergrouporder(andserverorderwithinthegroup),
determinesserveraccessorder.
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 84

Whendefiningtheserveraccesssequenceforauthenticationwithaaa authentication login default,there
isanimpliedlocalincludedasthelastiteminthelist.IfnoRADIUSservercanbereached,localauthentication
willbeattempted.
| Single         | source | IP address | for     | consistent |     | source |     |     |
| -------------- | ------ | ---------- | ------- | ---------- | --- | ------ | --- | --- |
| identification |        | to AAA     | servers |            |     |        |     |     |
Ifapplicabletoyourinstallation,itisrecommendedthatyouperformtheoptionalconfigurationmentionedinthis
section.
IfyourtopologyallowstheAAAservertobereachedthroughmultiplepaths,theserverinterpretsthe
incomingpacketstobefromdifferentswitcheseventhoughtheyareallcomingfromthesameswitch.
HavingaswitchassociatedwithmultipleIPaddressesmakesitmoredifficulttointerpretsystemlogsand
accountingdata.
ToensurethatalltrafficsentfromtheswitchtotheAAAserverusesthesamesourceIPaddress,useip
source-interfaceoripv6 source-interface.Thesetwocommandsplustherelatedcommandsshow
ip
source-interfaceandshow ipv6 source-interfacearedescribedunderLayer2/3Interfacecommandsin
theCommand-LineInterfaceGuide.
| RADIUS | general | tasks |     |     |     |     |     |     |
| ------ | ------- | ----- | --- | --- | --- | --- | --- | --- |
GeneralRADIUStasks,notspecifictoauthentication,areasfollows:
| Task |     | Commandname |     | Example |     |     |     |     |
| ---- | --- | ----------- | --- | ------- | --- | --- | --- | --- |
ConfiguringaRADIUS radius-server radius-server host 1.1.1.1 vrf default
| server           |     | host         |     | no radius-server   |     | host   | 1.1.1.1 | vrf default |
| ---------------- | --- | ------------ | --- | ------------------ | --- | ------ | ------- | ----------- |
| Showingglobaland |     | show radius- |     | show radius-server |     | detail |         |             |
| RADIUSserver     |     | server       |     |                    |     |        |         |             |
configurations
ConfiguringaRADIUS aaa group server aaa group server radius sg3
| servergroup         |     |          |         | no aaa   | group server  |     | radius | sg3 |
| ------------------- | --- | -------- | ------- | -------- | ------------- | --- | ------ | --- |
| Showingservergroups |     | show aaa | server- | show aaa | server-groups |     |        |     |
groups
|                     |     |        |     | aaa group | server  | radius | sg3    |         |
| ------------------- | --- | ------ | --- | --------- | ------- | ------ | ------ | ------- |
| AddingaRADIUSserver |     | server |     |           |         |        |        |         |
|                     |     |        |     | server    | 1.1.1.4 | port   | 32 vrf | default |
toaserver-group
| DeletingaRADIUS    |     | server |     | aaa group | server  | tacacs | sg3    |         |
| ------------------ | --- | ------ | --- | --------- | ------- | ------ | ------ | ------- |
| serverfromaserver- |     |        |     | no server | 1.1.1.4 | port   | 32 vrf | default |
group
ConfiguringaRADIUS radius-server key radius-server key plaintext mypasskey123
globalpasskey
ConfiguringPAPorCHAP radius-server radius-server auth-type chap
|           |     |           |     | no radius-server |     | auth-type |     |     |
| --------- | --- | --------- | --- | ---------------- | --- | --------- | --- | --- |
| forRADIUS |     | auth-type |     |                  |     |           |     |     |
RemoteAAAwithRADIUS|85

| Task                 |     | Commandname   | Example          |            |
| -------------------- | --- | ------------- | ---------------- | ---------- |
| ConfiguringtheRADIUS |     | radius-server | radius-server    | timeout 15 |
|                      |     |               | no radius-server | timeout    |
| globaltimeout        |     | timeout       |                  |            |
|                      |     |               | radius-server    | retries 3  |
| ConfiguringtheRADIUS |     | radius-server |                  |            |
| globalretries        |     | retries       | no radius-server | retries    |
Overridingtheglobal radius-server radius-server host 1.1.1.1 retries 2
| retriesforaRADIUS |     | host |     |     |
| ----------------- | --- | ---- | --- | --- |
server
| RADIUS | authentication |     |     |     |
| ------ | -------------- | --- | --- | --- |
RADIUSauthenticationoccursasfollows:
UsercredentialsaresentfromtheswitchtoRADIUSserverusingthePAPorCHAPauthentication
n
protocol.
Ifauserisauthenticated,theirroleiscommunicatedtotheswitchasAdministrator,Operator,orAuditor.
n
Anunknownuserorauserwhoenteredaninvalidpasswordisidentifiedassuchtotheswitch,which
n
thenrejectsuserlogin.
| About | authentication | fail-through |     |     |
| ----- | -------------- | ------------ | --- | --- |
Normally,authenticationisperformedbythefirstAAAserverreached.Ararelyneededfeaturenamed
"Authenticationfail-through"isavailable.IfAuthenticationfail-throughisenabledandauthenticationfails
onthefirstreachableAAAserver,authenticationisattemptedonthesecondAAAserver,andsoon,until
successfulauthenticationortheserverlistisexhausted.
EnablingAuthenticationfail-throughistypicallyunnecessarybecausetheusercredentialdatabasesshould
beconsistentacrossallAAAservers.Authenticationfail-throughmightbehelpfulifyourAAAusercredential
databasesarenotquicklysynchronizedacrossallAAAservers.
| RADIUS | authentication | tasks |     |     |
| ------ | -------------- | ----- | --- | --- |
TheRADIUSauthentication-relatedtasksareasfollows:
Command
| Task |     | Example |     |     |
| ---- | --- | ------- | --- | --- |
name
Configuring aaa aaa authentication login default group rg1 rg2 radius local
the
authenticatio
| authenticatio | n login |     |     |     |
| ------------- | ------- | --- | --- | --- |
nsequence
forthedefault
connection
type
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 86

Task

Configuring
the
authenticatio
n sequence
for the https-
server
connection
type

Removing
remote AAA
for the default
connection
type

Configuring
authenticatio
n fail-through

Command
name

aaa
authenticatio
n login

aaa
authenticatio
n login

aaa
authenticatio
n allow-fail-
through

Example

aaa authentication login https-server group rg1 radius
local

no aaa authentication login default

aaa authentication allow-fail-through
no aaa authentication allow-fail-through

Showing the
authenticatio
n sequence

show aaa
authenticatio
n

show aaa authentication

Configuring two-factor authentication

Two-factor authentication is available for added security. In two-factor authentication, X.509 certificate-
based authentication is combined with RADIUS authentication. When a user establishes an SSH connection
to the switch, two factor-authentication occurs as follows:

n The username in the user's X.509 certificate is validated against the local user accounts on the switch.

n The username and password are validated against the accounts on the RADIUS server and the

configured trust anchors.

Prerequisites

n The switch SSH server is enabled.

n Your switch management computer, though its SSH client, is connected to the switch.

n A remote RADIUS server is available to authenticate switch users and is configured on the switch.

n Every user that will use two-factor authentication is configured both on the RADIUS server and locally on
the switch using identical usernames. Users are added locally on the switch with the user command.
These usernames must precisely match the usernames identified by the X.509 user certificates.

n The X.509 CA certificate is both installed on your switch management computer and is also visible to
your computer's SSH client. The X.509 CA certificate is the root of trust for the client certificate being
used.

n One X.509 certificate per user is available on your switch management computer and is visible to your
computer's SSH client. The usernames identified by these user certificates must be the same as the
usernames already defined on the RADIUS server and locally on the switch.

Procedure

Remote AAA with RADIUS | 87

1. CreateaTAprofilewiththecommandcrypto pki ta-profile.ThiscommandswitchestotheTA
configurationcontext.TheTAprofileiswheretheswitchstorestherootcertificateoftheCAthatis
usedtovalidatethecertificatesofclientscommunicatingwiththeSSHserver.
2. Althoughoptional,itisrecommendedthatyouenablecertificaterevocationcheckingwiththe
| commandrevocation-check |     |     |     | ocsp. |     |     |     |     |
| ----------------------- | --- | --- | --- | ----- | --- | --- | --- | --- |
3. ImporttherootcertificateoftheCAwiththecommandta-certificate.
4. ExittheTAconfigurationcontextwiththecommandexit.
5. Foreachuserthatwillbeusingtwo-factorauthentication,importthepublickeyfromtheindividual
X.509usercertificatewiththecommanduser <USERNAME> authorized-key <PUBKEY>.Eachuser
identifiedby<USERNAME>mustexistlocallyontheswitchandontheRADIUSauthenticationserver.
6. Enabletwo-factorauthenticationwiththecommandssh two-factor-authentication.
Example
Thisexampleinstallstherootcertificateroot-certandenablestwo-factorauthenticationforuseradmin:
| switch(config)#              |     | crypto | pki | ta-profile       |     | root-cert |      |     |
| ---------------------------- | --- | ------ | --- | ---------------- | --- | --------- | ---- | --- |
| switch(config-ta-root-cert)# |     |        |     | revocation-check |     |           | ocsp |     |
switch(config-ta-root-cert)#
ta-certificate
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-ta-cert)# |     |     |     | -----BEGIN |     | CERTIFICATE----- |     |     |
| ----------------------- | --- | --- | --- | ---------- | --- | ---------------- | --- | --- |
switch(config-ta-cert)# MIIDuTCCAqECCQCuoxeJ2ZNYcjANBgkqhkiG9w0BAQsFADCBq
switch(config-ta-cert)# VVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEDAOBgNVBAcMB1JvY
switch(config-ta-cert)# BAoMA0hQTjEVMBMGA1UECwwMSFBOUm9zZXZpbGxlMSowKAYDV
...
switch(config-ta-cert)# x3WFf3dFZ8o9sd5LVAHneH/ztb9MP34z+le1V346r12L2MDL8
switch(config-ta-cert)# BIzD/ST/HaWI+0S+S80rm93PSscEbb9GWk7vshh5E8DH73nW/
switch(config-ta-cert)# 3LvMLZcssSe5J2Ca2XIhfDme8UaNZ7syGYoCD/TMsAW0nG7yY
| switch(config-ta-cert)# |     |     |     | -----END | CERTIFICATE----- |     |     |     |
| ----------------------- | --- | --- | --- | -------- | ---------------- | --- | --- | --- |
switch(config-ta-cert)#
| The     | certificate | you    | are        | importing | has        | the | following | attributes: |
| ------- | ----------- | ------ | ---------- | --------- | ---------- | --- | --------- | ----------- |
| Issuer: | C=US,       | ST=CA, | L=Rocklin, |           | O=Company, |     | OU=Site,  |             |
CN=site.com/emailAddress=test.ca@site.com
| Subject: | C=US, | ST=CA, | L=Rocklin, |     | O=Company, |     | OU=Site, |     |
| -------- | ----- | ------ | ---------- | --- | ---------- | --- | -------- | --- |
CN=8400/emailAddress=test.ca@site.com
| Serial                       | Number: | 12121221634631568498 |      |             |     | (0xaea51217d5945772) |     |     |
| ---------------------------- | ------- | -------------------- | ---- | ----------- | --- | -------------------- | --- | --- |
| Do you                       | want    | to accept            | this | certificate |     | (y/n)?               | y   |     |
| TA certificate               |         | accepted.            |      |             |     |                      |     |     |
| switch(config-ta-root-cert)# |         |                      |      | exit        |     |                      |     |     |
switch(config)#
| switch(config)# |     | user | admin | authorized-key |     |     | ssh-rsa |     |
| --------------- | --- | ---- | ----- | -------------- | --- | --- | ------- | --- |
AAAAB3NzaC1yc2EAAAADAQABAAACAQC6krLTrFTnzg3YjLiZKTZEYnh4cUiuOK+cjduxFnZUa
...
iAfcGvqvWtWWBSoWd011DeEZNKnOO8uEKeTEcAjfrnRHeOk2QJmw== "sv1@site.net"
switch(config)#
| switch(config)# |        | ssh | two-factor-authentication |     |     |     |     |     |
| --------------- | ------ | --- | ------------------------- | --- | --- | --- | --- | --- |
| Secure          | RADIUS |     | (RadSec)                  |     |     |     |     |     |
RADIUSprotocolusesUDPasunderlyingtransportlayerprotocol.RadSecisaprotocolthatsupports
RADIUSoverTCPandTLS.InconventionalRADIUSrequests,securityisaconcernastheconfidentialdatais
sentusingweakencryptionalgorithms.Theaccessrequestsareinplaintextincludesinformationsuchas
username,IPaddressandsoon.Theuserpasswordisanencryptedsharedsecret.Asaresult,
eavesdropperscanlistentotheseRADIUSrequestsandcollectconfidentialinformation.Dataprotectionis
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 88

necessary in roaming environments where the RADIUS packets travel across multiple administrative
domains and untrusted networks.

RadSec module secures the communication between the switch and RADIUS server using TLS connection.
Using RADIUS over TLS provides users with the flexibility to host RADIUS servers across geographies and
WAN networks.

For enabling RADIUS security, a CLI option tls is provided with the command radius-server host, where
tls stands for Transport Layer Security.

Advantages:

n Secures the communication between the switch and RADIUS server using a TLS session.

n Provides flexibility and enhances security to host RADIUS servers across geographies and WAN networks.

n Uses digital certificates to authenticate both client and server connection.

RadSec configuration

To configure RadSec protocol, use the following commands:

n Configure TLS using the command radius-server host tls.

n Associate the leaf certificate with RadSec feature (radsec-client) using the command crypto pki

application. To use switch inbuilt IDEVID certificate, add device-identity with the command crypto
pki application. By default, switch uses the local certificate for Radsec application. For more
information on installing certificates, see PKI chapter.

RadSec mandates validating server certificates SAN/CN while establishing connections.

Deployment scenarios

You can deploy the RADIUS/TLS servers in any of the following scenarios:

n Scenario 1: Switch establishes TLS connection with the RADIUS server.

n Scenario 2: Switch establishes TLS connection with the proxy server, which communicates with the

RADIUS server.

Figure 1 Scenario 1: Switch establishes TLS connection with the RADIUS server

In this scenario, the RADIUS server is across WAN. The RADIUS/TLS secures the user data by creating an
encrypted TLS tunnel between the switch and authentication server.

Remote AAA with RADIUS | 89

Figure 2 Scenario 2: Switch establishes TLS connection with the proxy server, which communicates with the
RADIUS server

In this scenario, multiple RADIUS servers are distributed over WAN (untrusted networks). RADIUS proxy
directs the RADIUS requests to the RADIUS server, which listens on UDP. The proxy server uses the switch
certificates to authenticate the client-server credentials. As a result, all RADIUS communications across the
network are TLS encrypted.

Example of RadSec configuration

Prerequisite

n ClearPass version is 6.7.4 or higher.

ClearPass as RadSec server

Following are the steps to configure ClearPass as RadSec server:

1. From the ClearPass Web UI, navigate to Administration > Certificates >Certificate store and

click Import Certificate to import the Root CA certificate to the ClearPass certificate store.

2. The Import Certificate window opens. In the Certificate Type field, select Server Certificate.

Specify the server and upload method. In the Usage field, you must select Radsec Server

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

90

Certificate.

3. Click Import.

4. next, click Create Certificate Signing Request. In the Common Name field, enter the IP address

of the ClearPass server. For configuring radius-server host , enter the hostname.

5. Click Submit. You can download the CSR or copy and paste the displayed CSR content into the web

form in the enrollment process.

6. Sign the created CSR with the CA.

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

Remote AAA with RADIUS | 91

WithRADIUS,commandaccountinglogsamaximumof247characterspercommandenteredbytheuser.
Thefollowingisnotcapturedormadeavailableasaccountinginformation:
n CLIcommandsthatreboottheswitch.
n Interactionsinthebashshell.
Localaccounting(alwaysenabled)mustbefunctioningproperlyforremoteAccountingtowork.
TheaccountinginformationissenttothefirstreachableremoteRADIUSAAAserver(configuredforremote
accounting).IfnoremoteRADIUSserverisreachable,localaccountingremainsavailable.
| Sample | port access | accounting | information |     |
| ------ | ----------- | ---------- | ----------- | --- |
rad_recv: Accounting-Request packet from host 2005::1 port 35513, id=112, length=190
|          | User-Name             | = "user32"            |                  |      |
| -------- | --------------------- | --------------------- | ---------------- | ---- |
|          | Calling-Station-Id    | = "00-0A-0A-00-40-00" |                  |      |
|          | Acct-Authentic        | = RADIUS              |                  |      |
|          | Service-Type          | = Framed-User         |                  |      |
|          | NAS-Port-Type         | = Ethernet            |                  |      |
|          | NAS-Port-Id           | = "1/1/5"             |                  |      |
|          | NAS-Port              | = 5                   |                  |      |
|          | Acct-Session-Id       | = "1571684206266"     |                  |      |
|          | Acct-Status-Type      | = Interim-Update      |                  |      |
|          | Acct-Input-Octets     | = 735624              |                  |      |
|          | Acct-Output-Octets    | = 2348060             |                  |      |
|          | Acct-Input-Packets    | = 10818               |                  |      |
|          | Acct-Output-Packets   | =                     | 26476            |      |
|          | Acct-Input-Gigawords  | =                     | 0                |      |
|          | Acct-Output-Gigawords |                       | = 0              |      |
|          | Acct-Session-Time     | = 183013              |                  |      |
|          | Called-Station-Id     | = "38-21-C7-5D-4A-40" |                  |      |
|          | NAS-Identifier        | = "switchz"           |                  |      |
|          | NAS-IP-Address        | = 205.1.1.1           |                  |      |
|          | NAS-IPv6-Address      | = 2005::1             |                  |      |
| Sample   | general               | accounting            | information      |      |
| ~~~~~~~~ | EXEC                  | ~~~~~~~~~~            |                  |      |
| Mon      | Jul 16 16:25:27       | 2018                  |                  |      |
|          | User-Name             | = "admin"             |                  |      |
|          | NAS-Identifier        | = "switchx"           |                  |      |
|          | NAS-Port              | = 331                 |                  |      |
|          | NAS-Port-Type         | = Virtual             |                  |      |
|          | Acct-Status-Type      | = Start               |                  |      |
|          | Acct-Session-Id       | = "1531769192494"     |                  |      |
|          | Acct-Authentic        | = Local               |                  |      |
|          | Calling-Station-Id    | = "0.0.0.0"           |                  |      |
|          | Event-Timestamp       | = "Jul                | 16 2018 16:25:22 | PDT" |
|          | Acct-Delay-Time       | = 0                   |                  |      |
|          | NAS-IP-Address        | = 10.10.10.1          |                  |      |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 92

| Acct-Unique-Session-Id |     |     | = "b83e29f4140c17b1" |     |
| ---------------------- | --- | --- | -------------------- | --- |
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
| NAS-Port-Type          |     | = Virtual         |                      |      |
| ---------------------- | --- | ----------------- | -------------------- | ---- |
| Acct-Status-Type       |     | = Accounting-On   |                      |      |
| Acct-Session-Id        |     | = "1531769192506" |                      |      |
| Acct-Authentic         |     | = Local           |                      |      |
| Calling-Station-Id     |     | = "0.0.0.0"       |                      |      |
| Event-Timestamp        |     | = "Jul            | 16 2018 17:12:56     | PDT" |
| Acct-Delay-Time        |     | = 0               |                      |      |
| NAS-IP-Address         |     | = 10.10.10.1      |                      |      |
| Acct-Unique-Session-Id |     |                   | = "b478e6402c86933e" |      |
Timestamp = 1531786382
| Mon Jul 16 | 17:12:55 2018 |     |     |     |
| ---------- | ------------- | --- | --- | --- |
User-Name = "UNKNOWN"
| NAS-Identifier |     | = "UNKNOWN" |     |     |
| -------------- | --- | ----------- | --- | --- |
NAS-Port = 331
| NAS-Port-Type |     | = Virtual |     |     |
| ------------- | --- | --------- | --- | --- |
RemoteAAAwithRADIUS|93

|     | Acct-Status-Type       | =                 | Accounting-Off |                    |      |     |     |     |
| --- | ---------------------- | ----------------- | -------------- | ------------------ | ---- | --- | --- | --- |
|     | Acct-Session-Id        | = "1531769192491" |                |                    |      |     |     |     |
|     | Acct-Authentic         | = Local           |                |                    |      |     |     |     |
|     | Calling-Station-Id     |                   | = "0.0.0.0"    |                    |      |     |     |     |
|     | Event-Timestamp        | = "Jul            | 16             | 2018 17:12:49      | PDT" |     |     |     |
|     | Acct-Delay-Time        | = 0               |                |                    |      |     |     |     |
|     | NAS-IP-Address         | = 10.10.10.1      |                |                    |      |     |     |     |
|     | Acct-Unique-Session-Id |                   | =              | "93da1f094121f2ee" |      |     |     |     |
|     | Timestamp              | = 1531786375      |                |                    |      |     |     |     |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ThissampleisrepresentativeandnotfromanyparticularRADIUSserverimplementation.
| RADIUS | accounting | tasks |     |     |     |     |     |     |
| ------ | ---------- | ----- | --- | --- | --- | --- | --- | --- |
TheRADIUSaccounting-relatedtasksareasfollows:
Comman
| Task |     | Example |     |     |     |     |     |     |
| ---- | --- | ------- | --- | --- | --- | --- | --- | --- |
dname
|             |     | aaa accounting |     | all-mgmt | default | start-stop | group rg1 | rg2 radius |
| ----------- | --- | -------------- | --- | -------- | ------- | ---------- | --------- | ---------- |
| Configuring | aaa |                |     |          |         |            |           |            |
local
| the        | accountin |     |     |     |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| accounting | g all-    |     |     |     |     |     |     |     |
sequence
mgmt
forthe
default
connection
type
Configuring aaa aaa accounting all-mgmt https-server start-stop group rg1 radius
| the | accountin | local |     |     |     |     |     |     |
| --- | --------- | ----- | --- | --- | --- | --- | --- | --- |
accounting
g all-
sequence
mgmt
forthe
https-server
connection
type
| Removing  | aaa       | no aaa | accounting | all-mgmt | default | start-stop |     |     |
| --------- | --------- | ------ | ---------- | -------- | ------- | ---------- | --- | --- |
| remoteAAA | accountin |        |            |          |         |            |     |     |
forthe
g all-
default
mgmt
connection
type
| Showingthe | show aaa  | show | aaa accounting |     |     |     |     |     |
| ---------- | --------- | ---- | -------------- | --- | --- | --- | --- | --- |
| accounting | accountin |      |                |     |     |     |     |     |
configuratio
g
n
| Example: | Configuring |     | the | switch | for | Remote | AAA | with |
| -------- | ----------- | --- | --- | ------ | --- | ------ | --- | ---- |
RADIUS
Prerequisites
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 94

RADIUSserversconfiguredingeneralaccordingtotheinformationinRemoteAAARADIUSserver
n
configurationrequirements.Theexactsettingsappropriatetoyourenvironmentwillvary.
n LoggedintotheswitchwithAdministratorprivilegeandintheconfigcontext.
Procedure
1. ConfiguretheglobalRADIUSpasskey(sharedsecret)as"xjkW74932qX3j_$"
| switch(config)# |     | radius-server | key | plaintext | xjkW74932qX3j_$ |     |     |
| --------------- | --- | ------------- | --- | --------- | --------------- | --- | --- |
switch(config)#
2. AddtheseconfigurationdetailsfortworemoteRADIUSservers.
n Server1withIPv4address10.0.0.2,onthemanagementinterface(belongingtoVRF“mgmt”),
usingthedefaultPAPprotocol.
Server2withIPv4address4.0.0.2,onthedatainterface(belongingtoVRF“default”),usingthe
n
CHAPprotocol.
| switch(config)# |     | radius-server | host | 10.0.0.2 | vrf mgmt  |      |     |
| --------------- | --- | ------------- | ---- | -------- | --------- | ---- | --- |
| switch(config)# |     | radius-server | host | 4.0.0.2  | auth-type | chap |     |
switch(config)#
3. CreateaRADIUSgroupnamedrad_grp1,assignRADIUSserver10.0.0.2tothegroup,showthe
groupinformation.
ThedefaultRADIUSgroupnamedradiusincludeseveryRADIUSserverregardlessofwhether
anyRADIUSserversarealsoassignedtoauser-definedRADIUSgroup.
| switch(config)#    |     | aaa group | server   | radius | rad_grp1 |     |     |
| ------------------ | --- | --------- | -------- | ------ | -------- | --- | --- |
| switch(config-sg)# |     | server    | 10.0.0.2 | vrf    | mgmt     |     |     |
| switch(config-sg)# |     | exit      |          |        |          |     |     |
switch(config)#
| switch(config)# |           | do show | aaa server-groups |     | radius |     |     |
| --------------- | --------- | ------- | ----------------- | --- | ------ | --- | --- |
| ******* AAA     | Mechanism | RADIUS  | *******           |     |        |     |     |
-------------------------------------------------------------------------
| GROUP NAME |     | | SERVER | NAME |     | | PORT | | VRF | | PRIORITY |
| ---------- | --- | -------- | ---- | --- | ------ | ----- | ---------- |
-------------------------------------------------------------------------
| rad_grp1 |     | | 10.0.0.2 |     |     | | 1812 | | mgmt | | 1 |
| -------- | --- | ---------- | --- | --- | ------ | ------ | --- |
-------------------------------------------------------------------------
| radius (default) |     | | 10.0.0.2 |     |     | | 1812 | | mgmt    | | 1 |
| ---------------- | --- | ---------- | --- | --- | ------ | --------- | --- |
| radius (default) |     | | 4.0.0.2  |     |     | | 1812 | | default | | 2 |
-------------------------------------------------------------------------
switch(config)#
4. DefinetheauthenticationsequencelistsothatthenewRADIUSgroupisfirst,thedefaultRADIUS
groupissecond,andlocalisthird.Showtheauthenticationsequence.
switch(config)# aaa authentication login default group rad_grp1 radius local
switch(config)#
| switch(config)# |     | do show | aaa authentication |     |     |     |     |
| --------------- | --- | ------- | ------------------ | --- | --- | --- | --- |
RemoteAAAwithRADIUS|95

AAA Authentication:
| Fail-through           |                 |               | : Disabled |
| ---------------------- | --------------- | ------------- | ---------- |
| Limit Login            | Attempts        |               | : Not set  |
| Lockout                | Time            |               | : 300      |
| Minimum                | Password Length |               | : Not set  |
| Default Authentication | for             | All Channels: |            |
-------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP | PRIORITY |
| ---------- | --- | ------- | -------- |
-------------------------------------------------------------------------------
| rad_grp1 |     | | 0 |     |
| -------- | --- | --- | --- |
| radius   |     | | 1 |     |
| local    |     | | 2 |     |
-------------------------------------------------------------------------------
switch(config)#
5. DefinetheaccountingsequencelistwithtwoRADIUSservergroups.Showtheaccountingsequence.
switch(config)# aaa accounting all default start-stop group rad_grp1 radius
switch(config)#
| switch(config)# | do show aaa | accounting |     |
| --------------- | ----------- | ---------- | --- |
AAA Accounting:
| Accounting         | Type    |           | : all        |
| ------------------ | ------- | --------- | ------------ |
| Accounting         | Mode    |           | : start-stop |
| Default Accounting | for All | Channels: |              |
------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP | PRIORITY |
| ---------- | --- | ------- | -------- |
------------------------------------------------------------------------------
| rad_grp1 |     | | 0 |     |
| -------- | --- | --- | --- |
| radius   |     | | 1 |     |
------------------------------------------------------------------------------
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 96

Chapter 10

Remote AAA (TACACS+, RADIUS)
commands

Remote AAA (TACACS+, RADIUS) commands

aaa accounting all-mgmt

Syntax

aaa accounting all-mgmt <CONNECTION-TYPE> start-stop {local | group <GROUP-LIST>}
no aaa accounting all-mgmt <CONNECTION-TYPE>

Description

Defines accounting as being local (with the name local) (the default). Or defines a sequence of remote AAA
server groups to be accessed for accounting purposes.

For remote accounting, the information is sent to the first reachable remote server that was configured with
this command for remote accounting. If no remote server is reachable, local accounting remains available.
Each available connection type (channel) can be configured individually as either local or using remote AAA
server groups. All server groups named in your command, must exist. This command can be issued multiple
times, once for each connection type. Local is always available for any connection type not configured for
remote accounting.

The system accounting log is not associated with any connection type (channel) and is therefore sent to the

accounting method configured on the default connection type (channel) only.

The no form of this command removes for the specified connection type, any defined remote AAA server
group accounting sequence. Local accounting is available for connection types without a configured remote
AAA server group list (whether default or for the specific connection type).

Command context

config

Parameters

<CONNECTION-TYPE>

One of these connection types (channels):

default

Defines a list of accounting server groups to be used for the default connection type. This
configuration applies to all other connection types (console, https-server, ssh) that are not explicitly
configured with this command. For example, if you do not use aaa accounting all-mgmt
console... to define the console accounting list, then this default configuration is used for console.

console

Defines a list of accounting server groups to be used for the console connection type.

https-server

Defines a list of accounting server groups to be used for the https-server (REST, Web UI) connection
type.

ssh

Defines a list of accounting server groups to be used for the ssh connection type.

start-stop

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

97

Selects accounting information capture at both the beginning and end of a process.

local

Selects local-only accounting when used without the group parameter.

group <GROUP-LIST>

Specifies the list of remote AAA server group names. Each name can be specified one time. Predefined
remote AAA group names tacacs and radius are available. Although not a group name, predefined
name local is available. User-defined TACACS+ and RADIUS server group names may also be used. The
remote AAA server groups are accessed in the order that the group names are listed in this command.
Within each group, the servers are accessed in the order in which the servers were added to the group.
Server groups are defined using command aaa group server and servers are added to a server group
with the command server.

Authority

Administrators or local user group members with execution rights for this command.

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

Defining the https-server accounting sequence based on one user-defined RADIUS server group and then
the default RADIUS server group.

switch(config)# aaa accounting all-mgmt https-server start-stop group rg1 radius

Setting local accounting for the default connection type:

Remote AAA (TACACS+, RADIUS) commands | 98

| switch(config)# | aaa | accounting  |     | all-mgmt | default | start-stop | local |
| --------------- | --- | ----------- | --- | -------- | ------- | ---------- | ----- |
| aaa accounting  |     | port-access |     |          | (RADIUS | only)      |       |
Syntax
Generalsyntaxdefinition:
aaa accounting port-access {start-stop {{local | group <GROUP-NAME>} |{interim <INTERVAL>
group <GROUP-NAME>}}}
aaa accounting port-access {stop-only {local | group <GROUP-NAME>}}
| no aaa accounting | port-access |     | [local | | group | | interim] |     |     |
| ----------------- | ----------- | --- | ------ | ------- | ---------- | --- | --- |
Listofallpossiblesyntaxforthiscommand:
| aaa accounting | port-access |     | start-stop | local |              |     |     |
| -------------- | ----------- | --- | ---------- | ----- | ------------ | --- | --- |
| aaa accounting | port-access |     | start-stop | group | <GROUP-NAME> |     |     |
aaa accounting port-access start-stop interim <INTERVAL> group <GROUP-NAME>
| aaa accounting    | port-access |     | stop-only | local |              |     |     |
| ----------------- | ----------- | --- | --------- | ----- | ------------ | --- | --- |
| aaa accounting    | port-access |     | stop-only | group | <GROUP-NAME> |     |     |
| no aaa accounting | port-access |     |           |       |              |     |     |
| no aaa accounting | port-access |     | local     |       |              |     |     |
| no aaa accounting | port-access |     | group     |       |              |     |     |
| no aaa accounting | port-access |     | interim   |       |              |     |     |
Description
Configuresportaccessaccountinginformationthatiscapturedfor802.1XandMAC-authenticatedclients.
Definesportaccessaccountingasbeinglocal(withtheparameterlocal)(thedefault).Ordefinesport
accessaccountingasbeingremote(withtheparametergroup <GROUP-NAME>)withasequenceofremote
RADIUSserversinasingleRADIUSservergrouptobeaccessedforportaccessaccountingpurposes.
ForremoteRADIUSportaccessaccounting,theinformationissenttothefirstreachableremoteRADIUS
serverinthespecifiedgroup.Ifauser-definedRADIUSservergroupisnamedinyourcommand,itmust
exist.
Thenoformofthiscommandworksasfollows:
port-access:Globallyunconfiguresportaccessaccounting.
| n no aaa accounting |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
n no aaa accounting port-access local:Unconfigureslocalportaccessaccounting.
n no aaa accounting port-access group:Unconfiguresremoteportaccessaccounting.
n no aaa accounting port-access interim:Unconfiguresinterimaccountingupdates.
Commandcontext
config
Parameters
start-stop
Selectsaccountinginformationcapturefromthepointatwhichtheclientisauthenticateduntiltheclient
disconnects.
stop-only
Selectsaccountinginformationcaptureonlyatthetimewhenaclientdisconnects.
local
Selectslocal-onlyaccounting.
group <GROUP-NAME>
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 99

Specifies a single RADIUS server group, either the built-in group named radius or a user-defined RADIUS
server group. Only one RADIUS server group name can be provided.

interim <INTERVAL>

Enables interim accounting updates (between the start and stop) and specifies the interval at which the
interim updates will be provided. Default: 60 minutes. Range: 1 to 525600 minutes.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring start-stop port access local accounting:

switch(config)# aaa accounting port-access start-stop local

Configuring start-stop port access remote accounting using the built-in radius server group:

switch(config)# aaa accounting port-access start-stop group radius

Configuring start-stop port access remote accounting using the built-in radius server group and enabling
interim accounting updates with an interval of 60 minutes:

switch(config)# aaa accounting port-access start-stop interim 60 group radius

Configuring stop-only port access remote accounting using the built-in radius server group:

switch(config)# aaa accounting port-access stop-only group radius

Unconfiguring remote port access accounting:

switch(config)# no aaa accounting port-access group

aaa authentication allow-fail-through

Syntax

aaa authentication allow-fail-through
no aaa authentication allow-fail-through

Description

Enables authentication fail-through. When this option is enabled, the next server/authentication method is
tried after an authentication failure.

The no form of this command disables authentication fail-through. If the system fails to authenticate with a
reachable TACACS+ or RADIUS server, the system does not attempt to authenticate with the next
TACACS+/RADIUS server.

Command context

config

Remote AAA (TACACS+, RADIUS) commands | 100

Authority

Administrators or local user group members with execution rights for this command.

Example

Enabling authentication fail-through:

switch(config)# aaa authentication allow-fail-through

aaa authentication login

Syntax

aaa authentication login <CONNECTION-TYPE> {local | group <GROUP-LIST>}
no aaa authentication login <CONNECTION-TYPE>

Description

Defines authentication as being local (with the name local) (the default). Or defines a sequence of remote
AAA server groups to be accessed for authentication purposes. Each available connection type (channel) can
be configured individually as either local or using remote AAA server groups. All server groups named in your
command, must exist. This command can be issued multiple times, once for each connection type. Local is
always available for any connection type not configured for remote AAA authentication.

If you do not want local authentication to occur in cases where all AAA servers contacted reject the user's
credentials, do not enable authentication fail-through (command aaa authentication allow-fail-through).

The no form of this command removes for the specified connection type, any defined remote AAA server
group authentication sequence. Local authentication is available for connection types without a configured
remote AAA server group list (whether default or for the specific connection type).

Command context

config

Parameters

<CONNECTION-TYPE>

One of these connection types (channels):
default

Defines a list of authentication server groups to be used for the default connection type. This
configuration applies to all other connection types (console, https-server, ssh) that are not explicitly
configured with this command. For example, if you do not use aaa authentication login
console... to define the console authentication list, then this default configuration is used for
console.

console

Defines a list of authentication server groups to be used for the console connection type.

https-server

Defines a list of authentication server groups to be used for the https-server (REST, Web UI)
connection type.

ssh

Defines a list of authentication server groups to be used for the ssh connection type.

local

Selects local-only authentication when used without the group parameter.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

101

group <GROUP-LIST>

Specifies the list of remote AAA server group names. Each name can be specified one time. Predefined
remote AAA group names tacacs and radius are available. Although not a group name, predefined
name local is available. User-defined TACACS+ and RADIUS server group names may also be used. The
remote AAA server groups are accessed in the order that the group names are listed in this command.
Within each group, the servers are accessed in the order in which the servers were added to the group.
Server groups are defined using command aaa group server and servers are added to a server group
with the command server.

If no AAA server is reachable, local authentication is attempted.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defining the default authentication sequence based on two user-defined TACACS+ server groups, then the
default TACACS+ server group, and finally (if needed), local authentication.

switch(config)# aaa authentication login default group tg1 tg2 tacacs local

Defining the console authentication sequence based on two user-defined TACACS+ server groups, then the
default TACACS+ server group, and finally (if needed), local authentication.

switch(config)# aaa authentication login console group tg2 tg3 tacacs local

Defining the ssh authentication sequence based on one user-defined TACACS+ server group and then the
default TACACS+ server group.

switch(config)# aaa authentication login ssh group tg2 tacacs

Defining the default authentication sequence based on two user-defined RADIUS server groups, then the
default RADIUS server group, and finally (if needed), local authentication.

switch(config)# aaa authentication login default group rg1 rg2 radius local

Defining the https-server authentication sequence based on one user-defined RADIUS server group and
then the default RADIUS server group.

switch(config)# aaa authentication login https-server group rg1 radius

Setting local authentication for the default connection type:

switch(config)# aaa authentication login default local

aaa authorization commands

Syntax

Remote AAA (TACACS+, RADIUS) commands | 102

aaa authorization commands <CONNECTION-TYPE> {local | none}
aaa authorization commands <CONNECTION-TYPE> group <GROUP-LIST>

no aaa authorization commands <CONNECTION-TYPE>

Description

Defines authorization as being basic local RBAC (specified as none), or as full-fledged local RBAC specified as
local (the default), or as remote TACACS+ (specified with group <GROUP-LIST>). Each available connection
type (channel) can be configured individually. All server groups named in the command, must exist. This
command can be issued multiple times, once for each connection type.

The no form of this command unconfigures authorization for the specified connection type, reverting to the
default of local.

Although only TACACS+ servers are supported for remote authorization, local authorization (basic or full-fledged)

can be used with remote RADIUS authentication.

Command context

config

Parameters

<CONNECTION-TYPE>

One of these connection types (channels):
default

Selects the default connection type for configuration. This configuration applies to all other
connection types (console, ssh) that are not explicitly configured with this command. For example, if
you do not use aaa authorization commands console... to define the console authorization list,
then this default configuration is used for console.

console

Selects the console connection type for configuration.

ssh

Selects the ssh connection type for configuration.

local (the default)

When used alone without group <GROUP-LIST>, selects local authorization which can be used to provide
authorization for a purely local setup without any remote AAA servers and also for when RADIUS is used
for remote Authentication and Accounting but Authorization is local.

When used after group, provides for fallback (to full-fledged local authorization) when every server in
every specified TACACS+ server group cannot be reached.

If any TACACS+ server in the specified groups is reachable, but the command fails to be authorized by that server,

the command is rejected and local authorization is never attempted. Local authorization is only attempted if every

TACACS+ server cannot be reached.

none

When used alone without group <GROUP-LIST>, selects basic local RBAC authorization, for use with the
built-in user groups (administrators, operators, auditors).

When used after group, provides for fallback (to basic local RBAC authorization) when every server in
every specified TACACS+ server group cannot be reached.

With none, for users belonging to user-defined user groups, all commands can be executed regardless of what
authorization rules are defined in such groups. For per-command local authorization, use local instead.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

103

group <GROUP-LIST>

Specifies the list of remote AAA server group names. Predefined remote AAA group name tacacs is
available. User-defined TACACS+ server group names may also be used. The remote AAA server groups
are accessed in the order that the group names are listed in this command. Within each group, the
servers are accessed in the order in which the servers were added to the group. Server groups are
defined using command aaa server group and servers are added to a server group using command
server.

It is recommended to always include either the special name local or none as the last name in the group
list. If both local and none are omitted, and no remote AAA server is reachable (or the first reachable
server cannot authorize the command), command execution for the current user will not be possible.

Authority

Administrators or local user group members with execution rights for this command.

Usage

TACACS+ server authorization considerations

Use caution when configuring authorization, as it has no fail through. If the switch is not configured properly, the

switch might get into an unusable state in which all command execution is prohibited.

To prevent authorization difficulties:

n Make sure that all listed TACACS+ servers can authorize users for command execution.

n Make sure that credential database changes are promptly synchronized across all TACACS+ servers.

n Make sure either local or none is included as the last name in the group list. If both local and none are
omitted, and no remote TACACS+ server is reachable (or the first reachable server cannot authorize),
authorization will not be possible.

n Although not recommended, if you choose to omit both local and none from the list, and are

manipulating configuration files, special caution is necessary. If the source configuration includes
TACACS⁠+ authorization and you are copying configuration from an existing switch into the running
configuration of a new switch, and you have not yet configured the interface or routing information to
reach the TACACS+ server, the switch will enter an unusable state, requiring hard reboot.

To avoid getting into this situation that can occur when local and none have been omitted, do either of
the following:

o In the configuration source, delete or comment-out the line configuring remote authorization. Then,

after the configuration copy and paste, manually configure authorization.

o Move the line configuring the authorization to the end of the source configuration before copying and

pasting.

Examples

Defining the default authorization sequence based on a user-defined TACACS+ server group, then the
default TACACS+ server group, and finally (as a precaution), local authorization:

switch(config)# aaa authorization commands default group tg1 tacacs local
All commands will fail if none of the servers in the group list are reachable.
Continue (y/n)? y

Defining the console authorization sequence based on two user-defined TACACS+ server groups, and finally
(as a precaution), local authorization:

Remote AAA (TACACS+, RADIUS) commands | 104

switch(config)# aaa authorization commands console group tg1 tg2 local
All commands will fail if none of the servers in the group list are reachable.
| Continue | (y/n)? | y   |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- |
Settingtheauthorizationfordefaulttolocal:
| switch(config)# |     | aaa authorization |     | commands | default | local |
| --------------- | --- | ----------------- | --- | -------- | ------- | ----- |
SettingtheauthorizationfortheSSHinterfacetonone:
| switch(config)# |       | aaa authorization |     | commands | ssh | none |
| --------------- | ----- | ----------------- | --- | -------- | --- | ---- |
| aaa             | group | server            |     |          |     |      |
Syntax
| aaa group | server       | {tacacs | | radius} | <SERVER-GROUP-NAME> |     |     |
| --------- | ------------ | ------- | --------- | ------------------- | --- | --- |
| no aaa    | group server | {tacacs | | radius} | <SERVER-GROUP-NAME> |     |     |
Description
CreatesanAAAservergroupthatiseitheremptyorcontainspreconfiguredRADIUS/TACACS+servers.You
cancreateamaximumof28servergroups.
Thenoformofthiscommanddeletesaservergroup.Onlyapreconfigureduser-definedRADIUS/TACACS+
servergroupcanbedeleted.RADIUSorTACACS+serversthatwereinadeletedservergroupremainapart
oftheirdefaultservergroup.ThedefaultservergroupforTACACS+serversistacacs.Thedefaultserver
groupforRADIUSserversisradius.
Commandcontext
config
Parameters
| server | {tacacs | | radius} |     |     |     |     |
| ------ | --------- | ------- | --- | --- | --- | --- |
Selecteithertacacsorradiusfortheservertype.
<SERVER-GROUP-NAME>
Specifiesthenameoftheservergrouptobecreated.Thenameoftheservergroupcanhaveamaximum
of32characters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreatingTACACS+servergroupsg1:
| switch(config)# |     | aaa group | server | tacacs | sg1 |     |
| --------------- | --- | --------- | ------ | ------ | --- | --- |
CreatingRADIUSservergroupsg3:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 105

| switch(config)# | aaa | group | server radius | sg3 |
| --------------- | --- | ----- | ------------- | --- |
DeletingTACACS+servergroupsg1:
| switch(config)# | no  | aaa group | server tacacs | sg1 |
| --------------- | --- | --------- | ------------- | --- |
DeletingRADIUSservergroupsg3:
| switch(config)# | no  | aaa group | server radius | sg3 |
| --------------- | --- | --------- | ------------- | --- |
| radius-server   |     | auth-type |               |     |
Syntax
| radius-server    | auth-type | {pap | | chap} |     |
| ---------------- | --------- | ---- | ------- | --- |
| no radius-server | auth-type |      |         |     |
Description
EnablestheCHAPorPAPauthenticationprotocol,whichisusedforcommunicationwiththeRADIUS
servers,atthegloballevel.Youcanoverridethiscommandwithafine-grainedperserverauth-type
configuration.
ThenoformofthiscommandresetstheglobalauthenticationmechanismforRADIUStoPAP,whichisthe
defaultauthenticationmechanismforRADIUS.
Commandcontext
config
Parameters
| auth-type {pap | | chap} |     |     |     |
| -------------- | ------- | --- | --- | --- |
SelectseitherthePAPorCHAPauthenticationprotocol.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
AuthenticatingCHAP:
| switch(config)# | radius-server |     | auth-type | chap |
| --------------- | ------------- | --- | --------- | ---- |
AuthenticatingPAP:
| switch(config)# | radius-server |      | auth-type | pap |
| --------------- | ------------- | ---- | --------- | --- |
| radius-server   |               | host |           |     |
Syntax
RemoteAAA(TACACS+,RADIUS)commands|106

radius-server host {<FQDN> | <IPV4> | <IPV6>}

[key [plaintext <PASSKEY> | ciphertext <PASSKEY>]]
[timeout <TIMEOUT-SECONDS>] [port <PORT-NUMBER>]
[auth-type {pap | chap}] [acct-port <ACCT-PORT>] [retries <RETRY-COUNT>]
[tracking {enable | disable}] [tracking-mode {any | dead-only}][vrf <VRF-NAME>]

no radius-server host {<FQDN> | <IPV4> | <IPV6>} [port <PORT-NUMBER>] [vrf <VRF-NAME>]

Description

Adds a RADIUS server. By default, the RADIUS server is associated with the server group named radius.

The no form of this command removes a previously added RADIUS server.

For enhanced security with IPsec, the alternative command radius-server host secure ipsec is available.
The standard non-IPsec radius-server host command does not modify any existing IPsec configuration. If
IPsec is already configured for the RADIUS server, then IPsec will remain enabled for the server.

Command context

config

Parameters

{<FQDN> | <IPV4> | <IPv6>}

Specifies the RADIUS server as:

n <FQDN>: a fully qualified domain name.

n <IPV4>: an IPv4 address.

n <IPV6>: an IPv6 address.

key [plaintext <PASSKEY> | ciphertext <PASSKEY>]

Specifies either a plaintext or an encrypted local shared-secret passkey for the server. As per RFC 2865,
the shared-secret can be a mix of alphanumeric and special characters. Plaintext passkeys are between 1
and 32 alphanumeric and special characters.

When key is entered without either sub-parameter, plaintext passkey prompting occurs upon pressing Enter.
Enter must be pressed immediately after the key parameter without entering other parameters. The entered
passkey characters are masked with asterisks.
When key is omitted, the server uses the global passkey. This command requires either the global or local
passkey to be set; otherwise the server will not be contacted. Command radius-server key is available for
setting the global passkey.

timeout <TIMEOUT-SECONDS>

Specifies the timeout. The range is 1 to 60 seconds. If a timeout is not specified, the value from the
global timeout for RADIUS is used.

port <PORT-NUMBER>

Specifies the authentication port number. Range: 1 to 65535. Default RADIUS: 1812.

auth-type {pap | chap}

Selects either PAP (default) or CHAP authentication type. If this parameter is not specified, the RADIUS
global default is used.
acct-port <ACCT-PORT>

Specifies the UDP accounting port number. Range: 1 to 65535. Default: 1813.

retries <RETRY-COUNT>

Specifies the number of retry attempts for contacting the specified RADIUS server. Range is 0 to 5
attempts. If no retry value is provided, the default value of 1 is used.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

107

| tracking {enable | | disable} |     |     |     |
| ---------------- | ---------- | --- | --- | --- |
EnablesordisablesservertrackingfortheRADIUSserver.Trackedserversareprobedatthestartofeach
servertrackingintervaltocheckiftheyarereachable.
Usecommandradius-server trackingtoconfigureRADIUSservertrackingglobally.
Servertrackingusesauthenticationrequestandresponsepacketstodetermineserverreachabilitystatus.The
servertrackingusernameandpasswordareusedtoformtherequestpacketwhichissenttotheserverwith
trackingenabled.Uponreceivingaresponsetotherequestpacket,theserverisconsideredtobereachable.
| tracking-mode | {any | dead-only} |     |     |     |
| ------------- | ----------------- | --- | --- | --- |
ConfigurestrackingmodefortheRADIUSserverthathastrackingenabledwiththeserver.Thetracking
modeisusedtomonitorthestatusofRADIUSserverreachability.Thedefaulttrackingmodeisany.
Setsthetrackingmodeto:
n any:tracktheRADIUSserverirrespectiveofitsserverreachability.
n dead-only:tracktheRADIUSserveronlywhentheserverismarkedasunreachable.
vrf VRF-NAME>
SpecifiestheVRFnametobeusedforcommunicatingwiththeserver.IfnoVRFnameisprovided,the
defaultVRFnameddefaultisused.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
IfthefullyqualifieddomainnameisprovidedfortheRADIUSserver,aDNSservermustbeconfiguredand
accessiblethroughthesameVRFwhichisconfiguredfortheRADIUSserver.Thisconfigurationisrequired
fortheresolutionoftheRADIUSserverhostnametoitsIPaddress.IfaDNSserverisnotavailableforthis
VRF,theRADIUSserversreachablethroughthisVRFmustbeconfiguredbymeansoftheirIPaddresses
only.
Examples
AddingaRADIUSserverwithanIPv4addressandapromptedpasskey:
| switch(config)# | radius-server     | host 1.1.1.5   | key |     |
| --------------- | ----------------- | -------------- | --- | --- |
| Enter the       | RADIUS server     | key: ********* |     |     |
| Re-Enter        | the RADIUS server | key: ********* |     |     |
AddingaRADIUSserverwithanIPv4addressandanamedVRF:
| switch(config)# | radius-server | host 1.1.1.1 | vrf mgmt |     |
| --------------- | ------------- | ------------ | -------- | --- |
AddingaRADIUSserverwithanIPv4address,aport,andanamedVRF:
| switch(config)# | radius-server | host 1.1.1.2 | port 32 vrf | mgmt |
| --------------- | ------------- | ------------ | ----------- | ---- |
RemoteAAA(TACACS+,RADIUS)commands|108

Adding a RADIUS server with an FQDN, a timeout, port number, and a named VRF:

switch(config)# radius-server host abc.com timeout 15 port 32 vrf vrf_blue

Adding a RADIUS server with an IPv6 address:

switch(config)# radius-server host 2001:0db8:85a3:0000:0000:8a2e:0370:7334

Adding a RADIUS server with tracking enabled and tracking mode is set to dead-only:

switch(config)# radius-server host 1.1.1.1 tracking enable tracking-mode dead-only

Adding a RADIUS server with tracking disabled:

switch(config)# radius-server host 1.1.1.1 tracking disable

Adding a RADIUS server with an IPv4 address, key, encrypted passkey, number of retries, and VRF name:

switch(config)# radius-server host 1.1.1.6 key ciphertext AQBapStbgHt1X2JlbcEcQl
xbbzWjrFr9UsfH3+00x5Qj0qcQBAAAAJ5WZBQ= retries 3 vrf vrf_red

Deleting a RADIUS server with an IPv4 address and specified VRF:

switch(config)# no radius-server host 1.1.1.1 vrf mgmt

Deleting a RADIUS server with an FQDN, port, and specified VRF:

switch(config)# no radius-server host abc.com port 32 vrf vrf_blue

radius-server host (ClearPass)

Syntax

radius-server host {<FQDN> | <IPV4> | <IPV6>} clearpass-username <CP-USERNAME>

clearpass-password [plaintext <PLAINTEXT-PASSWORD> | ciphertext <CIPHERTEXT-PASSWORD>]

Description

Configures the ClearPass username and password for a radius server.

Command context

config

Parameters

{<FQDN> | <IPV4> | <IPv6>}

Specifies the RADIUS server as:

n <FQDN>: a fully qualified domain name.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

109

n <IPV4>: an IPv4 address.

n <IPV6>: an IPv6 address.

clearpass-username <CP-USERNAME>

Specifies the ClearPass username.

clearpass-password plaintext <PLAINTEXT-PASSWORD>

Specifies the password as plaintext. The password is visible as cleartext when entered but is encrypted
thereafter. Command history does show the password as cleartext.

clearpass-password ciphertext <CIPHERTEXT-PASSWORD>

Specifies the password as Base64 ciphertext.

When clearpass-password is entered without a following sub-parameter, plaintext password prompting occurs
upon pressing Enter. The entered password characters are masked with asterisks.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring a ClearPass username and password for a radius server with a plaintext password:

switch(config)# radius-server host 1.1.1.2 clearpass-username admn1

clearpass-password plaintext uni@#1

Configuring a ClearPass username and password for a radius server with a prompted plaintext password:

switch(config)# radius-server host 1.1.1.3 clearpass-username op clearpass-password
Enter the ClearPass server password: *********
Re-Enter the ClearPass server password: *********

Configuring a ClearPass username and password for a radius server with a ciphertext password:

switch(config)# radius-server host 1.1.1.4 clearpass-username bx clearpass-password

ciphertext AQBpXz13c1U1Jt7KMjAIOgjE/lPDfgrYxT6SCi+Di2B+CAAAOnPZmUvMVpq

radius-server host secure ipsec

Syntax

Syntax for a RADIUS server that uses IPsec for authentication:
radius-server host {<FQDN> | <IPV4> | <IPV6>}

[key [plaintext <PASSKEY> | ciphertext <PASSKEY>]]
[timeout <TIMEOUT-SECONDS>] [port <PORT-NUMBER>]
[auth-type {pap | chap}] [acct-port <ACCT-PORT>] [retries <RETRY-COUNT>]
[tracking {enable | disable}] [tracking-mode {any | dead-only}] [vrf <VRF-NAME>]
secure ipsec authentication spi <SPI-INDEX> <AUTH-TYPE> <AUTH-KEY-TYPE> [<AUTH-KEY>]

no radius-server host {<FQDN> | <IPV4> | <IPV6>} [port <PORT-NUMBER>]

[vrf <VRF-NAME>] secure ipsec authentication

Syntax for a RADIUS server that uses IPsec for both authentication and encryption:

Remote AAA (TACACS+, RADIUS) commands | 110

| radius-server   | host               | {<FQDN>   | |   | <IPV4>       | | <IPV6>}      |     |
| --------------- | ------------------ | --------- | --- | ------------ | -------------- | --- |
| [key [plaintext |                    | <PASSKEY> |     | | ciphertext | <PASSKEY>]]    |     |
| [timeout        | <TIMEOUT-SECONDS>] |           |     | [port        | <PORT-NUMBER>] |     |
[auth-type {pap | chap}] [acct-port <ACCT-PORT>] [retries <RETRY-COUNT>]
[tracking {enable | disable}] [tracking-mode {any | dead-only}] [vrf <VRF-NAME>]
secure ipsec encryption spi <SPI-INDEX> <AUTH-TYPE> <AUTH-KEY-TYPE>
| [<AUTH-KEY>] |     | <ENCRYPT-TYPE> |     | <ENCRYPT-KEY-TYPE> |     | [<ENCRYPT-KEY>] |
| ------------ | --- | -------------- | --- | ------------------ | --- | --------------- |
no radius-server host {<FQDN> | <IPV4> | <IPV6>} [port <PORT-NUMBER>]
| [vrf <VRF-NAME>] |     | secure | ipsec | encryption |     |     |
| ---------------- | --- | ------ | ----- | ---------- | --- | --- |
Description
AddsaRADIUSserverthatusesIPsecforenhancedsecurity(authenticationandpossiblyencryption).By
default,theRADIUSserverisassociatedwiththeservergroupnamedradius.
ThenoformofthiscommandremovesapreviouslyaddedRADIUS(withIPsec)server.
UnlessenhancedsecuritywithIPsecisrequired,usetheradius-server hostcommandinstead.
Commandcontext
config
Parameters
| {<FQDN> | <IPV4> |     | | <IPv6>} |     |     |     |     |
| ---------------- | --- | --------- | --- | --- | --- | --- |
SpecifiestheRADIUSserveras:
<FQDN>:afullyqualifieddomainname.
n
<IPV4>:anIPv4address.
n
<IPV6>:anIPv6address.
n
| key [plaintext |     | <PASSKEY> | |   | ciphertext | <PASSKEY>] |     |
| -------------- | --- | --------- | --- | ---------- | ---------- | --- |
Selectseitheraplaintextoranencryptedlocalshared-secretpasskeyfortheserver.AsperRFC2865,
shared-secretcanbeamixofalphanumericandspecialcharacters.Plaintextpasskeysarebetween1and
32alphanumericandspecialcharacters.
Whenkeyisenteredwithouteithersub-parameter,plaintextpasskeypromptingoccursuponpressingEnter.
Entermustbepressedimmediatelyafterthekeyparameterwithoutenteringotherparameters.Theentered
passkeycharactersaremaskedwithasterisks.
Whenkeyisomitted,theserverusestheglobalpasskey.Thiscommandrequireseithertheglobalorlocal
passkeytobeset;otherwisetheserverwillnotbecontacted.Commandradius-server keyisavailablefor
settingtheglobalpasskey.
| timeout <TIMEOUT-SECONDS> |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- |
Specifiesthetimeout.Therangeis1to60seconds.Ifatimeoutisnotspecified,thevaluefromthe
globaltimeoutforRADIUSisused.
port <PORT-NUMBER>
Specifiestheauthenticationportnumber.Range:1to65535.Default:1812.
| auth-type {pap | |   | chap} |     |     |     |     |
| -------------- | --- | ----- | --- | --- | --- | --- |
SelectseitherthePAP(thedefault)orCHAPauthenticationtypes.Ifthisparameterisnotspecified,the
RADIUSglobaldefaultisused.
| acct-port | <ACCT-PORT> |     |     |     |     |     |
| --------- | ----------- | --- | --- | --- | --- | --- |
SpecifiestheUDPaccountingportnumber.Range:1to65535.Default:1813.
| retries <RETRY-COUNT> |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 111

Specifies the number of retry attempts for contacting the specified RADIUS server. Range is 0 to 5
attempts. If no retry value is provided, the default value of 1 is used.

tracking {enable | disable}

Enables or disables server tracking for the RADIUS server. Tracked servers are probed at the start of each
server tracking interval to check if they are reachable.

Use command radius-server tracking to configure RADIUS server tracking globally.

Server tracking uses authentication request and response packets to determine server reachability status. The

server tracking user name and password are used to form the request packet which is sent to the server with

tracking enabled. Upon receiving a response to the request packet, the server is considered to be reachable.

tracking-mode {any | dead-only}

Configures tracking mode for the RADIUS server that has tracking enabled with the server. The tracking
mode is used to monitor the status of RADIUS server reachability. The default tracking mode is any.

Sets the tracking mode to:

n any: track the RADIUS server irrespective of its server reachability.

n dead-only: track the RADIUS server only when the server is marked as unreachable.

vrf <VRF-NAME>

Specifies the VRF name to be used for communicating with the server. If no VRF name is provided, the
default VRF named default is used.

spi <SPI-INDEX>

Specifies the Security Parameters Index. The SPI is an identification tag carried in the IPsec AH header.
The SPI must be unique on the switch. Range: 256 to 4294967295.

<AUTH-TYPE>

Specifies the authentication algorithm: md5, sha1, or sha256.

<AUTH-KEY-TYPE>

Specifies the authentication key type: plaintext, hex-string, or ciphertext.

[<AUTH-KEY>]

Specifies the authentication key. For <AUTH-TYPE> of ciphertext, this is the ciphertext string.

For <AUTH-TYPE> of plaintext or hex-string:

n md5 (plaintext): 1 to 16 characters, (hex-string): 2 to 32 hexadecimal digits.

n sha1 (plaintext): 1 to 20 characters, (hex-string): 2 to 40 hexadecimal digits.

n sha256 (plaintext): 1 to 32 characters, (hex-string): 2 to 64 hexadecimal digits.

When <AUTH-KEY-TYPE> is not followed by <AUTH-KEY>, plaintext authentication key prompting occurs upon
pressing Enter. Enter must be pressed immediately after the <AUTH-KEY-TYPE> parameter without entering
other parameters. The entered authentication key characters are masked with asterisks.

<ENCRYPT-TYPE>

Specifies the encryption algorithm: 3des, aes, des, or null.

<ENCRYPT-KEY-TYPE>

Specifies the encryption key type: plaintext, hex-string, or ciphertext.

[<ENCRYPT-KEY>]

Specifies the encryption key. For <ENCRYPT-TYPE> of ciphertext, this is the ciphertext string.

For <ENCRYPT-TYPE> of plaintext or hex-string:

n 3des (plaintext): 24 characters, (hex-string): 48 hexadecimal digits.

n aes (plaintext): 16, 24, or 32 characters, (hex-string): 32, 48, or 64 hexadecimal digits.

Remote AAA (TACACS+, RADIUS) commands | 112

des (plaintext):8characters,(hex-string):16hexadecimaldigits.
n
When<ENCRYPT-KEY-TYPE>isnotfollowedby<ENCRYPT-KEY>,plaintextencryptionkeypromptingoccursupon
pressingEnter.Entermustbepressedimmediatelyafterthe<ENCRYPT-KEY-TYPE>parameterwithoutentering
otherparameters.Theenteredencryptionkeycharactersaremaskedwithasterisks.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
IfthefullyqualifieddomainnameisprovidedfortheRADIUSserverhost,aDNSservermustbeconfigured
andaccessiblethroughthesameVRFasmentionedfortheserverhost.Thisconfigurationisrequiredforthe
resolutionoftheRADIUSserverhostnametoitsIPaddress.IfaDNSserverisnotavailableforthisVRF,the
RADIUSserversreachablethroughthisVRFmustbeconfiguredbymeansoftheirIPaddressesonly.
Examples
AddingaRADIUSserverwithanIPv4address,aplaintextpasskey,andIPsecauthentication(md5plaintext).
switch(config)# radius-server host 1.1.1.1 key plaintext 98ab vrf mgmt secure
| ipsec | authentication | spi 261 | md5 plaintext | 1abc |     |
| ----- | -------------- | ------- | ------------- | ---- | --- |
AddingaRADIUSserverwithanIPv4addressandapromptedIPsecauthentication(md5)plaintext
authenticationkey.
switch(config)# radius-server host 1.1.1.1 secure ipsec authentication spi 261 md5
| Enter the | IPsec authentication     |     | key: ******** |     |     |
| --------- | ------------------------ | --- | ------------- | --- | --- |
| Re-Enter  | the IPsec authentication |     | key: ******** |     |     |
AddingaRADIUSserverwithanIPv4address,IPsecauthentication(MD5plaintext),andIPsecencryption
(AESplaintext):
| switch(config)# | radius-server | host | 1.1.1.2 | vrf mgmt | secure |
| --------------- | ------------- | ---- | ------- | -------- | ------ |
ipsec encryption spi 262 md5 plaintext 9xyz aes plaintext 1234567890abcdef
AddingaRADIUSserverbyprovidinganIPv4addressandIPsecMD5authenticationtype,andthen
respondingtopromptsforthekeysandencryptiontype:
switch(config)# radius-server host 1.1.1.6 secure ipsec encryption spi 262 md5
| Enter the | IPsec authentication     |      | key: ********        |     |     |
| --------- | ------------------------ | ---- | -------------------- | --- | --- |
| Re-Enter  | the IPsec authentication |      | key: ********        |     |     |
| Enter the | IPsec encryption         | type | (3des/aes/des/null)? |     | aes |
| Enter the | IPsec encryption         | key: | ********             |     |     |
| Re-Enter  | the IPsec encryption     | key: | ********             |     |     |
AddingaRADIUSserverwithanIPv4address,trackingenabled,trackingmode,IPsecauthentication(MD5
plaintext),IPsecencryption(AESplaintext)issettodead-only:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 113

switch(config)# radius-server host 1.1.1.1 tracking enable tracking-mode dead-only
|     | vrf | mgmt secure |                  | ipsec | encryption |     | spi 262 | md5 plaintext | 9xyz |
| --- | --- | ----------- | ---------------- | ----- | ---------- | --- | ------- | ------------- | ---- |
|     | aes | plaintext   | 1234567890abcdef |       |            |     |         |               |      |
RemovingaRADIUSserver:
|     | switch(config)# |     | no  | radius-server |     | host | 1.1.1.1 | vrf mgmt |     |
| --- | --------------- | --- | --- | ------------- | --- | ---- | ------- | -------- | --- |
RemovingtheipsecconfigurationfromaRADIUSserver:
switch(config)# no radius-server host 1.1.1.2 vrf mgmt secure ipsec encryption
| radius-server |     |     |     | host | tls | (RadSec) |     |     |     |
| ------------- | --- | --- | --- | ---- | --- | -------- | --- | --- | --- |
Syntax
| radius-server  |               | host               | {<FQDN>  |             | | <IPV4>    | |       | <IPV6>}        |     |     |
| -------------- | ------------- | ------------------ | -------- | ----------- | ----------- | ------- | -------------- | --- | --- |
| tls            | [timeout      | <TIMEOUT-SECONDS>] |          |             |             | [port   | <PORT-NUMBER>] |     |     |
| [auth-type     |               | {pap               | | chap}] | [tracking   |             | {enable | | disable}]    |     |     |
| [tracking-mode |               | {any               | |        | dead-only}] |             | [vrf    | <VRF-NAME>]    |     |     |
| no             | radius-server |                    | host     | {<FQDN>     | |           | <IPV4>  | | <IPV6>}      |     |     |
| tls            | [port         | <PORT-NUMBER>]     |          | [vrf        | <VRF-NAME>] |         |                |     |     |
Description
AddsaRadSecserver.Bydefault,theRADIUSserverisassociatedwiththeservergroupnamedradius.
RadSecisusedtosecurethecommunicationbetweenRADIUSserverandRADIUSclientusingTLS.
ThenoformofthiscommandremovesapreviouslyaddedRadSecserver.
Thesharedkeywillbeaddedasradsecforconnectionestablishment.
Commandcontext
config
Parameters
| {<FQDN> | |   | <IPV4> | | <IPv6>} |     |     |     |     |     |     |
| ------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- |
SpecifiestheRADIUSserveras:
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
n <IPV6>:anIPv6address.
tls
EstablishesRADIUSconnectionoverTLS.
| timeout | <TIMEOUT-SECONDS> |     |     |     |     |     |     |     |     |
| ------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Specifiesthetimeout.Therangeis1to60seconds.Ifatimeoutisnotspecified,thevaluefromthe
globaltimeoutforRADIUSisused.
port <PORT-NUMBER>
SpecifiestheportnumbertoestablishRadSecconnection.Range:1to65535.Default:2083.
| auth-type |     | {pap | | chap} |     |     |     |     |     |     |
| --------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- |
RemoteAAA(TACACS+,RADIUS)commands|114

Selects either PAP (default) or CHAP authentication type. If this parameter is not specified, the RADIUS
global default is used.

tracking {enable | disable}

Enables or disables server tracking for the RADIUS server. Tracked servers are probed at the start of each
server tracking interval to check if they are reachable.

Use command radius-server tracking to configure RADIUS server tracking globally.

Server tracking uses authentication request and response packets to determine server reachability status. The

server tracking user name and password are used to form the request packet which is sent to the server with

tracking enabled. Upon receiving a response to the request packet, the server is considered to be reachable.

tracking-mode {any | dead-only}

Configures tracking mode for the RADIUS server that has tracking enabled with the server. The tracking
mode is used to monitor the status of RADIUS server reachability. The default tracking mode is any.

Sets the tracking mode to:

n any: track the RADIUS server irrespective of its server reachability.

n dead-only: track the RADIUS server only when the server is marked as unreachable.

vrf <VRF-NAME>

Specifies the VRF name to be used for communicating with the server. If no VRF name is provided, the
default VRF named default is used.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Adding a RADIUS server over TLS with an IPv4 address and a named VRF:

switch(config)# radius-server host 1.1.1.1 tls vrf mgmt

Adding a RADIUS server over TLS with an IPv4 address and default port:

switch(config)# radius-server host 1.1.1.1 tls port

Adding a RADIUS server over TLS with tracking enabled and tracking mode is set to dead-only:

switch(config)# radius-server host 1.1.1.1 tls tracking enable tracking-mode dead-
only

Adding a RADIUS server over TLS with an IPv4 address, a port, and a named VRF:

switch(config)# radius-server host 1.1.1.2 tls port 32 vrf mgmt

Adding a RADIUS server over TLS with an IPv6 address:

switch(config)# radius-server host 2001:0db8:85a3:0000:0000:8a2e:0370:7334 tls

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

115

| radius-server | key |     |     |     |
| ------------- | --- | --- | --- | --- |
Syntax
radius-server key [plaintext <GLOBAL-PASSKEY> | ciphertext <GLOBAL-PASSKEY>]
| no radius-server | key |     |     |     |
| ---------------- | --- | --- | --- | --- |
Description
CreatesormodifiesaRADIUSglobalpasskey.TheRADIUSglobalpasskeyisusedasashared-secretfor
encryptingthecommunicationbetweenallRADIUSserversandtheswitch.TheRADIUSglobalpasskeyis
requiredforauthenticationunlesslocalpasskeyshavebeenset.Bydefault,theRADIUSglobalpasskeyis
empty.Iftheadministratorhasnotsetthiskey,theswitchwillnotbeabletoperformRADIUS
authentication.Theswitchwillinsteadrelyontheauthenticationmechanismconfiguredwithaaa
| authentication | login. |     |     |     |
| -------------- | ------ | --- | --- | --- |
Whenthiscommandisenteredwithoutparameters,plaintextpasskeypromptingoccursuponpressingEnter.The
enteredpasskeycharactersaremaskedwithasterisks.
Thenoformofthecommandremovestheglobalpasskey.
Commandcontext
config
Parameters
plaintext <GLOBAL-PASSKEY>
SpecifiestheRADIUSglobalpasskeyinplaintextformatwithalengthof1to31characters.AsperRFC
2865,ashared-secretcanbeamixofalphanumericandspecialcharacters.
ciphertext <GLOBAL-PASSKEY>
SpecifiestheRADIUSglobalpasskeyinencryptedformat.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Addingtheglobalpasskey:
| switch(config)# | radius-server |     | key plaintext | mypasskey123 |
| --------------- | ------------- | --- | ------------- | ------------ |
Addingtheglobalpasskeywithprompting:
| switch(config)# | radius-server     |                | key       |     |
| --------------- | ----------------- | -------------- | --------- | --- |
| Enter the       | RADIUS server     | key: ********* |           |     |
| Re-Enter        | the RADIUS server | key:           | ********* |     |
Removingtheglobalpasskey:
| switch(config)# | no radius-server |     | key |     |
| --------------- | ---------------- | --- | --- | --- |
RemoteAAA(TACACS+,RADIUS)commands|116

radius-server retries

Syntax

radius-server retries <0-5>
no radius-server retries

Description

Sets at the global level the number of retries the switch makes before concluding that the RADIUS server is
unreachable.

You can override this setting with a fine-grained per RADIUS server retries configuration.

The no form of this command resets the RADIUS global retries to the default retries value of 1.

Command context

config

Parameters

retries <0-5>

Specifies the number of retry attempts for contacting RADIUS servers. Range is 0 to 5 retries.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch(config)# radius-server retries 3

radius-server timeout

Syntax

radius-server timeout [<1-60>]
no radius-server timeout

Description

Specifies the number of seconds to wait for a response from the RADIUS server before trying the next
RADIUS server. If a value is not specified, a default value of 5 seconds is used. You can override this value
with a fine-grained per server timeout configured for individual servers.

The no form of this command resets the RADIUS global authentication timeout to the default of 5 seconds.

Command context

config

Parameters

timeout <1-60>

Specifies the timeout interval of 1 to 60 seconds. The default is 5 seconds.

Authority

Administrators or local user group members with execution rights for this command.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

117

Examples
SettingtheRADIUSservertimeout:
switch(config)#
|     |     | radius-server | timeout | 10  |
| --- | --- | ------------- | ------- | --- |
ResettingthetimeoutfortheRADIUSservertothedefault:
| switch(config)# |     | no radius-server |     | timeout  |
| --------------- | --- | ---------------- | --- | -------- |
| radius-server   |     | tls timeout      |     | (RadSec) |
Syntax
| radius-server    | tls | timeout [<1-60>] |     |     |
| ---------------- | --- | ---------------- | --- | --- |
| no radius-server | tls | timeout          |     |     |
Description
SpecifiesthenumberofsecondstowaitforaresponsefromtheRadSecserverbeforetryingthenext
RADIUSorRadSecserver.Ifavalueisnotspecified,adefaultvalueof5secondsisused.Youcanoverride
thisvaluewithafine-grainedperservertimeoutconfiguredforindividualservers.
ThenoformofthiscommandresetstheRadSecglobalauthenticationtimeouttothedefaultof5seconds.
Commandcontext
config
Parameters
| timeout <1-60> |     |     |     |     |
| -------------- | --- | --- | --- | --- |
Specifiesthetimeoutintervalof1to60seconds.Thedefaultis5seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingtheRadSecservertimeout:
| switch(config)# |     | radius-server | tls | timeout 10 |
| --------------- | --- | ------------- | --- | ---------- |
ResettingthetimeoutfortheRadSectothedefault:
| switch(config)# |     | no radius-server |     | tls timeout |
| --------------- | --- | ---------------- | --- | ----------- |
| radius-server   |     | tracking         |     |             |
Syntax
| radius-server    | tracking | interval | <INTERVAL> |     |
| ---------------- | -------- | -------- | ---------- | --- |
| no radius-server | tracking | interval |            |     |
RemoteAAA(TACACS+,RADIUS)commands|118

| radius-server    | tracking   | retries            | <RETRIES> |              |              |
| ---------------- | ---------- | ------------------ | --------- | ------------ | ------------ |
| no radius-server |            | tracking retries   |           |              |              |
| radius-server    | tracking   | user-name          |           | <NAME>       |              |
| [password        | [plaintext | <PASSWORD>         |           | | ciphertext | <PASSWORD>]] |
| no radius-server |            | tracking user-name |           | <NAME>       |              |
Description
ConfiguresRADIUSservertrackingsettingsgloballyforallconfiguredRADIUSserversthathavetracking
| enabledwiththeradius-server |     |     | hostcommandonindividualservers. |     |     |
| --------------------------- | --- | --- | ------------------------------- | --- | --- |
Thenoformofthecommandremovesthespecifiedconfiguration,revertingittoitsdefault.Thenoform
withuser-namealsoclearsthepassword(resetsittoempty).
Commandcontext
config
Parameters
| interval <INTERVAL> |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
Specifiesthetimeinterval,inseconds,towaitbeforecheckingtheserverreachabilitystatus.Default:
300.Range60to84600.
| retries <RETRIES> |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- |
Specifiesthenumberofserverretries.Default:GlobalRADIUSretries.Range:0to5.
user-name <NAME> [password [plaintext <PASSWORD> | ciphertext <PASSWORD>]]
Specifiestheusername(andoptionallyapassword)tobeusedforserverchecking.Thedefaultuser
nameisradius-tracking-userwithanemptypassword.
Thepasswordisoptionalandmaybeenteredasplaintextorpastedinasciphertext.Theplaintext
passwordisvisibleascleartextwhenenteredbutisencryptedthereafter.Commandhistorydoesshow
thepasswordascleartext.
Whenpasswordisenteredwithoutafollowingsub-parameter,plaintextpasswordpromptingoccursupon
pressingEnter.Theenteredpasswordcharactersaremaskedwithasterisks.
Theuserdoesnothavetobeconfiguredontheserver.Servertrackingcanstillbeperformedwithauserwhichis
notconfiguredontheserverbecauseauthenticationfailureontheserverachievesconfirmationthattheserveris
reachable.
Servertrackingusesauthenticationrequestandresponsepacketstodetermineserverreachabilitystatus.The
servertrackingusernameandpasswordareusedtoformtherequestpacketwhichissenttotheserverwith
trackingenabled.Uponreceivingaresponsetotherequestpacket,theserverisconsideredtobereachable.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringatrackingintervalof120seconds:
| switch(config)# |     | radius-server |     | tracking interval | 120 |
| --------------- | --- | ------------- | --- | ----------------- | --- |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 119

Revertingthetrackingintervaltoitsdefaultof300seconds:
| switch(config)# |     | no radius-server |     | tracking | interval |     |
| --------------- | --- | ---------------- | --- | -------- | -------- | --- |
Configuringthreeretries:
| switch(config)# |     | radius-server |     | tracking retries |     | 3   |
| --------------- | --- | ------------- | --- | ---------------- | --- | --- |
Configuringuserradius-trackerwithaplaintextpassword.
switch(config)#
|     |          | radius-server |         | tracking user-name |     | radius-tracker |
| --- | -------- | ------------- | ------- | ------------------ | --- | -------------- |
|     | password | plaintext     | track$1 |                    |     |                |
Configuringuserradius-trackerwithapromptedplaintextpassword.
switch(config)# radius-server tracking user-name radius-tracker password
| Enter    | the | RADIUS server | tracking | password:          | ******* |         |
| -------- | --- | ------------- | -------- | ------------------ | ------- | ------- |
| Re-Enter | the | RADIUS server |          | tracking password: |         | ******* |
Revertingthetrackingusernametoitsdefaultofradius-tracking-user:
| switch(config)# |     | no radius-server |     | tracking | user-name |     |
| --------------- | --- | ---------------- | --- | -------- | --------- | --- |
server
Syntax
server {<FQDN> | <IPV4> | <IPV6>} [tls][port <PORT-NUMBER>] [vrf <VRF-NAME>]
no server {<FQDN> | <IPV4> | <IPV6>} [tls][port <PORT-NUMBER>] [vrf <VRF-NAME>]
Description
AddsaTACACS+/RADIUSservertoaserver-group.OnlytheconfiguredTACACS+/RADIUSserversare
allowedtobeaddedwithintheservergroup.Ifthesameservernameexistswithmultipleportsormultiple
VRFs,specifytheservername,port,andVRFwhenaddingtheservertotheserver-group.
ThenoformofthiscommandremovesaTACACS+/RADIUSserverfromaserver-group.
Commandcontext
config-sg
Parameters
| {<FQDN> | | <IPV4> | | <IPv6>} |     |     |     |     |
| ------- | -------- | --------- | --- | --- | --- | --- |
Specifiestheserveras:
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
<IPV6>:anIPv6address.
n
tls
SpecifiestheTLSprotectionfortheRADIUSserver.
RemoteAAA(TACACS+,RADIUS)commands|120

IfTLSisconfiguredwithoutaportnumber,thesystemsearchestheRADIUSserverbyhostnameand
setsthedefaultauthenticationport(2083).Groupserverpriorityisassignedbasedonthesequencein
whichtheserversareadded.
port <PORT-NUMBER>
Specifiestheauthenticationportnumber.Range:1to65535.DefaultTACACS+(TCP):49,RADIUS(UDP):
1812andRadSec:2083.
Ifaportnumberisnotprovided,thesystemsearchestheTACACS+/RADIUSserverbyhostnameand
setsthedefaultauthenticationport.Groupserverpriorityisassignedbasedonthesequenceinwhich
theserversareadded.
vrf <VRF-NAME>
SpecifiestheVRFname.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
AddingaservertoTACACS+servergroupsg1byprovidinganIPv4address,portnumber,andVRFname:
| switch(config)#    | aaa group | server tacacs | sg1            |
| ------------------ | --------- | ------------- | -------------- |
| switch(config-sg)# | server    | 1.1.1.2 port  | 32 vrf default |
AddingaservertoTACACS+servergroupsg2byprovidinganIPv6addressanddefaultVRF:
| switch(config)# | aaa group | server tacacs | sg2 |
| --------------- | --------- | ------------- | --- |
switch(config-sg)# server 2001:0db8:85a3:0000:0000:8a2e:0370:7334 vrf default
AddingaservertoRADIUSservergroupsg3byprovidinganIPv4address,portnumber,andVRFname:
| switch(config)#    | aaa group | server radius | sg3            |
| ------------------ | --------- | ------------- | -------------- |
| switch(config-sg)# | server    | 1.1.1.5 port  | 12 vrf default |
AddingaservertoRADIUSservergroupsg3withTLSprotectionbyprovidinganIPv4address,portnumber,
andVRFname:
| switch(config)#    | aaa group | server radius | sg3                 |
| ------------------ | --------- | ------------- | ------------------- |
| switch(config-sg)# | server    | 1.1.1.5 tls   | port 12 vrf default |
AddingaservertoRADIUSservergroupsg4byprovidinganIPv6addressanddefaultVRF:
| switch(config)# | aaa group | server radius | sg4 |
| --------------- | --------- | ------------- | --- |
switch(config-sg)# server 2001:0db8:85a3:0000:0000:8a2e:0371:7334 vrf default
AddingaservertoRADIUSservergroupsg4byprovidinganIPv4address,portnumber,andVRFname:
| switch(config)#    | aaa group | server radius | sg4            |
| ------------------ | --------- | ------------- | -------------- |
| switch(config-sg)# | server    | 1.1.1.6 port  | 32 vrf vrf_red |
SpecifyinganIPv4addresswhenremovingaTACACS+serverfromservergroupsg1:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 121

| switch(config)# |     | aaa | group | server tacacs | sg1 |     |     |
| --------------- | --- | --- | ----- | ------------- | --- | --- | --- |
switch(config-sg)#
|     |     | no  | server | 1.1.1.2 | port 12 | vrf default |     |
| --- | --- | --- | ------ | ------- | ------- | ----------- | --- |
SpecifyinganIPv6addresswhenremovingaTACACS+serverfromservergroupsg2withthedefaultVRF:
| switch(config)# |     | aaa | group | server tacacs | sg2 |     |     |
| --------------- | --- | --- | ----- | ------------- | --- | --- | --- |
switch(config-sg)# no server 2001:0db8:85a3:0000:0000:8a2e:0370:7334 vrf default
| show aaa | accounting |     |     |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- | --- | --- |
Syntax
| show aaa accounting |     | [vsx-peer] |     |     |     |     |     |
| ------------------- | --- | ---------- | --- | --- | --- | --- | --- |
Description
Showstheaccountingconfigurationperconnectiontype(channel).
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ConfiguringandthenshowingtheaccountingsequenceforTACACS+groupsandlocal:
switch(config)# aaa accounting all default start-stop group tg1 tg2 tacacs local
switch(config)#
|     |     | aaa | accounting | all ssh | start-stop | group tg1 | tg2 |
| --- | --- | --- | ---------- | ------- | ---------- | --------- | --- |
switch(config)# aaa accounting all console start-stop group tg4 tacacs local
switch(config)# aaa accounting all https-server start-stop local group tacacs tg3
| switch(config)# |      | exit           |     |     |     |     |     |
| --------------- | ---- | -------------- | --- | --- | --- | --- | --- |
| switch#         | show | aaa accounting |     |     |     |     |     |
AAA Accounting:
| Accounting |     | Type    |          |     |     | : all        |     |
| ---------- | --- | ------- | -------- | --- | --- | ------------ | --- |
| Accounting |     | Mode    |          |     |     | : start-stop |     |
| Accounting | for | default | channel: |     |     |              |     |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     | | GROUP | PRIORITY |     |     |
| ---------- | --- | --- | --- | ------- | -------- | --- | --- |
---------------------------------------------------------------------------------
| tg1    |     |     |     | | 0 |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| tg2    |     |     |     | | 1 |     |     |     |
| tacacs |     |     |     | | 2 |     |     |     |
| local  |     |     |     | | 3 |     |     |     |
---------------------------------------------------------------------------------
RemoteAAA(TACACS+,RADIUS)commands|122

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
| switch(config)# | exit |     |     |
| --------------- | ---- | --- | --- |
switch#
show aaa accounting
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
---------------------------------------------------------------------------------
| Accounting | for console | channel: |     |
| ---------- | ----------- | -------- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |
| ---------- | --- | ---------------- | --- |
---------------------------------------------------------------------------------
tg4 | 0
radius | 1
local | 2
---------------------------------------------------------------------------------
Configuringandthenshowingonlylocalaccountingfordefault:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 123

|     | switch(config)# |     | aaa | accounting |     | all default | start-stop |     | local |     |
| --- | --------------- | --- | --- | ---------- | --- | ----------- | ---------- | --- | ----- | --- |
switch(config)#
exit
|     | switch#         | show | aaa accounting |          |     |     |     |              |     |     |
| --- | --------------- | ---- | -------------- | -------- | --- | --- | --- | ------------ | --- | --- |
|     | AAA Accounting: |      |                |          |     |     |     |              |     |     |
|     | Accounting      |      | Type           |          |     |     |     | : all        |     |     |
|     | Accounting      |      | Mode           |          |     |     |     | : start-stop |     |     |
|     | Accounting      | for  | default        | channel: |     |     |     |              |     |     |
---------------------------------------------------------------------------------
|     | GROUP NAME |     |     |     |     | | GROUP | PRIORITY |     |     |     |
| --- | ---------- | --- | --- | --- | --- | ------- | -------- | --- | --- | --- |
---------------------------------------------------------------------------------
|     | local |     |     |     |     | | 0 |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| show | aaa | accounting |     |     |     | port-access |     | (RADIUS |     | only) |
| ---- | --- | ---------- | --- | --- | --- | ----------- | --- | ------- | --- | ----- |
Syntax
show aaa accounting port-access [interface {<IF-NAME> | all} client-status [mac <MAC-ADDR>]]
[vsx-peer]
Description
Showsoverallorspecificportaccessaccountinginformation.
Commandcontext
Operator(>)orManager(#)
Parameters
| interface | {<IF-NAME> |     | |   | all} |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
Selectseitheroneinterfaceorallinterfacesforshowing.
mac <MAC-ADDR>
SpecifiesaclientstationMACaddress(xx:xx:xx:xx:xx:xx),wherexisahexadecimalnumberfrom0toF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingtheoverallportaccessaccountinginformation:
|     | switch#        | show | aaa accounting |        | port-access |     |     |     |     |     |
| --- | -------------- | ---- | -------------- | ------ | ----------- | --- | --- | --- | --- | --- |
|     | AAA Accounting |      | Port           | Access |             |     |     |     |     |     |
===========================
|     | Radius | Accounting |         | Enabled |     | : yes        |     |     |     |     |
| --- | ------ | ---------- | ------- | ------- | --- | ------------ | --- | --- | --- | --- |
|     | Radius | Server     | Group   |         |     | : acct_group |     |     |     |     |
|     | Local  | Accounting | Enabled |         |     | : no         |     |     |     |     |
RemoteAAA(TACACS+,RADIUS)commands|124

| Accounting | Mode           |     | : start-stop |
| ---------- | -------------- | --- | ------------ |
| Interim    | Update Enabled |     | : yes        |
| Interim    | Interval       |     | : 12 minutes |
Showingtheportaccessaccountinginformationforaclient.
switch# show aaa accounting port-access interface 1/1/1 client-status
| Port Access               | Client Status | Details |     |
| ------------------------- | ------------- | ------- | --- |
| Client a6:4f:1e:6a:3d:2c, |               | test1   |     |
============================
| Session | Details |     |     |
| ------- | ------- | --- | --- |
---------------
| Port       |         | : 1/1/1 |     |
| ---------- | ------- | ------- | --- |
| Session    | Time    | : 100s  |     |
| Accounting | Details |         |     |
------------------
| Accounting | Session        | ID : 1234 |     |
| ---------- | -------------- | --------- | --- |
| Input      | Packets        | : 1028    |     |
| Input      | Octets         | : 8224    |     |
| Output     | Packets        | : 2048    |     |
| Output     | Octets         | : 8000    |     |
| Input      | Gigaword       | : 0       |     |
| Output     | Gigaword       | : 0       |     |
| show aaa   | authentication |           |     |
Syntax
show aaa authentication
[vsx-peer]
Description
Showstheauthenticationconfigurationperconnectiontype(channel).
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ConfiguringTACACS+authenticationsequencesandthenshowingtheconfigurationperconnectiontype
(channel):
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 125

switch(config)# aaa authentication login default group tg1 tg2 tg3 tg4 tacacs local
switch(config)#
|     | aaa authentication | login ssh | group tg1 | tg2 |
| --- | ------------------ | --------- | --------- | --- |
switch(config)# aaa authentication login console group tg4 tacacs local
switch(config)# aaa authentication login https-server local group tacacs tg3
| switch(config)# | exit               |     |     |     |
| --------------- | ------------------ | --- | --- | --- |
| switch# show    | aaa authentication |     |     |     |
AAA Authentication:
| Fail-through     |             | : Enabled |     |     |
| ---------------- | ----------- | --------- | --- | --- |
| Limit Login      | Attempts    | : Not set |     |     |
| Lockout Time     |             | : 300     |     |     |
| Minimum Password | Length      | : Not set |     |     |
| Authentication   | for default | channel:  |     |     |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |     |
| ---------- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| tg1    |     | | 0 |     |     |
| ------ | --- | --- | --- | --- |
| tg2    |     | | 1 |     |     |
| tg3    |     | | 2 |     |     |
| tg4    |     | | 3 |     |     |
| tacacs |     | | 4 |     |     |
| local  |     | | 5 |     |     |
---------------------------------------------------------------------------------
| Authentication | for ssh channel: |     |     |     |
| -------------- | ---------------- | --- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |     |
| ---------- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| tg1 |     | | 0 |     |     |
| --- | --- | --- | --- | --- |
| tg2 |     | | 1 |     |     |
---------------------------------------------------------------------------------
| Authentication | for console | channel: |     |     |
| -------------- | ----------- | -------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |     |
| ---------- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| tg4    |     | | 0 |     |     |
| ------ | --- | --- | --- | --- |
| tacacs |     | | 1 |     |     |
| local  |     | | 2 |     |     |
---------------------------------------------------------------------------------
| Authentication | for https-server | channel: |     |     |
| -------------- | ---------------- | -------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |     |     |
| ---------- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| local  |     | | 0 |     |     |
| ------ | --- | --- | --- | --- |
| tacacs |     | | 1 |     |     |
| tg3    |     | | 2 |     |     |
---------------------------------------------------------------------------------
ConfiguringRADIUSauthenticationsequencesandthenshowingtheconfigurationperconnectiontype
(channel):
switch(config)# aaa authentication login default group rg1 rg2 rg3 rg4 radius local
switch(config)# aaa authentication login console group rg4 radius local
| switch(config)# | exit |     |     |     |
| --------------- | ---- | --- | --- | --- |
switch#
show aaa authentication
AAA Authentication:
| Fail-through |          | : Enabled |     |     |
| ------------ | -------- | --------- | --- | --- |
| Limit Login  | Attempts | : Not set |     |     |
| Lockout Time |          | : 300     |     |     |
RemoteAAA(TACACS+,RADIUS)commands|126

| Minimum Password | Length      | : Not set |     |     |
| ---------------- | ----------- | --------- | --- | --- |
| Authentication   | for default | channel:  |     |     |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP | PRIORITY |     |
| ---------- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| rg1    |     | | 0 |     |     |
| ------ | --- | --- | --- | --- |
| rg2    |     | | 1 |     |     |
| rg3    |     | | 2 |     |     |
| rg4    |     | | 3 |     |     |
| radius |     | | 4 |     |     |
| local  |     | | 5 |     |     |
---------------------------------------------------------------------------------
| Authentication | for console | channel: |     |     |
| -------------- | ----------- | -------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP | PRIORITY |     |
| ---------- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| rg4    |     | | 0 |     |     |
| ------ | --- | --- | --- | --- |
| radius |     | | 1 |     |     |
| local  |     | | 2 |     |     |
---------------------------------------------------------------------------------
Configuringonlydefaultauthenticationandthenshowingthedefaultconnectiontype(channel):
| switch(config)# | aaa authentication | login | default | local |
| --------------- | ------------------ | ----- | ------- | ----- |
| switch(config)# | exit               |       |         |       |
| switch# show    | aaa authentication |       |         |       |
AAA Authentication:
| Fail-through     |             |          | : Disabled |     |
| ---------------- | ----------- | -------- | ---------- | --- |
| Limit Login      | Attempts    |          | : Not      | set |
| Lockout Time     |             |          | : 300      |     |
| Minimum Password | Length      |          | : Not      | set |
| Authentication   | for default | channel: |            |     |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP | PRIORITY |     |
| ---------- | --- | ------- | -------- | --- |
---------------------------------------------------------------------------------
| local |     | | 0 |     |     |
| ----- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
| show aaa | authorization |     |     |     |
| -------- | ------------- | --- | --- | --- |
Syntax
| show aaa authorization | [vsx-peer] |     |     |     |
| ---------------------- | ---------- | --- | --- | --- |
Description
Showstheauthorizationconfigurationperconnectiontype(channel).
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 127

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Configuringandthenshowingtheauthorizationsequencefordefaultandconsoleconnectiontypes
(channels):
switch(config)# aaa authorization commands default group tg1 tacacs none
All commands will fail if none of the servers in the group list are reachable.
| Continue (y/n)? | y   |     |
| --------------- | --- | --- |
switch(config)#
switch(config)# aaa authorization commands console group tg1 tg2 tacacs none
All commands will fail if none of the servers in the group list are reachable.
| Continue (y/n)? | y    |     |
| --------------- | ---- | --- |
| switch(config)# | exit |     |
switch#
| switch# show  | aaa authorization |          |
| ------------- | ----------------- | -------- |
| Authorization | for default       | channel: |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |
| ---------- | --- | ---------------- |
---------------------------------------------------------------------------------
| tg1    |     | | 0 |
| ------ | --- | --- |
| tacacs |     | | 1 |
| none   |     | | 2 |
---------------------------------------------------------------------------------
| Authorization | for console | channel: |
| ------------- | ----------- | -------- |
---------------------------------------------------------------------------------
| GROUP NAME |     | | GROUP PRIORITY |
| ---------- | --- | ---------------- |
---------------------------------------------------------------------------------
| tg1    |     | | 0 |
| ------ | --- | --- |
| tg2    |     | | 1 |
| tacacs |     | | 2 |
| none   |     | | 3 |
---------------------------------------------------------------------------------
| show aaa | server-groups |     |
| -------- | ------------- | --- |
Syntax
| show aaa server-groups | [tacacs | | radius] [vsx-peer] |
| ---------------------- | ------- | -------------------- |
Description
ShowsTACACS+andRADIUSAAAservergroupinformationforallservertypesorforthespecifiedserver
type.
Commandcontext
Operator(>)orManager(#)
Parameters
tacacs
RemoteAAA(TACACS+,RADIUS)commands|128

NarrowsthecommandoutputtoonlyTACACS+servers.
radius
NarrowsthecommandoutputtoonlyRADIUSservers.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingallAAAservergroupinformation:
| switch# show | aaa server-groups |                 |     |     |
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
| ******* AAA | Mechanism | RADIUS ******* |     |     |
| ----------- | --------- | -------------- | --- | --- |
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
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 129

--------------------------------------------------------------------------------
| GROUP NAME | |   | SERVER NAME |     | | PORT | VRF | | PRIORITY |
| ---------- | --- | ----------- | --- | ------------ | ---------- |
--------------------------------------------------------------------------------
| sg2 | |   | 2001:0db8:85a3:0000:0000:8a2e: |     |                |     |
| --- | --- | ------------------------------ | --- | -------------- | --- |
|     |     | 0370:7334                      |     | | 49 | default | | 1 |
--------------------------------------------------------------------------------
| sg1 | |   | 1.1.1.2 |     | | 12 | mgmt | | 1 |
| --- | --- | ------- | --- | ----------- | --- |
--------------------------------------------------------------------------------
| tacacs (default) | |   | FQDN.com                       |     | | 32 | mgmt      | | 1 |
| ---------------- | --- | ------------------------------ | --- | ---------------- | --- |
| tacacs (default) | |   | 1.1.1.1                        |     | | 49 | mgmt      | | 2 |
| tacacs (default) | |   | 1.1.1.2                        |     | | 12 | mgmt      | | 3 |
| tacacs (default) | |   | abc.com                        |     | | 32 | vrf_red   | | 4 |
| tacacs (default) | |   | 2001:0db8:85a3:0000:0000:8a2e: |     |                  |     |
|                  |     | 0370:7334                      |     | | 49 | default   | | 5 |
| tacacs (default) | |   | 1.1.1.3                        |     | | 32 | vrf_blue| | 6   |
--------------------------------------------------------------------------------
ShowingRADIUSservergroupinformation:
| switch# show | aaa server-groups | radius         |     |     |     |
| ------------ | ----------------- | -------------- | --- | --- | --- |
| ******* AAA  | Mechanism         | RADIUS ******* |     |     |     |
--------------------------------------------------------------------------------
| GROUP NAME | |   | SERVER NAME |     | | PORT | VRF | | PRIORITY |
| ---------- | --- | ----------- | --- | ------------ | ---------- |
--------------------------------------------------------------------------------
| sg4 | |   | 2001:0db8:85a3:0000:0000:8a2e: |     |                  |     |
| --- | --- | ------------------------------ | --- | ---------------- | --- |
|     |     | 0370:7334                      |     | | 1812 | default | | 1 |
--------------------------------------------------------------------------------
| sg3 | |   | 1.1.1.5 |     | | 12 | mgmt | | 1 |
| --- | --- | ------- | --- | ----------- | --- |
--------------------------------------------------------------------------------
| radius (default) | |   | 1.1.1.4                        |     | | 1812 | mgmt    | | 1 |
| ---------------- | --- | ------------------------------ | --- | ---------------- | --- |
| radius (default) | |   | 1.1.1.5                        |     | | 12 | mgmt      | | 2 |
| radius (default) | |   | abc1.com                       |     | | 32 | mgmt      | | 3 |
| radius (default) | |   | 2001:0db8:85a3:0000:0000:8a2e: |     |                  |     |
|                  |     | 0370:7334                      |     | | 1812 | default | | 4 |
| radius (default) | |   | 1.1.1.6                        |     | | 32 | vrf_red   | | 5 |
| radius (default) | |   | 1.1.1.7                        |     | | 32 | vrf_blue| | 6   |
--------------------------------------------------------------------------------
| show accounting |     | log |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Syntax
| show accounting | log [last | <QTY-TO-SHOW> | | all] |     |     |
| --------------- | --------- | ------------- | ------ | --- | --- |
Description
Enteredwithoutoptionalparameters,thiscommandshowsallaccountinglogrecordsforthecurrentboot.
Sensitiveinformationismaskedfromthelog,bybeingrepresentedasasterisks.
Thisshow accounting logcommandreplacestheshow audit-logcommandthatissupportedonlyin10.00
releases.
Commandcontext
Manager(#)orAuditor(auditor>)
Parameters
RemoteAAA(TACACS+,RADIUS)commands|130

last <QTY-TO-SHOW>

Specifies how many most-recent accounting log records to show for the current boot. Range: 1 to 1000.

all

Selects for showing, all accounting records from the current boot and the previous boot.

Authority

Auditors or Administrators or local user group members with execution rights for this command. Auditors
can execute this command from the auditor context (auditor>) only.

Usage

The log message starts with the record type, which is specific to AOS-CX. Values are the following:
USER_START

Record of a user login action.

USER_END

Record of a user logout action.

USYS_CONFIG

Record of a command executed by the user.

The three types of accounting log information are identified by the msg= element starting with the rec=
item as follows:

n Exec is identified with: msg='rec=ACCT_EXEC

n Command is identified with: msg='rec=ACCT_CMD

n System is identified with: msg='rec=ACCT_SYSTEM

The user group is indicated by priv-lvl, which is specific to AOS-CX. Values are the following:

Privilege
level

User group

1

15

19

operators

administrators

auditors

The value of service indicates which user interface was used:
service=shell

Indicates that the log entry is a result of a CLI command.

service=https-server

Indicates that the log entry is a result of a REST API request or a Web UI action.

The string value of data identifies the CLI command or REST API request that was executed.

These elements are shown in context under Examples.

Examples

Showing the accounting log for the previous and current boot. Line breaks have been added for readability.

switch# show accounting log all

---------------------------------------------------------------------------------

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

131

| Local accounting |     | logs from | previous | boot |     |     |     |     |
| ---------------- | --- | --------- | -------- | ---- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
----
| type=DAEMON_START |     | msg=audit(Nov |     | 05 2018 | 23:00:58.607:9057) |     |     | :   |
| ----------------- | --- | ------------- | --- | ------- | ------------------ | --- | --- | --- |
auditd start, ver=2.4.3 format=raw kernel=4.9.119-yocto-standard res=success
----
| type=USER_START |     | msg=audit(Nov |     | 05 2018 | 23:06:42.398:42) |     |     | :   |
| --------------- | --- | ------------- | --- | ------- | ---------------- | --- | --- | --- |
msg='rec=ACCT_EXEC op=start session=CONSOLE timezone=UTC user=user1 priv-lvl=15
| auth-method=LOCAL |              | auth-type=LOCAL |              | service=shell |     | isconfig=no |     |     |
| ----------------- | ------------ | --------------- | ------------ | ------------- | --- | ----------- | --- | --- |
| hostname=8xxx     | addr=0.0.0.0 |                 | res=success' |               |     |             |     |     |
----
| type=USYS_CONFIG |     | msg=audit(Nov |     | 05 2018 | 23:06:42.399:43) |     |     | :   |
| ---------------- | --- | ------------- | --- | ------- | ---------------- | --- | --- | --- |
msg='rec=ACCT_CMD op=stop session=CONSOLE timezone=UTC user=user1 priv-lvl=15
| auth-method=LOCAL |               | auth-type=LOCAL |              | service=shell |              | isconfig=no |     |     |
| ----------------- | ------------- | --------------- | ------------ | ------------- | ------------ | ----------- | --- | --- |
| data="enable"     | hostname=8xxx |                 | addr=0.0.0.0 |               | res=success' |             |     |     |
----
| type=USYS_CONFIG |     | msg=audit(Nov |     | 05 2018 | 23:08:24.693:51) |     |     | :   |
| ---------------- | --- | ------------- | --- | ------- | ---------------- | --- | --- | --- |
msg='rec=ACCT_CMD op=stop session=CONSOLE timezone=UTC user=user1 priv-lvl=1
| auth-method=LOCAL |     | auth-type=LOCAL |     | service=shell |     | isconfig=no |     |     |
| ----------------- | --- | --------------- | --- | ------------- | --- | ----------- | --- | --- |
data="configure terminal" hostname=8xxx addr=0.0.0.0 res=success'
----
| type=USYS_CONFIG |     | msg=audit(Nov |     | 05 2018 | 23:08:39.108:52) |     |     | :   |
| ---------------- | --- | ------------- | --- | ------- | ---------------- | --- | --- | --- |
msg='rec=ACCT_CMD op=stop session=CONSOLE timezone=UTC user=user1 priv-lvl=15
| auth-method=LOCAL  |              | auth-type=LOCAL |              | service=shell |     | isconfig=yes |     |     |
| ------------------ | ------------ | --------------- | ------------ | ------------- | --- | ------------ | --- | --- |
| data="https-server |              | rest            | access-mode  | read-write"   |     |              |     |     |
| hostname=8xxx      | addr=0.0.0.0 |                 | res=success' |               |     |              |     |     |
----
| type=USER_START |     | msg=audit(Nov |     | 05 2018 | 23:10:57.238:58) |     |     | :   |
| --------------- | --- | ------------- | --- | ------- | ---------------- | --- | --- | --- |
msg='rec=ACCT_EXEC op=start session=REST timezone=UTC user=admin priv-lvl=15
| auth-method=LOCAL      |                | auth-type=LOCAL          |     | service=https-server |     |     |     |     |
| ---------------------- | -------------- | ------------------------ | --- | -------------------- | --- | --- | --- | --- |
| data="http-method=POST |                | http-uri=/rest/v1/login" |     |                      |     |     |     |     |
| hostname=8xxx          | addr=127.0.0.1 |                          |     | res=success'         |     |     |     |     |
----
| type=USYS_CONFIG |     | msg=audit(Nov |     | 05 2018 | 23:15:11.958:75) |     |     | :   |
| ---------------- | --- | ------------- | --- | ------- | ---------------- | --- | --- | --- |
msg='rec=ACCT_CMD op=stop session=CONSOLE timezone=UTC user=user1 priv-lvl=15
| auth-method=LOCAL |     | auth-type=LOCAL |     | service=shell |     | isconfig=yes |     |     |
| ----------------- | --- | --------------- | --- | ------------- | --- | ------------ | --- | --- |
data="tacacs-server host 2.2.2.2" hostname=8xxx addr=0.0.0.0 res=success'
----
| type=USYS_CONFIG |     | msg=audit(Nov |     | 05 2018 | 23:15:37.090:76) |     |     | :   |
| ---------------- | --- | ------------- | --- | ------- | ---------------- | --- | --- | --- |
msg='rec=ACCT_CMD op=stop session=REST timezone=UTC user=admin priv-lvl=15
| auth-method=LOCAL |     | auth-type=LOCAL |     | service=https-server |     |     |     |     |
| ----------------- | --- | --------------- | --- | -------------------- | --- | --- | --- | --- |
data="http-method=GET http-uri=/rest/v1/system/vrfs/mgmt/tacacs_servers"
| hostname=8xxx | addr=127.0.0.1 |     |     | res=success' |     |     |     |     |
| ------------- | -------------- | --- | --- | ------------ | --- | --- | --- | --- |
----
| type=USER_END | msg=audit(Nov |     | 05  | 2018 23:26:59.207:90) |     |     | :   |     |
| ------------- | ------------- | --- | --- | --------------------- | --- | --- | --- | --- |
msg='rec=ACCT_EXEC op=stop session=REST timezone=UTC user=admin priv-lvl=15
| auth-method=LOCAL      |                | auth-type=LOCAL           |     | service=https-server |     |     |     |     |
| ---------------------- | -------------- | ------------------------- | --- | -------------------- | --- | --- | --- | --- |
| data="http-method=POST |                | http-uri=/rest/v1/logout" |     |                      |     |     |     |     |
| hostname=8xxx          | addr=127.0.0.1 |                           |     | res=success'         |     |     |     |     |
----
| type=USER_END | msg=audit(Nov |     | 05  | 2018 23:27:49.164:93) |     |     | :   |     |
| ------------- | ------------- | --- | --- | --------------------- | --- | --- | --- | --- |
msg='rec=ACCT_EXEC op=stop session=CONSOLE timezone=UTC user=user1 priv-lvl=15
| auth-method=LOCAL |              | auth-type=LOCAL |              | service=shell |     | isconfig=no |     |     |
| ----------------- | ------------ | --------------- | ------------ | ------------- | --- | ----------- | --- | --- |
| hostname=8xxx     | addr=0.0.0.0 |                 | res=success' |               |     |             |     |     |
---------------------------------------------------------------------------------
| Local accounting |     | logs from | current | boot |     |     |     |     |
| ---------------- | --- | --------- | ------- | ---- | --- | --- | --- | --- |
---------------------------------------------------------------------------------
----
| type=DAEMON_START |     | msg=audit(Nov |     | 05 2018 | 23:32:05.642:626) |     |     | :   |
| ----------------- | --- | ------------- | --- | ------- | ----------------- | --- | --- | --- |
auditd start, ver=2.4.3 format=raw kernel=4.9.119-yocto-standard res=success
----
RemoteAAA(TACACS+,RADIUS)commands|132

| type=USER_START |     | msg=audit(Nov |     | 05  | 2018 | 23:35:52.915:11) |     | :   |
| --------------- | --- | ------------- | --- | --- | ---- | ---------------- | --- | --- |
msg='rec=ACCT_EXEC op=start session=CONSOLE timezone=UTC user=admin priv-lvl=15
| auth-method=LOCAL |              | auth-type=LOCAL |     |              | service=shell |     | isconfig=no |     |
| ----------------- | ------------ | --------------- | --- | ------------ | ------------- | --- | ----------- | --- |
| hostname=8xxx     | addr=0.0.0.0 |                 |     | res=success' |               |     |             |     |
----
| type=USYS_CONFIG |     | msg=audit(Nov |     |     | 05 2018 | 23:35:52.917:12) |     | :   |
| ---------------- | --- | ------------- | --- | --- | ------- | ---------------- | --- | --- |
msg='rec=ACCT_CMD op=stop session=CONSOLE timezone=UTC user=admin priv-lvl=15
auth-method=LOCAL auth-type=LOCAL service=shell isconfig=no data="enable"
| hostname=8xxx   | addr=0.0.0.0 |     |     | res=success' |     |     |     |     |
| --------------- | ------------ | --- | --- | ------------ | --- | --- | --- | --- |
| show accounting |              |     | log | port-access  |     |     |     |     |
Syntax
| show accounting | log | port-access |     | [last | <QTY-TO-SHOW> |     | | all] |     |
| --------------- | --- | ----------- | --- | ----- | ------------- | --- | ------ | --- |
Description
Showsnetworkuseraccountinglogrecords.
Commandcontext
Manager(#)orAuditor(auditor>)
Parameters
last <QTY-TO-SHOW>
Specifieshowmanymost-recentportaccessaccountinglogrecordstoshowforthecurrentboot.Range:
1to1000.
all
Selectsforshowing,allportaccessaccountingrecordsfromthecurrentbootandthepreviousboot.
Authority
AuditorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.Auditors
canexecutethiscommandfromtheauditorcontext(auditor>)only.
Examples
Showingportaccesslogoutput.Linebreakshavebeenaddedforreadability.
| switch# show | accounting |     | log | port-access |     | all |     |     |
| ------------ | ---------- | --- | --- | ----------- | --- | --- | --- | --- |
...
-----
| type=USER_ACCT |     | msg=audit(Jan |     | 25  | 2020 | 11:03:59.458:70) |     | :   |
| -------------- | --- | ------------- | --- | --- | ---- | ---------------- | --- | --- |
msg='rec=ACCT_NETWORK session=PORT-ACCESS timezone=Asia/Kolkata user=NETWORK_USER
auth-method=PORT-ACCESS auth-type=RADIUS service=shell isconfig=no
"System-accounting-STOP-for-session-port-access User-Name = 0006000000c7,
Calling-Station-Id = 00:06:00:00:00:c7, NAS-Port-Id = 1/1/2, NAS-Port = 2,
Acct-Session-Id = 1579930311220, Acct-Session-Time = 128 Acct-Input-Octets =
85607360,
Acct-Output-Octets = 4305, Acct-Input-Packets = 1337615, Acct-Output-Packets = 32,
Acct-Input-Gigawords = 0, Acct-Output-Gigawords = 0 Acct-Terminate-Cause = NAS
| Request "      |     |              |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
| hostname=main1 |     | res=success' |     |     |     |     |     |     |
-----
...
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 133

show radius-server
Syntax
| show radius-server | [detail] [vsx-peer] |     |
| ------------------ | ------------------- | --- |
Description
ShowsconfiguredRADIUSserversinformation.
Commandcontext
Operator(>)orManager(#)
Parameters
detail
SelectsadditionalRADIUSserverdetailsandglobalparametersforshowing.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
Whentheshow radius-servercommandshowsNonefortheshared-secret,thepasskeyismissing.
Examples
ShowingasummaryoftheglobalRADIUSconfiguration:
switch#
show radius-server
| ******* Global | RADIUS Configuration | ******* |
| -------------- | -------------------- | ------- |
| Shared-Secret: | None                 |         |
| Timeout: 60    |                      |         |
| Auth-Type:     | pap                  |         |
| Retries: 5     |                      |         |
TLSTimeout:60
| Tracking Time       | Interval (seconds):  | 60  |
| ------------------- | -------------------- | --- |
| Tracking Retries:   | 5                    |     |
| Tracking User-name: | radius-tracking-user |     |
| Tracking Password:  | None                 |     |
| Number of Servers:  | 1                    |     |
---------------------------------------------------------------------------
| SERVERNAME | |TLS | |PORT|VRF |
| ---------- | ---- | --------- |
---------------------------------------------------------------------------
| 20.1.1.129                              | | |1812|default |                 |
| --------------------------------------- | --------------- | --------------- |
| 1.1.1.4                                 | | |1812|mgmt    |                 |
| 1.1.1.5                                 | | |12 |mgmt     |                 |
| abc1.com                                | | |32           | |mgmt           |
| 2001:0db8:85a3:0000:0000:8a2e:0371:7334 |                 | | |1812|default |
| 1.1.1.6                                 | | |32 |vrf_red  |                 |
| 1.1.1.7                                 | | |32 |vrf_blue |                 |
---------------------------------------------------------------------------
RemoteAAA(TACACS+,RADIUS)commands|134

ShowingasummaryofaRADIUSserverwhentheper-serversharedkeyortheglobalRADIUSsharedkeyis
notset:
| switch# show   | radius-server        |     |         |
| -------------- | -------------------- | --- | ------- |
| ******* Global | RADIUS Configuration |     | ******* |
| Shared-Secret: | None                 |     |         |
| Timeout: 60    |                      |     |         |
| Auth-Type:     | pap                  |     |         |
| Retries: 5     |                      |     |         |
TLSTimeout:60
| Tracking Time       | Interval (seconds):  |     | 60  |
| ------------------- | -------------------- | --- | --- |
| Tracking Retries:   | 5                    |     |     |
| Tracking User-name: | radius-tracking-user |     |     |
| Tracking Password:  | None                 |     |     |
| Number of           | Servers: 1           |     |     |
---------------------------------------------------------------------------
| SERVERNAME |     | |TLS | |PORT|VRF |
| ---------- | --- | ---- | --------- |
---------------------------------------------------------------------------
| 20.1.1.129 |     | | |1812|default |     |
| ---------- | --- | --------------- | --- |
---------------------------------------------------------------------------
ShowingdetailsofaglobalRADIUSconfiguration:
| switch# show   | radius-server        | detail |         |
| -------------- | -------------------- | ------ | ------- |
| ******* Global | RADIUS Configuration |        | ******* |
Shared-Secret: AQBapb+HsdpqV1QcA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout: 5 |     |     |     |
| ---------- | --- | --- | --- |
| Auth-Type: | pap |     |     |
| Retries: 5 |     |     |     |
TLSTimeout:60
| Tracking Time       | Interval (seconds):  |              | 60     |
| ------------------- | -------------------- | ------------ | ------ |
| Tracking Retries:   | 5                    |              |        |
| Tracking User-name: | radius-tracking-user |              |        |
| Tracking Password:  | None                 |              |        |
| Number of           | Servers: 1           |              |        |
| ****** RADIUS       | Server Information   |              | ****** |
| Server-Name         |                      | : 20.1.1.129 |        |
| Auth-Port           |                      | : 1812       |        |
| Accounting-Port     |                      | : 1813       |        |
| VRF                 |                      | : default    |        |
| TLSEnabled          | :No                  |              |        |
| Shared-Secret       |                      | : None       |        |
| Timeout             |                      | : 60         |        |
| Retries             |                      | : 5          |        |
| Auth-Type           |                      | : pap        |        |
| Server-Group        |                      | : radius     |        |
| Default-Priority    |                      | : 4          |        |
| Tracking            |                      | : disabled   |        |
| Tracking-Mode       |                      | : any        |        |
| Reachability-Status |                      | : N/A        |        |
| ClearPass-Username  |                      | :            |        |
| ClearPass-Password  |                      | : None       |        |
ShowingdetailsofaRADIUSserverwhentheper-serversharedkeyandtheglobalRADIUSsharedkeyare
notset:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 135

| switch#        | show radius-server | detail        |         |
| -------------- | ------------------ | ------------- | ------- |
| *******        | Global RADIUS      | Configuration | ******* |
| Shared-Secret: | None               |               |         |
| Timeout:       | 5                  |               |         |
| Auth-Type:     | pap                |               |         |
| Retries:       | 1                  |               |         |
TLSTimeout:5
| Number           | of Servers: 1             |           |        |
| ---------------- | ------------------------- | --------- | ------ |
| ******           | RADIUS Server Information |           | ****** |
| Server-Name      |                           | : 1.1.1.1 |        |
| Auth-Port        |                           | : 2083    |        |
| VRF              |                           | : default |        |
| Shared-Secret    | (default)                 | : None    |        |
| Timeout          | (default)                 | : 5       |        |
| Retries          | (default)                 | : 1       |        |
| Auth-Type        | (default)                 | : pap     |        |
| Server-Group     | (default)                 | : radius  |        |
| Default-Priority |                           | : 1       |        |
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
RemoteAAA(TACACS+,RADIUS)commands|136

| show radius-server |     |     | secure | ipsec |
| ------------------ | --- | --- | ------ | ----- |
Syntax
show radius-server secure ipsec { server-list | host {<FQDN> | <IPV4> | <IPv6>} [port
| <PORT-NUMBER>] | [vrf <VRF-NAME>] |     | [vsx-peer] | }   |
| -------------- | ---------------- | --- | ---------- | --- |
Description
ShowsinformationforoneorallRADIUSserversconfiguredwithIPsec.
Commandcontext
Operator(>)orManager(#)
Parameters
server-list
Selectsallserversforshowing.
| host {<FQDN> | | <IPV4> | | <IPv6>} |     |     |
| ------------ | -------- | --------- | --- | --- |
SpecifiestheRADIUSserveras:
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
n <IPV6>:anIPv6address.
port <PORT-NUMBER>
Specifiestheauthenticationportnumber.Range:1to65535.Default:1812.
vrf <VRF-NAME>
SpecifiestheVRFnametobeusedforcommunicatingwiththeserver.IfnoVRFnameisprovided,the
defaultVRFnameddefaultisused.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
TheIPseckeyisshowninanexportableciphertextformat.
Examples
ShowinginformationforRADIUSserver1.1.1.1securedwithIPsec:
| switch#        | show radius-server |     | secure ipsec | host 1.1.1.1 |
| -------------- | ------------------ | --- | ------------ | ------------ |
| IPsec          |                    |     | : enabled    |              |
| Protocol       |                    |     | : ESP        |              |
| Authentication |                    |     | : MD5        |              |
| Encryption     |                    |     | : AES        |              |
| SPI            |                    |     | : 1234       |              |
ShowinginformationforallRADIUSserverssecuredwithIPsec:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 137

| switch# show       | radius-server | secure ipsec | server-list |
| ------------------ | ------------- | ------------ | ----------- |
| Server             |               | : 1.1.1.1    |             |
| IPsec              |               | : enabled    |             |
| Protocol           |               | : ESP        |             |
| Authentication     |               | : MD5        |             |
| Encryption         |               | : AES        |             |
| SPI                |               | : 1234       |             |
| Server             |               | : 1.1.1.2    |             |
| IPsec              |               | : enabled    |             |
| Protocol           |               | : ESP        |             |
| Authentication     |               | : MD5        |             |
| Encryption         |               | : AES        |             |
| SPI                |               | : 12341      |             |
| show radius-server |               | statistics   |             |
Syntax
show radius-server statistics {authentication | accounting} [vsx-peer]
Description
ShowsauthenticationoraccountingstatisticsforallconfiguredRADIUSservers.
Theaccountingstatisticsareonlyforportaccess.
Commandcontext
Operator(>)orManager(#)
Parameters
| {authentication | | accounting} |     |     |
| --------------- | ------------- | --- | --- |
Selectsthetypeofstatisticstoshow.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingRADIUSserverauthenticationstatistics:
| switch# show    | radius-server | statistics | authentication |
| --------------- | ------------- | ---------- | -------------- |
| Server Name     | : rad1        |            |                |
| Auth-Port       | : 1812        |            |                |
| Accounting-Port | : 1813        |            |                |
| VRF             | : mgmt        |            |                |
| TLS Enabled     | : Yes         |            |                |
RemoteAAA(TACACS+,RADIUS)commands|138

|     | Authentication |     | Statistics |     |     |     |
| --- | -------------- | --- | ---------- | --- | --- | --- |
-------------------------
|     | Round              | Trip Time   |           |     | : 100 |     |
| --- | ------------------ | ----------- | --------- | --- | ----- | --- |
|     | Pending            | Requests    |           |     | : 0   |     |
|     | Timeouts           |             |           |     | : 6   |     |
|     | Bad Authenticators |             |           |     | : 2   |     |
|     | Packets            | Dropped     |           |     | : 0   |     |
|     | Access             | Requests    |           |     | : 20  |     |
|     | Access             | Challenge   |           |     | : 8   |     |
|     | Access             | Accepts     |           |     | : 14  |     |
|     | Access             | Rejects     |           |     | : 0   |     |
|     | Access             | Response    | Malformed |     | : 0   |     |
|     | Access             | Retransmits |           |     | : 0   |     |
|     | Tracking           | Requests    |           |     | : 5   |     |
|     | Tracking           | Responses   |           |     | : 5   |     |
|     | Unknown            | Response    | Code      |     | : 0   |     |
ShowingRADIUSserveraccountingstatistics:
| switch# | show            | radius-server |        | statistics |     | accounting |
| ------- | --------------- | ------------- | ------ | ---------- | --- | ---------- |
|         | Server Name     |               | : rad1 |            |     |            |
|         | Auth-Port       |               | : 1812 |            |     |            |
|         | Accounting-Port |               | : 1813 |            |     |            |
|         | VRF             |               | : mgmt |            |     |            |
|         | TLS Enabled     |               | : No   |            |     |            |
|         | Accounting      | Statistics    |        |            |     |            |
-------------------------
|      | Round              | Trip Time   |      |            | :   | 100  |
| ---- | ------------------ | ----------- | ---- | ---------- | --- | ---- |
|      | Pending            | Requests    |      |            | :   | 0    |
|      | Timeouts           |             |      |            | :   | 5    |
|      | Bad Authenticators |             |      |            | :   | 1    |
|      | Packets            | Dropped     |      |            | :   | 0    |
|      | Accounting         | Requests    |      |            | :   | 15   |
|      | Accounting         | Responses   |      |            | :   | 10   |
|      | Accounting         | Response    |      | Malformed  | :   | 0    |
|      | Accounting         | Retransmits |      |            | :   | 0    |
|      | Unknown            | Response    | Code |            | :   | 0    |
| show | radius-server      |             |      | statistics |     | host |
Syntax
show radius-server statistics {authentication | accounting} host {<FQDN> | <IPV4> | <IPv6>}
| [tls] | [port <PORT-NUMBER>] |     |     | [vrf | <VRF-NAME>] | [vsx-peer] |
| ----- | -------------------- | --- | --- | ---- | ----------- | ---------- |
Description
ShowsauthenticationstatisticsforthespecifiedRADIUSserveronthespecifiedvrf.
Theaccountingstatisticsareonlyforportaccess.
Commandcontext
Operator(>)orManager(#)
Parameters
| {authentication |     | | accounting} |     |     |     |     |
| --------------- | --- | ------------- | --- | --- | --- | --- |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 139

Selectsthetypeofstatisticstoshow.
| host {<FQDN> | | <IPV4> | | <IPv6>} |     |
| ------------ | -------- | --------- | --- |
SpecifiestheRADIUSserveras:
n <FQDN>:afullyqualifieddomainname.
n <IPV4>:anIPv4address.
n <IPV6>:anIPv6address.
tls
EstablishesRADIUSconnectionoverTLS.
port <PORT-NUMBER>
Specifiestheauthenticatedport.Range:1to65535.
vrf <VRF-NAME>
SpecifiestheVRFnametobeusedforcommunicatingwiththeserver.IfnoVRFnameisprovided,the
defaultVRFnameddefaultisused.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingRADIUSserverauthenticationstatisticswithTLSenabled:
switch# show radius-server statistics authentication host 20.1.1.49 tls
| Server          | Name | : 20.1.1.49 |     |
| --------------- | ---- | ----------- | --- |
| Auth-Port       |      | : 2083      |     |
| Accounting-Port |      | : 2083      |     |
| VRF             |      | : default   |     |
| TLS Enabled     |      | : Yes       |     |
| Authentication  |      | Statistics  |     |
-------------------------
| Round              | Trip Time      |           | : 3  |
| ------------------ | -------------- | --------- | ---- |
| Pending            | Requests       |           | : 0  |
| Timeouts           |                |           | : 0  |
| Bad                | Authenticators |           | : 0  |
| Packets            | Dropped        |           | : 0  |
| Access             | Requests       |           | : 13 |
| Access             | challenge      |           | : 6  |
| Access             | Accepts        |           | : 3  |
| Access             | Rejects        |           | : 4  |
| Access             | Response       | Malformed | : 0  |
| show tacacs-server |                |           |      |
Syntax
| show tacacs-server | [detail] | [vsx-peer] |     |
| ------------------ | -------- | ---------- | --- |
Description
RemoteAAA(TACACS+,RADIUS)commands|140

ShowstheconfiguredTACACS+servers.
Commandcontext
Operator(>)orManager(#)
Parameters
detail
SelectsadditionalTACACS+serverdetailsandglobalparametersforshowing.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingasummaryofaglobalTACACS+configurationwithashared-secret:
| switch# | show tacacs-server |               |         |
| ------- | ------------------ | ------------- | ------- |
| ******* | Global TACACS+     | Configuration | ******* |
Shared-Secret: AQBapb+HsdpqV1Q3CPCBMQTG8e1cA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout:   | 5             |     |     |
| ---------- | ------------- | --- | --- |
| Auth-Type: | pap           |     |     |
| Number     | of Servers: 5 |     |     |
-------------------------------------------------------------------------------
SERVER NAME | PORT | VRF
-------------------------------------------------------------------------------
1.1.1.1 | 49 | mgmt
1.1.1.2 | 12 | mgmt
abc.com | 32 | vrf_blue
2001:0db8:85a3:0000:0000:8a2e:0370:7334 | 49 | default
1.1.1.3 | 32 | vrf_red
-------------------------------------------------------------------------------
ShowingdetailsofaglobalTACACS+configuration:
| switch# | show tacacs-server | detail        |         |
| ------- | ------------------ | ------------- | ------- |
| ******* | Global TACACS+     | Configuration | ******* |
Shared-Secret: AQBapb+HsdpqV1Q3CPCBMQTG8e1cA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout:    | 5              |             |        |
| ----------- | -------------- | ----------- | ------ |
| Auth-Type:  | pap            |             |        |
| Number      | of Servers: 5  |             |        |
| ******      | TACACS+ Server | Information | ****** |
| Server-Name |                | : 1.1.1.2   |        |
| Auth-Port   |                | : 12        |        |
| VRF         |                | : mgmt      |        |
Shared-Secret (default) : AQBapb+HsdpqV1Q3CPCBMQTG8eeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout   | (default) | : 5   |     |
| --------- | --------- | ----- | --- |
| Auth-Type | (default) | : pap |     |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 141

| Server-Group   |     | : sg1                                     |     |
| -------------- | --- | ----------------------------------------- | --- |
| Group-Priority |     | : 1                                       |     |
| Server-Name    |     | : 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |     |
| Auth-Port      |     | : 49                                      |     |
| VRF            |     | : default                                 |     |
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
1.1.1.1 | 49 | default
-------------------------------------------------------------------------------
ShowingTACACS+serverdetailswhenper-serversharedkeyandglobalTACACS+sharedkeyisnotset:
| switch# | show tacacs-server | detail        |         |
| ------- | ------------------ | ------------- | ------- |
| ******* | Global TACACS+     | Configuration | ******* |
RemoteAAA(TACACS+,RADIUS)commands|142

| Shared-Secret:     | None           |             |        |
| ------------------ | -------------- | ----------- | ------ |
| Timeout:           | 5              |             |        |
| Auth-Type:         | pap            |             |        |
| Number             | of Servers: 1  |             |        |
| ******             | TACACS+ Server | Information | ****** |
| Server-Name        |                | : 1.1.1.1   |        |
| Auth-Port          |                | : 49        |        |
| VRF                |                | : default   |        |
| Shared-Secret      | (default)      | : None      |        |
| Timeout            | (default)      | : 5         |        |
| Auth-Type          | (default)      | : pap       |        |
| Server-Group       | (default)      | : tacacs    |        |
| Default-Priority   |                | : 1         |        |
| show tacacs-server |                | statistics  |        |
Syntax
| show tacacs-server | statistics |     |     |
| ------------------ | ---------- | --- | --- |
[vsx-peer]
Description
ShowsauthenticationstatisticsforallconfiguredTACACS+servers.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingTACACS+serverauthenticationstatistics:
| switch#        | show tacacs-server | statistics |     |
| -------------- | ------------------ | ---------- | --- |
| Server         | Name : tac1        |            |     |
| Auth-Port      | : 49               |            |     |
| VRF            | : mgmt             |            |     |
| Authentication | Statistics         |            |     |
----------------------------------------------
| Round Trip     | Time     | : 1 |     |
| -------------- | -------- | --- | --- |
| Pending        | Requests | : 0 |     |
| Timeout        |          | : 0 |     |
| Unknown        | Types    | : 0 |     |
| Packet         | Dropped  | : 0 |     |
| Auth Start     |          | : 8 |     |
| Auth challenge |          | : 0 |     |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 143

Auth Accepts
Auth Rejects
Auth reply malformed
Tracking Requests
Tracking Responses

: 4
: 4
: 0
: 0
: 0

show tech aaa

Syntax

show tech aaa

Description

Shows the AAA configuration settings.

Command context

Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Example

Showing the AAA configuration settings:

switch# show tech aaa
====================================================
Show Tech executed on Tue Feb 14 02:19:11 2017
====================================================
====================================================
[Begin] Feature aaa
====================================================

*********************************
Command : show aaa authentication
*********************************
AAA Authentication:

Fail-through
Limit Login Attempts
Lockout Time
Minimum Password Length

: Enabled
: Not set
: 300
: Not set

Authentication for ssh channel:
---------------------------------------------------------------------------------
| GROUP PRIORITY
GROUP NAME
---------------------------------------------------------------------------------
local
---------------------------------------------------------------------------------

| 0

Authentication for https-server channel:
---------------------------------------------------------------------------------
GROUP NAME
| GROUP PRIORITY
---------------------------------------------------------------------------------
local
---------------------------------------------------------------------------------

| 0

Authentication for console channel:

Remote AAA (TACACS+, RADIUS) commands | 144

---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| local |     |     | | 0 |
| ----- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authentication | for default |     | channel: |
| -------------- | ----------- | --- | -------- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| tacacs |     |     | | 0 |
| ------ | --- | --- | --- |
| local  |     |     | | 1 |
---------------------------------------------------------------------------------
*********************************
| Command | : show aaa accounting |     |     |
| ------- | --------------------- | --- | --- |
*********************************
AAA Accounting:
| Accounting | Type        |          | : all        |
| ---------- | ----------- | -------- | ------------ |
| Accounting | Mode        |          | : start-stop |
| Accounting | for default | channel: |              |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| local |     |     | | 0 |
| ----- | --- | --- | --- |
---------------------------------------------------------------------------------
| Accounting | for ssh channel: |     |     |
| ---------- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| tacacs |     |     | | 0 |
| ------ | --- | --- | --- |
| local  |     |     | | 1 |
---------------------------------------------------------------------------------
| Accounting | for https-server |     | channel: |
| ---------- | ---------------- | --- | -------- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| tacacs |     |     | | 0 |
| ------ | --- | --- | --- |
---------------------------------------------------------------------------------
*********************************
| Command | : show aaa authorization |     |     |
| ------- | ------------------------ | --- | --- |
*********************************
| Authorization | for default |     | channel: |
| ------------- | ----------- | --- | -------- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| none |     |     | | 0 |
| ---- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authorization | for console |     | channel: |
| ------------- | ----------- | --- | -------- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     | | GROUP PRIORITY |
| ---------- | --- | --- | ---------------- |
---------------------------------------------------------------------------------
| none |     |     | | 0 |
| ---- | --- | --- | --- |
---------------------------------------------------------------------------------
| Authorization | for ssh | channel: |     |
| ------------- | ------- | -------- | --- |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 145

---------------------------------------------------------------------------------
| GROUP NAME |     |     |     |     | | GROUP PRIORITY |     |     |
| ---------- | --- | --- | --- | --- | ---------------- | --- | --- |
---------------------------------------------------------------------------------
| tacacs |     |     |     |     | | 0 |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| none   |     |     |     |     | | 1 |     |     |
---------------------------------------------------------------------------------
*********************************
| Command | : show | aaa | server-groups |     |     |     |     |
| ------- | ------ | --- | ------------- | --- | --- | --- | --- |
*********************************
| ******* | AAA | Mechanism | TACACS+ | ******* |     |     |     |
| ------- | --- | --------- | ------- | ------- | --- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     |     | | SERVER NAME | | PORT | PRIORITY | | VRF |
| ---------- | --- | --- | --- | --- | ------------- | ----------------- | ----- |
---------------------------------------------------------------------------------
| tacacs | (default) |     |     |     | | 1.1.1.1 | | 49 | 1 | | mgmt |
| ------ | --------- | --- | --- | --- | --------- | -------- | ------ |
---------------------------------------------------------------------------------
| ******* | AAA | Mechanism | RADIUS | ******* |     |     |     |
| ------- | --- | --------- | ------ | ------- | --- | --- | --- |
---------------------------------------------------------------------------------
| GROUP NAME |     |     |     |     | | SERVER NAME | | PORT | PRIORITY | | VRF |
| ---------- | --- | --- | --- | --- | ------------- | ----------------- | ----- |
---------------------------------------------------------------------------------
***********************************
| Command | : show | tacacs-server |     | detail |     |     |     |
| ------- | ------ | ------------- | --- | ------ | --- | --- | --- |
***********************************
| *******        | Global      | TACACS+                                       | Configuration        |         | ******* |     |     |
| -------------- | ----------- | --------------------------------------------- | -------------------- | ------- | ------- | --- | --- |
| Shared-Secret: |             | G8ekK1cA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA= |                      |         |         |     |     |
| Timeout:       | 5           |                                               |                      |         |         |     |     |
| Auth-Type:     | pap         |                                               |                      |         |         |     |     |
| Tracking:      | disabled    |                                               |                      |         |         |     |     |
| Tracking       | Time        | Interval                                      | (seconds):           |         | 300     |     |     |
| Tracking       | User-name:  |                                               | tacacs-tracking-user |         |         |     |     |
| Tracking       | Password:   |                                               | None                 |         |         |     |     |
| Number         | of Servers: |                                               | 1                    |         |         |     |     |
| ******         | TACACS+     | Server                                        | Information          |         | ******  |     |     |
| Server-Name    |             |                                               | :                    | 1.1.1.1 |         |     |     |
| Auth-Port      |             |                                               | :                    | 49      |         |     |     |
| VRF            |             |                                               | :                    | mgmt    |         |     |     |
Shared-Secret : KCdmOMxMD26T0fQoXfJbtj9j2AUxlGn6eCAAAAF2MkfMTojqX
| Timeout             | (default) |           | :   | 5        |     |     |     |
| ------------------- | --------- | --------- | --- | -------- | --- | --- | --- |
| Auth-Type           | (default) |           | :   | pap      |     |     |     |
| Server-Group        |           | (default) | :   | tacacs   |     |     |     |
| Default-Priority    |           |           | :   | 1        |     |     |     |
| Tracking            |           |           | :   | disabled |     |     |     |
| Reachability-Status |           |           | :   | N/A      |     |     |     |
***********************************
| Command | : show | radius-server |     | detail |     |     |     |
| ------- | ------ | ------------- | --- | ------ | --- | --- | --- |
***********************************
| ******* | Global | RADIUS | Configuration |     | ******* |     |     |
| ------- | ------ | ------ | ------------- | --- | ------- | --- | --- |
Shared-Secret: CPCBMQTG8ekK1cA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA=
| Timeout:   | 5           |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- | --- |
| Auth-Type: | pap         |     |     |     |     |     |     |
| Retries:   | 1           |     |     |     |     |     |     |
| Number     | of Servers: |     | 0   |     |     |     |     |
====================================================
| [End] Feature |     | aaa |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- |
RemoteAAA(TACACS+,RADIUS)commands|146

====================================================
====================================================
| Show Tech | commands |     | executed | successfully |     |     |
| --------- | -------- | --- | -------- | ------------ | --- | --- |
====================================================
| tacacs-server |     |     | auth-type |     |     |     |
| ------------- | --- | --- | --------- | --- | --- | --- |
Syntax
| tacacs-server    | auth-type |           | {pap | | chap} |     |     |
| ---------------- | --------- | --------- | ---- | ------- | --- | --- |
| no tacacs-server |           | auth-type |      |         |     |     |
Description
EnablestheCHAPorPAPauthenticationprotocol,whichisusedforcommunicationwiththeTACACS+
servers,atthegloballevel.Youcanoverridethiscommandwithafine-grainedperserverauth-type
configuration.
ThenoformofthiscommandresetstheglobalauthenticationmechanismforTACACS+toPAP,whichisthe
defaultauthenticationmechanismforTACACS+.
Commandcontext
config
Parameters
| auth-type | {pap | | chap} |     |     |     |     |
| --------- | ------ | ----- | --- | --- | --- | --- |
SelectseitherthePAPorCHAPauthenticationprotocol.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingcommandforCHAPauthentication:
| switch(config)# |     | tacacs-server |     | auth-type |     | chap |
| --------------- | --- | ------------- | --- | --------- | --- | ---- |
EnablingcommandforPAPauthentication:
| switch(config)# |     | tacacs-server |      | auth-type |     | pap |
| --------------- | --- | ------------- | ---- | --------- | --- | --- |
| tacacs-server   |     |               | host |           |     |     |
Syntax
| tacacs-server   | host               | {<FQDN>   |     | | <IPV4>     | | <IPV6>}      |             |
| --------------- | ------------------ | --------- | --- | ------------ | -------------- | ----------- |
| [key [plaintext |                    | <PASSKEY> |     | | ciphertext |                | <PASSKEY>]] |
| [timeout        | <TIMEOUT-SECONDS>] |           |     | [port        | <PORT-NUMBER>] |             |
[auth-type {pap | chap}] [tracking {enable | disable}] [vrf <VRF-NAME>]
| no tacacs-server |     | host | {<FQDN> | | <IPV4> | |   | <IPV6>} |
| ---------------- | --- | ---- | ------- | -------- | --- | ------- |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 147

[port <PORT-NUMBER>] [vrf <VRF-NAME>]

Description

Adds a TACACS+ server. By default, the TACACS+ server is associated with the server group named tacacs.

The no form of this command removes a previously added TACACS+ server.

Command context

config

Parameters

{<FQDN> | <IPV4> | <IPv6>}

Specifies the TACACS+ server as:

n <FQDN>: a fully qualified domain name.

n <IPV4>: an IPv4 address.

n <IPV6>: an IPv6 address.

key {plaintext <PASSKEY> | ciphertext <PASSKEY>}

Specifies either a plaintext or an encrypted local shared-secret passkey for the server. As per RFC 2865,
shared-secret can be a mix of alphanumeric and special characters. The length of shared-secret in
plaintext format is fewer than 32 characters.

When key is entered without either sub-parameter, plaintext passkey prompting occurs upon pressing Enter. The
entered passkey characters are masked with asterisks.
When key is omitted, the server uses the global passkey. This command requires either the global or local
passkey to be set; otherwise the server will not be contacted. Command radius-server key is available for
setting the global passkey.

timeout <TIMEOUT-SECONDS>

Specifies the timeout. The range is 1 to 60 seconds. The default timeout is 5 seconds.

port <PORT-NUMBER>

Specifies the TCP authentication port number. Range: 1 to 65535. Default: 49.

auth-type {pap | chap}

Selects either PAP (default) or CHAP authentication type. If this parameter is not specified, the TACACS+
global default is used.

tracking {enable | disable}

Enables or disables server tracking for the server. Tracked servers are probed at the start of each server
tracking interval to check if they are reachable. Unreachable servers are skipped in favor of servers that
are proven to be reachable. Use command tacacs-server tracking to configure TACACS+ server
tracking.
vrf <VRF-NAME>

Specifies the VRF name to be used for communicating with the server. If no VRF name is provided, the
default VRF named default is used.

Authority

Administrators or local user group members with execution rights for this command.

Usage

If the fully qualified domain name is provided for the TACACS+ server, a DNS server must be configured and
accessible through the same VRF which is configured for the TACACS+ server. This configuration is required
for the resolution of the TACACS+ server hostname to its IP address. If a DNS server is not available for this

Remote AAA (TACACS+, RADIUS) commands | 148

VRF,theTACACS+serversreachablethroughthisVRFmustbeconfiguredbymeansoftheirIPaddresses
only.
Examples
AddingaTACACS+serverwithanIPv4address,plaintextpasskey,timeout,port,authenticationtype,and
VRFname:
switch(config)# tacacs-server host 1.1.1.3 key plaintext test-123 timeout 15 port 32
| auth-type | chap vrf vrf_red |     |     |     |
| --------- | ---------------- | --- | --- | --- |
AddingaTACACS+serverwithanIPv4addressandpromptedplaintextpasskey:
| switch(config)# | tacacs-server     | host 1.1.1.5   | key |     |
| --------------- | ----------------- | -------------- | --- | --- |
| Enter the       | TACACS server     | key: ********* |     |     |
| Re-Enter        | the TACACS server | key: ********* |     |     |
AddingaTACACS+serverwithanIPv4addressandanamedVRF:
| switch(config)# | tacacs-server | host 1.1.1.1 | vrf mgmt |     |
| --------------- | ------------- | ------------ | -------- | --- |
AddingaTACACS+serverwithanIPv4address,aport,andanamedVRF:
| switch(config)# | tacacs-server | host 1.1.1.2 | port 32 vrf | mgmt |
| --------------- | ------------- | ------------ | ----------- | ---- |
AddingaTACACS+serverwithanFQDN,atimeout,portnumber,andanamedVRF:
switch(config)# tacacs-server host abc.com timeout 15 port 32 vrf vrf_blue
AddingaTACACS+serverwithanIPv6address:
switch(config)# tacacs-server host 2001:0db8:85a3:0000:0000:8a2e:0370:7334
DeletingaTACACS+serverwithanIPv4addressandspecifiedVRF:
| switch(config)# | no tacacs-server | host 1.1.1.1 | vrf mgmt |     |
| --------------- | ---------------- | ------------ | -------- | --- |
DeletingaTACACS+serverwithanFQDN,port,andspecifiedVRF:
switch(config)# no tacacs-server host abc.com port 32 vrf vrf_blue
| tacacs-server | key |     |     |     |
| ------------- | --- | --- | --- | --- |
Syntax
tacacs-server key [plaintext <GLOBAL-PASSKEY> | ciphertext <GLOBAL-PASSKEY>]
| no tacacs-server | key |     |     |     |
| ---------------- | --- | --- | --- | --- |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 149

Description
CreatesormodifiesaTACACS+globalpasskey.TheTACACS+globalpasskeyisusedasashared-secretfor
encryptingthecommunicationbetweenallTACACS+serversandtheswitch.TheTACACS+globalpasskeyis
requiredforauthenticationunlesslocalpasskeyshavebeenset.Bydefault,theTACACS+globalpasskeyis
empty.Iftheadministratorhasnotsetthiskey,theswitchwillnotbeabletoperformTACACS+
authentication.Theswitchwillinsteadrelyontheauthenticationmechanismconfiguredwithaaa
| authentication | login. |     |     |     |
| -------------- | ------ | --- | --- | --- |
Whenthiscommandisenteredwithoutparameters,plaintextpasskeypromptingoccursuponpressingEnter.The
enteredpasskeycharactersaremaskedwithasterisks.
Thenoformofthecommandremovestheglobalpasskey.
Commandcontext
config
Parameters
plaintext <GLOBAL-PASSKEY>
SpecifiestheTACACS+globalpasskeyinplaintextformatwithalengthof1to31characters.AsperRFC
2865,shared-secretcanbeamixofalphanumericandspecialcharacters.
ciphertext <GLOBAL-PASSKEY>
SpecifiestheTACACS+globalpasskeyinencryptedformat.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Addingtheglobalpasskey:
| switch(config)# | tacacs-server |     | key plaintext | mypasskey123 |
| --------------- | ------------- | --- | ------------- | ------------ |
Addingtheglobalpasskeywithprompting:
| switch(config)# | tacacs-server     |                | key       |     |
| --------------- | ----------------- | -------------- | --------- | --- |
| Enter the       | TACACS server     | key: ********* |           |     |
| Re-Enter        | the TACACS server | key:           | ********* |     |
Removingtheglobalpasskey:
| switch(config)# | no tacacs-server |     | key |     |
| --------------- | ---------------- | --- | --- | --- |
| tacacs-server   | timeout          |     |     |     |
Syntax
| tacacs-server    | timeout [<1-60>] |     |     |     |
| ---------------- | ---------------- | --- | --- | --- |
| no tacacs-server | timeout          |     |     |     |
Description
RemoteAAA(TACACS+,RADIUS)commands|150

SpecifiesthenumberofsecondstowaitforaresponsefromtheTACACS+serverbeforetryingthenext
TACACS+server.Ifavalueisnotspecified,adefaultvalueof5secondsisused.Youcanoverridethisvalue
withafine-grainedperservertimeoutconfiguredforindividualservers.
ThenoformofthiscommandresetstheTACACS+globalauthenticationtimeouttothedefaultof5seconds.
Commandcontext
config
Parameters
| timeout <1-60> |     |     |     |     |
| -------------- | --- | --- | --- | --- |
Specifiesthetimeoutintervalof1to60seconds.Thedefaultis5seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SpecifyingtheTACACS+servertimeout:
| switch(config)# |     | tacacs-server | timeout 10 |     |
| --------------- | --- | ------------- | ---------- | --- |
ResettingthetimeoutfortheTACACS+servertothedefault:
| switch(config)# |     | no tacacs-server | timeout |     |
| --------------- | --- | ---------------- | ------- | --- |
| tacacs-server   |     | tracking         |         |     |
Syntax
| tacacs-server    | tracking   | interval           | <INTERVAL>   |              |
| ---------------- | ---------- | ------------------ | ------------ | ------------ |
| no tacacs-server |            | tracking interval  |              |              |
| tacacs-server    | tracking   | user-name          | <NAME>       |              |
| [password        | [plaintext | <PASSWORD>         | | ciphertext | <PASSWORD>]] |
| no tacacs-server |            | tracking user-name | <NAME>       |              |
Description
ConfiguresTACACS+servertrackingsettingsgloballyforallconfiguredTACACS+serversthathavetracking
| enabledwiththetacacs-server |     |     | hostcommandonindividualservers. |     |
| --------------------------- | --- | --- | ------------------------------- | --- |
Thenoformofthecommandremovesthespecifiedconfiguration,revertingittoitsdefault.Thenoform
withuser-namealsoclearsthepassword(resetsittoempty).
Commandcontext
config
Parameters
| interval <INTERVAL> |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
Specifiesthetimeinterval,inseconds,towaitbeforecheckingtheserverreachabilitystatus.Default:
300.Range60to84600.
user-name <NAME> [password [plaintext <PASSWORD> | ciphertext <PASSWORD>]]
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 151

Specifies the user name (and optionally a password) to be used for server checking. The default user
name is tacacs-tracking-user with an empty password.

The password is optional and may be entered as plaintext or pasted in as ciphertext. The plaintext
password is visible as cleartext when entered but is encrypted thereafter. Command history does show
the password as cleartext.

When password is entered without a following sub-parameter, plaintext password prompting occurs upon
pressing Enter. The entered password characters are masked with asterisks.

The user does not have to be configured on the server. Server tracking can still be performed with a user which is

not configured on the server because authentication failure on the server achieves confirmation that the server is

reachable.

Server tracking uses authentication request and response packets to determine server reachability status. The

server tracking user name and password are used to form the request packet which is sent to the server with

tracking enabled. Upon receiving a response to the request packet, the server is considered to be reachable.

Authority

Administrators or local user group members with execution rights for this command.

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

Reverting the tracking user name to its default of tacacs-tracking-user:

switch(config)# no tacacs-server tracking user-name

Remote AAA (TACACS+, RADIUS) commands | 152

Chapter 11
|        |                       |     | RADIUS | dynamic | authorization |
| ------ | --------------------- | --- | ------ | ------- | ------------- |
| RADIUS | dynamic authorization |     |        |         |               |
RADIUSdynamicauthorizationprovidestheabilitytomakechangestoauseraccountsessionwhileitisin
progress.Thisabilityincludesdisconnectingasessionorupdatingsomeaspectoftheauthorizationforthe
session.Italsoincludes"potbounce"inwhichtheinterfaceonwhichaclientisconnectedisbroughtdown
andthenbackup(usingCOA(changeofauthorization).
RADIUSdynamicauthorizationenablesordisablestheprocessingof"Disconnect"and"Changeof
Authorization(CoA)"messagesfromtheRADIUSserver.Whenenabled,theRADIUSservercandynamically
terminateorchangetheauthorizationparameters(suchasVLAN/user-roleassignment)usedinanactive
clientsessionontheswitch.
SeealsoRFC3576availableathttp://www.ietf.org/rfc/rfc3576.txtforgeneralinformationonthedynamic
authorizationextensionstoRADIUS.
| Requirements |     | and tips |     |     |     |
| ------------ | --- | -------- | --- | --- | --- |
TheswitchvalidatesthesemandatoryattributesthatmustbepresentintheCoA/DisconnectMessage:
Username
n
|     | IPorNAS IPV6orNASIdentifier |     |     |     |     |
| --- | --------------------------- | --- | --- | --- | --- |
n NAS
n Anyoneofthefollowingcombinationsisusedtoidentifytheclientsession:
o NAS-PortandCalling-Station-ID
o NAS-Port-IDandCalling-Station-ID
o Accounting-Session-ID
RADIUSserverrequirements:
n ForClearPasstoprovideCoAcapabilities,inthecasewheretheswitchsendstheNAS-IPaddressasa
routableIPaddress,theCLIcommandip source interfacemustbeexecutedwiththeradius
parameter.
n InCISCOISE,tosendtheCoArequestwiththesameusernameasintheRADIUSAccept,theIdentity
rewriteoptionhastobeconfigured.
| RADIUS | dynamic           | authorization | commands |     |     |
| ------ | ----------------- | ------------- | -------- | --- | --- |
| radius | dyn-authorization | enable        |          |     |     |
Syntax
| radius    | dyn-authorization | enable |     |     |     |
| --------- | ----------------- | ------ | --- | --- | --- |
| no radius | dyn-authorization | enable |     |     |     |
Description
153
| AOS-CX10.07SecurityGuide| | (6200,6300,6400SwitchSeries) |     |     |     |     |
| ------------------------- | ---------------------------- | --- | --- | --- | --- |

Enables RADIUS dynamic authorization. This command must be issued before the configuration set with
other radius dyn-authorization commands takes effect.

The no form of this command disables RADIUS dynamic authorization.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling RADIUS dynamic authorization:

switch(config)# radius dyn-authorization enable

radius dyn-authorization client

Syntax

radius dyn-authorization client {<IPV4> | <IPV6> | <HOSTNAME>}

[secret-key [plaintext <PASSKEY> | ciphertext] <PASSKEY>]]
[time-window <WIDTH>] [replay-protection {enable|disable}]

no radius dyn-authorization client {<IPV4> | <IPV6> | <HOSTNAME>} [vrf <VRF-NAME>]

Description

Configures RADIUS dynamic authorization for the specified client on the specified (or default) VRF.

The no form of this command unconfigures RADIUS dynamic authorization for the specified client on the
specified (or default) VRF.

Command context

config

Parameters

<IPV4> | <IPV6> | <HOSTNAME>

Specifies the client IPv4 address, IPv6 address, or host name.
secret-key [plaintext <PASSKEY> | ciphertext <PASSKEY>]

Specifies the dynamic authorization server (RADIUS server) shared secret key required for client access.
Provide either a plaintext or an encrypted shared-secret passkey. As per RFC 2865, the shared-secret can
be a mix of alphanumeric and special characters. Plaintext passkeys are between 1 and 32 alphanumeric
and special characters.

When secret-key is entered without either sub-parameter, plaintext shared secret prompting occurs upon
pressing Enter. Enter must be pressed immediately after the secret-key parameter without entering other
parameters. The entered shared secret characters are masked with asterisks.

time-window <WIDTH>

Specifies the width of the synchronization window (in seconds) between the RADIUS dynamic
authorization client and the RADIUS dynamic authorization server. Default 300. Range: 1 to 65535.

replay-protection {enable|disable}

RADIUS dynamic authorization | 154

Enables or disables RADIUS dynamic authorization replay protection for the specified client on the
specified (or default) VRF.

vrf <VRF-NAME>

Specifies the VRF on which the identified client is connected. When omitted, VRF default is assumed.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring RADIUS dynamic authorization with replay protection for a client on the default VRF:

switch(config)# radius dyn-authorization client 1.1.2.5 replay-protection enable

Configuring RADIUS dynamic authorization with time window and shared secret for a client on the default
VRF:

switch(config)# radius dyn-authorization client 1.1.2.7 time-window 8

secret-key plaintext skF82#450

Configuring RADIUS dynamic authorization with a prompted shared secret:

switch(config)# radius dyn-authorization client 1.1.2.7 secret-key
Enter the RADIUS dyn-authorization key: *********
Re-Enter the RADIUS dyn-authorization key: *********

Configuring RADIUS dynamic authorization for a client on the adm2 VRF:

switch(config)# radius dyn-authorization client 1.1.2.1 vrf adm2

radius dyn-authorization client tls (RadSec)

Syntax

radius dyn-authorization client [<IPV4> | <IPV6> |
<HOSTNAME>] tls [replay-protection {enable|disable}][time-window <WIDTH>]
[vrf <VRF-NAME>]

no radius dyn-authorization [client <IP-ADDR>] tls [vrf <VRF-NAME>]

Description

Enables TLS protection for a RADIUS dynamic authorization client on the specified (or default) VRF. RadSec
is a protocol that supports RADIUS over TLS.

The no form of this command deletes TLS protection for the dynamic authorization client.

RadSec server must be configured before configuring dynamic authorization.

Command context

config

Parameters

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

155

<IPV4> | <IPV6> | <HOSTNAME>

Specifies the client IPv4 address, IPv6 address, or host name.

time-window <WIDTH>

Specifies the width of the synchronization window (in seconds) between the RADIUS dynamic
authorization client and the RADIUS dynamic authorization server. Default 300. Range: 1 to 65535.

tls

Specifies the TLS protection for the RADIUS server.

replay-protection {enable|disable}

Enables or disables RADIUS dynamic authorization replay protection for the specified client on the
specified (or default) VRF.

vrf <VRF-NAME>

Specifies the VRF on which the identified client is connected. When omitted, VRF default is assumed.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enables TLS protection for a RADIUS dynamic authorization client with replay protection and time window
for a client on the default VRF:

switch(config)# radius dyn-authorization client 1.1.2.5 tls replay-protection enable

time-window 8

Deleting TLS protection for a dynamic authorization client on the adm2 VRF:

switch(config)# no radius dyn-authorization client 1.1.2.7 tls VRF adm2

radius dyn-authorization port

Syntax

radius dyn-authorization port <PORT-NUMBER>

Description

Sets the RADIUS dynamic authorization server UDP/TCP port.

Command context

config

Parameters

<PORT-NUMBER>

Specifies the UDP or TCP port. Default UDP: 3799 and TCP:2083

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the RADIUS dynamic authorization server UDP port back to its default 3799:

RADIUS dynamic authorization | 156

| switch(config)# | radius | dyn-authorization | port 3799 |     |
| --------------- | ------ | ----------------- | --------- | --- |
SettingtheRADIUSdynamicauthorizationserverTCPportbacktoitsdefault2083:
| switch(config)# | radius            | dyn-authorization | port 2083 |     |
| --------------- | ----------------- | ----------------- | --------- | --- |
| show radius     | dyn-authorization |                   |           |     |
Syntax
| show radius | dyn-authorization |     |     |     |
| ----------- | ----------------- | --- | --- | --- |
Description
ShowsRADIUSdynamicauthorizationconfigurationandsummarizedstatisticsforallclientsconfiguredfor
dynamicauthorization.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
Showcommandoutputitemidentification:
| Radius Dynamic | Authorization:EnabledorDisabledstatus,systemwide. |     |     |     |
| -------------- | ------------------------------------------------- | --- | --- | --- |
n
n Radius Dynamic Authorization Port:TheUDPorTCPportusedfordynamicauthorization(default
3799).
Invalid Client Address in CoA Requests:ThenumberofCoA(changeofauthorization)requests
n
receivedwithanincorrectDAC(dynamicauthorizationclient)address.
Invalid Client Address in Disconnect Requests:Thenumberofdisconnectrequestsreceivedwith
n
incorrectDACaddress.
n Disconnect Requests:ThenumberofdisconnectrequestsreceivedfromtheDAC.
| Disconnect | ACKs:ThenumberofDisconnect-ACKssenttotheDAC. |     |     |     |
| ---------- | -------------------------------------------- | --- | --- | --- |
n
| Disconnect | NAKs:ThenumberofDisconnect-NAKssenttotheDAC. |     |     |     |
| ---------- | -------------------------------------------- | --- | --- | --- |
n
n CoA Requests:ThenumberofCoA-requestsreceivedfromtheDAC.
n CoA ACKs:ThenumberofCoA-ACKssenttotheDAC.
n CoA NAKs:ThenumberofCoA-NAKssenttotheDAC.
Example
ShowingRADIUSdynamicauthorizationsummarizedstatisticsforallclientsconfiguredfordynamic
authorization:
| switch#    | show radius | dyn-authorization |               |             |
| ---------- | ----------- | ----------------- | ------------- | ----------- |
| Status and | Counters    | - RADIUS Dynamic  | Authorization | Information |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 157

|     | RADIUS  | Dynamic       | Authorization    |        |                 |      |           | : Enabled |
| --- | ------- | ------------- | ---------------- | ------ | --------------- | ---- | --------- | --------- |
|     | RADIUS  | Dynamic       | Authorization    |        | UDP             | Port |           | : 3799    |
|     | Invalid |               | Client Addresses |        | in CoA Requests |      |           | : 0       |
|     | Invalid |               | Client Addresses |        | in Disconnect   |      | Requests: | 0         |
|     | Dynamic | Authorization |                  | Client | Information     |      |           |           |
=========================================
|     | IP Address    |            |          | : 1.1.2.1  |     |     |     |     |
| --- | ------------- | ---------- | -------- | ---------- | --- | --- | --- | --- |
|     | VRF           |            |          | : adm2     |     |     |     |     |
|     | Replay        | Protection |          | : Disabled |     |     |     |     |
|     | TLSEnabled    |            | :Yes     |            |     |     |     |     |
|     | Time          | Window     |          | : 20       |     |     |     |     |
|     | Disconnect    |            | Requests | : 1        |     |     |     |     |
|     | Disconnect    |            | ACKs     | : 1        |     |     |     |     |
|     | Disconnect    |            | NAKs     | : 0        |     |     |     |     |
|     | CoA Requests  |            |          | : 7        |     |     |     |     |
|     | CoA ACKs      |            |          | : 2        |     |     |     |     |
|     | CoA-NAKs      |            |          | : 5        |     |     |     |     |
|     | Shared-Secret |            |          | :          |     |     |     |     |
AQBapb+HsdpqV1Q3CPCBMQTG8ekK1cA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA=
|     | IP Address    |            |          | : 1.1.2.5 |     |     |     |     |
| --- | ------------- | ---------- | -------- | --------- | --- | --- | --- | --- |
|     | VRF           |            |          | : default |     |     |     |     |
|     | Replay        | Protection |          | : Enabled |     |     |     |     |
|     | TLSEnabled    |            | :No      |           |     |     |     |     |
|     | Time          | Window     |          | : 20      |     |     |     |     |
|     | Disconnect    |            | Requests | : 6       |     |     |     |     |
|     | Disconnect    |            | ACKs     | : 6       |     |     |     |     |
|     | Disconnect    |            | NAKs     | : 0       |     |     |     |     |
|     | CoA Requests  |            |          | : 9       |     |     |     |     |
|     | CoA ACKs      |            |          | : 5       |     |     |     |     |
|     | CoA-NAKs      |            |          | : 4       |     |     |     |     |
|     | Shared-Secret |            |          | :         |     |     |     |     |
AQBapb+HsdpqV1Q3CPCBMQTG8ekK1cA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA=
|     | IP Address    |            |          | : 1.1.2.7  |     |     |     |     |
| --- | ------------- | ---------- | -------- | ---------- | --- | --- | --- | --- |
|     | VRF           |            |          | : default  |     |     |     |     |
|     | Replay        | Protection |          | : Disabled |     |     |     |     |
|     | TLSEnabled    |            | :Yes     |            |     |     |     |     |
|     | Time          | Window     |          | : 8        |     |     |     |     |
|     | Disconnect    |            | Requests | : 6        |     |     |     |     |
|     | Disconnect    |            | ACKs     | : 6        |     |     |     |     |
|     | Disconnect    |            | NAKs     | : 0        |     |     |     |     |
|     | CoA Requests  |            |          | : 9        |     |     |     |     |
|     | CoA ACKs      |            |          | : 5        |     |     |     |     |
|     | CoA-NAKs      |            |          | : 4        |     |     |     |     |
|     | Shared-Secret |            |          | :          |     |     |     |     |
AQBapb+HsdpqV1Q3CPCBMQTG8ekK1cA+CyD0RvfbeA8BEgikCgAAAJOwZSNzA2SWrLA=
| show | radius |     | dyn-authorization |     |     | client |     |     |
| ---- | ------ | --- | ----------------- | --- | --- | ------ | --- | --- |
Syntax
| show | radius | dyn-authorization |     |     | client <IP-ADDR> |     | [vrf | <VRF-NAME>] |
| ---- | ------ | ----------------- | --- | --- | ---------------- | --- | ---- | ----------- |
Description
ShowsRADIUSdynamicauthorizationstatisticsforthespecifiedclientonthespecifiedVRF.
Commandcontext
RADIUSdynamicauthorization|158

Operator(>)orManager(#)
Parameters
client <IP-ADDR>
SpecifiestheclientIPv4orIPv6address.
vrf <VRF-NAME>
SpecifiestheVRFonwhichtheidentifiedclientisconnected.Whenomitted,VRFdefaultisassumed.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
Showcommandoutputitemidentification:
n Total Requests:ThenumberofDisconnectandCoA(changeofauthorization)requestsreceivedfrom
theDAC(dynamicauthorizationclient).
n Authorize Only Requests:ThenumberofDisconnectandCoArequestsreceivedfromtheDACwithan
"Authorizeonly"Service-Typeattribute.
Malformed Requests:ThenumberofmalformedDisconnectandCoArequestsreceivedfromtheDAC.
n
n Bad Authenticator Requests:ThenumberofDisconnectandCoArequestsreceivedfromthisDACwith
aninvalidauthenticatorfield.
Dropped Requests:ThenumberofDisconnectandCoArequestsfromthisDACthathavebeensilently
n
discardedforreasonsotherthanmalformed,badauthenticators,orunknowntype.
| Total ACK | Responses:ThenumberofDisconnect-ACKssenttotheDAC. |     |     |     |     |
| --------- | ------------------------------------------------- | --- | --- | --- | --- |
n
| Total NAK | Responses:ThenumberofDisconnect-NAKssenttotheDAC. |     |     |     |     |
| --------- | ------------------------------------------------- | --- | --- | --- | --- |
n
n Session Not Found Responses:ThenumberofDisconnect-NAKssenttotheDACbecausenosession
contextcouldbefound.
User Sessions Modified:Thenumberofusersessionsforwhichauthorizationchangeddueto
n
DisconnectandCoArequestsreceivedfromtheDAC.
Example
ShowingRADIUSdynamicauthorizationstatisticsforclient1.1.2.1onVRFdefault:
| switch# show | radius | dyn-authorization |     | client 1.1.2.1 | vrf default |
| ------------ | ------ | ----------------- | --- | -------------- | ----------- |
Status and Counters - RADIUS Dynamic Authorization Client Information
| VRF Name      |         |     | : default  |     |     |
| ------------- | ------- | --- | ---------- | --- | --- |
| Authorization | Client  |     | : 1.1.2.1  |     |     |
| Unknown       | Packets |     | : 55       |     |     |
| Message-Type  |         |     | Disconnect |     | CoA |
---------------------------------------------------------------
| Total Requests    |           |           | 2147483647 |     | 10         |
| ----------------- | --------- | --------- | ---------- | --- | ---------- |
| Authorize         | Only      | Requests  | 10         |     | 10         |
| Malformed         | Requests  |           | 10         |     | 10         |
| Bad Authenticator |           | Requests  | 2147483647 |     | 2147483647 |
| Dropped           | Requests  |           | 10         |     | 10         |
| Total ACK         | Responses |           | 10         |     | 10         |
| Total NAK         | Responses |           | 10         |     | 10         |
| Session           | Not Found | Responses | 10         |     | 10         |
| User Sessions     | Modified  |           | 20         |     | 20         |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 159

show radius dyn-authorization client tls (RadSec)

Syntax

show radius dyn-authorization client <IP-ADDR> tls [vrf <VRF-NAME>]

Description

Shows RADIUS dynamic authorization statistics for the specified client on the specified VRF.

Command context

Operator (>) or Manager (#)

Parameters

client <IP-ADDR>

Specifies the client IPv4 or IPv6 address.

vrf <VRF-NAME>

Specifies the VRF on which the identified client is connected. When omitted, VRF default is assumed.

tls

Specifies whether TLS is enabled for the dynamic authorization client.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

Show command output item identification:

n Total Requests: The number of Disconnect and CoA (change of authorization) requests received from

the DAC (dynamic authorization client).

n Authorize Only Requests: The number of Disconnect and CoA requests received from the DAC with an

"Authorize only" Service-Type attribute.

n Malformed Requests: The number of malformed Disconnect and CoA requests received from the DAC.

n Bad Authenticator Requests: The number of Disconnect and CoA requests received from this DAC with

an invalid authenticator field.

n

Dropped Requests: The number of Disconnect and CoA requests from this DAC that have been silently

discarded for reasons other than malformed, bad authenticators, or unknown type.

n Total ACK Responses: The number of Disconnect-ACKs sent to the DAC.

n Total NAK Responses: The number of Disconnect-NAKs sent to the DAC.

n Session Not Found Responses: The number of Disconnect-NAKs sent to the DAC because no session

context could be found.

n User Sessions Modified: The number of user sessions for which authorization changed due to

Disconnect and CoA requests received from the DAC.

Example

Showing RADIUS dynamic authorization statistics for client 1.1.2.1 with TLS enabled on VRF default:

switch# show radius dyn-authorization client 1.1.2.1 vrf default
Status and Counters - RADIUS Dynamic Authorization Client Information

RADIUS dynamic authorization | 160

| VRF Name      |         | : default |            |     |
| ------------- | ------- | --------- | ---------- | --- |
| Authorization | Client  | : 1.1.2.1 |            |     |
| TLS Enabled   |         | : Yes     |            |     |
| Unknown       | Packets | : 55      |            |     |
| Message-Type  |         |           | Disconnect | CoA |
---------------------------------------------------------------
| Total Requests    |           |           | 2147483647 | 10         |
| ----------------- | --------- | --------- | ---------- | ---------- |
| Authorize         | Only      | Requests  | 10         | 10         |
| Malformed         | Requests  |           | 10         | 10         |
| Bad Authenticator |           | Requests  | 2147483647 | 2147483647 |
| Dropped           | Requests  |           | 10         | 10         |
| Total ACK         | Responses |           | 10         | 10         |
| Total NAK         | Responses |           | 10         | 10         |
| Session           | Not Found | Responses | 10         | 10         |
| User Sessions     | Modified  |           | 20         | 20         |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 161

Chapter 12

PKI

PKI

The public key infrastructure (PKI) feature enables administrators to manage digital certificates on the
switch. The switch uses certificates to validate SSH clients when acting as an SSH server, and when
communicating with syslog servers when TLS encryption is used.

PKI concepts

Digital certificate

A digital certificate is an electronic form of identification that stores important information about an entity
(such as a computer, program, or website). Certificates help secure digital transactions by enabling the end
parties to validate each other's identity. Digital certificates are issued by a certificate authority (CA) and are
composed of an encoded string of characters (usually stored in a file). For example:
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

A certificate authority (CA) is an entity that can issue and sign digital certificates. A CA can be a well-known,
trusted commercial company, or a private entity controlled by your organization. For a commercial CA, the
CA validates the credentials of a user before issuing a certificate and signing it, guaranteeing a certificate
holder's identity. For a private CA, self-signed certificates can be generated as needed for devices on your
network without paying a commercial company.

Root certificate

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

162

A root certificate is a self-signed certificate that is deemed the root of trust for a certificate chain. This is the
certificate that identifies a CA, and is used by the CA to sign any certificates that it issues. When two peers
attempt to establish a secure connection, they use the CA's public key to verify that each other's certificates
were indeed signed by a trusted certificate authority.

Each root CA certificate has a unique fingerprint, which is the hash value of the certificate content. The
fingerprint of a root CA certificate can be used to authenticate the validity of the root CA.

In a certificate chain, the root CA generates a self-signed certificate, and each lower level CA holds a CA
certificate (intermediate certificate) issued by the CA immediately above it. The hierarchy of these
certificates forms a chain of trust.

Leaf certificate

This is the certificate used by a software entity, such as a syslog client, to identify itself to a peer when
establishing a secure connection.

Intermediate certificate

An intermediate certificate is a CA which has been issued by the root certificate or by another intermediate
certificate. Intermediate CAs can issue leaf certificates and sit in between the root and leaf certificates. The
use of an intermediate CA allows administrators to segregate their PKI groups.

Trust anchor

This is the certificate that acts as the base of trust for the validation of other certificates. A trust anchor can
be a root or intermediate certificate issued by a CA.

OCSP

The online certificate status protocol (OCSP) is a real-time method for determining the revocation status of a
certificate. When two peers attempt to establish a secure connection, they can query an OCSP responder to
determine the status (valid or revoked) of each other's certificates. The OCSP responder for a certificate is
typically provided by a server managed by the CA that issued the certificate.

PKI on the switch
The AOS-CX Switch Series switches provides for installation of certificate authority (CA) certificates and the
generation and installation of leaf certificates.

Trust anchor profiles

The switch supports 64 trust anchor (TA) profiles. Each TA profile stores a trusted CA certificate. The
certificate can be either a root CA certificate, which must be self-signed, or an intermediate CA certificate
that is issued by another CA.

The certificate must have its BasicConstraints field with CA key set to true, and its KeyUsage extension field
set with keyCertSign and/or cRLSign.

CA certificates are used to:

n Validate the certificates that remote peers present when attempting to establish a secure connection

with a service on the switch, for example, the SSH server.

PKI | 163

n Validate leaf certificates installed on the switch that are used, for example, by the syslog client, the Web

UI, or REST API.

The TA profile also enables configuration of real-time checking of certificate revocation (through OCSP).

Leaf certificates

Leaf certificates can be installed on the switch for use by features such as the syslog client, the Web UI, or
REST API. If you are purchasing a certificate from a trusted CA, the switch can generate the certificate signing
request (CSR) that is used to obtain the certificate. The switch can also directly generate self-signed
certificates. Alternatively, the certificate and private key can be generated outside the switch and then
imported. X509 certificate management software such as OpenSSL can be used to generate the private key
and CSR and then combine the certificate and private key into one PEM or PKCS#12 file suitable for
importation into the switch.

Mandatory matching of peer device hostname

While validating the peer device certificates, the switch checks that the peer device configured hostname
matches either the Subject Alternative Name (SAN) field or the Common Name (CN) within the certificate
Subject field. If the SAN field is present and matches the hostname, validation succeeds, otherwise it fails. If
the SAN field is not present, and the CN matches the hostname, validation succeeds, otherwise it fails.

PKI EST
EST (Enrollment over Secure Transport) (RFC 7030) defines the protocol that devices use to request trusted
certificate authority (CA) certificates and to enroll / re-enroll device certificates from CA services using secure
channels, specifically HTTP over TLS.

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

n EST supports up to:

o 16 EST profiles

o 63 trusted CA certificates downloaded from EST servers.

o 18 device certificates enrolled through EST services.

n EST profile configuration is supported through the CLI and the REST API PKI_EST_Profile.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

164

CAcertificaterequestanddevicecertificateenrollmentissupportedthroughtheCLIandtheREST
n
| customAPICertificateManager |     |           | /certificate. |                 |            |     |
| --------------------------- | --- | --------- | ------------- | --------------- | ---------- | --- |
| Prerequisites               |     | for using | EST           | for certificate | enrollment |     |
n EstablishthePKIinfrastructureforyouorganization,withtheCAchainandservicereadytoissue
certificates.IssueaservicecertificatefortheESTserver.
InstalltherootCAcertificateinaTAprofileontheswitchthatwillvalidatetheESTservercertificateusing
n
| CLIcommandscryptopki |     |     | ta-profileandta-certificate. |     |     |     |
| -------------------- | --- | --- | ---------------------------- | --- | --- | --- |
Optionally,preconfigureanESTclientcertificateontheswitch.
n
MaketheESTserverreachablefromtheswitch.ConnecttheCAservice(s)totheESTserver.Ifthereisa
n
clientcertificatefortheESTclient,installtherootCAcertificateontheserverthatwillvalidatetheclient
certificate.
| EST profile |     | configuration |     |     |     |     |
| ----------- | --- | ------------- | --- | --- | --- | --- |
Intheglobalconfigurationcontext,createanESTprofileandenteritscontext:
| crypto pki | est-profile | <EST-NAME> |     |     |     |     |
| ---------- | ----------- | ---------- | --- | --- | --- | --- |
InanESTprofilecontext,configuretheESTprofileparametersusingthesecommands:
url <URL>
vrf <VRF-NAME>
| username                     | <USERNAME> | password    | [ciphertext | <CIPHERTEXT-PASSWORD> |     | |   |
| ---------------------------- | ---------- | ----------- | ----------- | --------------------- | --- | --- |
|                              |            |             | plaintext   | <PLAINTEXT-PASSWORD>] |     |     |
| retry-interval               |            | <INTERVAL>  |             |                       |     |     |
| retry-count                  | <RETRIES>  |             |             |                       |     |     |
| arbitrary-label              |            | <LABEL>     |             |                       |     |     |
| arbitrary-label-enrollment   |            |             | <LABEL>     |                       |     |     |
| arbitrary-label-reenrollment |            |             | <LABEL>     |                       |     |     |
| reenrollment-lead-time       |            | <LEAD-TIME> |             |                       |     |     |
| Certificate                  |            | enrollment  |             |                       |     |     |
Intheglobalconfigurationcontext,createacertificateandenteritscontext:
| crypto pki | certificate | <CERT-NAME> |     |     |     |     |
| ---------- | ----------- | ----------- | --- | --- | --- | --- |
Inacertificateconfigurationcontext,configurethecertificateparameters:
| key-type | {rsa         | [key-size   | <K-SIZE>]      | | ecdsa [curve-size | <C-SIZE>]} |     |
| -------- | ------------ | ----------- | -------------- | ------------------- | ---------- | --- |
| subject  | [common-name |             | <COMMON-NAME>] |                     |            |     |
|          | [country     | <COUNTRY>]  |                |                     |            |     |
|          | [locality    | <LOCALITY>] |                |                     |            |     |
[org <ORG-NAME>]
|     | [org-unit | <ORG-UNIT>] |     |     |     |     |
| --- | --------- | ----------- | --- | --- | --- | --- |
|     | [state    | <STATE>]    |     |     |     |     |
Inacertificateconfigurationcontext,enrollthecertificateusinganESTservice:
| enroll est-profile |     | <EST-NAME>    |     |     |     |     |
| ------------------ | --- | ------------- | --- | --- | --- | --- |
| Certificate        |     | re-enrollment |     |     |     |     |
n There-enrollmentrequestissentautomaticallytothesameESTserverthatwasusedfortheoriginal
enrollment.
n Theswitchpresentstheenrolledcertificatebeingre-enrolledtotheESTserverforauthentication.Ifthe
certificatehasexpiredorauthenticationfailsforanyreason,theswitchfallsbacktousingtheESTclient
PKI|165

certificate or the username and password in the EST profile, whichever is configured, and performs a new
certificate enrollment.

n Re-enrollment lead-time is configurable in the EST profile using CLI command reenrollment-lead-time.
It sets the number of days before certificate expiry date that certificate re-enrollment will be initiated.

Checking EST profile and certificate configuration

Show the list of EST profiles or details of a specific EST profile:
show crypto pki est-profile [<EST-NAME>]

Show a list of TA profiles whether directly configured or EST-enrolled, or details of a specific TA profile:
show crypto pki ta-profile [<TA-NAME>]

Show the list of certificates whether directly configured or EST-enrolled, or details of a specific certificate:
show crypto pki certificate [<CERT-NAME> [plaintext | pem]]

Show all certificates assigned to the switch EST client as well as certificates that are assigned to other
applications on the switch.:
show crypto pki application

EST best practices

Ensure the following:

n A time synchronization service is used on both the switch (the EST client) and the EST server.

n In all CA certificates, the Basic Constraints field has CA set to true, pathlen is set appropriately, and Key

Usage is set with keyCertSign.

n In all leaf certificates, the Extended Key Usage field is set with the appropriate purpose as follows:

o For server certificates, set with serverAuth. The Key Usage field has at least one of

digitalSignature, keyEncipherment, or keyAgreement.

o For client certificates, set with clientAuth. The Key Usage field has at least one of

digitalSignature, or keyAgreement.

n The EST server is configured to include the intermediate issuer CA certificates in the trusted CA certificate

chain that the EST server sends to the switch (the EST client) upon request.

Example using EST for certificate enrollment
This example illustrates the configuration of an EST profile and enrolling application certificates using an EST
server.

Prerequisites:

n An EST server is reachable from the switch management port.

n Availability of the root CA certificate used to validate the server certificate.

This example shows the following:

n Installing the root CA certificate as a TA profile for validation of the EST server certificate.

n Configuring an EST profile with the EST server information, including the username and password for

client authentication and the EST server URL.

n Issuing a request to enroll a leaf certificate using the EST server.

n Assigning the enrolled certificate to the EST client and syslog client on the switch.

Each section in the below example is preceded by descriptive text.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

166

Example
================================================================================
| The switch | in its default | configuration | state. |
| ---------- | -------------- | ------------- | ------ |
================================================================================
| switch# | show running-config |     |     |
| ------- | ------------------- | --- | --- |
| Current | configuration:      |     |     |
!
| !Version          | ArubaOS-CX FL.10.06.0001CM |     |     |
| ----------------- | -------------------------- | --- | --- |
| !export-password: | default                    |     |     |
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
ip dhcp
!
!
| https-server | vrf default |     |     |
| ------------ | ----------- | --- | --- |
| https-server | vrf mgmt    |     |     |
switch#
================================================================================
The mgmt port is connected to a network with DNS available and the
| EST server | reachable. |     |     |
| ---------- | ---------- | --- | --- |
================================================================================
PKI|167

switch#
|                          | show       | interface       | mgmt |     |                              |     |     |     |     |     |
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
switch(config)#
|     |     | crypto | pki | ta-profile |     | root-ca-for-est-server |     |     |     |     |
| --- | --- | ------ | --- | ---------- | --- | ---------------------- | --- | --- | --- | --- |
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
| The certificate |     | you | are | importing | has | the | following |     | attributes: |     |
| --------------- | --- | --- | --- | --------- | --- | --- | --------- | --- | ----------- | --- |
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
switch(config)#
================================================================================
Configure the EST profile with the EST server URL, username/password.
================================================================================
| switch(config)# |     | crypto | pki | est-profile |     | test-est-server |     |     |     |     |
| --------------- | --- | ------ | --- | ----------- | --- | --------------- | --- | --- | --- | --- |
switch(config-est-test-est-server)#
switch(config-est-test-est-server)# user fred password plaintext barney
switch(config-est-test-est-server)#
switch(config-est-test-est-server)#
url https://999.0.10.229:8443/.well-known/est
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 168

switch(config-est-test-est-server)#
switch(config-est-test-est-server)#
exit
switch(config)#
================================================================================
At the time the EST URL is set, the switch sends a request to the EST server to
get the set of trusted CA certs. If that is successful, TA profiles will be
| auto-created | for      | those | CA certs.   |         |                  |     |     |     |
| ------------ | -------- | ----- | ----------- | ------- | ---------------- | --- | --- | --- |
| Display      | the list | of    | TA profiles | and EST | profile details. |     |     |     |
================================================================================
| switch(config)# |      | show | crypto pki | ta-profile     |     |            |       |     |
| --------------- | ---- | ---- | ---------- | -------------- | --- | ---------- | ----- | --- |
| TA Profile      | Name |      |            | TA Certificate |     | Revocation | Check |     |
-------------------------------- -------------------- ----------------
| test-est-server-est-ta00         |      |          |              | Installed,                                | valid           | OCSP     |     |     |
| -------------------------------- | ---- | -------- | ------------ | ----------------------------------------- | --------------- | -------- | --- | --- |
| test-est-server-est-ta02         |      |          |              | Installed,                                | valid           | OCSP     |     |     |
| test-est-server-est-ta05         |      |          |              | Installed,                                | valid           | OCSP     |     |     |
| test-est-server-est-ta01         |      |          |              | Installed,                                | valid           | OCSP     |     |     |
| root-ca-for-est-server           |      |          |              | Installed,                                | valid           | disabled |     |     |
| test-est-server-est-ta04         |      |          |              | Installed,                                | valid           | OCSP     |     |     |
| test-est-server-est-ta03         |      |          |              | Installed,                                | valid           | OCSP     |     |     |
| switch(config)#                  |      | show     | crypto pki   | est-profile                               |                 |          |     |     |
|                                  |      |          |              | Downloaded                                | Enrolled        |          |     |     |
| Profile                          | Name |          |              | TA Profiles                               | Certificates    |          |     |     |
| -------------------------------- |      |          |              | -----------                               | ------------    |          |     |     |
| test-est-server                  |      |          |              |                                           | 6               | 1        |     |     |
| switch(config)#                  |      | show     | crypto pki   | est-profile                               | test-est-server |          |     |     |
| Profile                          | Name |          | :            | test-est-server                           |                 |          |     |     |
| Service                          | VRF  |          | :            | mgmt                                      |                 |          |     |     |
| Service                          | URL  |          | :            | https://999.0.10.229:8443/.well-known/est |                 |          |     |     |
| Arbitrary                        |      | Label    |              | : not                                     | configured      |          |     |     |
| Arbitrary                        |      | Label    | Enrollment   | : not                                     | configured      |          |     |     |
| Arbitrary                        |      | Label    | Reenrollment | : not                                     | configured      |          |     |     |
| Authentication                   |      | Username | :            | fred                                      |                 |          |     |     |
| Authentication                   |      | Password | :            |                                           |                 |          |     |     |
AQBapR7ndgoxkMlWQUQvK+Dvd3S6m+s9fdaPQwdkMbIYEMnMBgAAAHRhhliYwA==
| Retry        | Interval     |          | :      | 30 seconds |     |     |     |     |
| ------------ | ------------ | -------- | ------ | ---------- | --- | --- | --- | --- |
| Retry        | Count        |          | :      | 3 times    |     |     |     |     |
| Reenrollment |              | Lead     | Time : | 2 days     |     |     |     |     |
| Downloaded   | TA           | Profiles | :      | 6          |     |     |     |     |
| Enrolled     | Certificates |          | :      |            |     |     |     |     |
cert-for-app
switch(config)#
================================================================================
| Originally, | the | switch | only has | two built-in | certificates. |     |     |     |
| ----------- | --- | ------ | -------- | ------------ | ------------- | --- | --- | --- |
================================================================================
| switch(config)# |     | show | crypto pki | certificate |     |     |     |     |
| --------------- | --- | ---- | ---------- | ----------- | --- | --- | --- | --- |
Certificate Name Cert Status EST Status Associated Applications
---------------------- -------------- ----------------- ----------------------------
--
| local-cert |     |     | installed | n/a |     | captive-portal, |     | est-client, |
| ---------- | --- | --- | --------- | --- | --- | --------------- | --- | ----------- |
PKI|169

|     |     |     |     |     |     |     |     |     | https-server, |     | radsec-client, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- |
syslog-client
| device-identity |     |     | installed |     |     | n/a |     |     | none |     |     |
| --------------- | --- | --- | --------- | --- | --- | --- | --- | --- | ---- | --- | --- |
switch(config)#
================================================================================
fields.
Create a new certificate, configure its key type, key size, and subject
================================================================================
| switch(config)# |     | crypto | pki | certificate |     | cert-for-app |     |     |     |     |     |
| --------------- | --- | ------ | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- |
switch(config-cert-cert-for-app)#
| switch(config-cert-cert-for-app)# |     |     |     |     | key-type |     | ecdsa | curve-size |     | 521 |     |
| --------------------------------- | --- | --- | --- | --- | -------- | --- | ----- | ---------- | --- | --- | --- |
switch(config-cert-cert-for-app)#
| switch(config-cert-cert-for-app)# |     |     |     |     | subject |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Do you want to use the switch serial number as the common name (y/n)? n
| Common | Name: | 999.100.205.146 |     |     |     |     |     |     |     |     |     |
| ------ | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Org Unit:
Aruba-Roseville
| Org Name: | HPE       |     |     |     |     |     |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Locality: | Roseville |     |     |     |     |     |     |     |     |     |     |
State: CA
| Country: | US  |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
switch(config-cert-cert-for-app)#
================================================================================
| Request | to enroll | the | certificate |     | through |     | the | EST server. |     |     |     |
| ------- | --------- | --- | ----------- | --- | ------- | --- | --- | ----------- | --- | --- | --- |
================================================================================
switch(config-cert-cert-for-app)# enroll est-profile test-est-server
| You are  | enrolling | a      | certificate  |     | with | the                 | following | attributes: |        |     |     |
| -------- | --------- | ------ | ------------ | --- | ---- | ------------------- | --------- | ----------- | ------ | --- | --- |
| Subject: | C=US,     | ST=CA, | L=Roseville, |     |      | OU=Aruba-Roseville, |           |             | O=HPE, |     |     |
CN=999.100.205.146
| Key Type: | ECDSA  | (521) |     |     |     |     |     |     |     |     |     |
| --------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Continue  | (y/n)? | y     |     |     |     |     |     |     |     |     |     |
Certificate enrollment via test-est-server has been initiated. Please use
| 'show crypto |     | pki certificate |     |     | cert-for-app' |     | to  | check | its status. |     |     |
| ------------ | --- | --------------- | --- | --- | ------------- | --- | --- | ----- | ----------- | --- | --- |
switch(config-cert-cert-for-app)#
================================================================================
| Check the | cert | status | to  | see | if enrollment |     | is  | successful. |     | It is. |     |
| --------- | ---- | ------ | --- | --- | ------------- | --- | --- | ----------- | --- | ------ | --- |
================================================================================
| switch(config-cert-cert-for-app)# |     |     |     |     | show | crypto |     | pki certificate |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ---- | ------ | --- | --------------- | --- | --- | --- |
Certificate Name Cert Status EST Status Associated Applications
---------------------- -------------- ----------------- ----------------------------
--
| local-cert |     |     | installed |     |     | n/a |     |     | captive-portal, |     | est-client,    |
| ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --------------- | --- | -------------- |
|            |     |     |           |     |     |     |     |     | https-server,   |     | radsec-client, |
syslog-client
| device-identity |     |     | installed |     |     | n/a    |         |     | none |     |     |
| --------------- | --- | --- | --------- | --- | --- | ------ | ------- | --- | ---- | --- | --- |
| cert-for-app    |     |     | installed |     |     | enroll | success |     | none |     |     |
switch(config-cert-cert-for-app)#
| switch(config-cert-cert-for-app)# |     |     |     |     | exit |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
switch(config)#
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 170

| switch(config)# |     | show crypto        | pki certificate | cert-for-app |     | pem |
| --------------- | --- | ------------------ | --------------- | ------------ | --- | --- |
| Certificate     |     | Name: cert-for-app |                 |              |     |     |
| Associated      |     | Applications:      |                 |              |     |     |
est-client
| Certificate |         | Status: installed |     |     |     |     |
| ----------- | ------- | ----------------- | --- | --- | --- | --- |
| EST         | Status: | enroll success    |     |     |     |     |
| Certificate |         | Type: regular     |     |     |     |     |
Intermediates:
|     | Subject: | C = US, ST   | = CA, O = HPE, | OU = Aruba, | CN  | = danest-int2 |
| --- | -------- | ------------ | -------------- | ----------- | --- | ------------- |
|     | Issuer:  | C = US, ST   | = CA, O = HPE, | OU = Aruba, | CN  | = danest-int1 |
|     | Serial   | Number: 0x02 |                |             |     |               |
|     | Subject: | C = US, ST   | = CA, O = HPE, | OU = Aruba, | CN  | = danest-int1 |
Issuer: C = US, ST = CA, L = Roseville, O = HPE, OU = Aruba, CN = danest-root
|     | Serial | Number: 0x01 |     |     |     |     |
| --- | ------ | ------------ | --- | --- | --- | --- |
Subject: C = US, ST = CA, L = Roseville, O = HPE, OU = Aruba, CN = danest-root
Issuer: C = US, ST = CA, L = Roseville, O = HPE, OU = Aruba, CN = danest-root
|     | Serial     | Number: 0xAB6626FXXXXD45D |     |     |     |     |
| --- | ---------- | ------------------------- | --- | --- | --- | --- |
|     | -----BEGIN | CERTIFICATE-----          |     |     |     |     |
MIICizCCAjKgAwIBAgICAIgwCQYHKoZIzj0EATBOMQswCQYDVQQGEwJVUzELMAkG
A1UECBMCQ0ExDDAKBgNVBAoTA0hQRTEOMAwGA1UECxMFQXJ1YmExFDASBgNVBAMT
C2RhbmVzdC1pbnQyMB4XDTIwMTAyODE5NTczOVoXDTIwMTEyNTE5NTczOVowbzEL
...
RTEOMAwGA1UECxMFQXJ1YmExFDASBgNVBAMTC2RhbmVzdC1pbnQxggECMAkGByqG
SM49BAEDSAAwRQIgVC1kVIewXhpBSQVqVsQ36MbzrhR4XsaGbQeu7+O8gbUCIQCH
cS17gcLbNxJ1WVr2jnZpPBxy9vID38FjirJiGZ5cZw==
|     | -----END   | CERTIFICATE----- |     |     |     |     |
| --- | ---------- | ---------------- | --- | --- | --- | --- |
|     | -----BEGIN | CERTIFICATE----- |     |     |     |     |
MIIBpzCCAU2gAwIBAgIBAjAJBgcqhkjOPQQBME4xCzAJBgNVBAYTAlVTMQswCQYD
VQQIEwJDQTEMMAoGA1UEChMDSFBFMQ4wDAYDVQQLEwVBcnViYTEUMBIGA1UEAxML
ZGFuZXN0LWludDEwHhcNMjAwNTIwMDUyNDExWhcNMzAwNTE4MDUyNDExWjBOMQsw
...
7ovbXodgN8lqDvBl1VTJYlLBSzl9FKMdMBswDAYDVR0TBAUwAwEB/zALBgNVHQ8E
BAMCAQYwCQYHKoZIzj0EAQNJADBGAiEA+i3x7KEZsxObVruM1kwqWe+QXiLKbgNL
fL077jsSMhYCIQD/dFBkH/yN0NFzb3wI7OaooO83HY2p/47t2pIBk/JNfg==
|     | -----END   | CERTIFICATE----- |     |     |     |     |
| --- | ---------- | ---------------- | --- | --- | --- | --- |
|     | -----BEGIN | CERTIFICATE----- |     |     |     |     |
MIIBuTCCAWGgAwIBAgIBATAJBgcqhkjOPQQBMGIxCzAJBgNVBAYTAlVTMQswCQYD
VQQIEwJDQTESMBAGA1UEBxMJUm9zZXZpbGxlMQwwCgYDVQQKEwNIUEUxDjAMBgNV
BAsTBUFydWJhMRQwEgYDVQQDEwtkYW5lc3Qtcm9vdDAeFw0yMDA1MjAwNTE1MjNa
...
BgNVHRMEBTADAQH/MAsGA1UdDwQEAwIBBjAJBgcqhkjOPQQBA0cAMEQCIGrlZmBX
SmbhDvG9pRiXG0YMqVbvZd37jRQdE+mEk2jfAiBFGhzMjUadhQbuPUTNs9A7bdYk
wej0mJe5bRpd7sqwRQ==
|     | -----END   | CERTIFICATE----- |     |     |     |     |
| --- | ---------- | ---------------- | --- | --- | --- | --- |
|     | -----BEGIN | CERTIFICATE----- |     |     |     |     |
MIIB2DCCAX6gAwIBAgIJAKtmJvZZy9RdMAoGCCqGSM49BAMCMGIxCzAJBgNVBAYT
AlVTMQswCQYDVQQIEwJDQTESMBAGA1UEBxMJUm9zZXZpbGxlMQwwCgYDVQQKEwNI
UEUxDjAMBgNVBAsTBUFydWJhMRQwEgYDVQQDEwtkYW5lc3Qtcm9vdDAeFw0yMDA1
...
VCnKTlhxfmV72nfxYpI979UsopuP5nCjHTAbMAwGA1UdEwQFMAMBAf8wCwYDVR0P
BAQDAgEGMAoGCCqGSM49BAMCA0gAMEUCIQDb/uHvU8DFRTyfnP9wk1i6sdeo6yN0
UvUO5t7/rrVxRQIgMHGjHhaN1nkjYBG8Ei3C1UDILiKlO7McMTCWVo4Ik5c=
|     | -----END | CERTIFICATE----- |     |     |     |     |
| --- | -------- | ---------------- | --- | --- | --- | --- |
switch(config)#
================================================================================
| Initially, | all | applications | use the | default local-cert. |     |     |
| ---------- | --- | ------------ | ------- | ------------------- | --- | --- |
================================================================================
| switch(config)# |     | show crypto | pki application |     |     |     |
| --------------- | --- | ----------- | --------------- | --- | --- | --- |
PKI|171

| Associated | Applications | Certificate | Name | Cert Status |     |
| ---------- | ------------ | ----------- | ---- | ----------- | --- |
-------------------------- ------------------- ---------------------------------
| captive-portal |     |     |     | not configured, | using local-cert |
| -------------- | --- | --- | --- | --------------- | ---------------- |
| est-client     |     |     |     | not configured, | using local-cert |
| https-server   |     |     |     | not configured, | using local-cert |
| radsec-client  |     |     |     | not configured, | using local-cert |
| syslog-client  |     |     |     | not configured, | using local-cert |
switch(config)#
================================================================================
| Assign | the newly enrolled | cert to | applications | as desired. |     |
| ------ | ------------------ | ------- | ------------ | ----------- | --- |
In this example, the cert is assigned to the est-client and syslog.
================================================================================
switch(config)# crypto pki application est-client certificate cert-for-app
switch(config)# crypto pki application syslog-client certificate cert-for-app
switch(config)#
| switch(config)# | show         | crypto pki  | application |             |     |
| --------------- | ------------ | ----------- | ----------- | ----------- | --- |
| Associated      | Applications | Certificate | Name        | Cert Status |     |
-------------------------- ------------------- ------------------------------
| captive-portal |     |              |     | not configured, | using local-cert |
| -------------- | --- | ------------ | --- | --------------- | ---------------- |
| est-client     |     | cert-for-app |     | valid           |                  |
| https-server   |     |              |     | not configured, | using local-cert |
| radsec-client  |     |              |     | not configured, | using local-cert |
| syslog-client  |     | cert-for-app |     | valid           |                  |
switch(config)#
| Example | including | the | use of an | intermediate | certificate |
| ------- | --------- | --- | --------- | ------------ | ----------- |
Thisexampleshowsthefollowing:
InstallingarootCAasaTAprofile.
n
CreatingaCSRforaleafcertificate.
n
InstallingthesignedleafcertificateissuedbyanintermediateCA.TheintermediateCAcertificateis
n
includedafterthesignedleafcertificate.
Eachsectioninthebelowexampleisprecededbydescriptivetext.
Example
================================================================================
| Install | root CA as a | TA profile |     |     |     |
| ------- | ------------ | ---------- | --- | --- | --- |
================================================================================
| switch(config)#         | crypto | pki ta-profile | root   |          |     |
| ----------------------- | ------ | -------------- | ------ | -------- | --- |
| switch(config-ta-root)# |        | ta-certificate | import | terminal |     |
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-ta-cert)# |     | -----BEGIN | CERTIFICATE----- |     |     |
| ----------------------- | --- | ---------- | ---------------- | --- | --- |
switch(config-ta-cert)# MIIGATCCA+mgAwIBAgIJAL/JIZfJ0GpcMA0GCSqGSIUAMIGOMQswCQYD
switch(config-ta-cert)# VQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESBwwJUm9zZXZpbGxl
switch(config-ta-cert)# MQwwCgYDVQQKDANIUEUxEzARBgNVBAsMCk5ldmcxFTATBgNVBAMMDFRl
...
switch(config-ta-cert)# rvadRXSAsUlevJRNNOyINrEJyOfUX2hAfLaiBYP+In6gKTAwVh1xLiXn
switch(config-ta-cert)# LlryAb2/go4BTYjil3eJyXxweUHheuBeesEslBawLv0cPCQPTTdbc97O
switch(config-ta-cert)# iWbyAmfSpD/TS3AgCLnBFPKEKsms0f0LF3/C9dRUXjIHT/LDBr+lgzY3
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 172

| switch(config-ta-cert)# |     |     |     | m2NCvxY= |                  |     |     |
| ----------------------- | --- | --- | --- | -------- | ---------------- | --- | --- |
| switch(config-ta-cert)# |     |     |     | -----END | CERTIFICATE----- |     |     |
switch(config-ta-cert)#
| The certificate |     | you | are | importing | has | the following | attributes: |
| --------------- | --- | --- | --- | --------- | --- | ------------- | ----------- |
Subject: C = US, ST = California, L = Roseville, O = HPE, OU = Networking,
| CN = Test | CA  | root, | emailAddress |     | =   | generic@corp.com |     |
| --------- | --- | ----- | ------------ | --- | --- | ---------------- | --- |
Issuer: C = US, ST = California, L = Roseville, O = HPE, OU = Networking,
| CN =Test       | CA root, | emailAddress       |      |             | = generic@corp.com |          |              |
| -------------- | -------- | ------------------ | ---- | ----------- | ------------------ | -------- | ------------ |
| Serial Number: |          | 0xBFC92197xxxxxxxx |      |             |                    |          |              |
| TA certificate |          | import             | is   | allowed     | only               | once for | a TA profile |
| Do you want    | to       | accept             | this | certificate |                    | (y/n)?   | y            |
switch(config-ta-root)#
exit
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
================================================================================
Install the signed leaf certificate issued by an intermediate CA. The
1intermediate CA certificate is included after the signed leaf certificate.
================================================================================
| switch(config-cert-leaf)# |     |     |     | import | terminal | ta-profile | root |
| ------------------------- | --- | --- | --- | ------ | -------- | ---------- | ---- |
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-cert-import)# |     |     |     | -----BEGIN |     | CERTIFICATE----- |     |
| --------------------------- | --- | --- | --- | ---------- | --- | ---------------- | --- |
switch(config-cert-import)# MIIEKTCCAhGgAwIBAgIJAO1LSoBmKxtbMA0GCSqGSIYxCzAJBgNV
switch(config-cert-import)# BAYTAkFVMRUwEwYDVQQIDAxJbnRlcm1lZGNVBAoMGEludGVybmV0
switch(config-cert-import)# IFdpZGdpdHMgUHR5IEx0ZDENMAsGA1UEAw0yMDA1MTQyMDI3MTla
...
switch(config-cert-import)# axnZcIaNp4eNi95in+TvckXA0eMLScNyR7IF+Wjn56H0fQKYsHp/
switch(config-cert-import)# jllbCkyB1xKnn6IpzIj/hvAx3NpA0jXx/qJA+V/cltaAL6+QPZmI
switch(config-cert-import)# vr5GZsoV72BHFOXxoteZlmWMUdVldYXXP2DzEUbttr9zojwz0MyK
PKI|173

| switch(config-cert-import)# |     | Qz5tc0BlGfJAtghykw== |                  |     |     |
| --------------------------- | --- | -------------------- | ---------------- | --- | --- |
| switch(config-cert-import)# |     | -----END             | CERTIFICATE----- |     |     |
| switch(config-cert-import)# |     | -----BEGIN           | CERTIFICATE----- |     |     |
switch(config-cert-import)# MIIFyzCCA7OgAwIBAgIJAO1LSoBmKxtwMA0GCSqGCIGOMQswCQYD
switch(config-cert-import)# VQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvc1UEBwwJUm9zZXZpbGxl
switch(config-cert-import)# MQwwCgYDVQQKDANIUEUxEzARBgNVBAsMCmcxFTATBgNVBAMMDFRl
...
switch(config-cert-import)# LM9DV3YNWOM4UMMP2HXaDDfqxZPX9Zsj6Gl/stRCh8SVfsF2duYR
switch(config-cert-import)# 5brLfEpiDhXrZVXxF9lljRABO2JPLSUufg7xr6M/K5aCujxVYzK7
switch(config-cert-import)# DQaCEw5NlmC1vpYlY2TG3dlUQPZDeQOAHwuBd4HewqDHWfp/T04=
| switch(config-cert-import)# |     | -----END | CERTIFICATE----- |     |     |
| --------------------------- | --- | -------- | ---------------- | --- | --- |
switch(config-cert-import)#
Leaf certificate is validated with root and imported successfully.
switch(config-cert-leaf)#
Installing a self-signed leaf certificate (created inside the
switch)
Thisproceduredescribeshowtocreate(whollyinsidetheswitch)andinstallaself-signedX.509leaf
certificate.Andassociateitwithoneofthefollowingswitchfeatures:syslogclient,RadSecclient,captive-
portal,HTTPSserver,orHSC(hardwareswitchcontroller).
Procedure
1. Createaleafcertificatecontextwiththecommandcrypto pki certificate.Thisswitchestothe
leafcertificateconfigurationcontext.
2. Defineleafcertificatepropertieswiththecommandsubject.
3. Settheencryptionkeytypefortheleafcertificatewiththecommandkey-type.
4. Generateandinstalltheself-signedcertificatewiththecommand enroll self-signed.
5. Exittheleafcertificatecontextwiththecommandexit.
6. Associatetheleafcertificatewithaswitchfeature(syslogclient,RadSecclient,captive-portal,HTTPS
| server,orHSC)withthecommandcrypto |     |     | pki | application. |     |
| --------------------------------- | --- | --- | --- | ------------ | --- |
Example
Thisexample:
Createstheleafcertificatecontext.
n
n Definestheleafcertificatecharacteristics.
n Createsandinstallstheself-signedleafcertificate.
n Associatestheleafcertificatewiththesyslogclient(application)ontheswitch.
| switch(config)#           | crypto  | pki cert | SS_LC            |                |     |
| ------------------------- | ------- | -------- | ---------------- | -------------- | --- |
| 8400X(config-cert-SS_LC)# |         | subject  | common-name      | SSLeaf country | US  |
| state CA locality         | Rocklin | org      | Company org-unit | Site           |     |
8400X(config-cert-SS_LC)#
|                           |                   | key-type | rsa key-size        | 3072        |     |
| ------------------------- | ----------------- | -------- | ------------------- | ----------- | --- |
| 8400X(config-cert-SS_LC)# |                   | enroll   | self-signed         |             |     |
| You are enrolling         | a certificate     |          | with the following  | attributes: |     |
| Subject: C=US,            | ST=CA, L=Rocklin, |          | OU=Site, O=Company, |             |     |
CN=SSLeaf
| Key Type: RSA   | (3072) |     |     |     |     |
| --------------- | ------ | --- | --- | --- | --- |
| Continue (y/n)? | y      |     |     |     |     |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 174

Self-signed certificate is created and enrolled successfully.
8400X(config-cert-SS_LC)# exit
switch(config)# crypto pki application syslog-client certificate SS_LC

Installing a self-signed leaf certificate (created outside the
switch)
This procedure describes how to install a self-signed X.509 leaf certificate (that was created outside the
switch). And then associate the certificate with one of the following switch features: syslog client, RadSec
client, captive-portal, HTTPS server, or HSC (hardware switch controller).

Prerequisites

A self-signed leaf certificate (including private-key data) must be created outside the switch.

Procedure

1. Create the leaf certificate context with the command crypto pki certificate which then switches

to the created leaf certificate context.

2.

Import the leaf certificate data into the switch with the command import(self-signed leaf
certificate).

3. Exit the leaf certificate context with the command exit.

4. Associate the leaf certificate with a switch feature (syslog client, RadSec client, captive-portal, HTTPS

server, or HSC) with the command crypto pki application.

Example

This example:

n Creates the leaf certificate context.

n Imports the self-signed leaf certificate.

n Associates the leaf certificate with the syslog client (application) on the switch.

switch(config)# switch(config)# crypto pki certificate SS_LC2
switch(config)# switch(config-cert-SS_LC)# import terminal self-signed
Paste the certificate in PEM format below, then hit enter and ctrl-D:
switch(config-cert-import)# -----BEGIN CERTIFICATE-----
switch(config-cert-import)# MIIFRDCCAyygAwIBAgIQP8nnS2Vp15u07xXMdktDJzANBgkqhkiG9
switch(config-cert-import)# MQswCQYDVQGEwJVUEOMAwGA1UECgwFXJ1YmxDAOgNBAMMB1Jvb3gw
switch(config-cert-import)# HhcNMTkNDEwMjIwNT1WhcjIwMTA0MjIwNE1WjBzQswQYDVQQGEwJV
...
switch(config-cert-import)# 1fIYZYGQyla0AwFuPTTxBXHYwRxTPbUYU5tumJrfwRPmE4OVY8S9D
switch(config-cert-import)# 1NGNm3NG03GqPScs/TF9bVyFA5BOrS5lmm7kNfRYlK8D/kMTfRreS
switch(config-cert-import)# YQ1u1NqShps=
switch(config-cert-import)# -----END CERTIFICATE-----
switch(config-cert-import)# -----BEGIN ENCRYPTED PRIVATE KEY-----
switch(config-cert-import)# MIIFDjBABgkqhkiG9wBBQ0wMzAbBgkqkiw0QwwDQImNpJMN7sVGwC
switch(config-cert-import)# MBQGCCqGSIb3DQMHAit+2qadNAASCMg5LYJ4AFm3EffhH5p51Ggr8
switch(config-cert-import)# IJ6L/UhEtH523nUkdV6gvoAWgoYaeD83PeswToAGv5VS8OMFTPttr
...
switch(config-cert-import)# OgSecqZsG6arbx0ESaYBir1c/6rPs1pcjbDxw283DiD1MWOpeoS2a
switch(config-cert-import)# iKnXnUMpVPfLc74ty2S41DtH0X9Sgf6aa1LjiStg+N7cND9XfGtj/
switch(config-cert-import)# cb4=

PKI | 175

| switch(config-cert-import)# |     |     | -----END |     | ENCRYPTED |     | PRIVATE KEY----- |
| --------------------------- | --- | --- | -------- | --- | --------- | --- | ---------------- |
switch(config-cert-import)#
| Enter import | password: | ******* |     |     |     |     |     |
| ------------ | --------- | ------- | --- | --- | --- | --- | --- |
Leaf certificate is validated as self-signed certificate and imported successfully.
| switch(config-cert-SS_LC2)# |     |     | exit |     |     |     |     |
| --------------------------- | --- | --- | ---- | --- | --- | --- | --- |
switch(config)# crypto pki application syslog-client certificate SS_LC2
| Installing | a certificate |     |     | of  | a root |     | CA  |
| ---------- | ------------- | --- | --- | --- | ------ | --- | --- |
Prerequisites
n AcertificateofarootCA(thatisusedasthesigner).
n RevocationcheckingURLsfortheCA(optional).
Procedure
1. CreateaTAprofilewiththecommandcrypto ta-profilewhichthenswitchestothecreatedTA
pki
profilecontext.
Step2isoptionalandsuggestedonlyforadvancedusers.
2. Optionallyenablecertificaterevocationcheckingwiththecommandrevocation-check ocsp.Most
certificatescontainrevocationcheckingURLsforOCSP.IfyouwanttooverridetheseURLs,configure
| customrevocationcheckingURLswiththecommandocsp |     |     |     |     |     |     | url. |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
3. ImportthecertificateoftherootCAwiththecommandta-certificate.
Example
Thisexampleinstallsthecertificateroot-certanddefinescustomrevocationcheckingURLs:
| switch(config)#              | crypto | pki | ta-profile       |     | root-cert |     |      |
| ---------------------------- | ------ | --- | ---------------- | --- | --------- | --- | ---- |
| switch(config-ta-root-cert)# |        |     | revocation-check |     |           |     | ocsp |
switch(config-ta-root-cert)# ocsp url primary http://ocsp-server.site.com
switch(config-ta-root-cert)# ocsp url secondary http://ocsp-server2.site.com
| switch(config-ta-root-cert)# |     |     | ta-certificate |     |     | import | terminal |
| ---------------------------- | --- | --- | -------------- | --- | --- | ------ | -------- |
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-ta-cert)# |     | -----BEGIN |     |     | CERTIFICATE----- |     |     |
| ----------------------- | --- | ---------- | --- | --- | ---------------- | --- | --- |
switch(config-ta-cert)# MIIDuTCCAqECCQCuoxeJ2ZNYcjANBgkqhkiG9w0BAQsFADCBqzELMAEBh
switch(config-ta-cert)# VVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEDAOBgNVBAcMB1JvY2tsDAKBg
switch(config-ta-cert)# BAoMA0hQTjEVMBMGA1UECwwMSFBOUm9zZXZpbGxlMSowKAYDVQocG5zdz
...
switch(config-ta-cert)# x3WFf3dFZ8o9sd5LVAHneH/ztb9MP34z+le1V346r12L2kpxmTOVJVyTO
switch(config-ta-cert)# BIzD/ST/HaWI+0S+S80rm93PSscEbb9GWk7vshh5EnW/moehBKcE4O1zy
switch(config-ta-cert)# 3LvMLZcssSe5J2Ca2XIhfDme8UaNZ7syGYMsAW0nG7yYHWkEOQu9s
| switch(config-ta-cert)# |     | -----END |     | CERTIFICATE----- |     |     |     |
| ----------------------- | --- | -------- | --- | ---------------- | --- | --- | --- |
switch(config-ta-cert)#
| The certificate | you          | are importing |     | has        | the | following | attributes: |
| --------------- | ------------ | ------------- | --- | ---------- | --- | --------- | ----------- |
| Issuer:         | C=US, ST=CA, | L=Rocklin,    |     | O=Company, |     | OU=Site,  |             |
CN=site.com/emailAddress=test.ca@site.com
| Subject: | C=US, ST=CA, | L=Rocklin, |     | O=Company, |     | OU=Site, |     |
| -------- | ------------ | ---------- | --- | ---------- | --- | -------- | --- |
CN=8400/emailAddress=test.ca@site.com
| Serial Number: | 12121221634631568498 |     |         |      | (0xaea51217d5945772) |     |              |
| -------------- | -------------------- | --- | ------- | ---- | -------------------- | --- | ------------ |
| TA certificate | import               | is  | allowed | only | once                 | for | a TA profile |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 176

| Do you want    | to  | accept this | certificate |     | (y/n)? | y   |     |     |
| -------------- | --- | ----------- | ----------- | --- | ------ | --- | --- | --- |
| TA certificate |     | accepted.   |             |     |        |     |     |     |
switch(config-ta-root-cert)#
| Installing | a   | CA-signed |     | leaf | certificate |     | (initiated | in the |
| ---------- | --- | --------- | --- | ---- | ----------- | --- | ---------- | ------ |
switch)
ThisproceduredescribeshowtocreateandinstallanX.509leafcertificatethatisinitiatedinsidetheswitch
butsignedoutsidetheswitchbyaCA.Andthenassociatethecertificatewithoneofthefollowingswitch
features:syslogclient,RadSecclient,HTTPSserver,orHSC(hardwareswitchcontroller).
Prerequisites
RootCAcertificateroot-certmustbeinstalledasdescribedinInstallingacertificateofarootCA.
Procedure
1. Createaleafcertificatecontextwiththecommandcrypto certificatewhichthenswitchesto
pki
thecreatedleafcertificateconfigurationcontext.
2. Defineleafcertificatepropertieswiththecommandsubject.
3. Settheencryptionkeytypefortheleafcertificatewiththecommandkey-type.
4. Generatethecertificatesigningrequest(CSR)withthecommandenroll terminal.
5. UsetheCSRtoobtainaleafcertificatefromtherootCA,usingtherootCAdirectlyasthesignerCA.
6. Importtheleafcertificateintotheswitchwiththecommandimport(CA-signed leaf certificate)
.
7. Exittheleafcertificatecontextwiththecommandexit.
8. Associatetheleafcertificatewithaswitchfeature(syslogclient,RadSecclient,HTTPSserver,orHSC)
| withthecommandcrypto |     |     | pki | application. |     |     |     |     |
| -------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
Example
Thisexample:
n Createstheleafcertificatecontext.
n Definestheleafcertificatecharacteristics.
GeneratestheleafcertificatesigningrequestintheswitchforgettingsignedoutsidetheswitchbyaCA.
n
ImportstheCA-signedleafcertificateintotheswitch.
n
n Associatestheleafcertificatewiththesyslogclient(application)ontheswitch.
| switch(config)# |     | crypto pki | certificate |     | lcert |     |     |     |
| --------------- | --- | ---------- | ----------- | --- | ----- | --- | --- | --- |
switch(config-cert-lcert)# subject common-name Leaf country US state CA
| locality                   | Rocklin   | org Company       |          | org-unit   | Site         |           |             |     |
| -------------------------- | --------- | ----------------- | -------- | ---------- | ------------ | --------- | ----------- | --- |
| switch(config-cert-lcert)# |           |                   | key-type |            | rsa key-size |           | 3072        |     |
| switch(config-cert-lcert)# |           |                   | enroll   | terminal   |              |           |             |     |
| You are                    | enrolling | a certificate     |          | with       | the          | following | attributes: |     |
| Subject:                   | C=US,     | ST=CA, L=Rocklin, |          | O=Company, |              | OU=Site   |             |     |
CN=Leaf
| Key Type: | RSA (2048) |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| Continue  | (y/n)?     | y   |     |     |     |     |     |     |
PKI|177

-----BEGIN CERTIFICATE REQUEST-----
MIIBozCCAQwCAQAwYzEVMBMGA1UEAxMMcG9kMDEtODQwMC0xMQ4wDAYDV
nViYTEMMAoGA1UEChMDSFBFMRIwEAYDVQQHEwlSb3NldmlsbGUxCzAJBg
NBMQswCQYDVQQGEwJVUzCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYE
...
GBAJ4L3lFFfWBEL+KAKpOGjZcVmwlBMqSKFtOFNF9nzmUmONmU3SKy6dz
7Au22mf3lWDxzrtCC/dj5RtWJeJekxp2LCIK/3eRXUwbYveQDKcxH7j9Z
ace+2tA68F2vlgRCQ/hcQH0YmNuaq4Ne3w0dhm7HlUrx
-----END CERTIFICATE REQUEST-----

switch(config-cert-lcert)# import terminal ta-profile root-cert
Paste the certificate in PEM format below, then hit enter and ctrl-D:
switch(config-cert-import)# -----BEGIN CERTIFICATE-----
switch(config-cert-import)# MIIFRDCCAyygwIBAgIQPnnS2Vp5u07XMdktDJzANBgkqhkiG9w0Bv
switch(config-cert-import)# MQswCQYDVQGEwJVEOMAwG1UECgwFJ1YmxDAOgNBMMB1Jvb3QgQ0Ew
switch(config-cert-import)# HhcNMTkNDEwMjIwNTWcjIwMTA0MjwNE1WBzQswQYDVQQGEwJVUzEL
...
switch(config-cert-import)# 1fIYZYGQyla0AwFuTTxBXYwRxPbUYU5tumrfwRPmE4OVY8S9DQgcr
switch(config-cert-import)# 1NGNm3NG03GqPcs/T9bVyF5BOrS5lmm7kNfRYl8D/kMTfRreSdxis
switch(config-cert-import)# YQ1u1NqShps=
switch(config-cert-import)# -----END CERTIFICATE-----
switch(config-cert-import)#
Leaf certificate is validated with root-cert and imported successfully.
switch(config-cert-lcert)# exit
switch(config)# crypto pki application syslog-client certificate lcert

Installing a CA-signed leaf certificate (created outside the
switch)
This procedure describes how to install an X.509 leaf certificate that was created and signed (by a CA)
outside the switch. And then associate the certificate with one of the following switch features: syslog client,
RadSec client, captive-portal, HTTPS server, or HSC (hardware switch controller).

Prerequisites

n Root CA certificate root-cert installed as described in Installing a certificate of a root CA.

n A CA-signed leaf certificate (including private-key data) created outside the switch.

Procedure

1. Create the leaf certificate context with the command crypto pki certificate which then switches

to the created leaf certificate context.

2.

Import the leaf certificate into the switch with the command import (CA-signed leaf
certificate).

3. Exit the leaf certificate context with the command exit.

4. Associate the leaf certificate with a switch feature (syslog client, RadSec client, captive-portal, HTTPS

server, or HSC) with the command crypto pki application.

Example

This example:

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

178

Createstheleafcertificatecontext.
n
importstheCA-signedleafcertificate.
n
Associatestheleafcertificatewiththesyslogclient(application)ontheswitch.
n
| switch(config)# |     |     | switch(config)# |     | crypto | pki certificate |     | CA_LC |
| --------------- | --- | --- | --------------- | --- | ------ | --------------- | --- | ----- |
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
| switch(config-cert-import)# |     |     |     | cb4=     |     |           |         |          |
| --------------------------- | --- | --- | --- | -------- | --- | --------- | ------- | -------- |
| switch(config-cert-import)# |     |     |     | -----END |     | ENCRYPTED | PRIVATE | KEY----- |
switch(config-cert-import)#
| Enter | import | password: | ******* |     |     |     |     |     |
| ----- | ------ | --------- | ------- | --- | --- | --- | --- | --- |
Leaf certificate is validated with root-cert and imported successfully.
| switch(config-cert-CA_LC)# |     |     |     | exit |     |     |     |     |
| -------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- |
switch(config)# crypto pki application syslog-client certificate CA_LC
PKI commands
| crypto | pki | application |     |     |     |     |     |     |
| ------ | --- | ----------- | --- | --- | --- | --- | --- | --- |
Syntax
| crypto    | pki application |             | <APP-NAME> |     | certificate | <CERT-NAME> |     |     |
| --------- | --------------- | ----------- | ---------- | --- | ----------- | ----------- | --- | --- |
| no crypto | pki             | application | <APP-NAME> |     | certificate |             |     |     |
Description
Associatesaleafcertificatewithafeature(application)ontheswitch.Bydefault,allfeaturesareassociated
withthedefault,self-signedcertificatelocal-cert.Thiscertificateiscreatedbytheswitchthefirsttimeit
starts.
Thenoformofthiscommandassociatesthespecifiedfeaturewiththedefaultcertificate.
Commandcontext
config
Parameters
<APP-NAME>
Specifiesthenameofafeatureontheswitch:
captive-portal:Captiveportal
n
PKI|179

n est-client: EST client

n hsc: Hardware switch controller.

n https-server: HTTPS server.

n radsec-client: RadSec client.

n syslog-client: Syslog client.

<CERT-NAME>

Specifies the name of an installed leaf certificate.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Associating the EST client with leaf certificate leaf-cert1:

switch(config)# crypto pki application est-client certificate leaf-cert1

Associating the syslog client with leaf certificate leaf-cert:

switch(config)# crypto pki application syslog-client certificate leaf-cert

syslog-client communicates with syslog server over TLS.

You can associate a certificate with the syslog-client application by enrolling the certificate manually or
through EST.

Setting the syslog client to use the default certificate:

switch(config)# no crypto pki application syslog-client certificate

Setting the RadSec client to use the default certificate:

switch(config)# no crypto pki application radsec-client certificate

Associating the RadSec client with leaf certificate leaf-cert:

switch(config)# crypto pki application radsec-client certificate leaf-cert

Associating the HTTPS server with leaf certificate leaf-cert2:

switch(config)# crypto pki application https-server certificate leaf-cert2

crypto pki certificate

Syntax

crypto pki certificate <CERT-NAME>

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

180

no crypto pki certificate <CERT-NAME>

Description

Creates a leaf certificate and changes to its context config-cert-<CERT-NAME>. If the specified leaf
certificate exists, this command changes to its context.

The first time the switch starts it creates a self-signed, default leaf certificate called local-cert. This
certificate is used by any switch application that does not have an associated leaf certificate.

The no form of this command deletes the specified leaf certificate. The default leaf certificate local-cert
cannot be deleted.

Command context

config

Parameters

<CERT-NAME>

Specifies the name of a leaf certificate. Range: 1 to 32 alphanumeric characters (excluding ").

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating leaf certificate leaf-cert:

switch(config)# crypto pki certificate leaf-cert
switch(config-cert-leaf-cert)#

Deleting leaf certificate leaf-cert:

switch(config)# no crypto pki certificate leaf-cert
The leaf certificate has associated applications. Deleting the certificate
will make the applications use the default certificate local-cert.
Continue (y/n)? y
switch(config)#

crypto pki ta-profile

Syntax

crypto pki ta-profile <TA-NAME>
no crypto pki ta-profile <TA-NAME>

Description

Creates a trust anchor (TA) profile and changes to the config-ta-<TA-NAME> context for the profile. Each TA
profile stores the certificate for a trusted CA. Up to 64 profiles can be defined.

If the specified TA profile exists, this command changes to the config-ta-<TA-NAME> context for the profile.

The no form of this command removes the specified TA profile.

When creating a new profile, If you exit the config-ta-<TA-NAME> context without importing the TA certificate,
the profile is discarded.

Command context

PKI | 181

config

Parameters

<TA-NAME>

Specifies the TA profile name. Range: 1 to 48 alphanumeric characters excluding ".

The TA profile name cannot end with est-ta<nn> where <nn> is 00 to 99. For example, company-trust-
anchor-est-ta01 is not allowed. This TA profile name suffix is reserved for TA profiles that are created for CA
certificates from EST servers.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating the TA profile root-cert:

switch(config)# crypto pki ta-profile root-cert
switch(config-ta-root-cert)#

Removing TA profile root-cert:

switch(config)# no crypto pki ta-profile root-cert

enroll self-signed

Syntax

enroll self-signed

Description

Generates a key pair and generates a self-signed certificate with it.

The subject fields and key type of the current leaf certificate must be defined before running this command.
If not, you are prompted to fill in the subject fields, and the key type is set to RSA 2048.

Command context

config-cert-<CERT-NAME>

Authority

Administrators or local user group members with execution rights for this command.

Example

Enrolling the leaf certificate leaf-cert:

switch(config-cert-leaf-cert)# enroll self-signed
You are enrolling a certificate with the following attributes:
Subject: C=US, ST=CA, L=Rocklin, OU=Site, O=Comp,

CN=Leaf01

Key Type: RSA (2048)

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

182

Continue (y/n)? y
Self-signed certificate is created and enrolled successfully.

switch(config-cert-leaf-cert)#

enroll terminal

Syntax

enroll terminal

Description

Generates a key pair and certificate signing request (CSR) for the current leaf certificate. Use the CSR to
obtain a signed certificate from a certificate authority (CA), and then import the certificate onto the switch
with the command import terminal.

The key type, and the certificate common name in the subject fields of the current leaf certificate must be
completed before running this command.

Command context

config-cert-<CERT-NAME>

Authority

Administrators or local user group members with execution rights for this command.

Example

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

import (CA-signed leaf certificate)

Syntax

import terminal ta-profile <TA-NAME> [password <PW>]
import <REMOTE-URL> ta-profile <TA-NAME> [password <PW>][vrf <VRF-NAME>]
import <STORAGE-URL> ta-profile <TA-NAME> [password <PW>]

Description

PKI | 183

Imports a CA-signed leaf certificate and then validates the certificate against the specified TA profile. If the
imported data includes a private key, the private key must match the leaf certificate being imported. If the
imported data does not include a private key, the certificate must match a CSR that was previously
generated with the command enroll terminal and must be signed by the CA whose root certificate is
installed in the specified TA profile. The TA profile must exist and have a TA certificate configured.

Parameters

terminal

Import the certificate by pasting PEM-format data at the console. Upon execution, the config-cert-
import context is entered for certificate pasting. To complete certificate data entry press Control-D in
your terminal program. Alternatively, the pasted certificate data can include at its end the delimiter END_
OF_CERTIFICATE (after the -----END CERTIFICATE----- line), making entry of Control-D unnecessary.

ta-profile <TA-NAME>

Specifies the TA profile name. Range: 1 to 48 alphanumeric characters excluding ".

<REMOTE-URL>

Specifies a certificate data file on a remote TFTP or SFTP server. The URL syntax is:

{tftp:// | sftp://<USER>@} {<IP>|<HOST>} [:<PORT>] [;blocksize=<SIZE>]/<FILE>

<STORAGE-URL>

Available on switch families that provide USB device file import capability, specifies a certificate data file
on a USB storage device inserted in the switch USB port. The URL syntax is:

usb:/<FILE>

password <PW>

Specifies the plaintext password used to decrypt the private key in the imported certificate data. When
this parameter is omitted, the password is prompted for as required. Range: 1 to 32 alphanumeric
characters.
vrf <VRF-NAME>

Specifies the name of the VRF to use for the remote URL file transfer. The default is mgmt.

Command context

config-cert-<CERT-NAME>

Authority

Administrators or local user group members with execution rights for this command.

Usage

n The imported data must include all the intermediate CA certificates in the certificate chain leading to the

certificate imported into the specified TA profile.

n This command cannot be used with the default certificate local-cert.

n The PEM data format is supported for all import sources. The PKCS#12 data format is supported for

<REMOTE-URL> and <STORAGE-URL>.

n The PEM data must be delimited with these lines for the certificate data:
-----BEGIN CERTIFICATE-----
-----END CERTIFICATE-----

And the PEM data must be delimited with either of these line pairs for the private key data:
-----BEGIN PRIVATE KEY-----
-----END PRIVATE KEY-----

-----BEGIN ENCRYPTED PRIVATE KEY-----
-----END ENCRYPTED PRIVATE KEY-----

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

184

Examples
Importingaleafcertificatefromtheconsole:
switch(config)#
|     |     |     | crypto | pki | certificate |     | leaf-cert |     |     |     |     |     |
| --- | --- | --- | ------ | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- |
switch(config-cert-leaf-cert1)# import terminal ta-profile root-cert
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-cert-import)# |     |     |     |     | -----BEGIN |     | CERTIFICATE----- |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | ---------- | --- | ---------------- | --- | --- | --- | --- | --- |
switch(config-cert-import)# MIIFRDCCAyygAwIBAgQP8nS2Vp15u0xXMdkDJzANBgkqhkiG9w0Bv
switch(config-cert-import)# MQswCQYDVQGEwJVUEOMAwGA1UCgwFXJ1YmDAgNBAMM1Jvb3QgQ0Ew
switch(config-cert-import)# HhcNMTkNDEwMjIwNT1WhcjIwMT0MjwNE1WjzQswQDVQQGEwJVUzEL
...
switch(config-cert-import)# 1fIYZYGQyla0AwFuPTTxBXHYwRxTPbUYU5umJfRPmE4VY8S9DQgcr
switch(config-cert-import)# 1NGNm3NG03GqPScs/TF9bVyFA5BOS5lmmkfRYK8D/kMTfRreSdxis
| switch(config-cert-import)# |     |     |     |     | YQ1u1NqShps= |     |                  |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | ------------ | --- | ---------------- | --- | --- | --- | --- | --- |
| switch(config-cert-import)# |     |     |     |     | -----END     |     | CERTIFICATE----- |     |     |     |     |     |
switch(config-cert-import)# -----BEGIN ENCRYPTED PRIVATE KEY-----
switch(config-cert-import)# MIIFDjBABgkqhkiG9wBBQ0wMzAbBgqkw0QwwDQIpJMN7sVGwCAggA
switch(config-cert-import)# MBQGCCqGSIb3DQMHAit+2qadNAASCgLYJ4Am3EfhH5p51Ggr86VqS
switch(config-cert-import)# IJ6L/UhEtH523nUkdV6gvAgoYaD83PswToAGv5VS8OMFTPttrn5/K
...
switch(config-cert-import)# OgSecqZsG6arbx0ESaYBir1c/6rPspcjbx283iD1MWOpeoS2aEmOX
switch(config-cert-import)# iKnXnUMpVPfLc74ty2S41DtH0X9gf6aa1jStg+7cND9XfGtjaV2+/
| switch(config-cert-import)# |     |     |     |     | cb4=     |     |           |     |         |          |     |     |
| --------------------------- | --- | --- | --- | --- | -------- | --- | --------- | --- | ------- | -------- | --- | --- |
| switch(config-cert-import)# |     |     |     |     | -----END |     | ENCRYPTED |     | PRIVATE | KEY----- |     |     |
switch(config-cert-import)#
| Enter | import | password: |     | ******* |     |     |     |     |     |     |     |     |
| ----- | ------ | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Leaf certificate is validated with root-cert and imported successfully.
switch(config-cert-leaf-cert)#
Importingaleafcertificatefromaremotefile:
| switch(config)# |     |     | crypto | pki | certificate |     | leaf-cert2 |     |     |     |     |     |
| --------------- | --- | --- | ------ | --- | ----------- | --- | ---------- | --- | --- | --- | --- | --- |
switch(config-cert-leaf-cert2)# import tftp://1.1.1.2/c2.p12 ta-profile root-cert
% Total % Received % Xferd Average Speed Time Time Time Current
|       |        |           |      |         |     | Dload  | Upload |     | Total    | Spent    | Left     | Speed |
| ----- | ------ | --------- | ---- | ------- | --- | ------ | ------ | --- | -------- | -------- | -------- | ----- |
| 100   | 3722   | 100       | 3722 | 0       |     | 0 391k |        | 0   | --:--:-- | --:--:-- | --:--:-- | 391k  |
| 100   | 3722   | 100       | 3722 | 0       |     | 0 376k |        | 0   | --:--:-- | --:--:-- | --:--:-- | 376k  |
| Enter | import | password: |      | ******* |     |        |        |     |          |          |          |       |
Leaf certificate is validated with root-cert and imported successfully.
switch(config-cert-leaf-cert2)#
| import | (self-signed |     |     | leaf | certificate) |     |     |     |     |     |     |     |
| ------ | ------------ | --- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Syntax
| import | terminal      | self-signed |             |     | [password | <PW>]     |           |     |             |     |     |     |
| ------ | ------------- | ----------- | ----------- | --- | --------- | --------- | --------- | --- | ----------- | --- | --- | --- |
| import | <REMOTE-URL>  |             | self-signed |     | [password |           | <PW>][vrf |     | <VRF-NAME>] |     |     |     |
| import | <STORAGE-URL> |             | self-signed |     |           | [password | <PW>]     |     |             |     |     |     |
Description
Importsaself-signedleafcertificateincludingitsmatchingprivatekey.
Parameters
terminal
ImportthecertificatebypastingPEM-formatdataattheconsole.Uponexecution,theconfig-cert-
importcontextisenteredforcertificatepasting.TocompletecertificatedataentrypressControl-Din
yourterminalprogram.Alternatively,thepastedcertificatedatacanincludeatitsendthedelimiterEND_
OF_CERTIFICATE(afterthe-----END CERTIFICATE-----line),makingentryofControl-Dunnecessary.
PKI|185

<REMOTE-URL>
SpecifiesacertificatedatafileonaremoteTFTPorSFTPserver.TheURLsyntaxis:
{tftp:// | sftp://<USER>@} {<IP>|<HOST>} [:<PORT>] [;blocksize=<SIZE>]/<FILE>
<STORAGE-URL>
AvailableonswitchfamiliesthatprovideUSBdevicefileimportcapability,specifiesacertificatedatafile
onaUSBstoragedeviceinsertedintheswitchUSBport.TheURLsyntaxis:
usb:/<FILE>
| password | <PW> |     |     |     |     |
| -------- | ---- | --- | --- | --- | --- |
Specifiestheplaintextpasswordusedtodecrypttheprivatekeyintheimportedcertificatedata.When
thisparameterisomitted,thepasswordispromptedforasrequired.Range:1to32alphanumeric
characters.
vrf <VRF-NAME>
SpecifiesthenameoftheVRFtousefortheremoteURLfiletransfer.Thedefaultismgmt.
Commandcontext
config-cert-<CERT-NAME>
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Thiscommandcannotbeusedwiththedefaultcertificatelocal-cert.
n
n ThePEMdataformatissupportedforallimportsources.ThePKCS#12dataformatissupportedfor
<REMOTE-URL>and<STORAGE-URL>.
ThePEMdatamustbedelimitedwiththeselinesforthecertificatedata:
n
| -----BEGIN | CERTIFICATE----- |     |     |     |     |
| ---------- | ---------------- | --- | --- | --- | --- |
| -----END   | CERTIFICATE----- |     |     |     |     |
AndthePEMdatamustbedelimitedwitheitheroftheselinepairsfortheprivatekeydata:
| -----BEGIN | PRIVATE          | KEY----- |          |     |     |
| ---------- | ---------------- | -------- | -------- | --- | --- |
| -----END   | PRIVATE KEY----- |          |          |     |     |
| -----BEGIN | ENCRYPTED        | PRIVATE  | KEY----- |     |     |
| -----END   | ENCRYPTED        | PRIVATE  | KEY----- |     |     |
Example
Importingaself-signedleafcertificatefromtheconsole:
| switch(config)#                   |     | crypto pki | certificate | ss-leaf-cert |             |
| --------------------------------- | --- | ---------- | ----------- | ------------ | ----------- |
| switch(config-cert-ss-leaf-cert)# |     |            | import      | terminal     | self-signed |
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-cert-import)# |     |     | -----BEGIN | CERTIFICATE----- |     |
| --------------------------- | --- | --- | ---------- | ---------------- | --- |
switch(config-cert-import)# MIID2TCCAsGgAwIBAgIJAKcrqokm6p9GMA0GCSqGSIb3DQEBCwUAM
switch(config-cert-import)# tDCCA5ygAwIBAgICEAEwDQYJKoZIhvcNAQELBQAwgYgxCzABAYTAl
switch(config-cert-import)# VQQGEwJVUzELMAkGA1UECAwCQ0ExDTALBgNVBAcMBFJvc2UxDDAKB
...
switch(config-cert-import)# +fWQLxhp+jKJGZGOZz/FENt2uSfZHzlXiu8n3g+EgqExenY1pBRJr
switch(config-cert-import)# VuEEoNb/YfkPXHHva4Zfx223q+f694wlVsHkENSzqr2goHpa2fOzq
switch(config-cert-import)# alewwdmVqCES+x8bvhf3C/6IB6ePkEsnMlHNTeM=
| switch(config-cert-import)# |     |     | -----END | CERTIFICATE----- |     |
| --------------------------- | --- | --- | -------- | ---------------- | --- |
switch(config-cert-import)# -----BEGIN ENCRYPTED PRIVATE KEY-----
switch(config-cert-import)# MIIFDjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBQwwDgQIt8Ni3
switch(config-cert-import)# MBQGCCqGSIb3DQMHBAiBHrejkcdpdASCBMjVxrrYYPNt3V1abr9k8
switch(config-cert-import)# 5GE0U99awh9ys4360WR95xOFGThvjkTyRWG511nGwVeLZs/7TPXWI
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 186

...
switch(config-cert-import)# hzc5ZT/w2F08icRI5mFbGoTAAw9IIWMOXGweaWQJDyKGrhg89GrnV
switch(config-cert-import)# M2UuP/tYuuO328QcenKZEJmZKCbx78oFRR+pgma4oeMaFTIyXE6Pr
switch(config-cert-import)# GAdCK8tkDiJ9DKbqdM5W0/nTJfqwUQlfl27dNrBAodsHdrw3UR99H
| switch(config-cert-import)# |     |     |     | SPo=     |     |           |     |         |          |     |     |
| --------------------------- | --- | --- | --- | -------- | --- | --------- | --- | ------- | -------- | --- | --- |
| switch(config-cert-import)# |     |     |     | -----END |     | ENCRYPTED |     | PRIVATE | KEY----- |     |     |
switch(config-cert-import)#
| Enter import |     | password: | ******* |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Leaf certificate is validated as self-signed certificate and imported successfully.
switch(config-cert-ss-leaf-cert)#
Importingaleafcertificatefromaremotefile:
| switch(config)# |     | crypto | pki | certificate |     | ss-leaf-cert2 |     |     |     |     |     |
| --------------- | --- | ------ | --- | ----------- | --- | ------------- | --- | --- | --- | --- | --- |
switch(config-cert-ss-leaf-cert2)# import tftp://1.1.1.2/ss2.p12 self-signed
% Total % Received % Xferd Average Speed Time Time Time Current
|              |     |           |         |     | Dload  | Upload |     | Total    | Spent    | Left     | Speed |
| ------------ | --- | --------- | ------- | --- | ------ | ------ | --- | -------- | -------- | -------- | ----- |
| 100 3230     | 100 | 3230      | 0       |     | 0 875k |        | 0   | --:--:-- | --:--:-- | --:--:-- | 875k  |
| 100 3230     | 100 | 3230      | 0       |     | 0 831k |        | 0   | --:--:-- | --:--:-- | --:--:-- | 831k  |
| Enter import |     | password: | ******* |     |        |        |     |          |          |          |       |
Leaf certificate is validated as self-signed certificate and imported successfully.
switch(config-cert-ss-leaf-cert2)#
key-type
Syntax
| key-type {rsa | [key-size |     | <K-SIZE>] |     | | ecdsa | [curve-size |     | <C-SIZE>]} |     |     |     |
| ------------- | --------- | --- | --------- | --- | ------- | ----------- | --- | ---------- | --- | --- | --- |
Description
Setsthekeytypeandkeysizeforthecurrentleafcertificate.Thekeytypeofthedefaultcertificatelocal-
certcannotbechanged.
Commandcontext
config-cert-<CERT-NAME>
Parameters
rsa
SpecifiesthekeytypeasRSA.
| key-size <K-SIZE> |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SpecifiestheRSAkeysizeinbits.Supportedvalues:2048,3072,4096.Default:2048
ecdsa
SpecifiesthekeytypeasECDSA.
| curve-size | <C-SIZE> |     |     |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SpecifiestheECDSAellipticcurvesizeinbits.Supportedvalues:256,348,521.Default:256
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingRSAencryptionontheleafcertificateleaf-cert:
PKI|187

| switch(config)# | crypto pki | certificate | leaf-cert |     |     |
| --------------- | ---------- | ----------- | --------- | --- | --- |
switch(config-cert-leaf-cert)#
|     |     | key-type | rsa | key-size 3072 |     |
| --- | --- | -------- | --- | ------------- | --- |
SettingECDSAencryptionontheleafcertificateleaf-cert:
| switch(config)#                | crypto pki | certificate | leaf-cert |            |     |
| ------------------------------ | ---------- | ----------- | --------- | ---------- | --- |
| switch(config-cert-leaf-cert)# |            | key-type    | ecdsa     | curve-size | 521 |
ocsp disable-nonce
Syntax
ocsp disable-nonce
no ocsp disable-nonce
Description
ConfiguresexclusionofthenoncefromOCSPrequests.AnonceisauniqueidentifierthatanOCSPclient
insertsinanOCSPrequestandexpectstheOCSPrespondertoincludeitinthecorrespondingOCSP
response.Thenoncemechanismhelpspreventreplayattacksinwhichamaliciousplayerattemptsto
masqueradeastheOCSPresponder.Althoughthenonceisincludedbydefault,itcanbeexcluded.Some
OCSPresponderschoosetonotsupporttheuseofthenonceduetoperformanceconsiderations.
Thenoformofthiscommandre-enablesnonceinclusioninOCSPrequests.
Commandcontext
config-ta-<TA-NAME>
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DisableinclusionofthenonceinOCSPrequestsforTAprofileroot-cert:
| switch(config)#              | crypto pki | ta-profile         | root-cert |     |     |
| ---------------------------- | ---------- | ------------------ | --------- | --- | --- |
| switch(config-ta-root-cert)# |            | ocsp disable-nonce |           |     |     |
EnableinclusionofthenonceinOCSPrequestsforTAprofileroot-cert:
| switch(config)#              | crypto pki | ta-profile | root-cert     |     |     |
| ---------------------------- | ---------- | ---------- | ------------- | --- | --- |
| switch(config-ta-root-cert)# |            | no ocsp    | disable-nonce |     |     |
ocsp enforcement-level
Syntax
| ocsp enforcement-level | {strict | | optional} |     |     |     |
| ---------------------- | ------- | ----------- | --- | --- | --- |
no enforcement-level
Description
SetseitherstrictorreducedenforcementoftheOCSPcheckofcertificates.Strictenforcementisenabledby
default.
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 188

The no form of this command resets enforcement to its default of strict.

Command context

config-ta-<TA-NAME>

Parameters

strict

Sets strict OCSP checking of certificates. The certificate is accepted only if all possible checking (including
validation failures, software system errors, configuration errors, transactional errors) is successful.

optional

Sets reduced OCSP checking of certificates. The certificate is accepted unless one or more of these
validation errors occur:

n Response signature invalid.

n Nonce in response mismatch.

n Certificate revoked, but only when revocation checking is possible. if revocation check is not possible,

the certificate is still accepted if there are no other validation errors.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting reduced OCSP checking of certificates:

switch(config)# crypto pki ta-profile root-cert
switch(config-ta-root-cert)# ocsp enforcement-level optional

Setting strict OCSP checking of certificates:

switch(config)# crypto pki ta-profile root-cert
switch(config-ta-root-cert)# ocsp enforcement-level strict

ocsp url

Syntax

ocsp url {primary | secondary} <URL>
no ocsp url {primary | secondary}

Description

Configures the OCSP responder URLs that the current TA profile uses to verify the revocation status of an
X.509 digital certificate. These URLs override the OCSP responder URL contained within the peer certificate
being verified (as well as URLs defined in any intermediate CAs in the chain of trust).

If no OCSP responder URLs are defined for a TA profile (default setting), then the OCSP responder URL in
the peer certificate is used for revocation status checking. (The OCSP responder URL is contained in a
certificate's Authority Information Access field, which is an X.509 v3 certificate extension.)

The no form of this command deletes the specified OCSP responder URL (primary or secondary) from the
current TA profile.

Command context

PKI | 189

config-ta-<TA-NAME>
Parameters
| {primary | | secondary} | <URL> |     |     |     |
| -------- | ------------ | ----- | --- | --- | --- |
SpecifytheHTTPURLoftheprimaryorsecondaryOCSPresponderusingeitherafullyqualifieddomain
nameorIPv4address.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DefiningtheprimaryOCSPURLfortheTAprofileroot-cert:
| switch(config)#              |     | crypto pki | ta-profile       | root-cert |      |
| ---------------------------- | --- | ---------- | ---------------- | --------- | ---- |
| switch(config-ta-root-cert)# |     |            | revocation-check |           | ocsp |
switch(config-ta-root-cert)# ocsp url primary http://ocsp-server.site.com
RemovingtheprimaryOCSPURLfromtheTAprofileroot-cert:
| switch(config)#              |     | crypto pki | ta-profile       | oot-cert    |      |
| ---------------------------- | --- | ---------- | ---------------- | ----------- | ---- |
| switch(config-ta-root-cert)# |     |            | revocation-check |             | ocsp |
| switch(config-ta-root-cert)# |     |            | no ocsp          | url primary |      |
ocsp vrf
Syntax
| ocsp vrf | <VRF-NAME> |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- |
| no ocsp  | vrf        |     |     |     |     |
Description
SetstheVRFthattheswitchusestocommunicatewithOCSPrespondersforOCSPchecking.VRFmgmtis
usedbydefault.
ThenoformofthiscommandresetstheVRFtoitsdefaultmgmt.
Commandcontext
config-ta-<TA-NAME>
Parameters
<VRF-NAME>
SpecifiesthenameoftheVRFtheswitchusestocommunicatewithOCSPresponders.Default:mgmt.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingtheOCSPresponderVRFtocorp1:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 190

| switch(config)# | crypto pki | ta-profile | root-cert |
| --------------- | ---------- | ---------- | --------- |
switch(config-ta-root-cert)#
|     |     | ocsp vrf | corp1 |
| --- | --- | -------- | ----- |
RevertingtheOCSPresponderVRFtoitsdefault:
| switch(config)#              | crypto pki | ta-profile | root-cert |
| ---------------------------- | ---------- | ---------- | --------- |
| switch(config-ta-root-cert)# |            | no ocsp    | vrf       |
| revocation-check             | ocsp       |            |           |
Syntax
| revocation-check | ocsp |     |     |
| ---------------- | ---- | --- | --- |
no revocation-check
Description
Enablescertificaterevocationcheckingforthecurrentprofileusingtheonlinecertificatestatusprotocol
(OCSP).
Thenoformofthiscommanddisablescertificaterevocationcheckingforthecurrentprofile.
Commandcontext
config-ta-<TA-NAME>
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingrevocationcheckingfortheTAprofileroot-cert:
| switch(config)#              | crypto pki | ta-profile       | root-cert |
| ---------------------------- | ---------- | ---------------- | --------- |
| switch(config-ta-root-cert)# |            | revocation-check | ocsp      |
DisablingrevocationcheckingfortheTAprofileroot-cert:
| switch(config)#              | crypto pki      | ta-profile          | root-cert |
| ---------------------------- | --------------- | ------------------- | --------- |
| switch(config-ta-root-cert)# |                 | no revocation-check |           |
| show crypto                  | pki application |                     |           |
Syntax
| show crypto pki | application |     |     |
| --------------- | ----------- | --- | --- |
Description
Showscertificateinformationforallfeatures(applications)usingleafcertificatesthataremanagedbyPKI.
Commandcontext
Manager(#)
Authority
PKI|191

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Showingcertificateinformationforallfeatures(applications)usingleafcertificates:
| switch#    | show         | crypto pki | application1 |     |      |      |        |     |     |
| ---------- | ------------ | ---------- | ------------ | --- | ---- | ---- | ------ | --- | --- |
| Associated | Applications |            | Certificate  |     | Name | Cert | Status |     |     |
------------------------ ---------------------- --------------------------------
| https-server  |     |                 |            |       |     | not      | configured, | using      | local-cert |
| ------------- | --- | --------------- | ---------- | ----- | --- | -------- | ----------- | ---------- | ---------- |
| syslog-client |     |                 | local-cert |       |     | valid    |             |            |            |
| hsc           |     |                 | xhsccert   |       |     | invalid, | using       | local-cert |            |
| radsec-client |     | device-identity |            | valid |     |          |             |            |            |
| show crypto   |     | pki certificate |            |       |     |          |             |            |            |
Syntax
| show crypto | pki | certificate | [<CERT-NAME> |     | [plaintext | |   | pem]] |     |     |
| ----------- | --- | ----------- | ------------ | --- | ---------- | --- | ----- | --- | --- |
Description
Showsalistofallconfiguredleafcertificates,ordetailedinformationforaspecificleafcertificate.
PossiblevaluesforCertStatusare:CSR pending,expired,expires soon,installed,malformed,not yet
known.
PossiblevaluesforESTStatusare:enroll failed, enroll pending,enroll retrying,enroll success,
n/a(certificateisnotEST-enrolled),reenroll failed,reenroll pending,reenroll retrying.
Commandcontext
Manager(#)
Parameters
<CERT-NAME>
Specifiestheleafcertificatename.Range:1to32alphanumericcharactersexcluding".
plaintext
Showscertificateinformationinplaintext.
pem
ShowscertificateinformationinPEMformat.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Showingalistofallconfiguredleafcertificates:
| switch# | show | crypto pki | certificate |     |     |     |     |     |     |
| ------- | ---- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
Certificate Name Cert Status EST Status Associated Applications
-------------------- -------------- ----------------- ------------------------------
| local-cert      |     |     | installed   |     | n/a             |     | radsec-client, |     | captive-portal |
| --------------- | --- | --- | ----------- | --- | --------------- | --- | -------------- | --- | -------------- |
| device-identity |     |     | installed   |     | n/a             |     | none           |     |                |
| pod01-99-1      |     |     | installed   |     | n/a             |     | https-server,  |     | est-client     |
| syslog-1        |     |     | CSR pending |     | enroll retrying |     | syslog-client  |     |                |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 192

leaf-cert1
leaf-cert2

installed
CSR pending

enroll success
enroll failed

none
none

Showing detailed information (in plaintext format) for leaf certificate pod01-99-1:

switch# show crypto pki certificate pod01-99-1 plaintext

Certificate Name: pod01-99-1
Associated Applications:

https-server, est-client
Certificate Status: installed
EST Status: n/a
Certificate Type: regular
Intermediates:

Subject: C = US, ST = CA, O = Company, OU = Lab-IT, CN = DeviceCA
Issuer: C = US, ST = CA, O = Company, OU = Lab-IT, CN = Lab-CA
Serial Number: 0x02

Subject: C = US, ST = CA, O = Company, OU = Lab-IT, CN = Lab-CA

Issuer: C = US, ST = CA, O = Company, OU = Lab-IT, CN = Lab-Root
Serial Number: 0x01

Certificate:

Data:

Version: 1 (0x0)
Serial Number: 14529416756121781768 (0xc9a2db8f3e3f4608)

Signature Algorithm: sha256WithRSAEncryption

Issuer: C=US, ST=CA, OU=Lab-IT, O=Company, CN=DeviceCA
Validity

Not Before: Jan 12 23:36:57 2018 GMT
Not After : Nov 1 23:36:57 2020 GMT

Subject: C=US, ST=CA, OU=Lab-IT, O=Company, CN=pod01-99-1
Subject Public Key Info:

Public Key Algorithm: rsaEncryption

Public-Key: (2048 bit)
Modulus:

00:a0:cd:ef:1b:f9:b8:bd:39:fc:7a:0e:00:17:ff:
2b:72:d8:4e:d4:df:49:36:ca:3a:f9:05:05:d7:e3:
d1:97:29:71:e6:33:b8:bb:8e:f0:ee:a6:e4:4a:f8:
...
fe:dd:d9:a0:af:59:47:25:b4:34:06:af:03:1d:33:
30:c3:85:fe:5c:e7:19:7f:ff:3a:b2:21:b8:e8:ed:
83:09

Exponent: 65537 (0x10001)

Signature Algorithm: sha256WithRSAEncryption

39:f6:03:86:03:d9:05:61:39:25:5f:0d:75:cc:05:ae:04:7e:
4c:a3:13:0b:f0:1e:af:68:0e:40:9f:ed:48:b6:5e:56:8c:53:
46:5b:c9:a4:e0:b0:bc:31:4b:a7:5d:0a:ed:7c:9c:f6:bf:1e:
...
39:f5:26:58:68:e2:13:ec:94:ac:60:8e:4b:b0:ba:45:cf:d6:
6a:4b:9f:7d:ae:3f:e5:2e:81:fe:ac:b3:65:44:35:47:a5:2f:
89:e7:58:a0

Showing detailed information (in PEM format) for leaf certificate leaf-cert1 with a status of CSR pending:

switch# show crypto pki certificate leaf-cert1 pem

Certificate Name: leaf-cert1

Associated Applications:

PKI | 193

syslog-client
|     | Certificate | Status:     | CSR pending  |     |     |     |
| --- | ----------- | ----------- | ------------ | --- | --- | --- |
|     | EST Status: | enroll      | retrying     |     |     |     |
|     | Certificate | Type:       | regular      |     |     |     |
|     | -----BEGIN  | CERTIFICATE | REQUEST----- |     |     |     |
MIICtTCCAZ0CAQAwcDEWMBQGA1UEAxMNc3lzbG9nLTg0MBYGA1UECxMPQ
XJ1YmEtUm9zZXZpbGxlMQ4wDAYDVQQKEYTESMBAGA1EBxMJUm9zZXZpbG
xlMQswCQYDVQQIEwJDQTELMAGA1UEBhMCVVMwggEiMSIb3DQEBAQUAA4I
...
cw2ytN6Idgh81k59x6DH7V/eORaKd5lq+oO7nkr6+QBf5L3f5Kb+TOFio
lei+EdCHMxxc07MK0n3dkziSW25HFUGsyEXVMK+BID3zbKDoUe6XVhvqI
mamXyghigLYDcbsn6WVw==
|      | -----END | CERTIFICATE    | REQUEST----- |     |     |     |
| ---- | -------- | -------------- | ------------ | --- | --- | --- |
| show | crypto   | pki ta-profile |              |     |     |     |
Syntax
| show | crypto pki | ta-profile | [<TA-NAME>] |     |     |     |
| ---- | ---------- | ---------- | ----------- | --- | --- | --- |
Description
ShowsalistofallconfiguredTAprofiles,ordetailedinformationforaspecificprofile.
Thiscommandshowsinformationforbothdirectly-configuredTAprofilesandTAprofilesthatweredynamically
downloadedfromESTservers.
Commandcontext
Manager(#)
Parameters
<TA-NAME>
SpecifiestheTAprofilename.Range:1to48alphanumericcharactersexcluding".
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShowingalistofallconfiguredTAprofiles:
| switch# | show | crypto | pki ta-profile |                |            |       |
| ------- | ---- | ------ | -------------- | -------------- | ---------- | ----- |
| Profile | Name |        |                | TA Certificate | Revocation | Check |
-------------------------------- ------------------ ----------------
| BASE_CA      |     |     |     | Installed,valid   | disabled |     |
| ------------ | --- | --- | --- | ----------------- | -------- | --- |
| BASE02_CA    |     |     |     | Installed,expired | disabled |     |
| root-cert    |     |     |     | Installed,valid   | OCSP     |     |
| ROOT-A_CA    |     |     |     | Not Installed     | OCSP     |     |
| EST-Service1 |     |     |     | Installed,valid   | None     |     |
| EST-Service2 |     |     |     | Installed,valid   | None     |     |
ShowingdetailedinformationforTAprofileroot-cert:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 194

| switch#    | show         | crypto        | pki       | ta-profile |                           | root-cert  |     |     |
| ---------- | ------------ | ------------- | --------- | ---------- | ------------------------- | ---------- | --- | --- |
| TA         | Profile      | Name          |           |            | : root-cert               |            |     |     |
| Revocation |              | Check         |           |            | : OCSP                    |            |     |     |
|            | OSCP         | Primary       | URL       |            | : http://ocsp1.domain.com |            |     |     |
|            | OCSP         | Secondary     | URL       |            | : Not                     | Configured |     |     |
|            | OCSP         | Disable-nonce |           |            | : false                   |            |     |     |
|            | OCSP         | Enforcement   |           | Level:     | strict                    |            |     |     |
|            | OCSP         | VRF           |           |            | : mgmt                    |            |     |     |
| TA         | Certificate: |               | Installed |            | and                       | valid      |     |     |
|            | Version:     | 3             | (0x2)     |            |                           |            |     |     |
|            | Serial       | Number:       |           |            |                           |            |     |     |
74:e6:6d:22:3f:52:cc:94:43:41:ab:66:a8:8d:47:b1
|     | Signature |                 | Algorithm: | sha1withRSAEncryption |                |     |             |       |
| --- | --------- | --------------- | ---------- | --------------------- | -------------- | --- | ----------- | ----- |
|     | Issuer:   | OU=DeviceTrust, |            |                       | OU=Operations, |     | O=Site,     | C=US, |
|     |           | CN=Site         | Trusted    |                       | Computing      |     | Root CA 1.0 |       |
Validity
|     | Not      | Before:         | Sep            | 14      | 03:12:06       | 2007 | GMT         |       |
| --- | -------- | --------------- | -------------- | ------- | -------------- | ---- | ----------- | ----- |
|     | Not      | After           | : Sep          | 14      | 03:21:14       | 2032 | GMT         |       |
|     | Subject: | OU=DeviceTrust, |                |         | OU=Operations, |      | O=Site,     | C=US, |
|     |          | CN=Site         |                | Trusted | Computing      |      | Root CA 1.0 |       |
|     | Subject  | Public          | Key            | Info:   |                |      |             |       |
|     | Public   |                 | Key Algorithm: |         | rsaEncryption  |      |             |       |
|     |          | RSA             | Public         | Key:    | (2048          | bit) |             |       |
|     |          | Modulus         | (2048          | bit):   |                |      |             |       |
30:0d:06:09:2a:86:48:86:f7:0d:01:01:01:05:33:
03:82:01:0f:00:30:82:01:3a:02:82:01:01:00:ac:
3d:60:3a:2e:ca:a4:34:db:5c:3b:6b:07:df:73:62:
...
20:c8:df:63:14:5a:e8:d3:ea:83:d8:47:a3:b5:2e:
bb:64:51:f0:be:13:b6:91:e4:32:45:58:5e:1f:0d:
02:03:01:00:01
|     |        | Exponent:   | 65537              |     | (0x10001)   |     |              |         |
| --- | ------ | ----------- | ------------------ | --- | ----------- | --- | ------------ | ------- |
|     | X509v3 | extensions: |                    |     |             |     |              |         |
|     | X509v3 |             | Key Usage:         |     |             |     |              |         |
|     |        | Digital     | Signature,         |     | Certificate |     | Signing, CRL | Signing |
|     | X509v3 |             | Basic Constraints: |     |             |     |              |         |
|     |        | CA:TRUE,    | pathlen:4          |     |             |     |              |         |
|     | X509v3 |             | Subject            | Key | Identifier: |     |              |         |
eb:d7:ec:db:8a:cb:f2:51:d5:06:e1:42:7b:39:a7:d0:1e:31:6e:bf
|     | Signature |     | Algorithm: | sha1withRSAEncryption |     |     |     |     |
| --- | --------- | --- | ---------- | --------------------- | --- | --- | --- | --- |
1c:90:f3:a4:f0:0d:e2:e3:e9:ae:01:e1:7d:a7:13:e2:cc:0b:
17:31:26:92:a2:5d:1d:19:60:54:03:13:9b:e1:73:6c:e4:b3:
01:4f:4e:ae:61:bd:ae:b6:12:d3:ab:08:ae:8c:47:92:d7:0d:
...
ca:cf:11:78:55:6d:06:49:fa:d4:8d:f3:ef:7f:79:38:35:5d:
16:5a:57:7f:a8:dc:b0:f8:a2:04:0d:17:0b:bb:58:32:30:e0:
2d:a8:37:a2
ta-certificate
Syntax
ta-certificate { [import [terminal]] | import {<REMOTE-URL> | <STORAGE-URL>} }
Description
ImportsaCAcertificateforuseinthecurrentTAprofile.ThecertificatemustbeinPEMformat.ThePEM
datamustbedelimitedwiththeselines:
-----BEGIN CERTIFICATE-----
-----END CERTIFICATE-----
PKI|195

OnlythefirstcertificateinthePEMdataisimported.Anyadditionalcertificatesareignored.
Commandcontext
config-ta-<TA-NAME>
Parameters
[import [terminal]]
Importthecertificatebypastingattheconsole(thedefault).Thisformofimportingisselectedwhether
ta-certificateisenteredwithoutparametersorifonlyimportisenteredorifimport terminalis
entered.Uponexecution,theconfig-ta-certcontextisenteredforcertificatepasting.Tocomplete
certificatedataentrypressControl-Dinyourterminalprogram.Alternatively,thepastedcertificatedata
canincludeatitsendthedelimiterEND_OF_CERTIFICATE(afterthe-----END CERTIFICATE-----line),
makingentryofControl-Dunnecessary..
import <REMOTE-URL>
ImportthecertificatefromafileonaremoteTFTPorSFTPserver.TheURLsyntaxis:
{tftp://|sftp://<USER>@}{<IP>|<HOST>}[:<PORT>][;blocksize=<SIZE>]/<FILE>
import <STORAGE-URL>
AvailableonswitchfamiliesthatprovideUSBdevicefileimportcapability,importthecertificatefroma
fileonaUSBstoragedeviceinsertedintheswitchUSBport.TheURLsyntaxis:
usb:/<FILE>
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ImportingacertificateintotheTAprofileroot-certbypastingPEM-formatcertificatedataattheconsole:
| switch(config)#              | crypto | pki | ta-profile     |     | root-cert |        |          |
| ---------------------------- | ------ | --- | -------------- | --- | --------- | ------ | -------- |
| switch(config-ta-root-cert)# |        |     | ta-certificate |     |           | import | terminal |
Paste the certificate in PEM format below, then hit enter and ctrl-D:
| switch(config-ta-cert)# |     |     | -----BEGIN |     | CERTIFICATE----- |     |     |
| ----------------------- | --- | --- | ---------- | --- | ---------------- | --- | --- |
switch(config-ta-cert)# MIIDuTCCAqECCQCuoxeJ2ZNYcjANBgkqhkiG9w0BAQsFADCBqzELMAEBh
switch(config-ta-cert)# VVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEDAOBgNVBAcMB1JvY2tsDAKBg
switch(config-ta-cert)# BAoMA0hQTjEVMBMGA1UECwwMSFBOUm9zZXZpbGxlMSowKAYDVQocG5zdz
...
switch(config-ta-cert)# x3WFf3dFZ8o9sd5LVAHneH/ztb9MP34z+le1V346r12L2kpxmTOVJVyTO
switch(config-ta-cert)# BIzD/ST/HaWI+0S+S80rm93PSscEbb9GWk7vshh5EnW/moehBKcE4O1zy
switch(config-ta-cert)# 3LvMLZcssSe5J2Ca2XIhfDme8UaNZ7syGYMsAW0nG7yYHWkEOQu9s
| switch(config-ta-cert)# |     |     | -----END | CERTIFICATE----- |     |     |     |
| ----------------------- | --- | --- | -------- | ---------------- | --- | --- | --- |
switch(config-ta-cert)#
| The certificate | you          | are        | importing | has        | the | following | attributes: |
| --------------- | ------------ | ---------- | --------- | ---------- | --- | --------- | ----------- |
| Issuer:         | C=US, ST=CA, | L=Rocklin, |           | O=Company, |     | OU=Site,  |             |
CN=site.com/emailAddress=test.ca@site.com
| Subject: | C=US, ST=CA, | L=Rocklin, |     | O=Company, |     | OU=Site, |     |
| -------- | ------------ | ---------- | --- | ---------- | --- | -------- | --- |
CN=9000/emailAddress=test.ca@site.com
| Serial Number: | 12121221634631568498 |      |             |      | (0xaea51217d5945772) |     |              |
| -------------- | -------------------- | ---- | ----------- | ---- | -------------------- | --- | ------------ |
| TA certificate | import               | is   | allowed     | only | once                 | for | a TA profile |
| Do you want    | to accept            | this | certificate |      | (y/n)?               |     | y            |
| TA certificate | accepted.            |      |             |      |                      |     |              |
switch(config-ta-root-cert)#
ImportingacertificateintotheTAprofileroot-cert2fromfilercert2-dataontheUSBdevice:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 196

| switch(config)# | crypto | pki | ta-profile |     | root-cert2 |     |
| --------------- | ------ | --- | ---------- | --- | ---------- | --- |
switch(config-ta-root-cert2)#
|                 |                |     | ta-certificate |     | import        | usb:/rcert2-data |
| --------------- | -------------- | --- | -------------- | --- | ------------- | ---------------- |
| The certificate | you            | are | importing      | has | the following | attributes:      |
| Issuer: C=US,   | ST=California, |     | L=Rocklin,     |     | O=Company,    | OU=Site,         |
CN=site.com/emailAddress=test.ca@site.com
| Subject: | C=US, ST=California, |     | L=Rocklin, |     | O=Company, | OU=Site, |
| -------- | -------------------- | --- | ---------- | --- | ---------- | -------- |
CN=9000/emailAddress=test.ca@site.com
| Serial Number: | 12121221634631568498 |      |             |      | (0xaea51217d5945772) |              |
| -------------- | -------------------- | ---- | ----------- | ---- | -------------------- | ------------ |
| TA certificate | import               | is   | allowed     | only | once for             | a TA profile |
| Do you want    | to accept            | this | certificate |      | (y/n)?               | y            |
| TA certificate | accepted.            |      |             |      |                      |              |
switch(config-ta-root-cert2)#
subject
Syntax
subject [common-name <COMMON-NAME>] [country <COUNTRY>] [locality <LOCALITY>]
| [org <ORG-NAME>] | [org-unit |     | <ORG-UNIT>] |     | [state <STATE>] |     |
| ---------------- | --------- | --- | ----------- | --- | --------------- | --- |
Description
Setsthesubjectfieldsforthecurrentleafcertificate.Ifthecommon-nameparameterisnotspecified,thenyou
arepromptedtodefineavalueforeachfield.Ifaconfiguredvalueexistsforanyfield,itispresentedasthe
default.
Thesubjectfieldsofthedefaultcertificatelocal-certcannotbechanged.
Commandcontext
config-cert-<CERT-NAME>
Parameters
| common-name | <COMMON-NAME> |     |     |     |     |     |
| ----------- | ------------- | --- | --- | --- | --- | --- |
Specifiesthecommonname.
country <COUNTRY>
Specifiestheregion.
| locality <LOCALITY> |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- |
Specifiesthelocality.
org <ORG-NAME>
Specifiestheorganization.
| org-unit <ORG-UNIT> |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- |
Specifiestheorganizationalunit.
state <STATE>
Specifiesthestate.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingsubjectfieldsfortheleafcertificateleaf-cert:
PKI|197

switch(config-cert-leaf-cert)# subject common-name Leaf01 country US
| locality | CA org Company | org-unit Site | state CA |
| -------- | -------------- | ------------- | -------- |
Settingsubjectfieldsfortheleafcertificateleaf-certinteractively:
| switch(config-cert-leaf-cert)# |     | subject |     |
| ------------------------------ | --- | ------- | --- |
Do you want to use the switch serial number as the common name (y/n)? n
| Enter Common   | Name : Leaf01  |     |     |
| -------------- | -------------- | --- | --- |
| Enter Org      | Unit : Site    |     |     |
| Enter Org      | Name : Company |     |     |
| Enter Locality | : Rocklin      |     |     |
| Enter State    | : CA           |     |     |
| Enter Country  | :              |     |     |
US
switch(config-cert-leaf-cert)#
| PKI EST | commands |     |     |
| ------- | -------- | --- | --- |
arbitrary-label
Syntax
| arbitrary-label | <LABEL> |     |     |
| --------------- | ------- | --- | --- |
no arbitrary-label
Description
WithintheESTprofilecontext,configuresthegenericoptionallabel(alsoknownasarbitrarylabel)tobe
concatenatedtotheESTserverURLthatisconfiguredwiththeurlcommand.Thereisnoarbitrarylabel
configuredbydefault.Anyexistingarbitrarylabelisreplacedbythiscommand.Theuseofarbitrarylabelsis
optional.
RFC7030allowstheuseofarbitrarylabelssothatoneESTservermayservemultipleCAswiththesame
serverURLthatgetsconcatenatedwithdifferentarbitrarylabels.Thesamelabelisusedforeveryrequest
madeunderaparticularESTprofile.
SomeESTschemesusearbitrarylabelsinamoresophisticatedway,definingdifferentlabelsfordifferent
typesofrequestsunderthesameESTprofile.Forexample,theCAcertificaterequestcouldusethegeneric
label(configuredwiththisarbitrary-labelcommand),thecertificateenrollmentrequestcouldusethe
enrollmentlabel(configuredwiththearbitrary-label-enrollmentcommand),andthere-enrollment
requestcouldusethere-enrollmentlabel(configuredwiththearbitrary-label-reenrollmentcommand).
NotethatonlyonelabelofeachofthethreeavailabletypescanbeconfiguredinanyESTprofile.
Thenoformofthiscommandremovesthegenericarbitrarylabel.
Commandcontext
config-est-<EST-NAME>
Parameters
<LABEL>
Specifiesthegenericarbitrarylabel.Range:Upto64characters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 198

Configuring the URL and generic arbitrary label. Note that with the URL and arbitrary label configured in this
example, the final URL the switch uses to request CA certificates from the EST server is https://est-
service999.com/.well-known/est/rsa2048/cacerts.

switch(config)# crypto pki est-profile EST-service1
switch(config)# url https://est-service999.com/.well-known/est
switch(config-est-EST-service1)# arbitrary-label rsa2048

Removing the generic arbitrary label:

switch(config)# crypto pki est-profile EST-service1
switch(config-est-EST-service1)# no arbitrary-label

arbitrary-label-enrollment

Syntax

arbitrary-label-enrollment <LABEL>
no arbitrary-label-enrollment

Description

Within the EST profile context, configures the arbitrary enrollment label to be concatenated to the EST
server URL that is configured with the url command. This label is specific to the enrollment operation.
There is no arbitrary enrollment label configured by default. Any existing arbitrary enrollment label is
replaced by this command. The use of arbitrary enrollment labels is optional.

When the enrollment label is not configured, the generic arbitrary label (created with the arbitrary-label
command) is used (if configured) for enrollment.

RFC 7030 allows the use of arbitrary labels so that one EST server may serve multiple CAs with the same
server URL that gets concatenated with different arbitrary labels. The same label is used for every request
made under a particular EST profile.

Some EST schemes use arbitrary labels in a more sophisticated way, defining different labels for different
types of requests under the same EST profile. For example, the CA certificate request could use the generic
label (configured with the arbitrary-label command) , the certificate enrollment request could use the
enrollment label (configured with this arbitrary-label-enrollment command), and the re-enrollment
request could use the re-enrollment label (configured with the arbitrary-label-reenrollment command).
Note that only one label of each of the three available types can be configured in any EST profile.

The no form of this command removes the arbitrary enrollment label.

Command context

config-est-<EST-NAME>

Parameters

<LABEL>

Specifies the arbitrary enrollment label. Range: Up to 64 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the arbitrary enrollment label:

PKI | 199

switch(config)# crypto pki est-profile EST-service1
switch(config-est-EST-service1)# arbitrary-label-enrollment ipsec-v7

Removing the arbitrary enrollment label :

switch(config)# crypto pki est-profile EST-service1
switch(config-est-EST-service1)# no arbitrary-label-enrollment

arbitrary-label-reenrollment

Syntax

arbitrary-label-reenrollment <LABEL>
no arbitrary-label-reenrollment

Description

Within the EST profile context, configures the arbitrary re-enrollment label to be concatenated to the EST
server URL that is configured with the url command. This label is specific to the re-enrollment operation.
There is no arbitrary re-enrollment label configured by default. Any existing arbitrary re-enrollment label is
replaced by this command. The use of arbitrary re-enrollment labels is optional.

When the re-enrollment label is not configured, the generic arbitrary label (created with the arbitrary-
label command) is used (if configured) for re-enrollment.

RFC 7030 allows the use of arbitrary labels so that one EST server may serve multiple CAs with the same
server URL that gets concatenated with different arbitrary labels. The same label is used for every request
made under a particular EST profile.

Some EST schemes use arbitrary labels in a more sophisticated way, defining different labels for different
types of requests under the same EST profile. For example, the CA certificate request could use the generic
label (configured with the arbitrary-label command) , the certificate enrollment request could use the
enrollment label (configured with the arbitrary-label-enrollment command), and the re-enrollment
request could use the re-enrollment label (configured with this arbitrary-label-reenrollment command).
Note that only one label of each of the three available types can be configured in any EST profile.

The no form of this command removes the arbitrary re-enrollment label.

Command context

config-est-<EST-NAME>

Parameters

<LABEL>

Specifies the arbitrary re-enrollment label. Range: Up to 64 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the arbitrary re-enrollment label:

switch(config)# crypto pki est-profile EST-service1
switch(config-est-EST-service1)# arbitrary-label-reenrollment ipsec-v7

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

200

Removingthearbitraryre-enrollmentlabel:
| switch(config)#                  |                 | crypto | pki est-profile | EST-service1                 |
| -------------------------------- | --------------- | ------ | --------------- | ---------------------------- |
| switch(config-est-EST-service1)# |                 |        | no              | arbitrary-label-reenrollment |
| crypto                           | pki est-profile |        |                 |                              |
Syntax
| crypto    | pki est-profile | <EST-NAME> |            |     |
| --------- | --------------- | ---------- | ---------- | --- |
| no crypto | pki est-profile |            | <EST-NAME> |     |
Description
CreatesacertificateEnrollmentoverSecureTransport(EST)profileandchangestotheconfig-est-<EST-
NAME>contextfortheprofile.EachESTprofilestoresinformationabouttheESTservice,includingESTserver
URLUpto16profilescanbecreated.
IfthespecifiedESTprofileexists,thiscommandchangestotheconfig-est-<EST-NAME>contextforthe
profile.
ThenoformofthiscommanddeletesthespecifiedESTprofile.ItalsodeletestheTAprofileswhoseCA
certificatesweredownloadedfromthecorrespondingESTserver,andtheleafcertificatesthatwereenrolled
usingthisESTprofile.
ThedeletionoftherelatedTAprofilesandenrolledcertificatesispermanent.IftheESTprofileisinthestartup
configurationandtheESTprofileisdeletedbutthisdeletionisnotupdatedinthestartupconfigurationbeforea
switchreboot,theESTprofilewillstillexistaftertherebootbuttherelatedTAprofilesandenrolledcertificates
willnotexist.
Commandcontext
config
Parameters
<EST-NAME>
SpecifiestheESTprofilename.Range:Upto32alphanumericcharacters(excluding").
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreatingESTprofileEST-Service1:
| switch(config)# |     | crypto | pki est-profile | EST-Service1 |
| --------------- | --- | ------ | --------------- | ------------ |
switch(config-est-service1)#
RemovingESTprofileservice1:
| switch(config)# |             | no crypto | pki est-profile | EST-Service1 |
| --------------- | ----------- | --------- | --------------- | ------------ |
| enroll          | est-profile |           |                 |              |
PKI|201

Syntax
| enroll est-profile | <EST-NAME> |     |     |     |     |
| ------------------ | ---------- | --- | --- | --- | --- |
Description
EnrollsaleafcertificatethrougharemoteEST(EnrollmentoverSecureTransport)server.
PerRFC7030,ESTenablesclientstorequestcertificatesigningservicesoversecureTLSconnections.The
switchgeneratesakeypairandthecorrespondingCSR.TheCSRissenttotheESTservertorequestsigning,
andthesignedcertificateisbereturnedtotheswitchwhereitisvalidated.Ifthewholeprocesssucceeds,
thecertificatecanbeusedasaleafcertificateontheswitch.Whentheleafcertificateapproachesitsexpiry
date,itwillberenewedautomaticallythroughthesameESTserver.
Eachenrollmentorre-enrollmentattemptstartswitha/cacertsrequestsenttotheESTservertogetthe
latestchainofCAcertificates.Aftertheenrollmentorre-enrollmentsucceeds,thischainofCAcertificates
willbecomparedwiththosedownloadedpreviouslyfromthesameESTserver.Updateswillbemadeas
appropriate.
Thesubjectfieldsofthecurrentleafcertificatemustbedefinedbeforerunningthiscommand.Ifthe
commonnamesubjectfieldisnotconfigured,thiscommandisrejected.
Thiscommandcannotbeusedtoenrollorrenewthedefaultcertificate"local-cert."
Commandcontext
config-cert-<CERT-NAME>
Parameters
<EST-NAME>
SpecifiesanexistingESTprofilename.Range:Upto32alphanumericcharacters(excluding").
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Enrollingleafcertificateleaf-cert1throughtheESTserveridentifiedinESTprofileEST-service1:
| switch(config-cert-leaf-cert1)# |              |              | enroll | est-profile         | EST-service1 |
| ------------------------------- | ------------ | ------------ | ------ | ------------------- | ------------ |
| You are enrolling               | a            | certificate  | with   | the following       | attributes:  |
| Subject:                        | C=US, ST=CA, | L=Roseville, |        | OU=Aruba-Roseville, | O=Aruba,     |
CN=leaf-cert1
| Key Type:   | RSA (2048  | bits)            |     |          |            |
| ----------- | ---------- | ---------------- | --- | -------- | ---------- |
| Continue    | (y/n)? y   |                  |     |          |            |
| Certificate | enrollment | via EST-service1 |     | has been | initiated. |
Please use `show crypto pki certificate leaf-cert1` to check its status.
switch(config-cert-leaf-cert1)#
reenrollment-lead-time
Syntax
| reenrollment-lead-time |     | <LEAD-TIME> |     |     |     |
| ---------------------- | --- | ----------- | --- | --- | --- |
no reenrollment-lead-time
Description
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 202

Within the EST profile context, sets the certificate re-enrollment lead time which is the number of days
before certificate expiry date that certificate re-enrollment will be initiated.

The no form of this command resets the EST server re-enrollment lead time to its default of 2 days.

Command context

config-est-<EST-NAME>

Parameters

<LEAD-TIME>

Specifies the certificate re-enrollment lead time in days. Range: 0 to 30 days. Default: 2 days.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the certificate re-enrollment lead time to 15 days:

switch(config)# crypto pki est-profile EST-service1
switch(config-est-EST-service1)# reenrollment-lead-time 15

Resetting the certificate re-enrollment lead time to its default of 2 days :

switch(config)# crypto pki est-profile EST-service1
switch(config-est-EST-service1)# no reenrollment-lead-time

retry-count

Syntax

retry-count <RETRIES>
no retry-count

Description

Within the EST profile context, sets the maximum number of retires to be attempted after the initial
certificate enrollment request fails.

The no form of this command resets the maximum number of certificate enrollment request retries to its
default of 3.

Command context

config-est-<EST-NAME>

Parameters

<RETRIES>

Specifies the maximum number of certificate enrollment request retries. Range: 0 to 32 retries. Default:
3 retries.

Authority

Administrators or local user group members with execution rights for this command.

Examples

PKI | 203

Settingtheretrycountto5retries:
| switch(config)#                  | crypto | pki est-profile | EST-service1 |     |
| -------------------------------- | ------ | --------------- | ------------ | --- |
| switch(config-est-EST-service1)# |        |                 | retry-count  | 5   |
Resettingtheretrycounttoitsdefaultof3retries:
| switch(config)#                  | crypto | pki est-profile | EST-service1   |     |
| -------------------------------- | ------ | --------------- | -------------- | --- |
| switch(config-est-EST-service1)# |        |                 | no retry-count |     |
retry-interval
Syntax
| retry-interval | <INTERVAL> |     |     |     |
| -------------- | ---------- | --- | --- | --- |
no retry-interval
Description
WithintheESTprofilecontext,setstheintervalatwhichafailedcertificateenrollmentrequestisretried.
Thenoformofthiscommandresetstheenrollmentrequestretryintervaltoitsdefaultof30seconds.
Commandcontext
config-est-<EST-NAME>
Parameters
<INTERVAL>
Specifiestheenrollmentrequestretryintervalinseconds.Range:30to600seconds.Default:30
seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingthecertificateenrollmentrequestretryintervalto45seconds:
| switch(config)#                  | crypto | pki est-profile | EST-service1   |     |
| -------------------------------- | ------ | --------------- | -------------- | --- |
| switch(config-est-EST-service1)# |        |                 | retry-interval | 45  |
Resettingtheretryintervaltoitsdefaultof30seconds:
| switch(config)#                  | crypto          | pki est-profile | EST-service1      |     |
| -------------------------------- | --------------- | --------------- | ----------------- | --- |
| switch(config-est-EST-service1)# |                 |                 | no retry-interval |     |
| show crypto                      | pki est-profile |                 |                   |     |
Syntax
| show crypto | pki est-profile | [<EST-NAME>] |     |     |
| ----------- | --------------- | ------------ | --- | --- |
Description
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 204

ShowsalistofallconfiguredESTprofiles,ordetailedinformationforaspecificprofile.
Commandcontext
Manager(#)
Parameters
<EST-NAME>
SpecifiestheESTprofilename.Range:Upto32alphanumericcharactersexcluding".
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShowingalistofallconfiguredESTprofiles:
| switch# show                     | crypto pki | est-profile |             |              |
| -------------------------------- | ---------- | ----------- | ----------- | ------------ |
|                                  |            |             | Downloaded  | Enrolled     |
| Profile Name                     |            |             | TA Profiles | Certificates |
| -------------------------------- |            |             | ----------- | ------------ |
| EST-service1                     |            |             | 2           | 3            |
| EST-service2                     |            |             | 1           | 2            |
| EST-service3                     |            |             | 2           | 0            |
ShowingdetailedinformationforESTprofileEST-service1:
| switch# show   | crypto pki         | est-profile                  | EST-service1     |     |
| -------------- | ------------------ | ---------------------------- | ---------------- | --- |
| Profile        | Name               | : EST-service1               |                  |     |
| Service        | VRF                | : mgmt                       |                  |     |
| Service        | URL                | : https://est-service999.com |                  |     |
| Arbitrary      | Label              |                              | : not configured |     |
| Arbitrary      | Label Enrollment   |                              | : /ipsec-VP7     |     |
| Arbitrary      | Label Reenrollment |                              | : not configured |     |
| Authentication | Username           | : est1                       |                  |     |
| Authentication | Password           | :                            |                  |     |
AQBapREALpWYm2z7L1LanOtR3vGkqhBN1hBUU2CuvQXUF/ggYgAAnAnGTnKq49P4c
dNQ6UqPbjHL4XzCO0T04djkhSUxPKGfnsWuFEONveh+JbEobqKImfwJjc3eWHiaUb
eNpPx2zN2Q1DdyxAAQi4rmKr8LITMTTMd7qr
| Retry Interval |              | : 45 | seconds |     |
| -------------- | ------------ | ---- | ------- | --- |
| Retry Count    |              | : 5  | times   |     |
| Reenrollment   | Lead Time    | : 2  | days    |     |
| Downloaded     | TA Profiles  | : 2  |         |     |
| Enrolled       | Certificates | :    |         |     |
leaf-cert1
leaf-cert2
leaf-cert3
url
Syntax
url <URL>
no url
Description
PKI|205

Within the EST profile context, configures the URL of the certificate enrollment EST server. This is not
configured by default. Any existing URL is replaced by this command.

The no form of this command removes the EST server URL within the selected EST profile. The removal of
the URL does not affect the TA profiles and enrolled certificates from the EST server.

Command context

config-est-<EST-NAME>

Parameters

<URL>

Specifies the EST server URL. Range: Up to 192 characters.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n The configuration and update of the EST profile URL triggers the sending of a /cacerts request to the

EST server. A successful request will result in a chain of trusted CA certificates being downloaded from the
EST server. Each CA certificate, either root CA certificates or intermediate CA certificates, will be saved as a
TA profile, with TA profile name <est-name>-est-taNN with NN representing two numerical digits. This TA
profile naming scheme with the -est-taNN suffix is reserved for TA profiles downloaded from EST
servers.

n Upon connection with an EST server, the switch authenticates the server by validating the server

certificate. For this validation to succeed, a TA profile needs to pre-exist in the switch with a CA certificate
from the issuer chain of the server certificate. Once the server is authenticated, all CA certificates in its
/cacerts response will be trusted, with no further validation occurring for them.

n The TA profiles with CA certificates downloaded from an EST server will have their revocation check set to

OCSP, enforcement set to optional, and the OCSP VRF set to the same as that of the EST profile.

Examples

Configuring the EST server URL :

switch(config)# crypto pki est-profile EST-service1
switch(config-est-EST-service1)# url https://est-service999.com/.well-known/est

Removing the EST server URL :

switch(config)# crypto pki est-profile EST-service1
switch(config-est-EST-service1)# no url

username

Syntax

username <USERNAME> password [ciphertext <CIPHERTEXT-PASSWORD> | plaintext <PLAINTEXT-
PASSWORD>]

no username

Description

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

206

Within the EST profile context, configures the user account information for the EST server that is used to
authenticate the switch before accepting requests from the switch. This is not configured by default. Any
existing username and password is replaced by this command.

When entered without either optional ciphertext or plaintext parameters, the plaintext password is
prompted for twice, with the characters entered masked with "*" symbols.

The no form of this command removes the user account information within the selected EST profile.

There are two ways the EST client on a CX switch can prove itself to an EST server: a certificate, and/or
username and password. At least one of the two must be configured for the EST request to succeed. If both
are configured, certificate authentication will be used. If a certificate is not configured or certificate
authentication fails, and username and password is configured, the username and password will be sent to
the EST server for authentication.

Command context

config-est-<EST-NAME>

Parameters

<USERNAME>

Specifies the EST server account user name. The exact user name requirements are set by the chosen EST
service. Range: Up to 32 alphanumeric characters.

ciphertext <CIPHERTEXT-PASSWORD>

Specifies the EST server account password as Base64 ciphertext. No password prompts are provided and
the ciphertext password is validated before the configuration is applied for the user.

The ciphertext password must be gotten from the EST service.

plaintext <PLAINTEXT-PASSWORD>

Specifies the password without prompting. The password is visible as cleartext when entered but is
encrypted thereafter. The exact password requirements are set by the chosen EST service. Range: Up to
64 alphanumeric characters.

Authority

Administrators or local user group members with execution rights for this command.

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

PKI | 207

| switch(config)# | crypto pki | est-profile | EST-service3 |
| --------------- | ---------- | ----------- | ------------ |
switch(config-est-EST-service3)#
|     |     | username | est1 password ciphertext |
| --- | --- | -------- | ------------------------ |
AQBpRALpWYm2z7L1LanOtR3vGkqhN1hBU2CuvQXUF/ggYgAAAHWaPqxU6nAnGTnKq49P4cdNQ6U
qPbjHL4XzO0T04djkUPKGfnsWuFEONveh+JbEobq63+1k80qBKImfwJjc3eWHiaUbeNpPx2zN2Q
1DdyxAAQi4rmKr8LITMTTMd7qr
RemovingtheESTuseraccountinformationforESTprofileEST-service2:
| switch(config)#                  | crypto pki | est-profile | EST-service2 |
| -------------------------------- | ---------- | ----------- | ------------ |
| switch(config-est-EST-service2)# |            | no          | username     |
vrf
Syntax
vrf <VRF-NAME>
no vrf
Description
WithintheESTprofilecontext,selectstheVRFthroughwhichtheESTservercanbereached.Anyexisting
VRFselectionisreplacedbythiscommand.Whenthiscommandisnotused,VRFmgmtisusedbydefaulton
switchfamiliessupportingthemgmtVRF,otherwisethedefaultVRFnameddefaultisused.
ThenoformofthiscommandselectsthedefaultVRFeithermgmtordefault.
Commandcontext
config-est-<EST-NAME>
Parameters
<VRF-NAME>
SpecifiesthenameoftheVRFtouseforESTservercommunication.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SelectingVRFit-servicesforESTservercommunications:
| switch(config)#                  | crypto pki | est-profile | EST-service1 |
| -------------------------------- | ---------- | ----------- | ------------ |
| switch(config-est-EST-service1)# |            | vrf         | it-services  |
ResettingtheVRFtoitsdefaultofmgmtforESTservercommunications:
| switch(config)#                  | crypto pki | est-profile | EST-service1 |
| -------------------------------- | ---------- | ----------- | ------------ |
| switch(config-est-EST-service1)# |            | no          | vrf          |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 208

Configuring enhanced security

Chapter 13

Configuring enhanced security

Several measures can be taken to enhance switch security, including setting secure mode to enhanced in the
Service OS. For maximum security, perform all the configuration described in this chapter.

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

complexity. To maintain enhanced security, configure the password complexity subcommand
settings no smaller than their defaults.

b. Configure passwords for all users, including admin. To make your password complexity settings
applicable to the default admin user, change the admin password after enabling password
complexity. The new admin password must respect your password complexity settings.

3. Ensure proper login management as follows:

a. Configure local user session management as described in CLI user session management

commands using cli-session and its subcommands max-per-user, timeout, and tracking-
range to achieve the wanted configuration. To maintain enhanced security, configure cli-
session subcommand settings no smaller than their defaults.

b. Restrict remote SSH connections to only use certified crypto algorithms using ssh certified-

algorithms-only.

c. Configure pre- and post-login banners using respectively, banner motd, and banner exec.

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

209

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

Enters the password-complexity context (shown in the switch prompt as config-pwd-cplx) for the purpose
of enabling and configuring password complexity. Password complexity enhances security by enforcing
specific password complexity requirements. Password complexity is disabled by default and must be
enabled by execution of the enable command.

The no form of this command reverts all settings to their default values and disables password complexity
enforcement.

To ensure that enhanced security is maintained, it is recommended that you do not set any values to less than

their defaults.

Password complexity apples only to local authentication. For remote authentication, you may choose to set up an

equivalent of password complexity according to whatever is supported on your particular TACACS+ or RADIUS

server.

Command context

config

Subcommands

These subcommands are available within the password complexity context (shown in the switch prompt as
config-pwd-cplx).
enable

Configuring enhanced security | 210

Enables password complexity enforcement. The enforcement only applies to passwords created after
this enabling. Existing passwords are not checked against password complexity.

disable

Disables password complexity enforcement.

[no] history-count <COUNT>

Specifies the number of previous passwords checked to prevent excessive reuse. Not applicable when
adding new users. The no form of this subcommand resets the value to its default. Default: 5. Range: 1
to 5.

[no] minimum-length <LENGTH>

Specifies the minimum password length. The no form of this subcommand resets the value to its default.
Default: 8. Range: 1 to 32.

[no] position-changes <POSITIONS>

Specifies the minimum number of characters that must change in the new password compared to the
previous password. Not applicable if no previous password exists, including when adding new users. The
no form of this subcommand resets the value to its default. Default: 8. Range: 1 to 32.

The number of password position changes is based on the number of simple character insertions,
deletions, or replacements. For example:

Old password: abCD4$ New password: abCD$    Position changes=1 ("4" deleted) Old password: abCD4$
New password: abCDEF4$ Position changes=2 ("EF" inserted) Old password: abCD4$ New password:
ebCD4$1 Position changes=2 ("a"replaced with "e," "1" added) Old password: abCD4$ New password:
abC$# Position changes=3 ("D4" deleted, "#" added)

[no] lowercase-count <COUNT>

Specifies the minimum lowercase character count for new passwords. The no form of this subcommand
resets the value to its default. Default: 1. Range: 0 to 32.

[no] uppercase-count <COUNT>

Specifies the minimum uppercase character count for new passwords. The no form of this subcommand
resets the value to its default. Default: 1. Range: 0 to 32.

[no] numeric-count <COUNT>

Specifies the minimum numeric digit count for new passwords. The no form of this subcommand resets
the value to its default. Default: 1. Range: 0 to 32.

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

existing ciphertext passwords will continue working until a password is changed. All new passwords must
be entered in plaintext form and be compliant with your password complexity configuration.

n The effective minimum password length may be larger than the configured minimum-length value. The

effective minimum password length is calculated as follows:

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

211

LARGEST-of:(minimum-length, position-changes,(SUM-of:lowercase-count+uppercase-
count+numeric-count+special-char-count))
Forexample,withminimum-length=8,andposition-changes=10(andthesumoftheotherfourcount
settings<=9),theeffective minimum-length is 10(becauseposition-changesislargest).Similarity,with
aminimum-length=12,position-changes=8,lowercase-count=8,uppercase-count=4,numeric-count=1,
special-char-count=1,theeffective minimum-length is 14(8+4+1+1=14)(becausesumoffthefour
countsislargest).
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
Configuringpasswordcomplexitysettingswithaneffectiveminimumlengthof14(becausethesumofthe
fourcountitemsis14):
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
Enablingpasswordcomplexity(withdefaultsettings)andchangingauser(admin1)passwordsuccessfully
butfailingtochangeanotheruser(admin2)passwordduetonotmeetingcomplexityrequirements:
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
Configuringenhancedsecurity|212

The new password does not meet one or more of the following complexity requirements:
| Minimum   | length          | : 8 |     |     |     |
| --------- | --------------- | --- | --- | --- | --- |
| Position  | changes         | : 8 |     |     |     |
| Numeric   | count           | : 1 |     |     |     |
| Lowercase | count           | : 1 |     |     |     |
| Uppercase | count           | : 1 |     |     |     |
| Special   | character count | : 1 |     |     |     |
switch(config)#
Withpasswordcomplexityalreadyenabled,attemptingtochangeanexistinguserpasswordbutfailing
becausethenewpasswordisidenticaltoarecentlyusedone(history-count).
| switch(config)# | user                      | admin1 password    |      |           |     |
| --------------- | ------------------------- | ------------------ | ---- | --------- | --- |
| Changing        | password for              | user admin1        |      |           |     |
| Enter old       | password:************     |                    |      |           |     |
| Enter new       | password:************     |                    |      |           |     |
| Confirm         | new password:************ |                    |      |           |     |
| User password   | not changed.              |                    |      |           |     |
| The new         | password is the           | same as a recently | used | password. |     |
switch(config)#
Withpasswordcomplexityalreadyenabled,creatinganewadminuser(admin3)withaplaintextpassword
thatmeetscomplexityrequirements.
| switch(config)#             | user                  | admin3 group administrators |     | password |     |
| --------------------------- | --------------------- | --------------------------- | --- | -------- | --- |
| Adding                      | user admin3           |                             |     |          |     |
| Enter password:************ |                       |                             |     |          |     |
| Confirm                     | password:************ |                             |     |          |     |
switch(config)#
Withpasswordcomplexityalreadyenabled,attemptingtocreateanewadminuser(admin4)witha
ciphertextpasswordbutfailingbecauseciphertextpasswordsarenotsupportedwithpasswordcomplexity
enabled.
switch(config)# user admin4 group administrators password ciphertext AQBapPd...==
Ciphertext passwords cannot be used when password complexity is enabled.
switch(config)#
| Configuring | remote | logging | using | SSH reverse | tunnel |
| ----------- | ------ | ------- | ----- | ----------- | ------ |
LoggingtoaremotesyslogservercanbemadecryptographicallysecurebyusingSSHreversetunnel.The
syslogdaemonontheswitchforwardslogmessagestotheSSHtunnel,andtheSSHtunnelendpointon
theremoteserverhostforwardsmessagestothelisteningsyslogserver.
Thisprocedureincludessampleconfigurationcommandsforauser-suppliedsyslogserverbasedonUbuntu
14.04.5LTSwithrsyslog.Itisuptotheusertochecktheirserverdocumentationandadjustthesample
commandsasrequired.Optionallyseeyourserverdocumentationforinformationonhowtousethesystemdand
autosshservicestoautomaticallyrestoretheSSHtunnelaftersystemreboot.
Prerequisites
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 213

Theuser-suppliedremotesyslogservermustbeonanetworkthatcanreachtheswitchmanagement
interface.
Procedure
1. ConfigureSSHserverontheswitch.
a. Enterthesecommands(althoughthisexampleusesthemgmtVRF,otherVRFscanbeused):
|     | switch(config)#         | interface | mgmt        |                  |     |
| --- | ----------------------- | --------- | ----------- | ---------------- | --- |
|     | switch(config-if-mgmt)# |           | no shutdown |                  |     |
|     | switch(config-if-mgmt)# |           | ip address  | <switch_mgmt_IP> |     |
switch(config-if-mgmt)#
exit
|     | switch(config)# | ssh | server vrf mgmt |     |     |
| --- | --------------- | --- | --------------- | --- | --- |
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
| CLI | user session | management |     |     | commands |
| --- | ------------ | ---------- | --- | --- | -------- |
cli-session
Syntax
cli-session
no cli-session
Description
EnterstheCLIsessioncontext(shownintheswitchpromptasconfig-cli-session)forthepurposeof
configuringCLIusersessionmanagement.SessionmanagementenhancessecuritybyenforcingspecificCLI
usersessionrequirements.Thefollowinginformationisprovidedattimeofsuccessfullogin:
n Whenapplicable,thenumberoffailedloginattemptssincethemostrecentsuccessfullogin.
Thedate,time,andlocation(consoleorIPaddressorhostname)ofthemostrecentprevioussuccessful
n
login.
n Thecountofsuccessfulloginswithinthepast(configurable)timeperiod.
Forexample:
| switch | login: admin |     |     |     |     |
| ------ | ------------ | --- | --- | --- | --- |
Password:
Configuringenhancedsecurity|214

There were 3 failed login attempts since the last successful login
Last login: 2019-04-20 08:51:33 from the console
User "admin" has logged in 73 times in the past 30 days

The no form of this command disables concurrent CLI user session restrictions and reverts timeout and
tracking-range to their default values.

To ensure that enhanced security is maintained, it is recommended that you keep CLI user session management
fully enabled by setting max-per-user to a nondefault value.

The cli-session command applies only to SSH/console login connection types. It does not apply to other
connection types such as REST.

Command context

config

Subcommands

These subcommands are available within the CLI session context.
[no] max-per-user <SESSIONS>

Specifies the maximum number of concurrent CLI sessions per user. The no form of this subcommand
disables concurrent CLI user session restrictions. Default: Disabled (no value). Range: 1 to 5.

When the same user name is configured for both local and remote authentication, both users, regardless of

privilege level, are considered to be the same user for the purpose of counting concurrent CLI sessions. For
example, with max-per-user set to 1 and user admin1 configured for local and remote authentication, only the
local user admin1 or the remote user admin1 can be logged in at any given moment. Both admin1 users cannot
be logged in simultaneously unless max-per-user is increased to at least 2.

[no] timeout <MINUTES>

Specifies the number of minutes a CLI session can be idle before the session is automatically terminated
and the user is logged out. A value of 0 minutes disables the session timeout. The no form of this
subcommand sets the timeout value to the default. Default 30: Range 0 to 4320.

This subcommand is the recommended replacement for the session-timeout command.

[no] tracking-range <DAYS>

Specifies the maximum number of days to track CLI user session logins. The no form of this
subcommand resets the value to its default. Default 30: Range 1 to 30.

exit

Exits the CLI session context.

end

Exits the CLI session context and then the config context.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring CLI user session settings for a maximum of one concurrent session, a 20-minute timeout, and
tracking for a maximum of 25 days.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

215

| switch(config)# | cli-session |     |     |     |
| --------------- | ----------- | --- | --- | --- |
switch(config-cli-session)#
|                             |     | max-per-user   | 1   |     |
| --------------------------- | --- | -------------- | --- | --- |
| switch(config-cli-session)# |     | timeout        | 20  |     |
| switch(config-cli-session)# |     | tracking-range | 25  |     |
| switch# exit                |     |                |     |     |
Aftersuccessfulearlierlogins,logginginfromtheconsolewithoutanyinterveningunsuccessfullogins.
| switch login: | admin1 |     |     |     |
| ------------- | ------ | --- | --- | --- |
Password:
| Last login:   | 2019-04-15 | 14:10:21 from | the console |         |
| ------------- | ---------- | ------------- | ----------- | ------- |
| User 'admin1' | has logged | in 65 times   | in the past | 25 days |
Attemptingtologinasadmin1whenalreadyloggedinasadmin1fromelsewhere.
| switch login: | admin1 |     |     |     |
| ------------- | ------ | --- | --- | --- |
Password:
| Too many | logins for | 'admin1' |     |     |
| -------- | ---------- | -------- | --- | --- |
Aftersuccessfulearlierlogins,attemptingtologintwicewithaninvalidpassword,followedbyasuccessful
login.
| switch login: | admin1 |     |     |     |
| ------------- | ------ | --- | --- | --- |
Password:
Login incorrect
| switch login: | admin1 |     |     |     |
| ------------- | ------ | --- | --- | --- |
Password:
Login incorrect
| switch login: | admin1 |     |     |     |
| ------------- | ------ | --- | --- | --- |
Password:
There were 2 failed login attempts since the last successful login
| Last login:   | 2019-04-15 | 17:22:45 from | 192.168.1.1 |         |
| ------------- | ---------- | ------------- | ----------- | ------- |
| User 'admin1' | has logged | in 72 times   | in the past | 25 days |
Configuringenhancedsecurity|216

Chapter 14

Captive portal (RADIUS)

Captive portal (RADIUS)

About captive portal (RADIUS)
Captive portal provides clients with Internet access based on http or https redirection. The client first gets
authenticated using MAC or 802.1x authentication which results in application of the captive portal profile.
The http or https request is then redirected to the captive portal server for user registration. Finally, with
Change of Authorization (CoA) with the Port Bounce VSA or Disconnect Message from the RADIUS server,
MAC, or 802.1X authentication occurs, providing the authenticated client with Internet access.

Captive portal is supported only for the clients getting authenticated through RADIUS servers.

For captive portal http or https redirection to occur, both of these requirements must be met:

n The client must be successfully authenticated with either MAC or 802.1x based authentication.

n The client must be assigned a role that includes a configured captive portal profile.

Captive portal is client-based. The redirect parameters (configured per client) can be configured using one of
these three methods:

n LUR (Local User Role): The captive portal and user role are configured on the switch. The role is sent
from the RADIUS server in the authentication response packet (with the Radius-accept) to the switch as
the authorization attribute VSA Aruba-User-Role. The role is then applied to the authenticated user. The
role returned from the RADIUS server must have earlier been configured on the switch with a matching
captive portal profile name. If the role (returned from the RADIUS server) is not present in the switch, the
authentication fails unless the client's credentials are present in the RADIUS server in which case a
RADIUS role will be created and then applied after authentication. In this situation, the client will be a
normal port access client and not a captive portal client. For captive portal to work it is mandatory to
have a role with a captive portal URL and to have captive portal policies associated.

n DUR (Downloadable User Role): After successful SSL connection is established (using certificates)

between the RADIUS server and switch, the captive portal and user role configurations are downloaded
to the switch, creating the role internally on the switch which is then applied to the authenticated user.
This method requires RADIUS server credentials configured on the switch and a RADIUS server root
certificate installed on the switch.

n RADIUS VSA (Vendor-Specific Attribute): The URL and policy rules are sent from the RADIUS server
(with the Radius-accept) to the switch as authorization attribute VSAs Aruba-Captive-Portal-URL and
Aruba-NAS-Filter-Rule. The role is created internally on the switch and then applied to the
authenticated user.

See also the captive portal information found under:

n Port access policy

n Port access role

n Supported RADIUS attributes

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

217

TheRADIUSserverandcaptiveportalservercanbeaClearPassserveractingasaRADIUSserveroranyother
RADIUSserver.ForClearPass,ClearPassPolicyManager(includingCaptivePortal),andrelateddocumentation,
seehttps://asp.arubanetworks.com/downloads,filteringfor"ArubaClearPass."
| IPv4 Captive | portal | example |     |     | configuration |     |     |
| ------------ | ------ | ------- | --- | --- | ------------- | --- | --- |
AbasicLUR(LocalUserRole)IPv4captiveportalconfiguration,includingpolicy,captiveportal,anduserrole
canbeconfiguredasfollows:
Policy configuration
Theorderoftheclassesinthepolicyisimportantforsuccessfulredirection.
| switch(config)# | class | ip clearpass |     |     |     |     |     |
| --------------- | ----- | ------------ | --- | --- | --- | --- | --- |
switch(config-class-ip)#
|                          |     | 10   | match tcp | any | 10.101.0.199 |     | eq 80  |
| ------------------------ | --- | ---- | --------- | --- | ------------ | --- | ------ |
| switch(config-class-ip)# |     | 20   | match tcp | any | 10.101.0.199 |     | eq 443 |
| switch(config-class-ip)# |     | exit |           |     |              |     |        |
switch(config)#
| switch(config)#          | class | ip dhcp |           |     |     |       |     |
| ------------------------ | ----- | ------- | --------- | --- | --- | ----- | --- |
| switch(config-class-ip)# |       | 10      | match udp | any | any | eq 67 |     |
| switch(config-class-ip)# |       | 20      | match udp | any | any | eq 53 |     |
| switch(config-class-ip)# |       | exit    |           |     |     |       |     |
switch(config)#
| switch(config)# | class | ip http |     |     |     |     |     |
| --------------- | ----- | ------- | --- | --- | --- | --- | --- |
switch(config-class-ip)#
|                          |     | 10   | match tcp | any | any | eq 80  |     |
| ------------------------ | --- | ---- | --------- | --- | --- | ------ | --- |
| switch(config-class-ip)# |     | 20   | match tcp | any | any | eq 443 |     |
| switch(config-class-ip)# |     | exit |           |     |     |        |     |
switch(config)#
| switch(config)#           | port-access |     | policy | cp_policy    |     |     |     |
| ------------------------- | ----------- | --- | ------ | ------------ | --- | --- | --- |
| switch(config-pa-policy)# |             | 10  | class  | ip dhcp      |     |     |     |
| switch(config-pa-policy)# |             | 20  | class  | ip clearpass |     |     |     |
switch(config-pa-policy)# 30 class ip http action redirect captive-portal
| switch(config-pa-policy)# |     | exit |     |     |     |     |     |
| ------------------------- | --- | ---- | --- | --- | --- | --- | --- |
switch(config)#
| Captive portal | configuration |     |     |     |     |     |     |
| -------------- | ------------- | --- | --- | --- | --- | --- | --- |
switch(config)# aaa authentication port-access captive-portal-profile cp_user
switch(config-captive-portal)# url http://10.101.0.199/guest/cp.php
| switch(config-captive-portal)# |     |     | url-hash-key |     | plaintext |     | cGxwe#123 |
| ------------------------------ | --- | --- | ------------ | --- | --------- | --- | --------- |
| switch(config-captive-portal)# |     |     | exit         |     |           |     |           |
switch(config)#
| User role configuration |             |           |                        |     |           |     |         |
| ----------------------- | ----------- | --------- | ---------------------- | --- | --------- | --- | ------- |
| switch(config)#         | port-access |           | role guest_role        |     |           |     |         |
| switch(config-pa-role)# |             | associate | captive-portal-profile |     |           |     | cp_user |
| switch(config-pa-role)# |             | associate | policy                 |     | cp_policy |     |         |
| switch(config-pa-role)# |             | exit      |                        |     |           |     |         |
switch(config)#
Captiveportal(RADIUS)|218

| IPv6 Captive |     | portal | example |     | configuration |     |     |
| ------------ | --- | ------ | ------- | --- | ------------- | --- | --- |
AbasicLUR(LocalUserRole)IPv6captiveportalconfigurationcanbeconfiguredasfollows:
Theorderoftheclassesinthepolicyisimportantforsuccessfulredirection.
| switch(config)#            |     | class | ipv6 HTTP |     |             |        |     |
| -------------------------- | --- | ----- | --------- | --- | ----------- | ------ | --- |
| switch(config-class-ipv6)# |     |       | 10 match  | tcp | any 2000::3 | eq 80  |     |
| switch(config-class-ipv6)# |     |       | 20 match  | tcp | any 2000::3 | eq 443 |     |
| switch(config-class-ipv6)# |     |       | exit      |     |             |        |     |
switch(config)#
### Class ICMP provides L2 address resolution for the IPv6 next hop address ###
| switch(config)#            |     | class | ipv6 ICMP |        |         |           |     |
| -------------------------- | --- | ----- | --------- | ------ | ------- | --------- | --- |
| switch(config-class-ipv6)  |     |       | 10 match  | icmpv6 | any any | icmp-type | 135 |
| switch(config-class-ipv6)  |     |       | 20 match  | icmpv6 | any any | icmp-type | 136 |
| switch(config-class-ipv6)# |     |       | exit      |        |         |           |     |
switch(config)#
| switch(config)#            |     | class | ipv6 TCP |     |         |        |     |
| -------------------------- | --- | ----- | -------- | --- | ------- | ------ | --- |
| switch(config-class-ipv6)# |     |       | 10 match | tcp | any any | eq 80  |     |
| switch(config-class-ipv6)# |     |       | 20 match | tcp | any any | eq 443 |     |
| switch(config-class-ipv6)# |     |       | exit     |     |         |        |     |
switch(config)#
| switch(config)#class       |     |             | ipv6 UDP |      |         |        |     |
| -------------------------- | --- | ----------- | -------- | ---- | ------- | ------ | --- |
| switch(config-class-ipv6)# |     |             | 10 match | udp  | any any | eq 547 |     |
| switch(config-class-ipv6)# |     |             | 20 match | udp  | any any | eq 53  |     |
| switch(config)#            |     | port-access | policy   | CP6  |         |        |     |
| switch(config-pa-policy)#  |     |             | 10 class | ipv6 | ICMP    |        |     |
| switch(config-pa-policy)#  |     |             | 20 class | ipv6 | UDP     |        |     |
| switch(config-pa-policy)#  |     |             | 30 class | ipv6 | HTTP    |        |     |
switch(config-pa-policy)# 40 class ipv6 TCP action redirect captive-portal
| switch(config-pa-policy)# |     |     | exit |     |     |     |     |
| ------------------------- | --- | --- | ---- | --- | --- | --- | --- |
switch(config)#
switch(config)# aaa authentication port-access captive-portal-profile CP6
switch(config-captive-portal)# url https://[2000::3]/guest/captive_portal.php
| switch(config-captive-portal)# |     |     |     | exit |     |     |     |
| ------------------------------ | --- | --- | --- | ---- | --- | --- | --- |
switch(config)#
| Captive            | portal |     | (RADIUS)    | commands |                        |     |     |
| ------------------ | ------ | --- | ----------- | -------- | ---------------------- | --- | --- |
| aaa authentication |        |     | port-access |          | captive-portal-profile |     |     |
Syntax
aaa authentication port-access captive-portal-profile <PROFILE-NAME>
no aaa authentication port-access captive-portal-profile <PROFILE-NAME>
Description
Createsthespecifiedcaptiveportalprofile(ifitdoesnotyetexist)andthenentersitscontext.Forexisting
captiveportalprofiles,thiscommandentersthecontextofthespecifiedcaptiveportalprofile.
Thenoformofthiscommanddeletesthespecifiedcaptiveportalprofile.
Commandcontext
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 219

config

Parameters

<PROFILE-NAME>

Specifies the captive portal profile name. Up to 64 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating a captive portal profile named employee and entering its context for additional configuration:

switch(config)# aaa authentication port-access captive-portal-profile employee
switch(config-captive-portal)# url http://1.1.1.1/employee/captiveportal.php
switch(config-captive-portal)#
switch(config-captive-portal)# url-hash-key plaintext cjQrJ9#$erty
switch(config-captive-portal)#
switch(config-captive-portal)# exit
switch(config)#

Deleting the captive portal profile named employee:

switch(config)# no aaa authentication port-access captive-portal-profile employee
switch(config)#

show port-access captive-portal-profile

Syntax

show port-access captive-portal-profile [name <PROFILE-NAME>]

Description

Shows the configuration information for all captive portal profiles or a particular captive portal profile.

Command context

Operator (>) or Manager (#)

Parameters

<PROFILE-NAME>

Specifies a captive portal profile name for which information will be shown.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Showing IPv4 local captive portal profile configuration information:

switch# show port-access captive-portal-profile name employee

Captive portal (RADIUS) | 220

| Captive Portal | Profile | Configuration                                  |     |
| -------------- | ------- | ---------------------------------------------- | --- |
| Name           |         | : employee                                     |     |
| Type           |         | : local                                        |     |
| URL            |         | : http://1.1.1.1/employee/captiveportal.php    |     |
| URL Hash       | Key     | : SWNGWyMeYubHPDgVIirpEUwNK5Uf+r1vmhBIncQPw1Y= |     |
ShowingIPv6localcaptiveportalprofileconfigurationinformation:
| switch# show   | port-access | captive-portal-profile                         | name CP6 |
| -------------- | ----------- | ---------------------------------------------- | -------- |
| Captive Portal | Profile     | Configuration                                  |          |
| Name           |             | : CP6                                          |          |
| Type           |             | : local                                        |          |
| URL            |             | : https://[2000::3]/guest/captive_portal.php   |          |
| URL Hash       | Key         | : SWNGWyMeYubHPDgVIirpEUwNK5Uf+r1vmhBIncQPw1Y= |          |
ShowingIPv6DURcaptiveportalprofileconfigurationinformation:
switch# show port-access captive-portal-profile name CP6_DUR_GUEST_ROLE
| Captive Portal | Profile | Configuration                                     |     |
| -------------- | ------- | ------------------------------------------------- | --- |
| Name           |         | : CP6_DUR_GUEST_ROLE                              |     |
| Type           |         | : downloaded                                      |     |
| URL            |         | : https://[2030:1::40]/guest/captive_portal_2.php |     |
ShowingIPv6RADIUSVSAcaptiveportalprofileconfigurationinformation:
switch# show port-access captive-portal-profile name RADIUS_2259748436
| Captive Portal | Profile | Configuration                                     |     |
| -------------- | ------- | ------------------------------------------------- | --- |
| Name           |         | : RADIUS_2259748436                               |     |
| Type           |         | : radius                                          |     |
| URL            |         | : https://[2030:1::40]/guest/captive_portal_2.php |     |
Showingallcaptiveportalprofileconfigurationinformation:
| switch# show   | port-access | captive-portal-profile                            |     |
| -------------- | ----------- | ------------------------------------------------- | --- |
| Captive Portal | Profile     | Configuration                                     |     |
| Name           |             | : CP6                                             |     |
| Type           |             | : local                                           |     |
| URL            |             | : https://[2000::3]/guest/captive_portal.php      |     |
| URL Hash       | Key         | : SWNGWyMeYubHPDgVIirpEUwNK5Uf+r1vmhBIncQPw1Y=    |     |
| Name           |             | : CP6_DUR_GUEST_ROLE                              |     |
| Type           |             | : downloaded                                      |     |
| URL            |             | : https://[2030:1::40]/guest/captive_portal_2.php |     |
| Name           |             | : RADIUS_2259748436                               |     |
| Type           |             | : radius                                          |     |
| URL            |             | : https://[2030:1::40]/guest/captive_portal_2.php |     |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 221

url

Syntax

url <URL>
no url

Description

Within the captive portal context, defines the captive portal URL.

The no form of this command deletes the captive portal URL.

Command context

config-captive-portal

Parameters

<URL>

Specifies the captive portal URL as an IPv4 or IPv6 address or a fully-qualified domain name. Up to 1024
characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating a captive portal profile named employee and then setting its IPv4 redirect URL:

switch(config)# aaa authentication port-access captive-portal-profile employee
switch(config-captive-portal)# url http://1.1.1.1/employee/captiveportal.php
switch(config-captive-portal)#
switch(config-captive-portal)# exit
switch(config)#

Entering the captive portal profile employee and then deleting its URL:

switch(config)# aaa authentication port-access captive-portal-profile employee
switch(config-captive-portal)# no url
switch(config-captive-portal)#
switch(config-captive-portal)# exit
switch(config)#

Creating a captive portal profile named guest and then setting its IPv6 redirect URL:

switch(config)# aaa authentication port-access captive-portal-profile CP6
switch(config-captive-portal)# url https://[2000::3]/guest/captive_portal.php
switch(config-captive-portal)#
switch(config-captive-portal)# exit
switch(config)#

url-hash-key

Syntax

url-hash-key [{plaintext | ciphertext} <HASH-KEY>]

Captive portal (RADIUS) | 222

no url-hash-key

Description

Within the captive portal context, defines the captive portal URL hash key.

When this command is entered without parameters, plaintext hash key prompting occurs upon pressing Enter.

The entered hash key characters are masked with asterisks.

The no form of this command deletes the captive portal URL hash key.

Command context

config-captive-portal

Parameters

{plaintext | ciphertext}

Selects the URL hash key type as either plaintext or ciphertext.

<HASH-KEY>

Specifies the captive portal URL hash key. Up to 128 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating a captive portal profile named employee and then setting its URL and URL hash key:

switch(config)# aaa authentication port-access captive-portal-profile employee
switch(config-captive-portal)# url http://1.1.1.1/employee/captiveportal.php
switch(config-captive-portal)#
switch(config-captive-portal)# url-hash-key plaintext cjQrJ9#$erty
switch(config-captive-portal)#

Creating a captive portal profile named guest and then setting its URL and entering the URL hash key when
prompted:

switch(config)# aaa authentication port-access captive-portal-profile guest
switch(config-captive-portal)# url http://1.1.1.1/guest/captiveportal.php
switch(config-captive-portal)#
switch(config-captive-portal)# url-hash-key
Enter the URL Hash-Key: ****
Re-Enter the URL Hash-Key: ****
switch(config-captive-portal)#

Entering the captive portal profile employee and then deleting its URL hash key:

switch(config)# aaa authentication port-access captive-portal-profile employee
switch(config-captive-portal)# no url-hash-key
switch(config-captive-portal)#

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

223

Chapter 15

Port access

Port access

Port access general commands

aaa authentication port-access auth-mode

Syntax

aaa authentication port-access auth-mode {client-mode | device-mode}

Description

Configures the authentication mode for the port. By default, client mode is enabled.

Command context

config-if

Parameters

client-mode

Selects client mode. In this mode, all clients connecting to the port are sent for authentication.

The maximum number of clients allowed to connect to the port is limited by the client limit value
configured with the aaa authentication port-access client-limit command.

device-mode

Selects device mode. In this mode, only the first client connecting to the port is sent for authentication.
Once this client is authenticated, the port is considered as open and all subsequent clients trying to
connect on that port are not sent for authentication.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring device mode authentication for a port:

switch(config-if)# aaa authentication port-access auth-mode device-mode

aaa authentication port-access auth-precedence

Syntax

aaa authentication port-access auth-precedence [dot1x mac-auth | mac-auth dot1x]

no aaa authentication port-access auth-precedence [dot1x mac-auth | mac-auth dot1x]
no aaa authentication port-access auth-precedence

Description

Configures the per port authentication precedence using the space separator.

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

224

By default, 802.1X authentication (dot1x) takes a higher precedence than MAC authentication (mac-auth).

The no form of the command resets the port access authentication precedence to the default, 802.1X
authentication followed by MAC authentication.

Command context

config-if

Parameters

dot1x mac-auth

Specifies that the port access authentication precedence is 802.1X authentication followed by MAC
authentication.

mac-auth dot1x

Specifies that the port access authentication precedence is MAC authentication followed by 802.1X
authentication.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring MAC authentication precedence on a port:

switch(config-if)# aaa authentication port-access auth-precedence mac-auth dot1x

Resetting the authentication precedence to the default value:

switch(config-if)# no aaa authentication port-access auth-precedence mac-auth dot1x

aaa authentication port-access auth-priority

Syntax

aaa authentication port-access auth-priority [dot1x mac-auth | mac-auth dot1x]
no aaa authentication port-access auth-priority [dot1x mac-auth | mac-auth dot1x]
no aaa authentication port-access auth-priority

Description

Configures the authentication priority using the space separator to specific interface.

Default auth-priority with concurrent onboarding is 802.1x followed by MAC authentication. With
authentication precedence, the default auth-priority follows the auth-precedence order.

The no form of the command resets the port access authentication priority to the default, is same as the
configured auth-precedence order.

The authentication priority is useful in deployments where clients such as wireless access points (APs), IT-
compliant-laptops or phones, or laptops without pre-loaded supplicant software must download the
supplicant software or firmware patches before attempting 802.1X authentication. In such cases, configure
the MAC authentication as the primary authentication method followed by 802.1X for the authentication
order. Meanwhile, configure 802.1x as the primary authentication priority and MAC authentication as
secondary to enforce access based on 802.1X. Thus the client (or end access device) will initially be
authenticated by MAC authentication with the access required to onboard and install the software or
patches, and subsequently attempt the 802.1X authentication.

Port access | 225

Reauthenticationwillbetriggeredforallhighprioritymethodsandnotjustthefinalsuccessful
authenticationmethod.
Commandcontext
config-if
Parameters
dot1x mac-auth
Specifiesthattheportaccessauthenticationpriorityis802.1XauthenticationfollowedbyMAC
authentication.
| mac-auth | dot1x |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- |
SpecifiesthattheportaccessauthenticationpriorityisMACauthenticationfollowedby802.1X
authentication.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringMACauthenticationpriorityonaport:
switch(config-if)# aaa authentication port-access auth-priority mac-auth dot1x
Resettingtheauthenticationprioritytothedefaultvalue:
switch(config-if)# no aaa authentication port-access auth-priority mac-auth dot1x
switch(config-if)# no aaa authentication port-access auth-priority
Sample configuration:
| interface | 1/1/1 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
no shutdown
no routing
|     | vlan access        | 1   |             |     |                 |                |
| --- | ------------------ | --- | ----------- | --- | --------------- | -------------- |
|     | aaa authentication |     | port-access |     | auth-precedence | mac-auth dot1x |
|     | aaa authentication |     | port-access |     | auth-priority   | dot1x mac-auth |
| aaa | authentication     |     | port-access |     | client-limit    |                |
Syntax
| aaa    | authentication | port-access |     | client-limit | <CLIENTS> |     |
| ------ | -------------- | ----------- | --- | ------------ | --------- | --- |
| no aaa | authentication | port-access |     | client-limit |           |     |
Description
Configuresthemaximumnumberofclientsthatcansimultaneouslyconnecttoaport.
Thenoformofthiscommandresetsthenumberofclientstothedefault.
Commandcontext
config-if
Parameters
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 226

<CLIENTS>

Specifies the maximum number of clients. Default: 1. Range: 1 to 32 (6200). 1 to 256 (6300, 6400).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the client limit for a port:

switch(config-if)# aaa authentication port-access client-limit 25

aaa authentication port-access (role)

Syntax

aaa authentication port-access [critical-role|preauth-role|reject-role|auth-role] <ROLE-
NAME>
no aaa authentication port-access [critical-role|preauth-role|reject-role|auth-role]

Description

Configures the role to assign to the clients depending on the client authentication state.

The no form of the command disassociates the roles that you assign to clients based on the authentication
state.

Command context

config-if

Parameters

critical-role

Specifies the role that is applied when the RADIUS server is unreachable for authentication or when there
is a request timeout.

preauth-role

Specifies the role that is applied when authentication is still in progress.

reject-role

Specifies the role that is applied when authentication has failed.

auth-role

Specifies the role that is applied to authenticated clients when a specific role is not assigned in the
RADIUS server.

<ROLE-NAME>

Specifies the role name.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring critical role for clients:

switch(config-if)# aaa authentication port-access critical-role role1

Port access | 227

port-access allow-flood-traffic

Syntax

port-access allow-flood-traffic {enable | disable}

Description

Enables or disables transmission of flood traffic, such as broadcast, multicast, and unknown unicast
messages through a security enabled port on which no client has been authenticated.

By default, transmission of flood traffic is disabled.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Usage

This command can be used to allow Wake-on-LAN packets on security enabled ports, before a client is
authenticated.

Examples

Enabling flood traffic on a port:

switch(config-if)# port-access allow-flood-traffic enable

port-access client-move

Syntax

port-access client-move {enable | disable}

Description

When client move is enabled (the default), a port access client can move to other port access-enabled
interfaces, at which time they will be re-authenticated on the new interface.

When client move is disabled, a client cannot move to other port access-enabled interfaces.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling client move:

switch(config)# port-access client-move enable

Disabling client move:

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

228

| switch(config)# |     | port-access   |     | client-move |     | disable |     |
| --------------- | --- | ------------- | --- | ----------- | --- | ------- | --- |
| port-access     |     | fallback-role |     |             |     |         |     |
Syntax
| port-access    | fallback-role |     | <ROLE-NAME> |             |     |     |     |
| -------------- | ------------- | --- | ----------- | ----------- | --- | --- | --- |
| no port-access | fallback-role |     |             | <ROLE-NAME> |     |     |     |
Description
Configuresthefallbackroletoassigntotheclientsonboardingonaport.Thisroleisappliedonlywhenno
derivedroleisappliedtotheclients.
Thenoformofthecommandresetsthefallbackrole.
Commandcontext
config-if
Parameters
<ROLE-NAME>
Specifiesthefallbackrolename.Themaximumnumberofcharacterssupportedis64.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Followingaretheconditionsforthefallbackroletobeappliedononboardingdevices:
n ThedeviceprofilelocalMACmatchfeaturewithblock-until-profile-appliedmodeisconfigured.
n DeviceprofilealongwithAAAisconfiguredbutnomatchwasfoundforthedeviceprofileclient.
n AAAmethodwithnorejectorcriticalroleisconfigured,andtheconnectiontoRADIUSserverfailed.
n 802.1Xauthenticationisenabledontheport,butthesupplicantofthedevicetimedouttorespondto
theauthenticationrequest.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringfallbackroleforaport:
| switch(config)#    |     | interface |             | 1/1/3 |               |     |            |
| ------------------ | --- | --------- | ----------- | ----- | ------------- | --- | ---------- |
| switch(config-if)# |     |           | port-access |       | fallback-role |     | fallback01 |
| port-access        |     | log-off   | client      |       |               |     |            |
Syntax
| port-access | log-off | client |     | mac <MAC-ADDRESS> |                  |     |     |
| ----------- | ------- | ------ | --- | ----------------- | ---------------- | --- | --- |
| port-access | log-off | client |     | interface         | <INTERFACE-NAME> |     |     |
| port-access | log-off | client |     | role <ROLE-NAME>  |                  |     |     |
Description
Logsofftheclientconnectedtoaportaccess-enabledinterface.
Portaccess|229

Command context

Manager (#)

Parameters

mac <MAC-ADDRESS>

Specifies the client MAC address.

interface <INTERFACE-NAME>

Specifies the client interface.

role <ROLE-NAME>

Specifies the client role.

Authority

Administrators or local user group members with execution rights for this command.

Example

Logging a client off from the switch, specifying the MAC address:

switch# port-access log-off client mac 00:50:56:bd:04:2d

Logging a client off from the switch, specifying the interface:

switch# port-access log-off client interface 1/1/1

Logging a client off from the switch, specifying the role:

switch# port-access log-off client role r1

port-access onboarding-method precedence

Syntax

port-access onboarding-method precedence [aaa device-profile | device-profile aaa]
no port-access onboarding-method precedence [aaa device-profile | device-profile aaa]

Description

Configures the precedence for the method to be used to authenticate onboarding devices for each
interface.

The no form of the command resets the authentication method precedence to the default precedence of
AAA followed by device profile.

AAA includes the 802.1X and MAC authentication methods whose precedence can be configured using the
aaa authentication port-access auth-precedence command. Here, the default precedence is 802.1X
authentication.

For example, if you configure AAA (both 802.1X and MAC) authentication methods and device profile on a
port, by default, the authentication precedence would be 802.1X, then MAC, and lastly device profile.

Command context

config-if

Parameters

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

230

aaa here refers to the authentication precedence configured using the aaa authentication port-access
auth-precedence command.

aaa device-profile

Specifies that the precedence for per port onboarding authentication method is AAA followed by device
profile.

device-profile aaa

Specifies that the precedence for per port onboarding authentication method is device profile followed
by AAA.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Configuring AAA method precedence on a port:

switch(config)# interface 1/1/1
switch(config-if)# port-access onboarding-method precedence device-profile aaa

Resetting the authentication method precedence:

switch(config)# interface 1/1/1
switch(config-if)# no port-access onboarding-method precedence device-profile aaa

port-access onboarding-method concurrent

Syntax

port-access onboarding-method concurrent <enable | disable>

Description

Configures all methods to start concurrently for faster onboarding process. If authentication priority is not
configured when enabling concurrent onboarding, the priority will be 802.1x followed by mac-auth and
device-profile.

Default priority for concurrent onboarding is 802.1x followed by mac-auth and device-profile.

When enabling concurrent onboarding on the port, existing clients will be de-authenticated and freshly
onboarded concurrently.

When concurrent onboarding is enabled, then auth-precedence will be ignored.

If concurrent onboarding is configured, the client will stay in pre-auth role till it gets succeeded by one
authentication method or gets failed by all the authentication methods.

When the authentication method with the highest priority fails, the profile of the next successful
authentication method is applied.

If all methods fail, the reject or critical role is applied based on the 802.1X authentication failure reason and
continues to reauthenticate with the 802.1X method.

Reauthentication will be triggered for all high priority methods and not just the final successful
authentication method.

Port access | 231

SomeRADIUSservermayblocktheclientwhenitreceivestworequests,mac-authand802.1X,fromthe
sameclientatthesametime.ThisisbecausetheRADIUSserverallowsonlyoneauthenticationrequest.In
suchcases,concurrentonboardingisnotfeasible.Topreventsuchscenarios,configureauth-precedence
withauth-priority.
Commandcontext
config-if
Parameters
enable
Enableclientstobeonboardedconcurrently.
disable
Disableclientstobeonboardedconcurrently.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Enablingconcurrentonboardingonaport:
| switch(config)# |     | interface | 1/1/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)# port-access onboarding-method concurrent enable
Disablingconcurrentonboardingonaport:
| switch(config)# |     | interface | 1/1/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)# port-access onboarding-method concurrent disable
Sample configuration:
| interface |     | 1/1/1 |     |     |     |     |
| --------- | --- | ----- | --- | --- | --- | --- |
no shutdown
no routing
|             | vlan        | access 999        |             |                 |        |                |
| ----------- | ----------- | ----------------- | ----------- | --------------- | ------ | -------------- |
|             | !aaa        | authentication    | port-access | auth-precedence |        | mac-auth dot1x |
|             | port-access | onboarding-method |             | concurrent      | enable |                |
| port-access |             | reauthenticate    |             | interface       |        |                |
Syntax
| port-access | reauthenticate |     | interface | <INTERFACE-NAME> |     |     |
| ----------- | -------------- | --- | --------- | ---------------- | --- | --- |
Description
Forcefullyreauthenticatesallclientsconnectedtoaninterface.
ClientsthatareintheHELDstateareignored.
Commandcontext
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 232

Manager (#)

Parameters

<INTERFACE-NAME>

Specifies the interface name.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring reauthentication of all clients on a port (6200 and 6300 Switch Series):

switch# port-access reauthenticate interface 1/1/1

Configuring reauthentication of all clients on a port (6400 Switch Series):

switch# port-access reauthenticate interface 1/3/1

port-access security violation action

Syntax

port-access security violation action [notify | shutdown]
no port-access security violation action

Description

Configures the action that the switch must take whenever a security violation occurs at a port, such as the
number of clients exceeds the configured client limit.

The no form of the command resets the action to the default action, notify.

Command context

config-if

Parameters

notify

Specifies that the switch notifies any security violation as an event or log in the syslog server. This action
is the default.

shutdown

Specifies that the switch shuts down the port where the client limit has exceeded.

A port that is shut down can be configured to auto-recover after a recovery period that can be
configured with the port-access security violation action shutdown auto-recovery and port-
access security violation action shutdown recovery-timer commands.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the shutdown security violation action for a port:

Port access | 233

sswitch(config-if)# port-access security violation action shutdown

Resetting the security violation action to the default value:

switch(config-if)# no port-access security violation action

port-access security violation action shutdown auto-recovery

Syntax

port-access security violation action shutdown auto-recovery [enable | disable]
no port-access security violation action shutdown auto-recovery

Description

Configures auto-recovery of the port when the security violation action is configured as shutdown.

This configuration allows the port that is shut down when a security violation occurs to automatically enable
after the recovery timer expires.

The no form of the command resets auto-recovery to the default, disable.

Command context

config-if

Parameters

enable

Enables auto-recovery of port when the security violation action is configured as shutdown.

disable

Disables auto-recovery of port when the security violation action is configured as shutdown.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling auto-recovery of port:

switch(config-if)# port-access security violation action shutdown auto-recovery
enable

Disabling auto-recovery of port:

switch(config-if)# no port-access security violation action shutdown auto-recovery

port-access security violation action shutdown recovery-timer

Syntax

port-access security violation action shutdown recovery-timer <RECOVERY-TIME>
no port-access security violation action shutdown recovery-timer

Description

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

234

Configures security violation recovery timer for the port when the security violation action is configured as
shutdown.

The no form of the command resets the shutdown recovery timer to the default, 10.

Command context

config-if

Parameters

<RECOVERY-TIME>

Specifies the recovery timer (in seconds) after which the port, which is shut down because of security
violation, is automatically enabled. Default: 10. Range: 10 to 600.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the shutdown recovery-timer on a port:

switch(config-if)# port-access security violation action shutdown recovery-timer 60

Resetting the shutdown recovery-timer to the default value:

switch(config-if)# no port-access security violation action shutdown recovery-timer

show aaa authentication port-access interface client-status

Syntax

show aaa authentication port-access interface {all|<INTERFACE-NAME>} client-status [mac
<MAC-ADDRESS>]

Description

Shows information about active port access sessions. The output can be filtered by interface or MAC
address.

Command context

Operator (>) or Manager (#)

Parameters

all

Specifies all interfaces.

<INTERFACE-NAME>

Specifies the interface name.

<MAC-ADDRESS>

Specifies the client MAC address.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Port access | 235

Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showinginformationforallports.
switch# show aaa authentication port-access interface all client-status
| Port Access               | Client Status | Details  |
| ------------------------- | ------------- | -------- |
| Client 00:50:56:96:93:d6, |               | John Doe |
============================
| Session | Details |     |
| ------- | ------- | --- |
---------------
| Port           | : 1/1/13   |     |
| -------------- | ---------- | --- |
| Session        | Time : 30s |     |
| Authentication | Details    |     |
----------------------
| Status | : dot1x | Authenticated |
| ------ | ------- | ------------- |
Auth Precedence : dot1x - Authenticated, mac-auth - Not attempted
| Authorization | Details |     |
| ------------- | ------- | --- |
----------------------
| Role   | : Employee |     |
| ------ | ---------- | --- |
| Status | : Applied  |     |
Client 00:50:56:96:50:28
============================
| Session | Details |     |
| ------- | ------- | --- |
---------------
| Port           | : 1/1/14   |     |
| -------------- | ---------- | --- |
| Session        | Time : 10s |     |
| Authentication | Details    |     |
----------------------
| Status | : mac-auth | Authenticated |
| ------ | ---------- | ------------- |
Auth Precedence : dot1x - Unauthenticated, mac-auth - Authenticated
| Authorization | Details |     |
| ------------- | ------- | --- |
----------------------
| Role             | : RADIUS_773420618 |     |
| ---------------- | ------------------ | --- |
| Status           | : Applied          |     |
| show port-access | clients            |     |
Syntax
show port-access clients [interface <INTERFACE-NAME>] [mac <MAC-ADDRESS>]
Description
Showssummarizedactiveportaccessclientinformation.TheoutputcanbefilteredbyinterfaceorMAC
address.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-NAME>
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 236

Specifiestheinterfacename.
<MAC-ADDRESS>
SpecifiestheclientMACaddress.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showinginformationforallclients.
| switch#     | show port-access | clients |     |     |     |     |     |
| ----------- | ---------------- | ------- | --- | --- | --- | --- | --- |
| Port Access | Clients          |         |     |     |     |     |     |
--------------------------------------------------------------------------------
| Port | MAC Address |     | Onboarded |     | Status | Role |     |
| ---- | ----------- | --- | --------- | --- | ------ | ---- | --- |
Method
--------------------------------------------------------------------------------
| 1/1/4  | 00:50:56:bd:04:c8 |     | port-security  |     | Success     |                  |          |
| ------ | ----------------- | --- | -------------- | --- | ----------- | ---------------- | -------- |
| 1/1/5  | 00:50:56:bd:32:07 |     |                |     | Success     | reject-role,     | Reject   |
| 1/1/5  | 00:50:56:bd:32:08 |     |                |     | Fail        | critical-...,    | Critical |
| 1/1/6  | 00:50:56:bd:50:43 |     | mac-auth       |     | Success     | auth-role,       | Auth     |
| 1/1/6  | 00:50:56:bd:50:45 |     | dot1x          |     | Success     | RADIUS_773420618 |          |
| 1/1/19 | 08:97:34:ad:e4:00 |     | device-profile |     | Success     | ap-role          |          |
| 1/1/20 | 00:50:56:bd:32:08 |     |                |     | In-Progress | preauth-role,    | Preauth  |
| 1/1/20 | 00:50:56:bd:32:06 |     |                |     | In-Progress |                  |          |
| 1/1/20 | 00:50:56:bd:32:09 |     |                |     | Fail        |                  |          |
1/1/212 00:60:56:bd:50:43 mac-auth Success fallback-role, Fallback
Showinginformationforclientsonaparticularinterface:
| switch#     | show port-access | clients | interface |     | 1/1/5 |     |     |
| ----------- | ---------------- | ------- | --------- | --- | ----- | --- | --- |
| Port Access | Clients          |         |           |     |       |     |     |
--------------------------------------------------------------------------------
| Port | MAC Address |     | Onboarded |     | Status | Role |     |
| ---- | ----------- | --- | --------- | --- | ------ | ---- | --- |
Method
--------------------------------------------------------------------------------
| 1/1/5 | 00:50:56:bd:32:07 |     |     |     | Success | reject-role,  | Reject   |
| ----- | ----------------- | --- | --- | --- | ------- | ------------- | -------- |
| 1/1/5 | 00:50:56:bd:32:08 |     |     |     | Fail    | critical-..., | Critical |
ShowinginformationforaparticularclientMACaddress:
| switch#     | show port-access | clients | mac | 00:50:56:bd:50:43 |     |     |     |
| ----------- | ---------------- | ------- | --- | ----------------- | --- | --- | --- |
| Port Access | Clients          |         |     |                   |     |     |     |
--------------------------------------------------------------------------------
| Port | MAC Address |     | Onboarded |     | Status | Role |     |
| ---- | ----------- | --- | --------- | --- | ------ | ---- | --- |
Method
--------------------------------------------------------------------------------
| 1/1/6            | 00:50:56:bd:50:43 |         | mac-auth |     | Success | auth-role, | Auth |
| ---------------- | ----------------- | ------- | -------- | --- | ------- | ---------- | ---- |
| show port-access |                   | clients | detail   |     |         |            |      |
Portaccess|237

Syntax
show port-access clients [interface <INTERFACE-NAME>] [mac <MAC-ADDRESS>] detail
Description
ShowsdetailedactiveportaccessclientsinformationincludingtheVLANgroupandVLANassociationfor
eachoftheauthenticatedclients.TheoutputcanbefilteredbyinterfaceorMACaddress.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-NAME>
Specifiestheinterfacename.
<MAC-ADDRESS>
SpecifiestheclientMACaddress.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingdetailedinformationforclientsonaparticularinterface(oneclient):
| switch# show | port-access | clients         | interface | 1/1/7 detail |
| ------------ | ----------- | --------------- | --------- | ------------ |
| Port Access  | Client      | Status Details: |           |              |
---------------------------------
| Client 2c:41:38:7f:35:b9, |     | John | Doe |     |
| ------------------------- | --- | ---- | --- | --- |
============================
| Session | Details |     |     |     |
| ------- | ------- | --- | --- | --- |
---------------
| Port    |         | : 1/1/7       |     |     |
| ------- | ------- | ------------- | --- | --- |
| Session | Time    | : 203s        |     |     |
| IPv4    | Address | : 10.10.10.10 |     |     |
| IPv6    | Address | :             |     |     |
VLAN Details
------------
| VLAN           | Group Name | : vlan_group1 |     |     |
| -------------- | ---------- | ------------- | --- | --- |
| VLANs          | Assigned   | : 12          |     |     |
| Access         |            | : 12          |     |     |
| Native         | Untagged   | :             |     |     |
| Allowed        | Trunk      | :             |     |     |
| Authentication |            | Details       |     |     |
----------------------
| Status |     | : mac-auth | Authenticated |     |
| ------ | --- | ---------- | ------------- | --- |
Auth Precedence : dot1x - Unauthenticated, mac-auth - Authenticated
| Auth          | History | : mac-auth | - Authenticated, | 203s ago |
| ------------- | ------- | ---------- | ---------------- | -------- |
| Authorization | Details |            |                  |          |
----------------------
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 238

| Role   | : RADIUS_21963402 |     |     |     |     |
| ------ | ----------------- | --- | --- | --- | --- |
| Status | : Applied         |     |     |     |     |
Role Information:
----------------
| Name : RADIUS_21963402 |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- |
| Type : radius          |     |     |     |     |     |
----------------------------------------------
| Reauthentication     |                | Period               | : 333 secs            |     |     |
| -------------------- | -------------- | -------------------- | --------------------- | --- | --- |
| Authentication       |                | Mode                 | :                     |     |     |
| Session              | Timeout        |                      | :                     |     |     |
| Client               | Inactivity     | Timeout              | :                     |     |     |
| Description          |                |                      | :                     |     |     |
| GatewayZone          |                | :zone_1              |                       |     |     |
| UBTGatewayRole       |                | :                    |                       |     |     |
| Access               | VLAN           |                      | :                     |     |     |
| Native               | VLAN           |                      | :                     |     |     |
| Allowed              | Trunk          | VLANs                | :                     |     |     |
| Access               | VLAN           | Name                 | :                     |     |     |
| Native               | VLAN           | Name                 | :                     |     |     |
| Allowed              | Trunk          | VLAN Names           | :                     |     |     |
| VLAN                 | Group          | Name                 | : vlan_group1         |     |     |
| MTU                  |                |                      | :                     |     |     |
| QOS                  | Trust Mode     |                      | :                     |     |     |
| STP                  | Administrative | Edge Port            | :                     |     |     |
| PoE                  | Priority       |                      | : low                 |     |     |
| CaptivePortalProfile |                | :testcpprof_29451201 |                       |     |     |
| Policy               |                |                      | : PERMIT-ALL_87364653 |     |     |
UBTZonedetails:
-----------------
| ZoneName          | :zone_1 |               |     |     |     |
| ----------------- | ------- | ------------- | --- | --- | --- |
| PrimaryController |         | :10.116.51.10 |     |     |     |
| BackupController  |         | :10.116.51.11 |     |     |     |
SACHeartBeatInterval:1
UACKeepAliveInterval:60
| VLANIdentifier | :4094    |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- |
| VRFName        | :my-vrf  |     |     |     |     |
| AdminState     | :ENABLED |     |     |     |     |
PAPISecurityKey :AQBapdxySvGPvdTlkYn1/naKX4O3jKHrm28xLYfO6mLOK499BwAAAHdJp/bL4FE=
CaptivePortalProfileConfiguration:
------------------------------------
| Name          |          | :testcpprof_29451201                          |     |     |     |
| ------------- | -------- | --------------------------------------------- | --- | --- | --- |
| Type          |          | :local                                        |     |     |     |
| URL           |          | :http://google.com                            |     |     |     |
| URLHashKey    |          | :SWNGWyMeYubHPDgVIirpEUwNK5Uf+r1vmhBIncQPw1Y= |     |     |     |
| Access Policy | Details: |                                               |     |     |     |
----------------------
| Policy Name   | : PERMIT-ALL_87364653 |     |             |     |     |
| ------------- | --------------------- | --- | ----------- | --- | --- |
| Policy Type   | : Local               |     |             |     |     |
| Policy Status | : Applied             |     |             |     |     |
| SEQUENCE      | CLASS                 |     | TYPE ACTION |     |     |
----------- ---------------------------- ---- ----------------------------------
| 10             | dns           |                            | ipv4 permit   |             |      |
| -------------- | ------------- | -------------------------- | ------------- | ----------- | ---- |
| 20             | dhcp          |                            | ipv4 permit   |             |      |
| 30             | clearpass-web |                            | ipv4 cir kbps | 1024 exceed | drop |
| 40 web-traffic |               | ipv4redirectcaptive-portal |               |             |      |
Portaccess|239

Class Details:
--------------
| class ip | dns           |         |     |     |     |     |     |
| -------- | ------------- | ------- | --- | --- | --- | --- | --- |
| 10 match |               | tcp any | any |     |     |     |     |
| class ip | dhcp          |         |     |     |     |     |     |
| 20 match |               | any any | any |     |     |     |     |
| class ip | clearpass-web |         |     |     |     |     |     |
| 30 match |               | any any | any |     |     |     |     |
classipweb-traffic
40matchanyanyany
ShowinginformationforaparticularclientMACaddress:
| 6300# show                | port-access |     | clients | mac               | 00:00:00:00:00:c8 |     | detail |
| ------------------------- | ----------- | --- | ------- | ----------------- | ----------------- | --- | ------ |
| Port Access               | Client      |     | Status  | Details:          |                   |     |        |
| Client 00:00:00:00:00:c8, |             |     |         | 00:00:00:00:00:c8 |                   |     |        |
============================
| Session | Details |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
---------------
| Port         |      | : 1/1/1 |     |     |     |     |     |
| ------------ | ---- | ------- | --- | --- | --- | --- | --- |
| Session      | Time | : 888s  |     |     |     |     |     |
| IPv4 Address |      | :       |     |     |     |     |     |
| IPv6 Address |      | :       |     |     |     |     |     |
VLAN Details
------------
| VLAN Group      | Name  | : test_group |     |     |     |     |     |
| --------------- | ----- | ------------ | --- | --- | --- | --- | --- |
| VLANs Assigned  |       | : 22         |     |     |     |     |     |
| Access          |       | : 22         |     |     |     |     |     |
| Native Untagged |       | :            |     |     |     |     |     |
| Allowed         | Trunk | :            |     |     |     |     |     |
| Authentication  |       | Details      |     |     |     |     |     |
----------------------
| Status |     | : mac-auth |     | Authenticated |     |     |     |
| ------ | --- | ---------- | --- | ------------- | --- | --- | --- |
Auth Precedence : dot1x - Unauthenticated, mac-auth - Authenticated
| Auth History  |                  | : mac-auth |     | - Authenticated,    |     | 288s ago |     |
| ------------- | ---------------- | ---------- | --- | ------------------- | --- | -------- | --- |
| dot1x -       | Unauthenticated, |            |     | Supplicant-Timeout, |     | 703s     | ago |
| dot1x -       | Unauthenticated, |            |     | 798s ago            |     |          |     |
| mac-auth      | - Authenticated, |            |     | 888s ago            |     |          |     |
| Authorization |                  | Details    |     |                     |     |          |     |
----------------------
| Role :   | RADIUS_2801090107 |     |     |     |     |     |     |
| -------- | ----------------- | --- | --- | --- | --- | --- | --- |
| Status : | Applied           |     |     |     |     |     |     |
Role Information:
| Name : | RADIUS_2801090107 |     |     |     |     |     |     |
| ------ | ----------------- | --- | --- | --- | --- | --- | --- |
| Type : | radius            |     |     |     |     |     |     |
----------------------------------------------
| Reauthentication        |           | Period  |      |        | : 600 | secs |     |
| ----------------------- | --------- | ------- | ---- | ------ | ----- | ---- | --- |
| Cached Reauthentication |           |         |      | Period | :     |      |     |
| Authentication          |           | Mode    |      |        | :     |      |     |
| Session                 | Timeout   |         |      |        | :     |      |     |
| Client Inactivity       |           | Timeout |      |        | :     |      |     |
| Description             |           |         |      |        | :     |      |     |
| Gateway                 | Zone      |         |      |        | :     |      |     |
| UBT Gateway             | Role      |         |      |        | :     |      |     |
| UBT Gateway             | Clearpass |         | Role |        | :     |      |     |
| Access VLAN             |           |         |      |        | :     |      |     |
| Native VLAN             |           |         |      |        | :     |      |     |
| Allowed                 | Trunk     | VLANs   |      |        | :     |      |     |
| Access VLAN             | Name      |         |      |        | :     |      |     |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 240

|     | Native             | VLAN   | Name    |           |     | :            |     |     |     |
| --- | ------------------ | ------ | ------- | --------- | --- | ------------ | --- | --- | --- |
|     | Allowed            | Trunk  | VLAN    | Names     |     | :            |     |     |     |
|     | VLAN Group         | Name   |         |           |     | : test_group |     |     |     |
|     | MTU                |        |         |           |     | :            |     |     |     |
|     | QOS Trust          | Mode   |         |           |     | :            |     |     |     |
|     | STP Administrative |        |         | Edge Port |     | :            |     |     |     |
|     | PoE Priority       |        |         |           |     | :            |     |     |     |
|     | Captive            | Portal | Profile |           |     | :            |     |     |     |
|     | Policy             |        |         |           |     | :            |     |     |     |
|     | GBP                |        |         |           |     | :            |     |     |     |
6300#
| show | port-access |     |     | clients | onboarding-method |     |     |     |     |
| ---- | ----------- | --- | --- | ------- | ----------------- | --- | --- | --- | --- |
Syntax
| show | port-access |     | clients | onboarding-method |     | <METHOD> |     |     |     |
| ---- | ----------- | --- | ------- | ----------------- | --- | -------- | --- | --- | --- |
Description
Showsactiveportaccessclientinformationforthespecifiedonboardingmethod.
Commandcontext
Operator(>)orManager(#)
Parameters
<METHOD>
Selectstheonboardingmethod.Availablemethods:device-profile,dot1x,mac-auth,port-security.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowinginformationforclientsonboardedusingMACauthentication.
|     | switch#     | show   | port-access | clients |     | onboarding-method | mac-auth |     |     |
| --- | ----------- | ------ | ----------- | ------- | --- | ----------------- | -------- | --- | --- |
|     | Port Access |        | Clients     |         |     |                   |          |     |     |
|     | Status      | codes: | device-mode |         |     |                   |          |     |     |
-----------------------------------------------------------------------------------
|     | Port |     | MAC-Address |     | Onboarding |     | Status | Role |     |
| --- | ---- | --- | ----------- | --- | ---------- | --- | ------ | ---- | --- |
Method
-----------------------------------------------------------------------------------
|     | 1/1/6 |     | 00:50:56:bd:50:43 |     | mac-auth |     | Success | auth-role, | auth |
| --- | ----- | --- | ----------------- | --- | -------- | --- | ------- | ---------- | ---- |
1/1/212 00:60:56:bd:50:43 mac-auth Success fallback-role, fallback
show port-access security violation client-limit-exceeded interface
Syntax
show port-access security violation client-limit-exceeded interface {all|<INTERFACE-NAME>}
Portaccess|241

Description
Showsinformationrelatedtoinformationonthenumberofclient-limit-exceededsecurityviolationsthat
haveoccurred.Theoutputcanbefilteredbyinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
all
Specifiesallinterfaces.
<INTERFACE-NAME>
Specifiestheinterfacename.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showinginformationforallports.
switch# show port-access security violation client-limit-exceeded interface all
| Client Limit | Exceeded | Violation   | Status Details |
| ------------ | -------- | ----------- | -------------- |
| Port         |          | : 1/1/1     |                |
| Violation    | Count    | : 10        |                |
| Violation    | State    | : Violation | Occurred       |
| Port         |          | : 1/1/2     |                |
| Violation    | Count    | : 10        |                |
| Violation    | State    | : None      |                |
Showinginformationforaparticularport.
switch# show port-access security violation client-limit-exceeded interface 1/1/1
| Client Limit | Exceeded | Violation      | Status Details |
| ------------ | -------- | -------------- | -------------- |
| Port         |          | : 1/1/1        |                |
| Violation    | Count    | : 10           |                |
| Violation    | State    | : None         |                |
| Port access  | 802.1X   | authentication |                |
IEEE802.1Xisastandardforport-basedauthentication.Thisstandardprovidesadministratorswithan
authenticationmechanismfordevicestryingtoaccessaLANorWLAN.802.1Xdefinestheencapsulationof
theExtensibleAuthenticationProtocol(EAP)overIEEE802,whichisknownasEAPoverLAN(EAPOL).
802.1Xauthenticationinvolvesthefollowingentities:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 242

n Supplicant: Device that tries to access the LAN.

n Authenticator: A network device, such as an Ethernet switch that authenticates the supplicant.

n Authentication Server: Typically a host running software supporting the RADIUS and EAP protocols

that provides an authentication service to the authenticator.

Until the supplicant is authenticated, the authenticator allows only EAPOL traffic through the port to which
the supplicant is connected. Only after the authentication is successful, the authenticator allows normal
traffic from the supplicant.

802.1X port-based authentication provides port-level security. It allows LAN access only on ports where a
single 802.1X-capable client (supplicant) has entered authorized RADIUS user credentials. 802.1X
authentication is recommended for applications where only one client can connect to the port at a time.
Using this option, the port processes all IP traffic as if it comes from the same client.

In addition to using CLI and REST APIs to obtain authentication details of port-access clients, you can use SNMP
to obtain these details.

Port access 802.1X authentication commands

aaa authentication port-access dot1x authenticator

Syntax

aaa authentication port-access dot1x authenticator {enable | disable}
no aaa authentication port-access dot1x authenticator

Description

Enables or disables 802.1X authentication globally or at the port-level.

The no form of the command deletes global 802.1X configuration details and disables 802.1x
authentication.

Command context

config
config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling 802.1X authentication globally:

switch(config)# aaa authentication port-access dot1x authenticator enable

Disabling 802.1X authentication globally:

switch(config)# aaa authentication port-access dot1x authenticator disable

Deleting and disabling global 802.1X authentication:

switch(config)# no aaa authentication port-access dot1x authenticator

Port access | 243

Enabling 802.1X authentication on a port:

switch(config-if)# aaa authentication port-access dot1x authenticator enable

Disabling 802.1X authentication on a port:

switch(config-if)# aaa authentication port-access dot1x authenticator disable

Deleting and disabling 802.1X authentication configuration on a port:

switch(config-if)# no aaa authentication port-access dot1x authenticator

aaa authentication port-access dot1x authenticator auth-method

Syntax

aaa authentication port-access dot1x authenticator auth-method eap-radius
no aaa authentication port-access dot1x authenticator auth-method eap-radius

Description

Configures the authentication mechanism used to control access to the network. The configured
authentication method will be used to authenticate 802.1X clients.

The no form of the command resets the authentication mechanism to the default, eap-radius.

Command context

config

Parameters

eap-radius

Specifies the EAP RADIUS as the 802.1X authentication method.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling the EAP RADIUS 802.1X authentication method on the switch:

switch(config)# aaa authentication port-access dot1x authenticator auth-method eap-
radius

Resetting the EAP RADIUS 802.1X authentication method on the switch:

switch(config)# no aaa authentication port-access dot1x authenticator auth-method
eap-radius

aaa authentication port-access dot1x authenticator cached-reauth

Syntax

aaa authentication port-access dot1x authenticator cached-reauth

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

244

no aaa authentication port-access dot1x authenticator cached-reauth

Description

Enables cached reauthentication on a port. Cached reauthentication allows 802.1X reauthentications to
succeed when the RADIUS server is unavailable. Users already authenticated retain their currently assigned
RADIUS attributes.

The no form of the command disables the cached reauthentication on a port.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling cached reauthentication on a port:

switch(config-if)# aaa authentication port-access dot1x authenticator cached-reauth

Disabling cached reauthentication on a port:

switch(config-if)# no aaa authentication port-access dot1x authenticator cached-
reauth

aaa authentication port-access dot1x authenticator cached-reauth-period

Syntax

aaa authentication port-access dot1x authenticator cached-reauth-period <PERIOD>
no aaa authentication port-access dot1x authenticator cached-reauth-period

Description

Configures the period during which an authenticated client, which has failed to reauthenticate because the
RADIUS server is unreachable, remains authenticated.

The no form of the command resets the cached reauthentication period to the default, 30 seconds.

Command context

config-if

Parameters

<PERIOD>

Specifies the cached reauthentication period (in seconds). Default: 30. Range: 30 to 86400.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the cached reauthentication period on a port:

Port access | 245

switch(config-if)# aaa authentication port-access dot1x authenticator cached-reauth-
period 300

Resetting the cached reauthentication period to the default value:

switch(config-if)# no aaa authentication port-access dot1x authenticator cached-
reauth-period

aaa authentication port-access dot1x authenticator discovery-period

Syntax

aaa authentication port-access dot1x authenticator discovery-period <PERIOD>
no aaa authentication port-access dot1x authenticator discovery-period

Description

Configures the period the port waits to retransmit the next EAPOL request identity frame on an 802.1X
enabled port that has no authenticated clients.

The no form of the command resets the discovery period to the default, 30 seconds.

Command context

config-if

Parameters

<PERIOD>

Specifies the discovery period (in seconds). Default: 30. Range: 1 to 65535.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the discovery period on a port:

switch(config-if)# aaa authentication port-access dot1x authenticator discovery-
period 120

Resetting the discovery period to the default value:

switch(config-if)# no aaa authentication port-access dot1x authenticator discovery-
period

aaa authentication port-access dot1x authenticator eapol-timeout

Syntax

aaa authentication port-access dot1x authenticator eapol-timeout <EAPOL-TIMEOUT>
no aaa authentication port-access dot1x authenticator eapol-timeout

Description

Configure the period the switch waits for a response from a client before retransmitting an EAPOL PDU.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

246

If the value is 0, the time period is calculated as per RFC 2988.

As per RFC 2988 2.1: Before Round-Trip Time (RTT) measurement, set Retransmission Timeout (RTO) to 3

seconds for initial retransmission and then double the RTO to provide back off as per section 5.5. Limit the

maximum RTO (RTOmax) to 20 seconds as per section 4.3 of RFC 3748.

The no form of the command resets the timeout period to the default.

Command context

config-if

Parameters

<EAPOL-TIMEOUT>

Specifies the EAPOL timeout period (in seconds). Range: 1 to 65535.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring EAPOL timeout on a port:

switch(config-if)# aaa authentication port-access dot1x authenticator eapol-timeout
120

Resetting the EAPOL timeout to the default value:

switch(config-if)# no aaa authentication port-access dot1x authenticator eapol-
timeout

aaa authentication port-access dot1x authenticator max-eapol-requests

Syntax

aaa authentication port-access dot1x authenticator max-eapol-requests <MAX-EAPOL-REQUESTS>
no aaa authentication port-access dot1x authenticator max-eapol-requests

Description

Configures the number of EAPOL requests to send to a supplicant that must time out before authentication
fails and the authentication session ends.

The no form of the command resets the maximum number of EAPOL requests to the default, 5.

Command context

config-if

Parameters

<MAX-EAPOL-REQUESTS>

Specifies the maximum number of EAPOL requests. Default: 5. Range: 1 to 10.

Authority

Administrators or local user group members with execution rights for this command.

Port access | 247

Examples

Configuring maximum EAPOL requests on a port:

switch(config-if)# aaa authentication port-access dot1x authenticator max-eapol-
requests 3

Resetting the maximum EAPOL requests on a port to default:

switch(config-if)# no aaa authentication port-access dot1x authenticator max-eapol-
requests

port-access dot1x authenticator max-retries

Syntax

aaa authentication port-access dot1x authenticator max-retries <max-retries>
no aaa authentication port-access dot1x authenticator max-retries

Description

Configures the maximum number of retries that the switch attempts to authenticate a client on a port
before marking the client as unauthenticated.

The no form of the command resets the maximum number of retries to the default, 2.

Command context

config-if

Parameters

<max-retries>

Indicates the number of authentication attempts. Default: 2. Range: 1 to 10.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring maximum authentication attempts on a port:

switch(config-if)# aaa authentication port-access dot1x authenticator max-retries 5

Resetting the maximum authentication attempts on a port to default:

switch(config-if)# no aaa authentication port-access dot1x authenticator max-retries

aaa authentication port-access dot1x authenticator quiet-period

Syntax

aaa authentication port-access dot1x authenticator quiet-period <PERIOD>
no aaa authentication port-access dot1x authenticator quiet-period

Description

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

248

Configures the period during which the port does not try to acquire a supplicant. This period begins after
the last authentication attempt, authorized by the maximum retries parameter, fails.

You can configure the number of maximum retries with the aaa authentication port-access dot1x
authenticator max-retries command.

The no form of the command resets the quiet period to the default, 60 seconds.

Command context

config-if

Parameters

<PERIOD>

Specifies the quiet period (in seconds). Default: 60. Range: 0 to 65535.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring quiet period on a port:

switch(config-if)# aaa authentication port-access dot1x authenticator quiet-period
100

Resetting the quiet period on a port to default:

switch(config-if)# no aaa authentication port-access dot1x authenticator quiet-
period

aaa authentication port-access dot1x authenticator radius server-group

Syntax

aaa authentication port-access dot1x authenticator radius server-group <GROUP-NAME>
no aaa authentication port-access dot1x authenticator radius server-group

Description

Configures the switch to use an existing RADIUS server group for 802.1X authentication.

The no form of the command resets the server group to the default, radius.

Command context

config

Parameters

<GROUP-NAME>

Specifies the name of the RADIUS server group.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the switch to use RADIUS server group employee:

Port access | 249

switch(config)# aaa authentication port-access dot1x authenticator radius server-
group employee

Resetting RADIUS server group configuration to default:

switch(config)# no aaa authentication port-access dot1x authenticator radius server-
group

aaa authentication port-access dot1x authenticator reauth

Syntax

aaa authentication port-access dot1x authenticator reauth
no aaa authentication port-access dot1x authenticator reauth

Description

Enables periodic reauthentication of authenticated clients on the port.

The no form of the command disables periodic reauthentication.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling periodic reauthentication on a port:

switch(config-if)# aaa authentication port-access dot1x authenticator reauth

Disabling periodic reauthentication on a port:

switch(config-if)# no aaa authentication port-access dot1x authenticator reauth

aaa authentication port-access dot1x authenticator reauth-period

Syntax

aaa authentication port-access dot1x authenticator reauth-period <PERIOD>
no aaa authentication port-access dot1x authenticator reauth-period

Description

Configures the period after which the authenticated clients are reauthenticated on the port. You must
enable reauthentication on the port before configuring the reauthentication period.

The no form of the command resets the reauthentication period to the default, 3600 seconds.

Command context

config-if

Parameters

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

250

<PERIOD>

Specifies the reauthentication period (in seconds). Default: 3600. Range: 1 to 65535.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring reauthentication period on a port:

switch(config-if)# aaa authentication port-access dot1x authenticator reauth-period
100

Resetting the reauthentication period to the default value:

switch(config-if)# no aaa authentication port-access dot1x authenticator reauth-
period

clear dot1x authenticator statistics interface

Syntax

clear dot1x authenticator statistics [interface <IF-NAME>]

Description

Clears the 802.1X authentication statistics associated with the port and all the authenticator clients
attached to this port.

If no interface is specified, the statistics is cleared for all 802.1X enabled ports.

Command context

Manager (#)

Parameters

<IF-NAME>

Specifies the interface name.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Clearing authentication statistics on a port (6200 and 6300 Switch Series):

switch# clear dot1x authenticator statistics interface 1/1/1

Clearing authentication statistics on a port (6400 Switch Series):

switch# clear dot1x authenticator statistics interface 1/3/1

Clearing authentication statistics on all ports:

Port access | 251

| switch# clear | dot1x authenticator |     | statistics |     |
| ------------- | ------------------- | --- | ---------- | --- |
show aaa authentication port-accessdot1xauthenticator interface client-status
Syntax
show aaa authentication port-access dot1x authenticator interface {all|<IF-NAME>}
| client-status | [mac <MAC-ADDRESS>] |     |     |     |
| ------------- | ------------------- | --- | --- | --- |
Description
Showsinformationaboutactive802.1Xauthenticationsessions.Theoutputcanbefilteredbyinterfaceor
MACaddress.
Commandcontext
Operator(>)orManager(#)
Parameters
all
Specifiesallinterfaces.
<IF-NAME>
Specifiestheinterfacename.
<MAC-ADDRESS>
SpecifiestheclientMACaddress.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingclientstatusinformationforallports.
switch# show aaa authentication port-access dot1x authenticator interface all
client-status
| Client FE:04:D7:50:89:37, |     | johndoe, | 1/1/1 |     |
| ------------------------- | --- | -------- | ----- | --- |
=========================================
| Authentication | Details |     |     |     |
| -------------- | ------- | --- | --- | --- |
----------------------
| Status         |            |        | : Authenticated |     |
| -------------- | ---------- | ------ | --------------- | --- |
| Type           |            |        | : Pass-Through  |     |
| EAP-Method     |            |        | : MD5           |     |
| Time Since     | Last State | Change | : 10s           |     |
| Authentication | Statistics |        |                 |     |
-------------------------
| Authentication |                      |     |     | : 0 |
| -------------- | -------------------- | --- | --- | --- |
| Authentication | Timeout              |     |     | : 0 |
| EAP-Start      | While Authenticating |     |     | : 0 |
| EAP-Logoff     | While Authenticating |     |     | : 0 |
| Successful     | Authentication       |     |     | : 0 |
| Failed         | Authentication       |     |     | : 0 |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 252

| Re-Authentication         |                    |          | : 0   |
| ------------------------- | ------------------ | -------- | ----- |
| Successful                | Re-Authentication  |          | : 0   |
| Failed                    | Re-Authentication  |          | : 0   |
| EAP-Start                 | When Authenticated |          | : 0   |
| EAP-Logoff                | When Authenticated |          | : 0   |
| Re-Auths                  | When Authenticated |          | : 0   |
| Cached                    | Re-Authentication  |          | : 0   |
| Client 9A:B4:59:97:D0:7E, |                    | janedoe, | 1/1/1 |
=========================================
| Authentication | Details |     |     |
| -------------- | ------- | --- | --- |
----------------------
| Status         |            |        | : Authenticated |
| -------------- | ---------- | ------ | --------------- |
| Type           |            |        | : Pass-Through  |
| EAP-Method     |            |        | : TLS           |
| Time Since     | Last State | Change | : 5s            |
| Authentication | Statistics |        |                 |
-------------------------
| Authentication    |                      |     | : 0 |
| ----------------- | -------------------- | --- | --- |
| Authentication    | Timeout              |     | : 0 |
| EAP-Start         | While Authenticating |     | : 0 |
| EAP-Logoff        | While Authenticating |     | : 0 |
| Successful        | Authentication       |     | : 0 |
| Failed            | Authentication       |     | : 0 |
| Re-Authentication |                      |     | : 0 |
| Successful        | Re-Authentication    |     | : 0 |
| Failed            | Re-Authentication    |     | : 0 |
| EAP-Start         | When Authenticated   |     | : 0 |
| EAP-Logoff        | When Authenticated   |     | : 0 |
| Re-Auths          | When Authenticated   |     | : 0 |
| Cached            | Re-Authentication    |     | : 0 |
show aaa authentication port-accessdot1xauthenticator interface port-statistics
Syntax
show aaa authentication port-access dot1x authenticator interface {all|<IF-NAME>} port-
statistics
Description
Showsinformationabout802.1Xports.Theoutputcanbefilteredbyinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
all
Specifiesallinterfaces.
<IF-NAME>
Specifiestheinterfacename.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Portaccess|253

Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showinginformationforallports.
switch# show aaa authentication port-access dot1x authenticator interface all port-
statistics
Port 1/1/1
==========
Client Details
--------------
| Number | of Clients         |     |         | :   | 1   |
| ------ | ------------------ | --- | ------- | --- | --- |
| Number | of Authenticated   |     | Clients | :   | 1   |
| Number | of Unauthenticated |     | Clients | :   | 0   |
Statistics
----------
| EAPOL Frames   |          | Received        |                 |     | : 4 |
| -------------- | -------- | --------------- | --------------- | --- | --- |
| EAPOL Frames   |          | Transmitted     |                 |     | : 3 |
| EAPOL Start    |          | Frames Received |                 |     | : 1 |
| EAPOL Logoff   |          | Frames          | Received        |     | : 0 |
| EAPOL Response |          | ID Frames       | Received        |     | : 2 |
| EAPOL Response |          | Frames          | Received        |     | : 1 |
| EAPOL Request  |          | ID Frames       | Transmitted     |     | : 2 |
| EAPOL Request  |          | Frames          | Transmitted     |     | : 1 |
| EAPOL Invalid  |          | Frames          | Received        |     | : 0 |
| EAPOL EAP      | Length   | Error           | Frames Received |     | : 0 |
| EAPOL Last     | Received |                 | Frame Version   |     | : 0 |
| EAPOL Last     | Received |                 | Frame Client    | MAC | : 0 |
Port 1/1/2
==========
Client Details
--------------
| Number | of Clients         |     |         | :   | 1   |
| ------ | ------------------ | --- | ------- | --- | --- |
| Number | of Authenticated   |     | Clients | :   | 1   |
| Number | of Unauthenticated |     | Clients | :   | 0   |
Statistics
----------
| EAPOL Frames   |          | Received        |                 |     | : 4 |
| -------------- | -------- | --------------- | --------------- | --- | --- |
| EAPOL Frames   |          | Transmitted     |                 |     | : 3 |
| EAPOL Start    |          | Frames Received |                 |     | : 1 |
| EAPOL Logoff   |          | Frames          | Received        |     | : 0 |
| EAPOL Response |          | ID Frames       | Received        |     | : 2 |
| EAPOL Response |          | Frames          | Received        |     | : 1 |
| EAPOL Request  |          | ID Frames       | Transmitted     |     | : 2 |
| EAPOL Request  |          | Frames          | Transmitted     |     | : 1 |
| EAPOL Invalid  |          | Frames          | Received        |     | : 0 |
| EAPOL EAP      | Length   | Error           | Frames Received |     | : 0 |
| EAPOL Last     | Received |                 | Frame Version   |     | : 0 |
| EAPOL Last     | Received |                 | Frame Client    | MAC | : 0 |
| Port access    | MAC      | authentication  |                 |     |     |
MACauthenticationisdesignedtobeusedattheedgeofanetwork.Itprovidesport-basedsecurity
measuresforprotectingprivatenetworksandswitchesfromunauthorizedaccess.Becausethismethod
doesnotrequireclientstorunspecialsupplicantsoftware(unlike802.1Xauthentication),itissuitabletobe
usedinlegacysystems,IoTdevices,andtemporaryaccesssituationswhereintroducingsupplicantsoftware
isnotanattractiveoption.OnlyaMACaddressisrequiredforauthentication.
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 254

MAC authentication relies on a RADIUS server to authenticate clients. This technique simplifies access
security management by using a master database on a single server to control client access. Up to three
RADIUS servers can be used for backup in case access to the primary server fails. It also means that the
same credentials can be used for authentication, regardless of which switch or switch port is the current
access point into the LAN.

On a port configured for MAC authentication, the switch operates as a port-access authenticator using a
RADIUS server, and the Challenge-Handshake Authentication Protocol (CHAP) and Password Authentication
Protocol (PAP) protocols. Inbound traffic is processed by the switch alone, until authentication occurs.
Some traffic from the switch to an unauthorized client is supported (for example, broadcast or unknown
destination packets) before authentication occurs.

MAC authentication allows wireless clients to move between switch ports (for example, moving from one
access point to another) without having to reauthenticate.

In addition to using CLI and REST APIs to obtain authentication details of port-access clients, you can use SNMP
to obtain these details.

How MAC authentication works

MAC authentication grants access to a secure network by authenticating devices. When a device connects to
the switch, either by direct link or through the network, the switch forwards the device MAC address to the
RADIUS server for authentication. The RADIUS server uses the device MAC address as the user name and
password, and grants or denies network access in the same way that it does for clients capable of interactive
logons. The process does not use a client device configuration or a logon session. MAC authentication is well
suited for clients not capable of providing interactive logons, such as telephones, printers, and wireless
access points. Also, because most RADIUS servers allow for authentication to depend on the source switch
and port through which the client connects to the network, you can use MAC authentication to lock a
particular device to a specific switch and port.

802.1X port access and MAC authentication can be configured at the same time on a port. A total of 256 clients

can be configured per port and 16,384 clients on the entire switch, irrespective of the authentication method.

After the limit of 16,384 clients is reached, no additional authentication clients are allowed on any port for any

method. The default is one client.

MAC authentication, MAC lockout, and port security are mutually exclusive on a given port. If you configure any of

these authentication methods on a port, you must disable LACP on the port.

How RADIUS server is used in MAC authentication

MAC authentication uses a RADIUS server to temporarily assign a port to a static VLAN to support an
authenticated client. During client authentication, the switch port membership is determined according to
the following hierarchy:

n A RADIUS-assigned VLAN.

n A static, port-based, untagged VLAN to which the port is configured. A RADIUS-assigned VLAN has

priority over switch-port membership in any VLAN.

Port access MAC authentication commands

aaa authentication port-access mac-auth

Port access | 255

Syntax
| aaa authentication | port-access | mac-auth | {enable |     | | disable} |
| ------------------ | ----------- | -------- | ------- | --- | ---------- |
Description
EnablesordisablesMACauthenticationgloballyorattheport-level.
Commandcontext
config
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingMACauthenticationonallinterfaces:
| switch(config)#         | aaa authentication |        | port-access |     | mac-auth |
| ----------------------- | ------------------ | ------ | ----------- | --- | -------- |
| switch(config-macauth)# |                    | enable |             |     |          |
DisablingMACauthenticationonallinterfaces:
| switch(config)#         | aaa authentication |         | port-access |     | mac-auth |
| ----------------------- | ------------------ | ------- | ----------- | --- | -------- |
| switch(config-macauth)# |                    | disable |             |     |          |
EnablingMACauthenticationonaninterface:
| switch(config-if)#         | aaa authentication |        |     | port-access | mac-auth |
| -------------------------- | ------------------ | ------ | --- | ----------- | -------- |
| switch(config-if-macauth)# |                    | enable |     |             |          |
DisablingMACauthenticationonaninterface:
| switch(config-if)#         | aaa authentication  |         |     | port-access | mac-auth |
| -------------------------- | ------------------- | ------- | --- | ----------- | -------- |
| switch(config-if-macauth)# |                     | disable |     |             |          |
| aaa authentication         | port-accessmac-auth |         |     | addr-format |          |
Syntax
aaa authentication port-access mac-auth addr-format {no-delimiter | single-dash |
multi-dash |multi-colon | no-delimiter-uppercase | single-dash-uppercase |
| multi-dash-uppercase | |   | multi-colon-uppercase} |     |     |     |
| -------------------- | --- | ---------------------- | --- | --- | --- |
no aaa authentication port-access mac-auth addr-format {no-delimiter | single-dash |
multi-dash |multi-colon | no-delimiter-uppercase | single-dash-uppercase |
| multi-dash-uppercase |     | | multi-colon-uppercase} |     |     |     |
| -------------------- | --- | ------------------------ | --- | --- | --- |
Description
ConfigurestheMACaddressformatthattheswitchmustuseintheRADIUSrequestmessage.
ThenoformofthecommandresetstheMACaddressformattothedefault,no-delimiter.
Commandcontext
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 256

config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingtheMACaddressformatontheswitch:
| switch(config)# | aaa authentication |     |     | port-access | mac-auth |
| --------------- | ------------------ | --- | --- | ----------- | -------- |
switch(config-macauth)#
|     |     | addr-format |     | single-dash |     |
| --- | --- | ----------- | --- | ----------- | --- |
ResettingtheMACaddressformatontheswitchtoitsdefault:
| switch(config)#         | aaa authentication  |     |             | port-access | mac-auth |
| ----------------------- | ------------------- | --- | ----------- | ----------- | -------- |
| switch(config-macauth)# |                     | no  | addr-format |             |          |
| aaa authentication      | port-accessmac-auth |     |             | auth-method |          |
Syntax
| aaa authentication    | port-access |     | mac-auth | auth-method | {chap | pap} |
| --------------------- | ----------- | --- | -------- | ----------- | ------------ |
| no aaa authentication | port-access |     | mac-auth | auth-method |              |
Description
ConfigurestheRADIUSauthenticationmethodforMACauthentication.
FollowingaretheMACauthenticationmethodssupported:
CHAP
n
PAP
n
ThePEAP-MSCHAPv2methodofauthenticationisnotsupported.
Thenoformofthecommandresetstheauthenticationmethodtothedefault,chap.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringtheRADIUSauthenticationmethodontheswitch:
| switch# config |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
switch(config)#
|                         | aaa authentication |             |     | port-access | mac-auth |
| ----------------------- | ------------------ | ----------- | --- | ----------- | -------- |
| switch(config-macauth)# |                    | auth-method |     | pap         |          |
ResettingtheRADIUSauthenticationmethodontheswitch:
Portaccess|257

switch(config)# no aaa authentication port-access mac-auth auth-method
| aaa authentication | port-accessmac-auth |     | cached-reauth |     |
| ------------------ | ------------------- | --- | ------------- | --- |
Syntax
| aaa authentication    | port-access | mac-auth | cached-reauth |     |
| --------------------- | ----------- | -------- | ------------- | --- |
| no aaa authentication | port-access | mac-auth | cached-reauth |     |
Description
Enablescachedreauthenticationonaport.CachedreauthenticationallowsMACreauthenticationsto
succeedwhentheRADIUSserverisunavailable.Userswhoarealreadyauthenticated,retaintheircurrently
assignedRADIUSattributes.
Thenoformofthecommanddisablescachedreauthentication.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingcachedreauthenticationonaport:
| switch(config-if)#         | aaa authentication |               | port-access | mac-auth |
| -------------------------- | ------------------ | ------------- | ----------- | -------- |
| switch(config-if-macauth)# |                    | cached-reauth |             |          |
Disablingcachedreauthenticationonaport:
| switch(config-if)#         | aaa authentication  |                  | port-access          | mac-auth |
| -------------------------- | ------------------- | ---------------- | -------------------- | -------- |
| switch(config-if-macauth)# |                     | no cached-reauth |                      |          |
| aaa authentication         | port-accessmac-auth |                  | cached-reauth-period |          |
Syntax
aaa authentication port-access mac-auth cached-reauth-period <PERIOD>
| no aaa authentication | port-access | mac-auth | cached-reauth-period |     |
| --------------------- | ----------- | -------- | -------------------- | --- |
Description
Configurestheperiodduringwhichanauthenticatedclient,whichhasfailedtoreauthenticatebecausethe
RADIUSserverisunreachable,remainsauthenticated.
Thenoformofthecommandresetsthecachedreauthenticationperiodtothedefault,30seconds.
Commandcontext
config-if
Parameters
<PERIOD>
Specifiesthecachedreauthenticationperiod(inseconds).Default:30.Range:30to86400.
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 258

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringcachedreauthenticationperiodonaport:
| switch(config-if)#         | aaa authentication |                      | port-access | mac-auth |
| -------------------------- | ------------------ | -------------------- | ----------- | -------- |
| switch(config-if-macauth)# |                    | cached-reauth-period |             | 300      |
Resettingthecachedreauthenticationperiodtothedefaultvalue:
| switch(config-if)#         | aaa authentication  |                         | port-access  | mac-auth |
| -------------------------- | ------------------- | ----------------------- | ------------ | -------- |
| switch(config-if-macauth)# |                     | no cached-reauth-period |              |          |
| aaa authentication         | port-accessmac-auth |                         | quiet-period |          |
Syntax
| aaa authentication    | port-access | mac-auth | quiet-period | <PERIOD> |
| --------------------- | ----------- | -------- | ------------ | -------- |
| no aaa authentication | port-access | mac-auth | quiet-period |          |
Description
Configurestheperiodduringwhichtheswitchdoesnottrytoauthenticatearejectedclient.
Thenoformofthecommandresetsthequietperiodtothedefault,60seconds.
Commandcontext
config-if
Parameters
<PERIOD>
Specifiesthequietperiod(inseconds).Default:60.Range:0to65535.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringthequietperiodonaport:
switch(config-if)#
|                            | aaa authentication |              | port-access | mac-auth |
| -------------------------- | ------------------ | ------------ | ----------- | -------- |
| switch(config-if-macauth)# |                    | quiet-period | 65          |          |
Resettingthequietperiodonaporttodefault:
| switch(config-if)#         | aaa authentication  |                 | port-access        | mac-auth |
| -------------------------- | ------------------- | --------------- | ------------------ | -------- |
| switch(config-if-macauth)# |                     | no quiet-period |                    |          |
| aaa authentication         | port-accessmac-auth |                 | radiusserver-group |          |
Syntax
Portaccess|259

aaa authentication port-access mac-auth radius server-group <GROUP-NAME>
| no aaa authentication | port-access |     | mac-auth | radius |     | server-group |
| --------------------- | ----------- | --- | -------- | ------ | --- | ------------ |
Description
ConfigurestheMACauthenticationservergroup.
Thenoformofthecommandresetstheauthenticationservergrouptothedefaultvalue,radius.
Commandcontext
config
Parameters
<GROUP-NAME>
SpecifiestheMACauthenticationservergroupname.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringtheMACauthenticationservergroup:
| switch# config          |                     |        |              |             |        |          |
| ----------------------- | ------------------- | ------ | ------------ | ----------- | ------ | -------- |
| switch(config)#         | aaa authentication  |        |              | port-access |        | mac-auth |
| switch(config-macauth)# |                     | radius | server-group |             | group1 |          |
| aaa authentication      | port-accessmac-auth |        |              |             | reauth |          |
Syntax
| aaa authentication    | port-access |     | mac-auth | reauth |     |     |
| --------------------- | ----------- | --- | -------- | ------ | --- | --- |
| no aaa authentication | port-access |     | mac-auth | reauth |     |     |
Description
EnablesperiodicMACreauthenticationofauthenticatedclientsontheport.
ThenoformofthecommanddisablesperiodicMACreauthenticationontheport.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingreauthenticationonaport:
| switch(config-if)#         | aaa | authentication |        | port-access |     | mac-auth |
| -------------------------- | --- | -------------- | ------ | ----------- | --- | -------- |
| switch(config-if-macauth)# |     |                | reauth |             |     |          |
Disablingreauthenticationonaport:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 260

| switch(config-if)# |     |     | aaa authentication |     |     | port-access | mac-auth |
| ------------------ | --- | --- | ------------------ | --- | --- | ----------- | -------- |
switch(config-if-macauth)#
|                    |     |                     |     | no  | reauth |               |     |
| ------------------ | --- | ------------------- | --- | --- | ------ | ------------- | --- |
| aaa authentication |     | port-accessmac-auth |     |     |        | reauth-period |     |
Syntax
| aaa authentication    |     | port-access |     | mac-auth | reauth-period |               | <PERIOD> |
| --------------------- | --- | ----------- | --- | -------- | ------------- | ------------- | -------- |
| no aaa authentication |     | port-access |     |          | mac-auth      | reauth-period |          |
Description
ConfigurestheperiodafterwhichMACauthenticatedclientsmustbereauthenticatedontheport.You
mustfirstenableMACreauthenticationontheportbeforeconfiguringtheMACreauthenticationperiod.
ThenoformofthecommandresetstheMACreauthenticationperiodtothedefault,3600seconds.
Commandcontext
config-if
Parameters
<PERIOD>
SpecifiestheMACreauthenticationperiod(inseconds).Default:3600.Range:1to65535.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringtheMACreauthenticationperiodonaport:
| switch(config-if)#         |     |     | aaa authentication |               |     | port-access | mac-auth |
| -------------------------- | --- | --- | ------------------ | ------------- | --- | ----------- | -------- |
| switch(config-if-macauth)# |     |     |                    | reauth-period |     | 60          |          |
ResettingtheMACreauthenticationperiodtoitsdefault:
| switch(config-if)#         |            |     | aaa authentication |     |               | port-access | mac-auth |
| -------------------------- | ---------- | --- | ------------------ | --- | ------------- | ----------- | -------- |
| switch(config-if-macauth)# |            |     |                    | no  | reauth-period |             |          |
| clear mac-auth             | statistics |     |                    |     |               |             |          |
Syntax
| clear mac-auth | statistics |     | [interface |     | <IF-NAME>] |     |     |
| -------------- | ---------- | --- | ---------- | --- | ---------- | --- | --- |
Description
ClearstheMACauthenticationstatisticsassociatedwiththeportandalltheauthenticatorstatemachines
associatedtothisport.
Ifnointerfaceisspecified,thestatisticsisclearedforallMACauthenticationenabledports.
Commandcontext
Operator(>)orManager(#)
Parameters
Portaccess|261

<IF-NAME>

Specifies the interface name.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Clearing MAC authentication statistics on a port (6200 and 6300 Switch Series):

switch# clear mac-auth statistics interface 1/1/1

Clearing MAC authentication statistics on a port (6400 Switch Series):

switch# clear mac-auth statistics interface 1/3/1

Clearing MAC authentication statistics on all ports:

switch# clear mac-auth statistics

show aaa authentication port-access mac-auth interface client-status

Syntax

show aaa authentication port-access mac-auth interface {all|<IF-NAME>}

client-status [mac <MAC-ADDRESS>]

Description

Shows information about MAC authentication clients status. The output can be filtered by interface or MAC
address.

Command context

Operator (>) or Manager (#)

Parameters

all

Specifies all interfaces.

<IF-NAME>

Specifies the interface name.

<MAC-ADDRESS>

Specifies the client MAC address.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

On the 6400 Switch Series, interface identification differs.

Showing client status information for all ports:

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

262

switch# show aaa authentication port-access mac-auth interface all client-status
| Port   | Access             | Client | Status Details |     |     |     |
| ------ | ------------------ | ------ | -------------- | --- | --- | --- |
| Client | AB:CD:DE:FF:AA:BB, |        | 1/1/1          |     |     |     |
=========================================
| Authentication |     | Details |     |     |     |     |
| -------------- | --- | ------- | --- | --- | --- | --- |
----------------------
| Status         |       |            |              |     | : Authenticated |     |
| -------------- | ----- | ---------- | ------------ | --- | --------------- | --- |
| Type           |       |            |              |     | : Pass-Through  |     |
| Auth-Method    |       |            |              |     | : CHAP          |     |
| Time           | Since | Last       | State Change |     | : 10 secs       |     |
| Authentication |       | Statistics |              |     |                 |     |
-------------------------
|                   | Authentication     |                   |               |     | : 1 |     |
| ----------------- | ------------------ | ----------------- | ------------- | --- | --- | --- |
| Authentication    |                    | Timeout           |               | : 0 |     |     |
| Successful        |                    | Authentication    |               | : 1 |     |     |
| Failed            | Authentication     |                   |               | : 0 |     |     |
| Re-Authentication |                    |                   |               | : 0 |     |     |
| Successful        |                    | Re-Authentication |               | : 0 |     |     |
| Failed            | Re-Authentication  |                   |               | : 0 |     |     |
|                   | Re-Auths           | When              | Authenticated |     | : 0 |     |
| Cached            | Re-Authentication  |                   |               | : 0 |     |     |
| Client            | DD:CD:AB:CS:EE:OI, |                   | 1/1/2         |     |     |     |
=========================================
| Authentication |     | Details |     |     |     |     |
| -------------- | --- | ------- | --- | --- | --- | --- |
----------------------
| Status         |         |            |              |     | : Unauthenticated |                |
| -------------- | ------- | ---------- | ------------ | --- | ----------------- | -------------- |
| Type           |         |            |              |     | : Pass-Through    |                |
| Auth-Method    |         |            |              |     | : CHAP            |                |
| Auth           | Failure | reason     |              |     | : Server reject/  | Server timeout |
| Time           | Since   | Last       | State Change |     | : 15 secs         |                |
| Authentication |         | Statistics |              |     |                   |                |
-------------------------
| Authentication    |                   |                    |     | : 1 |     |     |
| ----------------- | ----------------- | ------------------ | --- | --- | --- | --- |
| Authentication    |                   | Timeout            |     | : 0 |     |     |
| Successful        |                   | Authentication     |     | : 0 |     |     |
| Failed            | Authentication    |                    |     | : 1 |     |     |
| Re-Authentication |                   |                    |     | : 0 |     |     |
| Successful        |                   | Re-Authentication  |     | : 0 |     |     |
| Failed            | Re-Authentication |                    |     | : 0 |     |     |
| Re-Auths          |                   | When Authenticated |     | : 0 |     |     |
| Cached            | Re-Authentication |                    |     | : 0 |     |     |
Showingstatusinformationforaclient:
switch# show aaa authentication port-access mac-auth interface 1/1/1 client-status
mac ab:cd:de:ff:aa:bb
| Port   | Access             | Client | Status Details |     |     |     |
| ------ | ------------------ | ------ | -------------- | --- | --- | --- |
| Client | AB:CD:DE:FF:AA:BB, |        | 1/1/1          |     |     |     |
=========================================
| Authentication |     | Details |     |     |     |     |
| -------------- | --- | ------- | --- | --- | --- | --- |
----------------------
| Status      |     |     |     |     | : Authenticated |     |
| ----------- | --- | --- | --- | --- | --------------- | --- |
| Type        |     |     |     |     | : Pass-Through  |     |
| Auth-Method |     |     |     |     | : CHAP          |     |
Portaccess|263

Time Since Last State Change

: 10 secs

Authentication Statistics
-------------------------
Authentication

Authentication Timeout
: 0
Successful Authentication
: 1
Failed Authentication
: 0
: 0
Re-Authentication
Successful Re-Authentication : 0
: 0
Failed Re-Authentication

: 1

Re-Auths When Authenticated

: 0

Cached Re-Authentication

: 0

show aaa authentication port-access mac-auth interface port-statistics

Syntax

show aaa authentication port-access mac-auth interface {all|<IF-NAME>} port-statistics

Description

Shows information about MAC authentication ports. The output can be filtered by interface.

Command context

Operator (>) or Manager (#)

Parameters

all

Specifies all interfaces.

<IF-NAME>

Specifies the interface name.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

On the 6400 Switch Series, interface identification differs.

Showing information for all ports.

switch# show aaa authentication port-access mac-auth interface all port-statistics

Port 1/1/1
==========

Client Details
--------------

: 3
Number of Clients
Number of authenticated clients
: 2
Number of unauthenticated clients : 1
Number of authenticating clients : 0

Port 1/1/2
==========

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

264

|     | Client Details |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
--------------
|      | Number | of Clients         |     |         | : 4 |     |
| ---- | ------ | ------------------ | --- | ------- | --- | --- |
|      | Number | of authenticated   |     | clients | : 2 |     |
|      | Number | of unauthenticated |     | clients | : 2 |     |
|      | Number | of authenticating  |     | clients | : 0 |     |
| Port | access | policy             |     |         |     |     |
Portaccesspolicyallowsnetworkadministratorstodefineasetofrules.Theserulesareusedtorestrictor
alterthepassageoftrafficforclientsonboardingtoaswitchthathasportsecurity(802.1X,MAC
authentication)enabled.
Unlikeclassifierpolicies,whichareassociatedwithindividualfrontplaneport,LinkAggregationGroup(LAG),
andVLANortunnelinterface,port-accesspoliciesareassociatedwithroles.Basedontheroleassociated
withauserafterauthentication,thepolicyisappliedtotheuser.
Theswitchcanobtainpoliciesfromanyofthefollowingsources:
n Local:Policiesconfiguredlocallyontheswitch.
Downloaded:PoliciesdownloadedfromaClearPassPolicyManagerserver.
n
RADIUS:PoliciesconfiguredusingtheNAS-Filter-RuleorAruba-NAS-Filter-RuleRADIUSattributes.
n
Bothlocalanddownloadedtypeofpoliciesdonothaveanystandardsassociatedwiththem.Policiesthatare
obtainedfromtheRADIUSservermustsupportallcriteriathatcanbedefinedusingtheNAS-Filter-Rule
attribute.
| Classes | and | actions | supported |     | by port | access policies |
| ------- | --- | ------- | --------- | --- | ------- | --------------- |
PortaccesspoliciessupportIPv4-andIPv6-basedclasses,andthefollowingactions.
n cir:Setthebandwidthlimitforguaranteedtraffic.
n drop:Dropthepacket.
n dscp:Remarkthe6-bitfieldintheIPheaderforpacketclassification.
n ip-precedence:Remarkthe3-bitfieldintheIPheaderwhichdenotesthepriorityofthedatagram.
local-priority:Changetheinternalprioritythatisusedtoqueuethepacketsfortransmission.
n
redirect:Redirectthepacketstoaspecifieddestination(captiveportalserver).
n
| Port | access | policy | commands |     |     |     |
| ---- | ------ | ------ | -------- | --- | --- | --- |
port-accesspolicy
Syntax
| port-access | policy | <POLICY-NAME> |     |     |     |     |
| ----------- | ------ | ------------- | --- | --- | --- | --- |
[<SEQUENCE-NUMBER>]
| class | {ip|ipv6}                | <CLASS-NAME> |     |                    |     |                    |
| ----- | ------------------------ | ------------ | --- | ------------------ | --- | ------------------ |
|       | action {<REMARK-ACTIONS> |              |     | | <POLICE-ACTIONS> |     | | <OTHER-ACTIONS>} |
[<SEQUENCE-NUMBER>]
| comment | ... |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- |
Portaccess|265

Description

Creates or modifies policy and policy entries. A policy is made up of one or more policy entries ordered and
prioritized by sequence numbers. Each entry has an IPv4/IPv6 class and one or more policy actions
associated with it.

A policy must be applied to a role using the associate policy command.

The no form of the command can be used to delete either a policy (use no with the policy command) or an
individual policy entry (use no with the sequence number).

Command context

config

The policy command takes you into the config-pa-policy context where you enter the policy entries.

Parameters

<POLICY-NAME>

Specifies the name of the policy.

<SEQUENCE-NUMBER>

Specifies a sequence number for the policy entry. Optional. Range: 1 to 4294967295.

comment

Specifies the description of an entry in the policy. Optional.

class {ip|ipv6} <CLASS-NAME>

Specifies a type of class, ip for IPv4 and ipv6 for IPv6 policy. And specifies a class name.

<REMARK-ACTIONS>

Remark actions can be any of the following options: {ip-precedence <IP-PRECEDENCE-VALUE> | dscp
<DSCP-VALUE> | local-priority <LOCAL-PRIORITY-VALUE>} where:
ip-precedence <IP-PRECEDENCE-VALUE>

Specifies the numeric IP precedence value. Range: 0 to 7.

dscp <DSCP-VALUE>

Specifies a Differentiated Services Code Point (DSCP) value. Enter either a numeric value (0 to 63) or a
keyword as follows:

Keyword

Status

Syntax

Description

AF11

AF12

AF13

AF21

AF22

AF23

AF31

Optional

Keyword

DSCP 10 (Assured Forwarding Class 1, low drop probability)

Optional

Keyword

DSCP 12 (Assured Forwarding Class 1, medium drop

probability)

Optional

Keyword

DSCP 14 (Assured Forwarding Class 1, high drop probability)

Optional

Keyword

DSCP 18 (Assured Forwarding Class 2, low drop probability)

Optional

Keyword

DSCP 20 (Assured Forwarding Class 2, medium drop

probability)

Optional

Keyword

DSCP 22 (Assured Forwarding Class 2, high drop probability)

Optional

Keyword

DSCP 26 (Assured Forwarding Class 3, low drop probability)

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

266

| Keyword | Status | Syntax | Description |
| ------- | ------ | ------ | ----------- |
AF32
|     | Optional | Keyword | DSCP28(AssuredForwardingClass3,mediumdrop |
| --- | -------- | ------- | ----------------------------------------- |
probability)
AF33
Optional Keyword DSCP30(AssuredForwardingClass3,highdropprobability)
AF41
Optional Keyword DSCP34(AssuredForwardingClass4,lowdropprobability)
AF42
|     | Optional | Keyword | DSCP36(AssuredForwardingClass4,mediumdrop |
| --- | -------- | ------- | ----------------------------------------- |
probability)
AF43
Optional Keyword DSCP38(AssuredForwardingClass4,highdropprobability)
CS0
|     | Optional | Keyword | DSCP0(ClassSelector0:Default) |
| --- | -------- | ------- | ----------------------------- |
CS1
|     | Optional | Keyword | DSCP8(ClassSelector1:Scavenger)       |
| --- | -------- | ------- | ------------------------------------- |
| CS2 | Optional | Keyword | DSCP16(ClassSelector2:OAM)            |
| CS3 | Optional | Keyword | DSCP24(ClassSelector3:Signaling)      |
| CS4 | Optional | Keyword | DSCP32(ClassSelector4:Realtime)       |
| CS5 | Optional | Keyword | DSCP40(ClassSelector5:Broadcastvideo) |
| CS6 | Optional | Keyword | DSCP48(ClassSelector6:Networkcontrol) |
CS7
|     | Optional | Keyword | DSCP56(ClassSelector7) |
| --- | -------- | ------- | ---------------------- |
EF
|                | Optional               | Keyword | DSCP46(ExpeditedForwarding) |
| -------------- | ---------------------- | ------- | --------------------------- |
| local-priority | <LOCAL-PRIORITY-VALUE> |         |                             |
Specifiesalocalpriorityvalue.Range:0to7.
<POLICE-ACTIONS>
Policeactionscanbethefollowing{cir kbps <RATE-BPS>cbs<BYTES> exceed}
where:
| cir kbps | <RATE-BPS> |     |     |
| -------- | ---------- | --- | --- |
SpecifiesaCommittedInformationRate(CIR)valueinKilobitspersecond.Range:1to4294967295.
cbs<BYTES>
SpecifiesaCommittedBurstSize(CBS)valueinbytes.Range:1to4294967295.
exceed
Specifiesactiontotakeonpacketsthatexceedtheratelimit.
<OTHER-ACTIONS>
Otheractionscanbethefollowing:
drop
Specifiesdroptraffic.
redirect
Specifiesredirectalltraffictoacaptiveportalserver.
Portaccess|267

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
n Anappliedpolicyprocessesthepacketsequentiallyagainstpolicyandclassentriesinthelist,untileither
thelastpolicyentryinthelisthasbeenevaluatedorthepacketmatchesanentry.Ifthereisnomatch,
thepacketwillbedroppedbyoneoftheimplicitdeny allIPv4andIPv6entries.
Enteringanexisting<POLICY-NAME>valuewillcausetheexistingpolicytobemodified,withanynew
n
<SEQUENCE-NUMBER>valuecreatinganadditionalpolicyentry,andanyexisting<SEQUENCE-NUMBER>value
replacingtheexistingpolicyentrywiththesamesequencenumber.
n Ifnosequencenumberisspecified,anewpolicyentrywillbeappendedtotheendoftheentrylistwitha
sequencenumberequaltothehighestpolicyentrycurrentlyinthelistplus10.Thesequencenumbers
maybereorderedwiththeport-access policy <POLICY-NAME> resequence <STARTING-SEQ-NUM>
<INCREMENT>command.
Ifapolicyisconfiguredwithoutanyaction,thedefaultaction,permit,isappliedforthatpolicy.
n
Examples
Creatingapolicywithseveralclassentries:
| switch(config)#           | port-access | policy   | POL1    |     |     |
| ------------------------- | ----------- | -------- | ------- | --- | --- |
| switch(config-pa-policy)# |             | 10 class | ip dns  |     |     |
| switch(config-pa-policy)# |             | 20 class | ip dhcp |     |     |
switch(config-pa-policy)# 30 class ip test action cir kbps 1024 exceed drop
| switch(config-pa-policy)# |     | exit |     |     |     |
| ------------------------- | --- | ---- | --- | --- | --- |
switch(config)#
|               | show port-access | policy | POL1 |     |     |
| ------------- | ---------------- | ------ | ---- | --- | --- |
| Access Policy | Details:         |        |      |     |     |
======================
| Policy Name   | : POL1    |     |             |     |     |
| ------------- | --------- | --- | ----------- | --- | --- |
| Policy Type   | : Local   |     |             |     |     |
| Policy Status | : Applied |     |             |     |     |
| SEQUENCE      | CLASS     |     | TYPE ACTION |     |     |
----------- --------------------------- ---- ----------------------------------
| 10  | dns  |     | ipv4 permit   |             |      |
| --- | ---- | --- | ------------- | ----------- | ---- |
| 20  | dhcp |     | ipv4 permit   |             |      |
| 30  | test |     | ipv4 cir kbps | 1024 exceed | drop |
Addingacommenttoanexistingclassentry:
| switch(config)#           | port-access    | policy      | POL1             |     |     |
| ------------------------- | -------------- | ----------- | ---------------- | --- | --- |
| switch(config-pa-policy)# |                | 20 comment  | DHCP-PERMIT      |     |     |
| switch(config-pa-policy)# |                | exit        |                  |     |     |
| switch(config)#           | show run       | port-access | policy POL1      |     |     |
| port-access               | policy POL1    |             |                  |     |     |
| 10 class                  | ip dns         |             |                  |     |     |
| 20 class                  | ip dhcp        |             |                  |     |     |
| 20 comment                | DHCP-PERMIT    |             |                  |     |     |
| 30 class                  | ip test action | cir kbps    | 1024 exceed drop |     |     |
Removingacommentfromanexistingclassentry:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 268

| switch(config)# |     | port-access | policy |     | POL1 |     |     |     |
| --------------- | --- | ----------- | ------ | --- | ---- | --- | --- | --- |
switch(config-pa-policy)#
no 20 comment
| switch(config-pa-policy)# |          |                | exit        |      |             |      |     |     |
| ------------------------- | -------- | -------------- | ----------- | ---- | ----------- | ---- | --- | --- |
| switch(config)#           |          | show run       | port-access |      | policy POL1 |      |     |     |
| port-access               |          | policy POL1    |             |      |             |      |     |     |
|                           | 10 class | ip dns         |             |      |             |      |     |     |
|                           | 20 class | ip dhcp        |             |      |             |      |     |     |
|                           | 30 class | ip test action | cir         | kbps | 1024 exceed | drop |     |     |
Modifyingapolicybyreplacingoneclasswithanotheratthesamesequencenumber:
switch(config)#
|                           |        | port-access      | policy   |        | POL1          |      |      |     |
| ------------------------- | ------ | ---------------- | -------- | ------ | ------------- | ---- | ---- | --- |
| switch(config-pa-policy)# |        |                  | 10 class |        | ip mds action | dscp | af21 |     |
| switch(config-pa-policy)# |        |                  | exit     |        |               |      |      |     |
| switch(config)#           |        | show port-access |          | policy | POL1          |      |      |     |
| Access                    | Policy | Details:         |          |        |               |      |      |     |
======================
| Policy   | Name   | : POL1    |     |     |      |        |     |     |
| -------- | ------ | --------- | --- | --- | ---- | ------ | --- | --- |
| Policy   | Type   | : Local   |     |     |      |        |     |     |
| Policy   | Status | : Applied |     |     |      |        |     |     |
| SEQUENCE |        | CLASS     |     |     | TYPE | ACTION |     |     |
----------- ---------------------------- ---- ----------------------------------
| 10  |     | mds  |     |     | ipv4 | dscp AF21 |             |      |
| --- | --- | ---- | --- | --- | ---- | --------- | ----------- | ---- |
| 20  |     | dhcp |     |     | ipv4 | permit    |             |      |
| 30  |     | test |     |     | ipv4 | cir kbps  | 1024 exceed | drop |
Removingaclass:
| switch(config)# |     | port-access | policy |     | POL1 |     |     |     |
| --------------- | --- | ----------- | ------ | --- | ---- | --- | --- | --- |
switch(config-pa-policy)#
no 10
| switch(config-pa-policy)# |        |                  | exit |        |      |     |     |     |
| ------------------------- | ------ | ---------------- | ---- | ------ | ---- | --- | --- | --- |
| switch(config)#           |        | show port-access |      | policy | POL1 |     |     |     |
| Access                    | Policy | Details:         |      |        |      |     |     |     |
======================
| Policy   | Name   | : POL1    |     |     |      |        |     |     |
| -------- | ------ | --------- | --- | --- | ---- | ------ | --- | --- |
| Policy   | Type   | : Local   |     |     |      |        |     |     |
| Policy   | Status | : Applied |     |     |      |        |     |     |
| SEQUENCE |        | CLASS     |     |     | TYPE | ACTION |     |     |
----------- ---------------------------- ---- ----------------------------------
| 20  |     | dhcp          |     |     | ipv4 | permit   |             |      |
| --- | --- | ------------- | --- | --- | ---- | -------- | ----------- | ---- |
| 30  |     | clearpass-web |     |     | ipv4 | cir kbps | 1024 exceed | drop |
port-accesspolicycopy
Syntax
| port-access |     | policy <POLICY-NAME> |     | copy | <DESTINATION-POLICY> |     |     |     |
| ----------- | --- | -------------------- | --- | ---- | -------------------- | --- | --- | --- |
Description
Copiesdetailsofanexistingpolicytoanewpolicy.Copyingapolicycopiesallitsentriesaswell.
Commandcontext
Portaccess|269

config
Parameters
<POLICY-NAME>
Specifiestheexistingpolicyname.
<DESTINATION-POLICY>
Specifiesthedestinationpolicyname.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Copyingapolicy:
| switch(config)# | port-access      | policy POL1 | copy POL1_copy |     |     |
| --------------- | ---------------- | ----------- | -------------- | --- | --- |
| switch(config)# | show port-access | policy      |                |     |     |
| Access Policy   | Details:         |             |                |     |     |
======================
| Policy Name   | : POL1    |     |             |     |     |
| ------------- | --------- | --- | ----------- | --- | --- |
| Policy Type   | : Local   |     |             |     |     |
| Policy Status | : Applied |     |             |     |     |
| SEQUENCE      | CLASS     |     | TYPE ACTION |     |     |
----------- --------------------------- ---- ----------------------------------
| 20            | dhcp        |     | ipv4 permit   |             |      |
| ------------- | ----------- | --- | ------------- | ----------- | ---- |
| 30            | test        |     | ipv4 cir kbps | 1024 exceed | drop |
| Policy Name   | : POL1_copy |     |               |             |      |
| Policy Type   | : Local     |     |               |             |      |
| Policy Status | : Applied   |     |               |             |      |
| SEQUENCE      | CLASS       |     | TYPE ACTION   |             |      |
----------- --------------------------- ---- ----------------------------------
| 20  | dhcp |     | ipv4 permit   |             |      |
| --- | ---- | --- | ------------- | ----------- | ---- |
| 30  | test |     | ipv4 cir kbps | 1024 exceed | drop |
port-accesspolicyresequence
Syntax
port-access policy <POLICY-NAME> resequence <STARTING-SEQ-NUM> <INCREMENT>
Description
Resequencesnumberinginapolicy.
Commandcontext
config
Parameters
<POLICY-NAME>
Specifiesthepolicywhereyouwanttoresequencepolicyentries.
<STARTING-SEQ-NUM>
Specifiesthesequencenumbertostartresequencingfrom.Range:1-4294967295.
<INCREMENT>
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 270

Specifieshowmuchtoincrementthesequencenumbersby.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Resequencingapolicystartingat5withanincrementof10:
| switch(config)# | port-access      | policy | POL1 resequence | 5 10 |     |
| --------------- | ---------------- | ------ | --------------- | ---- | --- |
| switch(config)# | show port-access | policy | POL1            |      |     |
| Access          | Policy Details:  |        |                 |      |     |
======================
| Policy   | Name : POL1      |     |             |     |     |
| -------- | ---------------- | --- | ----------- | --- | --- |
| Policy   | Type : Local     |     |             |     |     |
| Policy   | Status : Applied |     |             |     |     |
| SEQUENCE | CLASS            |     | TYPE ACTION |     |     |
----------- --------------------------- ---- ----------------------------------
| 5   | dhcp |     | ipv4 permit |                  |      |
| --- | ---- | --- | ----------- | ---------------- | ---- |
| 15  | test |     | ipv4 cir    | kbps 1024 exceed | drop |
port-accesspolicyreset
Syntax
| port-access | policy <POLICY-NAME> | reset |     |     |     |
| ----------- | -------------------- | ----- | --- | --- | --- |
Description
Resetsthepolicyconfigurationtomatchthecurrenthardwareconfigurationofthepolicy.
Commandcontext
config
Parameters
<POLICY-NAME>
Specifiesthenameofthepolicytobereset.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Resettingapolicy:
| switch(config)#           | port-access | policy   | POL2    |     |     |
| ------------------------- | ----------- | -------- | ------- | --- | --- |
| switch(config-pa-policy)# |             | 20 class | ip dhcp |     |     |
switch(config-pa-policy)# 40 class test2 action cir kbps 1024 exceed drop
| switch(config-pa-policy)# |                  | exit   |         |     |     |
| ------------------------- | ---------------- | ------ | ------- | --- | --- |
| switch(config)#           | show port-access | policy | POL1-V2 |     |     |
| Access                    | Policy Details:  |        |         |     |     |
======================
Portaccess|271

| Policy   | Name   | : POL2    |     |     |      |        |     |     |
| -------- | ------ | --------- | --- | --- | ---- | ------ | --- | --- |
| Policy   | Type   | : Local   |     |     |      |        |     |     |
| Policy   | Status | : Applied |     |     |      |        |     |     |
| SEQUENCE | CLASS  |           |     |     | TYPE | ACTION |     |     |
----------- ---------------------------- ---- ----------------------------------
| 20              | dhcp  |             |        |       | ipv4 | permit   |             |      |
| --------------- | ----- | ----------- | ------ | ----- | ---- | -------- | ----------- | ---- |
| 40              | test2 |             |        |       | ipv4 | cir kbps | 1024 exceed | drop |
| switch(config)# |       | port-access | policy | POLV2 |      |          |             |      |
switch(config-pa-policy)# 50 class ip test3 action cir kbps 1024 exceed drop
switch(config-pa-policy)#
no 20
| switch(config-pa-policy)# |        |          | exit        |        |      |     |     |     |
| ------------------------- | ------ | -------- | ----------- | ------ | ---- | --- | --- | --- |
| switch(config)#           |        | show     | port-access | policy | POL2 |     |     |     |
| Access                    | Policy | Details: |             |        |      |     |     |     |
======================
| Policy   | Name   | : POL2     |     |     |      |        |     |     |
| -------- | ------ | ---------- | --- | --- | ---- | ------ | --- | --- |
| Policy   | Type   | : Local    |     |     |      |        |     |     |
| Policy   | Status | : Rejected |     |     |      |        |     |     |
| SEQUENCE | CLASS  |            |     |     | TYPE | ACTION |     |     |
----------- ---------------------------- ---- ----------------------------------
| 40              | test2   |             |             |             | ipv4  | cir kbps | 1024 exceed | drop |
| --------------- | ------- | ----------- | ----------- | ----------- | ----- | -------- | ----------- | ---- |
| 50              | test3   |             |             |             | ipv4  | cir kbps | 1024 exceed | drop |
| switch(config)# |         | port-access | policy      | POK2        | reset |          |             |      |
| Following       | policy  | entries     | will        | be removed: |       |          |             |      |
| class ip        | test3   | action      | cir kbps    | 1024 exceed |       | drop     |             |      |
| Following       | policy  | entries     | will        | be added:   |       |          |             |      |
| 20 class        | ip dhcp |             |             |             |       |          |             |      |
| Do you          | want to | continue    | (y/n)?      | y           |       |          |             |      |
| switch(config)# |         | show        | port-access | policy      | POL2  |          |             |      |
| Access          | Policy  | Details:    |             |             |       |          |             |      |
======================
| Policy   | Name   | : POL1-V2 |     |     |      |        |     |     |
| -------- | ------ | --------- | --- | --- | ---- | ------ | --- | --- |
| Policy   | Type   | : Local   |     |     |      |        |     |     |
| Policy   | Status | : Applied |     |     |      |        |     |     |
| SEQUENCE | CLASS  |           |     |     | TYPE | ACTION |     |     |
----------- ---------------------------- ---- ----------------------------------
| 20  | dhcp  |     |     |     | ipv4 | permit   |             |      |
| --- | ----- | --- | --- | --- | ---- | -------- | ----------- | ---- |
| 40  | test2 |     |     |     | ipv4 | cir kbps | 1024 exceed | drop |
clear port-accesspolicyhitcounts
Syntax
| clear port-access |     | policy | <POLICY-NAME> | hitcounts |     | {port | | client} |     |
| ----------------- | --- | ------ | ------------- | --------- | --- | ----- | --------- | --- |
Description
Clearsstatisticsandconformrateofpolicyappliedonaportorclient.
Commandcontext
Operator(>)orManager(#)
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 272

Parameters
<POLICY-NAME>
Specifiesthepolicyname.
port
Clearsthepolicystatisticsmatchingpolicynameintheportmode.
client
Clearsthepolicystatisticsmatchingpolicynameintheclientmode.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Clearingpolicyhitcounts:
| switch# show | port-access | policy     | POL6     | hitcounts | port |     |     |
| ------------ | ----------- | ---------- | -------- | --------- | ---- | --- | --- |
| Port Access  | Policy      | Hit-Counts | Details: |           |      |     |     |
======================================
| Policy Name   | : POL4    |     |             |     |     |     |                |
| ------------- | --------- | --- | ----------- | --- | --- | --- | -------------- |
| Policy Type   | : Local   |     |             |     |     |     |                |
| Policy Status | : Applied |     |             |     |     |     |                |
| SEQUENCE      | CLASS     |     | TYPE ACTION |     |     |     | CUR-RATE(kbps) |
-------- ----------------- ---- --------------------------------- --------------
| 3          | test8       |     | ipv4 cir | kbps 1024 | exceed drop |     | 512       |
| ---------- | ----------- | --- | -------- | --------- | ----------- | --- | --------- |
| Class Name | : dhcp      |     |          |           |             |     |           |
| Class Type | : ipv4      |     |          |           |             |     |           |
| SEQUENCE   | CLASS-ENTRY |     |          |           |             |     | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 10         | match icmp      | any | any count |     |     |     | 0         |
| ---------- | --------------- | --- | --------- | --- | --- | --- | --------- |
| Class Name | : clearpass-web |     |           |     |     |     |           |
| Class Type | : ipv4          |     |           |     |     |     |           |
| SEQUENCE   | CLASS-ENTRY     |     |           |     |     |     | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 15         | match udp     | any any | count |     |     |     | 15101830  |
| ---------- | ------------- | ------- | ----- | --- | --- | --- | --------- |
| Class Name | : web-traffic |         |       |     |     |     |           |
| Class Type | : ipv4        |         |       |     |     |     |           |
| SEQUENCE   | CLASS-ENTRY   |         |       |     |     |     | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 10         | match any   | any any  | count    |      |            |     | 241       |
| ---------- | ----------- | -------- | -------- | ---- | ---------- | --- | --------- |
| 20         | match any   | 10.1.1.1 | 10.1.1.2 | dscp | AF11 count |     | 50        |
| Class Name | : class6    |          |          |      |            |     |           |
| Class Type | : ipv6      |          |          |      |            |     |           |
| SEQUENCE   | CLASS-ENTRY |          |          |      |            |     | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 10  | match any    | any any         | count |                 |     |           | 173 |
| --- | ------------ | --------------- | ----- | --------------- | --- | --------- | --- |
| 20  | match icmpv6 | 2001:db8:a::123 |       | 2001:db8:a::125 |     | dscp AF11 |     |
|     | count        |                 |       |                 |     |           | 32  |
Portaccess|273

switch#
switch#
|     | clear | port-access |     | policy POL6 | hitcounts | port |     |     |
| --- | ----- | ----------- | --- | ----------- | --------- | ---- | --- | --- |
switch#
| switch# | show   | port-access |            | policy POL6 | hitcounts | port |     |     |
| ------- | ------ | ----------- | ---------- | ----------- | --------- | ---- | --- | --- |
| Port    | Access | Policy      | Hit-Counts | Details:    |           |      |     |     |
======================================
| Policy   | Name   | : POL4    |     |             |     |     |     |                |
| -------- | ------ | --------- | --- | ----------- | --- | --- | --- | -------------- |
| Policy   | Type   | : Local   |     |             |     |     |     |                |
| Policy   | Status | : Applied |     |             |     |     |     |                |
| SEQUENCE | CLASS  |           |     | TYPE ACTION |     |     |     | CUR-RATE(kbps) |
-------- ----------------- ---- --------------------------------- --------------
| 3        | test8 |             |     | ipv4 cir | kbps 1024 | exceed | drop | 512       |
| -------- | ----- | ----------- | --- | -------- | --------- | ------ | ---- | --------- |
| Class    | Name  | : dhcp      |     |          |           |        |      |           |
| Class    | Type  | : ipv4      |     |          |           |        |      |           |
| SEQUENCE |       | CLASS-ENTRY |     |          |           |        |      | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 10       |      | match icmp      | any | any count |     |     |     | 0         |
| -------- | ---- | --------------- | --- | --------- | --- | --- | --- | --------- |
| Class    | Name | : clearpass-web |     |           |     |     |     |           |
| Class    | Type | : ipv4          |     |           |     |     |     |           |
| SEQUENCE |      | CLASS-ENTRY     |     |           |     |     |     | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 15       |      | match udp     | any | any count |     |     |     | 0         |
| -------- | ---- | ------------- | --- | --------- | --- | --- | --- | --------- |
| Class    | Name | : web-traffic |     |           |     |     |     |           |
| Class    | Type | : ipv4        |     |           |     |     |     |           |
| SEQUENCE |      | CLASS-ENTRY   |     |           |     |     |     | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 10       |      | match any   | any      | any count |      |      |       | 0         |
| -------- | ---- | ----------- | -------- | --------- | ---- | ---- | ----- | --------- |
| 20       |      | match any   | 10.1.1.1 | 10.1.1.2  | dscp | AF11 | count | 0         |
| Class    | Name | : class6    |          |           |      |      |       |           |
| Class    | Type | : ipv6      |          |           |      |      |       |           |
| SEQUENCE |      | CLASS-ENTRY |          |           |      |      |       | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 10  |     | match any    | any | any count       |                 |     |           | 0   |
| --- | --- | ------------ | --- | --------------- | --------------- | --- | --------- | --- |
| 20  |     | match icmpv6 |     | 2001:db8:a::123 | 2001:db8:a::125 |     | dscp AF11 |     |
|     |     | count        |     |                 |                 |     |           | 0   |
show port-accesspolicy
Syntax
| show port-access |     | policy | [<POLICY-NAME>] |     |     |     |     |     |
| ---------------- | --- | ------ | --------------- | --- | --- | --- | --- | --- |
Description
Showsvariousaspectsofpoliciesandtheircurrentusage.Detailsofapolicyincludingthecontentofa
specificpolicyisshown.
Followingarethepossiblevaluesforpolicytypes:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 274

Local—Userconfiguredpolicy
n
Downloaded—Downloadeduserpolicy
n
RADIUS—PolicyobtainedfromtheRADIUSserver
n
Followingarethepossiblevaluesforpolicystatus:
Applied—Policyissuccessfullyappliedinthehardware.
n
n Rejected—Policyisnotsupportedinthehardware.
n In-Progress—Policyisbeingprocessedinthehardware.
n Failed—DisplayedwhentheswitchfailstoapplythepolicyconfigurationbecausetheTCAMresources
areunavailableorfull.
Ifapolicyisconfiguredwithoutanyaction,theshowcommandwillrepresentsuchanentrywiththeactionas
permit.
Commandcontext
Operator(>)orManager(#)
Parameters
<POLICY-NAME>
Specifiesthepolicyname.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showinginformationforallpolicies:
switch(config)#
|               | show port-access policy |     |     |     |
| ------------- | ----------------------- | --- | --- | --- |
| Access Policy | Details:                |     |     |     |
======================
| Policy Name   | : POL1    |             |     |     |
| ------------- | --------- | ----------- | --- | --- |
| Policy Type   | : Local   |             |     |     |
| Policy Status | : Applied |             |     |     |
| SEQUENCE      | CLASS     | TYPE ACTION |     |     |
----------- --------------------------- ---- ----------------------------------
| 20            | dhcp        | ipv4 permit   |             |      |
| ------------- | ----------- | ------------- | ----------- | ---- |
| 30            | test        | ipv4 cir kbps | 1024 exceed | drop |
| Policy Name   | : POL1_copy |               |             |      |
| Policy Type   | : Local     |               |             |      |
| Policy Status | : Applied   |               |             |      |
| SEQUENCE      | CLASS       | TYPE ACTION   |             |      |
----------- --------------------------- ---- ----------------------------------
| 20  | dhcp | ipv4 permit   |             |      |
| --- | ---- | ------------- | ----------- | ---- |
| 30  | test | ipv4 cir kbps | 1024 exceed | drop |
Showinginformationforaparticularpolicy:
Portaccess|275

| switch(config)# | show port-access |     | policy | POL1 |     |     |     |
| --------------- | ---------------- | --- | ------ | ---- | --- | --- | --- |
| Access Policy   | Details:         |     |        |      |     |     |     |
======================
| Policy Name   | : POL1    |     |     |      |        |     |     |
| ------------- | --------- | --- | --- | ---- | ------ | --- | --- |
| Policy Type   | : Local   |     |     |      |        |     |     |
| Policy Status | : Applied |     |     |      |        |     |     |
| SEQUENCE      | CLASS     |     |     | TYPE | ACTION |     |     |
----------- --------------------------- ---- ----------------------------------
| 20  | dhcp |     |     | ipv4 | permit   |             |      |
| --- | ---- | --- | --- | ---- | -------- | ----------- | ---- |
| 30  | test |     |     | ipv4 | cir kbps | 1024 exceed | drop |
show port-accesspolicyhitcounts
Syntax
Syntaxthatshowsstatisticalinformationintheformofhitcounts:
| show port-access | policy <POLICY-NAME> |     |     | hitcounts | {port | | client} |     |
| ---------------- | -------------------- | --- | --- | --------- | ----- | --------- | --- |
Description
Showsthestatisticsandthecurrentrateofpolicyappliedontheportortheclient.
Commandcontext
Operator(>)orManager(#)
Parameters
<POLICY-NAME>
Specifiesthepolicyname.
port
Showspolicystatisticsmatchingthepolicynameintheportmode.
client
Showspolicystatisticsmatchingthepolicynameintheclientmode.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showingpolicyhitcounts(statistics)withcurrentrate:
| switch# show | port-access       | policy | POL6     | hitcounts | port |     |     |
| ------------ | ----------------- | ------ | -------- | --------- | ---- | --- | --- |
| Port Access  | Policy Hit-Counts |        | Details: |           |      |     |     |
======================================
| Policy Name   | : POL1    |     |             |     |     |     |                |
| ------------- | --------- | --- | ----------- | --- | --- | --- | -------------- |
| Policy Type   | : Local   |     |             |     |     |     |                |
| Policy Status | : Applied |     |             |     |     |     |                |
| SEQUENCE      | CLASS     |     | TYPE ACTION |     |     |     | CUR-RATE(kbps) |
-------- ----------------- ---- --------------------------------- --------------
| 30  | test8 |     | ipv4 cir | kbps | 1024 exceed | drop | 512 |
| --- | ----- | --- | -------- | ---- | ----------- | ---- | --- |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 276

| Class Name | : dhcp      |     |     |     |           |
| ---------- | ----------- | --- | --- | --- | --------- |
| Class Type | : ipv4      |     |     |     |           |
| SEQUENCE   | CLASS-ENTRY |     |     |     | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 10         | match icmp      | any any count |     |     | 982150    |
| ---------- | --------------- | ------------- | --- | --- | --------- |
| Class Name | : clearpass-web |               |     |     |           |
| Class Type | : ipv4          |               |     |     |           |
| SEQUENCE   | CLASS-ENTRY     |               |     |     | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 70         | match udp     | any any count |     |     | 15101830  |
| ---------- | ------------- | ------------- | --- | --- | --------- |
| Class Name | : web-traffic |               |     |     |           |
| Class Type | : ipv4        |               |     |     |           |
| SEQUENCE   | CLASS-ENTRY   |               |     |     | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 4          | match any   | any any count     |           |       | 3194      |
| ---------- | ----------- | ----------------- | --------- | ----- | --------- |
| 5          | match any   | 10.1.1.1 10.1.1.2 | dscp AF11 | count | 1716      |
| Class Name | : class6    |                   |           |       |           |
| Class Type | : ipv6      |                   |           |       |           |
| SEQUENCE   | CLASS-ENTRY |                   |           |       | HIT-COUNT |
----------- ------------------------------------------------------- -----------
| 10          | match any    | any any count   |                 |           | 0   |
| ----------- | ------------ | --------------- | --------------- | --------- | --- |
| 20          | match icmpv6 | 2001:db8:a::123 | 2001:db8:a::125 | dscp AF11 |     |
|             | count        |                 |                 |           | 0   |
| Port access | role         |                 |                 |           |     |
Everydevicethatconnectstoaportisassociatedwitharole.Rolesareassociatedwithallclients,both
authenticatedandunauthenticated,andappliedtoeachusersession.Bydefault,rolesareenabledona
switch.
Followingareafewexamplesofuserrolenamesandtheaccessprivilegesthatcanbeconfigured:
n Employee—Providecompleteaccesstonetworkresources.
n Contractor—Providelimitedaccesstonetworkresources.
n Guest—ProvideonlyInternetbrowsingaccess.
Eachuserroledeterminestheclientnetworkprivileges,frequencyofreauthentication,applicablebandwidth
contracts,andotherpermissions.
ActiveuserrolesappliedonclientsarecreatedonlyonTernaryContent-AddressableMemory(TCAM)resource
availabilityoftheswitch.
Auserroleconsistsofthefollowingoptionalparameters:
| n Ingress user | policy |     |     |     |     |
| -------------- | ------ | --- | --- | --- | --- |
L3(IPv4and/orIPv6)orderedlistofclasseswithactions.
n captive-portal-profile
Assignsacaptiveportalprofileforthisrole.
Portaccess|277

n inactivity-timeout

The inactivity timeout period in seconds with a range of 300 to 4294967295 for the authenticated
client for an implicit logoff.

n reauth-period

Sets the reauthentication period in seconds or 0 to disable.

n vlan access

Sets the untagged VLAN ID.

n vlan trunk

Sets the tagged VLAN ID.

n auth-mode

Sets the configuration in user role to either device-mode or port-mode. The following are the attributes:
o

poe-priority

Specifies the PoE priority for the interface.
o

mtu

Configures the MTU support for the client.
o

vlan trunk allowed

Specifies the list of tagged VLANs configured for the interface.
o

trust-mode

Configures the QoS trust mode for the client.

Operational notes

Following are some of the operational notes to be considered for port access roles:

n On the 6200 Switch Series, a maximum of 4096 authenticated clients are supported.

n On the 6300, 6400 Switch Series, a maximum of 4096 authenticated clients are supported.

n When roles are enabled, they are applied to all devices connected to ports where authentication is

configured.

n Special roles, such as, critical, reject, pre-auth, and auth are applied depending on the authentication state

of the device.

n Roles can be applied in one of the following two ways:

o Vendor-Specific Attribute (VSA)-Derived Role

Type: RADIUS: Aruba

Name: Aruba-User-Role

ID: 25

Value: <myUserRole>

See Vendor-Specific Attributes supported in session authorization.

The RADIUS server (ClearPass Policy Manager server) determines how the VSA-Derived Role is applied to
the user. The role is sent to the switch through a RADIUS VSA. The VSA derived role will have the same
precedence order as the authentication type (802.1x, MAC authentication).

o User Derived Role (UDR)

The UDR is applied when the roles are enabled.

UDR will have the same precedence order as the authentication type (802.1x, MAC authentication).

Downloadable user roles

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

278

Downloadable user roles enable AOS-CX switches to download user roles, policy, and class from the
ClearPass Policy Manager server. The download facilitates the configuration of policies and attributes for a
specific user role which can then be stored locally on the switch. New users can then be assigned the same
locally stored version of the user role in ClearPass Policy Manager server, enabling the administrator to save
time in reconfiguring each user individually.

The command radius-server host WORD clearpass-username WORD clearpass-password (plaintext |
ciphertext) can only be used if the user role is going to be downloaded from the ClearPass Policy Manager
server.

Special roles

Special roles are always local roles that are created to support instances when the deployments are not yet
complete. They are also helpful when any network issues occur during authentication of devices. Special
roles are always purpose-based, that is, they are applied only in instances such as the RADIUS server is not
reachable for authentication or when a single role has to be applied across all switches.

The following special roles are available:

n Critical role

n Reject role

n Pre-authentication role

n Auth-role

n Fallback role

Critical role

The critical role is applied to devices when the RADIUS server is unreachable during the first authentication
process or during reauthentication. This role helps ensure that the devices have limited access to the
network even though the authentication is not completed. Once the RADIUS server is available for
authentication, the devices are authenticated and the ultimate role is applied.

Reject role

The reject role is applied when the RADIUS server rejects a device during authentication. The reject role gives
restricted access to the device compared to a full access role.

Pre-authentication role

The pre-authentication (pre-auth) role allows a device, such as an IP phone, to have network access before
the device is authenticated. The pre-auth role is triggered when a MAC-based client is connected to a switch
before being authenticated by the RADIUS server. Devices must be assigned a VLAN to provide network
connectivity. Two new VLANs are created for pre-auth role functionality, one for voice traffic and one for
data traffic. Pre-auth role VLANs can be configured on the switch individually or within a user-role. Devices
that can be connected to the switch without authentication are divided into two categories:

n Devices that send voice traffic.

n Devices that send data traffic.

Either one of pre-auth role VLANs (voice and/or data) or a pre-auth role can be configured for a port. However,

both a VLAN and role cannot coexist for an interface. Initial traffic on the port is restricted only by Access Control

Lists (ACLs) configured for the port or for VLANs or ACLs in the role.

Impact of pre-auth role on existing features

Port access | 279

Unauthenticated devices

Configuring pre-auth role VLAN will change the behavior of unauthenticated devices. Normally,
authentication-enabled ports will not provide unauthenticated client any network access until the device
is authenticated by the RADIUS server. With pre-auth role VLAN configured, the client will be assigned to
the pre-auth role VLAN until the RADIUS server authenticates the device.

Unauthenticated clients will be placed into the VLAN specified in the pre-auth role. After authenticated
by the RADIUS server, the client will be placed into the VLAN specified in the RADIUS authentication
command string or as specified in the RADIUS authentication accept string.

LLDP-bypass

When LLDP-bypass is enabled on the switch, Aruba APs are not authenticated. Therefore pre-auth role
VLAN is not applicable.

Bypass using device-identity

Pre-auth role VLAN is not applicable to VoIP devices because they do not need authentication. It is
applicable to PCs that need authentication.

ACLs applied on an interface

If an ACL rule is applied on an interface, which is part of a pre-auth role VLAN, traffic coming through that
interface will be affected. Traffic will be affected based on the rule in the ACL.

ACLs applied on a VLAN

If an ACL rule is applied on a pre-auth role VLAN, traffic entering that VLAN will be affected. Traffic will be
affected based on the rule in the ACL.

Rate-limiting on an interface

If the traffic is rate-limited on an interface as part of a pre-auth role VLAN, the traffic will be impacted.
The traffic will be affected based on the rule in the rate-limiting configuration command.

Authenticated or rejected clients

Clients that are authenticated or rejected by the RADIUS server are given different VLANs. These clients
are moved from pre-auth role to new VLANs based on the authentication by the RADIUS server.

MAC pinning

Clients whose MAC addresses are pinned and have undergone authentication will always be treated as
authenticated. Pre-auth role VLAN is not applicable in this scenario.

Effect of RADIUS tracking on pre-auth role

If RADIUS tracking is enabled and no RADIUS server is available for authentication, the port will be
changed from a pre-auth role VLAN to a critical VLAN. The time taken to move from pre-auth role VLAN
to critical VLAN depends on the time it takes for RADIUS tracker to inform the subsystem.

Restrictions

The pre-auth role restrictions are as follows:

n It will not support more than one tagged or untagged VLAN membership either through direct VLAN

configuration or through user-roles.

n It is not applicable for authentication methods other than MAC-based.

n It is not available to be configured from WebUI, Menu, or REST.

Auth-role

After the RADIUS server authenticates a device, if no role is configured on the server, it sends an empty
access accept packet to the switch. The switch translates this empty packet to assign an auth-role to the
device. The switch then checks if an auth-role is configured on that port and assigns this role to the device.

Fallback role

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

280

Thefallbackroleisappliedtoonboardingdeviceswhenthereisnoderivedroleavailableforthedevices.
Followingaretheconditionsforthefallbackroletobeappliedononboardingdevices:
n ThedeviceprofilelocalMACmatchfeaturewithblock-until-profile-appliedmodeisconfigured.
DeviceprofilealongwithAAAisconfiguredbutnomatchwasfoundforthedeviceprofileclient.
n
AAAmethodwithnorejectorcriticalroleisconfigured,andtheconnectiontoRADIUSserverfailed.
n
n 802.1Xauthenticationisenabledontheport,butthesupplicantofthedevicetimedouttorespondto
theauthenticationrequest.
| Port      | access                 | role commands |     |     |     |
| --------- | ---------------------- | ------------- | --- | --- | --- |
| associate | captive-portal-profile |               |     |     |     |
Syntax
| associate    | captive-portal-profile |     |     | <PROFILE-NAME> |     |
| ------------ | ---------------------- | --- | --- | -------------- | --- |
| no associate | captive-portal-profile |     |     | <PROFILE-NAME> |     |
Description
Associatesthecaptiveportalprofilewiththecurrentrole.
Thenoformofthiscommanddissociatesthecaptiveportalprofilewiththerole.
Commandcontext
config-pa-role
Theport-access rolecommandtakesyouintotheconfig-pa-rolecontext.
Parameters
<PROFILE-NAME>
Specifiesthecaptiveportalprofilenametoassociatewiththecurrentrole.
Theprofilemustbepresentintheswitchbeforeassociatingitwitharole.Length:1to64characters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Associatingacaptiveportalprofilewitharole:
| switch(config)#         |     | port-access | role      | role01                 |        |
| ----------------------- | --- | ----------- | --------- | ---------------------- | ------ |
| switch(config-pa-role)# |     |             | associate | captive-portal-profile | prof01 |
Dissociatingacaptiveportalprofilefromtherole:
| switch(config-pa-role)# |        |     | no associate | captive-portal-profile |     |
| ----------------------- | ------ | --- | ------------ | ---------------------- | --- |
| associate               | policy |     |              |                        |     |
Syntax
| associate    | policy | <POLICY-NAME> |     |     |     |
| ------------ | ------ | ------------- | --- | --- | --- |
| no associate | policy | <POLICY-NAME> |     |     |     |
Portaccess|281

Description

Associates the policy with the current role.

The no form of this command dissociates the policy from the role.

Command context

config-pa-role

The port-access role command takes you into the config-pa-role context.

Parameters

<POLICY-NAME>

Specifies the policy name to associate with the current role. The maximum number of characters allowed
is 64.

Only those policies created by using the port-access policy command are allowed to be associated with a
role.

Policies created using the policy command are not allowed to be associated with a role.

Policies that are of the downloaded type are not allowed to be associated with a role.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Associating a policy with a role:

switch(config)# port-access role role01
switch(config-pa-role)# associate policy policy01

Dissociating a policy from the role:

switch(config-pa-role)# no associate policy poilcy01

auth-mode

Syntax

auth-mode {client-mode | device-mode}

Description

Configures the authentication mode for the clients that are associated with the current role.

Command context

config

The port-access role command takes you into the config-pa-role context.

Parameters

client-mode

Selects client mode. In this mode, all clients connecting to the port are sent for authentication.

device-mode

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

282

Selects device mode. In this mode, only the first client connecting to the port is sent for authentication.
Once this client is authenticated, the port is considered as open and all subsequent clients trying to
connect on that port are not sent for authentication.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the client authentication mode:

switch(config-pa-role)# auth-mode client-mode

cached-reauth-period

Syntax

cached-reauth-period [<PERIOD>]
no cached-reauth-period

Description

Enables cached reauthentication, setting the period after which clients that associated with the current role
must be reauthenticated.

The no form of this command disables cached authentication.

Command context

config-pa-role

The port-access role command takes you into the config-pa-role context.

Parameters

<PERIOD>

Specifies the cached reauthentication period (in seconds) for clients associated with the role. Default:
None. Range: 30 to 4294967295 .

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling cached reauthentication and setting its period to 200 seconds:

switch(config-pa-role)# cached-reauth-period 200

Disabling cached reauthentication:

switch(config-pa-role)# no cached-reauth-period

client-inactivity timeout

Syntax

client-inactivity timeout {<CLIENT-INACTIVITY-PERIOD> | none}

Port access | 283

no client-inactivity timeout

Description

Configures the period that the switch waits for a response from a client after which it removes the client
from the role.

The no form of the command resets the timeout period to the default.

Command context

config-pa-role

The port-access role command takes you into the config-pa-role context.

Parameters

<CLIENT-INACTIVITY-PERIOD>

Specifies the client inactivity time (in seconds). Default: 300. Range: 300 to 4294967295.

none

Specifies that the client must not be deleted because of inactivity.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring client inactivity timer for a role:

switch(config-pa-role)# client-inactivity timeout 3600

description

Syntax

description <ROLE-DESCRIPTION>

Description

Configures the role description.

Command context

config-pa-role

The port-access role command takes you into the config-pa-role context.

Parameters

<ROLE-DESCRIPTION>

Specifies the role description. Up to 255 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the role description:

switch(config-pa-role)# description student role

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

284

gateway-zone zone gateway-role

Syntax

gateway-zone zone <ZONE-NAME> gateway-role <GATEWAY-ROLE-NAME>

Description

Configures the per-role gateway zone details needed for user-based tunneling (UBT). For information on
UBT, see the Fundamentals Guide.

Command context

config-pa-role

The port-access role command takes you into the config-pa-role context.

Parameters

<ZONE-NAME>

Specifies the role gateway zone name.

<GATEWAY-ROLE-NAME>

Specifies the gateway role name. The gateway role must already exist.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring role gateway zone details:

switch(config-pa-role)# gateway-zone zone zone1 gateway-role role1

mtu

Syntax

mtu <MTU-SIZE>

Description

Configures the MTU size of a client for a role.

Command context

config-pa-role

The port-access role command takes you into the config-pa-role context.

Parameters

<MTU-SIZE>

Specifies the MTU size in bytes of a client for a role. Range: 68 to 9198.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring client MTU size:

Port access | 285

| switch(config-pa-role)# |     | mtu | 9198 |     |
| ----------------------- | --- | --- | ---- | --- |
poe-priority
Syntax
| poe-priority | {critical | | high | | low} |     |
| ------------ | --------- | ------ | ------ | --- |
no poe-priority
Description
Configuresthepowerdistributionpriorityfortheportaccessroles.Highpowerconsumptioncanbe
preventedusingpoe-prioritycontrolmechanism.
Thenoformofthiscommandrestoresthepowerdistributiontoitsdefaultpriority.
Commandcontext
config-pa-role
Theport-access rolecommandtakesyouintotheconfig-pa-rolecontext.
Parameters
critical
Specifiescriticalpriority.
high
Specifieshighpriority.
low
Specifieslowpriority.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringPoEpriorityforanewrole:
| switch(config)#         |     | port-access  | role role01 |          |
| ----------------------- | --- | ------------ | ----------- | -------- |
| switch(config-pa-role)# |     | poe-priority |             | critical |
ResettingPoEpriorityfortheroletoitsdefault:
| switch(config)#         |     | port-access | role role01  |     |
| ----------------------- | --- | ----------- | ------------ | --- |
| switch(config-pa-role)# |     | no          | poe-priority |     |
port-accessrole
Syntax
| port-access    | role <ROLE-NAME> |             |     |     |
| -------------- | ---------------- | ----------- | --- | --- |
| no port-access | role             | <ROLE-NAME> |     |     |
Description
Createsanewportaccessroleormodifiesanexistingrole.Thiscommandtakesyouintotheconfig-pa-
rolecontext.Amaximumof32portaccessrolescanbecreated.
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 286

The no form of this command deletes a role.

Command context

config

Parameters

<ROLE-NAME>

Specifies the role name. The maximum number of characters allowed is 64.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating a new role:

switch(config)# port-access role basic01

reauth-period

Syntax

reauth-period <PERIOD>
no reauth-period

Description

Configures the period after which clients that associated with the current role must be reauthenticated.

The reauthentication period configured here takes precedence over the reauthentication period configured at the

port level.

Command context

config-pa-role

The port-access role command takes you into the config-pa-role context.

Parameters

<PERIOD>

Specifies the reauthentication period (in seconds) for clients associated with the role. Default: None.
Range: 1 to 86400.

Reauthentication period of less than 60 seconds is not recommended.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring reauthentication period:

switch(config-pa-role)# reauth-period 3000

Port access | 287

session timeout

Syntax

session-timeout <SESSION-TIMEOUT>
no session-timeout

Description

Configures the session timeout for the role. After the timeout period, the session will be disconnected.

Command context

config-pa-role

The port-access role command takes you into the config-pa-role context.

Parameters

<SESSION-TIMEOUT>

Specifies the session timeout (in seconds). Range: 1 to 4294967295.

A session timeout period of less than 60 seconds is not recommended.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring session timeout for a role:

switch(config-pa-role)# session timeout 3600

show aaa authentication port-access interface client-status

Syntax

show aaa authentication port-access interface {all | <IF-NAME>}
client-status [mac <MAC-ADDRESS>]

Description

Shows information about the status of the role applied on ports.

Command context

Operator (>) or Manager (#)

Parameters

all

Specifies all interfaces.

<IF-NAME>

Specifies the instance name.

<MAC-ADDRESS>

Specifies the client MAC address.

Authority

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

288

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showinginformationaboutaclient:
switch# show aaa authentication port-access interface all client-status mac
00:00:00:00:00:01
| Port Access | Client Status | Details |
| ----------- | ------------- | ------- |
Client 00:00:00:00:00:01
============================
| Session | Details |     |
| ------- | ------- | --- |
---------------
| Port           | : 1/7/24    |     |
| -------------- | ----------- | --- |
| Session        | Time : 151s |     |
| Authentication | Details     |     |
----------------------
| Status | : mac-auth | Authenticated |
| ------ | ---------- | ------------- |
Auth Precedence : mac-auth - Authenticated, dot1x - Not attempted
| Authorization | Details |     |
| ------------- | ------- | --- |
----------------------
| Role   | : UserRole_1 |     |
| ------ | ------------ | --- |
| Status | : Applied    |     |
show port-accessrole
Syntax
show port-access role {local | clearpass|radius | name <ROLE-NAME>}
Description
Showsinformationaboutrolesconfiguredlocally,ordownloadedfromClearPassPolicyManagerand
RADIUSserver.
Commandcontext
Operator(>)orManager(#)
Parameters
local
Showsinformationaboutlocallyconfiguredroles.
clearpass
ShowsinformationaboutrolesdownloadedfromClearPassPolicyManager.
radius
ShowsinformationaboutrolesdownloadedfromtheRADIUSserver.
<ROLE-NAME>
Specifiestherolename.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Portaccess|289

Examples
Showinglocallyconfiguredroleinformation:
switch#
| show | port-access |     | role local |     |     |     |
| ---- | ----------- | --- | ---------- | --- | --- | --- |
Role Information
| Name : | local_role_01 |     |     |     |     |     |
| ------ | ------------- | --- | --- | --- | --- | --- |
| Type : | local         |     |     |     |     |     |
----------------------------------------------
| Reauthentication     |            |        | Period    |      | : 333 secs |     |
| -------------------- | ---------- | ------ | --------- | ---- | ---------- | --- |
| Authentication       |            | Mode   |           |      | :          |     |
| Session              | Timeout    |        |           |      | :          |     |
| Client               | Inactivity |        | Timeout   |      | :          |     |
| Tunneled             | Node       | Server | Zone      |      | :          |     |
| Tunneled             | Node       | Server | Secondary | Role | :          |     |
| Access               | VLAN       |        |           |      | :          |     |
| Native               | VLAN       |        |           |      | :          |     |
| Allowed              | Trunk      | VLANs  |           |      | :          |     |
| MTU                  |            |        |           |      | :          |     |
| QoS Trust            | Mode       |        |           |      | :          |     |
| PoE Priority         |            |        |           |      | : low      |     |
| CaptivePortalProfile |            |        | :         |      |            |     |
| Policy               |            |        |           |      | :          |     |
ShowinginformationforrolesdownloadedfromClearPassPolicyManager:
| switch# show | port-access |     | role clearpass |     |     |     |
| ------------ | ----------- | --- | -------------- | --- | --- | --- |
Role Information:
| Name : CP_GIRI_DUR_GUEST_ROLE-3058-7 |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- |
| Type : clearpass                     |     |     |     |     |     |     |
| Status: Completed                    |     |     |     |     |     |     |
----------------------------------------------
| Reauthentication   |            |         | Period    |     | : 300 secs                          |              |
| ------------------ | ---------- | ------- | --------- | --- | ----------------------------------- | ------------ |
| Authentication     |            | Mode    |           |     | :                                   |              |
| Session            | Timeout    |         |           |     | : 1000000                           | secs         |
| Client             | Inactivity |         | Timeout   |     | :                                   |              |
| Description        |            |         |           |     | : Guest                             | role for CP6 |
| Gateway            | Zone       |         |           |     | :                                   |              |
| UBT Gateway        |            | Role    |           |     | :                                   |              |
| Access             | VLAN       |         |           |     | : 20                                |              |
| Native             | VLAN       |         |           |     | :                                   |              |
| Allowed            | Trunk      | VLANs   |           |     | :                                   |              |
| Access             | VLAN       | Name    |           |     | : vlan20                            |              |
| Native             | VLAN       | Name    |           |     | :                                   |              |
| Allowed            | Trunk      | VLAN    | Names     |     | :                                   |              |
| MTU                |            |         |           |     | :                                   |              |
| QOS Trust          | Mode       |         |           |     | :                                   |              |
| STP Administrative |            |         | Edge Port |     | : true                              |              |
| PoE Priority       |            |         |           |     | :                                   |              |
| Captive            | Portal     | Profile |           |     | : CP6_CP_GIRI_DUR_GUEST_ROLE-3058-7 |              |
| Policy             |            |         |           |     | : CP6_CP_GIRI_DUR_GUEST_ROLE-3058-7 |              |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 290

ShowinginformationforrolesdownloadedfromaRADIUSserver:
| switch# show | port-access |     | role radius |     |     |
| ------------ | ----------- | --- | ----------- | --- | --- |
Role Information
| Name : | RADIUS_21963402 |     |     |     |     |
| ------ | --------------- | --- | --- | --- | --- |
| Type : | radius          |     |     |     |     |
----------------------------------------------
| Reauthentication     |            | Period |                      |      | : 333 secs            |
| -------------------- | ---------- | ------ | -------------------- | ---- | --------------------- |
| Authentication       |            | Mode   |                      |      | :                     |
| Session              | Timeout    |        |                      |      | :                     |
| Client               | Inactivity |        | Timeout              |      | :                     |
| Tunneled             | Node       | Server | Zone                 |      | :                     |
| Tunneled             | Node       | Server | Secondary            | Role | :                     |
| Access               | VLAN       |        |                      |      | : 10                  |
| Native               | VLAN       |        |                      |      | :                     |
| Allowed              | Trunk      | VLANs  |                      |      | :                     |
| MTU                  |            |        |                      |      | :                     |
| QoS Trust            | Mode       |        |                      |      | :                     |
| PoE Priority         |            |        |                      |      | : low                 |
| CaptivePortalProfile |            |        | :testcpprof_29451201 |      |                       |
| Policy               |            |        |                      |      | : PERMIT-ALL_87364653 |
stp-admin-edge-port
Syntax
stp-admin-edge-port
no stp-admin-edge-port
Description
Configurestheportasaspanningtreeadministrativeedgeportfortherole.Thisconfigurationremovesthe
portparticipationfromSTPinteractionswhenonboardingdevices.Thisinturnhelpsinfasteronboardingof
devices.
ThenoformofthecommanddisablesSTPedgeportfunctionality.
IftheportreceivesSTPBPDUontheSTPadministrativeedgeconfiguredport,theportwillmovetotheSTPstate.
YoumustconfiguretheportasanSTPadministrativeedgeportonlyifyouaresurethattheconnecteddevicewill
notparticipateinSTPinteractions.
Commandcontext
config-pa-role
Theport-access rolecommandtakesyouintotheconfig-pa-rolecontext.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ConfiguringSTPedgeportforarole:
| switch(config)#         |     | port-access | role                | role01 |     |
| ----------------------- | --- | ----------- | ------------------- | ------ | --- |
| switch(config-pa-role)# |     |             | stp-admin-edge-port |        |     |
Portaccess|291

trust-mode

Syntax

trust-mode [dscp | cos | none]
no trust-mode

Description

Configures QoS trust mode for the role.

The no form of this command configures the default trust mode for the role.

Command context

config-pa-role

The port-access role command takes you into the config-pa-role context.

Parameters

dscp

Specifies to trust DSCP and preserve the 802.1p priority.

cos

Specifies to trust 802.1p priority and retain DSCP or IP-ToS.

none

Specifies to not trust any priority fields.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring DSCP trust mode for a role:

switch(config)# port-access role role01
switch(config-pa-role)# trust-mode dscp

vlan

Syntax

vlan {access | trunk native | trunk allowed} <VLAN-ID>
no vlan {access | trunk native | trunk allowed} <VLAN-ID>

Or
vlan {access name | trunk native name | trunk allowed name} <VLAN-NAME>
no vlan {access name | trunk native name | trunk allowed name} [<VLAN-NAME>]

Description

Configures VLAN IDs or VLAN names, and VLAN modes for a port access role. You can configure either VLAN
IDs or VLAN names, or a combination of both for a role.

The no form of the command deletes the VLAN configuration from the role. For trunk allowed VLAN names,
you can delete the VLAN names individually or all names at once.

Command context

config-pa-role

The port-access role command takes you into the config-pa-role context.

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

292

Parameters
access <VLAN-ID>
SpecifiestheVLANIDfortheaccessVLAN.SupportsasingleVLANIDintherange1to4094.
trunk native<VLAN-ID>
SpecifiesthenativeVLANIDonthetrunkinterface.SupportsasingleVLANIDintherange1to4094.
trunk allowed<VLAN-ID>
SpecifiesthelistoftaggedorallowedVLANsonthetrunkinterface.SupportsalistofVLANIDsinthe
range1to4094.The6300,6400SwitchSeriessupportamaximumof1024trunkallowedVLANIDs.The
6200SwitchSeriessupportsamaximumof256trunkallowedVLANIDs.
access name<VLAN-NAME>
SpecifiestheVLANnamefortheaccessVLAN.SupportsasingleVLANnamewithamaximumlengthof
32characters.
| trunk native name<VLAN-NAME> |     |     |     |
| ---------------------------- | --- | --- | --- |
SpecifiesthenativeVLANnameonthetrunkinterface.SupportsasingleVLANnamewithamaximum
lengthof32characters.
| trunk allowed name<VLAN-NAME> |     |     |     |
| ----------------------------- | --- | --- | --- |
SpecifiesthetaggedorallowedVLANnameonthetrunkinterface.SupportsasingleVLANnameineach
CLIwithamaximumlengthof32characters.Theswitchsupportsamaximumof50trunkallowedVLAN
names.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
NotethefollowingpointswhenconfiguringtheVLANIDsandnamesforarole:
ForVLANaccessandVLANtrunknativerespectively,itisrecommendedtoconfigureonlyoneofeither
n
VLANIDornameforarole.IncasebothVLANIDandnameareconfigured,thenVLANIDtakes
precedenceandisappliedwiththerole.
n ForVLANtrunkallowed,youcancollectivelyconfigureamaximumof50namesand1024VLANIDson
the6300,6400SwitchSeries,or256VLANIDsonthe6200SwitchSeries.Incasethislimitisexceededin
therole,thenthatroleisrejectedwhenapplyingittoanonboardingdevice.
Examples
ConfiguringVLANmodesandVLANIDsforanewrole:
| switch(config)#         | port-access | role role01     |     |
| ----------------------- | ----------- | --------------- | --- |
| switch(config-pa-role)# | vlan        | trunk native 10 |     |
switch(config-pa-role)#
|                         | vlan | trunk allowed 11-15 |     |
| ----------------------- | ---- | ------------------- | --- |
| switch(config-pa-role)# | vlan | access 50           |     |
ConfiguringVLANmodesandVLANnamesforanewrole:
| switch(config)#         | port-access | role role10        |       |
| ----------------------- | ----------- | ------------------ | ----- |
| switch(config-pa-role)# | vlan        | trunk native name  | hpe01 |
| switch(config-pa-role)# | vlan        | trunk allowed name | data  |
Portaccess|293

| switch(config-pa-role)# | vlan trunk | allowed name | voice |
| ----------------------- | ---------- | ------------ | ----- |
| switch(config-pa-role)# | vlan trunk | allowed name | video |
DeletingVLANconfigurationfromarole:
| switch(config-pa-role)# | no vlan | trunk native  | 10    |
| ----------------------- | ------- | ------------- | ----- |
| switch(config-pa-role)# | no vlan | trunk allowed | 10-15 |
| switch(config-pa-role)# | no vlan | access 50     |       |
DeletingtrunkallowedVLANnamesfromaroleindividually:
| switch(config-pa-role)# | no vlan | trunk native  | name hpe01 |
| ----------------------- | ------- | ------------- | ---------- |
| switch(config-pa-role)# | no vlan | trunk allowed | name data  |
switch(config-pa-role)#
|                         | no vlan | trunk allowed | name voice |
| ----------------------- | ------- | ------------- | ---------- |
| switch(config-pa-role)# | no vlan | trunk allowed | name video |
DeletingtrunkallowedVLANnamesfromaroleallatonce:
| switch(config-pa-role)# | no vlan | trunk native  | name hpe01 |
| ----------------------- | ------- | ------------- | ---------- |
| switch(config-pa-role)# | no vlan | trunk allowed | name       |
| Port access VLAN        | groups  |               |            |
VLANgroupingenablesuserdistributionacrossVLANsinaVLANgrouptoreducethesizeofbroadcast
domains.ThissupportsdynamicloadbalancingofusersacrossVLANsbyonboardingnewusersontheleast
populatedVLANinthegroup.
AVLANgroupisaconfigurationconstruct,whichcontainsmultipleVLANsallocatedtothatgroup.VLAN
groupleveragestheexistingstandardattributeTunnel-Group-Private-ID(81).Thisstandardattributeis
overloadedtobeinterpretedastheVLANgroupname,iftheVLANnamedoesnotexistontheswitchwith
thatname.VLAN groupissupportedonlythroughRADIUSattributes;thereisnosupportavailablethrough
localrolesordownloadableuserroles.
| VLAN grouping limitations |     |     |     |
| ------------------------- | --- | --- | --- |
ThefollowinglimitationsapplytoVLANgrouping:
n VLANsmustbecreatedtobeallocated.AnyVLAN thatdoesnotexistontheswitchisignoredfrom
allocation.
n WhenaVLANisallocatedfromaVLANgroup,andissubsequentlyremovedfromtheVLANgroup,no
changeisperformedontheclient,untiltheclientexpiresorarolechangeisperformed.Re-
authenticationhasnoeffect.
DeletingaVLANgroupafteraVLANfromthatgroupisallocatedtoaclient,doesnotaffecttheclient.
n
ItisnotrecommendedtousereservedVLANsinthepool.AnyVLANthatisreservedforanother
n
purpose,suchasUBT,isallocated,butfailsauthorization.
WhentheVLANgroupandVLANnameareconfiguredwiththesamenameontheswitch;upon
n
authentication,theVLANnametakesprecedenceandclientsareappliedtotheVLANname.
| VLAN group load | balancing |     |     |
| --------------- | --------- | --- | --- |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 294

VLANgroupingprovidesdistributionofclientsacrosstheVLANsintheswitchtoreducethebroadcast
domainofsecureclients.ThisfeatureenablesallocatingaVLANfromapreconfiguredlistofpool,thus
reducingtheneedfortheadministratortoloadbalancethenetwork.
LoadbalancingbetweenVLANsadherestothefollowingrules:
n AglobalportaccessperVLANclientcountismaintained.
ForanewlyauthenticatedclientwiththeattributeofaVLANgroup,theswitchiteratesthroughallVLANs
n
intheVLANgroupandassignstheVLANwiththelowestnumberofclients.
n IncaseswheremorethanoneVLANhasthesameleastclientcount,theswitchassignstheVLANwiththe
lowestVLANIDtotheauthenticatedclient.
n VLANgroupload-balancingcanbeviewedwiththeshowport-accessclientsdetailcommandoutput,
whichshowstheVLANassociationandVLANgroupnameforeachauthenticatedclient.
n ThefollowingexampleconfigurationshowsaVLANgroupand4VLANsassociatedwithit:
| port-access    | vlan-group  | vgp1 |
| -------------- | ----------- | ---- |
| associate-vlan | 10,20,30,40 |      |
Foreightnewlyauthenticatedclients,theVLANassignmentorderisasfollows:
| Client  | VLAN    | Assignment |
| ------- | ------- | ---------- |
| Client1 | VLAN 10 |            |
| Client2 | VLAN 20 |            |
| Client3 | VLAN30  |            |
| Client4 | VLAN40  |            |
| Client5 | VLAN 10 |            |
| Client6 | VLAN 20 |            |
| Client7 | VLAN30  |            |
| Client8 | VLAN40  |            |
n TheVLANclientcountisacrossmultipleVLANgroupsandmultipleinterfaces.
o Example 1:Client1authenticateswithgroupvgp1containingVLANs10,20wherebothVLANshave
aclientcountofzero.Client1isassignedVLAN10sincebothVLANshavethesameclientcountof
zero,andVLAN10hasthelowerVLANID.Next,client2authenticateswithgroupvgp2andis
assignedVLAN20sinceVLAN20hasthelowerclientcount,eventhoughitlieswithinadifferent
VLANgroup.
o Example 2:Client1authenticatesoninterface1/1/1withgroupvgp1containingVLANs10,20.Next,
client2authenticatesoninterface1/1/2onthesameordifferentVLANgroup.TheorderofVLAN
assignmentforclient1andclient2isVLAN10andVLAN20,respectively.
| Port access | VLAN | group commands |
| ----------- | ---- | -------------- |
associate-vlan
Syntax
Portaccess|295

| associate-vlan    | <VLAN-ID> |           |     |     |     |     |
| ----------------- | --------- | --------- | --- | --- | --- | --- |
| no associate-vlan |           | <VLAN-ID> |     |     |     |     |
Description
AssociatesVLANswithanexistingVLANgroup.
ThenoformofthiscommandremovestheassociationoftheVLANwiththespecifiedVLANgroup.
Commandcontext
config-pa-vlan-group
Parameters
<VLAN-ID>
SpecifiestheVLANoraspecificsetofVLANs.Range1to4094.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
AssociatingVLANswith group1:
| switch(config)#               |     | port-access |     | vlan-group     | group1 |               |
| ----------------------------- | --- | ----------- | --- | -------------- | ------ | ------------- |
| switch(config-pa-vlan-group)# |     |             |     | associate-vlan |        | 5,10-15,20,21 |
AssociatingadditionalVLANswith group1:
| switch(config)#               |     | port-access |     | vlan-group     | group1 |       |
| ----------------------------- | --- | ----------- | --- | -------------- | ------ | ----- |
| switch(config-pa-vlan-group)# |     |             |     | associate-vlan |        | 30-40 |
DissociatingVLANs10-15fromVLANgroup1:
| switch(config-pa-vlan-group)# |     |     |     | no associate-vlan |     | 10-15 |
| ----------------------------- | --- | --- | --- | ----------------- | --- | ----- |
port-accessvlan-group
Syntax
| port-access    | vlan-group |     | <NAME> |     |     |     |
| -------------- | ---------- | --- | ------ | --- | --- | --- |
| no port-access | vlan-group |     | <NAME> |     |     |     |
Description
CreatesthespecifiedVLANgroup(ifitdoesnotalreadyexist)andthenentersitscontextconfig-pa-vlan-
group.ForanexistingVLANgroup,thiscommandentersthecontextofthespecifiedVLANgroup.
ThenoformofthiscommandremovesthespecifiedVLANgroup.
Inorderforthegrouptobeappliedtoaclient,VLANsassociatedtothegroupshouldbeconfiguredonthe
switch.Ifnot,theroledisplaysanerror.
Commandcontext
config
Parameters
<NAME>
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 296

SpecifiesthenameoftheVLAN group.Range2to32characters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreatingVLAN group1andassociatingVLANswithit:
| switch(config)#               | port-access |     | vlan-group     | group1 |               |
| ----------------------------- | ----------- | --- | -------------- | ------ | ------------- |
| switch(config-pa-vlan-group)# |             |     | associate-vlan |        | 5,10-15,20,21 |
DissociatingVLANs10-15fromVLANgroup1:
| switch(config-pa-vlan-group)# |     |     | no associate-vlan |     | 10-15 |
| ----------------------------- | --- | --- | ----------------- | --- | ----- |
show running-configport-accessvlan-group
Syntax
| show running-config | port-access |     | vlan-group |     |     |
| ------------------- | ----------- | --- | ---------- | --- | --- |
Description
ShowsinformationforallconfiguredVLANgroups.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
ShowingtheportaccessVLANgroupconfiguration:
| switch# show | running-config |     | port-access | vlan-group |     |
| ------------ | -------------- | --- | ----------- | ---------- | --- |
...
| port-access | vlan-group | group1 |     |     |     |
| ----------- | ---------- | ------ | --- | --- | --- |
associate-vlan 5,20,21,30-40
| port-access | vlan-group | group2 |     |     |     |
| ----------- | ---------- | ------ | --- | --- | --- |
associate-vlan 50-60,75-85
...
Portaccess|297

|     |     |     |     |              |     |     |        | Chapter    | 16    |
| --- | --- | --- | --- | ------------ | --- | --- | ------ | ---------- | ----- |
|     |     |     |     | Configurable |     |     | RADIUS | attributes | (port |
access)
| Configurable | RADIUS | attributes |     | (port | access) |     |     |     |     |
| ------------ | ------ | ---------- | --- | ----- | ------- | --- | --- | --- | --- |
RADIUSaccessrequestandaccountingrequestpacketsaresenttoaRADIUSserverduringauthentication
andaccountingofportaccessclientsrespectively.TheseaccessrequestpacketscontainvariousAVPs
(AttributeValuePairs)thatcarrytheinformationabouttheRADIUSserverandtheclient.Forexample,these
AVPsincludeitemssuchasusernameandRADIUSserveridentifier(hostname).Similarkindsofdetailsare
includedinaccountingrequestpacketswhicharesenttoaccountingservers.Includingtheseattributesin
accessrequestpacketshelpsadministratorsassignappropriateaccesspoliciestotheclients.
OntheAOS-CX6000SwitchSeries,severalcommandsareprovidedforconfiguringRADIUSattributesper
RADIUSservergroupforusewithportaccessclientauthenticationbyRADIUS.
| Configurable         |     | RADIUS |     | attribute |     | commands |     |     |     |
| -------------------- | --- | ------ | --- | --------- | --- | -------- | --- | --- | --- |
| aaa radius-attribute |     | group  |     |           |     |          |     |     |     |
Syntax
| aaa radius-attribute    |     | group <GROUP-NAME> |              |     |     |     |     |     |     |
| ----------------------- | --- | ------------------ | ------------ | --- | --- | --- | --- | --- | --- |
| no aaa radius-attribute |     | group              | <GROUP-NAME> |     |     |     |     |     |     |
Description
ConfiguresanexistingRADIUS servergroupforwhichtheconfiguredRADIUS attributeswillbeincludedin
requestpackets.Enterstheconfig-radius-attrcontext.
ThenoformofthiscommandunconfigurestheRADIUSservergroupfortheconfiguredRADIUSattributes.
Commandcontext
config
Parameters
<GROUP-NAME>
SpecifiesanexistingRADIUSservergroupname.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringvarious RADIUS attributesforrad_group1:
| switch(config)#             |     | aaa radius-attribute |                         | group        | rad_group1   |                |              |     |     |
| --------------------------- | --- | -------------------- | ----------------------- | ------------ | ------------ | -------------- | ------------ | --- | --- |
| switch(config-radius-attr)# |     |                      | nas-id                  | value        | ARUBA_NAS-01 |                |              |     |     |
| switch(config-radius-attr)# |     |                      | nas-id                  | request-type |              | authentication |              |     |     |
| switch(config-radius-attr)# |     |                      | tunnel-private-group-id |              |              |                | value static |     |     |
switch(config-radius-attr)# tunnel-private-group-id request-type authentication
UnconfiguringRADIUS attributesforrad_group1:
298
| AOS-CX10.07SecurityGuide| | (6200,6300,6400SwitchSeries) |     |     |     |     |     |     |     |     |
| ------------------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |

| switch(config)# |              | no aaa radius-attribute |     | group | rad_group1 |
| --------------- | ------------ | ----------------------- | --- | ----- | ---------- |
| nas-id          | request-type |                         |     |       |            |
Syntax
| nas-id    | request-type | {authentication |     | | accounting | | both} |
| --------- | ------------ | --------------- | --- | ------------ | ------- |
| no nas-id | request-type | {authentication |     | | accounting | | both} |
Description
Fortheselected(bycontext)RADIUSservergroup,configurestheNetworkAccessServer(NAS) IDrequest
typeforwhichtheattributeconfiguredwithcommandnas-id valuewillbeincluded.
Thenoformofthiscommandunconfiguresthespecifiedrequesttype.
Commandcontext
config-radius-attr
Parameters
authentication
Selectstheauthenticationrequesttype.
accounting
Selectstheaccountingrequesttype.
both
Selectsboththeauthenticationandaccountingrequesttypes.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringtheauthenticationrequesttypeforrad_group1:
| switch(config)#             |     | aaa radius-attribute |        | group        | rad_group1     |
| --------------------------- | --- | -------------------- | ------ | ------------ | -------------- |
| switch(config-radius-attr)# |     |                      | nas-id | request-type | authentication |
Configuringboththeauthenticationandaccountingrequesttypesforrad_group2:
| switch(config)#             |     | aaa radius-attribute |        | group        | rad_group2 |
| --------------------------- | --- | -------------------- | ------ | ------------ | ---------- |
| switch(config-radius-attr)# |     |                      | nas-id | request-type | both       |
Unconfiguringtheauthenticationrequesttypeforrad_group1:
| switch(config)# |     | aaa radius-attribute |     | group | rad_group1 |
| --------------- | --- | -------------------- | --- | ----- | ---------- |
switch(config-radius-attr)# no nas-id request-type authentication
| nas-id | value |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- |
Syntax
| nas-id    | value <NAS-ID> |           |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- |
| no nas-id | [value         | <NAS-ID>] |     |     |     |
ConfigurableRADIUSattributes(portaccess)|299

Description

For the selected (by context) RADIUS server group, configures the Network Access Server Identifier (NAS ID)
(type 32, RFC 2865). The NAS ID is sent in the RADIUS access request and accounting packets to notify the
source of the RADIUS access request.

The no form of this command unconfigures the specified NAS ID.

Command context

config-radius-attr

Parameters

<NAS-ID>

Specifies the FQDN or other unique identifying name of the Network Access Server (NAS). Range 1 to
253 characters.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the Network Access Server (NAS) ID for rad_group1:

switch(config)# aaa radius-attribute group rad_group1
switch(config-radius-attr)# nas-id value ARUBA_NAS-01

Unconfiguring the NAS ID for rad_group1:

switch(config)# aaa radius-attribute group rad_group1
switch(config-radius-attr)# no nas-id value ARUBA_NAS-01

Unconfiguring both the NAS-ID value and the request type for rad_group2:

switch(config)# aaa radius-attribute group rad_group2
switch(config-radius-attr)# no nas-id

tunnel-private-group-id request-type

Syntax

tunnel-private-group-id request-type {authentication | accounting | both}
no tunnel-private-group-id request-type {authentication | accounting | both}

Description

For the selected (by context) RADIUS server group, configures the request type for which the attribute
configured with command tunnel-private-group-id value will be included.

The no form of this command unconfigures the specified request type.

Command context

config-radius-attr

Parameters

authentication

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

300

Selects the authentication request type.

accounting

Selects the accounting request type.

both

Selects both the authentication and accounting request types.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the authentication request type for rad_group1:

switch(config)# aaa radius-attribute group rad_group1
switch(config-radius-attr)# tunnel-private-group-id request-type authentication

Configuring both the authentication and accounting request types for rad_group2:

switch(config)# aaa radius-attribute group rad_group2
switch(config-radius-attr)# tunnel-private-group-id request-type both

Unconfiguring the authentication request type for rad_group2:

switch(config)# aaa radius-attribute group rad_group2
switch(config-radius-attr)# no tunnel-private-group-id request-type authentication

tunnel-private-group-id value

Syntax

tunnel-private-group-id value {static | dynamic}
no tunnel-private-group-id value {static | dynamic}

Description

For the selected (by context) RADIUS server group, configures the tunnel-private-group-id value (type
81, RFC 2868) that will be sent in RADIUS access-request packets. This is used for VLAN identification.

The no form of this command unconfigures specified tunnel-private-group-id value.

Command context

config-radius-attr

Parameters

static

Causes the switch to send (as an attribute value) the native VLAN of the client port.

dynamic

Causes the switch to send (as an attribute value) the client VLAN assigned by server. This is applicable
during re-authentication scenarios.

Authority

Administrators or local user group members with execution rights for this command.

Configurable RADIUS attributes (port access) | 301

Examples
Configuringrad_group1fortheRADIUSattributetoidentifythenativeVLANoftheclientport:
switch(config)#
aaa radius-attribute group rad_group1
| switch(config-radius-attr)# |     | tunnel-private-group-id | value static |
| --------------------------- | --- | ----------------------- | ------------ |
Configuringrad_group2fortheRADIUSattributetoidentifytheclientVLANassignedbytheserver:
| switch(config)# | aaa radius-attribute | group rad_group2 |     |
| --------------- | -------------------- | ---------------- | --- |
switch(config-radius-attr)# tunnel-private-group-id value dynamic
Unconfiguring(forrad_group1)theRADIUSattributetoidentifythenativeVLANoftheclientport:
| switch(config)# | aaa radius-attribute | group rad_group1 |     |
| --------------- | -------------------- | ---------------- | --- |
switch(config-radius-attr)# no tunnel-private-group-id value static
Unconfiguring(forrad_group3)boththegroup-IDvalueandrequesttype:
| switch(config)#             | aaa radius-attribute | group rad_group3           |     |
| --------------------------- | -------------------- | -------------------------- | --- |
| switch(config-radius-attr)# |                      | no tunnel-private-group-id |     |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 302

Chapter 17
|           |        |            |     | Supported | RADIUS | attributes |
| --------- | ------ | ---------- | --- | --------- | ------ | ---------- |
| Supported | RADIUS | attributes |     |           |        |            |
ArubaOS-CXsupportsvariousRADIUSserverattributestobeappliedduringauthenticationofclients.This
sectionliststheattributessupportedinthefollowingfeatures:
n 802.1Xauthentication
n MACauthentication
Dynamicauthorization
n
Sessionauthorizationin802.1XandMACauthentication,andCoA
n
n RADIUSservertracking
n RADIUSnetworkaccounting
Thefollowingtermsareusedinthelistofattributes:
n Tx:AttributeaddedintherequestpacketsthataresenttotheRADIUSserver.
Rx:AttributeprocessedintheresponsepacketsreceivedfromtheRADIUSserver.
n
| Attributes | supported |     | in 802.1X | authentication |     |     |
| ---------- | --------- | --- | --------- | -------------- | --- | --- |
FollowingaretheRADIUSattributessupportedin802.1Xauthentication:
| | Attribute | name | | Tx | | Rx | Notes |     |     | |   |
| ----------- | ---- | ------ | ---------- | --- | --- | --- |
|-----------------------|----|----|---------------------------------------------------|
| | User-name          |     | | Y | | N | RFC2865      |     |     | |   |
| -------------------- | --- | ----- | ---------------- | --- | --- | --- |
| | Calling-station-id |     | | Y | | N | RFC2865/3580 |     |     | |   |
| | Called-station-id  |     | | Y | | N | RFC2865/3580 |     |     | |   |
| | NAS-port-id        |     | | Y | | N | RFC2869      |     |     | |   |
| | NAS-port           |     | | Y | | N | RFC2865      |     |     | |   |
| | Service-Type       |     | | Y | | N | RFC2865      |     |     | |   |
| | EAP-Message        |     | | Y | | N | RFC2869      |     |     | |   |
| | State              |     | | Y | | Y | RFC2865      |     |     | |   |
| Session-Timeout | N | Y | RFC2865 - Used as EAP timeout in Challenge packet |
| | NAS-IP-Address        |           | | Y | | N | RFC2865 |                |     | |   |
| ----------------------- | --------- | ----- | ----------- | -------------- | --- | --- |
| | NAS-Identifier        |           | | Y | | N | RFC2865 |                |     | |   |
| | NAS-Ipv6-Address      |           | | Y | | N | RFC3162 |                |     | |   |
| | Message-Authenticator |           | | Y | | Y | RFC2869 |                |     | |   |
| Attributes              | supported |       | in MAC      | authentication |     |     |
FollowingaretheRADIUSattributessupportedinMACauthentication:
| | Attribute | name | | Tx | | Rx | Notes | |   |     |     |
| ----------- | ---- | ------ | ---------- | --- | --- | --- |
|-----------------------|----|----|--------------|
| | User-name          |     | | Y | | N | RFC2865      | |   |     |     |
| -------------------- | --- | ----- | ---------------- | --- | --- | --- |
| | Calling-station-id |     | | Y | | N | RFC2865/3580 | |   |     |     |
| | Called-station-id  |     | | Y | | N | RFC2865/3580 | |   |     |     |
| | NAS-port-id        |     | | Y | | N | RFC2869      | |   |     |     |
| | NAS-port           |     | | Y | | N | RFC2865      | |   |     |     |
| | Service-Type       |     | | Y | | N | RFC2865      | |   |     |     |
| | State              |     | | Y | | Y | RFC2865      | |   |     |     |
| | NAS-IP-Address     |     | | Y | | N | RFC2865      | |   |     |     |
303
| AOS-CX10.07SecurityGuide| | (6200,6300,6400SwitchSeries) |     |     |     |     |     |
| ------------------------- | ---------------------------- | --- | --- | --- | --- | --- |

| | NAS-Identifier        |           | | Y | | N | RFC2865 | |             |     |     |
| ----------------------- | --------- | ----- | ----------- | ------------- | --- | --- |
| | NAS-Ipv6-Address      |           | | Y | | N | RFC3162 | |             |     |     |
| | Message-Authenticator |           | | Y | | Y | RFC2869 | |             |     |     |
| | Chap-Challenge        |           | | Y | | N | RFC2865 | |             |     |     |
| | Chap-Password         |           | | Y | | N | RFC2865 | |             |     |     |
| | User-Password         |           | | Y | | N | RFC2865 | |             |     |     |
| Attributes              | supported |       | in dynamic  | authorization |     |     |
FollowingaretheRADIUSattributessupportedindynamicauthorization:
| | Attribute | name | | Tx | | Rx | Notes | |   |     |     |
| ----------- | ---- | ------ | ---------- | --- | --- | --- |
|-----------------------|----|----|--------------|
| | User-name             |     | | N | | Y | RFC2865      | |   |     |     |
| ----------------------- | --- | ----- | ---------------- | --- | --- | --- |
| | Calling-station-id    |     | | N | | Y | RFC2865/3580 | |   |     |     |
| | Called-station-id     |     | | N | | Y | RFC2865/3580 | |   |     |     |
| | NAS-port-id           |     | | N | | Y | RFC2869      | |   |     |     |
| | NAS-port              |     | | N | | Y | RFC2865      | |   |     |     |
| | NAS-IP-Address        |     | | N | | Y | RFC2865      | |   |     |     |
| | NAS-Identifier        |     | | N | | Y | RFC2865      | |   |     |     |
| | NAS-Ipv6-Address      |     | | N | | Y | RFC3162      | |   |     |     |
| | Error-cause           |     | | Y | | N | RFC5176      | |   |     |     |
| | Acct-Terminate-Cause  |     | | Y | | Y | RFC2866      | |   |     |     |
| | Acct-Session-Id       |     | | N | | Y | RFC2866      | |   |     |     |
| | Message-Authenticator |     | | N | | Y | RFC2869      | |   |     |     |
| | Event-Timestamp       |     | | N | | Y | RFC2869      | |   |     |     |
n Oneormoreofthefollowingattributes,NAS-IP-Address,NAS-Identifier,NAS-IPv6-Address,is
mandatoryforprocessingChangeofAuthorization(CoA)requestsfromdynamicauthorizationclients.
EitherAcct-Session-Idattribute,oroneorbothofNAS-portandNAS-port-idattributesandthe
n
Calling-station-idattributeismandatorytoidentifytheusersessionforprocessingCoArequestsfrom
dynamicauthorizationclients.
n TheUser-nameattributeismandatoryforprocessingallCoArequests.
TheAcct-Terminate-CauseattributeisusedintheCoAdisconnectrequestandresponsemessages.
n
Allsessionauthorizationattributes(bothVSAandstandard)aresupportedintheCoAmessageonly,
n
includingAruba-Port-Bounce.
| Session             | authorization |            | attributes | supported | in 802.1X | and |
| ------------------- | ------------- | ---------- | ---------- | --------- | --------- | --- |
| MAC authentication, |               |            | and CoA    |           |           |     |
| Standard            | session       | attributes | supported  |           |           |     |
Followingarethestandardsessionattributessupportedin802.1XandMACauthentication,andCoA:
| | Attribute | name | | ID | | Type | Notes | |   |     |     |
| ----------- | ---- | ---- | -------------- | --- | --- | --- |
|-------------------------|----|--------|---------|
| | Filter-Id               |     | | 11 | | String | RFC3580 | |   |     |     |
| ------------------------- | --- | ---- | ------------------ | --- | --- | --- |
| | Egress-VLANID           |     | | 56 | | Octet | RFC4675  | |   |     |     |
| | Egress-VLAN-Name        |     | | 58 | | String | RFC4675 | |   |     |     |
| | Tunnel-Type             |     | | 64 | | Octet | RFC2868  | |   |     |     |
| | Tunnel-Medium-Type      |     | | 65 | | Octet | RFC2868  | |   |     |     |
| | Tunnel-Private-Group-ID |     | | 81 | | String | RFC2868 | |   |     |     |
| | NAS-Filter-Rule         |     | | 92 | | String | RFC4849 | |   |     |     |
| | Framed-MTU              |     | | 12 | | Octet | RFC2865  | |   |     |     |
| | Session-Timeout         |     | | 27 | | Octet | RFC2865  | |   |     |     |
| | Terminate-Action        |     | | 29 | | Octet | RFC2865  | |   |     |     |
| | Idle-Timeout            |     | | 28 | | Octet | RFC2865  | |   |     |     |
SupportedRADIUSattributes|304

WhenmultipleclientsrequestadifferentMTUvalueusingtheFramed-MTUattribute,thehighestMTUvalue
requestedamongtheclientswillbeprogrammedontheport.
Vendor-Specific Attributes supported in session authorization
FollowingaretheVendor-SpecificAttributes(VSAs)supportedinsessionauthorization:
| Attribute Name | Length | Type | Aruba Vendor ID | Aruba Attribute Type |
|-----------------------------|--------|---------|-----------------|----------------------|
| | Aruba-CPPM-Role           | | <=63  | | string  | | 14823 | | 23 | |   |
| --------------------------- | ------- | --------- | ------- | ---- | --- |
| | Aruba-PoE-Priority        | | 4     | | integer | | 14823 | | 49 | |   |
| | Aruba-Port-Auth-Mode      | | 4     | | integer | | 14823 | | 50 | |   |
| | Aruba-NAS-Filter-Rule     | | <=247 | | string  | | 14823 | | 51 | |   |
| | Aruba-QoS-Trust-Mode      | | 4     | | integer | | 14823 | | 52 | |   |
| | Aruba-Gateway-Zone        | | <=63  | | string  | | 14823 | | 54 | |   |
| | Aruba-UBT-Gateway-Role    | | <=63  | | string  | | 14823 | | 53 | |   |
| | Aruba-Captive-Portal-URL  | | <=247 | | string  | | 14823 | | 43 | |   |
| | Aruba-User-Role           | | <=63  | | string  | | 14823 | | 1  | |   |
| | Aruba-Port-Bounce         | | 4     | | Integer | | 14823 | | 40 | |   |
| | Aruba-STP-Admin-Edge-Port | | 4     | | Integer | | 14823 | | 55 | |   |
n ChangeofAuthorizationofspecificattributesintheuserroleisnotsupported.Onlyentirerolecanbe
changed.
n SimilarlyifthesessionisusingRADIUSattributes,CoAcanchangeonlytheRADIUSsessionattributes.
n ChangeofAuthorizationtouserroleforasessionusingRADIUSattributesisnotsupportedeither.Ifthis
actionisattempted,aNAKmessageissent.
Description of VSAs
Aruba-CPPM-Role
ThisattributeisusedtodownloadrolesfromClearPassPolicyManager.
Aruba-PoE-Priority
SpecifiesthePoEpriorityofonboardingdevicespostauthentication.Followingarethesupportedvalues:
n 0:Critical
1:Medium
n
2:Low
n
ThisattributeoverridesthePoEpriorityconfiguredontheportwherethedeviceonboards.Thisattribute
istypicallyusedforinfrastructuredevices.Whenmultipleclientsrequestdifferentpriorities,thecritical
prioritytakesprecedenceovermediumpriorityandthemediumprioritytakesprecedenceoverlow
prioritysetting.
Aruba-Port-Auth-Mode
Specifiestheauthenticationmodeoftheportpostauthentication.Followingarethesupportedvalues:
1:Devicemode—Inthismode,aninfrastructuredevice,forexample,switchoraccesspoint,is
n
authenticatedfirst,andalldevicesconnectingtothisauthenticateddeviceareallowedaccess.Here,
thepolicyandVLANattributesareappliedattheport-level.Indevicemode,itisexpectedthatonly
onedeviceisactiveandauthenticatedatanyinstant.UntaggedVLANwilloverridetheportVLANID
andthetaggedVLANswilloverridethetaggedVLANsthatareconfiguredontheportusingtheCLI.
| AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) |     |     |     |     | 305 |
| ---------------------------------------------------- | --- | --- | --- | --- | --- |

n 2: Client mode—In this mode, all devices trying to onboard on that port are authenticated. Here, the
policy and VLAN attributes are applied per client. Untagged VLAN is configured using MAC-based
VLAN. Tagged VLANs are arbitrated among all clients and the result is applied to the port.

Aruba-NAS-Filter-Rule

This attribute is similar to the NAS-Filter-Rule RFC attribute but with additional functionality to support
vendor-specific actions in the rule. The vendor-specific action supported is cp-redirect that is used to
redirect device HTTP traffic to captive portal authentication. This attribute can be used to perform other
actions such as count and rate-limiting. Multiple instances of this attribute are supported, however, the
maximum number of filter rules (including this VSA and NAS-Filter-Rule) supported per client is 128. A
single NAS-Filter-Rule attribute split across multiple VSAs is not supported as servers such as
FreeRadius and ClearPass Policy Manager do not terminate filter rule with '\0' value. Most policy servers
use one filter rule per VSA.

Aruba-QoS-Trust-Mode

Specifies how the switch assigns local priority values to ingress packets. Following are the supported
values:

n 0: Trust mode DSCP

n 1: Trust mode QoS

n 2: No trust mode configuration

This attribute overrides the trust mode configured on the port where the device onboards. This attribute
is typically used for infrastructure devices. When multiple clients request different trust modes, the DSCP
trust mode takes precedence over QoS trust mode and the QoS trust mode takes precedence over no
trust mode configuration setting.

Aruba-Gateway-Zone

Specifies the gateway zone name where the device traffic will be tunneled after authentication.

Aruba-UBT-Gateway-Role

Specifies the role to be applied for devices in the controller. This attribute must be used with the Aruba-
Gateway-Zone attribute for onboarding devices using User-Based Tunneling (UBT).

Aruba-Captive-Portal-URL

Specifies the URL to be used for captive portal redirection. This attribute plus the Aruba-NAS-Filter-
Rule VSA must be used to authenticate a client using captive portal authentication. For URLs that have a
size more than 247 characters, multiple VSAs can be used and the switch will merge these VSAs to form a
single URL. The maximum URL size supported is 1024 characters.

Aruba-User-Role

Specifies the role that must be applied for the devices post authentication. The role must be defined on
the switch. All the session attributes can be defined in the role. Session authorization attributes (both
standard and VSAs) sent with this attribute are ignored.

Aruba-Port-Bounce

Used in the CoA message to signal the switch to shut down the port for the duration specified.

Aruba-STP-Admin-Edge-Port

When enabled, the port will be treated as STP edge port. Even if STP is configured on the port, it will not
be executed. Traffic forwarding will occur immediately when a device connects to the port and completes
authentication. Following are the supported values:

n 0: Disable STP admin edge port.

n 1: Enable STP admin edge port.

Attributes supported in RADIUS network accounting
Following are the attributes supported in RADIUS network accounting:

Supported RADIUS attributes | 306

| | Attribute | name | | Tx | | Rx | Notes |     |     | |   |
| ----------- | ---- | ------ | ---------- | --- | --- | --- |
|-----------------------|----|----|---------------------------------------|
| | User-name          |     | | N | | N | RFC2865 |     |     | |   |
| -------------------- | --- | ----- | ----------- | --- | --- | --- |
| | Calling-station-id |     | | Y | | N | RFC2865 |     |     | |   |
| | Calling-station-id |     | | Y | | N | RFC2865 |     |     | |   |
| | NAS-port-id        |     | | Y | | N | RFC2869 |     |     | |   |
| | NAS-port           |     | | Y | | N | RFC2865 |     |     | |   |
| | NAS-port-Type      |     | | Y | | N | RFC2865 |     |     | |   |
| | Service-Type       |     | | Y | | N | RFC2865 |     |     | |   |
| | NAS-IP-Address     |     | | Y | | N | RFC2865 |     |     | |   |
| | NAS-Identifier     |     | | Y | | N | RFC2865 |     |     | |   |
| | NAS-Ipv6-Address   |     | | Y | | N | RFC3162 |     |     | |   |
| | Acct-Authentic     |     | | Y | | N | RFC2866 |     |     | |   |
| | Acct-Session-Id    |     | | Y | | N | RFC2866 |     |     | |   |
| | Acct-Status-Type   |     | | Y | | N | RFC2866 |     |     | |   |
| Acct-Input-Octets | Y | N | RFC2866 - In Interim and Stop packets |
| Acct-Output-Octets | Y | N | RFC2866 - In Interim and Stop packets |
| Acct-Input-Packets | Y | N | RFC2866 - In Interim and Stop packets |
| Acct-Output-Packets | Y | N | RFC2866 - In Interim and Stop packets |
| Acct-Input-Gigawords | Y | N | RFC2869 - In Interim and Stop packets |
| Acct-Output-Gigawords | Y | N | RFC2869 - In Interim and Stop packets |
| Acct-Session-Time | Y | N | RFC2866 - In Interim and Stop packets |
| | Acct-Terminate-Cause |           | | Y | | N | RFC2866 | - in Stop | packet          | |   |
| ---------------------- | --------- | ----- | ----------- | --------- | --------------- | --- |
| | Class                |           | | Y | | N | RFC2865 |           |                 | |   |
| Attributes             | supported |       | in RADIUS   |           | server tracking |     |
FollowingaretheattributessupportedinRADIUSservertracking:
| | Attribute | name | | Tx | | Rx | Notes | |   |     |     |
| ----------- | ---- | ------ | ---------- | --- | --- | --- |
|-----------------------|----|----|--------------|
| | User-name        |     | | Y | | N | RFC2865 | |   |     |     |
| ------------------ | --- | ----- | ----------- | --- | --- | --- |
| | NAS-IP-Address   |     | | Y | | N | RFC2865 | |   |     |     |
| | NAS-Identifier   |     | | Y | | N | RFC2865 | |   |     |     |
| | NAS-Ipv6-Address |     | | Y | | N | RFC3162 | |   |     |     |
| | Chap-Challenge   |     | | Y | | N | RFC2865 | |   |     |     |
| | Chap-Password    |     | | Y | | N | RFC2865 | |   |     |     |
| | User-Password    |     | | Y | | N | RFC2865 | |   |     |     |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 307

Chapter 18

Port security

Port security

Port security enables you to configure each switch port with a unique list of the MAC addresses of devices
that are authorized to access the network through that port. This security enables individual ports to detect,
prevent, and log attempts by unauthorized devices to communicate through the switch.

MAC Lockdown, also known as Static Addressing, is used to prevent station movement and MAC address
hijacking, by allowing a given MAC address to use only an assigned port on the switch. MAC Lockdown also
restricts the client device to a specific VLAN.

MAC Lockout enables blocking a specific MAC address so that the switch drops all traffic to or from the
specified address.

Port security does not prevent intruders from receiving broadcast and multicast traffic. MAC Lockdown has a
higher priority over port security.

Port-security sticky MAC
Sticky MAC is a port security feature that learns MAC addresses on an interface and retains the MAC
information. When sticky learning is enabled on a port, all non-static MAC addresses are considered as sticky
MACs. Also, all newly on-boarded clients are considered as sticky MACs. The sticky authorized clients are not
affected by a switch reboot or link-flap once the MAC addresses are learnt. When disabled, all sticky MACs on
the port are made as dynamic clients.

Sticky MACs can be configured statically (sticky-static) and also be learned dynamically (sticky-dynamic) on a
sticky-learn enabled port.

n If the same MAC address is configured as sticky-static and static on a sticky learning port, sticky MAC

configuration takes precedence.

n Static non-sticky MAC addition is supported on a sticky learning enabled port.

n Existing static port-security MACs on a port are not changed to sticky MAC on enabling the sticky MAC

feature.

n Moving sticky MAC clients from one port to another is a violation. You can view the violation information

using the show port-access security violation sticky-mac-client-move interface command.
Also, the following event log message will be displayed: Port security sticky client move violation
triggered on port {port} for client with MAC address {mac_addr}.

n Downgrading AOS-CX from 10.07 or later versions to earlier versions after learning port-security sticky

MACs and upgrading it back to 10.07 or later versions might cause unstable behavior of sticky MACs. So, it is

recommended to disable port-security configuration at the global context during migration of software

image back to 10.07 or later versions in such scenarios.

Basic operation

Default port security operation

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

308

The default port security setting for each port is dynamic mode in which the switch learns addresses from
inbound traffic from any connected device.

Intruder protection

A port that detects an intruder blocks the intruding device from transmitting to the network through that
port.

General operation for port security

On a per-port basis, you can configure security measures to block unauthorized devices, and to send notice
of security violations. Once port security is configured, you can then monitor the network for security
violations through one or more of the following:

n Alert flags captured by network management tools.

n Alert Log entries in the WebAgent

n Event Log entries in the console interface

For any port, you can configure the following:

n Action—Used when a port detects an intruder. Specifies whether to send an SNMP trap to a network

management station and whether to disable the port.

n Address limit—Sets the number of authorized MAC addresses allowed on the port.

n Address learn mode—Specify how the port acquires authorized MAC addresses. After configuring the
maximum secure MAC address limit, the MAC address can be learned by one of the following ways:

o Configure all MAC addresses by using the mac-address command.

o Allow the port to dynamically learn all MAC addresses.

o Configure some MAC addresses and allow the rest to be learned dynamically.

n Static—Enables you to set a fixed limit on the number of MAC addresses authorized for the port and to
specify some or all the authorized addresses. (If you specify only some of the authorized addresses, the
port learns the remaining authorized addresses from the traffic it receives from connected devices.)

n Configured—Requires that you specify all MAC addresses authorized for the port. The port is not allowed

to learn addresses from inbound traffic.

n Authorized (MAC) Addresses—Specify up to eight devices (MAC addresses) that are allowed to send

inbound traffic through the port. This feature:

o Closes the port to inbound traffic from any unauthorized devices that are connected to the port.

o Provides the option for sending an SNMP trap notifying of an attempted security violation to a

network management station and, optionally, disables the port.

n Port Access—Allows only the MAC address of a device authenticated through the switch 802.1X Port-

Based access control.

Blocking unauthorized traffic
Unless you configure the switch to disable a port on which a security violation is detected, the switch
security measures block unauthorized traffic without disabling the port. This implementation enables you
to apply the security configuration to ports on which hubs, switches, or other devices are connected, and to
maintain security while also maintaining network access to authorized users.

Port security | 309

| Figure | 3 Howportsecuritycontrolsaccess |     |     |
| ------ | ------------------------------- | --- | --- |
BroadcastandMulticasttrafficisalwaysallowed,andcanbereadbyintrudersconnectedtoaportonwhichyou
haveconfiguredportsecurity.
| Trunk | group | exclusion |     |
| ----- | ----- | --------- | --- |
Portsecuritydoesnotoperateoneitherastaticordynamictrunkgroup.Ifyouconfigureportsecurityon
oneormoreportsthatarelateraddedtoatrunkgroup,theswitchresetstheportsecurityparametersfor
thoseportstothefactorydefaultconfiguration.PortsconfiguredforeitherActiveorPassiveLACP,and
whicharenotmembersofatrunk,canbeconfiguredforportsecurity.
| Port        | security      | commands |     |
| ----------- | ------------- | -------- | --- |
| port-access | port-security |          |     |
Syntax
| port-access | port-security | {enable | | disable} |
| ----------- | ------------- | ------- | ---------- |
Description
Enablesordisablesportsecuritygloballyorattheportlevel.
Commandcontext
config
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingportsecurityglobally:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 310

| switch(config)# |     | port-access |     | port-security |     | enable |
| --------------- | --- | ----------- | --- | ------------- | --- | ------ |
Disablingportsecurityglobally:
| switch(config)# |     | port-access |     | port-security |     | disable |
| --------------- | --- | ----------- | --- | ------------- | --- | ------- |
Enablingportsecurityonaport:
| switch(config-if)# |     |     | port-access |     | port-security | enable |
| ------------------ | --- | --- | ----------- | --- | ------------- | ------ |
Disablingportsecurityonaport:
| switch(config-if)# |     |               | port-access |     | port-security | disable |
| ------------------ | --- | ------------- | ----------- | --- | ------------- | ------- |
| port-access        |     | port-security |             |     | client-limit  |         |
Syntax
| port-access    | port-security |     | client-limit |              | <CLIENTS> |     |
| -------------- | ------------- | --- | ------------ | ------------ | --------- | --- |
| no port-access | port-security |     |              | client-limit |           |     |
Description
Configuresthemaximumnumberofclientsthatareallowedonaport.Afterconfiguringthemaximum
clientslimit,theMACaddressesoftheclientscanbelearnedbyoneofthefollowingmethods:
n UsercanmanuallyconfigureallMACaddressesbyusingthemac-addresscommand.
n UsercanallowtheporttodynamicallylearnallMACaddresses.
UsercanconfigureafixednumberofMACaddressesandallowtheswitchtolearntheremaining
n
addressesdynamically.
Thenoformofthecommandresetsthenumberofclientstothedefault,1.
Commandcontext
config-if
Parameters
<CLIENTS>
Specifiesthemaximumnumberofclients.Default:1.Range:1to32(6200).1to64(6300,6400).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringclientlimitonaport:
| switch(config-if)#               |     |     | port-access |     | port-security | enable |
| -------------------------------- | --- | --- | ----------- | --- | ------------- | ------ |
| switch(config-if-port-security)# |     |     |             |     | client-limit  | 64     |
Portsecurity|311

| port-access |     | port-security |     |     | mac-address |     |     |
| ----------- | --- | ------------- | --- | --- | ----------- | --- | --- |
Syntax
| port-access    | port-security |               |     | mac-address |     | <MAC-ADDRESS> |     |
| -------------- | ------------- | ------------- | --- | ----------- | --- | ------------- | --- |
| no port-access |               | port-security |     | mac-address |     | <MAC-ADDRESS> |     |
Description
ConfigurestheMACaddressesofstaticclients.
Thenoformofthiscommandremovesanauthorizedstaticclientfromtheport.
Commandcontext
config-if
Parameters
<MAC-ADDRESS>
SpecifiestheMACaddressesofthestaticclients.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringastaticclientonaport:
| switch(config-if)# |     |     | port-access |     | port-security |     |     |
| ------------------ | --- | --- | ----------- | --- | ------------- | --- | --- |
switch(config-if-port-security)#
|     |     |     |     |     | mac-address | aa:bb:cc:dd:ee:ff |     |
| --- | --- | --- | --- | --- | ----------- | ----------------- | --- |
Deletingastaticclientonaport:
| switch(config-if)# |     |     | port-access |     | port-security |     |     |
| ------------------ | --- | --- | ----------- | --- | ------------- | --- | --- |
switch(config-if-port-security)# no mac-address aa:bb:cc:dd:ee:ff
| show port-access |     |     | port-security |     |     | interface | client-status |
| ---------------- | --- | --- | ------------- | --- | --- | --------- | ------------- |
Syntax
| show port-access |     | port-security |                |     | interface | {all|<IF-NAME>} |     |
| ---------------- | --- | ------------- | -------------- | --- | --------- | --------------- | --- |
| client-status    |     | [mac          | <MAC-ADDRESS>] |     |           |                 |     |
Description
Showsportsecurityclientsstatusinformationfortheports.TheoutputcanbefilteredbyinterfaceorMAC
address.
Commandcontext
Operator(>)orManager(#)
Parameters
all
Selectsallinterfaces.
<IF-NAME>
Specifiestheinterfacename.
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 312

<MAC-ADDRESS>
SpecifiestheclientMACaddress.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingclientstatusinformationforallports:
switch# show port-access port-security interface all client-status
| Port Security      | Client | Status Details |      |
| ------------------ | ------ | -------------- | ---- |
| Authorized-Clients |        | Type           | Port |
-------------------------------------------
| AB:CD:DE:FF:AA:BB |     | static         | 1/1/1 |
| ----------------- | --- | -------------- | ----- |
| DD:CD:AB:CD:EE:O1 |     | dynamic        | 1/1/2 |
| 00:50:56:96:7e:fc |     | sticky-dynamic | 1/3/2 |
Showingclientstatusinformationwithsticky-learningenabledforallports:
switch# show port-access port-security interface all client-status
| Port Security      | Client | Status Details |      |
| ------------------ | ------ | -------------- | ---- |
| Authorized-Clients |        | Type           | Port |
---------------------------------------------
| AB:CD:DE:FF:AA:BB |     | sticky-static  | 1/1/1 |
| ----------------- | --- | -------------- | ----- |
| DD:CD:AB:CD:EE:O1 |     | sticky-dynamic | 1/1/2 |
| DE:CD:AB:BB:EE:O2 |     | sticky-dynamic | 1/1/2 |
Showingclientstatusinformationforaclient:
switch# show port-access port-security interface 1/3/2 client-status mac
00:50:56:96:7e:fc
| Port Security      | Client | Status Details |      |
| ------------------ | ------ | -------------- | ---- |
| Authorized-Clients |        | Type           | Port |
--------------------------------------------------
| 00:50:56:96:7e:fc |     | sticky-dynamic | 1/3/2 |
| ----------------- | --- | -------------- | ----- |
Showingclientstatusinformationforaport:
switch# show port-access port-security interface 1/3/2 client-status
| Port Security      | Client | Status Details |      |
| ------------------ | ------ | -------------- | ---- |
| Authorized-Clients |        | Type           | Port |
--------------------------------------------------
| 00:50:56:96:7e:fc |     | sticky-dynamic | 1/3/2 |
| ----------------- | --- | -------------- | ----- |
Portsecurity|313

| show | port-access | port-security |     | interface | port-statistics |
| ---- | ----------- | ------------- | --- | --------- | --------------- |
Syntax
show port-access port-security interface {all|<IF-NAME>} port-statistics
Description
Showsportsecuritystatisticsfortheportsinaswitch.Theoutputcanbefilteredbyinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
all
Selectsallinterfaces.
<IF-NAME>
Specifiestheinterfacename.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showinginformationforallports.
switch# show port-access port-security interface all port-statistics
| Port | 1/1/1 |     |     |     |     |
| ---- | ----- | --- | --- | --- | --- |
==========
|     | Client Details |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- |
--------------
|              | Number | of authorized        | clients | : 0 |     |
| ------------ | ------ | -------------------- | ------- | --- | --- |
|              | Number | of sticky authorized | clients | : 2 |     |
| sticky-learn |        | enable               |         |     |     |
Syntax
| sticky-learn    | enable |        |     |     |     |
| --------------- | ------ | ------ | --- | --- | --- |
| no sticky-learn |        | enable |     |     |     |
Description
Enablesstickylearningontheport.AlltheexistingandnewMACslearnedontheportaremadesticky.
Thenoformofthiscommanddisablesthestickylearningontheport.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 314

Examples
Enablingstickylearningontheport:
switch(config)#
|                                  |     | interface   | 1/1/1         |        |     |
| -------------------------------- | --- | ----------- | ------------- | ------ | --- |
| switch(config-if)#               |     | port-access | port-security |        |     |
| switch(config-if-port-security)# |     |             | sticky-learn  | enable |     |
Disablingstickylearningontheport:
| switch(config)#                  |     | interface   | 1/1/1           |        |     |
| -------------------------------- | --- | ----------- | --------------- | ------ | --- |
| switch(config-if)#               |     | port-access | port-security   |        |     |
| switch(config-if-port-security)# |     |             | no sticky-learn | enable |     |
| sticky-learn                     | mac |             |                 |        |     |
Syntax
| sticky-learn    | mac <MAC-ADDRESS> |               | [vlan <VLAN-ID>] |     |     |
| --------------- | ----------------- | ------------- | ---------------- | --- | --- |
| no sticky-learn | mac               | <MAC-ADDRESS> | [vlan <VLAN-ID>] |     |     |
Description
ConfigurestheMACaddressesofstickystaticclients.Afterconfiguring,clientsaredirectlyaddedtothe
MAC addresstable.
Thenoformofthiscommandremovesanauthorizedstickystaticclientfromtheport.
Commandcontext
config-if
Parameters
<MAC-ADDRESS>
SpecifiestheMACaddressesofstaticstickyclients.
vlan <VLAN-ID>
SpecifiestheVLANIDforthestaticstickyclient.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringastickystaticclientonaport:
| switch(config)#    |     | interface   | 1/1/1         |     |     |
| ------------------ | --- | ----------- | ------------- | --- | --- |
| switch(config-if)# |     | port-access | port-security |     |     |
switch(config-if-port-security)#
|     |     |     | sticky-learn | mac-address | aa:bb:cc:dd:ee:ff |
| --- | --- | --- | ------------ | ----------- | ----------------- |
ConfiguringastickystaticclientwithaVLANIDonaport:
| switch(config)#    |     | interface   | 1/1/1         |     |     |
| ------------------ | --- | ----------- | ------------- | --- | --- |
| switch(config-if)# |     | port-access | port-security |     |     |
switch(config-if-port-security)# sticky-learn mac-address aa:bb:cc:dd:ee:ff vlan 4
Portsecurity|315

Removingastickystaticclientfromaport:
|     | switch(config)#    |     | interface   |     | 1/1/1 |               |     |
| --- | ------------------ | --- | ----------- | --- | ----- | ------------- | --- |
|     | switch(config-if)# |     | port-access |     |       | port-security |     |
switch(config-if-port-security)# no sticky-learn mac-address aa:bb:cc:dd:ee:ff
| show | port-access |     |     | security |     | violation | sticky-mac-client-move |
| ---- | ----------- | --- | --- | -------- | --- | --------- | ---------------------- |
interface
Syntax
show port-access security violation sticky-mac-client-move interface {all|<INTERFACE-NAME>}
Description
Showsinformationaboutthesticky-macclientmoveviolation.Theoutputcanbefilteredbyinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
all
Specifiesallinterfaces.
<INTERFACE-NAME>
Specifiestheinterfacename.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showinginformationforallports.
switch# show port-access port-security violation sticky-mac-client-move
|     |            | interface | all  |           |     |                |     |
| --- | ---------- | --------- | ---- | --------- | --- | -------------- | --- |
|     | Sticky MAC | Client    | Move | Violation |     | Status Details |     |
----------------------------------------------------
|     | Port |     | Violation |     | Violation-Count |     |     |
| --- | ---- | --- | --------- | --- | --------------- | --- | --- |
----------------------------------------------------
|     | 1/1/1 |     | No  |     |     | 0   |     |
| --- | ----- | --- | --- | --- | --- | --- | --- |
|     | 1/1/2 |     | Yes |     |     | 10  |     |
|     | 1/1/5 |     | No  |     |     | 10  |     |
Showinginformationforaparticularport.
switch# show port-access port-security violation sticky-mac-client-move
|     |            | interface | 1/1/1 |           |     |                |     |
| --- | ---------- | --------- | ----- | --------- | --- | -------------- | --- |
|     | Sticky MAC | Client    | Move  | Violation |     | Status Details |     |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 316

----------------------------------------------------

Port

Violation

Violation-Count

----------------------------------------------------

1/1/1

No

10

Port security | 317

Chapter 19
Fault Monitor
Fault Monitor
AOS-CXswitchesconsistofautomaticdetectionandcontrolforcertainlinkerrorsandexcessivetraffic
conditions.FaultmonitorcanbeusedtologaneventorsendSNMPtrapsfortheseconditionsand
temporarilydisabletheporttoprotectthenetwork.Monitoringcanbeenabledforallrecognizedfaultsor
forindividualfaultsafterthethresholdactionandauto-enableparametersforeachcanbeconfigured.
FaultmonitorappliesonlytophysicalportsandnottoLAGs,tunnels,VSFlinks,orothertypesofinterfaces.
FaultscanbeappliedtotheindividualmembersofaLAG.
| Fault monitoring |     | conditions |
| ---------------- | --- | ---------- |
Thefollowingfaultconditionsaremonitored:
| Excessive | oversize | packets |
| --------- | -------- | ------- |
Anexcessiveoversizedpacketfaultisreportedwhentheamountofingressoversizedframesper10,000
receivedframesexceedstheconfiguredthresholdvalueinatwentysecondinterval.Inoversizepacketfault,
thepacketssizeismorethantheconfiguredMTUontheinterfacewithgoodcyclicredundancycheck(CRC).
| Excessive | jabbers |     |
| --------- | ------- | --- |
Anexcessivejabbersfaultisreportedwhentheamountofingressjabberframesper10,000receivedframes
exceedstheconfiguredthresholdvalueinatwentysecondinterval.Injabbersfault,thepacketssizeismore
thantheconfiguredMTUontheinterfacewithbadCRC.
| Excessive | fragments |     |
| --------- | --------- | --- |
Anexcessivefragmentfaultisreportedwhentheamountofingressfragmentframesper10,000received
framesexceedstheconfiguredthresholdvalueinatwentysecondinterval.Infragmentsfault,thepacket
sizeislesserthantheconfiguredMTUontheinterfacewithbadCRC.
| Excessive | CRC errors |     |
| --------- | ---------- | --- |
AnexcessiveCRCerrorfaultisreportedwhentheamountofingresscrc-errorframesper10,000received
framesexceedstheconfiguredthresholdvalueinatwentysecondinterval.
| Excessive | TX drops |     |
| --------- | -------- | --- |
ExcessiveTXdropsfaultisanexampleofoverbandwidth.Itisreportedwhenegressdroppedpacketsper
10,000transmittedframesexceedstheconfiguredthresholdvalueinatwentysecondinterval.
| Excessive | link flaps |     |
| --------- | ---------- | --- |
Alinkflapfaultisreportedwhenthecountoftransitionsbetweenlink-upandlink-downstateexceedsthe
configuredthresholdinatensecondinterval.
| Excessive | broadcasts |     |
| --------- | ---------- | --- |
318
| AOS-CX10.07SecurityGuide| | (6200,6300,6400SwitchSeries) |     |
| ------------------------- | ---------------------------- | --- |

Abroadcaststormfaultisreportedwhentheaverageingresstrafficrateofbroadcastpacketsexceedsthe
configuredthresholdinatwentysecondinterval.
Thedefaultthresholdlevelisconfiguredasapercentageofthebandwidthoftheport.Largertheframe
size,smallertheconvertedthresholdvalueinPPS.Hencelargerframesrequirelowerthresholdpercent
configurationstohitthefault.
| Excessive | multicasts |     |     |     |
| --------- | ---------- | --- | --- | --- |
Amulticaststormfaultisreportedwhentheaverageingresstrafficrateofmulticastpacketsexceedsthe
configuredthresholdinatwentysecondinterval.
| Excessive | collisions |     |     |     |
| --------- | ---------- | --- | --- | --- |
Anexcessivecollisionfaultisanexampleofoverbandwidth,itgetsreportedwhenegresscollisionframes
per10,000transmittedframesexceedstheconfiguredthresholdvalueina20secondinterval.
| Excessive | Late Collisions |     |     |     |
| --------- | --------------- | --- | --- | --- |
Anexcessivelatecollisionfaultisreportedwheningresslate-collisionframesper10,000receivedframes
exceedstheconfiguredthresholdvalueina300secondinterval.
| Fault monitor | commands     |         |            |         |
| ------------- | ------------ | ------- | ---------- | ------- |
| Command       | for creating | a fault | monitoring | profile |
Syntax
| fault-monitor    | profile <profile-name> |     |     |     |
| ---------------- | ---------------------- | --- | --- | --- |
| no fault-monitor | profile <profile-name> |     |     |     |
Description
Createsafaultmonitoringprofile.Youcancreatemaximumof16faultmonitoringprofilestomonitor
differenttypesofinterfaces.
Thenoformofthiscommanddeletesthefaultmonitoringprofile.
Commandcontext
config
Parameters
<profile-name>
Specifiesthefaultmonitorprofilename.Profilenameacceptsthespecialcharactersandthenamemust
notexceed64characters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Creatingafaultmonitorprofile:
FaultMonitor|319

switch(config)# fault-monitor profile noisy-ports
switch(config-fault-monitor-profile)#

Deleting a fault monitor profile:

switch(config)# no fault-monitor profile noisy-ports
switch(config)#

Commands for enabling and disabling the faults

Syntax

all | excessive-oversize-packets | excessive-jabbers | excessive-fragments |
excessive-crc-errors | excessive-tx-drops | excessive-link-flaps | excessive-broadcasts |
excessive-multicasts | excessive-collisions | excessive-late-collisions

no all | excessive-oversize-packets | excessive-jabbers | excessive-fragments |
excessive-crc-errors | excessive-tx-drops | excessive-link-flaps | excessive-broadcasts |
excessive-multicasts | excessive-collisions | excessive-late-collisions

Description

Enables the faults for a profile.

If user has not configured threshold, action or auto-enable parameters, then this command enables fault with the

default values.

By default, the faults are disabled in a profile. Configuring threshold, action, or auto-enable will not enable the

fault.

The no form of this command disables the faults for a profile.

Command context

config-fault-monitor-profile

Parameters

all

Enables all the faults for a profile.

excessive-oversize-packets

Enables excessive oversize packets fault for a profile.

excessive-jabbers

Enables excessive jabbers fault for a profile.
excessive-fragments

Enables excessive fragments fault for a profile.

excessive-crc-errors

Enables excessive CRC errors fault for a profile.

excessive-tx-drops

Enables excessive transmit fault for a profile.

excessive-link-flaps

Enables excessive link flaps fault for a profile.

excessive-broadcasts

Enables excessive broadcasts fault for a profile.

excessive-multicasts

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

320

Enablesexcessivemulticastsfaultforaprofile.
excessive-collisions
Enablesexcessivecollisionsfaultforaprofile.
excessive-late-collisions
Enablesexcessivelatecollisionsfaultforaprofile.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingthefaultsforaprofile:
switch(config-fault-monitor-profile)# all
switch(config-fault-monitor-profile)# excessive-oversize-packets
switch(config-fault-monitor-profile)# excessive-jabbers
switch(config-fault-monitor-profile)# excessive-fragments
switch(config-fault-monitor-profile)# excessive-crc-errors
switch(config-fault-monitor-profile)# excessive-tx-drops
switch(config-fault-monitor-profile)# excessive-link-flaps
switch(config-fault-monitor-profile)# excessive-broadcasts
switch(config-fault-monitor-profile)# excessive-multicasts
switch(config-fault-monitor-profile)# excessive-collisions
switch(config-fault-monitor-profile)# excessive-late-collisions
Disablingthefaultsforaprofile:
| switch(config-fault-monitor-profile)# |     | no all |     |     |
| ------------------------------------- | --- | ------ | --- | --- |
switch(config-fault-monitor-profile)# no excessive-oversize-packets
| switch(config-fault-monitor-profile)# |     | no excessive-jabbers    |     |     |
| ------------------------------------- | --- | ----------------------- | --- | --- |
| switch(config-fault-monitor-profile)# |     | no excessive-fragments  |     |     |
| switch(config-fault-monitor-profile)# |     | no excessive-crc-errors |     |     |
| switch(config-fault-monitor-profile)# |     | no excessive-tx-drops   |     |     |
| switch(config-fault-monitor-profile)# |     | no excessive-link-flaps |     |     |
| switch(config-fault-monitor-profile)# |     | no excessive-broadcasts |     |     |
| switch(config-fault-monitor-profile)# |     | no excessive-multicasts |     |     |
| switch(config-fault-monitor-profile)# |     | no excessive-collisions |     |     |
switch(config-fault-monitor-profile)# no excessive-late-collisions
| Commands    | for applying | or changing | the action | and configuring |
| ----------- | ------------ | ----------- | ---------- | --------------- |
| auto-enable | for a fault  |             |            |                 |
Syntax
[all | excessive-oversize-packets | excessive-jabbers | excessive-fragments |
excessive-crc-errors | excessive-tx-drops | excessive-link-flaps | excessive-broadcasts |
excessive-multicasts | excessive-collisions | excessive-late-collisions ]
| [action {notify | | notify-and-disable | [auto-enable | <timeout>]}] |     |
| --------------- | -------------------- | ------------ | ------------ | --- |
no [all | excessive-oversize-packets | excessive-jabbers | excessive-fragments |
excessive-crc-errors | excessive-tx-drops | excessive-link-flaps | excessive-broadcasts |
excessive-multicasts | excessive-collisions | excessive-late-collisions ]
| [action {notify | | notify-and-disable | [auto-enable]}] |     |     |
| --------------- | -------------------- | --------------- | --- | --- |
Description
Appliesanactionandconfigurestheauto-enabletimerforthefault.Defaultaction:notifywithauto-
enabletimerdisabled.
FaultMonitor|321

The no form of this command removes the action and auto-enable timer for the fault.

Command context

config-fault-monitor-profile

Parameters

notify

Specifies the action as notify for the faults. Notifies through events, DLOGs, and SNMP trap. It is
enabled by default.

notify-and-isable

Specifies the action as notify-and-disable for the faults. Notifies through events, DLOGs, and SNMP
trap, and then disables the port.

auto-enable <timeout>

Re-enables the port automatically after the specified time. Specifies the time value in seconds. Time
range: 1-604800 seconds.

The fault parameter values are saved in the database even after the fault is disabled from the profile. These

values are used when you enable the fault in the profile again.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring notify-and-disable action for the faults:

switch(config-fault-monitor-profile)# all action notify-and-disable
switch(config-fault-monitor-profile)# excessive-oversize-packets action notify-and-
disable
switch(config-fault-monitor-profile)# excessive-jabbers action notify-and-disable
switch(config-fault-monitor-profile)# excessive-late-collisions action notify-and-
disable

Configuring notify action for the faults:

switch(config-fault-monitor-profile)# all action notify
switch(config-fault-monitor-profile)# excessive-oversize-packets action notify
switch(config-fault-monitor-profile)# excessive-jabbers action notify
switch(config-fault-monitor-profile)# excessive-collisions action notify

Configuring notify-and-disable action with auto-enable timer for the faults:

switch(config-fault-monitor-profile)# excessive-oversize-packets action notify-and-
disable auto-enable 80
switch(config-fault-monitor-profile)# excessive-jabbers action notify-and-disable
auto-enable 100
switch(config-fault-monitor-profile)# excessive-collisions action notify-and-disable
auto-enable 70

Changing the fault action to default:

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

322

switch(config-fault-monitor-profile)# no excessive-oversize-packets action
switch(config-fault-monitor-profile)#
|     |     | no  | excessive-jabbers | action |
| --- | --- | --- | ----------------- | ------ |
Removingtheauto-enabletimerconfigurationforthefault:
switch(config-fault-monitor-profile)# no all action notify-and-disable auto-enable
switch(config-fault-monitor-profile)# no excessive-jabbers action notify-and-disable
auto-enable
| Commands | for configuring | the threshold | for the | fault |
| -------- | --------------- | ------------- | ------- | ----- |
Syntax
excessive-jabbers | excessive-crc-errors | excessive-oversize-packets |
excessive-fragments | excessive-tx-drops | excessive-collisions |
excessive-late-collisions
no excessive-jabbers | excessive-crc-errors | excessive-oversize-packets |
excessive-fragments | excessive-tx-drops | excessive-collisions |
| excessive-late-collisions | {threshold} |                |     |     |
| ------------------------- | ----------- | -------------- | --- | --- |
| excessive-link-flaps      | {threshold  | count <count>} |     |     |
no excessive-link-flaps {threshold}
excessive-broadcasts | excessive-multicasts {threshold [percent <value> | pps <value>]}
| no excessive-broadcasts | | excessive-multicasts |     | {threshold} |     |
| ----------------------- | ---------------------- | --- | ----------- | --- |
Description
Configuresandchangesthefaultthresholdvaluefortheprofile.
Thenoformofthiscommandsetsthethresholdtoitsdefaultvalue.
Commandcontext
config-fault-monitor-profile
Parameters
| threshold value | <value> |     |     |     |
| --------------- | ------- | --- | --- | --- |
Specifiesthefaultthresholdvalue.Defaultthresholdvalue:25.
| threshold count | <value> |     |     |     |
| --------------- | ------- | --- | --- | --- |
Specifiesthefaultthresholdcount.Defaultthresholdcount:7.
| threshold percent | <value> |     |     |     |
| ----------------- | ------- | --- | --- | --- |
Specifiesthefaultthresholdbandwidthpercentage.Range:1to100.Defaultthresholdpercent:5.
| threshold pps | <value> |     |     |     |
| ------------- | ------- | --- | --- | --- |
SpecifiesthefaultthresholdPPS.Range:1-195312500.
Ifexcessive-broadcastorexcessive-multicastfaultsareconfiguredwiththethresholdhigherthantherate-
limitthreshold,thefollowingoccurs:
Faultreportingstillhappensastheporthasactuallyreceivedpacketsataratethatviolateditsthreshold.
n
Trafficgetsshapedasperrate-limitconfigurationandanypacketexceedingtherate-limitthreshold
n
getsdropped.
Thesetwofault-monitoringandrate-limitingfeaturesareorthogonaltooneanother.
Authority
FaultMonitor|323

Administrators or local user group members with execution rights for this command.

Examples

Configuring the excessive jabbers, oversize packets, CRC, fragments, and TX faults with threshold value:

switch(config-fault-monitor-profile)# excessive-jabbers threshold value 30
switch(config-fault-monitor-profile)# excessive-oversize-packets threshold value 40
switch(config-fault-monitor-profile)# excessive-crc-errors threshold value 35
switch(config-fault-monitor-profile)# excessive-fragments threshold value 50
switch(config-fault-monitor-profile)# excessive-tx-drops threshold value 20
switch(config-fault-monitor-profile)# excessive-collisions threshold value 40
switch(config-fault-monitor-profile)# excessive-late-collisions threshold value 30

Configuring the excessive link flaps fault with threshold count:

switch(config-fault-monitor-profile)# excessive-link-flaps threshold count 10

Configuring the excessive broadcasts and multicasts faults with threshold:

switch(config-fault-monitor-profile)# excessive-broadcasts threshold percent 40
switch(config-fault-monitor-profile)# excessive-broadcasts threshold pps 400000
switch(config-fault-monitor-profile)# excessive-multicasts threshold percent 10
switch(config-fault-monitor-profile)# excessive-multicasts threshold pps 10000

Removing the configured threshold value for the faults:

switch(config-fault-monitor-profile)# no excessive-jabbers threshold
switch(config-fault-monitor-profile)# no excessive-oversize-packets threshold
switch(config-fault-monitor-profile)# no excessive-crc-errors threshold
switch(config-fault-monitor-profile)# no excessive-fragments threshold
switch(config-fault-monitor-profile)# no excessive-tx-drops threshold
switch(config-fault-monitor-profile)# no excessive-link-flaps threshold
switch(config-fault-monitor-profile)# no excessive-broadcasts threshold
switch(config-fault-monitor-profile)# no excessive-multicasts threshold
switch(config-fault-monitor-profile)# no excessive-late-collisions threshold

Command for applying a fault monitoring profile to a port

Syntax

apply fault-monitor profile <profile-name>
no apply fault-monitor profile <profile-name>

Description

Configures the fault monitoring profile to an interface. The profile is allowed to be modified after it is
applied on a port.

The no form of this command removes the fault monitoring profile from an interface.

Command context

config-if

Parameters

<profile-name>

AOS-CX 10.07 Security Guide (6200, 6300, 6400 Switch Series)

324

Specifiesthefaultmonitorprofilename.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuringthefaultmonitoringprofiletoaninterface:
| switch(config)#    |     | interface 1/1/1     |                     |     |
| ------------------ | --- | ------------------- | ------------------- | --- |
| switch(config-if)# |     | apply fault-monitor | profile noisy-ports |     |
Configuringthefaultmonitoringprofiletoaspecifiedrangeofinterfaces:
| switch(config)#    |         | interface 1/1/2-1/1/24 |                     |             |
| ------------------ | ------- | ---------------------- | ------------------- | ----------- |
| switch(config-if)# |         | apply fault-monitor    | profile quiet-ports |             |
| Command            | for     | configuring            | VSX synchronization | for a fault |
| monitoring         | profile |                        |                     |             |
Syntax
vsx-sync
no vsx-sync
Description
ConfiguresVSXsynchronizationforafaultmonitoringprofile.
ThenoformofthiscommandremovestheVSXsynchronizationforafaultmonitoringprofile.
Commandcontext
config-fault-monitor-profile
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ConfiguringVSXsynchronizationforafaultmonitoringprofile:
| switch(config-fault-monitor-profile)# |     |         | vsx-sync |     |
| ------------------------------------- | --- | ------- | -------- | --- |
| show fault-monitor                    |     | profile |          |     |
Syntax
| show fault-monitor |     | profile                |     |     |
| ------------------ | --- | ---------------------- | --- | --- |
| show fault-monitor |     | profile <profile-name> |     |     |
Description
Showsthefaultmonitoringprofileinformation.Thecommandwithouttheprofilenamedisplaysallthe
availablefaultmonitoringprofiles.
FaultMonitor|325

Parameters
<profile-name>
Specifiesthefaultmonitorprofilename.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Displayingthefaultmonitoringinformationforalltheprofilesavailableontheswitch:
| switch# show | fault-monitor | profile |     |     |     |
| ------------ | ------------- | ------- | --- | --- | --- |
-------------------------------------------------------------------------------
| Fault monitor | profile: | 'noisy-ports' |     |     |     |
| ------------- | -------- | ------------- | --- | --- | --- |
-------------------------------------------------------------------------------
Auto
| Fault |     | Enabled | Threshold | Action | Enable |
| ----- | --- | ------- | --------- | ------ | ------ |
-------------------------------------------------------------------------------
| excessive-broadcasts       |     | yes | 400000 pps | notify             | --  |
| -------------------------- | --- | --- | ---------- | ------------------ | --- |
| excessive-multicasts       |     | yes | 10 percent | notify             | --  |
| excessive-link-flaps       |     | yes | 10         | notify             | --  |
| excessive-oversize-packets |     | yes | 40         | notify-and-disable | 80  |
| excessive-jabbers          |     | yes | 30         | notify-and-disable | 100 |
| excessive-fragments        |     | yes | 50         | notify             | --  |
| excessive-crc-errors       |     | yes | 35         | notify             | --  |
| excessive-tx-drops         |     | yes | 20         | notify             | --  |
| excessive-collisions       |     | yes | 40         | notify             | 70  |
| excessive-late-collisions  |     | yes | 30         | notify-and-disable | --  |
-------------------------------------------------------------------------------
| Fault monitor | profile: | 'quiet-ports' |     |     |     |
| ------------- | -------- | ------------- | --- | --- | --- |
-------------------------------------------------------------------------------
Auto
| Fault |     | Enabled | Threshold | Action | Enable |
| ----- | --- | ------- | --------- | ------ | ------ |
-------------------------------------------------------------------------------
| excessive-broadcasts       |     | yes | 300000 pps | notify             | --  |
| -------------------------- | --- | --- | ---------- | ------------------ | --- |
| excessive-multicasts       |     | yes | 100000 pps | notify             | --  |
| excessive-link-flaps       |     | yes | 20         | notify-and-disable | 45  |
| excessive-oversize-packets |     | yes | 25         | notify-and-disable | 20  |
| excessive-jabbers          |     | yes | 30         | notify             | --  |
| excessive-fragments        |     | yes | 60         | notify             | --  |
| excessive-crc-errors       |     | yes | 25         | notify-and-disable | 30  |
| excessive-tx-drops         |     | yes | 30         | notify             | --  |
Displayingthefaultmonitoringdetailsforaparticularprofile:
| switch# show | fault-monitor | profile | noisy-ports |     |     |
| ------------ | ------------- | ------- | ----------- | --- | --- |
-------------------------------------------------------------------------------
| Fault monitor | profile: | 'noisy-ports' |     |     |     |
| ------------- | -------- | ------------- | --- | --- | --- |
-------------------------------------------------------------------------------
Auto
| Fault |     | Enabled | Threshold | Action | Enable |
| ----- | --- | ------- | --------- | ------ | ------ |
-------------------------------------------------------------------------------
| excessive-broadcasts       |     | yes | 400000 pps | notify             | --  |
| -------------------------- | --- | --- | ---------- | ------------------ | --- |
| excessive-multicasts       |     | yes | 10 percent | notify             | --  |
| excessive-link-flaps       |     | yes | 10         | notify             | --  |
| excessive-oversize-packets |     | yes | 40         | notify-and-disable | 80  |
| excessive-jabbers          |     | yes | 30         | notify-and-disable | 100 |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 326

| excessive-fragments       |               | yes | 50      |     |     | notify             | --  |
| ------------------------- | ------------- | --- | ------- | --- | --- | ------------------ | --- |
| excessive-crc-errors      |               | yes | 35      |     |     | notify             | --  |
| excessive-tx-drops        |               | yes | 20      |     |     | notify             | --  |
| excessive-collisions      |               | yes | 40      |     |     | notify             | 70  |
| excessive-late-collisions |               | yes | 30      |     |     | notify-and-disable | --  |
| show interface            | fault-monitor |     | profile |     |     |                    |     |
Syntax
| show interface | [<IF-NAME>|<IF-RANGE>] |     | fault-monitor |     | profile |     |     |
| -------------- | ---------------------- | --- | ------------- | --- | ------- | --- | --- |
Description
Showsthefaultmonitoringprofileconfiguredfortheparticularinterface,rangeofinterfaces,orallthe
interfaces.
Parameters
<IF-NAME>
Specifiestheinterfacename.
<IF-RANGE>
Specifiestheinterfacerange.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Displayingalltheinterfacesconfiguredwiththefaultmonitoringprofiles:
| switch# | show interface | fault-monitor | profile |     |     |     |     |
| ------- | -------------- | ------------- | ------- | --- | --- | --- | --- |
--------------------------------------------------------------------------
| Port | Fault Monitor | Profile |     |     |     |     |     |
| ---- | ------------- | ------- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------
| 1/1/1 | noisy-ports |     |     |     |     |     |     |
| ----- | ----------- | --- | --- | --- | --- | --- | --- |
| 1/1/2 | quiet-ports |     |     |     |     |     |     |
| 1/1/4 | quiet-ports |     |     |     |     |     |     |
| 1/1/5 | noisy-ports |     |     |     |     |     |     |
| 1/1/6 | noisy-ports |     |     |     |     |     |     |
| 1/1/7 | quiet-ports |     |     |     |     |     |     |
Displayingthelistorrangeofinterfacesconfiguredwiththefaultmonitoringprofiles:
| switch# | show interface | 1/1/1-1/1/2,1/1/6 |     | fault-monitor |     | profile |     |
| ------- | -------------- | ----------------- | --- | ------------- | --- | ------- | --- |
--------------------------------------------------------------------------
| Port | Fault Monitor | Profile |     |     |     |     |     |
| ---- | ------------- | ------- | --- | --- | --- | --- | --- |
--------------------------------------------------------------------------
| 1/1/1          | noisy-ports   |     |        |     |     |     |     |
| -------------- | ------------- | --- | ------ | --- | --- | --- | --- |
| 1/1/2          | quiet-ports   |     |        |     |     |     |     |
| 1/1/6          | noisy-ports   |     |        |     |     |     |     |
| show interface | fault-monitor |     | status |     |     |     |     |
Syntax
| show interface | [<IF-NAME>|<IF-RANGE>] |     | fault-monitor |     | status |     |     |
| -------------- | ---------------------- | --- | ------------- | --- | ------ | --- | --- |
FaultMonitor|327

Description
Showstheactivefaultmonitoringprofileconfiguredfortheparticularinterface,rangeofinterfaces,orall
theinterfaces.
Parameters
<IF-NAME>
Specifiestheinterfacename.
<IF-RANGE>
Specifiestheinterfacerange.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Displayingactivefaultinformationforalltheinterfacesconfiguredwiththefaultmonitoringprofiles:
| switch# show | interface | fault-monitor | status        |      |       |      |
| ------------ | --------- | ------------- | ------------- | ---- | ----- | ---- |
|              |           |               |               |      | Port  | Time |
| Port Fault   |           |               | Fault Elapsed | Time | State | Left |
--------------------------------------------------------------------------------
1/1/1 excessive-broadcasts Tue Apr 14 14:29:09 UTC 2020 down 60
| excessive-jabbers |     |     | Tue Apr | 15 14:29:09 UTC | 2020 -- | --  |
| ----------------- | --- | --- | ------- | --------------- | ------- | --- |
1/1/2 excessive-oversize-packets Tue Apr 16 14:29:09 UTC 2020 down --
Displayingactivefaultinformationforthelistorrangeofinterfacesconfiguredwiththefaultmonitoring
profiles:
| switch# show | interface | 1/3/1,1/3/3 | fault-monitor | status |       |      |
| ------------ | --------- | ----------- | ------------- | ------ | ----- | ---- |
|              |           |             |               |        | Port  | Time |
| Port Fault   |           |             | Occurring     | Since  | State | Left |
--------------------------------------------------------------------------------
1/1/4 excessive-broadcasts Tue Apr 14 14:29:09 UTC 2020 down 60
| excessive-jabbers |     |     | Tue Apr | 15 14:29:09 UTC | 2020 -- | 100 |
| ----------------- | --- | --- | ------- | --------------- | ------- | --- |
show running-config
Syntax
show running-config
Description
Showstherunningconfigurationforthefaultmonitoringprofile.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Displayingrunningconfigurationforthefaultmonitoringprofiles:
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 328

| switch# show  | running-config |             |     |     |     |     |     |
| ------------- | -------------- | ----------- | --- | --- | --- | --- | --- |
| fault-monitor | profile        | noisy-ports |     |     |     |     |     |
excessive-broadcasts
| excessive-broadcasts |     |     | threshold | pps | 10000 |     |     |
| -------------------- | --- | --- | --------- | --- | ----- | --- | --- |
excessive-multicasts
| excessive-multicasts |     |     | threshold | pps | 10000 |     |     |
| -------------------- | --- | --- | --------- | --- | ----- | --- | --- |
excessive-link-flaps
| excessive-link-flaps |     |     | threshold | count | 7   |     |     |
| -------------------- | --- | --- | --------- | ----- | --- | --- | --- |
excessive-oversize-packets
| excessive-oversize-packets |     |     |     | threshold | value 40 |     |     |
| -------------------------- | --- | --- | --- | --------- | -------- | --- | --- |
excessive-jabbers
| excessive-jabbers |     | threshold |     | value | 30  |     |     |
| ----------------- | --- | --------- | --- | ----- | --- | --- | --- |
excessive-fragments
| excessive-fragments |     | threshold |     | value | 50  |     |     |
| ------------------- | --- | --------- | --- | ----- | --- | --- | --- |
excessive-crc-errors
| excessive-crc-errors |     |     | threshold | value | 35  |     |     |
| -------------------- | --- | --- | --------- | ----- | --- | --- | --- |
excessive-tx-drops
| excessive-tx-drops |     | threshold |     | value | 20  |     |     |
| ------------------ | --- | --------- | --- | ----- | --- | --- | --- |
excessive-collisions
| excessive-collisions |     |     | threshold | value | 40  |     |     |
| -------------------- | --- | --- | --------- | ----- | --- | --- | --- |
excessive-late-collisions
| excessive-late-collisions |       |         |     | threshold   | value 30 |     |     |
| ------------------------- | ----- | ------- | --- | ----------- | -------- | --- | --- |
| interface                 | 1/1/1 |         |     |             |          |     |     |
| apply fault-monitor       |       | profile |     | noisy-ports |          |     |     |
| show running-config       |       |         | all |             |          |     |     |
Syntax
| show running-config | all |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
Description
Showstherunningconfigurationwithalloptionsforthefaultmonitoringprofile.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Displayingrunningconfigurationwithoptionsforthefaultmonitoringprofile:
| switch# show  | running-config |             | all |     |     |     |     |
| ------------- | -------------- | ----------- | --- | --- | --- | --- | --- |
| fault-monitor | profile        | noisy-ports |     |     |     |     |     |
excessive-broadcasts
| excessive-broadcasts |     |     | threshold | pps                | 10000 |             |      |
| -------------------- | --- | --- | --------- | ------------------ | ----- | ----------- | ---- |
| excessive-broadcasts |     |     | action    | notify-and-disable |       | auto-enable | 2000 |
excessive-multicasts
| excessive-multicasts |     |     | threshold | pps    | 10000 |     |     |
| -------------------- | --- | --- | --------- | ------ | ----- | --- | --- |
| excessive-multicasts |     |     | action    | notify |       |     |     |
excessive-link-flaps
| excessive-link-flaps |     |     | threshold | count              | 7   |             |      |
| -------------------- | --- | --- | --------- | ------------------ | --- | ----------- | ---- |
| excessive-link-flaps |     |     | action    | notify-and-disable |     | auto-enable | 2000 |
no excessive-oversize-packets
| excessive-oversize-packets |     |     |     | threshold | value 40 |     |     |
| -------------------------- | --- | --- | --- | --------- | -------- | --- | --- |
| excessive-oversize-packets |     |     |     | action    | notify   |     |     |
no excessive-jabbers
| excessive-jabbers |     | threshold |        | value | 30  |     |     |
| ----------------- | --- | --------- | ------ | ----- | --- | --- | --- |
| excessive-jabbers |     | action    | notify |       |     |     |     |
FaultMonitor|329

no excessive-fragments
| excessive-fragments | threshold | value  | 50  |
| ------------------- | --------- | ------ | --- |
| excessive-fragments | action    | notify |     |
no excessive-crc-errors
| excessive-crc-errors | threshold | value  | 35  |
| -------------------- | --------- | ------ | --- |
| excessive-crc-errors | action    | notify |     |
no excessive-late-collisions
| excessive-late-collisions |     | threshold | value 30 |
| ------------------------- | --- | --------- | -------- |
| excessive-late-collisions |     | action    | notify   |
no excessive-collisions
| excessive-collisions | threshold | value  | 40  |
| -------------------- | --------- | ------ | --- |
| excessive-collisions | action    | notify |     |
no excessive-tx-drops
| excessive-tx-drops | threshold | value  | 20  |
| ------------------ | --------- | ------ | --- |
| excessive-tx-drops | action    | notify |     |
AOS-CX10.07SecurityGuide(6200,6300,6400SwitchSeries) 330

Chapter 20
|          |              |       | Auditors | and auditing | tasks |
| -------- | ------------ | ----- | -------- | ------------ | ----- |
| Auditors | and auditing | tasks |          |              |       |
Theauditorsgroupenablesadministratorstocreateusersthatcanperformauditingtaskswithoutallowing
thoseuserstheauthoritytovieworchangetheswitchconfiguration.
Asisthecaseforotherusers,auditorscanaccesstheswitchusingtheWebUI,RESTAPI,ortheCLI.
| Auditing | tasks | (CLI) |     |     |     |
| -------- | ----- | ----- | --- | --- | --- |
WhenyoulogontotheswitchCLIasauserwithauditorrights,youhaveaccesstotheauditorcommand
contextonly.
auditor>
Thetasksthatcanbeperformedbyauditorsareasfollows.Thecommandslistedaretheonlycommands
auditorscanexecuteotherthansessioncommandslikeprint,list,andexit.However,auditorscanuseall
commandoptionsexceptasnoted.Seethecommanddescriptionforeachcommandforcomplete
informationaboutthecommand.
| Task                   |     | Commandname     | Example                 |             |     |
| ---------------------- | --- | --------------- | ----------------------- | ----------- | --- |
| Showeventlogcontents   |     | show events     | show events             | -a -r       |     |
|                        |     |                 | show accounting         | log last 10 |     |
| Showlocalaccountinglog |     | show accounting |                         |             |     |
| contents               |     | log             |                         |             |     |
| Copycommandoutputtoa   |     | copy command-   | copy command-output     |             |     |
| remoteserverortoalocal |     | output          | "show events            | -a -r"      |     |
| USBdrive.              |     |                 | tftp://10.100.0.12/file |             |     |
Whenusingthecopy command-output command,userswithauditorrightscanspecifythefollowingcommands
only:
| show accounting | log |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
show events
| Auditing | tasks | (Web UI) |     |     |     |
| -------- | ----- | -------- | --- | --- | --- |
AuditorshaveaccesstotheLogpageonly.WhenyoulogontotheswitchWebUIasauserwithauditor
rights,theLogpageisdisplayed.
FromtheLogpage,youcanviewandexporteventlogentries.
TheWebUIdoesnotprovideaccesstotheaccountinglogs.
331
| AOS-CX10.07SecurityGuide| | (6200,6300,6400SwitchSeries) |     |     |     |     |
| ------------------------- | ---------------------------- | --- | --- | --- | --- |

REST requests and accounting logs
All REST requests—including GET requests—are logged to the accounting (audit) log.

The URI of the REST API resource for accounting logs is the following:
/rest/v10.04/logs/audit

In an accounting log entry for a REST request:

n service=https-server indicates that the log entry is a result of a REST API request or a Web UI action.

n The string value of data identifies the REST API request that was executed.

For more information about accounting log entries, see the description of the show accounting log CLI
command.

Auditors and auditing tasks | 332

Support and Other Resources

Chapter 21

Support and Other Resources

Accessing Aruba Support

Aruba Support Services

https://www.arubanetworks.com/support-services/

Aruba Support Portal

https://asp.arubanetworks.com/

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

Airheads social forums and Knowledge
Base

https://community.arubanetworks.com/

Software licensing

https://lms.arubanetworks.com/

End-of-Life information

https://www.arubanetworks.com/support-services/end-of-life/

Aruba software and documentation

https://asp.arubanetworks.com/downloads

Accessing Updates
You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

AOS-CX 10.07 Security Guide | (6200, 6300, 6400 Switch Series)

333

https://asp.arubanetworks.com/downloads

If you are unable to find your product in the Aruba Support Portal, you may need to search My Networking,
where older networking products can be found:

My Networking

https://www.hpe.com/networking/support

To view and update your entitlements, and to link your contracts and warranties with your profile, go to the
Hewlett Packard Enterprise Support Center More Information on Access to Support Materials page:

https://support.hpe.com/portal/site/hpsc/aae/home/

Access to some updates might require product entitlement when accessed through the Hewlett Packard
Enterprise Support Center. You must have an HP Passport set up with relevant entitlements.

Some software products provide a mechanism for accessing software updates through the product
interface. Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://asp.arubanetworks.com/notifications/subscriptions (requires an active Aruba Support Portal (ASP)
account to manage subscriptions). Security notices are viewable without an ASP account.

Warranty Information
To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Regulatory Information
To view the regulatory information for your product, view the Safety and Compliance Information for Server,
Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs, product
recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For more
information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation Feedback
Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

Support and Other Resources | 334