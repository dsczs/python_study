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


if __name__ == '__main__':
    test_nd_array_4_oper()
