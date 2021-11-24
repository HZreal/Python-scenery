# 生成器

# 根据程序员制定的规则循环生成数据，当条件不成立时则生成数据结束。
# 数据不是一次性全部生成处理，而是使用一个，再生成一个，可以节约大量的内存

# 创建生成器有两种方式：
# 1.类似于列表推导式，中括号改成小括号即可
# 2. yield关键字，在函数里有yeild，可以认为该函数就是一个生成器

# 方式一：
# 列表推导式
my_list = [value * 2 for value in range(3)]
# 生成器
my_generator = (value * 2 for value in range(3))
# print(my_generator)
# 生成器的取值使用next()函数，获取生成器中的下一个值
# value = next(my_generator)         # 每次取一个
# print(value)
# value = next(my_generator)         # 每次取一个
# print(value)
# value = next(my_generator)         # 每次取一个
# print(value)
# value = next(my_generator)       # 每次取一个
# print(value)                     # 此时StopIteration迭代异常

# 循环取值
# while True:
#     try:
#         value = next(my_generator)
#         print(value)
#     except Exception as e:
#         break         # 捕获异常则跳出循环，取值完成

# for循环内部自动调用next()函数，出现异常则自动捕获
# for value in my_generator:
#     print(value)





# 方式二：
# 在函数里使用yield关键字，则此函数就是一个生成器
def my_generator():
    for i in range(3):
        print('开始生成数据...')
        # 当程序执行到yield处会暂停执行，并把结果返回，再次启动生成器时会在暂停的地方继续执行
        yield i
        print('上次数据生成了...')
# 创建生成器
result = my_generator()
print(result)         # generator

# value = next(result)
# print(value)
# value = next(result)
# print(value)
# value = next(result)
# print(value)

# 生成器把所有数据生成完成后再生成依然会报错StopIteraion
for value in result:
    print(value)



































