# -*- coding: utf-8 -*-
"""
用户身份验证

Version: 0.1
Author: dsczs
"""


def login():
    from selenium import webdriver
    import time
    import random
    from browsermobproxy import Server
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.action_chains import ActionChains

    # proxy
    server = Server(r'D:\FTP\browsermob-proxy-2.1.4-bin\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
    server.start()
    proxy = server.create_proxy()

    chrome_options = Options()
    # 不加载图片,加快访问速度
    # chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # 设置为开发者模式，避免被识别
    chrome_options.add_experimental_option('excludeSwitches',
                                    ['enable-automation'])
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    proxy.new_har("alimama", options={'captureHeaders': True, 'captureContent': True})

    # 登录
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get("https://login.taobao.com/member/login.jhtml?style=minisimple&from=alimama&redirectURL=http://login.taobao.com/member/taobaoke/login.htm?is_login=1&full_redirect=true&disableQuickLogin=true")
    time.sleep(2)

    name = browser.find_element_by_name("TPL_username")
    name.send_keys("小刚和婉庆")
    password = browser.find_element_by_name("TPL_password")
    time.sleep(1)
    password.send_keys("")
    login_button = browser.find_element_by_id("J_SubmitStatic")
    login_button.click()

    time.sleep(6)
    # browser.refresh()

    huakuai = browser.find_element_by_id("nc_1__bg")
    action = ActionChains(browser)

    action.click_and_hold(huakuai).perform()
    action.move_by_offset(10, 0).perform()  # 平行移动鼠标

    time.sleep(22)
    print("滑块完成")
    # 这里必须休眠 需要跳转
    time.sleep(50)

    # 打印cookie
    cookie1 = browser.get_cookies()
    print("cookie = ", cookie1)

    time.sleep(111)
    # 商品搜索
    browser.get("https://pub.alimama.com/myunion.htm")
    # search = browser.find_elements_by_css_selector(".search .el-input__inner")
    # search[0].send_keys("南极人10双袜子男四季男士长袜中筒透气吸汗运动商务休闲棉袜保暖长筒棉袜 男士中筒袜10双")
    # search_button = browser.find_elements_by_css_selector(".search .el-icon-search")
    # search_button[0].click()
    time.sleep(2)

    # 打开推广地址弹窗
    # js = '$("#first_sku_btn").click()'
    # browser.execute_script(js)

    result = proxy.har
    # print(result)

    for entry in result['log']['entries']:
        print(entry)
        # if "mercury.jd.com/log.gif" in entry['request']['url']:
        #     print("###############")
        #     # 从头中取cookie
        #     header = entry['request']['headers']
        #     for h in header:
        #         if h['name'] == 'Cookie':
        #             print(h['value'])
        #             my_cookie = h['value']
        #             print("my_cookie ->{}".format(my_cookie))

    # 截屏
    # browser.get_screenshot_as_file("E:\\jd.png")

    time.sleep(11111)


if __name__ == '__main__':
    login()
