# 装饰器:就是给已有函数增加额外功能的函数，它本质上就是一个闭包函数。

# 装饰器的功能特点:
# 1.不修改已有函数的源代码
# 2.不修改已有函数的调用方式
# 3.给已有函数增加额外的功能


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
