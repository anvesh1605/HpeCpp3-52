| AOS-CX    |       |       | 10.12 |        | Network |        |       |
| --------- | ----- | ----- | ----- | ------ | ------- | ------ | ----- |
| Analytics |       |       |       | Engine |         | Guide  |       |
| 6200,     | 6300, | 6400, |       | 8320,  | 8325,   | 8360,  | 8400, |
|           | 9300, | 10000 |       | Switch |         | Series |       |
Published:May2023
Edition:1

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
| Contents                                         |                            |        |              | 3   |
| ------------------------------------------------ | -------------------------- | ------ | ------------ | --- |
| About this                                       | document                   |        |              | 8   |
| Applicableproducts                               |                            |        |              | 8   |
| Latestversionavailableonline                     |                            |        |              | 8   |
| Commandsyntaxnotationconventions                 |                            |        |              | 8   |
| Abouttheexamples                                 |                            |        |              | 9   |
| Identifyingswitchportsandinterfaces              |                            |        |              | 10  |
| Identifyingmodularswitchcomponents               |                            |        |              | 11  |
| Aruba Network                                    | Analytics                  | Engine | Introduction | 12  |
| AOS-CXWebUIforAnalyticsintroduction              |                            |        |              | 12  |
| ArubaNetworkAnalyticEnginescriptsintroduction    |                            |        |              | 12  |
| ArubaNetworkAnalyticagentsintroduction           |                            |        |              | 13  |
| Built-inscriptsandagents                         |                            |        |              | 13  |
| Aruba-certifiedscripts                           |                            |        |              | 14  |
| ArubaSolutionsExchange(ASE)introduction          |                            |        |              | 14  |
| User-createdscripts                              |                            |        |              | 14  |
| DevelopercommunitiesfortheNetworkAnalyticsEngine |                            |        |              | 15  |
|                                                  | ArubaSolutionExchange(ASE) |        |              | 15  |
|                                                  | GitHub                     |        |              | 15  |
|                                                  | AirheadsCommunity          |        |              | 15  |
| ArubaNetworkAnalyticsEnginesupportedmaximums     |                            |        |              | 15  |
AOS-CX Network Analytics Engine (NAE) Design considerations 17
| NAEfactorsthatimpactsystemresources            |           |        |           | 17  |
| ---------------------------------------------- | --------- | ------ | --------- | --- |
| NAEdeploymentconsiderations                    |           |        |           | 17  |
| ConsiderationswhenwritinganNAEagent            |           |        |           | 18  |
| Aruba Network                                  | Analytics | Engine | framework | 19  |
| Configurationandstatedatabase                  |           |        |           | 19  |
| Timeseriesdatabase                             |           |        |           | 19  |
| AOS-CXRESTAPI                                  |           |        |           | 20  |
| PythonandtheRESTAPIforscripts                  |           |        |           | 20  |
| "Sandboxes"foragentactions                     |           |        |           | 21  |
| Managing                                       | scripts   |        |           | 22  |
| ManagingNAEscriptsacrossswitchsoftwareupdates  |           |        |           | 22  |
| ViewingscriptdetailsusingtheWebUI              |           |        |           | 23  |
| DownloadingascriptusingtheWebUI                |           |        |           | 24  |
| UploadingascriptusingtheWebUI                  |           |        |           | 25  |
| UpdatingascriptusingtheWebUI                   |           |        |           | 26  |
| DeletingascriptusingtheWebUI                   |           |        |           | 26  |
| GettinginformationaboutscriptsusingtheRESTAPI  |           |        |           | 27  |
| UploadingascriptusingtheRESTAPI                |           |        |           | 28  |
| UpdatingascriptusingtheRESTAPI                 |           |        |           | 29  |
| DeletingascriptusingtheRESTAPI                 |           |        |           | 29  |
| DownloadingascriptfromtheswitchusingtheRESTAPI |           |        |           | 30  |
3
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

| showrunning-configcommandoutputforagentsandscripts  |                                        |     |     | 30  |
| --------------------------------------------------- | -------------------------------------- | --- | --- | --- |
| Scriptstatus                                        |                                        |     |     | 31  |
| Managing                                            | agents                                 |     |     | 32  |
| ViewingalistofagentsinstalledonaswitchusingtheWebUI |                                        |     |     | 32  |
| ViewingagentinformationusingtheWebUI                |                                        |     |     | 32  |
| FindingalertdetailsusingtheWebUI                    |                                        |     |     | 36  |
| WorkingwithanAnalyticstimeseriesgraph               |                                        |     |     | 38  |
|                                                     | Customizingdatadisplayedonthegraph     |     |     | 39  |
|                                                     | Zoominginonthegraph                    |     |     | 40  |
|                                                     | Downloadingthegraphasanimageor.csvfile |     |     | 41  |
|                                                     | Viewinganalertonthegraph               |     |     | 41  |
| EnablingadisabledagentusingtheWebUI                 |                                        |     |     | 44  |
| DisablinganagentusingtheWebUI                       |                                        |     |     | 44  |
| DeletinganagentusingtheWebUI                        |                                        |     |     | 45  |
| CreatinganagentfromanexistingscriptusingtheWebUI    |                                        |     |     | 45  |
| ChangingtheconfigurationofanagentusingtheWebUI      |                                        |     |     | 46  |
| GettinginformationaboutagentsusingtheRESTAPI        |                                        |     |     | 47  |
| CreatinganagentfromanexistingscriptusingtheRESTAPI  |                                        |     |     | 48  |
| EnablinganagentusingtheRESTAPI                      |                                        |     |     | 49  |
| DisablinganagentusingtheRESTAPI                     |                                        |     |     | 49  |
| ChangingtheconfigurationofanagentusingtheRESTAPI    |                                        |     |     | 50  |
| DeletinganagentusingtheRESTAPI                      |                                        |     |     | 51  |
ShowingtheCurrentandMaximumNumberofAgents,Monitors,andScripts 51
| Agentstatus                                       |           |        |        | 53  |
| ------------------------------------------------- | --------- | ------ | ------ | --- |
| Behaviorswhenmultipleagentsmonitorthesameresource |           |        |        | 53  |
| Troubleshooting                                   | agent and | script | issues | 55  |
Showingthecurrentandmaximumnumberofagents,monitors,andscripts 55
| HighswitchCPUandmemoryusageareaffectingswitchperformance |                       |     |     | 57  |
| -------------------------------------------------------- | --------------------- | --- | --- | --- |
| DownloadingNAEsupportfiles                               |                       |     |     | 57  |
|                                                          | NAEsupportfilecontent |     |     | 58  |
| Error:"Switchtimeandbrowsertimearenotinsync"             |                       |     |     | 58  |
Analyticstimeseriesgraphdisplaysmessageinsteadofdata:"Agentdatanotfound,please
| verify..."                                            |     |     |     | 59  |
| ----------------------------------------------------- | --- | --- | --- | --- |
| Inaccurateornodatadisplayedinanalyticstimeseriesgraph |     |     |     | 60  |
| URIerrors                                             |     |     |     | 61  |
Error:"TheNAEAgentisnotcreated...DBconstraintviolationerrors" 61
| Error:"TheNAEAgenthasPythonerrors." |     |     |     | 62  |
| ----------------------------------- | --- | --- | --- | --- |
Error:"Timeseriesdatacannotbegenerated...TheURIisinvalidornotconfigured" 62
| Error:"Thescriptsyntaxisinvalid"                          |                 |          |       | 64  |
| --------------------------------------------------------- | --------------- | -------- | ----- | --- |
| Error:"Thescriptagentsyntaxisinvalid"                     |                 |          |       | 64  |
| Error:"Sandboxtimedoutwhilerunningscript"                 |                 |          |       | 64  |
| Error:"Theagentinstantiatedsandboxhastimedout"            |                 |          |       | 65  |
| Error:"Unabletoparseconditionexpression..."               |                 |          |       | 66  |
| Error:"TheCLIcommandisinvalid"                            |                 |          |       | 67  |
| Error:"Commandfailed:non-zeroexitstatus"                  |                 |          |       | 67  |
| Error:"Theactionisinvalid"                                |                 |          |       | 68  |
| ActionShelloutputerror:"notavailableinenhancedsecuremode" |                 |          |       | 68  |
| Using the                                                 | Aruba Solutions | Exchange | (ASE) | 70  |
| FindingNAEscriptsontheASEwebsite                          |                 |          |       | 70  |
| FindingNAEscriptsontheASEusingtheWebUI                    |                 |          |       | 70  |
| ViewingrecentchangestoexistingNAEsolutions                |                 |          |       | 71  |
| DownloadingorinstallingascriptfromtheASEusingtheWebUI     |                 |          |       | 71  |
| DownloadingasolutionfromtheASEwebsitetoyourworkstation    |                 |          |       | 72  |
Contents|4

| NAE                            | scripts repository                             | on GitHub | 74  |
| ------------------------------ | ---------------------------------------------- | --------- | --- |
| Scripts                        | and security                                   |           | 75  |
| Scripts                        |                                                |           | 76  |
| Pythonversionandlibrarysupport |                                                |           | 76  |
|                                | Pythonmodulesavailable                         |           | 76  |
|                                | Third-partyPythonlibrariesavailable            |           | 78  |
| RESTAPIversionsupport          |                                                |           | 78  |
| Rulesforscriptfiles            |                                                |           | 78  |
| Scriptexample                  |                                                |           | 78  |
| Partsofascript                 |                                                |           | 80  |
| Header                         |                                                |           | 81  |
| Importstatements               |                                                |           | 82  |
| Manifest                       |                                                |           | 82  |
|                                | Requireditems                                  |           | 82  |
|                                | Optionalitems                                  |           | 82  |
| Parameterdefinitions           |                                                |           | 84  |
|                                | ParameterDefinitionsdescription                |           | 85  |
| Agentclassconstructor          |                                                |           | 86  |
|                                | Graph                                          |           | 87  |
|                                | Title                                          |           | 88  |
|                                | on_agent_re_enable                             |           | 88  |
|                                | on_agent_restart                               |           | 89  |
|                                | on_parameter_change                            |           | 90  |
|                                | Baselinesfordynamicthresholdsformonitors       |           | 90  |
|                                | Baselineworkflowandconsiderations              |           | 91  |
|                                | Exampleofbaselinesinatimeseriesgraph           |           | 92  |
|                                | Exampleofascriptthatusesbaselines              |           | 93  |
|                                | Baseline                                       |           | 94  |
|                                | ADCs                                           |           | 98  |
|                                | ADCListclass                                   |           | 99  |
|                                | ADCEntryclass                                  |           | 100 |
| Monitors                       |                                                |           | 102 |
|                                | URIsformonitors                                |           | 103 |
|                                | PathcomponentoftheURI                          |           | 103 |
|                                | QuerycomponentoftheURI                         |           | 104 |
|                                | WildcardcharactersinmonitoredURIs              |           | 105 |
|                                | ParametersinmonitoredURIs                      |           | 105 |
|                                | Slash(/)charactersinmonitoredURIs              |           | 106 |
|                                | AttributefiltersinmonitoredURIs                |           | 107 |
|                                | ConstructingaURIusingtheAOS-CXRESTAPIReference |           | 107 |
|                                | Aggregateoperators                             |           | 109 |
|                                | Aggregatefunctions                             |           | 110 |
|                                | Nestedaggregatefunctionsandoperators           |           | 112 |
|                                | Aggregatefunctionsinmonitorsandconditions      |           | 112 |
| Rules                          |                                                |           | 113 |
| Conditions                     |                                                |           | 113 |
|                                | Clearconditions                                |           | 114 |
|                                | Conditionexpressionsyntax                      |           | 115 |
Durations,evaluationdelays,andpausesinconditionexpressions 115
Conjunction(AND),disjunction(OR),andmultiplesubconditions 116
|         | FunctionbehaviorwhenmonitoredURIdoesnotcontainwildcards |     | 117 |
| ------- | ------------------------------------------------------- | --- | --- |
|         | FunctionbehaviorwhenmonitoredURIhaswildcards            |     | 118 |
| Actions |                                                         |     | 119 |
|         | Predefinedactions                                       |     | 119 |
5
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

|                                       | ActionCLI,CLIaction       |           |               | 120 |
| ------------------------------------- | ------------------------- | --------- | ------------- | --- |
|                                       | ActionCustomReport        |           |               | 121 |
|                                       | ActionShell,SHELLaction   |           |               | 122 |
|                                       | ActionSyslog,Syslogaction |           |               | 123 |
|                                       | Callbackactions           |           |               | 125 |
|                                       | Clearactions              |           |               | 125 |
|                                       | Alertlevelfunctions       |           |               | 127 |
|                                       | Loggingfunctions          |           |               | 127 |
| Agents                                |                           |           |               | 129 |
| Agentsanduserauthority                |                           |           |               | 129 |
| Rulesforagentnames                    |                           |           |               | 129 |
| Updatingagentsparametervalue          |                           |           |               | 129 |
| NetworkAnalyticsEngineSafeguards      |                           |           |               | 129 |
| Network                               | Analytics                 | Engine    | Lite          | 131 |
| UseCases                              |                           |           |               | 133 |
| Network                               | Analytics                 | Engine    | commands      | 136 |
| naecli-authorization                  |                           |           |               | 136 |
| shownae-agent                         |                           |           |               | 137 |
| shownae-agentalerts                   |                           |           |               | 139 |
| shownae-agentalertsdetails            |                           |           |               | 140 |
| shownae-script                        |                           |           |               | 142 |
| showrunning-config(nae-lite)          |                           |           |               | 143 |
| Network                               | Analytics                 | Engine    | Lite commands | 145 |
| actions                               |                           |           |               | 145 |
| desc                                  |                           |           |               | 147 |
| disable                               |                           |           |               | 148 |
| monitorresource                       |                           |           |               | 149 |
| nae-agentlite                         |                           |           |               | 152 |
| nae-agentliteactivate                 |                           |           |               | 153 |
| set-conditionmonitor                  |                           |           |               | 154 |
| set-conditionwatch                    |                           |           |               | 156 |
| showrunning-confignae-agent           |                           |           |               | 158 |
| tags                                  |                           |           |               | 159 |
| watchevent-log                        |                           |           |               | 160 |
| HTTPS                                 | server commands           |           |               | 162 |
| https-serverauthenticationcertificate |                           |           |               | 162 |
| https-serverauthenticationpassword    |                           |           |               | 163 |
| https-servermax-user-sessions         |                           |           |               | 164 |
| https-serverrestaccess-mode           |                           |           |               | 164 |
| https-serversessioncloseall           |                           |           |               | 165 |
| https-serversession-timeout           |                           |           |               | 166 |
| https-servervrf                       |                           |           |               | 167 |
| showhttps-server                      |                           |           |               | 168 |
| showhttps-serverauthentication        |                           |           |               | 169 |
| Support                               | and Other                 | Resources |               | 171 |
| AccessingArubaSupport                 |                           |           |               | 171 |
| AccessingUpdates                      |                           |           |               | 172 |
|                                       | ArubaSupportPortal        |           |               | 172 |
|                                       | MyNetworking              |           |               | 172 |
Contents|6

Warranty Information
Regulatory Information
Documentation Feedback

172
172
173

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

7

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

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

example-text

In code and screen examples, indicates text entered by a user.

Any of the following:

Identifies a placeholder—such as a parameter or a variable—that you must

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

8

Convention

Usage

n <example-text>
n <example-text>
n example-text

n example-text

|

{ }

[ ]

… or

...

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

Variable information in CLI prompts

About this document | 9

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

On the 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

On the 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.
The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

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

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

10

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

Chapter 2

Aruba Network Analytics Engine
Introduction

Aruba Network Analytics Engine Introduction

The Aruba Network Analytics Engine is a first-of-its-kind built-in framework for network assurance and
remediation. Combining the full automation and deep visibility capabilities of the AOS-CX operating
system, this unique framework enables monitoring, collecting network data, evaluating conditions, and
taking corrective actions through simple scripting agents.

This engine is integrated with the AOS-CX system configuration and time series databases, enabling you
to examine historical trends and predict future problems due to scale, security, and performance
bottlenecks. With that information, you can create software modules that automatically detect such
issues and take appropriate actions.

With the faster network insights and automation provided by the Aruba Network Analytics Engine, you
can reduce the time spent on manual tasks and address current and future demands driven by Mobility
and IoT.

AOS-CX Web UI for Analytics introduction
The AOS-CX Web UI provides access to information related to Aruba Network Analytics Engine agents,
scripts, and alerts on the switch, including time-series data graphs and other information generated by
the enabled agents.

From the AOS-CX Web UI, select Analytics in the navigation pane to view information in the Analytics
Dashboard. You can display time-series graph panels for up to nine agents on the dashboard. However,
many more agents can be enabled on a switch.

From the Analytics Dashboard, you can open Analytics detail pages. Analytics detail pages allow you to
enable, disable, create, delete, or edit agents, upload scripts, and view detailed data about monitored
resources. Administrator rights are required for actions that modify an agent.

For more information about the Web UI, see the Introduction to the Web UI Guide.

Figure 1 Analytics Dashboard in the Web UI

Aruba Network Analytic Engine scripts introduction

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

12

An Aruba Network Analytics Engine script is a Python script that defines which switch resources to
monitor and, optionally, rules that define what actions to take when certain conditions are true.

Examples of tasks a script can define include the following:

n Monitoring average CPU usage and sending a system log message when the CPU usage is greater

than 70% for 5 minutes.

n Monitoring the connection state of a particular BGP neighbor and executing a CLI command when

the connection state transitions from UP to DOWN.

A script is used to create an agent, which is a specifically-configured executable instance of a script on a
switch. A single script can be the template for many different agents.

Aruba Network Analytic agents introduction
An Aruba Network Analytics Engine agent is a specifically-configured executable instance of an NAE
script on a switch. When the agent is enabled, it performs the tasks defined by the script. Agents have
administrator rights.

For scripts that provide configuration parameters, different agents can be configured to use specific
parameter values when performing the tasks defined by the script.

For example, a script that monitors the connection state of a particular BGP neighbor can define a
parameter to specify which BGP neighbor to monitor. From that script, you can do the following:

n You can create an agent to monitor a specific BGP neighbor by specifying that BGP neighbor as the

value of the parameter.

n You can create multiple agents—one for each BGP neighbor you want to monitor.

n When a new BGP neighbor is added, you can create an agent to monitor that neighbor without

having to change the script itself.

Some parameters that are integers—such as a CPU utilization threshold—can be changed for a given
agent after that agent has been created. Network administrators can change such parameters easily
through the Web UI—no programming skill is required.

Built-in scripts and agents
Built-in scripts and agents are installed on the switch before the switch is shipped from the factory. All
scripts and agents have information about their origin associated with them. Built-in scripts and agents
have an origin of "system" and are marked System Created in the Web UI.

Built-in scripts and agents cannot be deleted. You can enable, disable, and change the configuration of
built-in agents.

If you create an additional agent from a built-in script, that agent is considered a user-created agent,
which can be deleted.

In the output of the show running-config command:

n Built-in scripts are not displayed

n Built-in agents are displayed only if one of more parameters has been changed and saved.

The current software release includes a single built-in script and agent that monitors several system
resources:

Aruba Network Analytics Engine Introduction | 13

n Built-inscript:system_resource_monitor
n Built-inagent:system_resource_monitor.default
| Aruba-certified |     | scripts |     |
| --------------- | --- | ------- | --- |
Aruba-certifiedNetworkAnalyticsEnginescriptsarewrittenandtestedbyAruba.
OntheArubaSolutionExchange,Aruba-certifiedscriptshavethefollowingtag:nae-aruba-certified
| Figure2 | ScripttagsasshownontheArubaSolutionExchange |          |                    |
| ------- | ------------------------------------------- | -------- | ------------------ |
| Figure3 | ScripttagsasshownintheWebUI                 |          |                    |
| Aruba   | Solutions                                   | Exchange | (ASE) introduction |
ArubaSolutionExchange(ASE)isautilitythatallowsuserstodynamicallycreateconfigurationsfor
manyArubaproducts.TheexchangeoffersasetofsolutionscertifiedbyArubaforspecificusecases.
ThecollectiveknowledgeoftheArubacommunitypowerstheSolutionExchange.Allusersare
encouragedtocreatesolutions,modifyexistingones,andsuggestideasfornewsolutions.
AccesstotheArubaSolutionExchangeisavailableat:
https://ase.arubanetworks.com/
Nologinisrequiredtobrowsetheexchangeorlookatinformationaboutsolutions.Downloading
solutionsorviewingsolutionsourcecodeisfreeforanyonewithavaliduseraccountwiththeAruba
SSOauthenticationsystem.Ifyoudonothaveanexistingaccount,registerforafreeAirheadsSocial
accountat:
http://community.arubanetworks.com
FormoreinformationaboutusingtheArubaSolutionExchange,see
https://ase.arubanetworks.com/docs
| User-created | scripts |     |     |
| ------------ | ------- | --- | --- |
14
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

The Aruba Network Analytics Engine is highly extensible through the use of scripts. You can create
scripts or find scripts created by other developers in the community to solve specific network issues.

Network Analytic Engine scripts must be written in Python. Although Python programming is beyond
the scope of this document, this document provides information about the structure and functions of
Network Analytics Engine scripts.

For more information about Network Analytics Engine scripts, see Scripts.

Developer communities for the Network Analytics Engine
There are several communities that facilitate the development, use, and sharing of scripts for the Aruba
Network Analytics Engine:

Aruba Solution Exchange (ASE)

The Aruba Solution Exchange (ASE) is the primary portal for Network Analytic Engine scripts. Aruba-
certified public scripts are posted to ASE. Developers can create their own Network Analytics Engine
solutions and post them for either private or public use. See the Aruba Solution Exchange at:

https://ase.arubanetworks.com/

GitHub

The NAE scripts repository on GitHub includes Aruba-certified Network Analytics Engine (NAE) scripts
and examples organized by feature or protocol and then by supported hardware platform. Developers
can fork and customize or enhance these scripts for their own use. See the repository at:

https://github.com/aruba/nae-scripts

Airheads Community

The Airheads community provides a place for members or participants to search for information, read
and post about topics of interest, and learn from each other. Guests (unregistered visitors) can browse
or search the community for information. Members (registered users) can post messages or comments,
track discussions, and get email notifications on posting activity and other community actions.

Within the Airheads community, there is a Developer Community group that is specific to APIs,
programming, and automation. The Developer Community is the recommended place to post questions
about the Aruba Network Analytics Engine (NAE).

See the Developer community at:

https://community.arubanetworks.com/t5/Developer-Community/bd-p/DeveloperCommunity

See the Airheads community at http://community.arubanetworks.com/

Aruba Network Analytics Engine supported maximums

8400 Aruba Switch Series

n Maximum number of scripts per switch: 50

n Maximum number of agents per switch: 100

n Maximum number of monitors per switch: 300

n Maximum script file size: 256 KB

n Number of days of time-series data to store: 400

n Amount of switch storage allocated to time-series data: 18 GB

Aruba Network Analytics Engine Introduction | 15

Aruba 8320, 8325, 9300, and 10000 Switch Series

n Maximum number of scripts per switch: 25

n Maximum number of agents per switch: 50

n Maximum number of monitors per switch: 150

n Maximum script file size: 256 KB

n Number of days of time-series data to store: 400

n Amount of switch storage allocated to time-series data: 9 GB

Aruba 6300 and 6400 Switch Series

n Maximum number of scripts per switch: 10

n Maximum number of agents per switch: 10

n Maximum number of monitors per switch: 130

n Maximum script file size: 256 KB

n Number of days of time-series data to store: 45

n Amount of switch storage allocated to time-series data: 3.1 GB

Aruba 6200 Switch Series

n Maximum number of scripts per switch: 10

n Maximum number of agents per switch: 10

n Maximum number of monitors per switch: 130

n Maximum script file size: 256 KB

n Number of days of time-series data to store: 15

n Amount of switch storage allocated to time-series data: 1 GB

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

16

AOS-CX Network Analytics Engine (NAE)
Design considerations

Chapter 3

AOS-CX Network Analytics Engine (NAE) Design considerations

The Network Analytics Engine (NAE) feature within AOS-CX switches is a framework for automating the
detection of issues and automating root cause analysis. This document covers design considerations
when deploying NAE agents within a network.

NAE factors that impact system resources
There are several factors that need to be considered when deploying NAE within a network:

n CPU and memory: The number of agents and what the agents do within their callbacks can impact
the CPU and memory of the system. NAE agents are not running at all times and will only run when
one of their conditions are met for, at most, 30 seconds. Agents will only consume, at most, 10% of
CPU and 64 MB of memory as well while running.

n Wildcards within monitors: The use of wildcards within an NAE monitor can increase the amount of

