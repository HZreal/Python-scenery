'''
import random

player = int(input("出拳头："))

computer = random.randint(0,2)
print(computer)

if ((player == 0)and(computer == 1) ) or ((player == 1)and(computer == 2)) or ((player == 2)and(computer == 0)):
   print("玩家获胜")
elif ((player == 0)and(computer == 2) ) or ((player == 1)and(computer == 0)) or ((player == 2)and(computer == 1)):
    print("电脑win")
else:
    print("平")

'''
'''
i = 0
while i < 5:
    print("对不住")
    i += 1
print("没问题")

''''''
i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print(result)
# 计数器为2时也可以完成，但是是人为大脑默认的+2也是偶数，此处用if判断是否为偶，符合计算机逻辑


# continue之前一定要修改计数器的值

'''

# ------------------------------------------------------------

"""
day = 0
while day < 5:
    i = 0
    while i < 5:
        if i <= day:
            print('*',end='')  #print()默认end为\n
        i += 1
    print('\n')    #换行
    day += 1
"""

'''
day = 0
while day < 5:
    i = 0
    while i < day:
        print('*',end='')  #print()默认end为\n
        i += 1
    print('\n')    #换行
    day += 1

'''

'''
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i} * {j} ={i*j}',end='    ')  #print()默认end为\n
        i += 1
    print('\n')    #换行
    j += 1

'''

'''
str1 = 'it heima'
for i in str1:
    if i == 'e':  
        break
    print(i,end=' ')
'''

'''
str1 = 'it heima'
for i in str1:
    if i == 'e':
        print('遇到e时不打印',end=' ')
        continue
    print(i,end=' ')

'''

'''
#else指的是循环正常结束之后要执行的代码，即如果是break终止循环的情况下，else后缩进的代码将不执行
i = 1
while i <= 5 :
    if i == 3:
        break
    print('我太难了')
    i += 1
else:
    print('哪里难了')
'''

'''
#如果是continue终止循环的情况下，else后缩进的代码会执行
i = 1
while i <= 5 :
    if i == 3:
        i += 1
        continue
    print('我太难了')
    i += 1 
else:
    print('哪里难了')
    
'''

'''
for 临时变量 in 序列：
    循环体
else:
    循环正常结束后要执行的
    
while  else 与for  else 相同， else后均是循环正常结束后要执行的（与其他语言不同）
'''

'''
# 遇到break时，else后面缩进的不执行,遇到continue,else后面的继续执行
str1 = 'it heima'
for i in str1:
    if i == 'e':
        break
    print(i,end=' ')
else:
    print('结束')
print('\n')
str1 = 'it heima'
for i in str1:
    if i == 'e':
        continue
    print(i,end=' ')
else:
    print('结束')

'''

# 整型int ：不可变数据类型
# a = 1
# print(id(a),type(a))          # 1912499232 <class 'int'>
# a = 2
# print(id(a),type(a))           # 1912499264 <class 'int'>


# 字符串

# 输出
# name = 'rose'
# print('我的名字是%s' % name)                 # %s格式化输出name字符串变量
# print(f'我的名字是{name}')                   # f格式化字符串
# print('我的名字是{}'.format(name))           # format()参数化给字符串传参
# 输入
# password = input('请输入您的密码：')
# print(f'您输入的密码是:{password}')
# print('您输入的密码是:%s'%password)


# 切片
# name = '012345678'
# print(name[1])
# print(name[2:5:1])    # 切片，开始位置下标，结束位置下标，步长
# print(name[2:5:2])    # 24
# print(name[2:])       # 2345678
# print(name[:5])       # 01234    不包括5 !!!
# print(name[::-1])     # 876543210       -1表示倒数选取    !!!
# print(name[-4:-1])    # 倒数第一个数下标为-1,以此类推   !!!
#
# print(name[-4:-1:-1])   # 无法选取
# print(name[-1:-4:-1])   # 可以选取   下标方向必须与步长方向一致才可以选取


