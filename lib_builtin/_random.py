import random

# 随机获取 [0, 1) 区间的一个浮点数
r = random.random()
print(r)

# 随机取样
choice = random.choice([1, 2, 3, 4])
print(choice)

# 随机取样（k个）
sample = random.sample([1, 2, 3, 4, 5, 6, 7], 2)
print(sample)

# 对数组元素随机调整顺序
arr = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(arr)
print('arr  ---->  ', arr)