resource consumption. Wildcards allow the agent to monitor an entire set of resources, but the
number of resources covered can be a large amount. For example, monitoring the tx_dropped
statistics for all interfaces will result in a metric for each interface:
/rest/v1/system/interfaces/*?attributes=statistics.tx_dropped

Each NAE metric results in a unique time series for this statistic. In this particular case, a switch with 500
interfaces equates to 500 time series metrics. In order to provide a rich history of each time series metric,
all NAE time series data is written to persistent storage. As noted within the manual, time series data is
collected and stored every 5 seconds.

n Alerts: Every ActionShell and ActionCLI output is written to persistent storage to provide a history of
events encountered by an NAE agent. This is useful for troubleshooting events that occurred in the
past and collecting relevant details associated with when those events occurred. These actions
consume storage resources. Also, the amount of data collected by these commands must be
considered.

n ADC’s: Application Data Collections (ADCs) are used to monitor traffic rates which can be utilized

within an NAE agent, but consume hardware resources used by ACLs, classifier policies, and other
traffic identifiers and filters. Hardware resources are limited based on platform. Please refer to the
“show resources” CLI command for a breakdown of hardware resource consumption.

NAE deployment considerations
It is highly recommended that any agent be thoroughly tested and vetted on a single or limited number
switches within the network prior to a wider deployment of such agent. NAE agents published by Aruba
have been tested for many customer deployments, but do not cover all cases. Customer networks can
be unique and may exhibit differences compared to a controlled lab environment.

All new NAE agents deployed within a customer network should be initially monitored to ensure that it is
performing according to expectations. The switch CPU and memory utilization can be reviewed through
the built-in System Resource Monitor NAE agent which provides the current and running history of
resource consumption. Storage usage can be monitored by reviewing the endurance utilization under
the show system resource-utilization command over time.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

17

There have been instances where the initial deployment of an NAE agent within a customer network
helped identify network oddity or misconfiguration from the start. The initial review of any NAE alerts
issued by this agent would quickly point out these misconfigurations. After making the necessary switch
or network changes, any future alerts would be reduced. As an example, a high number of RX drops
may indicate a bad fiber cable. Replacement of this cable would then result in less or zero RX drops and
the NAE agent will stop issuing alerts.

NAE agents are published through the Aruba Solution Exchange (ASE) and, much like switch firmware,
can be updated at any time. It is recommended that customers periodically check the ASE website for
any updates to NAE agents that are used within their network.

Considerations when writing an NAE agent
Aruba publishes agents which take the design recommendations covered in this document into
consideration, but NAE agents can be written by 3rd party developers and customers. As a result, care
should be taken when writing an NAE agent. Areas to consider include, and are not limited to:

n The use of wildcards should be used sparingly in order to reduce the memory and storage used by

the agent.

n Alerts should not be triggered frequently in order to reduce the wear of the storage device.

n The thresholds on conditions shouldn’t trigger often in order to reduce the number of alerts and CPU

time needed to act on the conditions.

n Any outbound network connections can only access the default VRF.

AOS-CX Network Analytics Engine (NAE) Design considerations | 18

Chapter 4

Aruba Network Analytics Engine
framework

Aruba Network Analytics Engine framework

The AOS-CX operating system has been built for programmability. With the database-centric design and
a programmatic interface to the entire database schema, network operators have access to every
network function and state within the switch.

Central to this design is the Aruba Network Analytics Engine framework, which includes the following:

n Full integration with the AOS-CX network operating system for logging events, maintaining high
availability during switch failover events, and interacting through the Web UI, REST API, and CLI.

n A REST API that can access every switch resource and state.

n Scripts and agents that can be programmed not only to monitor switch resources, but also

automatically execute actions when certain conditions are met over time.

n A built-in Python interpreter.

n A Python sandbox that exists only while an agent executes an action. The sandbox has full access to

the internal database and the time series database.

Configuration and state database
The AOS-CX operating system is a modular, database-centric operating system. Every aspect of the
switch configuration and state information is modeled in the AOS-CX switch database and is accessible
through the REST API.

Developers can access a specific configuration, statistic, or status result for any aspect of the switch
through its REST URI. Switches that are members of a stack are treated as a single switch.

For example:

n The following URI accesses the link state information about interface 1/1/5:
/rest/v1/system/ports/1%2F1%2F5?attributes=link_state

n The following URI accesses the link state of all interfaces on the switch:
/rest/v1/system/interfaces/*?attributes=link_state

n The following URI accesses the number of received packets on interface 1/1/5:
/rest/v1/system/interfaces/1%2F1%2F5?attributes=statistics.rx_packets

n The following URI accesses the link state information about interface 2/1/5 (stack member 2, slot 1,

port 5):

/rest/v1/system/ports/2%2F1%2F5?attributes=link_state

Time series database
The Aruba Network Analytics Engine includes a built-in time series database. Time-series data about the
resources monitored by agents are automatically collected and presented in graphs in the switch Web
UI. The database makes the data seamlessly available to agents that use rules that evaluate network
conditions over time.

Old time-series data is removed automatically either as the storage space on the switch is used, or as
the maximum number of days of data is reached. The amount of storage space consumed at any given
time depends on the number of switch resources being monitored at that time. Each monitored

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

19

resource creates one time series. Each time series consumes approximately 240 KB of storage for each
day.

When creating a script, software developers do not interact with this database directly. Use of the
database is automatically handled by the Monitor and Rule functions.

AOS-CX REST API
Switches running the AOS-CX software are fully programmable with a REST (REpresentational State
Transfer) API, allowing easy integration with other devices both on premises and in the cloud. This
programmability—combined with the Aruba Network Analytics Engine—accelerates network
administrator understanding of and response to network issues.

The AOS-CX REST API enables programmatic access to the AOS-CX configuration and state database at
the heart of the switch. By using a structured model, changes to the content and formatting of the CLI
output do not affect the programs you write. And because the configuration is stored in a structured
database instead of a text file, rolling back changes is easier than ever, thus dramatically reducing a risk
of downtime and performance issues.

The AOS-CX REST API is a web service that performs operations on switch resources using HTTPS POST,
GET, PUT, and DELETE methods.

A switch resource is indicated by its Uniform Resource Identifier (URI). A URI can be made up of several
components, including the host name or IP address, port number, the path, and an optional query
string. The AOS-CX operating system includes the AOS-CX REST API Reference, which is a web interface
based on the Swagger UI. The AOS-CX REST API Reference provides the reference documentation for
the REST API, including resources URIs, models, methods, and errors. The AOS-CX REST API Reference
shows most of the supported read and write methods for all switch resources.

Python and the REST API for scripts
Network Analytics Engine scripts are written in Python, and the Network Analytics Engine provides a
built-in Python interpreter that is used when validating scripts and creating agents from scripts.

Python is the go-to language for network engineers:

n Python is high-level and human-readable.

n Python is popular with an active development community.

n There are many libraries (code written for you that you can use in your programs) available.

Python and the REST API to the AOS-CX database provide powerful tools to support network
automation. By using Python and the REST API, you can move far beyond CLI scripting in network
automation.

In the past, a network engineer might use Perl scripts to automate show and configure CLI commands.
This scheme provided some automation, but it was inefficient because it still used the CLI to interact
with the switch. CLI inputs and outputs are in an unstructured, human-readable format. You must use
text processing based on specific CLI output to extract the information you want.

For example, you would have to write code to detect a MAC address in the large continuous string of
text that is the CLI output. The CLI output might have many things to make it human-readable, such as
table formatting, column headings, introductory text, and so forth, and the way MAC addresses are
presented can vary by CLI, operating system version, and sometimes even by individual command
output.

Aruba Network Analytics Engine framework | 20

In contrast, by using programmatic APIs such as the AOS-CX REST API, you can get the information you
are looking for in a predictable and structured way. For example, you can ask for and get just the MAC
address.

Although Python programming is beyond the scope of this document, this document provides
information about the structure and functions of Network Analytics Engine scripts.

"Sandboxes" for agent actions
When an agent performs an action, the action is performed in a "sandbox" that is created when the
action starts and removed when the action completes. The sandbox is in the default VRF, so it does not
have access to the management network.

A sandbox is an isolated, tightly controlled environment in which programs can be run. Sandboxes
restrict what a program can do, giving it the appropriate permissions and computing resources without
allowing it access to the entire computing environment.

This design has the following benefits:

n Agents coexist and are prevented from using an excessive amount of CPU resources.

n Agents can benefit from the high-availability features of AOS-CX. During a switch failover event, the
daemon that handles the sandbox can recover its state information and continue operations as
before.

n Agents are prevented from accessing sensitive information—such as certificate files—in the switch

operating system.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

21

Chapter 5

Managing scripts

Managing scripts

You can view a list of scripts and information about specific scripts on the switch using any of the
following interfaces:

n Web UI Analytics panel on the Overview page

The Analytics panel shows the total number of scripts, agents, and monitors compared to the total
number supported on the switch.

n Web UI Analytics dashboard

n REST API GET method on the nae_scripts resource

n CLI show nae-script command

Managing NAE scripts across switch software updates
After you update the switch software to a new release or install an older software release on the switch,
some Aruba Network Analytics Engine (NAE) scripts might not be valid. A script might not be valid
because the script uses a URI or API function that is not valid on that software release. The existing
scripts might generate errors, and the NAE data might not be valid until you upload the new scripts and
clear the NAE data.

Prerequisites

The new switch software has been installed on the switch.

Procedure

1. Clear the NAE data by entering the clear nae-data command from the manager context.

switch# clear nae-data

2. For each script that is not marked System Created in the Web UI, locate the version of the script

that supports the software release running on the switch.
n For Aruba-certified NAE scripts, the Aruba Solutions Exchange (ASE) includes tags that indicate

the minimum and maximum supported software release.

n For switches running 10.01 and later software releases, when you select the ASE download
button in the Web UI, the Web UI displays only the Aruba-certified NAE scripts that are
supported on the software release running on the switch.

n For scripts that are not Aruba-certified NAE scripts downloaded from the ASE, see the
information provided by the script author about which script version is supported.

3. Follow the instructions for updating a script.

The steps to update a script depend on the switch software release version that was running
when the script was installed.

4. On the Analytics Dashboard, locate and close any time series graph panels for the default agent

from the previous software release.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

22

The default agent is created from the built-in script. The name of the agent is based on the name
of the built-in script. Built-in scripts and agents have an origin of "system" and are marked System
Created in the Web UI. Built-in scripts and their agents are updated automatically. However,
sometimes the time series graph panel for the previous default agent is not closed during the
update. After the software update, instead of graphed data, such panels show an error message
beginning with: Agent data not found.

Viewing script details using the Web UI

Prerequisites

You must be logged in to the AOS-CX Web UI.

Procedure

1. From the Overview page, look at the Analytics panel to view the total number of scripts, agents,

and monitors compared to the total number supported on the switch.

For example, Scripts: 7/25 indicates that there are total of seven scripts out of a maximum of
25 scripts supported on this switch.

2. Select Analytics from the AOS-CX Web UI navigation pane. The Analytics Dashboard is displayed.

3. The Scripts panel in the Analytics Dashboard shows a list of the scripts available on the switch.

4. From the Scripts panel, select a link to a specific script to display the Script Details page.

You can view the following script details.

Managing scripts | 23

n Script Details panel: Shows script information, and if the script is system created. You can select the

+ sign to create an agent from the script.

n Script Parameters panel: Shows a list of parameters configured in the script. Select a parameter to

display a dialog box with a description of the parameter.

n Script Contents panel: Shows the programmatic contents of the script. You can click the down

arrow to download the script.

n Script Details panel: Shows script information, and if the script is system created. You can select the

+ sign to create an agent from the script.

n Script Parameters panel: Shows a list of parameters configured in the script. Select a parameter to

display a dialog box with a description of the parameter.

n Script Contents panel: Shows the programmatic contents of the script. You can click the down

arrow to download the script.

Downloading a script using the Web UI
You may want to change a downloaded script and upload it again after making changes. You can
download a script and save the file to the specified location.

Prerequisites

You must be logged in to the AOS-CX Web UI.

Procedure

1. Select Analytics from the navigation pane.

2.

In the Analytics Dashboard, in the Scripts panel, click Scripts to display the Script Management
page.

3. Select a script row (not the script link) and click

Download to download the script.

You can also download a script from the Script Details page, in the Script Contents panel, where

you see the
In the download dialog box, you can either open the script file or save the file.

button.

4.

Saving will overwrite any existing file in the specified location with the same name.

To download the script, click OK. To cancel this operation, click Cancel.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

24

Uploading a script using the Web UI

Prerequisites

You must be logged in to the AOS-CX Web UI with administrator rights.

Procedure

1. Select Analytics from the navigation pane.

2.

In the Analytics Dashboard, in the Scripts panel, click Scripts to display the Script Management
page.

3.

In the Script Management page, click Upload.

4. The Upload Script dialog box is displayed where you can specify a script file to upload. You can

either drag and drop a file or browse to select the file to upload. Click Next to continue with the
upload or click Cancel.

5.

In the Upload Script dialog box, do the following:
a. Verify that the correct script is displayed.
b. Optionally, select Save running config to startup.

If you do not save the running configuration to the startup configuration, the change is not
preserved when the switch is rebooted.

c. To upload the script, click Upload. To cancel this operation or to upload a different script

than the script that is displayed, click Back.

6.

If the name of the script as shown in the script manifest matches the name of the existing script,
when you upload the script, the Aruba Network Analytics Engine (NAE) does the following:

If the name of the script as shown in the script manifest matches the name of the existing script,
a confirmation dialog box is displayed. Confirm that you want the existing script to be updated.
n Displays a message that a script with the same name exits, and asks you to confirm that you

want to update the existing script.

n Deletes the existing script and agents

n Replaces the existing script with the new script

n Recreates the agents with the same parameters that were used before the script was updated.

If the upload is successful, a success message is displayed. The new script is added to the list of
available scripts, or the existing script is updated.

Managing scripts | 25

If the upload is unsuccessful, an error is displayed indicating what parts of the script manifest are
invalid.

If the script has a syntax error but it contains the required manifest, the upload will complete. However,
the status field will show an error indicator. If you go to the Script Details page, you can get more details
on the error.

Updating a script using the Web UI

Prerequisites

You must be logged in to the AOS-CX Web UI with administrator rights.

Procedure

1.

If the new script has the same name as the existing script, and the existing script was installed
while the switch was running AOS-CX software version 10.03 or later, upload the new script:

The name in the manifest of the script must match the name of the script in the Scripts panel of
the Analytics Dashboard exactly. For example, a script with a version number in the name does
not match a script that does not include a version number in the name. The script file name is not
required to match the script name in the manifest. For example, the script file name can include a
version number.

If the name of the script as shown in the script manifest matches the name of the existing script,
when you upload the script, the Aruba Network Analytics Engine (NAE) does the following:

n Displays a message that a script with the same name exits and asks you to confirm that you

want to update the existing script.

n Deletes the existing script and agents

n Replaces the existing script with the new script

n Recreates the agents with the same parameters that were used before the script was updated.

If the monitors in the new script and the existing script are the same, previously collected time-
series data is preserved when the script is updated. Clearing the NAE data is not required.

2.

If the name of the new script does not match the name of the existing script, or the existing script
was installed while the switch was running an AOS-CX software version earlier than 10.03, do the
following:
a. Delete the existing script. When you delete a script, the agents are deleted automatically.
b. Upload the new script.
c. Clear the NAE data by entering the clear nae-data command from the manager context.

switch# clear nae-data

d. Create agents associated with the new script.
e. Add time series graph panels for the agents to the Analytics Dashboard.

Deleting a script using the Web UI

Deleting a script also deletes all agents associated with that script.

Prerequisites

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

26

YoumustbeloggedintotheAOS-CXWebUIwithadministratorrights.
Procedure
1. SelectAnalyticsfromthenavigationpane.
2. IntheAnalyticsDashboard,intheScriptspanel,clickScriptstodisplaytheScriptManagement
page.
3. Selectascriptrow(notthescriptlink)andclickDelete.
4. Intheconfirmationdialogbox,dothefollowing:
a. Optionally,selectSave running config to startup.Ifyoudonotsavetherunning
configurationtothestartupconfiguration,thechangeisnotpreservedwhentheswitchis
rebooted.
| b.      | Todeletethescript,clickConfirm.Tocancel,clickCancel. |       |         |           |          |
| ------- | ---------------------------------------------------- | ----- | ------- | --------- | -------- |
| Getting | information                                          | about | scripts | using the | REST API |
InstructionsandexamplesinthisdocumentuseanIPaddressthatisreservedfordocumentation,
192.0.2.5,asanexampleoftheIPaddressfortheswitch.Toaccessyourswitch,youmustusetheIP
addressorhostnameofthatswitch.
Prerequisites
YoumustbeloggedintotheswitchRESTAPI.
Procedure
n Togetdetailedinformationaboutaspecificscript,usetheGETmethodontheURIofthescript.
Thisexamplegetsinformationaboutthescriptnamed
com.arubanetworks.mac_arp_count_monitor:
GET https://192.0.2.5/rest/v1/system/nae_scripts/com.arubanetworks.mac_arp_count_monitor
Thefollowingexampleistheresponsebodyfortherequest.Theentirescriptisreturnedinbase64
format.Becauseofthelengthofthescript,theexampleshowsonlypartofthescript.
{
| "author": | "Aruba Networks", |     |     |     |     |
| --------- | ----------------- | --- | --- | --- | --- |
"description": "MAC address learned on VLAN ID and number of neighbors learned
| using | ARP", |     |     |     |     |
| ----- | ----- | --- | --- | --- | --- |
"expert_only": false,
| "nae_parameters": | {   |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- |
"Vlan_Id": "/rest/v1/system/nae_scripts/mac_arp_count_monitor/nae_
parameters/Vlan_Id"
},
| "name":   | "mac_arp_count_monitor", |     |     |     |     |
| --------- | ------------------------ | --- | --- | --- | --- |
| "origin": | "user",                  |     |     |     |     |
"script": "IyAtKi0gY29XBUCAgICpdGRvcih1cmky...LCAnQVJQIFRhYmxlIENvdW50JykK",
| "status": | {   |     |     |     |     |
| --------- | --- | --- | --- | --- | --- |
"state": "VALIDATED"
},
| "tags":    | ['bridging','vlan','mac','neighbors','arp'] |     |     |     |     |
| ---------- | ------------------------------------------- | --- | --- | --- | --- |
| "version": | "1.0"                                       |     |     |     |     |
}
Managingscripts|27

n To get a list of all the scripts, use the GET method on the URI of the nae_scripts collection of the

script.

For example:
GET https://192.0.2.5/rest/v1/system/nae_scripts

Example response:

[

]

"/rest/v1/system/nae_scripts/system_resource_monitor",
"/rest/v1/system/nae_scripts/mac_arp_count_monitor",
"/rest/v1/system/nae_scripts/ospf_neighbor"

Uploading a script using the REST API
Instructions and examples in this document use an IP address that is reserved for documentation,
192.0.2.5, as an example of the IP address for the switch. To access your switch, you must use the IP
address or hostname of that switch.

Prerequisites

n You must be logged in to the switch REST API with a user name that has administrator rights.

n The switch REST API access mode must be read-write.

n The script must be encoded in base64 format.

Scripts you download from the Aruba Solution Exchange website (instead of through the switch Web UI)
or the GitHub repository are not in base64 format. You must encode those scripts before you upload
them.

Procedure

Use the POST method to upload the script to the nae_scripts resource collection.

For example:

POST https://192.0.2.5/rest/v1/system/nae_scripts
{

"name": "port_admin_state_monitor",
"expert_only":false,
"script": "<script_content_encoded_in_base64_format>"

}

In the example:

n The name of the script is: port_admin_state_monitor

n The expert_only parameter indicates whether it is recommended that someone using the script

have expert knowledge about the script. Typically, this parameter is false.

n <script_content_encoded_in_base64_format> is the text string of the script after it is encoded in base64

format. For an example of a script in base64 encoded format, see Script example.

If the script name in the Manifest of the new script exactly matches the name of an script that has
already been uploaded, the upload fails with a message that informs you that the script already exists.
You can use the PUT method to update the existing script.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

28

If you are uploading a script to replace an existing script, but the script name in the Manifest is not an
exact match, you must delete the script you want to replace.

Updating a script using the REST API
Instructions and examples in this document use an IP address that is reserved for documentation,
192.0.2.5, as an example of the IP address for the switch. To access your switch, you must use the IP
address or hostname of that switch.

Prerequisites

n You must be logged in to the switch REST API with a user name that has administrator rights.

n The switch REST API access mode must be read-write.

Procedure

1.

If the name of the script in the Manifest is an exact match to the name of the existing script, and
the existing script was installed while the switch was running AOS-CX software version 10.03 or
later, use the PUT method to update the script.

When the PUT method is used, the existing script and agents are deleted, the script is replaced,
and the agents are automatically recreated with the same parameters that were used before the
script was updated. If the monitors in the new script and the existing script are the same,
previously collected time-series data is preserved when the script is updated.

2.

If the existing script was installed while the switch was running an AOS-CX software version
earlier than 10.03, or the script name in the Manifest does not match the name of the existing
script—for example one has a version number in the name and the other does not—you must
delete the existing script and then upload the new script:
a. Use the DELETE method to delete the script.

When you delete a script, all associated agents are deleted automatically.

b. Use the POST method to upload the modified script.
c. Clear the NAE data.
d. Create agents associated with the new switch.

Deleting a script using the REST API
Instructions and examples in this document use an IP address that is reserved for documentation,
192.0.2.5, as an example of the IP address for the switch. To access your switch, you must use the IP
address or hostname of that switch.

Deleting a script also deletes all agents associated with that script.

Prerequisites

n You must be logged in to the switch REST API with a user name that has administrator rights.

n The switch REST API access mode must be read-write.

Procedure

To delete a script, use the DELETE method on the URI of the script.

The following example deletes the script: com.myco.bgp_mon.
DELETE https://192.0.2.5/rest/v1/system/nae_scripts/com.myco.bgp_mon

Managing scripts | 29

Downloading a script from the switch using the REST API
Instructions and examples in this document use an IP address that is reserved for documentation,
192.0.2.5, as an example of the IP address for the switch. To access your switch, you must use the IP
address or hostname of that switch.

Prerequisites

You must be logged in to the switch REST API.

Procedure

Use the GET method on the URI of the script.

This example downloads script named com.arubanetworks.mac_arp_count_monitor.
GET https://192.0.2.5/rest/v1/system/nae_scripts/com.arubanetworks.mac_arp_count_monitor

The following example is the response body for the request. The entire script is returned in base64
format. Because of the length of the script, the example shows only part of the script.

{

"author": "Aruba Networks",
"description": "MAC address learned on VLAN ID and number of neighbors learned

using ARP",

"expert_only": false,
"nae_parameters": {

"Vlan_Id": "/rest/v1/system/nae_scripts/mac_arp_count_monitor/nae_

parameters/Vlan_Id"

},
"name": "mac_arp_count_monitor",
"origin": "user",
"script": "IyAtKi0gY29XBUCAgICpdGRvcih1cmky...LCAnQVJQIFRhYmxlIENvdW50JykK",
"status": {

"state": "VALIDATED"

},
"version": "1.0"

}

show running-config command output for agents and
scripts
Built-in scripts are not included in the output of the show running-config command.

A built-in agent is included in the output of the show running-config command only if one or more of
the agent parameters has been modified and saved.

User-created scripts and agents are included in the output of the show running-config command.

The output of the show running-config command includes the following information for scripts and
agents:

n The name of the script.

n The value of the expert_only parameter. Typically, this parameter has a value of false.

n The script code in base64 format.

n The name of the agent.

n The value of the enabled parameter.

n The name of each agent parameter, followed by its value in base64 format.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

30

The following example shows the output of show running-config for a user-created NAE script and one
agent that monitors a route count. The name of the script is: route_count_monitor. The name of the
agent is: route_count_instance1.

The entire script is returned in base64 format. Because of the length of the script, the example shows
only part of the script.

switch# show running-config
...
nae-script route_count_monitor false IyAtKi0gY29kaW5nOiB1dGYtOCAtK
i0NCiMNCiMgQ29weXJpZ2h0IChjKSAyMDE3IEhld2xldHQgUGFja2FyZCBFbnRlcnB
...
yaXNlIERldmVsb3BtZW50IExQDQojDQojIExpY2Vuc2VkIHVuZGVyIHRoZSBBcGFja
nae-agent route_count_monitor route_count_instance1 false upper_co
unt_threshold:MTAwMDA= vrf_name:ZGVmYXVsdA== lower_count_threshold
:OTUwMA==
...

Script status
A script can have the following status values:

CREATED

The script has been uploaded to the switch, but script validation has not begun.

ERROR

The script validation process detected an error that would result in execution errors. Resolve the
error by modifying the script.

VALIDATING

The script syntax and components (manifest, parameters, monitor, condition, and action) are in the
process of being validated.

VALIDATED

The script syntax and components (manifest, parameters, monitor, condition, and action) have been
validated and no errors have been found.

Managing scripts | 31

Chapter 6

Managing agents

Managing agents

You can view a list of agents and information about specific agents on the switch using any of the
following interfaces:

n Web UI Analytics panel on the Overview page

The Analytics panel shows the total number of scripts, agents, and monitors compared to the total
number supported on the switch.

n Web UI Analytics dashboard

n REST API GET method on the nae_agents resource

n CLI show nae-agent command

Viewing a list of agents installed on a switch using the Web
UI

Prerequisites

You must be logged in to the AOS-CX Web UI.

Procedure

1. Select Analytics from the ArubasOS-CX Web UI navigation pane. The Analytics Dashboard is

displayed.

2. The Agents panel in the Analytics Dashboard shows a list of the agents installed on the switch,

along with the status of each agent.

Viewing agent information using the Web UI
You can view Analytics agent information including: agent status, script information, agent parameters,
one or more time series graphs, and any alerts generated.

Prerequisites

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

32

n You must be logged in to the Web UI.

n Ensure that the switch and the client where Web UI is running are set to use NTP or to a time zone

based on UTC time. Otherwise, NAE agent data might be incorrect or missing.

For example, if the time on switch is set to 2 hours ahead of the client manually instead of by changing
the time zone offset, the agent data is populated according to the new time on switch. If the switch time
is set back to match client time later, the Time Series Database does not overwrite the old data.
Therefore the client Web UI shows inaccurate data.

Procedure

1. From the Overview page, look at the Analytics panel to see the total number of agents in critical,

major, and minor status. If the panel is outlined in red, it indicates agent status issues.

2. To go to the Analytics Dashboard, select the Analytics link in the Analytics panel on the Overview

page.

View the following information on the Analytics Dashboard:

n

Top banner: Shows the number of agents with each type of status.

n Agents panel: Lists the agents installed on the switch and indicates the status of each agent.

If there is an error in an agent, the Agents panel shows an error icon next to the agent status.
Optionally, you can add an Analytics agent time series graph to the Analytics Dashboard by clicking
the + plus sign next to any agent listed in the Agents panel.

The time series graph shows data collected by the Analytics agent. If an agent has multiple time
series graphs, the graph displayed on the Analytics Dashboard is specified by the script. You

Managing agents | 33

cannot choose which graph to display on the Analytics Dashboard, but you can see all the graphs in
the Agent Details page.

Click the Agents link to display the Agent Management page. On this page you can create, edit,
delete, enable, and disable an agent.

n Scripts panel: Lists available scripts.

Select a script from the list to display the Script Details page where you can view script details,
create an agent to run the script, and download the script.

Click the Scripts link to display the Script Management page. On this page you can upload,
download or delete a script, create an agent, and access the Aruba Solution Exchange to find more
scripts.

n Alerts panel: Lists alerts generated by all agents.

Select an alert in the list and click Details to display the Alert Details dialog box.

Click the Alerts link to display a list of the alerts with information on the rule and actions for each
alert.

n Time series graphs: If an agent time series graph has been added to the Analytics Dashboard, the
graph is outlined in the agent status color. Agents can have more than one time series graph, but
only one graph for the agent is displayed in the Analytics dashboard. Click the link in the graph to
display the Agent Details page.

3. From the Analytics Dashboard, Agents panel, select the link to a specific agent. The Agent Details

page is displayed.

View the following information from the Agent Details page:

n Agent Details panel: Shows information about the agent.

Select the
Select the
information, create an agent to run the script, and download the script.

Edit button to enable or disable an agent and modify agent parameters.
View Script button to display the Script Details page where you can view script

n Status panel: Shows the status of the agent and when the status was last updated. For some

agents, you may see additional information. For example:

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

34

System Created

If the Status panel includes the statement System Created, the agent cannot be deleted.

Baseline Thresholds

If the Status panel includes Baseline Thresholds, the agent can learn about the activity
being measured and set low thresholds and high thresholds based on what it learns. The
Baseline Thresholds information shown in the Status panel includes the number of
thresholds in the following states:

Active

When a baseline threshold is in the active state, the agent has learned and established the
high and low thresholds, and the agent executes actions and generates alerts based on
those low or high thresholds.

Inactive

When agent is disabled, the baseline stops collecting data and updating thresholds. After
the agent is re-enabled, the baseline goes into the learning state again.

Learning

While a baseline threshold is in the learning state:

o The agent gathers data related to that baseline until the initial learning period completes.

Low and high thresholds are determined using the learning algorithm defined in the script,
and are set only after learning state is completed.

o Default thresholds (if specified in the script) are used to determine whether to execute

actions or generate alerts.

Baseline thresholds remain in the learning state for a script-specified period of time after the
agent is enabled.

Selecting Baseline Thresholds displays a dialog box that shows additional information about
all the baselines for the agent, including the name, the associated monitor, state, and the
current learned low and high thresholds.

If there is an agent error, an error indicator is shown and you can hover over it for more
information.

Managing agents | 35

n Parameters panel: Shows the parameters used by the agent. For example, a parameter can

be a threshold value that, when breached, causes the agent status to change and an alert to be
generated. Selecting a parameter displays the description in a dialog box.

n Time Series graph: Graphs the data collected by the agent over time. Agents might have more
than one time series graph. Alert indicators and configuration checkpoints are overlaid on the
graph.

Alert indicators can include: a red or yellow triangle for an alert, a green triangle for return to
normal, a blue triangle for an alert on several resources being monitored. An example of an
alert on several resources: when monitoring multiple interfaces (wildcard), if an interface goes
down, a red alert is generated. If another interface goes down, then a blue alert is generated.
A green alert will not be generated until all the interfaces are back up.

Configuration checkpoints are shown as purple diamonds on the graph.

Clicking an alert indicator on the graph displays the Alert Details dialog box.

n Alerts panel: Lists alerts.

Select the Alerts link to display a list of the alerts with information on the rule and actions for
each alert.

Select an alert and click Details to display the Alert Details dialog box.

Select an alert and click Navigate to change the time series graph to show the time period
with this alert.

Finding alert details using the Web UI
You can view details on the alerts displayed in the Web UI.

Prerequisites

You must be logged in to the Web UI.

Procedure

1. Select Analytics from the navigation pane.

2.

In the Analytics Dashboard, the Alerts panel lists the alerts for all agents.

3. To see the alerts for a specific agent, in the Analytics Dashboard Agents panel or Alerts panel,

select an agent.

4.

In the Agent Details page, the agent alerts are listed in the Alerts panel.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

36

5.

In the Alerts panel, select an alert and click Details to view the Alert Details dialog box. To close
the dialog box, click Close.

You can also access alert details directly from the Analytics Dashboard by selecting an alert in the
Alerts panel and clicking Details.

6. The Action Result(s) in Alert Details dialog box might include additional details about actions

and links to the action result output.

To view the Action Result Output dialog box for an action, click the Output link.

Managing agents | 37

Working with an Analytics time series graph
Data collected by an Analytics agent is displayed in the Web UI in one or more time series graphs. An
agent has at least one graph. An agent can have multiple graphs as specified in the script, but only one
graph represents the agent on the Analytics dashboard. The graph that represents the agent on the
Analytics dashboard is specified in the script.

If the Analytics dashboard does not include a graph for an agent, you can add the graph that represents
that agent from Analytics dashboard. Graphs on the Analytics dashboard represent a live view only. The
graph customization toolbar is not available from the Analytics dashboard.

The Agent Details page displays all the graphs for an agent, with each graph displayed in a panel.

Configuration checkpoints and alert indicators are overlaid on the graph. Configuration checkpoints are
shown as purple diamonds. Alert indicators can include the following:

n A red or yellow triangle for an alert

n A green triangle for a return to normal

n A blue triangle for an alert on several resources being monitored.

The graph displays alerts for all metrics being monitored. However, time series graphical information
can be shown for a maximum of eight metrics. The metrics that are being shown on the graph are listed
at the bottom of the graph.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

38

n Customizing data displayed on the graph on page 39

n Zooming in on the graph on page 40

n Downloading the graph as animage or .csv file on page 41

n Viewing an alert on the graph on page 41

Customizing data displayed on the graph

There are several ways you can customize the data displayed on a time series graph to show more or
less data.

Procedure

1. View a tooltip for each data point on the graph by hovering the cursor over the data point.

The tooltip displays the date, time range, and min-max range.

2. Hover over a specific item in the legend following the graph to show only that specific data line on

the graph. The other data will be less visible.

From the graph shown on the Agent Details page, click the
the Customize Chart dialog box.
n The default mode is Automatic Monitoring, where the most meaningful monitors and

Configure Chart button to open

resources are automatically selected to display on the agent graph. To customize what data
(monitors and resources) you want displayed on the agent time series graph, select
Customize Monitoring.

Managing agents | 39

n You can sort and filter the Show column. If a monitor is a wildcard type, then you see a

different icon from the check box, where you can click and select subresources under that
monitor.

The graph displays alerts for all metrics being monitored. However, the graph can show graphed
data for a maximum of eight metrics at a time. The metrics that are being shown on the graph are
listed at the bottom of the graph. You can choose which metrics to show. To remove the metric
from the graph, clear the box in the Show column of the metric you want to remove. To show a
metric in the graph, select the box in the Show column of the metric you want to display.

n The Resources Selected column shows how many total resources are selected out of the total

available resources.

n If a monitor can have an aggregation function, that function is displayed in the Aggregation

column.

Zooming in on the graph

There are several different ways to zoom in on a specific time period on the time series graph.

Procedure

1. Zoom in and out on the graph by selecting a zoom level from the options displayed at the top of
the time series graph: 1 hour, 1 day, 10 days, 30 days, 90 days, 180 days, 1 year. You can also
select Custom to enter a specific date and time range.

2. Or you can highlight a custom range of data on the graph as follows:

a. Position the cursor on the time axis of the graph until a vertical line appears through the

time.

b. Drag the vertical line to the left or right to the beginning or end of the time period you want

to view.

c. The selected time period is highlighted and the begin and end dates are displayed next to the

Custom zoom level.

d. Release the mouse button and the graph is redrawn for just the time period selected.

3. Reset the graph to the default by selecting the Live zoom level.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

40

Downloading the graph as animage or .csv file

You can download the graph either as an image or represented as a set of comma-separated values
that can be opened in spreadsheet programs. The download options are accessed from the down arrow
in the top right corner of the time series graph:

n To download the graph as an image, click the down arrow and select Download Chart. The graph is

downloaded in a file in .png format.

n To download the graph as a set of comma-separated values, click the down arrow and select Export

to CSV.

The graph is downloaded in a file in .csv format.

Viewing an alert on the graph

The graph shown on the Agent Details page might not show the time period or resource associated with
a specific alert. Use this procedure to change the graph to show the alert and the associated metric.

Procedure

1. From the alerts panel on the Agent Details page, select an alert and click Navigate.

The graph is changed to display the time period containing the alert. However, the alert might be for a
metric that is being monitored but that is not being shown in the graph.

The graph displays alerts for all metrics being monitored. However, the graph can show graphed data
for a maximum of eight metrics at a time. The metrics that are being shown on the graph are listed at
the bottom of the graph.

Managing agents | 41

2. To adjust the graph display to show the metrics for the alert, do the following:

a. Locate the alert on the graph and click the alert triangle flag. The Alert Details dialog box is

displayed.

b. Click View on Graph.

3.

If the graph is showing eight metrics and the metric you want to display is the ninth metric, you
must choose an existing metric to clear so that the graph can show the metric associated with the
alert.

For example:

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

42

a. Clear the selection box for the metrics you no longer want to show.

For example:

b. Click View on Graph.

The graph is changed to show the metric associated with the alert.

For example:

Managing agents | 43

4. YoucanresetthegraphtothedefaultbyselectingtheLivezoomlevel.
| Enabling | a disabled | agent | using the | Web UI |
| -------- | ---------- | ----- | --------- | ------ |
Prerequisites
YoumustbeloggedintotheAOS-CXWebUIwithadministratorrights.
Procedure
1. SelectAnalyticsfromthenavigationpane.
2. IntheAnalyticsDashboard,intheAgentspanel,clickAgents.
3. TheAgentManagementpageisdisplayed.Toenableadisabledagent,selecttheagentrow(not
thelink)foranagentthatisdisabledandclickEnable.
4. Intheconfirmationdialogbox,dothefollowing:
| a. Optionally,selectSave |     | running | config to startup. |     |
| ------------------------ | --- | ------- | ------------------ | --- |
Ifyoudonotsavetherunningconfigurationtothestartupconfiguration,thechangeis
notpreservedwhentheswitchisrebooted.
| b. Toenabletheagent,clickConfirm.Tocancel,clickCancel. |          |       |         |     |
| ------------------------------------------------------ | -------- | ----- | ------- | --- |
| Disabling                                              | an agent | using | the Web | UI  |
Prerequisites
44
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

You must be logged in to the AOS-CX Web UI with administrator rights.

Procedure

1. Select Analytics from the navigation pane.

2.

In the Analytics Dashboard, in the Agents panel, click Agents.

3. The Agent Management page is displayed. To disable an agent, select the agent row (not the link)

in the list and click Disable.

4.

In the dialog box, click Confirm to disable the agent or Cancel. Optionally, check the box to Save
the running config to startup. If you do not select Save the running config to startup, the
change is not preserved when the switch is rebooted.

Deleting an agent using the Web UI

Prerequisites

You must be logged in to the AOS-CX Web UI with administrator rights.

Procedure

1. Select Analytics from the navigation pane.

2.

In the Analytics Dashboard, in the Agents panel, click Agents.

3. The Agent Management page is displayed. To delete an agent, select the agent row (not the link)

in the list and click Delete.

4.

In the dialog box, click Confirm to delete the agent or Cancel. Optionally, check the box to Save
the running config to startup. If you do not select Save the running config to startup, the
change is not preserved when the switch is rebooted.

Creating an agent from an existing script using the Web UI

Prerequisites

You must be logged in to the AOS-CX Web UI with administrator rights.

Procedure

Managing agents | 45

1. Select Analytics from the navigation pane.

2.

In the Analytics Dashboard, in the Agents panel, click Agents.

3. The Agent Management page is displayed. To create an agent, click + Create.

You can also create an agent from the Scripts Management page by selecting a script row and
clicking + Create Agent. Access the Scripts Management page from the Analytics Dashboard by
selecting the Scripts link in the Scripts panel.

4.

In the Create Agent dialog box, enter the agent information.
a. To see a list of scripts available on the switch, click the down arrow next to the Script field.
b. Select a script for the agent to run.
c. Enter a name for the agent.
d. Based on the script you selected, a list of parameters is displayed without values in the Value

column. Enter the values for the parameters.

The More Info column displays additional information about the parameter, such as the
default value.

If the More Info column includes the lock icon, the value of the parameter is encrypted. The
characters you enter are masked on the screen with bullet characters.

If you do not enter a value and there is a default value defined, the default value is used.

If the Value column labels the parameter as Required and that parameter does not include a
default value, you must supply a value before you can create the agent.

e. Optionally, check the box to Save running config to startup.

If you do not save the running configuration to the startup configuration, the change is not
preserved when the switch is rebooted.

f. To create an agent running the specified script with the parameter values entered, click

Create. To cancel the operation, click Cancel.

Changing the configuration of an agent using the Web UI

Prerequisites

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

46

You must be logged in to the AOS-CX Web UI with administrator rights.

Procedure

1. Select Analytics from the navigation pane.

2.

In the Analytics Dashboard, in the Agents panel, click Agents.

3. The Agent Management page is displayed. To edit an agent, select the agent row (not the link) in

the list and click Edit.

4.

In the Edit dialog box, change parameter values you want to change.

Only integer values (threshold or rate) can be changed.

You can also disable or enable the agent by clicking the Enabled slider.

5. Optionally, select Save running config to startup.

If you do not save the running configuration to the startup configuration, the change is not
preserved when the switch is rebooted.

6. To save your changes, click Save. To cancel, click Cancel.

Getting information about agents using the REST API
Instructions and examples in this document use an IP address that is reserved for documentation,
192.0.2.5, as an example of the IP address for the switch. To access your switch, you must use the IP
address or hostname of that switch.

Prerequisites

You must be logged in to the switch REST API.

Procedure

n To get detailed information about a specific agent, use the GET method on the URI of the agent.

This example gets information about the agent named com.myco.bgp_mon.Agent1:
GET https://192.0.2.5/rest/v1/system/nae_scripts/com.myco.bgp_mon/nae_
agents/com.myco.bgp_mon.Agent1

The following response is an example of an agent that has an error:

{

}

"name": "com.myco.bgp_mon.Agent1",
"disabled":false,
"parameters_values":{

"threshold":"10"

}

"status": {

"error_at": "1490134092",
"error_description": "The URI is invalid or not supported",
"executed_at": "1490134092",

n To get a list of the agents of a specific script, use the GET method on the URI of the nae_agents

collection of the script.

This example gets a list of the agents of the script com.myco.bgp_mon:
GET https://192.0.2.5/rest/v1/system/nae_scripts/com.myco.bgp_mon/nae_agents

Managing agents | 47

The following is an example of a response for a script, port_admin_state_monitor, that has multiple
agents:

[

]

"/rest/v1/system/nae_scripts/port_admin_state_monitor/nae_agents/port-1_1_1",
"/rest/v1/system/nae_scripts/port_admin_state_monitor/nae_agents/port-1_1_2"

n To get detailed information about all the agents on the switch, use the GET method and use

wildcards for the script name and agent name:

For example:

GET https://192.0.2.5/rest/v1/system/nae_scripts/*/nae_agents/*

Creating an agent from an existing script using the REST API
Instructions and examples in this document use an IP address that is reserved for documentation,
192.0.2.5, as an example of the IP address for the switch. To access your switch, you must use the IP
address or hostname of that switch.

Prerequisites

n You must be logged in to the switch REST API with a user name that has administrator rights.

n The switch REST API access mode must be read-write.

n The script you will use to create the agent must be in a VALIDATED state.

Procedure

1. Use the POST method on the URI of the nae_agents collection of the script. In the request body,

provide the required information in JSON format.

This example creates an agent with the following characteristics:

n The name of the agent is: com.myco.bgp_mon.Agent1

n The name of the script is: com.myco.bgp_mon

n The agent is created in a disabled state ("disabled":true).

n The threshold parameter of the script is set to the value 10.

POST https://192.0.2.5/rest/v1/system/nae_scripts/com.myco.bgp_mon/nae_
agents
{

"name": "com.myco.bgp_mon.Agent1",
"disabled":true,
"parameters_values":{

"threshold":"10"

}

}

n Agents must have a unique name. If an agent that has the same name exists, the request fails

with response code 400 and the message:
NAE agent <agent_name> exists already

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

48

n If you supply a parameter value that is not the expected type for that parameter, the request

fails with response code 400 and the message:
Value type mismatch for the parameter <parameter_name>

n If the JSON request body does not include a parameter, but the script defines a default value

for that parameter, the default value is used.

If the JSON request body does not include a parameter that is required by the script, and the
script does not define a default for that parameter, the agent is created, but the agent has the
following error message:

The NAE Agent has Python errors. Please check hpe-policyd logs for Python

errors.

Enabling an agent using the REST API
Instructions and examples in this document use an IP address that is reserved for documentation,
192.0.2.5, as an example of the IP address for the switch. To access your switch, you must use the IP
address or hostname of that switch.

Prerequisites

n You must be logged in to the switch REST API with a user name that has administrator rights.

n The switch REST API access mode must be read-write.

Procedure

n To enable the agent at the time the agent is created, set the disabled parameter to false when you

create the agent.

For example:

POST https://192.0.2.5/rest/v1/system/nae_scripts/com.myco.bgp_mon/nae_agents
{

"name": "com.myco.bgp_mon.Agent1",
"disabled":false,
"parameters_values":{

"threshold":"10"

}

}

n To enable an existing agent, use the PUT method to set the disabled parameter to false.

For example:

PUT https://192.0.2.5/rest/v1/system/nae_scripts/com.myco.bgp_mon/nae_
agents/com.myco.bgp_mon.Agent1
{

"disabled":false,
"parameters_values":{

"threshold":"10"

}

}

Disabling an agent using the REST API

Managing agents | 49

Instructions and examples in this document use an IP address that is reserved for documentation,
192.0.2.5, as an example of the IP address for the switch. To access your switch, you must use the IP
address or hostname of that switch.

Prerequisites

n You must be logged in to the switch REST API with a user name that has administrator rights.

n The switch REST API access mode must be read-write.

Procedure

To disable an agent, use the PUT method to set the disabled parameter to true.

For example:

PUT https://192.0.2.5/rest/v1/system/nae_scripts/com.myco.bgp_mon/nae_
agents/com.myco.bgp_mon.Agent1
{

"disabled":true

}

Changing the configuration of an agent using the REST API
Instructions and examples in this document use an IP address that is reserved for documentation,
192.0.2.5, as an example of the IP address for the switch. To access your switch, you must use the IP
address or hostname of that switch.

Prerequisites

n You must be logged in to the switch REST API with a user name that has administrator rights.

n The switch REST API access mode must be read-write.

Procedure

1. Disable the agent.

For example:

PUT https://192.0.2.5/rest/v1/system/nae_scripts/com.myco.bgp_mon/nae_
agents/com.myco.bgp_mon.Agent1
{

"disabled":true

}

2. Update and enable the agent by using the PUT method on the URI of the agent.

The PUT method replaces the agent specified by the URI. If the agent has multiple parameters in
parameters_values, any parameters that you do not specify in the PUT method are reset to their
default values. If you do not specify a value for a required parameter, and that parameter does
not have a default value, the agent configuration is changed, but the agent has the following error
message:

The NAE Agent has Python errors. Please check hpe-policyd logs for Python errors.

This example changes the value of the short-term high threshold for com.myco.bgp_mon.Agent1
to 22.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

50

PUT https://192.0.2.5/rest/v1/system/nae_scripts/com.myco.bgp_mon/nae_
agents/com.myco.bgp_mon.Agent1
{

"disabled":false,
"parameters_values":{

"short_term_high_threshold":"22"

}

}

Deleting an agent using the REST API
Instructions and examples in this document use an IP address that is reserved for documentation,
192.0.2.5, as an example of the IP address for the switch. To access your switch, you must use the IP
address or hostname of that switch.

Prerequisites

n You must be logged in to the switch REST API with a user name that has administrator rights.

n The switch REST API access mode must be read-write.

Procedure

To delete an agent, use the DELETE method on the URI of the agent.

You are not required to disable the agent before deleting it.

The following example deletes Agent1 of the script: com.myco.bgp_mon.
DELETE https://192.0.2.5/rest/v1/system/nae_scripts/com.myco.bgp_mon/nae_
agents/com.myco.bgp_mon.Agent1

Deleting a script also deletes all agents associated with that script.

Showing the Current and Maximum Number of Agents,
Monitors, and Scripts

Procedure

n To use the CLI, enter the show capacities-status nae command. For example:

switch# show capacities-status nae

System Capacities Status: Filter NAE
Value Maximum
Capacities Status Name
------------------------------------------------------------------------------
Number of configured NAE agents currently active in the system
Number of configured NAE monitors currently active in the system
Number of configured NAE scripts currently active in the system

25
50
12

1
7
1

For detailed information about the show capacities-status command, see the Command-Line Interface
Guide.

n To use the Web UI, on the Overview page, look at the Analytics panel to see the total number of

scripts, agents, and monitors compared to the total number supported on the switch.

Managing agents | 51

For example, Agents: 6/50 indicates that there are total of six enabled and disabled agents out of a
maximum of 50 agents supported on this switch.

n To use the REST API, do the following:

1. To get information about maximum number of scripts, agents, and monitors, send a GET

request to the /system resource, specifying the attributes=capacities query parameter. For
example:

GET /rest/v1/system/?attributes=capacities

The response body contains capacity information about multiple switch features. The
information about the Network Analytics Engine starts with the string: nae_

For example:

{

"capacities": {

...
...
"nae_agents": 50,
"nae_monitors": 150,
"nae_notification_handlers": 8,
"nae_notification_queue_size": 25000,
"nae_notifications_rate": 25000,
"nae_notifications_rate_per_monoitor": 500,
"nae_scripts": 25,
"nae_tsdb_disk_quota": 9,
...
...

}

}

{

"capacities": {

...
...
"nae_agents": 50,
"nae_monitors": 150,
"nae_notification_handlers": 8,
"nae_notification_queue_size": 25000,
"nae_notifications_rate": 25000,
"nae_notifications_rate_per_monoitor": 500,
"nae_scripts": 25,
"nae_tsdb_disk_quota": 9,
...

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

52

...

}

}

2. To get information about the current number of scripts, agents, and monitors, send a GET
request to the /system resource, specifying the attributes=capacities_status query
parameter. For example:

GET /rest/v1/system/?attributes=capacities_status

The response body contains information about multiple switch features. The information
about the Aruba Network Analytics Engine starts with the string: nae_

For example:

{

"capacities_status": {

...
...
"nae_agents": 6,
"nae_monitors": 27,
"nae_scripts": 7,
...
...

}

}

Agent status
Agents are either enabled or disabled.

An agent that is enabled can have the following status values:

CRITICAL

The agent has encountered a critical error during execution. For information about the error, see the
Analytics Dashboard of the Web UI.

MAJOR

The agent has encountered a major error during execution. For information about the error, see the
Analytics Dashboard of the Web UI.

MINOR

The agent has encountered a minor error during execution. For information about the error, see the
Analytics Dashboard of the Web UI.

NORMAL

Indicates that the agent is actively monitoring network conditions and handling events.

Behaviors when multiple agents monitor the same
resource

Managing agents | 53

A time series is a sequence of data points taken in successive equally spaced points in time.

A time series is associated with the monitored resource attribute, not the agent:

n Only one time series is created for that resource URI (including the attribute), regardless of how

many agents are monitoring the same resource.

n The time series remains in the time series database as long as there is at least one agent monitoring

that URI. The entire time series in the time series database is deleted only when all the agents
monitoring that URI are deleted.

If the agents have different conditions or threshold values, actions (such as alert generation) are taken
for each condition met, but the time series being used is the same for all agents. As a result, an agent
might evaluate conditions at the time it is enabled based on data that existed prior to that time, such as
if the condition aggregates data over time.

For example, consider the following scenario:

1. You create two agents, both of which are disabled:

n Agent A1 monitors CPU utilization.

n Agent A2 monitors CPU utilization and has an action to create an alert when the average over

the last 1 minute of CPU utilization is greater than 90%.

2. You enable agent A1, which starts monitoring CPU utilization.

3. The CPU utilization is above 90% for 5 minutes.

4. You enable agent A2.

5. Agent A2 creates an alert immediately—instead of after one minute—because the time series
already shows that the average of the previous minute of CPU utilization is greater than 90%.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

54

Chapter 7
|                 |             | Troubleshooting | agent  | and script | issues |
| --------------- | ----------- | --------------- | ------ | ---------- | ------ |
| Troubleshooting | agent and   | script issues   |        |            |        |
| Showing         | the current | and maximum     | number | of agents, |        |
| monitors,       | and scripts |                 |        |            |        |
Procedure
n TousetheCLI,entertheshow capacities-status naecommand.Forexample:
| switch#    | show capacities-status | nae        |     |               |     |
| ---------- | ---------------------- | ---------- | --- | ------------- | --- |
| System     | Capacities Status:     | Filter NAE |     |               |     |
| Capacities | Status Name            |            |     | Value Maximum |     |
------------------------------------------------------------------------------
Number of configured NAE agents currently active in the system 1 25
Number of configured NAE monitors currently active in the system 7 50
Number of configured NAE scripts currently active in the system 1 12
Fordetailedinformationabouttheshow capacities-statuscommand,seetheCommand-LineInterface
Guide.
TousetheWebUI,ontheOverviewpage,lookattheAnalyticspaneltoseethetotalnumberof
n
scripts,agents,andmonitorscomparedtothetotalnumbersupportedontheswitch.
Forexample,Agents: 6/50indicatesthattherearetotalofsixenabledanddisabledagentsoutofa
maximumof50agentssupportedonthisswitch.
n TousetheRESTAPI,dothefollowing:
1. Togetinformationaboutmaximumnumberofscripts,agents,andmonitors,sendaGET
requesttothe/systemresource,specifyingtheattributes=capacitiesqueryparameter.For
example:
GET /rest/v1/system/?attributes=capacities
Theresponsebodycontainscapacityinformationaboutmultipleswitchfeatures.The
informationabouttheNetworkAnalyticsEnginestartswiththestring:nae_
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000Switch
55
Series)

For example:

{

"capacities": {

...
...
"nae_agents": 50,
"nae_monitors": 150,
"nae_notification_handlers": 8,
"nae_notification_queue_size": 25000,
"nae_notifications_rate": 25000,
"nae_notifications_rate_per_monoitor": 500,
"nae_scripts": 25,
"nae_tsdb_disk_quota": 9,
...
...

}

}

{

"capacities": {

...
...
"nae_agents": 50,
"nae_monitors": 150,
"nae_notification_handlers": 8,
"nae_notification_queue_size": 25000,
"nae_notifications_rate": 25000,
"nae_notifications_rate_per_monoitor": 500,
"nae_scripts": 25,
"nae_tsdb_disk_quota": 9,
...
...

}

}

2. To get information about the current number of scripts, agents, and monitors, send a GET
request to the /system resource, specifying the attributes=capacities_status query
parameter. For example:

GET /rest/v1/system/?attributes=capacities_status

The response body contains information about multiple switch features. The information
about the Aruba Network Analytics Engine starts with the string: nae_

For example:

{

"capacities_status": {

...
...
"nae_agents": 6,
"nae_monitors": 27,
"nae_scripts": 7,
...
...

Troubleshooting agent and script issues | 56

}

}

High switch CPU and memory usage are affecting switch
performance

Symptom

A switch that has Network Analytics Engine (NAE) agents installed is experiencing high CPU usage, high
memory usage, or both, and overall performance is affected.

Cause

The NAE is attempting to monitor too many switch resources. For example, a script uses wildcard
characters in a URI to monitor all interfaces, ACLs, or VLANs, and the switch has hundreds or thousands
of those items.

Action

1. Verify that the resources associated with the NAE are consuming the memory and CPU resources

by entering the following commands in the switch CLI:
n show system resource-utilization daemon hpe-tsdbd

n show system resource-utilization daemon hpe-policyd

n show system resource-utilization daemon prometheus

The response to the show system resource-utilization daemon <daemon> command shows
the CPU and memory usage the specified daemon.

2.

Identify installed scripts that include the wildcard character (*) in the URIs of monitors.

For example, the following scripts written by Aruba contain wildcard characters to specify resources
that can exist in large numbers on a switch:

n tx_rx_stats_monitor

n fault_finder

In the Web UI, the Script Details page shows the contents of the script.

Look for monitor URIs that specify the wildcard character for resources that your switch has in large
numbers. For example:

n interfaces/*

n acls/*

n vlans/*

3. Delete agents associated with the scripts you identified.

Disabling the agent is not sufficient because the switch does not delete time series data when an
agent is disabled.

Downloading NAE support files
You can download support information specific to the Aruba Network Analytics Engine (NAE) as a file in
tar.gz format using TFTP, SFTP, or USB.

Procedure

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

57

From the CLI, use the copy support-files command and specify the NAE feature.

Example of copying NAE support files to a remote server using TFTP:

switch# copy support-files feature nae tftp://10.100.0.12/file.tar.gz vrf mgmt

Example of copying NAE support files to a remote server using SFTP:

switch# copy support-files feature nae sftp://root@10.0.14.206/file.tar.gz vrf
mgmt

Example of copying the NAE support files to a storage drive connected to the USB port of the switch:

switch# copy support-files feature nae usb:/file.tar.gz

For detailed information about the copy support-files command, see the Command-Line Interface
Guide.

NAE support file content

The Aruba Network Analytics Engine (NAE) support files include the following information:

n Configuration information about all the NAE agents and scripts

n All NAE scripts in the same format as when they are returned by the show running-config command

n The nae_alert.journal file, which contains the NAE alerts

n If your support specialist has executed commands to collect memory and CPU profile information
before the copy support-files command is executed, the following information is included:

o The memory and CPU profiles of the hpe-policyd daemon

o The memory and CPU profiles of the hpe-tsdbd daemon

Error: "Switch time and browser time are not in sync"

Symptom

The Web UI displays a yellow caution triangle in the top banner and an error dialog box with the
following title:
Switch time and browser time are not in sync

The content of the dialog box indicates how many seconds the switch time is ahead of or behind the
browser time, and states that the information displayed in the Web UI might not be accurate.

In addition, time series graphs on the Analytics page might be missing expected data, might have data
shown with inaccurate times, or might display incorrect data.

Cause

The switch and the client from which you are viewing the UI are not set to the same time. For example:

n The switch has been rebooted and the time has not been set correctly. For example, the switch could

not reach its configured NTP server.

n Instead of using Coordinated Universal Time (UTC) with a time zone offset or getting the time from

an NTP server, either the switch or the client is manually set to a different time.

Troubleshooting agent and script issues | 58

Action

n Try clearing or resetting the web client browser cache.

n Ensure that the web client from which you are viewing the Web UI is set to a time zone based on UTC.

For example, if your workstation is set to Eastern Standard Time (EST), and you want to use Pacific
Standard Time (PST), change the time by setting the time zone instead of by manually resetting the time.

n Ensure that the switch is set to use NTP or to a time zone based on UTC time.

o NTP synchronizes the time of day among a set of distributed time servers and clients to correlate
events when receiving system logs and other time-specific events from multiple network devices.
All NTP communications use Coordinated Universal Time (UTC). To show the NTP status, use the
show ntp status command.

o For information about configuring the switch to use NTP, see the Fundamentals Guide.

After you configure the switch, clear the NAE data by entering the clear nae-data command from the
manager context.

For example:

switch# clear nae-data

n If the switch is set to use NTP and there has been a significant clock change, clear the NAE data by

using the clear nae-data command.

For example:

switch# clear nae-data

Analytics time series graph displays message instead of
data: "Agent data not found, please verify..."

Symptom

The time series graph of a monitor displays the following message instead of graphed data:
Agent data not found, please verify that the agent has not be deleted

Cause

The switch operating system software was updated to a different software release, and the name of the
agent after the update is not an exact match to the name of the agent before the update.

For example:

n Before the software update, there was an Analytics time series graph for an agent with the following

name:

system_resource_monitor.1.1.default

n The same script for the new software has the name system_resource_monitor instead of the name

system_resource_monitor.1.1.

n After the software update:

o The name of the new agent is based on the new script name. The new agent name is the

following:

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

59

system_resource_monitor.default

o The Web UI continues to display the Analytics graph of the older agent, system_resource_

monitor.1.1.default, which has no data and displays the error message.

Action

1. Close the panel that is displaying the error message.

2.

If there is no Analytics time series graph displayed with the new agent name, add the panel by
clicking the + plus sign next to the agent in the Agents panel.

Inaccurate or no data displayed in analytics time series
graph

Symptom

The time series graph of a monitor is missing expected data, has data shown with inaccurate times, or
incorrect data.

For example, a chart that graphs when a port goes down shows a port as up when it is down, does not
show any state for the port, or shows the event as happening at a time that does not match the actual
event--such as in future.

Solution 1

Cause

The switch and the client from which you are viewing the UI are not set to the same time. For example,
instead of using Coordinated Universal Time (UTC) with a time zone offset or getting the time from an
NTP server, either the switch or the client is manually set to a different time.

Action

n Try clearing or resetting the web client browser cache.

n Ensure that the web client from which you are viewing Web UI is set to a time zone based on UTC.
For example, if your workstation is set to Eastern Standard Time (EST), and you want to use Pacific
Standard Time (PST), change the time by setting the time zone instead of by manually resetting the
time.

n Ensure that the switch is set to use NTP or to a time zone based on UTC time.

o NTP synchronizes the time of day among a set of distributed time servers and clients to correlate
events when receiving system logs and other time-specific events from multiple network devices.
All NTP communications use Coordinated Universal Time (UTC).

To show the NTP status, use the show ntp status command.

o For information about configuring the switch to use NTP, see the Fundamentals Guide.

After you configure the switch, clear the NAE data by entering the clear nae-data command from the
manager context.

For example:

switch# clear nae-data

Troubleshooting agent and script issues | 60

n If the switch is set to use NTP and there has been a significant clock change, clear the NAE data by

using the clear nae-data command.

For example:

switch# clear nae-data

Solution 2

Cause

The switch operating system software was updated to a different software release.

Action

1. Clear the NAE data by entering the clear nae-data command from the manager context.

For example:

switch# clear nae-data

2. Examine the alerts for agent or script errors.

Ensure that the scripts loaded on the switch support the software release installed on the switch.

3.

If a script does not support the current software release, delete the script and upload the
replacement script.

4. After you upload replacement scripts, clear the NAE data again by entering the clear nae-data

command from the manager context.

URI errors
Agents can encounter errors not related to script syntax. For example:

n The agent attempts to monitor a port that exists on the switch but is not up.

n The agent attempts to monitor a port that does not exist on this switch.

n The agent attempts to monitor a LAG that has not been configured.

n The specified attribute is not correct for the resource. For example, the query string of the resource

URI specifies nx_packets instead of rx_packets.

LAGs and ports are examples of switch resources. Every switch resource is identified by a URI (Universal
Resource Identifier), so the kinds of errors listed previously are a category of errors called URI errors.

Error: "The NAE Agent is not created...DB constraint
violation errors"

Symptom

When you attempt to create an agent, the agent appears in the Agents panel with a red triangle error
symbol and status of Unknown. The error message is the following:

The NAE Agent is not created. Please check hpe-policd logs for DB constraint violation
errors.

Cause

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

61

Attempting to create the agent resulted in creating more monitors than the NAE supports on the switch.

Action

1. Delete the agent that has the error.

2. To view the maximum number of monitors supported on the switch, see the Analytics panel on

the Overview page of the Web UI.

In the following example, the Analytics panel does not display an agent error because the agent
was not created. However, the Analytics panel does show that the number of monitors exceeds
the maximum number of 150.

3. Reduce the number of monitors by identifying and deleting other agents.

Disabling an agent is not sufficient. The switch does not reduce the count of monitors used when
agents are disabled.

4. Create the agents you want to use.

Error: "The NAE Agent has Python errors."

Symptom

An agent has the following error:
The NAE Agent has Python errors. Please check hpe-policyd logs for Python errors.

Solution 1

Cause

When the agent was created, the user supplied an invalid value for a required parameter.

Action

Change the configuration of the agent to include a valid value for the parameter.

Solution 2

Cause

The agent has an error that was not caused by an invalid required parameter.

For example, the value provided for an optional parameter might have caused a processing error.

Action

Examine the log files for the hpe-policyd daemon to identify which Python errors occurred, and take
corrective action.

Error: "Timeseries data cannot be generated...The URI is
invalid or not configured"

Symptom

Troubleshooting agent and script issues | 62

Anagentisinanerrorstateandisnotcollectingdataforoneofitsmonitoredresources.
TheAgentErrormessageisthefollowing:
| Timeseries    | data cannot  | be     | generated     | due to       |        |
| ------------- | ------------ | ------ | ------------- | ------------ | ------ |
| the following | agent        | error: | The URI       | is invalid   | or not |
| configured.   | Either       | please | upload        | a new script | with a |
| valid URI,    | or configure |        | the resource, | disable the  |        |
| instance,     | and enable   | again: | <uri>         |              |        |
Inthemessage,<uri>istheresourcethatisinvalidornotconfigured.Forexample:
/rest/v1/system/bridge/vlans/*/macs?count
| Solution | 1   |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
Cause
IftheresourceURIissupportedonthisswitchandoperatingsystemversion,themostlikelyreasonfor
theerroristhattheswitchresource—suchasaport—isnotinanUPstate.
Action
1. Resolvetheproblemthatiscausingtheresourcetobeunavailable.
Forexample,ifaportisadministrativelydown,bringtheporttoanUPstate.
2. Disabletheagent.
3. Enabletheagent.
| Solution | 2   |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
Cause
TheagentusesaresourceIDfromauser-suppliedparameter,andtheusersuppliedaresourceIDthat
isinvalid(suchasaportthatdoesnotexist).
Action
1. Deletetheagent.
2. CreateandenableanagentthatspecifiesavalidresourceID(suchasportnumber).
| Solution | 3   |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
Cause
TheresourceURIisnotauser-suppliedparameter,andisnotsupportedonthisswitchandsoftware
version.
Forexample,aURIthatincludes/bridgeinthepathisnotvalidon10.03andlaterversions.
Action
n IfthescriptwasdownloadedfromtheArubaSolutionsExchange(ASE),replaceorupdatethescript
withascriptthatsupportsthesoftwareversionrunningontheswitch.
1. Ifthescriptwasloadedonaswitchrunningversion10.03orlaterandthescriptnamematches
thenewscriptname,youcanusetheupdateprocesstoreplacethescript.
2. Ifthescriptwasloadedwhiletheswitchwasrunningaversionearlierthan10.03,youmust
deletetheexistingscript,uploadthenewscript,andcreatenewagents.
n IfthescriptnotascriptdownloadedfromtheASE,dothefollowing:
| 1.  | Deleteallagentsassociatedwiththescript. |     |     |     |     |
| --- | --------------------------------------- | --- | --- | --- | --- |
Considerrecordinginformationabouttheagentnamesandparametervaluessothatyoucan
createequivalentagentsfromthemodifiedscript.
63
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

