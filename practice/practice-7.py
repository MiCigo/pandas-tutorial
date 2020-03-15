'''
@Description: code
@Author: MiCi
@Date: 2020-03-14 21:39:35
@LastEditTime: 2020-03-15 21:30:43
@LastEditors: MiCi
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Practice7(object):

    def __init__(self):
        return

    def exercise(self):
        path = './data/train.csv'
        titanicData = pd.read_csv(path)
        print(titanicData.head(5))

        # 设置PassengerId设置为索引
        titanicData.set_index('PassengerId')
        print(titanicData.head(5))

        # 多少人生还
        print(titanicData['Survived'].sum())

        # 绘制男女比例扇形图
        males = (titanicData['Sex'] == 'male').sum()
        females = (titanicData['Sex'] == 'female').sum()
        pieData = [males, females]
        plt.subplot(2, 2, 1)
        plt.pie(pieData, labels=['Males', 'Females'],
                shadow=False, explode=(0.15, 0), startangle=90, autopct='%1.1f%%')
        plt.title("Sex Proportion")

        # 绘制男女年龄散点图
        ax = plt.subplot(2, 2, 2)
        malesAge = titanicData[titanicData['Sex'] == 'male']['Age']
        malesFare = titanicData[titanicData['Sex'] == 'male']['Fare']
        ax.scatter(malesAge, malesFare, alpha=0.5)
        femalesAge = titanicData[titanicData['Sex'] == 'female']['Age']
        femalesFare = titanicData[titanicData['Sex'] == 'female']['Fare']
        ax.scatter(femalesAge, femalesFare, c='green', alpha=0.6)

        # 绘制船票价格直方图
        plt.subplot(2, 2, 3)
        fareData = titanicData['Fare'].sort_values(ascending=False)
        binsVal = np.arange(0, 600, 10)
        plt.hist(fareData, bins=binsVal)
        plt.xlabel('Fare')
        plt.ylabel('Frequency')

        # 绘制生还者价格直方图
        plt.subplot(2, 2, 4)
        fareData = titanicData[titanicData['Survived']
                               == 1]['Fare'].sort_values(ascending=False)
        binsVal = np.arange(0, 600, 10)
        plt.hist(fareData, bins=binsVal)
        plt.xlabel('Survive Fare')
        plt.ylabel('Frequency')
        plt.show()

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Practice7()
    example.exercise()
