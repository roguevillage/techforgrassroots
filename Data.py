# DEPENDENCIES
import Respondent

# MACROS
NUM_RESPONDENTS = 50

# GLOBAL DATA STRUCTURE (BAD, OH WELL!)
r = []

# Intitalize all respondent data structures
for i in range(NUM_RESPONDENTS):
    r.append(Respondent.Respondent())

# Respondent 0
r[0].disc.wordOfMouth = 1
r[0].disc.physical = 1

r[0].udisc.instagram = 1
r[0].udisc.wordOfMouth = 1

r[0].ease.easeLevel = 2

r[0].easeRat.eventsInfo = 1
r[0].easeRat.noLiveFeed = 1
r[0].easeRat.noRoute = 1

r[0].safe.safetyLevel = 5

r[0].safeRat.dontOrganize = 1
r[0].safeRat.governmentSurveillance = 1
r[0].safeRat.fear = 1
r[0].safeRat.privatePage = 1
r[0].safeRat.trustFriends = 1

r[0].improv.liveFeed = 1
r[0].improv.routeDetails = 1

# Respondent 1
r[1].disc.instagram = 1

r[1].udisc.instagram = 1

r[1].ease.easeLevel = 5

r[1].easeRat.peopleShare = 1
r[1].easeRat.groupShare = 1

r[1].safe.safetyLevel = 2

r[1].safeRat.dontShare = 1
r[1].safeRat.strengthInNumbers = 1
r[1].safeRat.dataColllection = 1
r[1].safeRat.vagueSecurity = 1
r[1].safeRat.fear = 1

r[1].improv.noSocialMedia = 1
r[1].improv.noDataCollection = 1

# Respondent 2
r[2].disc.wordOfMouth = 1

r[2].udisc.facebook = 1

r[2].ease.easeLevel = 5

r[2].easeRat.peopleShare = 1
r[2].easeRat.groupShare = 1

r[2].safe.safetyLevel = 2

r[2].safeRat.dataCollection = 1
r[2].safeRat.differentValues = 1
r[2].safeRat.powerToHarm = 1

r[2].improv.anonymity = 1

# Respondent 3
r[3].disc.wordOfMouth = 1

r[3].udisc.facebook = 1

r[3].ease.easeLevel = 5

r[3].easeRat.searchGood = 1
r[3].easeRat.groupShare = 1

r[3].safe.safetyLevel = 1

r[3].safeRat.noEncryption = 1
r[3].safeRat.dataCollection = 1

r[3].improv.protectedCategories = 1

# Respondent 4
r[4].disc.wordOfMouth = 1

r[4].udisc.facebook = 1

r[4].ease.easeLevel = 3

r[4].easeRat.groupShare = 1
r[4].easeRat.peopleShare = 1
r[4].easeRat.searchBad = 1

r[4].safe.safetyLevel = 1

r[4].safeRat.fear = 1
r[4].safeRat.selfCensorship = 1 

r[4].improv.cyberLiteracy = 1
r[4].improv.rightsLiteracy = 1

# Respondent 5
r[5].disc.wordOfMouth = 1

r[5].udisc.twitter = 1
r[5].udisc.facebook = 1
r[5].udisc.instagram = 1

r[5].ease.easeLevel = 3

r[5].easeRat.searchBad = 1
r[5].easeRat.alreadyKnow = 1

r[5].safe.safetyLevel = 1

r[5].safeRat.vpn = 1

r[5].improv.cyberLiteracy = 1
r[5].improv.noFinancialIncentive = 1
r[5].improv.democratized=1

# Respondent 6
r[6].disc.news = 1

r[6].udisc.websites = 1
r[6].udisc.google = 1

r[6].ease.easeLevel = 2

r[6].easeRat.misinformation = 1
r[6].easeRat.floodBad = 1

r[6].safe.safetyLevel = 1

r[6].safeRat.noCredibility = 1

r[6].improv.sourceVerification = 1

# Respondent 7
r[7].disc.news = 1

r[7].udisc.websites = 1
r[7].udisc.google = 1

r[7].ease.easeLevel = 2

r[7].easeRat.misinformation = 1

r[7].safe.safetyLevel = 1

r[7].safeRat.noCredibility = 1

r[7].improv.sourceVerification = 1

# Respondent 8
r[8].disc.instagram = 1