2. ModifythescripttospecifyonlyURIsthatarevalidforthisswitchandoperatingsystem
version.
| 3.     | Replacethescriptontheswitchwiththemodifiedscript. |        |             |     |     |
| ------ | ------------------------------------------------- | ------ | ----------- | --- | --- |
| 4.     | Createagentsfromthemodifiedscript.                |        |             |     |     |
| 5.     | Enablethenewagents.                               |        |             |     |     |
| Error: | "The script                                       | syntax | is invalid" |     |     |
Symptom
Scriptvalidationfailswiththeerror:The
|     |     |     | script syntax | is invalid |     |
| --- | --- | --- | ------------- | ---------- | --- |
Cause
Duringthevalidationprocess,asyntaxerrorwasdetectedinthescriptPythoncode.
Action
1. Modifythescripttocorrectthesyntaxerrors.
2. Replacethescriptontheswitchwiththemodifiedscript.
| Error: | "The script | agent | syntax | is invalid" |     |
| ------ | ----------- | ----- | ------ | ----------- | --- |
Symptom
Agentcreationfailswiththeerror:The script agent syntax is invalid
Cause
Intheagentcreationrequest,onethefollowingoccurred:
n Thecreationrequestspecifiedascriptnamethatdoesnotmatchanyscriptinstalledontheswitch.
n Aparametervaluewasusedthatdoesnotmatchthesyntaxortypeoftheparameterdefinedbythe
script.
Action
Modifytheagentcreationrequest.
| Error: | "Sandbox | timed | out while | running | script" |
| ------ | -------- | ----- | --------- | ------- | ------- |
Symptom
Anagentisinanerrorstateandisnotcollectingdata.IntheWebUI,theAgent Detailspagedisplays
theerror:
| Sandbox  | timed out while | running | script |     |     |
| -------- | --------------- | ------- | ------ | --- | --- |
| Solution | 1               |         |        |     |     |
Cause
Theswitchisoperatingunderaheavyload.
Action
Troubleshootingagentandscriptissues|64

1. Iftheagentisnotalreadydisabled,disabletheagent.
2. Whentheoperatingloadfortheswitchreturnstonormal,enabletheagent.
| Solution | 2   |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
Cause
Thescriptthathasmanymonitorsandfunctionsorexecutesloopsthattakealongtime.
Action
1. Modifythescripttocorrectthedesignissues,suchasreplacingalargerscriptwithseveral
smallerscripts.
a. Deleteallagentsassociatedwiththescript.Considerrecordinginformationabouttheagent
namesandparametervaluessothatyoucancreateequivalentagentsfromthemodified
script.
|        | b. Modifythescript.                                  |              |     |         |           |      |
| ------ | ---------------------------------------------------- | ------------ | --- | ------- | --------- | ---- |
|        | c. Replacethescriptontheswitchwiththemodifiedscript. |              |     |         |           |      |
|        | d. Createagentsfromthemodifiedscript.                |              |     |         |           |      |
|        | e. Enablethenewagents.                               |              |     |         |           |      |
| Error: | "The agent                                           | instantiated |     | sandbox | has timed | out" |
Symptom
Anagentisinanerrorstateandisnotcollectingdata.IntheWebUI,theAgent Detailspagedisplays
theerror:
| The agent | instantiated | sandbox has | timed out |     |     |     |
| --------- | ------------ | ----------- | --------- | --- | --- | --- |
| Solution  | 1            |             |           |     |     |     |
Cause
Theswitchisoperatingunderaheavyload.
Action
1. Iftheagentisnotalreadydisabled,disabletheagent.
2. Whentheoperatingloadfortheswitchreturnstonormal,enabletheagent.
| Solution | 2   |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
Cause
Thescripthasmanymonitorsandfunctionsorexecutesloopsthattakealongtime.
Action
1. Modifythescripttocorrectthedesignissues,suchasreplacingalargerscriptwithseveral
smallerscripts.
|     | a. Deleteallagentsassociatedwiththescript. |     |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- |
Considerrecordinginformationabouttheagentnamesandparametervaluessothatyou
cancreateequivalentagentsfromthemodifiedscript.
|     | b. Modifythescript.                                  |     |     |     |     |     |
| --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
|     | c. Replacethescriptontheswitchwiththemodifiedscript. |     |     |     |     |     |
|     | d. Createagentsfromthemodifiedscript.                |     |     |     |     |     |
|     | e. Enablethenewagents.                               |     |     |     |     |     |
65
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