# 查找
# mystr = 'today is a nice day, is very well'
# print(mystr.find('is'))
# print(mystr.find('is',2,12))   # 下标2到12之间查找is
# print(mystr.find('ios'))     # 查不出返回-1

# print(mystr.index('is'))
# print(mystr.index('is',2,12))
# print(mystr.index('ios',2,12))   #差不出，报错

# find与index用法相同，查找失败时前者返回-1，后者报错
# rfind() rindex() 是从右边开始查找，用法相同

# print(mystr.count('is',2,30))   #返回is出现的次数
# print(mystr.count('ios',2,30))   #返回0表示没有，不会报错


# 修改(不可变数据类型)
# mystr = 'today is a nice day, is very well'
# new_str = mystr.replace('is', 'and')
# print(mystr, id(mystr))
# print(new_str, id(new_str))    # 原来mystr不变 修改后的数据是函数返回值  replace为不可变修改

# rm_str = 'well'
# rm_str为要删除的字符序列  可以为空字符' '    '\n'   '\r'   '\t'    且字符在删除序列内，就删除掉，不论顺序
# mystr.strip(rm_str)              # 删除s字符串中开头和结尾处，位于 rm删除序列的字符
# mystr.lstrip(rm_str)             # 开头删除
# mystr.rstrip(rm_str)             # 结尾删除

# mystr.endswith()

# split分割
# list1 = mystr.split('is')
# print(list1)
# list2 = mystr.split('is',1)   #1表示分割次数
# print(list2)

# join 合并列表里面的字符串为一个大字符串
# mylist = ['aa','bb','cc']
# new_str = '...'.join(mylist)      #用 ... 来合并mylist
# print(new_str)

# capitalize()   字符串首字母变大写
# title() 每个单词首字母都变大写
# lower() 所有大写转小写
# upper()  所有小写转大写


# 列表：可变数据类型
#   index  count
#  in   not in 是否在列表
# 列表为可变数据类型   !!!

# append(数据)   参数作为整体添加至原列表
# extend(数据)   结尾增加数据  把参数拆开后再添加至原列表，即参数是序列时拆成单个字母，参数是列表时拆成单个序列再插入
# insert(位置下标，数据)   在指定位置前增加数据

# del(list)  del(list,下标)
# pop(下标)    删除指定下标的数据，不指定下标默认最后一个数据，返回的是删除的数据
# remove(数据)   直接删除列表中的某指定数据
# clear()  清空列表，返回空列表

# 对list中的元素直接赋值替换，即修改
# 逆置list.reverse()
# 排序list.sort(key,reverse) reverse=True降序 reverse=False升序(默认)

# 列表复制
# list2 = list1.copy()


# while遍历
# list = ['tom','jack','rose']
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1
# for 遍历
# for i in list:
#     print(i)


# 列表嵌套  [[1,2,3],[4,5],[6,7,8,9]]
# name_list = [['Tom','Jack','Lily'],['张三','李四','王五'],['xiaoming','xiaohong']]
# print(name_list[0])
# print(name_list[0][1])

'''
import random
teachers = ['A','B','C','D','E','F','G','H']
offices = [[],[],[]]
for name in teachers:
    # append extend insert
    num = random.randint(0,2)
    offices[num].append(name)
print(offices)
i = 1
for office in offices:
    print(f'办公室{i}的人数是{len(office)}')
    print(office)
    i += 1
'''