r[8].udisc.instagram = 1

r[8].ease.easeLevel = 2

r[8].easeRat.misinformation = 1

r[8].safe.safetyLevel = 4

r[8].improv.accountVerification = 1

# Respondent 9
r[9].disc.wordOfMouth = 1

r[9].udisc.wordOfMouth = 1
r[9].udisc.facebook = 1
r[9].udisc.websites = 1
r[9].udisc.google = 1

r[9].ease.easeLevel = 2

r[9].easeRat.slowUpdates = 1

r[9].safe.safetyLevel = 2

r[9].safeRat.trackActivists = 1
r[9].safeRat.governmentSurveillance = 1
r[9].safeRat.dataCollection = 1

r[9].improv.anonymity = 1
r[9].improv.noSocialMedia = 1
r[9].improv.noFinancialIncentive = 1

# Respondent 10
r[10].disc.instagram = 1

r[10].udisc.instagram = 1
r[10].udisc.facebook = 1

r[10].ease.easeLevel = 3

r[10].easeRat.misinformation = 1
r[10].easeRat.connections = 1
r[10].easeRat.peopleShare = 1

r[10].safe.safetyLevel = 4

r[10].safeRat.hadntThought = 1

r[10].improv.accountVerification = 1

# Respondent 11
r[11].disc.wordOfMouth = 1

r[11].udisc.facebook = 1
r[11].udisc.instagram = 1
r[11].udisc.reddit = 1

r[11].ease.easeLevel = 5

r[11].easeRat.eventsInfo = 1
r[11].easeRat.searchGood = 1

r[11].safe.safetyLevel = 5

r[11].safeRat.discernCredibility = 1

r[11].improv.sourceInfo = 1
r[11].improv.orgVerification = 1

# Respondent 12
r[12].disc.facebook = 1

r[12].udisc.websites = 1
r[12].udisc.facebook = 1

r[12].ease.easeLevel = 3

r[12].easeRat.connections = 1
r[12].easeRat.floodBad = 1
r[12].easeRat.alreadyKnow = 1

r[12].safe.safetyLevel = 4

r[12].safeRat.whitePrivilege = 1
r[12].safeRat.dontShare = 1

r[12].improv.anonymity = 1
r[12].improv.noDataCollection = 1
r[12].improv.numPeopleNoID = 1

# Respondent 13
r[13].disc.wordOfMouth = 1

r[13].udisc.instagram = 1
r[13].udisc.wordOfMouth = 1

r[13].ease.easeLevel = 1

r[13].easeRat.floodBad = 1
r[13].easeRat.cumulativeFeed = 1

r[13].safe.safetyLevel = 3

r[13].safeRat.employerRetribution = 1
r[13].safeRat.selfCensorship = 1

r[13].improv.noFinancialIncentive = 1
r[13].improv.moralAlignment = 1

# Respondent 14
r[14].disc.wordOfMouth = 1

r[14].udisc.websites = 1
r[14].udisc.wordOfMouth = 1

r[14].ease.easeLevel = 2

r[14].easeRat.misinformation = 1
r[14].easeRat.connections = 1

r[14].safe.safetyLevel = 5

r[14].safeRat.whitePrivilege = 1
r[14].safeRat.dataCollection = 1
r[14].safeRat.cautiousWhoSees = 1
r[14].safeRat.fear = 1

r[14].improv.noSocialMedia = 1
r[14].improv.encryption = 1
r[14].improv.noFinancialIncentive = 1
r[14].improv.noGovernmentTies = 1
r[14].improv.noEmailPhoneLink = 1

# Respondent 15
r[15].disc.facebook

r[15].udisc.facebook
r[15].udisc.instagram

r[15].ease.easeLevel = 4

r[15].easeRat.peopleShare = 1
r[15].easeRat.searchGood = 1

r[15].safe.safetyLevel = 4

r[15].safeRat.quickestMethod = 1

r[15].improv.physicalVerification = 1

# Respondent 16
r[16].disc.facebook

r[16].udisc.facebook
r[16].udisc.instagram

r[16].ease.easeLevel = 4

r[16].easeRat.peopleShare = 1

r[16].safe.safetyLevel = 4

r[16].safeRat.quickestMethoed = 1

r[16].improv.sponsoredPosts = 1

# Respondent 17
r[17].disc.facebook

