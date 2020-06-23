# DEPENDENCIES
import math
import Respondent


# MACROS
NUM_RESPONDENTS = 50

# IMPORT DATA
from Data import *


########################## DISCOVERY ANALYSIS ##############################

def isSocialMedia(s):
    if (s.facebook == 1 or s.instagram == 1 or s.twitter == 1):
        return True
    else:
        return False

def isOtherTech(s):
    if (s.youtube == 1 or s.email == 1 or s.text == 1 or s.reddit == 1 or s.websites == 1 or s.google == 1 or s.news == 1):
        return True
    else:
        return False

def isPhysical(s):
    if (s.physicalDiscovery == 1 or s.collegeCampuses == 1 or s.flyers == 1):
        return True
    else:
        return False

def isNetworks(s):
    if (s.wordOfMouth == 1 or s.localGroups == 1 or s.work == 1):
        return True
    else:
        return False

def discMethod():

    sm = 0
    net = 0
    otech = 0
    phys = 0

    for i in range(len(r)):
        if (isSocialMedia(r[i].disc)):
            sm += 1
        if (isNetworks(r[i].disc)):
            net += 1
        if (isOtherTech(r[i].disc)):
            otech += 1
        if (isPhysical(r[i].disc)):
            phys += 1
        

    total = NUM_RESPONDENTS
    
    print("Social Media (Discovery): ", sm, " of ", total, " (", (sm/total*100), "% )")
    print("Personal Networks (Discovery): ", net, " of ", total, " (", (net/total*100), "% )")
    print("Other Technology (Discovery): ", otech, " of ", total, " (", (otech/total*100), "% )")
    print("Physical (Discovery) ", phys, " of ", total, " (", (phys/total*100), "% )")

def udiscMethod():

    sm = 0
    net = 0
    otech = 0
    phys = 0

    for i in range(len(r)):
        if (isSocialMedia(r[i].udisc)):
            sm += 1
        if (isNetworks(r[i].udisc)):
            net += 1
        if (isOtherTech(r[i].udisc)):
            otech += 1
        if (isPhysical(r[i].udisc)):
            phys += 1
        

    total = NUM_RESPONDENTS
    
    print("Social Media (Usual Discovery): ", sm, " of ", total, " (", (sm/total*100), "% )")
    print("Personal Networks (Usual Discovery): ", net, " of ", total, " (", (net/total*100), "% )")
    print("Other Technology (Usual Discovery): ", otech, " of ", total, " (", (otech/total*100), "% )")
    print("Physical (Usual Discovery) ", phys, " of ", total, " (", (phys/total*100), "% )")
    

def overallDiscMethod():

    sm = 0
    net = 0
    otech = 0
    phys = 0

    for i in range(len(r)):
        if (isSocialMedia(r[i].disc) or isSocialMedia(r[i].udisc)):
            sm += 1
        if (isNetworks(r[i].disc) or isNetworks(r[i].udisc)):
            net += 1
        if (isOtherTech(r[i].disc) or isOtherTech(r[i].udisc)):
            otech += 1
        if (isPhysical(r[i].disc) or isPhysical(r[i].udisc)):
            phys += 1
        

    total = NUM_RESPONDENTS
    
    print("Social Media (Overall Discovery): ", sm, " of ", total, " (", (sm/total*100), "% )")
    print("Personal Networks (Overall Discovery): ", net, " of ", total, " (", (net/total*100), "% )")
    print("Other Technology (Overall Discovery): ", otech, " of ", total, " (", (otech/total*100), "% )")
    print("Physical (Overall Discovery) ", phys, " of ", total, " (", (phys/total*100), "% )")



# INFOSEC BOOLS

def isInfosecProblemEase(e):
    if (e.misinformation == 1 or e.censorship == 1 or e.sourceVerification == 1):
        return True
    else:
        return False

def isInfosecProblemSafe(s):
    if (s.noCredibility == 1 or s.misinformation == 1 or s.discernCredibility == 1 or s.communityVerification == 1 or s.censorship == 1 or s.unreliable == 1):
        return True
    else:
        return False

def isInfosecProblemImprov(i):
    if (i.sourceVerification == 1 or i.orgVerification == 1 or i.accountVerification == 1 or i.physicalVerification == 1 or i.documentEvidence == 1 or i.infoPrevEvents == 1):
        return True
    else:
        return False
    
