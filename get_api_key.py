#requires path of file that stores the apiKey
def getAPIKey():
    apiKeyFilePath = 'C:\\Users\\tyralyn\\Desktop\\pythonStuff\\lol\\api_key.txt'
    f = open(apiKeyFilePath,'r')
    apiKey=f.read()
    return apiKey
