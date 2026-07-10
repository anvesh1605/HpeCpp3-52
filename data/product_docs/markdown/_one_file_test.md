| AOS-CX       | 10.07 | High |
| ------------ | ----- | ---- |
| Availability | Guide |      |
PartNumber:5200-7854
Published:April2021
Edition:1

CopyrightInformation
©Copyright2021HewlettPackardEnterpriseDevelopmentLP.
Open Source Code
ThisproductincludescodelicensedundertheGNUGeneralPublicLicense,theGNULesserGeneralPublic
License,and/orcertainotheropensourcelicenses.Acompletemachine-readablecopyofthesourcecode
correspondingtosuchcodeisavailableuponrequest.Thisofferisvalidtoanyoneinreceiptofthis
informationandshallexpirethreeyearsfollowingthedateofthefinaldistributionofthisproductversion
byHewlettPackardEnterpriseCompany.Toobtainsuchsourcecode,sendacheckormoneyorderinthe
amountofUS$10.00to:
HewlettPackardEnterpriseCompany
6280AmericaCenterDrive
SanJose,CA95002
USA
Notices
Theinformationcontainedhereinissubjecttochangewithoutnotice.TheonlywarrantiesforHewlett
PackardEnterpriseproductsandservicesaresetforthintheexpresswarrantystatementsaccompanying
suchproductsandservices.Nothinghereinshouldbeconstruedasconstitutinganadditionalwarranty.
HewlettPackardEnterpriseshallnotbeliablefortechnicaloreditorialerrorsoromissionscontainedherein.
Confidentialcomputersoftware.ValidlicensefromHewlettPackardEnterpriserequiredforpossession,use,
orcopying.ConsistentwithFAR12.211and12.212,CommercialComputerSoftware,ComputerSoftware
Documentation,andTechnicalDataforCommercialItemsarelicensedtotheU.S.Governmentunder
vendor'sstandardcommerciallicense.
Linkstothird-partywebsitestakeyououtsidetheHewlettPackardEnterprisewebsite.HewlettPackard
EnterprisehasnocontroloverandisnotresponsibleforinformationoutsidetheHewlettPackard
Enterprisewebsite.
Acknowledgments
Intel®,Itanium®,Optane™,Pentium®,Xeon®,IntelInside®,andtheIntelInsidelogoaretrademarksof
IntelCorporationintheU.S.andothercountries.
Microsoft®andWindows®areeitherregisteredtrademarksortrademarksofMicrosoftCorporationinthe
UnitedStatesand/orothercountries.
Adobe®andAcrobat®aretrademarksofAdobeSystemsIncorporated.
Java®andOracle®areregisteredtrademarksofOracleand/oritsaffiliates.
UNIX®isaregisteredtrademarkofTheOpenGroup.
Allthird-partymarksarepropertyoftheirrespectiveowners.
|2

Contents
Contents
| Contents                                   |                                | 3   |
| ------------------------------------------ | ------------------------------ | --- |
| About this                                 | Document                       | 5   |
| ApplicableProducts                         |                                | 5   |
| LatestVersionAvailableOnline               |                                | 5   |
| CommandSyntaxNotationConventions           |                                | 5   |
| AbouttheExamples                           |                                | 6   |
| IdentifyingSwitchPortsandInterfaces        |                                | 6   |
| IdentifyingModularSwitchComponents         |                                | 8   |
| High Availability                          |                                | 9   |
| HighAvailabilityOverview                   |                                | 9   |
| ManagementModuleFailoverOverview           |                                | 10  |
| AAAonSwitcheswithMultipleManagementModules |                                | 12  |
| HighAvailabilityCommands                   |                                | 12  |
|                                            | redundancyswitchover           | 12  |
| BFD                                        |                                | 14  |
| BFDFeatures                                |                                | 14  |
| ConfiguringBFDforanIPv4StaticRoute         |                                | 15  |
| ConfiguringBFDforBGP                       |                                | 16  |
| ConfiguringBFDForOSPFv2                    |                                | 18  |
| ConfiguringBFDForOSPFv3                    |                                | 19  |
| ConfiguringBFDforPIMOverIPv4               |                                | 21  |
| ConfiguringBFDforPIMOverIPv6               |                                | 22  |
| ConfiguringBFDforVRRP                      |                                | 24  |
| BFDCommands                                |                                | 25  |
|                                            | bfd                            | 25  |
|                                            | bfd<IPV4-ADDR>                 | 25  |
|                                            | bfdall-interfaces              | 26  |
|                                            | bfddetect-multiplier           | 27  |
|                                            | bfddisable                     | 27  |
|                                            | bfdenable(Context:config-hsc)  | 28  |
|                                            | bfddisable(Context:config-hsc) | 28  |
|                                            | bfdechodisable                 | 29  |
|                                            | bfdecho-src-ip-address         | 30  |
|                                            | bfdmin-echo-receive-interval   | 30  |
|                                            | bfdmin-receive-interval        | 31  |
|                                            | bfdmin-transmit-interval       | 32  |
|                                            | clearbfdstatistics             | 33  |
|                                            | ipospfbfd                      | 33  |
|                                            | ipospfbfddisable               | 34  |
|                                            | iproutebfd                     | 34  |
|                                            | ipv6ospfv3bfd                  | 35  |
|                                            | ipv6ospfv3bfddisable           | 36  |
|                                            | neighborfall-overbfd           | 37  |
|                                            | showbfd                        | 37  |
|                                            | showbfdinterface               | 39  |
|                                            | showhsc                        | 41  |
3
AOS-CX10.07HighAvailabilityGuide| UserGuide

| ERPS                               |                                             |     | 42  |
| ---------------------------------- | ------------------------------------------- | --- | --- |
| Limitations,Conflicts,orExclusions |                                             |     | 42  |
| ERPSCommands                       |                                             |     | 44  |
|                                    | clearerpsring<ringid>instance<id>           |     | 44  |
|                                    | clearerpsstatistics                         |     | 45  |
|                                    | erpsring                                    |     | 45  |
|                                    | erpsring<ringid><port0|port1>interface      |     | 46  |
|                                    | erpsring<ringid>description                 |     | 47  |
|                                    | erpsring<ringid>guard-interval              |     | 47  |
|                                    | erpsring<ringid>hold-off-interval           |     | 48  |
|                                    | erpsring<ringid>instance                    |     | 49  |
|                                    | erpsring<ringid>instance<id>control-vlan    |     | 50  |
|                                    | erpsring<ringid>instance<id>description     |     | 50  |
|                                    | erpsring<ringid>instance<id>enable          |     | 51  |
|                                    | erpsring<ringid>instance<id>protected-vlans |     | 52  |
erpsring<ringid>instance<id>protection-switch{{manual|force}<port0>|<port1>} 53
|                       | erpsring<ringid>instance<id>revertive |           | 54  |
| --------------------- | ------------------------------------- | --------- | --- |
|                       | erpsring<ringid>instance<id>role      |           | 55  |
|                       | erpsring<ringid>instance<id>rpl       |           | 56  |
|                       | erpsring<ringid>meg-level             |           | 57  |
|                       | erpsring<ringid>parent-ring           |           | 58  |
|                       | erpsring<ringid>sub-ring              |           | 58  |
|                       | erpsring<ringid>tcn-propogation       |           | 59  |
|                       | erpsring<ringid>transmission-interval |           | 60  |
|                       | erpsring<ringid>wtr-interval          |           | 60  |
|                       | showerpsstatistics                    |           | 61  |
|                       | showerpsstatus                        |           | 62  |
|                       | showerpssummary                       |           | 65  |
| Support               | and Other                             | Resources | 66  |
| AccessingArubaSupport |                                       |           | 66  |
| AccessingUpdates      |                                       |           | 66  |
|                       | ArubaSupportPortal                    |           | 66  |
|                       | MyNetworking                          |           | 67  |
| WarrantyInformation   |                                       |           | 67  |
| RegulatoryInformation |                                       |           | 67  |
| DocumentationFeedback |                                       |           | 67  |
Contents|4

Chapter 1
About this Document
About this Document
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedforadministrators
responsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
Applicable Products
Thisdocumentappliestothefollowingproducts:
n Aruba6200SwitchSeries(JL724A,JL725A,JL726A,JL727A,JL728A)
n Aruba6300SwitchSeries(JL658A,JL659A,JL660A,JL661A,JL662A,JL663A,JL664A,JL665A,JL666A,
JL667A,JL668A,JL762A)
n Aruba6400SwitchSeries(JL741A,R0X26A,R0X27A,R0X29A,R0X30A)
n Aruba8320SwitchSeries(JL479A,JL579A,JL581A)
n Aruba8325SwitchSeries(JL624A,JL625A,JL626A,JL627A)
n Aruba8360SwitchSeries(JL700A,JL701A,JL702A,JL703A,JL706A,JL707A,JL708A,JL709A,JL710A,
JL711A)
n Aruba8400SwitchSeries(JL375A,JL376A)
Latest Version Available Online
Updatestothisdocumentcanoccurafterinitialpublication.Forthelatestversionsofproduct
documentation,seethelinksprovidedinSupportandOtherResources.
Command Syntax Notation Conventions
Convention Usage
example-text Identifiescommandsandtheiroptionsandoperands,codeexamples,
filenames,pathnames,andoutputdisplayedinacommandwindow.Itemsthat
appearliketheexampletextinthepreviouscolumnaretobeenteredexactly
asshownandarerequiredunlessenclosedinbrackets([ ]).
example-text Incodeandscreenexamples,indicatestextenteredbyauser.
Anyofthefollowing: Identifiesaplaceholder—suchasaparameteroravariable—thatyoumust
n <example-text> substitutewithanactualvalueinacommandorincode:
n <example-text>
n Foroutputformatswhereitalictextcannotbedisplayed,variablesare
n example-text
enclosedinanglebrackets(< >).Substitutethetext—includingthe
n example-text
enclosinganglebrackets—withanactualvalue.
n Foroutputformatswhereitalictextcanbedisplayed,variablesmight
ormightnotbeenclosedinanglebrackets.Substitutethetext
includingtheenclosinganglebrackets,ifany,withanactualvalue.
AOS-CX10.07HighAvailabilityGuide| UserGuide 5

Convention Usage
| Verticalbar.AlogicalORthatseparatesmultipleitemsfromwhichyoucan
chooseonlyone.
Anyspacesthatareoneithersideoftheverticalbarareincludedfor
readabilityandarenotarequiredpartofthecommandsyntax.
{ } Braces.Indicatesthatatleastoneoftheencloseditemsisrequired.
[ ] Brackets.Indicatesthattheencloseditemoritemsareoptional.
…or Ellipsis:
... n Incodeandscreenexamples,averticalorhorizontalellipsisindicatesan
omissionofinformation.
n Insyntaxusingbracketsandbraces,anellipsisindicatesitemsthatcanbe
repeated.Whenanitemfollowedbyellipsesisenclosedinbrackets,zero
ormoreitemscanbespecified.
About the Examples
Examplesinthisdocumentarerepresentativeandmightnotmatchyourparticularswitchorenvironment.
Theslotandportnumbersinthisdocumentareforillustrationonlyandmightbeunavailableonyour
switch.
Understandingthe CLI prompts
Whenillustratingthepromptsinthecommandlineinterface(CLI),thisdocumentusesthegenericterm
switch,insteadofthehostnameoftheswitch.Forexample:
switch>
TheCLIpromptindicatesthecurrentcommandcontext.Forexample:
switch>
Indicatestheoperatorcommandcontext.
switch#
Indicatesthemanagercommandcontext.
switch(CONTEXT-NAME)#
Indicatestheconfigurationcontextforafeature.Forexample:
switch(config-if)#
Identifiestheinterfacecontext.
Variable information in CLI prompts
Incertainconfigurationcontexts,thepromptmayincludevariableinformation.Forexample,wheninthe
VLANconfigurationcontext,aVLANnumberappearsintheprompt:
switch(config-vlan-100)#
Whenreferringtothiscontext,thisdocumentusesthesyntax:
switch(config-vlan-<VLAN-ID>)#
Where<VLAN-ID>isavariablerepresentingtheVLANnumber.
Identifying Switch Ports and Interfaces
AboutthisDocument|6

Physicalportsontheswitchandtheircorrespondinglogicalsoftwareinterfacesareidentifiedusingthe
format:
member/slot/port
On the 6200Switch Series
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to8.The
primaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis1.
n slot:Linemodulenumber.Always1.
n port:Physicalnumberofaportonalinemodule.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4inslot1onmember1.
On the 6300Switch Series
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to10.The
primaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis1.
n slot:Linemodulenumber.Always1.
n port:Physicalnumberofaportonalinemodule.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4inslot1onmember1.
On the 6400Switch Series
n member:Always1.VSFisnotsupportedonthisswitch.
n slot:Specifiesphysicallocationofamoduleintheswitchchassis.
o Managementmodulesareonthefrontoftheswitchinslots1/1and1/2.
o Linemodulesareonthefrontoftheswitchstartinginslot1/3.
n port:Physicalnumberofaportonalinemodule.
Forexample,thelogicalinterface1/3/4insoftwareisassociatedwithphysicalport4inslot3onmember1.
On the 83xxSwitch Series
n member:Always1.VSFisnotsupportedonthisswitch.
n slot:Linemodulenumber.Always1.
n port:Physicalnumberofaportonalinemodule
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4inslot1onmember1.
Ifusingbreakoutcables,theportdesignationchangestox:y,wherexisthephysicalportandyisthelanewhen
splitto4x10Gor4x25G.Forexample,thelogicalinterface1/1/4:2insoftwareisassociatedwithlane2on
physicalport4inslot1onmember1.
On the 8400Switch Series
n member:Always1.VSFisnotsupportedonthisswitch.
n slot:Specifiesphysicallocationofamoduleintheswitchchassis.
o Managementmodulesareonthefrontoftheswitchinslots1/5and1/6.
o Linemodulesareonthefrontoftheswitchinslots1/1through1/4,and1/7through1/10.
n port:Physicalnumberofaportonalinemodule
AOS-CX10.07HighAvailabilityGuide|UserGuide 7

Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4inslot1onmember1.
Identifying Modular Switch Components
n Powersuppliesareonthefrontoftheswitchbehindthebezelabovethemanagementmodules.Power
suppliesarelabeledinsoftwareintheformat:member/powersupply:
o member:1.
o powersupply:1to4.
n Fansareontherearoftheswitchandarelabeledinsoftwareas:member/tray/fan:
o member:1.
o tray:1to4.
o fan:1to4.
n Fabricmodulesarenotlabeledontheswitchbutarelabeledinsoftwareintheformat:member/module:
o member:1.
o member:1or2.
n Thedisplaymoduleontherearoftheswitchisnotlabeledwithamemberorslotnumber.
AboutthisDocument|8

Chapter 2
High Availability
High Availability
TheHighAvailability(HA)featurehasthreecomponents:
n RedundantManagement
n OVSDBsynchronization
n Filesystemreplication
High Availability Overview
KeygoalsofHAinclude:
n Achievefive-nines(99.999%)availabilityofswitchingtrafficthroughminimizationofunplannednetwork
outages.
n Faulttolerant:Nosingleactivecomponentfailurewillcauseanoutage.
n Livereplacementofhardwarewithminimalornodisruption.
Terminology:
n MM:Abbreviationformanagementmodule
n MM toMM link:Referstothe10GbE-KREthernetlinkbetweentwoMMs
n OVSDB:AbbreviationforOpenvSwitchDatabase
n Active MM:Managementmodulethathascontrolofthechassis
n Standby MM:Backupmanagementmodulefortheactivemanagementmodule
n JSON-RPC:RemoteprocedurecallprotocolencodedinJSON
KeypartsoftheHAfeatureinclude:
Networkredundancy:Protocolsandredundantnetworkpathsprovideredundancyinthenetwork,
enablingtraffictocontinueflowingifanetworklinkornetworkswitchfails.
Hardware redundancy:Redundanthardwarecomponents(powersupplies,fabriccards,management
modules)allowcontinuedswitchingtrafficorsystemmanagementintheeventofahardwarefailureor
hardwaremaintenance.Thisfunctionalityissupportedthrough:
n Fastfailover(managementfailover)
n Hotinsertandremoval(allfield-replaceablehardwarecomponents)
Redundancyofspecific,field-replaceablehardwarecomponentsincludes:
n Redundancymanagement(managementmodules),whichisinchargeof:
o HAinfrastructure
o Filesynchronization
o OVSDBsynchronization
o MMfailover
AOS-CX10.07HighAvailabilityGuide| UserGuide 9

