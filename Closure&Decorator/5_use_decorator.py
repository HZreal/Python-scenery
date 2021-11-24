import time

# 定义装饰器，计算work函数的执行时间
def decorator(func):
    def inner():
        begin = time.time()
        func()         # 原work函数在此执行
        end = time.time()
        exe_time = end - begin
        print(exe_time)
    return inner

# @decorator 表示去执行装饰器函数，做了两件事：
# 1. func=work  即将work作为参数赋给func
# 2. work=inner  即将装饰器返回函数inner重命名为work
# 以后任何地方调用work()，都是调用inner()，且inner内部用到的func就是最初的work
@decorator
def work():
    for i in range(10000):
        print(i)
work()


















