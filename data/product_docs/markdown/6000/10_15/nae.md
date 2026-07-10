| AOS-CX |           | 10.15.xxxx |        |        | Network |       |
| ------ | --------- | ---------- | ------ | ------ | ------- | ----- |
|        | Analytics |            | Engine |        | Guide   |       |
| 5420,  | 6200,     | 6300,      | 6400,  | 8320,  | 8325,   | 8360, |
|        | 8400,     | 9300,      | 10000  | Switch | Series  |       |
Published:January2025
Version:1

Copyright Information

© Copyright 2025 Hewlett Packard Enterprise Development LP.

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

3

Contents
| About this                                       | document                   |        |              | 10  |
| ------------------------------------------------ | -------------------------- | ------ | ------------ | --- |
| Applicableproducts                               |                            |        |              | 10  |
| Latestversionavailableonline                     |                            |        |              | 10  |
| Commandsyntaxnotationconventions                 |                            |        |              | 11  |
| Abouttheexamples                                 |                            |        |              | 11  |
| Identifyingswitchportsandinterfaces              |                            |        |              | 12  |
| Identifyingmodularswitchcomponents               |                            |        |              | 13  |
| Aruba Network                                    | Analytics                  | Engine | Introduction | 14  |
| AOS-CXWebUIforAnalyticsintroduction              |                            |        |              | 14  |
| ArubaNetworkAnalyticEnginescriptsintroduction    |                            |        |              | 14  |
| ArubaNetworkAnalyticagentsintroduction           |                            |        |              | 15  |
| Built-inscriptsandagents                         |                            |        |              | 15  |
| Aruba-certifiedscripts                           |                            |        |              | 16  |
| ArubaSolutionsExchange(ASE)introduction          |                            |        |              | 16  |
| User-createdscripts                              |                            |        |              | 16  |
| DevelopercommunitiesfortheNetworkAnalyticsEngine |                            |        |              | 17  |
|                                                  | ArubaSolutionExchange(ASE) |        |              | 17  |
|                                                  | GitHub                     |        |              | 17  |
|                                                  | AirheadsCommunity          |        |              | 17  |
| ArubaNetworkAnalyticsEnginesupportedmaximums     |                            |        |              | 17  |
AOS-CX Network Analytics Engine (NAE) Design considerations 19
| NAEfactorsthatimpactsystemresources                |           |        |           | 19  |
| -------------------------------------------------- | --------- | ------ | --------- | --- |
| NAEdeploymentconsiderations                        |           |        |           | 19  |
| ConsiderationswhenwritinganNAEagent                |           |        |           | 20  |
| Aruba Network                                      | Analytics | Engine | framework | 21  |
| Configurationandstatedatabase                      |           |        |           | 21  |
| Timeseriesdatabase                                 |           |        |           | 21  |
| AOS-CXRESTAPI                                      |           |        |           | 22  |
| PythonandtheRESTAPIforscripts                      |           |        |           | 22  |
| "Sandboxes"foragentactions                         |           |        |           | 23  |
| Managing                                           | scripts   |        |           | 24  |
| ManagingNAEscriptsacrossswitchsoftwareupdates      |           |        |           | 24  |
| ViewingscriptdetailsusingtheWebUI                  |           |        |           | 25  |
| DownloadingascriptusingtheWebUI                    |           |        |           | 26  |
| UploadingascriptusingtheWebUI                      |           |        |           | 27  |
| UpdatingascriptusingtheWebUI                       |           |        |           | 28  |
| DeletingascriptusingtheWebUI                       |           |        |           | 28  |
| GettinginformationaboutscriptsusingtheRESTAPI      |           |        |           | 29  |
| UploadingascriptusingtheRESTAPI                    |           |        |           | 30  |
| UpdatingascriptusingtheRESTAPI                     |           |        |           | 31  |
| DeletingascriptusingtheRESTAPI                     |           |        |           | 31  |
| DownloadingascriptfromtheswitchusingtheRESTAPI     |           |        |           | 32  |
| showrunning-configcommandoutputforagentsandscripts |           |        |           | 32  |
| Scriptstatus                                       |           |        |           | 33  |
5
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide| (5420,6200,6300,6400,8xxx,9300,10000SwitchSeries)

| Managing                                            | agents                                 |     |     |     |     | 34  |
| --------------------------------------------------- | -------------------------------------- | --- | --- | --- | --- | --- |
| ViewingalistofagentsinstalledonaswitchusingtheWebUI |                                        |     |     |     |     | 34  |
| ViewingagentinformationusingtheWebUI                |                                        |     |     |     |     | 34  |
| FindingalertdetailsusingtheWebUI                    |                                        |     |     |     |     | 38  |
| WorkingwithanAnalyticstimeseriesgraph               |                                        |     |     |     |     | 40  |
|                                                     | Customizingdatadisplayedonthegraph     |     |     |     |     | 41  |
|                                                     | Zoominginonthegraph                    |     |     |     |     | 42  |
|                                                     | Downloadingthegraphasanimageor.csvfile |     |     |     |     | 43  |
|                                                     | Viewinganalertonthegraph               |     |     |     |     | 43  |
| EnablingadisabledagentusingtheWebUI                 |                                        |     |     |     |     | 46  |
| DisablinganagentusingtheWebUI                       |                                        |     |     |     |     | 46  |
| DeletinganagentusingtheWebUI                        |                                        |     |     |     |     | 47  |
| CreatinganagentfromanexistingscriptusingtheWebUI    |                                        |     |     |     |     | 47  |
| ChangingtheconfigurationofanagentusingtheWebUI      |                                        |     |     |     |     | 48  |
| GettinginformationaboutagentsusingtheRESTAPI        |                                        |     |     |     |     | 49  |
| CreatinganagentfromanexistingscriptusingtheRESTAPI  |                                        |     |     |     |     | 50  |
| EnablinganagentusingtheRESTAPI                      |                                        |     |     |     |     | 51  |
| DisablinganagentusingtheRESTAPI                     |                                        |     |     |     |     | 51  |
| ChangingtheconfigurationofanagentusingtheRESTAPI    |                                        |     |     |     |     | 52  |
| DeletinganagentusingtheRESTAPI                      |                                        |     |     |     |     | 53  |
ShowingtheCurrentandMaximumNumberofAgents,Monitors,andScripts 53
| Agentstatus                                       |       |            |        |     |     | 55  |
| ------------------------------------------------- | ----- | ---------- | ------ | --- | --- | --- |
| Behaviorswhenmultipleagentsmonitorthesameresource |       |            |        |     |     | 55  |
| Troubleshooting                                   | agent | and script | issues |     |     | 57  |
Showingthecurrentandmaximumnumberofagents,monitors,andscripts 57
| HighswitchCPUandmemoryusageareaffectingswitchperformance |                       |     |     |     |     | 59  |
| -------------------------------------------------------- | --------------------- | --- | --- | --- | --- | --- |
| DownloadingNAEsupportfiles                               |                       |     |     |     |     | 59  |
|                                                          | NAEsupportfilecontent |     |     |     |     | 60  |
| Error:"Switchtimeandbrowsertimearenotinsync"             |                       |     |     |     |     | 60  |
Analyticstimeseriesgraphdisplaysmessageinsteadofdata:"Agentdatanotfound,please
| verify..."                                            |     |     |     |     |     | 61  |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| Inaccurateornodatadisplayedinanalyticstimeseriesgraph |     |     |     |     |     | 62  |
| URIerrors                                             |     |     |     |     |     | 63  |
Error:"TheNAEAgentisnotcreated...DBconstraintviolationerrors" 63
| Error:"TheNAEAgenthasPythonerrors." |     |     |     |     |     | 64  |
| ----------------------------------- | --- | --- | --- | --- | --- | --- |
Error:"Timeseriesdatacannotbegenerated...TheURIisinvalidornotconfigured" 65
| Error:"Thescriptsyntaxisinvalid"                          |           |            |           |          |           | 66  |
| --------------------------------------------------------- | --------- | ---------- | --------- | -------- | --------- | --- |
| Error:"Thescriptagentsyntaxisinvalid"                     |           |            |           |          |           | 66  |
| Error:"Sandboxtimedoutwhilerunningscript"                 |           |            |           |          |           | 66  |
| Error:"Theagentinstantiatedsandboxhastimedout"            |           |            |           |          |           | 67  |
| Error:"Unabletoparseconditionexpression..."               |           |            |           |          |           | 68  |
| Error:"TheCLIcommandisinvalid"                            |           |            |           |          |           | 69  |
| Error:"Commandfailed:non-zeroexitstatus"                  |           |            |           |          |           | 69  |
| Error:"Theactionisinvalid"                                |           |            |           |          |           | 70  |
| ActionShelloutputerror:"notavailableinenhancedsecuremode" |           |            |           |          |           | 70  |
| Using the                                                 | HPE Aruba | Networking | Solutions | Exchange | Solutions |     |
| Exchange                                                  |           |            |           |          |           | 72  |
| FindingNAEscriptsontheASEwebsite                          |           |            |           |          |           | 72  |
| FindingNAEscriptsontheASEusingtheWebUI                    |           |            |           |          |           | 72  |
| ViewingrecentchangestoexistingNAEsolutions                |           |            |           |          |           | 73  |
| DownloadingorinstallingascriptfromtheASEusingtheWebUI     |           |            |           |          |           | 73  |
| DownloadingasolutionfromtheASEwebsitetoyourworkstation    |           |            |           |          |           | 74  |
|6

| NAE                            | scripts repository                             | on GitHub | 76  |
| ------------------------------ | ---------------------------------------------- | --------- | --- |
| Scripts                        | and security                                   |           | 77  |
| Scripts                        |                                                |           | 78  |
| Pythonversionandlibrarysupport |                                                |           | 78  |
|                                | Pythonmodulesavailable                         |           | 78  |
|                                | Third-partyPythonlibrariesavailable            |           | 80  |
| RESTAPIversionsupport          |                                                |           | 80  |
| Rulesforscriptfiles            |                                                |           | 80  |
| Scriptexample                  |                                                |           | 80  |
| Partsofascript                 |                                                |           | 82  |
| Header                         |                                                |           | 83  |
| Importstatements               |                                                |           | 84  |
| Manifest                       |                                                |           | 84  |
|                                | Requireditems                                  |           | 84  |
|                                | Optionalitems                                  |           | 84  |
| AlertDescriptionAPI            |                                                |           | 86  |
| Parameterdefinitions           |                                                |           | 87  |
|                                | ParameterDefinitionsdescription                |           | 87  |
| Agentclassconstructor          |                                                |           | 88  |
|                                | Graph                                          |           | 89  |
|                                | Title                                          |           | 90  |
|                                | on_agent_re_enable                             |           | 91  |
|                                | on_agent_restart                               |           | 91  |
|                                | on_parameter_change                            |           | 92  |
|                                | Baselinesfordynamicthresholdsformonitors       |           | 93  |
|                                | Baselineworkflowandconsiderations              |           | 93  |
|                                | Exampleofbaselinesinatimeseriesgraph           |           | 95  |
|                                | Exampleofascriptthatusesbaselines              |           | 96  |
|                                | Baseline                                       |           | 97  |
|                                | ADCs                                           |           | 100 |
|                                | ADCListclass                                   |           | 102 |
|                                | ADCEntryclass                                  |           | 103 |
| Monitors                       |                                                |           | 105 |
|                                | URIsformonitors                                |           | 106 |
|                                | PathcomponentoftheURI                          |           | 106 |
|                                | QuerycomponentoftheURI                         |           | 106 |
|                                | WildcardcharactersinmonitoredURIs              |           | 107 |
|                                | ParametersinmonitoredURIs                      |           | 108 |
|                                | Slash(/)charactersinmonitoredURIs              |           | 109 |
|                                | AttributefiltersinmonitoredURIs                |           | 109 |
|                                | ConstructingaURIusingtheAOS-CXRESTAPIReference |           | 110 |
|                                | Aggregateoperators                             |           | 112 |
|                                | Aggregatefunctions                             |           | 113 |
|                                | Nestedaggregatefunctionsandoperators           |           | 114 |
|                                | Aggregatefunctionsinmonitorsandconditions      |           | 115 |
| Rules                          |                                                |           | 115 |
| Conditions                     |                                                |           | 116 |
|                                | Clearconditions                                |           | 117 |
|                                | Conditionexpressionsyntax                      |           | 117 |
Durations,evaluationdelays,andpausesinconditionexpressions 118
Conjunction(AND),disjunction(OR),andmultiplesubconditions 119
|         | FunctionbehaviorwhenmonitoredURIdoesnotcontainwildcards |     | 120 |
| ------- | ------------------------------------------------------- | --- | --- |
|         | FunctionbehaviorwhenmonitoredURIhaswildcards            |     | 120 |
| Actions |                                                         |     | 122 |
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 7

|                                       | Predefinedactions         |        |               | 122 |
| ------------------------------------- | ------------------------- | ------ | ------------- | --- |
|                                       | ActionCLI,CLIaction       |        |               | 122 |
|                                       | ActionCustomReport        |        |               | 123 |
|                                       | ActionShell,SHELLaction   |        |               | 125 |
|                                       | ActionSyslog,Syslogaction |        |               | 126 |
|                                       | Callbackactions           |        |               | 127 |
|                                       | Clearactions              |        |               | 128 |
|                                       | Alertlevelfunctions       |        |               | 129 |
|                                       | Loggingfunctions          |        |               | 130 |
| Agents                                |                           |        |               | 131 |
| Agentsanduserauthority                |                           |        |               | 131 |
| Rulesforagentnames                    |                           |        |               | 131 |
| Updatingagentsparametervalue          |                           |        |               | 131 |
| NetworkAnalyticsEngineSafeguards      |                           |        |               | 131 |
|                                       | IO Limiting               |        |               | 132 |
|                                       | TimeSeriesLimiting        |        |               | 132 |
|                                       | AlertThrottling           |        |               | 132 |
|                                       | RulesLimiting             |        |               | 132 |
|                                       | AlertSizeLimiting         |        |               | 132 |
| Network                               | Analytics                 | Engine | Lite          | 133 |
| UseCases                              |                           |        |               | 135 |
| Network                               | Analytics                 | Engine | commands      | 141 |
| naecli-authorization                  |                           |        |               | 141 |
| shownae-agent                         |                           |        |               | 142 |
| shownae-agentalerts                   |                           |        |               | 144 |
| shownae-agentalertsdetails            |                           |        |               | 146 |
| shownae-script                        |                           |        |               | 147 |
| uerieshowrunning-config(nae-lite)     |                           |        |               | 149 |
| Network                               | Analytics                 | Engine | Lite commands | 150 |
| actions(NAE-Lite)                     |                           |        |               | 150 |
| desc                                  |                           |        |               | 156 |
| disable                               |                           |        |               | 157 |
| monitorresource                       |                           |        |               | 158 |
| nae-agentlite                         |                           |        |               | 161 |
| nae-agentliteactivate                 |                           |        |               | 162 |
| 2set-conditionmonitor                 |                           |        |               | 163 |
| 5set-conditionwatch                   |                           |        |               | 165 |
| showrunning-confignae-agent           |                           |        |               | 167 |
| tags                                  |                           |        |               | 168 |
| watchevent-log                        |                           |        |               | 170 |
| HTTPS                                 | server commands           |        |               | 172 |
| https-serverauthenticationcertificate |                           |        |               | 172 |
| https-serverauthenticationpassword    |                           |        |               | 173 |
| https-servermax-user-sessions         |                           |        |               | 173 |
| https-serverrestaccess-mode           |                           |        |               | 174 |
| https-serversessioncloseall           |                           |        |               | 175 |
| https-serversession-timeout           |                           |        |               | 176 |
| https-servervrf                       |                           |        |               | 177 |
| showhttps-server                      |                           |        |               | 178 |
| showhttps-serverauthentication        |                           |        |               | 180 |
|8

| Support                            | and Other | Resources | 181 |
| ---------------------------------- | --------- | --------- | --- |
| AccessingHPEArubaNetworkingSupport |           |           | 181 |
| AccessingUpdates                   |           |           | 182 |
| WarrantyInformation                |           |           | 182 |
| RegulatoryInformation              |           |           | 182 |
| DocumentationFeedback              |           |           | 182 |
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 9

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing HPE Aruba Networking switches on
a network.

Applicable products

This document applies to the following products:

n HPE Aruba Networking 5420 Switch Series (S0U67A, S0U55A, S0U63A, S0U64A, S0U65A, S0U75A,

S0U72A, S0U78A, S0U58A, S0U73A, S0U74A, S0U71A, S0U76A, S0U70A, S0U77A, S0U60A, S0U61A,
S0U62A, S0U66A, S0U68A)

n HPE Aruba Networking 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A, R8Q68A,
R8Q69A, R8Q70A, R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A, JL724B, JL725B,
JL726B, JL727B, JL728B, S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,  S0M87A,  S0M88A,
S0M89A,  S0M90A, S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

n HPE Aruba Networking 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A,

JL665A, JL666A, JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A, S0X44A, S3L75A,
S3L76A, S3L77A)

n HPE Aruba Networking 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B,
R0X40C, R0X41A, R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C,
R0X26A, R0X27A, JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

n HPE Aruba Networking 8100 Switch Series (R9W94A, R9W95A, R9W96A, R9W97A)

n HPE Aruba Networking 8320 Switch Series (JL479A, JL579A, JL581A)

n HPE Aruba Networking 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n HPE Aruba Networking 8325H Switch Series (S4B20A, S4B21A, S4B22A, S4B23A, S2T42A, S2T46A,

S2T47A, S2T48A)

n HPE Aruba Networking 8325P Switch Series (S0G12A, S4A48A)

n HPE Aruba Networking 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A,

JL709A, JL710A, JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C, JL709C, JL710C, JL711C,
JL704C, JL705C, JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

n HPE Aruba Networking 8400 Switch Series (JL366A, JL363A, JL687A)

n HPE Aruba Networking 9300 Switch Series (R9A29A, R9A30A, R8Z96A, S0F81A, S0F82A, S0F83A,

S0F84A, S0F85A, S0F86A, S0F87A, S0F88A, S0F95A, S0F96A)

n HPE Aruba Networking 10000 Switch Series (R8P13A, R8P14A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

10

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

About this document | 11

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
format: member/slot/port.

On the HPE Aruba Networking 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

On the HPE Aruba Networking 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.
The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the HPE Aruba Networking 6400 and 5420 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
member 1.

On the HPE Aruba Networking 8xxx, 9300/9300S, and 10000 Switch Series

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

12

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on physical port 4 in slot 1 on

member 1.

On the HPE Aruba Networking 8400 Switch Series

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

About this document | 13

Aruba Network Analytics Engine

Chapter 2

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

14

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

Aruba Network Analytics Engine Introduction | 15

n Built-inscript:system_resource_monitor
n Built-inagent:system_resource_monitor.default
| Aruba-certified |     | scripts |     |
| --------------- | --- | ------- | --- |
Aruba-certifiedNetworkAnalyticsEnginescriptsarewrittenandtestedbyAruba.
OntheArubaSolutionExchange,Aruba-certifiedscriptshavethefollowingtag:nae-aruba-certified
| Figure1 | ScripttagsasshownontheArubaSolutionExchange |          |                    |
| ------- | ------------------------------------------- | -------- | ------------------ |
| Figure2 | ScripttagsasshownintheWebUI                 |          |                    |
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
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 16

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

Aruba Network Analytics Engine Introduction | 17

n Number of days of time-series data to store: 400

n Amount of switch storage allocated to time-series data: 18 GB

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

18

AOS-CX Network Analytics Engine (NAE)

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
switches within the network prior to a wider deployment of such agent. NAE agents published by HPE
Aruba Networking have been tested for many customer deployments, but do not cover all cases.
Customer networks can be unique and may exhibit differences compared to a controlled lab
environment.

All new NAE agents deployed within a customer network should be initially monitored to ensure that it is
performing according to expectations. The switch CPU and memory utilization can be reviewed through
the built-in System Resource Monitor NAE agent which provides the current and running history of

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

19

resource consumption. Storage usage can be monitored by reviewing the endurance utilization under
the show system resource-utilization command over time.

There have been instances where the initial deployment of an NAE agent within a customer network
helped identify network oddity or misconfiguration from the start. The initial review of any NAE alerts
issued by this agent would quickly point out these misconfigurations. After making the necessary switch
or network changes, any future alerts would be reduced. As an example, a high number of RX drops
may indicate a bad fiber cable. Replacement of this cable would then result in less or zero RX drops and
the NAE agent will stop issuing alerts.

NAE agents are published through the HPE Aruba Networking Solutions Exchange and, much like switch
firmware, can be updated at any time. It is recommended that customers periodically check the HPE
Aruba Networking Solutions Exchange website for any updates to NAE agents that are used within their
network.

Considerations when writing an NAE agent

HPE Aruba Networking publishes agents which take the design recommendations covered in this
document into consideration, but NAE agents can be written by 3rd party developers and customers. As
a result, care should be taken when writing an NAE agent. Areas to consider include, and are not limited
to:

n The use of wildcards should be used sparingly in order to reduce the memory and storage used by

the agent.

n Alerts should not be triggered frequently in order to reduce the wear of the storage device.

n The thresholds on conditions shouldn’t trigger often in order to reduce the number of alerts and CPU

time needed to act on the conditions.

n Any outbound network connections can only access the default VRF.

AOS-CX Network Analytics Engine (NAE) Design considerations | 20

Aruba Network Analytics Engine

Chapter 4

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

21

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

Aruba Network Analytics Engine framework | 22

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

23

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

24

4. On the Analytics Dashboard, locate and close any time series graph panels for the default agent

from the previous software release.

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

Managing scripts | 25

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

26

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

Managing scripts | 27

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

28

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
Managingscripts|29

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

30

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

Managing scripts | 31

DELETE https://192.0.2.5/rest/v1/system/nae_scripts/com.myco.bgp_mon
| Downloading | a script | from the | switch | using the | REST API |
| ----------- | -------- | -------- | ------ | --------- | -------- |
InstructionsandexamplesinthisdocumentuseanIPaddressthatisreservedfordocumentation,
192.0.2.5,asanexampleoftheIPaddressfortheswitch.Toaccessyourswitch,youmustusetheIP
addressorhostnameofthatswitch.
Prerequisites
YoumustbeloggedintotheswitchRESTAPI.
Procedure
UsetheGETmethodontheURIofthescript.
Thisexampledownloadsscriptnamedcom.arubanetworks.mac_arp_count_monitor.
GET https://192.0.2.5/rest/v1/system/nae_scripts/com.arubanetworks.mac_arp_count_monitor
Thefollowingexampleistheresponsebodyfortherequest.Theentirescriptisreturnedinbase64
format.Becauseofthelengthofthescript,theexampleshowsonlypartofthescript.
{
| "author": "Aruba | Networks", |     |     |     |     |
| ---------------- | ---------- | --- | --- | --- | --- |
"description": "MAC address learned on VLAN ID and number of neighbors learned
using ARP",
| "expert_only":    | false, |     |     |     |     |
| ----------------- | ------ | --- | --- | --- | --- |
| "nae_parameters": | {      |     |     |     |     |
"Vlan_Id": "/rest/v1/system/nae_scripts/mac_arp_count_monitor/nae_
parameters/Vlan_Id"
},
| "name": "mac_arp_count_monitor", |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- |
| "origin": "user",                |     |     |     |     |     |
"script": "IyAtKi0gY29XBUCAgICpdGRvcih1cmky...LCAnQVJQIFRhYmxlIENvdW50JykK",
| "status": { |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- |
"state": "VALIDATED"
},
| "version": "1.0" |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
}
| show running-config |     | command | output | for agents | and |
| ------------------- | --- | ------- | ------ | ---------- | --- |
scripts
Built-inscriptsarenotincludedintheoutputoftheshow running-configcommand.
Abuilt-inagentisincludedintheoutputoftheshow running-configcommandonlyifoneormoreof
theagentparametershasbeenmodifiedandsaved.
User-createdscriptsandagentsareincludedintheoutputoftheshow running-configcommand.
Theoutputoftheshow running-configcommandincludesthefollowinginformationforscriptsand
agents:
n Thenameofthescript.
n Thevalueoftheexpert_onlyparameter.Typically,thisparameterhasavalueoffalse.
n Thescriptcodeinbase64format.
Thenameoftheagent.
n
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 32

n The value of the enabled parameter.

n The name of each agent parameter, followed by its value in base64 format.

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

Managing scripts | 33

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

34

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

Managing agents | 35

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

36

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

Managing agents | 37

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

38

5.

In the Alerts panel, select an alert and click Details to view the Alert Details dialog box. To close
the dialog box, click Close.

You can also access alert details directly from the Analytics Dashboard by selecting an alert in the
Alerts panel and clicking Details.

6. The Action Result(s) in Alert Details dialog box might include additional details about actions

and links to the action result output.

To view the Action Result Output dialog box for an action, click the Output link.

Managing agents | 39

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

40

n Customizing data displayed on the graph on page 41

n Zooming in on the graph on page 42

n Downloading the graph as animage or .csv file on page 43

n Viewing an alert on the graph on page 43

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

Managing agents | 41

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

42

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

Managing agents | 43

2. To adjust the graph display to show the metrics for the alert, do the following:

a. Locate the alert on the graph and click the alert triangle flag. The Alert Details dialog box is

displayed.

b. Click View on Graph.

3.

If the graph is showing eight metrics and the metric you want to display is the ninth metric, you
must choose an existing metric to clear so that the graph can show the metric associated with the
alert.

For example:

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

44

a. Clear the selection box for the metrics you no longer want to show.

For example:

b. Click View on Graph.

The graph is changed to show the metric associated with the alert.

For example:

Managing agents | 45

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
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 46

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

Managing agents | 47

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

48

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

Managing agents | 49

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

50

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

Managing agents | 51

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

52

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
Capacities Status Name
Value Maximum
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

Managing agents | 53

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

54

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

Managing agents | 55

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

56

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
n TousetheWebUI,ontheOverviewpage,lookattheAnalyticspaneltoseethetotalnumberof
scripts,agents,andmonitorscomparedtothetotalnumbersupportedontheswitch.
Forexample,Agents: 6/50indicatesthattherearetotalofsixenabledanddisabledagentsoutofa
maximumof50agentssupportedonthisswitch.
n TousetheRESTAPI,dothefollowing:
1. Togetinformationaboutmaximumnumberofscripts,agents,andmonitors,sendaGET
requesttothe/systemresource,specifyingtheattributes=capacitiesqueryparameter.For
example:
GET /rest/v1/system/?attributes=capacities
57
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries)

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