# 元组：又被称为只读列表，即数据可以被查询，但不能被修改，属于不可变数据类型
# tuple 放弃了对元素的增删（内存结构设计上变的更精简），换取的是性能上的提升：创建tuple比list要快，存储空间比list占用更小，多线程并发的时候，tuple是不需要加锁的，不用担心安全问题
# 元组也支持切片，但是它只支持通过切片访问元组中的元素，不支持修改
# 元组比列表中的访问和处理速度更快，所以如果只需要对其中的元素进行访问，而不进行任何修改，建议使用元组
# 关系操作符 in 和 not in 也可以直接应用在元组上，这跟列表是一样的
# 相对于list而言，tuple是不可变的，这使得它可以作为dict的key，或者扔进set里，而list则不行
# t1 = (10, 20, 30)
# print(type(t1))
# t2 = (10, )
# print(type(t2))   # tuple
# t3 = (10)
# print(type(t3))   # int
# t4 = ('aaa')
# print(type(t4))   # str
# t5 = ('aaa',)
# print(type(t5))   # tuple

# 元组数据不支持修改，只支持查找
# index() 存在返回下标查找不存在则报错
# count()
# len()
# t1 = ('aa', 'bb', 'cc', 'dd')
# print(t1[0])
# print(t1.index('aa'))
# print(t1.index('aaa'))        # 报错
# print(t1.count('aa'))           # 1
# print(t1.count('aaa'))          # 0
# print(len(t1))
# t1[0] = 'aaa'   元组数据不支持修改
# t2 = ('aa','bb',['cc','dd'])
# t2[2][0] = 'Tom'
# print(t2)    #元组里面有列表，里面的列表可修改

# 验证属于不可变数据类型
# c1 = ['1','2']
# c = (1,2,c1)
# print(c,id(c),type(c))         # (1, 2, ['1', '2']) 386030735432 <class 'tuple'>
# c1[1] = 'djx'
# print(c,id(c),type(c))         # (1, 2, ['1', 'djx']) 386030735432 <class 'tuple'>
# 虽然在列表中更改了值，但是列表的地址没有改变，列表在元组中的地址的值没有改变，所以也就意味着元组没有发生变化。我们就可以认为元组是不可变数据类型

# 可以间接的修改元组：通过拷贝现有的元组片段构造一个新的元组的方式解决，实质是新建一个元祖
# 思想：通过分片的方法让元组拆分成两部分，然后再使用连接操作符（+）合并成一个新元组
# temp = ("龙猫", "泰迪", "叮当猫")
# print(id(temp))
# new_temp = temp[:2] + ("小猪佩奇",) + temp[2:]          # 实质是新建一个元祖
# print(new_temp, id(new_temp))                           # ('龙猫', '泰迪', '小猪佩奇', '叮当猫')


# 字典：可变数据类型
# python中唯一的映射类型，采用键值对（key-value）的形式   无序存储数据
# OrderDict有序字典       # from collections import OrderedDict

# dict1 = {'name':'Tom','age':'22','gender':'男'}
# dict2 = {}
# dict3 = dict()   # 函数创建

# 添加|修改
# dict[key]   key存在则修改，不存在则新添加
# dict1['name'] = 'xiaoming'   #name存在 则修改
# print(dict1)
# dict1['book'] = '论语'    #key不存在则添加
# print(dict1)

# 删除
# del(dict1)
# print(dict1)   #直接清除，提示未被定义
# del dict1['name']
# del dict1['names']  #不存在此key报错

# dict1.clear()   清空，返回空字典

# 查找
# 按key查找
# print(dict1['name'])   #返回对应的value
# 用函数
# print(dict1.get('name'))   #Tom
# print(dict1.get('names'))    #None
# print(dict1.get('names','Lily'))   #Lily
# print(dict1.keys())  #查找所有的key
# print(dict1.values())  #查找所有的value
# print(dict1.items())  #查找所有的键值对,返回的是元组

'''
# 循环遍历
# 遍历key
for key in dict1.keys():
    print(key)
# 遍历value
for value in dict1.values():
    print(value)
# 遍历元素,
for item in dict1.items():
    print(item)
# 遍历键值对
for key,value in dict1.items():
    print(key)
    print(value)
    print(f'{key}={value}')    
'''

