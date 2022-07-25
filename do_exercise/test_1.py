# 1.
# 可变类型的拷贝
# dicts = {'one': 1, 'two': 2, 'three': 3}
# tmp = dicts.copy()
# tmp['one'] = 'abc'
# print(dicts)
# print(tmp)

# 2.
# a = [1, 2, 3]
# b = [1, 2, 4]
# print(id(a[1]) == id(b[1]))  # True
# python 为了提高内存利用效率会对一些简单的对象（如数值较小的int型对象，字符串等）采用重用对象内存的办法


# 3.
# 使用sorted()进行排序会生成新的序列，生成的新序列和原序列id值必然不同。对于可变对象，sorted()进行排序时原序列也发生变化
# 对于+=操作，如果是可变对象，则操作前后序列的id值不变，如果是不可变对象，则操作前后序列的id值改变，
# A
# lis = [1, 3, 2]
# a = id(lis)
# lis = sorted(lis)
# b = id(lis)
# print(a == b)

# B
# lis = [1, 3, 2]
# a = id(lis)
# lis += [4, 5]
# b = id(lis)
# print(a == b)  # 只有B选项这个正确

# C
# tup = (1, 3, 2)
# a = id(tup)
# tup += (4, 5)
# b = id(tup)
# print(a == b)

# D
# tup = (1, 3, 2)
# a = id(tup)
# tup = sorted(tup)
# b = id(tup)
# print(a == b)

# 4.求两数的最大公约数，
# 使用欧几里得算法，原理是
#      如果q=0，返回p；判断p>q
#      如果p>q，则p、q的最大公约数等于q与p%q的最大公约数，以此递归
# def f(a, b):
#     if b == 0:
#         return a
#     else:
#         return f(b, a % b)
#
# f(10, 3)


# 5.
# 变量也有两种类型：基本类型和引用类型。
# 基本类型的变量保存原始值，即它代表的值就是数值本身；
# 而引用类型的变量保存引用值，"引用值"指向内存空间的地址，代表了某个对象的引用，而不是对象本身，
# a = [['1', '2'] for i in range(2)]
# print('修改前的a---  ', a)
# print(id(a[0]) == id(a[1]))         # 地址不同
# a[0][1] = '3'
# print('修改后的a---  ', a)
#
# b = [['1', '2']] * 2
# print('修改前的b---  ', b)
# print(id(b[0]) == id(b[1]))         # 嵌套列表乘法得到的每个元素项都是引用，地址相同
# b[0][0] = '4'                       # 修改b[0]，b[1]也会同样改变
# print('修改后的b---  ', b)
#
# c = [1, 2] * 2
# print(id(c[0]) == id(c[1]))


# Intel中规定，栈是从高地址向低地址生长的；堆是由低地址向高地址增长的。ARM就没有规定的很死，可以选择栈是升序还是降序。
# 在任何计算机上，Python3代码中的float类型都没有办法直接表示[0,1]区间内的所有实数。因为计算机里的浮点类型只是一种用离散方式近似表达实数区间的方法，就可以知道，Python 里的 float 是不可能涵盖 [0,1] 区间内的所有实数的。即，只是---近似---表示，不是真正的能表达实数区间。


# 6.
# name = '顺顺'
# def f1():
#     print(name)
# def f2():
#     name = '丰丰'
# f1()
# f2()
# f1()

# 7. 字典的key，可以为int，字符串
# dicts = {}
# dicts[(1, 2, (1, ))] = 'abc'          # 可以，只有当元组内的所有元素都为不可变类型的时候，才能成为字典的key
# dicts[[1, ]] = 'abc'                # TypeError: unhashable type: 'list'
# dicts[{'a': 2}] = 'abc'                # TypeError: unhashable type: 'list'
# print(dicts)


# 8. 当参数为可变对象时，传参采用的是引用传递，修改形参将对实参造成影响；当参数为不可变对象时，传参采用的是值传递，修改形参对实参无影响，
# a = [1]
# b = 2
# c = 1
# def fn(lis, obj):
#     lis.append(b)
#     return lis, obj
#
# fn(a, c)
# print(fn(a, c))         # ([1, 2, 2], 2)
# 实参a为可变类型，作为形参传入函数中被修改时会影响原本a的值，实参c为不可变类型，传入函数中被修改时c的原始值不变


# 9. 使用import导入模块时，查找模块的顺序为
# ①内建模块
# ②程序的根目录/当前路径，即执行Python脚本文件所在的路径
# ③环境变量中的PYTHONPATH
# ④python安装路径，即标准库中


# 10. 修改全局变量时需要global声明
# a = 1
# b = [1, 2]
# def _variable():
#     # a = 3     # 定义局部变量a，与上述全局变量a不一样
#
#     # global 表示声明修改全局变量的内存地址
#     global a
#     a = 2
#     print(a)
#
#     # b为可变类型，不需要声明
#     b.append(3)
#
# _variable()


# 11.
# class Cat:
#     def __init__(self, color="白色"):
#         self.__color = color
#
# cat = Cat("绿色")
# print(cat._Cat__color)


# 12.
t1 = 0 or 1
t2 = 0 or 1 and True
print(t1)
print(t2)



# 13. range对象 支持索引取值，切片
_range = range(5)
print(type(_range), _range)
r1 = _range[2:]
r2 = _range[-1]
print(r1)
print(r2)











































































































