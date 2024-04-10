"""
 @author: sizhong
 @date: 2023-09-21
 @File: LNS.py
 @Description:
"""
import random
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']


class Solution:
    # 使用符号编号表示一个访问路径route
    def __init__(self):
        self.route = []
        self.cost = 0  # 解对应的总成本


class Lns_tsp(object):
    def __init__(self, distance, num_node):
        self.distance = distance
        self.num_node = num_node

    def get_route_cost(self, route):
        # 计算成本的函数
        cost = 0
        for i in range(1, len(route)):
            cost += self.distance[route[i - 1]][route[i]]
        return cost

    def destroy_operator(self, solution, num_destroy):
        # 破坏算子: 随机选择num_destroy个不重复的破坏点（即删除num_destroy个城市）
        destroy_node_bank = []  # 保存被删除的城市节点
        while len(destroy_node_bank) < num_destroy:
            n = random.randint(0, self.num_node - 1)
            while n in destroy_node_bank:
                n = random.randint(0, self.num_node - 1)
            destroy_node_bank.append(n)
            solution.route.remove(n)
        return solution, destroy_node_bank

    def repair_operator(self, solution, destroy_node_bank):
        # 修复算子: 贪婪插入，插入到成本最小的位置
        for n in destroy_node_bank:
            # 计算将n插入各个位置的成本
            insert_list = np.full(len(solution.route), 0)
            for i in range(0, len(solution.route)):
                insert_list[i] = self.distance[solution.route[i - 1]][n] + self.distance[n][solution.route[i]] - \
                                 self.distance[solution.route[i]][solution.route[i - 1]]

            greedy_index = np.where(insert_list == min(insert_list))[0][0]

            solution.route.insert(greedy_index, n)
        return solution


def plot_best_vales_iteration(best_values_record):
    # 绘制最优解随着迭代变化的趋势
    plt.figure()
    plt.plot([i + 1 for i in range(len(best_values_record))], best_values_record)
    plt.xlabel('迭代次数')
    plt.ylabel('最优值')
    plt.show()


def plot_route(route, city_location):
    plt.figure()
    # 绘制散点
    x = np.array(city_location)[:, 0]  # 横坐标
    y = np.array(city_location)[:, 1]  # 纵坐标
    plt.scatter(x, y, color='r')
    # 绘制城市编号
    for i, txt in enumerate(range(1, len(city_location) + 1)):
        plt.annotate(txt, (x[i], y[i]))
    # 绘制方向
    x0 = x[route]
    y0 = y[route]
    for i in range(len(city_location) - 1):
        plt.quiver(x0[i], y0[i], x0[i + 1] - x0[i], y0[i + 1] - y0[i], color='b', width=0.005, angles='xy', scale=1,
                   scale_units='xy')
    plt.quiver(x0[-1], y0[-1], x0[0] - x0[-1], y0[0] - y0[-1], color='b', width=0.005, angles='xy', scale=1,
               scale_units='xy')

    plt.xlabel('横坐标')
    plt.ylabel('纵坐标')
    plt.show()


if __name__ == '__main__':
    ############## 算例和参数设置 ############################
    # 城市节点的位置信息，一行代表一个城市的横坐标及纵坐标
    city_location = [[94, 99],
                     [66, 67],
                     [14, 78],
                     [95, 56],
                     [68, 9],
                     [26, 20],
                     [51, 67],
                     [39, 39],
                     [5, 55],
                     [12, 33],
                     [55, 85],
                     [98, 46],
                     [36, 39],
                     [65, 100],
                     [57, 89],
                     [88, 24],
                     [53, 96],
                     [91, 41],
                     [32, 69],
                     [38, 38],
                     [38, 39],
                     [85, 100],
                     [7, 37],
                     [85, 96],
                     [89, 48],
                     [85, 35],
                     [32, 29],
                     [31, 25],
                     [20, 17],
                     [75, 21],
                     [74, 29],
                     [6, 32],
                     [20, 81],
                     [62, 1],
                     [11, 48],
                     [1, 69],
                     [99, 70],
                     [20, 27],
                     [25, 42],
                     [6, 31],
                     [78, 24],
                     [42, 39],
                     [83, 30],
                     [94, 10],
                     [90, 37],
                     [76, 73],
                     [9, 56],
                     [39, 33],
                     [74, 15],
                     [77, 14]]

    num_node = len(city_location)  # 城市节点的数量
    iter_num = 300  # 迭代次数
    random.seed(3)  # 随机种子
    num_destroy = int(num_node * 0.2)  # 破坏程度

    # 计算距离成本矩阵 distance, 直接使用欧式距离
    distance = np.full((num_node, num_node), 0)
    for i in range(num_node):
        for j in range(num_node):
            distance[i][j] = ((city_location[i][0] - city_location[j][0]) ** 2 + (
                        city_location[i][1] - city_location[j][1]) ** 2) ** 0.5

    ############## 产生初始解 ############################
    solution = Solution()
    solution.route = [i for i in range(num_node)]  # 按照节点编号依次相连构成初始解也可随机产生
    lns = Lns_tsp(distance, num_node)
    solution.cost = lns.get_route_cost(solution.route)  # 计算初始解对应的目标成本
    best_solution = deepcopy(solution)  # 初始化最优解=初始解
    best_values_record = [0 for i in range(iter_num)]  # 初始化保存最优解的集合

    ############## 执行LNS ############################
    for n_gen in range(iter_num):
        tem_solution = deepcopy(solution)
        # 执行破坏修复算子，得到临时解
        tem_solution, destroy_node_bank = lns.destroy_operator(tem_solution, num_destroy)
        tem_solution = lns.repair_operator(tem_solution, destroy_node_bank)
        # 计算临时解的目标值
        tem_solution.cost = lns.get_route_cost(tem_solution.route)

        # 接受标准：如果临时解比当前解好，直接接受；且更新最优解
        if tem_solution.cost < best_solution.cost:
            solution = deepcopy(tem_solution)
            best_solution = deepcopy(tem_solution)
        best_values_record[n_gen] = best_solution.cost

    ############## 绘制结果 ############################
    plot_best_vales_iteration(best_values_record)
    plot_route(best_solution.route, city_location)
