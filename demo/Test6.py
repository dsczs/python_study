# -*- coding: utf-8 -*-
"""
用户身份验证

Version: 0.1
Author: dsczs
"""


def t1():
    import re
    str = '''74BD5D5E43AA4B8248C5001BA8A2CABF1647A5DB6CE15C13F131A51C838B7C2E62479003E5A070C7A4790E19559E3025C0E87293A7A7B4CAB9142BE218264213025F3B71CDC99CA427507D6C6700D8D7F56690FB5343ACF18FCEBD0EFC40835519F38D3C0A20096AF197EFD1C4970CCE3D3C5ABDD40E7B1284590FC33C505B722D8CFF9D91A394AC2'}, {'domain': '.jd.com', 'expiry': 1582858178.213369, 'httpOnly': False, 'name': 'pin', 'path': '/', 'secure': False, 'value': 'tel15665549707'}, {'domain': '.jd.com', 'expiry': 1924905600, 'httpOnly': False, 'name': '3AB9D23F7A4B3C9B', 'path': '/', 'secure': False, 'value': '75P5I6LO3CIGYQYC7L2FP254LVX247V47SUEJJMCF2STDPDROFSMYRJW3KF5LTHXPUEEFIZOHVRIRUYZSNESVU6L5E'}, {'domain': '.jd.com', 'expiry': 1582858178.213393, 'httpOnly': True, 'name': 'unick', 'path': '/', 'secure': False, 'value': 'tel15665549707'}, {'domain': '.jd.com', 'expiry': 1582858178.21345, 'httpOnly': False, 'name': '_tp', 'path': '/', 'secure': False, 'value': '2MGjEXUerxEsnRjnEY8hUA%3D%3D'}, {'domain': '.jd.com', 'expiry': 1582858178.213489, 'httpOnly': True, 'name': '_pst', 'path': '/', 'secure': False, 'value': 'tel15665549707'}, {'domain': 'www.jd.com', 'expiry': 1611802180, 'httpOnly': False, 'name': 'o2State', 'path': '/', 'secure': False, 'value': '{%22webp%22:true%2C%22lastvisit%22:1580266180542}'}, {'domain': '.jd.com', 'expiry': 1595818179, 'httpOnly': False, 'name': '__jda', 'path': '/', 'secure': False, 'value': '76161171.1580266175806708769992.1580266176.1580266176.1580266176.1'}, {'domain': '.jd.com', 'expiry': 1581130180, 'httpOnly': False, 'name': 'ipLoc-djd', 'path': '/', 'secure': False, 'value': '14-1140-18376-0'}, {'domain': '.jd.com', 'expiry': 1580267979, 'httpOnly': False, 'name': '__jdb', 'path': '/', 'secure': False, 'value': '76161171.3.1580266175806708769992|1.1580266176'}, {'domain': '.jd.com', 'httpOnly': False, 'name': '__jdc', 'path': '/', 'secure': False, 'value': '76161171'}, {'domain': '.jd.com', 'expiry': 1581130180, 'httpOnly': False, 'name': 'areaId', 'path': '/', 'secure': False, 'value': '14'}]
            '''
    a = re.findall(r'__jdv', str)

    print(a)

if __name__ == '__main__':
    t1()