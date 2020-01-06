# -*- coding: utf-8 -*-
from numpy import *


# 打印 eye
def print_eye():
    arr = eye(4)
    print(arr)


# ndarray
def test_ndarray():
    import numpy as np

    # 一维数组
    arr = np.array([1, 3, 4])
    print("arr = ", arr)

    # 二维数组
    arr2 = np.array([[2, 3], [3, 5]])
    print("arr2 = ", arr2)

    # dtype类型
    arr3 = np.array([2, 4], dtype=float32)
    print("arr3 = ", arr3)

    # 元祖转np array
    arr4 = np.array((2, 3))
    print("arr4 = ", arr4)

# ndarray new
def test_ndarray2():
    import numpy as np

    arr = np.array([[1, 3, 5], [3, 5, 6]])
    print("arr = ", arr)
    print("arr.shape = ", arr.shape)

    arr2 = arr.reshape((3, 2))
    print("arr2 = ", arr2)


# test ndarray range
def test_nd_array_range():
    import numpy as np

    arr = np.arange(1, 10, 2, int32)
    print("arr = ", arr)


# nd array 四则运算
def test_nd_array_4_oper():
    import numpy as np
    # add
    a = np.array([1, 2, 4])
    b = np.array([2, 4, 8])
    c = a + b
    print("c = ", c)

    # del
    d = a - b
    print("d = ", d)

    # mulit 每一行乘以每一列的和累加 例如第一行乘以第一列的和累加 第二行乘以第二列的和累加
    e = a * b
    print("e = ", e)

    # divide
    f = a / b
    print("f = ", f)


# nd array 遍历
def test_nd_array_iterator():
    import numpy as np

    arr = np.arange(6).reshape((3, 2))
    print("原始arr = ", arr)

    print('迭代输出元素：')
    for x in np.nditer(arr):
        print(x, end=',')


# 字符串操作
def test_char():
    import numpy as np
    a = np.char.add(['hello'], [' numpy'])
    print("a = ", a)

    # 两个的时候是第一个的第一个与第二个的第一个拼接
    b = np.char.add(['hello', 'hello'], [' numpy', ' python'])
    print("b = ", b)

    # 重复值
    c = np.char.multiply(' numpy ', 3)
    print("c = ", c)

    # 首字母大写
    d = np.char.capitalize('numpy')
    print("d = ", d)

    # 字符串切割
    e = np.char.split('i study python', ' ')
    print("e = ", e)


if __name__ == '__main__':
    test_char()