def isInfosecProblemGeneral(r):
    if (isInfosecProblemEase(r.easeRat) or isInfosecProblemSafe(r.safeRat) or isInfosecProblemImprov(r.improv)):
        return True
    else:
        return False

########################## EASE RATIONALE ANALYSIS ##############################

def isConnectionsEase(e):
    if (e.connections == 1 or e.peopleShare == 1 or e.groupShare == 1 or e.alreadyKnow == 1 or e.disconnected == 1 or e.oneLeadsNext == 1):
        return True
    else:
        return False

def isTimingProblemEase(e):
    if (e.slowUpdates == 1 or e.noLiveFeed == 1):
        return True
    else:
        return False


def isFeatGoodEase(e):
    if (e.locationEvents == 1 or e.eventsInfo == 1 or e.searchGood == 1 or e.algorithmRecommendations == 1 or e.floodGood == 1 or e.cumulativeFeed == 1):
        return True
    else:
        return False


def isFeatBadEase(e):
    if (e.searchBad == 1 or e.floodBad == 1):
        return True
    else:
        return False


# Overall ease level
def easeLevel():

    level1 = 0
    level2 = 0
    level3 = 0
    level4 = 0
    level5 = 0
    na = 0


    for i in range(len(r)):
        l = r[i].ease.easeLevel
        if l == 1:
            level1 += 1
        elif l == 2:
            level2 += 1
        elif l == 3:
            level3 += 1
        elif l == 4:
            level4 += 1
        elif l == 5:
            level5 += 1
        else:
            na += 1

    total = level1 + level2 + level3 + level4 + level5
    
    print("Ease Level 1: ", level1, " of ", total, " (", (level1/total*100), "% )")
    print("Ease Level 2: ", level2, " of ", total, " (", (level2/total*100), "% )")
    print("Ease Level 3: ", level3, " of ", total, " (", (level3/total*100), "% )")
    print("Ease Level 4: ", level4, " of ", total, " (", (level4/total*100), "% )")
    print("Ease Level 5: ", level5, " of ", total, " (", (level5/total*100), "% )")


# For ease level = 3, how many were "easy if you are already connected; hard otherwise"
def easyIfConnected():

    total = 0
    eic = 0

    for i in range(len(r)):
        if (r[i].ease.easeLevel == 3):
            total += 1
            if (isConnectionsEase(r[i].easeRat)):
                eic += 1


    print("Easy if Connected: ", eic, " of ", total, " (", (eic/total*100), "% )")

# Ease rationale analysis
def easeRat():

    infosec = 0
    timing = 0
    conns = 0
    featGood = 0
    featBad = 0


    for i in range(len(r)):
        if (isInfosecProblemEase(r[i].easeRat)):
            infosec += 1
        if (isTimingProblemEase(r[i].easeRat)):
            timing += 1
        if (isConnectionsEase(r[i].easeRat)):
            conns += 1
        if (isFeatGoodEase(r[i].easeRat)):
            featGood += 1
        if (isFeatBadEase(r[i].easeRat)):
            featBad += 1
            

    total = NUM_RESPONDENTS
    
    print("Information Uncertainty (Ease): ", infosec, " of ", total, " (", (infosec/total*100), "% )")
    print("Timing Problems (Ease): ", timing, " of ", total, " (", (timing/total*100), "% )")
    print("Connections (Ease): ", conns, " of ", total, " (", (conns/total*100), "% )")
    print("Good Features (Ease): ", featGood, " of ", total, " (", (featGood/total*100), "% )")
    print("Bad Features (Ease): ", featBad, " of ", total, " (", (featBad/total*100), "% )")



########################## SAFETY RATIONALE ANALYSIS ##############################

# actively take steps to hide personal info
def isPrivProblemSafe(s):
    if (s.dontShare == 1 or s.falseIdentity == 1 or s.cautiousWhoSees == 1 or s.selfCensorship == 1 or s.postEventNoConvo or s.privatePage == 1 or s.dontOrganize == 1 or s.privateBrowsing == 1 or s.vpn == 1 or s.privateInfoPublic == 1 or s.noPrivacy == 1):
        return True
    else:
        return False

def isSecProblemSafe(s):
    if (s.hacking == 1 or s.phoneVulnerability or s.noEncryption):
        return True
    else:
        return False

def isDataProblemSafe(s):
    if (s.dataCollection == 1):
        return True
    else:
        return False