# aaa = ['a', 'b', 'c']
# bbb = [1, 2, 3]
# ccc = dict.fromkeys(aaa, bbb)               # {'a': [1, 2, 3], 'b': [1, 2, 3], 'c': [1, 2, 3]}
# ccc = dict(zip(aaa, bbb))                   # {'a': 1, 'b': 2, 'c': 3}
# print(ccc)

# 字典映射
# bbb = 5
# ccc = 44
# aaa = {bbb: ccc}
# print(aaa[bbb])


# 集合set  ：可变数据类型
# 没有重复且无序性  用于去重和关系运算
'''
s1 = {10,20,30}
print(s1)
s0 = set()
print(type(s0))
s2 = {10,30,20,10,20,40,30}
print(s2)     #集合里没有重复
s3 = set('abcdefg')
print(s3)
s4 = set()  #创建空集合
s5 = {}   #创建空字典
'''

# s1 = {10,20}
# s1.add(100)
# s1.add(100)  #集合有自动去重功能，不会报错但已经有了100则不需添加
# s1.add([10,20])    #报错,此时增加的是序列应该用update
# s1.update([10,20,30,40,50])
# print(s1)

# s1 = {10,20,30,40,50}
# s1.remove(10)     #删除指定数据，不存在时报错
# s1.discard(60)    #删除指定数据，不存在时不会报错
# del_num = s1.pop()    #随机删除某个数据，并返回该数据

# s1 = {10,20,30,40,50}
# in 和not in 判断数据是否存在集合里
# print(10 in s1)
# print(10 not in s1)

# 合并  +
# str1 + str2
# list1 + list2
# t1 + t2
# dict1 + dict2   #报错 字典不能合并
# 复制  *
# str1 = '-'
# print(str1 * 11)
#   +和*均不支持字典     !!!

# in 和 not in
# str1 = 'abcd'
# list1 = [10,20,30,40]
# t1 = (100,200,300)
# dict1 = {'name':'Python','age':'30'}
# print('a' in str1)
# print(10 not in list1)
# print(100 in t1)
# print('name' in dict1)
# print('name' in dict1.keys() )

# len()
# del 目标   或者   del(目标)

# max() 和 min()  返回元素的最大值最小值
# print(max(str1))
# print(min(list1))

# range(start,end,step)  生成从start到end(不包括)的数字，步长为step
# for i in range(1,10,1):
#     print(i)
# for i in range(10):   # 默认从0开始，步长为1 但end不能省
#     print(i)

# enumerate(可遍历对象，start = 0)  返回的结果是元组
# list1 = ['a','b','c','d']
# for i in enumerate(list1):
#     print(i)


# 容器类型转换
# tuple()  转换成元组
# list()
# set()


# 推导式  -------创建或控制有规律的数据
# 列表推导式
# 输出0~10的列表
# list1 = []
# i = 0
# while i < 10:
#     list1.append(i)
#     i += 1
# print(list1)
#
# list2 = []
# for i in range(10):
#     list2.append(i)
# print(list2)
#
# list3 = [i for i in range(10)]
# print(list3)
#
# #输出0~10的偶数列表
# list4 = [i for i in range(0,10,2)]
# print(list4)
#
# list5 = []
# for i in range(10):
#     if i % 2 == 0:
#         list5.append(i)
# print(list5)
#
# list6 = [i for i in range(10) if i % 2 == 0]
# print(list6)
#
# #创建[(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
# list7 = []
# for i in range(1,3):
#     for j in range(0,3):
#         list7.append((i,j))
# print(list7)
#
# list8 = [(i,j) for i in range(1,3) for j in range (0,3)]
# print(list8)
#


# 字典推导式 -------------快速合并列表为字典或者提取字典中的目标数据
# dict1 = {i : i**2 for i in range(1,6)}
# print(dict1)

# 将两个列表合并成一个字典
# list1 = ['name','age','gender','interest']
# list2 = ['Tom','22','men']
# dict = {list1[i]:list2[i] for i in range(min(len(list1),len(list2)))}
# print(dict)

