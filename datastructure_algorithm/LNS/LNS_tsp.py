"""
 @author: huang
 @date: 2023-09-21
 @File: LNS_tsp.py
 @Description:
"""
import random
import math

# 定义TSP问题的城市坐标
cities = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (2, 1),
    'D': (3, 4),
    'E': (4, 2)
}


# 计算两个城市之间的距离
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# 计算路径的总距离
def total_distance(path: list):
    total = 0
    for i in range(len(path) - 1):
        total += distance(path[i], path[i + 1])
    return total


# 初始化解（随机排列城市）
def initial_solution():
    cities_list = list(cities.keys())
    random.shuffle(cities_list)
    return cities_list


# 邻域操作：交换两个城市的位置
def swap(city_list, i, j):
    new_list = city_list[:]
    new_list[i], new_list[j] = new_list[j], new_list[i]
    return new_list


# LNS算法
def lns_tsp(max_iterations, max_no_improvement):
    """"""
    current_solution = initial_solution()
    current_distance = total_distance(current_solution)
    best_solution = current_solution[:]
    best_distance = current_distance
    no_improvement = 0

    for iteration in range(max_iterations):
        # 选择一个邻域操作，这里选择随机交换两个城市的位置
        i, j = random.sample(range(len(current_solution)), 2)
        new_solution = swap(current_solution, i, j)
        new_distance = total_distance(new_solution)

        # 如果新解更优，接受它；否则以一定概率接受它
        if new_distance < current_distance or random.random() < math.exp(
                -(new_distance - current_distance) / (iteration + 1)):
            current_solution = new_solution
            current_distance = new_distance
            if current_distance < best_distance:
                best_solution = current_solution[:]
                best_distance = current_distance
                no_improvement = 0
        else:
            no_improvement += 1

        # 如果连续一定迭代次数内没有改进，则退出
        if no_improvement >= max_no_improvement:
            break

    return best_solution, best_distance


# 运行LNS算法
best_solution, best_distance = lns_tsp(max_iterations=100000, max_no_improvement=100)

print("最优路径:", best_solution, "\n最短距离:", best_distance)

