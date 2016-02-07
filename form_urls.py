import get_api_key

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

freestylinrough = 28328081
champDatabase = {}

#requestContents
def getAllChampsSuffix(regionId):
	return "/api/lol/"+regionId+"/v1.2/champion?"

def getChampSuffix(regionId, championId):
	return  "/api/lol/"+regionId+"/v1.2/champion/"+str(championId)+"?"

def getChampMastery(platformId, summonerId, championId):
        return "/championmastery/location/"+platformId+"/player/"+str(summonerId)+"/champion/"+str(championId)+"?"

def getAllChampMasteries(platformId, summonerId, championId):
        return "/championmastery/location"+platformId+"/player/"+str(summonerId)+"/champions?"

def getChampMasteryScore(platformId, summonerId):
        return "/championmastery/location/"+platformId+"/player/"+str(summonerId)+"/score?"

def getTopNChampMasteries(platformId, summonerId, n):
        return "/championmastery/location/"+platformId+"/player/"+str(summonerId)+"/topchampions"+"?count="+str(n)+"&"

def getCurrentGame(platformId, summonerId):
        return "/observer-mode/rest/consumer/getSpectatorGameInfo/"+platformId+"/"+summonerId+"?"

def getFeaturedGames():
        return "/observer-mode/rest/featured?"

def getRequestURL(suffix):
	return (requestPrefix+suffix+requestGlue+get_api_key.getAPIKey())