# 提取字典中目标数据
# dict1 = {'MBP':268,'HP':125,'DELL':201,'Lenove':199,'acer':99}
# dict2 = {key : value for key,value in dict1.items() if value >= 200}
# print(dict2)


# 集合推导式
# list1 = [1,1,2]
# set1 = {i ** 2 for i in list1}
# print(set1)    #自动去重


#
# def add_num(a,b):
#     result = a + b
#     return result
#
# i = int(input('请输入第一个加数:'))
# j = int(input('请输入第一个加数:'))
#
# print(add_num(i,j))


# global a   声明a是全局变量


# 位置参数          参数个数和参数顺序必须一一对应
# 关键字参数           清除了参数的顺序需求，无序
# 缺省参数(又称默认参数)       函数定义时就给了形参默认值
# 不定长参数(可变参数)         用于不确定调用的时候回传递多少个参数(不传递也可)


# 包裹位置参数传递   ---------------根据实参具体情况返回一个元祖
# def user_info1(*args):
#     print(args)
# user_info1('Tom')
# user_info1('Tom',22)
# user_info1('Tom',22,'男')

#      包裹关键字参数传递   --------------------
# def user_info2(**kwargs):
#     print(kwargs)
# user_info2()     #返回空字典
# user_info2(name = 'Tom')
# user_info2(name = 'Tom',age = 22)


# 元组拆包
# def return_num():
#     return 100,200
# num1, num2 = return_num()     #用两个变量分别接受
# print(num1)
# print(num2)


# 交换变量的值
# 1.引入第三个变量
# c = a, a = b, b = c
# 2.直接赋值交换
# a,b = 1,2
# a,b = b,a
# print(a,b)


# 引用   -----python中，值是靠引用来传递的
# int
# a = 1
# b = a
# print(id(a))     # id()返回的是变量的内存地址
# print(id(b))
#
# a = 2
# print(id(a))
# print(id(b))

# list ----与int相同

# 引用可以当做实参
# def test1(a):
#     print(a)
#     print(id(a))
#
#     a += a
#     print(a)
#     print(id(a))
# b = 100
# test1(b)     # int为不可变类型，另辟内存存储，所以前后id值不同
# c = [11,22]
# test1(c)      # list是可变数据类型，在原地址处存储，所以id值相同

# 可变类型---------修改的是原数据,在原地址处修改更新
# list
# dict
# set
# 不可变类型---------修改的不是原数据，另辟内存存储，另用变量接收
# int
# float
# str
# tuple


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


# lambda匿名函数       python有限支持匿名函数
# lambda 参数列表：表达式
# 冒号前面的表示函数参数，冒号后面即是表达式且能有一个表达式。即匿名函数的限制，不用写return，返回值就是该表达式的结果

# （1）直接赋给一个变量，然后再像一般函数那样调用
# func = lambda x, y, z: x * y * z
# func(1, 2, 3)

# （2）将lambda函数作为参数传递给其他函数比如说结合map、filter、sorted、reduce等一些Python内置函数使用
# filter(function, iterable) 用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表,第一个为函数，第二个为序列
# filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6])               # [3, 6]

# map(function, iterable) 会根据提供的函数对指定序列做映射，即以序列中的每一个元素调用function函数，返回包含每次function函数返回值的新列表
# map(lambda x: x**2, range(5))              # [0, 1, 4, 9, 16]

# sorted(iterable, cmp, key, reverse) 函数对所有可迭代的对象进行排序操作
# 参数：cmp--比较函数  key--可迭代类型中某个属性，对给定元素的每一项进行排序   reverse--排序规则，reverse=True降序，reverse=False升序（默认）
# list.sort( key=None, reverse=False)用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
# 参数：key--主要是用来进行比较的元素  reverse--排序规则
# sort 与 sorted 区别：
# sort是应用在list上的方法，sorted可以对所有可迭代的对象进行排序操作。
# list的sort方法在原内存空间上进行操作，对列表本身进行修改，不返回副本，而内建函数sorted方法不是在原内存空间上进行的操作，而是返回一个新的list
# ali = [('b', 3), ('a', 2), ('d', 4), ('c', 1)]
# sorted(ali, key=lambda x: x[0])               # 表示根据可迭代对象的第一个元素进行排序，即按照字母排序 [('a',2),('b',3),('c',1),('d',4)]

