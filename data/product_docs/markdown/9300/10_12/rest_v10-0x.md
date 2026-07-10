AOS-CX 10.12 REST API Guide

All AOS-CX Series Switches

Published: August 2023
Edition: 2

Copyright Information

© Copyright 2023 Hewlett Packard Enterprise Development LP.

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

| 2

Contents
Contents
| Contents                             |                                            |             |          | 3   |
| ------------------------------------ | ------------------------------------------ | ----------- | -------- | --- |
| About                                | this document                              |             |          | 8   |
| Applicableproducts                   |                                            |             |          | 8   |
| Latestversionavailableonline         |                                            |             |          | 8   |
| Commandsyntaxnotationconventions     |                                            |             |          | 8   |
| Abouttheexamples                     |                                            |             |          | 9   |
| Identifyingswitchportsandinterfaces  |                                            |             |          | 10  |
| Identifyingmodularswitchcomponents   |                                            |             |          | 11  |
| Introduction                         | to                                         | the AOS-CX  | REST API | 12  |
| RESTAPIversions                      |                                            |             |          | 12  |
| RESTAPIaccessmodes                   |                                            |             |          | 15  |
|                                      | Read-writeaccessmode                       |             |          | 15  |
|                                      | Read-onlyaccessmode                        |             |          | 15  |
| RESTAPIURI                           |                                            |             |          | 15  |
|                                      | PartsofaURI                                |             |          | 15  |
|                                      | URIpath,includingpathparameters            |             |          | 16  |
|                                      | Querycomponent                             |             |          | 16  |
| Resources                            |                                            |             |          | 17  |
|                                      | Resourcecollectionsandsingletons           |             |          | 17  |
|                                      | Collections                                |             |          | 17  |
|                                      | Subcollections                             |             |          | 18  |
|                                      | Singletons                                 |             |          | 18  |
|                                      | Categoriesofresourceattributes             |             |          | 18  |
|                                      | Configurationattributes                    |             |          | 18  |
|                                      | Writableattributes                         |             |          | 19  |
|                                      | Statusattributes                           |             |          | 19  |
|                                      | Statisticsattributes                       |             |          | 19  |
|                                      | Attributecategoriesmightvary               |             |          | 19  |
| Enabling                             | Access                                     | to the REST | API      | 20  |
| Settingtheadminpassword              |                                            |             |          | 21  |
| ShowingtheRESTAPIaccessconfiguration |                                            |             |          | 21  |
| DisablingaccesstotheRESTAPI          |                                            |             |          | 21  |
| HTTPSservercommands                  |                                            |             |          | 22  |
|                                      | https-serverauthenticationcertificate      |             |          | 22  |
|                                      | https-serverauthenticationpassword         |             |          | 23  |
|                                      | https-servermax-user-sessions              |             |          | 24  |
|                                      | https-serverrestaccess-mode                |             |          | 25  |
|                                      | https-serverrestfirmware-site-distribution |             |          | 26  |
|                                      | https-serversessioncloseall                |             |          | 27  |
|                                      | https-serversession-timeout                |             |          | 27  |
|                                      | https-servervrf                            |             |          | 28  |
|                                      | showhttps-server                           |             |          | 29  |
|                                      | showhttps-serverauthentication             |             |          | 30  |
| Accessing                            | the                                        | AOS-CX REST | API      | 32  |
3
AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches)

| AuthenticatingRESTAPIsessions                     |                                                      |           |      | 32  |
| ------------------------------------------------- | ---------------------------------------------------- | --------- | ---- | --- |
| Usergroupsandaccessauthorization                  |                                                      |           |      | 33  |
| AOS-CX                                            | REST API                                             | Reference | (UI) | 35  |
| AccessingtheRESTAPIusingtheAOS-CXRESTAPIReference |                                                      |           |      | 35  |
|                                                   | LogginginandloggingoutusingtheAOS-CXRESTAPIReference |           |      | 35  |
| AOS-CXRESTAPIReferencebasics                      |                                                      |           |      | 36  |
|                                                   | AOS-CXRESTAPIReferencehomepage                       |           |      | 36  |
| Writemethods(POST,PUT,PATCH,andDELETE)            |                                                      |           |      | 40  |
|                                                   | Considerationswhenmakingconfigurationchanges         |           |      | 41  |
|                                                   | Considerationsforportsandinterfaces                  |           |      | 41  |
|                                                   | Hardware(system)interfaces                           |           |      | 41  |
|                                                   | LAGinterfaces                                        |           |      | 41  |
|                                                   | VLANinterfaces                                       |           |      | 42  |
|                                                   | Writemethods(POST,PUT)supportedinread-onlymode       |           |      | 42  |
| GETmethodusageandconsiderations                   |                                                      |           |      | 42  |
|                                                   | GETmethodparameters                                  |           |      | 42  |
|                                                   | Wildcardcharactersupport                             |           |      | 43  |
|                                                   | Attributesparameter                                  |           |      | 43  |
|                                                   | Countparameter                                       |           |      | 44  |
|                                                   | Depthparameter                                       |           |      | 44  |
|                                                   | Filterparameter                                      |           |      | 45  |
|                                                   | Selectorparameter                                    |           |      | 45  |
| POSTmethodusageandconsiderations                  |                                                      |           |      | 47  |
| PUTmethodusageandconsiderations                   |                                                      |           |      | 48  |
|                                                   | PUTrequestbodyrequirements                           |           |      | 48  |
|                                                   | PUTbehavior                                          |           |      | 48  |
|                                                   | ExceptionstothePUTstrictreplacebehavior              |           |      | 48  |
|                                                   | BestpracticeforbuildingthePUTrequestbody             |           |      | 49  |
| PATCHmethodusageandconsiderations                 |                                                      |           |      | 49  |
| DELETEmethodusageandconsiderations                |                                                      |           |      | 49  |
| RESTrequestsandaccountinglogs                     |                                                      |           |      | 49  |
| AOS-CXRESTAPIreferencesummary                     |                                                      |           |      | 50  |
|                                                   | SwitchRESTAPIaccessdefault                           |           |      | 50  |
|                                                   | SwitchRESTAPIdefaultaccessmode                       |           |      | 50  |
|                                                   | EnablingaccesstotheWebUIandRESTAPI                   |           |      | 50  |
|                                                   | SettingtheRESTAPIaccessmodetoread-write              |           |      | 50  |
|                                                   | ShowingtheRESTAPIaccessconfiguration                 |           |      | 50  |
|                                                   | AOS-CXRESTAPIReferenceURL:                           |           |      | 51  |
|                                                   | RESTAPIversionsandswitchsoftwareversions             |           |      | 51  |
|                                                   | GettingRESTAPIversioninformationfromaswitch          |           |      | 51  |
|                                                   | Protocol                                             |           |      | 51  |
|                                                   | Port                                                 |           |      | 51  |
|                                                   | Requestandresponsebodyformat                         |           |      | 51  |
|                                                   | Sessionidletimeout                                   |           |      | 51  |
|                                                   | Sessionhardtimeout                                   |           |      | 51  |
|                                                   | Authentication                                       |           |      | 51  |
|                                                   | HTTPSclientsessions                                  |           |      | 52  |
|                                                   | VSXpeerswitchaccess                                  |           |      | 52  |
| Using                                             | Curl Commands                                        |           |      | 53  |
| Aboutthecurlcommandexamples                       |                                                      |           |      | 53  |
| GettingtheRESTAPIversionsontheswitch              |                                                      |           |      | 54  |
| AccessingtheRESTAPIusingcurl                      |                                                      |           |      | 54  |
|                                                   | Logginginusingcurl                                   |           |      | 55  |
|                                                   | Passingthecookiebacktotheswitch                      |           |      | 56  |
Contents|4

|          | LoggingOutUsingCurl                                    |     |     | 57  |
| -------- | ------------------------------------------------------ | --- | --- | --- |
| Examples |                                                        |     |     | 58  |
|          | Example:GETmethod                                      |     |     | 58  |
|          | Example:GettinganddeletingcertificatesusingRESTAPIs    |     |     | 59  |
|          | Gettingalistofallcertificates                          |     |     | 59  |
|          | Gettingacertificate                                    |     |     | 59  |
|          | Deletingacertificate                                   |     |     | 60  |
|          | Example:Generatingaself-signedcertificateusingRESTAPIs |     |     | 60  |
Example:GettingandinstallingasignedleafcertificateusingRESTAPIs 61
Example:AssociatingaleafcertificatewithaswitchfeatureusingRESTAPIs 64
|                                       | Example:ConfigurationmanagementusingRESTAPIs        |               |            | 65  |
| ------------------------------------- | --------------------------------------------------- | ------------- | ---------- | --- |
|                                       | Downloadingaconfiguration                           |               |            | 65  |
|                                       | Downloadingthestartupconfiguration:                 |               |            | 65  |
|                                       | Uploadingaconfiguration                             |               |            | 66  |
|                                       | Copyingaconfiguration                               |               |            | 66  |
|                                       | Example:FirmwareupgradeusingRESTAPIs                |               |            | 67  |
|                                       | Uploadingafileasthesecondaryfirmwareimage           |               |            | 67  |
|                                       | Bootingthesystemusingthesecondaryfirmwareimage      |               |            | 67  |
|                                       | Example:LogoperationsusingRESTAPIs                  |               |            | 68  |
|                                       | Eventlogs                                           |               |            | 68  |
|                                       | Accounting(audit)logs                               |               |            | 68  |
|                                       | Example:PingoperationsusingRESTAPIs                 |               |            | 69  |
|                                       | Example:TracerouteoperationsusingRESTAPIs           |               |            | 69  |
|                                       | Example:UsermanagementusingRESTAPIs                 |               |            | 70  |
|                                       | Creatingauser                                       |               |            | 70  |
|                                       | Changingapassword                                   |               |            | 70  |
|                                       | Deletingauser                                       |               |            | 71  |
|                                       | Example:CreatinganACLwithaninterfaceusingRESTAPIs   |               |            | 71  |
|                                       | Example:CreatingaVLANandaVLANinterfaceusingRESTAPIs |               |            | 73  |
|                                       | Example:Enablingroutingonaninterface                |               |            | 74  |
|                                       | Example:PATCH Method                                |               |            | 75  |
|                                       | EnablingaVLAN                                       |               |            | 75  |
|                                       | EnablingCentral                                     |               |            | 75  |
|                                       | ChangingtheSourceIP ofaVRF                          |               |            | 75  |
|                                       | UsingGET andPATCH toUpdatetheadminstateofaVLAN      |               |            | 75  |
|                                       | UsingPATCH toUpdateaNon-configurableattribute       |               |            | 77  |
| AnyCLI                                |                                                     |               |            | 78  |
| Commandsavailableperplatform          |                                                     |               |            | 78  |
| CLIoperations                         |                                                     |               |            | 82  |
| CLIcommandsoperations                 |                                                     |               |            | 83  |
| Swagger                               |                                                     |               |            | 83  |
| FullURI                               |                                                     |               |            | 83  |
| CURLexample                           |                                                     |               |            | 83  |
| Errorcodes                            |                                                     |               |            | 83  |
| Allowedcommands                       |                                                     |               |            | 84  |
| Fullexample                           |                                                     |               |            | 87  |
| Secure                                | Mode                                                |               |            | 89  |
| Commandsavailableperplatform          |                                                     |               |            | 92  |
| VSX peer                              | switches                                            | and REST      | API access | 98  |
| Examplesofcurlcommands                |                                                     |               |            | 98  |
| Example:InteractingwithaVSXpeerswitch |                                                     |               |            | 99  |
| AOS-CX                                | real-time                                           | notifications | subsystem  | 101 |
5
AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches)

Secure WebSocket Protocol connections for notifications
Notification topics as switch resource URIs
Rules for topic URIs
Notification security features
AOS-CX real-time notifications subsystem reference summary

Connection protocol
Port
Message format
Message types
Authorization
Notification resource URI
Session idle timeout
Session hard timeout
Subscription persistence
Configuration maximums
Enabling the notifications subsystem on a switch
Establishing a secure WebSocket connection through a web browser
Establishing a secure WebSocket connection using a script
Subscribing to topics
Unsubscribing from topics
Subscription throttling
Parts of a subscribe message

Subscribe message example
Components of a subscribe message

Parts of a subscription success message
Example success message
Components of subscription success message
Components of a topic

Parts of a notification message

Notification message examples
Components of a notification message
Components of a topic

Example: Browser-based WebSocket connection

About the example
Example screen
Example HTML source

Example: Getting information about current subscribers

Troubleshooting

General troubleshooting tips

Connectivity
Resources, attributes, and behaviors
GET, PUT, PATCH, POST, and DELETE methods
Hardware and other features

REST API response codes
Error "'admin' password is not set"
Error "certificate verify failed" returned from curl command
HTTP 400 error "Invalid Operation"
HTTP 400 error "Value is not configurable" or "Bad Request"
HTTP 401 error "Authorization Required"

Solution 1
Solution 2

HTTP 401 error "Login failed: session limit reached"
HTTP 403 error "Forbidden" on a write request
HTTP 403 error "Forbidden" on a GET request
HTTP 404 error "Page not found" when accessing the switch URL

101
102
102
103
103
103
103
103
103
103
103
104
104
104
104
104
104
104
105
106
107
109
109
109
109
110
110
110
111
111
112
112
113
113
114
114
116

118
118
118
118
118
120
121
122
122
122
123
123
123
124
124
124
125
125

Contents | 6

HTTP404error"Objectnotfound"onobjectwith"ports/"or"interfaces/"inURIPath 126
HTTP404error"Objectnotfound"returnedfromaswitchthatsupportsmultipleRESTAPI
| versions(10.04andlater)                           |                    |           | 126 |
| ------------------------------------------------- | ------------------ | --------- | --- |
| HTTP404error"Objectnotfound"whenusingawritemethod |                    |           | 126 |
| HTTP404error"Pagenotfound"whenusingawritemethod   |                    |           | 127 |
| LogoutFails                                       |                    |           | 127 |
| Support                                           | and Other          | Resources | 128 |
| AccessingArubaSupport                             |                    |           | 128 |
| AccessingUpdates                                  |                    |           | 129 |
|                                                   | ArubaSupportPortal |           | 129 |
|                                                   | MyNetworking       |           | 129 |
| WarrantyInformation                               |                    |           | 129 |
| RegulatoryInformation                             |                    |           | 129 |
| DocumentationFeedback                             |                    |           | 130 |
7
AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches)

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 4100i Switch Series (JL817A, JL818A)

n Aruba 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A)

n Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A, R8Q68A, R8Q69A, R8Q70A,

R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A)

n Aruba 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B, R0X40C, R0X41A,
R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C, R0X26A, R0X27A,
JL741A)

n Aruba 8100 Switch Series (R9W94A, R9W95A, R9W96A, R9W97A)

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C, JL709C, JL710C, JL711C, JL704C, JL705C,
JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

n Aruba 8400 Switch Series (JL366A, JL363A, JL687A)

n Aruba 9300 Switch Series (R9A29A, R9A30A, R8Z96A)