o StandbyMMconfiguration
o Softwareversionupdate
TheActiveMMcontrolsinfrastructure,files,andthedatabase.IftheActiveMMisremoved,allmanagement
passestotheStandbyMM.
n Fabricredundancy(fabriccards)
n Networkinterfaceredundancy(linecards)
n Powermanagement(powersupplies)
n Software redundancy:Software(includingdaemons)providesredundancyinsoftwarebysupporting
oneormoreofthefollowingmethods:
o Nonstopswitchingrestart:
ThedaemonreadsitslastknownstateorthecurrenthardwarestatefromOVSDB.
l
Thedaemonadjustsitsinternalstatetomatchthelastknownstate.
l
Thereisnotrafficinterruptionandnomomentintimewherethelastknownconfigurationisnot
l
ineffect.
Thedaemonrestartsfastenoughtorespondtoprotocolsthatrequirepeercommunication
l
withouttimingout.
ExamplesincludeLACP,ACLS,TCAMentries,andMSTP.
l
o Gracefulrestart:
CurrentstateisstillreadfromOVSDB.Trafficfollowstherulesofthisstateuntiltheprotocolhas
l
fullyrecovered.
Connectionstootherswitchesarere-established.
l
Currentstateisrepublishedtopeers,whichcanthenrespondbackwithadjustments.
l
Examplesincluderoutingprotocols.
l
o Fullstatereset:
Anynon-defaultruntimestatethedaemonhasinhardwareorOVSDBisforcedbacktothedefault
l
state.
Anyconnectionsareclosedandhavetobemanuallyrestarted.
l
Thisisprimarilyforuser-facingdaemonsandfeaturesforwhichthedefaultstatedoesnothavea
l
largeimpactontraffic.
ExamplesincludeSSH,webserver,TFTP,andCLI.
l
Management Module Failover Overview
TherearetwotypesofManagementModule(MM)failover:
n Controlledfailover:TheusertriggersthistypeoffailoverbyrebootingtheActiveMMorrunningthe
redundancy switchovercommand.
n Uncontrolledfailover:ThistypeoffailoveristriggeredbyunexpectedeventslikeacrashontheActive
MMorhotremovaloftheActiveMM.
InadualMMchassis,theStandbyMMdetectsfailovereventsinoneofthefollowingways:
n AmailboxinterruptisreceivedfromtheActiveMMtoindicatetakeover.Thisinterruptcancomefor
controlledoruncontrolledfailover(exceptforahotremoval).
n ActiveMMhotremovaldetection.
HighAvailability|10

n HeartbeatlossdetectedontheStandbyMMformorethan10seconds.
IftheActiveMMisnotrespondingandisstillnotdetectedbythefirsttwomethods,itwillbecaught
bythismethod.
Failoverrequirements:
n TheStandbyMMmustbepresenttotriggerafailover.AnUnassignedMMwillnevertriggerafailover.
n TheRedundantManagementDaemon(hpe-rdntmgmtd)isresponsiblefortriggeringfailoverfromthe
StandbyMM.
n Whenafailoveristriggered,theStandbyMMbecomestheActiveMMwhilethepreviouslyActiveMMis
rebooted.
Standbyrecoveryrequirements:
n TheActiveMMmustbepresenttotriggerarecovery.
n TheRedundantManagementDaemon(hpe-rdntmgmtd)isresponsiblefortriggeringrecoverfromthe
ActiveMM.
n Whenarecoveryistriggered,theActiveMMrebootsthenonresponsiveStandbyMM.Thisactionoccurs
foranyofthefollowingconditions:
Condition:HeartbeatlostfromActiveMM:
n ThefailovermonitorthreadontheStandbyMMwillincrementtheheartbeatfailedcount.
n Thehpe-rdntmgmtddaemonontheStandbyMMwill:
o Detectthefailoverconditionduetoheartbeatfailcountincreasingpastthemaximumof10and
triggeringfailover
o InitiaterebootoftheActiveMM.
n ActiveMMwilljoinasastandbyafterreboot.
Condition:HeartbeatlostfromStandbyMM:
n TherecovermonitorthreadontheActiveMMwillincrementtheheartbeatfailedcount.
n Thehpe-rdntmgmtddaemonontheActiveMMwill:
o Detecttherecoverconditionduetoheartbeatfailcountincreasingpastthemaximumof7and
triggeringrecover.
o InitiaterebootofStandbyMM.
n StandbyMMwilljoinasastandbyafterreboot.
Condition:PlannedrebootofActiveMM:
n AplannedrebootontheActiveMMwillsendafailovercommandtotheStandbyMM.
n Thehpe-rdntmgmtddaemonontheStandbyMMwill:
o Processthiscommandandperformafailoverimmediatelyinsteadofwaitingforthefailovermonitor
todetectitusingheartbeats.
o InitiaterebootoftheActiveMM.
n ActiveMMwilljoinasastandbyafterreboot.
Condition:RemovalofActiveMM:
AOS-CX10.07HighAvailabilityGuide|UserGuide 11

n RemovaloftheActiveMMfromSlot1triggersthehpe-rdntmgmtddaemonontheStandbyMMto
initiatefailoverimmediatelyinsteadofwaitingforthefailovermonitortodetectitusingheartbeats.
n ActiveMMwilljoinasastandbyafterreboot.
Condition:CrashonActiveMM:
n AcrashontheActiveMMishandledbythecrashhandler,whichsendsafailovercommandtothe
StandbyMM.
n Thehpe-rdntmgmtddaemonontheStandbyMMwill:
o Processthiscommandandperformfailoverimmediatelyinsteadofwaitingforthefailovermonitor
todetectitusingheartbeats.
o InitiaterebootoftheActiveMM.
n ActiveMMwilljoinasastandbyafterreboot.
Condition:redundancy switchovercommand:
n Userexecutestheredundancy switchovercommandontheActiveMM.
n ThisactionwillsendatakeoversignaltotheStandbyMMandreboottheActiveMM.
n Thehpe-rdntmgmtddaemononStandbyMMwillprocessthistakeoversignalandperformfailover
immediately.
n ActiveMMwilljoinasastandbyafterreboot.
Why didmy secondMM not take overafterActive failed?
ThisactionwillhappenifthesecondMMisnotStandby-Ready.
ThesecondMMmustbeelectedasStandbyandinareadystatebeforefailover.Ifnot,adoublefaultoccursand
thesecondMMwillnottakeover.
AAA on Switches with Multiple Management Modules
Considerthefollowingwhenworkingwithlocalauthentication,authorization,andaccounting(AAA)on
switcherswithmultiplemanagementmodules:
n Localauthentication:
o TheuserdatabaseissynchronizedbetweentheActiveandStandbymanagementmodules.
o Onlylocalusersbelongingtotheadministratorsgroupandusinglocalpasswordauthenticationare
permittedtologintotheStandbymanagementmodule.Alternatively,theStandbymanagement
modulecanbeaccessedfromtheActivemanagementmodulebyprovidingaloggedinadminuser
password.
n Localauthorization:
o AfewnonconfigurationcommandsareavailableontheStandbymanagementmodule.
o Forexpertusers,thebashshellisavailableontheStandbymanagementmodule.
n Localaccounting:
o TheauditlogsusedforlocalaccountingareavailableonlyontheActiveManagementModule.
High Availability Commands
redundancy switchover
HighAvailability|12

Syntax
redundancy switchover
Description
CausestheswitchtoimmediatelyswitchovertotheStandbyManagementModule.Thiscommandmustbe
executedfromtheActiveManagementModuleandwillfailiftheStandbyManagementModuleisinafailed
stateornotpresent.
Commandcontext
Manager(#)
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Thisexampleshowstheredundancyswitchovercommandonanactivemanagementmodulewitha
standbymanagementmodulethatispresent.
switch#redundancy switchover
This command causes the switch to immediately switchover to the Standby Management
Module.
Do you want to continue [y/n]?
Thisexampleshowstheredundancyswitchovercommandonanactivemanagementmodulewitha
standbymanagementmodulethatisabsent.
switch#redundancy switchover
Standby Management Module not found, switchover request ignored.
Thisexampleshowstheredundancyswitchovercommandonastandbymanagementmodule.
switch#redundancy switchover
Redundancy switchover must be performed from the Active Management Module,
switchover request ignored.
AOS-CX10.07HighAvailabilityGuide|UserGuide 13

Chapter 3
BFD
BFD
TheBFDfeatureandthusthisentirechapterisnotapplicabletothe6200SwitchSeries.
BidirectionalForwardingDetection(BFD)providesageneral-purpose,standard,medium-andprotocol-
independentfastfailuredetectionmechanism.ItcandetectandmonitortheconnectivityoflinksinIPto
detectcommunicationfailuresquickly.BFDoperatesindependentlyofmedia,dataprotocols,androuting
protocols.
BFDestablishesasessionbetweentwonetworkdevicestodetectfailuresonthebidirectionalforwarding
pathsbetweenthedevicesandprovideservicesforupper-layerprotocols.BFDprovidesnoneighbor
discoverymechanism.ProtocolsthatBFDservicesnotifyBFDofdevicestowhichitneedstoestablish
sessions.Afterasessionisestablished,ifnoBFDcontrolpacketisreceivedfromthepeerwithinthe
negotiatedBFDinterval,BFDnotifiesafailuretotheprotocol,whichthentakesappropriatemeasures.
BFDoperatesintwomodes:
n Asynchronousmode:Inthismode,anoperatingdeviceperiodicallysendsBFDcontrolpacketstoanother
device.IftheotherdevicedoesnotreceiveBFDcontrolpacketfromthepeerwithinthespecifiedinterval,
ittearsdowntheBFDsession.
n Demandmode:inthismode,itisassumedthatanoperatingdevicehasanindependentwayofverifying
thatithasconnectivitytothepeer.OnceaBFDsessionisestablished,onedevicemayrequestthatthe
otherdevicestopssendingBFDcontrolpackets,exceptwhentheconnectionmustbeexplicitlyvalidated,
inwhichcaseashortsequenceofBFDcontrolpacketsisexchanged.Demandmodemayoperate
independentlyineachdirection,orsimultaneously.
BFDalsohasanechofunction.Whenechoisactive,anoperatingdeviceperiodicallysendsBFDecho
packets.ThepeerdevicereturnsthereceivedBFDechopacketsbackwithoutprocessingthem(itloops
themthroughitsforwardingpath).IfthesendingdevicedoesnotreceiveBFDechopacketsfromthepeer
withinaspecifiedinterval,thesessionisconsidereddown.Sincetheechofunctionishandlingthetaskof
detection,therateofperiodictransmissionofcontrolpacketsmaybereducedinasynchronousmode,and
eliminatedindemandmode.
BFD Features
BGP,OSPFv2,OSPFv3,PIMv4andPIMv6,staticroutes,andVRRPareclientsofBFD.
Supported:
n BFDv1
n Asynchronousmode+echo
n IPv6(8400,6400and6300switchesonly)
n AsynchronousmodeonIPv6tunnelinterfaces(8400switchesonly)
n AsynchronousmodeforVxLANtunnels(8325,8360and8400switchesonly)
n Singlehop
n IPv4
AOS-CX10.07HighAvailabilityGuide| UserGuide 14

n RoP,SVI,andLAGinterfaces
n VSXsynchronization.Formoreinformation,seetheVirtualSwitchingExtension(VSX)Guideforyour
switchandsoftwareversion.
n LoopbacksaresupportedforVxLANsessions(8325,8360and8400switchesonly),andstaticroutes
(6300,6400and8400switchesonly).SameIPversionrestrictionsapply.
Notsupported:
n MIBsupport
n IPv6(832xswitchesonly)
n Demandmode
n Micro-BFD
n Authentication
n Echofunctionontunnelinterfaces
n BFDsessionsarenotsupportedontunnelinterfaces(6300,6400,and8320switchesonly)
n IPv6BFDsessionsarenotsupported(8320,8325,and8360switchesonly)
n EchofunctionforIPv6
n Asynchronousmodeontunnelinterfaces(832xswitchesonly)
n Multi-hopconfigurations.BFDworksonlyfordirectlyconnectedneighbors.BFDneighborsmustbeno
morethanoneIPhopaway.
n Passiveandvirtuallinkinterfaces.Loopbacksarenotsupportedonthe8320,8325and8360switches
withtheexceptionofVXLANsessionson8325and8360switches.
n Exceedingamaximumof20BFDsessionswithintervalvaluesof300ms.Spurioussessionsflapswill
occurwhenthelimitofsessionsisexceeded.
n Minimumintervalsof300msareonlycompatiblewiththeasync_vxlanmode(BFDsessionsacross
VxLAN)andisnotuserconfigurable.
n Settingminimumtransmittimeintervalbetween500msand1000ms,andbfd detect-multiplierless
than3mightresultinspuriousflaps.
Configuring BFD for an IPv4 Static Route
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. EnableBFDonanIPv4staticroutewiththecommandip route bfd.
3. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
BFD setting Default value Commandtochange it
SetstheBFDdetection 5 bfd detect-multiplier
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
BFD|15

| BFD setting |     | Default value | Commandtochange | it  |
| ----------- | --- | ------------- | --------------- | --- |
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
| 4. ReviewBFDconfigurationsettingswiththecommandsshow |     |     | bfd. |     |
| ---------------------------------------------------- | --- | --- | ---- | --- |
Example
EnablingBFDonastaticIPv4route.
| switch# config     |             |                      |     |     |
| ------------------ | ----------- | -------------------- | --- | --- |
| switch(config)#    | bfd         |                      |     |     |
| switch# interface  | 1/1/1       |                      |     |     |
| switch(config-if)# | no shutdown |                      |     |     |
| switch(config-if)# | ip address  | 192.168.1.1/24       |     |     |
| switch(config-if)# | exit        |                      |     |     |
| switch(config)#    | ip route    | 10.0.2.0/24 20.0.0.2 | bfd |     |
| Configuring        | BFD for     | BGP                  |     |     |
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. CreateaBGPpeerandinitiateaconnectiontoitwiththecommandneighbor remote-as.
3. EnableBFDonaBGPinterfacewiththecommandneighbor fall-over bfd.
4. Defineanaddressfamilyandactivateitwiththecommandsaddress-familyandneighbor
activate.
5. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
| BFD setting         |     | Default value | Commandtochange       | it  |
| ------------------- | --- | ------------- | --------------------- | --- |
| SetstheBFDdetection |     | 5             | bfd detect-multiplier |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
| 6. ReviewBFDconfigurationsettingswiththecommandsshow |     |     | bfd. |     |
| ---------------------------------------------------- | --- | --- | ---- | --- |
AOS-CX10.07HighAvailabilityGuide|UserGuide 16

Example
EnablingBFDonaBGPinterface.
switch#
config
| switch(config)#                | bfd    |                |            |              |            |          |     |     |
| ------------------------------ | ------ | -------------- | ---------- | ------------ | ---------- | -------- | --- | --- |
| switch(config)#                | router | bgp 100        |            |              |            |          |     |     |
| switch(config-router)#         |        | neighbor       | 10.1.231.2 |              | remote-as  | 100      |     |     |
| switch(config-router)#         |        | neighbor       | 10.1.231.2 |              | fall-over  | bfd      |     |     |
| switch(config-router)#         |        | address-family |            | ipv4-unicast |            |          |     |     |
| switch(config-router-ipv4-uc)# |        |                | neighbor   |              | 10.1.231.2 | activate |     |     |
| switch(config-router-ipv4-uc)# |        |                | exit       |              |            |          |     |     |
| switch(config-router)#         |        | exit           |            |              |            |          |     |     |
| switch(config)#                | exit   |                |            |              |            |          |     |     |
switch#
show ip bgp neighbors
| Codes: ^ Inherited | from | peer-group |     |     |     |     |     |     |
| ------------------ | ---- | ---------- | --- | --- | --- | --- | --- | --- |
VRF : default
| BGP Neighbor        | 9.0.0.1   | (External)    |        |          |                   |            |         |           |
| ------------------- | --------- | ------------- | ------ | -------- | ----------------- | ---------- | ------- | --------- |
| Description         |           | :             |        |          |                   |            |         |           |
| Peer-group          |           | :             |        |          |                   |            |         |           |
| Remote              | Router Id | : 0.0.0.0     |        |          | Local             | Router     | Id      | : (null)  |
| Remote              | AS        | : 100         |        |          | Local             | AS         |         | : 100     |
| Remote              | Port      | : 0           |        |          | Local             | Port       |         | : 0       |
| State               |           | : Idle        |        |          | Admin             | Status     |         | : Up      |
| Conn. Established   |           | : 0           |        |          | Conn.             | Dropped    |         | : 0       |
| Passive             |           | : No          |        |          | Update-Source     |            |         | :         |
| Cfg. Hold           | Time      | : 180         |        |          | Cfg.              | Keep       | Alive   | : 60      |
| Neg. Hold           | Time      | : 0           |        |          | Neg.              | Keep       | Alive   | : 0       |
| Up/Down             | Time      | : 00h:00m:00s |        |          | Alt.              | Local-AS   |         | : 0       |
| Local-AS            | Prepend   | : No          |        |          |                   |            |         |           |
| Fall-over           |           | : No          |        |          | BFD               |            |         | : Enabled |
| Password            |           | :             |        |          |                   |            |         |           |
| Last Err            | Sent      | : No          | Error  |          |                   |            |         |           |
| Last SubErr         | Sent      | : No          | Error  |          |                   |            |         |           |
| Last Err            | Rcvd      | : No          | Error  |          |                   |            |         |           |
| Last SubErr         | Rcvd      | : No          | Error  |          |                   |            |         |           |
| Graceful-Restart    |           | : Enabled     |        |          | Rt.               | Reflect.   | Client: | No        |
| Gr. Restart         | Time      | : 120         |        |          | Gr.               | Stalepath  | Time    | : 150     |
| Max. Prefix         |           | : 0           |        |          | Send              | Community  |         | :         |
| Allow-AS            | in        | : 0           |        |          | Remove            | Private-AS |         | : No      |
| Advt. Interval      |           | : 30          |        |          | TTL               |            |         | : 255     |
| Soft Reconfig       | In        | :             |        |          | Local             | Cluster-ID |         | :         |
| Nexthop-Self        |           | :             |        |          | Default-Originate |            |         | :         |
| Weight              |           | : 0           |        |          |                   |            |         |           |
| TTL Security        | Hops      | : 0           |        |          |                   |            |         |           |
| Routemap            | In        | :             |        |          |                   |            |         |           |
| Routemap            | Out       | :             |        |          |                   |            |         |           |
| Message statistics: |           |               |        |          |                   |            |         |           |
|                     |           | Sent          | Rcvd   |          |                   |            |         |           |
|                     |           | -----         | ------ |          |                   |            |         |           |
| Open                |           | 0             |        | 0        |                   |            |         |           |
| Notification        |           | 0             |        | 0        |                   |            |         |           |
| Updates             |           | 0             |        | 0        |                   |            |         |           |
| Keepalives          |           | 0             |        | 0        |                   |            |         |           |
| Route Refresh       |           | 0             |        | 0        |                   |            |         |           |
| Total               |           | 0             |        | 0        |                   |            |         |           |
| Capability          |           | Advertised    |        | Received |                   |            |         |           |
BFD|17

---------------------------------------------
| Route Refresh |         | No         | No  |     |
| ------------- | ------- | ---------- | --- | --- |
| Graceful      | Restart | No         | No  |     |
| Four Octet    | ASN     | No         | No  |     |
| Configuring   | BFD     | For OSPFv2 |     |     |
Prerequisites
OSPFv2mustbeenabled.
n
n ICMPmustbedisabled.
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. EnableBFDonallOSPFinterfaceswiththecommandbfd all-interfaces,orenableBFDona
| specificinterfacewiththecommandip |     | ospf | bfd. |     |
| --------------------------------- | --- | ---- | ---- | --- |
3. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
| BFD setting         |     | Default value | Commandtochange       | it  |
| ------------------- | --- | ------------- | --------------------- | --- |
| SetstheBFDdetection |     | 5             | bfd detect-multiplier |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,settingadetectionmultiplierof1)can
sometimesleadtoBFDsessionflapsdependingupontrafficconditions.
4. ReviewBFDconfigurationsettingswiththecommandsshow bfd.
Examples
ThisexampleshowshowtoenableBFDonallOSPFv2interfaces.
| switch# config  |     |     |     |     |
| --------------- | --- | --- | --- | --- |
| switch(config)# | bfd |     |     |     |
switch(config)#
|                        | router    | ospf 1             |     |     |
| ---------------------- | --------- | ------------------ | --- | --- |
| switch(config-ospf-1)# |           | area 1             |     |     |
| switch(config-ospf-1)# |           | bfd all-interfaces |     |     |
| switch(config-ospf-1)# |           | exit               |     |     |
| switch(config)         | router    | ospf 2             |     |     |
| switch(config-ospf-2)# |           | area 2             |     |     |
| switch(config-ospf-2)# |           | bfd all-interfaces |     |     |
| switch(config-ospf-2)# |           | exit               |     |     |
| switch(config)#        | interface | 1/1/1              |     |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 18

