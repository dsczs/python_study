# -*- coding: utf-8 -*-
from pythondemo.AppLog import AppLog


def test_class():
    pass


def test_func():
    pass


def test_thread():
    pass


def test_hello():
    print("hello")


def test_if():
    if True:
        print("true")
    else:
        print("false")

    a = 2
    if a == 3:
        print("a = 3")
    elif a == 2:
        print("a = 2")
    else:
        print("a = ", a)


def test_for():
    a = [1, 3, 4, 3]
    for b in a:
        if b % 2 == 1:
            print("b = ", b)
        else:
            continue


def test_time():
    import time
    a = time.time()
    print("a = ", a)

    print("格式化时间为 ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# 处理异常
def test_exception():
    try:
        a = 1 / 0
    except Exception as e:
        AppLog('pythondemo test1 test_exception').error(e)


if __name__ == '__main__':
    test_exception()