def isSurvProblemSafe(s):
    if (s.surveillance == 1 or s.alwaysWatching == 1 or s.employerRetribution == 1 or s.governmentSurveillance == 1 or s.trackActivists == 1):
        return True
    else:
        return False

def isPersonalDataSafe(s):
    if (isPrivProblemSafe(s) or isDataProblemSafe(s) or isSurvProblemSafe(s)):
        return True
    else:
        return False

def isNoBetterSafe(s):
    if (s.mostReach == 1 or s.easiestMethod == 1 or s.nothingBetter == 1 or s.quickestMethod == 1):
        return True
    else:
        False

def isNoThoughtSafe(s):
    if (s.hadntThought == 1):
        return True
    else:
        return False

def isWhitePrivSafe(s):
    if (s.whitePrivilege == 1 or s.triggeringPOC):
        return True
    else:
        return False

def isCommunitySafe(s):
    if (s.strengthInNumbers == 1 or s.strengthInCommunity == 1 or s.communityVerification == 1 or s.trustFriends == 1):
        return True
    else:
        return False

def isOtherTechSafe(s):
    if (s.signal == 1 or s.vpn == 1 or s.privateBrowsing == 1 or s.firewall == 1 or s.firewall):
        return True
    else:
        return False

def isValuesProblemSafe(s):
    if (s.differentValues == 1):
        return True
    else:
        return False

def isGeneralFearSafe(s):
    if (s.fear == 1 or s.powerToHarm == 1):
        return True
    else:
        return False

def isEduProblemSafe(s):
    if (s.vagueSecurity == 1):
        return True
    else:
        return False

def isEduGoodSafe(s):
    if (s.moreEducation == 1):
        return True
    else:
        return False


# General Safety Level
def safeLevel():

    level1 = 0
    level2 = 0
    level3 = 0
    level4 = 0
    level5 = 0
    na = 0


    for i in range(len(r)):
        l = r[i].safe.safetyLevel
        if l == 1:
            level1 += 1
        elif l == 2:
            level2 += 1
        elif l == 3:
            level3 += 1
        elif l == 4:
            level4 += 1
        elif l == 5:
            level5 += 1
        else:
            print(i)
            na += 1

    total = level1 + level2 + level3 + level4 + level5

    print("Safety Level 1: ", level1, " of ", total, " (", (level1/total*100), "% )")
    print("Safety Level 2: ", level2, " of ", total, " (", (level2/total*100), "% )")
    print("Safety Level 3: ", level3, " of ", total, " (", (level3/total*100), "% )")
    print("Safety Level 4: ", level4, " of ", total, " (", (level4/total*100), "% )")
    print("Safety Level 5: ", level5, " of ", total, " (", (level5/total*100), "% )")
    

# Safety Rationale Analysis
def safeRat():

    priv = 0
    sec = 0
    datamine = 0
    surv = 0
    pdata = 0
    nothink = 0
    nobetter = 0
    whitePriv = 0
    community = 0
    infosec = 0
    edubad = 0
    edugood = 0
    tech = 0 #do specific tech breakdown
    val = 0
    fear = 0

    for i in range(len(r)):
        s = r[i].safeRat
        if (isPrivProblemSafe(s)):
            priv += 1
        if (isSecProblemSafe(s)):
            sec += 1
        if (isDataProblemSafe(s)):
            datamine += 1
        if (isSurvProblemSafe(s)):
            surv += 1
        if (isPersonalDataSafe(s)):
            pdata += 1
        if (isNoThoughtSafe(s)):
            nothink += 1
        if (isNoBetterSafe(s)):
            nobetter += 1
        if (isWhitePrivSafe(s)):
            whitePriv += 1
        if (isCommunitySafe(s)):
            community += 1
        if (isInfosecProblemSafe(s)):
            infosec += 1
        if (isEduProblemSafe(s)):
            edubad += 1
        if (isEduGoodSafe(s)):
            edugood += 1
        if (isOtherTechSafe(s)):
            tech += 1
        if (isValuesProblemSafe(s)):
            val += 1
        if (isGeneralFearSafe(s)):
            fear += 1

    total = NUM_RESPONDENTS
    
    print("Privacy Concerns (Safety): ", priv, " of ", total, " (", (priv/total*100), "% )")           
    print("Security Concerns (Safety): ", sec, " of ", total, " (", (sec/total*100), "% )")
    print("Data Collection Concerns (Safety): ", datamine, " of ", total, " (", (datamine/total*100), "% )")
    print("Surveillance Concerns (Safety): ", surv, " of ", total, " (", (surv/total*100), "% )")
    print("General Personal Information Concerns (Safety): ", pdata, " of ", total, " (", (pdata/total*100), "% )")
    print("No Prior Thought (Safety): ", nothink, " of ", total, " (", (nothink/total*100), "% )")
    print("No Better Alternatives (Safety): ", nobetter, " of ", total, " (", (nobetter/total*100), "% )")
    print("White Privilege (Safety): ", whitePriv, " of ", total, " (", (whitePriv/total*100), "% )")
    print("Community Protection (Safety): ", community, " of ", total, " (", (community/total*100), "% )")
    print("Information Security Concerns (Safety): ", infosec, " of ", total, " (", (infosec/total*100), "% )")
    print("Educational Concerns (Safety): ", edubad, " of ", total, " (", (edubad/total*100), "% )")
    print("Educational Growth (Safety): ", edugood, " of ", total, " (", (edugood/total*100), "% )")
    print("Use of Privacy-Enhancing Technology (Safety): ", tech, " of ", total, " (", (tech/total*100), "% )")
    print("Values Difference Concern (Safety): ", val, " of ", total, " (", (val/total*100), "% )")
    print("General fear (Safety): ", fear, " of ", total, " (", (fear/total*100), "% )")