| switch(config-if)# |     | no  | shutdown |     |     |     |     |     |
| ------------------ | --- | --- | -------- | --- | --- | --- | --- | --- |
switch(config-if)#
|                    |      | ip           | address  | 192.168.1.1/24 |     |     |     |     |
| ------------------ | ---- | ------------ | -------- | -------------- | --- | --- | --- | --- |
| switch(config-if)# |      | ip           | ospf     | 1 area         | 1   |     |     |     |
| switch(config-if)# |      | exit         |          |                |     |     |     |     |
| switch(config)#    |      | interface    |          | 1/1/2          |     |     |     |     |
| switch(config-if)# |      | no           | shutdown |                |     |     |     |     |
| switch(config-if)# |      | ip           | address  | 192.168.1.2/24 |     |     |     |     |
| switch(config-if)# |      | ip           | ospf     | 2 area         | 2   |     |     |     |
| switch(config-if)# |      | exit         |          |                |     |     |     |     |
| switch(config)#    |      | exit         |          |                |     |     |     |     |
| switch#            | show | bfd          |          |                |     |     |     |     |
| Admin status       |      | : Enabled    |          |                |     |     |     |     |
| Echo source        |      | IP : 2.2.2.2 |          |                |     |     |     |     |
Statistics:
| Total Number |     | of Control | Packets |     | Transmitted | : 42 |     |     |
| ------------ | --- | ---------- | ------- | --- | ----------- | ---- | --- | --- |
| Total Number |     | of Control | Packets |     | Received    | : 42 |     |     |
| Total Number |     | of Control | Packets |     | Dropped     | : 0  |     |     |
Session Interface Source IP Destination IP Echo State Application
------- --------- --------------- --------------- -------- ---------- -----------
| 1   | 1/1/1 | 192.168.1.1 |     |     | 100.100.100.101 |     | Enabled Up | OSPF |
| --- | ----- | ----------- | --- | --- | --------------- | --- | ---------- | ---- |
| 2   | 1/2/2 | 192.168.1.2 |     |     | 10.1.5.6        |     | Enabled Up | OSPF |
ThisexampleshowshowtoenableBFDonaspecificOSPFv2interface.
| switch#                | config |           |          |                |     |     |     |     |
| ---------------------- | ------ | --------- | -------- | -------------- | --- | --- | --- | --- |
| switch(config)#        |        | bfd       |          |                |     |     |     |     |
| switch(config)#        |        | router    | ospf     | 1              |     |     |     |     |
| switch(config-ospf-1)# |        |           | area     | 1              |     |     |     |     |
| switch(config-ospf-1)# |        |           | exit     |                |     |     |     |     |
| switch(config)#        |        | interface |          | 1/1/1          |     |     |     |     |
| switch(config-if)#     |        | no        | shutdown |                |     |     |     |     |
| switch(config-if)#     |        | ip        | address  | 192.168.1.1/24 |     |     |     |     |
switch(config-if)#
|                     |               | ip          | ospf   | 1 area  | 1   |     |     |     |
| ------------------- | ------------- | ----------- | ------ | ------- | --- | --- | --- | --- |
| switch(config-if)#  |               | ip          | ospf   | bfd     |     |     |     |     |
| switch(config-if)#  |               | exit        |        |         |     |     |     |     |
| switch(config)#     |               | exit        |        |         |     |     |     |     |
| switch#             | show          | bfd session | 1      |         |     |     |     |     |
| BFD Session         |               | Information | –      | Session | 1   |     |     |     |
| Min Tx              | Interval      | (sec)       | : 10   |         |     |     |     |     |
| Min Rx              | Interval      | (sec)       | : 10   |         |     |     |     |     |
| Min Echo            | Rx            | Interval    | (msec) | : 700   |     |     |     |     |
| Detect              | Multiplier    | : 3         |        |         |     |     |     |     |
| Application         |               | : OSPF      |        |         |     |     |     |     |
| Local Discriminator |               | :           | 1      |         |     |     |     |     |
| Remote              | Discriminator |             | : 1    |         |     |     |     |     |
| Echo :              | Enabled       |             |        |         |     |     |     |     |
| Local Diagnostic    |               | : N/A       |        |         |     |     |     |     |
| Remote              | Diagnostic:   | N/A         |        |         |     |     |     |     |
| Flap count:         |               | 0           |        |         |     |     |     |     |
| Internal            | state:        | Up          |        |         |     |     |     |     |
Interface Source IP Destination IP State Pkt In Pkt Out Pkt Drop
--------- --------------- --------------- ---------- -------- -------- --------
| 1/1/1       | 192.168.1.1 |     |     | 100.100.100.101 |     | Up  | 100 101 | 0   |
| ----------- | ----------- | --- | --- | --------------- | --- | --- | ------- | --- |
| Configuring |             | BFD | For | OSPFv3          |     |     |         |     |
Prerequisites
BFD|19

OSPFv3mustbeenabled.
n
ICMPmustbedisabled.
n
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. EnableBFDonallOSPFinterfaceswiththecommandbfd all-interfaces,orenableBFDona
| specificinterfacewiththecommandipv6 |     |     | ospfv3 | bfd. |     |
| ----------------------------------- | --- | --- | ------ | ---- | --- |
3. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
| BFD setting         |     |     | Default value | Commandtochange       | it  |
| ------------------- | --- | --- | ------------- | --------------------- | --- |
| SetstheBFDdetection |     |     | 5             | bfd detect-multiplier |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
| 4. ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     | bfd. |     |
| ---------------------------------------------------- | --- | --- | --- | ---- | --- |
Examples
ThisexampleshowshowtoenableBFDonanallOSPFv3interfaces.
| switch# config           |           |                    |           |     |     |
| ------------------------ | --------- | ------------------ | --------- | --- | --- |
| switch(config)#          | bfd       |                    |           |     |     |
| switch(config)#          | router    | ospfv3             | 1         |     |     |
| switch(config-ospfv3-1)# |           | area               | 1         |     |     |
| switch(config-ospfv3-1)# |           | router-id          | 1.1.1.1   |     |     |
| switch(config-ospfv3-1)# |           | bfd all-interfaces |           |     |     |
| switch(config-ospfv3-1)# |           | exit               |           |     |     |
| switch(config)           | router    | ospfv3 2           |           |     |     |
| switch(config-ospfv3-2)# |           | area               | 2         |     |     |
| switch(config-ospfv3-2)# |           | router-id          | 1.1.1.2   |     |     |
| switch(config-ospfv3-2)# |           | bfd all-interfaces |           |     |     |
| switch(config-ospfv3-2)# |           | exit               |           |     |     |
| switch(config)#          | interface | 1/1/1              |           |     |     |
| switch(config-if)#       | no        | shutdown           |           |     |     |
| switch(config-if)#       | ipv6      | address            | 100::1/64 |     |     |
| switch(config-if)#       | ipv6      | ospfv3             | 1 area 1  |     |     |
| switch(config-if)#       | exit      |                    |           |     |     |
| switch(config)#          | interface | 1/1/2              |           |     |     |
| switch(config-if)#       | no        | shutdown           |           |     |     |
| switch(config-if)#       | ipv6      | address            | 100::2/64 |     |     |
| switch(config-if)#       | ipv6      | ospfv3             | 2 area 2  |     |     |
| switch(config-if)#       | exit      |                    |           |     |     |
| switch(config)#          | exit      |                    |           |     |     |
| switch# show             | bfd       |                    |           |     |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 20

| Admin status: | enabled |               |     |     |     |     |     |     |     |
| ------------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| Echo source   | IP:     | 100.100.100.1 |     |     |     |     |     |     |     |
Statistics:
| Total number      | of          | control | packets |     | transmitted: | 20  |             |     |      |
| ----------------- | ----------- | ------- | ------- | --- | ------------ | --- | ----------- | --- | ---- |
| Total number      | of          | control | packets |     | received:    | 17  |             |     |      |
| Total number      | of          | control | packets |     | dropped:     | 0   |             |     |      |
| Session Interface |             | VRF     | Source  |     | IP           |     | Destination | IP  | Echo |
| State             | Application |         |         |     |              |     |             |     |      |
------- --------- ------- --------------- --------------- --------
| ------------ | ------------ |     |     |     |     |     |     |     |     |
| ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
1 tunnel1 default fe80::94f1:28a0:1ef:700 fe80::94f1:28a0:1ef:a100 enabled
| up  | ospfv3 |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
2 tunnel1 default fe80::94e2:37b1:1ef:111 fe80::94e2:37b1:1ef:555 enabled
| up  | ospfv3 |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ThisexampleshowshowtoenableBFDonaspecificOSPFv3interface.
| switch# config  |     |        |        |     |     |     |     |     |     |
| --------------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- |
| switch(config)# |     | bfd    |        |     |     |     |     |     |     |
| switch(config)# |     | router | ospfv3 | 1   |     |     |     |     |     |
switch(config-ospfv3-1)#
|                          |     |           | area      | 1   |           |     |     |     |     |
| ------------------------ | --- | --------- | --------- | --- | --------- | --- | --- | --- | --- |
| switch(config-ospfv3-1)# |     |           | router-id |     | 1.1.1.1   |     |     |     |     |
| switch(config-ospfv3-1)# |     |           | exit      |     |           |     |     |     |     |
| switch(config)#          |     | interface | 1/1/1     |     |           |     |     |     |     |
| switch(config-if)#       |     | no        | shutdown  |     |           |     |     |     |     |
| switch(config-if)#       |     | ipv6      | address   |     | 100::1/64 |     |     |     |     |
| switch(config-if)#       |     | ipv6      | ospfv3    | 1   | area      | 1   |     |     |     |
| switch(config-if)#       |     | ipv6      | ospfv3    | bfd |           |     |     |     |     |
| switch(config-if)#       |     | exit      |           |     |           |     |     |     |     |
| switch(config)#          |     | exit      |           |     |           |     |     |     |     |
switch#
| show          | bfd     | interface     |     | 1/1/1 |     |     |     |     |     |
| ------------- | ------- | ------------- | --- | ----- | --- | --- | --- | --- | --- |
| Admin status: | enabled |               |     |       |     |     |     |     |     |
| Echo source   | IP:     | 100.100.100.1 |     |       |     |     |     |     |     |
Statistics:
| Total number      | of          | control | packets |        | transmitted: | 20  |             |     |      |
| ----------------- | ----------- | ------- | ------- | ------ | ------------ | --- | ----------- | --- | ---- |
| Total number      | of          | control | packets |        | received:    | 17  |             |     |      |
| Total number      | of          | control | packets |        | dropped:     | 0   |             |     |      |
| Session Interface |             | VRF     |         | Source | IP           |     | Destination | IP  | Echo |
| State             | Application |         |         |        |              |     |             |     |      |
------- --------- --------- --------------- --------------- -------
| - ------------ |     | ------------ |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
1 tunnel1 default fe80::94f1:28a0:1ef:700 fe80::94f1:28a0:1ef:a100 enabled
| up          | ospfv3 |     |     |     |      |      |     |     |     |
| ----------- | ------ | --- | --- | --- | ---- | ---- | --- | --- | --- |
| Configuring |        | BFD | for | PIM | Over | IPv4 |     |     |     |
Prerequisites
PIMmustbeenabledgloballyandonthespecificinterfacethatwillsupportBFD.
Procedure
BFD|21

1. EnableBFDsupportwiththecommandbfd.
2. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
|     | BFD setting         |     |     |     | Default | value |     | Commandtochange       |     | it  |
| --- | ------------------- | --- | --- | --- | ------- | ----- | --- | --------------------- | --- | --- |
|     | SetstheBFDdetection |     |     |     | 5       |       |     | bfd detect-multiplier |     |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
3. SwitchtotheinterfaceonwhichyouwanttoenableBFDwiththecommandinterface.
| 4.  | EnableBFDsupportwiththecommandip                  |     |     |     |     | pim-sparse |     | bfd. |     |     |
| --- | ------------------------------------------------- | --- | --- | --- | --- | ---------- | --- | ---- | --- | --- |
| 5.  | ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     |     |            |     | bfd. |     |     |
Examples
ThisexampleshowshowtoconfigurePIMandenableBFDoninterface1/1/2.
|     | switch# config      |         |           |            |             |     |     |     |     |     |
| --- | ------------------- | ------- | --------- | ---------- | ----------- | --- | --- | --- | --- | --- |
|     | switch(config)#     |         | bfd       |            |             |     |     |     |     |     |
|     | switch(config)#     |         | router    | pim        |             |     |     |     |     |     |
|     | switch(config-pim)# |         | enable    |            |             |     |     |     |     |     |
|     | switch(config-pim)# |         | exit      |            |             |     |     |     |     |     |
|     | switch(config)#     |         | interface |            | 1/1/2       |     |     |     |     |     |
|     | switch(config-if)#  |         | no        | shutdown   |             |     |     |     |     |     |
|     | switch(config-if)#  |         | ip        | address    | 10.1.1.1/24 |     |     |     |     |     |
|     | switch(config-if)#  |         | ip        | pim-sparse | enable      |     |     |     |     |     |
|     | switch(config-if)#  |         | ip        | pim-sparse | bfd         |     |     |     |     |     |
|     | switch(config-if)#  |         | exit      |            |             |     |     |     |     |     |
|     | switch(config)#     |         | exit      |            |             |     |     |     |     |     |
|     | switch# show        | bfd     |           |            |             |     |     |     |     |     |
|     | Admin status:       | enabled |           |            |             |     |     |     |     |     |
Statistics:
|     | Total number      | of          | control | packets | transmitted: |     | 7   |             |     |      |
| --- | ----------------- | ----------- | ------- | ------- | ------------ | --- | --- | ----------- | --- | ---- |
|     | Total number      | of          | control | packets | received:    |     | 8   |             |     |      |
|     | Total number      | of          | control | packets | dropped:     | 0   |     |             |     |      |
|     | Session Interface |             | VRF     |         | Source IP    |     |     | Destination | IP  | Echo |
|     | State             | Application |         |         |              |     |     |             |     |      |
------- --------- --------- ------------------- ---------------------- -------- ----
|     | -------- ------------ |     |         |     |     |     |     |          |     |            |
| --- | --------------------- | --- | ------- | --- | --- | --- | --- | -------- | --- | ---------- |
|     | 1 1/1/2               |     | default |     | N/A |     |     | 10.1.1.2 |     | enabled up |
pim
| Configuring |     |     | BFD | for | PIM Over |     | IPv6 |     |     |     |
| ----------- | --- | --- | --- | --- | -------- | --- | ---- | --- | --- | --- |
Prerequisites
AOS-CX10.07HighAvailabilityGuide|UserGuide 22

