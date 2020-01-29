# -*- coding: utf-8 -*-
"""
用户身份验证

Version: 0.1
Author: dsczs
"""


def login():
    from selenium import webdriver
    import time

    # 登录
    browser = webdriver.Chrome()
    browser.get("https://passport.jd.com/common/loginPage?from=media")
    time.sleep(2)
    name = browser.find_element_by_name("loginname")
    name.send_keys("15665549707")
    password = browser.find_element_by_name("nloginpwd")
    password.send_keys("hadoop123")
    login_button = browser.find_element_by_id("paipaiLoginSubmit")
    login_button.click()

    # 这里必须休眠 需要跳转
    time.sleep(5)

    # 打印cookie
    cookie1 = browser.get_cookies()
    print("cookie = ", cookie1)

    # 商品搜索
    browser.get("https://union.jd.com/proManager/index?pageNo=1")
    search = browser.find_elements_by_css_selector(".search .el-input__inner")
    search[0].send_keys("南极人10双袜子男四季男士长袜中筒透气吸汗运动商务休闲棉袜保暖长筒棉袜 男士中筒袜10双")
    search_button = browser.find_elements_by_css_selector(".search .el-icon-search")
    search_button[0].click()
    time.sleep(2)

    # 打开推广地址弹窗
    js = '$("#first_sku_btn").click()'
    browser.execute_script(js)

    time.sleep(11111)


if __name__ == '__main__':
    login()
