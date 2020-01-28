# -*- coding: utf-8 -*-
"""
鸢尾花

Version: 0.1
Author: dsczs
"""


def t1():
    from sklearn.datasets import load_iris
    iris_dataset = load_iris()
    print("keys of iris_dataset:\n{}".format(iris_dataset.keys()))
    for _ in iris_dataset.keys():
        print("this is {} : \n".format(_))
        print(iris_dataset.get(_))

    data = iris_dataset.get("data")
    print(data)


def t2():
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris
    import numpy as np
    iris_dataset = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris_dataset.get("data"),
                                                        iris_dataset.get("target"),
                                                        random_state=0)
    print("x_train = ", x_train)
    print("x_test = ", x_test)
    print("y_train = ", y_train)
    print("y_test = ", y_test)


def t3():
    from sklearn.datasets import load_breast_cancer
    iris_dataset = load_breast_cancer()
    print("keys of iris_dataset:\n{}".format(iris_dataset.keys()))
    for _ in iris_dataset.keys():
        print("this is {} : \n".format(_))
        print(iris_dataset.get(_))


def t4():
    from sklearn.linear_model import LinearRegression


if __name__ == '__main__':
    t3()
