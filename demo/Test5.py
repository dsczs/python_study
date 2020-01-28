# -*- coding: utf-8 -*-
"""
用户身份验证

Version: 0.1
Author: dsczs
"""


def login():
    from selenium import webdriver
    import time
    import requests
    import json

    browser = webdriver.Chrome()
    browser.get("https://passport.jd.com/common/loginPage?from=media")
    time.sleep(2)
    name = browser.find_element_by_name("loginname")
    name.send_keys("15665549707")
    password = browser.find_element_by_name("nloginpwd")
    password.send_keys("hadoop123")
    login_button = browser.find_element_by_id("paipaiLoginSubmit")
    login_button.click()
    cookie1 = browser.get_cookies()
    print("cookie = ", cookie1)
    req = requests.Session()
    # browser.get("https://union.jd.com/proManager/index?pageNo=1")
    for c in cookie1:
        req.cookies.set(c['name'], c['value'])
    header = {'Content-Type': 'application/json',
              'referer': 'https://union.jd.com/proManager/index?pageNo=1&keywords=%E8%8D%A3%E8%80%809X%20%E9%BA%92%E9%BA%9F810%204000mAh%E7%BB%AD%E8%88%AA%204800%E4%B8%87%E8%B6%85%E6%B8%85%E5%A4%9C%E6%8B%8D%206.59%E8%8B%B1%E5%AF%B8%E5%8D%87%E9%99%8D%E5%85%A8%E9%9D%A2%E5%B1%8F%20%E5%85%A8%E7%BD%91%E9%80%9A6GB%2B64GB%20%E9%AD%85%E6%B5%B7%E8%93%9D'}

    jsondata = '{"data":{"isPinGou":0,"materialId":100006947212,"materialType":1,"planId":0,"promotionType":15,"receiveType":"cps","wareUrl":"http://item.jd.com/100006947212.html","isSmartGraphics":0,"requestId":"s_c9683f3330db474413a66872c84c3e2af2"}}'
    json = json.dumps(jsondata)

    result = req.post("https://union.jd.com/proManager/index?pageNo=1", data=json).content
    print("result = ", result)
    time.sleep(111)


def content():
    import requests
    from bs4 import BeautifulSoup
    html = requests.session().get("https://order.jd.com/center/list.action").content
    soup = BeautifulSoup(html, features="html.parser")
    print("html -> ", html)


if __name__ == '__main__':
    login()