# reduce(function, iterable)函数会对参数序列中元素进行累积，先对集合中的第1、2个元素进行func操作，得到的结果再与第三个数据进行func操作，依次执行到最可迭代对象最后一个元素后
# from functools import reduce
# result = reduce(lambda x, y: '{},{}'.format(x, y), [1, 2, 3, 4, 5, 6, 7, 8, 9])          # 1,2,3,4,5,6,7,8,9
# print(result)


# python内置高阶函数
# map(func, list)  --------------将传入的函数变量func作用到list变量的每个元素中,并将结果组成新的列表py2/迭代器py3
# list1 = [1, 2, 3, 4, 5]
# def func(x):
#     return x ** 2
# result = map(func, list1)
# print(result)
# print(list(result))   # 需要转换数据类型才能打印输出

# reduce(func, list)   -----------其中func必须有两个参数，每次func计算的结果继续和序列的下一个元素做累积计算
# import functools
# list2 = [1, 2, 3, 4, 5]
# def func(a, b):
#     return a + b
# result = functools.reduce(func, list2)
# print(result)

# filter(func, list)    --------用于过滤序列中不符合该函数条件的元素，返回一个filter对象，如果要转换成列表，用list()
# list3 = [1,2,3,4,5,6,7,8,9,10]
# def func(x):
#     return x % 2 == 0
# result = filter(func, list3)
# print(list(result))

# zip函数：参数为多个可迭代对象
# 用于将这多个对象中下标索引对应的元素打包成一个元组，返回一个列表(py2.x)或者一个zip对象(py3.x)
# python2.x返回由这些元组组成的列表。Python3.x中为了减少内存，返回的是一个zip对象。如需展示列表，需手动 list() 转换
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表
# seq = ['one', 'two', 'three']
# seq1 = [1, 2, 3]
# seq2 = [4, 5, 6, 7]
# seq3 = [8, 9, 10, 11, 12]
# zip_obj = zip(seq, seq1)
# print(zip(seq))                                                         # 不报错，
# print(zip_obj)                                                          # <zip object at 0x10487e700>可以理解成(('one', 1), ('two', 2), ('three', 3))    是个生成器(使用过后，再次使用就是空对象)
# print('压缩两个并转成list-------', list(zip_obj))                         # [('one', 1), ('two', 2), ('three', 3)]
# print('压缩两个并转成dict', dict(zip_obj))                                # {'one': 1, 'two': 2, 'three': 3}    不注释上一行，则此处为空字典
# print('压缩多个并转成list-------', list(zip(seq, seq1, seq2, seq3)))       # 元素个数与最短的列表一致   [('one', 1, 4, 8), ('two', 2, 5, 9), ('three', 3, 6, 10)]
# print('压缩多个并转成dict-------', dict(zip(seq, seq1, seq2, seq3)))       # 报错

# a, b = zip(*zip(seq, seq1))
# c, d = zip(*zip_obj)                      # 会报错
# print('解压------', list(a), list(b))


# 文件操作
# 打开文件
# open(name, mode, buffering)
# name:目标文件名字符串或者目标文件路径
# mode:访问模式  省略时默认为r
# buffering设置缓冲

# 访问模式mode
#   r: 只读,不可写，r模式打开文件不存在时会报错
#   w: 只写 ,文件不存在则新建文件，执行写入，会覆盖原有内容
#   a: 追加  ----文件不存在则新建，在原有内容上新增内容
#   rb:
#   wb:

# 设置缓冲buffering

