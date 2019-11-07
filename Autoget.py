import http.cookiejar as HC
import browsercookie
import requests
import urllib.request
import urllib
import json
from http.cookies import SimpleCookie

#cookies
rcs = {'login': 'tianchunyang168', 'password': '123456',
       'JSESSIONID': 'E8AC75753E6C55399FD967C06CE27CCF', '__lfcc': '1'}

r = requests.post(
    'http://btsj.1598game.cn/ShopCtro/InitLand', cookies=rcs)
session = requests.session()
# load jason context :dict. show the 'data' in the dict
landata = json.loads(r.text)['data']
lclist = ''
landcodels = []
for i in landata:
    #print(i['landcode'])
    lclist = lclist + ',' + i['landcode']
    landcodels.append(i['landcode'])
#print(lclist)
#print(landcodels)

count = 0
n = input("施肥次数：")
line = 1
while count < int(n):
    rl = requests.post(
        'http://btsj.1598game.cn/LandCtro/LandFertilize?landcodeList='+lclist, cookies=rcs)
    if json.loads(rl.text)['msg'] == "施肥成功！":
        #print('OK!')
        count = count+1
    else:
        #print(rl.text)
        rb = requests.post(
            'http://btsj.1598game.cn/ShopCtro/buyProp?buySize=18&ShopId=4', cookies=rcs)
        print(rb.text)
    # harvest lands
    if count/10 >= line:
        line = line+1
        for h in landcodels:
            rv = requests.post(
                'http://btsj.1598game.cn/LandCtro/harvest?landcode='+h, cookies=rcs)
            print(rv.text)
