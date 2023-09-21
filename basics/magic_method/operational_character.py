# __add__
# __iadd__
# __sub__


# __add__ 用于当两个对象进行 + 操作时的调用，于是整数、字符串、列表、元祖

# __add__    用新的变量存储拼接后的结果，原列表不变
# __iadd__   在原列表上拼接，并返回

# __add__可用于整型、字符串、元祖，而__iadd__不可以，原因是整型、字符串、元祖为不可变类型，无法在原地址处修改


# 整型
a1 = 1
a2 = 2
# a12 = a1 + a1
a12 = a1.__add__(a2)       # 等价
print(a1)
print(a12)

# 字符串
b1 = 'hhhh'
b2 = 'zzzz'
# b12 = b1 + b2
b12 = b1.__add__(b2)         # 等价
print(b1)
print(b12)


# 元祖
c1 = (1, 2, 3, 4, 5)
c2 = (7, 8, 9)
# c12 = c1 + c2
c12 = c1.__add__(c2)        # 等价
print(c1)
print(c12)


# 列表
# d1 = [1, 2, 3, 4, 5]
# d2 = [7, 8, 9]
# d12 = d1.__add__(d2)
# print(d1)         # d1 依然不变
# print(d12)

# d12 = d1.__iadd__(d2)
# print(d1)        # d1 已经是扩展了的列表
# print(d12)


# 字典：字典没有实现__add__方法，不能进行 + 操作

# 自定义Dict并定义__add__使字典支持 + 操作
# class MyDict(dict):
#     def __add__(self, item):
#         return self.update(item)
#
# e1 = MyDict(name='hh')
# e2 = MyDict(age=22)
# e12 = e1 + e2
# # e12 = e1.__add__(e2)
# print(e1)
# print(ee)


# 集合: 没有实现__add__方法，不能进行 + 操作
f1 = {1, 2, 3, 4, 5}
f2 = {4, 5, 6}
# f12 = f1 + f2             # error



# __sub__      实现了此方法的类，可进行 - 操作，如整型、集合

# 整型
a3 = 3
a4 = 1
# a34 = a3 - a4
a34 = a3.__sub__(a4)
print(a34)

# 集合         求差集
f3 = {1, 2, 3, 4, 5}
f4 = {4, 5, 6}
# f34 = f3 - f4
f34 = f3.__sub__(f4)
print(f34)




# __mul__

# 整型
a5 = 3
a6 = 4
# a56 = a5 * a6
a56 = a5.__mul__(a6)
print(a5)
print(a56)


# 字符串
b3 = 'jk'
# b33 = b3 * 3
b33 = b3.__mul__(3)
print(b33)


#































