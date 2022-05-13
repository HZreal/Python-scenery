# 生成器

# 根据程序员制定的规则循环生成数据，当条件不成立时则生成数据结束。
# 数据不是一次性全部生成处理，而是使用一个，再生成一个，可以节约大量的内存

# 生成器是一种特殊的可迭代对象，它会延迟加载元素，直到被请求才会加载。这在处理大量数据时会非常高效，它能提升存储效率。
# 相比之下，list 对象为了方便计数和索引，一次性创建所有的元素。所以跟生成器相比，在元素个数相同时，list 需要占用更多内存

# 创建生成器有两种方式：
# 1.类似于列表推导式，中括号改成小括号即可
# 2. yield关键字，在函数里有yield，可以认为该函数就是一个生成器，每执行到yield，生成器就会自动弹出一个值

# 方式一：
# 列表推导式
# my_list = [value * 2 for value in range(3)]
# 创建生成器
# my_generator = (value * 2 for value in range(3))
# print(my_generator)


# 1.next函数唤醒生成器，    生成器的取值使用next()函数，获取生成器中的下一个值
# value = next(my_generator)         # 每次取一个
# print(value)
# value = next(my_generator)         # 每次取一个
# print(value)
# value = next(my_generator)         # 每次取一个
# print(value)
# value = next(my_generator)       # 每次取一个
# print(value)                     # 此时StopIteration迭代异常

# 2.while循环取值
# while True:
#     try:
#         value = next(my_generator)
#         print('取的值为----->', value)
#     except StopIteration as e:
#         print('无值可取，结束---------------------------')
#         break  # 捕获异常则跳出循环，取值完成


# 3.for循环取值，内部自动调用next()函数，出现异常自动捕获结束
# for value in my_generator:
#     print(value)


# 方式二：
# 在函数里使用yield关键字，则此函数就是一个生成器
# def _generator():
#     for i in range(3):
#         print('开始生成第%d个数据之前...' % i)
#         # 当程序执行到yield处会暂停执行，并把结果返回，再次启动生成器时会在暂停的地方继续执行，通过打印的------------------分隔线可知
#         yield (i + 1)**2
#         print('第%d个数据生成了...' % i)
#     yield 5
#     print('end--------------------')


# # 创建生成器
# generator_obj = _generator()
# print(generator_obj)       # generator对象


# 1.next唤醒生成器,取值
# value = next(generator_obj)
# print(value)
# print('---------------------')
# value = next(generator_obj)
# print(value)
# print('---------------------')
# value = next(generator_obj)
# print(value)
# print('---------------------')

# 2.for取值，生成器把所有数据生成完成后再生成依然会报错StopIteraion
# for value in generator_obj:
#     print(value)





# next 与 send 区别
# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:", res)
#
# g = foo()
# print(next(g))
# print("*"*20)
# print(next(g))
# 执行结果：
# starting...
# 4
# ********************
# res: None
# 4
# 解析：执行next方法到yield时，并没有执行赋值操作给res传参，直接弹出值
# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:", res)

# g = foo()
# res = next(g)           # 等价于 g.__next__()
# print(res)
# print("*"*20)
# res = g.send(7)
# print(res)
# 执行结果：
# starting...
# 4
# ********************
# res: 7
# 4
# 解析：执行send到yield时，是会执行赋值操作给res传参的，并弹出值



# def generate():
#     i = 0
#     while i < 5:
#         print("before yield --------")
#         xx = yield i
#         print(xx)
#         i += 1
#
# g = generate()
# r = g.send(None)  # <==> next(g) 第一次启动，执行到yield i（此时i=0），挂起任务，主程序继续往下执行
# print(r)
# r = g.send("lalala")  # 第二次唤醒生成器，从上次的yield i 处继续执行，即往左执行，把lalala赋值给xx后，往下执行，直到下次的yield i（此时i=1），挂起任务
# print(r)


















