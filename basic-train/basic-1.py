'''
@Description: code
@Author: MiCi
@Date: 2020-03-12 08:55:59
@LastEditTime: 2020-03-12 23:20:24
@LastEditors: MiCi
'''

import pandas as pd
import numpy as np


class Basic1(object):

    def __init__(self):
        return

    def basic_use(self):

        # 数据导入
        filename, query, connection_object, json_string, url, table_name = ''
        # 导入csv格式文件中的数据
        pd.read_csv(filename)
        # 导入有分隔符的文本 (如TSV) 中的数据
        pd.read_table(filename)
        # 导入Excel格式文件中的数据
        pd.read_excel(filename)
        # 导入SQL数据表/数据库中的数据
        pd.read_sql(query, connection_object)
        # 导入JSON格式的字符，URL地址或者文件中的数据
        pd.read_json(json_string)
        # 导入经过解析的URL地址中包含的数据框 (DataFrame) 数据
        pd.read_html(url)
        # 导入系统粘贴板里面的数据
        pd.read_clipboard()
        # 导入Python字典 (dict) 里面的数据，其中key是数据框的表头，value是数据框的内容。
        pd.DataFrame(dict)

        # 数据导出
        df = pd.DataFrame()
        # 将数据框 (DataFrame)中的数据导入csv格式的文件中
        df.to_csv(filename)
        # 将数据框 (DataFrame)中的数据导入Excel格式的文件中
        df.to_excel(filename)
        # 将数据框 (DataFrame)中的数据导入SQL数据表/数据库中
        df.to_sql(table_name, connection_object)
        # 将数据框 (DataFrame)中的数据导入JSON格式的文件中
        df.to_json(filename)

        return

    def basic_use2(self):
        # 2个重要的数据结构
        # DataFrame 数据框对象，类似二维表
        # Series 数组对象，带有标签label(或称索引index)

        # DataFrame
        df = pd.DataFrame(np.random.rand(10, 5))
        print(df)

        # 添加日期索引
        df.index = pd.date_range('2020/1/1', periods=df.shape[0])
        print(df)

        # 查看df前几行&后几行
        print('Head:', df.head(5))
        print('Tail:', df.tail(5))

        # 查看df的行数与列数
        print('Shape:', df.shape)

        # 查看df基本信息：索引、数据类型、内存
        print('Info:', df.info())

        # 查看df描述信息
        print('Describe:', df.describe())

        # df数据选取
        df = pd.DataFrame(np.random.rand(5, 5), columns=list('ABCDE'))

        # 以Series的形式返回选取列
        print(df['A'])

        # 以DataFrame的形式返回选取的列
        print(df[['A', 'C', 'E']])

        # 选取x行y列iloc[x, y]
        print(df.iloc[0, 0])

        # Series
        testList = ['a', 'b', 3, 3, 3]
        testSeries = pd.Series(testList)
        print(testSeries)

        # 查询每个数值出现的次数
        print(testSeries.value_counts(dropna=False))

        # 使用iloc按位置选取
        print(testSeries.iloc[0])

        # 按照索引选取
        print(testSeries.loc[1])

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Basic1()
    example.basic_use2()
