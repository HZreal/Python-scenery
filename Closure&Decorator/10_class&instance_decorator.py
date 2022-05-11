# 一、类装饰器
# 通过类来装饰函数func，相当于无参装饰器
# 原理：show = MyDecorator(show)  装饰过程就是类的初始化！！！
#       被装饰函数将函数名func作为参数传给类，对类初始化返回一个实例对象，
#       并将这个实例对象赋给func(或者说将这个实例对象重命名为func)
#       以后对func的调用：func()，就是对该类实例对象的调用，调用时会执行__call__方法


class MyDecorator(object):
    def __init__(self, func):            # 相当于装饰器函数
        print('类的初始化过程就是装饰的过程, you can do some decorate-related operation here ------')
        self.func = func

    def __call__(self, *args, **kwargs):       # 被装饰函数func有参数时被args/kwargs接收
        print('被装饰后，新函数(实例)被调用的执行 ------')
        print('函数实参-----', args, kwargs)
        print('you can add some other operation before origin func ------')
        return self.func(*args, **kwargs)
        # print('you can add some other operation after origin func ------')

@MyDecorator           # 相当于 show = MyDecorator(show), 此时的 show 就是实例对象
def show(f1, f2):
    add_sum = f1 + f2
    print('----func show is executing------', add_sum)
    return add_sum
# 装饰后的show即是一个MyDecorator对象
print(show)                            # 输出show，为MyDecorator对象，此时并未执行__call__方法
add_sum = show(10, f2=22)                   # show(实例)的调用即是__call__的执行，若__call__方法有返回值，则实例的调用有返回值
print(add_sum)




# 二、实例装饰器
# 通过实例来装饰函数func，可以在类初始化时进行传参，即带参装饰器        ---------如flask的@route('/index', methods=[])
# 装饰过程就是执行__call__的过程！！！
# 装饰的过程中，可以进行适当操作，
# 装饰过程的最后是否return
#         a. 没有return时，原被装饰函数func=None
#         b. 有return时，原被装饰函数func被覆盖为return的结果，通常为一个闭包函数
class InstanceDecorator:
    def __init__(self, d1, d2):                # 类初始化(即装饰器初始化)时传参，即带参装饰器
        self.d1 = d1
        self.d2 = d2
        print('initialize decorator, you can do some operation related to decorator itself here')
        self.extra_init()

    def extra_init(self):
        """
        这里可以根据参数d1, d2对装饰器进行初始化配置
        """
        pass

    def __call__(self, func):                  # 相当于装饰器函数
        print('start decorate, you can do some decorate-related operation here ------')

        def wrapper(*args, **kwargs):          # 被装饰函数func有参数时被args/kwargs接收
            print('函数实参-----', args, kwargs)
            print('you can add some other operation before origin func ------')
            res = func(*args, **kwargs)
            print('you can add some other operation after origin func ------')
            return res

        # return 'wrapper11'                   # 用于测试原被装饰函数被覆盖的结果
        return wrapper                         # 返回一个闭包wrapper(保存了原func函数)，覆盖到原func，以后func的调用即是wrapper的调用


@InstanceDecorator(d1='dd11', d2='dd22')
def hello_func_without_params():
    print('----hello_func_without_params is executing------')

print('hello_func1 ===========', hello_func_without_params)            # 为闭包函数
hello_func_without_params()

@InstanceDecorator(d1='dd33', d2='dd44')
def hello_func_with_params(f1, f2):
    print('----hello_func_with_params is executing------')
    return f1 + f2
f12 = hello_func_with_params('aaa', f2='bbb')









# 实例方法装饰器，本质还是函数装饰器
class InstanceDecorator:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def decorator(self, func):              # 装饰器函数
        print(self.d1, self.d2)             # 装饰的过程可以用到实例的某些属性
        print('start decorate, you can do some decorate-related operation here ------')

        def wrapper(*args, **kwargs):
            print('函数实参-----', args, kwargs)
            print('you can add some other operation before origin func ------')
            res = func(*args, **kwargs) + 'ccc'
            print('you can add some other operation after origin func ------')
            return res

        return wrapper        # return会把函数wrapper重新赋给hello_func2，以至于hello_func2可以被调用，调用hello_func2时实际调用的是wrapper

ins_deco = InstanceDecorator(d1='abc', d2='123')

@ins_deco.decorator
def hello_func3(f1, f2):
    return f1 + f2
res = hello_func3('aaa', f2='bbb')
print('res', res)








# 扩展：
'''
对象默认是无法被调用的
class AAA():
    pass
a = AAA()
a()
'''


# 函数之所以能够被调用，是因为内部使用了__call__方法
def function():
    a = 1

    def add():
        print('add ---')

    print('func ')

# dir()查看内部使用的属性和方法
# print(dir())                         # 获得当前模块的属性列表
# print(dir(Mydecorator))              # 获得当前类的属性列表
# print(dir(function))                 # 获得当前函数的属性列表
# 可以用“函数名function的点操作”查看内部系统分配的隐藏函数，如下
# print(function.__dir__())
