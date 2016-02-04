########################################################################
#                                                                      #
#   Testing functionality of form_urls methods: checks to determine    #
#   whether URLs made in form_urls.py make correct calls to LOL API    #
#   Calls that are incorrect in format should return JSON content      #
#   comprised of a status key and status message and code (bad API     #
#   calls). Calls that are not proper URLS (URLS that lead to una-     #
#   vailable webpages will be request errors. These are not currently  #
#   supported.                                                         #
#                                                                      #
########################################################################

import form_urls
import requests
import requests_cache
import json

freestylinrough = 28328081
platformId=form_urls.platform_ids[form_urls.DEFAULT_REGION]
regionId = form_urls.region_ids[form_urls.DEFAULT_REGION]

def testURL(URL):
    r=requests.get(URL,auth=('user', 'pass'))
    j=json.loads(r.text)
    statusFlag = True if 'status' in j else False
    if statusFlag:
        return ("bad api call. status: "+j['status']['message']+" (" + str(j['status']['status_code'])+")")
    return 'GoOd'
