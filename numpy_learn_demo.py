import numpy as np
'''
numpy中的一维数组
'''
#
# list1 = [1,2,3,4]
# x = np.array(list1)
# print(list1)
# print(type(list1))
# print(x)
# print(type(x))
'''
numpy中的二维数组
'''
# np_ar = np.array([[1,2,3],[4,5,6]])
# print(type(np_ar))
# print(np_ar)
#
# c = np_ar[np_ar>2]
# print(c)

'''
产生连续的序列---方式1
'''
# x1 = np.arange(5)
# x2 = np.arange(3, 7)
# x3 = np.arange(1,10,2)
# print("x1=", x1)
# print("x2=", x2)
# print("x3=", x3)

'''
产生连续的数组---方式2
该方式表示产生多少个数字，从起始位到结束位
'''
# x1 = np.linspace(1, 10, 3)
# print("x1 =", x1)

'''
切片、重构、转置
'''
a = [[1, 2, 3], [4, 5, 6]]
print(type(a))
print(a)
np_ar = np.array(a)
print(type(np_ar))
print(np_ar)
print("取出第0,1行，第1,2列。切片后的结果\n", np_ar[0:2, 1:3])   # 切片，原矩阵的第1,2行，第2,3列 ,python语言的特点：包头不包尾。
np_ar2 = np_ar.reshape(3, 2)   # 重构 改变矩阵的形状
np_ar3 = np_ar[0:1, :]
print("取出第0行，所有列(即第一行)。切片后的结果：\n", np_ar3)
np_ar4 = np_ar[:, 2:]
print("取出第3列（即第三列）\n", np_ar4)
print("重构后的结果：\n", np_ar2)
print("转置后的结果：\n", np_ar.T)   # 数组转置
