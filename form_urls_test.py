########################################################################
#                                                                      #
#   Testing functionality of form_urls methods: checks to determine    #
#   whether URLs made in form_urls.py make correct calls to LOL API    #
#   Calls that are incorrect in format should return JSON content      #
#   comprised of a status key and status message and code (bad API     #
#   calls). Calls that are not proper URLS (URLS that lead to una-     #
#   vailable webpages are connection errors. Code should currently     #
#   connection errors, as well as all of the other possible requests   #
#   exceptions. See http://docs.python-requests.org/en/latest/user/    #
#   quickstart/#errors-and-exceptions for more information about re-   #
#   quests exceptions and errors.                                      #
#                                                                      #
########################################################################

import form_urls
import requests
import requests_cache
import json

freestylinrough = 28328081
gammajoker=29719769
spiritualcreed=45315427
xxlobsterxxcrabx=20022996
westrice= 19674238
bates550=22453757
summonerIdList=[freestylinrough, gammajoker, spiritualcreed, xxlobsterxxcrabx, westrice, bates550]


bates550Match1=2091919922
bates550Match2=2091856984
bates550Match3=2091697670
positiveteamenvironment="TEAM-3ed957d0-3f21-11e5-bc58-c81f66dcfb5a"

NAPlatform=form_urls.platform_ids[form_urls.DEFAULT_REGION]
NARegion = form_urls.region_ids[form_urls.DEFAULT_REGION]

b1=form_urls.baseReqURL()
b2=form_urls.basicAPIReq('LEAGUE')
b3=form_urls.championReq().allChampions()
b4=(form_urls.championReq()).champion(1)

def testURL(URL):
    try:
        r=requests.get(URL,auth=('user', 'pass'))
        j=json.loads(r.text)
        statusFlag = True if 'status' in j else False
        if statusFlag:
            return ("bad api call. status: "+j['status']['message']+" (" + str(j['status']['status_code'])+")")
        return 'GoOd'
    except requests.exceptions.HTTPError:
        return ("invalid HTTP response")
    except requests.exceptions.Timeout:
        return ("request timed out")
    except requests.exceptions.TooManyRedirects:
        return ("request exceeds configured number of maximum redirections")
    except requests.exceptions.ConnectionError:
        return ("connection error occurred")
    except requests.exceptions.URLRequired:
        return ("valid URL required to make request")
    except requests.exceptions.ConnectTimeout:
        return ("request timed out while trying to connect to remote server")
    except requests.exceptions.ReadTimeout:
        return ("server did not send any data in the allotted amount of time")
    except requests.exceptions.RequestException:
        return ("ambiguous exception occurred while handling your request")


