# -*- coding: utf-8 -*-
"""
用户身份验证

Version: 0.1
Author: dsczs
"""


def login():
    from selenium import webdriver
    import time

    browser = webdriver.Chrome()
    browser.get("https://passport.jd.com/common/loginPage?from=media")
    time.sleep(2)
    name = browser.find_element_by_name("loginname")
    name.send_keys("15665549707")
    password = browser.find_element_by_name("nloginpwd")
    password.send_keys("hadoop123")
    login_button = browser.find_element_by_id("paipaiLoginSubmit")
    login_button.click()
    time.sleep(10)
    cookie = browser.get_cookies()
    print("cookie = ", cookie)
    browser.get("https://order.jd.com/center/list.action")
    time.sleep(1111)


def content():
    import requests
    from bs4 import BeautifulSoup
    html = requests.session().get("https://order.jd.com/center/list.action").content
    soup = BeautifulSoup(html, features="html.parser")
    print("html -> ", html)


if __name__ == '__main__':
    login()