r[17].udisc.facebook
r[17].udisc.instagram

r[17].ease.easeLevel = 4

r[17].easeRat.peopleShare = 1
r[17].easeRat.algorithmRecommendations = 1

r[17].safe.safetyLevel = 3

r[17].safeRat.cautiousWhoSees = 1

r[17].improv.orgVerification = 1

# Respondent 18
r[18].disc.wordOfMouth = 1

r[18].udisc.twitter = 1

r[18].ease.easeLevel = 1

r[18].easeRat.misinformation = 1

r[18].safe.safetyLevel = 3

r[18].safeRat.selfCensorship = 1

r[18].improv.communityVerification = 1

# Respondent 19
r[19].disc.facebook = 1

r[19].udisc.facebook = 1
r[19].udisc.news = 1
r[19].udisc.wordOfMouth = 1

r[19].ease.easelevel = 4

r[19].easeRat.eventsInfo = 1

r[19].safe.safetyLevel = 2

r[19].safeRat.privateInfoPublic = 1

r[19].improv.privacy = 1
r[19].improv.anonymity = 1

# Respondent 20
r[20].disc.facebook = 1

r[20].udisc.facebook = 1
r[20].udisc.news = 1
r[20].udisc.wordOfMouth = 1

r[20].ease.easeLevel = 4

r[20].easeRat.searchBad = 1
r[20].easeRat.slowUpdates = 1

r[20].safe.safetyLevel = 1

r[20].safeRat.surveillance = 1
r[20].safeRat.noPrivacyLaws = 1

r[20].improv.allInOne = 1
r[20].improv.onlyOrganizersSee = 1
r[20].improv.reminders = 1

# Respondent 21
r[21].disc.facebook = 1

r[21].udisc.facebook = 1

r[21].ease.easeLevel = 4

r[21].easeRat.sourceVerification = 1
r[21].easeRat.cumulativeFeed = 1

r[21].safe.safetyLevel = 4

r[21].safeRat.strengthInCommunity = 1
r[21].safeRat.communityVerification = 1

r[21].improv.physicalVerification = 1
r[21].improv.documentEvidence = 1
r[21].improv.allInOne = 1

# Respondent 22
r[22].disc.facebook = 1

r[22].udisc.facebook = 1
r[22].udisc.twitter = 1
r[22].udisc.instagram = 1
r[22].udisc.localNews = 1
r[22].udisc.wordOfMouth = 1

r[22].ease.easeLevel = 2

r[22].easeRat.slowUpdates = 1
r[22].easeRat.groupShare = 1

r[22].safe.safetyLevel = 5

r[22].safeRat.discernCredibility = 1

r[22].improv.orgVerification = 1

# Respondent 23
r[23].disc.facebook = 1

r[23].udisc.wordofMouth = 1
r[23].udisc.facebook = 1

r[23].ease.easeLevel = 4

r[23].easeRat.connections = 1
r[23].easeRat.peopleShare = 1

r[23].safe.safetyLevel = 5

r[23].safeRat.dontShare = 1
r[23].safeRat.signal = 1
r[23].safeRat.noPrivacy = 1

r[23].improv.userFriendly = 1
r[23].improv.security = 1

# Respondent 24
r[24].disc.instagram = 1

r[24].udisc.instagram = 1
r[24].udisc.localGroups = 1

r[24].ease.easeLevel = 3

r[24].easeRat.connections = 1
r[24].easeRat.groupShare = 1

r[24].safe.safetyLevel = 2

r[24].safeRat.dontShare = 1
r[24].safeRat.trackActivists = 1
r[24].safeRat.governmentSurveillance = 1
r[24].safeRat.fear = 1
r[24].safeRat.nothingBetter = 1
r[24].safeRat.signal = 1

r[24].improv.noSocialMedia = 1
r[24].improv.security = 1
r[24].improv.userFriendly = 1

# Respondent 25
r[25].disc.instagram = 1

r[25].udisc.instagram = 1
r[25].udisc.wordOfMouth = 1

r[25].ease.easeLevel = 3

r[25].easeRat.alreadyKnow = 1
r[25].easeRat.sourceVerification = 1

r[25].safe.safetyLevel = 4

r[25].safeRat.alwaysWatching = 1

r[25].improv.noFinancialIncentive = 1
r[25].improv.noPowerIncentive = 1
r[25].improv.encryption = 1

