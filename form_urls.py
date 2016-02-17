import get_api_key
import time
import datetime

#strings holding api parts
#api in form of requestPrefix + requestContent+ requestGlue + the actual API key

requestPrefix="https://na.api.pvp.net"
requestGlue="api_key="
lolAPIPathPrefix="/api/lol"
championMasteryPathPrefix="/championmastery/location"
publicTournamentPathPrefix="/tournament/public"
shardsPathPrefix="/shards"
observerModePathPrefix="/observer-mode"

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

versions={ 'CHAMPION': 'v1.2',
'CHAMPION_MASTERY': '',
'CURRENT_GAME': 'v1.0',
'FEATURED_GAME': 'v1.0',
'GAME': 'v1.3',
'LEAGUE': 'v2.5',
'LOL_STATIC_DATA': 'v1.2',
'LOL_STATUS': 'v1.0',
'MATCH': 'v2.2',
'MATCH_LIST': 'v2.2',
'STATS': 'v1.3',
'SUMMONER': 'v1.4',
'TEAM': 'v2.4'}

basic_request_types={ 'CHAMPION': 'champion',
'CHAMPION_MASTERY': '',
'CURRENT_GAME': '',
'FEATURED_GAME': '',
'GAME': 'game',
'LEAGUE': 'league',
'LOL_STATIC_DATA': 'static-data',
'LOL_STATUS': 'status',
'MATCH': 'match',
'MATCH_LIST': 'matchlist',
'STATS': 'stats',
'SUMMONER': 'summoner',
'TEAM': 'team'}

by={"SUMMONER": 'summoner',
"TEAM": 'team',
"TOURNAMENT":'tournament',
"ACCOUNT": 'account'
"NAME":'name'
"CODE":'code'
}

#path_variables = ={ 'CHAMPION': 'champion',
##'CHAMPIONS':'champions',
#'PLAYER': 'player',
#'SCORE': 'score'
#'TOP_CHAMPIONS': 'topchampions',
#'BY_SUMMONER': '',
##'CURRENT_GAME': 'v1.0',
##'FEATURED_GAME': 'featured',
#'GAME': 'game',
##'LEAGUE': 'v2.5',
#'LOL_STATIC_DATA': 'v1.2',
#'LOL_STATUS': 'v1.0',
#'MATCH': 'v2.2',
#'MATCH_LIST': 'v2.2',
#'STATS': 'v1.3',
#'SUMMONER': 'v1.4',
#'TEAM': 'v2.4'}

champDatabase = {}

#for getting an epochMilliseconds time to pass to matchlist requests
def dateAndTimeToEpochMilliseconds(year, month, day, hour=0, minute=0, second=0, millisecond=0):
        return (1000*time.mktime(datetime.datetime(year, month, day, hour, minute, second, millisecond).timetuple()))

#construct entire URL given path and values, for all requests
def constructRequestURL(path, values):
        return ()


def basicRequestSuffix(static, region, version, requestType):
        if static:
        else:


#######################
#  champion suffixes  #
#######################
def allChampions(regionId):
	return "/api/lol/"+regionId+"/"+versions['CHAMPION']+"/champion?"

def champion(regionId, championId):
	return  "/api/lol/"+regionId+"/"+versions['CHAMPION']+"/champion/"+str(championId)+"?"

######################
#  mastery suffixes  #
######################
def championMastery(platformId, summonerId, championId):
        return "/championmastery/location/"+platformId+"/player/"+str(summonerId)+"/champion/"+str(championId)+"?"

def allChampionMasteries(platformId, summonerId, championId):
        return "/championmastery/location"+platformId+"/player/"+str(summonerId)+"/champions?"

def championMasteryScore(platformId, summonerId):
        return "/championmastery/location/"+platformId+"/player/"+str(summonerId)+"/score?"

def topNChampionMasteries(platformId, summonerId, n):
        return "/championmastery/location/"+platformId+"/player/"+str(summonerId)+"/topchampions"+"?count="+str(n)+"&"

###########################
#  current game suffixes  #
###########################
def currentGameInfo(platformId, summonerId):
        return "/observer-mode/rest/consumer/getSpectatorGameInfo/"+platformId+"/"+summonerId+"?"

