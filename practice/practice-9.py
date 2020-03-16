'''
@Description: code
@Author: MiCi
@Date: 2020-03-16 20:45:50
@LastEditTime: 2020-03-16 21:26:56
@LastEditors: MiCi
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Practice9(object):

    def __init__(self):
        return

    def exercise(self):
        path = './data/iris.csv'
        irisData = pd.read_csv(path, names=[
                               'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
        print(irisData.head(10))

        # 缺失数据
        print(pd.isnull(irisData).sum())

        # 将petal_length第10~19行设置为缺失值
        irisData.iloc[10:20, 2:3] = np.nan
        print(irisData.head(20))

        # 将缺失值替换为1.0
        irisData['petal_length'].fillna(1, inplace=True)
        print(irisData.head(20))

        # 删除class列
        del irisData['class']
        print(irisData.head(10))

        # 将前三行设置为缺失值
        irisData.iloc[0:3, :] = np.nan
        print(irisData.head(10))

        # 删除有缺失值的行
        irisData = irisData.dropna(how='any')
        print(irisData.head(20))

        # 重新设置索引
        irisData = irisData.reset_index(drop=True)
        print(irisData.head(20))

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Practice9()
    example.exercise()
