# 装饰器:就是给已有函数增加额外功能的函数，它本质上就是一个闭包函数。

# 装饰器的功能特点:
# 1.不修改已有函数的源代码
# 2.不修改已有函数的调用方式
# 3.给已有函数增加额外的功能


# 装饰器要点:
#     1. @符号的本质就是，将被装饰的函数func作为装饰器decorator的参数传入，装饰器返回的inner(实质是一个闭包)赋给func变量
#        @符号后不管是多么复杂的表达式，最终的表现形式都是一个闭包函数@decorator(func)
#        其中函数decorator、带参decorator('')最终表现就是@decorator(func)，类Decorator最终表现为__init__(self, func)、实例Decorator('')最终表现为__call__(self, func)，三者实质一样
#     2. 装饰器函数的参数仅有一个且是函数类型！当然对于类/实例作为装饰器，其装饰函数(__init__/__call__)还有参数self
#     3. 被装饰函数func若有参数，其实参将被inner的形参接收；装饰器本身若有参数，只需在装饰器decorator外包一个函数(参数即装饰器本身所需参数，返回值返回decorator)
#     4. 被装饰后，现func的调用即inner的调用，inner中可以执行任何操作，但由于装饰器的意义(即在不改变原func下对原func进行扩展逻辑)，通常要执行原func；
#        inner的返回值本身可有可无，但是原func若有返回值则inner必须返回出去，于是可改用通用装饰器(inner参数写成*args、**kwargs，返回值return func(*args、**kwargs))
# 装饰器的副作用：
#      会使原函数的属性被改变，比如func.__name__，函数func被装饰后，func不再是原来的func，原来的func将无法被直接调用
#      可采用from functools import wraps，避免这种影响，详看_std_function.py







# 需求：对comment()这个函数添加评论前的登录验证功能

# 定义装饰器
def decorator(func):  # 参数仅有一个且是函数类型！！！
    print('装饰器执行了')

    # 把添加的登录验证功能放在内部函数里面
    def inner():
        print('test()登录验证进行中...')
        func()

    return inner


def comment():
    # 法一：最直接的方法就是添加登录验证函数test(),但是更改了原comment函数
    # test()
    print('发表评论')



# 法二：调用装饰器-------------在原comment()函数外面，没有影响到该函数的源代码以及调用方式

# 以前闭包的调用方式
# new_func = decorator(comment)      # 在闭包返回给new_func变量
# new_func()

# 把闭包返回的变量名直接写成comment
comment = decorator(comment)  # 此时的comment变成指向inner了 ！！！
comment()  # 调用comment()实际就是调用inner()


# 语法糖写法:
@decorator  # 实际就是对 comment = decorator(comment) 的封装  comment=inner
def comment():
    print('发表评论')


comment()
