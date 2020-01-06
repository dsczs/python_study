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



if __name__ == '__main__':
    test_ndarray()
