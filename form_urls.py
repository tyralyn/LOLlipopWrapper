import get_api_key

#strings holding api parts
#api in form of requestPrefix + requestContent+ requestGlue + the actual API key

requestPrefix="https://na.api.pvp.net"
requestGlue="?api_key="

BRAZIL = 'br'
EUROPE_NORDIC_EAST = 'eune'
EUROPE_WEST =  'euw'
LATIN_AMERICA_NORTH = 'lan'
LATIN_AMERICA_SOUTH = 'las'
NORTH_AMERICA = 'na'
OCEANIA = 'oce'
RUSSIA = 'ru'
TURKEY = 'tr'
SOUTH_EAST_ASIA = 'sea'
REPUBLIC_OF_KOREA = 'kr'
PUBLIC_BETA_ENVIRONMENT = 'pbe'

DEFAULT_REGION = NORTH_AMERICA

champDatabase = {}

#requestContents
def getAllChampsSuffix():
	return "/api/lol/"+DEFAULT_REGION+"/v1.2/champion"

def getChampSuffix(champID):
	return  "/api/lol/"+DEFAULT_REGION+"/v1.2/champion/"+champID		

def getRequestURL(suffix):
	return (requestPrefix+getAllChampsSuffix()+requestGlue+get_api_key.getAPIKey())
