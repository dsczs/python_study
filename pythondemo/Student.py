# -*- coding: utf-8 -*-


class Student:
    # 全局变量
    public_var = 22
    # 局部变量 不可直接引用
    __name = ''
    __age = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def test_hello(self):
        print("this.name = ", self.__name, "this.age = ", self.__age)

    def __str__(self) -> str:
        return "this.name = " + self.__name + " this.age = " + str(self.__age)