############################ IMPROVEMENT ANALYSIS ################################

def isAllInOneImprov(i):
    if (i.allInOne == 1):
        return True
    else:
        return False

def isNoSMImprov(i):
    if (i.noSocialMedia == 1):
        return True
    else:
        return False

def isMoneyImprov(i):
    if (i.noFinancialIncentive == 1 or i.noAds == 1):
        return True
    else:
        return False

def isCorpBadImprov(i):
    if (i.noSocialMedia == 1 or i.noFinancialIncentive == 1 or i.noPowerIncentive == 1 or i.noSurveillanceIncentive == 1 or i.moralAlignment == 1 or i.stopFuelingAnxiety == 1):
        return True
    else:
        return False

def isAnonImprov(i):
    if (i.anonymity == 1 or i.numPeopleNoID == 1):
        return True
    else:
        return False

def isCommunityImprov(i):
    if (i.democratized == 1 or i.decentralized == 1 or i.communityControlled == 1):
        return True
    else:
        return False

def isEncImprov(i):
    if (i.encryption == 1):
        return True
    else:
        return False

def isSecImprov(i):
    if (i.security == 1 or i.noHacking == 1):
        return True
    else:
        return False

def isUsabilityImprov(i):
    if (i.userFriendly == 1):
        return True
    else:
        return False

def isPrivImprov(i):
    if (isSurvImprov(i) or i.noDataCollection == 1 or i.privacy == 1 or isAnonImprov(i) or i.onlyOrganizersSee == 1 or i.noEmailPhoneLink == 1):
        return True
    else:
        return False

def isDataImprov(i):
    if (i.noDataCollection == 1):
        return True
    else:
        return False

def isSurvImprov(i):
    if (i.noSurveillanceIncentive == 1 or i.noGovernmentTies == 1):
        return True
    else:
        return False

def isFeatImprov(i):
    if (i.protectedCategories == 1 or i.sponsoredPosts == 1 or i.reminders == 1 or i.liveFeed == 1 or i.routeInfo == 1 or i.eventCalendar == 1 or i.orgCoordination == 1 or i.allyInstructions == 1):
        return True
    else:
        return False

def isEduImprov(i):
    if (i.cyberLiteracy == 1 or i.rightsLiteracy == 1 or i.notQualified):
        return True
    else:
        return False

def isGenSecImprov(i):
    if (isDataImprov(i) or isEncImprov(i) or isPrivImprov(i)):
        return True
    else:
        return False

def isValuesImprov(i):
    if (i.moralAlignment == 1):
        return True
    else:
        return False