PIMmustbeenabledgloballyandonthespecificinterfacethatwillsupportBFD.
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
| BFD setting         |     |     |     | Default | value |     | Commandtochange       |     | it  |     |
| ------------------- | --- | --- | --- | ------- | ----- | --- | --------------------- | --- | --- | --- |
| SetstheBFDdetection |     |     |     | 5       |       |     | bfd detect-multiplier |     |     |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
3. SwitchtotheinterfaceonwhichyouwanttoenableBFDwiththecommandinterface.
| 4. EnableBFDsupportwiththecommandip                  |     |     |     |     | pim-sparse |     | bfd. |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | ---------- | --- | ---- | --- | --- | --- |
| 5. ReviewBFDconfigurationsettingswiththecommandsshow |     |     |     |     |            |     | bfd. |     |     |     |
Examples
ThisexampleshowshowtoconfigurePIMandenableBFDoninterface1/1/2.
| switch# config      |         |           |            |            |     |     |     |     |     |     |
| ------------------- | ------- | --------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
| switch(config)#     |         | bfd       |            |            |     |     |     |     |     |     |
| switch(config)#     |         | router    | pim6       |            |     |     |     |     |     |     |
| switch(config-pim)# |         | enable    |            |            |     |     |     |     |     |     |
| switch(config-pim)# |         | exit      |            |            |     |     |     |     |     |     |
| switch(config)#     |         | interface |            | 1/1/2      |     |     |     |     |     |     |
| switch(config-if)#  |         | no        | shutdown   |            |     |     |     |     |     |     |
| switch(config-if)#  |         | ipv6      | address    | 2130::1/64 |     |     |     |     |     |     |
| switch(config-if)#  |         | ipv6      | mld        | enable     |     |     |     |     |     |     |
| switch(config-if)#  |         | ip        | pim-sparse | enable     |     |     |     |     |     |     |
| switch(config-if)#  |         | ip        | pim-sparse | bfd        |     |     |     |     |     |     |
| switch(config-if)#  |         | exit      |            |            |     |     |     |     |     |     |
| switch(config)#     |         | exit      |            |            |     |     |     |     |     |     |
| switch# show        | bfd     |           |            |            |     |     |     |     |     |     |
| Admin status:       | enabled |           |            |            |     |     |     |     |     |     |
| Echo source         | IP:     | <none>    |            |            |     |     |     |     |     |     |
Statistics:
| Total number      | of  | control     | packets | transmitted: |     | 8   |             |     |     |      |
| ----------------- | --- | ----------- | ------- | ------------ | --- | --- | ----------- | --- | --- | ---- |
| Total number      | of  | control     | packets | received:    |     | 8   |             |     |     |      |
| Total number      | of  | control     | packets | dropped:     | 0   |     |             |     |     |      |
| Session Interface |     | VRF         |         | Source IP    |     |     | Destination | IP  |     | Echo |
| State             |     | Application |         |              |     |     |             |     |     |      |
------- --------- --------- ------------------- ----------------------------- ------
| -- ------------ |     | ------------ |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
BFD|23

| 1           | 1/1/2 |     | default |     | N/A  |     | fe80::94f1:2821:2ef:6300 |     |
| ----------- | ----- | --- | ------- | --- | ---- | --- | ------------------------ | --- |
| enabled     |       | up  | pimv6   |     |      |     |                          |     |
| Configuring |       |     | BFD     | for | VRRP |     |                          |     |
Procedure
1. EnableBFDsupportwiththecommandbfd.
2. EnableBFDonaVRRPinterfacewiththecommandbfd<IPV4-ADDR>.
3. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
|     | BFD                 | setting |     |     | Default value |     | Commandtochange       | it  |
| --- | ------------------- | ------- | --- | --- | ------------- | --- | --------------------- | --- |
|     | SetstheBFDdetection |         |     |     | 5             |     | bfd detect-multiplier |     |
multiplieronaninterface.
Setstheminimumtime 500milliseconds bfd min-echo-receive-interval
intervalbetweenreceived
BFDechopackets.
Setstheminimumtime 3000milliseconds bfd min-transmit-interval
intervalbetweentransmitted
BFDcontrolpacketsonan
interface.
Configuringthetimerstobetooaggressive(forexample,detect-multiplierof1)cansometimeslead
toBFDsessionflapsdependingupontrafficconditions.
4. ReviewBFDconfigurationsettingswiththecommandsshow bfd.
Example
EnablingBFDonaVRRPinterface.
|     | switch#                 | config    |          |                      |                  |      |      |     |
| --- | ----------------------- | --------- | -------- | -------------------- | ---------------- | ---- | ---- | --- |
|     | switch(config)#         |           | bfd      |                      |                  |      |      |     |
|     | switch#                 | interface | 1/1/1    |                      |                  |      |      |     |
|     | switch(config-if)#      |           | no       | shutdown             |                  |      |      |     |
|     | switch(config-if)#      |           | ip       | address              | 192.168.1.1/24   |      |      |     |
|     | switch(config-if)#      |           | vrrp     | 1                    | address-family   | ipv4 |      |     |
|     | switch(config-if-vrrp)# |           |          | bfd                  | 192.158.1.2      |      |      |     |
|     | switch(config-if-vrrp)# |           |          | exit                 |                  |      |      |     |
|     | switch#                 | show      | vrrp     |                      |                  |      |      |     |
|     | VRRP is                 | enabled   |          |                      |                  |      |      |     |
|     | Interface               | 1/1/1     | - Group  | 1                    | - Address-Family |      | IPv4 |     |
|     | State                   | is MASTER |          |                      |                  |      |      |     |
|     | State                   | duration  | 56 mins  | 57.826               | secs             |      |      |     |
|     | Virtual                 | IP        | address  | is 192.168.1.1       |                  |      |      |     |
|     | Virtual                 | MAC       | address  | is 00:00:5e:00:01:01 |                  |      |      |     |
|     | Advertisement           |           | interval | is                   | 1000 msec        |      |      |     |
|     | Preemption              |           | enabled  |                      |                  |      |      |     |
|     | Priority                | is        | 100      |                      |                  |      |      |     |
|     | BFD is                  | enabled   |          |                      |                  |      |      |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 24

Master Router is 192.168.1.1 (local), priority is 100
Master Advertisement interval is 1000 msec
Master Down interval is unknown
Tracked object ID is 1, and state Down
BFD Commands
bfd
Syntax
bfd
no bfd
Description
EnablesBFDsupportontheswitch.BFDisdisabledbydefault.
ThenoformofthiscommanddisablesBFDandremovesallrelatedconfigurationsettings.TodisableBFD,
butretainconfigurationsettings,usethecommandbfddisable.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingBFDsupport:
switch(config)# bfd
DisablingBFDsupportandremovingallconfigurationsettings:
switch(config)# no bfd
bfd <IPV4-ADDR>
Syntax
bfd <IPV4-ADDR>
no bfd <IPV4-ADDR>
Description
EnablesBFDunderVRRPforthespecifiedIPaddress.BFDisasynchronousandechomodeissupported.
ThenoformofthiscommanddisablesBFDunderVRRPforthespecifiedIPaddress.
Commandcontext
config-if-vrrp
Parameters
BFD|25

<IPV4-ADDR>
SpecifiestheaddressonwhichtoenableBFDinIPv4format(x.x.x.x),wherexisadecimalnumber
from0to255.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDontheaddress10.0.0.1onVRRP1:
| switch(config)#         | interface | 1/1/1            |      |
| ----------------------- | --------- | ---------------- | ---- |
| switch(config-if)#      | routing   |                  |      |
| switch(config-if)#      | vrrp      | 1 address-family | ipv4 |
| switch(config-if-vrrp)# |           | bfd 10.0.0.1     |      |
DisablingBFDontheaddress10.0.0.1onVRRP1:
| switch(config)#    | interface | 1/1/1 |     |
| ------------------ | --------- | ----- | --- |
| switch(config-if)# | routing   |       |     |
switch(config-if)#
|                         | vrrp | 1 address-family | ipv4 |
| ----------------------- | ---- | ---------------- | ---- |
| switch(config-if-vrrp)# |      | no bfd 10.0.0.1  |      |
bfd all-interfaces
Syntax
bfd all-interfaces
no bfd all-interfaces
Description
EnablesBFDonallOSPFv2orOSPFv3interfaces.
ThenoformofthiscommanddisablesBFDonallOSPFv2/OSPFv3orPIMIPv4/IPv6interfaces,excluding
thoseonwhichBFDwasenabledattheinterfacelevelwiththecommandsip ospf bfdandipv6 ospfv3
bfd.
Commandcontext
config-ospf-<INSTANCE-TAG>
config-ospfv3-<INSTANCE-TAG>
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingBFDonallOSPFv2interfaces:
| switch(config)#        | router | ospf 1             |     |
| ---------------------- | ------ | ------------------ | --- |
| switch(config-ospf-1)# |        | bfd all-interfaces |     |
DisablingBFDonallOSPFv2interfaces:
AOS-CX10.07HighAvailabilityGuide|UserGuide 26

| switch(config)# | router ospf | 1   |     |
| --------------- | ----------- | --- | --- |
switch(config-ospf-1)#
|     | no  | bfd all-interfaces |     |
| --- | --- | ------------------ | --- |
EnablingBFDonallOSPFv3interfaces:
| switch(config)#          | router ospfv3 | 1                  |     |
| ------------------------ | ------------- | ------------------ | --- |
| switch(config-ospfv3-1)# |               | bfd all-interfaces |     |
DisablingBFDonallOSPFv3interfaces:
| switch(config)#          | router ospfv3 | 1                     |     |
| ------------------------ | ------------- | --------------------- | --- |
| switch(config-ospfv3-1)# |               | no bfd all-interfaces |     |
bfd detect-multiplier
Syntax
| bfd detect-multiplier | <MULTIPLIER> |     |     |
| --------------------- | ------------ | --- | --- |
no bfd detect-multiplier
Description
SetsBFDdetectionmultiplieronaninterface.
ThenoformofthiscommandsetstheBFDdetectionmultipliertothedefaultvalueof5.
Commandcontext
config-if
Parameters
<MULTIPLIER>
SpecifiestheBFDdetectionmultiplier.Range:1to5.Default:5.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingtheBFDdetectionmultiplierto3:
| switch(config-if)# | bfd detect-multiplier |     | 3   |
| ------------------ | --------------------- | --- | --- |
SettingtheBFDdetectionmultipliertothedefaultvalue:
| switch(config-if)# | no bfd | detect-multiplier |     |
| ------------------ | ------ | ----------------- | --- |
bfd disable
Syntax
bfd disable
BFD|27

Description
DisablesBFDontheswitch,butretainsallconfigurationsettings.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DisablingBFD:
| switch(config)# | bfd disable |             |
| --------------- | ----------- | ----------- |
| bfd enable      | (Context:   | config-hsc) |
Syntax
| switch(config-hsc)# | bfd enable |        |
| ------------------- | ---------- | ------ |
| switch(config-hsc)# | no bfd     | enable |
Description
EnablesordisablesBFDforHSCfeature.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
n BFDmustbeenabledgloballytoworkforHSC.
Examples
EnablingBFDsupportforHSC:
| switch(config)#     | hsc |        |
| ------------------- | --- | ------ |
| switch(config-hsc)# | bfd | enable |
DisablingBFDsupportforHSC:
| switch(config)#     | hsc       |             |
| ------------------- | --------- | ----------- |
| switch(config-hsc)# | no        | bfd enable  |
| bfd disable         | (Context: | config-hsc) |
Syntax
| switch(config-hsc)# | bfd disable |     |
| ------------------- | ----------- | --- |
AOS-CX10.07HighAvailabilityGuide|UserGuide 28

Description
DisablesBFDforHSCfeature.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DisablingBFDsupportforHSC:
switch(config)# hsc
switch(config-hsc)# bfd disable
bfd echo disable
Syntax
bfd echo disable
no bfd echo disable
Description
DisablessupportforBFDechopackets.Echopacketsupportisenabledbydefault.
ThenoformofthiscommandenablessupportforBFDechopackets.
Togglingthisfeatureon8325or8360switchesmaycauserouteflapping.
Commandcontext
config
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDechopacketsupportonallinterfaces:
switch(config)# no bfd echo disable
DisablingBFDechopacketsupportonallinterfaces:
switch(config)# bfd echo disable
EnablingBFDechopacketsupportoninterface1/1/1:
BFD|29

| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
|     | bfd | echo disable |     |
| --- | --- | ------------ | --- |
DisablingBFDechopacketsupportoninterface1/1/1:
| switch(config)#    | interface | 1/1/1        |     |
| ------------------ | --------- | ------------ | --- |
| switch(config-if)# | no bfd    | echo disable |     |
bfd echo-src-ip-address
Syntax
| bfd echo-src-ip-address | <IPV4-ADDR> |     |     |
| ----------------------- | ----------- | --- | --- |
no bfd echo-src-ip-address
Description
SetsthesourceIPv4addressforBFDechopackets.Thisaddressisusedinallechosessions.
ThesourceIPaddressmustnotbeonthesamenetworksegmentasanyswitchinterface,otherwisealarge
numberofICMPredirectpacketsmaybesentbytheremotedevice,causingnetworkcongestion.
ThenoformofthiscommandremovesthesourceIPv4addressforBFDechopackets,whichcausesthe
switchtostopsendingechopackets.Whenavalidvalueisset,allsessionswithapeerthatiscapableof
receivingechopackets,willstarttransmittingechopackets.BFDcontrolsessionscontinuetorun
concurrentlywithechopackets.
Commandcontext
config
Parameters
<IPV4-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingthesourceIPaddressto198.51.100.1:
| switch(config)# | bfd echo-src-ip-address |     | 198.51.100.1 |
| --------------- | ----------------------- | --- | ------------ |
RemovingthesourceIPaddress:
| switch(config)# | no bfd | echo-src-ip-address |     |
| --------------- | ------ | ------------------- | --- |
bfd min-echo-receive-interval
Syntax
AOS-CX10.07HighAvailabilityGuide|UserGuide 30

bfd min-echo-receive-interval <INTERVAL>
no bfd min-echo-receive-interval
Description
SetstheminimumtimeintervalbetweenreceivedBFDechopackets.
ThenoformofthiscommandsetstheminimumintervalbetweenreceivedBFDechopacketstothedefault
valueof500milliseconds.
Commandcontext
config
Parameters
<INTERVAL>
Specifiestheminimumreceptionintervalinmilliseconds.Avalueof0meansthattheswitchdoesnot
supportreceptionofBFDechopackets.Range:0,50to1000.Default:500.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingtheminimumreceptionintervalto1000milliseconds:
switch(config)# bfd min-echo-receive-interval 1000
Settingtheminimumreceptionintervaltothedefaultvalue:
switch(config)# no bfd min-echo-receive-interval
bfd min-receive-interval
Syntax
bfd min-receive-interval <INTERVAL>
no bfd min-receive-interval
Description
SetstheminimumtimeintervalbetweenreceivedBFDcontrolpacketsonaninterface.
ThenoformofthiscommandsetstheminimumintervalbetweenreceivedBFDcontrolpacketstothe
defaultvalueof3000milliseconds.
Commandcontext
config-if
Parameters
<INTERVAL>
Specifiestheminimumreceiveintervalinmilliseconds.Avalueof0meansthattheswitchdoesnot
supportreceptionofBFDcontrolpackets.Range:500to20000.3000. Default:3000.
Authority
BFD|31

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingtheminimumreceiveintervalto1000milliseconds:
switch(config-if)# bfd min-receive-interval 1000
Settingtheminimumreceiveintervaltothedefaultvalue:
switch(config-if)# no bfd min-receive-interval
bfd min-transmit-interval
Syntax
bfd min-transmit-interval <INTERVAL>
no bfd min-transmit-interval
Description
SetstheminimumtimeintervalbetweentransmittedBFDcontrolpacketsonaninterface.
ThenoformofthiscommandsetstheminimumintervalbetweentransmittedBFDcontrolpacketstothe
defaultvalueof3000ms.
Commandcontext
config-if
Parameters
<INTERVAL>
Specifiestheminimumtransmitintervalinmilliseconds.Range:500to20000(6300,6400,8360,8400).
50to20000(8320,8325).Default:3000.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
n Iftheminimumtimeintervalissetbetween500msand1000ms,thenbfd detect-multipliermustbe
settoatleast3.
n Ifbfd detect-multiplierissetto1,thentheminimumtransmitintervalmustbesettoatleast3000
ms.
n Whenevertheminimumtimeintervalissettoavaluelessthan1000ms,BFDautomaticallyadjuststhe
transmissionintervalto1000msifanyofthefollowingconditionsapply:
o Thesessionisoperatinginasynchronousmodeandechoisenabled.
o Thesessionstateisinanyotherstatethanup.
AsdescribedinRFC5880,thisbehavioroccursbecauseBFDechoprovidesquickdetectionwhichallows
theBFDasynchronoussessiontoloweritstraffic/resourcerequirements.
Examples
AOS-CX10.07HighAvailabilityGuide|UserGuide 32