| Error: | "Unable | to parse | condition | expression..." |
| ------ | ------- | -------- | --------- | -------------- |
Symptom
Time-seriesdataforthemonitoredresourceisbeingcollected,butnoalertsaretriggeredforthe
condition.IntheWebUI,theAgent Detailspagedisplaysthefollowingerror:
Unable to parse condition expression, invalid condition syntax <condition>
<condition>istheconditionexpressionthathastheerror.
Forexample:
Unable to parse condition expression, invalid condition syntax: rate
/rest/v1/system/interfaces/*?attributes=link_resets per and 10 seconds > 1
Inaddition,theswitcheventlogsmightcontainerrorsrelatedtotherulethatcontainsthecondition.
Youcanentertheshow event -d hpe-policydcommandtodisplayeventsrelatedtotheAruba
NetworkAnalyticsEnginescripts.
Forexample:
| switch# | show event | -d hpe-policyd |     |     |
| ------- | ---------- | -------------- | --- | --- |
2018-0one-09:09:21:49.906768|hpe-policyd|5504|LOG_ERR|AMM|-|Error executing NAE
action CLI belonging to condition system_resource_monitor.1.0.default.condition_7
and agent system_resource_monitor.default due to Command failed: non-zero
| exit | status. |     |     |     |
| ---- | ------- | --- | --- | --- |
Cause
Thecauseisoneofthefollowing:
n Thereisasyntaxerrorintheconditionexpression.
Conditionexpressionscanincludeoperators,functions,andkeywords—allofwhichmustbeinthe
requiredsequence.Forexample:
| o Correctsyntax:r.condition('{} |     |     | > {}', [value,threshold]) |     |
| ------------------------------- | --- | --- | ------------------------- | --- |
o
| Incorrectsyntax:r.condition('> |     |     | {} {}', [value,threshold]) |     |
| ------------------------------ | --- | --- | -------------------------- | --- |
n Thereisamismatchbetweenthenumberofparameterspassedtotheconditionexpressionandthe
numberofparametersexpected.
Forexample,thefollowingexpressionexpectstwoinputsbutisonlypassedoneinput:
| r.condition('{} | >   | {}', [value]) |     |     |
| --------------- | --- | ------------- | --- | --- |
Whentheinputstoafunctionareastringandanarray,thePythoninterpreterdoesnotdetect
mismatchesinparametersandvalues.Forexample,accordingtothePythoninterpreter,theexpression
r.condition('>', [])couldbevalid,soitdoesnotreturnasyntaxerrorduringscriptvalidation.
Howeverwhenthescriptisrun,theexpressionhasnomeaningbecausethecomparatorhasnovalues
tocompare,sothe"Unabletoparseconditionexpression..."errorisreturned.
Action
1. Modifythescripttocorrecttheconditionexpression:
|     | a. Deleteallagentsassociatedwiththescript. |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- |
Considerrecordinginformationabouttheagentnamesandparametervaluessothatyou
cancreateequivalentagentsfromthemodifiedscript.
|     | b. Modifythescript.                                  |     |     |     |
| --- | ---------------------------------------------------- | --- | --- | --- |
|     | c. Replacethescriptontheswitchwiththemodifiedscript. |     |     |     |
Troubleshootingagentandscriptissues|66

|        | d. Createagentsfromthemodifiedscript. |     |         |     |             |     |
| ------ | ------------------------------------- | --- | ------- | --- | ----------- | --- |
|        | e. Enablethenewagents.                |     |         |     |             |     |
| Error: | "The                                  | CLI | command |     | is invalid" |     |
Symptom
AnagentisinanerrorstateandisnotsuccessfullyexecutingaCLIcommandspecifiedinthescript.The
scripthasthefollowingerror:
| The CLI | command | is  | invalid |     |     |     |
| ------- | ------- | --- | ------- | --- | --- | --- |
Cause
AscriptactionspecifiesaCLIcommandthatisnotvalidonthisswitchandsoftwareversion.
Action
1. DeterminewhichCLIcommandisinvalid.Toseewhichcommandfailed,intheWebUI,youcan
viewtheAction ResultsectionoftheAlert Detailsscreenofthealertthatgeneratedthiserror.
Youcansearchforthefollowingerrorintheeventlog:
| NAE | Action | CLI | command | <command> | is not supported |     |
| --- | ------ | --- | ------- | --------- | ---------------- | --- |
<command>isthenameoftheunsupportedcommand.
Forexample:
| NAE | Action | CLI | command | datetime | is not supported |     |
| --- | ------ | --- | ------- | -------- | ---------------- | --- |
2. ModifythescripttochangetheCLIcommandorremovethescriptactionthatcontainsthe
command.
|     | a. Deleteallagentsassociatedwiththescript. |     |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- |
Considerrecordinginformationabouttheagentnamesandparametervaluessothatyou
cancreateequivalentagentsfromthemodifiedscript.
|        | b. Modifythescript.                                  |     |     |         |          |              |
| ------ | ---------------------------------------------------- | --- | --- | ------- | -------- | ------------ |
|        | c. Replacethescriptontheswitchwiththemodifiedscript. |     |     |         |          |              |
|        | d. Createagentsfromthemodifiedscript.                |     |     |         |          |              |
|        | e. Enablethenewagents.                               |     |     |         |          |              |
| Error: | "Command                                             |     |     | failed: | non-zero | exit status" |
Symptom
AnagentisinanerrorstateandisnotsuccessfullyexecutingaCLIcommandspecifiedinthescript,and
thefollowingconditionsaretrue:
n Theagenthasthefollowingerror:
| Command | failed: | non-zero |     | exit status |     |     |
| ------- | ------- | -------- | --- | ----------- | --- | --- |
n IntheAction Result Outputdialogbox,theoutputoftheCLIcommandisthefollowing:
| Cannot | execute | command. | Command | not | allowed. |     |
| ------ | ------- | -------- | ------- | --- | -------- | --- |
n Theswitchisconfiguredtousearemoteauthenticationandauthorizationservice,suchasTACACS+.
Cause
NetworkAnalyticsEngine(NAE)scriptsexecuteCLIcommandsastheadminuser,anddonotattemptto
authenticatebeforeexecutingtheCLIcommand.Theremoteauthenticationandauthorizationserviceis
notallowingtheadminusertoexecutecommandswithoutpriorauthentication.
67
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

Action
Configuretheremoteauthenticationandauthorizationservicetoallowauthorizationwithout
authenticationfortheadminuser.
| Error: | "The action | is invalid" |     |     |     |
| ------ | ----------- | ----------- | --- | --- | --- |
Symptom
Anagentisinanerrorstateandisnotsuccessfullyexecutinganactionspecifiedinthescript.Thescript
hasthefollowingerror:
| The action | is invalid |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- |
Cause
AscriptactionspecifiesanactionthatisnotaCLIcommandandisnotvalidonthisswitchandsoftware
version.
Action
1. Determinewhichscriptactionisinvalid.
Toseewhichcommandoractionfailed,intheWebUI,viewtheAction Resultsectionofthe
| Alert | Detailsscreenofthealertthatgeneratedthiserror. |     |     |     |     |
| ----- | ---------------------------------------------- | --- | --- | --- | --- |
2. Modifythescripttochangeorremovethescriptactionthatcontainsthecommand.
|     | a. Deleteallagentsassociatedwiththescript. |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- |
Considerrecordinginformationabouttheagentnamesandparametervaluessothatyou
cancreateequivalentagentsfromthemodifiedscript.
|             | b. Modifythescript.                   |        |                |             |        |
| ----------- | ------------------------------------- | ------ | -------------- | ----------- | ------ |
|             | c. Uploadthemodifiedscript.           |        |                |             |        |
|             | d. Createagentsfromthemodifiedscript. |        |                |             |        |
|             | e. Enablethenewagents.                |        |                |             |        |
| ActionShell | output                                | error: | "not available | in enhanced | secure |
mode"
Symptom
IntheWebUI,analerthasanAlert DetailsdialogboxthatshowsanActionShellcommandthathasa
resultofERROR.TheAction Result Outputdialogboxforthatcommandincludesthefollowingerror:
| not available | in enhanced | secure mode |     |     |     |
| ------------- | ----------- | ----------- | --- | --- | --- |
Thescriptandtheagentarenotinanerrorstate.
Cause
Theswitchisconfiguredinenhancedsecuremode.
Action
Dooneofthefollowing:
n Ignoretheerror.Theenhancedsecuremodeoftheswitchdeniesaccesstoshellcommandsby
design.
Troubleshootingagentandscriptissues|68

n Change the configuration of the switch from enhanced secure mode to standard mode. For more

information about enhanced secure mode, see the Security Guide.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

69

Using the Aruba Solutions Exchange
(ASE)

Chapter 8

Using the Aruba Solutions Exchange (ASE)

Finding NAE scripts on the ASE website
No login is required to browse the website or view information about a script. To download a script or to
view the source code from the website, you must be logged in. Alternatively, you can download scripts
from the Web UI without logging in to the ASE.

Prerequisites

You must have access to the Aruba Solutions Exchange (ASE) website at:

https://ase.arubanetworks.com/

Procedure

1. On the top toolbar, select SOLUTIONS.

2.

In the navigation pane, under PRODUCTS, select NAE.

3. To filter the list by additional criteria, select one or more tags under TAGS. For example:

n To view Aruba certified NAE solutions, select the tag: nae-aruba-certified

n To view solutions that are related to ports, select the tag: port

n To view solutions that apply to your switch series, select the tag that contains the product

number, for example: 8400x

Filtering on multiple tags is treated as an OR operation. Solutions are displayed if they have any
one of the selected tags.

Finding NAE scripts on the ASE using the Web UI

Prerequisites

You must be logged in to the AOS-CX Web UI.

Procedure

1. Select Analytics from the navigation pane.

2.

In the Analytics Dashboard, in the Scripts panel, click the
download scripts from the Aruba Solution Exchange (ASE). From the Web UI, only Aruba-certified
scripts are listed. For other scripts, go to the ASE directly.

ASE download button to view and

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

70

YoucanalsoaccesstheArubaSolutionExchangefromtheScriptManagementpagewhereyou
| selectthe |     | button. |     |     |     |     |
| --------- | --- | ------- | --- | --- | --- | --- |
3. TheArubaSolutionExchangepageisdisplayed,listingtheavailablescripts.Youcanselectascript
| andclickView | Scripttoseetheprogrammaticscriptcontents. |         |             |               |     |     |
| ------------ | ----------------------------------------- | ------- | ----------- | ------------- | --- | --- |
| Viewing      | recent                                    | changes | to existing | NAE solutions |     |     |
Nologinisrequiredtobrowsethewebsiteorviewinformationaboutascript.Todownloadascriptor
toviewthesourcecodefromthewebsite,youmustbeloggedin.Alternatively,youcandownload
scriptsfromtheWebUIwithoutloggingintotheASE.
Prerequisites
YoumusthaveaccesstotheArubaSolutionsExchange(ASE)websiteat:
https://ase.arubanetworks.com/
Procedure
1. Selectthesolution.
2. Onthesolutiondetailspage,viewtherecentchangesintheRecent Changesbox.Youcanview
| additionalchangeinformationbyclickingMore |     |               | Details. |          |           |     |
| ----------------------------------------- | --- | ------------- | -------- | -------- | --------- | --- |
| Downloading                               |     | or installing | a script | from the | ASE using | the |
Web UI
ThisproceduredownloadsanNAEscriptfromtheASEtothespecifiedlocation.
UsingtheArubaSolutionsExchange(ASE)|71

Prerequisites

You must be logged in to the AOS-CX Web UI. Administrator rights are required to install a script, but not
required to download a script to your local system.

Procedure

1. Select Analytics from the navigation pane.

2.

In the Analytics Dashboard, in the Scripts panel, click the
ASE download button to view and
download scripts from the Aruba Solution Exchange (ASE). You can also access the Aruba Solution

Exchange from the Script Management page where you select the

button.

3. The Aruba Solution Exchange page is displayed, listing the available scripts.

4. Select an installed script you want to download and click Download. If the script has not yet been

installed, see the next step to install it.

You are prompted to either open the file or save the file to the location you select.

Saving will overwrite any existing file in the specified location with the same name.

Click OK or Cancel.

5.

If the script has not yet been installed on the switch, you can select Install instead of Download.

In the message dialog box, click Confirm to install the script or Cancel.

Downloading a solution from the ASE website to your
workstation
Use this procedure when you want to download a solution to your workstation from the ASE website
before you upload the script to a switch. Alternatively you can download a script directly to your switch
from the Web UI.

Prerequisites

You must be logged in to the Aruba Solutions Exchange (ASE).

Procedure

1. On the ASE, search or browse for the solution you want to use.

2.

In the DETAILS column, click the title of the solution.

The detailed information about the solution is displayed.

3. Verify that the displayed solution is the solution you want to download.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

72

The Description shows information about the solution, including software required and
platforms supported.

4. Click Finish.

5.

In the dialog box, select CONFIG.

6. Do one of the following:

n To download the solution, click Download.

n To receive the solution as an email attachment, click Email Me.

The email is sent to the email address associated with the account you used to log in to the ASE.

n To send the solution to as an attachment to an email address other than the email address

associated with the account you used to log in to the ASE, enter the email address in the Email
address text box and click Forward.

7. Click Close.

Using the Aruba Solutions Exchange (ASE) | 73

NAE scripts repository on GitHub

Chapter 9

NAE scripts repository on GitHub

Aruba publishes Aruba Network Analytics Engine scripts and examples to the following GitHub
repository:

https://github.com/aruba/nae-scripts

You can use this repository like any other GitHub repository:

n You can fork and clone the repository into your own account profile.

n You can explore the scripts (in the agents folder) and examples and use them to create your own

customized scripts.

n You can use the pull-request process to propose any additions or changes to the scripts.

The scripts and examples are organized by feature or protocol and then by supported platform. For
more information about the structure and use of this repository, see the README.md file in the repository.

For more information about using GitHub, see:

https://help.github.com/

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

74

Chapter 10

Scripts and security

Scripts and security

Aruba-certified scripts have been written and tested by Aruba. However, it is a good practice to examine
all scripts before you upload them to understand what actions agents created from them will take on
your switch.

It is also a good practice to save a switch checkpoint before you create and enable an agent for first time
so that you can recover the switch configuration if an agent performs an undesirable action.

Reading the description of the script in the ASE or readme file on the GitHub repository can give you a
good idea about what the script is intended to do, but to know what actions a script will take requires
examining the Python code. Look for text phrases such as the following (the lack of closing parentheses
in the search string is intentional):

n action("CLI"

n ActionCLI

n action("SHELL"

n ActionShell

n requests.

Action CLI functions that execute a switch CLI command. The command is provided as an argument to
that function. Commands that include the text config or configure can be an indicator that the function
is changing the configuration of the switch.

Action SHELL functions execute a command in the underlying operating system of the switch. The
command is provided as an argument to that function.

Functions that begin with the text requests. can be REST API requests that use the requests library to
make POST, PUT, or DELETE messages to the switch or to other network locations.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

75

Chapter 11

Scripts

Scripts

Python version and library support

Python version

The Aruba Network Analytics Engine supports scripts written in Python 3.5.X.

Python modules available

In addition to the standard Python libraries, the following Python modules are provided with the Aruba
Network Analytics Engine:

python3-misc

Usage example:
import os

For more information, see:

https://docs.python.org/3.5/library/os.html#miscellaneous-system-information

python3-pkgutil

Usage example:
from pkgutil import extend_path
...
__path__ = extend_path(__path__, __name__)
...

For more information, see:

https://docs.python.org/3.5/library/pkgutil.html

python3-importlib

Usage example:
import importlib

For more information, see:

https://docs.python.org/3.5/library/importlib.html

python3-datetime

Usage example:
import datetime

For more information, see:

https://docs.python.org/3.5/library/datetime.html

python3-enum

Usage example:

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

76

from enum import Enum
...
class Color(Enum):
...
...
...
...

red = 1
green = 2
blue = 3

For more information, see:

https://docs.python.org/3.5/library/enum.html

python3-compression

Usage examples:
import zlib
import gzip
import bz2
import lzma
import zipfile
import tarfile

For more information, see:

https://docs.python.org/3.5/library/archiving.html

python3-numbers

Usage example:
import numbers

For more information, see:

https://docs.python.org/3.5/library/numbers.html

python3-selectors

Usage example:
import selectors

For more information, see:

https://docs.python.org/3.5/library/selectors.html

python3-signal

Usage example:
import signal
...
# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)
...

For more information, see:

https://docs.python.org/3.5/library/signal.html

tar

Usage example:
import tarfile
...
tar = tarfile.open("sample.tar.gz")
tar.extractall()
tar.close()
...

For more information, see:

Scripts | 77

https://docs.python.org/3/library/tarfile.html

Third-party Python libraries available

The following third-party Python libraries are provided with the Aruba Network Analytics Engine
framework. To use the library in a script, import the library.

requests

The requests library is an HTTP library for Python.

Usage example:
import requests
...
r = requests.get('https://api.github.com/events')
r.json()
...

In a Python NAE script, when you specify the URI of a local switch resource, do not specify the external
IP address or host name. Instead, use the HTTP_ADDRESS global constant.

For example, instead of the following:
LOCAL_SYSTEM = '127.0.0.1:5577'
uri = 'http://' + LOCAL_SYSTEM + '/rest/v1/system/ports/1%2F1%2F5?attributes=link_state'

Specify the following:
uri = HTTP_ADDRESS + '/rest/v1/system/ports/1%2F1%2F5?attributes=link_state'

For more information about the requests library, see:

http://docs.python-requests.org/en/master/

jsondiff

The jsondiff library is an MIT-licensed Python library used for comparing and patching JSON and JSON-
like structures in Python.

Usage example:
import jsondiff
...
diff({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

For more information, see:

https://github.com/ZoomerAnalytics/jsondiff

REST API version support
Network Analytics Engine (NAE) scripts can monitor REST v1 resources only.

Rules for script files

n Format: If you upload script using the REST API, you must convert the file to base64-encoding. If you

upload the script using the Web UI, the conversion is done automatically.

n For information about coding style, naming conventions, and other best practices, see the style guide

for Python code (PEP 8).

Script example

Script file port_admin_state_monitor.1.0.py

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

78

#-*- coding: utf-8 -*-
#
#Copyright (c) 2017 Hewlett Packard Enterprise Development LP
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing,
#software distributed under the License is distributed on an
#"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#KIND, either express or implied. See the License for the
#specific language governing permissions and limitations
#under the License.

Manifest = {

'Name': 'port_admin_state_monitor',
'Description': 'Port Admin Status Monitoring Agent',
'Version': '1.0',
'Author': 'Aruba Networks'

}

ParameterDefinitions = {

'port_id': {

'Name': 'Port Id',
'Description': 'Port to be monitored',
'Type': 'string',
'Default': '1/1/1'

}

}

class Policy(NAE):

def __init__(self):

#Port status

uri1 = '/rest/v1/system/ports/{}?attributes=admin'
self.m1 = Monitor(

uri1,
'Port admin status',
[self.params['port_id']])

self.r1 = Rule('Port disabled administratively')
self.r1.condition('transition {} from "up" to "down"', [self.m1])
self.r1.action(self.action_port_down)

#Reset policy status when port is up

self.r2 = Rule('Port enabled administratively')
self.r2.condition('transition {} from "down" to "up"', [self.m1])
self.r2.action(self.action_port_up)

def action_port_down(self, event):

ActionSyslog(

'Port {} is disabled administratively',
[self.params['port_id']])

ActionCLI("show lldp configuration {}", [self.params['port_id']])
ActionCLI("show interface {} extended", [self.params['port_id']])
if self.get_alert_level() != AlertLevel.CRITICAL:
self.set_alert_level(AlertLevel.CRITICAL)

self.logger.debug("### Critical Callback executed")

def action_port_up(self, event):

self.logger.info("Current alert level: " + str(self.get_alert_level()))
if self.get_alert_level() is not None:

ActionSyslog(

Scripts | 79

'Port {} is enabled administratively',
[self.params['port_id']])

self.remove_alert_level()
self.logger.debug('Unset the previous status')

self.logger.debug('### Normal Callback executed')

Script in base64 encoded format

Iy0qLSBjb2Rpbmc6IHV0Zi04IC0qLQ0KIw0KI0NvcHlyaWdodCAoYykgMjAxNyBIZXdsZXR0IFBhY2thcmQgRW50Z
XJwcmlzZSBEZXZlbG9wbWVudCBMUA0KIw0KI0xpY2Vuc2VkIHVuZGVyIHRoZSBBcGFjaGUgTGljZW5zZSwgVmVyc2
lvbiAyLjAgKHRoZSAiTGljZW5zZSIpOw0KI3lvdSBtYXkgbm90IHVzZSB0aGlzIGZpbGUgZXhjZXB0IGluIGNvbXB
saWFuY2Ugd2l0aCB0aGUgTGljZW5zZS4NCiNZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQN
CiMNCiNodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjANCiMNCiNVbmxlc3MgcmVxdWlyZ
WQgYnkgYXBwbGljYWJsZSBsYXcgb3IgYWdyZWVkIHRvIGluIHdyaXRpbmcsDQojc29mdHdhcmUgZGlzdHJpYnV0ZW
QgdW5kZXIgdGhlIExpY2Vuc2UgaXMgZGlzdHJpYnV0ZWQgb24gYW4NCiMiQVMgSVMiIEJBU0lTLCBXSVRIT1VUIFd
BUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkNCiNLSU5ELCBlaXRoZXIgZXhwcmVzcyBvciBpbXBsaWVkLiBT
ZWUgdGhlIExpY2Vuc2UgZm9yIHRoZQ0KI3NwZWNpZmljIGxhbmd1YWdlIGdvdmVybmluZyBwZXJtaXNzaW9ucyBhb
mQgbGltaXRhdGlvbnMNCiN1bmRlciB0aGUgTGljZW5zZS4NCg0KTWFuaWZlc3QgPSB7DQogICAgJ05hbWUnOiAncG
9ydF9hZG1pbl9zdGF0ZV9tb25pdG9yJywNCiAgICAnRGVzY3JpcHRpb24nOiAnUG9ydCBBZG1pbiBTdGF0dXMgTW9
uaXRvcmluZyBBZ2VudCcsDQogICAgJ1ZlcnNpb24nOiAnMS4wJywNCiAgICAnQXV0aG9yJzogJ0FydWJhIE5ldHdv
cmtzJw0KfQ0KDQpQYXJhbWV0ZXJEZWZpbml0aW9ucyA9IHsNCiAgICAncG9ydF9pZCc6IHsNCiAgICAgICAgJ05hb
WUnOiAnUG9ydCBJZCcsDQogICAgICAgICdEZXNjcmlwdGlvbic6ICdQb3J0IHRvIGJlIG1vbml0b3JlZCcsDQogIC
AgICAgICdUeXBlJzogJ3N0cmluZycsDQogICAgICAgICdEZWZhdWx0JzogJzEvMS8xJw0KICAgIH0NCn0NCg0KY2x
hc3MgUG9saWN5KE5BRSk6DQoNCiAgICBkZWYgX19pbml0X18oc2VsZik6DQoNCiNQb3J0IHN0YXR1cw0KICAgICAg
ICB1cmkxID0gJy9yZXN0L3YxL3N5c3RlbS9wb3J0cy97fT9hdHRyaWJ1dGVzPWFkbWluJw0KICAgICAgICBzZWxmL
m0xID0gTW9uaXRvcigNCiAgICAgICAgICAgIHVyaTEsDQogICAgICAgICAgICAnUG9ydCBhZG1pbiBzdGF0dXMnLA
0KICAgICAgICAgICAgW3NlbGYucGFyYW1zWydwb3J0X2lkJ11dKQ0KICAgICAgICBzZWxmLnIxID0gUnVsZSgnUG9
ydCBkaXNhYmxlZCBhZG1pbmlzdHJhdGl2ZWx5JykNCiAgICAgICAgc2VsZi5yMS5jb25kaXRpb24oJ3RyYW5zaXRp
b24ge30gZnJvbSAidXAiIHRvICJkb3duIicsIFtzZWxmLm0xXSkNCiAgICAgICAgc2VsZi5yMS5hY3Rpb24oc2VsZ
i5hY3Rpb25fcG9ydF9kb3duKQ0KDQojUmVzZXQgcG9saWN5IHN0YXR1cyB3aGVuIHBvcnQgaXMgdXANCiAgICAgIC
Agc2VsZi5yMiA9IFJ1bGUoJ1BvcnQgZW5hYmxlZCBhZG1pbmlzdHJhdGl2ZWx5JykNCiAgICAgICAgc2VsZi5yMi5
jb25kaXRpb24oJ3RyYW5zaXRpb24ge30gZnJvbSAiZG93biIgdG8gInVwIicsIFtzZWxmLm0xXSkNCiAgICAgICAg
c2VsZi5yMi5hY3Rpb24oc2VsZi5hY3Rpb25fcG9ydF91cCkNCg0KICAgIGRlZiBhY3Rpb25fcG9ydF9kb3duKHNlb
GYsIGV2ZW50KToNCiAgICAgICAgQWN0aW9uU3lzbG9nKA0KICAgICAgICAgICAgJ1BvcnQge30gaXMgZGlzYWJsZW
QgYWRtaW5pc3RyYXRpdmVseScsDQogICAgICAgICAgICBbc2VsZi5wYXJhbXNbJ3BvcnRfaWQnXV0pDQogICAgICA
gIEFjdGlvbkNMSSgic2hvdyBsbGRwIGNvbmZpZ3VyYXRpb24ge30iLCBbc2VsZi5wYXJhbXNbJ3BvcnRfaWQnXV0p
DQogICAgICAgIEFjdGlvbkNMSSgic2hvdyBpbnRlcmZhY2Uge30gZXh0ZW5kZWQiLCBbc2VsZi5wYXJhbXNbJ3Bvc
nRfaWQnXV0pDQogICAgICAgIGlmIHNlbGYuZ2V0X2FsZXJ0X2xldmVsKCkgIT0gQWxlcnRMZXZlbC5DUklUSUNBTD
oNCiAgICAgICAgICAgIHNlbGYuc2V0X2FsZXJ0X2xldmVsKEFsZXJ0TGV2ZWwuQ1JJVElDQUwpDQogICAgICAgIHN
lbGYubG9nZ2VyLmRlYnVnKCIjIyMgQ3JpdGljYWwgQ2FsbGJhY2sgZXhlY3V0ZWQiKQ0KDQogICAgZGVmIGFjdGlv
bl9wb3J0X3VwKHNlbGYsIGV2ZW50KToNCiAgICAgICAgc2VsZi5sb2dnZXIuaW5mbygiQ3VycmVudCBhbGVydCBsZ
XZlbDogIiArIHN0cihzZWxmLmdldF9hbGVydF9sZXZlbCgpKSkNCiAgICAgICAgaWYgc2VsZi5nZXRfYWxlcnRfbG
V2ZWwoKSBpcyBub3QgTm9uZToNCiAgICAgICAgICAgIEFjdGlvblN5c2xvZygNCiAgICAgICAgICAgICAgICAnUG9
ydCB7fSBpcyBlbmFibGVkIGFkbWluaXN0cmF0aXZlbHknLA0KICAgICAgICAgICAgICAgIFtzZWxmLnBhcmFtc1sn
cG9ydF9pZCddXSkNCiAgICAgICAgICAgIHNlbGYucmVtb3ZlX2FsZXJ0X2xldmVsKCkNCiAgICAgICAgICAgIHNlb
GYubG9nZ2VyLmRlYnVnKCdVbnNldCB0aGUgcHJldmlvdXMgc3RhdHVzJykNCg0KICAgICAgICBzZWxmLmxvZ2dlci
5kZWJ1ZygnIyMjIE5vcm1hbCBDYWxsYmFjayBleGVjdXRlZCcp

Parts of a script
An Aruba Network Analytics Engine script is a Python script that defines which switch resources to
monitor and, optionally, rules that define what actions to take when certain conditions are true.

The main structures of a script are the following:

n Header

n Import statements

n Manifest

n Parameter definitions

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

80

n Agent class constructor, which can contain the following:

Agent functions

The agent constructor can contain functions that are restricted to a specific monitor, rule, or action.

Examples of agent functions include the following:

o The Graph, Title, and Baseline functions.

o Functions related to agent events, such as on_agent_restart and on_parameter_change.

o Functions related to Aruba Analytics Data Collections (ADCs).

Monitors

A monitor uses the REST URI of a resource to define the resource on the switch to be monitored by
the agent.

o All monitors generate time-series data about resource they monitor. The data can be viewed in

time-series graphs in the Web UI.

o Optionally, a monitor can be associated with rules that execute actions when certain network

conditions are true.

Rules

Rules define under which conditions to execute actions.

o Rules are optional.

o A rule can be defined with conditions that reference multiple monitors.

o A rule must contain a condition.

o A rule is not required to contain actions. A rule that does not contain actions does not generate an

alert when an active condition transitions to true.

Conditions

The condition of a rule defines the circumstance under which actions, if any, are executed. The clear
condition is an optional part of the rule that determines when a network condition or event is no
longer occurring.

Actions

Actions are the tasks done by the agent in response to defined conditions. Actions can automate
many of the things an administrator might do to troubleshoot network issues. Actions are part of a
rule.

Actions are optional.

Header
The script header includes legal, copyright, and license information.

The following is an example of a script header for an Aruba-certified script:
#-*- coding: utf-8 -*-
#
#Copyright (C) 2017 Hewlett Packard Enterprise Development LP
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#http://www.apache.org/licenses/LICENSE-2.0
#

Scripts | 81

| #Unless   | required     | by      | applicable  | law         | or      | agreed to       | in writing, |       |
| --------- | ------------ | ------- | ----------- | ----------- | ------- | --------------- | ----------- | ----- |
| #software | distributed  |         | under       | the         | License | is distributed  |             | on an |
| #"AS IS"  | BASIS,       | WITHOUT | WARRANTIES  |             | OR      | CONDITIONS      | OF          | ANY   |
| #KIND,    | either       | express | or implied. |             | See     | the License     | for         | the   |
| #specific | language     |         | governing   | permissions |         | and limitations |             |       |
| #under    | the License. |         |             |             |         |                 |             |       |
| Import    | statements   |         |             |             |         |                 |             |       |
TheimportstatementsspecifythePythonmodulesthatdefinefunctionsusedelsewhereinthescript.If
youareusingseveralfunctionsfromthesamemodule,considerimportingthewholemodule.
ThefollowingexampleimportstheEnumfunctionsfromtheenumlibraryandimportsthedatetime
module.
| from enum | import | Enum |     |     |     |     |     |     |
| --------- | ------ | ---- | --- | --- | --- | --- | --- | --- |
import datetime
Manifest
ThemanifestintroducesthescripttothePythoncompiler.Themanifestisrequired.
Exampleofamanifest:
| Manifest | = {                                        |     |     |     |     |     |     |     |
| -------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| 'Name':  | 'com.arubanetworks.cpu_monitor_threshold', |     |     |     |     |     |     |     |
'Description': 'System CPU Monitoring Policy on configured threshold values',
| 'Version':           |                 | '0.1', |               |     |         |          |     |     |
| -------------------- | --------------- | ------ | ------------- | --- | ------- | -------- | --- | --- |
| 'Author':            |                 | 'Aruba | Networks',    |     |         |          |     |     |
| 'AOSCXPlatformList': |                 |        | ['64xx',      |     | '832x', | '8400'], |     |     |
| 'AOSCXVersionMin':   |                 |        | '10.09.1000', |     |         |          |     |     |
| 'AOSCXVersionMax':   |                 |        | '10.10',      |     |         |          |     |     |
| 'Tags':              | ['application'] |        |               |     |         |          |     |     |
}
| Required |     | items |     |     |     |     |     |     |
| -------- | --- | ----- | --- | --- | --- | --- | --- | --- |
Name
Specifiesauniquenameforthescript.Thenamemustbeatextstringthatstartswithaletteror
numberandcancontainalphanumericcharactersandthespecialcharacters.(dot),-(hyphen),and
_(underscore).Range:3to80alphanumericcharacters.
ArubaNetworksrecommendsthatthenamebeacanonicalname(CNAME).Thecanonicalname
followsthereversedomainnamenotation.Forexample:com.myco.bgp_mon1.0
Description
Describeswhatthescriptdoes.Mustbeatextstring.
Version
Specifiesversioninformationaboutthescript.Theversionmustbeatextstringthatstartswitha
letterornumberandcancontainalphanumericcharactersandthespecialcharacters.(dot),-
(hyphen),and_(underscore).Versionmustnotbeempty.
Author
Specifiestheauthorofthescript.Mustbeatextstring.
| Optional | items |     |     |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
AOSCXPlatformList
SpecifiestheexactlistofAOS-CX platforms(modelnumbers)onwhichtheNAEScriptispermittedto
run.Theplatformlistisenclosedinsquarebracketswitheachplatformenclosedinsingleordouble
82
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

quotes and separated from other platforms with a comma. The platform can include the lowercase
"x" as a wildcard, as in '64xx' to match 6405 and 6410, and '832x' to match 8320 and 8325.

If this optional field is omitted or the field value is not specified, the platform will not be enforced.
This field deprecates TargetPlatform.

Example: 'AOSCXPlatformList': ['64xx', '832x', '8400']

The 6400 Switch Series is indicated as either '64xx' or '6405', 6410'. '6400' does not match any platform.

The 8400X Switch is indicated as either '8400' or '8400X'.

AOSCXVersionMin

Specifies the minimum required AOS-CX software version that this NAE Script requires to run. The
version is enclosed in single or double quotes. Optionally, a 4-digit software build number (in the
form ".9999") can be included to the immediate right of the version.

If this optional field is omitted or the field value is not specified, the minimum AOS-CX version will
not be enforced, meaning that there is no required minimum software version. This field deprecates
TargetSoftwareVersion.

Example: 'AOSCXVersionMin': '10.09.1000'

AOSCXVersionMax

Specifies the maximum permissible AOS-CX software version on which this NAE Script can run. The
version is enclosed in single or double quotes. Optionally, a 4-digit software build number (in the
form ".9999") can be included to the immediate right of the version.

If this optional field is omitted or the field value is not specified, the maximum AOS-CX version will
not be enforced, meaning that there is no upper limit to the software version. This field deprecates
TargetSoftwareVersion.

Example: 'AOSCXVersionMax': '10.10'

APIVersion (deprecated as of AOS-CX 10.10)

Specifies which NAE script API version is required to run this script. This item is informational only.
No validation or action is performed for this item.

Default: 1.0.0

TargetPlatform (deprecated as of AOS-CX 10.10)

Replaced by AOSCXPlatformList. Specifies the switch platform on which the script is designed to be
executed. If this item is not specified, the script is considered to be platform independent. This item
is informational only. No validation or action is performed for this item.

Example: 8325

TargetSoftwareVersion (deprecated as of AOS-CX 10.10)

Replaced by AOSCXVersionMin and AOSCXVersionMax. Specifies the switch firmware version or
versions on which the script is designed to be executed. If TargetPlatform is not specified, the script
is expected to work with any software version. This item is informational only. No validation or action
is performed for this item.

Example: 10.03

Tags

Specifies one or more tags to provide information about the script.

Scripts | 83

The following tags are used by NetEdit to categorize and group the script and related alerts, and to
automatically incorporate new NAE scripts into the health ranking for each of the following
categories:

n application

n segmentation

n service (includes Client Services)
n routing

n bridging

n device

n other

Each tag must be a text string. This item is informational only. No validation or action by the NAE is
performed for this item.

Examples:

n

n

'Tags': ['application']

'Tags': ['segmentation','vlan']

The manifest tags are not shown in the Web UI or the CLI, and they are not the same as the script
tags in the ASE. To view the tags associated with a script installed on a switch, you can do one of the
following:

n Look at the Manifest in the script by viewing the script contents on the Script Details page of the

Web UI.

n Use the REST API to get information about the script.

Parameter definitions
The ParameterDefinitions statement defines the parameters that are used in the script.

When a user creates an agent, the user can specify values for the parameters. The user must specify
values for parameters that the script identifies as required parameters.

When you write a script, Hewlett Packard Enterprise recommends that you create parameters for any
user-configurable option in the script.

If the script has no parameters, omit the ParameterDefinitions statement.

The following example of a ParameterDefinitions statement defines the following parameters:

threshold

The threshold parameter is an integer and has a default value 90.

password

The password parameter is a string. The parameter is optional. If the user supplies a value, the user-
supplied text is encrypted when the text is stored.

ParameterDefinitions = {

'threshold': {

'Name': 'Critical CPU Threshold value in percentage',
'Description': ('When System CPU utilization exceeds this value, '

'set the policy status to Critical and the policy will log

'

'system daemon CPU utilization details and CPU queue

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

84

statistics in syslog.'),
| 'Type': 'integer', |     |     |
| ------------------ | --- | --- |
| 'Default': 90      |     |     |
}
| 'password': {       |           |            |
| ------------------- | --------- | ---------- |
| 'Name': 'Password', |           |            |
| 'Description':      | ' Service | Password', |
| 'Type': 'string',   |           |            |
| 'Encrypted':        | True,     |            |
| 'Required':         | False     |            |
}
}
ParameterDefinitions description
Structure and syntax
TheParameterDefinitionsisaPythondictionarythatcontainsoneormoreparameters.Each
parameterisdefinedbyaPythondictionarycontaininginformationspecifictotheparameter.Atthe
timetheagentiscreated,thedefaultvalueisassignedtotheparameterunlesstheuserspecifiesa
differentvalue.
Thispartofthescriptisomittedifthescriptdoesnotincludeuser-definedparameters.
ParameterDefinitions = {
'<param_name>': {
'Name': '<descriptive_parameter_name>',
| 'Description': | '<description>' |     |
| -------------- | --------------- | --- |
'Type': '<datatype>',
'Default': <default_value>,
| 'Encrypted': '<True_or_False>' |     |     |
| ------------------------------ | --- | --- |
| 'Required': '<True_or_False>'  |     |     |
}
}
Components
Eachparameterdefinitionmustcontainthefollowing:
The parameter declaration
Specifiesauniquenameforparameter.Thisnamemustbeuniquewithinthescript.Thenameisa
textstringthatcancontainalphanumericcharacters,-(hyphen),and_(underscore).Example:
threshold
Name
Thenameoftheparameter.Thisnameisdisplayedintheuserinterfaces.
Description
Describestheparameter.ThisdescriptionisdisplayedtousersintheCreate Agentscreenofthe
WebUI.
Type
Specifiesthedatatypeofparameter.Parametertypeisoneofthefollowingvalues:
integer
n
string
n
Default
Specifiesthedefaultvalueoftheparameter.Atthetimetheagentiscreated,thedefaultvalueis
assignedtotheparameterunlesstheuserspecifiesadifferentvalue.Youmustspecifyadefaultif
theparameterispartofamonitororacondition.Otherwise,providingadefaultvalueisoptional.
Scripts|85

Encrypted

Specifies whether the user-supplied text is to be encrypted when the text is stored.

When Encrypted is True, the parameter is stored in a secure way. The parameter value will be
available in plain text only when the Network Analytics Engine script is executed.

Default: False

Required

Specifies whether the user is required to supply a value. Use this attribute to force the user to
provide a value for this parameter.

When Required is True, the parameter is required. If the user does not provide a value for this
parameter, an error is returned and the agent is not created.

When Required is False, the parameter is optional. If the user does not provide a value for this
parameter, the default value of the parameter is used.

Default: False

Agent class constructor

Syntax

The agent class constructor must begin with the following declaration:
class Agent(NAE):

def __init__(self):

The name of the constructor, Agent, is recommended, but using a different name does not result in an
error.

Description

The main body of the script is the agent class constructor. The agent class constructor can contain:

n Monitors

n Conditions

n Rules

n Actions

n Agent functions such as Graph, on_parameter_change, and Baseline.

n Analytics Data Collections (ADCs)

Example

Example of an agent class constructor:
class Agent(NAE):

def __init__(self):

uri1 = '/rest/v1/system/subsystems/*/*/power_supplies/*?attributes=status'
self.m1 = Monitor(uri1, name='System CPU utilization')

self.r1 = Rule('High CPU utilization')
self.r1.condition('{} > {}', [self.m1, self.params['threshold']])
self.r1.action(self.action_high_cpu)
self.r1.action("CLI","top cpu")
self.r1.action("SHELL","ps -ef")

def action_high_cpu(self, event):

self.set_alert_level(AlertLevel.CRITICAL)

# CPU value when the Condition met

cpu = event["value"]
ActionSyslog("CPU Utilization at %s%." % cpu)

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

86

ActionCLI("top cpu")
ActionShell("ps -ef")

Graph

Syntax

Graph(<monitor-set>[, title=<title>][, dashboard_display=True])

Description

The Graph function enables you to select a monitor or group of monitors to display together in a graph
on the Agent Details page in the Web UI.

Parameters

<monitor-set>

Specifies a comma-separated list of monitors to be included in this graph. The list must be enclosed
in brackets ([]), which define a list in Python. The list must include at least one monitor.

Examples:

n [self.monitor1]

n [self.m1, self.m2, self.m3]

<title>

Specifies the title to be displayed for this graph. The definition of <title> must use the Title
function.

For example: title=Title("My graph title")

dashboard_display=True

Specifies that this graph represent this agent on the Analytics Dashboard of the Web UI. You must
specify this parameter for exactly one graph per agent.

If either of the following is true, a script error is generated:

n The script has multiple Graph functions defined, but none of those Graph functions set the parameter

dashboard_display=True.

n The script has multiple Graph functions defined, and more than one of those Graph functions sets the

parameter dashboard_display=True.

Usage

The Aruba Network Analytics Engine (NAE) provides the Graph function to enable you to select a monitor
or group of monitors to display together in a graph on the Agent Details page in the Web UI.

The Agent Details page can include up to nine graphs. If the script does not include a Graph function, a
default graph is created automatically. The default graph includes all the monitors in the script. You use
the dashboard_display=True parameter to specify which graph is to represent the agent in on the
Analytics Dashboard of the Web UI.

The graph displays alerts for all metrics being monitored. However, the graph can show graphed data
for a maximum of eight metrics at a time. The metrics that are being shown on the graph are listed at
the bottom of the graph.

When the agent is created, the NAE selects the most appropriate metrics to graph, up to a maximum of
eight. After the agent is created, a Web UI user can customize the graph and choose which metrics to
display.

Examples

Scripts | 87

Inthefollowingexample,graphg1includesdatafrommonitorsm1andm2.Thegraphdoesnothavea
customtitleandisnotthegraphthatrepresentstheagentintheAnalyticsDashboard.
| self.g1 | = Graph([self.m1, |     | self.m2]) |     |
| ------- | ----------------- | --- | --------- | --- |
Inthefollowingexample,graphg2includesdatafrommonitorm1.Thegraphhasacustomtitle,butitis
notthegraphthatrepresentstheagentintheAnalyticsDashboard.
title = Title("CPU utilisation by {} daemon ", [self.params["daemon_name"]])
| self.g2 | = Graph([self.m1], |     | title=title) |     |
| ------- | ------------------ | --- | ------------ | --- |
Inthefollowingexample,graphg2includesdatafrommonitorm1.Thegraphhasacustomtitleanditis
thegraphthatrepresentstheagentintheAnalyticsDashboard.
| title = | Title("CPU | utilisation | by hpe-policyd | daemon") |
| ------- | ---------- | ----------- | -------------- | -------- |
self.g2 = Graph([self.m1], title=title, dashboard_display=True)
Title
Syntax
| Title("<title-string>"[, |     |     | <params>]) |     |
| ------------------------ | --- | --- | ---------- | --- |
Description
Createsatextstringtobeusedasacustomtitleforagraphorforapredefinedaction.
Parameters
<title-string>
Specifiesthepythonstringtobeusedforthetitle.Thestringcancontainparameters.Tospecifythat
aparameterisexpected,usethefollowingcharacters:
{}
| Forexample:"Print |     | interface | {} details" |     |
| ----------------- | --- | --------- | ----------- | --- |
<params>
Optional.Containstheparameterstobeusedinthetitlestring.Ifmultipleparametersareused,they
mustbepassedtothefunctionintheordertheyarerequiredbythetitlestring.
Usage
TheArubaNetworkAnalyticsEngineprovidestheTitlefunctiontoenableyoutospecifycustomtitles
whendefiningmultiplegraphs,ortoshowspecificinformationaboutanactionbeingperformedbyan
agent.Forexample,ifyoudefineatitleforeachCLIactioninascript,ausercanseewhichactionis
beingperformedbylookingattheAlertDetailspageintheWebUI.
Examples
Thefollowingexampledefinesatitlethatisusedforagraph.Thetitlestringincludesaparameter.
title = Title("CPU utilisation by {} daemon ", [self.params["daemon_name"]])
| self.g1 | = Graph([self.m1], |     | title=title) |     |
| ------- | ------------------ | --- | ------------ | --- |
ThefollowingexampledefinesatitlethatisusedforaCLIaction.Thetitlestringdoesnotincludea
parameter.
| title =                   | Title("Show | switch | configuration") |                 |
| ------------------------- | ----------- | ------ | --------------- | --------------- |
| self.r.action("CLI","show |             |        | running-config  | ", title=title) |
on_agent_re_enable
Syntax
| on_agent_re_enable(<agent>, |     |     | <event>) |     |
| --------------------------- | --- | --- | -------- | --- |
Description
88
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

Performs the specified actions when the NAE agent is re-enabled.

Parameters

<agent>

Specifies the agent that has the changed parameters.

Typically, this parameter is defined as the variable: self

<event>

Specifies a Python dictionary that contains the event information.

Typically, this parameter is defined as the variable: event

Usage

When an agent is disabled, it does not perform monitoring tasks. When an agent is re-enabled, it might
not be in the correct state to perform its monitoring tasks. The Aruba Network Analytics Engine
provides the on_agent_re_enable function to enable you to specify actions to perform to update an
agent after it is re-enabled.

Example

def on_agent_re_enable(self, event):

self.remove_alert_level()
ActionCustomReport("Agent re-enabled")

on_agent_restart

Syntax

on_agent_restart(<agent>, <event>)

Description

Performs the specified actions when the NAE agent is restarted.

Parameters

<agent>

Specifies the agent that has the changed parameters.

Typically, this parameter is defined as the variable: self

<event>

Specifies a Python dictionary that contains the event information.

Typically, this parameter is defined as the variable: event

Usage

The NAE daemon might be stopped and restarted because of a management module failover operation
or because a core dump operation has been performed.

When the NAE daemon restarts, it restarts the agents. When an agent is restarted, it might not be in the
correct state to perform its monitoring tasks. The Aruba Network Analytics Engine provides the on_
agent_restart function to enable you to specify actions to perform to update an agent after it is
restarted.

Example

def on_agent_restart(self, event):

ActionCLI("show core-dumps")
self.remove_alert_level()

Scripts | 89

on_parameter_change
Syntax
| on_parameter_change(<agent>, |     | <params>) |     |     |
| ---------------------------- | --- | --------- | --- | --- |
Description
Performsthespecifiedactionswhenauserchangesthevalueofanagentparameter.
Parameters
<agent>
Specifiestheagentthathasthechangedparameters.
Typically,thisparameterisdefinedasthevariable:self
<params>
SpecifiesaPythondictionarythatcontainsthenameofthechangedparameter,theoldvalue,and
thenewvalue.
Usage
ParametersthataredefinedintheParameterDefinitionsofascriptcanbechangedbyauserafterthe
usercreatestheagent.
TheArubaNetworkAnalyticsEngineprovidestheon_parameter_changefunctiontoenableyouto
specifyactionstheagentistoperformwhentheuserchangesthevalueofoneormoreparameters.
Example
| ParameterDefinitions |                    | = {        |                   |     |
| -------------------- | ------------------ | ---------- | ----------------- | --- |
| 'interface_id':      |                    | {          |                   |     |
|                      | 'Name': 'Interface | Id',       |                   |     |
|                      | 'Description':     | 'Interface | to be monitored', |     |
'Type': 'string',
|     | 'Default': '1/1/1' |     |     |     |
| --- | ------------------ | --- | --- | --- |
}
}
uri1 = '/rest/v1/system/interfaces/{}?attributes=link_state'
| self.m1                       | = Monitor(uri1,          | 'Interface              | Link State') |     |
| ----------------------------- | ------------------------ | ----------------------- | ------------ | --- |
| def on_parameter_change(self, |                          | params):                |              |     |
| interface_id                  | = params['interface_id'] |                         |              |     |
| if                            | interface_id["old"]      | != interface_id["new"]: |              |     |
self.remove_alert_level()
| Baselines | for dynamic | thresholds |     | for monitors |
| --------- | ----------- | ---------- | --- | ------------ |
Manyagentsmonitorthingslikenetworktraffic,whichcanvarythroughouttheday.
Monitorsusuallycontainrulestogenerateanalert—andpossiblyexecuteotheractions—when
somethingliketherateofincomingpacketsexceedsacertainvalue.Thisvalueiscommonlyreferredto
asathreshold.
Itisdifficultforascriptwritertochooseathresholdvaluethatisappropriateforallswitchesinall
networks.Forexample:
n Therateofincomingtrafficforoneswitchmightberelativelyhigh,evenundernormal
circumstances.
90
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

n On a different switch on a different network, that same incoming traffic rate might be considered

abnormally high, and the network admin would want an alert to be generated in those
circumstances.

n If the script writer chooses a threshold based on the lower incoming traffic rate, the agent

monitoring the high-traffic switch will either generate numerous alerts or will remain in an alert state
for most of the time. Because the threshold is lower than a traffic rate that is considered normal for
that switch, the alerts generated because of the lower thresholds are considered "false positives" by
the network administrator.

The Baseline function provides a way to specify thresholds that are appropriate to the network
conditions on the switch. When an agent is created and enabled, it spends a specified amount of time
"learning" about the data it is monitoring before it sets thresholds that are calculated based on what it
learned.

In addition, these thresholds are dynamic. The agent continues to learn about the data it monitors and
the Baseline function adjusts the thresholds accordingly. For example, if the lower-traffic switch starts
to get consistently higher incoming traffic rates, the Baseline function adjusts the thresholds to reflect
the newly learned rates.

If desired, the script writer can specify default thresholds that can be used to determine when to set
and clear alerts while the agent in a learning state. Otherwise the agent does not generate alerts while it
learning about the data.

The methods used to determine the baseline from which to calculate the thresholds—both during the
initial learning state and over time—depend on the algorithm selected in the Baseline function.

Baseline workflow and considerations

The following diagram shows a summary of the workflow of a Baseline function that uses
MaxAlgorithm in its threshold calculations:

Choosing threshold multipliers

The high threshold is used in the determination of the condition which, when true, triggers the
generation of an alert and, optionally, the execution of additional actions.

The low threshold is used in the rule to determine the clear condition, which—when true—triggers
actions such as resetting the alert level.

At the end of the initial learning period and at the end of the continuous learning window, the
MaxAlgorithm function calculates a single baseline value based on the smoothed data. In the Baseline
function, you specify a high-threshold multiplier and a low-threshold multiplier to apply to this baseline
value, resulting in the high threshold and the low threshold, against which datapoints are evaluated.

In effect, this strategy creates a "corridor" in which data can fluctuate without triggering alerts.

n If you choose a low number for the high-threshold multiplier, smaller variations from the baseline

trigger alerts, which can result in alerts being triggered for what might be normal fluctuations in data.

n If you choose a high number for the high-threshold multiplier, the threshold might be exceeded less

often, resulting in fewer alerts.

Effect of learning periods

Scripts | 91

Both the continuous learning window and the initial learning period are part of the look-back
mechanism used by the Baseline function. These learning durations are used to determine how many
datapoints to consider when calculating the baseline.

Using a period of time instead of specifying a number of datapoints is useful for situations in which
knowing what a representative number of datapoints might be is difficult, but a representative amount
of time is easier to estimate. However, getting enough data during the learning period to make a good
calculation can depend on the length of the learning period and how typical the network conditions are
when the agent is enabled.

Choosing a longer learning period enables the Baseline algorithms to distinguish important trends
while ignoring temporary large fluctuations in data. Choose a learning period that is significantly longer
than a situation that you would consider to be temporary for that kind of data.

For example:

n If the agent is enabled at a time when network traffic is low and the initial learning period is 10

minutes, the thresholds that are calculated are based on that low traffic. When more users arrive two
hours later and network traffic increases, the measured traffic quickly exceeds the threshold.

n However, if you choose a learning period of one day, the "normal" fluctuations in traffic throughout
the day are included in the baseline, resulting in thresholds that are appropriate to the situation.

Anomalies and baseline recalculations

Data that exceeds the high threshold is considered an anomaly.

If an anomaly occurred during the continuous learning window, all data points that occurred during the
continuous learning window are ignored and thresholds are not recalculated. This design prevents the
thresholds from being reset as a result of a temporary "spike" in data.

If no anomalies occurred during the continuous learning window, the Baseline function updates the
thresholds based on the latest result provided by the MaxAlgorithm function.

Example of baselines in a time series graph

The following is an example the time series graph for a monitor that includes baselines:

n The initial learning time is one minute.

n There are no default thresholds.

In this graph:

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

92

n Thegreenlineistherawdata.
n Theorangelineisthehighthresholdascalculatedbythebaseline.
Thebluelineisthelowthresholdascalculatedbythebaseline.
n
Theeventsinthetimelineareasfollows:
1. At20:32:30,anagentiscreatedandenabled.Thebaselineentersthelearningstate.Becausethe
scriptdidnotspecifydefaultthresholds,therearenothresholdsdefined.Inthegraph,justthe
greenlinefortherawdataisdisplayed.
2. At20:33:30,thebaselineexitsthelearningstateandenterstheactivestate:
|     | n Thehighthresholdandthelowthresholdcalculationsarecompleted. |     |     |     |
| --- | ------------------------------------------------------------- | --- | --- | --- |
n Thegraphbeginsthedisplayoftheorangelineforthehighthresholdandthebluelineforthe
lowthreshold.
n Theagentwillgenerateanalertwhenthemonitoredtrafficrate(inpacketspersecond)
exceedsthehighthreshold.
n Theagentwillclearthealertwhenthemonitoredtrafficrate(inpacketspersecond)drops
belowthelowthreshold.
3. At20:37:33,analertistriggeredbecausethemonitoredtrafficrateexceedsthehighthreshold.
4. At20:39:15,thealertisclearedbecausethemonitoredtrafficrate(inpacketspersecond)islower
thanthelowthreshold.
5. At20:40:30,thethresholdsareupdated.
Inthiscase,thethresholdsaresetsignificantlyhigherbecausethealgorithmincludesallthedatainits
continuouslearningwindow,whichincludedthetimeinwhichthetrafficratewasmuchhigherthan
thepreviousthreshold.
Ifthescriptspecifiedalongerinitiallearningtime,suchasoneday,thecalculationsusedtocreatethe
thresholdscanincludethetypicalfluctuationsindatathatcanoccur,resultinginmoreappropriate
thresholdsandalertsthattriggeronlyforsignificantanomalies.
| Example | of a script | that uses | baselines |     |
| ------- | ----------- | --------- | --------- | --- |
Thefollowingisanexampleofascriptthatincludesmultiplemonitorsandbaselines:
| Manifest | = {                                     |     |     |     |
| -------- | --------------------------------------- | --- | --- | --- |
| 'Name':  | 'single_interface_tx_rx_stats_monitor', |     |     |     |
'Description': 'Policy to monitor tx/rx packets stats of a interface',
| 'Version': | '2.0', |           |     |     |
| ---------- | ------ | --------- | --- | --- |
| 'Author':  | 'Aruba | Networks' |     |     |
}
| ParameterDefinitions |                    | = {        |       |             |
| -------------------- | ------------------ | ---------- | ----- | ----------- |
| 'interface_id':      |                    | {          |       |             |
|                      | 'Name': 'Interface |            | Id',  |             |
|                      | 'Description':     | 'Interface | to be | monitored', |
|                      | 'Type': 'string',  |            |       |             |
|                      | 'Default':         | '1/1/1'    |       |             |
}
}
class Agent(NAE):
| def | __init__(self): |                                                  |           |             |
| --- | --------------- | ------------------------------------------------ | --------- | ----------- |
|     | # algorithm     | for dynamic                                      | Threshold | calculation |
|     | self.alg        | = MaxAlgorithm(continuous_learning_window="10m") |           |             |
# rx packets
uri1 = '/rest/v1/system/interfaces/{}?attributes=statistics.rx_packets'
Scripts|93

rate_m1 = Rate(uri1, "10 seconds", [self.params['interface_id']])
| self.m1 | = Monitor( |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- |
rate_m1,
| 'Rx     | Packets           | (packets |     | per second)') |           |     |              |
| ------- | ----------------- | -------- | --- | ------------- | --------- | --- | ------------ |
| self.r1 | = Rule('Rule      |          | for | Monitor       | Interface |     | rx Packets') |
| title1  | = Title("Baseline |          |     | for Interface |           | rx  | Packets")    |
self.baseline1 = Baseline(self.m1, algorithm=self.alg, title=title1,
high_threshold_factor=2,
low_threshold_factor=1.2,
initial_learning_time='1d')
| self.r1.condition('{}               |     |         | > {}', | [self.m1, |                      | self.baseline1]) |                  |
| ----------------------------------- | --- | ------- | ------ | --------- | -------------------- | ---------------- | ---------------- |
| self.r1.clear_condition('{}         |     |         |        | <         | {}', [self.m1,       |                  | self.baseline1]) |
| self.r1.action("ALERT_LEVEL",       |     |         |        |           | AlertLevel.CRITICAL) |                  |                  |
| self.r1.clear_action("ALERT_LEVEL", |     |         |        |           |                      | AlertLevel.NONE) |                  |
| # rx packets                        |     | dropped |        |           |                      |                  |                  |
uri2 = '/rest/v1/system/interfaces/{}?attributes=statistics.rx_dropped'
| self.m2 | = Monitor( |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- |
uri2,
| 'Rx | Packets | Dropped | (packets)', |     |     |     |     |
| --- | ------- | ------- | ----------- | --- | --- | --- | --- |
[self.params['interface_id']])
# tx packets
uri3 = '/rest/v1/system/interfaces/{}?attributes=statistics.tx_packets'
rate_m3 = Rate(uri3, "10 seconds", [self.params['interface_id']])
| self.m3 | = Monitor( |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- |
rate_m3,
| 'Tx     | Packets           | (packets |     | per second)') |           |     |              |
| ------- | ----------------- | -------- | --- | ------------- | --------- | --- | ------------ |
| self.r3 | = Rule('Rule      |          | for | Monitor       | Interface |     | tx Packets') |
| title3  | = Title("Baseline |          |     | for Interface |           | tx  | Packets")    |
self.baseline3 = Baseline(self.m3, algorithm=self.alg, title=title3,
high_threshold_factor=2,
low_threshold_factor=1.2,
initial_learning_time='1d')
| self.r3.condition('{}               |     |         | > {}', | [self.m3, |                      | self.baseline3]) |                  |
| ----------------------------------- | --- | ------- | ------ | --------- | -------------------- | ---------------- | ---------------- |
| self.r3.clear_condition('{}         |     |         |        | <         | {}', [self.m3,       |                  | self.baseline3]) |
| self.r3.action("ALERT_LEVEL",       |     |         |        |           | AlertLevel.CRITICAL) |                  |                  |
| self.r3.clear_action("ALERT_LEVEL", |     |         |        |           |                      | AlertLevel.NONE) |                  |
| # tx packets                        |     | dropped |        |           |                      |                  |                  |
uri4 = '/rest/v1/system/interfaces/{}?attributes=statistics.tx_dropped'
| self.m4 | = Monitor( |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- |
uri4,
| 'Tx | Packets | Dropped | (packets)', |     |     |     |     |
| --- | ------- | ------- | ----------- | --- | --- | --- | --- |
[self.params['interface_id']])
Baseline
Syntax
Baseline(<monitor>
[, title=<title>]
[, algorithm=<algorithm>]
[, high_threshold_factor=<high-multiplier>]
[, low_threshold_factor=<low-multiplier>]
[, initial_learning_time="<duration>"]
[, default_thresholds=(<lthresh>,<hthresh>)]
)
Description
TheBaselinefunctioncalculatesandsetslowandhighthresholdsforamonitorbasedondata
gatheredduringalearningperiodafteranagentisenabledorrestarted.
94
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

The calculated thresholds account for typical fluctuations in the data, enabling alerts to be triggered
only for conditions exceeding the learned "normal" range. The Baseline function also calculates new
thresholds and updates baselines at specified intervals, enabling the monitor to adjust as network
conditions change.

Parameters

<monitor>

Specifies the monitor to which the baseline applies.

If the monitored URI contains wildcards, the baseline is calculated against all resources pointed to by
expanding the wildcard. The same baseline thresholds apply to all resources.

<title>

Specifies the title to be displayed for this baseline. If specified, the title is displayed in the Web UI as
the name of the baseline.

The definition of title must use the Title function.

For example: title=Title("Baseline for CPU utilization")

<algorithm>

Specifies the algorithm to use to calculate the baseline thresholds.

The supported and default algorithm is: MaxAlgorithm

<high-multiplier>

Specifies the high-threshold multiplier to apply to the value calculated by the algorithm.

The algorithm result multiplied by the high-multiplier determines the current high threshold for the
monitor.

Typically, the high threshold is used to determine when the rule condition is true and therefore to
trigger an alert and execute actions.

Default: 2

<low-multiplier>

Specifies the low-threshold multiplier to apply to the value calculated by the algorithm.

The algorithm result multiplied by the low-multiplier determines the current low threshold for the
monitor.

Typically, the low threshold is used to determine when the clear condition is true and therefore to
execute clear actions, such as clearing the alert.

Default: 1

<duration>

Specifies amount of time series data required for learning.

The initial learning time is used determine how long to stay in the initial learning state after an agent
is enabled. If there is already a time series in the database for the monitored resource, the Baseline
function compares the amount of data to the initial learning time and includes that data.

For example, if the initial learning time is one hour and one or more hours of time series data exists
in the database, the thresholds are set immediately. If there is 55 minutes of data available, the
agent stays in the initial learning state for five minutes. If there is no data available, the baseline
stays in the initial learning state for one hour.

During the initial learning state, the baseline function looks at the monitored data and uses its
algorithm to determine normal patterns versus anomalies. Unless you specify values for the
default_thresholds parameter, the agent does not generate alerts during the initial learning state.

Ensure that the initial learning time is long enough to gather enough data to determine normal
versus abnormal patterns.

For example:

Scripts | 95

n Ifyouaremonitoringsomethingthatisupdatedinfrequently,alongerinitiallearningtimemightbe
requiredtoobtainenoughdata.
n Ifanagentismonitoringnetworktrafficandthatagentisenabledduringatimethathasunusually
lowtraffic,thebaselinecalculatesalowvalue,and"normal"trafficlevelsexceedthethreshold,
creatinganalert.Bysettingalongerdurationfortheinitiallearningperiod,youmaximizetheability
ofthealgorithmtomakecalculationsbasedontypicalconditions.
Theformatfor<duration>is<number><unit>,where<unit>isoneofthefollowing:
| Value |     |     |     |     |     | Meaning |     |
| ----- | --- | --- | --- | --- | --- | ------- | --- |
| s     |     |     |     |     |     | seconds |     |
| m     |     |     |     |     |     | minutes |     |
| h     |     |     |     |     |     | hours   |     |
| d     |     |     |     |     |     | days    |     |
| w     |     |     |     |     |     | weeks   |     |
Default:1h
| <lthresh> | and | <hthresh> |     |     |     |     |     |
| --------- | --- | --------- | --- | --- | --- | --- | --- |
Specifiesthedefaultlowanddefaulthighthresholds.Thesethresholdsareusedwhilethebaselineis
intheinitiallearningstate.Boththresholdsmustbespecified.
Ifdefaultthresholdsarenotspecified,alertsarenottriggeredforthemonitorwhilethebaselineisin
thelearningstate.
Example
Thefollowingexamplecontainsamonitorthatincludesabaseline:
| # algorithm | for                                              | dynamic | Threshold |     | calculation |     |     |
| ----------- | ------------------------------------------------ | ------- | --------- | --- | ----------- | --- | --- |
| self.alg    | = MaxAlgorithm(continuous_learning_window="10m") |         |           |     |             |     |     |
# rx packets
uri1 = '/rest/v1/system/interfaces/{}?attributes=statistics.rx_packets'
rate_m1 = Rate(uri1, "10 seconds", [self.params['interface_id']])
| self.m1 | = Monitor( |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- |
rate_m1,
| 'Rx     | Packets           | (packets |     | per second)') |           |     |              |
| ------- | ----------------- | -------- | --- | ------------- | --------- | --- | ------------ |
| self.r1 | = Rule('Rule      |          | for | Monitor       | Interface |     | rx Packets') |
| title1  | = Title("Baseline |          |     | for Interface |           | rx  | Packets")    |
self.baseline1 = Baseline(self.m1, algorithm=self.alg, title=title1,
high_threshold_factor=2,
low_threshold_factor=1.2,
initial_learning_time='1d')
| self.r1.condition('{}               |     |     | > {}', | [self.m1, |                      | self.baseline1]) |                  |
| ----------------------------------- | --- | --- | ------ | --------- | -------------------- | ---------------- | ---------------- |
| self.r1.clear_condition('{}         |     |     |        | <         | {}', [self.m1,       |                  | self.baseline1]) |
| self.r1.action("ALERT_LEVEL",       |     |     |        |           | AlertLevel.CRITICAL) |                  |                  |
| self.r1.clear_action("ALERT_LEVEL", |     |     |        |           |                      | AlertLevel.NONE) |                  |
MaxAlgorithm
Syntax
MaxAlgorithm(continuous_learning_window="<duration>")
96
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

Description
TheMaxAlgorithmfunctionsmoothsrawdatawithintheinitiallearningtimeorthecontinuouslearning
windowbycalculatinganaverageovertimetofindthegreatestnormaldataduringthepastlearning
window.
Parameters
continuous-learning-window="<learning-window>"
Specifieshowfrequentlytoupdatebaselinecalculationswhenthebaselineisintheactivestate,and
howfartolookbackatdatawhenrecalculatingthebaselinethresholdafteranagentisrestarted.
Ifanagentisdisabledandthenre-enabled,thecalculationisbasedontheinitiallearningtime
definedbytheBaselinefunctioninstead.
Default:1h
Forexample,ifthecontinuouslearningwindowisonehour,andthereis55minutesofstoreddata,
theMaxAlgorithmfunctionrecalculatesthebaselineusedforthresholdsafterfiveminutes.
Theformatfor<learning-window>is<number><unit>,where<unit>isoneofthefollowing:
| Value |     |     | Meaning |
| ----- | --- | --- | ------- |
| s     |     |     | seconds |
| m     |     |     | minutes |
| h     |     |     | hours   |
| d     |     |     | days    |
| w     |     |     | weeks   |
Example
| # algorithm | for dynamic                                     | Threshold | calculation |
| ----------- | ----------------------------------------------- | --------- | ----------- |
| self.alg    | = MaxAlgorithm(continuous_learning_window="2h") |           |             |
| How the     | MaxAlgorithm                                    | function  | works       |
TheMaxAlgorithmfunctionusessmootheddataovertimetofindthemaximumvalueandcalculatea
baselineof"typical"data.Bysettingahighthresholdbasedonthiscalculation,thenumberoffalse
positivescanbereduced.Theagentgeneratesalertsforextremeanomaliesonly.
TheMaxAlgorithmfunctionisbestfordatathathasnolimitonitsmaximumvalue,suchasincoming
networktraffic.
| Smoothing | data |     |     |
| --------- | ---- | --- | --- |
TheMaxAlgorithmfunctionusesthe"simplemovingaverage"algorithmtosmoothdata.
Ingeneral,datasmoothingistheprocessofdetectingandremoving"noise"data,allowingimportant
patternstoremain.
Initsformula,thesimplemovingaveragealgorithmreducestheinfluenceofdatapointsthatarenot
similartotheothersbecauseitincludesmultipledatapointsinthecalculation.Inaddition,ateach
subsequentmeasurementpoint,thenewdatapointisaddedandtheoldestdatapointisremoved,so
short-termanomaliesareeventuallyremovedfromthecalculation.
Forexample,considerasimplemovingaveragethatiscalculatedbasedonfivedatapoints.Ifincoming
trafficrates—measuredinpacketspersecondatregularintervals—are10,11,100,4and5:
Scripts|97

n The highest datapoint, 100, is very different from the other datapoints. However the influence of that
datapoint on the result is limited because the formula takes the average of five datapoints. In this
case, the average is 26.

n In addition, over time, the result will be a lower number if the additional datapoints are also lower.

Choosing a continuous learning window

The longer the learning window, the more datapoints that are collected, and the less influence a short-
term fluctuation in data has on the result.

Consider the network traffic example. If the continuous learning window is 10 minutes, the new
thresholds will be calculated based on traffic during that time. If, during that time, network traffic is low,
the Baseline function calculates the new thresholds based on that value. When the traffic increases, the
traffic rate quickly exceeds the threshold and the agent generates an alert. If the network traffic was
unusually low during the learning period, the typical network traffic can result in an undesired alert
(false positive).

ADCs

Aruba Analytics Data Collections (ADCs) are script-defined rules to provide statistics about different
types of network traffic passing through a switch. Network traffic statistics can be gathered based on
many different frame or packet characteristics, including—but not limited to—the following:

n Source IP address (IPv4 or IPv6)

n Destination IP address (IPv4 or IPv6)

n Layer 3 (IP) protocol

n Layer 4 application ports

n Physical switch port

You can create ADCs and view ADC information through NAE scripts only. Multiple agents can use the
same ADC.

ADCs are one of two types: IPv4 and IPv6. There can be multiple ADCs of each type.

ADCs are similar to ACLs in the following ways:

n ADCs and ACLs are installed in the switch hardware ASIC and share underlying mechanisms and

limitations, including using TCAM entries.

n ADCs and ACLs are defined in switch configuration database in similar ways.

An ADC is composed of one or more ADC entries ordered and prioritized by sequence numbers. The
lowest sequence number is the highest prioritized ADC entry. The ADC processes a packet sequentially
against entries in the list until either the packet matches an ADC entry or the last ADC entry in the list
has been evaluated.

Notes:

n When the agent instantiated from the script that defines the ADC is disabled or deleted, the NAE

deletes the ADC. Disabling or deleting the agent is the only method to delete the ADC.

n If the switch is configured to create an automatic checkpoint (using the checkpoint auto <time>

command), the NAE does not create the ADC.

n The ADCList class includes methods to add entries and to get entries. After an entry is added, it

cannot be modified or deleted.

The following is an example of a script that defines an ADC list and entries:

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

98

| Manifest       | = {                         |          |           |            |       |        |     |             |     |     |
| -------------- | --------------------------- | -------- | --------- | ---------- | ----- | ------ | --- | ----------- | --- | --- |
| 'Name':        | 'adc_hit_counters_monitor', |          |           |            |       |        |     |             |     |     |
| 'Description': |                             | 'Network |           | Analytics  | Agent | Script |     | to monitor' |     |     |
|                |                             | 'ADC     | hit       | counters', |       |        |     |             |     |     |
| 'Version':     |                             | '1.0',   |           |            |       |        |     |             |     |     |
| 'Author':      |                             | 'Aruba   | Networks' |            |       |        |     |             |     |     |
}
| ParameterDefinitions       |                |                            | = {        |     |              |        |        |           |         |             |
| -------------------------- | -------------- | -------------------------- | ---------- | --- | ------------ | ------ | ------ | --------- | ------- | ----------- |
| 'office365_traffic_bound': |                |                            |            |     | {            |        |        |           |         |             |
|                            | 'Name':        | 'office365_traffic_bound', |            |     |              |        |        |           |         |             |
|                            | 'Description': |                            | 'Traffic   |     | flow to/from |        | Office | 365, '    |         |             |
|                            |                |                            | 'paramater |     | options:     | \'to\' | or     | \'from\', | default | is \'to\'', |
|                            | 'Type':        | 'String',                  |            |     |              |        |        |           |         |             |
|                            | 'Default':     | 'to'                       |            |     |              |        |        |           |         |             |
}
}
# IPv4Addresses contains a large list of IP addresses. For readability,
| # a small | sample | of  | addresses | is  | shown | in this | example. |     |     |     |
| --------- | ------ | --- | --------- | --- | ----- | ------- | -------- | --- | --- | --- |
IPv4Addresses = ["13.65.240.22/255.255.255.255", "13.66.58.59/255.255.255.255",
"13.70.156.206/255.255.255.255",
"13.71.145.114/255.255.255.255", "13.71.145.122/255.255.255.255",
"13.71.151.88/255.255.255.255",
"191.237.218.239/255.255.255.255",
"207.46.134.255/255.255.255.255",
"207.46.153.155/255.255.255.255"]
class Agent(NAE):
| def | __init__(self):                                |     |     |     |     |     |     |          |     |     |
| --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
|     | if str(self.params['office365_traffic_bound']) |     |     |     |     |     |     | == 'to': |     |     |
self.adc_outgress = ADCList("office365_outgress", ADCList.Type.IPV4,
| "Traffic | from                  | Office365")                    |                                                          |                      |         |     |        |     |     |     |
| -------- | --------------------- | ------------------------------ | -------------------------------------------------------- | -------------------- | ------- | --- | ------ | --- | --- | --- |
|          | for                   | i in                           | range(0,                                                 | len(IPv4Addresses)): |         |     |        |     |     |     |
|          |                       | entry                          | = ADCEntry(ADCEntry.Type.MATCH).dst_ip(IPv4Addresses[i]) |                      |         |     |        |     |     |     |
|          |                       | self.adc_outgress.add_entry(i, |                                                          |                      |         |     | entry) |     |     |     |
|          | ipv4_outgress_traffic |                                |                                                          |                      | = Rate( |     |        |     |     |     |
"/rest/v1/system/adc_lists/office365_
| outgress/ipv4?attributes=statistics.*", |                            |                                             |     |     |                            | "15s")     |     |             |         |     |
| --------------------------------------- | -------------------------- | ------------------------------------------- | --- | --- | -------------------------- | ---------- | --- | ----------- | ------- | --- |
|                                         | ipv4_outgress_sum          |                                             |     | =   | Sum(ipv4_outgress_traffic) |            |     |             |         |     |
|                                         | self.ipv4_outgress_monitor |                                             |     |     |                            | = Monitor( |     |             |         |     |
|                                         |                            | ipv4_outgress_sum,                          |     |     | "Ipv4                      | Traffic    | to  | Office365") |         |     |
|                                         | elif                       | str(self.params['office365_traffic_bound']) |     |     |                            |            |     | ==          | 'from': |     |
self.adc_ingress = ADCList("office365_ingress", ADCList.Type.IPV4,
| "Traffic | to Office365")       |                               |                                                          |                      |         |     |        |     |     |     |
| -------- | -------------------- | ----------------------------- | -------------------------------------------------------- | -------------------- | ------- | --- | ------ | --- | --- | --- |
|          | for                  | i in                          | range(0,                                                 | len(IPv4Addresses)): |         |     |        |     |     |     |
|          |                      | entry                         | = ADCEntry(ADCEntry.Type.MATCH).src_ip(IPv4Addresses[i]) |                      |         |     |        |     |     |     |
|          |                      | self.adc_ingress.add_entry(i, |                                                          |                      |         |     | entry) |     |     |     |
|          | ipv4_ingress_traffic |                               |                                                          |                      | = Rate( |     |        |     |     |     |
"/rest/v1/system/adc_lists/office365_
| ingress/ipv4?attributes=statistics.*", |                           |                   |     |     |                           | "15s")   |      |             |     |     |
| -------------------------------------- | ------------------------- | ----------------- | --- | --- | ------------------------- | -------- | ---- | ----------- | --- | --- |
|                                        | ipv4_ingress_sum          |                   |     | =   | Sum(ipv4_ingress_traffic) |          |      |             |     |     |
|                                        | self.ipv4_ingress_monitor |                   |     |     | =                         | Monitor( |      |             |     |     |
|                                        |                           | ipv4_ingress_sum, |     |     | "Ipv4                     | Traffic  | from | Office365") |     |     |
else:
|          | raise    | Exception("Invalid |     |         | Parameters, |       | "    |           |         |         |
| -------- | -------- | ------------------ | --- | ------- | ----------- | ----- | ---- | --------- | ------- | ------- |
|          |          |                    |     | "please | create      | agent | with | parameter | 'to' or | 'from', |
| default: | \'to\'") |                    |     |         |             |       |      |           |         |         |
ADCList class
Scripts|99

Syntax

ADCList("<name>", <type>[, "<description>")

Description

Python class for an Analytics Data Collections (ADC) list. Creates and returns the ADC list.

Parameters

<name>

Specifies the name of the list. The format of <name> is a Python text string.

<type>

Specifies the type of ADC.

Valid values are the following:

n ADCList.Type.IPV4

n ADCList.Type.IPV6

<description>

Description of the ADC list. The format of <description> is a Python text string.

Methods

add_entry(<seq>, <adc_entry>)

Adds the ADC entry object <adc_entry> to the ADC list at sequence number <seq>.

The sequence number is a positive integer that is unique within the ADC list. If the sequence number
exists in the ADC list, an agent error is generated. Range: 0 through 4294967295

Example:
self.adc.add_entry(10, entry1)

get_entries()

Returns a Python list of all ADC entries in the ADC list.

Example:
self.adc.get_entries()

Example

self.adc_outgress = ADCList("office365_outgress", ADCList.Type.IPV4, "Traffic from
Office365")

ADCEntry class

Syntax

ADCEntry(<type>)

Description

Python class that represents an entry in an Analytics Data Collections (ADC) list. Creates the ADC entry.

Returns the ADC entry object.

Parameters

<type>

Specifies the action to be taken by the ADC entry.

Valid values are the following:

ADCEntry.Type.MATCH

Update statistics for packets that match this ADC entry.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

100

ADCEntry.Type.IGNORE

Take no action for packets that match this ADC entry.

Methods

src_ip("<IP-ADDR>[/<MASK>]")

Adds the source IP address information to the entry.

Returns the ADC entry object.

<IP-ADDR>

Specifies the IP address.

/<MASK>

Specifies the subnet mask.

Example:
src_ip("10.0.0.1/255.255.255.255")

dst_ip("<IP-ADDR>[/<MASK>]")

Adds the destination IP address information to the entry.

Returns the ADC entry object.

<IP-ADDR>

Specifies the IP address.

/<MASK>

Specifies the subnet mask.

Example:
dst_ip("10.0.0.2/255.255.255.255")

src_port("<PORT>")

Adds the source port information to the entry.

Default: If no source port is specified, traffic ingressing any source port is matched.

Returns the ADC entry object.

<PORT>

Specifies the port number.

Example:
src_port("1/1/2")
src_l4_port(<L4-PORT>)

Adds the layer 4 source port information to the entry.

Returns the ADC entry object.

<L4-PORT>

Specifies the layer 4 port number.

Example:

src_l4_port(6640)

dst_l4_port(<L4-PORT>)

Adds the layer 4 destination port information to the entry.

Returns the ADC entry object.

<L4-PORT>

Specifies the layer 4 port number.

Example:
dst_l4_port(8080)

protocol(<protocol>[, flags={<flags>}])

Adds the network protocol information to the entry, which enables you to match or ignore packets
based on the network protocol used or based on specific protocol flags.

Scripts | 101

Returns the ADC entry object.

<protocol>

Specifies the network protocol.

Use the following value to specify the TCP protocol:
ADCEntry.Protocol.TCP

flags={<flags>}

Sets protocol flags for this ADC entry. Contains a comma-separated list of flag names and values in
the following format:
"<flag-name>": True

If an entry sets multiple flags, the packet matches the entry if all the flag conditions match.

The following flag names are supported for the TCP protocol:

tcp_urg

Urgent.

tcp_ack

Acknowledgment.

tcp_psh

Push buffered data to receiving application.

tcp_rst

Reset the connection.

tcp_syn

Synchronize sequence numbers.

tcp_fin

Finish connection.

tcp_established

Established connection.

Default: No flags are set.

Example:
protocol(ADCEntry.Protocol.TCP, flags={“tcp_ack”: True, “tcp_psh”:
True, “tcp_rst”: True, “tcp_syn”: True, “tcp_fin”: True})

Example

entry1 = ADCEntry(ADCEntry.Type.MATCH).src_ip(     "10.0.0.1/255.255.255.255").dst_ip
("10.0.0.2/255.255.255.255") .protocol(ADCEntry.Protocol.TCP)

Monitors
In a script, a monitor defines what resource the agent will monitor when the agent is enabled on a
switch.

There is no rule that limits how many monitors can be specified in a single script. However the total
number of scripts, agents, and monitors supported depends on the computing capacity of the switch.

A resource is any concept (received packets on a particular interface, user, CPU utilization, and so forth)
that can be addressed and referenced using a URI.

Monitor function

The monitor is defined by the Monitor function, which has the following arguments:

n The item to be monitored—expressed as the REST URI of a system resource. This URI must include a

query string that specifies the attribute or attributes to be monitored.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

102

n IftheURIincludesaparameter,thenameoftheparameter.
n Thenameofthemonitor,whichisastringthatisuniqueamongthemonitorsdefinedinthatscript.
| Intheexample,thenameofthemonitoris:Interface |     |     | Received | Bytes. |
| -------------------------------------------- | --- | --- | -------- | ------ |
ThefollowingisanexampleofamonitorthatusesaparameterfortheresourceID.Themonitor,
namedInterface Received Bytes,recordsthereceivedbytesoftheinterfacethatwillbespecifiedby
theuserwhentheagentiscreated.
self.monitor = Monitor('/rest/v1/system/interfaces/{}?attributes=rx_bytes',
| [self.params['iface_id'] |     | ],name='Interface | Received | Bytes') |
| ------------------------ | --- | ----------------- | -------- | ------- |
Thefollowingisanexampleofthesamemonitorexceptthatitdoesnotuseaparameterforthe
resourceIDoftheinterface.Instead,theresourceIDisdefinedas1%2f1%2f7,whichisthepercent-
encodedrepresentationoftheswitchmember/slot/portnotation:1/1/7.
self.monitor = Monitor('/rest/v1/system/interfaces/1%2f1%2f7?attributes=rx_bytes',
| name='Interface | Received | Bytes') |     |     |
| --------------- | -------- | ------- | --- | --- |
Inthepreviousexample:
n TheURIpathis:/rest/v1/system/interfaces/1%2f1%2f7
n TheresourceIDportionofthepathis:1%2f1%2f7
n TheURIquerystringis:?attributes=rx_bytes
TogettheURIofaresourcetomonitor,youcanusetheAOS-CXRESTAPIReferencebrowserinterface
toaccesstheRESTAPI.FormoreinformationabouttheRESTAPIandtheSwaggerUI,seetheRESTAPI
Guide.
WhenyouspecifythemonitoredURI,youcanalsousevariablestorepresenttheURI.Thisstrategycan
simplifyupdatingascriptwiththeRESTAPIversionchangesortomakecodemorereadablewhenthere
arelongURIpaths.
Forexample:
| #Received | bytes on | a user-specified | interface |     |
| --------- | -------- | ---------------- | --------- | --- |
uri1 = '/rest/v1/system/interfaces/{}?attributes=rx_bytes'
|     | self.m1 = | Monitor( |     |     |
| --- | --------- | -------- | --- | --- |
uri1,
|     | 'Interface | Received Bytes', |     |     |
| --- | ---------- | ---------------- | --- | --- |
[self.params['iface_id']])
| URIs | for monitors |     |     |     |
| ---- | ------------ | --- | --- | --- |
TheURIofamonitoredresourceiscomposedofseveralcomponents,includingthehostnameorhost
IPaddress,thepath,andthequerystringthatspecifiestheattributetomonitor.
InaPythonNAEscript,whenyouspecifytheURIofalocalswitchresourcetomonitor,omittheserver
URLportionoftheURI.SpecifyonlythepathandquerystringportionoftheURI.
Forexample:
| cpu_uri | = '/rest/v1/system/daemons/{}?' |     | \   |     |
| ------- | ------------------------------- | --- | --- | --- |
'attributes=resource_utilization.cpu'
IftheswitchisaVSXswitch,youcanspecifythepeerswitchbyprepending/vsx-peertothepath
portionoftheURI.
Forexample:
| peer_cpu_uri | = '/vsx-peer/rest/v1/system/daemons/{}?' |     |     | \   |
| ------------ | ---------------------------------------- | --- | --- | --- |
'attributes=resource_utilization.cpu'
| Path component |     | of the URI |     |     |
| -------------- | --- | ---------- | --- | --- |
ThepathcomponentoftheURIiseverythingbeforethequestionmark(?)character.Thepathisa
hierarchy.Theforwardslash(/)characterindicatesthehierarchicalrelationshipbetweenresources.
Scripts|103

Because the forward slash character has special meaning, forward slash characters that are part of the
URL path must be percent-encoded, with the code %2F representing the forward slash.

For example, the following URI specifies interface 1/1/5:

/rest/v1/system/interfaces/1%2F1%2F5?attributes=statistics.rx_packets

The path portion of a monitored resource URI can contain the following:

n The wildcard character

n User-defined parameters

Query component of the URI

The query component is sometimes called the query string. In a URI, the question mark (?) character
indicates the beginning of the query component.

The query component of a monitored URI must contain at least one key=value pair. Multiple pairs are
separated by the ampersand (&) character.

The following keys are supported:
attributes

When the key is attributes, value is the name of an attribute. The attribute must be an attribute of
the resource specified by the path component of the URI. Multiple values are supported. Commas
separate the values.

For example:
/rest/v1/system/vlans?depth=1&attributes=id,name,type

When a URI defines a monitor in an Aruba Network Analytics Engine script, attribute values in the
query string support an additional dot notation that the Network Analytics Engine uses to access
additional information. For example:
/rest/v1/system/subsystems/management_module/1%2F5?attributes=resource_utilization.cpu

This dot notation is supported for certain URIs that define monitors in Network Analytics Engine
scripts only.

filter

When the key is filter, value is an attribute-name:attribute-value pair that specifies the name
and value of an attribute. The attribute must be an attribute of the resource specified by the path
component of the URI. Multiple attribute and value pairs are supported. Commas separate the pairs.

For example:

...&filter=type:vlan,admin_state:up

Examples of URIs for monitors

CPU utilization

/rest/v1/system/subsystems/system/base?attributes=resource_utilization.cpu

Memory utilization

/rest/v1/system/subsystems/system/base?attributes=resource_utilization.memory

Packets received on interface 1/1/5

/rest/v1/system/interfaces/1%2F1%2F5?attributes=statistics.rx_packets

Packets transmitted from a user-specified interface

/rest/v1/system/interfaces/{}?attributes=tx_bytes

Link states of all physical interfaces

/rest/v1/system/interfaces/*?attributes=link_state&filter=type:system

Link states of all physical interfaces in a administrative down state

/rest/v1/system/interfaces/*?attributes=link_state&filter=type:system,admin_state:down

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

104

Wildcard characters in monitored URIs

The URI passed to the Monitor function can contain the asterisk (*) wildcard character instead of a
component in the URI path.

For example:

n The following URI specifies the configuration attributes of all interfaces:
"https://192.0.2.5/rest/v1/system/interfaces/*?selector=configuration"

n The following URI specifies all routes regardless of VRF:
"https://192.0.2.5/rest/v1/system/vrfs/*/routes"