# Improvement recommendations analysis
def improv():

    aio = 0
    nosm = 0
    corpbad = 0
    anon = 0
    community = 0
    enc = 0
    sec = 0
    ease = 0
    priv = 0
    data = 0
    surv = 0
    val = 0
    feat = 0
    money = 0
    edu = 0
    cred = 0
    gensec = 0

    for i in range(len(r)):
        j = r[i].improv
        if (isAllInOneImprov(j)):
            aio += 1
        if (isNoSMImprov(j)):
            nosm += 1
        if (isCorpBadImprov(j)):
            corpbad += 1
        if (isAnonImprov(j)):
            anon += 1
        if (isCommunityImprov(j)):
            community += 1
        if (isEncImprov(j)):
            enc += 1
        if (isSecImprov(j)):
            sec += 1
        if (isUsabilityImprov(j)):
            ease += 1
        if (isPrivImprov(j)):
            priv += 1
        if (isDataImprov(j)):
            data += 1
        if (isSurvImprov(j)):
            surv += 1
        if (isValuesImprov(j)):
            val += 1
        if (isFeatImprov(j)):
            feat += 1
        if (isMoneyImprov(j)):
            money += 1
        if (isEduImprov(j)):
            edu += 1
        if (isInfosecProblemImprov(j)):
            cred += 1
        if (isGenSecImprov(j)):
            gensec += 1

    total = NUM_RESPONDENTS - 2
    
    print("All in One Platform (Improv): ", aio, " of ", total, " (", (aio/total*100), "% )")
    print("No Social Media (Improv): ", nosm, " of ", total, " (", (nosm/total*100), "% )")
    print("Negativity Towards Corporations (Improv): ", corpbad, " of ", total, " (", (corpbad/total*100), "% )")
    print("Anonymity (Improv): ", anon, " of ", total, " (", (anon/total*100), "% )")
    print("Community Control (Improv): ", community, " of ", total, " (", (community/total*100), "% )")
    print("Encryption (Improv): ", enc, " of ", total, " (", (enc/total*100), "% )")
    print("Security (Improv): ", sec, " of ", total, " (", (sec/total*100), "% )")
    print("Usability (Improv): ", ease, " of ", total, " (", (ease/total*100), "% )")
    print("Privacy (Improv): ", priv, " of ", total, " (", (priv/total*100), "% )")
    print("No Data Collection (Improv): ", data, " of ", total, " (", (data/total*100), "% )")
    print("No Surveillance (Improv): ", surv, " of ", total, " (", (surv/total*100), "% )")
    print("Values Alignment (Improv): ", val, " of ", total, " (", (val/total*100), "% )")
    print("Suggested Features (Improv): ", feat, " of ", total, " (", (feat/total*100), "% )")
    print("No Financial Incentive (Improv): ", money, " of ", total, " (", (money/total*100), "% )")
    print("More Education (Improv): ", edu, " of ", total, " (", (edu/total*100), "% )")
    print("Authentication (Improv): ", cred, " of ", total, " (", (cred/total*100), "% )")
    print("General Security (Improv): ", gensec, " of ", total, " (", (gensec/total*100), "% )")
       

############################ COMBINED ANALYSIS ################################

def isInfosecProblemGeneral(r):
    if (isInfosecProblemEase(r.easeRat) or isInfosecProblemSafe(r.safeRat) or isInfosecProblemImprov(r.improv)):
        return True
    else:
        return False

def isPrivProblemGeneral(r):
    if (isPersonalDataSafe(r.safeRat) or isPrivImprov(r.improv)):
        return True
    else:
        return False

def isSurvProblemGeneral(r):
    if (isSurvProblemSafe(r.safeRat) or isSurvImprov(r.improv)):
        return True
    else:
        return False

def isCommunityGeneral(r):
    if (isConnectionsEase(r.easeRat) or isCommunitySafe(r.safeRat) or isCommunityImprov(r.improv)):
        return True
    else:
        return False

def isDataProblemGeneral(r):
    if (isDataProblemSafe(r.safeRat) or isDataImprov(r.improv)):
        return True
    else:
        return False

# General information security concern
def infosecConcern():

    infosecEase = 0
    infosecSafe = 0
    infosecImp = 0
    infosec = 0
    
    for i in range(len(r)):
        if (isInfosecProblemEase(r[i].easeRat)):
            infosecEase += 1
        if (isInfosecProblemSafe(r[i].safeRat)):
            infosecSafe += 1
        if (isInfosecProblemImprov(r[i].improv)):
            infosecImp += 1
        if (isInfosecProblemGeneral(r[i])):
            infosec += 1

    total = NUM_RESPONDENTS

    print("Information Uncertainty (Ease): ", infosecEase, " of ", total, " (", (infosecEase/total*100), "% )")
    print("Information Uncertainty (Safety): ", infosecSafe, " of ", total, " (", (infosecSafe/total*100), "% )")
    print("Information Uncertainty (Improvement): ", infosecImp, " of ", total, " (", (infosecImp/total*100), "% )")
    print("Information Uncertainty (Total): ", infosec, " of ", total, " (", (infosec/total*100), "% )")

