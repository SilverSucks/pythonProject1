import numpy as np
import pandas as pd

arr1 = np.arange(3, 9)
s1 = pd.Series(arr1)
print(s1)
print(type(s1))
# Series的取值
print("s1中下标为1 的值：\n", s1[1])
print("取下标从0到3（包头不包尾）的值进行切片\n", s1[0:3])

dic1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
s2 = pd.Series(dic1)
print("s2:\n")
print(s2)


'''
DataFrame的使用
'''
# 通过列表创建
arr2 = np.arange(12).reshape(4, 3)   # 创建一个4x3的矩阵
df1 = pd.DataFrame(arr2)
print("df1:\n", df1)
print(type(df1))
# 通过字典创建
dic2 = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12], 'd': [13, 14, 15, 16]}
df2 = pd.DataFrame(dic2)
print("df2:\n", df2)
# 手动改变df1的列名
df1.columns = ['colm1', 'colm2', 'colm3']
print("改变列名后的df1:\n", df1)

'''
标签切片     冒号操作 取的是范围， 列表操作取得是  列表中固定的值
'''
# loc  通过行和列的索引访问数据
print("取出df2中的第一行：")
print(df2.loc[0])


# 通过标签来在多个轴上进行选择
print("冒号切片和列表切片的区别：")
print(df2.loc[[1, 2, 3], ['a', 'c']])
print(df2.loc[1:2, ['a', 'c']])

'''
位置选择，iloc通过行和列的下标来访问数据
'''
print("行号为3的行：")
print(df2.iloc[3])
print("通过数值进行切片")
print(df2.iloc[1:3, 0:2])
