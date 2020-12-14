from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("http://btsj.1598game.cn/user/Manor.jsp")
print(browser.page_source)
time.sleep(5)
