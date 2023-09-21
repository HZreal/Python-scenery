import functools
import time


# 定义装饰器，计算work函数的执行时间
def decorator(func):
    print('start decorate ----')

    def inner():
        begin = time.time()
        func()  # 原work函数在此执行
        end = time.time()
        exe_time = end - begin
        print('exe_time ---->  ', exe_time)

    return inner


# @decorator 表示去执行装饰器函数，做了两件事：
# 1. func=work          将work作为函数decorator的参数传入，返回inner
# 2. work=inner         将函数decorator的返回函数inner重命名为work
# 以后任何地方work的调用，都是调用inner，且inner内部用到的func就是最初的work

@decorator
def work():
    for i in range(10):
        print(i)


work()




# 通用装饰器，返回inner
def decorator2(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

# 扩展逻辑(此方式不算是标准的装饰器，语法上可行，用@操作单纯的给原函数包装一下，增添额外的print操作)
def wrapper(func):
    print('wrapper some extra operation ...')
    return func

@wrapper
# @decorator2
def hello(a, b):
    return a + b

print(hello(1, 2))
print(hello.__name__)          # wrapper装饰时输出hello，decorator2装饰时输出inner











