# python内置高阶函数

# filter
# functools.reduce

import functools
from functools import reduce, wraps, partial, update_wrapper

# filter(function, iterable)
# 用于过滤序列，过滤掉不符合条件的元素，返回一个filter可迭代对象，保存符合条件的元素。如果要转换成列表，可用list()；也可直接遍历迭代器取值
# 第一个参数为过滤函数，第二个为待过滤序列
# filter_obj = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6])
# for i in filter_obj:
#     print(i)
# print(list(filter_obj))        # [3, 6]

# 去除空值
# list_1 = ['', 123, '123', [], {'a': 'b'}, (), ['a', 3], set()]
# print(list(filter(None, list_1)))
# print('-------------------------------------------------------')



# reduce(func, iterable)
# 会对iterable的元素进行累积处理，先对iterable中的第1、2个元素进行func操作，得到的结果再与第三个数据进行func操作，依次执行到iterable的最后一个元素
# 每次func计算的结果继续和iterable的下一个元素做累积计算
# 求列表元素之和
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9]))       # 45
# 求阶乘
# print(reduce(lambda x, y: x * y, [i+1 for i in range(6)]))



# map(function, iterable)
# 会根据func对指定iterable做映射，即iterable中的每一个元素调用func函数，返回一个迭代器，保存每次func函数映射的结果
# map_obj = map(lambda x: x ** 2, range(5))
# print(map_obj, list(map_obj))
# print('-------------------------------------------------------')



# sorted(iterable, key, reverse)
# 对可迭代对象进行排序
# 参数：
# key -- 排序的规则函数，带一个参数
# reverse -- 排序顺序，reverse=True降序，reverse=False升序（默认）
# 按可迭代对象元素的第一个属性排序
# print(sorted([['helen', 22], ['alin', 21], ['faker', 23]], key=lambda x: x[0]))
# 字典按值排列
score_map = {'language': 88, 'math': 89, 'english': 78}
sorted_score = sorted(score_map.items(), key=lambda x: x[1], reverse=True)
# print('=========字典按值排列==========', sorted_score)
# 按元素十位数与个位数之和排序
# print(sorted([12, 23, 11, 14, 51, 32, 49], key=lambda x: x / 10 + x % 10, reverse=True))
# 按元素绝对值大小排序
# print(sorted([4, 3, -1, -2, -5, ], key=abs))
# 按元素小写反向排序
# print(sorted(['bcd', 'about', 'diff', 'create'],key=str.lower,reverse=True))

# 使用sorted()进行排序会生成新的序列，生成的新序列和原序列id值必然不同。对于可变对象，sorted()进行排序时原序列也发生变化



# list.sort(key=None, reverse=False)
# 用于对列表进行排序，如果指定参数，则使用比较函数指定的比较函数
# 参数：
# key -- 用来比较的规则函数
# reverse -- 排序顺序
# persons = [['Alice', 26, 'F'], ['Trudy', 25, 'M'], ['Bob', 25, 'M'], ['Helen', 22, 'F']]
# 按可迭代对象元素的第一个属性排序
# persons.sort(key=lambda x : x[0])
# print(persons)

# 按性别排序，女性优先，性别相同时按年龄从小到大排序
# def compare_1(person_a, person_b):
#     if person_a[2] == person_b[2]:  # if their gender become same
#         return person_a[1] - person_b[1]  # return True if person_a is younger
#     else:  # if their gender not matched
#         if person_b[2] == 'F':  # give person_b first priority if she is female
#             return 1
#         else:  # otherwise give person_a first priority
#             return -1
# persons.sort(key=functools.cmp_to_key(compare_1))
# print(persons)

# 按十位数与个位数之和排序
# def compare_2(a1, a2):
#     return (a1 / 10 + a1 % 10) - (a2 / 10 + a2 % 10)
# data_list = [12, 23, 11, 14, 51, 32, 49]
# data_list.sort(key=functools.cmp_to_key(compare_2), reverse=True)
# print('data_list -----', data_list)


# sort 与 sorted 区别：
# sort是应用在list上的方法，sorted可以对所有可迭代的对象进行排序操作。
# list的sort方法在原内存空间上进行操作，对列表本身进行修改，不返回副本，而内建函数sorted方法不是在原内存空间上进行的操作，而是返回一个新的list
print('-------------------------------------------------------')




