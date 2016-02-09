#requires path of file that stores the apiKey
def getAPIKey():
    apiKeyFilePath = 'C:\\Users\\tyralyn\\Desktop\\programming\\lolAPIWrapper\\api_key.txt'
    f = open(apiKeyFilePath,'r')
    apiKey=f.read()
    return apiKey
