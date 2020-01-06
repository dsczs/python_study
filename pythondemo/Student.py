# -*- coding: utf-8 -*-


class Student:

    name = ''
    age = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def test_hello(self):
        print("this.name = ", self.name, "this.age = ", self.age)
