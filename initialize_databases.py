import form_urls
import requests
import requests_cache
import json
import time

requests_cache.install_cache(cache_name='lol_test_cache', backend='sqlite', expire_after=180)

def testCache():
    for i in range (0,10):
        now = time.ctime(int(time.time()))
        r=requests.get(form_urls.getRequestURL(form_urls.getAllChampsSuffix()),auth=('user', 'pass'))
        #j=json.loads(r.text)
        print ("Time: {0} / Used Cache: {1}".format(now, r.from_cache))

    
    
def initChampDatabase():
    d = {}
    r=requests.get(form_urls.getRequestURL(form_urls.getAllChampsSuffix()),auth=('user', 'pass'))
    allChampsJ=json.loads(r.text)
    for i in range(0, len(allChampsJ["champions"])):
        d[allChampsJ["champions"][i]["id"]]=[]
    return (d)
