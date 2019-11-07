import http.cookiejar as HC
import browsercookie
import requests
import urllib.request
import urllib
import json
from http.cookies import SimpleCookie

# cookies
rcs = {'login': '', 'password': '',
       'JSESSIONID': '', '__lfcc': '1'}

r = requests.post(
    'http://btsj.1598game.cn/ShopCtro/InitLand', cookies=rcs)
session = requests.session()
# load jason context :dict. show the 'data' in the dict
landata = json.loads(r.text)['data']
lclist = ''
landcodels = []
for i in landata:
    # print(i['landcode'])
    lclist = lclist + ',' + i['landcode']
    landcodels.append(i['landcode'])
# print(lclist)
# print(landcodels)

count = 0
n = input("施肥次数：")
line = 1
while count < int(n):
    rl = requests.post(
        'http://btsj.1598game.cn/LandCtro/LandFertilize?landcodeList='+lclist, cookies=rcs)
    if json.loads(rl.text)['msg'] == "施肥成功！":
        # print('OK!')
        count = count+1
    else:
        # print(rl.text)
        rb = requests.post(
            # red:6 yellow: 5 black:4
            'http://btsj.1598game.cn/ShopCtro/buyProp?buySize=18&ShopId=4', cookies=rcs)
        print(rb.text)
    # harvest lands
    if count/10 >= line:
        line = line+1
        for h in landcodels:
            rv = requests.post(
                'http://btsj.1598game.cn/LandCtro/harvest?landcode='+h, cookies=rcs)
            print(rv.text)


"""
# headers = {"User-Agent": "Mozilla/5.0"}

# # 获取页面信息
# response = requests.get("http://btsj.1598game.cn/user/Manor.jsp",
#                         cookies=firefox_cookie, headers=headers, verify=False)




body = {'login': 'tian168', 'password': '123150'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
response, content = http.request(
    url, 'POST', headers=headers, body=urllib.urlencode(body))

headers = {'Cookie': response['set-cookie']}

url = 'http://www.example.com/home'
response, content = http.request(url, 'GET', headers=headers)
"""