#############################
#  featured games suffixes  #
#############################
def featuredGamesList():
        return "/observer-mode/rest/featured?"

###########################
#  recent games suffixes  #
###########################
def recentGames(regionId, summonerId):
        return "/api/lol/"+regionId+"/v1.3/game/by-summoner/"+str(summonerId)+"/recent?"

######################
#  leagues suffixes  #
######################
def leaguesBySummoner(regionId, summonerIds):
        s= "/api/lol/"+regionId+"/v2.5/league/by-summoner/"
        summonerList=','.join(map(str,summonerIds))
        s = s + summonerList + "?"
        return s

def leagueEntriesBySummoner(regionId, summonerIds):
        s=leaguesBySummonerSuffix(regionId, summonerIds)
        s=s[:-1]+"/entry?"
        return s
        

#def leaguesByTeamSuffix(regionId, teamIds)

#def leagueEntriesByTeamSuffix(regionId, teamIds)

def challengerTierLeagues(regionId):
        return "/api/lol/"+regionId+"/v2.5/league/challenger"

def masterTierLeagues(regionId):
        return "/api/lol/"+regionId+"/v2.5/league/master"

####################
#  match suffixes  #
####################
def match(regionId, matchId, includeTimeline=False):
        return "/api/lol/"+regionId+"/v2.2/match/"+str(matchId)+"?includeTimeline="+str(includeTimeline)+"&"        

########################
#  matchlist suffixes  #
########################
def matchList(regionId, summonerId, championIds=[], rankedQueues=[], seasons=[], beginTime=-1, endTime=-1, beginIndex=-1, endIndex=-1):
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
def rankedStats(regionId, summonerId, season=""):
        seasonString = "" if season == "" else ("season="+season+"&")
        return "/api/lol/"+regionId+"/v1.3/stats/by-summoner/"+str(summonerId)+"/ranked?"+seasonString
        
def playerStats(regionId, summonerId, season=""):
        seasonString = "" if season == "" else ("season="+season+"&")
        return "/api/lol/"+regionId+"/v1.3/stats/by-summoner/"+str(summonerId)+"/summary?"+seasonString

#######################
#  summoner suffixes  #
#######################
#def summonersByAccountIdsSuffix(regionId, accountIds):

def summonersByNames(regionId, summonerNames):
        summonerNamesList=','.join(summonerNames)
        return "/api/lol/"+regionId+"/v1.4/summoner/by-name/"+summonerNamesList+"?"

def summonersBySummonerIds(regionId, summonerIds):
        summonerIdsList=','.join(map(str,summonerIds))
        return "/api/lol/"+regionId+"/v1.4/summoner/"+summonerIdsList+"?"

def masteryPagesBySummonerIds(regionId, summonerIds):
        summonerIdsList=','.join(map(str,summonerIds))
        return "/api/lol/"+regionId+"/v1.4/summoner/"+summonerIdsList+"/masteries?"

def summonerNamesBySummonerIds(regionId, summonerIds):
        summonerIdsList=','.join(map(str,summonerIds))
        return "/api/lol/"+regionId+"/v1.4/summoner/"+summonerIdsList+"/name?"

def runePagesBySummonerIds(regionId, summonerIds):
        summonerIdsList=','.join(map(str,summonerIds))
        return "/api/lol/"+regionId+"/v1.4/summoner/"+summonerIdsList+"/runes?"

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


###################
#  team suffixes  #
###################
def teamsBySummonerIds(regionId, summonerIds):
        summonerIdsList=','.join(map(str,summonerIds))
        return "/api/lol/"+regionId+"/v2.4/team/by-summoner/"+summonerIdsList+"?"

def teamsByTeamIds(regionId, teamIds):
        teamIdsList=','.join(map(str,teamIds))
        return "/api/lol/"+regionId+"/v2.4/team/"+teamIdsList+"?"

##########################################
#  get the request URL given the suffix  #
##########################################
def getRequestURL(suffix):
	return (requestPrefix+suffix+requestGlue+get_api_key.getAPIKey())