n Aruba 10000 Switch Series (R8P13A, R8P14A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

Usage

example-text

Identifies commands and their options and operands, code examples,
filenames, pathnames, and output displayed in a command window. Items
that appear like the example text in the previous column are to be entered
exactly as shown and are required unless enclosed in brackets ([ ]).

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

8

Convention

Usage

example-text

In code and screen examples, indicates text entered by a user.

Any of the following:
n <example-text>
n <example-text>
n example-text

n example-text

|

{ }

[ ]

… or

...

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables
are enclosed in angle brackets (< >). Substitute the text—including
the enclosing angle brackets—with an actual value.

n For output formats where italic text can be displayed, variables

might or might not be enclosed in angle brackets. Substitute the
text including the enclosing angle brackets, if any, with an actual
value.

Vertical bar. A logical OR that separates multiple items from which you can
choose only one.
Any spaces that are on either side of the vertical bar are included for
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

About this document | 9

| Variable information |     | in CLI prompts |     |
| -------------------- | --- | -------------- | --- |
Incertainconfigurationcontexts,thepromptmayincludevariableinformation.Forexample,whenin
theVLANconfigurationcontext,aVLANnumberappearsintheprompt:
switch(config-vlan-100)#
Whenreferringtothiscontext,thisdocumentusesthesyntax:
switch(config-vlan-<VLAN-ID>)#
Where<VLAN-ID>isavariablerepresentingtheVLANnumber.
| Identifying | switch | ports and | interfaces |
| ----------- | ------ | --------- | ---------- |
Physicalportsontheswitchandtheircorrespondinglogicalsoftwareinterfacesareidentifiedusingthe
format:
member/slot/port
| On the 4100i | Switch | Series |     |
| ------------ | ------ | ------ | --- |
n member:Always1.VSFisnotsupportedonthisswitch.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4ontheswitch.
| On the 6000 | and 6100 | Switch Series |     |
| ----------- | -------- | ------------- | --- |
n member:Always1.VSFisnotsupportedonthisswitch.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4ontheswitch.
| On the 6200 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to8.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis
1.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4inslot1on
member1.
| On the 6300 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to10.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis
1.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4onmember1.
| On the 6400 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
10
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------ | ------------------------- | --- | --- |

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
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

About this document | 11

Introduction to the AOS-CX REST API

Chapter 2

Introduction to the AOS-CX REST API

The Aruba 6000 Switch Series and 6100 Switch Series only support the default VRF and has no management port.

Therefore, references in this guide to other VRFs or the management port do no apply to the 6000 switches and

6100 switches. Configuration for these switches should be done over an SVI having a physical port with access to

the SVI, since the physical ports in the 6000 and 6100 are not routed.

Switches running the AOS-CX software are fully programmable with a REST (REpresentational State
Transfer) API, allowing easy integration with other devices both on premises and in the cloud. This
programmability—combined with the Aruba Network Analytics Engine—accelerates network
administrator understanding of and response to network issues.

The AOS-CX REST API is a web service that performs operations on switch resources using HTTPS POST,
GET, PUT, PATCH, and DELETE methods.

The AOS-CX REST API enables programmatic access to the AOS-CX configuration and state database at
the heart of the switch. By using a structured model, changes to the content and formatting of the CLI
output do not affect the programs you write. The configuration is stored in a structured database,
instead of a text file, making it easier to roll back changes, and dramatically reducing the risk of
downtime and performance issues.

REST API versions
From AOS-CX release 10.04, the AOS-CX switches support access through multiple versions of the REST
API. The REST API versions supported on the AOS-CX switches are v10.04, v10.08, v10.09, v10.10, v10.11,
and v10.12. The REST API version v10.04 is supported from AOS-CX release 10.04 and later.

REST v1 is deactivated and no longer supported with AOS-CX 10.12

The version declared in the REST request must match one of the versions of the REST API supported on
the switch. The REST API version is included in the Uniform Resource Identifier (URI) used in REST
requests.

In the following example, the REST API version is v10.12:
https://192.0.2.5/rest/v10.12/latest/system

In the following example, the REST API version is v10.09:
https://192.0.2.5/rest/v10.09/system

In the following example, the REST API version is v10.04:
https://192.0.2.5/rest/v10.04/system

Compatibility

The following table shows the compatibility of AOS-CX switches with older REST API versions. To
maintain compatibility with older versions on new AOS-CX switches, old versions continue to be
published and use the same schema as the newest REST API version.

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

12

Switch Rest Rest v10.08 Rest v10.09 Rest v10.10 Rest v10.11 Rest v10.12
| series  | v10.04 API | API          | API      | API      | API | API |
| ------- | ---------- | ------------ | -------- | -------- | --- | --- |
| 6000    | Yes(with   | Yes(with     | Yes(with | Yes(with | Yes | Yes |
| (Rxxxx) | 10.12      | 10.12schema) | 10.12    | 10.12    |     |     |
|         | schema)    |              | schema)  | schema)  |     |     |
| 6100    | Yes        | Yes          | Yes      | Yes      | Yes | Yes |
(exceptfor
Rxxxx)
| 6100    | Yes(with | Yes(with     | Yes(with | Yes(with | Yes | Yes |
| ------- | -------- | ------------ | -------- | -------- | --- | --- |
| (Rxxxx) | 10.12    | 10.12schema) | 10.12    | 10.12    |     |     |
|         | schema)  |              | schema)  | schema)  |     |     |
| 6200    | Yes      | Yes          | Yes      | Yes      | Yes | Yes |
(exceptfor
JLxxxA)
| 6200       | Yes(with | Yes(with     | Yes(with | Yes(with | Yes | Yes |
| ---------- | -------- | ------------ | -------- | -------- | --- | --- |
| (JLxxxA)   | 10.12    | 10.12schema) | 10.12    | 10.12    |     |     |
|            | schema)  |              | schema)  | schema)  |     |     |
| 6300       | Yes      | Yes          | Yes      | Yes      | Yes | Yes |
| 6400       | Yes      | Yes          | Yes      | Yes      | Yes | Yes |
| 8100       | N/A      | N/A          | N/A      | N/A      | N/A | Yes |
| 8320       | Yes      | Yes          | Yes      | Yes      | Yes | Yes |
| 8325       | Yes      | Yes          | Yes      | Yes      | Yes | Yes |
| 8360       | Yes(with | Yes(with     | Yes      | Yes      | Yes | Yes |
| (Exceptfor | 10.12    | 10.12schema) |          |          |     |     |
| JL7xxC)    | schema)  |              |          |          |     |     |
| 8360       | Yes      | Yes          | Yes      | Yes      | Yes | Yes |
(JL7XXC)
| 8400  | Yes      | Yes | Yes | Yes | Yes | Yes |
| ----- | -------- | --- | --- | --- | --- | --- |
| 4100i | Yes(with | Yes | Yes | Yes | Yes | Yes |
10.12
schema)
| 6000 | Yes(with | Yes | Yes | Yes | Yes | Yes |
| ---- | -------- | --- | --- | --- | --- | --- |
10.12
schema)
| 8360     | Yes(with | Yes(with     | Yes | Yes | Yes | Yes |
| -------- | -------- | ------------ | --- | --- | --- | --- |
| (JL7XXC) | 10.12    | 10.12schema) |     |     |     |     |
schema)
| 9300  | Yes(with | Yes(with     | Yes(with | Yes | Yes | Yes |
| ----- | -------- | ------------ | -------- | --- | --- | --- |
|       | 10.12    | 10.12schema) | 10.12    |     |     |     |
|       | schema)  |              | schema)  |     |     |     |
| 10000 | Yes(with | Yes(with     | Yes      | Yes | Yes | Yes |
IntroductiontotheAOS-CXRESTAPI|13

Switch Rest Rest v10.08 Rest v10.09 Rest v10.10 Rest v10.11 Rest v10.12
| series | v10.04 API | API          | API | API | API | API |
| ------ | ---------- | ------------ | --- | --- | --- | --- |
|        | 10.12      | 10.12schema) |     |     |     |     |
schema)
ThefollowingtableshowsthestateofeachSwaggerUIpageperAOS-CXswitch.
| Switch   | Swagger    | Swagger    | Swagger    | Swagger    | Swagger | Swagger |
| -------- | ---------- | ---------- | ---------- | ---------- | ------- | ------- |
| series   | v10.04     | v10.08     | v10.09     | v10.10     | v10.11  | v10.12  |
| 6000     | Yes(sameas | Yes(sameas | Yes(sameas | Yes(sameas | Yes     | Yes     |
| (Rxxxxx) | 10.12)     | 10.12)     | 10.12)     | 10.12)     |         |         |
| 6100     | Yes        | Yes        | Yes        | Yes        | Yes     | Yes     |
(exceptfor
Rxxxx)
| 6100    | Yes(sameas | Yes(sameas | Yes(sameas | Yes(sameas | Yes | Yes |
| ------- | ---------- | ---------- | ---------- | ---------- | --- | --- |
| (Rxxxx) | 10.12)     | 10.12)     | 10.12)     | 10.12)     |     |     |
| 6200    | Yes        | Yes        | Yes        | Yes        | Yes | Yes |
(exceptfor
Rxxxx)
| 6200    | Yes(sameas | Yes(sameas | Yes(sameas | Yes(sameas | Yes | Yes |
| ------- | ---------- | ---------- | ---------- | ---------- | --- | --- |
| (Rxxxx) | 10.12)     | 10.12)     | 10.12)     | 10.12)     |     |     |
| 6300    | Yes        | Yes        | Yes        | Yes        | Yes | Yes |
| 6400    | Yes        | Yes        | Yes        | Yes        | Yes | Yes |
| 8100    | N/A        | N/A        | N/A        | N/A        | N/A | Yes |
| 8320    | Yes        | Yes        | Yes        | Yes        | Yes | Yes |
| 8325    | Yes        | Yes        | Yes        | Yes        | Yes | Yes |
| 8360    | Yes        | Yes        | Yes        | Yes        | Yes | Yes |
(JL7XXA)
| 8400  | Yes        | Yes | Yes | Yes | Yes | Yes |
| ----- | ---------- | --- | --- | --- | --- | --- |
| 4100i | Yes(sameas | Yes | Yes | Yes | Yes | Yes |
10.12)
| 6000 | Yes(sameas | Yes | Yes | Yes | Yes | Yes |
| ---- | ---------- | --- | --- | --- | --- | --- |
10.12)
| 8360     | Yes(sameas | Yes(sameas | Yes        | Yes | Yes | Yes |
| -------- | ---------- | ---------- | ---------- | --- | --- | --- |
| (JL7XXC) | 10.12)     | 10.12)     |            |     |     |     |
| 9300     | Yes(sameas | Yes(sameas | Yes(sameas | Yes | Yes | Yes |
|          | 10.12)     | 10.12)     | 10.12)     |     |     |     |
| 10000    | Yes(sameas | Yes(sameas | Yes        | Yes | Yes | Yes |
|          | 10.12)     | 10.12)     |            |     |     |     |
14
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |     |     |
| ------------------------ | ------------------------- | --- | --- | --- | --- | --- |

REST API access modes
The REST API supports two access modes:

n read-write (default)

n read-only

The default read-write access mode is not displayed in the show running-configuration command.
You can change the access mode to read-only using the https-server rest access-mode read-only CLI
command from the global configuration (config) context. You can validate the mode set using the show
https-server command.

Read-write access mode

In the read-write access mode:

n The AOS-CX REST API Reference shows most of the supported read and write methods for all switch

resources.

n The REST API can access and change every configurable aspect of the switch as modeled in the

configuration and state database.

The REST API is powerful, but must be used with extreme caution: For most values, no semantic

validation is performed on the data that you write to the database, and configuration errors can

destabilize the switch.

Read-only access mode

In the read-only access mode:

n Most switch resources support only GET methods, but some resources allow PUT or POST methods.

For example, you can use POST to log into the switch, use PUT to upload a new running
configuration, or use POST to upload a new firmware version.

n Read-only mode applies to all clients, including Aruba Central, Aruba Fabric Composer (AFC) and

NetEdit.

n For most switch resources, the AOS-CX REST API Reference does not show any write methods (POST,
PUT, PATCH, and DELETE) the resource might support. To show those write methods, read-write
mode must be enabled.

n A request to a read-only resource returns the code 405 Method Not Allowed.

n Once read-only mode is enabled, it can only be disabled through the switch command-line interface.

REST API URI
A switch resource is indicated by its Uniform Resource Identifier (URI). A URI is the location of a specific
web resource. A URI can be made up of several components, including the host name or IP address,
port number, the path, and an optional query string.

Parts of a URI

The two main parts of a URI are the path and the (optional) query component.

Introduction to the AOS-CX REST API | 15

URI path, including path parameters

The path is the part of the URI starting with the server URL and ending with the resource ID. In URIs that
have a query component, the path is everything before the question mark (?). The path has a hierarchy.
In a path, the forward slash (/) indicates the hierarchical relationship between resources.

Because the forward slash has a special meaning, the forward slash characters that are part of the URI
path must be percent-encoded with the code %2F, which represents the forward slash. For example, the
following URI represents the resource utilization for the management module in slot 1/5:
https://192.0.2.5/rest/v10.xx/system/subsystems/management_
module,1%2F5?attributes=resource_utilization

URI prefix

The URI prefix is the system URL and REST API version information. This information is specific to a
particular switch and REST API version, and is the same for every REST API request to that switch.

Script writers often create a variable for the URI prefix. Using a variable enables the writer to update a
script or use the same script logic for a different switch by updating the value of the URI prefix variable.

The URI prefix contains the following:

Server URL

The web server address of the switch.

Examples:

n https://192.0.2.5

n

n

https://10.17.0.1

https://myswitch.mycompany.com

If Virtual Switching Extension (VSX) is enabled, you can access most resources of the peer switch from
this switch by adding /vsx-peer in the URI path between the server URL and /rest. For more
information about VSX, see VSX peer switches and REST API access.

For example:
GET https://192.0.2.5/vsx-peer/rest/v10.xx/system/vsx?attributes=oper_status

REST API and version identifier

For example: /rest/v10.xx

Path parameters

A path parameter is a part of the URI path that can vary. Typically path parameters indicate a specific
instance of a resource in a collection, such as a specific VLAN in the vlans collection. The path can
contain several path parameters. Path parameters are indicated by braces {}.

For example, the AOS-CX REST API Reference displays the resource for specific VLAN as the following:
/system/vlans/{id}

When you send a request for VLAN 10, the URI you provide must substitute the VLAN ID, 10, for the {id}
query parameter. For example:
/system/vlans/10

In the AOS-CX REST API Reference, you enter the value of the path parameter in the Value field of the id
parameter.

Query component

In many cases, the unique identification of a resource requires a URI that contains both a path and a
query component. The query component is sometimes called the query string.

For example, CPU utilization is a resource represented by the following URI:

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

16

https://192.0.2.5/rest/v10.xx/system/subsystems/management_
module,1%2F5?attributes=resource_utilization

In a URI, the question mark (?) indicates the beginning of the query component. The query component
contains nonhierarchical data, and the format of the query string depends on the implementation of
the REST API.

The query component often contains "<key>=<value>" pairs separated by the ampersand (&) character.
Multiple attribute values are supported and are separated by commas. For example:
https://192.0.2.5/rest/v10.xx/system/vlans?depth=2&attributes=id,name,type

"Dot" notation for Network Analytics Engine URIs only

When a URI defines a monitor in an Aruba Network Analytics Engine (NAE) script, attribute values in the
query string support an additional dot notation that the Network Analytics Engine uses to access
additional information. For example:
https://192.0.2.5/rest/v10.09/system/subsystems/management_
module,1%2F5?attributes=resource_utilization.cpu

The dot notation is supported for certain URIs that define monitors only in NAE scripts.

Resources
In a REST API, the primary representation of data is called a resource. A resource is a representation of
an entity in the system as a URI. The entities can include hardware objects, statistical information,
configuration information, and status information. The URI might or might not include a query
component. Resources are nouns—anything that can be named can be a resource.

Examples of resources:

n The resource utilization information:
https://192.0.0.5/rest/v10.xx/system/subsystems?attributes=resource_utilization

n The list of configured VLANs:
https://192.0.2.5/rest/v10.xx/system/vlans

n The list of all users:
https://192.0.2.5/rest/v10.xx/system/users

n The user with the ID: myadmin:
https://192.0.2.5/rest/v10.xx/system/users/myadmin

n The secondary firmware image:
https://192.0.2.5/rest/v10.xx/firmware?image=secondary

Resource collections and singletons

Collections

A collection is a directory of resources managed by the server. Typically, a resource collection contains
multiple resource instances and the collection name is in the plural form.

For example:

n

n

/system/vlans

/system/users

n /fullconfigs

A GET request to a collection returns the set of JSON objects representing the members of the
collection. The following curl example shows the GET request and response returned for the vlans
collection:

Introduction to the AOS-CX REST API | 17

$ curl -k GET -b /tmp/auth_cookie "https://192.0.2.5/rest/v10.04/system/vlans"
{
| "1": "/rest/v10.04/system/vlans/1", |                                 |     |
| ----------------------------------- | ------------------------------- | --- |
| "10":                               | "/rest/v10.04/system/vlans/10", |     |
| "20":                               | "/rest/v10.04/system/vlans/20"  |     |
}
EachURIinthelistrepresentsaconfiguredVLAN.
TogettheJSONdataforVLAN10,youmusteithersendtheGETrequesttotheURIrepresentingVLAN
10("/rest/v10.xx/system/vlans/10"),oryoumustusethedepthparametertoexpandthelistofURIs
inthevlanscollectiontogettheJSONdataforalltheVLANsinthecollection.
Subcollections
Asingleresourceinstancecanalsocontainsubcollectionsofresources.
n Inthefollowingexample,vlansisasubcollectionofthesystemresource:
/system/vlans
n Inthefollowingexample,routesisasubcollectionofthedefaultVRFresourceinstance:
/system/vrfs/default/routes
Singletons
Therearesomeresourcesthatcanonlyhaveoneinstance.Theseresourcesarecalledsingletonsand
theresourcecollectionnameisinthesingularform.
Forexample:
n /system
/system/vsx
n
n /firmware
Becausethereisonlyoneresourceinasingletoncollection,GETrequestsreturntheJSON
representationoftheresourceinsteadofaURIlistofoneitem.Inaddition,youdonotneedtosupplya
resourceIDintheURLofaGETrequest.Forexample,thefollowingGETrequesttothefirmwareURI
returnstheJSONdatathatrepresentsthefirmwareresource:
$ curl -k GET -b /tmp/auth_cookie "https://192.0.2.5/rest/v10.xx/firmware"
{
| "current_version":   | "TL.10.00.0006E-686-g4a43ab9", |     |
| -------------------- | ------------------------------ | --- |
| "primary_version":   | "TL.10.00.0006E-686-g4a43ab9", |     |
| "secondary_version": |                                | "", |
"default_image": "primary",
| "booted_image": | "primary" |     |
| --------------- | --------- | --- |
}
| Categories | of resource | attributes |
| ---------- | ----------- | ---------- |
Resourcescancontainmanyattributes,andtheyareorganizedintothefollowingcategoriestoenable
moreefficientmanagement:
| Configuration | attributes |     |
| ------------- | ---------- | --- |
Configurationattributesrepresentuser-owneddata.Althoughanattributemustbeinthe
configurationcategorytobemodifiedbyauser,notallattributesintheconfigurationcategorycan
bemodifiedaftertheresourceinstanceiscreated.Configurationattributesthatcannotbechanged
18
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |
| ------------------------ | ------------------------- | --- |

after the resource is created are called immutable attributes. This distinction matters when using a
PUT request, because immutable attributes cannot be included in the request body.

For example, a VLAN ID is an immutable attribute. You cannot change the ID of the VLAN after the
VLAN is created. The VLAN name, in contrast, is a mutable (writable) attribute. You can change the
VLAN name after the VLAN is created.

Writable attributes

Writable attributes are the subset of configuration attributes that are mutable. Writable attributes
can be modified by a user after the resource is created. When using the PUT method to modify a
resource, only writable attributes can be included in the request body.

In REST v10.04 and later versions, the GET method selector parameter includes a value of writable,
which enables you to get only the mutable configuration attributes of a resource.

Status attributes

Status attributes contain system-owned data such as the admin account and various status fields.
You cannot create or modify instances of attributes in this category.

Statistics attributes

Statistics attributes contain system-owned data such as counters. You cannot create or modify
instances of attributes in this category.

Attribute categories might vary

A given attribute need not necessarily be in the same category from resource to resource, or even
resource instance to resource instance. If the system owns an instance of a resource, attributes of that
resource (which might be configuration attributes if a user owns the resource instance) become status
attributes, which cannot be modified by users.

For example, a user can create VLANs. However, the system can also create VLANs. System-owned
VLANs have many attributes that are considered to be in the status category and not the configuration
category. The status category is used when the data is owned by the system and cannot be overwritten
by a user.

Often a resource has a single attribute that indicates whether the resource is owned by the system or
by a user. For example, for a VLAN, the type attribute indicates whether the VLAN was created by a
user.

When this indicator attribute indicates that the resource is owned by the system, the other attributes
that might have been in the configuration category are categorized as status attributes. Likewise, when
the indicator attribute indicates that the resource is owned by a user, the other configuration attributes
remain available for modification by users. In other words, the categories for other attributes on the
resource follow the indicator attribute.

Introduction to the AOS-CX REST API | 19

Enabling Access to the REST API

Chapter 3

Enabling Access to the REST API

The AOS-CX Web UI and AOS-CX real-time notifications subsystem rely on the REST API, therefore, all
three are enabled or disabled together.

To access the REST API, Web UI, or notifications subsystem, the HTTPS server must be enabled on the
specified VRF. The VRF you specify determines from which network the features can be accessed. You
can enable access on multiple VRFs, including user-defined VRFs, by entering the https-server vrf
command for each VRF on which you want to enable access.

Prerequisites

n You must be in the global configuration context: switch(config)#.

n For the password-based authentication, the password for the admin user must be configured on the

switch.

n For the certificate-based authentication method, the trust anchor (TA) profile is needed to validate

the client certificate. Also, a RADIUS server must be configured on the switch. For more information
on configuring certificates and managing certificates, see the AOS-CX Security Guide.

Procedure

Enable HTTPS server access for the specified VRF.

For example:

n To enable access on all data ports on the switch, specify the default VRF:

switch(config)# https-server vrf default

The Aruba 6000 Switch Series and 6100 Switch Series only supports the default VRF.

n To enable access on the OOBM port (management interface IP address), specify the management VRF

(not applicable to the 6000 and 6100):

switch(config)# https-server vrf mgmt

n To enable access on ports that are members of the VRF named vrfprogs, specify vrfprogs:

switch(config)# https-server vrf vrfprogs

In the case of password authentication, if the switch responds with the following error, the admin user
must have a valid password:
Failed to enable https-server on VRF mgmt. 'admin' password is not set

The switch is shipped from the factory with a default user named admin without a password. The admin
user must set a valid password before HTTPS servers can be enabled.

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

20

| Setting | the admin | password |     |
| ------- | --------- | -------- | --- |
UsethefollowingAPItologinastheadmin.
POST /rest/v10.xx/login?username=admin
Anewsessionisstartedandaresponsecode268isreturnedalongwiththemessage:"Session is
restricted. Administrator password must be set before continuing."
ThissessionisvalidonlytochangetheadminpasswordandlogoutfromtheRESTAPIUI.Anyotherrequestwill
| returnaForbidden | code | (403). |     |
| ---------------- | ---- | ------ | --- |
UsethefollowingAPItochangetheadminpassword.Ellipses(...)representdatanotincludedinthe
example.
PUT /rest/v10.xx/system/users/admin
{
...
| "password": | "<enter the | password>" |     |
| ----------- | ----------- | ---------- | --- |
...
}
Afterthepasswordischangedsuccessfully,thesessionrestrictionisremoved.
| Showing | the REST | API | access configuration |
| ------- | -------- | --- | -------------------- |
ToshowtheRESTAPIaccessconfiguration,inthemanagercontext(#)oftheCLI,entertheshow https-
servercommand.
Forexample:
| switch# | show https-server |               |     |
| ------- | ----------------- | ------------- | --- |
|         | HTTPS Server      | Configuration |     |
----------------------------
|     | VRF         | :      | mgmt, default |
| --- | ----------- | ------ | ------------- |
|     | REST Access | Mode : | read-write    |
TheAruba6000SwitchSeriesand6100SwitchSeriesonlysupportsthedefaultVRF.
ThecommandoutputliststheVRFsonwhichaccesstoRESTAPIisenabledandshowsthecurrentREST
APIaccessmode.
IfaccessisnotenabledonanyVRF,theVRFconfigurationisdisplayedas<none>.
Forexample:
| switch# | show https-server |               |     |
| ------- | ----------------- | ------------- | --- |
|         | HTTPS Server      | Configuration |     |
----------------------------
|           | VRF         | :      | <none>     |
| --------- | ----------- | ------ | ---------- |
|           | REST Access | Mode : | read-write |
| Disabling | access      | to the | REST API   |
EnablingAccesstotheRESTAPI|21

TheAOS-CXWebUIandAOS-CXreal-timenotificationssubsystemrelyontheRESTAPI,therefore,allthreeare
enabledordisabledtogether.
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
DisableHTTPSserveraccessforthespecifiedVRFbyusingthenoformofthehttps-server vrf
command.
Forexample,thefollowingcommanddisablesRESTAPIaccessontheswitchdataportsinthedefault
VRF:
| switch(config)# |     | no https-server | vrf default |
| --------------- | --- | --------------- | ----------- |
Youcanusetheshow https-servercommandtoshowthecurrentconfiguration:
| switch# | show   | https-server  |     |
| ------- | ------ | ------------- | --- |
| HTTPS   | Server | Configuration |     |
----------------------------
| VRF          |        | : mgmt            |             |
| ------------ | ------ | ----------------- | ----------- |
| REST         | Access | Mode : read-write |             |
| HTTPS        | server | commands          |             |
| https-server |        | authentication    | certificate |
https-server authentication certificate [authorization radius] [username {<CERT-FIELD>}]
Description
Enablesauthenticationusinganx509certificateforauthentication.Whenthisoptionisconfigured,the
https-serverusestheuserspecifiedcertificateforauthentication,andthespecifiedauthorization
mechanismisusedtoobtainthecorrespondinguserrole.Theusernameembeddedinthecertificateis
usedforauthorizationwitharemoteuserdatabase.
Enablingpasswordauthenticationistheonlywayofdisablingcertificateauthentication.
Onlyoneauthenticationmethodcanbeenabledatatime.Ifyouwanttodisablecertificate-basedauthentication,
thenthepassword-basedauthenticationmustbeenabled.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<AUTHORIZATION-RADIUS>
Specifiesthataftercertificateauthenticationsucceeds,insteadof
promptingforapassword,theHTTPSservercheckstheRADIUS
serveronlyforauthorization.
Whenthisparameterisomitted,authorization radiusisstill
theassumedactivesetting.
22
| AOS-CX10.12RESTAPIGuide| |     | (AllAOS-CXSeriesSwitches) |     |
| ------------------------ | --- | ------------------------- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<CERT-FIELD> Selectswhichcertificateusernamefieldistobeusedfor
authorization.
n Specifyuser_pincipal_nametousethecertificate
UserPrincipalName(UPN)field.Thisisthedefault.
n Specifycommon_nametousethecertificateCommonName
(CN)field.
Whenthisparameterisomitted,user_pincipal_nameis
assumed.
Example
Enablingauthenticationusingthecertificate:
switch(config)# https-server authentication certificate authorization radius
| username  | common_name |         |                    |
| --------- | ----------- | ------- | ------------------ |
| Command   | History     |         |                    |
| Release   |             |         | Modification       |
| 10.11     |             |         | Commandintroduced. |
| Command   | Information |         |                    |
| Platforms | Command     | context | Authority          |
config
4100i Administratorsorlocalusergroupmemberswithexecutionrights
| 6200 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
6300
6400
8100
8320
8325
8360
8400
9300
10000
| https-server | authentication |          | password |
| ------------ | -------------- | -------- | -------- |
| https-server | authentication | password |          |
Description
Enablesauthenticationusingusernameandpassword,whichcorrespondstothedefaultauthentication
mechanism.Enablingthepasswordauthenticationmodedisablesthecertificateauthenticationmode.
Onlyoneauthenticationmethodcanbeenabledatatime.
EnablingAccesstotheRESTAPI|23

Example
Enablingauthenticationusingthepassword:
switch(config)#
|           |             | https-server | authentication |                    | password |
| --------- | ----------- | ------------ | -------------- | ------------------ | -------- |
| Command   | History     |              |                |                    |          |
| Release   |             |              |                | Modification       |          |
| 10.11     |             |              |                | Commandintroduced. |          |
| Command   | Information |              |                |                    |          |
| Platforms | Command     | context      |                | Authority          |          |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6200
6300
6400
8100
8320
8325
8360
8400
9300
10000
| https-server |                   | max-user-sessions |               |     |     |
| ------------ | ----------------- | ----------------- | ------------- | --- | --- |
| https-server | max-user-sessions |                   | <SESSION-AMT> |     |     |
Description
SetsthemaximumamountofconcurrentopensessionsforanygivenuserthroughtheHTTPSserver.
Theamountofconcurrentopensessionsmayhaveanimpactonsystemperformance,soitis
recommendedtosetthisvaluetotheminimumnecessary.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<SESSION-AMT>
Specifiesthemaximumnumberofusersessionsallowed.
Default: 6.Maximumvalue: 8.
Example
Setthemaximumnumberofconcurrentusersessionstothemaximumof8:
| switch(config)# |         | https-server | max-user-sessions |     | 8   |
| --------------- | ------- | ------------ | ----------------- | --- | --- |
| Command         | History |              |                   |     |     |
24
| AOS-CX10.12RESTAPIGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------ | --- | ------------------------- | --- | --- | --- |

| Release   |             |     |         | Modification      |           |     |
| --------- | ----------- | --- | ------- | ----------------- | --------- | --- |
| 10.08     |             |     |         | Commandintroduced |           |     |
| Command   | Information |     |         |                   |           |     |
| Platforms | Command     |     | context |                   | Authority |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| https-server |      | rest        | access-mode |            |               |     |
| ------------ | ---- | ----------- | ----------- | ---------- | ------------- | --- |
| https-server | rest | access-mode |             | {read-only | | read-write} |     |
Description
ChangestheRESTAPIaccessmode.Thedefaultmodeisread-write.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
read-write
Selectstheread/writemode.AllowsPOST,PUT,PATCH,and
DELETEmethodstobecalledonallconfigurableelementsinthe
switchdatabase.
| read-only |     |     |     | Selectstheread-onlymode.Writeaccesstomostswitch |     |     |
| --------- | --- | --- | --- | ----------------------------------------------- | --- | --- |
resourcesthroughtheRESTAPIisdisabled.
Usage
Settingthemodetoread-writeontheRESTAPIallowsPOST,PUT,PATCH,andDELETEmethodstobe
calledonallconfigurableelementsintheswitchdatabase.
Bydefault,RESTAPIsinthedeviceareintheread-writemode.SomeswitchresourcesallowPOST,PUT,
PATCH,andDELETEregardlessofRESTAPImode.RESTAPIsthatarerequiredtosupporttheWebUIor
theNetworkAnalyticsEngineexposePOST,PUT,PATCH,orDELETEoperations,eveniftheRESTAPI
accessmodeissettoread-only.
TheRESTAPIinread/writemodeisintendedforusebyadvancedprogrammerswhohaveagood
understandingofthesystemschemaanddatarelationshipsintheswitchdatabase.
BecausetheRESTAPIinread/writemodecanaccesseveryconfigurableelementinthedatabase,itispowerfulbut
mustbeusedwithextremecaution:Nosemanticvalidationisperformedonthedatayouwritetothedatabase,
andconfigurationerrorscandestabilizetheswitch.
On6300switchesor6400switches,bydefault,theHTTPSserverisenabledinread-writemodeonthe
mgmtVRF.IfyouenabletheHTTPSserveronadifferentVRF,theHTTPSserverisenabledinread-only
mode.
Example
| switch(config)# |     | https-server |     | rest | access-mode | read-only |
| --------------- | --- | ------------ | --- | ---- | ----------- | --------- |
EnablingAccesstotheRESTAPI|25

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| https-server    | rest                            | firmware-site-distribution |     |
| --------------- | ------------------------------- | -------------------------- | --- |
| https-server    | rest firmware-site-distribution |                            |     |
| no https-server | rest firmware-site-distribution |                            |     |
Description
Enablesthefirmwaresitedistributionserver.
Thefirmwaresitedistributionallowsyoutouseaswitchtodistributeafirmwareimagefiletoother
switchesinthesamenetwork.Thispreventstheswitchesfromconnectingtothecloudoranexternal
networktodownloadafirmwareimagefile.
Onenablingthefirmwaresitedistribution,itexposesaRESTendpointthatallowstheswitchesto
downloadaswitchprimaryorsecondaryfirmwareimage.
Asperthelimitation,uptotwoswitchescandownloadthefirmwareimagesimultaneously.
ThisendpointistobeusedalongwithREST/firmwareendpointtohandlethefirmwaredownloadand
installationprocess.
Thenoformofthiscommanddisablesthefirmwaresitedistributionserver.
Example
Enablingthefirmwaresitedistributionserver:
switch(config)#
|     | https-server | rest | firmware-site-distribution |
| --- | ------------ | ---- | -------------------------- |
Disablingthefirmwaresitedistributionserver:
switch(config)# no https-server rest firmware-site-distribution
| Command History     |     |     |                   |
| ------------------- | --- | --- | ----------------- |
| Release             |     |     | Modification      |
| 10.10               |     |     | Commandintroduced |
| Command Information |     |     |                   |
26
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------ | ------------------------- | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| https-server | session | close     | all |
| ------------ | ------- | --------- | --- |
| https-server | session | close all |     |
Description
InvalidatesandclosesallHTTPSsessions.AllexistingWebUIandRESTsessionsareloggedoutandall
real-timenotificationfeatureWebSocketconnectionsareclosed.
Usage
Typically,auserthathasconsumedtheallowedconcurrentHTTPSsessionsandisunabletoaccessthe
sessioncookietologoutmanuallymustwaitforthesessionidletimeouttostartanothersession.This
commandisintendedasaworkaroundtowaitingfortheidletimeouttocloseanHTTPSsession.This
commandstopsandstartsthehpe-restdservice,sousingthiscommandaffectsallexistingREST
sessions,WebUIsessions,andreal-timenotificationsubscriptions.
Example
| switch#        | https-server | session close | all          |
| -------------- | ------------ | ------------- | ------------ |
| Command        | History      |               |              |
| Release        |              |               | Modification |
| 10.07orearlier |              |               | --           |
| Command        | Information  |               |              |
| Platforms      | Command      | context       | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| https-server | session-timeout |           |     |
| ------------ | --------------- | --------- | --- |
| https-server | session-timeout | <MINUTES> |     |
Description
Configuresthetimeout,inminutes,foranygivenHTTPSserversession.Avalueof0disablesthe
timeout.ThiscommanddoesnotaffectsessionsusedforCentralconnections.
| Parameter |     |     | Description                                     |
| --------- | --- | --- | ----------------------------------------------- |
| <MINUTES> |     |     | Specifiesthemaximumidletime,inminutesforanHTTPS |
session.Default: 20.Maximum: 480(8hours).0disablesthe
timeout,butthemaxiumisstillenforced.
EnablingAccesstotheRESTAPI|27

Example
| switch(config)#     | https-server | session-timeout |                   | 10  |
| ------------------- | ------------ | --------------- | ----------------- | --- |
| Command History     |              |                 |                   |     |
| Release             |              |                 | Modification      |     |
| 10.08               |              |                 | Commandintroduced |     |
| Command Information |              |                 |                   |     |
| Platforms           | Command      | context         | Authority         |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| https-server    | vrf            |     |     |     |
| --------------- | -------------- | --- | --- | --- |
| https-server    | vrf <VRF-NAME> |     |     |     |
| no https-server | vrf <VRF-NAME> |     |     |     |
Description
ConfiguresandstartstheHTTPSserveronthespecifiedVRF,allowingaccesstoRESTandtheWebUI
fromportsassignedtothatVRF.ThiscommanddoesnotaffectaccesstoCentralinstances,asthis
featurehasitsowndedicatedconnectionchannel
ThenoformofthecommandstopsanyHTTPSserversrunningonthespecifiedVRFandremovesthe
HTTPSserverconfiguration.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<VRF-NAME> SpecifiestheVRFname.Required.Length:Upto32alphanumeric
characters.
Usage
Byusingthiscommand,youenableaccesstoboththeWebUIandtotheRESTAPIonthespecifiedVRF.
YoucanenableaccessonmultipleVRFs.
Bydefault,8100,8320,8325,8360,8400,9300,and10000SwitchSerieshaveanHTTPSserverenabled
onthemgmtVRF.
Bydefault,the6200,6300,and6400SwitchSerieshaveanHTTPSserverenabledonthemgmtVRFand
onthedefaultVRF.
WhentheHTTPSserverisnotconfiguredandrunning,attemptstoaccesstheWebUIorRESTAPIresult
| in404 Founderrors. |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
Not
TheVRFyouselectdeterminesfromwhichnetworktheWebUIandRESTAPIcanbeaccessed.
Forexample:
n IfyouwanttoenableaccesstotheRESTAPIandWebUIthroughtheOOBMport(managementIP
address),specifythebuilt-inmanagementVRF(mgmt).
28
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------ | ------------------------- | --- | --- | --- |

n IfyouwanttoenableaccesstotheRESTAPIandWebUIthroughthedataports(for"inband
management"),specifythebuilt-indefaultVRF(default).
n IfyouwanttoenableaccesstotheRESTAPIandWebUIthroughonlyasubsetofdataportsonthe
switch,specifyotherVRFsyouhavecreated.
ArubaNetworkAnalyticsEnginescriptsruninthedefaultVRF,butyoudonothavetoenableHTTPS
serveraccessonthedefaultVRFforthescriptstorun.IftheswitchhascustomArubaNetworkAnalytics
EnginescriptsthatrequireaccesstotheInternet,thenforthosescriptstoperformtheirfunctions,you
mustconfigureaDNSnameserveronthedefaultVRF.
Examples
Enablingaccessonallportsontheswitch,specifythedefaultVRF:
| switch(config)# | https-server | vrf | default |
| --------------- | ------------ | --- | ------- |
EnablingaccessontheOOBMport(managementinterfaceIPaddress),specifythemanagementVRF:
| switch(config)# | https-server | vrf | mgmt |
| --------------- | ------------ | --- | ---- |
EnablingaccessonportsthataremembersoftheVRFnamedvrfprogs,specifyvrfprogs:
| switch(config)# | https-server | vrf | vrfprogs |
| --------------- | ------------ | --- | -------- |
EnablingaccessonthemanagementportandportsthataremembersoftheVRFnamedvrfprogs,
entertwocommands:
| switch(config)# | https-server | vrf | mgmt     |
| --------------- | ------------ | --- | -------- |
| switch(config)# | https-server | vrf | vrfprogs |
The6200switchessupportonlytwoVRFs.OnemanagementVRFandonedefaultVRF.Youcannotaddanother
VRF.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show https-server
| show https-server | [vsx-peer] |     |     |
| ----------------- | ---------- | --- | --- |
EnablingAccesstotheRESTAPI|29

Description
ShowsthestatusandconfigurationoftheHTTPSserver.TheRESTAPIandwebuserinterfaceare
accessibleonlyonVRFsthathavetheHTTPSserverfeaturesconfigured.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
ShowstheconfigurationoftheHTTPSserverfeatures.
VRF
ShowstheVRFs,ifany,forwhichHTTPSserverfeaturesareconfigured.
| REST Access | Mode |     |     |     |
| ----------- | ---- | --- | --- | --- |
ShowstheconfigurationoftheRESTaccessmode:
read-write
POST,PUT,andDELETEmethodscanbecalledonallconfigurableelementsintheswitchdatabase.Thisisthe
defaultvalue.
read-only
WriteaccesstomostswitchresourcesthroughtheRESTAPIisdisabled.
Examples
| switch#      | show https-server |     |     |     |
| ------------ | ----------------- | --- | --- | --- |
| HTTPS Server | Configuration     |     |     |     |
----------------------------
| VRF                 |         | :    | default,   | mgmt         |
| ------------------- | ------- | ---- | ---------- | ------------ |
| REST Access         | Mode    | :    | read-write |              |
| Max sessions        | per     | user | : 6        |              |
| Session             | timeout |      | : 20       |              |
| Command History     |         |      |            |              |
| Release             |         |      |            | Modification |
| 10.07orearlier      |         |      |            | --           |
| Command Information |         |      |            |              |
| Platforms           | Command |      | context    | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show https-server |                |     | authentication |     |
| ----------------- | -------------- | --- | -------------- | --- |
| show https-server | authentication |     |                |     |
Description
30
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------ | ------------------------- | --- | --- | --- |

Showsthehttps-serverauthenticationmodestatus.
Examples
Showingtheauthenticationmethodwiththepasswordmodeenabled:
| switch#        | show https-server | authentication |     |
| -------------- | ----------------- | -------------- | --- |
| Authentication | Modes             | Status         |     |
----------------------------
| Password    | Status | : enabled  |     |
| ----------- | ------ | ---------- | --- |
| Certificate | Status | : disabled |     |
Showingtheauthenticationmethodwiththecertificatemodeenabled:
| switch#        | show https-server | authentication |     |
| -------------- | ----------------- | -------------- | --- |
| Authentication | Modes             | Status         |     |
----------------------------
| Password            | Status  | : disabled |                    |
| ------------------- | ------- | ---------- | ------------------ |
| Certificate         | Status  | : enabled  |                    |
| Command History     |         |            |                    |
| Release             |         |            | Modification       |
| 10.11               |         |            | CommandIntroduced. |
| Command Information |         |            |                    |
| Platforms           | Command | context    | Authority          |
4100i Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6200 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6300 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
6400
8100
8320
8325
8360
8400
9300
10000
EnablingAccesstotheRESTAPI|31

Accessing the AOS-CX REST API

Chapter 4

Accessing the AOS-CX REST API

You can access the REST API using any REST client interface that supports HTTPS requests, and supports
obtaining and passing a session cookie.

Examples of client interfaces include the following:

Scripts and programs that support HTTPS requests

A flexible way to access the AOS-CX REST API is to use a programming language that supports HTTPS
requests, such as Python, to write programs that automate network management tasks.

The curl command-line interface

You can use curl commands either interactively or within a script to make REST requests. Using curl
commands is a way to execute GET requests without writing a script. Using curl commands is a way
to test REST requests that you are considering to incorporate into an application.

Browser-based interfaces such as Postman or the AOS-CX REST API Reference

Examples of browser-based interfaces include Postman and the AOS-CX REST API Reference.

The AOS-CX REST API Reference documents the switch resources, parameters, and JSON models for
each HTTPS method supported by the resource. Because the AOS-CX REST API Reference is browser-
based, it can share the session cookie with a Web UI session active in another browser tab. The AOS-
CX REST API Reference is not intended to be used as a configuration tool and is not required for day-
to-day operations.

The AOS-CX REST API Reference is one way to execute GET requests without writing a script. The AOS-
CX REST API Reference can be used during script coding to help you construct the URIs—with their
query parameters—that you use in a script or curl command.

Authenticating REST API sessions
When you start a REST API session, you use the POST method to access the login resource of the switch
and pass the username and password information as data. Ensure that HTTPS is configured to use port
443. Requests to port 80 are redirected to port 443.

If the credentials are accepted, your authenticated session is started for that username, and the switch
returns a cookie containing encoded session information.

In subsequent calls to the API—including to the logout resource—the session cookie is passed back to
the switch.

The same session cookie is shared across browser tabs, and depending on the browser, multiple
browser windows. However, the same session cookie is not shared across devices and scripts. For
example, if a user logs into the Web UI from a laptop, again with a tablet, and then uses the same user
name in a curl command, that user has three concurrent client sessions.

The maximum number of concurrent HTTPS sessions per user per switch is eight. There is an upper limit of 48

total sessions per switch. It is a best practice to log out of HTTPS sessions when you are finished using them.

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

32

HTTPS sessions will automatically time out after 20 minutes of inactivity, and have a hard time limit of
eight hours, regardless of whether the session is active. You can run the https-server session close
all command to close all current HTTPS sessions. For more information about using the command, see
https-server session close all .

Authentication through methods other than the session cookie, such as OAuth or certificates, is not
supported. The server uses self-signed certificates.

The procedure to pass the session cookie back and forth from the switch depends on how you access
the REST API.

For example:

n If you log in to the REST API using the AOS-CX REST API Reference or using the Web UI and open the
API Reference in another browser tab, the browser handles the session cookie for you. You do not
have to save or otherwise manage the session cookie.

n If you access the REST API using another method, such as the curl tool, you must do the following:

o Save the session cookie returned from the login request.

o Pass that saved cookie to the switch with every subsequent request you make to the REST API,

including the logout resource.

Although it is possible to pass the user name and password information as a query string in the

login URL, browser logs or tools outside the switch might save the accessed URL in cleartext in log

entries. Instead, Hewlett Packard Enterprise recommends that you pass the credential information

as data when using programs such as curl to log in to the switch.

For examples of accessing the REST API using curl, see Accessing the REST API using curl.

User groups and access authorization
For switch resources, the access authorization granted to a user is determined by the group to which
the user belongs. Each user group is assigned a number that represents a privilege level. This number is
used to represent the user group in logs and in places in which the group name is too long to display.

The following predefined user groups are supported:

User group

operators

administrators

auditors

Privilege
level

Description

1

15

19

Authorized for read access to non-sensitive data.

Authorized for read and write access to all switch

resources. Write access also requires that the REST API

is in read-write access mode.

Authorized for read access to audit log (/logs/audit)
and event log (/logs/event) resources only.

All users can access the POST method of the login and logout resources. However, the login requests
fail if the user is not a member of one of the predefined user groups. For example, login attempts fail
when attempted by a member of a user-defined local user group.

If a user attempts a request for which they are not authorized, the switch returns an HTTP 403
"Forbidden" error.

Accessing the AOS-CX REST API | 33

If an authorized user attempts a write request but the REST API is in read-only mode, the switch returns
an HTTP 404 "Page not found" error.

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

34

AOS-CX REST API Reference (UI)

Chapter 5

AOS-CX REST API Reference (UI)

The AOS-CX operating system includes the AOS-CX REST API Reference, which is a web interface based
on the Swagger 3.0 UI. For more information about Swagger, see https://swagger.io/.

The AOS-CX REST API Reference provides the reference documentation for REST API, including the switch
resources, parameters, errors, and JSON models for each HTTPS method supported by the resource. The
AOS-CX REST API Reference shows most of the supported read and write methods for all switch
resources.

Since the AOS-CX REST API Reference is browser-based, it can share the session cookie with a Web UI
session active in another browser tab. The AOS-CX REST API Reference is not intended to be used as a
configuration tool and is not required for day-to-day operations.

The AOS-CX REST API Reference is one way to execute HTTP requests like GET, PUT, POST, PATCH, and
DELETE, without writing a script. The AOS-CX REST API Reference can be used during script coding to
help you construct the URIs and data body (in the case of PATCH, POST, or PUT)—with their query
parameters—that you use in a script or curl command.

Accessing the REST API using the AOS-CX REST API Reference

Although the AOS-CX REST API Reference interacts directly with the REST API, the AOS-CX REST API
Reference is not intended as a management or configuration interface. Use caution when using the
Submit button for POST, PATCH, or PUT methods because this action can result in changes to your
current environment.

Prerequisites

n HTTPS server access must be enabled on the VRF from which you are accessing the switch.

n With a few exceptions, using the PUT, POST, PATCH, or DELETE methods require the following

conditions to be true:

o The REST API access mode must be set to read-write.

o The user name you use to log in must be a member of the administrators group.

Procedure

1. To view the reference documentation for the REST v10.xx API, access the following URL using a

browser: https://<IP-ADDR>/api/v10.xx/

<IP-ADDR> is the IP address or hostname of your switch.

For example: https://192.0.2.5/api/v10.xx/

Logging in and logging out using the AOS-CX REST API Reference

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

35

Prerequisites

n Access to the switch REST API must be enabled.

n You must have used a supported browser to access the switch at:

https://<IP-ADDR>/api/v10.xx/

<IP-ADDR> is the IP address or hostname of your switch.

Procedure

1. Log in to the switch using the Login resource:

1. Expand the Login section.

The POST method for the login resource is displayed.

2. Expand the resource by clicking POST or the resource name, /login.

3. Click Try it out.

4. Enter your user name in the User name field.

5. Enter your password in the Password field.

6. Click Execute.

If the operation is successful, the REST API returns response code 200.

2. When you finish your session, log out by expanding the Logout resource and clicking Execute.

AOS-CX REST API Reference basics
This section provides information about the different components of the AOS-CX REST API user
interface.

AOS-CX REST API Reference home page

The following is an example of a portion of the AOS-CX REST API Reference home page for a switch
running AOS-CX software:

AOS-CX REST API Reference (UI) | 36

n The link at the top of the page displays the JSON representation of the RESTful interface.

n The Servers drop-down lists the base URL to access the REST API.

n The switch resource URIs are organized in groups. The group names are listed in alphabetical order

on the AOS-CX REST API Reference home page.

The group name does not always match the resource collection name. Use the group names as a
navigation aid only.

n Group names that are in gray have the URI entries—also called endpoints—collapsed. When you
hover over the group name, it turns black. Click the group name to expand it and show the list of
methods and URIs in the group.

The following example shows the list of the methods and URIs in the Subsystem group:

n The methods that are shown might depend on the REST API access mode. Some methods might not

be displayed if the REST API access mode is read-only.

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

37

n Methods and resources might be displayed that you do not have the authorization to access. For
example, users with operator rights are not authorized to make PATCH, PUT, or POST requests to
most resources. If you submit a request for which you are not authorized, the switch returns the
following error: HTTP error 403 "Forbidden"

n The resource collection name is subsystems (not Subsystem).

n Items in braces, such as {type} and {name}, are path parameters. If you submit a request to a

resource URI that includes a path parameter, you are required to supply a value for the parameter.

To show more information about an item on the list, click the URI path. The following example shows a
part of the information displayed when GET on /system/subsystems is selected:

You can use the browser scroll bar to navigate to information about the implementation of this method
and resource, including the required and optional parameters. You must click Try it out to edit the
parameters.

n The required parameters are shown with * required.

For example, the POST method of the login resource requires a user name and password:

AOS-CX REST API Reference (UI) | 38

n Path parameters, such as {id}, are listed as required parameters:

n The Execute button sends the request. Click Cancel to exit the edit mode without sending the

request.

Although the AOS-CX REST API Reference interacts directly with the REST API, the AOS-CX REST API Reference is not

intended as a management or configuration interface. Use caution when using the Execute button for PATCH,

POST, or PUT methods because this action can result in changes to your current environment.

In GET requests, there can be multiple attributes and parameters you can use to filter results.

For example:

You can select multiple attributes:

n To select a range of attributes, click the first attribute, then press Shift, and then click the last

attribute in the range you want to select.

n To select attributes that are not adjacent in the list, press Ctrl, then click each attribute you want to

select.

The JSON model for the resource is described in Model and shown with example values in Example
Values for each method. The following example shows the JSON model and example values for PUT
method of the /system/subsystems/{type}/{name} resource:

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

39

Afterarequestissubmitted,theAOS-CXRESTAPIReferenceshowsadditionalinformation,including
thefollowing:
n Thecurlcommandequivalentofthesubmittedrequest
n ThesubmittedrequestURL,includingthespecifiedparametersandvalues.
n Theresponsebodyreturnedbytheswitch
n Theresponsecodereturnedbytheswitch
n Theresponseheadersreturnedbytheswitch
ThecurlcommandandrequestURLsaredisplayedusingpercentencodingforcertaincharactersinthe
querystringportionoftheURL:
| Character       | Percent-encoded | equivalent |     |
| --------------- | --------------- | ---------- | --- |
| ,(comma)        | %2C             |            |     |
| :(colon)        | %3A             |            |     |
| /(forwardslash) | %2F             |            |     |
Whenyouentercurlcommandsorsubmitrequeststhroughothermeans,percentencodingis
permittedbutnotrequiredinthequerystringoftheURI.
| Write methods | (POST, | PUT, PATCH, | and DELETE) |
| ------------- | ------ | ----------- | ----------- |
ThesupportedwritemethodsarePOST,PUT,PATCH,andDELETE:
n POSTcreatesaresource.
n PUTreplacesaresource.
n PATCH updatesaresource.
n DELETEremovesaresource.
AOS-CXRESTAPIReference(UI)|40

Notallresourcessupportallwritemethods.SeetheAOS-CXRESTAPIReferenceforthemethods
supportedbyeachresource.TheRESTAPImustbeinread-writemodefortheAOS-CXRESTAPI
Referencetoshowallthewritemethodsaresourcesupports.
| Considerations |     | when making | configuration | changes |
| -------------- | --- | ----------- | ------------- | ------- |
TheRESTAPIcanaccessandchangeeveryconfigurableaspectoftheswitchasmodeledinthe
configurationandstatedatabase.However,changingtheconfigurationofaswitchthroughtheRESTAPI
canbedifferentthanchangingtheconfigurationthroughtheCLI.
Asingleconfigurationchangetotheswitchcanrequirechangestomultipleresourcesinthe
configurationandstatedatabase.Oftenthesechangesmustbemadeinaspecificorder.
TheCLIcommandshavebeenprogrammedtowork"behindthescenes"tomakethecorrectdatabase
changesandtoperformdatavalidationchecksontheuserinput.Incontrast,whenyouusetheREST
APItomakeaconfigurationchange,youmustbecomefamiliarwiththerepresentationalmodelsofthe
switchresources,thetypeandformatofthedatarequired,andtherequiredorderofwriteoperations
tovariousresources.
TheRESTAPIispowerfulbutmustbeusedwithextremecaution:Nosemanticvalidationisperformed
onthedatayouwritetothedatabase,andconfigurationerrorscandestabilizetheswitch.Hewlett
PackardEnterpriserecommendsthatyourefertothetestedexampleswhenusingtheRESTAPIto
makeconfigurationchanges.
| Considerations |     | for ports | and interfaces |     |
| -------------- | --- | --------- | -------------- | --- |
TheRESTAPIprovidestheinterfacesresourcetoconfigureandgetinformationaboutswitchports
andinterfacesofalltypes.Youdonotusetheportsresourcetomanageports.
| Hardware | (system) | interfaces |     |     |
| -------- | -------- | ---------- | --- | --- |
n Hardwareinterfacesareoftypesystem.
n Hardwareinterfacesareincludedinthedatabaseautomatically.
n Interfacesoftypesystemcannotbeaddedordeleted.
LAG interfaces
n LAGinterfacesareoftypelag.
n YoucanusetheDELETEmethodtodeleteaLAGinterface.
ExampleofcreatingaLAGinterfacewithmemberports1/1/1and1/1/2:
MethodandURI:
POST "/rest/v10.xx/system/interfaces"
Requestbody:
{
| "name":       | "lag50",                            |     |     |     |
| ------------- | ----------------------------------- | --- | --- | --- |
| "vrf":        | "/rest/v10.xx/system/vrfs/default", |     |     |     |
| "type":       | "lag",                              |     |     |     |
| "interfaces": | [                                   |     |     |     |
"/rest/v10.xx/system/interfaces/1%2F1%2F1",
41
| AOS-CX10.12RESTAPIGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |
| ------------------------ | --- | ------------------------- | --- | --- |

"/rest/v10.xx/system/interfaces/1%2F1%2F2"

]

}

VLAN interfaces

n VLAN interfaces are of type vlan.

n You can use the DELETE method to delete a VLAN interface.

Example of creating a VLAN interface:

Method and URI:
POST "/rest/v10.xx/system/interfaces"

Request body:
{

"name": "vlan2",
"vlan_tag": "/rest/v10.04/system/vlans/2",
"vrf": "/rest/v10.04/system/vrfs/default",
"type": "vlan"

}

Write methods (POST, PUT) supported in read-only mode

The following switch resources support write methods (POST, PUT, or both) even when the REST API
access mode is set to read-only:

n Configuration management: */rest/v10.xx/fullconfigs*

n Firmware: */rest/v.10xx/firmware*

n User login and logout:

o */rest/v.10xx/login

o */rest/v.10xx/logout

n Aruba Network Analytics Engine and scripts: */rest/v10.xx/system/nae_scripts*

The * indicates more text to be added in URI path.

GET method usage and considerations
The GET method is a read method that gets the resource specified by the URI. Data is returned in JSON
format in the response body.

Using GET on a resource collection results in a list of URIs. Each URI in the list corresponds to a specific
resource in the collection.

Using GET on a specific resource returns the attributes of that resource.

GET method parameters

The GET method supports the following parameters in the query string of the URI:

n attributes

n count

n depth

n filter

n selector

AOS-CX REST API Reference (UI) | 42

A path query parameter is specified as a "key=value" pair. When permitted, multiple values are
separated by the comma (,) character.

For example:

n attributes=id,name,type

n count=true

n depth=2

n filter=type:static

n selector=writable

A path query parameter can be used alone or in combination with other parameters. The ampersand (&)
character separates each parameter in the string.

For example:
GET "https://192.0.2.5/rest/v10.09/system/vlans?depth=2&attributes=id,name,type"

The count and filter attributes and wildcard character are supported from AOS-CX release 10.05 and
later.

Wildcard character support

When you use the GET method, the URI can contain the asterisk (*) wildcard character instead of a
component in URI path. You can use wildcard characters in multiple places in the path. You cannot use a
wildcard character as part of the query string.

The wildcard character must replace the entire component in the path. Regular expressions are not
supported. For example, you can use a wildcard to specify all VRFs, but you cannot use a regular
expression to specify all VRFs that begin with the letter r.

By using a wildcard character in place of a component in the path, you can specify that GET return
information about multiple resources without requiring you to name each resource instance or to
execute multiple GET requests.

For example:

n The following URI specifies all routes regardless of VRF:
"https://192.0.2.5/rest/v10.xx/system/vrfs/*/routes"

n The following URI specifies all ACL entries of type IPv4, regardless of the name of the ACL:
"https://192.0.2.5/rest/v10.xx/system/acls/*,ipv4/cfg_aces"

n The following URI specifies the connection state of all BGP neighbors belonging to all BGP routers in

the "red" VRF:

"https://192.0.2.5/rest/v10.xx/system/vrfs/red/bgp_routers/*/bgp_
neighbors/*?attributes=status"

Attributes parameter

The attributes parameter of the GET method reduces the returned data for each entry to include only
the attributes specified in the comma-separated list. The attribute names in the URI must match the
attribute names in the AOS-CX REST API Reference.

For a list of the available attributes for a resource, see the GET method of that resource in the AOS-CX
REST API Reference.

Example request:
GET "https://192.0.2.5/rest/v10.xx/system/vlans?depth=2&attributes=id,name,type"

Example response:
{

{

"id": 1,

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

43

"name": "DEFAULT_VLAN_1",
"type": "default"

},
{

"id": 2,
"name": "VLAN2",
"type": "static"

},
{

"id": 3,
"name": "VLAN3",
"type": "static"

}

}

Count parameter

The count parameter of the GET method returns the number of entries that match the specified URI.
The count parameter can be useful when specifying resource collections or for getting statistical
information.

You can specify the count parameter as either of the following:

n count

n count=true

Examples:

n Use the count parameter to get the total number of VLANs:
GET "https://192.0.2.5/rest/v10.xx/system/vlans?count=true"

n Use the count parameter with the filter parameter to get the total number of interfaces in a down

administrative state:

GET "https://192.0.2.5/rest/v10.xx/system/interfaces?count&filter=admin_state:down"

Depth parameter

The depth parameter of the GET method specifies to what level URIs in response bodies are to be
expanded and replaced by the JSON representation of that resource:

n Default: 1

n Maximum: 4

For each level of depth, the REST API expands one level of URIs into their JSON data representations in
the response body.

Using the depth parameter can result in large amounts of returned data, depending on the number of items in

the list and the amount of JSON data that represents each item.

For example, a GET request on the vlans resource returns a list of URIs (using the default depth=1).
Example request:
GET "https://192.0.2.5/rest/v10.xx/system/vlans"

Example response:
{

"1": "/rest/v10.xx/system/vlans/1",
"10": "/rest/v10.xx/system/vlans/10",
"20": "/rest/v10.xx/system/vlans/20"

}

AOS-CX REST API Reference (UI) | 44

To specify that those URIs also be expanded and replaced with the JSON data, specify depth=2 as a
parameter in the GET request.

Example request:
GET "https://192.0.2.5/rest/v10.xx/system/vlans?depth=2"

Example response (ellipses represent data omitted from this example):
{

{

"id": 1,

"name": "DEFAULT_VLAN_1",
"type": "default",
…

"flood_enabled_subsystems": {

URI-of-first-subsystem

URI-of-last-subsystem

{

},
…
{

}

}

},

{ "id": 10,

"name": "vlan10",
"type": "static",
…

"flood_enabled_subsystems": {

URI-of-first-subsystem

URI-of-last-subsystem

{

},
…
{

}

}

}

}

Each VLAN in the preceding example includes an attribute, flood_enabled_subsystems, which contains
a list of URIs that represent the flood-enabled systems. To specify that those URIs also be expanded and
replaced with the JSON data, specify depth=3 as a parameter in the GET request.

Filter parameter

The filter parameter of the GET method reduces the returned data to include only those entries that
match the filter criteria. Specify the filter criteria in a comma-separated list of attribute name:value
pairs.

Examples:

n Use the filter parameter to get only the static VLANS:
GET "https://192.0.2.5/rest/v10.xx/system/vlans?filter=type:static"

n Use the filter parameter to get the BGP routes that have 1.1.1.1 as a peer:
GET "https://192.0.2.5/rest/v10.xx/system/vrfs/default/bgp_routes?filter=peer:1.1.1.1"

Selector parameter

The selector parameter of the GET method filters the returned data to include only those attributes
that belong to the specified category. By using the selector parameter, you avoid having to list
attributes individually using the attributes parameter.

The default is to include all categories. Use a comma (,) to separate multiple category values.

The selector categories are the following:

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

45

configuration

Contains user-owned information. Attributes in the configuration category can be supplied by users
through REST requests or through the switch CLI. Although an attribute must be in the configuration
category to be modified by a user, not all attributes in the configuration category can be modified
after the resource instance is created.

writable

Contains the mutable (writable) configuration attributes.

statistics

Contains system-supplied data such as counters. Attributes in the statistics category cannot be
written by users.

status

Contains system-owned data such as the admin account and various status fields. Attributes in the
status category cannot be written by users.

For example, to get the configuration attributes of all VLANs, when you specify the URI of the GET
method, do the following:

n Specify depth=2 to direct the REST API return the JSON representations of each VLAN instead of the

URI of each VLAN in the list. If you do not specify depth=2, the REST API returns each VLAN
represented as a URI, which does not include the attributes of the individual VLANs.

n Specify the selector parameter with the value configuration.

GET "https://192.0.2.5/rest/v10.09/system/vlans?depth=2&selector=configuration"

Example response:
{

{

"admin": "up",
"id": 1,
"mgmd_enable": {},
"mgmd_igmp_block_ports": [],
"mgmd_igmp_fastleave_ports": [],
"mgmd_igmp_forcedfastleave_ports": [],
"mgmd_igmp_forward_ports": [],
"mgmd_igmp_static_groups": [],
"mgmd_mld_block_ports": [],
"mgmd_mld_fastleave_ports": [],
"mgmd_mld_forcedfastleave_ports": [],
"mgmd_mld_forward_ports": [],
"mgmd_mld_static_groups": [],
"name": "VLAN1",
"type": "static"

},
{

"admin": "up",
"id": 10,
"mgmd_enable": {},
"mgmd_igmp_block_ports": [],
"mgmd_igmp_fastleave_ports": [],
"mgmd_igmp_forcedfastleave_ports": [],
"mgmd_igmp_forward_ports": [],
"mgmd_igmp_static_groups": [],
"mgmd_mld_block_ports": [],
"mgmd_mld_fastleave_ports": [],
"mgmd_mld_forcedfastleave_ports": [],
"mgmd_mld_forward_ports": [],
"mgmd_mld_static_groups": [],
"name": "VLAN10",
"type": "static"

},
{

AOS-CX REST API Reference (UI) | 46

"admin": "up",
"id": 20,
| "mgmd_enable":               | {}, |     |
| ---------------------------- | --- | --- |
| "mgmd_igmp_block_ports":     |     | [], |
| "mgmd_igmp_fastleave_ports": |     | [], |
"mgmd_igmp_forcedfastleave_ports": [],
| "mgmd_igmp_forward_ports":  |     | [], |
| --------------------------- | --- | --- |
| "mgmd_igmp_static_groups":  |     | [], |
| "mgmd_mld_block_ports":     |     | [], |
| "mgmd_mld_fastleave_ports": |     | [], |
"mgmd_mld_forcedfastleave_ports": [],
| "mgmd_mld_forward_ports": |     | [], |
| ------------------------- | --- | --- |
| "mgmd_mld_static_groups": |     | [], |
"name": "VLAN20",
"type": "static"
}
}
| POST method | usage | and considerations |
| ----------- | ----- | ------------------ |
ThePOSTmethodcreatesaninstanceofaresourceinthecollectionspecifiedbytheURI:
n NotallresourcessupportthePOSTmethod.SeetheAOS-CXRESTAPIReferenceforthemethods
supportedbyeachresource.TheRESTAPImustbeinread-writemodetoseeallthePOSTmethods
supported.
n SomeresourcessupportthePOSTmethodevenwhentheRESTAPIisinread-onlymode.
WhenyouusethePOSTmethod,theURImustpointtothecollection—nottotheresourceyouare
n
creating.TheresourceyouarecreatingissentinJSONformatintherequestbody.
o TheJSONrepresentationmustincludeallfieldsrequiredbytheJSONmodelofthatresource.
o TheJSONrepresentationcancontainonlyconfigurationattributes.Itmustnotcontainattributes
inthestatusorthestatisticscategory.
n YoucanPOSTonlyoneresourceatatime.
n Mostresourceshaveahierarchicalrelationship.Youmustcreatetheparentbeforeyoucancreate
thechild.
Forexample,tocreateanACLentry:
1. TheACLmustbecreatedfirstbysendingtheJSONdataoftheACLintherequestbodyinaPOST
requesttotheURIoftheaclscollection:
/system/acls
2. TheentrycanthenbecreatedbysendingtheJSONdataoftheentryintherequestbodyina
POSTrequesttotheURIoftheACL:
/system/acls/<ACL-name>,<ACL-type>/cfg_aces
ThefollowingisanexampleofusingthePOSTmethodtocreateasubinterfaceinstance:
POST "https://{{mgmt-ip}}/rest/v10.11/system/interfaces"
{
"name": "1/1/3.1026",
"type": "vlansubint",
"routing": true,
| "subintf_parent":             | "/rest/latest/system/interfaces/1%2F1%2F3", |     |
| ----------------------------- | ------------------------------------------- | --- |
| "subintf_vlan": 1026,         |                                             |     |
| "ip4_address": "10.5.2.1/24", |                                             |     |
"admin": "up"
}
Formoreinformationaboutsubinterfaces,refertotheFundamentalsGuide.
47
| AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches) |     |     |
| -------------------------------------------------- | --- | --- |

PUT method usage and considerations
The PUT method updates an instance of a resource by replacing the existing resource with the resource
provided in the request body.

Configuration attributes that are set at the time a resource is created and that cannot be changed
afterward are called immutable attributes. Configuration attributes that can be changed after a
resource is created are called mutable or writable attributes. The PUT method is used replace writable
attributes only.

n Not all resources support the PUT method. For information about the methods supported for a

resource, see the AOS-CX REST API Reference. The REST API must be in read-write mode to see all
the PUT methods supported.

n The URI must specify a specific resource, not a collection.

n The URI must specify a resource that currently exists.

n For almost all resources, the PUT method is implemented as a strict replace operation.

All mutable configuration attributes are replaced. Any mutable attribute that the JSON data in request
body does not include is either removed (if there is no default value) or reset to its default value.

PUT request body requirements

The JSON data in the request body must include mutable (writable) configuration attributes only.

The JSON model used for the PUT method request body is different from the JSON model used for the
GET or the POST method.

The JSON model of a PUT method for a resource contains the mutable attributes only. In contrast, the
JSON models for GET and POST methods can include both mutable and immutable attributes.

See the AOS-CX REST API Reference for the JSON model of a PUT method for a resource.

PUT behavior

The PUT operation is a replace operation—not an update operation—because the resource instance in
the request body replaces every changeable configuration attribute of the existing resource. To update
specific fields, use the PATCH operation.

Any mutable attribute that the JSON data in request body does not include is either removed (if there is no default

value) or reset to its default value.

For example:

n If you attempt a PUT operation on the System resource to change the host name, and you supply

only the host name, you will destabilize the switch because the other attributes will be reset to their
defaults, which might be empty.

n If you attempt to change the name of a VLAN and supply only the name in the PUT request, every

other attribute in that VLAN is set to its default of empty.

Exceptions to the PUT strict replace behavior

For Network Analytics Engine agents, the PUT behavior is not a strict replace implementation. You can
enable or disable agents without the supplying the entire set of configuration attributes in the PUT
request body. For more information about the Network Analytic Engine resources, see the Network
Analytics Engine Guide.

AOS-CX REST API Reference (UI) | 48

Best practice for building the PUT request body

Hewlett Packard Enterprise recommends the following procedure for building the PUT request body.

1. Use the GET method with selector=writable to obtain the writable (mutable) configuration

attributes for the resource you want to change.

For example:
GET "https://192.0.2.5/rest/v10.xx/system/interfaces/vlan200?selector=writable"

2. Change the values of the attributes to match your wanted configuration.

Any attribute you do not include in the request body will be set to its default value, which could
be empty.

3. Use the resulting JSON data as the request body for the PUT request.

PATCH method usage and considerations
The PATCH method is an HTTP method that updates values in an existing resource using only the
desired values in the request body.

n The PATCH method does not require fetching the current resource in order to send a new request, as

the PUT method requires, simplifying automation and reducing bandwidth usage.

n The PATCH method is used to add JSON keys or array elements, but cannot be used to remove

JSON keys or array elements.

n This method is only supported by the system and the resources under it. Not all resources support

the PATCH method.

The REST API must be in read-write mode to see all the PATCH methods supported.

PATCH is only available on versions REST v10.04 or later.

DELETE method usage and considerations
The DELETE method deletes an instance of a resource.

n Not all resources support the DELETE method. See the AOS-CX REST API Reference for the methods

supported by each resource. The REST API must be in read-write mode to see all the DELETE
methods supported.

n The URI must specify a specific resource instance. The URI must not specify a collection.

n Child subcollections and resources are deleted when you delete the parent resource. For example, if

you delete an ACL, its ACL entries are deleted automatically.

n DELETE requests do not contain a request body.

n DELETE requests do not return a response body.

REST requests and accounting logs
All REST requests—including GET requests—are logged to the accounting (audit) log.

The URI of the REST API resource for accounting logs is the following:
/rest/v10.xx/logs/audit

In an accounting log entry for a REST request:

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

49

n service=https-serverindicatesthatthelogentryisaresultofaRESTAPIrequestoraWebUI
action.
n ThestringvalueofdataidentifiestheRESTAPIrequestthatwasexecuted.
Formoreinformationaboutaccountinglogentries,seethedescriptionoftheshow accounting logCLI
command.
| AOS-CX | REST | API | reference |     | summary |     |
| ------ | ---- | --- | --------- | --- | ------- | --- |
Thefollowinginformationisintendedasaquickreferenceforexperiencedusers.Valuesarenot
configurableunlessnotedotherwise.
| Switch | REST | API | access | default |     |     |
| ------ | ---- | --- | ------ | ------- | --- | --- |
8100,8320,8325,8360,8400,9300,10000SwitchSeries:EnabledonthemgmtVRF
6200,6300,6400SwitchSeries:EnabledonthemgmtVRF
4100i,6000,6100SwitchSeries:EnabledonthedefaultVRF
| Switch | REST | API | default | access | mode |     |
| ------ | ---- | --- | ------- | ------ | ---- | --- |
Read-write
| Enabling | access |     | to the | Web | UI and | REST API |
| -------- | ------ | --- | ------ | --- | ------ | -------- |
CLIcommand:
| https-server | vrf | <VRF-NAME> |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | --- |
Example:
| switch(config)# |          | https-server |     |        | vrf mgmt |               |
| --------------- | -------- | ------------ | --- | ------ | -------- | ------------- |
| Setting         | the REST |              | API | access | mode     | to read-write |
CLIcommand:
| https-server | rest | access-mode |     | read-write |     |     |
| ------------ | ---- | ----------- | --- | ---------- | --- | --- |
Example:
| switch(config)# |     | https-server |     |        | rest access-mode | read-write |
| --------------- | --- | ------------ | --- | ------ | ---------------- | ---------- |
| Showing         | the | REST         | API | access | configuration    |            |
CLIcommand:
show https-server
Example:
| switch(config)# |        | show          | https-server |     |     |     |
| --------------- | ------ | ------------- | ------------ | --- | --- | --- |
| HTTPS           | Server | Configuration |              |     |     |     |
----------------------------
AOS-CXRESTAPIReference(UI)|50

| VRF    |             | : default,    | mgmt |      |     |     |     |
| ------ | ----------- | ------------- | ---- | ---- | --- | --- | --- |
| REST   | Access Mode | : read-write  |      |      |     |     |     |
| AOS-CX | REST        | API Reference |      | URL: |     |     |     |
REST latestAPI:https://<IP-ADDR>/api/latest/
REST v10.09API:https://<IP-ADDR>/api/v10.09/
REST v10.08API:https://<IP-ADDR>/api/v10.08/
RESTv10.04API:https://<IP-ADDR>/api/v10.04/
<IP-ADDR>istheIPaddressorhostnameofyourswitch.
Example:https://192.0.2.5/api/v10.04/
| REST     | API versions | and         | switch | software    | versions            |          |         |
| -------- | ------------ | ----------- | ------ | ----------- | ------------------- | -------- | ------- |
| REST API | version      |             |        |             | Switch              | software | version |
| v10.09   |              |             |        |             | AOS-CX10.09andlater |          |         |
| v10.08   |              |             |        |             | AOS-CX10.08andlater |          |         |
| v10.04   |              |             |        |             | AOS-CX10.04andlater |          |         |
| Getting  | REST         | API version |        | information | from                | a switch |         |
MethodandURItogettheRESTAPIversionssupportedontheswitch:
GET "https://<IP-ADDR>/rest"
<IP-ADDR>istheIPaddressorhostnameofyourswitch.
Protocol
HTTPS
Port
443
| Request | and response |     | body | format |     |     |     |
| ------- | ------------ | --- | ---- | ------ | --- | --- | --- |
JSON
| Session | idle timeout |     |     |     |     |     |     |
| ------- | ------------ | --- | --- | --- | --- | --- | --- |
20minutes
| Session | hard | timeout |     |     |     |     |     |
| ------- | ---- | ------- | --- | --- | --- | --- | --- |
Eighthours,regardlessofwhetherthesessionisactive.
Authentication
SessioncookiefromsuccessfulHTTPSloginrequest.
51
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |     |     |     |
| ------------------------ | ------------------------- | --- | --- | --- | --- | --- | --- |

HTTPS client sessions

n Maximum of 48 sessions per switch.

n Maximum of six concurrent client sessions per user.

n The same session cookie is shared across browser tabs and, depending on the browser, multiple

browser windows.

n The same session cookie is not shared across devices and scripts.

For example, if a user logs into the Web UI from a laptop, again with a tablet, and then uses the same
user name in a curl command, that user has three concurrent client sessions.

VSX peer switch access

If Virtual Switching Extension (VSX) is enabled on both switches, and the ISL is up, you can access the
VSX peer switch from your connected switch. To access the peer VSX switch, insert /vsx-peer in the URI
path between the server URL and /rest. Not supported for login, Web UI, or AOS-CX REST API Reference
access. For more information about VSX, see VSX peer switches and REST API access.

For example:

n Accessing a VSX switch:
https://192.0.2.5/rest/v10.xx/…

n Accessing its VSX peer switch:
https://192.0.2.5/vsx-peer/rest/v10.xx/…

AOS-CX REST API Reference (UI) | 52

Chapter 6

Using Curl Commands

Using Curl Commands

There are several tools available for accessing RESTful web service APIs, one of which is curl. The curl
tool, created by the cURL project, is a command-line application for transferring data using URL syntax.

For details on installing the curl application, see https://curl.haxx.se/download.html.

The curl application has many options, which are described in detail in the curl manual (run curl --
manual) and at https://curl.haxx.se/docs/manpage.html.

About the curl command examples
In the curl examples, the workstation is running a Linux-based operating system and curl version 7.35 is
installed.

The curl examples generated by the AOS-CX REST API Reference might use different options than in
other examples, and do not include cookie file handling because the cookie is handled by the browser.

Many examples of curl commands are formatted in multiple lines for readability. The backslash (\)
continuation character at the end of the line indicates that the command continues on the next line.

The curl command examples in this document use minimal options. The following options are
commonly used in the curl command examples:

-b<cookie-file>

Specifies that the file <cookie-file>, which contains the session cookie, be passed with the request.
<cookie-file> specifies the path and name of the cookie file.

When you use curl, you log in at the beginning of your session and log out at the end of the session.
When you log in, you must save the cookie returned from the login request. You must provide the
cookie with every subsequent curl command.

-k

Specifies that the curl program not attempt to verify the server certificate against the list of certificate
authorities included with the curl software.

The switch uses self-signed certificates. By default, the curl program attempts to verify certificates
against its list of certificate authorities, and attempts to verify self-signed certificates will fail.
Therefore you must use the –k option to disable attempts to verify self-signed certificates against a
certificate authority.

--noproxy

Specifies that a web proxy is not required. The --noproxy option is appropriate where execution of
curl commands does not need a proxy to access the applications.

If your network is configured to require a proxy to access applications, use the --proxy option
instead of the --noproxy option.

-d '<string>'

Specifies that curl send the data in <string> in a POST request using the content-type application/x-
www-form-urlencoded.

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

53

-X
Specifiesamethodthatcurlwouldnotusebydefault.TypicallyusedwithPUT,DELETE,andPOST
methodsonly.
| -Hor--header | <header> |     |     |     |
| ------------ | -------- | --- | --- | --- |
SpecifiesanextraheaderintheHTTPrequest.
-D
Specifiesthatcurlwritethereturnedprotocolheaderstothestandardoutputfile.Usedfor
debugging.
Moreoptionscanbeusedtocustomizeyourexperienceforyourenvironment.Formoreinformation
aboutcurloptions,see:
https://curl.haxx.se/docs/manpage.html
| Getting | the REST | API versions | on the | switch |
| ------- | -------- | ------------ | ------ | ------ |
TogetinformationaboutthelatestandallavailableRESTAPIversionsonaswitch,executeaGET
requesttothefollowingURI:
"https://<IP-ADDR>/rest"
<IP-ADDR>istheIPaddressorhostnameofyourswitch.
ExamplemethodandURI:
GET "https://192.0.2.5/rest"
Examplecurlcommand:
| $ curl              | -k GET \ |     |     |     |
| ------------------- | -------- | --- | --- | --- |
| -b /tmp/auth_cookie |          | \   |     |     |
"https://192.0.2.5/rest"
Exampleresponsebody:
{
| "latest":  | {               |     |     |     |
| ---------- | --------------- | --- | --- | --- |
| "version": | "v10.09",       |     |     |     |
| "prefix":  | "/rest/v10.09", |     |     |     |
| "doc":     | "/api/v10.09"   |     |     |     |
},
| "v10.09":  | {               |     |     |     |
| ---------- | --------------- | --- | --- | --- |
| "version": | "v10.09",       |     |     |     |
| "prefix":  | "/rest/v10.09", |     |     |     |
| "doc":     | "/api/v10.09"   |     |     |     |
},
| "v10.04":  | {               |     |     |     |
| ---------- | --------------- | --- | --- | --- |
| "version": | "v10.04",       |     |     |     |
| "prefix":  | "/rest/v10.04", |     |     |     |
| "doc":     | "/api/v10.04"   |     |     |     |
}
}
| Accessing | the REST | API using | curl |     |
| --------- | -------- | --------- | ---- | --- |
Whenyouusecurl,youloginatthebeginningofyoursessionandlogoutattheendofthesession.
Whenyoulogin,youmustsavethecookiereturnedfromtheloginrequestsothatyoucanpassthat
samecookievaluetotheswitchinsubsequentcurlcommands.
UsingCurlCommands|54

Prerequisites

n Access to the switch REST API must be enabled.

Procedure

1. To access the AOS-CX REST API using curl, use curl version 7.35 or later. The examples provided in

this document are tested with version 7.35.

2. For all curl commands, use the -k option to disable certificate validation.

The switch uses self-signed certificates. By default, the curl program attempts to verify certificates
against its list of certificate authorities, and attempts to verify self-signed certificates fail.
Therefore you must use the –k option to disable attempts to verify self-signed certificates against
a certificate authority.

3. Start your session by logging in. When you log in, save the cookie file by specifying the -c option

with a file name.

4.

In all subsequent curl commands—including logging out—pass the cookie value back to the
switch by specifying the -b option with the same file name.

5. At the end of the session, log out of the switch using curl.

Logging out at the end of the session is important because the number of concurrent HTTPS sessions per

client and per switch are limited, and session cookies are not shared across devices and scripts.

Logging in using curl

Prerequisites

Access to the switch REST API must be enabled.

Credential information (user name, password, domain, and authentication tokens) used in curl commands entered

at a command-line prompt might be saved in the command history. For security reasons, Hewlett Packard

Enterprise recommends that you disable command history before executing commands containing credential

information.

Procedure

Use the following curl command to access the login resource of the switch and provide your user name
and password as data:

Syntax:
curl [--noproxy <IP-ADDR>] -k -X POST
-c <COOKIE-FILE>=
-H 'Content-Type: multipart/form-data'
"https://<IP-ADDR>/rest/v10.xx/login"-F 'username=<USER-NAME>' -F 'password=<PASSWORD>'

Options:
-k

Specifies that the curl program not attempt to verify the server certificate against the list of certificate
authorities included with the curl software.

The switch uses self-signed certificates. By default, the curl program attempts to verify certificates
against its list of certificate authorities, and attempts to verify self-signed certificates fail. Therefore

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

55

youmustusethe–koptiontodisableattemptstoverifyself-signedcertificatesagainstacertificate
authority.
-X
Specifiesamethodthatcurlwouldnotusebydefault.Typically,usedonlywithPOST,PUT,PATCH,or
DELETEmethods.
| --noproxy | IP-ADDR> |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
Optional.The--noproxyoptionisappropriatewhereexecutionofcurlcommandsdoesnotneeda
proxytoaccesstheapplcations.Ifyournetworkisconfiguredtorequireaproxytoaccess
applications,usethe--proxyoption.<IP-ADDR>specifiestheIPaddressorhostnameoftheswitch.
-C <COOKIE-FILE>
Specifiesthefileinwhichtostorethesessioncookie.Thissessioncookieisrequiredwhenyou
executesubsequentcurlcommands.
| -H or --header | <header> |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- |
SpecifiesanextraheaderintheHTTPrequest.
-F
Specifiesthatthecurlcommandwillemulateafilled-informinwhichauserhaspressedthesubmit
buttonfortheHTTPprotocolfamily.ThiscausescurltoPOSTdatausingtheContent-Type
multipart/form-data.
<USER-NAME>
Specifiestheusername.
<PASSWORD>
Specifiesthepasswordfortheuser.
AlthoughitispossibletopasstheusernameandpasswordinformationasaquerystringintheloginURI,system
logssavetheaccessedURIincleartextinlogentries.HewlettPackardEnterpriserecommendsthatyoupassthe
credentialinformationasdatainsteadofintheURIwhenusingprogramssuchascurltologintotheswitch.
Example:
| $ curl                                 | --noproxy  | "192.0.2.5" |                    | -k -X POST | \                    |
| -------------------------------------- | ---------- | ----------- | ------------------ | ---------- | -------------------- |
| -c /tmp/auth_cookie                    |            |             | \-H 'Content-Type: |            | multipart/form-data' |
| \"https://192.0.2.5/rest/v10.09/login" |            |             |                    |            | \                    |
| -F 'username=test'                     |            | -F          | 'password=test'    |            |                      |
| Passing                                | the cookie |             | back               | to the     | switch               |
Prerequisites
StartasessionbyloggingintotheRESTAPIandsavethecookiefile.
Procedure
Usethefollowingcurlcommandtopassthecookiefilebacktotheswitchusingthe-boption.
Syntax:
| curl [--noproxy | <IP-ADDR>] |     | -k  | GET |     |
| --------------- | ---------- | --- | --- | --- | --- |
-b <COOKIE-FILE>
-H 'Content-Type:application/json'
| -H 'Accept: | application/json' |     |     |     |     |
| ----------- | ----------------- | --- | --- | --- | --- |
"https://<IP-ADDR>/rest/v10.xx/system"
Options:
| --noproxy | <IP-ADDR> |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- |
UsingCurlCommands|56

Optional. The --noproxy option is appropriate where execution of curl commands does not need a
proxy to access the applications. If your network is configured to require a proxy to access
applications, use the --proxy option. <IP-ADDR> specifies the IP address or hostname of the switch.

-k

Specifies that the curl program not attempt to verify the server certificate against the list of certificate
authorities included with the curl software.

The switch uses self-signed certificates. By default, the curl program attempts to verify certificates
against its list of certificate authorities, and attempts to verify self-signed certificates fail. Therefore
you must use the –k option to disable attempts to verify self-signed certificates against a certificate
authority.

-b <COOKIE-FILE>

Specifies that the file <cookie-file>, which contains the session cookie, be passed with the request.
The <cookie-file> specifies the path and name of the cookie file.

When you use curl, you log in at the beginning of your session and log out at the end of the session.
When you log in, you must save the cookie returned from the login request. You must provide the
cookie with every subsequent curl command.

-H or --header <header>

Specifies an extra header in the HTTP request.

Example:

$ curl --noproxy -k GET
-b /tmp/auth_cookie \
-H 'Content-Type:application/json' \
-H 'Accept: application/json' \
"https://192.0.2.5/rest//system"

Logging Out Using Curl
Use the following curl command to access the logout resource of the switch:
Syntax:
curl [--noproxy <IP-ADDR>] -k -X POST
-b <COOKIE-FILE>
"https://<IP-ADDR>/rest/v10.xx/logout"

Options:
-k

Specifies that the curl program not attempt to verify the server certificate against the list of certificate
authorities included with the curl software.

The switch uses self-signed certificates. By default, the curl program attempts to verify certificates
against its list of certificate authorities, and attempts to verify self-signed certificates fail. Therefore
you must use the –k option to disable attempts to verify self-signed certificates against a certificate
authority.

--noproxy<IP-ADDR>

Optional. The --noproxy option is appropriate where execution of curl commands does not need a
proxy to access the applications. If your network is configured to require a proxy to access
applications, use the --proxy option. <IP-ADDR> specifies the IP address or hostname of the switch.

-b <COOKIE-FILE>

Specifies the file that contains the session cookie.

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

57

When you use curl, you log in at the beginning of your session and log out at the end of the session. When you

log in, you must save the cookie returned from the login request so that you can pass that same cookie value to
the switch in subsequent curl commands. When you log in, save the cookie file by specifying the -c option with a
file name.

In subsequent curl commands, pass the cookie value back to the switch by specifying the -b option with the
same file name.

-X

Specifies a method that curl would not use by default. Typically, used only with POST, PUT, or DELETE
methods.

Example:

$ curl --noproxy "192.0.2.5" -k -X POST \
-b /tmp/auth_cookie \
"https://192.0.2.5/rest/v10.09/logout"

Examples
The following examples show how you can use curl with AOS-CX REST API. The response body might
vary based on the AOS-CX switch series. For example, the 8320 and 6400 switches show VSX
information, whereas the 6300 and 6200 switches show VSF and PoE information.

As a best practice, before you perform a GET, PUT, PATCH, POST, or DELETE operation, you must login
to create a session and save the cookie file by specifying the -c option with a file name. After you
perform the operation, you must logout to end the session and pass the cookie file back to the switch
by specifying the -b option with the same file name. The following examples assume that you are
performing the step to login before performing the operations in the example and logout after
performing the operations. For more information, see Accessing the REST API using curl.

The request and response body in the following examples contain a truncated part of the actual data. The data

that you see after running the curl commands might vary. Ellipses (…) in the response body represent data not

shown in the example.

Example: GET method

Instructions and examples in this document use an IP address that is reserved for documentation,
192.0.2.5, as an example of the IP address for the switch. To access your switch, you must use the IP
address or hostname of that switch.

n Get the list of all VLANS:
GET "https://192.0.2.5/rest/v10.xx/system/vlans"

n Expand the list of URIs in the vlans collection by one level, which replaces the URI for the VLAN

with the JSON data for that VLAN.

GET "https://192.0.2.5/rest/v10.xx/system/vlans?depth=2"

n Get the administrative state of interface 1/1/3:
https://192.0.2.5/rest/v10.xx/system/interfaces/1%2F1%2F3?attributes=admin

n Use the attributes parameter to get all interfaces but show only the attributes name and ipv4_

address:

Using Curl Commands | 58

GET "https://192.0.2.5/rest/v10.xx/system/interfaces?depth=2&attributes=name,ipv4_
address"
n UsetheselectorparametertogetallthewritableconfigurationattributesofVLAN100:
GET "https://192.0.2.5/rest/v10.xx/system/vlans/100?selector=writable"
n Usetheselectorparametertogetallthesystemattributesthatareinthecategories
configurationandstatus:
GET "https://192.0.2.5/rest/v10.xx/system?selector=configuration,status"
| Example: | Getting   | and              | deleting | certificates | using REST | APIs |
| -------- | --------- | ---------------- | -------- | ------------ | ---------- | ---- |
| Getting  | a list of | all certificates |          |              |            |      |
Itisimportanttonotethatthecertificateresourcesdonotsupporttheuseofinternationalizedstrings.Since
UTF8istheonlysupportedencoding,aSubjectAlternativeName(SAN)mustbeusedinstead.
ExamplemethodandURI:
GET "https://192.0.2.5/rest/v10.xx/certificates"
Examplecurlcommand:
| $ curl | --noproxy        | 192.0.2.5 | -k GET | \   |     |     |
| ------ | ---------------- | --------- | ------ | --- | --- | --- |
| -b     | /tmp/auth_cookie | \         |        |     |     |     |
"https://192.0.2.5/rest/v10.09/certificates”
Onsuccessfulcompletion,theswitchreturnsresponsecode200OKandaresponsebodycontaining
thecertificateresourceURLsindexedbythecertificatename.Forexample:
{
| "my-cert-1": | "/rest/v10.xx/certificates/my-cert-1", |     |     |     |     |     |
| ------------ | -------------------------------------- | --- | --- | --- | --- | --- |
| "my-cert-2": | "/rest/v10.xx/certificates/my-cert-2"  |     |     |     |     |     |
}
| Getting | a certificate |     |     |     |     |     |
| ------- | ------------- | --- | --- | --- | --- | --- |
ExamplemethodandURI:
GET "https://192.0.2.5/rest/v10.xx/certificates/my-cert-2"
Examplecurlcommand:
| $ curl | --noproxy        | 192.0.2.5 | -k GET | \   |     |     |
| ------ | ---------------- | --------- | ------ | --- | --- | --- |
| -b     | /tmp/auth_cookie | \         |        |     |     |     |
"https://192.0.2.5/rest/v10.09/certificates/my-cert-2"
Onsuccessfulcompletion,theswitchreturnsresponsecode200OKandaresponsebodycontaining
thecertificate.
Forexample:
'{
| "cert_name":   | "my-cert-2", |                |     |     |     |     |
| -------------- | ------------ | -------------- | --- | --- | --- | --- |
| "cert_type":   | "regular"    |                |     |     |     |     |
| "cert_status": |              | "csr_pending", |     |     |     |     |
| "key_type":    | "RSA",       |                |     |     |     |     |
| "key_size":    | 2048,        |                |     |     |     |     |
| "subject":     | {            |                |     |     |     |     |
| "common_name": |              | "CX-8400",     |     |     |     |     |
| "country":     | "US",        |                |     |     |     |     |
| "locality:     | "el          | camino",       |     |     |     |     |
| "state":       | "CA",        |                |     |     |     |     |
| "org":         | "HPE",       |                |     |     |     |     |
59
| AOS-CX10.12RESTAPIGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |     |     |
| ------------------------ | --- | ------------------------- | --- | --- | --- | --- |

| "org_unit": "Aruba" |     |     |     |
| ------------------- | --- | --- | --- |
},
| "certificate": | "<certificate-in-PEM-format>" |     |     |
| -------------- | ----------------------------- | --- | --- |
}'
Deleting a certificate
ExamplemethodandURI:
DELETE "https://192.0.2.5/rest/v10.xx/certificates/my-cert-3"
Examplecurlcommand:
| $ curl --noproxy    | 192.0.2.5 | -k -X DELETE | \   |
| ------------------- | --------- | ------------ | --- |
| -b /tmp/auth_cookie | \         |              |     |
"https://192.0.2.5/rest/v10.09/certificates/my-cert-3"
Onsuccessfulcompletion,theswitchreturnsresponsecode204.
Example: Generating a self-signed certificate using REST APIs
Thefollowingexamplegeneratesaself-signedcertificate.
ExamplemethodandURI:
POST "https://192.0.2.5/rest/v10.xx/certificates"
Examplerequestbody:
{
...
| "certificate_name": | "my-cert-1", |     |     |
| ------------------- | ------------ | --- | --- |
"subject": {
| "country": "US", |     |     |     |
| ---------------- | --- | --- | --- |
"state": "CA",
"org": "HPE",
| "org_unit": "Aruba",       |             |     |     |
| -------------------------- | ----------- | --- | --- |
| "common_name":             | "CX-8400"}, |     |     |
| "key_type": "RSA",         |             |     |     |
| "key_size": 2048,          |             |     |     |
| "cert_type": "self-signed" |             |     |     |
...
}
Examplecurlcommand:
| $ curl --noproxy    | 192.0.2.5 | -k -X POST | \   |
| ------------------- | --------- | ---------- | --- |
| -b /tmp/auth_cookie | \         |            |     |
"https://192.0.2.5/rest/v10.09/certificates”
–d '{
...
| "certificate_name": | "my-cert-1",  |     |     |
| ------------------- | ------------- | --- | --- |
| "subject": {        |               |     |     |
| "country":          | "US",         |     |     |
| "state": "CA",      |               |     |     |
| "org": "HPE",       |               |     |     |
| "org_unit":         | "Aruba",      |     |     |
| "common_name":      | "CX-8400"},   |     |     |
| "key_type":         | "RSA",        |     |     |
| "key_size":         | 2048,         |     |     |
| "cert_type":        | "self-signed" |     |     |
...
}'
Onsuccessfulcompletion,theswitchreturnsresponsecode201Created.
UsingCurlCommands|60

Example: Getting and installing a signed leaf certificate using REST
APIs

This example includes the step to create a trust anchor (TA) profile. If the TA profile had previously been
configured, that step of the example would be skipped. The TA profile is used to validate the signed
certificate when you import the certificate as part of the PUT request.

For more information about certificates and certificate management, see the Security Guide.

1. Create a TA Profile

a. From the certificate authority (CA), get a copy of the certificate against which you will validate

leaf certificates.

The certificate you validate leaf certificates against can be a root certificate or an intermediate
certificate.

The steps to get the leaf certificate depend on the CA and the operating system you use.

b. Create a JSON object with a certificate key and a name key.

For example:

{

"name": "<profile-name>", "certificate": "<root-ca-cert>"

}

n For the value of the name key, replace <profile-name> with the name of the TA profile you

want to create.

n For the value of the certificate key, replace <root-ca-cert> by pasting the copied

certificate.

n After pasting, edit the text to ensure proper loading as a JSON object by doing the following:

o Ensure the certificate headers and footers are treated as separate lines by adding \n

characters after the header and before the footer.

The following example shows the \n characters in bold.
{

"name": "myta",
"certificate": "-----BEGIN CERTIFICATE-----\nMIIF2DCCA8CgAwIBAgIlCnL

MA0GCSqGSIb3DQEBCwUAMHkxCzAJBgNVBAYTAkdCMRAwDgYDVQQIDAdFbmdsYW5kMRIwEAYDVQDAl
...
PKj0FmJ1+Qzw9Bcm6HiPTyxOVozMeRQzSQhTZVlh3OvBw/cUwTIqFJCe/afNQCqa9XnvTpJvP/Q3z
...
S4L9sxrk/i3hKB88\n-----END CERTIFICATE-----"\
}

o Ensure that any private key headers and footers are treated as separate lines by adding

\n characters before and after them as needed.

For example:
\n-----BEGIN PRIVATE KEY-----\n
MIIFDjBABgkqhkiG9wBBQ0wMzAbBgqkw0QwwDQIpJMN7sVGwCAggA
...
iKnXnUMpVPfLc74ty2S41DtH0X9gf6aa1jStg+7cND9XfGtjaV2CA

\n-----END PRIVATE KEY-----\n
\n-----BEGIN ENCRYPTED PRIVATE KEY-----\n
IJ6L/UhEtH523nUkdV6gvAgoYaD83PswToAGv5VS8OMFTPttrn5/K
...
OgSecqZsG6arbx0ESaYBir1c/6rPspcjbx283iD1MWOpeoS2aEmOX=
\n-----END ENCRYPTED PRIVATE KEY-----\n

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

61

c. UsethePOSTmethodtocreatetheTAprofilewiththecopiedcertificate.IncludetheJSON
objectintherequestbody:
ExamplemethodandURI:
POST "https://192.0.2.5/rest/v10.xx/system/pki_ta_profiles"
Examplecurlcommands:
$ curl --noproxy 192.0.2.5 -k -X POST \ -b /tmp/primary_auth_cookie \ -H
'Content-Type:application/json' "https://192.0.2.5/rest/v10.04/system/pki_ta_
profiles" -d '{ "  name": "myta", "certificate": "-----BEGIN CERTIFICATE-----
\nMIIF2DCCA8CgAwIBAgIJANkWgud1lCnL
MA0GCSqGSIb3DQEBCwUAMHkxCzAJBgNVBAYTAkdCMRAwDgYDVQQIDAdFbmdsYW5kMRIwEAYDVQQKDAl
...
PKj0FmJ1+Qzw9Bcm6HiPTyxOVozMeRQzSQhTZVlh3OvBw/cUwTIqFJCe/afNQCqa9XnvTpJvP/Q3ze6
| S4L9sxrk/i3hKB88\n-----END |     | CERTIFICATE-----" | }   |
| -------------------------- | --- | ----------------- | --- |
'Onsuccessfulcompletion,theswitchreturnsresponsecode201Created.
2. Createacertificatewithapendingcertificatesigningrequest(CSR).
Forinformationabouttherequiredandoptionalitemsintherequestbody,seetheJSONmodel
forthecertificatesresourceintheAOS-CXRESTAPIReference.
ExamplemethodandURI:
POST "https://192.0.2.5/rest/v10.xx/certificates"
Examplerequestbody:
{
| "certificate_name": | "my-cert-name", |     |     |
| ------------------- | --------------- | --- | --- |
"subject": {
| "common_name":   | "CX-8400" |     |     |
| ---------------- | --------- | --- | --- |
| "country": "US", |           |     |     |
| "locality":"el   | camino",  |     |     |
"state": "CA",
"org": "HPE",
| "org_unit": "Aruba", |     |     |     |
| -------------------- | --- | --- | --- |
},
| "key_type": "RSA",     |     |     |     |
| ---------------------- | --- | --- | --- |
| "key_size": 2048,      |     |     |     |
| "cert_type": "regular" |     |     |     |
}
Examplecurlcommand:
| $ curl --noproxy            | 192.0.2.5 | -k -X POST | \   |
| --------------------------- | --------- | ---------- | --- |
| -b /tmp/primary_auth_cookie |           | \          |     |
-d '{
| "certificate_name": | "my-cert-name", |     |     |
| ------------------- | --------------- | --- | --- |
| "subject": {        |                 |     |     |
| "common_name":      | "CX-8400"       |     |     |
| "country":          | "US",           |     |     |
| "locality":"el      | camino",        |     |     |
| "state": "CA",      |                 |     |     |
| "org": "HPE",       |                 |     |     |
| "org_unit":         | "Aruba",        |     |     |
},
| "key_type":  | "RSA",    |     |     |
| ------------ | --------- | --- | --- |
| "key_size":  | 2048,     |     |     |
| "cert_type": | "regular" |     |     |
}'
"https://192.0.2.5/rest/v10.09/certificates"
Onsuccessfulcompletion,theswitchreturnsresponsecode Created.
201
UsingCurlCommands|62

3. Get the certificate you created in the previous step.

Example method and URI:
GET "https://192.0.2.5/rest/v10.xx/certificates/my-cert-name"

Example curl command:

$ curl --noproxy 192.0.2.5 -k GET \
-b /tmp/primary_auth_cookie \
"https://192.0.2.5/rest/v10.09/certificates/my-cert-name"

On successful completion, the switch returns response code 200 OK and a response body
containing the CSR in PEM format.

4. Send the CSR to the CA for signing.

The steps to send the CSR depend on the CA and the operating system you use.

The CA returns the signed certificate in PEM format.

5.

Import the signed certificate by using a PUT request to update the my-cert-name certificate with
the signed certificate you received from the CA.

The imported certificate data must include all the intermediate CA certificates in the certificate
chain leading to the certificate that was imported into the specified TA profile.

If you copy and paste the certificate into a JSON object, you must ensure that the certificate and
private key headers and footers are processed as separate lines by editing the text to add \n
characters as needed.

As part of the PUT request, the switch attempts to validate the certificate against the pool of all TA
profiles installed on the switch. The certificate is accepted if it is validated with one of the TA
profiles.

Example method and URI:
PUT "https://192.0.2.5/rest/v10.xx/certificates/my-cert-name"

Example request body:
{

"certificate": "-----BEGIN CERTIFICATE-----\n

MIIFRDCCAyygAwIBAgQP8nS2Vp15u0xXMdkDJzANBgkqhkiG9w0Bv
...
1NGNm3NG03GqPScs/TF9bVyFA5BOS5lmmkfRYK8D/kMTfRreSdxis
YQ1u1NqShps=
\n-----END CERTIFICATE-----\n
\n-----BEGIN ENCRYPTED PRIVATE KEY-----\n
MIIFDjBABgkqhkiG9wBBQ0wMzAbBgqkw0QwwDQIpJMN7sVGwCAggA
...
iKnXnUMpVPfLc74ty2S41DtH0X9gf6aa1jStg+7cND9XfGtjaV2+/
cb4=
\n-----END ENCRYPTED PRIVATE KEY-----"
}

Example curl commands:

$ curl --noproxy 192.0.2.5 -k -X PUT \
-b /tmp/primary_auth_cookie \
-d '{

"certificate": "-----BEGIN CERTIFICATE-----\n

MIIFRDCCAyygAwIBAgQP8nS2Vp15u0xXMdkDJzANBgkqhkiG9w0Bv
...
1NGNm3NG03GqPScs/TF9bVyFA5BOS5lmmkfRYK8D/kMTfRreSdxis

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

63

YQ1u1NqShps=
\n-----END CERTIFICATE-----\n
\n-----BEGIN ENCRYPTED PRIVATE KEY-----\n
MIIFDjBABgkqhkiG9wBBQ0wMzAbBgqkw0QwwDQIpJMN7sVGwCAggA
...
iKnXnUMpVPfLc74ty2S41DtH0X9gf6aa1jStg+7cND9XfGtjaV2+/
cb4=
\n-----END ENCRYPTED PRIVATE KEY-----"
}'
"https://192.0.2.5/rest/v10.09/certificates/my-cert-name"

On successful completion, the switch returns response code 200 OK.

The certificate is installed and ready to be associated with switch features.

Example: Associating a leaf certificate with a switch feature using
REST APIs

The following example associates the signed certificate my-cert-name with the HTTPS server switch
feature. For complete information about the switch features to which you can associate a leaf
certificate, see the AOS-CX Security Guide.

Procedure

1. Get the configuration attributes of the system resource:

Example method and URI:
GET "https://192.0.2.5/rest/v10.xx/system?selector=configuration"

Example curl command:

$ curl --noproxy 192.0.2.5 -k GET \
-b /tmp/primary_auth_cookie \
"https://192.0.2.5/rest/v10.09/system?selector=configuration"

On successful completion, the switch returns response code 200 and a JSON object containing
the configuration attributes.

2.

In the portion of the response body that defines the certificate name for the HTTPS server,
change the value to: my-cert-name.

The certificate name associated with the HTTPS server is the value assigned to the https-server
key, which is under the certificate_association key. By default, the certificate name is: local-
cert

The request body of a PUT request is permitted to include only the mutable configuration
attributes. In the AOS-CX software releases to which this example applies, all the configuration
attributes for the system resource are mutable attributes, so you do not need to edit the JSON
object to remove the immutable attributes.

3. Using a PUT request, update the system resource with the edited JSON data as the request body.

Example method and URI:
PUT "https://192.0.2.5/rest/v10.xx/system"

Example request body:

Using Curl Commands | 64

{
"aaa": {
...
},
...
|     | "certificate_association": |     |                 | {   |     |     |
| --- | -------------------------- | --- | --------------- | --- | --- | --- |
|     | "https-server":            |     | "my-cert-name", |     |     |     |
|     | "syslog-client":           |     | "local-cert"    |     |     |     |
},
...
}
Examplecurlcommand:
|     | $ curl --noproxy            |     | 192.0.2.5 | -k -X PUT | \   |     |
| --- | --------------------------- | --- | --------- | --------- | --- | --- |
|     | -b /tmp/primary_auth_cookie |     |           | \         |     |     |
-d '{
|     | "aaa": | {   |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- |
...
},
...
|     | "certificate_association": |                  |     | {               |     |     |
| --- | -------------------------- | ---------------- | --- | --------------- | --- | --- |
|     |                            | "https-server":  |     | "my-cert-name", |     |     |
|     |                            | "syslog-client": |     | "local-cert"    |     |     |
},
...
}'
"https://192.0.2.5/rest/v10.09/system"
Onsuccessfulcompletion,theswitchreturnsresponsecode200OK.
| Example:    | Configuration   |     | management |     | using REST | APIs |
| ----------- | --------------- | --- | ---------- | --- | ---------- | ---- |
| Downloading | a configuration |     |            |     |            |      |
Downloadingthecurrentconfiguration:
n ExamplemethodandURI:
GET "https://192.0.2.5/rest/v10.xx/fullconfigs/running-config"
n Examplecurlcommand:
| $ curl | --noproxy                | 192.0.2.5 | -k  | GET \ |     |     |
| ------ | ------------------------ | --------- | --- | ----- | --- | --- |
| -b     | /tmp/primary_auth_cookie |           | \   |       |     |     |
"https://192.0.2.5/rest/v10.09/fullconfigs/running-config"
| Downloading | the | startup | configuration: |     |     |     |
| ----------- | --- | ------- | -------------- | --- | --- | --- |
n ExamplemethodandURI:
GET "https://192.0.2.5/rest/v10.xx/fullconfigs/startup-config"
n Examplecurlcommand:
| $ curl | --noproxy                | 192.0.2.5 | -k  | GET \ |     |     |
| ------ | ------------------------ | --------- | --- | ----- | --- | --- |
| -b     | /tmp/primary_auth_cookie |           | \   |       |     |     |
"https://192.0.2.5/rest/v10.09/fullconfigs/startup-config"
Onsuccessfulcompletion,theswitchreturnsresponsecode200OKandaresponsebodycontaining
theentireconfigurationinJSONformat.
65
| AOS-CX10.12RESTAPIGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |     |     |
| ------------------------ | --- | ------------------------- | --- | --- | --- | --- |

Uploading a configuration

The following example shows uploading a configuration to become the running configuration. The
running configuration is the only configuration that can be updated using this technique, however, you
can copy other configurations. For more information about copying configurations, see Copying a
configuration.

n Example method and URI:
PUT "https://192.0.2.5/rest/v10.xx/fullconfigs/running-config"

The request body must contain the configuration—in JSON format—to be uploaded.

n Example curl command:

$ curl --noproxy 192.0.2.5 -k -X PUT \
-b /tmp/auth_cookie \
"https://192.0.2.5/rest/v10.09/fullconfigs/running-config" \
–d '{
…
}'

The configuration being uploaded—represented as ellipsis but not shown in this example—is in JSON
format in the body of the command (enclosed in braces).

On successful completion, the switch returns response code 200 OK.

Copying a configuration

To replace an existing configuration with another, use a REST PUT request to the destination
configuration. Use the from query string parameter to specify the source configuration.

n At least one of the source or the destination configuration must be either running-config or

startup-config. You cannot copy a checkpoint to a different checkpoint.

n If you specify a destination checkpoint that exists, an error is returned. You cannot overwrite an

existing checkpoint.

The syntax of the method and URI is as follows:
PUT "https://<IPADDR>/rest/v10.xx/fullconfigs/<destination-config>?
from=/rest/v10.xx/fullconfigs/<source-config>"

Copying the running configuration to the startup configuration:

n Example method and URI:
PUT "https://192.0.2.5/rest/v10.xx/fullconfigs/startup-config?
from=/rest/v10.xx/fullconfigs/running-config"

n Example curl command:

$ curl --noproxy 192.0.2.5 -k -X PUT \
-b /tmp/auth_cookie -D-
"https://192.0.2.5/rest/v10.09/fullconfigs/startup-config?
from=/rest/v10.09/fullconfigs/running-config"

Copying the startup configuration to the running configuration:

n Example method and URI:
PUT "https://192.0.2.5/rest/v10.xx/fullconfigs/running-config?
from=/rest/v10.xx/fullconfigs/startup-config"

Using Curl Commands | 66

n Examplecurlcommand:
$ curl
|                     | --noproxy |     | 192.0.2.5 |     | -k  | -X PUT | \   |     |
| ------------------- | --------- | --- | --------- | --- | --- | ------ | --- | --- |
| -b /tmp/auth_cookie |           |     |           | -D- |     |        |     |     |
"https://192.0.2.5/rest/v10.09/fullconfigs/running-config?
from=/rest/v10.09/fullconfigs/startup-config"
Copyingacheckpointtotherunningconfiguration:
n ExamplemethodandURI:
PUT "https://192.0.2.5/rest/v10.xx/fullconfigs/running-config?
from=/rest/v10.xx/fullconfigs/MyCheckpoint"
n Examplecurlcommand:
| $ curl              | --noproxy |     | 192.0.2.5 |     | -k  | -X PUT | \   |     |
| ------------------- | --------- | --- | --------- | --- | --- | ------ | --- | --- |
| -b /tmp/auth_cookie |           |     |           | -D- |     |        |     |     |
"https://192.0.2.5/rest/v10.09/fullconfigs/running-config?
from=/rest/v10.09/fullconfigs/MyCheckpoint"
Copyingtherunningconfigurationtoacheckpoint:
n ExamplemethodandURI:
PUT "https://192.0.2.5/rest/v10.xx/fullconfigs/MyCheckpoint?
from=/rest/v10.xx/fullconfigs/running-config"
n Examplecurlcommand:
| $ curl              | --noproxy |     | 192.0.2.5 |     | -k  | -X PUT | \   |     |
| ------------------- | --------- | --- | --------- | --- | --- | ------ | --- | --- |
| -b /tmp/auth_cookie |           |     |           | -D- |     |        |     |     |
"https://192.0.2.5/rest/v10.09/fullconfigs/MyCheckpoint?
from=/rest/v10.09/fullconfigs/running-config"
| Example:  |     | Firmware |     | upgrade   |     | using    | REST  | APIs |
| --------- | --- | -------- | --- | --------- | --- | -------- | ----- | ---- |
| Uploading | a   | file as  | the | secondary |     | firmware | image |      |
Inthefollowingexample,acurlcommandisusedtouploadthefirmwareimagefilefromthelocal
workstationtotheswitch,asthesecondaryfirmwareimage.The-FoptionspecifiesthatthePOST
methodisusedtouploadthefile.
ExamplemethodandURI:
POST "https://192.0.2.5/rest/v10.xx/firmware?image=secondary"
Therequestbodycontainstheswitchfirmwareimagefileinbinaryformat.
Examplecurlcommand:
| $ curl            | --noproxy |                   | -k                | -b /tmp/auth_cookie |     |     | \   |     |
| ----------------- | --------- | ----------------- | ----------------- | ------------------- | --- | --- | --- | --- |
| -H 'Content-Type: |           |                   | application/json' |                     |     | \   |     |     |
| -H 'Accept:       |           | application/json' |                   |                     |     | \   |     |     |
-F "fileupload=@/myfirmwarefiles/myswitchfirmware_2020020905.swi" \
https://192.0.2.5/rest/v10.09/firmware?image=secondary
Inthecurlcommand,thePOSTrequestishandledaspartofthe-Foption.
| Booting | the | system | using | the | secondary |     | firmware | image |
| ------- | --- | ------ | ----- | --- | --------- | --- | -------- | ----- |
67
| AOS-CX10.12RESTAPIGuide| |     |     | (AllAOS-CXSeriesSwitches) |     |     |     |     |     |
| ------------------------ | --- | --- | ------------------------- | --- | --- | --- | --- | --- |

Example method and URI:
POST "https://192.0.2.5/rest/v10.xx/boot?image=secondary"

Example curl command:

$ curl --noproxy -k -X POST -b /tmp/auth_cookie \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
"https://192.0.2.5/rest/v10.09/boot?image=secondary"

Example: Log operations using REST APIs

Event logs

A GET request to /rest/v10.xx/logs/event URI returns all entries from all the event logs on the switch,
including logs from internal processes.

The information returned by this request was not optimized for human readability. If you want to
examine the log entries, Hewlett Packard Enterprise recommends that you use the Web UI. The Web UI
also provides a method to export log entries.

In the following example, the MESSAGE_ID parameter filters the output to include event log messages
only:

n 50c0fa81c2a545ec982a54293f1b1945 identifies event log messages from the active management

module.

n 73d7a43eaf714f97bbdf2b251b21cade identifies event log messages from the standby management

module. Not all switches have a standby management module.

Example method and URI:
GET "https://192.0.2.5/rest/v10.xx/logs/event?
limit=1000&
priority=4&
since=24%20hour%20ago&
MESSAGE_ID=50c0fa81c2a545ec982a54293f1b1945,73d7a43eaf714f97bbdf2b251b21cade"

Example curl command:

$ curl --noproxy 192.0.2.5 -k GET \
-b /tmp/primary_auth_cookie \
"https://192.0.2.5/rest/v10.09/logs/event?
limit=1000&
priority=4&
since=24%20hour%20ago&
MESSAGE_ID=50c0fa81c2a545ec982a54293f1b1945,73d7a43eaf714f97bbdf2b251b21cade"

Accounting (audit) logs

A GET request to the /rest/v10.xx/logs/audit URI returns all entries from the accounting logs on the
switch.

For a list of supported query parameters, see the AOS-CX REST API Reference.

Example method and URI:
GET "https://192.0.2.5/rest/v10.xx/logs/audit?
since=24%20hour%20ago&
usergroup=administrators&
session=CLI"

Example curl command:

Using Curl Commands | 68

$ curl --noproxy 192.0.2.5 -k GET \
-b /tmp/primary_auth_cookie \
"https://192.0.2.5/rest/v10.09/logs/audit?
since=24%20hour%20ago&
usergroup=administrators&
session=CLI"

Example: Ping operations using REST APIs

This example gets ping statistics for the ping target.

Example method and URI:
GET "https://192.0.2.5/rest/v10.xx/ping?
ping_target=192.0.2.10&
is_ipv4=true&
ping_data_size=100&
ping_time_out=2&
ping_repetitions=1&
ping_type_of_service=0&
include_time_stamp=false&
include_time_stamp_address=false&
record_route=false&
mgmt=false"

Example curl command:

$ curl --noproxy 192.0.2.5 -k GET \
-b /tmp/primary_auth_cookie \
"https://192.0.2.5/rest/v10.09/ping?
ping_target=192.0.2.10&
is_ipv4=true&
ping_data_size=100&
ping_time_out=2&
ping_repetitions=1&
ping_type_of_service=0&
include_time_stamp=false&
include_time_stamp_address=false&
record_route=false&
mgmt=false"

On successful completion, the switch returns response code 200 OK and a response body containing
the output string produced by the ping operation.

Example: Traceroute operations using REST APIs

Example method and URI:
GET "https://192.0.2.5/rest/v10.xx/traceroute?
ip=192.0.2.10&
is_ipv4=true&
timeout=3&
destination_port=33434&
max_ttl=30&
min_ttl=1&
probes=3&
mgmt=false"

Example curl command:

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

69

| $ curl                      | --noproxy 192.0.2.5 | -k GET \ |     |
| --------------------------- | ------------------- | -------- | --- |
| -b /tmp/primary_auth_cookie |                     | \        |     |
"https://192.0.2.5/rest/v10.09/traceroute?
ip=192.0.2.10&
is_ipv4=true&
timeout=3&
destination_port=33434&
max_ttl=30&
min_ttl=1&
probes=3&
mgmt=false"
Onsuccessfulcompletion,theswitchreturnsresponsecode200OKandaresponsebodycontaining
theoutputstringproducedbythetracerouteoperation.
| Example: | User management | using REST | APIs |
| -------- | --------------- | ---------- | ---- |
| Creating | a user          |            |      |
ExamplemethodandURI:
POST "https://192.0.2.5/rest/v10.xx/system/users"
Examplerequestbody:
{
...
| "name":     | "myadmin",  |     |     |
| ----------- | ----------- | --- | --- |
| "password": | "P@ssw0rd", |     |     |
"user_group": "/rest/v10.xx/system/user_groups/administrators",
| "origin": | "configuration" |     |     |
| --------- | --------------- | --- | --- |
...
}
Examplecurlcommand:
| $ curl              | --noproxy -k -X POST | \   |     |
| ------------------- | -------------------- | --- | --- |
| -b /tmp/auth_cookie | \                    |     |     |
"https://192.0.2.5/rest/v10.09/system/users”
–d '{
...
| "name":     | "myadmin",  |     |     |
| ----------- | ----------- | --- | --- |
| "password": | "P@ssw0rd", |     |     |
"user_group": "/rest/v10.09/system/user_groups/administrators",
| "origin": | "configuration" |     |     |
| --------- | --------------- | --- | --- |
...
}'
Onsuccessfulcompletion,theswitchreturnsresponsecode201Created.
| Changing | a password |     |     |
| -------- | ---------- | --- | --- |
ExamplemethodandURI:
PUT "https://192.0.2.5/rest/v10.xx/system/users/myadmin"
Examplerequestbody:
{
| "password": | "P@ssw0rd2g" |     |     |
| ----------- | ------------ | --- | --- |
"current_password": "current_password"
}'
}
UsingCurlCommands|70

Examplecurlcommand:
| $ curl | --noproxy        | -k  | -X PUT | \   |     |     |     |     |
| ------ | ---------------- | --- | ------ | --- | --- | --- | --- | --- |
| -b     | /tmp/auth_cookie |     | \      |     |     |     |     |     |
"https://192.0.2.5/rest/v10.09/system/users/myadmin”
–d '{
|     | "password":         | "P@ssw0rd2g" |                    |     |     |     |     |     |
| --- | ------------------- | ------------ | ------------------ | --- | --- | --- | --- | --- |
|     | "current_password": |              | "current_password" |     |     |     |     |     |
}'
}'
Onsuccessfulcompletion,theswitchreturnsresponsecode200OK.
| Deleting | a user |     |     |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
ExamplemethodandURI:
DELETE "https://192.0.2.5/rest/v10.xx/system/users/myadmin"
Examplecurlcommand:
| $ curl | --noproxy        | -k  | -X DELETE | \   |     |     |     |     |
| ------ | ---------------- | --- | --------- | --- | --- | --- | --- | --- |
| -b     | /tmp/auth_cookie |     | \         |     |     |     |     |     |
"https://192.0.2.5/rest/v10.09/system/users/myadmin"
Onsuccessfulcompletion,theswitchreturnsresponsecode204NoContent.
| Example: | Creating |     | an ACL | with an | interface |     | using REST | APIs |
| -------- | -------- | --- | ------ | ------- | --------- | --- | ---------- | ---- |
ThisexampleshowscreatingthefollowingACLandinterfaceconfigurationonaswitchatIPaddress
192.0.2.5:
| access-list | ip ACLv4   |              |     |                    |     |         |     |     |
| ----------- | ---------- | ------------ | --- | ------------------ | --- | ------- | --- | --- |
| 10          | permit tcp | 10.0.100.101 |     | eq 80 10.0.100.102 |     | eq 8000 |     |     |
| interface   | 1/1/2      |              |     |                    |     |         |     |     |
no shutdown
| apply | access-list | ip  | ACLv4 | out |     |     |     |     |
| ----- | ----------- | --- | ----- | --- | --- | --- | --- | --- |
1. CreatingtheACL.
|     | $ curl --noproxy    |           | 192.0.2.5 | -k -X | POST | \   |     |     |
| --- | ------------------- | --------- | --------- | ----- | ---- | --- | --- | --- |
|     | -b /tmp/auth_cookie |           | -d        | '{    |      |     |     |     |
|     | "cfg_version":      |           | 0,        |       |      |     |     |     |
|     | "list_type":        | "ipv4",   |           |       |      |     |     |     |
|     | "name":             | "ACLv4"}' |           |       |      |     |     |     |
"https://192.0.2.5/rest/v10.09/system/acls"
2. CreatinganACLentry.
|     | $ curl --noproxy    |                                 | 192.0.2.5 | -k -X | POST | \   |     |     |
| --- | ------------------- | ------------------------------- | --------- | ----- | ---- | --- | --- | --- |
|     | -b /tmp/auth_cookie |                                 | -d        | '{    |      |     |     |     |
|     | "action":           | "permit",                       |           |       |      |     |     |     |
|     | "dst_ip":           | "10.0.100.102/255.255.255.255", |           |       |      |     |     |     |
|     | "dst_l4_port_max":  |                                 | 8000,     |       |      |     |     |     |
|     | "dst_l4_port_min":  |                                 | 8000,     |       |      |     |     |     |
71
| AOS-CX10.12RESTAPIGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |     |     |     |     |
| ------------------------ | --- | ------------------------- | --- | --- | --- | --- | --- | --- |

| "protocol": 6,                            |      |     |     |
| ----------------------------------------- | ---- | --- | --- |
| "sequence_number":                        | 10,  |     |     |
| "src_ip": "10.0.100.101/255.255.255.255", |      |     |     |
| "src_l4_port_max":                        | 80,  |     |     |
| "src_l4_port_min":                        | 80}' |     |     |
"https://192.0.2.5/rest/v10.09/system/acls/ACLv4,ipv4/cfg_aces"
3. GettingtheACLwritableconfigurationattributestouseinthenextstep.
| $ curl --noproxy    | 192.0.2.5 | -k GET | \   |
| ------------------- | --------- | ------ | --- |
| -b /tmp/auth_cookie | \         |        |     |
"https://192.0.2.5/rest/v10.09/system/acls/ACLv4,ipv4?selector=writable"
Responsebody:
{
...
| "cfg_aces": "/rest/v10.04/system/acls/ACLv4,ipv4/cfg_aces", |                   |     |     |
| ----------------------------------------------------------- | ----------------- | --- | --- |
| "cfg_version":                                              | 3738959816497071, |     |     |
| "vsx_sync": []                                              |                   |     |     |
...
| "list_type": "ipv4", |     |     |     |
| -------------------- | --- | --- | --- |
"name": "ACLv4"
...
}
4. UpdatingtheACLconfigurationusingthereturnbodyreceivedfromtheGETrequestperformed
inthepreviousstep.
AnywritableattributesyoudonotincludeinthePUTrequestbodyaresettotheirdefaults,which
couldbeempty.
ThefollowingexampleshowstherequesttoupdatetheACLconfiguration:
| $ curl --noproxy    | 192.0.2.5 | -k -X PUT | \   |
| ------------------- | --------- | --------- | --- |
| -b /tmp/auth_cookie | -d '{     |           |     |
"cfg_aces":{"10":"/rest/v10.09/system/acls/ACLv4,ipv4/cfg_aces/10"},
| "cfg_version":1}' | \   |     |     |
| ----------------- | --- | --- | --- |
"https://192.0.2.5/rest/v10.09/system/acls/ACLv4,ipv4"
5. Gettingthewritableattributesofaninterface.
TheGETresponsebodyincludesonlytheconfigurationattributesthathavebeenset.
| $ curl --noproxy    | 192.0.2.5 | -k GET | \   |
| ------------------- | --------- | ------ | --- |
| -b /tmp/auth_cookie | \         |        |     |
"https://192.0.2.5/rest/v10.09/system/interfaces/1%2F1%2F2?selector=writabl
e"
Responsebody:
{
...
| "cdp_disable":                | false, |       |     |
| ----------------------------- | ------ | ----- | --- |
| "description":                | null,  |       |     |
| "lldp_med_loc_civic_ca_info": |        | {},   |     |
| "lldp_med_loc_civic_info":    |        | null, |     |
| "lldp_med_loc_elin_info":     |        | null, |     |
UsingCurlCommands|72

| "options": {},                            |     |        |        |
| ----------------------------------------- | --- | ------ | ------ |
| "other_config":                           | {   |        |        |
| "lldp_dot3_macphy_disable":               |     | false, |        |
| "lldp_med_capability_disable":            |     | false, |        |
| "lldp_med_network_policy_disable":        |     |        | false, |
| "lldp_med_topology_notification_disable": |     |        | false  |
},
| "pfc_priorities_config":           |             | null, |                        |
| ---------------------------------- | ----------- | ----- | ---------------------- |
| "selftest_disable":                | false,      |       |                        |
| "udld_arubaos_compatibility_mode": |             |       | "forward_then_verify", |
| "udld_compatibility":              | "aruba_os", |       |                        |
| "udld_enable":                     | false,      |       |                        |
| "udld_interval":                   | 7000,       |       |                        |
| "udld_retries":                    | 4,          |       |                        |
| "udld_rfc5171_compatibility_mode": |             |       | "normal",              |
| "user_config":                     | {           |       |                        |
| "admin": "down"                    |             |       |                        |
...
}
6. EnablingtheinterfaceandaddingtheACLinformationtotheinterfacebyusingthereturnbody
receivedfromtheGETrequestperformedinthepreviousstep.Themodifiedvaluesareshownin
thefollowingexample.
| $ curl --noproxy    | 192.0.2.5 | -k -X PUT | \   |
| ------------------- | --------- | --------- | --- |
| -b /tmp/auth_cookie | -d        |           |     |
'{
...
| "user_config": | {"admin": | "up" }, |     |
| -------------- | --------- | ------- | --- |
"aclv4_out_cfg":"/rest/v10.09/system/acls/ACLv4,ipv4",
"aclv4_out_cfg_version":1,
...
}' -D- \
"https://192.0.2.5/rest/v10.09/system/interfaces/1%2F1%2F2"
Example: Creating a VLAN and a VLAN interface using REST APIs
ThisexampleshowscreatingthefollowingVLANandinterfaceconfigurationonaswitchatIPaddress
192.0.2.5:
vlan 2
no shutdown
interface vlan 2
1. CreatingtheVLAN.
| $ curl --noproxy    | 192.0.2.5 | -k -X POST | \   |
| ------------------- | --------- | ---------- | --- |
| -b /tmp/auth_cookie | -d        | '{         |     |
"name":"vlan2",
"id":2,
"type":"static",
| "admin":"up"}' | \   |     |     |
| -------------- | --- | --- | --- |
"https://192.0.2.5/rest/v10.09/system/vlans"
2. CreatinganinterfacewithVLANinformation
| $ curl --noproxy    | 192.0.2.5 | -k -X POST | \   |
| ------------------- | --------- | ---------- | --- |
| -b /tmp/auth_cookie | -d        | '{         |     |
"vrf": "/rest/v10.09/system/vrfs/default",
73
AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches)

"vlan_tag":"/rest/v10.09/system/vlans/2",
"name":"vlan2",
|     | "type":"vlan"}' | \   |     |
| --- | --------------- | --- | --- |
-D- "https://192.0.2.5/rest/v10.09/system/interfaces"
| Example: | Enabling | routing | on an interface |
| -------- | -------- | ------- | --------------- |
Thefollowingexampleshowshowtoenableroutingonaninterface.
| interface | 1/1/1 |     |     |
| --------- | ----- | --- | --- |
routing
1. Gettingthewritableconfigurationinformationfortheinterface.
|     | $ curl --noproxy    | 192.0.2.5 | -k GET \ |
| --- | ------------------- | --------- | -------- |
|     | -b /tmp/auth_cookie | \         |          |
-H 'Content-Type:application/json'
|     | -H 'Accept: | application/json' |     |
| --- | ----------- | ----------------- | --- |
"https://192.0.2.5/rest/v10.09/system/interfaces/1%2F1%2F1?selector=writabl
e"
Responsebody:
TheGETresponsebodyincludesonlytheconfigurationattributesthathavebeenset.
{
...
|     | "routing": | false, |     |
| --- | ---------- | ------ | --- |
"udld_arubaos_compatibility_mode": "forward_then_verify",
|     | "udld_compatibility": |        | "aruba_os", |
| --- | --------------------- | ------ | ----------- |
|     | "udld_enable":        | false, |             |
|     | "udld_interval":      | 7000,  |             |
|     | "udld_retries":       | 4,     |             |
"udld_rfc5171_compatibility_mode": "normal",
|     | "user_config":        | {}    |     |
| --- | --------------------- | ----- | --- |
|     | "vlan_mode":          | null, |     |
|     | "vlan_tag":           | null, |     |
|     | "vlan_translations":  |       | {}, |
|     | "vlan_trunks":        | [],   |     |
|     | "vlans_per_protocol": |       | {}, |
"vrf": null,
...
}
2. UpdatetheinterfaceusingthereturnbodyreceivedfromtheGETrequest,modifyingtherouting
| attributetobe:"routing": |     | true. |     |
| ------------------------ | --- | ----- | --- |
AnywritableattributesyoudonotincludeinthePUTrequestbodyaresettotheirdefaults,which
couldbeempty.
|     | $ curl --noproxy    | -X PUT            | \   |
| --- | ------------------- | ----------------- | --- |
|     | -b /tmp/auth_cookie | \                 |     |
|     | -H 'Content-Type:   | application/json' |     |
|     | -H 'Accept:         | application/json' |     |
-d '{
...
"routing":true,
UsingCurlCommands|74

...
}'
"https://192.0.2.5/rest/v10.09/system/interfaces/1%2F1%2F1"
| Example: |        | PATCH Method |     |     |     |     |
| -------- | ------ | ------------ | --- | --- | --- | --- |
| Enabling | a VLAN |              |     |     |     |     |
Examplecurlcommand:
$ curl -k --noproxy <ip> -X PATCH -b /tmp/cookies -d '{"admin":"up"}' -D-
"https://<ip>/rest/<version>/system/vlans/100"
| Enabling | Central |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- |
Examplecurlcommand:
$ curl -k --noproxy <ip> -b /tmp/cookies -X PATCH -d '{"disable":false}' -D-
"https://<ip>/rest/<version>/system/aruba_central"
| Changing | the | Source | IP of | a VRF |     |     |
| -------- | --- | ------ | ----- | ----- | --- | --- |
Examplecurlcommand:
$ curl -k --noproxy <ip> -b /tmp/cookies -X PATCH -d '{"source_ip":
{"all":"10.1.1.1"}}' -D- "https://<ip>/rest/<version>/system/vrfs/mgmt"
| Using GET and |     | PATCH to |     | Update | the admin | state of a VLAN |
| ------------- | --- | -------- | --- | ------ | --------- | --------------- |
ExampleGET curlcommand:
$ curl --noproxy -k -X GET "https://192.0.2.5/rest/v10.09/system/vlans/100 -H
| "accept:                |                                  | */*" -d           | ""         | -b /tmp/auth_cookie |               |     |
| ----------------------- | -------------------------------- | ----------------- | ---------- | ------------------- | ------------- | --- |
| HTTP/1.1                |                                  | 200 OK            |            |                     |               |     |
| Server:                 |                                  | nginx             |            |                     |               |     |
| Date:                   | Wed,                             | 03 Nov            | 2021       | 22:53:02            | GMT           |     |
| Content-Type:           |                                  | application/json; |            |                     | charset=utf-8 |     |
| Transfer-Encoding:      |                                  |                   | chunked    |                     |               |     |
| Connection:             |                                  | keep-alive        |            |                     |               |     |
| Etag:                   | be17a56d01ca6eba8fc1901a4f5d2fd6 |                   |            |                     |               |     |
| X-Frame-Options:        |                                  |                   | SAMEORIGIN |                     |               |     |
| X-Content-Type-Options: |                                  |                   |            | nosniff             |               |     |
| X-XSS-Protection:       |                                  |                   | 1;         | mode=block          |               |     |
Strict-Transport-Security: max-age=31536000; includeSubdomains;
Content-Security-Policy: script-src 'self' 'unsafe-inline'; object-src 'none';
| font-src |     | *; media-src |     | 'none'; | form-action | 'self'; |
| -------- | --- | ------------ | --- | ------- | ----------- | ------- |
Onsuccessfulcompletion,theswitchreturnsthefollowing:
{
...
| "admin":                 |     | "up", |     |     |     |     |
| ------------------------ | --- | ----- | --- | --- | --- | --- |
| "clear_ip_bindings":     |     |       |     | {}, |     |     |
| "delete_macs_rejected":  |     |       |     | {}, |     |     |
| "delete_macs_requested": |     |       |     | {}, |     |     |
| "description":           |     | null, |     |     |     |     |
75
| AOS-CX10.12RESTAPIGuide| |     | (AllAOS-CXSeriesSwitches) |     |     |     |     |
| ------------------------ | --- | ------------------------- | --- | --- | --- | --- |

| "flood_enabled_subsystems": |     | {}, |     |     |
| --------------------------- | --- | --- | --- | --- |
"id": 100,
| "internal_usage": | {}, |     |     |     |
| ----------------- | --- | --- | --- | --- |
"macs": "/rest/v10.09/system/vlans/100/macs",
| "macs_invalid": | null, |     |     |     |
| --------------- | ----- | --- | --- | --- |
...
}
ExamplePATCHcurlcommand:
$ curl --noproxy -k -X PATCH "https://192.0.2.5/rest/v10.09/system/vlans"/100 -H
| "accept:                | */*" -d '{"admin": | "down"}'   |     | -b /tmp/auth_cookie |
| ----------------------- | ------------------ | ---------- | --- | ------------------- |
| HTTP/1.1                | 204 No Content     |            |     |                     |
| Server:                 | nginx              |            |     |                     |
| Date: Wed,              | 03 Nov 2021        | 22:54:43   | GMT |                     |
| Connection:             | keep-alive         |            |     |                     |
| X-Frame-Options:        | SAMEORIGIN         |            |     |                     |
| X-Content-Type-Options: |                    | nosniff    |     |                     |
| X-XSS-Protection:       | 1;                 | mode=block |     |                     |
Strict-Transport-Security: max-age=31536000; includeSubdomains;
Content-Security-Policy: script-src 'self' 'unsafe-inline'; object-src 'none';
| font-src | *; media-src | 'none'; | form-action | 'self'; |
| -------- | ------------ | ------- | ----------- | ------- |
ExampleGET curlcommand:
$ curl
--noproxy -k -X GET "https://192.0.2.5/rest/v10.09/system/vlans/100 -H
| "accept:           | */*" -d ""        | -b /tmp/auth_cookie |               |     |
| ------------------ | ----------------- | ------------------- | ------------- | --- |
| HTTP/1.1           | 200 OK            |                     |               |     |
| Server:            | nginx             |                     |               |     |
| Date: Wed,         | 03 Nov 2021       | 22:53:02            | GMT           |     |
| Content-Type:      | application/json; |                     | charset=utf-8 |     |
| Transfer-Encoding: |                   | chunked             |               |     |
| Connection:        | keep-alive        |                     |               |     |
Etag: be17a56d01ca6eba8fc1901a4f5d2fd6
| X-Frame-Options:        | SAMEORIGIN |            |     |     |
| ----------------------- | ---------- | ---------- | --- | --- |
| X-Content-Type-Options: |            | nosniff    |     |     |
| X-XSS-Protection:       | 1;         | mode=block |     |     |
Strict-Transport-Security: max-age=31536000; includeSubdomains;
Content-Security-Policy: script-src 'self' 'unsafe-inline'; object-src 'none';
| font-src | *; media-src | 'none'; | form-action | 'self'; |
| -------- | ------------ | ------- | ----------- | ------- |
$ curl --noproxy -k -X GET "https://192.0.2.5/rest/v10.09/system/vlans"/100 -H
| "accept:           | */*" -d ""        | -b /tmp/auth_cookie |               |     |
| ------------------ | ----------------- | ------------------- | ------------- | --- |
| HTTP/1.1           | 200 OK            |                     |               |     |
| Server:            | nginx             |                     |               |     |
| Date: Wed,         | 03 Nov 2021       | 22:54:52            | GMT           |     |
| Content-Type:      | application/json; |                     | charset=utf-8 |     |
| Transfer-Encoding: |                   | chunked             |               |     |
| Connection:        | keep-alive        |                     |               |     |
Etag: d54a643eb48515e94ea94bd501d9d2c8
| X-Frame-Options:        | SAMEORIGIN |            |     |     |
| ----------------------- | ---------- | ---------- | --- | --- |
| X-Content-Type-Options: |            | nosniff    |     |     |
| X-XSS-Protection:       | 1;         | mode=block |     |     |
Strict-Transport-Security: max-age=31536000; includeSubdomains;
Content-Security-Policy: script-src 'self' 'unsafe-inline'; object-src 'none';
| font-src | *; media-src | 'none'; | form-action | 'self'; |
| -------- | ------------ | ------- | ----------- | ------- |
Onsuccessfulcompletion,theswitchreturnsthefollowing:
{
...
| "admin":                | "down", |     |     |     |
| ----------------------- | ------- | --- | --- | --- |
| "clear_ip_bindings":    |         | {}, |     |     |
| "delete_macs_rejected": |         | {}, |     |     |
UsingCurlCommands|76

| "delete_macs_requested":                      |       | {}, |     |     |
| --------------------------------------------- | ----- | --- | --- | --- |
| "description":                                | null, |     |     |     |
| "flood_enabled_subsystems":                   |       | {}, |     |     |
| "id": 100,                                    |       |     |     |     |
| "internal_usage":                             | {},   |     |     |     |
| "macs": "/rest/v10.09/system/vlans/100/macs", |       |     |     |     |
| "macs_invalid":                               | null, |     |     |     |
...
}
| Using PATCH to | Update | a Non-configurable |     | attribute |
| -------------- | ------ | ------------------ | --- | --------- |
ExamplePATCHcurlcommand:
$ curl --noproxy -k -X PATCH "https://192.0.2.5/rest/v10.09/system/vlans"/100 -H
| "accept:                | */*" -d '{"oper_state": |               | "up"}' | -b /tmp/auth_cookie |
| ----------------------- | ----------------------- | ------------- | ------ | ------------------- |
| HTTP/1.1                | 400 Bad Request         |               |        |                     |
| Server:                 | nginx                   |               |        |                     |
| Date: Wed,              | 03 Nov 2021             | 23:08:02      | GMT    |                     |
| Content-Type:           | text/plain;             | charset=utf-8 |        |                     |
| Content-Length:         | 73                      |               |        |                     |
| Connection:             | keep-alive              |               |        |                     |
| X-Content-Type-Options: |                         | nosniff       |        |                     |
| X-Frame-Options:        | SAMEORIGIN              |               |        |                     |
| X-Content-Type-Options: |                         | nosniff       |        |                     |
| X-XSS-Protection:       | 1;                      | mode=block    |        |                     |
Strict-Transport-Security: max-age=31536000; includeSubdomains;
Content-Security-Policy: script-src 'self' 'unsafe-inline'; object-src 'none';
| font-src | *; media-src | 'none'; | form-action | 'self'; |
| -------- | ------------ | ------- | ----------- | ------- |
cannot modify the attribute: oper_state, reason: Non-configurable column
$
77
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------ | ------------------------- | --- | --- | --- |

Chapter 7

AnyCLI

AnyCLI

AnyCLI is a custom REST resource that allows for a predefined list of troubleshooting CLI commands to
be executed via REST API. Only one command is permitted per request and no concurrent requests are
allowed. The resource also provides an endpoint to retrieve the full list of available commands.

AnyCLI does not support CLI configuration commands. Only a subset of read-only show commands are available.

URI

n The URI to execute a CLI command: /rest/{version}/cli

n The URI to retrieve allowed CLI commands: /rest/{version}/cli/commands

Limitations

n Valid versions: v10.04 and higher

n Invalid version: v1

Security

Allowed roles: Administrator and operator.

Prohibited: Auditor

Response Time

If the response time exceeds the http server timeout (10min) the command will be canceled and with a
408 Request Timeout generated.

Concurrent Requests

One command is allowed per request.

Commands available per platform
The mechanism exposed via REST mirrors the same level of support the CLI has for a predefined list of
CLI commands. If a command is available but has a limitation, then the REST CLI feature will reflect the
same. For details in the description, usability, and health of any particular command, it is recommended
to review the functionality guide where the feature that command belongs to is documented.

Not all show commands are available on every platform. As per the Error Code section, an "invalid
command" response is expected whenever the CLI doesn't support the command. However, without
executing the command through CLI REST has no visibility into whether the command is available on any
given platform. Since the /cli/commands endpoint does not interact with CLI, it does not filter
unsupported commands.

The Allowed Commands section lists the complete set of commands available through REST CLI. The
commands from that list (which are not present in the Commands Available Per Platform table) are
available in every platform.

The table below describes whether a command is available or not for any given platform. An X denotes
the command is available in that platform:

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

78

|                       | 4   |     |     |     |     |     | 1   |
| --------------------- | --- | --- | --- | --- | --- | --- | --- |
|                       | 6   | 6 6 | 6   | 6 8 | 8 8 | 8 9 |     |
| Commands              | 1   |     |     |     |     |     | 0   |
|                       | 0   | 1 2 | 3   | 4 3 | 3 3 | 4 3 |     |
| Available Per         | 0   |     |     |     |     |     | 0   |
|                       | 0   | 0 0 | 0   | 0 2 | 2 6 | 0 0 |     |
| Platform              | 0   |     |     |     |     |     | 0   |
|                       | 0   | 0 0 | 0   | 0 0 | 5 0 | 0 0 |     |
|                       | i   |     |     |     |     |     | 0   |
| showactive-gateway    |     |     | X   | X X | X X | X X | X   |
| showaaaauthentication | X X | X X | X   | X   | X   |     |     |
port-accessinterfaceall
client-status
| showbgpall          |     |     | X   | X X | X X | X X | X   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
| showbgpallcommunity |     |     | X   | X X | X X | X X | X   |
| showbgpall          |     |     | X   | X X | X X | X X | X   |
extcommunity
| showbgpallflap- |     |     | X   | X X | X X | X X | X   |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
statistics
| showbgpallneighbors |     |     | X   | X X | X X | X X | X   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
| showbgpallpaths     |     |     | X   | X X | X X | X X | X   |
| showbgpallsummary   |     |     | X   | X X | X X | X X | X   |
| showbgpall-vrfall   |     |     | X   | X X | X X | X X | X   |
| showbgpall-vrfall   |     |     | X   | X X | X X | X X | X   |
neighbors
| showbgpall-vrfallpaths |     |     | X   | X X | X X | X X | X   |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| showbgpall-vrfall      |     |     | X   | X X | X X | X X | X   |
summary
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
community
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
extcommunity
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
flap-statistics
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
neighbors
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
paths
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
summary
AnyCLI|79

|                  | 4   |     |       |     |     | 1   |
| ---------------- | --- | --- | ----- | --- | --- | --- |
|                  | 6   | 6 6 | 6 6 8 | 8 8 | 8 9 |     |
| Commands         | 1   |     |       |     |     | 0   |
|                  | 0   | 1 2 | 3 4 3 | 3 3 | 4 3 |     |
| Available Per    | 0   |     |       |     |     | 0   |
|                  | 0   | 0 0 | 0 0 2 | 2 6 | 0 0 |     |
| Platform         | 0   |     |       |     |     | 0   |
|                  | 0   | 0 0 | 0 0 0 | 5 0 | 0 0 |     |
|                  | i   |     |       |     |     | 0   |
| showbgpl2vpnevpn |     |     | X X   | X X | X X | X   |
| showbgpl2vpnevpn |     |     | X X   | X X | X X | X   |
extcommunity
| showbgpl2vpnevpn |     |     | X X | X X | X X | X   |
| ---------------- | --- | --- | --- | --- | --- | --- |
neighbors
| showbgpl2vpnevpn |     |     | X X | X X | X X | X   |
| ---------------- | --- | --- | --- | --- | --- | --- |
paths
| showbgpl2vpnevpn |     |     | X X | X X | X X | X   |
| ---------------- | --- | --- | --- | --- | --- | --- |
summary
| showdhcp-server     |     | X   | X X X | X X | X X | X   |
| ------------------- | --- | --- | ----- | --- | --- | --- |
| showdhcpv4-snooping | X X | X X | X X   | X   | X   |     |
binding
| showdhcpv4-snooping | X X | X X | X X   | X   | X   |     |
| ------------------- | --- | --- | ----- | --- | --- | --- |
| showdhcpv6-server   |     | X   | X X X | X X | X X | X   |
| showdhcpv6-snooping | X X | X X | X X   | X   | X   |     |
binding
| showdhcpv6-snooping | X X | X X | X X | X   | X   |     |
| ------------------- | --- | --- | --- | --- | --- | --- |
| showevpnevidetail   |     |     | X X | X X | X X | X   |
| showevpnevi         |     |     | X X | X X | X X | X   |
| showevpnmac-ip      |     |     | X X | X X | X X | X   |
| showevpnvtep-       |     |     | X X | X X | X X | X   |
neighborall-vrfs
| showgbprole-mapping   |     |     | X X | X   |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- |
| showinterfacevxlanvni |     | X   | X X | X X | X X | X   |
vteps
| showinterfacevxlanvni |     | X   | X X | X X | X X | X   |
| --------------------- | --- | --- | --- | --- | --- | --- |
| showinterfacevxlan    |     | X   | X X | X X | X X | X   |
vtepsdetail
| showinterfacevxlan |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- |
vteps
| showipmroute |     | X   | X X X | X X | X X | X   |
| ------------ | --- | --- | ----- | --- | --- | --- |
80
| AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches) |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- |

|                    | 4   |     |     |     |     |     | 1   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
|                    | 6   | 6 6 | 6   | 6 8 | 8 8 | 8 9 |     |
| Commands           | 1   |     |     |     |     |     | 0   |
|                    | 0   | 1 2 | 3   | 4 3 | 3 3 | 4 3 |     |
| Available Per      | 0   |     |     |     |     |     | 0   |
|                    | 0   | 0 0 | 0   | 0 2 | 2 6 | 0 0 |     |
| Platform           | 0   |     |     |     |     |     | 0   |
|                    | 0   | 0 0 | 0   | 0 0 | 5 0 | 0 0 |     |
|                    | i   |     |     |     |     |     | 0   |
| showipospfall-vrfs |     | X   | X   | X X | X X | X X | X   |
| showipospfborder-  |     | X   | X   | X X | X X | X X | X   |
routersall-vrfs
| showippim              |     | X   | X   | X X | X X | X X | X   |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| showipv6mroute         |     | X   | X   | X X | X X | X X | X   |
| showipv6ospfv3all-vrfs |     | X   | X   | X X | X X | X X | X   |
| showipv6ospfv3         |     | X   | X   | X X | X X | X X | X   |
border-routersall-vrfs
| showipv6pim6    |     | X   | X   | X X | X X | X X | X   |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
| shownd-snooping |     | X   | X   | X   | X   |     |     |
binding
| shownd-snooping |     | X   | X   | X   | X   |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
prefix-list
| shownd-snooping |     | X   | X   | X   | X X | X   | X   |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
statistics
| shownd-snooping        |     | X   | X   | X   | X X | X   | X   |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| showport-accessclients | X X | X X | X   | X   | X   |     |     |
onboarding-method
device-profile
| showport-accessclients | X X | X X | X   | X   | X   |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
onboarding-method
dot1x
| showport-accessclients | X X | X X | X   | X   | X   |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
onboarding-method
mac-auth
| showport-accessclients | X X | X X | X   | X   | X   |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
onboarding-method
port-security
| showport-accessclients | X X | X X | X   | X   | X   |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| showport-accessgbp     |     |     | X   | X   | X   |     |     |
| showport-accesspolicy  | X X | X X | X   | X   | X   |     |     |
| showport-accessport-   | X X | X X | X   | X   | X   |     |     |
securityinterfaceall
client-status
AnyCLI|81

|                      | 4   |     |     |     |     |     | 1   |
| -------------------- | --- | --- | --- | --- | --- | --- | --- |
|                      | 6   | 6 6 | 6   | 6 8 | 8 8 | 8 9 |     |
| Commands             | 1   |     |     |     |     |     | 0   |
|                      | 0   | 1 2 | 3   | 4 3 | 3 3 | 4 3 |     |
| Available Per        | 0   |     |     |     |     |     | 0   |
|                      | 0   | 0 0 | 0   | 0 2 | 2 6 | 0 0 |     |
| Platform             | 0   |     |     |     |     |     | 0   |
|                      | 0   | 0 0 | 0   | 0 0 | 5 0 | 0 0 |     |
|                      | i   |     |     |     |     |     | 0   |
| showport-accessport- | X X | X X | X   | X   | X   |     |     |
securityinterfaceall
port-statistics
| showport-accessrole | X X | X X | X   | X   | X   |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
local
| showport-accessrole | X X | X X | X   | X   | X   |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
radius
| showport-accessport- | X X | X X | X   | X   | X   |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- |
securityviolationclient-
limit-exceededinterface
all
| showpower-over- | X X | X   | X   | X   |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
ethernet
| showradiusdyn- | X X | X X | X   | X   | X   |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- |
authorization
| showsecuremode          | X X | X X | X   | X X | X X | X X | X   |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- |
| showubtbrief            | X   | X   | X   | X   |     |     |     |
| showubtinformation      | X   | X   | X   | X   |     |     |     |
| showvsfdetail           |     | X   | X   |     |     |     |     |
| showvsflinkdetail       |     | X   | X   |     |     |     |     |
| showvsflinkerror-detail |     | X   | X   |     |     |     |     |
| showvsftopology         |     | X   | X   |     |     |     |     |
| showvsf                 |     | X   | X   |     |     |     |     |
| showvsxipigmp           |     |     |     | X X | X X | X X | X   |
| showvsxiproute          |     |     |     | X X | X X | X X | X   |
| showvsxipv6route        |     |     |     | X X | X X | X X | X   |
| showvsxmac-address-     |     |     |     | X X | X X | X X | X   |
table
| showvsxstatus |     |     |     | X X | X X | X X | X   |
| ------------- | --- | --- | --- | --- | --- | --- | --- |
CLI operations
Obtainsthevtyshoutputfromexecutingacommand.
POST
82
| AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches) |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |

Bodyoftherequestmustcontainacmdkeywiththecorrespondingcommandfromtheallowedlistof
commandsasitsvalue.Responsebodywillcontaintheplain/textoutputofvtyshifsuccessful.
Request body
{
"cmd": <cmd>
}
Response body
<vtysh_output>
| CLI commands | operations |     |
| ------------ | ---------- | --- |
Obtainsthelistofallowedcommands.
GET
ResponsebodywillcontainaJSONobjectscommandswiththelistofallowedcommands.
Response body
{
| "commands": <allowed_commands> |     |     |
| ------------------------------ | --- | --- |
}
Swagger
https://{IP}/api/{version}/cli
Full URI
n FullURI:https://{IP}/rest/{version}/cli/
n FullURI:https://{IP}/rest/{version}/cli/commands/
CURL example
| curl -k --noproxy               | "{IP}"            | -b cookies \ |
| ------------------------------- | ----------------- | ------------ |
| -X POST "https://{IP}/rest/cli" |                   | \            |
| -H "content-type:               | application/json" | \            |
| -d '{"cmd":"show                | uptime"}'         |              |
| curl -k --noproxy               | "{IP}"            | -b cookies \ |
-X GET "https://{IP}/rest/cli/commands" \
| -H "accept: application/json" |     |     |
| ----------------------------- | --- | --- |
Error codes
AnyCLI|83

HTTP Code

200 OK

400 Bad Request

Error

None

Response

VTYSH output

Invalid Input, Command incomplete or
Ambiguous command

Invalid command.

400 Bad Request

Invalid JSON Payload missing key

Invalid JSON input. '{}' required
parameter missing

401 Unauthorized

Authorization error

401 Authorization Required

403 Forbidden

403 Forbidden

Command not allowed (non in preset-list)

Command '{}' not allowed

Command not allowed on CLI

Command not allowed

429 Too Many Requests

Multiple Concurrent Requests Error

429 Too Many Requests

502 Bad Gateway

Any other CLI error

Command execution failed

Allowed commands

n show aaa accounting

n show aaa authentication port-access interface all client-status

n show aaa authentication

n show aaa authorization

n show aaa server-groups

n show active-gateway

n show arp all-vrfs

n show arp

n show bgp all

n show bgp all community

n show bgp all extcommunity

n show bgp all flap-statistics

n show bgp all neighbors

n show bgp all paths

n show bgp all summary

n show bgp all-vrf all

n show bgp all-vrf all neighbors

n show bgp all-vrf all paths

n show bgp all-vrf all summary

n show bgp ipv4 unicast

n show bgp ipv4 unicast community

n show bgp ipv4 unicast extcommunity

n show bgp ipv4 unicast flap-statistics

n show bgp ipv4 unicast neighbors

n show bgp ipv4 unicast paths

n show bgp ipv4 unicast summary

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

84

n show bgp l2vpn evpn

n show bgp l2vpn evpn extcommunity

n show bgp l2vpn evpn neighbors

n show bgp l2vpn evpn paths

n show bgp l2vpn evpn summary

n show boot-history

n show capacities

n show capacities-status

n show class ip

n show class ipv6

n show clock

n show copp-policy statistics

n show dhcp-relay

n show dhcp-server

n show dhcpv4-snooping binding

n show dhcpv4-snooping

n show dhcpv6-relay

n show dhcpv6-server

n show dhcpv6-snooping binding

n show dhcpv6-snooping

n show environment

n show evpn evi detail

n show evpn evi

n show evpn mac-ip

n show evpn vtep-neighbor all-vrfs

n show gbp role-mapping

n show interface brief

n show interface error-statistics

n show interface lag

n show interface physical

n show interface qos

n show interface queues

n show interface statistics

n show interface tunnel

n show interface utilization

n show interface vxlan vni vteps

n show interface vxlan vni

n show interface vxlan vteps detail

n show interface vxlan vteps

n show interface vxlan

n show interface

n show ip dns

n show ip helper-address

AnyCLI | 85

n show ip igmp

n show ip mroute

n show ip multicast summary

n show ip ospf all-vrfs

n show ip ospf border-routers all-vrfs

n show ip ospf interface all-vrfs

n show ip pim

n show ip route all-vrfs

n show ipv6 helper-address

n show ipv6 mld

n show ipv6 mroute

n show ipv6 neighbors all-vrfs

n show ipv6 neighbors

n show ipv6 ospfv3 all-vrfs

n show ipv6 ospfv3 border-routers all-vrfs

n show ipv6 ospfv3 interface all-vrfs

n show ipv6 pim6

n show lacp aggregates

n show lacp interfaces

n show lldp local

n show lldp neighbor

n show loop-protect

n show mac-address-table

n show module

n show nd-snooping binding

n show nd-snooping prefix-list

n show nd-snooping statistics

n show nd-snooping

n show ntp associations

n show ntp servers

n show ntp status

n show port-access clients onboarding-method device-profile

n show port-access clients onboarding-method dot1x

n show port-access clients onboarding-method mac-auth

n show port-access clients onboarding-method port-security

n show port-access clients

n show port-access gbp

n show port-access policy

n show port-access port-security interface all client-status

n show port-access port-security interface all port-statistics

n show port-access role local

n show port-access role radius

n show port-access port-security violation client-limit-exceeded interface all

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

86

n show power-over-ethernet

n show qos dscp-map

n show qos queue-profile

n show qos schedule-profile

n show qos trust

n show radius dyn-authorization

n show radius-server

n show resources

n show secure-mode

n show spanning-tree detail

n show spanning-tree mst detail

n show system inventory

n show system resource-utilization

n show tacacs-server

n show ubt brief

n show ubt information

n show uptime

n show version

n show vlan

n show vrf

n show vsf detail

n show vsf link detail

n show vsf link error-detail

n show vsf topology

n show vsf

n show ztp information

Full example
Get the full list of available commands:

n URI: /rest/{version}/cli/commands

n Valid versions: v10.04 and higher

n Operation: GET

n Query parameters: empty

n Request body: empty

n Response body: snippet

curl -X GET -b /tmp/cookies \
"https://{IP}/rest/{version}/cli/commands" \
-H "accept: application/json

n Response body: snippet

AnyCLI | 87

{
"commands":[
...
| "show | lldp local",    |     |     |     |
| ----- | --------------- | --- | --- | --- |
| "show | lldp neighbor", |     |     |     |
...
]
}
Then,retrievethevtyshoutputfromthecommandwithaPOST:
n URI:/rest/{version}/cli
n Operation:POST
n Query parameters:empty
n Request body:snippet
{
| "cmd": | "show uptime" |     |     |     |
| ------ | ------------- | --- | --- | --- |
}
curl -X POST -b /tmp/cookies "https://{IP}/rest/{version}/cli" \
| -H "content-type: | application/json" |            | -d '{"cmd":"show | uptime"}' |
| ----------------- | ----------------- | ---------- | ---------------- | --------- |
| n Response        | body:snippet      |            |                  |           |
| System has        | been up           | 11 minutes |                  |           |
88
AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches)