Troubleshooting agent and script issues | 58

"nae_scripts": 7,
...
...

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

59

Procedure

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

Troubleshooting agent and script issues | 60

n Instead of using Coordinated Universal Time (UTC) with a time zone offset or getting the time from an

NTP server, either the switch or the client is manually set to a different time.

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

61

n After the software update:

o The name of the new agent is based on the new script name. The new agent name is the

following:

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

Troubleshooting agent and script issues | 62

| switch# | clear nae-data |     |     |     |
| ------- | -------------- | --- | --- | --- |
n IftheswitchissettouseNTPandtherehasbeenasignificantclockchange,cleartheNAEdataby
| usingtheclear | nae-datacommand. |     |     |     |
| ------------- | ---------------- | --- | --- | --- |
Forexample:
| switch#  | clear nae-data |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Solution | 2              |     |     |     |
Cause
Theswitchoperatingsystemsoftwarewasupdatedtoadifferentsoftwarerelease.
Action
1. CleartheNAEdatabyenteringtheclear nae-datacommandfromthemanagercontext.
Forexample:
|     | switch# clear | nae-data |     |     |
| --- | ------------- | -------- | --- | --- |
2. Examinethealertsforagentorscripterrors.
Ensurethatthescriptsloadedontheswitchsupportthesoftwarereleaseinstalledontheswitch.
3. Ifascriptdoesnotsupportthecurrentsoftwarerelease,deletethescriptanduploadthe
replacementscript.
4. Afteryouuploadreplacementscripts,cleartheNAEdataagainbyenteringtheclear nae-data
commandfromthemanagercontext.
URI errors
Agentscanencountererrorsnotrelatedtoscriptsyntax.Forexample:
n Theagentattemptstomonitoraportthatexistsontheswitchbutisnotup.
n Theagentattemptstomonitoraportthatdoesnotexistonthisswitch.
n TheagentattemptstomonitoraLAGthathasnotbeenconfigured.
n Thespecifiedattributeisnotcorrectfortheresource.Forexample,thequerystringoftheresource
URIspecifiesnx_packetsinsteadofrx_packets.
LAGsandportsareexamplesofswitchresources.EveryswitchresourceisidentifiedbyaURI(Universal
ResourceIdentifier),sothekindsoferrorslistedpreviouslyareacategoryoferrorscalledURIerrors.
| Error:    | "The NAE | Agent | is not created...DB | constraint |
| --------- | -------- | ----- | ------------------- | ---------- |
| violation | errors"  |       |                     |            |
Symptom
Whenyouattempttocreateanagent,theagentappearsintheAgentspanelwitharedtriangleerror
symbolandstatusofUnknown.Theerrormessageisthefollowing:
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 63

The NAE Agent is not created. Please check hpe-policd logs for DB constraint violation
errors.

Cause

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

Troubleshooting agent and script issues | 64