# Respondent 26
r[26].disc.instagram = 1

r[26].udisc.instagram = 1
r[26].udisc.wordOfMouth = 1

r[26].ease.easeLevel = 4

r[26].easeRat.connections = 1
r[26].easeRat.groupShare = 1
r[26].easeRat.sourceVerification = 1

r[26].safe.safetyLevel = 4

r[26].safeRat.alwaysWatching = 1

r[26].improv.encryption = 1

# Respondent 27
r[27].disc.instagram = 1

r[27].udisc.wordOfMouth = 1
r[27].udisc.facebook = 1

r[27].ease.easeLevel = 3

r[27].easeRat.alreadyKnow = 1

r[27].safe.safetyLevel = 1

r[27].safeRat.surveillance = 1
r[27].safeRat.vpn = 1
r[27].safeRat.privateBrowsing = 1

r[27].improv.noFinancialIncentive = 1
r[27].improv.noAds = 1
r[27].improv.noSurveillanceIncentive = 1
r[27].improv.encryption = 1

# Respondent 28
r[28].disc.instagram = 1

r[28].udisc.instagram = 1

r[28].ease.easeLevel = 3

r[28].easeRat.alreadyKnow = 1
r[28].easeRat.searchGood = 1

r[28].safe.safetyLevel = 2

r[28].safeRat.alwaysWatching = 1
r[28].safeRat.firewall = 1
r[28].safeRat.vpn = 1

r[28].improv.noSocialMedia = 1
r[28].improv.noGovernmentTies = 1
r[28].improv.decentralized = 1
r[28].improv.communityControlled = 1

# Respondent 29
r[29].disc.wordOfMouth = 1

r[29].udisc.facebook = 1
r[29].udisc.twitter = 1

r[29].ease.easeLevel = 2

r[29].easeRat.connections = 1
r[29].easeRat.groupShare = 1

r[29].safe.safetyLevel = -1

r[29].safeRat.hadntThought = 1
r[29].safeRat.surveillance = 1
r[29].safeRat.hacking = 1
r[29].safeRat.phoneVulnerability = 1

r[29].improv.noFinancialIncentive = 1
r[29].improv.encryption = 1

# Respondent 30
r[30].disc.wordOfMouth = 1

r[30].udisc.instagram = 1
r[30].udisc.twitter = 1

r[30].ease.easeLevel = 1

r[30].easeRat.floodBad = 1
r[30].easeRat.connections = 1

r[30].safe.safetyLevel = 1

r[30].safeRat.surveillance = 1
r[30].safeRat.phonVulnerability = 1

r[30].improv.noFinancialIncentive = 1
r[30].improv.encryption = 1
r[30].improv.communityControlled = 1

# Respondent 31
r[31].disc.facebook = 1

r[31].udisc.facebook = 1
r[31].udisc.wordOfMouth = 1

r[31].ease.easeLevel = 3

r[31].easeRat.connections = 1

r[31].safe.safetyLevel = 4

r[31].safeRat.dataCollection = 1

r[31].improv.userFriendly = 1

# Respondent 32
r[32].disc.wordOfMouth = 1

r[32].udisc.facebook = 1
r[32].udisc.instagram = 1

r[32].ease.easeLevel = 3

r[32].easeRat.censorship = 1

r[32].safe.safetyLevel = 1

r[32].safeRat.surveillance = 1
r[32].safeRat.dataCollection = 1
r[32].safeRat.governmentSurveillance = 1
r[32].safeRat.signal = 1

r[32].improv.encryption = 1
r[32].improv.noFinancialIncentive = 1
r[32].improv.noGovernmentTies = 1

# Respondent 33
r[33].disc.instagram = 1

r[33].udisc.instagram = 1
r[33].udisc.physicalDiscovery = 1

r[33].ease.easeLevel = 4

r[33].easeRat.peopleShare = 1

r[33].safe.safetyLevel = 2

r[33].safeRat.cautiousWhoSees = 1
r[33].safeRat.fear = 1
r[33].safeRat.triggeringPOC = 1

r[33].improv.allInOne = 1

# Respondent 34
r[34].disc.wordOfMouth = 1

r[34].udisc.wordOfMouth = 1
r[34].udisc.physicalDiscovery = 1

