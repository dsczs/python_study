# -*- coding: utf-8 -*-
"""
用户身份验证

Version: 0.1
Author: dsczs
"""
if __name__ == '__main__':
    import time
    from selenium import webdriver

    login_url = 'https://passport.jd.com/common/loginPage?from=media'
    driver = webdriver.PhantomJS()
    driver.get(login_url)
    time.sleep(5)

    account = driver.find_element_by_id('loginname')
    password = driver.find_element_by_id('nloginpwd')
    submit = driver.find_element_by_id('paipaiLoginSubmit')

    account.clear()
    password.clear()
    account.send_keys('15665549707')
    password.send_keys('hadoop123')

    submit.click()
    time.sleep(5)

    # cookie和前面一样的方式获取和保存
    cookies = driver.get_cookies()
    print(cookies)
    web = driver.get("https://union.jd.com/overview")
    print(web)
    driver.close()
