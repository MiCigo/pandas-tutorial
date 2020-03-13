'''
@Description: code
@Author: MiCi
@Date: 2020-03-12 21:11:37
@LastEditTime: 2020-03-13 17:16:41
@LastEditors: MiCi
'''

import pandas as pd
import numpy as np


class Basic3(object):

    def __init__(self):
        return

    def basic_use(self):
        df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
        # 选取A列数值大于0.5的列
        print(df[df['A'] > 0.5])

        # 选取A大于0.5、C大于0.7的列
        print(df[(df['A'] > 0.5) & (df['C'] > 0.7)])

        # 按照E列升序排序
        print(df.sort_values('E'))

        # 使用ascending为降序
        print(df.sort_values('E', ascending=False))

        # 根据多列不同条件排序
        print(df.sort_values(['A', 'E'], ascending=[True, False]))

        # 使用appley对每一行取最大值
        print(df.apply(np.max, axis=1))

        # 对某列做分组
        df = pd.DataFrame({'A':
                           np.array(
                               ['foo', 'foo', 'foo', 'foo', 'bar', 'bar']),
                           'B':
                           np.array(
                               ['one', 'one', 'two', 'two', 'three', 'three']),
                           'C':
                           np.array(['small', 'medium', 'large',
                                     'large', 'small', 'small']),
                           'D':
                           np.array([1, 2, 2, 3, 3, 5])})
        print(df.groupby('A').count())

        print(df.groupby(['B', 'C']).sum())

        # 根据B分组，取D的平均值
        print(df.groupby('B')['D'].mean())

        # 根据A、B为索引，C为数值列求和
        print(df.pivot_table(df, index=['A', 'B'], columns=['C'],
                             aggfunc=np.sum))

        # 使用agg对group列做操作
        print(df.groupby('A').agg(np.mean))

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Basic3()
    example.basic_use()