| Error:  | "Timeseries |             | data | cannot | be generated...The | URI is |
| ------- | ----------- | ----------- | ---- | ------ | ------------------ | ------ |
| invalid | or not      | configured" |      |        |                    |        |
Symptom
Anagentisinanerrorstateandisnotcollectingdataforoneofitsmonitoredresources.
TheAgentErrormessageisthefollowing:
| Timeseries    | data cannot       | be     | generated     | due to       |        |     |
| ------------- | ----------------- | ------ | ------------- | ------------ | ------ | --- |
| the following | agent             | error: | The URI       | is invalid   | or not |     |
| configured.   | Either            | please | upload        | a new script | with a |     |
| valid         | URI, or configure |        | the resource, | disable      | the    |     |
| instance,     | and enable        | again: | <uri>         |              |        |     |
Inthemessage,<uri>istheresourcethatisinvalidornotconfigured.Forexample:
/rest/v1/system/bridge/vlans/*/macs?count
| Solution | 1   |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
Cause
IftheresourceURIissupportedonthisswitchandoperatingsystemversion,themostlikelyreasonfor
theerroristhattheswitchresource—suchasaport—isnotinanUPstate.
Action
1. Resolvetheproblemthatiscausingtheresourcetobeunavailable.
Forexample,ifaportisadministrativelydown,bringtheporttoanUPstate.
2. Disabletheagent.
3. Enabletheagent.
| Solution | 2   |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
Cause
TheagentusesaresourceIDfromauser-suppliedparameter,andtheusersuppliedaresourceIDthat
isinvalid(suchasaportthatdoesnotexist).
Action
1. Deletetheagent.
2. CreateandenableanagentthatspecifiesavalidresourceID(suchasportnumber).
| Solution | 3   |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
Cause
TheresourceURIisnotauser-suppliedparameter,andisnotsupportedonthisswitchandsoftware
version.
Forexample,aURIthatincludes/bridgeinthepathisnotvalidon10.03andlaterversions.
Action
IfthescriptwasdownloadedfromtheArubaSolutionsExchange(ASE),replaceorupdatethescript
n
withascriptthatsupportsthesoftwareversionrunningontheswitch.
1. Ifthescriptwasloadedonaswitchrunningversion10.03orlaterandthescriptnamematches
thenewscriptname,youcanusetheupdateprocesstoreplacethescript.
2. Ifthescriptwasloadedwhiletheswitchwasrunningaversionearlierthan10.03,youmust
deletetheexistingscript,uploadthenewscript,andcreatenewagents.
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 65

n IfthescriptnotascriptdownloadedfromtheASE,dothefollowing:
| 1.  | Deleteallagentsassociatedwiththescript. |     |     |     |     |
| --- | --------------------------------------- | --- | --- | --- | --- |
Considerrecordinginformationabouttheagentnamesandparametervaluessothatyoucan
createequivalentagentsfromthemodifiedscript.
2. ModifythescripttospecifyonlyURIsthatarevalidforthisswitchandoperatingsystem
version.
| 3.     | Replacethescriptontheswitchwiththemodifiedscript. |        |             |     |     |
| ------ | ------------------------------------------------- | ------ | ----------- | --- | --- |
| 4.     | Createagentsfromthemodifiedscript.                |        |             |     |     |
| 5.     | Enablethenewagents.                               |        |             |     |     |
| Error: | "The script                                       | syntax | is invalid" |     |     |
Symptom
| Scriptvalidationfailswiththeerror:The |     |     | script syntax | is invalid |     |
| ------------------------------------- | --- | --- | ------------- | ---------- | --- |
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
Troubleshootingagentandscriptissues|66

Cause
Theswitchisoperatingunderaheavyload.
Action
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
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 67

|        | b. Modifythescript.                                  |          |           |                |
| ------ | ---------------------------------------------------- | -------- | --------- | -------------- |
|        | c. Replacethescriptontheswitchwiththemodifiedscript. |          |           |                |
|        | d. Createagentsfromthemodifiedscript.                |          |           |                |
|        | e. Enablethenewagents.                               |          |           |                |
| Error: | "Unable                                              | to parse | condition | expression..." |
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
| o Correctsyntax:r.condition('{}  |     |     | > {}', [value,threshold])  |     |
| -------------------------------- | --- | --- | -------------------------- | --- |
| o Incorrectsyntax:r.condition('> |     |     | {} {}', [value,threshold]) |     |
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
Troubleshootingagentandscriptissues|68

1. Modifythescripttocorrecttheconditionexpression:
|     | a. Deleteallagentsassociatedwiththescript. |     |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- |
Considerrecordinginformationabouttheagentnamesandparametervaluessothatyou
cancreateequivalentagentsfromthemodifiedscript.
|        | b. Modifythescript.                                  |     |         |     |             |     |
| ------ | ---------------------------------------------------- | --- | ------- | --- | ----------- | --- |
|        | c. Replacethescriptontheswitchwiththemodifiedscript. |     |         |     |             |     |
|        | d. Createagentsfromthemodifiedscript.                |     |         |     |             |     |
|        | e. Enablethenewagents.                               |     |         |     |             |     |
| Error: | "The                                                 | CLI | command |     | is invalid" |     |
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
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 69

| Cannot | execute command. | Command not | allowed. |     |     |
| ------ | ---------------- | ----------- | -------- | --- | --- |
Theswitchisconfiguredtousearemoteauthenticationandauthorizationservice,suchasTACACS+.
n
Cause
NetworkAnalyticsEngine(NAE)scriptsexecuteCLIcommandsastheadminuser,anddonotattemptto
authenticatebeforeexecutingtheCLIcommand.Theremoteauthenticationandauthorizationservice
isnotallowingtheadminusertoexecutecommandswithoutpriorauthentication.
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
Troubleshootingagentandscriptissues|70

The switch is configured in enhanced secure mode.

Action

Do one of the following:

n Ignore the error. The enhanced secure mode of the switch denies access to shell commands by

design.

n Change the configuration of the switch from enhanced secure mode to standard mode. For more

information about enhanced secure mode, see the Security Guide.

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

71

Using the HPE Aruba Networking

Chapter 8

Using the HPE Aruba Networking Solutions Exchange Solutions Exchange

Finding NAE scripts on the ASE website

No login is required to browse the website or view information about a script. To download a script or to
view the source code from the website, you must be logged in. Alternatively, you can download scripts
from the Web UI without logging in to the HPE Aruba Networking Solutions Exchange.

Prerequisites

You must have access to the HPE Aruba Networking Solutions Exchange website at:

https://ase.arubanetworks.com/

Procedure

1. On the top toolbar, select SOLUTIONS.

2.

In the navigation pane, under PRODUCTS, select NAE.

3. To filter the list by additional criteria, select one or more tags under TAGS. For example:

n To view HPE Aruba Networking Solutions Exchange certified NAE solutions, select the tag: nae-

aruba-certified

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
download scripts from the HPE Aruba Networking Solution Exchange. From the Web UI, only
Aruba-certified scripts are listed. For other scripts, go to the HPE Aruba Networking Solution
Exchange directly.

download button to view and

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

72

YoucanalsoaccesstheHPEArubaNetworkingSolutionExchangefromtheScriptManagement
| pagewhereyouselectthe |     | button. |     |     |     |     |
| --------------------- | --- | ------- | --- | --- | --- | --- |
3. TheHPEArubaNetworkingSolutionExchangepageisdisplayed,listingtheavailablescripts.You
canselectascriptandclickView Scripttoseetheprogrammaticscriptcontents.
| Viewing | recent | changes | to existing | NAE solutions |     |     |
| ------- | ------ | ------- | ----------- | ------------- | --- | --- |
Nologinisrequiredtobrowsethewebsiteorviewinformationaboutascript.Todownloadascriptor
toviewthesourcecodefromthewebsite,youmustbeloggedin.Alternatively,youcandownload
scriptsfromtheWebUIwithoutloggingintotheHPEArubaNetworkingSolutionsExchange.
Prerequisites
YoumusthaveaccesstotheHPEArubaNetworkingSolutionsExchangewebsiteat:
https://ase.arubanetworks.com/
Procedure
1. Selectthesolution.
2. Onthesolutiondetailspage,viewtherecentchangesintheRecent Changesbox.Youcanview
| additionalchangeinformationbyclickingMore |     |               | Details. |          |           |     |
| ----------------------------------------- | --- | ------------- | -------- | -------- | --------- | --- |
| Downloading                               |     | or installing | a script | from the | ASE using | the |
Web UI
ThisproceduredownloadsanNAEscriptfromtheASEtothespecifiedlocation.
UsingtheHPEArubaNetworkingSolutionsExchangeSolutionsExchange |73

Prerequisites

You must be logged in to the AOS-CX Web UI. Administrator rights are required to install a script, but not
required to download a script to your local system.

Procedure

1. Select Analytics from the navigation pane.

2.

In the Analytics Dashboard, in the Scripts panel, click the
download scripts from the HPE Aruba Networking Solution Exchange. You can also access the
HPE Aruba Networking Solution Exchange from the Script Management page where you select
the

ASE download button to view and

button.

3. The HPE Aruba Networking Solution Exchange page is displayed, listing the available scripts.

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

You must be logged in to the HPE Aruba Networking Solution Exchange.

Procedure

1. On the HPE Aruba Networking Solutions Exchange, search or browse for the solution you want to

use.

2.

In the DETAILS column, click the title of the solution.

The detailed information about the solution is displayed.

3. Verify that the displayed solution is the solution you want to download.

The Description shows information about the solution, including software required and
platforms supported.

4. Click Finish.

5.

In the dialog box, select CONFIG.

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

74

6. Do one of the following:

n To download the solution, click Download.

n To receive the solution as an email attachment, click Email Me.

The email is sent to the email address associated with the account you used to log in to the ASE.

n To send the solution to as an attachment to an email address other than the email address

associated with the account you used to log in to the HPE Aruba Networking Solution
Exchange, enter the email address in the Email address text box and click Forward.

7. Click Close.

Using the HPE Aruba Networking Solutions Exchange Solutions Exchange | 75

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

76

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

77

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

78

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

Scripts | 79

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

80

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

Scripts | 81

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

82

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

Scripts | 83

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
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 84

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

Scripts | 85

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

Alert Description API

The NAE python framework provides an API for initializing , setting, and clearing the alert description for
the alert information of the agent. This field is used to store any information regarding why the agent or
its sub-agents are in their respective alert levels. The API only stores the details of the most recent alert
level state change, rather than maintaining anextensive history. Scripts with sub-agents will not receive
updates to the alert description on a per sub-agent level unless the overall agent alert level changes.

API to initialize the alert description:

self.init_alert_description({"(sub)agent name": "Normal"})

API to set the entire alert description:

self.set_alert_description("Description String")

API to set a specified sub-agent alert description:

self.set_alert_description_for_key("(sub)agent name", "Description String")

API to clear a specified (sub)agent alert description:

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

86

self.clear_alert_description_for_key("(sub)agent name", "Normal")
Parameter definitions
TheParameterDefinitionsstatementdefinestheparametersthatareusedinthescript.
Whenausercreatesanagent,theusercanspecifyvaluesfortheparameters.Theusermustspecify
valuesforparametersthatthescriptidentifiesasrequiredparameters.
Whenyouwriteascript,HewlettPackardEnterpriserecommendsthatyoucreateparametersforany
user-configurableoptioninthescript.
Ifthescripthasnoparameters,omittheParameterDefinitionsstatement.
ThefollowingexampleofaParameterDefinitionsstatementdefinesthefollowingparameters:
threshold
Thethresholdparameterisanintegerandhasadefaultvalue90.
password
Thepasswordparameterisastring.Theparameterisoptional.Iftheusersuppliesavalue,theuser-
suppliedtextisencryptedwhenthetextisstored.
ParameterDefinitions = {
| 'threshold': {    |     |                    |              |     |     |
| ----------------- | --- | ------------------ | ------------ | --- | --- |
| 'Name': 'Critical | CPU | Threshold value in | percentage', |     |     |
'Description': ('When System CPU utilization exceeds this value, '
|     | 'set the | policy status | to Critical and | the policy | will log |
| --- | -------- | ------------- | --------------- | ---------- | -------- |
'
|     | 'system | daemon CPU utilization | details | and CPU | queue |
| --- | ------- | ---------------------- | ------- | ------- | ----- |
statistics in syslog.'),
| 'Type': 'integer', |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- |
| 'Default': 90      |     |     |     |     |     |
}
| 'password': {       |           |            |     |     |     |
| ------------------- | --------- | ---------- | --- | --- | --- |
| 'Name': 'Password', |           |            |     |     |     |
| 'Description':      | ' Service | Password', |     |     |     |
| 'Type': 'string',   |           |            |     |     |     |
| 'Encrypted':        | True,     |            |     |     |     |
| 'Required':         | False     |            |     |     |     |
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
| 'Description': | '<description>' |     |     |     |     |
| -------------- | --------------- | --- | --- | --- | --- |
'Type': '<datatype>',
'Default': <default_value>,
Scripts|87

'Encrypted': '<True_or_False>'
'Required': '<True_or_False>'

}

}

Components

Each parameter definition must contain the following:

The parameter declaration

Specifies a unique name for parameter. This name must be unique within the script. The name is a
text string that can contain alphanumeric characters, - (hyphen), and _ (underscore). Example:
threshold

Name

The name of the parameter. This name is displayed in the user interfaces.

Description

Describes the parameter. This description is displayed to users in the Create Agent screen of the
Web UI.

Type

Specifies the datatype of parameter. Parameter type is one of the following values:

n integer

n string

Default

Specifies the default value of the parameter. At the time the agent is created, the default value is
assigned to the parameter unless the user specifies a different value. You must specify a default if
the parameter is part of a monitor or a condition. Otherwise, providing a default value is optional.

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

88

Description
Themainbodyofthescriptistheagentclassconstructor.Theagentclassconstructorcancontain:
n Monitors
n Conditions
n Rules
Actions
n
n AgentfunctionssuchasGraph,on_parameter_change,andBaseline.
n AnalyticsDataCollections(ADCs)
Example
Exampleofanagentclassconstructor:
class Agent(NAE):
def __init__(self):
uri1 = '/rest/v1/system/subsystems/*/*/power_supplies/*?attributes=status'
| self.m1 | = Monitor(uri1, |     | name='System      |     | CPU | utilization') |
| ------- | --------------- | --- | ----------------- | --- | --- | ------------- |
| self.r1 | = Rule('High    |     | CPU utilization') |     |     |               |
self.r1.condition('{} > {}', [self.m1, self.params['threshold']])
self.r1.action(self.action_high_cpu)
| self.r1.action("CLI","top  |     |     | cpu")   |       |     |     |
| -------------------------- | --- | --- | ------- | ----- | --- | --- |
| self.r1.action("SHELL","ps |     |     |         | -ef") |     |     |
| def action_high_cpu(self,  |     |     | event): |       |     |     |
self.set_alert_level(AlertLevel.CRITICAL)
|     | #   | CPU value | when | the | Condition | met |
| --- | --- | --------- | ---- | --- | --------- | --- |
cpu = event["value"]
| ActionSyslog("CPU |                 | Utilization |     | at %s%." | %   | cpu) |
| ----------------- | --------------- | ----------- | --- | -------- | --- | ---- |
|                   | ActionCLI("top  |             |     | cpu")    |     |      |
|                   | ActionShell("ps |             |     | -ef")    |     |      |
Graph
Syntax
Graph(<monitor-set>[, title=<title>][, dashboard_display=True])
Description
TheGraphfunctionenablesyoutoselectamonitororgroupofmonitorstodisplaytogetherinagraph
ontheAgentDetailspageintheWebUI.
Parameters
<monitor-set>
Specifiesacomma-separatedlistofmonitorstobeincludedinthisgraph.Thelistmustbeenclosed
inbrackets([]),whichdefinealistinPython.Thelistmustincludeatleastonemonitor.
Examples:
[self.monitor1]
n
| [self.m1, self.m2, | self.m3] |     |     |     |     |     |
| ------------------ | -------- | --- | --- | --- | --- | --- |
n
<title>
Specifiesthetitletobedisplayedforthisgraph.Thedefinitionof<title>mustusetheTitle
function.
| Forexample:title=Title("My |     |     | graph | title") |     |     |
| -------------------------- | --- | --- | ----- | ------- | --- | --- |
Scripts|89

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

In the following example, graph g1 includes data from monitors m1 and m2. The graph does not have a
custom title and is not the graph that represents the agent in the Analytics Dashboard.
self.g1 = Graph([self.m1, self.m2])

In the following example, graph g2 includes data from monitor m1. The graph has a custom title, but it is
not the graph that represents the agent in the Analytics Dashboard.
title = Title("CPU utilisation by {} daemon ", [self.params["daemon_name"]])
self.g2 = Graph([self.m1], title=title)

In the following example, graph g2 includes data from monitor m1. The graph has a custom title and it is
the graph that represents the agent in the Analytics Dashboard.
title = Title("CPU utilisation by hpe-policyd daemon")
self.g2 = Graph([self.m1], title=title, dashboard_display=True)

Title

Syntax

Title("<title-string>"[, <params>])

Description

Creates a text string to be used as a custom title for a graph or for a predefined action.

Parameters

<title-string>

Specifies the python string to be used for the title. The string can contain parameters. To specify that
a parameter is expected, use the following characters:

{}

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

90

For example: "Print interface {} details"

<params>

Optional. Contains the parameters to be used in the title string. If multiple parameters are used, they
must be passed to the function in the order they are required by the title string.

Usage

The Aruba Network Analytics Engine provides the Title function to enable you to specify custom titles
when defining multiple graphs, or to show specific information about an action being performed by an
agent. For example, if you define a title for each CLI action in a script, a user can see which action is
being performed by looking at the Alert Details page in the Web UI.

Examples

The following example defines a title that is used for a graph. The title string includes a parameter.
title = Title("CPU utilisation by {} daemon ", [self.params["daemon_name"]])
self.g1 = Graph([self.m1], title=title)

The following example defines a title that is used for a CLI action. The title string does not include a
parameter.
title = Title("Show switch configuration")
self.r.action("CLI","show running-config ", title=title)

on_agent_re_enable

Syntax

on_agent_re_enable(<agent>, <event>)

Description

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

Scripts | 91

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

on_parameter_change

Syntax

on_parameter_change(<agent>, <params>)

Description

Performs the specified actions when a user changes the value of an agent parameter.

Parameters

<agent>

Specifies the agent that has the changed parameters.

Typically, this parameter is defined as the variable: self

<params>

Specifies a Python dictionary that contains the name of the changed parameter, the old value, and
the new value.

Usage

Parameters that are defined in the ParameterDefinitions of a script can be changed by a user after the
user creates the agent.

The Aruba Network Analytics Engine provides the on_parameter_change function to enable you to
specify actions the agent is to perform when the user changes the value of one or more parameters.

Example

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

92

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
n Onadifferentswitchonadifferentnetwork,thatsameincomingtrafficratemightbeconsidered
abnormallyhigh,andthenetworkadminwouldwantanalerttobegeneratedinthose
circumstances.
n Ifthescriptwriterchoosesathresholdbasedonthelowerincomingtrafficrate,theagent
monitoringthehigh-trafficswitchwilleithergeneratenumerousalertsorwillremaininanalertstate
formostofthetime.Becausethethresholdislowerthanatrafficratethatisconsiderednormalfor
thatswitch,thealertsgeneratedbecauseofthelowerthresholdsareconsidered"falsepositives"by
thenetworkadministrator.
TheBaselinefunctionprovidesawaytospecifythresholdsthatareappropriatetothenetwork
conditionsontheswitch.Whenanagentiscreatedandenabled,itspendsaspecifiedamountoftime
"learning"aboutthedataitismonitoringbeforeitsetsthresholdsthatarecalculatedbasedonwhatit
learned.
Inaddition,thesethresholdsaredynamic.Theagentcontinuestolearnaboutthedataitmonitorsand
theBaselinefunctionadjuststhethresholdsaccordingly.Forexample,ifthelower-trafficswitchstarts
togetconsistentlyhigherincomingtrafficrates,theBaselinefunctionadjuststhethresholdstoreflect
thenewlylearnedrates.
Ifdesired,thescriptwritercanspecifydefaultthresholdsthatcanbeusedtodeterminewhentoset
andclearalertswhiletheagentinalearningstate.Otherwisetheagentdoesnotgeneratealertswhileit
learningaboutthedata.
Themethodsusedtodeterminethebaselinefromwhichtocalculatethethresholds—bothduringthe
initiallearningstateandovertime—dependonthealgorithmselectedintheBaselinefunction.
| Baseline | workflow | and considerations |     |     |
| -------- | -------- | ------------------ | --- | --- |
ThefollowingdiagramshowsasummaryoftheworkflowofaBaselinefunctionthatuses
MaxAlgorithminitsthresholdcalculations:
Scripts|93

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

94

Example of baselines in a time series graph

The following is an example the time series graph for a monitor that includes baselines:

n The initial learning time is one minute.

n There are no default thresholds.

In this graph:

n The green line is the raw data.

n The orange line is the high threshold as calculated by the baseline.

n The blue line is the low threshold as calculated by the baseline.

The events in the timeline are as follows:

1. At 20:32:30, an agent is created and enabled. The baseline enters the learning state. Because the
script did not specify default thresholds, there are no thresholds defined. In the graph, just the
green line for the raw data is displayed.

2. At 20:33:30, the baseline exits the learning state and enters the active state:
n The high threshold and the low threshold calculations are completed.

n The graph begins the display of the orange line for the high threshold and the blue line for the

low threshold.

n The agent will generate an alert when the monitored traffic rate (in packets per second)

exceeds the high threshold.

n The agent will clear the alert when the monitored traffic rate (in packets per second) drops

below the low threshold.

3. At 20:37:33, an alert is triggered because the monitored traffic rate exceeds the high threshold.

4. At 20:39:15, the alert is cleared because the monitored traffic rate (in packets per second) is lower

than the low threshold.

5. At 20:40:30, the thresholds are updated.

In this case, the thresholds are set significantly higher because the algorithm includes all the data in its
continuous learning window, which included the time in which the traffic rate was much higher than
the previous threshold.

Scripts | 95

Ifthescriptspecifiedalongerinitiallearningtime,suchasoneday,thecalculationsusedtocreatethe
thresholdscanincludethetypicalfluctuationsindatathatcanoccur,resultinginmoreappropriate
thresholdsandalertsthattriggeronlyforsignificantanomalies.
| Example | of a script |     | that uses |     | baselines |     |     |     |
| ------- | ----------- | --- | --------- | --- | --------- | --- | --- | --- |
Thefollowingisanexampleofascriptthatincludesmultiplemonitorsandbaselines:
| Manifest | = {                                     |     |     |     |     |     |     |     |
| -------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| 'Name':  | 'single_interface_tx_rx_stats_monitor', |     |     |     |     |     |     |     |
'Description': 'Policy to monitor tx/rx packets stats of a interface',
| 'Version': |        | '2.0', |           |     |     |     |     |     |
| ---------- | ------ | ------ | --------- | --- | --- | --- | --- | --- |
| 'Author':  | 'Aruba |        | Networks' |     |     |     |     |     |
}
| ParameterDefinitions |                |            | = {        |      |       |             |     |     |
| -------------------- | -------------- | ---------- | ---------- | ---- | ----- | ----------- | --- | --- |
| 'interface_id':      |                |            | {          |      |       |             |     |     |
|                      | 'Name':        | 'Interface |            | Id', |       |             |     |     |
|                      | 'Description': |            | 'Interface |      | to be | monitored', |     |     |
|                      | 'Type':        | 'string',  |            |      |       |             |     |     |
|                      | 'Default':     | '1/1/1'    |            |      |       |             |     |     |
}
}
class Agent(NAE):
| def | __init__(self): |                                                  |             |     |           |             |     |     |
| --- | --------------- | ------------------------------------------------ | ----------- | --- | --------- | ----------- | --- | --- |
|     | # algorithm     |                                                  | for dynamic |     | Threshold | calculation |     |     |
|     | self.alg        | = MaxAlgorithm(continuous_learning_window="10m") |             |     |           |             |     |     |
# rx packets
uri1 = '/rest/v1/system/interfaces/{}?attributes=statistics.rx_packets'
rate_m1 = Rate(uri1, "10 seconds", [self.params['interface_id']])
|     | self.m1 | = Monitor( |     |     |     |     |     |     |
| --- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
rate_m1,
|     | 'Rx     | Packets           | (packets |     | per second)') |           |     |              |
| --- | ------- | ----------------- | -------- | --- | ------------- | --------- | --- | ------------ |
|     | self.r1 | = Rule('Rule      |          | for | Monitor       | Interface |     | rx Packets') |
|     | title1  | = Title("Baseline |          |     | for Interface |           | rx  | Packets")    |
self.baseline1 = Baseline(self.m1, algorithm=self.alg, title=title1,
high_threshold_factor=2,
low_threshold_factor=1.2,
initial_learning_time='1d')
|     | self.r1.condition('{}               |     |         | >   | {}', [self.m1, |                      | self.baseline1]) |                  |
| --- | ----------------------------------- | --- | ------- | --- | -------------- | -------------------- | ---------------- | ---------------- |
|     | self.r1.clear_condition('{}         |     |         |     | <              | {}', [self.m1,       |                  | self.baseline1]) |
|     | self.r1.action("ALERT_LEVEL",       |     |         |     |                | AlertLevel.CRITICAL) |                  |                  |
|     | self.r1.clear_action("ALERT_LEVEL", |     |         |     |                |                      | AlertLevel.NONE) |                  |
|     | # rx packets                        |     | dropped |     |                |                      |                  |                  |
uri2 = '/rest/v1/system/interfaces/{}?attributes=statistics.rx_dropped'
|     | self.m2 | = Monitor( |     |     |     |     |     |     |
| --- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
uri2,
|     | 'Rx | Packets | Dropped |     | (packets)', |     |     |     |
| --- | --- | ------- | ------- | --- | ----------- | --- | --- | --- |
[self.params['interface_id']])
# tx packets
uri3 = '/rest/v1/system/interfaces/{}?attributes=statistics.tx_packets'
rate_m3 = Rate(uri3, "10 seconds", [self.params['interface_id']])
|     | self.m3 | = Monitor( |     |     |     |     |     |     |
| --- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
rate_m3,
|     | 'Tx     | Packets           | (packets |     | per second)') |           |     |              |
| --- | ------- | ----------------- | -------- | --- | ------------- | --------- | --- | ------------ |
|     | self.r3 | = Rule('Rule      |          | for | Monitor       | Interface |     | tx Packets') |
|     | title3  | = Title("Baseline |          |     | for Interface |           | tx  | Packets")    |
self.baseline3 = Baseline(self.m3, algorithm=self.alg, title=title3,
high_threshold_factor=2,
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 96

low_threshold_factor=1.2,
initial_learning_time='1d')

self.r3.condition('{} > {}', [self.m3, self.baseline3])
self.r3.clear_condition('{} < {}', [self.m3, self.baseline3])
self.r3.action("ALERT_LEVEL", AlertLevel.CRITICAL)
self.r3.clear_action("ALERT_LEVEL", AlertLevel.NONE)

# tx packets dropped
uri4 = '/rest/v1/system/interfaces/{}?attributes=statistics.tx_dropped'
self.m4 = Monitor(

uri4,
'Tx Packets Dropped (packets)',
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

The Baseline function calculates and sets low and high thresholds for a monitor based on data
gathered during a learning period after an agent is enabled or restarted.

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

Scripts | 97

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
agent stays in the initial learning state for five minutes. If there is no data available, the baseline stays
in the initial learning state for one hour.

During the initial learning state, the baseline function looks at the monitored data and uses its
algorithm to determine normal patterns versus anomalies. Unless you specify values for the
default_thresholds parameter, the agent does not generate alerts during the initial learning state.

Ensure that the initial learning time is long enough to gather enough data to determine normal
versus abnormal patterns.

For example:

n If you are monitoring something that is updated infrequently, a longer initial learning time might be

required to obtain enough data.

n If an agent is monitoring network traffic and that agent is enabled during a time that has unusually
low traffic, the baseline calculates a low value, and "normal" traffic levels exceed the threshold,
creating an alert. By setting a longer duration for the initial learning period, you maximize the ability
of the algorithm to make calculations based on typical conditions.

The format for <duration> is <number><unit>, where <unit> is one of the following:

Value

s

m

h

d

w

Meaning

seconds

minutes

hours

days

weeks

Default: 1h
<lthresh> and <hthresh>

Specifies the default low and default high thresholds. These thresholds are used while the baseline is
in the initial learning state. Both thresholds must be specified.

If default thresholds are not specified, alerts are not triggered for the monitor while the baseline is in
the learning state.

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

98

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
| Value |     |     |     |     |     | Meaning |     |
| ----- | --- | --- | --- | --- | --- | ------- | --- |
| s     |     |     |     |     |     | seconds |     |
| m     |     |     |     |     |     | minutes |     |
| h     |     |     |     |     |     | hours   |     |
| d     |     |     |     |     |     | days    |     |
| w     |     |     |     |     |     | weeks   |     |
Scripts|99

Example

# algorithm for dynamic Threshold calculation
self.alg = MaxAlgorithm(continuous_learning_window="2h")

How the MaxAlgorithm function works

The MaxAlgorithm function uses smoothed data over time to find the maximum value and calculate a
baseline of "typical" data. By setting a high threshold based on this calculation, the number of false
positives can be reduced. The agent generates alerts for extreme anomalies only.

The MaxAlgorithm function is best for data that has no limit on its maximum value, such as incoming
network traffic.

Smoothing data

The MaxAlgorithm function uses the "simple moving average" algorithm to smooth data.

In general, data smoothing is the process of detecting and removing "noise" data, allowing important
patterns to remain.

In its formula, the simple moving average algorithm reduces the influence of datapoints that are not
similar to the others because it includes multiple datapoints in the calculation. In addition, at each
subsequent measurement point, the new data point is added and the oldest data point is removed, so
short-term anomalies are eventually removed from the calculation.

For example, consider a simple moving average that is calculated based on five datapoints. If incoming
traffic rates—measured in packets per second at regular intervals—are 10, 11, 100, 4 and 5:

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

100

YoucancreateADCsandviewADCinformationthroughNAEscriptsonly.Multipleagentscanusethe
sameADC.
ADCsareoneoftwotypes:IPv4andIPv6.TherecanbemultipleADCsofeachtype.
ADCsaresimilartoACLsinthefollowingways:
n ADCsandACLsareinstalledintheswitchhardwareASICandshareunderlyingmechanismsand
limitations,includingusingTCAMentries.
n ADCsandACLsaredefinedinswitchconfigurationdatabaseinsimilarways.
AnADCiscomposedofoneormoreADCentriesorderedandprioritizedbysequencenumbers.The
lowestsequencenumberisthehighestprioritizedADCentry.TheADCprocessesapacketsequentially
againstentriesinthelistuntileitherthepacketmatchesanADCentryorthelastADCentryinthelist
hasbeenevaluated.
Notes:
n WhentheagentinstantiatedfromthescriptthatdefinestheADCisdisabledordeleted,theNAE
deletestheADC.DisablingordeletingtheagentistheonlymethodtodeletetheADC.
n Iftheswitchisconfiguredtocreateanautomaticcheckpoint(usingthecheckpoint auto <time>
command),theNAEdoesnotcreatetheADC.
n TheADCListclassincludesmethodstoaddentriesandtogetentries.Afteranentryisadded,it
cannotbemodifiedordeleted.
ThefollowingisanexampleofascriptthatdefinesanADClistandentries:
| Manifest       | = {                         |           |            |              |             |     |     |
| -------------- | --------------------------- | --------- | ---------- | ------------ | ----------- | --- | --- |
| 'Name':        | 'adc_hit_counters_monitor', |           |            |              |             |     |     |
| 'Description': |                             | 'Network  | Analytics  | Agent Script | to monitor' |     |     |
|                |                             | 'ADC hit  | counters', |              |             |     |     |
| 'Version':     | '1.0',                      |           |            |              |             |     |     |
| 'Author':      | 'Aruba                      | Networks' |            |              |             |     |     |
}
| ParameterDefinitions       |                | = {                        |          |                |              |         |             |
| -------------------------- | -------------- | -------------------------- | -------- | -------------- | ------------ | ------- | ----------- |
| 'office365_traffic_bound': |                |                            | {        |                |              |         |             |
|                            | 'Name':        | 'office365_traffic_bound', |          |                |              |         |             |
|                            | 'Description': | 'Traffic                   | flow     | to/from Office | 365, '       |         |             |
|                            |                | 'paramater                 | options: | \'to\'         | or \'from\', | default | is \'to\'', |
|                            | 'Type':        | 'String',                  |          |                |              |         |             |
|                            | 'Default':     | 'to'                       |          |                |              |         |             |
}
}
# IPv4Addresses contains a large list of IP addresses. For readability,
| # a small | sample | of addresses | is shown | in this | example. |     |     |
| --------- | ------ | ------------ | -------- | ------- | -------- | --- | --- |
IPv4Addresses = ["13.65.240.22/255.255.255.255", "13.66.58.59/255.255.255.255",
"13.70.156.206/255.255.255.255",
"13.71.145.114/255.255.255.255", "13.71.145.122/255.255.255.255",
"13.71.151.88/255.255.255.255",
"191.237.218.239/255.255.255.255",
"207.46.134.255/255.255.255.255",
"207.46.153.155/255.255.255.255"]
class Agent(NAE):
| def | __init__(self):                                |     |     |     |          |     |     |
| --- | ---------------------------------------------- | --- | --- | --- | -------- | --- | --- |
|     | if str(self.params['office365_traffic_bound']) |     |     |     | == 'to': |     |     |
Scripts|101

self.adc_outgress = ADCList("office365_outgress", ADCList.Type.IPV4,
"Traffic from Office365")
| for i in range(0,                                              | len(IPv4Addresses)): |         |     |        |     |
| -------------------------------------------------------------- | -------------------- | ------- | --- | ------ | --- |
| entry = ADCEntry(ADCEntry.Type.MATCH).dst_ip(IPv4Addresses[i]) |                      |         |     |        |     |
| self.adc_outgress.add_entry(i,                                 |                      |         |     | entry) |     |
| ipv4_outgress_traffic                                          |                      | = Rate( |     |        |     |
"/rest/v1/system/adc_lists/office365_
outgress/ipv4?attributes=statistics.*", "15s")
| ipv4_outgress_sum                                | =   | Sum(ipv4_outgress_traffic) |          |                |     |
| ------------------------------------------------ | --- | -------------------------- | -------- | -------------- | --- |
| self.ipv4_outgress_monitor                       |     | =                          | Monitor( |                |     |
| ipv4_outgress_sum,                               |     | "Ipv4                      | Traffic  | to Office365") |     |
| elif str(self.params['office365_traffic_bound']) |     |                            |          | == 'from':     |     |
self.adc_ingress = ADCList("office365_ingress", ADCList.Type.IPV4,
"Traffic to Office365")
| for i in range(0,                                              | len(IPv4Addresses)): |         |     |        |     |
| -------------------------------------------------------------- | -------------------- | ------- | --- | ------ | --- |
| entry = ADCEntry(ADCEntry.Type.MATCH).src_ip(IPv4Addresses[i]) |                      |         |     |        |     |
| self.adc_ingress.add_entry(i,                                  |                      |         |     | entry) |     |
| ipv4_ingress_traffic                                           |                      | = Rate( |     |        |     |
"/rest/v1/system/adc_lists/office365_
ingress/ipv4?attributes=statistics.*", "15s")
| ipv4_ingress_sum          | = Sum(ipv4_ingress_traffic) |       |          |                  |     |
| ------------------------- | --------------------------- | ----- | -------- | ---------------- | --- |
| self.ipv4_ingress_monitor |                             | =     | Monitor( |                  |     |
| ipv4_ingress_sum,         |                             | "Ipv4 | Traffic  | from Office365") |     |
else:
| raise Exception("Invalid |         | Parameters, |       | "              |                 |
| ------------------------ | ------- | ----------- | ----- | -------------- | --------------- |
|                          | "please | create      | agent | with parameter | 'to' or 'from', |
default: \'to\'")
ADCList class
Syntax
| ADCList("<name>", <type>[, "<description>") |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- |
Description
PythonclassforanAnalyticsDataCollections(ADC)list.CreatesandreturnstheADClist.
Parameters
<name>
Specifiesthenameofthelist.Theformatof<name>isaPythontextstring.
<type>
SpecifiesthetypeofADC.
Validvaluesarethefollowing:
n ADCList.Type.IPV4
n ADCList.Type.IPV6
<description>
DescriptionoftheADClist.Theformatof<description>isaPythontextstring.
Methods
add_entry(<seq>, <adc_entry>)
AddstheADCentryobject<adc_entry>totheADClistatsequencenumber<seq>.
ThesequencenumberisapositiveintegerthatisuniquewithintheADClist.Ifthesequencenumber
existsintheADClist,anagenterrorisgenerated.Range:0through4294967295
Example:
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 102

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

Scripts | 103

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

104

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

n If the URI includes a parameter, the name of the parameter.

n The name of the monitor, which is a string that is unique among the monitors defined in that script.

In the example, the name of the monitor is: Interface Received Bytes.

The following is an example of a monitor that uses a parameter for the resource ID. The monitor,
named Interface Received Bytes, records the received bytes of the interface that will be specified by
the user when the agent is created.
self.monitor = Monitor('/rest/v1/system/interfaces/{}?attributes=rx_bytes',

[self.params['iface_id'] ],name='Interface Received Bytes')

The following is an example of the same monitor except that it does not use a parameter for the
resource ID of the interface. Instead, the resource ID is defined as 1%2f1%2f7, which is the percent-
encoded representation of the switch member/slot/port notation: 1/1/7.
self.monitor = Monitor('/rest/v1/system/interfaces/1%2f1%2f7?attributes=rx_bytes',
name='Interface Received Bytes')

In the previous example:

n The URI path is: /rest/v1/system/interfaces/1%2f1%2f7

n The resource ID portion of the path is: 1%2f1%2f7

n The URI query string is: ?attributes=rx_bytes

To get the URI of a resource to monitor, you can use the AOS-CX REST API Reference browser interface
to access the REST API. For more information about the REST API and the Swagger UI, see the REST API
Guide.

When you specify the monitored URI, you can also use variables to represent the URI. This strategy can
simplify updating a script with the REST API version changes or to make code more readable when there
are long URI paths.

Scripts | 105

For example:
#Received bytes on a user-specified interface

uri1 = '/rest/v1/system/interfaces/{}?attributes=rx_bytes'
self.m1 = Monitor(

uri1,
'Interface Received Bytes',
[self.params['iface_id']])

URIs for monitors

The URI of a monitored resource is composed of several components, including the host name or host
IP address, the path, and the query string that specifies the attribute to monitor.

In a Python NAE script, when you specify the URI of a local switch resource to monitor, omit the server
URL portion of the URI. Specify only the path and query string portion of the URI.

For example:
cpu_uri = '/rest/v1/system/daemons/{}?' \

'attributes=resource_utilization.cpu'

If the switch is a VSX switch, you can specify the peer switch by prepending /vsx-peer to the path
portion of the URI.

For example:
peer_cpu_uri = '/vsx-peer/rest/v1/system/daemons/{}?' \

'attributes=resource_utilization.cpu'

Path component of the URI

The path component of the URI is everything before the question mark (?) character. The path is a
hierarchy. The forward slash (/) character indicates the hierarchical relationship between resources.

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

106

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

Scripts | 107

n Youcanuseawildcardtospecifyallinterfaces,butyoucannotusethewildcardcharactertospecify
theinterfacesinmember1,slot2.
WhendesigningscriptsthatusewildcardcharactersinmonitoredURIs,beawarethatusingawildcardcharacter
forcertainresourcescanresultinhighswitchCPUandmemoryutilization,whichcaninturnaffectthe
performanceoftheswitch.
UsingawildcardforresourcessuchasACLs,interfaces,VLANs,orVRFs,mightnotresultinperformanceissuesin
acustomerenvironmentthatincludesasmallnumberofthoseresources.However,whenthesamescriptis
installedinacustomerenvironmentthathasalargenumberofthoseresources—suchas500interfaces—
thousandsoftimeseriesinstancesarecreated.
Eachmonitoredresourcecreatesonetimeseries.EachtimeseriesrequiresswitchCPU,memory,andstorage
spaceinthetimeseriesdatabase.Switchperformancecanbeaffectedwhentheresidentmemoryresources
usedbytheNAEexceedsapproximately500MB.
MonitoringthecountofresourcesbyincludingthecountparameterintheURI—evenonthousandsof
resources—doesnotcauseperformanceissues.
| Parameters | in monitored |     | URIs |     |     |     |
| ---------- | ------------ | --- | ---- | --- | --- | --- |
Youcanuseuser-definedparameterstodefinetheresourceIDintheURIpassedtotheMonitor
function.
Forexample,insteadofcreatingamonitorforaspecificinterfaceonaswitch,youcandefinea
parameterforthatinterface.Then,whentheagentiscreated,theusersuppliestheidentifierof
interfacetobemonitored.
ParametersinmonitoredURIscanonlybeusedtospecifyresourceidentifiers,whicharethelastpartof
thepathbeforethequerystring.UsingparameterstospecifyattributesorotherURIcomponentsisnot
supported.
Parametersareindicatedbybraces{}.
ThefollowingexampleshowstheuseofaparameterfortheIDofaninterface:
self.monitor = Monitor("/system/interfaces/{}?attributes=rx_bytes",
|     |     | [self.params["iface_id"] |     |     | ],name="Interface | Received Bytes") |
| --- | --- | ------------------------ | --- | --- | ----------------- | ---------------- |
Intheexample:
n IntheURI,insteadofspecifyingaspecificinterface,theURIcontainsthefollowingcharactersto
indicatethataparameterisexpected:
{}
n Thefollowingargumentindicatesthatthenameoftheuser-definedparameterisiface_id:
| [self.params["iface_id"] |     |     | ],  |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- |
n Theiface_idparameterisdefinedintheParameterDefinitionsportionofthescript:
| ParameterDefinitions |                    | =       | {          |                   |     |     |
| -------------------- | ------------------ | ------- | ---------- | ----------------- | --- | --- |
| 'iface_id':          | {                  |         |            |                   |     |     |
|                      | 'Name': 'Interface |         | Id',       |                   |     |     |
|                      | 'Description':     |         | 'Interface | to be monitored', |     |     |
|                      | 'Type': 'string',  |         |            |                   |     |     |
|                      | 'Default':         | '1/1/1' |            |                   |     |     |
}
| Examples | of invalid | parameter |     | definitions |     |     |
| -------- | ---------- | --------- | --- | ----------- | --- | --- |
Thefollowingparameterdefinitionisinvalidbecauseitattemptstocreateaparameterforanattribute,
suchasreceivedbytesortransmittedbytes:
| # Example | of invalid | parameter |     | usage: attribute |     |     |
| --------- | ---------- | --------- | --- | ---------------- | --- | --- |
self.monitor = Monitor("/system/interfaces/1%2F1%2F5?attributes={}",
| [self.params["attr"] |     | ],  | name="Interface | Received | Bytes") |     |
| -------------------- | --- | --- | --------------- | -------- | ------- | --- |
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 108

Thefollowingparameterdefinitionisinvalidbecauseitattemptstocreateaparameterforacomponent
oftheURIthatisnottheresourceID:
| # Example | of  | invalid | parameter: |     | URI component | not resource | ID  |
| --------- | --- | ------- | ---------- | --- | ------------- | ------------ | --- |
self.monitor = Monitor("/system/{}/1%2F1%2F5?attributes=rx_bytes",
| [self.params["resource"] |                |     |     | ],name="Interface |      | Received Bytes") |     |
| ------------------------ | -------------- | --- | --- | ----------------- | ---- | ---------------- | --- |
| Slash                    | (/) characters |     | in  | monitored         | URIs |                  |     |
ToavoidmistakenlyinterpretingslashesinresourceIDaspartoftheURIpath,slash(/)charactersina
resourceIDthatisnotauser-definableparametermustbeencodedas:%2for%2F.
InthepathcomponentofaURI,theslash(/)characterisareservedcharacterthatisadelimiter
betweenpathsegments.Forexample:
path/to/resourceID
Resourcesonaswitchmightalsousetheslashcharacterintheiridentifications.Forexample:
Aninterfacemightbeidentifiedbyamember/slot/portnotation,suchas:1/1/7
n
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
Thefollowingexampleshowspartsofascriptthatdefinesinterface_idasauser-definedparameter
andthenpassesthatparametertoaMonitorfunctionandtoanActionCLIfunction.
| ParameterDefinitions |                |            | =       | {           |                  |            |     |
| -------------------- | -------------- | ---------- | ------- | ----------- | ---------------- | ---------- | --- |
| 'interface_id':      |                |            | {       |             |                  |            |     |
|                      | 'Name':        | 'Monitored |         | Interface', |                  |            |     |
|                      | 'Description': |            |         | 'The id     | of the monitored | interface, |     |
|                      | 'Type':        | 'string',  |         |             |                  |            |     |
|                      | 'Default':     |            | '1/1/1' |             |                  |            |     |
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
| ActionCLI('show |     | interface |     | {}', | [self.params['interface_id']] |     |     |
| --------------- | --- | --------- | --- | ---- | ----------------------------- | --- | --- |
...
| Attribute | filters | in  | monitored |     | URIs |     |     |
| --------- | ------- | --- | --------- | --- | ---- | --- | --- |
Sometypesofattributescanbefilteredfurtherbyspecifyinganattributenameandvaluepairinstead
ofjustanattributename.
Forexample,youmightwanttospecifythatonlyphysicalinterfacesbemonitored.Thereisnowayto
specifyonlythephysicalinterfacesintheURIpath.However,physicalinterfaceshaveanattributecalled
type,whichhasavalueofsystem.
Thefilterkeywordindicatesthatthevaluethatfollowstheequalsign(=)isanattributeandvaluepair.
Scripts|109

The filtered attribute must be the name of an attribute of the resource specified by the path component
of the URI.

The attribute must be one of the following data types:

n integer

n string

n boolean

For information about the names, types, and values of attributes of a resource, see the AOS-CX REST API
Reference.

The syntax of the attribute and value pair is the following:
attribute-name:attribute-value

Multiple attribute and value pairs are supported. Commas separate the pairs. For example:
...&filter=type:vlan,admin_state:up

Examples

The following example shows a monitored URI that specifies the received packets of all physical
interfaces.
uri1 = '/rest/v1/system/interfaces/*?attributes=statistics.rx_packets&filter=type:system'
self.m1 = Monitor(uri1, 'rx on all physical interfaces')

The following example shows a monitored URI that specifies the received packets of VLAN interfaces
that are in an up state.
uri2 = '/rest/v1/system/interfaces/*?attributes=statistics.rx_
packets&filter=type:vlan,admin_state:up'
self.m2 = Monitor(uri2, 'rx on UP VLAN interfaces')

Constructing a URI using the AOS-CX REST API Reference

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

110

3. Click the endpoint in the GET method to expand the collection.

4. Navigate to the Parameters section and select the attribute or attributes you want to display.

You can select multiple attributes:

n To select a range of attributes, click the first attribute, then press Shift, and then click the last

attribute in the range you want to select.

n To select attributes that are not adjacent in the list, press Ctrl, then click each attribute you

want to select.

5. Click Submit.

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

Scripts | 111

c.

If you are specifying subcomponent of the attribute, view the Response Body and record the
exact name of the attribute component to add to the query portion of the URI.

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

112

| max_m | = Max(uri2) |     |     |     |     |     |
| ----- | ----------- | --- | --- | --- | --- | --- |
self.m15 = Monitor(max_m, name='Resource Utilization Poll Interval')
Average
Calculatestheaverageofthemonitoredresourcevalues.WhenthemonitoredURIcontainswildcard
characters,thisfunctioncalculatesandreturnstheaveragevalueoverthecurrentvaluesofall
resourcespointedtobyexpandingthewildcards.
Example:
| avg_m | = Average(uri2) |     |     |     |     |     |
| ----- | --------------- | --- | --- | --- | --- | --- |
self.m17 = Monitor(avg_m, name='Resource Utilization Poll Interval')
| Aggregate |     | functions |     |     |     |     |
| --------- | --- | --------- | --- | --- | --- | --- |
Aggregatefunctionsaretime-dependentandarecomputedoveratimeinterval.Aggregatefunctions
includetheratefunctionandfunctionswithnamesthatincludethekeywordOverTime.Aggregate
functionsmustspecifyatimeinterval.
Transitionandratiocalculationsarenotconsideredaggregatefunctions.
IfthemonitoredURIincludesparametersandthemonitorisanaggregatefunction,theparameter
mustbepassedtotheaggregatefunctioninsteadoftotheMonitorfunction.
Forexample:
uri2 = '/rest/v1/system/interfaces/{}?attributes=statistics.rx_packets'
avg_m = AverageOverTime(uri2, "1 hour", [self.params['interface_id']])
| self.m2 | = Monitor(avg_m, |     | 'Rx Packets') |     |     |     |
| ------- | ---------------- | --- | ------------- | --- | --- | --- |
Intheexamplesofthefunctions,uri2isthefollowing:
uri2 = '/rest/v1/system?attributes=resource_utilization_poll_interval'
Theaggregatefunctionsarethefollowing:
CountOverTime
Countsthenumberofdistincttime-seriesdatapointsthathavebeengeneratedduringthespecified
periodoftime.
ExampleCountOverTime:
| count_over_m |         | = CountOverTime(uri2, |                | "5  | minutes")   |                 |
| ------------ | ------- | --------------------- | -------------- | --- | ----------- | --------------- |
|              | self.m2 | = Monitor(            |                |     |             |                 |
|              |         | count_over_m,         | name='Resource |     | Utilization | Poll Interval') |
SumOverTime
Calculatesthesumofthemonitoredresourcevaluesthatoccurredduringthespecifiedperiodof
time.WhenthemonitoredURIcontainswildcardcharacters,thisfunctionsumsoverthecurrent
valuesofallresourcespointedtobyexpandingthewildcards.
ExampleSumOverTime:
| sum_over_m |          | = SumOverTime(uri2, |                | "5 minutes") |             |                 |
| ---------- | -------- | ------------------- | -------------- | ------------ | ----------- | --------------- |
|            | self.m10 | =                   | Monitor(       |              |             |                 |
|            |          | sum_over_m,         | name='Resource |              | Utilization | Poll Interval') |
MinOverTime
Calculatestheminimumofthemonitoredresourcevalues.WhenthemonitoredURIcontains
wildcardcharacters,thisfunctionreturnstheminimumvalueoverthecurrentvaluesofallresources
pointedtobyexpandingthewildcards.
ExampleMinOverTime:
| min_over_m |         | = MinOverTime(uri2, |                | "5 minutes") |             |                 |
| ---------- | ------- | ------------------- | -------------- | ------------ | ----------- | --------------- |
|            | self.m2 | = Monitor(          |                |              |             |                 |
|            |         | min_over_m,         | name='Resource |              | Utilization | Poll Interval') |
Scripts|113

MaxOverTime
Calculatesthemaximumofthemonitoredresourcevalues.WhenthemonitoredURIcontains
wildcardcharacters,thisfunctionreturnsthemaximumvalueoverthecurrentvaluesofallresources
pointedtobyexpandingthewildcards.
Example:MaxOverTime:
| max_over_m | = MaxOverTime(uri2, |                | "5 minutes") |             |                 |
| ---------- | ------------------- | -------------- | ------------ | ----------- | --------------- |
|            | self.m16 =          | Monitor(       |              |             |                 |
|            | max_over_m,         | name='Resource |              | Utilization | Poll Interval') |
AverageOverTime
Calculatestheaverageofthemonitoredresourcevaluesoverthespecifiedperiodoftime.Whenthe
monitoredURIcontainswildcardcharacters,thisfunctioncalculatesandreturnstheaveragevalue
overthecurrentvaluesofallresourcespointedtobyexpandingthewildcards.
ExampleAverageOverTime:
| avg_over_m | = AverageOverTime(uri2, |                | "5  | minutes")   |                 |
| ---------- | ----------------------- | -------------- | --- | ----------- | --------------- |
|            | self.m18 =              | Monitor(       |     |             |                 |
|            | avg_over_m,             | name='Resource |     | Utilization | Poll Interval') |
Rate
Calculatestheper-secondaveragerateofincreaseforthemonitoredresourcevalueoverthe
specifiedperiodoftime.WhenthemonitoredURIcontainswildcardcharacters,thisfunction
calculatestheper-secondaveragerateofincreaseforeachofthemonitoredresourcespointedtoby
expandingthewildcards.
Example:
| rate_m | = Rate(uri2, | "5 minutes") |     |     |     |
| ------ | ------------ | ------------ | --- | --- | --- |
self.m8 = Monitor(rate_m, name='Resource Utilization Poll Interval')
Time interval
Theformatofthetimeintervalisthefollowing:
| "<number> | <unit>" |     |     |     |     |
| --------- | ------- | --- | --- | --- | --- |
Thevaluefor<unit>isoneofthefollowing:
n second
n seconds
n minute
n minutes
n day
days
n
hour
n
n hours
| Forexample:"12 | seconds"  |           |     |           |     |
| -------------- | --------- | --------- | --- | --------- | --- |
| Nested         | aggregate | functions | and | operators |     |
Nestinganaggregatefunctionoroperatorinsideofanaggregatefunctionenablesyoutocombinethe
capabilitiesofbothtocreateoneresult.Thenestedfunctionoroperatorisexecutedfirst,andthenthe
enclosingoperatorisexecuted.
Forexample,thefollowingnestedfunctioncalculatestherateoftheswitchresourceandsumsthe
calculatedratesacrossalltheURIspointedtobytheexpandedwildcard:
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 114

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
packet value. In the example, the condition self.rule2.condition triggers an alert when the average
of received packets on an interface becomes greater than 50 within the past five minutes.
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

Scripts | 115

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

116

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

o The clear action—removing the alert level—is executed only when the clear condition becomes

true—the CPU utilization drops below 70%. The clear condition becomes inactive and is no longer
evaluated. The condition becomes active again and is evaluated at regular intervals.

In effect, one of the ways you can use a clear condition is to use it in combination with the condition to
set both a high threshold and a low threshold.

You define a clear condition using the clear_condition function. The clear_condition function
contains the condition expression (in quotes) and, optionally, any parameters used in the condition
expression.

Example of a clear condition in a monitor:
self.monitor = Monitor(AverageOverTime("/rest/v1/system/subsystems/management_
module/1%2F5?attributes=resource_utilization.cpu", "5 minutes")
self.rule = Rule("")
self.rule.condition("{} > 90", [self.monitor])
seld.rule.action("ALERT_LEVEL", AlertLevel.CRITICAL)
self.rule.clear_condition("{} < 70", [self.monitor])
self.rule.clear_action(self.set_normal)

Condition expression syntax

The condition of a rule is a one-line expression that uses the following syntax, expressed in EBNF
(Extended Backus-Naur) notation:
uri
enum

= ? https://tools.ietf.org/html/rfc3986 ?
= ? string ?

Scripts | 117

| integer      | = ? signed     | int64     |           | ?       |                |         |           |         |
| ------------ | -------------- | --------- | --------- | ------- | -------------- | ------- | --------- | ------- |
| list_element | = '"' ,        | ( enum    | |         | integer | )              | , '"'   |           |         |
| list         | = list_element |           | ,         | { ","   | , list_element |         | }         |         |
| operator     | = "<" |        | ">"       | | "=="    | | "!="  | |              | "<=" |  | ">="      |         |
| over         | = "over"       | , integer |           | , time  |                |         |           |         |
| for          | = "for"        | , integer |           | , time  |                |         |           |         |
| time         | = "second"     | |         | "seconds" |         | | "minute"     | |       | "minutes" | | "day" |
|              | | "days"       | |         | "hour"    | |       | "hours"        | | "day" | |         | "days"  |
| aggregator   | = "count"      | |         | "sum"     | | "min" | |              | "max" | | "avg"     |         |
| pause        | = "pause"      | ,         | integer   | ,       | time           |         |           |         |
| operation1   | = uri ,        | operator  |           | , list  | , [ for        | ] ,     | [ pause   | ]       |
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
Ifaconditionexpressionhastheforkeywordfollowedbyaduration,theexpressionwillbe
evaluatedandmonitoredforthatparticulardurationbeforetheconditionisconsideredtrueand
anyruleactionsareexecuted.
Forexample,thefollowingconditionexpressionistrueonlyifthecountoftheconn_statehasbeen
lessthan5forthreeminutes:
count /v1/system/vrfs/red/bgp_routers/bgp_neighbors/?attributes=conn_state < 5 for 3
minutes
| pause followed | by a duration |     |     |     |     |     |     |     |
| -------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Ifaconditionexpressionhasthepausekeywordfollowedbyaduration,theconditionwillnotbe
monitoredforthespecifieddurationaftertheconditionismet.However,becausetheconditionis
true,anyruleactionsareexecutedbeforemonitoringispaused.
Forexample,thefollowingconditionexpressionspecifiesthatthespanningtreetcn_countwillnot
bemonitoredforoneminuteafterthetcn_countisgreaterthan10.
| /v1/system/vlan/1/spanning_tree/tcn_count |     |     |     |     |     | > 10 | pause | 1 minute |
| ----------------------------------------- | --- | --- | --- | --- | --- | ---- | ----- | -------- |
Usingthesekindsofexpressionscanreducethenumberofactionstaken—suchaslogentries
generated—whenanetworkconditionistemporary,butstillensurethatactionsaretakenat
intervalstheadministratorconsiderstobereasonable.
Examples
rate /v1/system?attributes=resource_utilization_poll_interval > 300 per 1 hour for 5
hours
rate /v1/system?attributes=resource_utilization_poll_interval > 300 per 2 hours for 5
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 118

days
avg over 1 minute /v1/system/interface/1?attributes=statistics.tx_dropped < 5 for 2
minutes
rate /v1/system?attributes=resource_utilization_poll_interval > 300 per 10 seconds for 5
minutes
avg over 1 minute /v1/system/interface/1?attributes=statistics.tx_dropped < 5 for 2
| minutes pause | 10 seconds |     |     |     |
| ------------- | ---------- | --- | --- | --- |
Conjunction (AND), disjunction (OR), and multiple subconditions
Whenyoudefineacondition,youcancreateanexpressionthatcombinesmultiplesubcondition
expressionsusingtheoperatorsAND,OR,andparenthesis.
Theconditionfunctionreturnstrueifthecombinationofthesubconditionsistrue.
Operatorprecedence:
1. Parenthesisoperator:()
2. ANDoperator
3. ORoperator
Forexample,considerthefollowingexpression:
| SubCondition1 | AND SubCondition2 | OR Subcondition3 |     |     |
| ------------- | ----------------- | ---------------- | --- | --- |
Becausetherearenoparenthesesinthisexpression,theANDoperationisevaluatedfirst.Theresultof
thatevaluationisthenevaluatedagainstSubcondition3usingtheORoperator.Theconditionfunction
returnstheresultofthesecondevaluation.Thefollowingtableshowstheresultsaccordingtothe
evaluationofeachsubcondition:
| Subcondition1 | Subcondition2 |     | Subcondition3 | Result |
| ------------- | ------------- | --- | ------------- | ------ |
| true          | true          |     | false         | true   |
| true          | false         |     | false         | false  |
| false         | true          |     | false         | false  |
| false         | false         |     | false         | false  |
| true          | true          |     | true          | true   |
| true          | false         |     | true          | true   |
| false         | true          |     | true          | true   |
| false         | false         |     | true          | true   |
Thefollowingexampleshowsaconditionwiththreedifferentsubconditions:
1. ResourceUtilizationPollInterval>50
2. Spanningtreehellotime>5
3. VLANadminstatus=down
Example:
uri1 = '/rest/v1/system?attributes=resource_utilization_poll_interval'
self.m1 = Monitor(uri1, name='Resource Utilization Poll Interval')
Scripts|119

uri2 = '/rest/v1/system?attributes=stp_config.hello_time'
self.m2 = Monitor(uri2, name='Spanning tree hello time')

uri3 = '/rest/v1/system/vlans/{}?attributes=admin'
self.m3 = Monitor(uri3, 'Vlan admin status', [self.params['vlan_id']])

self.r1 = Rule("Rule 1")
self.r1.condition('({} > 50 AND {} > 5) OR {} == "down"', [self.m1, self.m2, self.m3])
self.r1.action(self.action_callback1)

Function behavior when monitored URI does not contain wildcards

The following are the behaviors of the supported condition expression functions when the monitored
URI does not contain wildcards—and thus points to one specific resource:
count

This function counts the number of distinct time-series data points that have been generated and
implicitly reflects the "count" of data points collected at each data collection interval.

For example, applying the count function to the following URI results in a value of 1.

/rest/v1/system/subsystems/chassis/base?attributes=resource_utilization.cpu

sum, min, max, and avg

Because there is just one resource, these aggregators return the current value of the resource. These
aggregators only apply to resources represented by integers, such as number of packets received or
CPU utilization.

Aggregator over time

When the keyword over follows one of the aggregators, the function behaves in a similar way but
performs its aggregation "over" the specified time in the past instead of over the current value only.

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

120

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

Scripts | 121

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

122

| n show vlan           | 100 |     |     |
| --------------------- | --- | --- | --- |
| n show running-config |     |     |     |
| n top memory          |     |     |     |
ThestringcanbeeitherasinglelineoramultilinestringwithlinebreaksusinganyPythonlinebreak
technique.
<title>
Specifiesthetitletobedisplayedforthisaction.Thedefinitionof<title>mustusetheTitle
function.
| Forexample:title=Title("interface |     |     | 1/1/1 no shutdown") |
| --------------------------------- | --- | --- | ------------------- |
Usage
n AllCLIcommandsaresupportedasinputtoCLIactions.
n Commandstringsarepassedwithoutvalidation.
n ThefirstCLIactionexecutedinascriptstartsfromthemanager(#)commandcontext.Toexecute
commandsinanothercontext,youmustincludethecommandstoenterthatcontext.
Forexample,toexecuteaconfigurationcommand,youmustenterthecorrectconfigurationcontext,as
inthefollowingaction:
| ActionCLI("config\ninterface |     | 1/1/1\nno | shutdown") |
| ---------------------------- | --- | --------- | ---------- |
SimilartoasingleCLIsession,subsequentCLIactionsinthescriptexecutefromthecommandcontext
thatisinplaceafterthepreviouscommandisexecuted.Inthepreviousexample,thecommandcontext
istheconfigcontext,andthenextCLIactionstartsintheconfigcontext.Commandsthatcannotbe
executedintheconfigcontextfail.
n Asabestpractice,includecommandsineachCLIcommandtoreturntoastandardcommand
contextappropriateforthescript—suchasthemanager(#)context.Forexample:
| ActionCLI("config\ninterface |     | 1/1/1\nno | shutdown\nexit\nexit") |
| ---------------------------- | --- | --------- | ---------------------- |
n Youcancreateacustomtitleforthisaction.ThetitleyoucreatecanhelptheuseroftheWebUIto
determinewhatactionwasexecuted.ThetitleisdisplayedintheAction ResultssectionoftheAlert
Detailsdialogbox.
Examples
ExamplesofamultilineCLIactions:
| ActionCLI("config\ninterface |     | 1/1/1\nno | shutdown\nexit\nexit") |
| ---------------------------- | --- | --------- | ---------------------- |
ExampleofaCLIactionthatusesaparameter:
| ActionCLI("show | interface | {}",[ self.params["iface_id"]]) |     |
| --------------- | --------- | ------------------------------- | --- |
ExampleofaCLIactionthatusesaparameterandacustomtitle:
title = Title("Print interface {} details",[self.params["iface_id"]])
self.ActionCLI("show interface {}", [self.params["iface_id"]], title=title)
ActionCustomReport
Syntax
Insideacallbackaction:
| ActionCustomReport(<template>[, |     | <params>][, | title=<title>]) |
| ------------------------------- | --- | ----------- | --------------- |
Description
Generatesamultiplelinereportwithcustomizedcontent.ThereportcontentcanbeviewedintheWeb
UIfromthealertdetailsfortheagent.
Scripts|123

Parameters
<template>
Specifiesthereporttemplatetousewhengeneratingthisreport.Thistemplatemustbedefined
elsewhereinthescript.
<title>
Specifiesthetitletobedisplayedforthisaction.Thedefinitionof<title>mustusetheTitle
function.
| Forexample:title=Title("Generate |     |     | final MAC | report") |     |
| -------------------------------- | --- | --- | --------- | -------- | --- |
Usage
Thisfunctioncanonlybeusedinsideacallbackaction.
Thescriptmustcontainthetemplate(code)thatgeneratesandformatsthereport.
Youcancreateacustomtitleforthisaction.ThetitleyoucreatecanhelptheuseroftheWebUIto
determinewhatactionwasexecuted.ThetitleisdisplayedintheAction ResultssectionoftheAlert
Detailsdialogbox.
Examples
Exampleofcallingthecustomreportactionwithaparameter:
| ActionCustomReport(my_template, |     | [self.params["author"]]) |     |     |     |
| ------------------------------- | --- | ------------------------ | --- | --- | --- |
ExampleofgeneratingacustomreportinHTMLformat:
uri1 = '/rest/v1/system/vlans/{}/macs/?count'
self.m1 = Monitor(uri1, 'Mac address count', [self.params['vlan_id']])
| self.r1 | = Rule('MAC | Address | Learnt') |     |     |
| ------- | ----------- | ------- | -------- | --- | --- |
self.r1.condition(
|     | '{} > 0 pause | {} minutes',                 |     |     |     |
| --- | ------------- | ---------------------------- | --- | --- | --- |
|     | [self.m1,     | self.params['alert_pause']]) |     |     |     |
self.r1.action(self.gen_custom_report)
| def gen_custom_report(self, |                                | event):                        |          |         |     |
| --------------------------- | ------------------------------ | ------------------------------ | -------- | ------- | --- |
| vlan_id                     | = self.params['vlan_id'].value |                                |          |         |     |
| type_s                      | = ["dynamic",                  | "static",                      | "mclag", | "vrrp"] |     |
| mac_report                  | = []                           |                                |          |         |     |
| for                         | m in type_s:                   |                                |          |         |     |
|                             | mac_all_dict                   | = self.get_mac_result(vlan_id, |          |         | m)  |
mac_report.append(mac_all_dict)
| final_report | =   | self.generate_htmlreport(mac_report) |     |     |     |
| ------------ | --- | ------------------------------------ | --- | --- | --- |
ActionCustomReport(final_report, title=Title("Generate final MAC report"))
| def get_mac_result(self, |                                                 | vlan_id,                          | mac_type): |     |     |
| ------------------------ | ----------------------------------------------- | --------------------------------- | ---------- | --- | --- |
| url                      | = 'http://127.0.0.1:5577/rest/v1/system/vlans/' |                                   |            |     | \   |
|                          | + str(vlan_id)                                  | + '/macs?count=true&filter=from:' |            |     | + \ |
mac_type
| r1                            | = self.rest_get(url)      |              |     |     |     |
| ----------------------------- | ------------------------- | ------------ | --- | --- | --- |
| result                        | = str(r1.json()["count"]) |              |     |     |     |
| return                        | result                    |              |     |     |     |
| def generate_htmlreport(self, |                           | mac_report): |     |     |     |
| html_prefix                   | =                         | '''<html>    |     |     |     |
<head>
<title>HPE-Aruba</title>
</head>
<body>
<table border="1">
|     | <tr align="center"> |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- |
<th><td colspan="4"><b>Summary</b></td></th>
</tr>
|     | <tr align="center"> |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- |
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 124

<th>

<td colspan="4">

<b>Number of MAC learnt on various types</b>

</td>

</th>

</tr>
<tr>

<th>

<th>

STATIC

DYNAMIC </th>
</th>

<th>
<th>

MCLAG
VRRP

</th>
</th>

</tr>

''' + self.get_mac_htmlcontent(mac_report) + '''
</table>

</body>

return html_prefix

</html>'''

For another example of a custom report, see the ospfv2_interface_state_flaps_impact_monitor
solution on the Aruba Solutions Exchange.

ActionShell, SHELL action

Syntax

Inside a callback action:
ActionShell("<command>"[, title=<title>])

Outside of a callback action:
self.r.action("SHELL","<command>"[, title=<title>])

Description

The SHELL action executes the specified command in the Bash shell of the underlying Linux operating
system of the switch.

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

Scripts | 125

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

126

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

Scripts | 127

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

For example, if you define an action to send a message to the log if the CPU utilization gets above 90%,
you can also define an action to send a different message to the log when a CPU utilization that was
above 90% drops to a lower utilization.

The clear action is executed only once—when the condition becomes invalid and the clear condition
becomes valid:

n If the rule does not have a clear condition defined, the default behavior is that the clear condition

becomes valid when the condition transitions from true to false.

For example, if the CPU utilization is greater than 90% (the condition is valid or true), the clear action is
executed when the CPU utilization is equal to or less than 90% (the condition becomes invalid), but not if
it continues to drop or if it remains less than 90% the next time the condition is evaluated. However, if
the CPU utilization becomes greater than 90% again, the clear action will be executed the next time the
CPU utilization drops to less than the threshold of 90%.

n If the rule has a clear condition defined, the clear condition becomes active the first time the

condition becomes true. However, the clear condition does not become valid until it is both active
and it becomes true.

For example, consider a clear condition that becomes true when the CPU utilization drops below 70%.
After the CPU utilization is becomes greater than 90% the clear condition becomes active, but it does
not become true until the CPU utilization drops below 70%. Therefore the clear action is not executed
until a CPU utilization that has been above 90% drops below 70%.

Both predefined and callback actions can be used in clear actions.

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

128

Thefollowingisanexampleofarulethatincludesanactionandtwoclearactions.Intheexample:
n OneoftheclearactionscallstheCLIactiontoexecutetheshow running-configCLIcommand:
| self.rule.clear_action("CLI","show |     |     | running-config") |
| ---------------------------------- | --- | --- | ---------------- |
n Theotherclearactioncallstheset_normalfunction,whichremovesthealertlevel:
self.rule.clear_action(self.set_normal)
Thefollowingexampleshowsamonitorthathasarulethatdefinesaclearactionsandaclear
condition:
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
| ActionSyslog("CPU    |     | Utilization | at %d" % cpu) |
| -------------------- | --- | ----------- | ------------- |
| ActionCLI("top       |     | cpu")       |               |
| def set_normal(self, |     | event):     |               |
self.remove_alert_level()
| Alert | level functions |     |     |
| ----- | --------------- | --- | --- |
TheArubaNetworkAnalyticsEngineprovidesseveralpredefinedfunctionsrelatedtoalerts.
Thealertlevelfunctionsget,set,orremovethealertleveloftheagent:
get_alert_level()
Getsthecurrentalertleveloftheagent.
Example:
| status | = self.get_alert_level() |     |     |
| ------ | ------------------------ | --- | --- |
set_alert_level(<Alert_Level>)
Setsthealertleveloftheagent.
Example:
self.set_alert_level(AlertLevel.CRITICAL)
The<Alert_Level>mustbeoneofthefollowingvalues:
AlertLevel.CRITICAL
Theagenthasdetectedacriticalissue.
AlertLevel.MAJOR
Theagenthasdetectedamajorissue.
AlertLevel.MINOR
Scripts|129

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

n logger.emerg("<message>")

n logger.alert("<message>")

n logger.critical("<message>")

n logger.error("<message>")

n logger.warning("<message>")

n logger.notice("<message>")

n logger.info("<message>")

n logger.debug("<message>")

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

130

Chapter 12

Agents

Agents

An HPE Aruba Networking Network Analytics Engine agent is a specifically-configured executable
instance of an Aruba Network Analytics Engine script on a switch. When the agent is enabled, it performs
the tasks defined by the script.

HPE Aruba Networking Network Analytics Engine agent sandboxes run in the default VRF. If a script has
a function that requires access to the Internet, this function fails unless the switch administrator
configures a DNS name server on the default VRF.

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

131

The HPE Aruba Networking Network Analytics Engine includes several safeguards. In order to preserve a
switch's persistent storage device, NAE imposes the following mechanisms:

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

Agents | 132

Chapter 13

Network Analytics Engine Lite

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

Using an NAE-Lite agent, you can define either one of the following:

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

133

n Schedule—ExecutesaconfiguredjobCLI commandsatthespecifictime.
n Trap—Createsasnmptrapmessageandsendsittotheconfiguredsnmpservers.
Thishelpsyoutonotifyandcollectmoredetailedinformationaboutthesystemtotroubleshootany
issues.
| NAE-Lite agent | limitations |     |     |     |
| -------------- | ----------- | --- | --- | --- |
ThefollowinglimitationsapplytoanNAE-Liteagent:
n Onlyoneagentperscriptissupported.Multipleagentsperscriptarenotsupported.
n Onlyoneresourceorsetofeventscanbemonitoredusingsetandclearconditions.Setandclear
conditioncanhavedifferentresourcesorsetofeventIDs.
n Insetandclearconditions,multiplerulesandcombinationsarenotsupported.
n Onlylimitedsetofpredefinedactionssuchassettingstatuslevel,sendingsystemlogmessage
(Syslog)andexecutingCLIcommandsaresupported.
n ParametersarenotsupportedinanNAE-Liteagent.
n Callbackactionsarenotsupported.
| NAE-Lite agent | tasks |     |     |     |
| -------------- | ----- | --- | --- | --- |
NAE-Litetasksareasfollows:
| Task           | Command   |                   |     |     |
| -------------- | --------- | ----------------- | --- | --- |
| CreatinganNAE- | nae-agent | lite <AGENT-NAME> |     |     |
Liteagent
desc <DESCRIPTION>
Configuringthe
descriptionfor
theNAE-Lite
agent
disable
Disablingthe
NAE-Liteagent
| Configuringthe | tags <TAG-LIST> |     |     |     |
| -------------- | --------------- | --- | --- | --- |
taglist
| Configuringthe | monitor | <MONITOR-NAME> | {resource | <RESOURCE>} |
| -------------- | ------- | -------------- | --------- | ----------- |
monitorfor group-by {count | sum | min | max | average } [over <DURATION>]]
| system | monitor | <MONITOR-NAME> | resource | <RESOURCE> |
| ------ | ------- | -------------- | -------- | ---------- |
resourceswith
group-by rate over {seconds | minutes | hours | days} <DURATION>
timeseriesdata
set-condition monitor <MONITOR-NAME> {{lt | le | eq | ne | gt | ge}
Settingthe
conditionforthe <VALUE> [for {seconds | minutes | hours | days} <DURATION>] |
| monitor | transition | from | <STRING-LIST> | to <STRING-LIST>} |
| ------- | ---------- | ---- | ------------- | ----------------- |
Clearingthe clear-condition monitor <MONITOR-NAME> {{lt | le | eq | ne | gt | ge}
conditionforthe <VALUE> [for {seconds | minutes | hours | days} <DURATION>]
|     | | transition | from | <STRING-LIST> | to <STRING-LIST>} |
| --- | ------------ | ---- | ------------- | ----------------- |
monitor
| Configuringthe | watch <WATCH-NAME> |     | {event-log | <EVENT-ID-LIST>} |
| -------------- | ------------------ | --- | ---------- | ---------------- |
watchforthe
NAE-Liteagent
NetworkAnalyticsEngineLite|134

| Task |     | Command |     |     |     |     |     |     |     |
| ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Settingthe set-condition watch event-log <WATCH-NAME> [include {all | any}
conditionforthe <REGEX-LIST>] [exclude <REGEX-LIST>] [count <COUNT>]
watch
clear-condition watch event-log <WATCH-NAME> [include {all | any}
Clearingthe
|     |     | <REGEX-LIST>] |     |     | [exclude | <REGEX-LIST>] |     | [count <COUNT>] |     |
| --- | --- | ------------- | --- | --- | -------- | ------------- | --- | --------------- | --- |
conditionforthe
watch
|     |     | status |     | {normal | | minor | | major | | critical} |     |     |
| --- | --- | ------ | --- | ------- | ------- | ------- | ----------- | --- | --- |
Configuring
|     |     | syslog |     | <MESSAGE> | [facility |     | <FACILITY>] | [severity | <SEVERITY>] |
| --- | --- | ------ | --- | --------- | --------- | --- | ----------- | --------- | ----------- |
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
|     | set-condition |                 | monitor |         | average_cpu     | gt  | 80  |     |     |
| --- | ------------- | --------------- | ------- | ------- | --------------- | --- | --- | --- | --- |
|     |               | status          | major   |         |                 |     |     |     |     |
|     |               | syslog          | "High   | cpu     | usage detected" |     |     |     |     |
|     |               | cli top         | cpu     |         |                 |     |     |     |     |
|     |               | clear-condition |         | monitor | average_cpu     |     | lt  | 40  |     |
|     |               | status          | normal  |         |                 |     |     |     |     |
exit
| nae-agent |        | lite   | cpu_monitor |       | activate |     |     |     |     |
| --------- | ------ | ------ | ----------- | ----- | -------- | --- | --- | --- | --- |
| Monitor   | system | memory |             | usage |          |     |     |     |     |
Thefollowingmemory_monitoragentcomputesthememoryusageandcreatesanalertifthecurrent
memoryusageishigherthan80%.Thetop memorycommandoutputiscapturedandpreservedwhen
thealertisgenerated.Additionally,theagentstatusissettomajorwhentheconditionismet.The
clear-conditionismetwhenthecurrentmemoryusagefallsbelow40%.Theagentstatusissetto
normaloncetheclear-conditionismet.
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 135

nae-agent lite memory_monitor

desc System memory monitoring
monitor memory resource system memory
set-condition monitor memory gt 80

status major
syslog "High memory usage detected"
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

Network Analytics Engine Lite | 136

|     | watch | mac_w | event-log |     | 4801 |     |     |     |     |
| --- | ----- | ----- | --------- | --- | ---- | --- | --- | --- | --- |
set-condition watch event-log mac_w include all "MAC 11:22:33:44:55:66","VLAN
| 10" | count | 10       |                   |     |     |     |     |     |     |
| --- | ----- | -------- | ----------------- | --- | --- | --- | --- | --- | --- |
|     |       | status   | minor             |     |     |     |     |     |     |
|     |       | cli show | mac-address-table |     |     |     |     |     |     |
exit
| nae-agent |     | lite   | mac_move |     | activate |     |     |     |     |
| --------- | --- | ------ | -------- | --- | -------- | --- | --- | --- | --- |
| Watch     | for | memory | events   |     |          |     |     |     |     |
Thefollowingwatch_memoryagentiscreatedtowatchforthesystemmemoryrelatedeventsfromthe
module1/1andperformactions.Theeventlog1208israisedwhenhighmemoryusageisdetectedand
theeventlog1207israisedwhenusagegetsbacktonormalrange.
| nae-agent |               | lite           | watch_memory |           |           |           |                  |             |       |
| --------- | ------------- | -------------- | ------------ | --------- | --------- | --------- | ---------------- | ----------- | ----- |
|           | desc          | Watch          | memory       | usage     |           |           |                  |             |       |
|           | watch         | high_mem       |              | event-log |           | 1208      |                  |             |       |
|           | watch         | normal_mem     |              | event-log |           | 1207      |                  |             |       |
|           | set-condition |                |              | watch     | event-log |           | high_mem include | any "1/1"   |       |
|           |               | status         | major        |           |           |           |                  |             |       |
|           |               | cli top        | mem          |           |           |           |                  |             |       |
|           |               | clear-condtion |              |           | watch     | event-log | normal_mem       | include any | "1/1" |
|           |               | status         |              | normal    |           |           |                  |             |       |
exit
| nae-agent     |                    | lite  | watch_memory |           |           | activate           |        |     |     |
| ------------- | ------------------ | ----- | ------------ | --------- | --------- | ------------------ | ------ | --- | --- |
| Watch         | for                | ICMP  | echo         |           |           |                    |        |     |     |
| nae-agent     |                    | lite  | icmp_IPSLA   |           |           |                    |        |     |     |
| desc          | Watch              | the   | loopback     |           | interface |                    | status |     |     |
| tags          | icmp,interface     |       |              |           |           |                    |        |     |     |
| watch         | loopback_interface |       |              |           | event-log |                    | 2402   |     |     |
| set-condition |                    |       | watch        | event-log |           | loopback_interface |        |     |     |
| status        |                    | major |              |           |           |                    |        |     |     |
| Watch         | for                | HTTPS | Server       | Down      |           |                    |        |     |     |
| nae-agent     |                    | lite  | https_IPSLA  |           |           |                    |        |     |     |
| desc          | Watch              | the   | https        | server    |           | status             |        |     |     |
| tags          | https,server       |       |              |           |           |                    |        |     |     |
| watch         | https_rest_disable |       |              |           | event-log |                    | 4661   |     |     |
| watch         | https_rest_enable  |       |              |           | event-log |                    | 4660   |     |     |
set-condition watch event-log https_rest_disable include any "REST server is
| disabled |        | on VRF      | mgmt"        |                   |     |      |                      |          |     |
| -------- | ------ | ----------- | ------------ | ----------------- | --- | ---- | -------------------- | -------- | --- |
| status   |        | major       |              |                   |     |      |                      |          |     |
| syslog   |        | "!CRITICAL! |              | severity_warning: |     |      | HTTPS server         | is down" |     |
| cli      | config | \n          | https-server |                   | vrf | mgmt | \n show https-server |          |     |
clear-condition watch event-log https_rest_enable include any "REST server is
| enabled   |     | on VRF    | mgmt"       |      |          |          |     |     |     |
| --------- | --- | --------- | ----------- | ---- | -------- | -------- | --- | --- | --- |
| nae-agent |     | lite      | https_IPSLA |      | activate |          |     |     |     |
| Watch     | for | Interface | and         | VLAN |          | Flapping |     |     |     |
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 137

Event|404|LOG_INFO|UKWN|1|Link status for interface 1/1/1 is down -
| Administratively |     |     | down |     |     |     |     |
| ---------------- | --- | --- | ---- | --- | --- | --- | --- |
Event|403|LOG_INFO|UKWN|1|Link status for interface 1/1/1 is up at 1 Gbps.
| nae-agent     |                | lite  | intflap_watch     |           |                |           |          |
| ------------- | -------------- | ----- | ----------------- | --------- | -------------- | --------- | -------- |
| watch         | interface_down |       |                   | event-log | 404            |           |          |
| watch         | interface_up   |       | event-log         |           | 403            |           |          |
| set-condition |                | watch | event-log         |           | interface_down |           |          |
| status        | critical       |       |                   |           |                |           |          |
| syslog        | "!CRITICAL!    |       | severity_warning: |           |                | interface | is down" |
cli config \n interface 1/1/1-1/1/28 \nno shutdown \nshow interface brief
| clear-condition |                |        | watch         | event-log | interface_up |            |     |
| --------------- | -------------- | ------ | ------------- | --------- | ------------ | ---------- | --- |
| syslog          | "interface     |        | is            | up and    | status       | to normal" |     |
| nae-agent       |                | lite   | intflap_watch |           | activate     |            |     |
| Watch           | for Scheduled  |        | Config        |           |              |            |     |
| nae-agent       |                | lite   | ledd_crash    |           |              |            |     |
| desc            | Watch          | system | crash         | event     |              |            |     |
| tags            | crash,resource |        |               |           |              |            |     |
| watch           | crash_event    |        | event-log     |           | 1201         |            |     |
| set-condition   |                | watch  | event-log     |           | crash_event  |            |     |
| status          | critical       |        |               |           |              |            |     |
cli copy core-dump daemon ledd tftp://10.80.2.204/coredump.txt vrf mgmt
schedule config\nschedule 1\n 10 job j1\n 20 job j2\n trigger every minutesm 30
| start         | 21:58                | 2024-02-06 |                          |           |          |         |     |
| ------------- | -------------------- | ---------- | ------------------------ | --------- | -------- | ------- | --- |
| nae-agent     |                      | lite       | ledd_crash               |           | activate |         |     |
| MSTP NAE      | LITE                 |            |                          |           |          |         |     |
| nae-agent     |                      | lite       | STP                      |           |          |         |     |
| desc          | Spanning-tree-script |            |                          |           |          |         |     |
| tags          | BPDU,MSTP,root       |            |                          |           |          |         |     |
| watch         | STP                  | event-log  | 2006,2007,2008,2009,2013 |           |          |         |     |
| watch         | topo1                | event-log  |                          | 2003      |          |         |     |
| set-condition |                      | watch      | event-log                |           | STP      | count 5 |     |
| status        | major                |            |                          |           |          |         |     |
| syslog        | "BPDU                | received   |                          | on admin" |          |         |     |
cli show spanning-tree \n show spanning-tree summary port \n show spanning-tree
| summary          | root          |        |                 |            |               |          |     |
| ---------------- | ------------- | ------ | --------------- | ---------- | ------------- | -------- | --- |
| OSPF Neighboring |               |        | Monitor         | CLI Script |               |          |     |
| nae-agent        |               | lite   | ospf_events_nei |            |               |          |     |
| watch            | ospf_neighbor |        | event-log       |            | 2401,2402     |          |     |
| set-condition    |               | watch  | event-log       |            | ospf_neighbor |          |     |
| status           | major         |        |                 |            |               |          |     |
| syslog           | "2401         | OSPFv2 | neighbor        |            | state         | changed" |     |
cli show ip ospf neighbor \n show ip ospf statistics \n show ip ospf interface
| clear-condition |          |        | watch           | event-log | ospf_neighbor |             |     |
| --------------- | -------- | ------ | --------------- | --------- | ------------- | ----------- | --- |
| syslog          | "2401    | OSPFv2 | neighbor        |           | state         | normalized" |     |
| nae-agent       |          | lite   | ospf_events_nei |           | activate      |             |     |
| #OSPF           | Router   | ID     | Duplication     |           | Monitor       | CLI script  |     |
| nae-agent       |          | lite   | ospf_events_rid |           |               |             |     |
| watch           | ospf_rid |        | event-log       | 2410      |               |             |     |
| set-condition   |          | watch  | event-log       |           | ospf_rid      |             |     |
NetworkAnalyticsEngineLite|138

status major
syslog "2410 OSPFv2 Router-ID duplicated"
cli show ip ospf
clear-condition watch event-log ospf_rid
syslog "2410 OSPFv2 Router-ID normalized"
nae-agent lite ospf_events_rid activate

BGP Monitor CLI Script

nae-agent lite BGP_Neighborship_Monitor_script
watch BGP_TEST_Down event-log 2902
watch BGP_TEST_UP event-log 2901
set-condition watch event-log BGP_TEST_Down
status major
syslog "Check_BGP_Status"
cli show bgp ipv4 unicast summary \n show bgp ipv4 unicast neighbors 10.10.10.2 \n
show bgp ipv4 unicast neighbors 10.10.10.2 routes
clear-condition watch event-log BGP_TEST_UP
status minor
syslog "BGP_is_BACK"
cli show bgp ipv4 unicast summary \n show bgp ipv4 unicast neighbors 10.10.10.2 \n
show bgp ipv4 unicast neighbors 10.10.10.2 routes
!
nae-agent lite BGP_Neighborship_Monitor_script activate

VSX Monitoring

vsx_device_roles

#VSX Device Role NAE Lite
nae-agent lite
watch vsx_role_primary event-log 7007
watch vsx_role_secondary event-log 7008
set-condition watch event-log vsx_role_primary include all “Device
role”,”primary”,”secondary”
status major
syslog "Device roles inconsistent" severity alert
cli show vsx status
clear-condition watch event-log vsx_role_secondary include all “Device role”,
”primary”,”secondary”
syslog “!NORMAL!: vsx device roles are consistent”
cli show vsx status
!
nae-agent lite
#VSX Peer States NAE Lite
nae-agent lite
watch vsx_peer_state_down event-log 7011, 7012, 7014
watch vsx_peer_state_up event-log 7013
set-condition watch event-log vsx_peer_state_down include all “Config Sync
Status,”Out-Of-Sync”,”peer_unreachable”
status critical
syslog “!CRITICAL! severity alert: peer device state is down”
cli show vsx status
clear-condition watch event-log vsx_peer_state_up include all “Config Sync
Status”, ”In-Sync”,”peer_reachable”
syslog “!NORMAL!: Local and Peer devices are up”
cli show vsx status
!
nae-agent lite vsx_peer_states activate

vsx_device_roles activate

vsx_peer_states

VSF Monitoring

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

139

| #Interface            | Link | Status            | CLI       | Script |                 |     |     |     |     |
| --------------------- | ---- | ----------------- | --------- | ------ | --------------- | --- | --- | --- | --- |
| nae-agent             | lite | int_link_status_1 |           |        |                 |     |     |     |     |
| watch link_state_down |      |                   | event-log |        | 404             |     |     |     |     |
| watch link_state_up   |      |                   | event-log |        | 403             |     |     |     |     |
| set-condition         |      | watch             | event-log |        | link_state_down |     |     |     |     |
status critical
| syslog            | "Watch1: | Link                 | down!     | Major    | major         | major" | severity |            | alert |
| ----------------- | -------- | -------------------- | --------- | -------- | ------------- | ------ | -------- | ---------- | ----- |
| cli show          | vsf      | link \n              | show      | int      | br            |        |          |            |       |
| clear-condition   |          | watch                | event-log |          | link_state_up |        | include  | all        | "up"  |
| syslog            | "Watch1: | link                 | is        | up"      |               |        |          |            |       |
| nae-agent         | lite     | int_link_status_1    |           |          | activate      |        |          |            |       |
| #VSF Member       | Boot     | CLI                  | Script    |          |               |        |          |            |       |
| nae-agent         | lite     | test_vsf_member_boot |           |          |               |        |          |            |       |
| watch boot_member |          | event-log            |           | 706,9913 |               |        |          |            |       |
| watch member_up   |          | event-log            |           | 9901     |               |        |          |            |       |
| set-condition     |          | watch                | event-log |          | boot_member   |        | include  | any "boot" |       |
status critical
| syslog   | "Watch1: | Warning! |     | severity_warning: |     |     | member | is booting" |     |
| -------- | -------- | -------- | --- | ----------------- | --- | --- | ------ | ----------- | --- |
| cli show | vsf      |          |     |                   |     |     |        |             |     |
clear-condition watch event-log member_up include all "complete"
| syslog              | "Watch1: | Member               | is        | up"  |               |          |         |     |        |
| ------------------- | -------- | -------------------- | --------- | ---- | ------------- | -------- | ------- | --- | ------ |
| nae-agent           | lite     | test_vsf_member_boot |           |      |               | activate |         |     |        |
| #VSF Link           | Watch    | CLI                  | Script    |      |               |          |         |     |        |
| nae-agent           | lite     | vsf_link_watch       |           |      |               |          |         |     |        |
| watch vsf_link_down |          |                      | event-log |      | 9924          |          |         |     |        |
| watch vsf_link_up   |          | event-log            |           | 9923 |               |          |         |     |        |
| set-condition       |          | watch                | event-log |      | vsf_link_down |          | include | all | "down" |
status critical
| syslog | "Watch1: | Link | down! | Major | major | major" | severity |     | alert |
| ------ | -------- | ---- | ----- | ----- | ----- | ------ | -------- | --- | ----- |
cli show vsf link \n show vsf topology \n show vsf link error-detail
| clear-condition |          | watch          | event-log |        | vsf_link_up |     | include | all | "up" |
| --------------- | -------- | -------------- | --------- | ------ | ----------- | --- | ------- | --- | ---- |
| syslog          | "Watch1: | vsf            | link      | is up" |             |     |         |     |      |
| nae-agent       | lite     | vsf_link_watch |           |        | activate    |     |         |     |      |
LACP Monitoring
| # LACP          | NAE lite |           |     |      |     |     |     |     |     |
| --------------- | -------- | --------- | --- | ---- | --- | --- | --- | --- | --- |
| nae-agent       | lite     | LACP      |     |      |     |     |     |     |     |
| watch LACP_DOWN |          | event-log |     | 1321 |     |     |     |     |     |
| watch LACP_UP   |          | event-log |     | 1321 |     |     |     |     |     |
set-condition watch event-log LACP_DOWN include any "Actor state: ALFO","Partner
state ALFO"
status critical
| syslog   | "LACP | Interface  | is  | down" |     |     |     |     |     |
| -------- | ----- | ---------- | --- | ----- | --- | --- | --- | --- | --- |
| cli show | lacp  | interfaces |     |       |     |     |     |     |     |
clear-condition watch event-log LACP_UP include all "Actor state: ALFNCD","Partner
state ALFNCD"
| syslog   | "LACP | is BACK"   |     |     |     |     |     |     |     |
| -------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| cli show | lacp  | aggregates |     |     |     |     |     |     |     |
!
| nae-agent | lite | LACP | activate |     |     |     |     |     |     |
| --------- | ---- | ---- | -------- | --- | --- | --- | --- | --- | --- |
NetworkAnalyticsEngineLite|140

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
| switch(config)# |     | no nae cli-authorization |     |     |     |     |
| --------------- | --- | ------------------------ | --- | --- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command   | History     |         |                   |     |     |     |
| --------- | ----------- | ------- | ----------------- | --- | --- | --- |
| Release   |             |         | Modification      |     |     |     |
| 10.11     |             |         | Commandintroduced |     |     |     |
| Command   | Information |         |                   |     |     |     |
| Platforms | Command     | context | Authority         |     |     |     |
5420 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6200 |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --------------- | --- | --- | --- |
6300
6400
8100
141
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries)

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8320
8325
8325P
8360
8400
9300
9300S
10000
| show nae-agent |                |            |     |
| -------------- | -------------- | ---------- | --- |
| show nae-agent | [<AGENT-NAME>] | [vsx-peer] |     |
Description
ShowsthedetailsoftheNAEAgent.Iftheagentnameisspecified,thenshowstheinformationdetailsof
thespecifiedagent.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<AGENT-NAME> Specifiesthenameoftheagent.Length:3to80alphanumeric
characters,includingunderscore(_).
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
TheoutputofthiscommandshowsthefollowinginformationabouttheHPEArubaNetworking
NetworkAnalyticsEngineagentsthatareconfiguredandenabledontheswitch:
| Parameter  | Description                                     |     |     |
| ---------- | ----------------------------------------------- | --- | --- |
| AgentName  | Thenameoftheagent.Length:3through80characters.  |     |     |
| ScriptName | Thenameofthescript.Length:3through80characters. |     |     |
Example:memory_monitor
| Version | Theversionnumberofthescript. |     |     |
| ------- | ---------------------------- | --- | --- |
| Origin  | Theoriginofthescript:        |     |     |
n system:Indicatesthatthescriptisprovidedaspartofthesystemsoftware.
n user:Indicatesthatauserloadedthescript.
n generated:IndicatesthattheagentisconfiguredusingtheCLI.
Disabled Indicateswhethertheagentisdisabledorenabledontheswitch:
n true:Indicatesthattheagentisdisabled.
n false:Indicatesthattheagentisenabledontheswitch.
| Status | Thecurrentstateoftheagent.Statusvaluesarethefollowing: |     |     |
| ------ | ------------------------------------------------------ | --- | --- |
n CRITICAL:Theagenthasencounteredacriticalerrorduringexecution.Forinformation
NetworkAnalyticsEnginecommands|142

| Parameter | Description |     |     |     |     |
| --------- | ----------- | --- | --- | --- | --- |
abouttheerror,seetheAnalyticsDashboardoftheWebUI.
n MAJOR:Theagenthasencounteredamajorerrorduringexecution.Forinformationabout
theerror,seetheAnalyticsDashboardoftheWebUI.
n MINOR:Theagenthasencounteredaminorerrorduringexecution.Forinformationabout
theerror,seetheAnalyticsDashboardoftheWebUI.
n NORMAL:Indicatesthattheagentisactivelymonitoringnetworkconditionsandhandling
events.
| Timeseries | Numberoftimeseriesassociatedwithagent. |     |     |     |     |
| ---------- | -------------------------------------- | --- | --- | --- | --- |
count
| Alertscount  | Numberofalertsgeneratedbytheagent.             |     |     |     |     |
| ------------ | ---------------------------------------------- | --- | --- | --- | --- |
| Rules        | NumberofPrometheusrulesassociatedwiththeagent. |     |     |     |     |
| Error        | Currenterrorstateoftheagent.                   |     |     |     |     |
| Recentalerts | Liststherecentalerts.                          |     |     |     |     |
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
ShowingthedetailsoftheNAEagentnamedmemory_monitor:
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 143

| switch#           | show nae-agent |     | memory_monitor |          |
| ----------------- | -------------- | --- | -------------- | -------- |
| Script Name       |                | :   | memory_monitor |          |
| Version           |                | :   | 1.0            |          |
| Origin            |                | :   | generated      |          |
| Disabled          |                | :   | false          |          |
| Status            |                | :   | NORMAL         |          |
| Time Series       | Count          | :   | 0              |          |
| Alerts Count      |                | :   | 0              |          |
| Rules             |                | :   | 0              |          |
| Error             |                | :   | None           |          |
| Alert Description |                | :   | Memory         | - Normal |
| Recent alerts     |                | :   |                |          |
<1> 2021-05-29 01:34:11 An action has been triggered by NAE agent memory_monitor
<2> 2021-05-28 06:11:00 An action has been triggered by NAE agent memory_monitor
<3> 2021-05-27 03:19:50 An action has been triggered by NAE agent memory_monitor
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command History |     |     |     |              |
| --------------- | --- | --- | --- | ------------ |
| Release         |     |     |     | Modification |
10.13.1000 CommandoutputupdatedtodisplayAlertDescriptionforthe
agentname.
| 10.09               |         |     |         | Added<AGENT-NAME> |
| ------------------- | ------- | --- | ------- | ----------------- |
| 10.07orearlier      |         |     |         | --                |
| Command Information |         |     |         |                   |
| Platforms           | Command |     | context | Authority         |
5420 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --------------------- |
6300
6400
8100
8320
8325
8325P
8360
8400
9300
9300S
10000
| show nae-agent |                |     | alerts |        |
| -------------- | -------------- | --- | ------ | ------ |
| show nae-agent | [<AGENT-NAME>] |     |        | alerts |
ShowsthealertsraisedbyalltheNAEagents.Iftheagentnameisspecified,thenshowsthealerts
raisedbythespecifiedagent.
NetworkAnalyticsEnginecommands|144

| Parameter    |     |     | Description                         |
| ------------ | --- | --- | ----------------------------------- |
| <AGENT-NAME> |     |     | SpecifiesthenameoftheNAE-Liteagent. |
Example
ShowingthealertsraisedbyalltheNAEagents:
| switch# show | nae-agent | alerts |     |
| ------------ | --------- | ------ | --- |
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
| switch# show | nae-agent | memory_monitor | alerts |
| ------------ | --------- | -------------- | ------ |
2021-06-13 07:54:47 An action has been triggered by NAE agent memory_monitor
2021-06-13 07:53:56 An action has been triggered by NAE agent memory_monitor
2021-06-06 21:48:27 An action has been triggered by NAE agent memory_monitor
2021-06-03 07:45:36 An action has been triggered by NAE agent memory_monitor
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.09               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
5420 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6300
6400
8100
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 145

| Platforms |     |     | Command | context |     |     | Authority |     |     |     |     |
| --------- | --- | --- | ------- | ------- | --- | --- | --------- | --- | --- | --- | --- |
8320
8325
8325P
8360
8400
9300
9300S
10000
| show | nae-agent |     |                | alerts |        | details |         |                 |     |     |     |
| ---- | --------- | --- | -------------- | ------ | ------ | ------- | ------- | --------------- | --- | --- | --- |
| show | nae-agent |     | [<AGENT-NAME>] |        | alerts |         | details | [<INSTANCE-ID>] |     |     |     |
Description
ShowsthedetailedinformationofaspecificNAEagentalertraisedbyalltheNAEagents.
OnlyCLI,alert,andsystemlogspecificactiondetailsaredisplayedastheoutput.Forotheractiondetails,referto
theWebUI.
| Parameter    |     |     |     |     |     |     |     | Description                                   |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- |
| <AGENT-NAME> |     |     |     |     |     |     |     | SpecifiesthenameoftheNAE-Liteagent.Length:3to |     |     |     |
80alphanumericcharacters,includingunderscore(_).
<INSTANCE-ID>
Specifiestheinstanceofthealert.Number1
representsthelatestalertwhereasNrepresentsthe
Nthrecentalert.Bydefault,itdisplaysthelatestalert
(INSTANCE-ID=1).
Example
ShowingthedetailsoftherecentalertoftheNAE-Liteagentnamedmemory_monitor:
|     | switch# | show | nae-agent |     | memory_monitor |     | alerts | details | 1   |     |     |
| --- | ------- | ---- | --------- | --- | -------------- | --- | ------ | ------- | --- | --- | --- |
2Alert Message: 2021-06-13 07:54:47 An action has been triggered by NAE agent
memory_monitor
|     | Action(s) | performed: |     | Alert, |     | CLI, Syslog |     |     |     |     |     |
| --- | --------- | ---------- | --- | ------ | --- | ----------- | --- | --- | --- | --- | --- |
|     | Action    | Details:   |     |        |     |             |     |     |     |     |     |
===============
|     | Action    | Alert:  | Alert     | level | changed           |     | to MAJOR |          |     |     |     |
| --- | --------- | ------- | --------- | ----- | ----------------- | --- | -------- | -------- | --- | --- | --- |
|     | Action    | Syslog: | Potential |       | mis-configuration |     |          | detected |     |     |     |
|     | Action    | CLI:    |           |       |                   |     |          |          |     |     |     |
|     | 6405# top | cpu     |           |       |                   |     |          |          |     |     |     |
top - 07:54:27 up 25 min, 1 user, load average: 10.45, 10.38, 8.48
Tasks: 295 total, 1 running, 294 sleeping, 0 stopped, 0 zombie
%Cpu(s): 2.2 us, 2.2 sy, 0.0 ni, 95.7 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st
MiB Mem : 7555.6 total, 1982.1 free, 2022.6 used, 3550.9 buff/cache
|     | MiB Swap:    |       | 0.0   | total, |         | 0.0  | free, | 0.0    | used. | 5307.9 avail | Mem     |
| --- | ------------ | ----- | ----- | ------ | ------- | ---- | ----- | ------ | ----- | ------------ | ------- |
|     | PID          | USER  |       | PR NI  |         | VIRT | RES   | SHR S  | %CPU  | %MEM TIME+   | COMMAND |
|     | 27776        | admin |       | 20     | 0       | 3540 | 2128  | 1580 R | 16.7  | 0.0 0:00.04  |         |
|     | /usr/bin/top |       | -b -n | 2 -c   | -o %CPU | -w   | 11+   |        |       |              |         |
NetworkAnalyticsEnginecommands|146

|     | 1 root | 20  | 0 14272 | 9468 | 5260 S 0.0 | 0.1 0:03.23 | /sbin/init |
| --- | ------ | --- | ------- | ---- | ---------- | ----------- | ---------- |
|     | 2 root | 20  | 0       | 0 0  | 0 S 0.0    | 0.0 0:00.00 | [kthreadd] |
|     | 3 root |     | 0 -20   | 0 0  | 0 I 0.0    | 0.0 0:00.00 | [rcu_gp]   |
Only the action Alert, action Syslog, and action CLI details are displayed in this
command.
| Please | refer | to the | Web UI for | other action | details. |     |     |
| ------ | ----- | ------ | ---------- | ------------ | -------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command   | History     |         |         |                   |     |     |     |
| --------- | ----------- | ------- | ------- | ----------------- | --- | --- | --- |
| Release   |             |         |         | Modification      |     |     |     |
| 10.09     |             |         |         | Commandintroduced |     |     |     |
| Command   | Information |         |         |                   |     |     |     |
| Platforms |             | Command | context | Authority         |     |     |     |
5420 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     |     | rightsforthiscommand. |     |     |     |
| ---- | --- | --- | --- | --------------------- | --- | --- | --- |
6300
6400
8100
8320
8325
8325P
8360
8400
9300
9300S
10000
show nae-script
| show nae-script |     | [vsx-peer] |     |     |     |     |     |
| --------------- | --- | ---------- | --- | --- | --- | --- | --- |
Description
ShowsinformationabouttheHPEArubaNetworkingNetworkAnalyticsEnginescriptsthatareavailable
ontheswitch.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 147

ThiscommandshowsthefollowinginformationabouttheHPEArubaNetworkingNetworkAnalytics
Enginescriptsthatareavailableontheswitch:
Script Name
Thenameofthescript.Length:3through80characters.
Example:system_resource_monitor_mm1.default
Version
Theversionnumberofthescript.
Origin
Theoriginofthescript:
system
Indicatesthatthescriptisprovidedaspartofthesystemsoftware.
user
Indicatesthatauserloadedthescript.
Status
Thecurrentstateofthescript.Statusvaluesarethefollowing:
CREATED
Thescripthasbeenuploadedtotheswitch,butscriptvalidationhasnotbegun.
ERROR
Thescriptvalidationprocessdetectedanerrorthatwouldresultinexecutionerrorsifanagent
runsthescript.Resolvetheerrorbymodifyingthescript.Forinformationabouttheerror,seethe
Analytics DashboardoftheWebUI.
VALIDATING
Thescriptsyntaxandcomponents(manifest,parameters,monitor,condition,andaction)arein
theprocessofbeingvalidated.
VALIDATED
Thescriptsyntaxandcomponents(manifest,parameters,monitor,condition,andaction)have
beenvalidatedandnoerrorshavebeenfound.
Example
switch# show nae-script
---------------------------------------------------------------------
| Script Name | Version | Origin | Status |
| ----------- | ------- | ------ | ------ |
---------------------------------------------------------------------
| fan_monitor                         | 1.0 | system | VALIDATED |
| ----------------------------------- | --- | ------ | --------- |
| interface_link_flap_monitor         | 1.0 | system | VALIDATED |
| interface_link_state_monitor        | 1.0 | system | VALIDATED |
| interface_tx_rx_stats_monitor       | 1.0 | system | VALIDATED |
| lag_imbalance_monitor               | 1.0 | system | VALIDATED |
| lag_status_monitor                  | 1.0 | system | VALIDATED |
| power_supply_monitor                | 1.0 | system | VALIDATED |
| stp_bpdu_tcn_rate_monitor           | 1.0 | system | VALIDATED |
| system_resource_monitor_mm1.default | 1.0 | system | VALIDATED |
| system_resource_monitor_mm2.default | 1.0 | system | VALIDATED |
| temp_sensor_monitor                 | 1.0 | system | VALIDATED |
---------------------------------------------------------------------
| Script Name | Version | Origin | Status |
| ----------- | ------- | ------ | ------ |
---------------------------------------------------------------------
| fan_monitor                   | 1.0 | system | VALIDATED |
| ----------------------------- | --- | ------ | --------- |
| interface_link_flap_monitor   | 1.0 | system | VALIDATED |
| interface_link_state_monitor  | 1.0 | system | VALIDATED |
| interface_tx_rx_stats_monitor | 1.0 | system | VALIDATED |
| lag_imbalance_monitor         | 1.0 | system | VALIDATED |
NetworkAnalyticsEnginecommands|148

| lag_status_monitor                  |     |     | 1.0 | system | VALIDATED |
| ----------------------------------- | --- | --- | --- | ------ | --------- |
| power_supply_monitor                |     |     | 1.0 | system | VALIDATED |
| stp_bpdu_tcn_rate_monitor           |     |     | 1.0 | system | VALIDATED |
| system_resource_monitor_mm1.default |     |     | 1.0 | system | VALIDATED |
| system_resource_monitor_mm2.default |     |     | 1.0 | system | VALIDATED |
| temp_sensor_monitor                 |     |     | 1.0 | system | VALIDATED |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
5420 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |     |     |
| ---- | --- | --- | --------------------- | --- | --- |
6300
6400
8100
8320
8325
8325P
8360
8400
9300
9300S
10000
| uerieshow | running-config |     | (nae-lite) |     |     |
| --------- | -------------- | --- | ---------- | --- | --- |
show running-config
Description
ShowstheNAE-Literunningconfiguration.
Example
ShowingtheNAE-Lite runningconfiguration:
| switch# show           | running-config |     |     |     |     |
| ---------------------- | -------------- | --- | --- | --- | --- |
| Current configuration: |                |     |     |     |     |
!
!Version Halon 0.1.0 (Build: ridley-Halon-0.1.0-master-20161110190644-dev)
| !Schema version | 0.1.8  |     |     |     |     |
| --------------- | ------ | --- | --- | --- | --- |
| hostname        | switch |     |     |     |     |
...
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 149

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
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command   |     | History     |         |         |     |                   |     |     |     |
| --------- | --- | ----------- | ------- | ------- | --- | ----------------- | --- | --- | --- |
| Release   |     |             |         |         |     | Modification      |     |     |     |
| 10.09     |     |             |         |         |     | Commandintroduced |     |     |     |
| Command   |     | Information |         |         |     |                   |     |     |     |
| Platforms |     |             | Command | context |     | Authority         |     |     |     |
5420 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     |     |     |     | rightsforthiscommand. |     |     |     |
| ---- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
6300
6400
8100
8320
8325
8325P
8360
8400
9300
9300S
10000
| Network |     |            | Analytics |     | Engine |     | Lite | commands |     |
| ------- | --- | ---------- | --------- | --- | ------ | --- | ---- | -------- | --- |
| actions |     | (NAE-Lite) |           |     |        |     |      |          |     |
NetworkAnalyticsEngineLitecommands|150

| status    | {normal | | minor | | major | | critical} |
| --------- | ------- | ------- | ------- | ----------- |
| no status | {normal | | minor | | major | | critical} |
syslog <MESSAGE> [facility {kern | user | mail | daemon | auth | syslog |
| lpr | | uucp | | authpriv | | cron | | ftp}] |
| --- | ------ | ---------- | ------ | ------- |
[severity {debug | info | notice | warning | err | crit | alert | emer}]
no syslog <MESSAGE> [facility {kern | user | mail | daemon | auth | syslog |
| lpr | | uucp | | authpriv | | cron | | ftp}] |
| --- | ------ | ---------- | ------ | ------- |
[severity {debug | info | notice | warning | err | crit | alert | emer}]
cli <COMMAND> {show system | redirect local-file} {show version | redirect tftp}
no cli <COMMAND>
| schedule    | <SCHEDULE> |            |     |     |
| ----------- | ---------- | ---------- | --- | --- |
| no schedule |            | <SCHEDULE> |     |     |
trap <TRAP>
| no trap | <TRAP> |     |     |     |
| ------- | ------ | --- | --- | --- |
Description
ConfiguresdifferentNAE-Liteagentactionstobeperformedwhenthesetconditionortheclear
conditionismet.ThefollowingNAEactionscanbeconfiguredforthesetandclearcondition:
status—SetthealertlevelfortheNAE-LiteAgent.
syslog—Createasyslogmessageandsendittotheconfiguredremotesyslogservers.
cli—ExecuteaCLIcommand.MultipleCLIcommandscanbespecifiedbyusing\nasthedelimiter.
schedule—ExecuteaconfiguredjobCLIcommandsatthespecifictime.
trap—Createasnmptrapmessageandsendittotheconfiguredsnmpservers.
| redirect | local-file—Storeoutputinthelocalfile. |                                                  |     |     |
| -------- | ------------------------------------- | ------------------------------------------------ | --- | --- |
| redirect | {tftp                                 | | sftp | scp}—Copytheoutputtoaremotedestination. |     |     |
redirect tftp://<IP>/file%Date%.txt—Appendthedate,time,andhostnameofthefile.
ThenoformofthiscommandremovestheactionsassociatedwiththeNAE-Liteagentcondition.
Parameter Description
normal SetstheNAE-Liteagentstatustonormal(default).
minor
SetstheNAE-Liteagentstatustominor.
major SetstheNAE-Liteagentstatustomajor.
critical
SetstheNAE-Liteagentstatustocritical.
<MESSAGE> Specifiesthesyslogmessagetobesentwhentheset
conditionortheclearconditionismet.Length:3to255
characters.
facility {kern | user | mail | Specifiesthesyslogfacilitycodetodenotethetypeof
daemon | auth | syslog | programthatisloggingthemessage.Thedefaultfacility
lpr | uucp | authpriv | cron | ftp} codeisdaemon.Optional.Thevalidfacilitycodevalues
are:
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 151

Parameter

Description

n kern: Sets the syslog message source as kernel.
n user: Sets the syslog message source as user space

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
n info: Sets the syslog severity as information (default).
n notice: Sets the syslog severity as notice.
n warning: Sets the syslog severity as warning.
n err: Sets the syslog severity as error.
n crit: Sets the syslog severity as critical.
n alert: Sets the syslog severity as alert.
n emer: Sets the syslog severity as emergency.

<COMMAND>

Specifies the CLI command to be executed when the set
condition or the clear condition is met.

{show system | redirect local-file}

Specifies where to relocate local-file.

{show version | redirect tftp}

Specifies where to relocate tftp.

Usage

Take note of the following requirements and recommendations:

n Syslog messages should be a minimum of 3 to a maximum of 255 characters. Syslog facility code can
be specified to denote the type of program that is logging the message. Remote syslog server could
use this facility to separate the syslogs into separate log buffers. Default facility code is `daemon`.
Syslog severity can be used to denote the severity of the syslog message. Default severity is `info`.

n SNMP trap messages should be a minimum of 3 and a maximum of 255 characters.

n Add the job configuration separately in the configuration node and execute the corresponding job

name in the action schedule CLI.

Network Analytics Engine Lite commands | 152

n It is not recommended to use NAE-lite action schedule CLI commands in the NAE-lite action CLI.

n It is not recommended to add the job configuration CLI and schedule configuration CLI together in

the action schedule CLI.

n Using action schedule CLI, the NAE-lite agent should load the recommended configuration from a

specified location(remote destination) to the switch. The action schedule executes the pre-configured
job CLI, which executes a copy of the default config to running-config. Only TFTP is allowed for the
job CLI execution.

NAE-Lite Action CLI Execution for SFTP/SCP

n SFTP/SCP transfer method is used to securely copy files from switch to remote server and requires a

password.

n NAE-Lite agent CLI execution is not a user-interactive command and password prompt is not allowed

to copy the file. Use SSH key-based authentication to copy the file from switch to a remote
destination.

n Before executing NAE-Lite action CLI for SFTP/SCP transfer methods, specify the remote-server user
information using CLI 'remote-server user USERNAME password (plaintext|ciphertext) PASSWORD
[host WORD]'.

It is recommended to use secure-prompt and Ciphertext options as these are more secure. The plaintext option

does not hide the password in the CLI.

The following steps are internal workflow for NAE-lite action CLI execution for SFTP/SCP:

1. The `remote-server user USERNAME password (plaintext|ciphertext) PASSWORD [host WORD]`
CLI is used to store the remote username, password and hostname(optional) in the OVSDB and
generate an SSH Key on the Switch. The generated `id_rsa` and `id_rsa.pub` SSH keys are stored
in the `/fs/nos/` file system.

2. During the execution of action CLI, read the remote username and password from the OVSDB

using sshpass establish the connection between switch and remote server.

3. Copy the public key to the remote server.

4. Copy the action CLI output file from switch to a remote destination.

Please note the following:

1. The usage of the public key with the SFTP/SCP client implies that there will only be one key.

2. This will not work with users authenticating with AAA, enhanced secure mode, and RADIUS

authentication.

3.

In HA scenarios, the public key will be synced between Active and Standby Modules.

4. The remote username and password should not be deleted from the OVSDB during the execution

of NAE-lite action CLI.

5. The SSH public key, should not be deleted from the file system during the execution of NAE-lite

Action CLI.

6. During the execution of NAE-lite action CLI, the output file will be copied to the remote
destination only for the matched remote user information specified in the OVSDB.

7. Multiple remote servers are not allowed. If the user updates the new remote server

configuration, it will overwrite the existing remote server from the OVSDB.

Examples

Setting the status level for the NAE-Lite agent condition:

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

153

| switch(config-nae-agent-condition)# | status | major |
| ----------------------------------- | ------ | ----- |
CreatingthesyslogmessagefortheNAE-Liteagentcondition:
switch(config-nae-agent-condition)# syslog "IPSLA server1 is down" severity err
ExecutingtheCLIcommandfortheNAE-Liteagentcondition:
switch(config-nae-agent-condition)# cli show version\nshow image
RemovingthedifferentactionsassociatedwiththeNAE-Liteagentcondition:
| switch(config-nae-agent-condition)# | no status | minor |
| ----------------------------------- | --------- | ----- |
switch(config-nae-agent-condition)# no syslog "Processing system event"
| switch(config-nae-agent-condition)# | no cli | show logging |
| ----------------------------------- | ------ | ------------ |
ExecutingthescheduleCLI command:
| switch(config-nae-agent-condition)# | schedule |     |
| ----------------------------------- | -------- | --- |
SCHEDULE Set the job schedule CLI command. The CLI commands can be specified by
using `\n` as the separator.
ExampleofascheduledCLI Command:
switch(config-nae-agent-condition)# schedule s1\n10 job j1\ntrigger every minutes
30 start 17:20 2023-11-21
Exampleofatrapmessage:
switch(config-nae-agent-condition)# trap High system CPU utilization
RemovingthescheduledCLI command:
| switch(config-nae-agent)# no schedule |     |     |
| ------------------------------------- | --- | --- |
Removingsnmptrapmessage:
| switch(config-nae-agent)# no trap |     |     |
| --------------------------------- | --- | --- |
UserconfiguredNAE-LiteagentCLIwithdateformat:
NetworkAnalyticsEngineLitecommands|154

| nae-agent     | lite  | event_crash |           |     |       |     |
| ------------- | ----- | ----------- | --------- | --- | ----- | --- |
| watch         | crash | event-log   | 1201      |     |       |     |
| set-condition |       | watch       | event-log |     | crash |     |
status minor
|     | syslog | "crash       | triggered | run      | to start"                      |     |
| --- | ------ | ------------ | --------- | -------- | ------------------------------ | --- |
|     | cli    | show version | |         | redirect | tftp://10.0.0.2/file%Date%.txt |     |
!
| nae-agent | lite | event_crash |     | activate |     |     |
| --------- | ---- | ----------- | --- | -------- | --- | --- |
Running-configforaboveNAE-agent:
| nae-agent     | lite  | event_crash |           |     |       |     |
| ------------- | ----- | ----------- | --------- | --- | ----- | --- |
| watch         | crash | event-log   | 1201      |     |       |     |
| set-condition |       | watch       | event-log |     | crash |     |
status minor
|     | syslog | "crash | triggered | run | to start" |     |
| --- | ------ | ------ | --------- | --- | --------- | --- |
cli show version | redirect tftp://10.0.0.2/file_2024-05-16_101230_
6300.txt
!
| nae-agent | lite | event_crash |     | activate |     |     |
| --------- | ---- | ----------- | --- | -------- | --- | --- |
NAE-Liteagentloadrecommendedconfigurationusingactionschedule:
job j1
| 10            | cli copy  | tftp://10.0.0.2/run_cfg.txt |           |      |           | running-config |
| ------------- | --------- | --------------------------- | --------- | ---- | --------- | -------------- |
| nae-agent     | lite      | switch_boot_up              |           |      |           |                |
| watch         | switch_up |                             | event-log | 4311 |           |                |
| set-condition |           | watch                       | event-log |      | switch_up |                |
status major
syslog "switch is up and load recommended configuration from a specified
location."
schedule config\nschedule s1\n10 job j1\ntrigger every minutes 30 start
12:30 2024-05-16
!
| nae-agent | lite | switch_boot_up |     | activate |     |     |
| --------- | ---- | -------------- | --- | -------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command | History     |     |     |     |                                   |     |
| ------- | ----------- | --- | --- | --- | --------------------------------- | --- |
| Release |             |     |     |     | Modification                      |     |
| 10.15   |             |     |     |     | AddedsupportforTFTP/SFTP/SCP.     |     |
| 10.14   |             |     |     |     | ScheduleandTrapactionsintroduced. |     |
| 10.09   |             |     |     |     | Commandintroduced                 |     |
| Command | Information |     |     |     |                                   |     |
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 155

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
5420 config-nae-agent- Administratorsorlocalusergroupmemberswithexecution
| 6200 | condition |     | rightsforthiscommand. |     |
| ---- | --------- | --- | --------------------- | --- |
6300
6400
8320
8325
8325P
8360
8400
9300
9300S
10000
desc
desc <DESCRIPTION>
no desc <DESCRIPTION>
Description
AddsthedescriptionfortheNAE-Liteagent.
ThenoformofthiscommandremovesthedescriptionfromtheNAE-Liteagent.
| Parameter |     |               |     | Description                                 |
| --------- | --- | ------------- | --- | ------------------------------------------- |
|           |     | <DESCRIPTION> |     | SpecifiesthedescriptionfortheNAE-Liteagent. |
Range:3to255characters
Example
AddingthedescriptionfortheNAE-Lite agent:
| switch(config-nae-agent)# |     | desc | Monitor | system memory |
| ------------------------- | --- | ---- | ------- | ------------- |
RemovingthedescriptionfortheNAE-Lite agent:
| switch(config-nae-agent)# |     | no desc | Monitor | system memory |
| ------------------------- | --- | ------- | ------- | ------------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command History     |     |     |                   |     |
| ------------------- | --- | --- | ----------------- | --- |
| Release             |     |     | Modification      |     |
| 10.09               |     |     | Commandintroduced |     |
| Command Information |     |     |                   |     |
NetworkAnalyticsEngineLitecommands|156

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
5420 config-nae-agent Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6300
6400
8100
8320
8325
8325P
8360
8400
9300
9300S
10000
disable
disable
no disable
Description
DisablestheNAE-liteagent.TheNAE-Liteagentsareenabledbydefault.
ThenoformofthiscommandenablestheNAE-Liteagent.
Example
DisablingtheNAE-Liteagent:
| switch(config-nae-agent)# |     | disable |     |
| ------------------------- | --- | ------- | --- |
EnablingtheNAE-Liteagent:
| switch(config-nae-agent)# |     | no disable |     |
| ------------------------- | --- | ---------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.09               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
5420 config-nae-agent Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
6200
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 157

| Platforms |     | Command |     | context | Authority |     |     |
| --------- | --- | ------- | --- | ------- | --------- | --- | --- |
6300
6400
8100
8320
8325
8325P
8360
8400
9300
9300S
10000
| monitor |     | resource |     |     |     |     |     |
| ------- | --- | -------- | --- | --- | --- | --- | --- |
monitor <MONITOR-NAME> resource <RESOURCE> [group-by {count | sum | min | max | average}
| [over | {seconds | |   | minutes | | hours | | days} <DURATION>]] |     |     |
| ----- | -------- | --- | ------- | ------- | -------------------- | --- | --- |
no monitor <MONITOR-NAME> resource <RESOURCE> [group-by {count | sum | min | max |
| average} | [over | {seconds |     | | minutes | | hours | days} | <DURATION>]] |     |
| -------- | ----- | -------- | --- | --------- | --------------- | ------------ | --- |
monitor <MONITOR-NAME> resource <RESOURCE> group-by rate over {seconds | minutes | hours
| | days} | <DURATION> |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- |
no monitor <MONITOR-NAME> resource <RESOURCE> group-by rate over {seconds | minutes |
| hours | | days} | <DURATION> |     |     |     |     |     |
| ----- | ------- | ---------- | --- | --- | --- | --- | --- |
Description
ConfiguresthemonitorfortheNAE-Liteagent.Themonitordefineswhatsystemresourcetheagent
mustmonitor.Monitorsaredefinedusingthetimeseriesfunctionanditsupportsthegroupingofdata.
ThenoformofthiscommandremovesthemonitorassociatedwiththeNAE-Liteagent.Before
removingthemonitor,youmustremovetheconditionusedinthemonitor.
| Parameter      |     |     |     |     |     |     | Description                   |
| -------------- | --- | --- | --- | --- | --- | --- | ----------------------------- |
| <MONITOR-NAME> |     |     |     |     |     |     | Specifiesthenameofthemonitor. |
Length:3to80alphanumeric
characters,includingunderscore
(_).
| <RESOURCE> |     |     |     |     |     |     | Specifiesthesystemresources |
| ---------- | --- | --- | --- | --- | --- | --- | --------------------------- |
suchasmemory,CPU,andstorage
The<RESOURCE>isdefinedasfollows:
utilizationforspecificmodulesthat
n  For5420,8400and6400SwitchSeries: needtobemonitored.Valuesare:
o system {cpu | memory} {management-module | n cpu:ConfigurestheCPU
|     | line-module} |     | <SLOT-ID> |     |     |     | monitoring. |
| --- | ------------ | --- | --------- | --- | --- | --- | ----------- |
n memory:Configuresthe
|     | o system | storage | {nos | | security | |   |     |     |
| --- | -------- | ------- | ---- | ---------- | --- | --- | --- |
memorymonitoring.
|     | coredump          | |       | logs     | | selftest} |     |     | n storage:Configuresthestorage |
| --- | ----------------- | ------- | -------- | ----------- | --- | --- | ------------------------------ |
|     | management-module |         |          | <SLOT-ID>   |     |     | utilizationmonitoring.         |
|     | system            | storage | coredump | line-module |     |     | n management-module:           |
o
Monitorsresourcesofthe
<SLOT-ID>
managementmodule.
For6300and6200SwitchSeries:
n
n line-module:Monitors
o system {cpu | memory} vsf member <MEMBER-ID> resourcesofthelinemodule.
NetworkAnalyticsEngineLitecommands|158

Parameter

Description

o system storage {nos | security | coredump |

logs | selftest} vsf member <MEMBER-ID>

n nos: Monitors the network

operating system storage

n For 8100, 8320, 8325, 8325H, 8325P, 8360, and 9300/9300S Switch

utilization.

Series:

o system {cpu | memory}

o system storage {nos | security | coredump |

logs | selftest}

group-by {count | sum | min | max | average}

over {seconds | minutes | hours | days} <DURATION>

n security: Monitors the security

storage utilization.

n coredump: Monitors the

coredump storage utilization.
n logs: Monitors the log storage

utilization.

n selftest: Monitors the self-test

storage utilization.

n <SLOT-ID>: Configure the

module slot ID. <SLOT-ID> is

the mandatory parameter for

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
current value. Values are:
seconds: Sets the time interval in
seconds. Range: 5 to 10000
minutes: Sets the time interval in
minutes. Range: 1 to 10000.
hours: Sets the time interval in
hours. Range: 1 to 10000.
days: Sets the time interval in days.
Range: 1 to 365.

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

159

| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
rate over {seconds | minutes | hours | days} <DURATION> Groupsbyrateofchangeofthe
monitoreddataoverthespecified
timeinterval.
Example
Configuringthemonitorforthesystem cpuresourceonthe1/1module(5420,8400and6400Switch
Series):
switch(config-nae-agent)# monitor sys_cpu resource system cpu management-module
1/1
ConfiguringthemonitorforthecalculatingtheaverageCPUusageoverthe30minutes(5420,8400and
6400SwitchSeries):
switch(config-nae-agent)# monitor avg_sys_cpu resource system cpu line-module 1/4
| group-by average | over minutes | 30  |     |     |     |
| ---------------- | ------------ | --- | --- | --- | --- |
ConfiguringthemonitorforthesystemCPUusageonthevsf member 1(6300and6200SwitchSeries):
switch(config-nae-agent)# monitor sys_cpu resource system cpu vsf member 1
ConfiguringthemonitorforthesystemCPUusage:
switch(config-nae-agent)#
|     |     | monitor | sys_cpu resource | system | cpu |
| --- | --- | ------- | ---------------- | ------ | --- |
ConfiguringthemonitorforcalculatingtheaverageCPUusageoverthe30minutesduration(8100,
8320,8325,8325H,8325P,8360,and9300/9300SSwitchSeries):
| switch(config-nae-agent) |     | #       |             |          |                     |
| ------------------------ | --- | ------- | ----------- | -------- | ------------------- |
|                          |     | monitor | avg_sys_cpu | resource | system cpu group-by |
| average over minutes     | 30  |         |             |          |                     |
Removingthemonitornamedsys_mem:
| switch(config-nae-agent)# |     | no monitor | sys_mem |     |     |
| ------------------------- | --- | ---------- | ------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
Command History
NetworkAnalyticsEngineLitecommands|160

| Release             |         |         | Modification      |
| ------------------- | ------- | ------- | ----------------- |
| 10.09               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
config-nae-agent Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
5420
6200
6300
6400
8320
8325
8325H
8325P
8360
8400
9300
9300S
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
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 161

RemovingalltheNAE-Liteagentconfigurations:
| switch(config)# |     | no  | nae-agent | lite |     |
| --------------- | --- | --- | --------- | ---- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command   | History     |         |         |     |                   |
| --------- | ----------- | ------- | ------- | --- | ----------------- |
| Release   |             |         |         |     | Modification      |
| 10.09     |             |         |         |     | Commandintroduced |
| Command   | Information |         |         |     |                   |
| Platforms |             | Command | context |     | Authority         |
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --- | --------------------- |
6300
6400
8100
8320
8325
8325P
8360
8400
9300
9300S
10000
| nae-agent    |      | lite activate     |     |          |     |
| ------------ | ---- | ----------------- | --- | -------- | --- |
| nae-agent    | lite | <AGENT-NAME>      |     | activate |     |
| no nae-agent |      | lite <AGENT-NAME> |     | activate |     |
Description
ActivatestheNAE-Liteagentcreation.Onceactivated,theNAE-Liteagentgetsgenerated,validated,and
beginsmonitoring.
WhenevermodifyingtheNAE-Liteagentconfiguration,afterallthemodificationsaredone,youmust
triggertheagentupdateprocessbyexecutingno nae-agent lite <AGENT-NAME> activatefollowedby
nae-agent lite <AGENT-NAME> activate.Theagentwillnotbecreatedorupdateduntilthenae-agent
| lite <AGENT-NAME> |     | activatecommandisexecuted. |     |     |     |
| ----------------- | --- | -------------------------- | --- | --- | --- |
ThenoformofthecommanddeactivatestheNAE-Liteagent.Oncethecommandisexecuted,theNAE-
Liteagentanditscorrespondingscriptwillbedeleted.
| Parameter    |     |     |     |     | Description                                     |
| ------------ | --- | --- | --- | --- | ----------------------------------------------- |
| <AGENT-NAME> |     |     |     |     | SpecifiesthenameoftheNAE-Liteagent.Length:3to80 |
alphanumericcharacters,includingunderscore(_).
NetworkAnalyticsEngineLitecommands|162

Example
ActivatingtheNAE-Liteagentnamedcrash_watch:
switch(config)#
|     | nae-agent |     | lite crash_watch | activate |
| --- | --------- | --- | ---------------- | -------- |
DeactivatingtheNAE-Liteagentnamedmem_monitor:
| switch(config)# | no  | nae-agent | lite mem_monitor | activate |
| --------------- | --- | --------- | ---------------- | -------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command History     |         |         |                   |     |
| ------------------- | ------- | ------- | ----------------- | --- |
| Release             |         |         | Modification      |     |
| 10.09               |         |         | Commandintroduced |     |
| Command Information |         |         |                   |     |
| Platforms           | Command | context | Authority         |     |
5420 config Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
6300
6400
8100
8320
8325
8325P
8360
8400
9300
9300S
10000
| 2set-condition |     | monitor |     |     |
| -------------- | --- | ------- | --- | --- |
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
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 163

Defines the condition for the monitor resource events. Once the condition is met, one or more actions
are executed based on the configuration.

The clear condition is an optional component of the condition and helps in identifying if an event,
usually an issue in the system, is no longer occurring. Clear conditions also address the problem when
data is fluctuating above and below the threshold, generating too many alerts. Initially, when an NAE-
Lite agent is created, only the set-condition is active. Once the set-condition is met, the condition
becomes inactive and the clear condition becomes active. The set-condition becomes active again once
the clear condition is met.

The no form of this command removes the monitor condition associated with the NAE-Lite agent.

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

Network Analytics Engine Lite commands | 164

switch(config-nae-agent)# no set-condition monitor line_mdl_state transition from
| "ready" to | "down","error" |     |     |
| ---------- | -------------- | --- | --- |
switch(config-nae-agent-condition)# no clear-condition monitor cpu lt 30 for
| minutes 30 |     |     |     |
| ---------- | --- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.09               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
config-nae-agent Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| 5420 | config-nae-agent- |     |     |
| ---- | ----------------- | --- | --- |
condition
6200
6300
6400
8320
8325
8325H
8325P
8360
8400
9300
9300S
10000
| 5set-condition |     | watch |     |
| -------------- | --- | ----- | --- |
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
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 165

fluctuating above and below the threshold, and generating too many alerts. Initially, when an NAE-Lite
agent is created, only the set-condition is active. Once the set-condition is met, the condition becomes
inactive and the clear condition becomes active. The set-condition becomes active again once the clear
condition is met.

The condition is met when any of the event logs watched by the <WATCH-NAME> has occurred and the
event log message fits the include or exclude <REGEX-LIST> (if configured) and the condition has
occurred for <COUNT> number of times (if configured).

The no form of this command removes the condition associated with the NAE-Lite agent.

Parameter

<WATCH-NAME>

Description

Specifies the name of the watch. This must be already defined
using the watch command.

include {all | any} <REGEX-LIST>

Configures the list of strings matching the regular expression
that must be included in the event log message. Optional.

all

any

<REGEX-LIST>

exclude

count <COUNT>

Includes all of the specified lists of regular expressions in event-
log messages.

Includes any of the specified lists of regular expressions in event-
log messages

Specifies the comma-separated list of one or more regular
expressions that must be matched against the event log
messages. Optional.

Configures the list of strings matching the regular expression
that must be included in the event log message. Optional.

Limits the number of times that the condition to be met
once in every specified count. Optional. For example, if
you want to monitor mac movement in the VLAN for every
10th time, then the count must be specified as 10.

Range: 1 to 4294967295.

Example

Defining the condition for the watch named ipsla_status including all the specified list:

switch(config-nae-agent)# set-condition watch event-log ipsla_status
include all "servername","failure" count 3

Clearing the condition for the watch named ipsla_status including all the specified list:

switch(config-nae-agent-condition)# clear-condition watch ipsla_status
include all "servername","success"

Defining the condition for the watch named ipsla_status excluding snmpd:

Network Analytics Engine Lite commands | 166

switch(config-nae-agent-condition)# set-condition watch event-log crash_event
| exclude snmpd |     |     |     |
| ------------- | --- | --- | --- |
RemovingtheconditionsassociatedwiththeNAE-Liteagent:
switch(config-nae-agent)# no set-condition watch event-log ipsla_status include
all "servername","failure"
switch(config-nae-agent-condition)# no clear-condition watch ipsla_status
| include all | "servername","success" |     |     |
| ----------- | ---------------------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.09               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
config-nae-agent Administratorsorlocalusergroupmemberswithexecution
|     | config-nae-agent- |     | rightsforthiscommand. |
| --- | ----------------- | --- | --------------------- |
5420
| 6200 | condition |     |     |
| ---- | --------- | --- | --- |
6300
6400
8320
8325
8325P
8360
8400
9300
9300S
10000
| show running-config |           | nae-agent |     |
| ------------------- | --------- | --------- | --- |
| show running-config | nae-agent |           |     |
Description
ShowstheNAE-Liteagentcurrentrunningconfigurations.
Example
ShowingtheNAE-Lite runningconfigurations:
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 167

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
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command   |     | History     |         |         |     |                   |     |     |     |
| --------- | --- | ----------- | ------- | ------- | --- | ----------------- | --- | --- | --- |
| Release   |     |             |         |         |     | Modification      |     |     |     |
| 10.09     |     |             |         |         |     | Commandintroduced |     |     |     |
| Command   |     | Information |         |         |     |                   |     |     |     |
| Platforms |     |             | Command | context |     | Authority         |     |     |     |
5420 Manager(#) Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     |     |     |     | rightsforthiscommand. |     |     |     |
| ---- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
6300
6400
8100
8320
8325
8325P
8360
8400
9300
9300S
10000
tags
NetworkAnalyticsEngineLitecommands|168

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
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.09               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
5420 config-nae-agent Administratorsorlocalusergroupmemberswithexecution
| 6200 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
6300
6400
8100
8320
8325
8325P
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 169

| Platforms | Command |     | context | Authority |     |     |
| --------- | ------- | --- | ------- | --------- | --- | --- |
8360
8400
9300
9300S
10000
| watch event-log       |     |           |                 |     |     |     |
| --------------------- | --- | --------- | --------------- | --- | --- | --- |
| watch <WATCH-NAME>    |     | event-log | <EVENT-ID-LIST> |     |     |     |
| no watch <WATCH-NAME> |     | event-log | <EVENT-ID-LIST> |     |     |     |
Description
ConfiguresthewatchsourcefortheNAE-Liteagent.Thisenablestheagenttowatchforspecificevents
occurringinthesystem.Event-drivenmonitoringcanbeperformedbywatchingtheeventlogofthe
system.
ForinformationoneventIDs,refertotheEventLogMessageReferenceGuide.
ThenoformofthiscommandremovesthewatchassociatedwiththeNAE-Liteagent.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<WATCH-NAME> SpecifiesthewatchnamefortheNAE-Liteagent.Length:3to80
alphanumericcharacters,includingunderscore(_).
<EVENT-ID-LIST> SpecifiesthelistofoneormoreeventIDsoftheeventlog
message.AmaximumoffiveeventIDscanbespecified.
Example
ConfiguringthewatchsourcefortheNAE-Liteagent.
| switch(config-nae-agent)# |     |     | watch | crash_event | event-log | 1201 |
| ------------------------- | --- | --- | ----- | ----------- | --------- | ---- |
RemovingthewatchsourceusedbytheNAE-Lite agent:
| switch(config-nae-agent)# |     |     | no watch | high_mem |     |     |
| ------------------------- | --- | --- | -------- | -------- | --- | --- |
switch(config-nae-agent)# no watch high_mem_event event-log 1208,1209
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideforyour
switchmodel.
| Command History |     |     |     |                   |     |     |
| --------------- | --- | --- | --- | ----------------- | --- | --- |
| Release         |     |     |     | Modification      |     |     |
| 10.09           |     |     |     | Commandintroduced |     |     |
NetworkAnalyticsEngineLitecommands|170

Command Information

Platforms

Command context

Authority

config-nae-agent

Administrators or local user group members with execution
rights for this command.

5420
6200
6300
6400
8100
8320
8325
8325P
8360
8400
9300
9300S
10000

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

171

Chapter 15

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

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

172

| Release   |             |     |         |     | Modification       |     |
| --------- | ----------- | --- | ------- | --- | ------------------ | --- |
| 10.11     |             |     |         |     | Commandintroduced. |     |
| Command   | Information |     |         |     |                    |     |
| Platforms | Command     |     | context |     | Authority          |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| https-server |                | authentication |     |          | password |     |
| ------------ | -------------- | -------------- | --- | -------- | -------- | --- |
| https-server | authentication |                |     | password |          |     |
Description
Enablesauthenticationusingusernameandpassword,whichcorrespondstothedefaultauthentication
mechanism.Enablingthepasswordauthenticationmodedisablesthecertificateauthenticationmode.
Onlyoneauthenticationmethodcanbeenabledatatime.
Example
Enablingauthenticationusingthepassword:
| switch(config)# |             | https-server |         | authentication |                                                    | password |
| --------------- | ----------- | ------------ | ------- | -------------- | -------------------------------------------------- | -------- |
| Command         | History     |              |         |                |                                                    |          |
| Release         |             |              |         |                | Modification                                       |          |
| 10.11           |             |              |         |                | Commandintroduced.                                 |          |
| Command         | Information |              |         |                |                                                    |          |
| Platforms       | Command     |              | context |                | Authority                                          |          |
|                 |             | config       |         |                | Administratorsorlocalusergroupmemberswithexecution |          |
Allplatforms
rightsforthiscommand.
| https-server |                   | max-user-sessions |     |               |     |     |
| ------------ | ----------------- | ----------------- | --- | ------------- | --- | --- |
| https-server | max-user-sessions |                   |     | <SESSION-AMT> |     |     |
Description
SetsthemaximumamountofconcurrentopensessionsforanygivenuserthroughtheHTTPSserver.
Theamountofconcurrentopensessionsmayhaveanimpactonsystemperformance,soitis
recommendedtosetthisvaluetotheminimumnecessary.
HTTPSservercommands|173

| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<SESSION-AMT> Specifiesthemaximumnumberofusersessionsallowed.
Default: 6.Maximumvalue: 8.
Example
Setthemaximumnumberofconcurrentusersessionstothemaximumof8:
| switch(config)# |     | https-server |     | max-user-sessions |     | 8   |
| --------------- | --- | ------------ | --- | ----------------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideorthe
RESTAPIGuideforyourswitchmodel.
| Command   | History     |     |         |                   |           |     |
| --------- | ----------- | --- | ------- | ----------------- | --------- | --- |
| Release   |             |     |         | Modification      |           |     |
| 10.08     |             |     |         | Commandintroduced |           |     |
| Command   | Information |     |         |                   |           |     |
| Platforms | Command     |     | context |                   | Authority |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| https-server |      | rest        | access-mode |            |               |     |
| ------------ | ---- | ----------- | ----------- | ---------- | ------------- | --- |
| https-server | rest | access-mode |             | {read-only | | read-write} |     |
Description
ChangestheRESTAPIaccessmode.Thedefaultmodeisread-write.Thiscommanddoesnotaffect
Centralconnections,whichhavepermissiontoalterconfigurationsregardlessoftheaccessmodeset
ontheswitch.
| Parameter  |     |     |     | Description                                       |     |     |
| ---------- | --- | --- | --- | ------------------------------------------------- | --- | --- |
| read-write |     |     |     | Selectstheread/writemode.AllowsPOST,PUT,PATCH,and |     |     |
DELETEmethodstobecalledonallconfigurableelementsinthe
switchdatabase.
read-only Selectstheread-onlymode.Writeaccesstomostswitchresources
throughtheRESTAPIisdisabled.
Usage
Settingthemodetoread-writeontheRESTAPIallowsPOST,PUT,PATCH,andDELETEmethodstobe
calledonallconfigurableelementsintheswitchdatabase.
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 174

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
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideorthe
RESTAPIGuideforyourswitchmodel.
| Command        | History     |     |         |     |              |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| Release        |             |     |         |     | Modification |     |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| https-server |         | session |     | close | all |     |
| ------------ | ------- | ------- | --- | ----- | --- | --- |
| https-server | session | close   | all |       |     |     |
Description
InvalidatesandclosesallHTTPSsessions.AllexistingWebUIsessions(includingsessionsusedfor
Centralconnections)willbeloggedout.RESTandWebUIuserswillhavetoreauthenticate.andallreal-
timenotificationfeatureWebSocketconnectionsareclosedandmustberesubscribed.
Usage
Typically,auserthathasconsumedtheallowedconcurrentHTTPSsessionsandisunabletoaccessthe
sessioncookietologoutmanuallymustwaitforthesessionidletimeouttostartanothersession.This
HTTPSservercommands|175

commandisintendedasaworkaroundtowaitingfortheidletimeouttocloseanHTTPSsession.This
commandstopsandstartsthehpe-restdservice,sousingthiscommandaffectsallexistingREST
sessions,WebUIsessions,andreal-timenotificationsubscriptions.
Example
| switch# | https-server |     | session | close | all |     |
| ------- | ------------ | --- | ------- | ----- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideorthe
RESTAPIGuideforyourswitchmodel.
| Command        | History     |     |         |     |              |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| Release        |             |     |         |     | Modification |     |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| https-server |                 | session-timeout |     |           |     |     |
| ------------ | --------------- | --------------- | --- | --------- | --- | --- |
| https-server | session-timeout |                 |     | <MINUTES> |     |     |
Description
Configuresthetimeout,inminutes,foranygivenHTTPSserversession.Avalueof0disablesthe
timeout.ThiscommanddoesnotaffectsessionsusedforCentralconnections.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<MINUTES> Specifiesthemaximumidletime,inminutesforanHTTPSsession.
Default: 20.Maximum: 480(8hours).0disablesthetimeout,but
themaxiumisstillenforced.
Example
| switch(config)# |     | https-server |     | session-timeout |     | 10  |
| --------------- | --- | ------------ | --- | --------------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideorthe
RESTAPIGuideforyourswitchmodel.
| Command | History |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 176

| Release             |         |         | Modification      |
| ------------------- | ------- | ------- | ----------------- |
| 10.08               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| https-server    | vrf            |     |     |
| --------------- | -------------- | --- | --- |
| https-server    | vrf <VRF-NAME> |     |     |
| no https-server | vrf <VRF-NAME> |     |     |
Description
ConfiguresandstartstheHTTPSserveronthespecifiedVRF,allowingaccesstoRESTandtheWebUI
fromportsassignedtothatVRF.ThiscommanddoesnotaffectaccesstoHPEArubaNetworkingCentral
instances,asthisfeaturehasitsowndedicatedconnectionchannel.
ThenoformofthecommandstopsanyHTTPSserversrunningonthespecifiedVRFandremovesthe
HTTPSserverconfiguration.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VRF-NAME> SpecifiestheVRFname.Required.Length:Upto32alphanumeric
characters.
Usage
Byusingthiscommand,youenableaccesstoboththeWebUIandtotheRESTAPIonthespecifiedVRF.
YoucanenableaccessonmultipleVRFs.
Bydefault,HPEArubaNetworking8100,8320,8325,8360,8400,9300/9300S,and10000SwitchSeries
haveanHTTPSserverenabledonthemgmtVRF.
Bydefault,theHPEArubaNetworking5420,6200,6300,and6400SwitchSerieshaveanHTTPSserver
enabledonthemgmtVRFandonthedefaultVRF.
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
HPEArubaNetworkingNetworkAnalyticsEnginescriptsruninthedefaultVRF,butyoudonothaveto
enableHTTPSserveraccessonthedefaultVRFforthescriptstorun.IftheswitchhascustomHPE
HTTPSservercommands|177

ArubaNetworkingNetworkAnalyticsEnginescriptsthatrequireaccesstotheInternet,thenforthose
scriptstoperformtheirfunctions,youmustconfigureaDNSnameserveronthedefaultVRF.
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
TheHPEArubaNetworking6200and5420switchessupportonlytwoVRFs.OnemanagementVRFandone
defaultVRF.YoucannotaddanotherVRF.
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideorthe
RESTAPIGuideforyourswitchmodel.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show https-server
| show https-server | [vsx-peer] |     |     |
| ----------------- | ---------- | --- | --- |
Description
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 178

ShowsthestatusandconfigurationoftheHTTPSserver.TheRESTAPIandwebuserinterfaceare
accessibleonlyonVRFsthathavetheHTTPSserverfeaturesconfigured.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
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
| switch# show | https-server  |     |     |     |
| ------------ | ------------- | --- | --- | --- |
| HTTPS Server | Configuration |     |     |     |
----------------------------
| VRF          |         | :    | default,   | mgmt |
| ------------ | ------- | ---- | ---------- | ---- |
| REST Access  | Mode    | :    | read-write |      |
| Max sessions | per     | user | : 6        |      |
| Session      | timeout |      | : 20       |      |
Formoreinformationonfeaturesthatusethiscommand,refertotheNetworkAnalyticsEngineGuideorthe
RESTAPIGuideforyourswitchmodel.
| Command History     |         |     |         |              |
| ------------------- | ------- | --- | ------- | ------------ |
| Release             |         |     |         | Modification |
| 10.07orearlier      |         |     |         | --           |
| Command Information |         |     |         |              |
| Platforms           | Command |     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
HTTPSservercommands|179

| show https-server |                | authentication |     |
| ----------------- | -------------- | -------------- | --- |
| show https-server | authentication |                |     |
Description
Showsthehttps-serverauthenticationmodestatus.
Examples
Showingtheauthenticationmethodwiththepasswordmodeenabled:
| switch# show   | https-server | authentication |     |
| -------------- | ------------ | -------------- | --- |
| Authentication | Modes        | Status         |     |
----------------------------
| Password    | Status | : enabled  |     |
| ----------- | ------ | ---------- | --- |
| Certificate | Status | : disabled |     |
Showingtheauthenticationmethodwiththecertificatemodeenabled:
| switch# show   | https-server | authentication |     |
| -------------- | ------------ | -------------- | --- |
| Authentication | Modes        | Status         |     |
----------------------------
| Password            | Status  | : disabled |                    |
| ------------------- | ------- | ---------- | ------------------ |
| Certificate         | Status  | : enabled  |                    |
| Command History     |         |            |                    |
| Release             |         |            | Modification       |
| 10.11               |         |            | CommandIntroduced. |
| Command Information |         |            |                    |
| Platforms           | Command | context    | Authority          |
Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
Allplatforms
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
AOS-CX10.15.xxxxNetworkAnalyticsEngineGuide|(5420,6200,6300,6400,8xxx,9300,10000SwitchSeries) 180

Chapter 16

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

Airheads social
forums and
Knowledge Base

https://community.arubanetworks.com/

AOS-CX Software

Videos on new features introduced in this release:

Technical Update

https://www.youtube.com/playlist?list=PLsYGHuNuBZcbWPEjjHuVMqP-Q_UL3CskS

channel on

YouTube.

HPE Aruba

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

181

| Networking | htm |     |
| ---------- | --- | --- |
Hardware
Documentation
andTranslations
Portal
| HPEAruba | https://networkingsupport.hpe.com/downloads |     |
| -------- | ------------------------------------------- | --- |
Networking
software
| Software | https://licensemanagement.hpe.com/ |     |
| -------- | ---------------------------------- | --- |
licensingand
FeaturePacks
End-of-Life https://www.arubanetworks.com/support-services/end-of-life/
information
| HPEAruba | https://developer.arubanetworks.com/ |     |
| -------- | ------------------------------------ | --- |
Networking
DeveloperHub
| Accessing | Updates |     |
| --------- | ------- | --- |
YoucanaccessupdatesfromtheHPEArubaNetworkingSupportPortalat
https://networkingsupport.hpe.com.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://networkingsupport.hpe./notifications/subscriptions(requiresanactiveHPEArubaNetworking
SupportPortalaccounttomanagesubscriptions).SecuritynoticesareviewablewithoutanHPEAruba
NetworkingSupportPortalaccount.
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
HPEArubaNetworkingiscommittedtoprovidingourcustomerswithinformationaboutthechemical
substancesinourproductsasneededtocomplywithlegalrequirements,environmentaldata(company
programs,productrecycling,energyefficiency),andsafetyinformationandcompliancedata,(RoHSand
WEEE).Formoreinformation,seehttps://www.arubanetworks.com/company/about-us/environmental-
citizenship/.
| Documentation |     | Feedback |
| ------------- | --- | -------- |
SupportandOtherResources|182

HPE Aruba Networking is committed to providing documentation that meets your needs. To help us
improve the documentation, send any errors, suggestions, or comments to Documentation Feedback
(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.15.xxxx Network Analytics Engine Guide | (5420, 6200, 6300, 6400, 8xxx, 9300, 10000 Switch Series)

183