Settingtheminimumtransmitintervalto500ms:
| switch(config-if)# |     | bfd min-transmit-interval |     | 500 |
| ------------------ | --- | ------------------------- | --- | --- |
Settingtheminimumtransmitintervaltothedefaultvalue:
| switch(config-if)# |                | no bfd | min-transmit-interval |     |
| ------------------ | -------------- | ------ | --------------------- | --- |
| clear              | bfd statistics |        |                       |     |
Syntax
| clear bfd | statistics | [session | <ID>] |     |
| --------- | ---------- | -------- | ----- | --- |
Description
ClearsstatisticsforallBFDsessionsorforaspecificBFDsession.
Commandscontext
Manager(#)
Parameters
| session | <ID> |     |     |     |
| ------- | ---- | --- | --- | --- |
SpecifiesasessionID.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ClearingstatisticsforallBFDsessions:
| switch# | clear | bfd statistics |     |     |
| ------- | ----- | -------------- | --- | --- |
ClearingstatisticsforBFDsession1:
| switch# | clear | bfd statistics | session 1 |     |
| ------- | ----- | -------------- | --------- | --- |
| ip ospf | bfd   |                |           |     |
Syntax
| ip ospf    | bfd |     |     |     |
| ---------- | --- | --- | --- | --- |
| no ip ospf | bfd |     |     |     |
Description
EnablesBFDforOSPFv2onthecurrentinterface.TheinterfacemusthaveOSPFv2enabledonit.This
overridestheglobalsettingsdefinedwiththecommandbfd all-interfaces.
Thenoformofthiscommandsetsthecurrentinterfacetotheglobalsettingsdefinedwiththecommand
bfd all-interfaces.
BFD|33

Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDoninterface1/1/1:
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | ip ospf   | bfd   |
DisablingBFDoninterface1/1/1:
| switch(config)#     | interface | 1/1/1    |
| ------------------- | --------- | -------- |
| switch(config-if)#  | no ip     | ospf bfd |
| ip ospf bfd disable |           |          |
Syntax
ip ospf bfd disable
Description
DisablesBFDforOSPFv2onthecurrentinterface.Thisoverridestheglobalsettingsdefinedwiththe
| commandbfd all-interfaces. |     |     |
| -------------------------- | --- | --- |
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDoninterface1/1/1:
| switch(config)#    | interface | 1/1/1       |
| ------------------ | --------- | ----------- |
| switch(config-if)# | ip ospf   | bfd disable |
ip route bfd
Syntax
ip route <DEST-IPV4-ADDR>/<NETMASK> [<NEXT-HOP-IP-ADDR> | <INTERFACE>] [bfd]
Description
AOS-CX10.07HighAvailabilityGuide|UserGuide 34

EnablesordisablesBFDonthespecifiedstaticroute.TodisableBFD,issuethecommandwithoutthebfd
option.
Commandcontext
config
Parameters
<DEST-IPV4-ADDR>
SpecifiesaroutedestinationinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
<NETMASK>
SpecifiesthenumberofbitsintheaddressmaskinCIDRformat(x),wherexisadecimalnumberfrom0
to128.
<NEXT-HOP-IP-ADDR>
SpecifiesthenexthopaddressforreachingthedestinationinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255.
<INTERFACE>
Specifiesthenexthopasanoutgoinginterface.
bfd
EnablesBFDonthestaticroute.OmitthisparametertodisableBFD.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDonastaticroute:
| switch(config)#    | interface  | 1/1/1       |     |
| ------------------ | ---------- | ----------- | --- |
| switch(config-if)# | ip address | 20.1.1.2/24 |     |
switch(config-if)# no shutdownswitch(config-if)#routingswitch(config-if)# exit
| switch(config)# | ip route | 192.0.0.0/8 | 20.1.1.1 bfd |
| --------------- | -------- | ----------- | ------------ |
DisablingBFDonastaticroute:
| switch(config)# | ip route | 192.0.0.0/8 | 20.1.1.1 |
| --------------- | -------- | ----------- | -------- |
EnablingBFDonastaticroute:
| switch(config)#    | interface  | 1/1/1       |     |
| ------------------ | ---------- | ----------- | --- |
| switch(config-if)# | ip address | 20.1.1.2/24 |     |
switch(config-if)# no shutdownswitch(config-if)#routingswitch(config-if)# exit
| switch(config)# | ip route | 192.0.0.0/8 | 1/1/1 bfd |
| --------------- | -------- | ----------- | --------- |
DisablingBFDonastaticroute:
| switch(config)# | ip route | 192.0.0.0/8 | 1/1/1 |
| --------------- | -------- | ----------- | ----- |
| ipv6 ospfv3     | bfd      |             |       |
BFD|35

Syntax
ipv6 ospfv3 bfd
no ipv6 ospfv3 bfd
Description
EnablesBFDforOSPFv3onthecurrentinterface.TheinterfacemusthaveOSPFv3enabledonit.This
overridestheglobalsettingsdefinedwiththecommandbfd all-interfaces.
Thenoformofthiscommandsetsthecurrentinterfacetotheglobalsettingsdefinedwiththecommand
bfd all-interfaces.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingBFD:
switch(config-if)# ipv6 ospfv3 bfd
DisablingBFD:
switch(config-if)# no ipv6 ospfv3 bfd
ipv6 ospfv3 bfd disable
Syntax
ipv6 ospfv3 bfd disable
Description
DisablesBFDonthecurrentOSPFv3interface.Thisoverridestheglobalsettingsdefinedwiththecommand
bfd all-interfaces.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingBFDoninterface1/1/1:
switch(config)# interface 1/1/1switch(config-if)#routedswitch(config-if)# ipv6 ospfv3
bfd disable
AOS-CX10.07HighAvailabilityGuide|UserGuide 36

| neighbor | fall-over |     | bfd |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- | --- | --- |
Syntax
| neighbor    | {<IP-ADDRESS>|<PEER-GROUP-NAME>} |     |     |     | fall-over |           | bfd |
| ----------- | -------------------------------- | --- | --- | --- | --------- | --------- | --- |
| no neighbor | {<IP-ADDRESS>|<PEER-GROUP-NAME>} |     |     |     |           | fall-over | bfd |
Description
EnablesBGPtoregisterwithBFDtoreceivefastpeeringsessiondeactivationmessagesfromBFD.
ThenoformofthiscommanddisablesBGPforBFD.
Currently,BFDissupportedonlywithIPv4neighbors.SupporttoenableBFDwithIPv6neighborswillbeaddedina
futurerelease.
Commandcontext
config-router
Parameters
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
<PEER-GROUP-NAME>
Specifiesapeergroup.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| switch(config-router)# |     |     | neighbor    | 1.1.1.1 | fall-over    |           |     |
| ---------------------- | --- | --- | ----------- | ------- | ------------ | --------- | --- |
| switch(config-router)# |     |     | no neighbor |         | 1.1.1.1      | fall-over | bfd |
| switch(config-router)# |     |     | neighbor    | PG      | fall-over    |           |     |
| switch(config-router)# |     |     | no neighbor |         | PG fall-over |           | bfd |
| show bfd               |     |     |             |         |              |           |     |
Syntax
| show bfd | [session | <ID>] | [all-vrfs | | vrf | <NAME>] | [vsx-peer] |     |
| -------- | -------- | ----- | --------- | ----- | ------- | ---------- | --- |
Description
ShowsinformationforallBFDsessionsorforaspecificBFDsession.
Commandscontext
| Manager (#) |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
Parameters
| session | <ID> |     |     |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- | --- |
SessionID.
all-vrfs
BFD|37

AllVRFs.
vrf <NAME>
SpecifiesthenameofaVRF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
PossiblevaluesforStateare:
n Up
n Down
n AdminDown
n Init
| PossiblevaluesforLocal | diagnosticandRemote |     | diagnosticare: |     |     |
| ---------------------- | ------------------- | --- | -------------- | --- | --- |
n Controldetectiontimeexpired(1):ThesessionhasstoppedreceivingBFDcontrolpacketsfromthepeer
afteronedetectiontime.
n Echofunctionfailed:ThesessionhasstoppedreceivingBFDEchopackets,sothesessionwasdeclared
Down.
n Neighborsignaledsessiondown:ApacketfromthepeerwasreceivedwitheitherAdminDownorDown
state.
n Forwardingplanereset:Notsetinthisrelease.
n Pathdown:TheforwardingpathwhenDown.
n Concatenatedpathdown:Notsetinthisrelease.
n Administrativelydown:TheadministratorhasdisabledBFD.
Reverseconcatenatedpathdown:Notsetinthisrelease.
n
Examples
ShowinginformationforallBFDsessions:
| switch# show | bfd          |     |     |     |     |
| ------------ | ------------ | --- | --- | --- | --- |
| Admin status | : Enabled    |     |     |     |     |
| Echo source  | IP : 2.2.2.2 |     |     |     |     |
Statistics:
| Total Number      | of Control | Packets Transmitted | : 42 |             |     |
| ----------------- | ---------- | ------------------- | ---- | ----------- | --- |
| Total Number      | of Control | Packets Received    | : 42 |             |     |
| Total Number      | of Control | Packets Dropped     | : 0  |             |     |
| Session Interface | VRF        | Source IP           |      | Destination | IP  |
| Echo              | State      | Application         |      |             |     |
------- --------- --------- ------------------------------- ------------------------
| ------- -------- | -------- | ------------ |     |            |     |
| ---------------- | -------- | ------------ | --- | ---------- | --- |
| 1 vlan10         | blue     | 10.10.10.1   |     | 10.10.10.2 |     |
| disabled         | up       | ospf         |     |            |     |
| 1 vlan10         | blue     | N/A          |     | 10.10.10.2 |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 38

|     | disabled | up    | static_routes |     |     |            |     |
| --- | -------- | ----- | ------------- | --- | --- | ---------- | --- |
| 2   | vlan40   | red   | 40.10.10.1    |     |     | 40.10.10.2 |     |
|     | disabled | up    | ospf          |     |     |            |     |
| 3   | vlan30   | red   | 30.10.10.1    |     |     | 30.10.10.2 |     |
|     | disabled | up    | ospf          |     |     |            |     |
| 4   | vlan20   | blue  | 20.10.10.1    |     |     | 20.10.10.2 |     |
|     | disabled | up    | ospf          |     |     |            |     |
| 5   | vlan50   | black | 50.10.10.1    |     |     | 50.10.10.2 |     |
|     | disabled | up    | ospf          |     |     |            |     |
| 6   | vlan60   | black | 60.10.10.1    |     |     | 60.10.10.2 |     |
|     | disabled | up    | ospf          |     |     |            |     |
7 vlan10 blue fe80::409:7380:a62:2400 fe80::409:7380:a49:a200
|     | disabled | up  | ospfv3 |     |     |     |     |
| --- | -------- | --- | ------ | --- | --- | --- | --- |
ShowinginformationforBFDsession1:
| switch#     | show bfd    | session | 1         |     |     |     |     |
| ----------- | ----------- | ------- | --------- | --- | --- | --- | --- |
| BFD Session | Information |         | – Session | 1   |     |     |     |
VRF: blue
| Min Tx              | Interval      | (msec) | : 10000 |     |     |     |     |
| ------------------- | ------------- | ------ | ------- | --- | --- | --- | --- |
| Min Rx              | Interval      | (msec) | : 10000 |     |     |     |     |
| Min Echo            | Rx Interval   | (msec) | : 700   |     |     |     |     |
| Detect              | Multiplier    | : 3    |         |     |     |     |     |
| Application         | : ospf        |        |         |     |     |     |     |
| Local Discriminator |               | : 1    |         |     |     |     |     |
| Remote              | Discriminator | :      | 1       |     |     |     |     |
Echo : Enabled
| Local Diagnostic |             | : no_diagnostic       |     |     |     |     |     |
| ---------------- | ----------- | --------------------- | --- | --- | --- | --- | --- |
| Remote           | Diagnostic: | administratively_down |     |     |     |     |     |
| State flaps:     | 0           |                       |     |     |     |     |     |
Interface Source IP Destination IP State Pkt In Pkt Out Pkt Drop
--------- --------------- --------------- ---------- -------- -------- --------
| 1/1/1 | 100.100.100.100 |     | 100.100.100.101 |     | Up  | 100 101 | 0   |
| ----- | --------------- | --- | --------------- | --- | --- | ------- | --- |
ShowinginformationforallBFDsessionsrelatedtoaparticularVRFinthesystem:
| switch#       | show bfd | vrf blue  |     |     |     |     |     |
| ------------- | -------- | --------- | --- | --- | --- | --- | --- |
| Admin status: | enabled  |           |     |     |     |     |     |
| Echo source   | IP:      | 100.1.1.1 |     |     |     |     |     |
Statistics:
| Total number | of        | control | packets     | transmitted: | 2226 |             |     |
| ------------ | --------- | ------- | ----------- | ------------ | ---- | ----------- | --- |
| Total number | of        | control | packets     | received:    | 2222 |             |     |
| Total number | of        | control | packets     | dropped:     | 0    |             |     |
| Session      | Interface | VRF     | Source      | IP           |      | Destination | IP  |
|              | Echo      | State   | Application |              |      |             |     |
------- --------- --------- ------------------------------- ------------------------
| ------- | -------- | -------- | ------------  |     |     |            |     |
| ------- | -------- | -------- | ------------- | --- | --- | ---------- | --- |
| 1       | vlan10   | blue     | 10.10.10.1    |     |     | 10.10.10.2 |     |
|         | disabled | up       | ospf          |     |     |            |     |
| 1       | vlan10   | blue     | N/A           |     |     | 10.10.10.2 |     |
|         | disabled | up       | static_routes |     |     |            |     |
| 4       | vlan20   | blue     | 20.10.10.1    |     |     | 20.10.10.2 |     |
|         | disabled | up       | ospf          |     |     |            |     |
7 vlan10 blue fe80::409:7380:a62:2400 fe80::409:7380:a49:a200
|          | disabled  | up  | ospfv3 |     |     |     |     |
| -------- | --------- | --- | ------ | --- | --- | --- | --- |
| show bfd | interface |     |        |     |     |     |     |
BFD|39

Syntax
| show bfd interface |     | <NAME> |     |     |     |     |     |
| ------------------ | --- | ------ | --- | --- | --- | --- | --- |
Description
ShowsinformationforallBFDsessionsrelatedtothespecifiedinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
interface <NAME>
Specifiesaninterface.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShowinginformationforallBFDsessionsrelatedtothespecifiedinterface:
switch#
|                      | show bfd       | interface | vlan10    |     |     |     |     |
| -------------------- | -------------- | --------- | --------- | --- | --- | --- | --- |
| BFD session          | information    |           | - Session |     | 1   |     |     |
| Min Tx               | interval       | (msec):   | 3000      |     |     |     |     |
| Min Rx               | interval       | (msec):   | 3000      |     |     |     |     |
| Min echo             | Rx interval    |           | (msec):   | 500 |     |     |     |
| Detect               | multiplier:    | 5         |           |     |     |     |     |
| Application:         | ospf           |           |           |     |     |     |     |
| Local discriminator: |                |           | 13211     |     |     |     |     |
| Remote               | discriminator: |           | 13211     |     |     |     |     |
Echo: disabled
| Local diagnostic: |             | no_diagnostic |        |     |          |             |     |
| ----------------- | ----------- | ------------- | ------ | --- | -------- | ----------- | --- |
| Remote            | diagnostic: | no_diagnostic |        |     |          |             |     |
| State flaps:      | 0           |               |        |     |          |             |     |
| Interface         | Source      | IP            |        |     |          | Destination | IP  |
| State             |             | Pkt           | Rx Pkt | Tx  | Pkt drop |             |     |
--------- --------------------------------------- ----------------------------------
| ----- ------------ |            | -------- |     | -------- | -------- |            |     |
| ------------------ | ---------- | -------- | --- | -------- | -------- | ---------- | --- |
| vlan10             | 10.10.10.1 |          |     |          |          | 10.10.10.2 |     |
| up                 |            | 453      | 455 |          | 0        |            |     |
===============================================
| BFD session          | information    |         | - Session |     | 1   |     |     |
| -------------------- | -------------- | ------- | --------- | --- | --- | --- | --- |
| Min Tx               | interval       | (msec): | 3000      |     |     |     |     |
| Min Rx               | interval       | (msec): | 3000      |     |     |     |     |
| Min echo             | Rx interval    |         | (msec):   | 500 |     |     |     |
| Detect               | multiplier:    | 5       |           |     |     |     |     |
| Application:         | static_routes  |         |           |     |     |     |     |
| Local discriminator: |                |         | 13211     |     |     |     |     |
| Remote               | discriminator: |         | 13211     |     |     |     |     |
Echo: disabled
| Local diagnostic: |             | no_diagnostic |        |     |          |             |     |
| ----------------- | ----------- | ------------- | ------ | --- | -------- | ----------- | --- |
| Remote            | diagnostic: | no_diagnostic |        |     |          |             |     |
| State flaps:      | 0           |               |        |     |          |             |     |
| Interface         | Source      | IP            |        |     |          | Destination | IP  |
| State             |             | Pkt           | Rx Pkt | Tx  | Pkt drop |             |     |
--------- --------------------------------------- ----------------------------------
| ----- ------------ |     | -------- |     | -------- | -------- |     |     |
| ------------------ | --- | -------- | --- | -------- | -------- | --- | --- |
AOS-CX10.07HighAvailabilityGuide|UserGuide 40

| vlan10 | N/A |     |     |     |     | 10.10.10.2 |     |
| ------ | --- | --- | --- | --- | --- | ---------- | --- |
| up     |     | 453 | 455 |     | 0   |            |     |
===============================================
| BFD session          | information    |         | - Session |     | 7   |     |     |
| -------------------- | -------------- | ------- | --------- | --- | --- | --- | --- |
| Min Tx               | interval       | (msec): | 3000      |     |     |     |     |
| Min Rx               | interval       | (msec): | 3000      |     |     |     |     |
| Min echo             | Rx interval    |         | (msec):   | 500 |     |     |     |
| Detect               | multiplier:    | 5       |           |     |     |     |     |
| Application:         |                | ospfv3  |           |     |     |     |     |
| Local discriminator: |                |         | 1402      |     |     |     |     |
| Remote               | discriminator: |         | 1402      |     |     |     |     |
Echo: disabled
| Local diagnostic: |             | no_diagnostic |        |     |          |             |     |
| ----------------- | ----------- | ------------- | ------ | --- | -------- | ----------- | --- |
| Remote            | diagnostic: | no_diagnostic |        |     |          |             |     |
| State flaps:      |             | 0             |        |     |          |             |     |
| Interface         | Source      | IP            |        |     |          | Destination | IP  |
| State             |             | Pkt           | Rx Pkt | Tx  | Pkt drop |             |     |
--------- --------------------------------------- ----------------------------------
| ----- ------------ |                         | -------- |     | -------- | -------- |                         |     |
| ------------------ | ----------------------- | -------- | --- | -------- | -------- | ----------------------- | --- |
| vlan10             | fe80::409:7380:a62:2400 |          |     |          |          | fe80::409:7380:a49:a200 |     |
| up                 |                         | 58       | 58  |          | 0        |                         |     |
show hsc
Syntax
show hsc
Description
Displaysconnectioninformationfortheremotecontroller.
Commandcontext
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Displayingconnectioninformationfortheremotecontroller:
| switch#         | show | hsc     |            |     |               |     |     |
| --------------- | ---- | ------- | ---------- | --- | ------------- | --- | --- |
| BFD status      | :    | Enabled |            |     |               |     |     |
| Controller      | IP   | Port    | Connection |     | Connection    |     |     |
| address         |      |         | status     |     | state         |     |     |
| --------------- |      | ------- | ---------- |     | ------------- |     |     |
| 192.168.16.17   |      | 6640    | UP         |     | ACTIVE        |     |     |
| 192.168.16.17   |      | 6650    | UP         |     | IDLE          |     |     |
| 192.168.16.17   |      | 6660    | DOWN       |     | BACKOFF       |     |     |
BFD|41

Chapter 4
ERPS
ERPS
ERPSsupportedonthefollowingswitches:
n 6300
n 6400
n 8320
n 8325
n 8360
n 8400
EthernetRingProtectionSwitching(ERPS)isaprotocoldefinedbytheInternationalTelecommunication
Union-TelecommunicationStandardizationSector(ITU-T)toeliminateloopsatLayer2.Becausethe
standardnumberisITU-TG.8032/Y1344,ERPSisalsocalledG.8032.ERPSdefinesRingAutoProtection
Switching(RAPS)ProtocolDataUnits(PDUs)andprotectionswitchingmechanisms.
ERPShastwoversions:
n ERPSv1releasedbyITU-TinJune2008,and
n ERPSv2releasedinAugust2010.
EPRSv2,fullycompatiblewithERPSv1,providesthefollowingenhancedfunctions:
n Multi-ringtopologies,suchasintersectingrings
n RAPSPDUtransmissiononnon-virtual-channels(NVCs)insub-rings
n ForcedSwitch(FS)andManualSwitch(MS)
n Revertiveandnon-revertiveswitching
Generally,redundantlinksareusedonanEthernetswitchingnetworksuchasaringnetworktoprovidelink
backupandenhancenetworkreliability.Theuseofredundantlinks,however,mayresultincreatingnetwork
loops,causingbroadcaststorms,andrenderingtheMACaddresstableunstable.Asaresult,communication
qualitydeteriorates,andcommunicationservicesmayevenbeinterrupted.
Ethernetnetworksdemandfasterprotectionswitching.STPdoesnotmeettherequirementforfast
convergence.
ERPS,astandardITU-Tprotocol,preventloopsonringnetworks.Itoptimizesdetectionandperformsfast
convergence.ERPSallowsallERPS-capabledevicesonaringnetworktocommunicate.
BenefitsofERPSinclude:
n Preventsbroadcaststormsandimplementsfasttrafficswitchoveronanetworkwherethereareloops.
n Providesfastconvergenceandcarrier-classreliability.
n AllowsallERPS-capabledevicesonaringnetworktocommunicate.
Limitations, Conflicts, or Exclusions
AOS-CX10.07HighAvailabilityGuide| UserGuide 42

n ERPScoexistswithSTPwiththefollowinglimitations:
o RingportsareexcludedfromSTPoperation.
ItisnotrecommendedtoconfigureanySpanningTreeinterfacecontext-relatedcommandsonthe
ERPSringport.BeforeconfiguringringportensureallSpanningTreeinterfacecontext-related
commandsareremovedfromtheinterface.
o WithVSX,STPoperatesonISLportsdespitebeingringports.
o OnlydefaultMSTPinstance(CIST)issupportedwithERPS.
o ERPScannotbeenabledwithmorethan252RPVSTinstances.Thislimitationisapplicableforall
supportedplatforms.
n DynamicVLANs(MVRP)arenotsupportedonERPSringports.
n MCLAGconfigurationonERPSringportsisnotsupported.
n ERPSandloopprotectarenotsupportedonthesameport.Ifenabledtogether,thebehavioris
undefined.
n ActiveGWisnotrecommendedonVLANsthatarenotpartofVSX-LAGs.ThiscanleadtotwoactiveGWs
onaringwhenISLfailsasSVIsofthoseVLANsarenotshutdownonVSX-secondary.Thisresultsin
frequentMACmovesforgatewayMACaddressacrossringnodes.
n Onsuchdeployments,wheregatewaysareservingVLANsacrossthering,VRRPisrecommended.
n Multiplemajor-rings(MRs)arenotsupportedinaVSXsolutionsinceVSX-ISLcanbepartofamaximum
ofoneMR.
n TopologiesmusthaveeitherasubringorMCLAGtoconnectdownstreamswitchesandnotamixof
both.
n SquareVSXtopologycannotbepartofsingleMRsinceMCLAGisnotsupportedasaringport.
n OnswitcheswithbothERPSandSTPenabled,aloopinvolvingringportsandSTPportsisnotprotected.
n RedundantlinksfromdownstreamswitchestoringnodesmustbeVSX-LAGs.
n Donotenableloop-protect,MVRP,andMCLAGonERPSringports.EnablingthesefeaturesonanERPS
ringportleadstoundefinedbehavior.
n HAlimitations:
o WithUDLD,redundancyswitchoverisnothitlessandresultsintrafficloss.
o UDLDcanbeusedonlyonringnodesthatareconnectedthroughrepeaters.Thislimitationisnot
applicablewithVSXbecauseUDLDdoesnothavetobeenabledonISL,andLANtrafficcanreacha
ringthroughISL.ThislimitationisapplicableforVSFswitchover.
n Increasetheguardintervalto1-2secondstopreventEthernetringnodesfromactingonoutdatedR-APS
messagesandthepossibilityofformingaclosedloop.
n Avoidusingvlan trunk allowed alloninterconnectionlinkinterfaces.Doingsocausesloopingofthe
subringR-APSpacketandcausesundefinedbehaviorforallringsconfiguredontheswitch.
n ProtectedVLANsinasubringthatarenotpartofamajorringareallowedtoaccommodateguestVLANs.
ClientsonthoseVLANscanonlyreachthegatewayforfurtherrouting.Theseclientscannotreachother
clientsonthesameVLAN.SuchVLANsmusthaveVRRPenabledgatewaysonbothringinterconnection
nodes.
n RPLneighborconfigurationontheringsincreasesconvergencetimetotheorderof300msacrosslink
failures.Networkscriticalofconvergencetimecarryingreal-timetrafficmustavoidRPLneighbor
configuration.
ERPS|43

n Usersmustexplicitlyhandlethedynamicchangeofaportfromtrunktoaccessinthefollowingcases:
o DefaultingaLAGinterfacethatispartofanERPSring.
o SwappingorremovinganISLlinkfromaVSXthatispartofanERPSring.
ThesecasesleadtotrafficlossintheERPSring,sobeforeperforminganyoftheseactions,usersmust
considertheprotocolusedontheinterface.IfitispartofanERPSring,configuretheportbacktotrunk
fromaccess.
n Enablingip neighbor-floodonSVIinterfacesisrecommendedforfasterconvergenceofroutedtraffic.
Thisisnotsupportedon6300or6400switches.
n SNMPisnotsupportedwithERPS.
n VLANsthathaveringportsmustbeincludedinprotectedVLANlistsofatleastoneERPSinstance.
IfVLANswithringportsarenotincludedinprotectedVLANlists,theVLAN-portcombinationisnot
managedbyERPSorSTPandtheportstateoftheVLANbecomesundefinedcausingaloopinthe
network.
ERPS Commands
clear erps ring <ringid> instance <id>
Syntax
clear erps ring <ringid> instance <id>
Description
Removestheprotectionswitchingandtriggersreversionbothinrevertiveandnon-revertiveoperation.This
commandwillnotchangetheconfiguredrevertiveoperationmode.
Commandcontext
Operator(>)orManager(#)
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239.
<id>
Required,specifiestheIDoftheringinstance.Range:1-2.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Removestheprotectionswitchingandtriggersreversionforring3,instance2:
switch# clear erps ring 3 instance 2
AOS-CX10.07HighAvailabilityGuide|UserGuide 44

clear erps statistics
Syntax
clear erps statistics [ring <id>] [instance <id>]
Description
ThiscommandclearstheERPSstatisticsforaringoraringinstance.
Commandcontext
Operator(>)orManager(#)
Parameters
<ringid>
Optional,specifiestheIDofthering.Range:1-239.
<id>
Optional,specifiestheIDoftheringinstance.Range:1-64.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ClearERPSstatisticsforring1:
switch# clear erps statistics ring 1
ClearERPSstatisticsforinstance1ofring1:
switch# clear erps statistics ring 1 instance 1
erps ring
Syntax
erps ring <ringid>
no erps ring <ringid>
Description
ThiscommandcreatesanERPSringwithagivenID.
Thenoformofthiscommandremovesalltheconfigurationsofthering,includinginstances.
Commandcontext
config
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
Authority
ERPS|45

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreateanERPSring:
switch(config)# erps ring 2
switch(config-ring-2)#
RemoveanERPSring:
switch(config)# no erps ring 2
switch(config-ring-2)#
erps ring <ringid> <port0|port1> interface
Syntax
erps ring <ringid>
<port0|port1> interface <ifname>
Description
ThiscommandconfigurestheERPSringmemberport.AnL2interfaceintheswitchisassociatedtooneof
thetwomemberportsofanERPSring.Incaseofaninterconnectionnode,onlyport0isapplicableforthe
sub-ring.
ThenoformofthiscommandremovestheassociationoftheringporttotheL2interfaceontheswitch.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<port0>
Required,setport0ofthering.
<port1>
Required,setport1ofthering.
<ifname>
Required,interfacename(string).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguretheERPSringmemberport:
switch(config)# erps ring 3
switch(config-erps-ring-3)# port0 interface 1/1/1
RemovetheassociationoftheringporttotheL2interfaceontheswitch:
AOS-CX10.07HighAvailabilityGuide|UserGuide 46

| switch(config)#             | erps     | ring 3      |     |
| --------------------------- | -------- | ----------- | --- |
| switch(config-erps-ring-3)# |          | no port0    |     |
| erps ring                   | <ringid> | description |     |
Syntax
| erps ring | <ringid> |     |     |
| --------- | -------- | --- | --- |
description <line>
Description
Thiscommandaddsdescriptiveinformationtohelpadministratorsandoperatorsunderstandthepurpose
ofaring.1-64printableASCIIcharactersareallowed.
Thenoformofthiscommandremovestheringinstancedescription.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<line>
Required,specifiesthedescriptiontext.Maximumlengthis64characters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Adddescriptiveinformationtoaring:
| switch(config)#            | erps | ring 3      |              |
| -------------------------- | ---- | ----------- | ------------ |
| switch(config-erps-ring-3) |      | description | HPE RnD ring |
Removedescriptiveinformationfromaring:
| switch(config)#            | erps     | ring 3         |     |
| -------------------------- | -------- | -------------- | --- |
| switch(config-erps-ring-3) |          | no description |     |
| erps ring                  | <ringid> | guard-interval |     |
Syntax
| erps ring      | <ringid> |                   |     |
| -------------- | -------- | ----------------- | --- |
| guard-interval |          | <10 milliseconds> |     |
Description
GuardtimerisusedinnodesrecoveringfromalocalfailuretoavoidloopsduetoearlierSignalFail(SF)
messagesthatmaybeinthering.
ERPS|47

Theconfigurationspecifiestheguardtimerdurationinunitsof10ms.Thetimerperiodmustbegreater
thanthemaximumexpectedforwardingdelayinwhichanR-APSmessagetraversestheentirering.The
defaultvalueis50.
Thenoformofthiscommandremovestheconfiguredvalueoftheguardintervalandsetsittothedefault
valueof50.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<10 milliseconds>
Required,specifiestheguardtimerdurationinunitsof10ms.Default:50.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Specifytheguardtimerduration:
switch(config)# erps ring 3
switch(config-erps-ring-3)# guard-interval 100
Removetheconfiguredvalueoftheguardintervalandsetittothedefaultvalueof50:
switch(config)# erps ring 3
switch(config-erps-ring-3)# no guard-interval
erps ring <ringid> hold-off-interval
Syntax
erps ring <ringid>
hold-off-interval <100 milliseconds>
Description
Specifieshold-offintervalinunitsof100ms.Ifspecified,adefectisnotreportedimmediately.Instead,the
hold-offtimerisstarted.Onexpirationofthetimer,ifthedefectstillexists,itisreportedtoprotection
switching.Thedefaultvalueforhold-offtimeris0.
Thenoformofthiscommandremovestheconfiguredvalueofthehold-offintervalandsetsittothe
defaultvalueof0.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<100 milliseconds>
AOS-CX10.07HighAvailabilityGuide|UserGuide 48

Required,specifiesthehold-offintervalinunitsof100ms.Default:0.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Specifythehold-offinterval:
switch(config)# erps ring 3
switch(config-erps-ring-3)# hold-off-interval 100
Removetheconfiguredvalueofthehold-offintervalandsetittothedefaultvalueof0:
switch(config)# erps ring 3
switch(config-erps-ring-3)# no hold-off-interval
erps ring <ringid> instance
Syntax
erps ring <ringid>
instance <id>
Description
OnacommonERPSnetwork,aphysicalringcanbeconfiguredwithasingleERPSring,andonlyoneblocked
portcanbespecifiedinthering.WhentheERPSringisinnormalstate,theblockedportprohibitsallservice
packetsfrompassingthrough.Asaresult,allservicedataistransmittedthroughonepathovertheERPS
ring,andtheotherlinkontheblockedportbecomesidle,leadingtoineffectiveuseofbandwidth.
Toimprovelinkuseefficiency,logicalringscanbeconfiguredinthesamephysicalringintheERPSmulti-
instance.AportmayhavedifferentrolesindifferentERPSringsanddifferentERPSringsusedifferent
controlVLANs.
AnERPSringmustbeconfiguredwithanERPinstance,andeachERPinstancespecifiesarangeofVLANs.
ThetopologycalculatedforaspecificERPSringonlytakeseffectintheERPSring.DifferentVLANscanuse
separatepaths,implementingtrafficloadbalancingandlinkbackup.
Thenoformofthiscommandremovestheinstanceofthering.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Createaringinstance:
ERPS|49

| switch(config)#        |     | erps | ring | 3        |     |     |
| ---------------------- | --- | ---- | ---- | -------- | --- | --- |
| switch(config-ring-3)# |     |      |      | instance | 2   |     |
Removearinginstance:
| switch(config)#        |               | erps | ring     | 3           |                   |     |
| ---------------------- | ------------- | ---- | -------- | ----------- | ----------------- | --- |
| switch(config-ring-3)# |               |      |          | no instance | 2                 |     |
| erps                   | ring <ringid> |      | instance |             | <id> control-vlan |     |
Syntax
| erps | ring <ringid> |      |              |     |       |     |
| ---- | ------------- | ---- | ------------ | --- | ----- | --- |
|      | instance      | <id> | control-vlan |     | <vid> |     |
Description
Thiscommandaddsacontrol-channelVLANtoaringinstance.InanERPSring,thecontrolVLANshouldbe
usedonlytoforwardRAPSPDUsandnotservicepackets.AllthedevicesinanERPSringinstancemustbe
configuredwiththesamecontrolVLAN,anddifferentERPSringinstancesmustusedifferentcontrolVLANs.
Thenoformofthiscommandremovesthecontrol-channelVLANoftheringinstance.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<vid>
Required,VLANID.Range:1-4094.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Addacontrol-channelVLANtoaringinstance:
| switch(config)#                   |     | erps | ring | 3   |              |     |
| --------------------------------- | --- | ---- | ---- | --- | ------------ | --- |
| switch(config-erps-ring-3)#       |     |      |      |     | instance 2   |     |
| switch(config-erps-ring-3-inst-2) |     |      |      |     | control-vlan | 10  |
Removethecontrol-channelVLANoftheringinstance:
| switch(config)#                   |               | erps | ring     | 3   |                  |     |
| --------------------------------- | ------------- | ---- | -------- | --- | ---------------- | --- |
| switch(config-erps-ring-3)#       |               |      |          |     | instance 2       |     |
| switch(config-erps-ring-3-inst-2) |               |      |          |     | no control-vlan  |     |
| erps                              | ring <ringid> |      | instance |     | <id> description |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 50

Syntax
| erps | ring <ringid> |      |             |     |        |     |
| ---- | ------------- | ---- | ----------- | --- | ------ | --- |
|      | instance      | <id> | description |     | <line> |     |
Description
Thiscommandaddsdescriptiveinformationtohelpadministratorsandoperatorsunderstandthepurpose
ofaringinstance.1-64printableASCIIcharactersareallowed.
Thenoformofthiscommandremovestheringinstancedescription.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<line>
Required,descriptiveinformationabouttheringinstance.1-64printableASCIIcharactersallowed.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Addringinstancedescription:
| switch(config)#                   |     | erps | ring | 3        |             |                  |
| --------------------------------- | --- | ---- | ---- | -------- | ----------- | ---------------- |
| switch(config-erps-ring-3)#       |     |      |      | instance | 2           |                  |
| switch(config-erps-ring-3-inst-2) |     |      |      |          | description | HPE RnD DataVlan |
Removeringinstancedescription:
| switch(config)#                   |               | erps | ring     | 3        |                |     |
| --------------------------------- | ------------- | ---- | -------- | -------- | -------------- | --- |
| switch(config-erps-ring-3)#       |               |      |          | instance | 2              |     |
| switch(config-erps-ring-3-inst-2) |               |      |          |          | no description |     |
| erps                              | ring <ringid> |      | instance |          | <id> enable    |     |
Syntax
| erps | ring <ringid> |      |        |     |     |     |
| ---- | ------------- | ---- | ------ | --- | --- | --- |
|      | instance      | <id> | enable |     |     |     |
Description
Thisconfigurationenablesprotectionswitchingonthegiveninstanceofthering.Itisdisabledbydefault.
Thenoformofthiscommanddisablesprotectionswitchingonthegiveninstanceofthering.
Commandcontext
config-erps-ring-<ringid>
Parameters
ERPS|51

<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enableprotectionswitchingonthegiveninstanceofthering:
| switch(config)#                   |     | erps ring | 3        |        |
| --------------------------------- | --- | --------- | -------- | ------ |
| switch(config-erps-ring-3)#       |     |           | instance | 2      |
| switch(config-erps-ring-3-inst-2) |     |           |          | enable |
Disableprotectionswitchingonthegiveninstanceofthering:
| switch(config)#                   |               | erps ring | 3        |                      |
| --------------------------------- | ------------- | --------- | -------- | -------------------- |
| switch(config-erps-ring-3)#       |               |           | instance | 2                    |
| switch(config-erps-ring-3-inst-2) |               |           |          | no enable            |
| erps                              | ring <ringid> | instance  |          | <id> protected-vlans |
Syntax
| erps | ring <ringid> |                      |     |            |
| ---- | ------------- | -------------------- | --- | ---------- |
|      | instance      | <id> protected-vlans |     | <vid-list> |
Description
ThiscommandspecifiesthesetofVLANsthatareprotectedbythisringinstance.
ThenoformofthiscommandremovesasetofVLANsthatareprotectedbythisringinstance.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<vd-list>
Required,rangeofVLANstobeprotectedbythisringinstance.Range:1-4094.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SpecifyasetofVLANsthatareprotectedbythisringinstance:
AOS-CX10.07HighAvailabilityGuide|UserGuide 52

| switch(config)#                   |     | erps ring | 3        |                 |     |         |
| --------------------------------- | --- | --------- | -------- | --------------- | --- | ------- |
| switch(config-erps-ring-3)#       |     |           | instance |                 | 2   |         |
| switch(config-erps-ring-3-inst-2) |     |           |          | protected-vlans |     | 1,10-50 |
RemoveasetofVLANsthatareprotectedbythisringinstance:
| switch(config)#                   |     | erps ring | 3        |     |                 |       |
| --------------------------------- | --- | --------- | -------- | --- | --------------- | ----- |
| switch(config-erps-ring-3)#       |     |           | instance |     | 2               |       |
| switch(config-erps-ring-3-inst-2) |     |           |          | no  | protected-vlans | 11,13 |
erps ring <ringid> instance <id> protection-switch {{manual|force}
<port0>|<port1>}
Syntax
erps ring <ringid> instance <id> protection-switch {{manual|force} <port0>|<port1>}
Description
Blocksaspecificringinterfaceinoneofthetwofollowingways:
n Force:Theswitchblocksaspecificringinterfaceregardlessoftheprotectionswitchingstateofthering
instance.
n Manual:Theswitchblocksaspecificringinterfaceifnootherprotectionswitcheventisactiveonthering
instance.
Theusercanverifywhethertheprotection-switchissuccessfulbyverifyingthestatusofinstanceandportstate
overwhichthiscommandisexecuted.
| switch# | erps     | ring 1 instance |          | 1 protection-switch |     | force port0 |
| ------- | -------- | --------------- | -------- | ------------------- | --- | ----------- |
| switch# | show     | erps status     |          |                     |     |             |
| Status  | for ERPS | Ring 1          | Instance | 1:                  |     |             |
====================================
| Ring ID        |           |          |     | : 1             |         |     |
| -------------- | --------- | -------- | --- | --------------- | ------- | --- |
| Instance       | ID        |          |     | : 1             |         |     |
| Port0          |           |          |     | : 1/1/5         | (Block) |     |
| Port1          |           |          |     | : 1/1/6         | (Up)    |     |
| Node Role      | (RPL)     |          |     | : Owner         | (port0) |     |
| Control        | VLAN      |          |     | : 50            |         |     |
| Protected      | VLAN      |          |     | : 1-49          |         |     |
| Subring        | (TCN)     |          |     | : No (No)       |         |     |
| Revertive      | Operation |          |     | : Revertive     |         |     |
| MEG Level      |           |          |     | : 7             |         |     |
| Transmission   |           | Interval |     | : 5 sec         |         |     |
| Guard Interval |           |          |     | : 0 sec         | 500 ms  |     |
| Hold-Off       | Interval  |          |     | : 0 sec         | 0 ms    |     |
| WTR Interval   |           |          |     | : 1 min         |         |     |
| Status         |           |          |     | : Forced-switch |         |     |
| Oper Down      | Reason    |          |     | : None          |         |     |
Commandcontext
Operator(>)orManager(#)
Parameters
ERPS|53

<ringid>
Required,specifiestheIDofthering.Range:1-239.
<id>
Required,specifiestheIDoftheringinstance.Range:1-2.
manual
Atypeofprotectionswitcheventinwhichtheswitchblocksaspecificringinterfaceifnootherprotection
switcheventisactiveontheringinstance.
force
Atypeofprotectionswitcheveninwhichtheswitchblocksaspecificringinterfaceregardlessofthe
protectionswitchingstateoftheringinstance.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Blockring3,interface2,port0ifnootherprotectionswitcheventisactiveontheringinstance:
switch# erps ring 3 instance 2 protection-switch manual port0
Blockring3,instance2,regardlessoftheprotectionswitchingstateoftheringinstance:
switch# erps ring 3 instance 2 protection-switch force port1
erps ring <ringid> instance <id> revertive
Syntax
erps ring <ringid> instance <id> revertive
Description
ConfiguresthedefaultrevertivemodeofoperationforanERPSring.Inrevertiveoperation,afterthe
conditionscausingprotectionswitchingarecleared,trafficchannelsarerestoredtotherecoveredlink
blockingtheRPL.ThisconfigurationismeaningfulonlyontheRPLnode.
Thenoformofthiscommandconfiguresnon-revertivemodeofoperationforanERPSring.Innon-revertive
operation,thetrafficchannelscontinuetousetheRPL,ifithasnotfailed,afterconditionscausing
protectionswitchingarecleared.ThisconfigurationismeaningfulonlyontheRPLnode.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
AOS-CX10.07HighAvailabilityGuide|UserGuide 54

Examples
ConfiguringthedefaultrevertivemodeofoperationforERPSring3,instance2:
| switch(config)#                    | erps | ring 3   |           |
| ---------------------------------- | ---- | -------- | --------- |
| switch(config-erps-ring-3)#        |      | instance | 2         |
| switch(config-erps-ring-3-inst-2)# |      |          | revertive |
Configuringnon-revertivemodeofoperationforERPSring3,instance2:
| switch(config)#                    | erps     | ring 3   |              |
| ---------------------------------- | -------- | -------- | ------------ |
| switch(config-erps-ring-3)#        |          | instance | 2            |
| switch(config-erps-ring-3-inst-2)# |          |          | no revertive |
| erps ring                          | <ringid> | instance | <id> role    |
Syntax
| erps ring | <ringid> |                               |     |
| --------- | -------- | ----------------------------- | --- |
| instance  | <id>     | role <rpl-owner|rpl-neighbor> |     |
Description
InERPS,thereisacentralnodecalledRPLOwnerNodewhichblocksoneoftheportstoensurethatthereis
noloopformedfortheEthernettraffic.ThelinkblockedbytheRPLownernodeiscalledtheRingProtection
LinkorRPL.ThenodeattheotherendoftheRPLisknownasRPLNeighborNode.ItusesR-APScontrol
messagestocoordinatetheactivitiesofswitchingon/offtheRPLlink.
Thiscommandspecifiestheroleofthenodeasownerorneighbor.
Thenoformofthiscommandremovestheconfigurationofthenoderolefromtheinstance.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<rpl-owner>
BlockstrafficatoneendoftheRPL.TheblockedendsendsoutperiodicR-APS.
<rpl-neighbor>
BlockstrafficatoneendoftheRPL.TheblockedenddoesnotgenerateperiodicR-APS.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Specifytheroleofthenodeasowner:
ERPS|55

| switch(config)#                   | erps | ring 3   |                |
| --------------------------------- | ---- | -------- | -------------- |
| switch(config-erps-ring-3)#       |      | instance | 2              |
| switch(config-erps-ring-3-inst-2) |      |          | role rpl-owner |
Specifytheroleofthenodeasneighbor:
| switch(config)#                   | erps | ring 3   |                    |
| --------------------------------- | ---- | -------- | ------------------ |
| switch(config-erps-ring-3)#       |      | instance | 3                  |
| switch(config-erps-ring-3-inst-2) |      |          | role rpl-neighbour |
Removetheconfigurationofthenoderolefromtheinstance:
| switch(config)#                   | erps     | ring 3   |          |
| --------------------------------- | -------- | -------- | -------- |
| switch(config-erps-ring-3)#       |          | instance | 2        |
| switch(config-erps-ring-3-inst-2) |          |          | no role  |
| erps ring                         | <ringid> | instance | <id> rpl |
Syntax
| erps ring | <ringid> |                   |     |
| --------- | -------- | ----------------- | --- |
| instance  | <id>     | rpl <port0|port1> |     |
Description
InERPS,thereisacentralnodecalledRPLOwnerNodewhichblocksoneoftheportstoensurethatthereis
noloopformedfortheEthernettraffic.ThelinkblockedbytheRPLownernodeiscalledtheRingProtection
LinkorRPL.ThenodeattheotherendoftheRPLisknownasRPLNeighborNode.ItusesR-APScontrol
messagestocoordinatetheactivitiesofswitchingtheRPLlinkonandoff.
ThiscommandspecifieswhichoftheERPSringportsistheRPL.
ThenoformofthiscommandremovestheRPLportconfigurationfromtheERPSringinstance.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<id>
Required,specifiestheERPSringinstanceidentifier.Range:1-2.
<port0>
Required,configureport0tobeRPLportinthisERPSringinstance.
<port1>
Required,configureport1tobeRPLportinthisERPSringinstance.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configureport0tobeRPLportinthisERPSringinstance:
AOS-CX10.07HighAvailabilityGuide|UserGuide 56

| switch(config)#                   | erps | ring | 3        |           |
| --------------------------------- | ---- | ---- | -------- | --------- |
| switch(config-erps-ring-3)#       |      |      | instance | 2         |
| switch(config-erps-ring-3-inst-2) |      |      | role     | rpl-owner |
| switch(config-erps-ring-3-inst-2) |      |      | rpl      | port0     |
Configureport1tobeRPLportinthisERPSringinstance:
| switch(config)#                   | erps | ring | 3        |               |
| --------------------------------- | ---- | ---- | -------- | ------------- |
| switch(config-erps-ring-3)#       |      |      | instance | 3             |
| switch(config-erps-ring-3-inst-2) |      |      | role     | rpl-neighbour |
| switch(config-erps-ring-3-inst-2) |      |      | rpl      | port1         |
RemovetheRPLportconfigurationfromtheERPSringInstance:
| switch(config)#                   | erps     | ring      | 3        |           |
| --------------------------------- | -------- | --------- | -------- | --------- |
| switch(config-erps-ring-3)#       |          |           | instance | 2         |
| switch(config-erps-ring-3-inst-2) |          |           | no       | rpl port0 |
| erps ring                         | <ringid> | meg-level |          |           |
Syntax
| erps ring | <ringid> |     |     |     |
| --------- | -------- | --- | --- | --- |
meg-level <-0-7>
Description
TheR-APSmessagestransmittedbyERPStaketheformofOAMPDUsasdefinedinG.8013.EachOAMPDU
istransmittedataspecifiedlevelknownastheMaintenanceEntityGroup(MEG)level.Thiscommand
configuresthelevelwithwhichtheERPSpacketsmustbetransmitted.
ThenoformofthiscommandremovestheconfiguredMEGlevelandsetsittothedefaultvalueof7.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<0-7>
Required,specifiesthemeg-level.Range:0-7.Default:7.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Specifythemeg-level:
| switch(config)#             | erps | ring | 3         |     |
| --------------------------- | ---- | ---- | --------- | --- |
| switch(config-erps-ring-3)# |      |      | meg-level | 4   |
Removetheconfiguredmeg-levelandsetittothedefaultvalueof7:
ERPS|57

| switch(config)#             | erps     | ring        | 3            |     |
| --------------------------- | -------- | ----------- | ------------ | --- |
| switch(config-erps-ring-3)# |          |             | no meg-level |     |
| erps ring                   | <ringid> | parent-ring |              |     |
Syntax
| erps ring | <ringid> |     |     |     |
| --------- | -------- | --- | --- | --- |
parent-ring <ringid>
Description
Thiscommandassociatesasub-ringtoaparent-ringandisrequiredforthesub-ringtonotifytheparent-
ringonchangeintopology.
Thenoformofthiscommandremovestheparentringidentifier.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<ringid>
Required,specifiestheIDoftheparent-ring.Range:1-239
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Associateasub-ringtoaparent-ring:
| switch(config)#             | erps | ring | 3           |     |
| --------------------------- | ---- | ---- | ----------- | --- |
| switch(config-erps-ring-3)# |      |      | parent-ring | 2   |
Removeaparent-ringidentifier:
| switch(config)#             | erps     | ring     | 3              |     |
| --------------------------- | -------- | -------- | -------------- | --- |
| switch(config-erps-ring-3)# |          |          | no parent-ring | 2   |
| erps ring                   | <ringid> | sub-ring |                |     |
Syntax
| erps ring | <ringid> |     |     |     |
| --------- | -------- | --- | --- | --- |
sub-ring
Description
Thiscommandistoconfigureasub-ring.Ifnotspecified,theringisamajor-ring.
Thenoformofthiscommandremovesthesub-ringconfigurationoftheringandconfiguresittobeamajor-
ring.
AOS-CX10.07HighAvailabilityGuide|UserGuide 58

Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configureasub-ring:
switch(config)# erps ring 2
switch(config-erps-ring-2)# sub-ring
Removethesub-ringconfigurationfromring2andconfigureittobeamajor-ring:
switch(config)# erps ring 2
switch(config-erps-ring-2)# no sub-ring
erps ring <ringid> tcn-propogation
Syntax
erps ring <ringid>
tcn-propogation
Description
Thiscommandistoconfigureasub-ringinterconnectionnodetopassatopologychangenotificationtothe
ringinstancefortheparentringwheneverthetopologyofthesub-ringchanges.Theparentringinstance
performsaForwardingDatabase(FDB)flushandsendsaprotocolmessagetoensurethatothernodeson
theparentringalsoperformanFDBflush.
Thenoformofthiscommanddisablestopologychangenotifications.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Configuretopologychangenotifications:
ERPS|59

| switch(config)# | erps | ring | 2   |     |
| --------------- | ---- | ---- | --- | --- |
switch(config-erps-ring-2)#
tcn-propogation
Disabletopologychangenotifications:
| switch(config)#             | erps     | ring                  | 2                  |     |
| --------------------------- | -------- | --------------------- | ------------------ | --- |
| switch(config-erps-ring-2)# |          |                       | no tcn-propogation |     |
| erps ring                   | <ringid> | transmission-interval |                    |     |
Syntax
| erps ring             | <ringid> |     |           |     |
| --------------------- | -------- | --- | --------- | --- |
| transmission-interval |          |     | <seconds> |     |
Description
SpecifiestheR-APSperiodictransmissionintervalinunitsofseconds.Defaultis5seconds.
Thenoformofthiscommandremovestheconfiguredvalueofthetransmissionintervalandsetsittothe
defaultvalueof5seconds.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<seconds>
Required,specifiestheR-APSperiodictransmissionintervalinunitsofseconds.Range:5seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SpecifytheR-APSperiodictransmissionintervalas10seconds:
| switch(config)#             | erps | ring | 3                     |     |
| --------------------------- | ---- | ---- | --------------------- | --- |
| switch(config-erps-ring-3)# |      |      | transmission-interval | 10  |
Removetheconfiguredvalueofthetransmissionintervalandsetittothedefaultvalueof5seconds:
| switch(config)#             | erps     | ring         | 3                        |     |
| --------------------------- | -------- | ------------ | ------------------------ | --- |
| switch(config-erps-ring-3)# |          |              | no transmission-interval |     |
| erps ring                   | <ringid> | wtr-interval |                          |     |
Syntax
| erps ring    | <ringid> |           |     |     |
| ------------ | -------- | --------- | --- | --- |
| wtr-interval |          | <minutes> |     |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 60

Description
TheRPLownernodeusesadelaytimerbeforeinitiatinganRPLblockincaseofbothrevertivemodeof
operationorbeforerevertingtoidlestateafterclearingoperatorcommands(FS,MS).
TheWaittoRestore(WTR)timercanbeconfiguredin1-minuteincrementsupto12minutes.Thedefault
valueis5minutes.WhenrecoveringfromanSF,thedelaytimermustbelongenoughtoallowthe
recoveringnetworktobecomestable.Inthedefaultrevertivemodeofoperation,theWTRtimerisusedto
preventfrequentoperationofprotectionswitchingduetointermittentSFdefects.
Thenoformofthiscommandremovestheconfiguredvalueofthewtr-intervalandsetsittothedefault
valueof5minutes.
Commandcontext
config-erps-ring-<ringid>
Parameters
<ringid>
Required,specifiestheIDofthering.Range:1-239
<seconds>
Required,specifiesthewtr-intervalinminutes.Range:1-12.Default:5.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Specifythewtr-interval:
switch(config)# erps ring 3
switch(config-erps-ring-3)# wtr-interval 7
Removetheconfiguredvalueofthewtr-intervalandsetittothedefaultvalueof5minutes:
switch(config)# erps ring 3
switch(config-erps-ring-3)# no wtr-interval
show erps statistics
Syntax
show erps statistics [ring <ringid>] [instance <id> [port0|port1]]
Description
ThiscommanddisplaysERPSstatistics.Thestatisticscanbedisplayedforthering,theinstance,orthe
instanceports.
Commandcontext
Operator(>)orManager(#)
Parameters
<ringid>
Optional,specifiestheIDofthering.Range:1-239.
ERPS|61

<id>
Optional,specifiestheIDoftheringinstance.Range:1-2.
<port0>
Optional,specifiestheringmemberport0.
<port1>
Optional,specifiestheringmemberport1.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
| switch#    | show erps statistics | ring       | 1   |
| ---------- | -------------------- | ---------- | --- |
| Statistics | for ERPS ring        | 1 instance | 1:  |
======================================
|                | Port0         |            | Port1        |
| -------------- | ------------- | ---------- | ------------ |
|                | -----         |            | -----        |
| Local Failures | 4             |            | 1            |
| R-APS          | Port0(Tx/Rx)  |            | Port1(Tx/Rx) |
| -----          | ------------  |            | ------------ |
| NR             | 1/1           |            | 1/1          |
| NR,RB          | 0/1           |            | 0/1          |
| SF             | 1/0           |            | 1/0          |
| MS             | 0/0           |            | 0/10         |
| FS             | 30/0          |            | 0/0          |
| Statistics     | for ERPS ring | 1 instance | 2:           |
======================================
|                | Port0                |            | Port1        |
| -------------- | -------------------- | ---------- | ------------ |
|                | -----                |            | -----        |
| Local Failures | 4                    |            | 1            |
| R-APS          | Port0(Tx/Rx)         |            | Port1(Tx/Rx) |
| -----          | ------------         |            | ------------ |
| NR             | 1/1                  |            | 1/1          |
| NR,RB          | 0/1                  |            | 0/1          |
| SF             | 1/0                  |            | 1/0          |
| MS             | 0/0                  |            | 0/10         |
| FS             | 30/0                 |            | 0/0          |
| switch#        | show erps statistics |            |              |
| Statistics     | for ERPS Ring        | 1 Instance | 1 :          |
==========================================
|                | Port0        |     | Port1        |
| -------------- | ------------ | --- | ------------ |
|                | -----        |     | -----        |
| Local Failures | 4            |     | 1            |
| R-APS          | Port0(Tx/Rx) |     | Port1(Tx/Rx) |
| -------        | ----------   |     | -----------  |
| NR             | 33/9         |     | 33/9         |
| NR,RB          | 58/0         |     | 58/0         |
| SF             | 4/0          |     | 4/0          |
| MS             | 0/0          |     | 0/0          |
| FS             | 0/0          |     | 0/0          |
| show erps      | status       |     |              |
AOS-CX10.07HighAvailabilityGuide|UserGuide 62

Syntax
show erps status [ring <ringid>] [instance <id>]
Description
Thiscommanddisplaysdetailedinformationaboutaspecificringorallinstancesofaring.
Theringinstancemaybeinoneofthefollowingstates:
n Idle:Theringinstanceisoperational.
n Initializing:Theringinstanceisnotoperational.
n Protection:Protectionswitchinghasbeentriggeredbyalocalorremotelinkfailure.
n Pending:Pendingclearanceofapreviousprotectionswitch.
n Down:Ringinstanceisnotactive.
n Manual-switch:ManualprotectionswitchingtriggeredbyAdmin-down.
n Force-switch:Forcedprotectionswitchingtriggeredbyadmin.
Aringinstancehasthefollowingreasonsfor"down"state:
n Disabled:Ringinstanceisadministrativelydisabled.
n Inconsistent Port Config:Thesameportisconfiguredasport0andport1orRPLportisconfiguredby
Admin-down.
n Incomplete Port Config:Onlyoneornoringportisconfigured.
n ProtectedVLANs Not Configured:ProtectedVLANlistisempty.
n ControlVLAN Not Configured:ControlVLANisnotconfigured.
Theringportscanbeinoneofthefollowingstates:
n Up:Portforwardscontrolanddatatraffic.
n Blocked:Portblocksbothcontrolanddatatraffic.
Commandcontext
Operator(>)orManager(#)
Parameters
<ringid>
Optional,specifiestheIDofthering.Range:1-239.
<id>
Optional,specifiestheIDoftheringinstance.Range:1-2.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowERPSstatusforring1andinstance1:
Status for ERPS Ring 1 Instance 1
=================================
Ring ID : 1
Ring description : ring_1
ERPS|63

| Instance       | ID          |     | : 1               |           |            |
| -------------- | ----------- | --- | ----------------- | --------- | ---------- |
| Instance       | description |     | : inst_1          |           |            |
| Port0          |             |     | : 1/0/1 (Blocked) |           |            |
| Port1          |             |     | : 1/0/2 (Up)      |           |            |
| Node Role      | (RPL)       |     | : Owner (Port0)   |           |            |
| Control        | VLAN        |     | : 100             |           |            |
| Protected      | VLAN        |     | : None            |           |            |
| Subring        | (TCN)       |     | : Yes (Yes)       |           |            |
| Revertive      | Operation   |     | : Revertive       |           |            |
| MEG Level      |             |     | : 1               |           |            |
| Transmission   | Interval    |     | : 5 sec           |           |            |
| Guard Interval |             |     | : 500 ms          |           |            |
| Hold-Off       | Interval    |     | : 1 sec           |           |            |
| WTR Interval   |             |     | : 5 min           |           |            |
| Status         |             |     | : Initializing    |           |            |
| Oper Down      | Reason      |     | : Protected       | Vlans Not | Configured |
ShowERPSstatusforring1:
| switch# | show erps     | status ring | 1   |     |     |
| ------- | ------------- | ----------- | --- | --- | --- |
| Status  | for ERPS Ring | 1 Instance  | 1   |     |     |
=================================
| Ring ID          |               |            | : 1               |     |     |
| ---------------- | ------------- | ---------- | ----------------- | --- | --- |
| Ring description |               |            | : ring_1          |     |     |
| Instance         | ID            |            | : 1               |     |     |
| Instance         | description   |            | : inst_1          |     |     |
| Port0            |               |            | : 1/0/1 (Blocked) |     |     |
| Port1            |               |            | : 1/0/2 (Up)      |     |     |
| Node Role        | (RPL)         |            | : Owner (Port0)   |     |     |
| Control          | VLAN          |            | : 100             |     |     |
| Protected        | VLAN          |            | : 1-10            |     |     |
| Subring          | (TCN)         |            | : Yes (Yes)       |     |     |
| Revertive        | Operation     |            | : Non-Revertive   |     |     |
| MEG Level        |               |            | : 1               |     |     |
| Transmission     | Interval      |            | : 5 sec           |     |     |
| Guard Interval   |               |            | : 500 ms          |     |     |
| Hold-Off         | Interval      |            | : 1 sec           |     |     |
| WTR Interval     |               |            | : 5 min           |     |     |
| Status           |               |            | : Idle            |     |     |
| Oper Down        | Reason        |            | : None            |     |     |
| Status           | for ERPS Ring | 1 Instance | 2                 |     |     |
=================================
| Ring ID          |             |     | : 1               |     |     |
| ---------------- | ----------- | --- | ----------------- | --- | --- |
| Ring description |             |     | : ring_1          |     |     |
| Instance         | ID          |     | : 2               |     |     |
| Instance         | description |     | : inst_2          |     |     |
| Port0            |             |     | : 1/0/3 (Blocked) |     |     |
| Port1            |             |     | : 1/0/4 (Up)      |     |     |
| Node Role        | (RPL)       |     | : Owner (Port0)   |     |     |
| Control          | VLAN        |     | : 110             |     |     |
| Protected        | VLAN        |     | : 20-30           |     |     |
| Subring          | (TCN)       |     | : No              |     |     |
| Revertive        | Operation   |     | : Revertive       |     |     |
| MEG Level        |             |     | : 1               |     |     |
| Transmission     | Interval    |     | : 5 sec           |     |     |
| Guard Interval   |             |     | : 500 ms          |     |     |
| Hold-Off         | Interval    |     | : 1 sec           |     |     |
| WTR Interval     |             |     | : 5 min           |     |     |
AOS-CX10.07HighAvailabilityGuide|UserGuide 64

| Status    |         | : Admin-Down |     |     |     |
| --------- | ------- | ------------ | --- | --- | --- |
| Oper Down | Reason  | : None       |     |     |     |
| show erps | summary |              |     |     |     |
Syntax
show erps summary
Description
ThiscommanddisplaysasummaryoftheERPSconfigurationandstatefortheERPSringinstances.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
| switch# | show erps summary |     |     |     |     |
| ------- | ----------------- | --- | --- | --- | --- |
ERPS Summary
============
| Flags:       | R - RPL, M - Major | Ring, S | - Sub Ring, | T - TCN | Enabled |
| ------------ | ------------------ | ------- | ----------- | ------- | ------- |
|              | * - RPL port       |         |             |         |         |
| Per-Instance | Summary            |         |             |         |         |
====================
| Ring Instance | Port0  | Port1  | Status        |     | Flags |
| ------------- | ------ | ------ | ------------- | --- | ----- |
| ---- -------- | -----  | -----  | ------        |     | ----- |
| 1 1           | 1/1/1  | *1/1/2 | Pending       |     | R,M   |
| 1 2           | 1/1/1  | 1/1/2  | Idle          |     | M     |
| 2 1           | *1/1/3 | -      | Protection    |     | R,S,T |
| 2 2           | 1/1/3  | -      | Admin-down    |     | S,T   |
| 3 1           | 1/1/4  | 1/1/5  | Manual-switch |     | M     |
| 3 2           | 1/1/4  | 1/1/5  | Force-switch  |     | M     |
ERPS|65

Chapter 5
Support and Other Resources
Support and Other Resources
Accessing Aruba Support
ArubaSupportServices https://www.arubanetworks.com/support-services/
ArubaSupportPortal https://asp.arubanetworks.com/
NorthAmericatelephone 1-800-943-4526(US&CanadaToll-FreeNumber)
+1-408-754-1200(Primary-TollNumber)
+1-650-385-6582(Backup-TollNumber-Useonlywhenallother
numbersarenotworking)
Internationaltelephone https://www.arubanetworks.com/support-services/contact-
support/
BesuretocollectthefollowinginformationbeforecontactingSupport:
n Technicalsupportregistrationnumber(ifapplicable)
n Productname,modelorversion,andserialnumber
n Operatingsystemnameandversion
n Firmwareversion
n Errormessages
n Product-specificreportsandlogs
n Add-onproductsorcomponents
n Third-partyproductsorcomponents
Other usefulsites
Otherwebsitesthatcanbeusedtofindinformation:
AirheadssocialforumsandKnowledge https://community.arubanetworks.com/
Base
Softwarelicensing https://lms.arubanetworks.com/
End-of-Lifeinformation https://www.arubanetworks.com/support-services/end-of-life/
Arubasoftwareanddocumentation https://asp.arubanetworks.com/downloads
Accessing Updates
YoucanaccessupdatesfromtheArubaSupportPortalortheHPEMyNetworkingWebsite.
Aruba Support Portal
AOS-CX10.07HighAvailabilityGuide| UserGuide 66

https://asp.arubanetworks.com/downloads
IfyouareunabletofindyourproductintheArubaSupportPortal,youmayneedtosearchMyNetworking,
whereoldernetworkingproductscanbefound:
My Networking
https://www.hpe.com/networking/support
Toviewandupdateyourentitlements,andtolinkyourcontractsandwarrantieswithyourprofile,gotothe
HewlettPackardEnterpriseSupportCenterMore Information on Access toSupport Materialspage:
https://support.hpe.com/portal/site/hpsc/aae/home/
AccesstosomeupdatesmightrequireproductentitlementwhenaccessedthroughtheHewlettPackard
EnterpriseSupportCenter.YoumusthaveanHPPassportsetupwithrelevantentitlements.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://asp.arubanetworks.com/notifications/subscriptions(requiresanactiveArubaSupportPortal(ASP)
accounttomanagesubscriptions).SecuritynoticesareviewablewithoutanASPaccount.
Warranty Information
Toviewwarrantyinformationforyourproduct,gotohttps://www.arubanetworks.com/support-
services/product-warranties/.
Regulatory Information
Toviewtheregulatoryinformationforyourproduct,viewtheSafetyandComplianceInformationforServer,
Storage,Power,Networking,andRackProducts,availableathttps://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts
Additionalregulatoryinformation
Arubaiscommittedtoprovidingourcustomerswithinformationaboutthechemicalsubstancesinour
productsasneededtocomplywithlegalrequirements,environmentaldata(companyprograms,product
recycling,energyefficiency),andsafetyinformationandcompliancedata,(RoHSandWEEE).Formore
information,seehttps://www.arubanetworks.com/company/about-us/environmental-citizenship/.
Documentation Feedback
Arubaiscommittedtoprovidingdocumentationthatmeetsyourneeds.Tohelpusimprovethe
documentation,sendanyerrors,suggestions,orcommentstoDocumentationFeedback(docsfeedback-
switching@hpe.com).Whensubmittingyourfeedback,includethedocumenttitle,partnumber,edition,
andpublicationdatelocatedonthefrontcoverofthedocument.Foronlinehelpcontent,includethe
productname,productversion,helpedition,andpublicationdatelocatedonthelegalnoticespage.
SupportandOtherResources|67