You can use wildcard characters in multiple places in the path. For example, the following Monitor
function monitors the connection state of all BGP neighbors belonging to all BGP routers in the "red"
VRF:
self.monitor = Monitor("/system/vrfs/red/bgp_routers/*/

bgp_neighbors/*?attributes=conn_state",
name="BGP Neighbor Connection State")

You cannot use a wildcard character as part of the query string. For example, you cannot use the
wildcard character to specify all attributes of a BGP neighbor.

The wildcard character must replace the entire component in the path. The wildcard character is not
part of a regular expression. For example:

n You can use a wildcard to specify all VRFs, but you cannot use a wildcard character to specify all VRFs

that begin with the letter r.

n You can use a wildcard to specify all interfaces, but you cannot use the wildcard character to specify

the interfaces in member 1, slot 2.

When designing scripts that use wildcard characters in monitored URIs, be aware that using a wildcard character
for certain resources can result in high switch CPU and memory utilization, which can in turn affect the

performance of the switch.

Using a wildcard for resources such as ACLs, interfaces, VLANs, or VRFs, might not result in performance issues in

a customer environment that includes a small number of those resources. However, when the same script is

installed in a customer environment that has a large number of those resources—such as 500 interfaces—

thousands of time series instances are created.

Each monitored resource creates one time series. Each time series requires switch CPU, memory, and storage

space in the time series database. Switch performance can be affected when the resident memory resources

used by the NAE exceeds approximately 500 MB.

Monitoring the count of resources by including the count parameter in the URI—even on thousands of
resources—does not cause performance issues.

Parameters in monitored URIs

You can use user-defined parameters to define the resource ID in the URI passed to the Monitor
function.

For example, instead of creating a monitor for a specific interface on a switch, you can define a
parameter for that interface. Then, when the agent is created, the user supplies the identifier of
interface to be monitored.

Parameters in monitored URIs can only be used to specify resource identifiers, which are the last part of
the path before the query string. Using parameters to specify attributes or other URI components is not
supported.

Parameters are indicated by braces {}.

Scripts | 105

ThefollowingexampleshowstheuseofaparameterfortheIDofaninterface:
self.monitor = Monitor("/system/interfaces/{}?attributes=rx_bytes",
|     |     | [self.params["iface_id"] |     |     |     | ],name="Interface | Received Bytes") |
| --- | --- | ------------------------ | --- | --- | --- | ----------------- | ---------------- |
Intheexample:
n IntheURI,insteadofspecifyingaspecificinterface,theURIcontainsthefollowingcharactersto
indicatethataparameterisexpected:
{}
Thefollowingargumentindicatesthatthenameoftheuser-definedparameterisiface_id:
n
| [self.params["iface_id"] |     |     | ],  |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- |
n Theiface_idparameterisdefinedintheParameterDefinitionsportionofthescript:
| ParameterDefinitions |                    | =       | {          |     |                |     |     |
| -------------------- | ------------------ | ------- | ---------- | --- | -------------- | --- | --- |
| 'iface_id':          | {                  |         |            |     |                |     |     |
|                      | 'Name': 'Interface |         | Id',       |     |                |     |     |
|                      | 'Description':     |         | 'Interface | to  | be monitored', |     |     |
|                      | 'Type': 'string',  |         |            |     |                |     |     |
|                      | 'Default':         | '1/1/1' |            |     |                |     |     |
}
| Examples | of invalid | parameter |     | definitions |     |     |     |
| -------- | ---------- | --------- | --- | ----------- | --- | --- | --- |
Thefollowingparameterdefinitionisinvalidbecauseitattemptstocreateaparameterforanattribute,
suchasreceivedbytesortransmittedbytes:
| # Example | of invalid | parameter |     | usage: | attribute |     |     |
| --------- | ---------- | --------- | --- | ------ | --------- | --- | --- |
self.monitor = Monitor("/system/interfaces/1%2F1%2F5?attributes={}",
| [self.params["attr"] |     | ],  | name="Interface |     | Received | Bytes") |     |
| -------------------- | --- | --- | --------------- | --- | -------- | ------- | --- |
Thefollowingparameterdefinitionisinvalidbecauseitattemptstocreateaparameterforacomponent
oftheURIthatisnottheresourceID:
| # Example | of invalid | parameter: |     | URI component |     | not resource | ID  |
| --------- | ---------- | ---------- | --- | ------------- | --- | ------------ | --- |
self.monitor = Monitor("/system/{}/1%2F1%2F5?attributes=rx_bytes",
| [self.params["resource"] |                |     | ],name="Interface |      |     | Received Bytes") |     |
| ------------------------ | -------------- | --- | ----------------- | ---- | --- | ---------------- | --- |
| Slash                    | (/) characters | in  | monitored         | URIs |     |                  |     |
ToavoidmistakenlyinterpretingslashesinresourceIDaspartoftheURIpath,slash(/)charactersina
resourceIDthatisnotauser-definableparametermustbeencodedas:%2for%2F.
InthepathcomponentofaURI,theslash(/)characterisareservedcharacterthatisadelimiter
betweenpathsegments.Forexample:
path/to/resourceID
Resourcesonaswitchmightalsousetheslashcharacterintheiridentifications.Forexample:
n Aninterfacemightbeidentifiedbyamember/slot/portnotation,suchas:1/1/7
n Apowersupplyunitmightbeidentifiedbyamember/PSUnotation,suchas:1/3
TocorrectlyspecifyaresourceIDinamonitoredURIthatdoesnotincludeparameters,youmust
substitute%2for%2FforeachslashcharacterintheresourceID.
Thefollowingexampleshowsthedefinitionofamonitorforinterface1/1/7anddoesnotusea
parameterfortheresourceID:
self.monitor = Monitor('/rest/v1/system/interfaces/1%2f1%2f7?attributes=tx_bytes',
| 'Monitored | interface') |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- | --- |
Ifthescriptdefinesauser-definedparametertospecifytheresourceID,URLencodingfortheslash
characterisnotusedwhenspecifyingthedefaultvalue.Likewise,whenauserentersavalueforthat
parameter,theydonothavetouseURLencodingfortheslashcharacterbecausetheWebUI
automaticallyusesURLencodingwhenstoringthevalue.
106
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

Thefollowingexampleshowspartsofascriptthatdefinesinterface_idasauser-definedparameter
andthenpassesthatparametertoaMonitorfunctionandtoanActionCLIfunction.
| ParameterDefinitions |                |     |            | = {         |           |           |            |
| -------------------- | -------------- | --- | ---------- | ----------- | --------- | --------- | ---------- |
| 'interface_id':      |                |     | {          |             |           |           |            |
|                      | 'Name':        |     | 'Monitored | Interface', |           |           |            |
|                      | 'Description': |     |            | 'The        | id of the | monitored | interface, |
|                      | 'Type':        |     | 'string',  |             |           |           |            |
|                      | 'Default':     |     | '1/1/1'    |             |           |           |            |
}
}
...
| self.monitor |     | = Monitor( |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | --- | --- |
'/rest/v1/system/interfaces/{}?attributes=tx_bytes',
| 'Monitored |     | interface', |     |     |     |     |     |
| ---------- | --- | ----------- | --- | --- | --- | --- | --- |
[ self.params['interface_id']])
...
| ActionCLI('show |     |     | interface | {}', | [self.params['interface_id']] |     |     |
| --------------- | --- | --- | --------- | ---- | ----------------------------- | --- | --- |
...
| Attribute |     | filters | in monitored |     | URIs |     |     |
| --------- | --- | ------- | ------------ | --- | ---- | --- | --- |
Sometypesofattributescanbefilteredfurtherbyspecifyinganattributenameandvaluepairinstead
ofjustanattributename.
Forexample,youmightwanttospecifythatonlyphysicalinterfacesbemonitored.Thereisnowayto
specifyonlythephysicalinterfacesintheURIpath.However,physicalinterfaceshaveanattributecalled
type,whichhasavalueofsystem.
Thefilterkeywordindicatesthatthevaluethatfollowstheequalsign(=)isanattributeandvaluepair.
Thefilteredattributemustbethenameofanattributeoftheresourcespecifiedbythepathcomponent
oftheURI.
Theattributemustbeoneofthefollowingdatatypes:
n integer
string
n
n boolean
Forinformationaboutthenames,types,andvaluesofattributesofaresource,seetheAOS-CXRESTAPI
Reference.
Thesyntaxoftheattributeandvaluepairisthefollowing:
attribute-name:attribute-value
Multipleattributeandvaluepairsaresupported.Commasseparatethepairs.Forexample:
...&filter=type:vlan,admin_state:up
Examples
ThefollowingexampleshowsamonitoredURIthatspecifiesthereceivedpacketsofallphysical
interfaces.
uri1 = '/rest/v1/system/interfaces/*?attributes=statistics.rx_packets&filter=type:system'
| self.m1 | = Monitor(uri1, |     |     | 'rx | on all | physical | interfaces') |
| ------- | --------------- | --- | --- | --- | ------ | -------- | ------------ |
ThefollowingexampleshowsamonitoredURIthatspecifiesthereceivedpacketsofVLANinterfaces
thatareinanupstate.
uri2 = '/rest/v1/system/interfaces/*?attributes=statistics.rx_
packets&filter=type:vlan,admin_state:up'
| self.m2      | = Monitor(uri2, |       |       | 'rx | on UP VLAN | interfaces') |           |
| ------------ | --------------- | ----- | ----- | --- | ---------- | ------------ | --------- |
| Constructing |                 | a URI | using | the | AOS-CX     | REST API     | Reference |
Scripts|107

To construct the URI of a resource to monitor, you can use the GET method in the AOS-CX REST API
Reference to generate most of the URI. However, to do the following, you must edit the URL you copy
and paste.

n Use the dot notation to specify a component of an attribute.

n Use a filter to specify an attribute name and value pair.

Procedure

1. Log into the switch from the AOS-CX REST API Reference:

a. Use a supported browser to access the switch at: https://<IP-ADDR>/api/

<IP-ADDR> is the IP address or hostname of your switch.

b. Expand the Login resource by clicking the resource name, /login, or by clicking Expand

Operations.

c. Enter your user name in the value of the username parameter.
d. Enter your password in the value of the password parameter.
e. Click Submit.

2. To expand the possible endpoints of a resource, click the resource name.

For example, CPU utilization is a kind of resource utilization, which is part of the subsystems
resource collection:

3. Click the endpoint in the GET method to expand the collection.

4. Navigate to the Parameters section and select the attribute or attributes you want to display.

You can select multiple attributes:

n To select a range of attributes, click the first attribute, then press Shift, and then click the last

attribute in the range you want to select.

n To select attributes that are not adjacent in the list, press Ctrl, then click each attribute you

want to select.

5. Click Submit.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

108

The displayed information expands to show the curl command equivalent, the request URL, and
the response body.

In the following example, the IP address of the switch is hidden by the gray box, and the response
body is not shown.

6. Construct the monitor URI from the Request URL and the Response Body (if needed).

a. Copy and paste the Request URL into your script.
b. Remove the server information and any other information you specify elsewhere (such as the

REST API version).

For example, the resulting URI is:
/rest/v1/system/subsystems?attributes=resource_utilization
If you are specifying subcomponent of the attribute, view the Response Body and record the
exact name of the attribute component to add to the query portion of the URI.

c.

For URIs specifying monitors only, you can specify components within attributes by using a
"dot" notation after the attribute name.

For example, In the Response Body, the CPU utilization is part of the resource_utilization
resource. You can specify that only the CPU resources be monitored by adding .cpu after the
attribute name. For example: resource_utilization.cpu.

The resulting example URI to monitoring CPU utilization is the following:
/rest/v1/system/subsystems?attributes=resource_utilization.cpu

d.

If you want to use the filter to specify both an attribute and a value, you must edit the URI to
use the filter keyword and specify the attribute name and the attribute value.

Aggregate operators

Aggregate operators are aggregate operations that can be computed independently of the passage of
time.

Transition and ratio calculations are not considered aggregate operators.

If the monitored URI includes parameters and the monitor is an aggregate operator, the parameter
must be passed to the aggregate operator instead of to the Monitor function.

In the examples of the functions, uri2 is the following:
uri2 = '/rest/v1/system?attributes=resource_utilization_poll_interval'

Scripts | 109

The aggregate operators are the following:
Count

Counts the number of distinct time-series data points that have been generated and implicitly
reflects the count of data points collected at every data collection interval.

Example:

count_m = Count(uri2)

self.m11 = Monitor(count_m, name='Resource Utilization Poll Interval')

Sum

Calculates the sum of the monitored resource values. When the monitored URI contains wildcard
characters, this function sums over the current values of all resources pointed to by expanding the
wildcards.

Example:

sum_m = Sum(uri2)

self.m9 = Monitor(sum_m, name='Resource Utilization Poll Interval')

Min or Max

Calculates the minimum or maximum of the monitored resource values. When the monitored URI
contains wildcard characters, this function returns the minimum or maximum value over the current
values of all resources pointed to by expanding the wildcards.

Example Max:

max_m = Max(uri2)

self.m15 = Monitor(max_m, name='Resource Utilization Poll Interval')

Average

Calculates the average of the monitored resource values. When the monitored URI contains wildcard
characters, this function calculates and returns the average value over the current values of all
resources pointed to by expanding the wildcards.

Example:

avg_m = Average(uri2)

self.m17 = Monitor(avg_m, name='Resource Utilization Poll Interval')

Aggregate functions

Aggregate functions are time-dependent and are computed over a time interval. Aggregate functions
include the rate function and functions with names that include the keyword OverTime. Aggregate
functions must specify a time interval.

Transition and ratio calculations are not considered aggregate functions.

If the monitored URI includes parameters and the monitor is an aggregate function, the parameter must
be passed to the aggregate function instead of to the Monitor function.

For example:
uri2 = '/rest/v1/system/interfaces/{}?attributes=statistics.rx_packets'
avg_m = AverageOverTime(uri2, "1 hour", [self.params['interface_id']])
self.m2 = Monitor(avg_m, 'Rx Packets')

In the examples of the functions, uri2 is the following:
uri2 = '/rest/v1/system?attributes=resource_utilization_poll_interval'

The aggregate functions are the following:
CountOverTime

Counts the number of distinct time-series data points that have been generated during the specified
period of time.

Example CountOverTime:

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

110

| count_over_m | = CountOverTime(uri2, |     | "5  | minutes") |     |
| ------------ | --------------------- | --- | --- | --------- | --- |
self.m2 = Monitor(
|     | count_over_m, | name='Resource |     | Utilization | Poll Interval') |
| --- | ------------- | -------------- | --- | ----------- | --------------- |
SumOverTime
Calculatesthesumofthemonitoredresourcevaluesthatoccurredduringthespecifiedperiodof
time.WhenthemonitoredURIcontainswildcardcharacters,thisfunctionsumsoverthecurrent
valuesofallresourcespointedtobyexpandingthewildcards.
ExampleSumOverTime:
| sum_over_m | = SumOverTime(uri2, |                | "5 minutes") |             |                 |
| ---------- | ------------------- | -------------- | ------------ | ----------- | --------------- |
|            | self.m10 = Monitor( |                |              |             |                 |
|            | sum_over_m,         | name='Resource |              | Utilization | Poll Interval') |
MinOverTime
Calculatestheminimumofthemonitoredresourcevalues.WhenthemonitoredURIcontains
wildcardcharacters,thisfunctionreturnstheminimumvalueoverthecurrentvaluesofallresources
pointedtobyexpandingthewildcards.
ExampleMinOverTime:
| min_over_m | = MinOverTime(uri2, |     | "5 minutes") |     |     |
| ---------- | ------------------- | --- | ------------ | --- | --- |
self.m2 = Monitor(
|     | min_over_m, | name='Resource |     | Utilization | Poll Interval') |
| --- | ----------- | -------------- | --- | ----------- | --------------- |
MaxOverTime
Calculatesthemaximumofthemonitoredresourcevalues.WhenthemonitoredURIcontains
wildcardcharacters,thisfunctionreturnsthemaximumvalueoverthecurrentvaluesofall
resourcespointedtobyexpandingthewildcards.
Example:MaxOverTime:
| max_over_m | = MaxOverTime(uri2, |                | "5 minutes") |             |                 |
| ---------- | ------------------- | -------------- | ------------ | ----------- | --------------- |
|            | self.m16 = Monitor( |                |              |             |                 |
|            | max_over_m,         | name='Resource |              | Utilization | Poll Interval') |
AverageOverTime
Calculatestheaverageofthemonitoredresourcevaluesoverthespecifiedperiodoftime.Whenthe
monitoredURIcontainswildcardcharacters,thisfunctioncalculatesandreturnstheaveragevalue
overthecurrentvaluesofallresourcespointedtobyexpandingthewildcards.
ExampleAverageOverTime:
| avg_over_m | = AverageOverTime(uri2, |                | "5  | minutes")   |                 |
| ---------- | ----------------------- | -------------- | --- | ----------- | --------------- |
|            | self.m18 = Monitor(     |                |     |             |                 |
|            | avg_over_m,             | name='Resource |     | Utilization | Poll Interval') |
Rate
Calculatestheper-secondaveragerateofincreaseforthemonitoredresourcevalueoverthe
specifiedperiodoftime.WhenthemonitoredURIcontainswildcardcharacters,thisfunction
calculatestheper-secondaveragerateofincreaseforeachofthemonitoredresourcespointedtoby
expandingthewildcards.
Example:
| rate_m = | Rate(uri2, "5 | minutes") |     |     |     |
| -------- | ------------- | --------- | --- | --- | --- |
self.m8 = Monitor(rate_m, name='Resource Utilization Poll Interval')
Time interval
Theformatofthetimeintervalisthefollowing:
"<number> <unit>"
Scripts|111

The value for <unit> is one of the following:

n second

n seconds

n minute

n minutes

n day

n days

n hour

n hours

For example: "12 seconds"

Nested aggregate functions and operators

Nesting an aggregate function or operator inside of an aggregate function enables you to combine the
capabilities of both to create one result. The nested function or operator is executed first, and then the
enclosing operator is executed.

For example, the following nested function calculates the rate of the switch resource and sums the
calculated rates across all the URIs pointed to by the expanded wildcard:

Sum(Rate(<uri-with-wildcard>))

Rules

n You can nest up to one aggregate function or aggregate operator inside an aggregate operator.

For example: Min(CountOverTime(<uri>)) and Min(Sum(<uri>)) are supported.

n You cannot nest an aggregate operator or aggregate function inside an aggregate function.

For example, Rate(Sum(<uri>)) and CountOverTime(Min(<uri>)) are not supported.

n You cannot nest two of the same aggregate operators.

For example, Sum(Sum(<uri>)) is not supported.

Aggregate functions in monitors and conditions

If an aggregate function or operator is used in the definition of the monitor, an aggregate function or
operator can not be used in a condition expression for that monitor.

If the aggregate function is defined at monitor level, the time series graph for the monitored resource is
a graph of the results of that aggregate function. In contrast, if the aggregate function is used in the
condition expression, the time series graph for the agent in the Web UI is based on raw data.

The following example shows an aggregate function, Average(uri), that is defined in the monitor. The
function uses the wildcard to average the received packets from all the interfaces, resulting in a graph
with a single curve, and triggering an alert when that average is over 50.
uri = '/rest/v1/system/interfaces/*?attributes=statistics.rx_packets'
avg = Average(uri)
self.monitor1 = Monitor(avg, name='Average Rx Packets on All Interfaces')
self.rule1 = Rule('Rx Packets')
self.rule1.condition('{} > 50', [self.monitor1])

The following example shows the avg aggregate function used in a condition expression. The monitor
results in a graph that has multiple curves, with one curve corresponding to each interface received
packet value. In the example, the condition self.rule2.condition triggers an alert when the average of
received packets on an interface becomes greater than 50 within the past five minutes.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

112

uri = '/rest/v1/system/interfaces/*?attributes=statistics.rx_packets'
avg = AverageOverTime(uri, "5 minutes")
self.monitor2 = Monitor(uri, name='Rx Packets on All Interfaces')
self.rule2 = Rule('Rx Packets')
self.rule2.condition('avg {} > 50', [self.monitor2])

Rules
Rules are optional components of the agent constructor, which is the main body of the Aruba Network
Analytics Engine script.

When you monitor something on a switch, you can define rules to execute actions when certain
conditions are true. For example, you might define a rule to send a message to the system log when
CPU utilization exceeds 90% of capacity.

A script can have multiple rules using any combination of monitors previously specified on the script. A
rule must include a condition, but actions are not required. A rule that does not include actions do not
generate an alert when a condition transitions to true or to false.

A rule consists of the following components:

n The Rule function, to which a text string identifying the rule is passed as an argument. For example:
Rule('High CPU utilization by ' + daemon_name)

n A condition, defined by the condition function of the rule.

n Zero or more actions, each of which is defined by the action function of the rule. Actions are

executed if the condition transitions from false to true.

n Zero or more clear actions, each of which is defined by the clear_action function of the rule. Clear

actions are executed if the condition transitions from true to false.

self.r1 = Rule('Minor CPU Utilization')
self.r1.condition(

'{} >= {}',
[self.m1,

self.params['minor_threshold']])
self.r1.action(self.action_minor_avg_cpu)
self.r1.clear_action(self.action_clear_minor_avg_cpu)

You can also create time-based rules that execute actions at a regular interval instead of in response to
the conditions of a monitored URI.

For example, you can use the every keyword to create a rule that executes an action every 60 seconds:
self.r1 = Rule("Periodic callback")
self.r1.condition("every 60 seconds")
self.r1.action(self.my_periodic_callback)

You can use parameters to make the interval configurable. However time-based rules do not support
clear conditions, conjunction operators, or disjunction operators.

Conditions
The condition and the clear condition are the part of the rule that determines which actions are
executed.

When an agent is created, the condition associated with the rule is active and the clear condition is
inactive. Time series data is collected every 5 seconds. Conditions and clear conditions—if any—are
evaluated at each time series data collection point.

When the condition is active and transitions from false to true:

Scripts | 113

n The rule actions, if any, are executed.

n The condition becomes inactive. The condition does not become active again until the clear condition

is true and becomes inactive.

n The clear condition becomes active.

When the clear condition is active and transitions from false to true:

n The clear actions, if any, are executed.

n The clear condition becomes inactive.

n The condition becomes active.

A condition can contain any number of monitors in its expression.

The following is an example of a condition in a rule:
# Monitoring average cpu value crossing 'minor_threshold' value that is set

# over a given time interval
self.r1.condition(

'{} >= {}',
[self.m1,

self.params['minor_threshold']])
self.r1.action(self.action_minor_avg_cpu)
self.r1.clear_action(self.action_clear_minor_avg_cpu)

The condition function contains the condition expression (in quotes) and, optionally, any parameters
used in the condition expression.

In the example, the condition expression is relatively simple. The condition expression uses the >=
operator to compare the current CPU value to the value of the minor_threshold parameter.

Condition and clear condition expressions can be complex and include aggregation functions, pauses
and durations in monitoring, and support for time-series data.

Clear conditions

The clear condition is an optional part of the rule that determines when a network condition or event is
no longer occurring.

When an agent is created, the condition associated with the rule is active and the clear condition is
inactive. When the condition becomes true:

n The condition becomes inactive and the clear condition becomes active.

n The condition does not become active again until the clear condition is true.

Using a clear condition can help to prevent the numerous alerts that can occur when monitored data
fluctuates narrowly above and below the threshold.

For example, consider a rule that sets the alert level to critical when CPU utilization exceeds 90%, and
removes the alert level when the condition is no longer true.

n If you do not define a clear condition and the CPU utilization frequently fluctuates between 85% and
91%, the monitor generates alerts and then removes the alert level every time the fluctuation occurs.

n Instead, if you define a clear condition to be when the CPU utilization drops below 70%, the following

behavior occurs:

o The first time the CPU utilization exceeds 90%, the alert level is set to critical. The condition

becomes inactive and it is no longer evaluated. Instead, the clear condition becomes active, and is
evaluated at regular intervals.

o The CPU utilization can fluctuate from above 90% to as low as 70%, an unlimited number of times.

The alert level remains critical and additional alerts are not generated.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

114

o Theclearaction—removingthealertlevel—isexecutedonlywhentheclearconditionbecomes
true—theCPUutilizationdropsbelow70%.Theclearconditionbecomesinactiveandisnolonger
evaluated.Theconditionbecomesactiveagainandisevaluatedatregularintervals.
Ineffect,oneofthewaysyoucanuseaclearconditionistouseitincombinationwiththeconditionto
setbothahighthresholdandalowthreshold.
Youdefineaclearconditionusingtheclear_conditionfunction.Theclear_conditionfunction
containstheconditionexpression(inquotes)and,optionally,anyparametersusedinthecondition
expression.
Exampleofaclearconditioninamonitor:
self.monitor = Monitor(AverageOverTime("/rest/v1/system/subsystems/management_
module/1%2F5?attributes=resource_utilization.cpu", "5 minutes")
| self.rule                       | = Rule("") |     |      |                      |                 |     |     |     |
| ------------------------------- | ---------- | --- | ---- | -------------------- | --------------- | --- | --- | --- |
| self.rule.condition("{}         |            | >   | 90", | [self.monitor])      |                 |     |     |     |
| seld.rule.action("ALERT_LEVEL", |            |     |      | AlertLevel.CRITICAL) |                 |     |     |     |
| self.rule.clear_condition("{}   |            |     |      | < 70",               | [self.monitor]) |     |     |     |
self.rule.clear_action(self.set_normal)
| Condition | expression |     | syntax |     |     |     |     |     |
| --------- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
Theconditionofaruleisaone-lineexpressionthatusesthefollowingsyntax,expressedinEBNF
(ExtendedBackus-Naur)notation:
| uri          | = ? https://tools.ietf.org/html/rfc3986 |           |           |         |                |         | ?         |         |
| ------------ | --------------------------------------- | --------- | --------- | ------- | -------------- | ------- | --------- | ------- |
| enum         | = ? string                              | ?         |           |         |                |         |           |         |
| integer      | = ? signed                              | int64     |           | ?       |                |         |           |         |
| list_element | = '"' ,                                 | ( enum    | |         | integer | )              | , '"'   |           |         |
| list         | = list_element                          |           | ,         | { ","   | , list_element |         | }         |         |
| operator     | = "<" |                                 | ">"       | | "=="    | | "!="  | |              | "<=" |  | ">="      |         |
| over         | = "over"                                | , integer |           | , time  |                |         |           |         |
| for          | = "for"                                 | , integer |           | , time  |                |         |           |         |
| time         | = "second"                              | |         | "seconds" |         | | "minute"     | |       | "minutes" | | "day" |
|              | | "days"                                | |         | "hour"    | |       | "hours"        | | "day" | | "days"  |         |
| aggregator   | = "count"                               | |         | "sum"     | | "min" | |              | "max" | | "avg"     |         |
| pause        | = "pause"                               | ,         | integer   | ,       | time           |         |           |         |
| operation1   | = uri ,                                 | operator  |           | , list  | , [ for        | ] ,     | [ pause   | ]       |
operation2 = aggregator , [ over ] , uri , operator , integer ,
|     | [ for | ] , | [ pause | ]   |     |     |     |     |
| --- | ----- | --- | ------- | --- | --- | --- | --- | --- |
operation3 = "rate" , uri, "per" , integer , time , operator , float ,
|     | [ for | ] , | [ pause | ]   |     |     |     |     |
| --- | ----- | --- | ------- | --- | --- | --- | --- | --- |
operation4 = "transition" , uri , "from" , list , "to" , list
operation5 = "ratio", "of", uri, "and", uri | integer, operator, integer,
|            | [ for      | ] ,      | [ pause | ]    |     |     |     |     |
| ---------- | ---------- | -------- | ------- | ---- | --- | --- | --- | --- |
| operation6 | = "every", | integer, |         | time |     |     |     |     |
Aconditionexpressioncanbeonlyintheformatdescribedbytheoperationsoperation1through
operation6.
Inoperation1,the>,<,<=,and>=operatorscannotbeappliediflisttokenisoftypeenum.
ThebehaviorsofthesupportedfunctionsdependonwhetherthemonitoredURIcontainswildcards.
Ifanaggregationfunctionisusedinthedefinitionofthemonitor,theequivalentaggregationfunction
cannotbeusedinaconditionexpressionforthatmonitor.
Durations, evaluation delays, and pauses in condition expressions
Thefollowingarethebehaviorswhenconditionexpressionincludesdurationsandeitherevaluation
delaysorevaluationpauses.
Adurationisannumberfollowedbyaspacefollowedbyoneofthevaluesforthetimekeyword.
| for followed | by a duration |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
Scripts|115

If a condition expression has the for keyword followed by a duration, the expression will be
evaluated and monitored for that particular duration before the condition is considered true and
any rule actions are executed.

For example, the following condition expression is true only if the count of the conn_state has been
less than 5 for three minutes:
count /v1/system/vrfs/red/bgp_routers/bgp_neighbors/?attributes=conn_state < 5 for 3
minutes

pause followed by a duration

If a condition expression has the pause keyword followed by a duration, the condition will not be
monitored for the specified duration after the condition is met. However, because the condition is
true, any rule actions are executed before monitoring is paused.

For example, the following condition expression specifies that the spanning tree tcn_count will not
be monitored for one minute after the tcn_count is greater than 10.
/v1/system/vlan/1/spanning_tree/tcn_count > 10 pause 1 minute

Using these kinds of expressions can reduce the number of actions taken—such as log entries
generated—when a network condition is temporary, but still ensure that actions are taken at
intervals the administrator considers to be reasonable.

Examples
rate /v1/system?attributes=resource_utilization_poll_interval > 300 per 1 hour for 5
hours

rate /v1/system?attributes=resource_utilization_poll_interval > 300 per 2 hours for 5
days

avg over 1 minute /v1/system/interface/1?attributes=statistics.tx_dropped < 5 for 2
minutes

rate /v1/system?attributes=resource_utilization_poll_interval > 300 per 10 seconds for 5
minutes

avg over 1 minute /v1/system/interface/1?attributes=statistics.tx_dropped < 5 for 2
minutes pause 10 seconds

Conjunction (AND), disjunction (OR), and multiple subconditions

When you define a condition, you can create an expression that combines multiple subcondition
expressions using the operators AND, OR, and parenthesis.

The condition function returns true if the combination of the subconditions is true.

Operator precedence:

1. Parenthesis operator: ()

2. AND operator

3. OR operator

For example, consider the following expression:
SubCondition1 AND SubCondition2 OR Subcondition3

Because there are no parentheses in this expression, the AND operation is evaluated first. The result of
that evaluation is then evaluated against Subcondition3 using the OR operator. The condition function
returns the result of the second evaluation. The following table shows the results according to the
evaluation of each subcondition:

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

116

| Subcondition1 |     | Subcondition2 | Subcondition3 |     | Result |
| ------------- | --- | ------------- | ------------- | --- | ------ |
| true          |     | true          | false         |     | true   |
| true          |     | false         | false         |     | false  |
| false         |     | true          | false         |     | false  |
| false         |     | false         | false         |     | false  |
| true          |     | true          | true          |     | true   |
| true          |     | false         | true          |     | true   |
| false         |     | true          | true          |     | true   |
| false         |     | false         | true          |     | true   |
Thefollowingexampleshowsaconditionwiththreedifferentsubconditions:
1. ResourceUtilizationPollInterval>50
2. Spanningtreehellotime>5
3. VLANadminstatus=down
Example:
uri1 = '/rest/v1/system?attributes=resource_utilization_poll_interval'
self.m1 = Monitor(uri1, name='Resource Utilization Poll Interval')
uri2 = '/rest/v1/system?attributes=stp_config.hello_time'
| self.m2 | = Monitor(uri2, | name='Spanning | tree hello | time') |     |
| ------- | --------------- | -------------- | ---------- | ------ | --- |
uri3 = '/rest/v1/system/vlans/{}?attributes=admin'
self.m3 = Monitor(uri3, 'Vlan admin status', [self.params['vlan_id']])
| self.r1 | = Rule("Rule | 1") |     |     |     |
| ------- | ------------ | --- | --- | --- | --- |
self.r1.condition('({} > 50 AND {} > 5) OR {} == "down"', [self.m1, self.m2, self.m3])
self.r1.action(self.action_callback1)
Function behavior when monitored URI does not contain wildcards
Thefollowingarethebehaviorsofthesupportedconditionexpressionfunctionswhenthemonitored
URIdoesnotcontainwildcards—andthuspointstoonespecificresource:
count
Thisfunctioncountsthenumberofdistincttime-seriesdatapointsthathavebeengeneratedand
implicitlyreflectsthe"count"ofdatapointscollectedateachdatacollectioninterval.
Forexample,applyingthecountfunctiontothefollowingURIresultsinavalueof1.
/rest/v1/system/subsystems/chassis/base?attributes=resource_utilization.cpu
| sum, min, | max,and | avg |     |     |     |
| --------- | ------- | --- | --- | --- | --- |
Becausethereisjustoneresource,theseaggregatorsreturnthecurrentvalueoftheresource.These
aggregatorsonlyapplytoresourcesrepresentedbyintegers,suchasnumberofpacketsreceivedor
CPUutilization.
| Aggregator | over | time |     |     |     |
| ---------- | ---- | ---- | --- | --- | --- |
Whenthekeywordoverfollowsoneoftheaggregators,thefunctionbehavesinasimilarwaybut
performsitsaggregation"over"thespecifiedtimeinthepastinsteadofoverthecurrentvalueonly.
Scripts|117

rate

The rate function calculates the per-second average rate of increase of the monitored resource.

For example, applying the rate function to the following URI calculates the per-second average of the
received packets on interface 1/1/5 for the last one minute:
/rest/v1/system/interfaces/1%2F1%2F5?attributes=statistics.rx_packets per 1 minute

transition

The transition evaluates to true if the specified resource changes state as defined.

The transition function only applies to columns of type boolean, enum, and list.

For example, the following expression is true when port 1/1/5 goes down:
transition /rest/v1/system/ports/1%2F1%2F5?attributes=admin from "up" to "down"

ratio

The ratio function calculates the ratio between numerator and denominator of the specified
resource.

The ratio function only applies to columns of type integer and has the restriction that the part of
URI preceding the token '?' be the same. That is, the ratio function can calculate the ratio between
two attributes of the same resource, but not between attributes of different resources.

For example, to determine the ratio of the received packets to transmitted packets for interface
1/1/5, use the following expression:

ratio of /rest/v1/system/interfaces/1%2F1%2F5?attributes=statistics.rx_packets and
/rest/v1/system/interfaces/1%2F1%2F5?attributes=statistics.tx_packets

Function behavior when monitored URI has wildcards

The following are the behaviors of the supported condition expression functions when the monitored
URI contains wildcards and thus points more than one resource:
count

This function counts the number of distinct time-series data points that have been generated and
implicitly reflects the "count" of data points collected at each data collection interval.

For example, the count function applied to the following URI results in the number of subsystems
that are present:

/rest/v1/system/subsystems/*/base?attributes=resource_utilization.cpu

sum

When the monitored URI contains wildcards, this function sums over the current values of all
resources pointed to by expanding the wildcard. This function only applies to columns of type
integer.

For example, the sum function applied to the following URI is the sum total of the value of the CPU
utilization of all subsystems configured in the system.
/rest/v1/system/subsystems/*/base?attributes=resource_utilization.cpu

min and max

When the monitored URI contains wildcards, these functions return the minimum or maximum of
the current value of all currently present resources pointed to by expanding the wildcard. This
function only applies to columns of type integer.

For example, the min function applied to the following URI returns the current minimum number of
received packets across all configured interfaces. In other words, you can use this function to
determine which interface received the fewest number of packets at this evaluation point.

/rest/v1/system/interfaces/*?attributes=statistics.rx_packets

avg

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

118

This function performs an average over the current values of all currently present resources pointed
to by expanding the wildcard. This function only applies to columns of type integer.

For example, the avg function applied to the following URI returns the average number of
transmitted packets across all configured interfaces:

/rest/v1/system/interfaces/*?attributes=statistics.tx_packets

Aggregator over time

When the keyword over follows one of the aggregators, the function behaves in a similar way but
performs its aggregation "over" the specified time in the past instead of over the current value only.
When the URI contains wildcards, the computation happens over each resource represented by the
wildcard.

rate

The rate function calculates the per-second average rate of increase for each of the monitored
resources.

For example, if interfaces 1/1/5 and 1/1/6 have been configured, using the following expression
returns the ratio of received packets to transmitted packets for each of the two interfaces:

/rest/v1/system/interfaces/*?attributes=statistics.rx_packets per 1 minute

transition

Similar to rate, the transition function finds the transitions for each of the resources pointed to by
expanding the wildcard in the monitored URI.

The transition function only applies to columns of type boolean, enum, and list.

For example, the following expression is true for every configured port that goes down:

transition(/rest/v1/system/ports/*?attributes=admin) from "up" to "down"

ratio

The ratio function finds the ratio between numerator and denominator for each of the resources
pointed to by expanding the wildcard.

For example, if interfaces 1/1/5 and 1/1/6 have been configured, using the following expression
returns the ratio of received packets to transmitted packets for each of the two interfaces:

ratio of /rest/v1/system/interfaces/*?attributes=statistics.rx_packets and

/rest/v1/system/interfaces/*?attributes=statistics.tx_packets

Actions
Actions are executed depending on the truth value of the condition in a rule.

Actions might include things like setting the agent status, executing certain CLI commands, or
generating system log messages.

Types of actions include the following:

Predefined action

Predefined actions are actions that are built in to the Aruba Network Analytics Engine framework.

Callback actions

Callback actions are callback functions defined in the script to perform additional processing.

Clear actions

Clear actions are predefined actions or callback actions that are executed only when the clear
condition of a rule is active and transitions from false to true.

Predefined actions

Scripts | 119

Predefined actions are action functions that are built in to the Aruba Network Analytics Engine
framework. These functions enable the agents of a script to do the following:

n Execute CLI commands in the AOS-CX network operating system.

n Execute shell commands in the underlying operating system of the switch.

n Send messages to the system log.

n Generate custom reports that communicate information collected by the agent.

ActionCLI, CLI action

Syntax

Inside a callback action:
ActionCLI("<command>"[, title=<title>])

Outside of a callback action:
self.r.action("CLI","<command>"[, title=<title>])

Description

The CLI action executes the specified command from the switch CLI.

Parameters

<command>

A text string of the CLI command as it would be entered at a switch prompt. Examples:

n show vlan 100

n show running-config

n top memory

The string can be either a single line or a multiline string with line breaks using any Python line break
technique.

<title>

Specifies the title to be displayed for this action. The definition of <title> must use the Title
function.

For example: title=Title("interface 1/1/1 no shutdown")

Usage

n All CLI commands are supported as input to CLI actions.

n Command strings are passed without validation.

n The first CLI action executed in a script starts from the manager (#) command context. To execute

commands in another context, you must include the commands to enter that context.

For example, to execute a configuration command, you must enter the correct configuration context, as
in the following action:
ActionCLI("config\ninterface 1/1/1\nno shutdown")

Similar to a single CLI session, subsequent CLI actions in the script execute from the command context
that is in place after the previous command is executed. In the previous example, the command context
is the config context, and the next CLI action starts in the config context. Commands that cannot be
executed in the config context fail.

n As a best practice, include commands in each CLI command to return to a standard command

context appropriate for the script—such as the manager (#) context. For example:

ActionCLI("config\ninterface 1/1/1\nno shutdown\nexit\nexit")

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

120

n Youcancreateacustomtitleforthisaction.ThetitleyoucreatecanhelptheuseroftheWebUIto
determinewhatactionwasexecuted.ThetitleisdisplayedintheAction ResultssectionoftheAlert
Detailsdialogbox.
Examples
ExamplesofamultilineCLIactions:
| ActionCLI("config\ninterface |     |     |     | 1/1/1\nno | shutdown\nexit\nexit") |     |
| ---------------------------- | --- | --- | --- | --------- | ---------------------- | --- |
ExampleofaCLIactionthatusesaparameter:
| ActionCLI("show |     | interface | {}",[ self.params["iface_id"]]) |     |     |     |
| --------------- | --- | --------- | ------------------------------- | --- | --- | --- |
ExampleofaCLIactionthatusesaparameterandacustomtitle:
title = Title("Print interface {} details",[self.params["iface_id"]])
self.ActionCLI("show interface {}", [self.params["iface_id"]], title=title)
ActionCustomReport
Syntax
Insideacallbackaction:
| ActionCustomReport(<template>[, |     |     |     | <params>][, |     | title=<title>]) |
| ------------------------------- | --- | --- | --- | ----------- | --- | --------------- |
Description
Generatesamultiplelinereportwithcustomizedcontent.ThereportcontentcanbeviewedintheWeb
UIfromthealertdetailsfortheagent.
Parameters
<template>
Specifiesthereporttemplatetousewhengeneratingthisreport.Thistemplatemustbedefined
elsewhereinthescript.
<title>
Specifiesthetitletobedisplayedforthisaction.Thedefinitionof<title>mustusetheTitle
function.
| Forexample:title=Title("Generate |     |     |     |     | final MAC | report") |
| -------------------------------- | --- | --- | --- | --- | --------- | -------- |
Usage
Thisfunctioncanonlybeusedinsideacallbackaction.
Thescriptmustcontainthetemplate(code)thatgeneratesandformatsthereport.
Youcancreateacustomtitleforthisaction.ThetitleyoucreatecanhelptheuseroftheWebUIto
determinewhatactionwasexecuted.ThetitleisdisplayedintheAction ResultssectionoftheAlert
Detailsdialogbox.
Examples
Exampleofcallingthecustomreportactionwithaparameter:
| ActionCustomReport(my_template, |     |     |     | [self.params["author"]]) |     |     |
| ------------------------------- | --- | --- | --- | ------------------------ | --- | --- |
ExampleofgeneratingacustomreportinHTMLformat:
| uri1 | = '/rest/v1/system/vlans/{}/macs/?count' |     |     |     |     |     |
| ---- | ---------------------------------------- | --- | --- | --- | --- | --- |
self.m1 = Monitor(uri1, 'Mac address count', [self.params['vlan_id']])
|     | self.r1 | = Rule('MAC | Address |     | Learnt') |     |
| --- | ------- | ----------- | ------- | --- | -------- | --- |
self.r1.condition(
|     | '{}       | > 0 pause                    | {}  | minutes', |     |     |
| --- | --------- | ---------------------------- | --- | --------- | --- | --- |
|     | [self.m1, | self.params['alert_pause']]) |     |           |     |     |
self.r1.action(self.gen_custom_report)
| def gen_custom_report(self, |     |     | event): |     |     |     |
| --------------------------- | --- | --- | ------- | --- | --- | --- |
Scripts|121

| vlan_id = self.params['vlan_id'].value |           |                  |     |     |
| -------------------------------------- | --------- | ---------------- | --- | --- |
| type_s = ["dynamic",                   | "static", | "mclag", "vrrp"] |     |     |
| mac_report = []                        |           |                  |     |     |
for m in type_s:
| mac_all_dict | = self.get_mac_result(vlan_id, |     | m)  |     |
| ------------ | ------------------------------ | --- | --- | --- |
mac_report.append(mac_all_dict)
| final_report = | self.generate_htmlreport(mac_report) |     |     |     |
| -------------- | ------------------------------------ | --- | --- | --- |
ActionCustomReport(final_report, title=Title("Generate final MAC report"))
| def get_mac_result(self,                            | vlan_id, mac_type):               |     |     |     |
| --------------------------------------------------- | --------------------------------- | --- | --- | --- |
| url = 'http://127.0.0.1:5577/rest/v1/system/vlans/' |                                   |     |     | \   |
| + str(vlan_id)                                      | + '/macs?count=true&filter=from:' |     |     | + \ |
mac_type
r1 = self.rest_get(url)
result = str(r1.json()["count"])
return result
| def generate_htmlreport(self, | mac_report): |     |     |     |
| ----------------------------- | ------------ | --- | --- | --- |
| html_prefix =                 | '''<html>    |     |     |     |
<head>
<title>HPE-Aruba</title>
</head>
<body>
| <table border="1"> |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
<tr align="center">
<th><td colspan="4"><b>Summary</b></td></th>
</tr>
<tr align="center">
<th>
<td colspan="4">
|     | <b>Number | of MAC learnt | on various | types</b> |
| --- | --------- | ------------- | ---------- | --------- |
</td>
</th>
</tr>
<tr>
| <th> | DYNAMIC </th> |     |     |     |
| ---- | ------------- | --- | --- | --- |
<th> STATIC </th>
| <th> | MCLAG </th> |     |     |     |
| ---- | ----------- | --- | --- | --- |
| <th> | VRRP </th>  |     |     |     |
</tr>
| ''' + self.get_mac_htmlcontent(mac_report) |     |     | + ''' |     |
| ------------------------------------------ | --- | --- | ----- | --- |
</table>
</body>
</html>'''
return html_prefix
Foranotherexampleofacustomreport,seetheospfv2_interface_state_flaps_impact_monitor
solutionontheArubaSolutionsExchange.
| ActionShell, SHELL action |     |     |     |     |
| ------------------------- | --- | --- | --- | --- |
Syntax
Insideacallbackaction:
ActionShell("<command>"[, title=<title>])
Outsideofacallbackaction:
self.r.action("SHELL","<command>"[, title=<title>])
Description
TheSHELLactionexecutesthespecifiedcommandintheBashshelloftheunderlyingLinuxoperating
systemoftheswitch.
122
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

Parameters

<command>

A text string of the shell command as it would be entered at a Linux prompt.

The string can be either a single line or a multiline string with line breaks using any Python line break
technique.

<title>

Specifies the title to be displayed for this action. The definition of <title> must use the Title
function.

For example: title=Title("ps -aux")

Usage

The SHELL action takes a string as input and pipes it to the switch Bash shell.

For example, the following ActionShell request lists the current processes running on the switch:
ActionShell("ps -aux")

You can create a custom title for this action. The title you create can help the user of the Web UI to
determine what action was executed. The title is displayed in the Action Results section of the Alert
Details dialog box.

Shell commands provide advanced and powerful access to the switch. Improper changes can make the switch

inoperable, potentially requiring the switch to be zeroized.

The shell is enabled on the switch by default. However, if the switch is configured to use enhanced
secure mode, access to the shell is denied. Agent attempts to execute a shell action are denied, and the
Action Result dialog box for that shell action indicates an error. However, the agent and the script are
not set to an error state, so the error can be ignored. For more information about enhanced secure
mode, see the Security Guide.

When shell actions enabled on a switch:

n SHELL actions execute with root privileges.

n The first SHELL action in a script executes from the root (/) directory.

n All Bash shell commands are supported as SHELL actions.

n Command strings are passed without validation.

n SHELL actions can be used with parameters.

Examples

Example of a SHELL action inside a callback action:
ActionShell("cd {}",[ self.params["path"])

Example of a SHELL action outside of a callback action:
self.r.action("SHELL", "cd {}",[ self.params["path"])

Example of a SHELL action that includes a custom title:
title=Title("cd {}",[ self.params["path"])
self.r.action("SHELL", "cd {}",[ self.params["path"], title=title)

ActionSyslog, Syslog action

Syntax

Inside a callback action:

Scripts | 123

ActionSyslog(
"<log_message>"
[, severity=<severity>]
[, title=<title>])

Outside of a callback action:
self.r.action("Syslog",
"<log_message>"
[, severity=<severity>]
[, title=<title>])

Description

The ActionSyslog action enters the specified message in the event log. Users can access event log
messages from the CLI, REST API, or Web UI of the switch.

Parameters

<log_message>

A text string of the message to be entered into the log.

The size and content of this message is subject to the same requirements as any other event log
message on this system.

<severity>

Specifies the severity of the log message.

The Aruba Network Analytics Engine supports the following values:

n SYSLOG_ALERT

n SYSLOG_CRIT

n SYSLOG_ERR

n SYSLOG_WARNING

n SYSLOG_INFO

Default: SYSLOG_INFO

<title>

Specifies the title to be displayed for this action. The definition of <title> must use the Title
function.

For example: title=Title("Report CPU utilization")

Usage

Use this action to record event log messages that can be accessed from the CLI, REST API, or Web UI of
the switch.

This action sends a message to the event log. Log messages are labeled with a severity level. Only the
specified message is sent to the log—additional information such as the monitor or agent name is not
included.

You can create a custom title for this action. The title you create can help the user of the Web UI to
determine what action was executed. The title is displayed in the Action Results section of the Alert
Details dialog box.

Examples

The following example sends a message to the event log, using the parameter message, inside a callback
action:
ActionSyslog("Sample message: {}", [self.params["message"]], severity=SYSLOG_WARNING,
facility=SYSLOG_DAEMON)

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

124

The following example sends a message to the event log, using the parameter message, outside of a
callback action:
self.r.action("Syslog", "Sample message: {}", [self.params["message"]])

Callback actions

Callback actions are callback functions that call other Python methods in the script to perform further
processing. Callback actions can also call predefined actions and functions that have been imported
from the supported Python modules or third-party libraries.

Callback actions are executed when the condition of a rule is true. If a callback action calls a predefined
action, that predefined action is executed asynchronously. Callback actions time out after five minutes.
This timeout interval is not editable.

This example contains a callback action, action_high_poll_interval, that calls the predefined actions
ActionSyslog and ActionCLI:

uri = '/rest/v1/system?attributes=resource_utilization_poll_interval'
self.m = Monitor(uri, name='My Monitor')
self.r = Rule('Resource Utilization Poll Interval')
self.r.condition('{} > 100 for 30 seconds', [self.m])
self.r.action(self.action_high_poll_interval)

def action_high_poll_interval(self, event):

self.set_alert_level(AlertLevel.CRITICAL)
ActionSyslog('High Poll Interval')
ActionCLI("show running-config")

Aruba Network Analytics Engine agent sandboxes run in the default VRF. If a script has a function that
requires access to the Internet, this function fails unless the switch administrator configures a DNS
name server on the default VRF.

When a condition is met, an event is generated and the callback action is executed using the event
details. The event parameter passed to the callback action contains those event details.

The event parameter contains a dictionary of key-value pairs. The dictionary includes the following keys:
event['labels']

The labels created by the time-series database.

event['condition_name']

The name of the condition that triggers the event.

event['monitor_name']

The name of the monitor.

event['time_series']

The name of the time series metric.

event['value']

The value of the time series metric.

event['timestamp']

The timestamp of the generated event.

event['condition_description']

The description of the condition that triggered the event.

Clear actions

You can define actions to execute when a clear condition is active and becomes true. These actions are
called "clear actions" because they often do things like set an alert level back to a normal value or reset
status.

Scripts | 125

Forexample,ifyoudefineanactiontosendamessagetothelogiftheCPUutilizationgetsabove90%,
youcanalsodefineanactiontosendadifferentmessagetothelogwhenaCPUutilizationthatwas
above90%dropstoalowerutilization.
Theclearactionisexecutedonlyonce—whentheconditionbecomesinvalidandtheclearcondition
becomesvalid:
n Iftheruledoesnothaveaclearconditiondefined,thedefaultbehavioristhattheclearcondition
becomesvalidwhentheconditiontransitionsfromtruetofalse.
Forexample,iftheCPUutilizationisgreaterthan90%(theconditionisvalidortrue),theclearactionis
executedwhentheCPUutilizationisequaltoorlessthan90%(theconditionbecomesinvalid),butnotif
itcontinuestodroporifitremainslessthan90%thenexttimetheconditionisevaluated.However,if
theCPUutilizationbecomesgreaterthan90%again,theclearactionwillbeexecutedthenexttimethe
CPUutilizationdropstolessthanthethresholdof90%.
n Iftherulehasaclearconditiondefined,theclearconditionbecomesactivethefirsttimethe
conditionbecomestrue.However,theclearconditiondoesnotbecomevaliduntilitisbothactive
anditbecomestrue.
Forexample,consideraclearconditionthatbecomestruewhentheCPUutilizationdropsbelow70%.
AftertheCPUutilizationisbecomesgreaterthan90%theclearconditionbecomesactive,butitdoes
notbecometrueuntiltheCPUutilizationdropsbelow70%.Thereforetheclearactionisnotexecuted
untilaCPUutilizationthathasbeenabove90%dropsbelow70%.
Bothpredefinedandcallbackactionscanbeusedinclearactions.
Thefollowingisanexampleofarulethatincludesanactionandtwoclearactions.Intheexample:
n OneoftheclearactionscallstheCLIactiontoexecutetheshow running-configCLIcommand:
| self.rule.clear_action("CLI","show |     |     | running-config") |
| ---------------------------------- | --- | --- | ---------------- |
n Theotherclearactioncallstheset_normalfunction,whichremovesthealertlevel:
self.rule.clear_action(self.set_normal)
Thefollowingexampleshowsamonitorthathasarulethatdefinesaclearactionsandaclearcondition:
self.monitor = Monitor(AverageOverTime("/rest/v1/system/subsystems/management_
module/1%2F5?attributes=resource_utilization.cpu", "5 minutes")
| self.rule                       | = Rule("") |        |                        |
| ------------------------------- | ---------- | ------ | ---------------------- |
| self.rule.condition("{}         |            | > 90", | [self.monitor])        |
| seld.rule.action("ALERT_LEVEL", |            |        | AlertLevel.CRITICAL)   |
| self.rule.clear_condition("{}   |            |        | < 70", [self.monitor]) |
self.rule.clear_action(self.set_normal)
| def set_normal(self, |     | event): |     |
| -------------------- | --- | ------- | --- |
self.remove_alert_level()
Thefollowingexampleshowsamonitorwitharulethatdefinesclearactionsbutdoesnotdefineaclear
condition:
self.monitor = Monitor(AverageOverTime("/rest/v1/system/subsystems/management_
module/1%2F5?attributes=resource_utilization.cpu", "5 minutes")
| self.rule               | = Rule("High | CPU Utilization") |                 |
| ----------------------- | ------------ | ----------------- | --------------- |
| self.rule.condition("{} |              | > 90"             | [self.monitor]) |
self.rule.action(self.action_high_cpu)
| self.rule.clear_action("CLI","show |     |     | running-config") |
| ---------------------------------- | --- | --- | ---------------- |
self.rule.clear_action(self.set_normal)
| def action_high_cpu(self, |            | event):       |     |
| ------------------------- | ---------- | ------------- | --- |
| # CPU                     | value when | the Condition | met |
cpu = event["/v1/system/subsystems/system/base?attributes=resource_utilization.cpu"]
| ActionSyslog("CPU |     | Utilization | at %d" % cpu) |
| ----------------- | --- | ----------- | ------------- |
| ActionCLI("top    |     | cpu")       |               |
126
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

def set_normal(self, event):
self.remove_alert_level()

Alert level functions

The Aruba Network Analytics Engine provides several predefined functions related to alerts.

The alert level functions get, set, or remove the alert level of the agent:
get_alert_level()

Gets the current alert level of the agent.

Example:
status = self.get_alert_level()

set_alert_level(<Alert_Level>)

Sets the alert level of the agent.

Example:
self.set_alert_level(AlertLevel.CRITICAL)

The <Alert_Level> must be one of the following values:
AlertLevel.CRITICAL

The agent has detected a critical issue.

AlertLevel.MAJOR

The agent has detected a major issue.

AlertLevel.MINOR

The agent has detected a minor issue.

remove_alert_level()

Removes the alert level of the agent.

Example:

self.remove_alert_level()

Logging functions

The Aruba Network Analytics Engine provides the predefined logger functions for sending messages to
the log and to set logging levels.

logger.setLevel(<level>)

Sets the default logging level specified by <level>. Valid values for <level> are the following:

n EMERG

n ALERT

n CRITICAL

n ERROR

n WARNING

n NOTICE

n INFO

n DEBUG

logger.log("<message>")

Sends the specified <message> at the default log level to the system log.

To send a message at a log level that is not the default log level, you can use one of the following
functions:

Scripts | 127

n logger.emerg("<message>")

n logger.alert("<message>")

n logger.critical("<message>")

n logger.error("<message>")

n logger.warning("<message>")

n logger.notice("<message>")

n logger.info("<message>")

n logger.debug("<message>")

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

128

Chapter 12

Agents

Agents

An Aruba Network Analytics Engine agent is a specifically-configured executable instance of an Aruba
Network Analytics Engine script on a switch. When the agent is enabled, it performs the tasks defined by
the script.

Aruba Network Analytics Engine agent sandboxes run in the default VRF. If a script has a function that
requires access to the Internet, this function fails unless the switch administrator configures a DNS
name server on the default VRF.

Agents and user authority
Agents have administrator authority to perform tasks such as executing CLI commands.

You must have administrator authority to create, delete, enable, disable, or change the configuration of
agents. You cannot delete built-in agents.

Rules for agent names
The <agent_name> must have the following characteristics:

n The name must be unique among the agents created for the script.

n The name must be a text string that starts with a letter or number and can contain alphanumeric

characters and the special characters . (dot), - (hyphen), and _ (underscore). Minimum length: three
characters. Maximum length: 80 characters.

Updating agents parameter value
An agent's parameter values can be updated using the following methods:

n An agent can be deleted and re-created with the new parameter value(s).

n Configuring the agent's parameter value(s) using the WebUI.

n Configuring the agent's parameter value(s) using the CLI.

When an agent is deleted and re-created with new parameter value(s), to view the previous alerts for
that agent in the WebUI, you must re-create the agent with the same name.

If the agent parameter(s) are edited on a running agent from WebUI or CLI, the script may need to
handle updating the current alert status and local storage with the special on_parameter_change
function. Using the CLI method, if you configure the agent parameter values with invalid types or data,
the agent enters an error state.

An agent can be created before the monitored resources are configured.

Network Analytics Engine Safeguards
The Aruba Network Analytics Engine includes several safeguards. In order to preserve a switch's
persistent storage device, NAE imposes the following mechanisms:

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

129

n IO limiting

n Time Series limiting

n Alert throttling

n Rules limiting

n Alert size limiting

IO Limiting

The IO rate of every switch is monitored and event log messages are issued whenever a high IO rate is
detected on the /fs/nos partition. If this event log message is issued, all running agents, except for the
default agent, are disabled. Agents are placed in an error state and another event log message is issued.
Users can then remove and restart agents in an error state as needed.

Time Series Limiting

Time series contributes to bytes written to the disk every five seconds. The more times series on the
switch, the more data will be written. In order to provide a runtime limiting of time series, the amount of
times series used per agent is monitored. The running count of time series is stored on a per agent and
per switch basis. Agents that exceed the switch's maximum timeseries capacity are disabled. Users can
then remove and restart disabled agents as needed.

Alert Throttling

The amount of alerts generated per agent and per minute is monitored to ensure that platform
capacities are not exceeded. If an agent exceeds the per minute limit, excessive incoming alerts will be
dropped and an event log message will be issued. If an agent exceeds the limit three times within five
minutes, the agent will be disabled and an event log message will be issued. Users can remove and
restart disabled agents as needed.

Rules Limiting

There is a limit of time series rules that NAE will support. These rules are evaluated every 5 seconds,
and the evaluation determines whether or not an action is triggered. The running count of rules is
stored on a per agent and system total basis. Agents that exceed the switch maximum are disabled.
Users can remove and restart disabled agents as needed.

Alert Size Limiting

Alerts are monitored per platform for the total size of output files generated. If the total size of an alert
has exceeded the limit, those actions are not stored in the alert, and an NAE generated syslog message
is logged. Other actions that do not result in output files, such as syslog actions or alert level changes,
are still present in the alert.

Agents | 130

Network Analytics Engine Lite

Chapter 13

Network Analytics Engine Lite

The Network Analytics Engine Lite (NAE-Lite) feature within AOS-CX switches is a CLI-based framework
for creating an NAE-Lite agent, defining the data to be monitored, specifying conditions, and associating
pre-defined actions to be executed when the conditions are met.

NAE-Lite agent

The NAE-Lite agent provides simplified monitoring and watch capability using CLI commands. This
enables the user to create an NAE agent through CLI to monitor specific resources and events by
providing the following set of information:

n Resources or events to be monitored

n Conditions to be met

n Actions to be performed

Network administrators can create an NAE-Lite agent easily through the CLI. Programming skill is not
required.

Monitors and Watches

Using an NAE-Lite agent, you can define either one of the following ways:

n Monitors: Monitor predefined resources such as memory, CPU, and storage utilization by using the

time series data. Monitors support grouping of data.

n Watches: Watch for specific system events occurring in event logs of the system using event IDs. Time

series data are not supported for watches.

n In an NAE-Lite agent, you can configure either monitors or watches. You cannot configure a combination of

both monitors and watches.

n In an NAE-Lite agent, you can configure a maximum of two monitors or watches.

Conditions

In an NAE-Lite agent, you can specify a condition to be met and an optional clear condition when the
condition is no longer active.

Actions

In an NAE-Lite agent, you can configure the following predefined actions to be performed when the
specified condition is met:

n Status—Sets the alert level for the NAE Agent.

n Syslog—Creates a system log message and send it to the configured remote syslog servers.

n CLI—Executes CLI commands.

This helps you to notify and collect more detailed information about the system to troubleshoot any
issues.

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

131

| NAE-Lite agent | limitations |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | --- |
ThefollowinglimitationsapplytoanNAE-Liteagent:
n Onlyoneagentperscriptissupported.Multipleagentsperscriptarenotsupported.
n Onlyoneresourceorsetofeventscanbemonitoredusingsetandclearconditions.Setandclear
conditioncanhavedifferentresourcesorsetofeventIDs.
n Insetandclearconditions,multiplerulesandcombinationsarenotsupported.
n Onlylimitedsetofpredefinedactionssuchassettingstatuslevel,sendingsystemlogmessage
(Syslog)andexecutingCLIcommandsaresupported.
n ParametersarenotsupportedinanNAE-Liteagent.
n Callbackactionsarenotsupported.
| NAE-Lite agent | tasks |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- |
NAE-Litetasksareasfollows:
| Task           | Command   |                   |     |     |     |
| -------------- | --------- | ----------------- | --- | --- | --- |
| CreatinganNAE- | nae-agent | lite <AGENT-NAME> |     |     |     |
Liteagent
desc <DESCRIPTION>
Configuringthe
descriptionfor
theNAE-Lite
agent
disable
Disablingthe
NAE-Liteagent
| Configuringthe | tags <TAG-LIST> |     |     |     |     |
| -------------- | --------------- | --- | --- | --- | --- |
taglist
| Configuringthe | monitor | <MONITOR-NAME> | {resource | <RESOURCE>} |     |
| -------------- | ------- | -------------- | --------- | ----------- | --- |
monitorfor group-by {count | sum | min | max | average } [over <DURATION>]]
| system | monitor | <MONITOR-NAME> | resource | <RESOURCE> |     |
| ------ | ------- | -------------- | -------- | ---------- | --- |
resourceswith
group-by rate over {seconds | minutes | hours | days} <DURATION>
timeseriesdata
set-condition monitor <MONITOR-NAME> {{lt | le | eq | ne | gt | ge}
Settingthe
conditionforthe <VALUE> [for {seconds | minutes | hours | days} <DURATION>] |
| monitor | transition | from | <STRING-LIST> | to <STRING-LIST>} |     |
| ------- | ---------- | ---- | ------------- | ----------------- | --- |
Clearingthe clear-condition monitor <MONITOR-NAME> {{lt | le | eq | ne | gt | ge}
conditionforthe <VALUE> [for {seconds | minutes | hours | days} <DURATION>]
|     | | transition | from | <STRING-LIST> | to  | <STRING-LIST>} |
| --- | ------------ | ---- | ------------- | --- | -------------- |
monitor
| Configuringthe | watch <WATCH-NAME> |     | {event-log | <EVENT-ID-LIST>} |     |
| -------------- | ------------------ | --- | ---------- | ---------------- | --- |
watchforthe
NAE-Liteagent
Settingthe set-condition watch event-log <WATCH-NAME> [include {all | any}
conditionforthe <REGEX-LIST>] [exclude <REGEX-LIST>] [count <COUNT>]
watch
Clearingthe clear-condition watch event-log <WATCH-NAME> [include {all | any}
|     | <REGEX-LIST>] | [exclude | <REGEX-LIST>] |     | [count <COUNT>] |
| --- | ------------- | -------- | ------------- | --- | --------------- |
NetworkAnalyticsEngineLite|132

| Task |     | Command |     |     |     |     |     |     |     |
| ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
conditionforthe
watch
|     |     | status |     | {normal | |   | minor | | major | critical} |     |     |
| --- | --- | ------ | --- | ------- | --- | ------- | ----------------- | --- | --- |
Configuring
|     |     | syslog |     | <MESSAGE> |     | [facility | <FACILITY>] | [severity | <SEVERITY>] |
| --- | --- | ------ | --- | --------- | --- | --------- | ----------- | --------- | ----------- |
actionstobe
|     |     | cli | <COMMAND> |     |     |     |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
performedwhen
theconditionis
met
| Activatingthe |     | nae-agent |     | lite | <AGENT-NAME> |     | activate |     |     |
| ------------- | --- | --------- | --- | ---- | ------------ | --- | -------- | --- | --- |
NAE-Liteagent
Use Cases
FollowingaresomeoftheusecaseswhereNAE-Liteagentisused:
| Monitor | system | CPU | usage |     |     |     |     |     |     |
| ------- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- |
Thefollowingcpu_monitoragentcomputestheaverageCPUusageoverthe1hourdurationand
createsanalertiftheusageishigherthan80%.Thetop cpucommandoutputiscapturedand
preservedwhenthealertisgenerated.Additionally,theagentstatusissettomajorwhenthecondition
ismet.Theclear-conditionismetwhentheaverageCPUusageoverthelast1hourfallsbelow40%.
Theagentstatusissettonormaloncetheclear-conditionismet.
| nae-agent |      | lite   | cpu_monitor |            |     |     |     |     |     |
| --------- | ---- | ------ | ----------- | ---------- | --- | --- | --- | --- | --- |
|           | desc | System | CPU         | monitoring |     |     |     |     |     |
monitor average_cpu resource system cpu group-by average over hours 1
|     | set-condition |                 | monitor |         | average_cpu |             | gt 80 |     |     |
| --- | ------------- | --------------- | ------- | ------- | ----------- | ----------- | ----- | --- | --- |
|     |               | status          | major   |         |             |             |       |     |     |
|     |               | syslog          | "High   | cpu     | usage       | detected"   |       |     |     |
|     |               | cli top         | cpu     |         |             |             |       |     |     |
|     |               | clear-condition |         | monitor |             | average_cpu | lt 40 |     |     |
|     |               | status          | normal  |         |             |             |       |     |     |
exit
| nae-agent |        | lite   | cpu_monitor |       | activate |     |     |     |     |
| --------- | ------ | ------ | ----------- | ----- | -------- | --- | --- | --- | --- |
| Monitor   | system | memory |             | usage |          |     |     |     |     |
Thefollowingmemory_monitoragentcomputesthememoryusageandcreatesanalertifthecurrent
memoryusageishigherthan80%.Thetop memorycommandoutputiscapturedandpreservedwhen
thealertisgenerated.Additionally,theagentstatusissettomajorwhentheconditionismet.The
clear-conditionismetwhenthecurrentmemoryusagefallsbelow40%.Theagentstatusissetto
normaloncetheclear-conditionismet.
| nae-agent |               | lite   | memory_monitor |            |        |           |     |     |     |
| --------- | ------------- | ------ | -------------- | ---------- | ------ | --------- | --- | --- | --- |
|           | desc          | System | memory         | monitoring |        |           |     |     |     |
|           | monitor       | memory | resource       |            | system | memory    |     |     |     |
|           | set-condition |        | monitor        |            | memory | gt 80     |     |     |     |
|           |               | status | major          |            |        |           |     |     |     |
|           |               | syslog | "High          | memory     | usage  | detected" |     |     |     |
133
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

cli top memory
clear-condition monitor memory lt 40

status normal

exit
nae-agent lite memory_monitor activate

Watch for any system daemon crash event

The following crash_watch agent is created to watch the event-log 1201for any daemon crash. The
agent also captures additional diagnostics information for debugging. Whenever there is a daemon
crash, the condition will be met and the diagnostic data will be collected.

nae-agent lite crash_watch

desc Watch system crash event
tags crash, resource
watch crash_event event-log 1201
set-condition watch event-log crash_event

status major
cli show core-dump\ntop cpu\ntop mem

exit
nae-agent lite crash_watch activate

Watch for specific daemon crash

The following cardd_crash agent is created to watch for the crash of hpe-cardd and capture additional
diagnostics information for debugging. Whenever the hpe-cardd daemon crashes, the condition is met
and the diagnostic data will be collected.

nae-agent lite cardd_crash
desc Watch cardd crash
tags crash, card
watch crash_event event-log 1201
set-condition watch event-log crash_event include all "hpe-cardd"

status major
cli show core-dump\ntop cpu\ntop mem

exit
nae-agent lite cardd_crash activate

Watch for too frequent mac moves

The following mac_move agent is created to watch for the mac move events and perform actions if a

specific mac has moved more than 10 times in the specific VLAN. The event log 4801 is raised whenever
a mac move happens. This agent monitors the mac move in VLAN 10.

nae-agent lite mac_move

desc Watch mac moves
tags mac
watch mac_w event-log 4801
set-condition watch event-log mac_w include all "MAC 11:22:33:44:55:66","VLAN

10" count 10

status minor
cli show mac-address-table

Network Analytics Engine Lite | 134

exit
| nae-agent |     | lite mac_move |        | activate |     |     |     |     |     |
| --------- | --- | ------------- | ------ | -------- | --- | --- | --- | --- | --- |
| Watch     | for | memory        | events |          |     |     |     |     |     |
Thefollowingwatch_memoryagentiscreatedtowatchforthesystemmemoryrelatedeventsfromthe
module1/1andperformactions.Theeventlog1208israisedwhenhighmemoryusageisdetectedand
theeventlog1207israisedwhenusagegetsbacktonormalrange.
| nae-agent |               | lite           | watch_memory |           |           |          |            |             |       |
| --------- | ------------- | -------------- | ------------ | --------- | --------- | -------- | ---------- | ----------- | ----- |
|           | desc          | Watch          | memory       | usage     |           |          |            |             |       |
|           | watch         | high_mem       | event-log    |           | 1208      |          |            |             |       |
|           | watch         | normal_mem     |              | event-log |           | 1207     |            |             |       |
|           | set-condition |                | watch        | event-log |           | high_mem | include    | any "1/1"   |       |
|           |               | status         | major        |           |           |          |            |             |       |
|           |               | cli top        | mem          |           |           |          |            |             |       |
|           |               | clear-condtion |              | watch     | event-log |          | normal_mem | include any | "1/1" |
|           |               | status         | normal       |           |           |          |            |             |       |
exit
| nae-agent |     | lite | watch_memory |     | activate |     |     |     |     |
| --------- | --- | ---- | ------------ | --- | -------- | --- | --- | --- | --- |
135
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

Chapter 14
|         |           |                 | Network | Analytics | Engine | commands |
| ------- | --------- | --------------- | ------- | --------- | ------ | -------- |
| Network | Analytics | Engine commands |         |           |        |          |
nae cli-authorization
nae cli-authorization
no nae cli-authorization
Description
ConfigurestheNAEagentactionCLI commandstorequireauthorization.Bydefault,theNAEagent
actionCLIcommandsaresubjecttoregularcommandauthorization,includingwhenTACACS+is
configuredforauthorization.UnlesstheconfiguredauthorizationmethodallowstheCLIcommands
sentbytheNAEagentasuseradmin,theNAEagentactionCLIcommandswillresultincommand
failures.
ThenoformofthecommanddisablestheauthorizationrequiredforNAE agentactionCLIcommands.
Examples
EnablingauthorizationrequirementforNAEagentactionCLIcommands:
| switch(config)# |     | nae cli-authorization |     |     |     |     |
| --------------- | --- | --------------------- | --- | --- | --- | --- |
DisablingauthorizationrequirementforNAEagentactionCLIcommands:
| switch(config)# |             | no nae cli-authorization |                   |     |     |     |
| --------------- | ----------- | ------------------------ | ----------------- | --- | --- | --- |
| Command         | History     |                          |                   |     |     |     |
| Release         |             |                          | Modification      |     |     |     |
| 10.11           |             |                          | Commandintroduced |     |     |     |
| Command         | Information |                          |                   |     |     |     |
| Platforms       | Command     | context                  | Authority         |     |     |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6300
6400
8100
8320
8325
8360
8400
9300
10000
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000Switch
136
Series)

show nae-agent
show nae-agent [<AGENT-NAME>] [vsx-peer]

Description

Shows the details of the NAE Agent. If the agent name is specified, then shows the information details of
the specified agent.

Parameter

<AGENT-NAME>

vsx-peer

Usage

Description

Specifies the name of the agent. Length: 3 to 80 alphanumeric
characters, including underscore (_).

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

This command shows the following information about the Aruba Network Analytics Engine agents that
are configured and enabled on the switch:

Agent Name

The name of the agent. Length: 3 through 80 characters.

Script Name

The name of the script. Length: 3 through 80 characters.

Example: memory_monitor

Version

The version number of the script.

Origin

The origin of the script:
system

Indicates that the script is provided as part of the system software.

user

Indicates that a user loaded the script.

generated

Indicates that the agent is configured using the CLI.

Disabled

Indicates whether the agent is disabled or enabled on the switch:
true

Indicates that the agent is disabled.

false

Indicates that the agent is enabled on the switch.

Status

The current state of the agent. Status values are the following:

CRITICAL

The agent has encountered a critical error during execution. For information about the error, see
the Analytics Dashboard of the Web UI.

MAJOR

Network Analytics Engine commands | 137

Theagenthasencounteredamajorerrorduringexecution.Forinformationabouttheerror,see
theAnalyticsDashboardoftheWebUI.
MINOR
Theagenthasencounteredaminorerrorduringexecution.Forinformationabouttheerror,see
theAnalyticsDashboardoftheWebUI.
NORMAL
Indicatesthattheagentisactivelymonitoringnetworkconditionsandhandlingevents.
UNKNOWN
Indicatesthatthestatusisunknown.
| Time series | count |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
Numberoftimeseriesassociatedwithagent.
Alerts count
Numberofalertsgeneratedbytheagent.
Rules
NumberofPrometheusrulesassociatedwiththeagent.
Error
Currenterrorstateoftheagent.
Recent alerts
Liststherecentalerts.
Example
ShowingthedetailsofalltheNAEagentsexistingintheswitch:
| switch# | show nae-agent |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
--------------------------------------------------------------------------
| Agent Name |     |     | Script Name |     | Version |
| ---------- | --- | --- | ----------- | --- | ------- |
Origin Disabled Status Time Series Count Alerts Count Rules Error
----------------------------------------------------------------------------------
--------------------------------------------------------------------------
com.arubanetworks.monitor.agent com.arubanetworks.monitor 1.0
| user                    | true | UNKNOWN | 0                             | 0   | 0 NONE  |
| ----------------------- | ---- | ------- | ----------------------------- | --- | ------- |
| interface_monitor.agent |      |         | interface_tx_rx_stats_monitor |     | 2.3     |
| user                    | true | UNKNOWN | 168                           | 10  | 36 NONE |
com.arubanetworks.wildcard.vlan.agent com.arubanetworks.wildcard.vlan 1.0
| user                            | false          | UNKNOWN  | 0                       | 0   | 0 ERROR  |
| ------------------------------- | -------------- | -------- | ----------------------- | --- | -------- |
| system_resource_monitor.default |                |          | system_resource_monitor |     | 1.3      |
| system                          | false          | NORMAL   | 6                       | 23  | 10 NONE  |
| event_monitor                   |                |          | event_monitor           |     | NA       |
| generated                       | NA             | NA       | 0                       | 0   | 0 Script |
| activation                      | is pending     |          |                         |     |          |
| cpu_monitor                     |                |          | cpu_monitor             |     | NA       |
| generated                       | NA             | NA       | 0                       | 0   | 0 Script |
| generation                      | is in          | progress |                         |     |          |
| mem_monitor                     |                |          | mem_monitor             |     | NA       |
| generated                       | NA             | NA       | 0                       | 0   | 0 Script |
| validation                      | is in          | progress |                         |     |          |
| interface_monitor               |                |          | interface_monitor       |     | NA       |
| generated                       | NA             | NA       | 0                       | 0   | 0 Agent  |
| creation                        | is in progress |          |                         |     |          |
| port_monitor                    |                |          | port_monitor            |     | NA       |
| generated                       | NA             | NA       | 0                       | 0   | 0 Agent  |
| updation                        | is in progress |          |                         |     |          |
138
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

ShowingthedetailsoftheNAEagentnamedmemory_monitor:
| switch#       | show nae-agent | memory_monitor   |     |
| ------------- | -------------- | ---------------- | --- |
| Script Name   |                | : memory_monitor |     |
| Version       |                | : 1.0            |     |
| Origin        |                | : generated      |     |
| Disabled      |                | : false          |     |
| Status        |                | : NORMAL         |     |
| Time Series   | Count          | : 0              |     |
| Alerts Count  |                | : 0              |     |
| Rules         |                | : 0              |     |
| Error         |                | : None           |     |
| Recent alerts |                | :                |     |
<1> 2021-05-29 01:34:11 An action has been triggered by NAE agent memory_monitor
<2> 2021-05-28 06:11:00 An action has been triggered by NAE agent memory_monitor
<3> 2021-05-27 03:19:50 An action has been triggered by NAE agent memory_monitor
| Command History |     |     |              |
| --------------- | --- | --- | ------------ |
| Release         |     |     | Modification |
10.09
Added<AGENT-NAME>
| 10.07orearlier      |         |         | --        |
| ------------------- | ------- | ------- | --------- |
| Command Information |         |         |           |
| Platforms           | Command | context | Authority |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
6400
8100
8320
8325
8360
8400
9300
10000
| show nae-agent |                | alerts |     |
| -------------- | -------------- | ------ | --- |
| show nae-agent | [<AGENT-NAME>] | alerts |     |
ShowsthealertsraisedbyalltheNAEagents.Iftheagentnameisspecified,thenshowsthealerts
raisedbythespecifiedagent.
| Parameter    |     |     | Description                         |
| ------------ | --- | --- | ----------------------------------- |
| <AGENT-NAME> |     |     | SpecifiesthenameoftheNAE-Liteagent. |
Example
ShowingthealertsraisedbyalltheNAEagents:
NetworkAnalyticsEnginecommands|139

| switch# | show nae-agent |     | alerts |     |     |
| ------- | -------------- | --- | ------ | --- | --- |
2021-06-13 07:53:56 An action has been triggered by NAE agent memory_monitor
2021-06-07 00:30:10 An action has been triggered by NAE agent system_resource_
monitor.default
2021-06-07 00:24:13 An action has been triggered by NAE agent system_resource_
monitor.default
2021-06-06 21:48:27 An action has been triggered by NAE agent memory_monitor
2021-06-06 18:44:41 An action has been triggered by NAE agent system_resource_
monitor.default
2021-06-06 18:31:53 An action has been triggered by NAE agent system_resource_
monitor.default
2021-06-06 20:19:03 An action has been triggered by NAE agent system_resource_
monitor.default
2021-06-06 20:15:05 An action has been triggered by NAE agent system_resource_
monitor.default
2021-06-03 07:45:36 An action has been triggered by NAE agent memory_monitor
ShowingthealertsraisedbytheNAEagentnamedmemory_monitor:
| switch# | show nae-agent |     | memory_monitor |     | alerts |
| ------- | -------------- | --- | -------------- | --- | ------ |
2021-06-13 07:54:47 An action has been triggered by NAE agent memory_monitor
2021-06-13 07:53:56 An action has been triggered by NAE agent memory_monitor
2021-06-06 21:48:27 An action has been triggered by NAE agent memory_monitor
2021-06-03 07:45:36 An action has been triggered by NAE agent memory_monitor
| Command History     |         |         |     |                   |     |
| ------------------- | ------- | ------- | --- | ----------------- | --- |
| Release             |         |         |     | Modification      |     |
| 10.09               |         |         |     | Commandintroduced |     |
| Command Information |         |         |     |                   |     |
| Platforms           | Command | context |     | Authority         |     |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --------------- | --- |
6400
8100
8320
8325
8360
8400
9300
10000
| show nae-agent |                | alerts |        | details |                 |
| -------------- | -------------- | ------ | ------ | ------- | --------------- |
| show nae-agent | [<AGENT-NAME>] |        | alerts | details | [<INSTANCE-ID>] |
Description
ShowsthedetailedinformationofaspecificNAEagentalertraisedbyalltheNAEagents.
140
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

OnlyCLI,alert,andsystemlogspecificactiondetailsaredisplayedastheoutput.Forotheractiondetails,referto
theWebUI.
| Parameter    |     |     |     |     |     |     |     | Description                                   |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- |
| <AGENT-NAME> |     |     |     |     |     |     |     | SpecifiesthenameoftheNAE-Liteagent.Length:3to |     |     |     |
80alphanumericcharacters,includingunderscore(_).
| <INSTANCE-ID> |     |     |     |     |     |     |     | Specifiestheinstanceofthealert.Number1 |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- |
representsthelatestalertwhereasNrepresentsthe
Nthrecentalert.Bydefault,itdisplaysthelatestalert
(INSTANCE-ID=1).
Example
ShowingthedetailsoftherecentalertoftheNAE-Liteagentnamedmemory_monitor:
| switch# | show | nae-agent |     | memory_monitor |     |     | alerts | details | 1   |     |     |
| ------- | ---- | --------- | --- | -------------- | --- | --- | ------ | ------- | --- | --- | --- |
2Alert Message: 2021-06-13 07:54:47 An action has been triggered by NAE agent
memory_monitor
| Action(s) |     | performed: |     | Alert, | CLI, | Syslog |     |     |     |     |     |
| --------- | --- | ---------- | --- | ------ | ---- | ------ | --- | --- | --- | --- | --- |
Action Details:
===============
| Action | Alert:  | Alert |           | level | changed           | to  | MAJOR |          |     |     |     |
| ------ | ------- | ----- | --------- | ----- | ----------------- | --- | ----- | -------- | --- | --- | --- |
| Action | Syslog: |       | Potential |       | mis-configuration |     |       | detected |     |     |     |
Action CLI:
| 6405# | top | cpu |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
top - 07:54:27 up 25 min, 1 user, load average: 10.45, 10.38, 8.48
Tasks: 295 total, 1 running, 294 sleeping, 0 stopped, 0 zombie
%Cpu(s): 2.2 us, 2.2 sy, 0.0 ni, 95.7 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st
MiB Mem : 7555.6 total, 1982.1 free, 2022.6 used, 3550.9 buff/cache
| MiB          | Swap:    |     | 0.0 total, |       |       | 0.0 | free, | 0.0    | used. | 5307.9 avail | Mem        |
| ------------ | -------- | --- | ---------- | ----- | ----- | --- | ----- | ------ | ----- | ------------ | ---------- |
|              | PID USER |     | PR         | NI    | VIRT  |     | RES   | SHR S  | %CPU  | %MEM TIME+   | COMMAND    |
| 27776        | admin    |     | 20         | 0     | 3540  |     | 2128  | 1580 R | 16.7  | 0.0 0:00.04  |            |
| /usr/bin/top |          | -b  | -n 2       | -c -o | %CPU  | -w  | 11+   |        |       |              |            |
|              | 1 root   |     | 20         | 0     | 14272 |     | 9468  | 5260 S | 0.0   | 0.1 0:03.23  | /sbin/init |
|              | 2 root   |     | 20         | 0     |       | 0   | 0     | 0 S    | 0.0   | 0.0 0:00.00  | [kthreadd] |
|              | 3 root   |     | 0          | -20   |       | 0   | 0     | 0 I    | 0.0   | 0.0 0:00.00  | [rcu_gp]   |
Only the action Alert, action Syslog, and action CLI details are displayed in this
command.
| Please  | refer       | to  | the | Web UI | for | other             | action | details. |     |     |     |
| ------- | ----------- | --- | --- | ------ | --- | ----------------- | ------ | -------- | --- | --- | --- |
| Command | History     |     |     |        |     |                   |        |          |     |     |     |
| Release |             |     |     |        |     | Modification      |        |          |     |     |     |
| 10.09   |             |     |     |        |     | Commandintroduced |        |          |     |     |     |
| Command | Information |     |     |        |     |                   |        |          |     |     |     |
NetworkAnalyticsEnginecommands|141

Platforms

Command context

Authority

Manager (#)

Administrators or local user group members with execution rights
for this command.

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

show nae-script
show nae-script [vsx-peer]

Description

Shows information about the Aruba Network Analytics Engine scripts that are available on the switch.

Parameter

vsx-peer

Usage

Description

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

This command shows the following information about the Aruba Network Analytics Engine scripts that
are available on the switch:

Script Name

The name of the script. Length: 3 through 80 characters.

Example: system_resource_monitor_mm1.default

Version

The version number of the script.

Origin

The origin of the script:
system

Indicates that the script is provided as part of the system software.

user

Indicates that a user loaded the script.

Status

The current state of the script. Status values are the following:

CREATED

The script has been uploaded to the switch, but script validation has not begun.

ERROR

The script validation process detected an error that would result in execution errors if an agent
runs the script. Resolve the error by modifying the script. For information about the error, see the
Analytics Dashboard of the Web UI.

VALIDATING

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

142

Thescriptsyntaxandcomponents(manifest,parameters,monitor,condition,andaction)arein
theprocessofbeingvalidated.
VALIDATED
Thescriptsyntaxandcomponents(manifest,parameters,monitor,condition,andaction)have
beenvalidatedandnoerrorshavebeenfound.
Example
| switch# | show nae-script |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- |
---------------------------------------------------------------------
| Script Name |     |     | Version | Origin | Status |
| ----------- | --- | --- | ------- | ------ | ------ |
---------------------------------------------------------------------
| fan_monitor                         |         |         | 1.0          | system | VALIDATED |
| ----------------------------------- | ------- | ------- | ------------ | ------ | --------- |
| interface_link_flap_monitor         |         |         | 1.0          | system | VALIDATED |
| interface_link_state_monitor        |         |         | 1.0          | system | VALIDATED |
| interface_tx_rx_stats_monitor       |         |         | 1.0          | system | VALIDATED |
| lag_imbalance_monitor               |         |         | 1.0          | system | VALIDATED |
| lag_status_monitor                  |         |         | 1.0          | system | VALIDATED |
| power_supply_monitor                |         |         | 1.0          | system | VALIDATED |
| stp_bpdu_tcn_rate_monitor           |         |         | 1.0          | system | VALIDATED |
| system_resource_monitor_mm1.default |         |         | 1.0          | system | VALIDATED |
| system_resource_monitor_mm2.default |         |         | 1.0          | system | VALIDATED |
| temp_sensor_monitor                 |         |         | 1.0          | system | VALIDATED |
| Command History                     |         |         |              |        |           |
| Release                             |         |         | Modification |        |           |
| 10.07orearlier                      |         |         | --           |        |           |
| Command Information                 |         |         |              |        |           |
| Platforms                           | Command | context | Authority    |        |           |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --------------- | --- | --- |
6400
8100
8320
8325
8360
8400
9300
10000
| show running-config |     | (nae-lite) |     |     |     |
| ------------------- | --- | ---------- | --- | --- | --- |
show running-config
Description
ShowstheNAE-Literunningconfiguration.
Example
ShowingtheNAE-Lite runningconfiguration:
NetworkAnalyticsEnginecommands|143

| switch# |     | show           | running-config |     |     |     |     |     |     |
| ------- | --- | -------------- | -------------- | --- | --- | --- | --- | --- | --- |
| Current |     | configuration: |                |     |     |     |     |     |     |
!
!Version Halon 0.1.0 (Build: ridley-Halon-0.1.0-master-20161110190644-dev)
| !Schema  |     | version | 0.1.8 |     |     |     |     |     |     |
| -------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- |
| hostname |     | switch  |       |     |     |     |     |     |     |
...
| nae-agent |               | memory_monitor  |             |         |         |             |           |           |        |
| --------- | ------------- | --------------- | ----------- | ------- | ------- | ----------- | --------- | --------- | ------ |
|           | desc          | Memory          | resource    |         | monitor |             |           |           |        |
|           | monitor       |                 | memory      | system  | memory  | line-module |           | 1/3       |        |
|           | set-condition |                 |             | monitor | memory  | gt          | 80        |           |        |
|           |               | status          | major       |         |         |             |           |           |        |
|           |               | syslog          | "High       | memory  | usage   | detected"   |           |           |        |
|           |               | cli             | show system |         |         |             |           |           |        |
|           |               | clear-condition |             |         | monitor | memory      | lt        | 40        |        |
|           |               |                 | status      | normal  |         |             |           |           |        |
|           |               |                 | syslog      | "Memory | usage   | is          | recovered | to normal | limit" |
exit
| nae-agent |               | crash_watch |                |           |           |             |     |     |     |
| --------- | ------------- | ----------- | -------------- | --------- | --------- | ----------- | --- | --- | --- |
|           | desc          | Watch       | the            | crash     | event     |             |     |     |     |
|           | tags          | crash,      | resource       |           |           |             |     |     |     |
|           | watch         | crash_event |                | event-log |           | 1201        |     |     |     |
|           | set-condition |             |                | watch     | event-log | crash_event |     |     |     |
|           |               | status      | major          |           |           |             |     |     |     |
|           |               | cli         | show core-dump |           | all       |             |     |     |     |
exit
| nae-agent |     | crash_watch    |     | activate |          |     |     |     |     |
| --------- | --- | -------------- | --- | -------- | -------- | --- | --- | --- | --- |
| nae-agent |     | memory_monitor |     |          | activate |     |     |     |     |
...
```
| Command   |     | History     |         |         |     |                   |     |     |     |
| --------- | --- | ----------- | ------- | ------- | --- | ----------------- | --- | --- | --- |
| Release   |     |             |         |         |     | Modification      |     |     |     |
| 10.09     |     |             |         |         |     | Commandintroduced |     |     |     |
| Command   |     | Information |         |         |     |                   |     |     |     |
| Platforms |     |             | Command | context |     | Authority         |     |     |     |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     |     |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- |
6400
8100
8320
8325
8360
8400
9300
10000
144
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

|     |     |     |     |         |           | Chapter | 15   |
| --- | --- | --- | --- | ------- | --------- | ------- | ---- |
|     |     |     |     | Network | Analytics | Engine  | Lite |
commands
| Network | Analytics | Engine Lite | commands |     |     |     |     |
| ------- | --------- | ----------- | -------- | --- | --- | --- | --- |
actions
| status    | {normal | | minor | major   | | critical} |     |     |     |     |
| --------- | --------- | --------------- | ----------- | --- | --- | --- | --- |
| no status | {normal   | | minor | major | | critical} |     |     |     |     |
syslog <MESSAGE> [facility {kern | user | mail | daemon | auth | syslog |
| lpr | | uucp | | authpriv | cron | | ftp}] |     |     |     |     |
| --- | -------- | --------------- | ------- | --- | --- | --- | --- |
[severity {debug | info | notice | warning | err | crit | alert | emer}]
no syslog <MESSAGE> [facility {kern | user | mail | daemon | auth | syslog |
| lpr | | uucp | | authpriv | cron | | ftp}] |     |     |     |     |
| --- | -------- | --------------- | ------- | --- | --- | --- | --- |
[severity {debug | info | notice | warning | err | crit | alert | emer}]
cli <COMMAND>
no cli <COMMAND>
Description
ConfiguresdifferentNAE-Liteagentactionstobeperformedwhenthesetconditionortheclear
conditionismet.ThefollowingNAEactionscanbeconfiguredforthesetandclearcondition:
status—SetthealertlevelfortheNAE-LiteAgent.
syslog—Createasyslogmessageandsendittotheconfiguredremotesyslogservers.
cli—ExecuteaCLIcommand.MultipleCLIcommandscanbespecifiedbyusing\nasthedelimiter.
ThenoformofthiscommandremovestheactionsassociatedwiththeNAE-Liteagentcondition.
| Parameter |     |     |     | Description                                  |     |     |     |
| --------- | --- | --- | --- | -------------------------------------------- | --- | --- | --- |
| normal    |     |     |     | SetstheNAE-Liteagentstatustonormal(default). |     |     |     |
minor
SetstheNAE-Liteagentstatustominor.
major
SetstheNAE-Liteagentstatustomajor.
| critical |     |     |     | SetstheNAE-Liteagentstatustocritical.       |     |     |     |
| -------- | --- | --- | --- | ------------------------------------------- | --- | --- | --- |
| <MESSAGE |     |     |     | Specifiesthesyslogmessagetobesentwhentheset |     |     |     |
conditionortheclearconditionismet.Length:3to255
characters.
facility {kern | user | mail | Specifiesthesyslogfacilitycodetodenotethetypeof
daemon | auth | syslog | programthatisloggingthemessage.Thedefaultfacility
lpr | uucp | authpriv | cron | ftp} codeisdaemon.Optional.Thevalidfacilitycodevalues
are:
n kern:Setsthesyslogmessagesourceaskernel.
n user:Setsthesyslogmessagesourceasuserspace
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000Switch
145
Series)

Parameter

Description

programs.

n mail: Sets the syslog message source as mail system.

n daemon: Sets the syslog message source as system

daemon (default).

n auth: Sets the syslog message source as

authentication subsystem.

n syslog: Sets the syslog message source as syslog

daemon.

n lpr: Sets the syslog message source as line printer

subsystem.

n uucp: Sets the syslog message source as unix-to-unix

copy subsystem.

n authpriv: Sets the syslog message source as security

subsystem.

n cron: Sets the syslog message source as cron

scheduler subsystem.

n ftp: Sets the syslog message source as FTP daemon.

[severity {debug | info | notice |

warning | err | crit | alert | emer}]

Specifies the severity level for the syslog message. The
severity level values are:

n debug: Sets the syslog severity level as debug.

n info: Sets the syslog severity as information

(default).

n notice: Sets the syslog severity as notice.

n warning: Sets the syslog severity as warning.

n err: Sets the syslog severity as error.

n crit: Sets the syslog severity as critical.

n alert: Sets the syslog severity as alert.

n emer: Sets the syslog severity as emergency.

Specifies the CLI command to be executed when the set
condition or the clear condition is met.

<COMMAND>

Example

Setting the status level for the NAE-Lite agent condition:

switch(config-nae-agent-condition)# status major

Creating the syslog message for the NAE-Lite agent condition:

switch(config-nae-agent-condition)# syslog "IPSLA server1 is down" severity err

Executing the CLI command for the NAE-Lite agent condition:

Network Analytics Engine Lite commands | 146

switch(config-nae-agent-condition)# cli show version\nshow image
RemovingthedifferentactionsassociatedwiththeNAE-Liteagentcondition:
| switch(config-nae-agent-condition)# |     |     | no status | minor |     |
| ----------------------------------- | --- | --- | --------- | ----- | --- |
switch(config-nae-agent-condition)#
|                                     |         |         | no syslog         | Processing   | system event |
| ----------------------------------- | ------- | ------- | ----------------- | ------------ | ------------ |
| switch(config-nae-agent-condition)# |         |         | no cli            | show logging |              |
| Command History                     |         |         |                   |              |              |
| Release                             |         |         | Modification      |              |              |
| 10.09                               |         |         | Commandintroduced |              |              |
| Command Information                 |         |         |                   |              |              |
| Platforms                           | Command | context | Authority         |              |              |
6200 config-nae-agent- Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 | condition |     | forthiscommand. |     |     |
| ---- | --------- | --- | --------------- | --- | --- |
6400
8320
8325
8360
8400
9300
10000
desc
desc <DESCRIPTION>
no desc <DESCRIPTION>
Description
AddsthedescriptionfortheNAE-Liteagent.
ThenoformofthiscommandremovesthedescriptionfromtheNAE-Liteagent.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<DESCRIPTION> SpecifiesthedescriptionfortheNAE-Liteagent.Range:3to255
characters
Example
AddingthedescriptionfortheNAE-Lite agent:
147
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

| switch(config-nae-agent)# |     | desc | Monitor | system memory |
| ------------------------- | --- | ---- | ------- | ------------- |
RemovingthedescriptionfortheNAE-Lite agent:
| switch(config-nae-agent)# |         | no desc | Monitor           | system memory |
| ------------------------- | ------- | ------- | ----------------- | ------------- |
| Command History           |         |         |                   |               |
| Release                   |         |         | Modification      |               |
| 10.09                     |         |         | Commandintroduced |               |
| Command Information       |         |         |                   |               |
| Platforms                 | Command | context | Authority         |               |
6200 config-nae-agent Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
6400
8100
8320
8325
8360
8400
9300
10000
disable
disable
no disable
Description
DisablestheNAE-liteagent.TheNAE-Liteagentsareenabledbydefault.
ThenoformofthiscommandenablestheNAE-Liteagent.
Example
DisablingtheNAE-Liteagent:
switch(config-nae-agent)#
disable
EnablingtheNAE-Liteagent:
| switch(config-nae-agent)# |     | no disable |     |     |
| ------------------------- | --- | ---------- | --- | --- |
| Command History           |     |            |     |     |
NetworkAnalyticsEngineLitecommands|148

| Release             |         |         | Modification      |     |     |
| ------------------- | ------- | ------- | ----------------- | --- | --- |
| 10.09               |         |         | Commandintroduced |     |     |
| Command Information |         |         |                   |     |     |
| Platforms           | Command | context | Authority         |     |     |
6200 config-nae-agent Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --------------- | --- | --- |
6400
8100
8320
8325
8360
8400
9300
10000
| monitor | resource |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- |
monitor <MONITOR-NAME> resource <RESOURCE> [group-by {count | sum | min | max | average}
| [over {seconds | | minutes | | hours | | days} <DURATION>]] |     |     |
| -------------- | --------- | ------- | -------------------- | --- | --- |
no monitor <MONITOR-NAME> resource <RESOURCE> [group-by {count | sum | min | max |
| average} [over | {seconds | | minutes | | hours | days} | <DURATION>]] |     |
| -------------- | -------- | --------- | --------------- | ------------ | --- |
monitor <MONITOR-NAME> resource <RESOURCE> group-by rate over {seconds | minutes | hours
| | days} <DURATION> |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- |
no monitor <MONITOR-NAME> resource <RESOURCE> group-by rate over {seconds | minutes |
| hours | days} | <DURATION> |     |     |     |     |
| ------------- | ---------- | --- | --- | --- | --- |
Description
ConfiguresthemonitorfortheNAE-Liteagent.Themonitordefineswhatsystemresourcetheagent
mustmonitor.Monitorsaredefinedusingthetimeseriesfunctionanditsupportsthegroupingofdata.
ThenoformofthiscommandremovesthemonitorassociatedwiththeNAE-Liteagent.Before
removingthemonitor,youmustremovetheconditionusedinthemonitor.
| Parameter      |     |     |     |     | Description                   |
| -------------- | --- | --- | --- | --- | ----------------------------- |
| <MONITOR-NAME> |     |     |     |     | Specifiesthenameofthemonitor. |
Length:3to80alphanumeric
characters,includingunderscore
(_).
| <RESOURCE> |     |     |     |     | Specifiesthesystemresources |
| ---------- | --- | --- | --- | --- | --------------------------- |
suchasmemory,CPU,andstorage
The<RESOURCE>isdefinedasfollows:
utilizationforspecificmodulesthat
| n  For8400and6400SwitchSeries: |     |     |     |     | needtobemonitored.Valuesare: |
| ------------------------------ | --- | --- | --- | --- | ---------------------------- |
o system {cpu | memory} {management-module | n cpu:ConfigurestheCPU
| line-module} | <SLOT-ID> |     |     |     | monitoring. |
| ------------ | --------- | --- | --- | --- | ----------- |
n memory:Configuresthe
| o system | storage {nos | | security | |   |     |     |
| -------- | ------------ | ---------- | --- | --- | --- |
memorymonitoring.
| coredump | | logs | | selftest} |     |     |     |
| -------- | ------ | ----------- | --- | --- | --- |
n storage:Configuresthe
149
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

Parameter

Description

management-module <SLOT-ID>

o system storage coredump line-module

<SLOT-ID>

n For 6300 and 6200 Switch Series:

o system {cpu | memory} vsf member <MEMBER-ID>

o system storage {nos | security | coredump |

logs | selftest} vsf member <MEMBER-ID>

n For 8100, 8320, 8325, 8360, and 9300 Switch Series:

o system {cpu | memory}

o system storage {nos | security | coredump |

logs | selftest}

group-by {count | sum | min | max | average}

over {seconds | minutes | hours | days} <DURATION>

storage utilization monitoring.
n management-module: Monitors

resources of the management

module.

n line-module: Monitors

resources of the line module.

n nos: Monitors the network

operating system storage

utilization.

n security: Monitors the

security storage utilization.

n coredump: Monitors the

coredump storage utilization.
n logs: Monitors the log storage

utilization.

n selftest: Monitors the self-

test storage utilization.
n <SLOT-ID>: Configure the

module slot ID. <SLOT-ID> is the

mandatory parameter for

representing the management

module or line module.

n vsf member <MEMBER-ID>:

Configures the VSF member ID.

The member ID is the
mandatory parameter.

Groups the monitored data based
on the parameters specified.
Values are:

n count: Groups by distinct

counts of monitored data.
n sum: Groups by summing the

monitored data.

n min: Groups by minimum value

of the monitored data.
n max: Groups the data by

maximum value of the

monitored data.

n average: Groups by average

value of the monitored data.

Group over the specified time
interval in the past instead of the

Network Analytics Engine Lite commands | 150

Parameter

Description

current value. Values are:

seconds: Sets the time interval in
seconds. Range: 5 to 10000

minutes: Sets the time interval in
minutes. Range: 1 to 10000.

hours: Sets the time interval in
hours. Range: 1 to 10000.

days: Sets the time interval in days.
Range: 1 to 365.

Groups by rate of change of the
monitored data over the specified
time interval.

rate over {seconds | minutes | hours | days} <DURATION>

Example

Configuring the monitor for the system cpu resource on the 1/1 module (8400 and 6400 Switch Series):

switch(config-nae-agent)# monitor sys_cpu resource system cpu management-module
1/1

Configuring the monitor for the calculating the average CPU usage over the 30 minutes (8400 and 6400
Switch Series):

switch(config-nae-agent)# monitor avg_sys_cpu resource system cpu line-module 1/4
group-by average over minutes 30

Configuring the monitor for the system CPU usage on the vsf member 1 (6300 and 6200 Switch Series):

switch(config-nae-agent)# monitor sys_cpu resource system cpu vsf member 1

Configuring the monitor for the system CPU usage:

switch(config-nae-agent)# monitor sys_cpu resource system cpu

Configuring the monitor for calculating the average CPU usage over the 30 minutes duration (8100,
8320, 8325, 8360, and 9300 Switch Series):

switch(config-nae-agent) # monitor avg_sys_cpu resource system cpu group-by
average over minutes 30

Removing the monitor named sys_mem:

switch(config-nae-agent)# no monitor sys_mem

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

151

| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.09               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
6200 config-nae-agent Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
6400
8320
8325
8360
8400
9300
10000
| nae-agent      | lite                |     |     |
| -------------- | ------------------- | --- | --- |
| nae-agent lite | <AGENT-NAME>        |     |     |
| no nae-agent   | lite [<AGENT-NAME>] |     |     |
Description
ConfigurestheNAE-Liteagent.Afterthecommandisexecuted,thecommandpromptentersintothe
nae-agentcontext.ThespecifiednameoftheagentisalsousedasthenameoftheNAEscript
generatedfromtheagentconfigurations.Thereforetheagentnamemustbeuniqueandmustnot
matchwithanyexistingNAEscriptsorNAE-Liteagentnames.
ThenoformofthecommandremovestheNAE-Liteagentconfiguration.Theno nae-agent lite
commandremovesalltheconfiguredNAE-Liteagents.
| Parameter    |     |     | Description                                     |
| ------------ | --- | --- | ----------------------------------------------- |
| <AGENT-NAME> |     |     | SpecifiesthenameoftheNAE-Liteagent.Length:3to80 |
alphanumericcharacters,includingunderscore(_).
Example
ConfiguringNAE-Liteagentnamedmem_monitorandenteringintothenae-agentcontext:
| switch(config)# | nae-agent | lite | mem_monitor |
| --------------- | --------- | ---- | ----------- |
switch(config-nae-agent)#
RemovingtheNAE-Liteagentnamedmem_monitor:
| switch(config-nae-agent)# |     | no nae-agent | lite mem_monitor |
| ------------------------- | --- | ------------ | ---------------- |
RemovingalltheNAE-Liteagentconfigurations:
NetworkAnalyticsEngineLitecommands|152

| switch(config)# |             | no      | nae-agent | lite |                   |     |
| --------------- | ----------- | ------- | --------- | ---- | ----------------- | --- |
| Command         | History     |         |           |      |                   |     |
| Release         |             |         |           |      | Modification      |     |
| 10.09           |             |         |           |      | Commandintroduced |     |
| Command         | Information |         |           |      |                   |     |
| Platforms       |             | Command | context   |      | Authority         |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --- | --------------- | --- |
6400
8100
8320
8325
8360
8400
9300
10000
| nae-agent    |      | lite              | activate |          |     |     |
| ------------ | ---- | ----------------- | -------- | -------- | --- | --- |
| nae-agent    | lite | <AGENT-NAME>      |          | activate |     |     |
| no nae-agent |      | lite <AGENT-NAME> |          | activate |     |     |
Description
ActivatestheNAE-Liteagentcreation.Onceactivated,theNAE-Liteagentgetsgenerated,validated,and
beginsmonitoring.
WhenevermodifyingtheNAE-Liteagentconfiguration,afterallthemodificationsaredone,youmust
triggertheagentupdateprocessbyexecutingno nae-agent lite <AGENT-NAME> activatefollowedby
nae-agent lite <AGENT-NAME> activate.Theagentwillnotbecreatedorupdateduntilthenae-agent
| lite <AGENT-NAME> |     | activatecommandisexecuted. |     |     |     |     |
| ----------------- | --- | -------------------------- | --- | --- | --- | --- |
ThenoformofthecommanddeactivatestheNAE-Liteagent.Oncethecommandisexecuted,theNAE-
Liteagentanditscorrespondingscriptwillbedeleted.
| Parameter    |     |     |     |     | Description                                     |     |
| ------------ | --- | --- | --- | --- | ----------------------------------------------- | --- |
| <AGENT-NAME> |     |     |     |     | SpecifiesthenameoftheNAE-Liteagent.Length:3to80 |     |
alphanumericcharacters,includingunderscore(_).
Example
ActivatingtheNAE-Liteagentnamedcrash_watch:
| switch(config)# |     | nae-agent |     | lite | crash_watch | activate |
| --------------- | --- | --------- | --- | ---- | ----------- | -------- |
DeactivatingtheNAE-Liteagentnamedmem_monitor:
153
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

| switch(config)#     | no      | nae-agent lite | mem_monitor       | activate |
| ------------------- | ------- | -------------- | ----------------- | -------- |
| Command History     |         |                |                   |          |
| Release             |         |                | Modification      |          |
| 10.09               |         |                | Commandintroduced |          |
| Command Information |         |                |                   |          |
| Platforms           | Command | context        | Authority         |          |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
6400
8100
8320
8325
8360
8400
9300
10000
| set-condition | monitor |     |     |     |
| ------------- | ------- | --- | --- | --- |
set-condition monitor <MONITOR-NAME> {{lt | le | eq | ne | gt | ge} <VALUE>[for {seconds
| minutes | hours | days} <DURATION>] | transition from <STRING-LIST> to <STRING-LIST>}
no set-condition monitor <MONITOR-NAME> {{lt | le | eq | ne | gt | ge} <VALUE> [for
{seconds | minutes | hours | days} <DURATION>] | transition from <STRING-LIST> to
<STRING-LIST>}
clear-condition monitor <MONITOR-NAME> {{lt | le | eq | ne | gt | ge} <VALUE> [for
{seconds | minutes | hours | days} <DURATION>] | transition from <STRING-LIST> to
<STRING-LIST>}
no clear-condition monitor <MONITOR-NAME> {{lt | le | eq | ne | gt | ge} <VALUE> [for
{seconds | minutes | hours | days} <DURATION>] | transition from <STRING-LIST> to
<STRING-LIST>}
Description
Definestheconditionforthemonitorresourceevents.Oncetheconditionismet,oneormoreactions
areexecutedbasedontheconfiguration.
Theclearconditionisanoptionalcomponentoftheconditionandhelpsinidentifyingifanevent,
usuallyanissueinthesystem,isnolongeroccurring.Clearconditionsalsoaddresstheproblemwhen
dataisfluctuatingaboveandbelowthethreshold,generatingtoomanyalerts.Initially,whenanNAE-
Liteagentiscreated,onlytheset-conditionisactive.Oncetheset-conditionismet,thecondition
becomesinactiveandtheclearconditionbecomesactive.Theset-conditionbecomesactiveagainonce
theclearconditionismet.
ThenoformofthiscommandremovesthemonitorconditionassociatedwiththeNAE-Liteagent.
NetworkAnalyticsEngineLitecommands|154

Parameter

<MONITOR-NAME>

<VALUE>

Description

Specifies the monitor name used in the condition.

Specifies the numeric value compared with the monitor value. The
defined values are:

n lt (less than)
n le (less than or equal to)
n eq (equal to)
n ne (not equal to)
n gt (greater than)
n ge (greater than or equal to)
n transition

<DURATION>

Specifies the time duration. The defined time duration are:

n seconds (Range: 5-10000)
n minutes (Range: 1-10000)
n hours (Range: 1-10000)
n day

<STRING-LIST>

Specifies the list of one or more strings representing the initial or
final value of the monitor. The strings are comma-separated and
each string must be contained within double-quotes.

Example

Configuring set conditions for the NAE-Lite agent:

switch(config-nae-agent)# set-condition monitor average_mem gt 70

Configuring the set and clear conditions for the NAE-Lite agent:

switch(config-nae-agent)# set-condition monitor cpu gt 70 for minutes 30
switch(config-nae-agent-condition)# clear-condition monitor cpu lt 30 for minutes
30

switch(config-nae-agent)# set-condition monitor line_mdl_state transition from
"ready" to "down","error"
switch(config-nae-agent-condition)# clear-condition monitor line_mdl_state
transition from "down","error" to "ready"

Removing the monitor conditions for the NAE-Lite agent:

switch(config-nae-agent)# no set-condition monitor line_mdl_state transition from
"ready" to "down","error"

switch(config-nae-agent-condition)# no clear-condition monitor cpu lt 30 for
minutes 30

Command History

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

155

| Release             |         |         | Modification      |
| ------------------- | ------- | ------- | ----------------- |
| 10.09               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
6200 config-nae-agent Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
config-nae-agent-
| 6400 | condition |     |     |
| ---- | --------- | --- | --- |
8320
8325
8360
8400
9300
10000
| set-condition | watch |     |     |
| ------------- | ----- | --- | --- |
set-condition watch event-log <WATCH-NAME> [include {all | any} <REGEX-LIST>] [exclude
| <REGEX-LIST>] | [count <COUNT>] |     |     |
| ------------- | --------------- | --- | --- |
no set-condition watch event-log <WATCH-NAME> [include {all | any} <REGEX-LIST>] [exclude
| <REGEX-LIST>] | [count <COUNT>] |     |     |
| ------------- | --------------- | --- | --- |
clear-condition watch event-log <WATCH-NAME> [include {all | any} <REGEX-LIST>] [exclude
| <REGEX-LIST>] | [count <COUNT>] |     |     |
| ------------- | --------------- | --- | --- |
no clear-condition watch event-log <WATCH-NAME> [include {all | any} <REGEX-LIST>]
| [exclude <REGEX-LIST>] |     | [count <COUNT>] |     |
| ---------------------- | --- | --------------- | --- |
Description
Definestheconditionforthewatchresourceevents.Oncetheconditionismet,oneormoreactionsare
executedbasedontheconfiguration.
Theclearconditionisanoptionalcomponentoftheconditionandhelpsinidentifyinganevent,usually
anissueinthesystem,isnolongeroccurring.Clearconditionsalsoaddresstheproblemwhendatais
fluctuatingaboveandbelowthethreshold,andgeneratingtoomanyalerts.Initially,whenanNAE-Lite
agentiscreated,onlytheset-conditionisactive.Oncetheset-conditionismet,theconditionbecomes
inactiveandtheclearconditionbecomesactive.Theset-conditionbecomesactiveagainoncetheclear
conditionismet.
Theconditionismetwhenanyoftheeventlogswatchedbythe<WATCH-NAME>hasoccurredandthe
eventlogmessagefitstheincludeorexclude<REGEX-LIST>(ifconfigured)andtheconditionhas
occurredfor<COUNT>numberoftimes(ifconfigured).
ThenoformofthiscommandremovestheconditionassociatedwiththeNAE-Liteagent.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<WATCH-NAME>
Specifiesthenameofthewatch.Thismustbealreadydefined
usingthewatchcommand.
include {all | any} <REGEX-LIST> Configuresthelistofstringsmatchingtheregularexpression
thatmustbeincludedintheeventlogmessage.Optional.
NetworkAnalyticsEngineLitecommands|156

| Parameter |     | Description |
| --------- | --- | ----------- |
all Includesallofthespecifiedlistsofregularexpressionsinevent-
logmessages.
any Includesanyofthespecifiedlistsofregularexpressionsinevent-
logmessages
<REGEX-LIST>
Specifiesthecomma-separatedlistofoneormoreregular
expressionsthatmustbematchedagainsttheeventlog
messages.Optional.
exclude Configuresthelistofstringsmatchingtheregularexpression
thatmustbeincludedintheeventlogmessage.Optional.
| count <COUNT> |     | Limitsthenumberoftimesthattheconditiontobemet |
| ------------- | --- | --------------------------------------------- |
onceineveryspecifiedcount.Optional.Forexample,ifyou
wanttomonitormacmovementintheVLANforevery10th
time,thenthecountmustbespecifiedas10.
Range:1to4294967295.
Example
Definingtheconditionforthewatchnamedipsla_statusincludingallthespecifiedlist:
switch(config-nae-agent)# set-condition watch event-log ipsla_status
| include all | "servername","failure" | count 3 |
| ----------- | ---------------------- | ------- |
Clearingtheconditionforthewatchnamedipsla_statusincludingallthespecifiedlist:
switch(config-nae-agent-condition)# clear-condition watch ipsla_status
| include all | "servername","success" |     |
| ----------- | ---------------------- | --- |
Definingtheconditionforthewatchnamedipsla_statusexcludingsnmpd:
switch(config-nae-agent-condition)# set-condition watch event-log crash_event
| exclude snmpd |     |     |
| ------------- | --- | --- |
RemovingtheconditionsassociatedwiththeNAE-Liteagent:
switch(config-nae-agent)# no set-condition watch event-log ipsla_status include
all "servername","failure"
switch(config-nae-agent-condition)# no clear-condition watch ipsla_status
| include all     | "servername","success" |     |
| --------------- | ---------------------- | --- |
| Command History |                        |     |
157
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

| Release   |     |             |         |         |     | Modification      |     |     |     |
| --------- | --- | ----------- | ------- | ------- | --- | ----------------- | --- | --- | --- |
| 10.09     |     |             |         |         |     | Commandintroduced |     |     |     |
| Command   |     | Information |         |         |     |                   |     |     |     |
| Platforms |     |             | Command | context |     | Authority         |     |     |     |
6200 config-nae-agent Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     |     |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- |
config-nae-agent-
| 6400 |     |     | condition |     |     |     |     |     |     |
| ---- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
8320
8325
8360
8400
9300
10000
| show | running-config |     |           |     | nae-agent |     |     |     |     |
| ---- | -------------- | --- | --------- | --- | --------- | --- | --- | --- | --- |
| show | running-config |     | nae-agent |     |           |     |     |     |     |
Description
ShowstheNAE-Liteagentcurrentrunningconfigurations.
Example
ShowingtheNAE-Lite runningconfigurations:
| switch# |     | show           | running-config |     | nae-agent |     |     |     |     |
| ------- | --- | -------------- | -------------- | --- | --------- | --- | --- | --- | --- |
| Current |     | configuration: |                |     |           |     |     |     |     |
!
...
| nae-agent |               | lite            | memory_monitor |           |           |             |           |           |        |
| --------- | ------------- | --------------- | -------------- | --------- | --------- | ----------- | --------- | --------- | ------ |
|           | desc          | Memory          | resource       |           | monitor   |             |           |           |        |
|           | monitor       |                 | memory         | system    | memory    | line-module |           | 1/3       |        |
|           | set-condition |                 |                | monitor   | memory    | gt          | 80        |           |        |
|           |               | status          | major          |           |           |             |           |           |        |
|           |               | syslog          | "High          | memory    | usage     | detected"   |           |           |        |
|           |               | cli             | show system    |           |           |             |           |           |        |
|           |               | clear-condition |                |           | monitor   | memory      | lt        | 40        |        |
|           |               |                 | status         | normal    |           |             |           |           |        |
|           |               |                 | syslog         | "Memory   | usage     | is          | recovered | to normal | limit" |
| nae-agent |               | lite            | crash_watch    |           |           |             |           |           |        |
|           | desc          | Watch           | the            | crash     | event     |             |           |           |        |
|           | tags          | crash,          | resource       |           |           |             |           |           |        |
|           | watch         | crash_event     |                | event-log |           | 1201        |           |           |        |
|           | set-condition |                 |                | watch     | event-log | crash_event |           |           |        |
|           |               | status          | major          |           |           |             |           |           |        |
|           |               | cli             | show core-dump |           | all       |             |           |           |        |
| nae-agent |               | lite            | crash_watch    |           | activate  |             |           |           |        |
| nae-agent |               | lite            | memory_monitor |           |           | activate    |           |           |        |
...
```
| Command |     | History |     |     |     |     |     |     |     |
| ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
NetworkAnalyticsEngineLitecommands|158

| Release             |         |         | Modification      |
| ------------------- | ------- | ------- | ----------------- |
| 10.09               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
6400
8100
8320
8325
8360
8400
9300
10000
tags
tags <TAG-LIST>
no tags <TAG-LIST>
Description
ConfiguresthetagsapplicablefortheNAE-Liteagent.Thetagsareusedtocategorizeandgroupthe
agent.
ThenoformofthiscommandremovesthetaglistsassociatedwiththeNAE-Liteagent.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<TAG-LIST> SpecifiesthetaglistfortheNAE-Liteagent.<TAG-LIST>isthe
commaseparatedlistoftags.Eachtagcanbeaminimumof3toa
maximumof32charactersinlength.Amaximumof16tagsare
supported.
Example
ConfiguringthetagsfortheNAE-Lite agent:
| switch(config-nae-agent)# |     | tags | memory,resource,ztag |
| ------------------------- | --- | ---- | -------------------- |
RemovingthetagsfortheNAE-Liteagent:
| switch(config-nae-agent)# |     | no tags |                 |
| ------------------------- | --- | ------- | --------------- |
| switch(config-nae-agent)# |     | no tags | memory,resource |
| Command History           |     |         |                 |
159
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

| Release             |         |         |     | Modification      |     |     |     |
| ------------------- | ------- | ------- | --- | ----------------- | --- | --- | --- |
| 10.09               |         |         |     | Commandintroduced |     |     |     |
| Command Information |         |         |     |                   |     |     |     |
| Platforms           | Command | context |     | Authority         |     |     |     |
6200 config-nae-agent Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- | --- |
6400
8100
8320
8325
8360
8400
9300
10000
| watch event-log       |     |           |                 |     |     |     |     |
| --------------------- | --- | --------- | --------------- | --- | --- | --- | --- |
| watch <WATCH-NAME>    |     | event-log | <EVENT-ID-LIST> |     |     |     |     |
| no watch <WATCH-NAME> |     | event-log | <EVENT-ID-LIST> |     |     |     |     |
Description
ConfiguresthewatchsourcefortheNAE-Liteagent.Thisenablestheagenttowatchforspecificevents
occurringinthesystem.Event-drivenmonitoringcanbeperformedbywatchingtheeventlogofthe
system.
ForinformationoneventIDs,refertotheEventLogMessageReferenceGuide.
ThenoformofthiscommandremovesthewatchassociatedwiththeNAE-Liteagent.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<WATCH-NAME> SpecifiesthewatchnamefortheNAE-Liteagent.Length:3to80
alphanumericcharacters,includingunderscore(_).
<EVENT-ID-LIST> SpecifiesthelistofoneormoreeventIDsoftheeventlog
message.AmaximumoffiveeventIDscanbespecified.
Example
ConfiguringthewatchsourcefortheNAE-Liteagent.
| switch(config-nae-agent)# |     |     | watch | crash_event | event-log | 1201 |     |
| ------------------------- | --- | --- | ----- | ----------- | --------- | ---- | --- |
RemovingthewatchsourceusedbytheNAE-Lite agent:
| switch(config-nae-agent)# |     |     | no watch | high_mem |     |     |     |
| ------------------------- | --- | --- | -------- | -------- | --- | --- | --- |
switch(config-nae-agent)#
|     |     |     | no watch | high_mem_event | event-log |     | 1208,1209 |
| --- | --- | --- | -------- | -------------- | --------- | --- | --------- |
NetworkAnalyticsEngineLitecommands|160

| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.09               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
6200 config-nae-agent Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
6400
8100
8320
8325
8360
8400
9300
10000
161
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

Chapter 16

HTTPS server commands

HTTPS server commands

https-server authentication certificate
https-server authentication certificate [authorization radius] [username {<CERT-FIELD>}]

Description

Enables authentication using an x509 certificate for authentication. When this option is configured, the
https-server uses the user specified certificate for authentication, and the specified authorization
mechanism is used to obtain the corresponding user role. The username embedded in the certificate is
used for authorization with a remote user database.

Enabling password authentication is the only way of disabling certificate authentication.

Only one authentication method can be enabled at a time. If you want to disable certificate-based authentication,

then the password-based authentication must be enabled.

Parameter

Description

<AUTHORIZATION-RADIUS>

<CERT-FIELD>

Specifies that after certificate authentication succeeds, instead of
prompting for a password, the HTTPS server checks the RADIUS
server only for authorization.
When this parameter is omitted, authorization radius is still
the assumed active setting.

Selects which certificate username field is to be used for
authorization.
n Specify user_pincipal_name to use the certificate
UserPrincipalName (UPN) field. This is the default.

n Specify common_name to use the certificate CommonName

(CN) field.

When this parameter is omitted, user_pincipal_name is
assumed.

Example

Enabling authentication using the certificate:

switch(config)# https-server authentication certificate authorization radius
username common_name

Command History

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

162

| Release   |             |     |         | Modification       |     |     |
| --------- | ----------- | --- | ------- | ------------------ | --- | --- |
| 10.11     |             |     |         | Commandintroduced. |     |     |
| Command   | Information |     |         |                    |     |     |
| Platforms | Command     |     | context | Authority          |     |     |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
| 6200 |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- |
6300
6400
8100
8320
8325
8360
8400
9300
10000
| https-server |                | authentication |          |     | password |     |
| ------------ | -------------- | -------------- | -------- | --- | -------- | --- |
| https-server | authentication |                | password |     |          |     |
Description
Enablesauthenticationusingusernameandpassword,whichcorrespondstothedefaultauthentication
mechanism.Enablingthepasswordauthenticationmodedisablesthecertificateauthenticationmode.
Onlyoneauthenticationmethodcanbeenabledatatime.
Example
Enablingauthenticationusingthepassword:
| switch(config)# |             | https-server |         | authentication     |     | password |
| --------------- | ----------- | ------------ | ------- | ------------------ | --- | -------- |
| Command         | History     |              |         |                    |     |          |
| Release         |             |              |         | Modification       |     |          |
| 10.11           |             |              |         | Commandintroduced. |     |          |
| Command         | Information |              |         |                    |     |          |
| Platforms       | Command     |              | context | Authority          |     |          |
4100i config Administratorsorlocalusergroupmemberswithexecutionrights
| 6200 |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- |
6300
6400
HTTPSservercommands|163

| Platforms | Command |     | context |     | Authority |     |
| --------- | ------- | --- | ------- | --- | --------- | --- |
8100
8320
8325
8360
8400
9300
10000
| https-server |                   | max-user-sessions |     |               |     |     |
| ------------ | ----------------- | ----------------- | --- | ------------- | --- | --- |
| https-server | max-user-sessions |                   |     | <SESSION-AMT> |     |     |
Description
SetsthemaximumamountofconcurrentopensessionsforanygivenuserthroughtheHTTPSserver.
Theamountofconcurrentopensessionsmayhaveanimpactonsystemperformance,soitis
recommendedtosetthisvaluetotheminimumnecessary.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<SESSION-AMT>
Specifiesthemaximumnumberofusersessionsallowed.
Default: 6.Maximumvalue: 8.
Example
Setthemaximumnumberofconcurrentusersessionstothemaximumof8:
| switch(config)# |             | https-server |         | max-user-sessions |                   | 8   |
| --------------- | ----------- | ------------ | ------- | ----------------- | ----------------- | --- |
| Command         | History     |              |         |                   |                   |     |
| Release         |             |              |         |                   | Modification      |     |
| 10.08           |             |              |         |                   | Commandintroduced |     |
| Command         | Information |              |         |                   |                   |     |
| Platforms       | Command     |              | context |                   | Authority         |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| https-server |      | rest        | access-mode |            |               |     |
| ------------ | ---- | ----------- | ----------- | ---------- | ------------- | --- |
| https-server | rest | access-mode |             | {read-only | | read-write} |     |
Description
ChangestheRESTAPIaccessmode.Thedefaultmodeisread-write.
164
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

| Parameter  |     |     |     |     | Description                                       |     |
| ---------- | --- | --- | --- | --- | ------------------------------------------------- | --- |
| read-write |     |     |     |     | Selectstheread/writemode.AllowsPOST,PUT,PATCH,and |     |
DELETEmethodstobecalledonallconfigurableelementsinthe
switchdatabase.
| read-only |     |     |     |     | Selectstheread-onlymode.Writeaccesstomostswitch |     |
| --------- | --- | --- | --- | --- | ----------------------------------------------- | --- |
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
| switch(config)# |             | https-server |         | rest | access-mode  | read-only |
| --------------- | ----------- | ------------ | ------- | ---- | ------------ | --------- |
| Command         | History     |              |         |      |              |           |
| Release         |             |              |         |      | Modification |           |
| 10.07orearlier  |             |              |         |      | --           |           |
| Command         | Information |              |         |      |              |           |
| Platforms       | Command     |              | context |      | Authority    |           |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| https-server |         | session |     | close | all |     |
| ------------ | ------- | ------- | --- | ----- | --- | --- |
| https-server | session | close   | all |       |     |     |
Description
HTTPSservercommands|165

InvalidatesandclosesallHTTPSsessions.AllexistingWebUIandRESTsessionsareloggedoutandall
real-timenotificationfeatureWebSocketconnectionsareclosed.
Usage
Typically,auserthathasconsumedtheallowedconcurrentHTTPSsessionsandisunabletoaccessthe
sessioncookietologoutmanuallymustwaitforthesessionidletimeouttostartanothersession.This
commandisintendedasaworkaroundtowaitingfortheidletimeouttocloseanHTTPSsession.This
commandstopsandstartsthehpe-restdservice,sousingthiscommandaffectsallexistingREST
sessions,WebUIsessions,andreal-timenotificationsubscriptions.
Example
| switch#        | https-server |     | session | close | all          |     |
| -------------- | ------------ | --- | ------- | ----- | ------------ | --- |
| Command        | History      |     |         |       |              |     |
| Release        |              |     |         |       | Modification |     |
| 10.07orearlier |              |     |         |       | --           |     |
| Command        | Information  |     |         |       |              |     |
| Platforms      | Command      |     | context |       | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| https-server |                 | session-timeout |     |           |     |     |
| ------------ | --------------- | --------------- | --- | --------- | --- | --- |
| https-server | session-timeout |                 |     | <MINUTES> |     |     |
Description
Configuresthetimeout,inminutes,foranygivenHTTPSserversession.Avalueof0disablesthe
timeout.ThiscommanddoesnotaffectsessionsusedforCentralconnections.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<MINUTES>
Specifiesthemaximumidletime,inminutesforanHTTPSsession.
Default: 20.Maximum: 480(8hours).0disablesthetimeout,but
themaxiumisstillenforced.
Example
| switch(config)# |         | https-server |     | session-timeout |     | 10  |
| --------------- | ------- | ------------ | --- | --------------- | --- | --- |
| Command         | History |              |     |                 |     |     |
166
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

| Release             |         |         | Modification      |
| ------------------- | ------- | ------- | ----------------- |
| 10.08               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| https-server    | vrf            |     |     |
| --------------- | -------------- | --- | --- |
| https-server    | vrf <VRF-NAME> |     |     |
| no https-server | vrf <VRF-NAME> |     |     |
Description
ConfiguresandstartstheHTTPSserveronthespecifiedVRF,allowingaccesstoRESTandtheWebUI
fromportsassignedtothatVRF.ThiscommanddoesnotaffectaccesstoCentralinstances,asthis
featurehasitsowndedicatedconnectionchannel
ThenoformofthecommandstopsanyHTTPSserversrunningonthespecifiedVRFandremovesthe
HTTPSserverconfiguration.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
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
| in404 Not Founderrors. |     |     |     |
| ---------------------- | --- | --- | --- |
TheVRFyouselectdeterminesfromwhichnetworktheWebUIandRESTAPIcanbeaccessed.
Forexample:
n IfyouwanttoenableaccesstotheRESTAPIandWebUIthroughtheOOBMport(managementIP
address),specifythebuilt-inmanagementVRF(mgmt).
n IfyouwanttoenableaccesstotheRESTAPIandWebUIthroughthedataports(for"inband
management"),specifythebuilt-indefaultVRF(default).
n IfyouwanttoenableaccesstotheRESTAPIandWebUIthroughonlyasubsetofdataportsonthe
switch,specifyotherVRFsyouhavecreated.
ArubaNetworkAnalyticsEnginescriptsruninthedefaultVRF,butyoudonothavetoenableHTTPS
serveraccessonthedefaultVRFforthescriptstorun.IftheswitchhascustomArubaNetworkAnalytics
HTTPSservercommands|167

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
Description
ShowsthestatusandconfigurationoftheHTTPSserver.TheRESTAPIandwebuserinterfaceare
accessibleonlyonVRFsthathavetheHTTPSserverfeaturesconfigured.
168
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

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
Showsthehttps-serverauthenticationmodestatus.
Examples
HTTPSservercommands|169

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
executionrightsforthiscommand.Operatorscanexecutethis
| 6200 | (#) |     |     |
| ---- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
6300
6400
8100
8320
8325
8360
8400
9300
10000
170
AOS-CX10.12NetworkAnalyticsEngineGuide| (6200,6300,6400,8xxx,9300,10000SwitchSeries)

Support and Other Resources

Chapter 17

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

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch

Series)

171

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
SupportandOtherResources|172

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

AOS-CX 10.12 Network Analytics Engine Guide | (6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

173