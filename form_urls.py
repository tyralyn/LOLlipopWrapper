import get_api_key
import time
import datetime

#strings holding api parts
#api in form of requestPrefix + requestContent+ requestGlue + the actual API key

requestPrefix="https://na.api.pvp.net/"
domainName="https://na.api.pvp.net/"


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
'RECENT_GAMES': 'game',
'LEAGUE': 'league',
'LOL_STATIC_DATA': 'static-data',
'LOL_STATUS': 'status',
'MATCH': 'match',
'MATCH_LIST': 'matchlist',
'STATS': 'stats',
'SUMMONER': 'summoner',
'TEAM': 'team'}

path_parts ={ 'API':'api',
'LOL':'lol',
'CHAMPION': 'champion',
'CHAMPIONS':'champions',
'PLAYER': 'player',
'SCORE': 'score',
'TOP_CHAMPIONS': 'topchampions',
'ENTRIES': 'entry',
'CHALLENGER':'challenger',
'MASTER':'master',
'ITEM':'item',
'LANGUAGE_STRINGS':'language-strings',
'MAP':'map',
'MASTERY':'mastery',
'MASTERIES':'mastery',
'REALM':'realm',
'RUNE':'rune',
'RUNES':'runes',
'NAME':'name',
'SUMMONER_SPELL':'summoner-spell',
'VERSIONS':'versions',
'RANKED':'ranked',
'SUMMARY':'summary'}

param_parts = { 'API_KEY': 'api_key',
'BY_SUMMONER': 'by-summoner',
'BY_TEAM': 'by-team',
'BY_TOURNAMENT':'by-tournament',
'BY_ACCOUNT': 'by-account',
'BY_NAME':'by-name',
'BY_CODE':'by-code',
'INCLUDE_TIMELINE' : 'includeTimeline'
}

champDatabase = {}

#for getting an epochMilliseconds time to pass to matchlist requests
def dateAndTimeToEpochMilliseconds(year, month, day, hour=0, minute=0, second=0, millisecond=0):
        return (1000*time.mktime(datetime.datetime(year, month, day, hour, minute, second, millisecond).timetuple()))

class baseReqURL:
        apiKey =  get_api_key.getAPIKey(get_api_key.filePath)
        requestType='BASE'
        def __init__(self):
                self.path = []
                self.params = {'API_KEY': self.apiKey}

        #returns list of path items as a string joined by '/' for URL construction
        def pathString(self): 
                return '/'.join(map(str,self.path))

        #returns dictionary of values as joined for URL
        def valueString(self):
                l = [ str(param_parts[k])+"="+str(v) for k, v in self.params.items()]
                return '&'.join(l)

        #construct entire URL given path and values, for all requests
        def constructReqURL(self):
                return domainName + self.pathString()+"?"+self.valueString()

        def printReqURL(self):
                print ("path: ", self.path)
                print ("params: ", self.params)
                print (self.constructReqURL())



class basicAPIReq(baseReqURL):
        pathPrefix=lolAPIPathPrefix
        regionId=region_ids[DEFAULT_REGION]
        requestType='BASIC'
        def __init__(self, requestType): 
                baseReqURL.__init__(self)
                self.path.append(path_parts['API'])
                self.path.append(path_parts['LOL'])
                self.path.append(self.regionId)
                self.requestType=requestType
                self.path.append(versions[self.requestType])
                self.path.append(basic_request_types[self.requestType])
        def setRegion(region):
                DEFAULT_REGION=region

#######################
#  champion suffixes  #
#######################
class championReq(basicAPIReq):
        def __init__(self):
                basicAPIReq.__init__(self, 'CHAMPION')
        def allChampions(self):
                return self
        def champion(self, championId):
                self.path.append(str(championId))
                return self

###########################
#  recent games suffixes  #
###########################
class recentGamesReq(basicAPIReq):
        def __init__(self):
                basicAPIReq.__init__(self, 'RECENT_GAMES')
        def recentGames(self):
                return self

######################
#  leagues suffixes  #
######################
class leagueReq(basicAPIReq):
        def __init__(self):
                basicAPIReq.__init__(self, 'LEAGUE')
        def leaguesBySummoner(regionId, summonerIds):
                self.path = self.path + summonerIds
                return self

        def leagueEntriesBySummoner(regionId, summonerIds):
                self.path = self.path + summonerIds
                self.path.append(path_parts['ENTRIES'])
                return self

        #def leaguesByTeamSuffix(regionId, teamIds)
        #def leagueEntriesByTeamSuffix(regionId, teamIds)
        def challengerLeagues():
                self.path.append(path_parts['CHALLENGER'])
                return self

        def masterLeagues():
                self.path.append(path_parts['MASTER'])
                return self

####################
#  match suffixes  #
####################

class matchReq(basicAPIReq):
        def __init__(self):
                basicAPIReq.__init__(self, 'MATCH')
        def matches(regionId, matchId, includeTimeline=False):
                self.path.append(regionId)
                self.path.append(matchId)
                self.params['INCLUDE_TIMELINE']=includeTimeline
                return self