r[34].ease.easeLevel = 2

r[34].easeRat.slowUpdates = 1
r[34].easeRat.searchBad = 1

r[34].safe.safetyLevel = 3

r[34].safeRat.misinformation = 1

r[34].improv.allInOne = 1

# Respondent 35
r[35].disc.instagram = 1

r[35].udisc.instagram = 1

r[35].ease.easeLevel = 5

r[35].easeRat.connections = 1
r[35].easeRat.floodGood = 1

r[35].safe.safetyLevel = 4

r[35].safeRat.whitePrivilege = 1

r[35].improv.notQualified = 1

# Respondent 36
r[36].disc.instagram = 1
r[36].disc.wordOfMouth = 1

r[36].udisc.instagram = 1
r[36].udisc.facebook = 1
r[36].udisc.wordOfMouth = 1

r[36].ease.easeLevel = 5

r[36].easeRat.connections = 1

r[36].safe.safetyLevel = 3

r[36].safeRat.postEventNoConvo = 1

r[36].improv.encryption = 1
r[36].improv.noGovernmentTies = 1
r[36].improv.noFinancialIncentive = 1

# Respondent 37
r[37].disc.facebook = 1

r[37].udisc.facebook = 1
r[37].udisc.wordOfMouth = 1

r[37].ease.easeLevel = 4

r[37].easeRat.searchGood = 1
r[37].easeRat.locationEvents = 1

r[37].safe.safetyLevel = 4

r[37].safeRat.privatePage = 1

r[37].improv.eventSpecific = 1

# Respondent 38
r[38].disc.facebook = 1

r[38].udisc.facebook = 1

r[38].ease.easeLevel = 4

r[38].easeRat.searchGood = 1
r[38].easeRat.locationEvents = 1

r[38].safe.safetyLevel = 4

r[38].safeRat.quickestMethod = 1

r[38].improv.eventSpecific = 1

# Respondent 39
r[39].disc.text = 1
r[39].disc.email = 1
r[39].disc.facebook = 1
r[39].disc.wordOfMouth = 1

r[39].udisc.text = 1
r[39].udisc.email = 1
r[39].udisc.facebook = 1
r[39].udisc.wordOfMouth = 1
r[39].udisc.websites = 1
r[39].udisc.twitter = 1
r[39].udisc.work = 1

r[39].ease.easeLevel = 3

r[39].easeRat.cumulativeFeed = 1

r[39].safe.safetyLevel = 1

r[39].safeRat.surveillance = 1
r[39].safeRat.dataCollection = 1
r[39].safeRat.governmentSurveillance = 1

r[39].improv.noFinancialIncentive = 1
r[39].improv.communityControlled = 1
r[39].improv.privacy = 1
r[39].improv.noGovernmentTies = 1

# Respondent 40
r[40].disc.instagram = 1
r[40].disc.wordOfMouth = 1

r[40].udisc.text = 1
r[40].udisc.email = 1
r[40].udisc.facebook = 1
r[40].udisc.wordOfMouth = 1
r[40].udisc.websites = 1
r[40].udisc.twitter = 1
r[40].udisc.work = 1

r[40].ease.easeLevel = 3

r[40].easeRat.floodBad = 1
r[40].easeRat.connections = 1

r[40].safe.safetyLevel = 2

r[40].safeRat.nothingBetter = 1
r[40].safeRat.dataCollection = 1

r[40].improv.security = 1

# Respondent 41
r[41].disc.instagram = 1
r[41].disc.facebook = 1
r[41].disc.wordOfMouth = 1

r[41].udisc.instagram = 1
r[41].udisc.facebook = 1
r[41].udisc.wordOfMouth = 1
r[41].udisc.work = 1

r[41].ease.easeLevel = 4

r[41].easeRat.connections = 1
r[41].easeRat.slowUpdates = 1

r[41].safe.safetyLevel = 1

r[41].safeRat.signal = 1
r[41].safeRat.trackActivists = 1
r[41].safeRat.governmentSurveillance = 1
r[41].safeRat.phoneVulnerability = 1

r[41].improv.allInOne = 1
r[41].improv.noSocialMedia = 1
r[41].improv.noFinancialIncentive = 1
r[41].improv.openSourceCode = 1
r[41].improv.communityControlled = 1
r[41].improv.noGovernmentTies = 1
r[41].improv.userFriendly = 1

