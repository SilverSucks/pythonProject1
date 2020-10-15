import matplotlib.pyplot as plt
import numpy as np
'''
利用knn,判断一个电影是动作片还是爱情片
'''
# fight = (3, 2, 1, 101, 99, 98, 18)
# kiss = (104, 100, 81, 10, 5, 2, 90)
# filmtype = (1, 1, 1, 2, 2, 2,3)
# plt.scatter(fight, kiss, c=filmtype)
# plt.show()

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

# 2.计算未知样本和每个训练样本的距离    测试数据
xx = np.array([18, 90])  # 测试样本转换为ndarray数据
dist = (((x-xx)**2).sum(1))**0.5    # 欧拉公式--欧式距离
print(dist)

# 3.将距离升序排序
sortedDist = dist.argsort()    # 结果为从低到高排序的索引

print('距离值从低到高排序，输出索引值', sortedDist)

# 4.选取距离最小的k个点，统计前k个点所在类别出现的次数
k = 4
classCount = {}  # 用字典统计每种类型出现的次数， 键---电影标签，值---统计出现的次数
for i in range(k):  # 产生一个0到k的序列
    voteLabel = y[sortedDist[i]]   # 键  根据sortedDist已经排序好的结果  去 y(电影类型)中映射
    '''
    更新字典的内容 
    如果元组中没有这个标签，加进去。如果有这个标签，在原来的基础上+1
    get()  取键值的函数
    字典[键的名称] = 字典.取出相应的键对应的值 + 1 
    '''
    classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
print('class:count', classCount)

# 5.多数表决，输出结果
'''
把最大的key输出出来
'''
maxType = 0
maxCount = 1
for key, value in classCount.items():
    if value > maxCount:
        maxType = key
        maxCount = value
print('output(预测的电影类型为):', maxType)