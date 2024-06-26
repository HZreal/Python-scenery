import json
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 计算欧拉距离
def calcDis2(dataSet, centroids, k):
    clalist = []
    for data in dataSet:
        diff = np.tile(data, (k, 1)) - centroids  # 相减   (np.tile(a, (2,1))就是把a先沿x轴复制1倍，即没有复制，仍然是 [0,1,2]。 再把结果沿y方向复制2倍得到array([[0,1,2],[0,1,2]]))
        squaredDiff = diff ** 2  # 平方
        squaredDist = np.sum(squaredDiff, axis=1)  # 和  (axis=1表示行)
        distance = squaredDist ** 0.5  # 开根号
        clalist.append(distance)
    clalist = np.array(clalist)  # 返回一个每个点到质点的距离len(dateSet)*k的数组
    return clalist

def calcDis(dataSet, centroids, k):
    cal_list = [np.sum((np.tile(data, (k, 1)) - centroids) ** 2, axis=1) ** 0.5 for data in dataSet]
    cal_list = np.array(cal_list)  # 返回一个每个点到质点的距离len(dateSet)*k的数组
    return cal_list


# 计算质心
def classify(dataSet, centroids, k):
    # 计算样本到质心的距离
    cal_list = calcDis(dataSet, centroids, k)
    # print(cal_list)
    # 分组并计算新的质心
    minDistIndices = np.argmin(cal_list, axis=1)  # axis=1 表示求出每行的最小值的下标
    newCentroids = pd.DataFrame(dataSet).groupby(
        minDistIndices).mean()  # DataFramte(dataSet)对DataSet分组，groupby(min)按照min进行统计分类，mean()对分类结果求均值
    newCentroids = newCentroids.values

    # 计算变化量
    changed = newCentroids - centroids

    return changed, newCentroids


# 使用k-means分类
def kmeans(dataSet, k):
    # 随机取质心
    centroids = random.sample(dataSet, k)
    # print(centroids)

    # 更新质心 直到变化量全为0
    changed, newCentroids = classify(dataSet, centroids, k)
    while np.any(changed != 0):
        changed, newCentroids = classify(dataSet, newCentroids, k)

    centroids = sorted(newCentroids.tolist())  # tolist()将矩阵转换成列表 sorted()排序

    # 根据质心计算每个集群
    cluster = []
    cal_list = calcDis(dataSet, centroids, k)  # 调用欧拉距离
    minDistIndices = np.argmin(cal_list, axis=1)
    for i in range(k):
        cluster.append([])
    for i, j in enumerate(minDistIndices):  # enymerate()可同时遍历索引和遍历元素
        cluster[j].append(dataSet[i])

    return centroids, cluster




if __name__ == '__main__':
    # dataset = [[1, 1], [1, 2], [2, 1], [6, 4], [6, 3], [5, 4]]
    with open(r'C:\Users\sizhong\file\project\SEV\源数据\车辆位置20230108-9点-添加电池信息.json', 'r', encoding='utf8') as f:
        source_data = json.loads(f.read())

    # filter
    filter_data = list(filter(lambda x: x['battery_capacity'] < 0.4, source_data))

    # parse data
    parse_data = [[float(i['lng']), float(i['lat'])] for i in filter_data]
    print('parse_data ---->  ', parse_data, len(parse_data) == len(filter_data), sep='\n')

    k = 3
    centroids, cluster = kmeans(parse_data, k)

    print('质心为 ---->  ', centroids)
    print('集群为 ---->  ')
    for i, v in enumerate(cluster):
        print(f'{i} ---->  ', v, '\n')


    # for i in range(len(dataset)):
    #     plt.scatter(dataset[i][0], dataset[i][1], marker='o', color='green', s=40, label='原始点')
    #     #  记号形状       颜色      点的大小      设置标签
    #     for j in range(len(centroids)):
    #         plt.scatter(centroids[j][0], centroids[j][1], marker='x', color='red', s=50, label='质心')
    #         plt.show()
