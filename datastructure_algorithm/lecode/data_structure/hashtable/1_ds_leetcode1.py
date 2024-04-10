"""
给定一个整数数组，一个整数目标值，求数组中某两个数之和等于目标值的这两个数的索引下标
"""



# num = []    # 元素为整数的列表
# target = 0    # 整数


def get_index_1(num: list, target: int):
    # 时间复杂度o(n^2)
    for index, value in enumerate(num):
        j = index + 1
        while j <= len(num):
            if value + num[j] == target:
                return [index, j]



def get_index_2(num: list, target: int):
    # 时间复杂度o(n^2)
    for index_s, item_s in enumerate(num):
        for index_d, item_d in enumerate(num):
            if index_d > index_s and item_s + item_d == target:
                return [index_s, index_d]


def get_index_3(num: list, target: int):
    # 时间复杂度o(n^2)
    index_s = len(num) - 1
    item_s = num.pop()
    while index_s > 0:
        for index_d, item_d in enumerate(num):
            if item_s + item_d == target:
                return [index_s, index_d]

        index_s -= 1
        item_s = num.pop()


def get_index_4(num: list, target: int):
    index_start = 0
    a = num[0]
    del num[0]
    while len(num) > 1:
        index_end = index_start + 1
        for item in num:
            index_end += 1
            if a + item == target:
                pass

def get_index_5(num: list, target: int):
    n = len(num)
    for i in range(n):
        for j in range(i + 1, n):
            if num[i] + num[j] == target:
                return [i, j]


# 使用哈希表-------------针对无序数组
# 时间复杂度为O(n) 对于每一个元素 x，我们可以 O(1)O(1) 地寻找 target - x
# 空间复杂度为O(n) 主要为哈希表的开销。
def twoSum(num: list, target: int):
    hashtable = dict()  # 哈希表/字典作映射，缓存
    for index, item in enumerate(num):
        if target - item in hashtable:
            return [hashtable[target - item], index]
        # 把当前值item及其索引i做映射放入哈希表(字典)，后续的继续遍历一旦找到item对应的数k(数k索引j)，则可通过字典，item映射取出i，即输出[i, j]
        hashtable[item] = index

    for index, item in enumerate(num):
        if item in hashtable:
            return [hashtable[item], index]
        hashtable[target - item] = index
    return []






def _test():
    l = [1, 2, 3, 4]
    a = l.pop()
    print(a)
    print(l)


if __name__ == '__main__':
    # _test()
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 10
    # res = get_index_5(num, target)
    res = twoSum(num, target)
    print(res)