# zip
# 参数为多个可迭代对象
# 用于将这多个对象中下标索引对应的元素打包成一个元组，返回一个列表(py2.x)或者一个zip对象(py3.x)
# python2.x返回由这些元组组成的列表。Python3.x中为了减少内存，返回的是一个zip对象。如需展示列表，需手动 list() 转换
# 如果各个迭代器的元素个数不一致，则返回列表的长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表
# seq = ['one', 'two', 'three']
# seq1 = [1, 2, 3]
# seq2 = [4, 5, 6, 7]
# seq3 = [8, 9, 10, 11, 12]
# zip_obj = zip(seq, seq1)
# print(zip(seq))  # 不报错，
# print(zip_obj)  # <zip object at 0x10487e700>可以理解成(('one', 1), ('two', 2), ('three', 3))    是个生成器(使用过后，再次使用就是空对象)
# print('压缩两个并转成list-------', list(zip_obj))  # [('one', 1), ('two', 2), ('three', 3)]
# print('压缩两个并转成dict', dict(zip_obj))  # {'one': 1, 'two': 2, 'three': 3}    不注释上一行，则此处为空字典
# print('压缩多个并转成list-------', list(zip(seq, seq1, seq2, seq3)))  # 元素个数与最短的列表一致   [('one', 1, 4, 8), ('two', 2, 5, 9), ('three', 3, 6, 10)]
# print('压缩多个并转成dict-------', dict(zip(seq, seq1, seq2, seq3)))       # 报错

# a, b = zip(*zip(seq, seq1))
# c, d = zip(*zip_obj)                                                    # 会报错
# print('解压------', list(a), list(b))
print('-------------------------------------------------------')



# 内置类partial
# partial是一个类，通过实现__new__，自定义实例化对象过程，使得对象内部保留原函数和固定参数，通过实现__call__，使得对象可以像函数一样被调用，再通过内部保留的原函数和固定参数以及传入的其它参数进行原函数调用。
# partial用于部分应用一个函数，它基于一个函数创建一个可调用对象，把原函数的某些参数固定，调用时只需要传递未固定的参数即可。
# 通俗点说：就是把原函数的部分参数固定了初始值，新的调用只需要传递其它参数

def add1(a, b, c):  # add1函数原本接收参数a、b、c
    print('add1 ----->  ', a + b + c)
# 经过partial包装之后，a参数的值被固定为了1，b参数的值被固定为了2，返回partial对象，此对象的调用只需要接收剩余的参数c即可。
add11_partial = partial(add1, 1, 2)          # __new__方法，将func和参数元祖拆包后保存在一个可调用对象中并返回这个对象
add11_partial(3)                             # 调用这个对象时执行__call__方法，将对象中已保存的参数a、b与当前传入的参数c合并，传给原函数add1执行
add12_partial = partial(add1, c=4)
add12_partial(1, 5)
add13_partial = partial(add1, b=4)
add13_partial(1, c=5)                        # 注意，一旦创建partial给定了关键字参数b，那么原函数此参数b后面的参数c必须以关键字传


# 以下这种做法失去了partial原有的意义，不可取
@partial               # add1_作为参数实例化partial，并将实例赋给add1_变量
def add1_(a, b, c):
    return a + b+ c
add1_(1, 2, 3)         # 调用add1_，即调用partial对象的__call__

# partial原理解析，下面自己简单实现(也即是官方源码重要部分)
class MyPartial:
    def __new__(cls, func, /, *args, **kwargs):
        self = super(MyPartial, cls).__new__(cls)
        self.func = func
        self.args = args
        self.kwargs = kwargs
        return self

    def __call__(self, /, *args, **kwargs):
        full_kwargs = self.kwargs.copy()
        full_kwargs.update(kwargs)
        return self.func(*self.args, *args, **full_kwargs)

def add2(a, b):
    print('add2 -----', a + b)
add2_partial = MyPartial(add2, 1)
add2_partial(2)

@MyPartial
def add2(a, b):
    print('add2 -----', a + b)
add2(1, 2)


