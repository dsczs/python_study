# -*- coding: utf-8 -*-


a = 22


def add():
    global a
    a = a + 1


if __name__ == '__main__':
    print(a)
    add()
    print(a)
