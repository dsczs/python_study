# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


def test_1():
    s = pd.Series([1, 3, 5])
    d = pd.date_range('20140101', periods=6)
    print(s)
    print(d)
    df = pd.DataFrame(np.random.randn(6, 4),index=d)
    print(df)
    df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
    print(df1)


if __name__ == '__main__':
    test_1()