class MyPartial2:
    def __call__(self, func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
@MyPartial2()
def add2(a, b):
    print('add2 -----', a + b)
add2(1, 2)

'''
补充: 
def fun1(a, b, /, c):            “/”之前的变量，只能通过位置方式传递参数，不能通过关键字形式传递参数
def fun1(a, b, *, c):            “*” 代表“*”之后的参数，只能用关键字参数的方式给出
'''

print('-------------------------------------------------------')



# 内置函数wraps
# 由于装饰器的副作用(会使原函数的属性被改变，原函数被装饰后不能再使用原函数)，部分场合要用到原函数的属性就很不方便
# wraps 旨在消除装饰器对原函数造成的影响，即对原函数的相关属性进行拷贝，已达到装饰器不修改原函数的目的
# 简单的说，wraps装饰wrapper函数，装饰的结果为新wrapper，但会将被wrapped的一些属性值赋值给新wrapper，最终让属性的显示更符合我们的直觉。

# wraps源码解析
# def update_wrapper(wrapper, wrapped):     # 顾名思义更新wrapper，wrapped是被装饰的原函数add3，wrapper是被装饰器装饰后的新函数inner
#         ...
#     return wrapper
# def wraps(wrapped):                       # 内部通过partial对象和update_wrapper函数实现
#     return partial(update_wrapper, wrapped=wrapped)
# 再进入源码看update_wrapper、wraps的另外两个参数: assigned, updated
# assigned 为一个元祖，默认为('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')，每一个元素attr在wrapped中的值会拷贝到wrapper
# 即assigned表示 wrapper需要从 wrapped 中拷贝的魔法函数attr组，源码: setattr(wrapper, attr, getattr(wrapped, attr))
# updated 为为一个元祖，默认为('__dict__', )，每一个元素attr在wrapped中的值会追加到wrapper
# 即updated表示 wrapper需要从 wrapped 中追加的魔法函数attr组，源码: getattr(wrapper, attr).update(getattr(wrapped, attr, {}))

# 根据源码，简单重新实现partial类、update_wrapper方法
class partial_:
    __slots__ = "func", "args", "keywords", "__dict__", "__weakref__"

    def __new__(cls, func, /, *args, **kwargs):
        self = super(partial_, cls).__new__(cls)

        self.func = func
        self.args = args
        self.kwargs = kwargs
        return self

    def __call__(self, /, *args, **kwargs):
        keywords = {**self.kwargs, **kwargs}
        return self.func(*self.args, *args, **keywords)         # 等价于 return update_wrapper(inner, wrapped=add3)

def update_wrapper_(wrapper, wrapped):
    wrapper.__wrapped__ = wrapped
    return wrapper

# wraps使用
def outer(func):        # outer装饰add3时，func = add3

    @wraps(func)                                         # 等同于@partial(update_wrapper, wrapped=func)，wraps装饰inner最终返回的还是inner
    # @partial(update_wrapper, wrapped=func)             # 即实例装饰器，先实例化partial(其中update_wrapper、func作为实例化参数)，然后装饰inner的过程就是调用__call__方法(inner作为__call__的参数传入)，并return update_wrapper(inner, wrapped=add3)
    # @partial_(update_wrapper_, wrapped=func)           # 源码的简单实现
    def inner(*args, **kwargs):                          # *args, **kwargs接收被装饰后add3的实参
        print('--- before func ---')
        func(*args, **kwargs)
        print('--- after func ---')

    # print('inner.__dict__   ==>   ', getattr(inner, '__dict__'))     # 输出 {'__wrapped__': <function add3 at 0x104f27820>} 原因是源码update_wrapper中执行了inner.__wrapped__ = add3

    return inner

# 基于原理，可如下等同描述outer2、outer3
def outer2(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
    update_wrapper(inner, func)
    return inner

def outer3(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
    return update_wrapper(inner, func)


@outer
# @outer2
# @outer3
def add3(a, b):
    print('add3 is executing -----', a + b)

print('add3.name ------', add3.__name__)                # 由于wraps消除装饰器的副作用，此处输出'add3'，不使用wraps装饰时输出'inner'
add3(1, 2)                                              # 调用add3就是调用inner(inner是被wraps装饰后的inner，此inner属性与原add3属性相同)






