# Respondent 42
r[42].disc.wordOfMouth = 1

r[42].udisc.instagram = 1

r[42].ease.easeLevel = 4

r[42].easeRat.connections = 1
r[42].easeRat.peopleShare = 1
r[42].easeRat.alreadyKnow = 1

r[42].safe.safetyLevel = 5

r[42].safeRat.whitePrivilege = 1
r[42].safeRat.easiestMethod = 1
r[42].safeRat.mostReach = 1
r[42].safeRat.misinformation = 1

r[42].improv.allInOne = 1
r[42].improv.eventCalendar = 1
r[42].improv.routeInfo = 1
r[42].improv.orgCoordination = 1

# Respondent 43
r[43].disc.physicalDiscovery = 1

r[43].udisc.collegeCampuses = 1
r[43].udisc.flyers = 1

r[43].ease.easeLevel = -1

r[43].safe.safetyLevel = 1

r[43].safeRat.hacking = 1
r[43].safeRat.falseIdentity = 1
r[43].safeRat.fear = 1

r[43].improv.stopFuelingAnxiety = 1

# Respondent 44
r[44].disc.physicalDiscovery = 1

r[44].udisc.collegeCampuses = 1
r[44].udisc.facebook = 1
r[44].udisc.twitter = 1
r[44].udisc.instagram = 1

r[44].ease.easeLevel = 2

r[44].easeRat.disconnected = 1

r[44].safe.safetyLevel = 2

r[44].safeRat.noInternet = 1
r[44].safeRat.hacking = 1

r[44].improv.noHacking = 1
r[44].improv.security = 1

# Respondent 45
r[45].disc.facebook = 1

r[45].udisc.facebook = 1
r[45].udisc.instagram = 1

r[45].ease.easeLevel = 5

r[45].easeRat.connections = 1
r[45].easeRat.groupShare = 1

r[45].safe.safetyLevel = 2

r[45].safeRat.vagueSecurity = 1
r[45].safeRat.fear = 1
r[45].safeRat.nothingBetter = 1

r[45].improv.allyInstructions = 1

# Respondent 46
r[46].disc.wordOfMouth = 1

r[46].udisc.wordOfMouth = 1
r[46].udisc.facebook = 1
r[46].udisc.instagram = 1

r[46].ease.easeLevel = 3

r[46].easeRat.echoChamber = 1
r[46].easeRat.groupShare = 1

r[46].safe.safetyLevel = 4

r[46].safeRat.misinformation = 1
r[46].safeRat.unreliable = 1

r[46].improv.allyInstructions = 1

# Respondent 47
r[47].disc.wordOfMouth = 1

r[47].udisc.wordOfMouth = 1
r[47].udisc.facebook = 1
r[47].udisc.instagram = 1

r[47].ease.easeLevel = 4

r[47].easeRat.searchGood = 1
r[47].easeRat.oneLeadsNext = 1

r[47].safe.safetyLevel = 4

r[47].safeRat.misinformation = 1
r[47].safeRat.unreliable = 1

r[47].improv.orgVerification = 1
r[47].improv.infoPrevEvents = 1
r[47].improv.accountVerification = 1

# Respondent 48
r[48].disc.physicalDiscovery = 1

r[48].udisc.instagram = 1
r[48].udisc.facebook = 1
r[48].udisc.twitter = 1
r[48].udisc.youtube = 1

r[48].ease.easeLevel = 4

r[48].easeRat.floodGood = 1
r[48].easeRat.peopleShare = 1

r[48].safe.safetyLevel = 4

r[48].safeRat.falseIdentity = 1
r[48].safeRat.censorship = 1
r[48].safeRat.surveillance = 1
r[48].strengthInNumbers = 1

# Respondent 49
r[49].disc.physicalDiscovery = 1

r[49].udisc.instagram = 1
r[49].udisc.facebook = 1
r[49].udisc.twitter = 1
r[49].udisc.youtube = 1

r[49].ease.easeLevel = 4

r[49].easeRat.floodGood = 1
r[49].easeRat.peopleShare = 1
r[49].easeRat.algorithmRecommendations = 1

r[49].safe.safetyLevel = 4

r[49].safeRat.moreEducation = 1
r[49].safeRat.censorship = 1
r[49].strengthInNumbers = 1
