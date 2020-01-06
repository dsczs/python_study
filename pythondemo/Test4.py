# -*- coding: utf-8 -*-
from pythondemo.Student import Student


if __name__ == '__main__':
    student = Student('hello', 33, 95)
    # student.test_hello()
    print(student)

    # 注意这里不可访问私有的成员变量 但是可以使用这种方式访问 name是private的
    print(student._Student__name)

    # score是protected可以直接通过实例访问
    print(student._score)

    print(Student.public_var)
