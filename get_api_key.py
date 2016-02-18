#requires path of file that stores the apiKey
def getAPIKey(filePath):
    apiKeyFilePath = filePath
    f = open(apiKeyFilePath,'r')
    apiKey=f.read()
    return apiKey
filePath='C:\\Users\\tyralyn\\Desktop\\programming\\lolAPIWrapper\\api_key.txt'
apiKey = getAPIKey(filePath)
