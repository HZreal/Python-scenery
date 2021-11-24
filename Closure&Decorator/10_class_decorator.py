# 类装饰器：通过定义一个类来装饰函数
# 原理：show = Mydecorator(show)
#       被装饰函数将函数名func作为参数传给类，对类初始化返回一个实例对象，
#       并将这个实例对象赋给func(或者说将这个实例对象重命名为func)
#       以后对函数的调用：func()，就是对该类实例对象的调用，需要用到__call__方法


class Mydecorator(object):
    def __init__(self, func):    # 初始化函数接收创建实例的参数
        self.__func = func       # 设置成私有属性，避免外界访问

    # __call__()方法：对象被调用时就来执行
    def __call__(self, *args, **kwargs):
        print('课程已讲完')
        self.__func()

    # def __str__(self):
    #     return '我是一个对象'

@Mydecorator           # 相当于 show = Mydecorator(show), 此时的show就是实例对象
def show():
    print('快要下课了')

# 执行show() ，即是对Mydecorator实例对象的调用，即是show() ==> 对象()
# 而默认实例对象无法被调用，需要借助__call__方法
print(show)     # object 类型
show()

# show.func



'''
默认对象是无法被调用的
class AAA():
    pass
a = AAA()
a()

'''

# 扩展：函数之所以能够被调用是因为内部使用了__call__方法
def function():
    a = 1
    def add():
        pass
    print('哈哈')

# dir()查看内部使用的属性和方法
# print(dir())                     # 获得当前模块的属性列表
# print(dir(Mydecorator))          # 获得当前类的属性列表
# print(dir(function))                 # 获得当前函数的属性列表
# 可以用“函数名function的点操作”查看内部系统分配的隐藏函数，如下
# print(function.__dir__())



























































