# function





def hello(p1, p2):
    """
    this function hello is used for test
    :param p1: params1
    :param p2: params2
    :return: int
    """
    print('----hello----')

# print(hello.__dict__)
# print(getattr(hello, '__dict__'))
# print(hello.__name__)
# print(hello.__module__)
# print(hello.__doc__)         # 获取文档字符串
# print(hello.__qualname__)
# print(hello.__annotations__)
# print(hello.__class__)
print('--------------')
print(hello.__doc__)




# 高阶函数
# def sum_num(a, b, f):    # f 是函数作为参数传入
#     return f(a) + f(b)
#
# result1 = sum_num(-1, 2, abs)
# print(result1)
# result2 = sum_num(1.4, 2.6, round)
# print(result2)


# 递归
# 函数内部自己调用自己
# 必须有出口
# 需求：输出1 * 2 * 3 * ... * i
# def multi(i):
#     if i == 1:
#         return 1
#     else:
#         return i * multi(i-1)
# print(multi(5))

# 需求：输出斐波拉契数列  1, 1, 2, 3, 5, 8, 13
# def fibonacci(num):
#     # 输出斐波拉契数列中第num个数
#     if num <= 0 or not isinstance(num, int):
#         return
#     if num == 1 or num == 2:
#         return 1
#     else:
#         return fibonacci(num - 2) + fibonacci(num - 1)
# for i in range(1, 10):
#     print(fibonacci(i))


# lambda匿名函数       python有限支持匿名函数
# lambda 参数列表：表达式
# 冒号前面的表示函数参数，冒号后面即是表达式且只能有一个表达式。即匿名函数的限制，不用写return，返回值就是该表达式的结果

# （1）直接赋给一个变量，然后再像一般函数那样调用
# func = lambda x, y, z: x * y * z
# func(1, 2, 3)

# （2）将lambda函数作为参数传递给其他函数比如说结合map、filter、sorted、reduce等一些Python内置函数使用
# 内容转往_std_function.py文件