Chapter 8

Secure Mode

Secure Mode

Secure mode provides a method of setting the security mode of the device. A zeroization is required
before switching between enhanced and standard secure modes.

Setting secure mode requires populating writable attribute SYSTEM::secure_mode with the following
value:

true

Limitations

n Valid versions: v10.04 and higher

n Invalid version: v1

Security

Allowed roles: Administrator and operator.

Prohibited: Auditor

Example

The "secure_mode" variable has two values, as follows:

nfalse: secure mode flag is not set and the device continues to operate in its current state

ntrue: secure mode flag is set and the device reboots immediately, performs a zeroization, and boots to
Secure mode

The "secure_mode" flag always returns false as the device reboots immediately after this value is set, and after

booting to any mode, the flag is reset to false.

Get the secure mode writable attributes:

* __URI__: `/REST/{VERSION}/system`
* __ Valid versions__: `v10.04` and higher
* __Operation__: `GET`
* __Query parameters__:
* `selector=writable`
* __Request body__: empty
* __Response body__:
```json
{
...
"secure_mode":null
...
}
```
* __Description__: Get writable secure mode attributes to use them for a `PUT`
* __Swagger__: `https://{IP}/api/{version}/#/System/get_system`
* __Full URI__: `https://{IP}/rest/{version}/system?selector=writable`
* __Curl example__:
```bash
curl -X GET -b /tmp/cookies \

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

89

"https://{IP}/rest/{version}/system?selector=writable" \
| -H "accept: | application/json" |     |     |     |     |     |
| ----------- | ----------------- | --- | --- | --- | --- | --- |
```
"secure_mode":null
| * __CLI | equivalent |     | commands__: |     | N/A |     |
| ------- | ---------- | --- | ----------- | --- | --- | --- |
Or,getrelevantsecuremodeparameters:
| * __URI__:       | `/REST/{VERSION}/system` |       |          |     |            |     |
| ---------------- | ------------------------ | ----- | -------- | --- | ---------- | --- |
| * __ Valid       | versions__:              |       | `v10.04` |     | and higher |     |
| * __Operation__: |                          | `GET` |          |     |            |     |
| * __Query        | parameters__:            |       |          |     |            |     |
* `selector=writable`
| * __Request  | body__: |         | empty |     |     |     |
| ------------ | ------- | ------- | ----- | --- | --- | --- |
| * __Response |         | body__: |       |     |     |     |
```json
{
...
"secure_mode":null
...
}
```
* __Description__: Get writable secure mode attributes to use them for a `PUT`
* __Swagger__: `https://{IP}/api/{version}/#/System/get_system`
* __Full URI__: `https://{IP}/rest/{version}/system?selector=writable`
| * __Curl | example__: |     |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- | --- |
```bash
| curl -X | GET -b | /tmp/cookies |     | \   |     |     |
| ------- | ------ | ------------ | --- | --- | --- | --- |
"https://{IP}/rest/{version}/system?attributes=secure_mode" \
| -H "accept: | application/json" |     |     |     |     |     |
| ----------- | ----------------- | --- | --- | --- | --- | --- |
```
| <HTTP/1/1                 | 200                              | OK                |               |          |               |     |
| ------------------------- | -------------------------------- | ----------------- | ------------- | -------- | ------------- | --- |
| < Server:                 | nginx                            |                   |               |          |               |     |
| < Date:                   | Mon,                             | 27 Mar            | 2023          | 22:35:54 | GMT           |     |
| < Content-Type:           |                                  | application/json; |               |          | charset=utf-8 |     |
| < Content-Length:         |                                  | 62                |               |          |               |     |
| < Connection:             |                                  | keep-alive        |               |          |               |     |
| < Etag:                   | 52c2158e26ef504acd5b65a6e00b4a2b |                   |               |          |               |     |
| < X-Frame-Options:        |                                  |                   | SAMEORIGIN    |          |               |     |
| < X-Content-Type-Options: |                                  |                   |               | nosniff  |               |     |
| < X-XSS-Protection:       |                                  |                   | 1; mode=block |          |               |     |
< Strict-Transport-Security: max-age=31536000; includeSubdomains;
< Content-Security-Policy: script-src 'self' 'unsafe-inline'; object-src 'none';
| font-src | *; media-src |     | 'none'; | form-action |     | 'self'; |
| -------- | ------------ | --- | ------- | ----------- | --- | ------- |
<
{
| "secure_mode": |     | null, |     |     |     |     |
| -------------- | --- | ----- | --- | --- | --- | --- |
}
Then,usethereturnedJSONtodoaPATCH:
| * __URI__:       | `/REST/{VERSION}/system` |         |          |     |            |     |
| ---------------- | ------------------------ | ------- | -------- | --- | ---------- | --- |
| * __ Valid       | versions__:              |         | `v10.10` |     | and higher |     |
| * __Operation__: |                          | `PATCH` |          |     |            |     |
| * __Query        | parameters__:            |         | empty    |     |            |     |
| * __Request      | body__:                  |         |          |     |            |     |
```json
{
"secure_mode":true
SecureMode|90

}
```
* __Description__: Initiate a zeroization followed by setting secure mode
* __Swagger__: `https://{IP}/api/{version}/#/System/patch_system`
| * __Full | URI__:     | `https://{IP}/rest/{version}/system` |     |
| -------- | ---------- | ------------------------------------ | --- |
| * __Curl | example__: |                                      |     |
```bash
| curl {IP}                            | -X PATCH | -b /tmp/cookies   | \   |
| ------------------------------------ | -------- | ----------------- | --- |
| "https://{IP}/rest/{version}/system" |          |                   | \   |
| -H "accept:                          | */*"     | \                 |     |
| -H "Content-Type:                    |          | application/json" | \   |
-d \
"{
\"secure_mode\":true
}"
```
| * __CLI        | equivalent | commands__:                     |     |
| -------------- | ---------- | ------------------------------- | --- |
| * [secure-mode |            | enhanced](#secure-mode-command) |     |
Or,usethereturnedJSONtodoaPUT:
| * __URI__:       | `/REST/{VERSION}/system` |          |            |
| ---------------- | ------------------------ | -------- | ---------- |
| * __ Valid       | versions__:              | `v10.10` | and higher |
| * __Operation__: |                          | `PATCH`  |            |
| * __Query        | parameters__:            | empty    |            |
| * __Request      | body__:                  |          |            |
```json
{
"secure_mode":true
}
```
* __Description__: Initiate a zeroization followed by setting secure mode
* __Swagger__: `https://{IP}/api/{version}/#/System/patch_system`
| * __Full | URI__:     | `https://{IP}/rest/{version}/system` |     |
| -------- | ---------- | ------------------------------------ | --- |
| * __Curl | example__: |                                      |     |
```bash
| curl {IP}                            | -X PUT | -b /tmp/cookies   | \   |
| ------------------------------------ | ------ | ----------------- | --- |
| "https://{IP}/rest/{version}/system" |        |                   | \   |
| -H "accept:                          | */*"   | \                 |     |
| -H "Content-Type:                    |        | application/json" | \   |
-d \
"{
\"secure_mode\":true
}"
ShowingthesecuremodesettingisreadfromtheSYSTEM::secure_mode_statusattribute:
| * __URI__:       | `/REST/{VERSION}/system` |          |            |
| ---------------- | ------------------------ | -------- | ---------- |
| * __ Valid       | versions__:              | `v10.10` | and higher |
| * __Operation__: |                          | `GET`    |            |
| * __Query        | parameters__:            | empty    |            |
| * __Request      | body__:                  | empty    |            |
| * __Response     | body__:                  |          |            |
``json
{
...
"secure_mode_status":"enhanced"
...
}
91
AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches)

```
| * __Description__: |     |     | Get the | current | status | of secure mode. |
| ------------------ | --- | --- | ------- | ------- | ------ | --------------- |
* __Swagger__: `https://{IP}/api/{version}/#/System/get_system`
| * __Full | URI__:     | `https://{IP}/rest/{version}/system` |     |     |     |     |
| -------- | ---------- | ------------------------------------ | --- | --- | --- | --- |
| * __Curl | example__: |                                      |     |     |     |     |
```bash
| curl -X                              | GET -b            | /tmp/cookies |     | \   |     |     |
| ------------------------------------ | ----------------- | ------------ | --- | --- | --- | --- |
| "https://{IP}/rest/{version}/system" |                   |              |     |     | \   |     |
| -H "accept:                          | application/json" |              |     |     |     |     |
Or,showingtherelevantsecuremodeparameters:
| * __URI__:       | `/REST/{VERSION}/system` |         |          |     |            |     |
| ---------------- | ------------------------ | ------- | -------- | --- | ---------- | --- |
| * __ Valid       | versions__:              |         | `v10.10` |     | and higher |     |
| * __Operation__: |                          | `GET`   |          |     |            |     |
| * __Query        | parameters__:            |         | empty    |     |            |     |
| * __Request      | body__:                  |         | empty    |     |            |     |
| * __Response     |                          | body__: |          |     |            |     |
``json
{
...
"secure_mode_status":"enhanced"
...
}
```
| * __Description__: |     |     | Get the | current | status | of secure mode. |
| ------------------ | --- | --- | ------- | ------- | ------ | --------------- |
* __Swagger__: `https://{IP}/api/{version}/#/System/get_system`
| * __Full | URI__:     | `https://{IP}/rest/{version}/system` |     |     |     |     |
| -------- | ---------- | ------------------------------------ | --- | --- | --- | --- |
| * __Curl | example__: |                                      |     |     |     |     |
```bash
| curl -X | GET -b | /tmp/cookies |     | \   |     |     |
| ------- | ------ | ------------ | --- | --- | --- | --- |
"https://{IP}/rest/{version}/system?attributes=secure_mode_status" \
| -H "accept:               | application/json"                |                   |               |          |               |     |
| ------------------------- | -------------------------------- | ----------------- | ------------- | -------- | ------------- | --- |
| < HTTP/1.1                | 200                              | OK                |               |          |               |     |
| < Server:                 | nginx                            |                   |               |          |               |     |
| < Date:                   | Mon,                             | 27 Mar            | 2023          | 22:35:54 | GMT           |     |
| < Content-Type:           |                                  | application/json; |               |          | charset=utf-8 |     |
| < Content-Length:         |                                  | 62                |               |          |               |     |
| < Connection:             |                                  | keep-alive        |               |          |               |     |
| < Etag:                   | 52c2158e26ef504acd5b65a6e00b4a2b |                   |               |          |               |     |
| < X-Frame-Options:        |                                  |                   | SAMEORIGIN    |          |               |     |
| < X-Content-Type-Options: |                                  |                   |               | nosniff  |               |     |
| < X-XSS-Protection:       |                                  |                   | 1; mode=block |          |               |     |
< Strict-Transport-Security: max-age=31536000; includeSubdomains;
< Content-Security-Policy: script-src 'self' 'unsafe-inline'; object-src 'none';
| font-src | *; media-src |     | 'none'; | form-action |     | 'self'; |
| -------- | ------------ | --- | ------- | ----------- | --- | ------- |
<
{
| "secure_mode_status": |     |     | "enhanced" |     |     |     |
| --------------------- | --- | --- | ---------- | --- | --- | --- |
}
| Commands |     | available |     | per | platform |     |
| -------- | --- | --------- | --- | --- | -------- | --- |
ThemechanismexposedviaRESTmirrorsthesamelevelofsupporttheCLIhasforapredefinedlistof
CLIcommands.Ifacommandisavailablebuthasalimitation,thentheRESTCLIfeaturewillreflectthe
same.Fordetailsinthedescription,usability,andhealthofanyparticularcommand,itisrecommended
toreviewthefunctionalityguidewherethefeaturethatcommandbelongstoisdocumented.
Notallshowcommandsareavailableoneveryplatform.AspertheErrorCodesection,an"invalid
command"responseisexpectedwhenevertheCLIdoesn'tsupportthecommand.However,without
SecureMode|92

executingthecommandthroughCLIRESThasnovisibilityintowhetherthecommandisavailableon
anygivenplatform.Sincethe/cli/commandsendpointdoesnotinteractwithCLI,itdoesnotfilter
unsupportedcommands.
TheAllowedCommandssectionliststhecompletesetofcommandsavailablethroughRESTCLI.The
commandsfromthatlist(whicharenotpresentintheCommandsAvailablePerPlatformtable)are
availableineveryplatform.
Thetablebelowdescribeswhetheracommandisavailableornotforanygivenplatform.AnXdenotes
thecommandisavailableinthatplatform:
|                       | 4   |     |     |     |     |     | 1   |
| --------------------- | --- | --- | --- | --- | --- | --- | --- |
|                       | 6   | 6 6 | 6   | 6 8 | 8 8 | 8 9 |     |
| Commands              | 1   |     |     |     |     |     | 0   |
|                       | 0   | 1 2 | 3   | 4 3 | 3 3 | 4 3 |     |
| Available Per         | 0   |     |     |     |     |     | 0   |
|                       | 0   | 0 0 | 0   | 0 2 | 2 6 | 0 0 |     |
| Platform              | 0   |     |     |     |     |     | 0   |
|                       | 0   | 0 0 | 0   | 0 0 | 5 0 | 0 0 |     |
|                       | i   |     |     |     |     |     | 0   |
| showactive-gateway    |     |     | X   | X X | X X | X X | X   |
| showaaaauthentication | X X | X X | X   | X   | X   |     |     |
port-accessinterfaceall
client-status
| showbgpall          |     |     | X   | X X | X X | X X | X   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
| showbgpallcommunity |     |     | X   | X X | X X | X X | X   |
| showbgpall          |     |     | X   | X X | X X | X X | X   |
extcommunity
| showbgpallflap- |     |     | X   | X X | X X | X X | X   |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
statistics
| showbgpallneighbors |     |     | X   | X X | X X | X X | X   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
| showbgpallpaths     |     |     | X   | X X | X X | X X | X   |
| showbgpallsummary   |     |     | X   | X X | X X | X X | X   |
| showbgpall-vrfall   |     |     | X   | X X | X X | X X | X   |
| showbgpall-vrfall   |     |     | X   | X X | X X | X X | X   |
neighbors
| showbgpall-vrfallpaths |     |     | X   | X X | X X | X X | X   |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| showbgpall-vrfall      |     |     | X   | X X | X X | X X | X   |
summary
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
community
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
extcommunity
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
flap-statistics
93
| AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches) |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |

|                    | 4   |     |     |     |     |     | 1   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
|                    | 6   | 6 6 | 6   | 6 8 | 8 8 | 8 9 |     |
| Commands           | 1   |     |     |     |     |     | 0   |
|                    | 0   | 1 2 | 3   | 4 3 | 3 3 | 4 3 |     |
| Available Per      | 0   |     |     |     |     |     | 0   |
|                    | 0   | 0 0 | 0   | 0 2 | 2 6 | 0 0 |     |
| Platform           | 0   |     |     |     |     |     | 0   |
|                    | 0   | 0 0 | 0   | 0 0 | 5 0 | 0 0 |     |
|                    | i   |     |     |     |     |     | 0   |
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
neighbors
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
paths
| showbgpipv4unicast |     |     | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
summary
| showbgpl2vpnevpn |     |     | X   | X   | X X | X X | X   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- |
| showbgpl2vpnevpn |     |     | X   | X   | X X | X X | X   |
extcommunity
| showbgpl2vpnevpn |     |     | X   | X   | X X | X X | X   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- |
neighbors
| showbgpl2vpnevpn |     |     | X   | X   | X X | X X | X   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- |
paths
| showbgpl2vpnevpn |     |     | X   | X   | X X | X X | X   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- |
summary
| showdhcp-server     |     | X   | X   | X X | X X | X X | X   |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
| showdhcpv4-snooping | X X | X X | X   | X   | X   | X   |     |
binding
| showdhcpv4-snooping | X X | X X | X   | X   | X   | X   |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
| showdhcpv6-server   |     | X   | X   | X X | X X | X X | X   |
| showdhcpv6-snooping | X X | X X | X   | X   | X   | X   |     |
binding
| showdhcpv6-snooping | X X | X X | X   | X   | X   | X   |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
| showevpnevidetail   |     |     | X   | X   | X X | X X | X   |
| showevpnevi         |     |     | X   | X   | X X | X X | X   |
| showevpnmac-ip      |     |     | X   | X   | X X | X X | X   |
| showevpnvtep-       |     |     | X   | X   | X X | X X | X   |
neighborall-vrfs
| showgbprole-mapping   |     |     | X   | X   | X   |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- |
| showinterfacevxlanvni |     | X   | X   | X   | X X | X X | X   |
vteps
SecureMode|94

|                       | 4   |     |     |     |     |     | 1   |
| --------------------- | --- | --- | --- | --- | --- | --- | --- |
|                       | 6   | 6 6 | 6   | 6 8 | 8 8 | 8 9 |     |
| Commands              | 1   |     |     |     |     |     | 0   |
|                       | 0   | 1 2 | 3   | 4 3 | 3 3 | 4 3 |     |
| Available Per         | 0   |     |     |     |     |     | 0   |
|                       | 0   | 0 0 | 0   | 0 2 | 2 6 | 0 0 |     |
| Platform              | 0   |     |     |     |     |     | 0   |
|                       | 0   | 0 0 | 0   | 0 0 | 5 0 | 0 0 |     |
|                       | i   |     |     |     |     |     | 0   |
| showinterfacevxlanvni |     | X   | X   | X   | X X | X X | X   |
| showinterfacevxlan    |     | X   | X   | X   | X X | X X | X   |
vtepsdetail
| showinterfacevxlan |     | X   | X   | X   | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
vteps
| showipmroute       |     | X   | X   | X X | X X | X X | X   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- |
| showipospfall-vrfs |     | X   | X   | X X | X X | X X | X   |
| showipospfborder-  |     | X   | X   | X X | X X | X X | X   |
routersall-vrfs
| showippim              |     | X   | X   | X X | X X | X X | X   |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| showipv6mroute         |     | X   | X   | X X | X X | X X | X   |
| showipv6ospfv3all-vrfs |     | X   | X   | X X | X X | X X | X   |
| showipv6ospfv3         |     | X   | X   | X X | X X | X X | X   |
border-routersall-vrfs
| showipv6pim6    |     | X   | X   | X X | X X | X X | X   |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
| shownd-snooping |     | X   | X   | X   | X   |     |     |
binding
| shownd-snooping |     | X   | X   | X   | X   |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
prefix-list
| shownd-snooping |     | X   | X   | X   | X X | X   | X   |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
statistics
| shownd-snooping        |     | X   | X   | X   | X X | X   | X   |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| showport-accessclients | X X | X X | X   | X   | X   |     |     |
onboarding-method
device-profile
| showport-accessclients | X X | X X | X   | X   | X   |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
onboarding-method
dot1x
| showport-accessclients | X X | X X | X   | X   | X   |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
onboarding-method
mac-auth
| showport-accessclients | X X | X X | X   | X   | X   |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
onboarding-method
port-security
95
| AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches) |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |

|                        | 4   |     |     |     |     |     | 1   |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
|                        | 6   | 6 6 | 6   | 6 8 | 8 8 | 8 9 |     |
| Commands               | 1   |     |     |     |     |     | 0   |
|                        | 0   | 1 2 | 3   | 4 3 | 3 3 | 4 3 |     |
| Available Per          | 0   |     |     |     |     |     | 0   |
|                        | 0   | 0 0 | 0   | 0 2 | 2 6 | 0 0 |     |
| Platform               | 0   |     |     |     |     |     | 0   |
|                        | 0   | 0 0 | 0   | 0 0 | 5 0 | 0 0 |     |
|                        | i   |     |     |     |     |     | 0   |
| showport-accessclients | X X | X X | X   | X   | X   |     |     |
| showport-accessgbp     |     |     | X   | X   | X   |     |     |
| showport-accesspolicy  | X X | X X | X   | X   | X   |     |     |
| showport-accessport-   | X X | X X | X   | X   | X   |     |     |
securityinterfaceall
client-status
| showport-accessport- | X X | X X | X   | X   | X   |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- |
securityinterfaceall
port-statistics
| showport-accessrole | X X | X X | X   | X   | X   |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
local
| showport-accessrole | X X | X X | X   | X   | X   |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
radius
| showport-accessport- | X X | X X | X   | X   | X   |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- |
securityviolationclient-
limit-exceededinterface
all
| showpower-over- | X X | X   | X   | X   |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
ethernet
| showradiusdyn- | X X | X X | X   | X   | X   |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- |
authorization
| showsecuremode          | X X | X X | X   | X X | X X | X X | X   |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- |
| showubtbrief            | X   | X   | X   | X   |     |     |     |
| showubtinformation      | X   | X   | X   | X   |     |     |     |
| showvsfdetail           |     | X   | X   |     |     |     |     |
| showvsflinkdetail       |     | X   | X   |     |     |     |     |
| showvsflinkerror-detail |     | X   | X   |     |     |     |     |
| showvsftopology         |     | X   | X   |     |     |     |     |
| showvsf                 |     | X   | X   |     |     |     |     |
| showvsxipigmp           |     |     |     | X X | X X | X X | X   |
| showvsxiproute          |     |     |     | X X | X X | X X | X   |
SecureMode|96

|                     | 4   |     |     |     |     | 1   |
| ------------------- | --- | --- | --- | --- | --- | --- |
|                     | 6 6 | 6 6 | 6 8 | 8 8 | 8 9 |     |
| Commands            | 1   |     |     |     |     | 0   |
|                     | 0 1 | 2 3 | 4 3 | 3 3 | 4 3 |     |
| Available Per       | 0   |     |     |     |     | 0   |
|                     | 0 0 | 0 0 | 0 2 | 2 6 | 0 0 |     |
| Platform            | 0   |     |     |     |     | 0   |
|                     | 0 0 | 0 0 | 0 0 | 5 0 | 0 0 |     |
|                     | i   |     |     |     |     | 0   |
| showvsxipv6route    |     |     | X X | X X | X X | X   |
| showvsxmac-address- |     |     | X X | X X | X X | X   |
table
| showvsxstatus |     |     | X X | X X | X X | X   |
| ------------- | --- | --- | --- | --- | --- | --- |
97
| AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches) |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- |

VSX peer switches and REST API access

Chapter 9

VSX peer switches and REST API access

If Virtual Switching Extension (VSX) is enabled, you can access the REST API of a peer switch without
having to separately log into or manage a session cookie from that peer switch.

To access a peer REST API from your connected switch, insert /vsx-peer in the URI path after the server
URL and before the REST API and version identifier.

For example:
https://192.0.2.5/vsx-peer/rest/v10.xx/...

The following uses of /vsx-peer in the URI path are not supported:

n You cannot specify the login resource. Requests to /vsx-peer/rest/v10.04/login are not required

because logging in to one device automatically gives you access to the peer device.

n You cannot access the Web UI of a VSX peer switch. Setting the browser address to https://<connected_

switch_ip>/vsx-peer is not supported.

n You cannot specify a VSX peer switch in the URIs in topic subscription messages in the real-time notifications

framework. However, you can access the real-time notifications framework on the VSX peer switch by setting

the connection address to the following:

wss://<connected_switch_ip>/vsx-peer/rest/v10.xx/notification

Please note the following points when using REST API with VSX.

n VSX must be enabled on both switches, and the interswitch link (ISL) must be up.

n REST API access must be enabled on the switch to which you are connected.

n For write access, the REST API access mode must be set to read-write on the switch to which you are

connected.

n You must be logged in to the switch to which you are connected. For example, if you are connected to

the primary VSX switch, you must be logged in to the primary switch.

n When configuration synchronization is enabled, supported configuration changes on the primary VSX
switch are replicated on the secondary VSX switch. Changing the configuration of a secondary VSX
switch might cause the configurations to be out of synchronization.

n Audit messages are logged on the peer switch, with the user information from the switch to which the

user is connected.

Examples of curl commands

n Getting the VSX status of the secondary VSX switch while connected to the primary VSX switch at IP

address 192.0.2.5:

$ curl --noproxy "192.0.2.5" -k GET \
-b /tmp/primary_auth_cookie \
"https://192.0.2.5/vsx-peer/rest/v10.09/system/vsx?attributes=oper_status"

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

98

n GettingtheVSXstatusoftheprimaryVSXswitchwhileconnectedtothesecondaryVSXswitchatIP
address192.0.2.6:
| $ curl                        | --noproxy | "192.0.2.6" | -k GET | \   |     |
| ----------------------------- | --------- | ----------- | ------ | --- | --- |
| -b /tmp/secondary_auth_cookie |           |             | \      |     |     |
"https://192.0.2.6/vsx-peer/rest/v10.09/system/vsx?attributes=oper_status"
n GettingthenamesandIPaddressesofinterfacesonsecondaryVSXswitchwhileconnectedtothe
primaryVSXswitchatIPaddress192.0.2.5:
| $ curl                      | --noproxy | "192.0.2.5" | -k GET | \   |     |
| --------------------------- | --------- | ----------- | ------ | --- | --- |
| -b /tmp/primary_auth_cookie |           |             | \      |     |     |
"https://192.0.2.5/vsx-
peer/rest/v10.09/system/interfaces?depth=2&attributes=name,ipv4_address"
FormoreinformationaboutVSX,seetheVirtualSwitchingExtension(VSX)Guide.
| Example: | Interacting |     | with | a VSX peer | switch |
| -------- | ----------- | --- | ---- | ---------- | ------ |
Inthefollowingexamples,VirtualSwitchingExtension(VSX)isenabled,theprimaryVSXswitchIP
addressis192.0.2.5,andthesecondaryVSXswitchIPaddressis192.0.2.6.
GettingthelistofallVLANSontheconnectedswitchatIPaddress192.0.2.5:
ExamplemethodandURI:
n
GET "https://192.0.2.5/rest/v10.xx/system/vlans"
n Examplecurlcommand:
| $ curl --noproxy            |     | 192.0.2.5 | -k GET \ |     |     |
| --------------------------- | --- | --------- | -------- | --- | --- |
| -b /tmp/primary_auth_cookie |     |           | \        |     |     |
"https://192.0.2.5/rest/v10.09/system/vlans"
GettingthelistofallVLANsonthepeerVSXswitch:
ExamplemethodandURI:
n
GET "https://192.0.2.5/vsx-peer/rest/v10.xx/system/vlans
n Examplecurlcommand:
| $ curl --noproxy            |     | 192.0.2.5 | -k GET \ |     |     |
| --------------------------- | --- | --------- | -------- | --- | --- |
| -b /tmp/primary_auth_cookie |     |           | \        |     |     |
"https://192.0.2.5/vsx-peer/rest/v10.09/system/vlans"
GettingtheVSXstatusofthesecondaryVSXswitchwhileconnectedtotheprimaryVSXswitchatIP
address192.0.2.5:
n ExamplemethodandURI:
GET “https://192.0.2.5/vsx-peer/rest/v10.xx/system/vsx?attributes?oper_status"
n Examplecurlcommand:
VSXpeerswitchesandRESTAPIaccess|99

| $ curl --noproxy            | 192.0.2.5 | -k GET \ |
| --------------------------- | --------- | -------- |
| -b /tmp/primary_auth_cookie |           | \        |
"https://192.0.2.5/vsx-peer/rest/v10.09/system/vsx?attributes?oper_status"
YoucanalsogettheVSXstatusoftheprimaryVSXswitchwhileconnectedtothesecondaryVSXswitch.
100
AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches)

Chapter 10

AOS-CX real-time notifications
subsystem

AOS-CX real-time notifications subsystem

The AOS-CX REST API, combined with built-in databases that provide configuration, state, statistical data,
and time-series data for the features and protocols running in the switch, provides a flexible means for
switch programmability. Each resource or collection of resources inside the switch is uniquely identified
by its URI.

Clients can use the REST API to request information about resources. However, this polling ability does
not address the specific use cases in which network management systems need to receive live data or
real-time events from the switch. There is a need to have a live notification subsystem that provides the
remote network management system with real-time information about any changes that occur in the
switch. Timely information about changes is important for troubleshooting and statistical data analyses,
as well as for the immediate reaction to real-time events.

The AOS-CX real-time notifications subsystem enables external clients to connect to the switch through
a secure WebSocket Protocol connection and to receive real-time notifications about the switch
resources, configuration changes, state changes, and statistical information of their interest.

The WebSocket Protocol was selected based on latency, throughput, resource utilization, network
overhead, and security requirements. The handshake part of the WebSocket protocol uses HTTPS, so
there is no need to open a new port on the switch side, and there is no need to provide a new
authentication mechanism. Multiple clients and connections are supported.

AOS-CX notification messages use JSON encoding. The JSON encoding was designed to align with REST
payloads, which enable clients to use combined REST and notification solutions.

The ability to subscribe to these push notifications about a variety of types of information about the
switch, combined with the structured nature of the JSON data reported by the switch database, enables
a form of network monitoring commonly called telemetry streaming.

Interested clients, known as subscribers, might include the following:

n Web clients such as the AOS-CX Web UI

n Network management systems

n Monitoring scripts

Secure WebSocket Protocol connections for notifications
You subscribe to and receive notifications from the switch through a secure WebSocket Protocol
(wss://) connection.

A secure WebSocket Protocol connection is a secure, persistent, and full-duplex connection between a
client and a server. Either the client or the server can send data in the form of messages at any time.

The handshake part of the WebSocket Protocol uses HTTPS, so there is no need to open a new port on
the switch side, and there is no need to provide a new authentication mechanism. When you connect to
a switch through a secure WebSocket Protocol connection, you pass the session cookie received from
logging in to the REST API. Secure WebSocket Protocol connections to switches running AOS-CX software
remain active until the connection is closed, even after the session cookie expires. Multiple clients and
connections are supported.

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

101

For more information about the WebSocket Protocol see RFC 6455: The WebSocket Protocol at:
https://tools.ietf.org/html/rfc6455

Notification topics as switch resource URIs

When you subscribe to notifications, you subscribe to notifications about specific topics. A topic is the
URI of a specific switch resource. That URI can contain a query string that specifies particular attributes
of that resource.

For example, specifying the following URI as a topic results in notifications being sent when the
administrative state or link state of any interface changes, but not when some other attribute of an
interface changes:
/rest/v10.09/system/interfaces?depth=2&attributes=admin_state,link_state

The AOS-CX REST API Reference lists all the switch resources. You can use the GET method of the
resource in the AOS-CX REST API Reference to determine the URI for that switch resource, including the
query string to specify an attribute or list of attributes.

Rules for topic URIs

A topic is the URI of a switch resource:

Not all switch resource URIs are supported as notification topics.

The Implementation Notes section of the GET method of the resource in the AOS-CX REST API
Reference indicates if the resource is not supported by the notifications subsystem.

n Wildcard characters (*) are supported. In this example, you can subscribe to all VLANS:

```dita/rest/v10.04/system/vlans/*
```

n Specifying a resource on a peer VSX switch, by including /vsx-peer in the URIs for topic subscription

messages, is not supported.

To specify a peer switch, include /vsx-peer in the URL of the WSS connection. For example, to get
notifications about VLANs on a peer, first open a connection to wss://192.0.2.5/vsx-
peer/rest/v10.xx/notification and then subscribe to /rest/v10.04/system/vlans as the topic
name.

You can specify a specific resource instance or a collection of resources. Examples of specific resource
instances:

n /rest/v10.xx/system/vrfs/default

n /rest/v10.xx/system/vlans/1

Examples of resource collections:

n /rest/v10.xx/system/vrfs/default/bgp_routers

n /rest/v10.xx/system/vlans

The depth query parameter is supported, with a maximum value of 2, only with resource collections. For
example:

n Correct: /rest/v10.xx/system/vlans?depth=1

n Incorrect: /rest/v10.xx/system/vlans?depth=3.

AOS-CX real-time notifications subsystem | 102

The attributes query parameter is supported. You can specify a comma-separated list of attribute
names in the query string for either resource collections or resource instances. If attributes are
specified, then the subscriber receives notification messages only when the value of one of the specified
attributes changes. For example:

The following URI specifies the administrative state and link state of all interfaces on the switch:

/rest/v10.xx/system/interfaces?attributes=admin_state,link_state

The following URI specifies the names of the VLANs:
/rest/v10.xx/system/vlans?depth=2&attributes=name

The names of the attributes must match the names as documented in the AOS-CX REST API Reference
for the GET method of the resource.

Notification security features

The notification feature uses secure WebSocket connections based on the TLS v1.2 protocol (Transport
Layer Security version 1.2), which is the same protocol used for the REST HTTPS connections.

The switch uses self-signed certificates. To avoid certificate verification errors, disable certificate
verification when establishing the connection.

AOS-CX real-time notifications subsystem reference summary

The following information is intended as a quick reference for experienced users. Values are not
configurable unless noted otherwise.

Connection protocol

WebSocket secure (wss://)

Port

443

Message format

JSON

Message types

The following are the supported message types:

n subscribe

n unsubscribe

n success

n error

n notification

Authorization

Session cookie from successful HTTPS login request

Notification resource URI

wss://<IP-ADDR>/rest/v10.xx/notification

<IP-ADDR> is the IP address of the switch.

For example:
wss://192.0.2.5/rest/v10.xx/notification

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

103

Session idle timeout

None

Session hard timeout

None

Subscription persistence

Subscriptions are active only while the WebSocket secure connection is open.

Configuration maximums

n Maximum number of subscribers per switch: 50

n Maximum number of topics in one subscription message: 2000

Enabling the notifications subsystem on a switch
The AOS-CX real-time notifications subsystem relies on the REST API, so the REST API must be enabled
on the switch and VRF from which you want to receive notifications.

HTTPS server must be enabled on the specified VRF. The VRF you specify determines from which
network the HTTPS server can be accessed. You can enable access on multiple VRFs, including user-
defined VRFs.

Establishing a secure WebSocket connection through a web
browser

Prerequisites

n Access to the switch REST API must be enabled. The REST API access mode can be either read-only or

read/write.

n The web browser you use must support the secure WebSocket Protocol.

Procedure

1. Open a web browser page and log in to the switch Web UI or the REST API.

The session cookie is managed by the browser and is shared among browser tabs.

2. From a different tab in the same browser, open the page that contains the WebSocket interface.

For example, many browsers have a plugin for secure WebSocket connections.

3. Connect to the switch at the following URL:

wss://<IP-ADDR>/rest/v10.xx/notification

<IP-ADDR> is the IP address of the switch.

For example:
wss://192.0.2.5/rest/v10.xx/notification

After the connection is established, you can use the interface to send subscribe or unsubscribe
messages and to view the responses and notification messages.

Establishing a secure WebSocket connection using a script

AOS-CX real-time notifications subsystem | 104

Access to the switch REST API must be enabled. The REST API access mode can be either read-only or
read/write.

n If you are using a script, you must include the actions to log in, get the session cookie, store the
session cookie, and pass the session cookie with the secure WebSocket connection request.

When you create the secure WebSocket connection, use the following URL:
wss://<IP-ADDR>/rest/v10.xx/notification

<IP-ADDR> is the IP address of the switch.

For example:
wss://192.0.2.5/rest/v10.xx/notification

n The exact methods to use to create connections and handle notification messages depend on the

scripting language and library module you choose.

Subscribing to topics

Prerequisites

n You must have a secure WebSocket connection to the switch.

n Access to the switch REST API must be enabled. The REST API access mode can be either read-only or

read/write.

Procedure

Using the WebSocket secure connection, send a subscribe message that contains the topics to which
you want to subscribe.

Some resource attributes—typically in the statistics category—are not populated until a client requests
the information.

For example:

{

"type": "subscribe",
"topics": [

"name": "/rest/v10.04/system/vrfs"

"name": "/rest/v10.04/system/vlans/1?attributes=admin,oper_state_reason"

{

},
{

}

]

}

If there is an error in the syntax of the subscribe message, an error message is sent back to the client
with the description of the error. For example, for the following incorrect subscribe message:

...
{"topics":[{"name":"/rest/v10.04/system/vrfssss"}],"type":"subscribe"}
...

The corresponding error message is sent:

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

105

{
"type":"error",
| "message": | "resource | or attribute | vrfssss not | found", |
| ---------- | --------- | ------------ | ----------- | ------- |
| "data":    | null      |              |             |         |
}
Ifthesubscriberalreadyhasasubscriptiontothespecifiedtopic,thefollowingerrorisreturned:
{
"type":"error",
"message":"The topic or combination of topics have been already subscribed."
}
Exampleofamessagereturnedbyasuccessfulsubscriptionattempt:
{
| "type": | "success", |     |     |     |
| ------- | ---------- | --- | --- | --- |
| "data": | [          |     |     |     |
{
"topicname": "/rest/v10.04/system/vlans/1?attributes=admin,oper_state_
reason",
| "resources": | [   |     |     |     |
| ------------ | --- | --- | --- | --- |
{
|     | "operation": | "", |     |     |
| --- | ------------ | --- | --- | --- |
"uri": "/rest/v10.04/system/vlans/1",
"values": {
|     | "admin":             | "up", |                  |     |
| --- | -------------------- | ----- | ---------------- | --- |
|     | "oper_state_reason": |       | "no_member_port" |     |
}
}
]
},
{
| "topicname": | "/rest/v10.04/system/vrfs", |     |     |     |
| ------------ | --------------------------- | --- | --- | --- |
| "resources": | [                           |     |     |     |
{
|     | "operation": | "", |     |     |
| --- | ------------ | --- | --- | --- |
"uri": "/rest/v10.04/system/vrfs/default",
"values": {}
},
{
|     | "operation": | "", |     |     |
| --- | ------------ | --- | --- | --- |
"uri": "/rest/v10.04/system/vrfs/mgmt",
"values": {}
}
]
}
],
| "subscriber_name": |     | "4bcf8uka90ki", |     |     |
| ------------------ | --- | --------------- | --- | --- |
}
| Unsubscribing | from | topics |     |     |
| ------------- | ---- | ------ | --- | --- |
Prerequisites
AOS-CXreal-timenotificationssubsystem|106

n YoumusthaveasecureWebSocketconnectiontotheswitch.
n TheswitchmusthaveRESTAPIaccessenabled.TheRESTAPIaccessmodecanbeeitherread-onlyor
read/write.
Procedure
UsethesecureWebSocketconnectiontosendanunsubscribemessagethatspecifiesthetopicortopics
fromwhichyounolongerwantnotifications.
Useacommatoseparatetopicsinalistoftopics.
Youmustbeconnectedasthesamesubscriberthatsubscribedtothetopic.Forexample,youmustbe
usingthesamewebbrowsersessionorbepassingthesamesessioncookiewiththerequest.
Forexample,tounsubscribenotificationsaboutthedefaultVRF,sendthefollowingmessagethrough
theWebSocketsecureconnection:
{
| "type":   | "unsubscribe", |     |
| --------- | -------------- | --- |
| "topics": | [              |     |
{
| "name": | "/rest/v10.04/system/vrfs/default" |     |
| ------- | ---------------------------------- | --- |
}
]
}
If the subscriber does not have a subscription to that topic, the following
| message is | returned: |     |
| ---------- | --------- | --- |
{
| "type": | "error", |     |
| ------- | -------- | --- |
"message": "subscription /rest/v10.04/system/vrfs doesn't exist"
| "data": | null |     |
| ------- | ---- | --- |
}
Theerrorcanindicatethatyouhavealreadyunsubscribed,theconnectionwaslost,oryouattemptedto
unsubscribefromadifferentsubscriber.
Iftherequestissuccessful,thefollowingmessageisreturned:
{
| "type":    | "success",    |               |
| ---------- | ------------- | ------------- |
| "message": | "Successfully | unsubscribe." |
}
| Subscription | throttling |     |
| ------------ | ---------- | --- |
Throttlingisanoptionalparameterthatcanbepassedinthesubscriptionmessagetospecifythe
notificationintervalinseconds.Notificationsareonlysentifthereareanychangesduringthespecified
intervaloftime.
ShowingasubscriptionforallVLANswithanintervalof5seconds:
{
| "type":     | "subscribe", |     |
| ----------- | ------------ | --- |
| "interval": | 5,           |     |
| "topics":   | [            |     |
{
107
AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches)

"name":"/rest/v10.04/system/vlans?depth=2"

}

]

}

With the throttling above, the system will send notifications for all VLANs every 5 seconds if there are
any changes to the VLANs.

In Figure 1, Subscription throttling notifications, the system sent a notification because a change was
made to the description and voice was enabled for one of the VLANs during the specified interval of
time.

Figure 1 Subscription throttling notifications

Subscription throttling can also be used to handle notifications for resource attributes that only provide
interval-based notifications, known as on-demand attributes.

Showing a subscription for an on-demand attributes with an interval of 10 seconds:

{

"type": "subscribe",
"interval": 10,
"topics": [

"name":"/rest/v10.04/system/interfaces/1%2F14?attributes=aclv4_out_
  statistics,policy_out_statistics"

{

}

]

}

In Figure 2, Subscription throttling notifications for on-demand attributes, the system sent a notification
for the on-demand attributes during the interval specified in the example above.

Figure 2 Subscription throttling notifications for on-demand attributes

AOS-CX real-time notifications subsystem | 108

| Parts of | a subscribe | message |     |     |
| -------- | ----------- | ------- | --- | --- |
Asubscribemessageisthemessagesentwhenasubscriberrequestsasubscriptiontoatopicona
switch.ThesubscribemessageisinJSONformat.
| Subscribe | message | example |     |     |
| --------- | ------- | ------- | --- | --- |
{
| "type":   | "subscribe", |     |     |     |
| --------- | ------------ | --- | --- | --- |
| "topics": | [            |     |     |     |
{
"name": "/rest/v10.04/system/vrfs"
},
{
"name": "/rest/v10.04/system/vlans/1?attributes=admin,oper_state_reason"
}
]
}
| Components | of a | subscribe | message |     |
| ---------- | ---- | --------- | ------- | --- |
type
Required.Forasubscribemessage,youmustspecifythefollowingvalue:subscribe
topics
Required.Thevalueisacomma-separatedlistofoneormoretopicsinJSONkey-valueformat.A
topicincludesonecomponent:
name
Required.Thenameofthetopic,identifiedbytheURIoftheswitchresource,includingthe
optionalquerystring.
| Parts of | a subscription |     | success | message |
| -------- | -------------- | --- | ------- | ------- |
109
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |
| ------------------------ | ------------------------- | --- | --- | --- |

Whenasubscriptionrequestissuccessful,asubscriptionsuccessmessageisreturned.Thesubscription
successmessageisinJSONformat.
| Example | success | message |     |     |
| ------- | ------- | ------- | --- | --- |
{
| "type": | "success", |     |     |     |
| ------- | ---------- | --- | --- | --- |
| "data": | [          |     |     |     |
{
"topicname": "/rest/v10.04/system/vlans/1?attributes=admin,oper_state_
reason",
|     | "resources": | [   |     |     |
| --- | ------------ | --- | --- | --- |
{
|     | "operation":         | "",                            |                  |     |
| --- | -------------------- | ------------------------------ | ---------------- | --- |
|     | "uri":               | "/rest/v10.04/system/vlans/1", |                  |     |
|     | "values":            | {                              |                  |     |
|     | "admin":             | "up",                          |                  |     |
|     | "oper_state_reason": |                                | "no_member_port" |     |
}
}
]
},
{
|     | "topicname": | "/rest/v10.04/system/vrfs", |     |     |
| --- | ------------ | --------------------------- | --- | --- |
|     | "resources": | [                           |     |     |
{
|     | "operation": | "",                                 |     |     |
| --- | ------------ | ----------------------------------- | --- | --- |
|     | "uri":       | "/rest/v10.04/system/vrfs/default", |     |     |
|     | "values":    | {}                                  |     |     |
},
{
|     | "operation": | "",                              |     |     |
| --- | ------------ | -------------------------------- | --- | --- |
|     | "uri":       | "/rest/v10.04/system/vrfs/mgmt", |     |     |
|     | "values":    | {}                               |     |     |
}
]
}
],
| "subscriber_name": |     | "4bcf8uka90ki", |     |     |
| ------------------ | --- | --------------- | --- | --- |
}
| Components | of  | subscription | success | message |
| ---------- | --- | ------------ | ------- | ------- |
type
Identifiesthetypeofmessage.Successmessageshavethetype:success
subscriber_name
Containsauniqueidentifierthatrepresentsthenameofthesubscriber.
data
Containsacomma-separatedlistofoneormoretopicsinJSONformat.
| Components | of  | a topic |     |     |
| ---------- | --- | ------- | --- | --- |
Inasubscriptionsuccessmessage,eachtopicinthedatacontainsthefollowingcomponents:
topicname
Containsthenameofthetopic,identifiedbytheURIoftheswitchresource,includingtheoptional
querystring.
resources
AOS-CXreal-timenotificationssubsystem|110

Containsacomma-separatedlistofoneormoreresourcesinJSONformat.WhentheURIofatopicis
aresourcecollection,atopicincludesmultipleresources.Intheexamplemessage,thevrfsresource
includestwoVRFinstances:defaultandmgmt.
Eachresourceincludesthefollowingcomponents:
operation
Thevalueofoperationisemptyforsuccessmessages.Thiscomponentisusedfornotification
messagesonly.
uri
ContainstheURIoftheresourceinstancewithintheresourcecollection.Ifthetopicnameisa
resourceinstanceinsteadofacollection,urimatchesthepathportionoftheURIintopicname
values
Containsthenamesandcurrentvaluesoftheattributesthatwerespecifiedinthequerystringof
topicname.
| Parts of | a notification | message |
| -------- | -------------- | ------- |
Anotificationmessageisthemessagesenttothesubscriberwhenthereisachangetoaswitch
resourcethatisthetopicofasubscription.ThenotificationmessageisinJSONformat.
Thecontentofanotificationmessagedependsonthetypeofchangethatoccurred.
| Notification | message | examples |
| ------------ | ------- | -------- |
Forthefollowingexamples,assumethatthefollowingsubscribemessagewasused:
{
| "type":   | "subscribe", |     |
| --------- | ------------ | --- |
| "topics": | [            |     |
{
"name": "/rest/v10.04/system/vlans?depth=2&attributes=name"
}
]
}
ThesubscriberreceivesanotificationwhenthenameofanyVLANchanges:
Inthefollowingexample,VLAN7hasbeenaddedtotheswitchconfiguration:
{
| "type": | "notification", |     |
| ------- | --------------- | --- |
| "data": | [               |     |
{
"topicname": "/rest/v10.04/system/vlans?depth=2&attributes=name",
|     | "resources": [ |     |
| --- | -------------- | --- |
{
|     | "operation": | "inserted", |
| --- | ------------ | ----------- |
"uri": "/rest/v10.04/system/vlans/VLAN7",
|     | "values": {     |     |
| --- | --------------- | --- |
|     | "name": "VLAN7" |     |
}
}
]
}
]
}
111
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |
| ------------------------ | ------------------------- | --- |

In the following example, VLAN7 has been deleted from the configuration:

{

"type": "notification",
"data": [

{

"topicname": "/rest/v10.04/system/vlans?depth=2&attributes=name",
"resources": [

"operation": "deleted",
"uri": "/rest/v10.04/system/vlans/VLAN7",
"values": {}

{

}

]

}

]

}

In the following example, the subscriber has subscribed to the following topic:
/rest/v10.xx/system/interfaces/1%2F1%2F2?attributes=name,admin_state

If either the name or the administrative state of interface 1/1/2 changes, a notification message is sent.
If attributes other than name or administrative state changes, no notification message is sent.

In the following example, the administrative state of the interface changed to up.

{

"type": "notification",
"data": [

{

"topicname":

"/rest/v10.04/system/interfaces/1%2F1%2F2?attributes=name,admin_state",

"resources": [

{

"operation": "modified",
"uri": "/rest/v10.04/system/interfaces/1%2F1%2F2",
"values": {

"admin_state": "up"

}

}

]

}

]

}

Components of a notification message

type

Identifies the type of message. Notification messages have the type: notification

data

Contains a comma-separated list of one or more topics in JSON format.

Components of a topic

In a notification message, each topic in the data contains the following components:

AOS-CX real-time notifications subsystem | 112

topicname

Contains the name of the topic, identified by the URI of the switch resource, including the optional
query string.

resources

Contains a comma-separated list of one or more resources in JSON format. When the URI of a topic is
a resource collection, a topic includes multiple resources.

Each resource includes the following components:
operation

For notification messages, operation is one of the following values:
inserted

The resource or resource attribute was added to the configuration of the switch.
deleted

The resource or resource attribute was deleted from the switch.
modified

The resource or resource attribute changed.

uri

Contains the URI of the resource instance within the resource collection. If the topicname is a
resource instance instead of a collection, uri matches the path portion of the URI in topicname.

values

The content of values depends on the operation:

n When the operation value is deleted, values is empty.

n When the operation value is inserted, values contains the current names and values of the
attributes specified in the query portion of the topicname. If no query string was included in
topicname, all attributes and values for that resource are included.

n When the operation value is modified, values contains the name and current value of the

attribute in the query string that changed value:

o If no query string was included in topicname, all attributes and values for that resource are

included.

o If multiple attributes are included in the query string of a topic and only some of those

attribute values changed, only the changed attributes are included.

o If an attribute that was not included in the query string changes, no notification message is

sent because that attribute is not part of the subscription.

Example: Browser-based WebSocket connection

About the example

The following example, websocket-client.html, uses HTML and Javascript to create a webpage that
you can use to establish a WSS connection and send and receive notification messages.

n Access to the switch REST API must be enabled on the VRF through which this browser will connect to

the switch.

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

113

n BeforeyoucanusetheHTMLpage,youmustlogintotheswitchWebUIorRESTAPIfromaseparate
tabinthesamewebbrowsersession.Thebrowsersharesthesessioncookiebetweentabs.
n Whenthebrowserpageisopen,inServer Location,substitutetheswitchIPaddressfor
{IPAddress}inwss://{IPAddress}/rest/v10.xx/notification,thenclickConnect.
n EnterthesubscriptionmessageinRequestandclickSend.
n ResponsesandnotificationsareshowninResponse.
| Example | screen |        |     |     |     |     |     |     |
| ------- | ------ | ------ | --- | --- | --- | --- | --- | --- |
| Example | HTML   | source |     |     |     |     |     |     |
<!DOCTYPE html>
<html lang="en">
<head>
| <title>Web    | Socket                  | Client     | Example</title> |     |     |     |     |     |
| ------------- | ----------------------- | ---------- | --------------- | --- | --- | --- | --- | --- |
| <script       | type="text/javascript"> |            |                 |     |     |     |     |     |
| window.onload |                         | = function |                 | ()  | {   |     |     |     |
var conn;
|     | var log  | = document.getElementById("log"); |     |     |     |     |     |     |
| --- | -------- | --------------------------------- | --- | --- | --- | --- | --- | --- |
|     | var msg  | = document.getElementById("msg"); |     |     |     |     |     |     |
|     | function | appendLog(item)                   |     |     | {   |     |     |     |
var doScroll = log.scrollTop === log.scrollHeight - log.clientHeight;
log.appendChild(item);
|     | if  | (doScroll)    |     | {   |                  |     |                     |     |
| --- | --- | ------------- | --- | --- | ---------------- | --- | ------------------- | --- |
|     |     | log.scrollTop |     | =   | log.scrollHeight |     | - log.clientHeight; |     |
}
}
|     | document.getElementById("connect").onclick |                       |                                     |     |            |       | = function | () { |
| --- | ------------------------------------------ | --------------------- | ----------------------------------- | --- | ---------- | ----- | ---------- | ---- |
|     | var                                        | server                | = document.getElementById("wsURL"); |     |            |       |            |      |
|     | conn                                       | = new                 | WebSocket(server.value);            |     |            |       |            |      |
|     | if                                         | (window["WebSocket"]) |                                     |     | {          |       |            |      |
|     |                                            | if (conn)             |                                     | {   |            |       |            |      |
|     |                                            | conn.onopen           |                                     |     | = function | (evt) | {          |      |
document.getElementById("disconnect").disabled = false
|     |     |     | document.getElementById("sendMsg").disabled |     |     |     |     | = false       |
| --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | ------------- |
|     |     |     | document.getElementById("connect").disabled |     |     |     |     | = true        |
|     |     |     | document.getElementById("status").innerHTML |     |     |     |     | = "Connection |
opened"
}
|     |     | conn.onclose |                                             |     | = function | (evt) | {   |               |
| --- | --- | ------------ | ------------------------------------------- | --- | ---------- | ----- | --- | ------------- |
|     |     |              | document.getElementById("status").innerHTML |     |            |       |     | = "Connection |
closed"
|     |     |     | document.getElementById("connect").disabled |     |     |     |     | = false |
| --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | ------- |
};
|     |     | conn.onmessage |     |          | = function              |                      | (evt) { |        |
| --- | --- | -------------- | --- | -------- | ----------------------- | -------------------- | ------- | ------ |
|     |     |                | var | messages | = evt.data.split('\n'); |                      |         |        |
|     |     |                | for | (var     | i = 0;                  | i < messages.length; |         | i++) { |
AOS-CXreal-timenotificationssubsystem|114

|     | var            | item = document.createElement("pre"); |     |     |
| --- | -------------- | ------------------------------------- | --- | --- |
|     | item.innerText | = messages[i];                        |     |     |
appendLog(item);
}
}
}
| } else { |     |     |     |     |
| -------- | --- | --- | --- | --- |
var item = document.createElement("pre");
item.innerHTML = "<b>Your browser does not support WebSockets.</b>";
appendLog(item);
}
};
| document.getElementById("disconnect").onclick |     |     | = function | () { |
| --------------------------------------------- | --- | --- | ---------- | ---- |
conn.close()
| document.getElementById("sendMsg").disabled    |     |     | =   | true   |
| ---------------------------------------------- | --- | --- | --- | ------ |
| document.getElementById("connect").disabled    |     |     | =   | false  |
| document.getElementById("disconnect").disabled |     |     |     | = true |
document.getElementById("status").innerHTML = "Connection closed"
};
| document.getElementById("form").onsubmit |     |     | = function | () { |
| ---------------------------------------- | --- | --- | ---------- | ---- |
| if (!conn)                               | {   |     |            |      |
return false;
}
| if (!msg.value) | {   |     |     |     |
| --------------- | --- | --- | --- | --- |
return false;
}
conn.send(msg.value);
| var item | = document.createElement("pre"); |     |     |     |
| -------- | -------------------------------- | --- | --- | --- |
item.classList.add("subscribeMsg");
| item.innerHTML | = msg.value; |     |     |     |
| -------------- | ------------ | --- | --- | --- |
appendLog(item);
| return false; |     |     |     |     |
| ------------- | --- | --- | --- | --- |
};
};
</script>
<style type="text/css">
html {
| overflow: hidden; |     |     |     |     |
| ----------------- | --- | --- | --- | --- |
}
body {
| overflow: hidden; |     |     |     |     |
| ----------------- | --- | --- | --- | --- |
| padding: 0;       |     |     |     |     |
| margin: 0;        |     |     |     |     |
width: 100%;
| height: 100%; |       |     |     |     |
| ------------- | ----- | --- | --- | --- |
| background:   | gray; |     |     |     |
}
#log {
| background:    | white;      |        |     |     |
| -------------- | ----------- | ------ | --- | --- |
| margin: 0;     |             |        |     |     |
| padding: 0.5em | 0.5em 0.5em | 0.5em; |     |     |
top: 1.5em;
left: 0.5em;
right: 0.5em;
| bottom: 3em;        |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
| overflow: auto;     |     |     |     |     |
| position: absolute; |     |     |     |     |
| height: 530px;      |     |     |     |     |
}
#form {
115
AOS-CX10.12RESTAPIGuide| (AllAOS-CXSeriesSwitches)

|     | padding: 0 | 0.5em 0 0.5em; |     |     |     |
| --- | ---------- | -------------- | --- | --- | --- |
margin: 0;
|     | position: absolute; |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- |
bottom: 3em;
top: 5em;
left: 8px;
width: 100%;
|     | overflow: hidden; |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- |
}
| #serverLocation |              | {      |     |     |     |
| --------------- | ------------ | ------ | --- | --- | --- |
|                 | padding-top: | 0.3em; |     |     |     |
}
| #requestSection |     | {   |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
height: 38px;
}
| #responseMsgSection |     | {   |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
height: 570px;
|     | position: relative; |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- |
}
</style>
</head>
<body>
<fieldset>
| <legend>Server | Location</legend> |     |     |     |     |
| -------------- | ----------------- | --- | --- | --- | --- |
<div>
| <input | type="button" | value="Connect"/>  |            |     |     |
| ------ | ------------- | ------------------ | ---------- | --- | --- |
| <input | type="button" | value="Disconnect" | disabled/> |     |     |
<input type="text" value="wss://{IPAddress}/rest/v10.04/notification" size="64">
<span></span>
</div>
</fieldset>
<fieldset>
<legend>Request</legend>
<form>
| <input | type="submit" | value="Send" | ; disabled/> |     |     |
| ------ | ------------- | ------------ | ------------ | --- | --- |
| <input | type="text"   | size="80"/>  |              |     |     |
</form>
</fieldset>
<fieldset>
<legend>Response</legend>
<div></div>
</fieldset>
</body>
</html>
| Example: | Getting | information | about | current | subscribers |
| -------- | ------- | ----------- | ----- | ------- | ----------- |
Togetinformationaboutthesubscribersreceivingnotificationsfromaswitch,youmustusetheREST
API.
InstructionsandexamplesinthisdocumentuseanIPaddressthatisreservedfordocumentation,
192.0.2.5,asanexampleoftheIPaddressfortheswitch.Toaccessyourswitch,youmustusetheIP
addressorhostnameofthatswitch.
Prerequisites
YoumustbeloggedintotheswitchRESTAPI.
Procedure
Togetthelistofcurrentsubscribers,sendaGETrequesttothenotification_subscribersresource.
AOS-CXreal-timenotificationssubsystem|116

For example:
GET "https://192.0.2.5/rest/v10.xx/system/notification_subscribers"

The response body is a list of URIs. The identifier at the end of the URI string is the subscriber name.

For example:
[

"rest/v10.xx/system/notification_subscribers/z6901beisjgf",
"rest/v10.xx/system/notification_subscribers/18l9g87erb42"

]

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

117

Chapter 11

Troubleshooting

Troubleshooting

General troubleshooting tips

Connectivity

Connectivity is often the first issue you encounter. Ensure that you have enabled https-server on the VRF
you are trying to use.

n To connect to the REST API through the management (OOBM) port, REST API access must be enabled

on the management VRF.

n To connect to the REST API through a data port, REST API access must be enabled on the default VRF

or a user-created VRF that includes that data port.

Resources, attributes, and behaviors

Resources, attributes, and behaviors might differ between different versions of the switch software.

If you are getting errors when making requests to switches with different software versions, use the
AOS-CX REST API Reference on each switch to compare the URI paths and attributes for the resource.
You might need to alter your code to handle the different software versions.

Resources, attributes, and behaviors might differ between different versions of the REST API, and the
switch supports access through multiple versions of the REST API.

OSPF and BGP routing information updates frequently due to the nature of these resources. Best
practices is to avoid using the REST API to view information about these resources, as this will trigger a
large number of insert event notifications.

The REST API supports Aruba clients such as Central, NetEdit, the AOS-CX WebUI and Network Analytics Engine

(NAE), and Aruba Fabric Composer (AFC). Each of these clients makes use of REST through polling or

subscriptions, where different requests are made to show the updated data to the user. Although it is possible to

use one or more of these clients simultaneously, it is not recommended to have more than one of the clients
connected at the same time, this can will cause high CPU and memory usage.

GET, PUT, PATCH, POST, and DELETE methods

Most resources do not allow POST, PATCH, PUT, or DELETE methods and do not display those methods
in the AOS-CX REST API Reference unless the REST access mode is set to read-write.

The JSON model of a resource can vary by method used. The JSON data you receive from the GET
method is not the same as the JSON data you can or must provide with the POST or PUT methods:

n The GET method model contains all the attributes.

n The POST method model contains only the configuration attributes.

n The PATCH method updates values in an existing resource using only the desired values in the

request body.

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

118

n The PUT method model contains only the mutable (changeable) configuration attributes. If you do
not provide all the mutable attributes in the request body of the PUT request, those attributes you
do not provide are set to their defaults, which could be empty. If you attempt to provide an
immutable attribute in a PUT request, an error is returned.

Use the GET method with the selector=configuration parameter to get only the configuration
attributes of a resource. Using the REST v10.04 API and later, you can also use the GET method with the
selector=writable parameter to get only the mutable configuration attributes of a resource.

You can use the AOS-CX REST API Reference to view information about the supported methods and
resource models. You can obtain additional platform-specific information through GET requests for
product information attributes or subsystem collections.

Aruba 8400 switch examples:

Example request:
GET "https://192.0.2.5/rest/v10.xx/system/subsystems"

Example response body:

{

"chassis,1": "/rest/v10.04/system/subsystems/chassis,1",
"line_card,1/3": "/rest/v10.04/system/subsystems/line_card,1%2F3",
"management_module,1/5": "/rest/v10.04/system/subsystems/management_

module,1%2F5"
}

Example request:
GET "https://192.0.2.5/rest/v10.xx/system/subsystems/chassis,1?attributes=product_info"

Example response body:

{

"product_info": {

"base_mac_address": "00:00:5E:00:53:00",
"device_version": "",
"instance": "1",
"number_of_macs": "512",
"part_number": "JL375A",
"product_description": "8400 8-slot Chassis/3xFan Trays/18xFans/Cable

Manager/X462 Bundle",

"product_name": "8400 Base Chassis/3xFT/18xFans/Cbl Mgr/X462 Bundle",
"serial_number": "SG00A2A00A",
"vendor": "Aruba"

}

}

Aruba 8320 switch examples:

Example request:
GET "https://192.0.2.5/rest/v10.xx/system/subsystems

Example response body:

{

"chassis,1": "/rest/v10.04/system/subsystems/chassis,1",
"line_card,1/1": "/rest/v10.04/system/subsystems/line_card,1%2F1 ",
"management_module,1/1": "/rest/v10.04/system/subsystems/management_

Troubleshooting | 119

module,1%2F1"
}
Examplerequest:
GET "https://192.0.2.5/rest/v10.xx/system/subsystems/chassis,1?attributes=product_info"
Exampleresponsebody:
{
| "product_info":     | {   |                      |
| ------------------- | --- | -------------------- |
| "base_mac_address": |     | "00:00:5E:00:53:01", |
| "device_version":   |     | "",                  |
"instance": "1",
| "number_of_macs":      |           | "74",         |
| ---------------------- | --------- | ------------- |
| "part_number":         | "JL479A", |               |
| "product_description": |           | "8320",       |
| "product_name":        |           | "8320",       |
| "serial_number":       |           | "TW00000000", |
"vendor": "Aruba"
}
}
| Hardware | and other | features |
| -------- | --------- | -------- |
Differentswitcheshavedifferenthardwareandfeatures.Forexample,themanagementmodule
resourceIDis1/1forsomeswitches,and1/4or1/5forotherswitches.Togetinformationaboutthe
switchmodel,usetheGETmethodrequestwiththeURIfortheplatform_namesystemattribute.
Forexample:
GET "https://192.0.2.5/rest/v10.xx/system?attributes=platform_name"
ThefollowingisanexampleofaresponsebodyforanAruba8320switch:
{
| "platform_name": | "8320" |     |
| ---------------- | ------ | --- |
}
ThefollowingisanexampleofaresponsebodyforanAruba8400switch:
{
| "platform_name": | "8400X" |     |
| ---------------- | ------- | --- |
}
Thewords"port"and"interface"havemeaningsthataredifferentfromothernetworkoperating
systems.IntheAOS-CXoperatingsystem:
n Aportisthelogicalrepresentationofaport.
n Aninterfaceisthehardwarerepresentationofaport.
Youcanenabledebugginglogsbyusingthedebugcommand.Themodulenameisrest.Youcanspecify
allseverityloglevelsoraminimumseverityloglevel.
Examplespecifyingallseverityloglevels:
| switch# | debug rest all |     |
| ------- | -------------- | --- |
120
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |
| ------------------------ | ------------------------- | --- |

Examplespecifyingaminimumseveritylogleveloferror:
| switch# | debug rest   | all severity | error |     |
| ------- | ------------ | ------------ | ----- | --- |
| REST    | API response | codes        |       |     |
Thefollowingtabledescribesthedifferentcategoriesoftheresponsecodes.
| Category |     | Description                                            |     |     |
| -------- | --- | ------------------------------------------------------ | --- | --- |
| 2xx      |     | Indicatesthattherequestwasacceptedsuccessfully.        |     |     |
| 4xx      |     | Returnstheclient-sideerrorresponsewiththeerrormessage. |     |     |
| 5xx      |     | Returnstheserver-sideerrorresponsewiththeerrormessage. |     |     |
ThefollowingaresomeresponsecodesthatyouwillseeintheRESTAPI.
| Response | code | Status |     | Description                             |
| -------- | ---- | ------ | --- | --------------------------------------- |
| 200      |      | OK     |     | ReturnedfromGETandPUToperations,andnon- |
configurationAPIcallssuchasLoginorLogoutwhen
therequestissuccessfullycompleted.
| 201 |     | Created |     | ReturnedfromPOSToperationswhenanewresource |
| --- | --- | ------- | --- | ------------------------------------------ |
wassuccessfullycreated.
| 204 |     | NoContent |     | ReturnedfromaPUT,POSTPATCH,,orDELETE |
| --- | --- | --------- | --- | ------------------------------------ |
operationwhentherequestwassuccessfully
processedandthereisnocontenttoreturn.
| 400 |     | Badrequest |     | Aproblemwiththerequestbody,suchasinvalid |
| --- | --- | ---------- | --- | ---------------------------------------- |
syntax,incorrectlyformattedJSON,ordataviolatinga
databaseconstraint.
401 Unauthorized Noactivesessionforthisclient(theloginAPIhasnot
beencalled)ortoomanysessionsalreadycreated
fromthisclient.
| 403 |     | Forbidden |     | Theclientsessionisvalid,butdoesnothave |
| --- | --- | --------- | --- | -------------------------------------- |
permissionstoaccesstherequestedresource.
| 404 |     | Notfound |     | Theresourcedoesnotexist,ortheURIisincorrectfor |
| --- | --- | -------- | --- | ---------------------------------------------- |
thedesiredresource.Canalsooccurwhenaccessing
thePOST,PUT,PATCH,orDELETEAPIwhiletheREST
access-modeissettoread-only.
500 Internalservererror Anunexpectederrorhasoccurredinprocessingthe
request.Viewthelogsonthedevicefordetails.
Troubleshooting|121

| Response | code | Status |     | Description |     |
| -------- | ---- | ------ | --- | ----------- | --- |
503 Serviceunavailable Thedeviceisreceivingmorerequeststhanitcan
processandisdefensivelyrejectingrequeststo
protectresources.
| Error | "'admin' | password | is not | set" |     |
| ----- | -------- | -------- | ------ | ---- | --- |
Symptom
AnattempttoenabletheHTTPSserverusingthehttps-server vrfcommandfailsandthefollowing
errorisreturned:
Failed to enable https-server on VRF <VRF>. 'admin' password is not set
Cause
Theswitchisshippedfromthefactorywithadefaultusernamedadminwithoutapassword.Theadmin
usermustsetavalidpasswordbeforeHTTPSserverscanbeenabled.
Action
Fromtheglobalconfigurationcontext,setavalidpasswordfortheadminuser.
Forexample:
| switch(config)# | user         | admin password |     |     |     |
| --------------- | ------------ | -------------- | --- | --- | --- |
| Changing        | password for | user admin     |     |     |     |
Enter password:************
| Confirm | password:************ |        |         |          |           |
| ------- | --------------------- | ------ | ------- | -------- | --------- |
| Error   | "certificate          | verify | failed" | returned | from curl |
command
Symptom
AcurlcommandtotheswitchURLfailswithanerrorsimilartothefollowing:
| SSL3_GET_SERVER_CERTIFICATE:certificate |     |     | verify | failed |     |
| --------------------------------------- | --- | --- | ------ | ------ | --- |
Cause
ThecurlprogramcouldnotverifytheswitchservercertificateagainsttheCAcertificatebundlethat
comeswiththecurlinstallation,andyoudidnotincludethe-koptioninthecurlcommand.
Action
Retrythecommandwiththe-koptionincluded.
TheswitchHTTPSserverusesself-signedcertificates,whichcannotbeverifiedagainstacertificate
authority.The-koptiondisablescurlcertificatevalidation.
Forexample:
| $ curl | -k --noproxy | "192.0.2.5" | GET /tmp/auth_cookie |     | \   |
| ------ | ------------ | ----------- | -------------------- | --- | --- |
"https://192.0.2.5/rest/v10.09/system/vlans"
| HTTP | 400 error | "Invalid | Operation" |     |     |
| ---- | --------- | -------- | ---------- | --- | --- |
122
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |     |
| ------------------------ | ------------------------- | --- | --- | --- | --- |

Symptom

A REST request returns response code 400 and the response body contains the following text string:
Invalid operation

Cause

The method used for this REST request is not supported for the specified resource. For example, the
Invalid operation response is returned if you attempt a DELETE request on the system resource.

Action

Use a method supported by the resource.

The AOS-CX REST API Reference displays the methods supported by each resource.

HTTP 400 error "Value is not configurable" or "Bad Request"

Symptom

A PUT, PATCH, or POST request returns response code 400 and the response body contains the
following text string:
Value <value> is not configurable

Cause

The JSON data in the POST, PATCH, or PUT request body contains non-configuration or immutable
attributes.

Action

Retry the request with the correct JSON resource model for that PUT, PATCH, or POST method.

To determine the configuration attributes of a resource, you can send a GET request with the
selector=configuration query parameter to the resource. Using the REST v10.04 API or later, you can
also use the GET method with the selector=writable parameter to get only the mutable configuration
attributes of the resource.

You can also use the AOS-CX REST API Reference to verify the JSON model of the PUT, PATCH, or POST
method of the resource.

The category an attribute belongs to can depend on whether that instance of the resource is owned by
the system or owned by a user. Configuration attributes can become status attributes in resource
instances that are owned by the system. Status attributes can not be modified by users.

In addition, some configuration attributes cannot be changed after a resource is created. These
immutable attributes cannot be included in a PUT request.

HTTP 401 error "Authorization Required"

Symptom

A REST request returns response code 401 and the response body contains the following text string:
Authorization Required

This response means that no valid session was found for the session token passed to the API.

Solution 1

Cause

Troubleshooting | 123

The user attempting the request is not logged into the REST API for one of the following reasons:

n The user has not yet logged in.

n The user logged in but the session has expired.

Action

Log in to the REST API.

Solution 2

Cause

The user attempting the request is not logged in to the REST API because the user did not pass the
correct session cookie to the API. Typically, incorrect session cookies are not a cause when accessing the
REST API through a browser because the browser automatically handles the session cookie.

Action

1. Ensure that you save the session cookie returned from the login request.

2. Ensure that you pass the same cookie back to the switch with every REST API request, including

the request to log out.

HTTP 401 error "Login failed: session limit reached"

Symptom

A REST request or Web UI login attempt returns response code 401 and the response body contains the
following text string:
Login failed: session limit reached

Cause

A user attempted to log into the REST API or the Web UI, but that user already has the maximum
number of concurrent sessions running.

Action

1. Log out from one of the existing sessions.

Browsers share a single session cookie across multiple tabs or even windows. However, scripts
that POST to the login resource and later do not POST to the logout resource can easily create the
maximum number of concurrent sessions.

2.

If the session cookie is lost and it is not possible to log out of the session, then wait for the
session idle time limit to expire.

When the session idle timeout expires, the session is terminated automatically.

3.

If it is required to stop all HTTPS sessions on the switch instead of waiting for the session idle time
limit to expire, you can stop all HTTPS sessions using the https-server session close all
command.

This command stops and starts the hpe-restd service, so using this command affects all existing
REST sessions and Web UI sessions.

HTTP 403 error "Forbidden" on a write request

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

124

Symptom

A POST, PUT, PATCH, or DELETE REST request returns response code 403 and the response body
contains the following text string:
Forbidden

Cause

The user attempting the request is not a member of the administrators group.

Action

Log in to the REST API with a user name that has administrator rights as part of the administrators
group.

The user must be a member of the predefined administrators group. POST requests to the login
resource fail for members of a user-defined local user group.

HTTP 403 error "Forbidden" on a GET request

Symptom

A GET REST request returns response code 403 and the response body contains the following text
string:
Forbidden

Cause

The user attempting the request is a member of the Auditors group, and the GET request specified a
switch resource that users with auditor rights are not permitted to access.

Action

Log in to the REST API with a user name that has operator or administrator rights.

HTTP 404 error "Page not found" when accessing the switch
URL

Symptom

The switch is operational and you are using the correct URL for the switch, but attempts to access the
REST API or Web UI result in an HTTP 404 "Page not found" error.

Cause

REST API access is not enabled on the VRF that corresponds to the access port you are using. For
example, you are attempting to access the REST API or Web UI from the management (OOBM) port, and
access is not enabled on the mgmt VRF.

Action

Use the https-server vrf command to enable REST API access on the specified VRF.

For example:

switch(config)# https-server vrf mgmt

Troubleshooting | 125

| HTTP 404         | error | "Object | not found" | on object | with | "ports/" |
| ---------------- | ----- | ------- | ---------- | --------- | ---- | -------- |
| or "interfaces/" |       | in URI  | Path       |           |      |          |
Symptom
ArequestwasmadewithanURIthatcontainsrest/v10.xx/andports/orinterfaces/intheURI
path,andtherequestreturnsresponsecode404andtheresponsebodycontainsthefollowingtext
string:
| Object not | found |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- |
Cause
Theresourcedoesnotexistinthesystem.TheURIintherequestisincorrect.
TheportscollectiondoesnotexistintheRESTv10.04orlaterAPIschema.
Action
ChangetherequesttoarequestthatisvalidfortheRESTv10.04orlaterAPI.
| HTTP 404      | error | "Object  | not found" | returned | from   | a switch   |
| ------------- | ----- | -------- | ---------- | -------- | ------ | ---------- |
| that supports |       | multiple | REST API   | versions | (10.04 | and later) |
Symptom
AswitchthatsupportsmultipleRESTAPIversionsreturnsresponsecode404andtheresponsebody
containsthefollowingtextstring:
| Object not | found |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- |
Cause
Theresourcedoesnotexistinthesystem.TheURIintherequestisincorrectfortheversionoftheREST
APIspecifiedintherequest.
Action
VerifytheURIoftheresourceandretrytherequest.
| HTTP 404 | error | "Object | not found" | when | using | a write |
| -------- | ----- | ------- | ---------- | ---- | ----- | ------- |
method
Symptom
APUTorDELETErequestreturnsresponsecode404andtheresponsebodycontainsthefollowingtext
string:
| Object not | found |     |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- | --- |
Cause
Theresourcedoesnotexistinthesystem.TheURIintherequestisincorrectortheresourcehasnot
beenaddedtotheconfiguration.
Action
VerifytheURIoftheresourceyouareattemptingtochangeordeleteandretrytherequest.
126
| AOS-CX10.12RESTAPIGuide| | (AllAOS-CXSeriesSwitches) |     |     |     |     |     |
| ------------------------ | ------------------------- | --- | --- | --- | --- | --- |

HTTP 404 error "Page not found" when using a write
method

Symptom

Using the GET method is successful, but attempting a POST, PUT, or DELETE method results in an HTTP
404 "Page not found" error.

Cause

The REST API access mode is set to read-only.

Action

Set the REST API access mode to read-write.

switch(config)# https-server rest access-mode read-write

Enabling the read-write mode on the REST API allows POST, PUT, and DELETE operations to be called on
all configurable elements in the switch database.

Logout Fails

Symptom

An attempt to log out of the REST API from a script or curl command fails.

Cause

The session cookie was not supplied or does not contain the correct session token.

Action

1. Repeat the command and send the correct session cookie or modify the script to send the correct

session cookie.

2.

If the session cookie has been lost and it is not possible to log out of the session, wait for the
session idle time limit to expire.

When the session idle timeout expires, the session is terminated automatically.

Troubleshooting | 127

Support and Other Resources

Chapter 12

Support and Other Resources

Accessing Aruba Support

Aruba Support Services

https://www.arubanetworks.com/support-services/

AOS-CX Switch Software Documentation
Portal

https://www.arubanetworks.com/techdocs/AOS-CX/help_
portal/Content/home.htm

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

Airheads social
forums and
Knowledge Base

AOS-CX Switch
Software
Documentation
Portal

Aruba Hardware
Documentation
and Translations

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/AOS-CX/help_portal/Content/home.htm

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

128

Portal
| Arubasoftware | https://asp.arubanetworks.com/downloads |     |
| ------------- | --------------------------------------- | --- |
| Software      | https://lms.arubanetworks.com/          |     |
licensing
End-of-Life https://www.arubanetworks.com/support-services/end-of-life/
information
| ArubaDeveloper | https://developer.arubanetworks.com/ |     |
| -------------- | ------------------------------------ | --- |
Hub
| Accessing | Updates |     |
| --------- | ------- | --- |
YoucanaccessupdatesfromtheArubaSupportPortalortheHPEMyNetworkingWebsite.
| Aruba | Support | Portal |
| ----- | ------- | ------ |
https://asp.arubanetworks.com/downloads
IfyouareunabletofindyourproductintheArubaSupportPortal,youmayneedtosearchMy
Networking,whereoldernetworkingproductscanbefound:
My Networking
https://www.hpe.com/networking/support
Toviewandupdateyourentitlements,andtolinkyourcontractsandwarrantieswithyourprofile,goto
theHewlettPackardEnterpriseSupportCenterMore Information on Access to Support Materials
page:
https://support.hpe.com/portal/site/hpsc/aae/home/
AccesstosomeupdatesmightrequireproductentitlementwhenaccessedthroughtheHewlettPackard
EnterpriseSupportCenter.YoumusthaveanHPPassportsetupwithrelevantentitlements.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://asp.arubanetworks.com/notifications/subscriptions(requiresanactiveArubaSupportPortal
(ASP)accounttomanagesubscriptions).SecuritynoticesareviewablewithoutanASPaccount.
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
SupportandOtherResources|129

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

AOS-CX 10.12 REST API Guide | (All AOS-CX Series Switches)

130