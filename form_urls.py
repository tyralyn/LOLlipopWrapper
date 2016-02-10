import get_api_key
import time
import datetime

#strings holding api parts
#api in form of requestPrefix + requestContent+ requestGlue + the actual API key

requestPrefix="https://na.api.pvp.net"
requestGlue="api_key="

DEFAULT_REGION='NORTH_AMERICA'

region_ids = {'BRAZIL' : 'br',
'EUROPE_NORDIC_EAST' : 'eune',
'EUROPE_WEST' :  'euw',
'LATIN_AMERICA_NORTH' : 'lan',
'LATIN_AMERICA_SOUTH' : 'las',
'NORTH_AMERICA' : 'na',
'OCEANIA' : 'oce',
'RUSSIA' : 'ru',
'TURKEY' : 'tr',
'SOUTH_EAST_ASIA' : 'sea',
'REPUBLIC_OF_KOREA' : 'kr',
'PUBLIC_BETA_ENVIRONMENT' : 'pbe'}

platform_ids = {'BRAZIL' : 'BR1',
'EUROPE_NORDIC_EAST' : 'EUN1',
'EUROPE_WEST' :  'EUW1',
'LATIN_AMERICA_NORTH' : 'LA1',
'LATIN_AMERICA_SOUTH' : 'LA2',
'NORTH_AMERICA' : 'NA1',
'OCEANIA' : 'OC1',
'RUSSIA' : 'RU',
'TURKEY' : 'TR1',
'SOUTH_EAST_ASIA' : '',
'REPUBLIC_OF_KOREA' : '',
'PUBLIC_BETA_ENVIRONMENT' : 'PBE',
'GLOBAL' : ''}

champDatabase = {}

def dateAndTimeToEpochMilliseconds(year, month, day, hour=0, minute=0, second=0, millisecond=0):
        return (1000*time.mktime(datetime.datetime(year, month, day, hour, minute, second, millisecond).timetuple()))

#######################
#  champion suffixes  #
#######################
def allChampionsSuffix(regionId):
	return "/api/lol/"+regionId+"/v1.2/champion?"

def championSuffix(regionId, championId):
	return  "/api/lol/"+regionId+"/v1.2/champion/"+str(championId)+"?"

######################
#  mastery suffixes  #
######################
def championMasterySuffix(platformId, summonerId, championId):
        return "/championmastery/location/"+platformId+"/player/"+str(summonerId)+"/champion/"+str(championId)+"?"

def allChampionMasteriesSuffix(platformId, summonerId, championId):
        return "/championmastery/location"+platformId+"/player/"+str(summonerId)+"/champions?"

def championMasteryScoreSuffix(platformId, summonerId):
        return "/championmastery/location/"+platformId+"/player/"+str(summonerId)+"/score?"

def topNChampionMasteriesSuffix(platformId, summonerId, n):
        return "/championmastery/location/"+platformId+"/player/"+str(summonerId)+"/topchampions"+"?count="+str(n)+"&"

###########################
#  current game suffixes  #
###########################
def currentGameInfoSuffix(platformId, summonerId):
        return "/observer-mode/rest/consumer/getSpectatorGameInfo/"+platformId+"/"+summonerId+"?"

#############################
#  featured games suffixes  #
#############################
def featuredGamesListSuffix():
        return "/observer-mode/rest/featured?"

###########################
#  recent games suffixes  #
###########################
def recentGamesSuffix(regionId, summonerId):
        return "/api/lol/"+regionId+"/v1.3/game/by-summoner/"+str(summonerId)+"/recent?"

######################
#  leagues suffixes  #
######################
def leaguesBySummonerSuffix(regionId, summonerIds):
        s= "/api/lol/"+regionId+"/v2.5/league/by-summoner/"
        summonerList=','.join(map(str,summonerIds))
        s = s + summonerList + "?"
        return s

