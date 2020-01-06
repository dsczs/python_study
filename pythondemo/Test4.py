# -*- coding: utf-8 -*-
from pythondemo.Student import Student


if __name__ == '__main__':
    student = Student('hello', 33)
    # student.test_hello()
    print(student)
    print(Student.public_var)
