# 获取浏览器cookie
import http.cookiejar as HC
import browsercookie
import requests
import urllib.request
import urllib
from http.cookies import SimpleCookie

rcs = [{
    "Host raw": "http://btsj.1598game.cn/",
    "Name raw": "JSESSIONID",
    "Path raw": "/",
    "Content raw": "022571B4617276AC7CAB0C763D0C14AD",
    "Expires": "At the end of the session",
    "Expires raw": "0",
    "Send for": "Any type of connection",
    "Send for raw": "false",
    "HTTP only raw": "false",
    "SameSite raw": "no_restriction",
    "This domain only": "Valid for host only",
    "This domain only raw": "true",
    "Store raw": "firefox-default",
    "First Party Domain": ""
}]
r = requests.get(
    'http://btsj.1598game.cn/user/Manor.jsp?Monitor=1', cookies=rcs)
session = requests.session()

# headers = {"User-Agent": "Mozilla/5.0"}

# # 获取页面信息
# response = requests.get("http://btsj.1598game.cn/user/Manor.jsp",
#                         cookies=firefox_cookie, headers=headers, verify=False)