def leagueEntriesBySummonerSuffix(regionId, summonerIds):
        s=leaguesBySummonerSuffix(regionId, summonerIds)
        s=s[:-1]+"/entry?"
        return s
        

#def leaguesByTeamSuffix(regionId, teamIds)

#def leagueEntriesByTeamSuffix(regionId, teamIds)

def challengerTierLeaguesSuffix(regionId):
        return "/api/lol/"+regionId+"/v2.5/league/challenger"

def masterTierLeaguesSuffix(regionId):
        return "/api/lol/"+regionId+"/v2.5/league/master"

####################
#  match suffixes  #
####################
def matchSuffix(regionId, matchId, includeTimeline=False):
        return "/api/lol/"+regionId+"/v2.2/match/"+str(matchId)+"?includeTimeline="+str(includeTimeline)+"&"        

########################
#  matchlist suffixes  #
########################
def matchListSuffix(regionId, summonerId, championIds=[], rankedQueues=[], seasons=[], beginTime=-1, endTime=-1, beginIndex=-1, endIndex=-1):
        optionalParameters = []
        if (len(championIds)>0):
                optionalParameters.append("championIds="+','.join(map(str,championIds)))
        if (len(rankedQueues)>0):
                optionalParameters.append("rankedQueues="+','.join(rankedQueues))
        if (len(seasons)>0):
                optionalParameters.append("seasons="+','.join(seasons))
        if (beginTime>0):
                optionalParameters.append("&beginTime="+str(int(beginTime)))
        if (endTime>0):
                optionalParameters.append("endTime="+str(int(endTime)))
        if (beginIndex>0):
                optionalParameters.append("beginIndex="+str(beginIndex))
        if (endIndex>0):
                optionalParameters.append("endIndex="+str(endIndex))
        s="/api/lol/"+regionId+"/v2.2/matchlist/by-summoner/"+str(summonerId)+"?"+('&'.join(optionalParameters))+'&'
        return s

#############################
#  summoner stats suffixes  #
#############################
#def rankedStatsSuffix(regionId, summonerId, season)
        
#def playerStatsSuffix(regionId, summonerId, season)


##########################
#  static data suffixes  #
##########################
#def championsListSuffix(regionId, locale, version dataById, champData)

#def championSuffix(regionId, championId, locale, version, champData)

#def itemsListSuffix(regionId, locale, version, itemListData)

#def itemSuffix(regionId, itemId, locale, version, itemData)

#def languageStringsDataSuffix(regionId, locale, version)

#def supportedLanguagesDataSuffix(regionId)

#def mapDataSuffix(regionId, locale, version)

#def masteryListSuffix(regionId, locale, version, masteryListData)

#def masterySuffix(region, masteryId, locale, version, masteryData)

#def realmSuffix(regionId)

#def runesListSuffix(regionId, locale, version, runeListData)

#def runeSuffix(regionId, runeId, locale, version, runeData)

#def summonerSpellListSuffix(regionId, locale, version, spellListData)

#def summonerSpellSuffix(regionId, spellId, locale, version, spellData)

#def versionDataSuffix(regionId)

#######################
#  summoner suffixes  #
#######################
#def summonersByAccountIdsSuffix(regionId, accountIds)

#def summonersByNamesSuffix(regionId, summonerNames)

#def summonersBySummonerIdsSuffix(regionId, summonerIds)

#def masteryPagesBySummonerIdsSuffix(regionId, summonerIds)

#def summonerNamesBySummonerIdsSuffix(regionId, summonerIds)

#def runePagesBySummonerIdsSuffix(regionId, summonerIds)

###################
#  team suffixes  #
###################
#def teamsBySummonerIdsSuffix(regionId, summonerIds)

#def teamsByTeamIdsSuffix(regionId, teamIds)

##########################################
#  get the request URL given the suffix  #
##########################################
def getRequestURL(suffix):
	return (requestPrefix+suffix+requestGlue+get_api_key.getAPIKey())