# buffering=-1 系统默认缓冲
# buffering=0或者False      关闭缓冲   只能在二进制模式下设置
# buffering=1或者True       选择为行缓冲  只能在text模式下可用
# buffering>1              表示缓冲区块大小

# f = open('text1.txt', 'r')
# f.write('aaa')
# f.close()                   # 文件不存在则报错

# f = open('text2.txt', 'w')
# f.write('bbbbbbb')
# f.close()                  # 文件不存在则新建

# f = open('text3.txt', 'a')
# f.write('aaaaaa' + '\n')
# f.close()


# 文件数据读取
# read(size)   ------size为读取字节数长度，默认为-1表示一次性读取所有，文件过大时不可取，容易造成内存不够崩溃
# f = open('text.txt', 'r')
# print(f.read())                 # 读取所有
# print(f.read(10))               # 换行符\n 也是一个字符
# f.close()

# readlines()  ----按照行的方式把文件整个内容一次性读取，返回一个列表，列表元素为每一行的数据
# f = open('text.txt', 'r')
# content = f.readlines()
# print(content)                     # 原文件最后一行没有换行，所以打印出来最后一行没有换行符
# f.close()

# readline()   -------一次读取一行内容
# f = open('text.txt', 'r')
# con = f.readline()
# print(con)
# con = f.readline()
# print(con)
# con = f.readline()
# print(con)
# f.close()

# seek() ------用来移动文件指针
# 偏移量offset   当前指针移动偏移量
# 文件指针位置whence：    0表示文件开头   1表示当前位置   2表示文件结尾
# f.seek(offset, whence)
# f.seek(0, 0)




# 文件备份
# 1.用户接收文件名
# old_name = input('请输入您要备份的文件名：')
# print(old_name)
# 2.规划备份文件名
# 2.1 找后缀                # sound.txt.mp3
# index = old_name.rfind('.')
# print(index)
# 2.2 切片，取前一半名字和后一半后缀
# name = old_name[:index]
# print(name)
# if index > 0:
#     postfix = old_name[index:]
# new_name = name + '[备份]' + postfix
# print(new_name)
# 3.写入数据
# old_file = open(old_name,'rb')
# new_file = open(new_name,'wb')
# 不确定文件大小，避免内存不够读取用，采用循环读取写入，当读取出来的数据没有了则终止循环
# while True:
#     content = old_file.read()
#     if len(content) == 0:
#         表示读取完
# break
# new_file.write(content)
# old_file.close()
# new_file.close()


# 文件和文件夹的操作      ----- 借助os模块
# import os

# 文件
# os.rename(src, dst)
# os.rename('text2.txt', 'text222.txt')                     # 重命名
# os.remove('text222.txt')                                 # 删除

# 文件夹
# os.mkdir('file1')   # 创建文件夹 参数为文件名
# os.rmdir('file1')    # 删除文件夹
# print(os.getcwd())     ---------返回当前文件所在目录路径

# 需求：在 aa文件夹 里面创建 bb文件夹
# 先切换目录再创建
# os.chdir('file1')
# os.mkdir('bb')

# print(os.listdir())       # 返回某文件夹下所有文件的一个列表
# print(os.listdir('file1'))

# os.rename('file2','file1')

# 批量重命名
# 添加字符串
# file_list = os.listdir()
# print(file_list)
# for i in file_list:
#     new_name = 'Python_' + i
#     os.rename(i,new_name)

# 删除字符串
# flag = 2
# file_list = os.listdir()
# for i in file_list:
#     if flag == 1:
#         new_name = 'Python_' + i
#     elif flag == 2:
#         num = len('Python_')
#         new_name = i[num:]
#     os.rename(i,new_name)


# py3.8新语法，支持在表达式中赋值
# 赋值表达式使用海象运算符 := 在表达式中为变量赋值
# a = 4
# if b := 4 == a:
#     print('111')
#
# c = (d := 0)
# print(c)


# f = open('text.txt', 'r')
# print(f.read())
# while chunk := f.read():
#     print(chunk)


