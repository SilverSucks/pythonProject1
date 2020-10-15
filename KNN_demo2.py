import matplotlib.pyplot as plt
import numpy as np
import KNN_function as knn     # 导入自己写的模块
'''
利用knn,判断一个电影是动作片还是爱情片
'''


# 1.构建数据集
fight = [3, 2, 1, 101, 99, 98]
kiss = [104, 100, 81, 10, 5, 2]
filmtype = [1, 1, 1, 2, 2, 2]  # 数字1代表 爱情片，数字2代表 武打片
plt.scatter(fight, kiss, c=filmtype)
plt.xlabel("fight")
plt.ylabel("kiss")
plt.title("movie")
# plt.show()
x = np.array([fight, kiss])  # 测试样本转变为ndarray数据
x = x.T

y = np.array(filmtype)
print(x)
print(y)
xx = np.array([18, 90])
# 参数1：测试集(xx)，参数2：训练集的输入(x)，参数3：训练集的标签(y), 参数4为k的值
result = knn.knn(xx, x, y, 4)
print(result)