# General surveillance concern
def survConcern():

    survSafe = 0
    survImp = 0
    surv = 0


    for i in range(len(r)):
        if (isSurvProblemSafe(r[i].safeRat)):
            survSafe += 1
        if (isSurvImprov(r[i].improv)):
            survImp += 1
        if (isSurvProblemGeneral(r[i])):
            surv += 1

    total = NUM_RESPONDENTS

    print("Surveillance Concern (Safety): ", survSafe, " of ", total, " (", (survSafe/total*100), "% )")
    print("Surveillance Concern (Improvement): ", survImp, " of ", total, " (", (survImp/total*100), "% )")
    print("Surveillance Concern (Total): ", surv, " of ", total, " (", (surv/total*100), "% )")


# General privacy concern
def privConcern():

    privSafe = 0
    privImp = 0
    priv = 0


    
    for i in range(len(r)):
        if (isPersonalDataSafe(r[i].safeRat)):
            privSafe += 1
        if (isPrivImprov(r[i].improv)):
            privImp += 1
        if (isPrivProblemGeneral(r[i])):
            priv += 1

    total = NUM_RESPONDENTS

    print("Privacy Concern (Safety): ", privSafe, " of ", total, " (", (privSafe/total*100), "% )")
    print("Privacy Concern (Improvement): ", privImp, " of ", total, " (", (privImp/total*100), "% )")
    print("Privacy Concern (Total): ", priv, " of ", total, " (", (priv/total*100), "% )")

# General data concern
def dataConcern():

    dataSafe = 0
    dataImp = 0
    data = 0


    
    for i in range(len(r)):
        if (isDataProblemSafe(r[i].safeRat)):
            dataSafe += 1
        if (isDataImprov(r[i].improv)):
            dataImp += 1
        if (isDataProblemGeneral(r[i])):
            data += 1

    total = NUM_RESPONDENTS

    print("Data Concern (Safety): ", dataSafe, " of ", total, " (", (dataSafe/total*100), "% )")
    print("Data Concern (Improvement): ", dataImp, " of ", total, " (", (dataImp/total*100), "% )")
    print("Data Concern (Total): ", data, " of ", total, " (", (data/total*100), "% )")

# Privacy or surveillance concern
def privSurvConcern():

    ps = 0

    for i in range(len(r)):
        if (isPrivProblemGeneral(r[i]) or isSurvProblemGeneral(r[i])):
            ps += 1

    total = NUM_RESPONDENTS

    print("Privacy or Surveillance Concern (Total): ", ps, " of ", total, " (", (ps/total*100), "% )")


# Community power
def commStr():
    
    commsEase = 0
    commsSafe = 0
    commsImp = 0
    comms = 0
    
    for i in range(len(r)):
        if (isConnectionsEase(r[i].easeRat)):
            commsEase += 1
        if (isCommunitySafe(r[i].safeRat)):
            commsSafe += 1
        if (isCommunityImprov(r[i].improv)):
            commsImp += 1
        if (isCommunityGeneral(r[i])):
            comms += 1

    total = NUM_RESPONDENTS

    print("Community Power (Ease): ", commsEase, " of ", total, " (", (commsEase/total*100), "% )")
    print("Community Power (Safety): ", commsSafe, " of ", total, " (", (commsSafe/total*100), "% )")
    print("Community Power (Improvement): ", commsImp, " of ", total, " (", (commsImp/total*100), "% )")
    print("Community Power (Total): ", comms, " of ", total, " (", (comms/total*100), "% )")


############################ PRINT ANALYSIS ################################

discMethod()
print("\n")
udiscMethod()
print("\n")
overallDiscMethod()
print("\n")
easeLevel()
easyIfConnected()
print("\n")
easeRat()
print("\n")
safeLevel()
print("\n")
safeRat()
print("\n")
improv()
print("\n")
infosecConcern()
print("\n")
privConcern()
print("\n")
survConcern()
print("\n")
dataConcern()
print("\n")
privSurvConcern()
print("\n")
commStr()

