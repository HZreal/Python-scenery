# 单例模式
# 单例模式保证了在程序的不同位置都可以且仅可以取到同一个对象实例：如果实例不存在，会创建一个实例；如果已存在就会返回这个实例。
# 因为单例是一个类，所以你也可以为其提供相应的操作方法，以便于对这个实例进行管理。


# 几种实现方式如下
# 1.使用模块(懂就行)
# 其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
# 因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了
# mysingleton.py
# class Singleton(object):
#     def foo(self):
#         pass
# singleton = Singleton()
# 将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象( from a import singleton)，这个对象即是单例模式的对象




# 2.使用函数装饰器装饰类   (用类装饰器去装饰类 原理一样)   ！！！
# 使用不可变的类地址作为键，其实例作为值，每次创造实例时，首先查看该类是否存在实例，存在的话直接返回该实例即可，否则新建一个实例并存放在字典中
# def Singleton(cls):
#     _instance = {}
#     def _singleton(*args, **kargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kargs)
#         return _instance[cls]
#     return _singleton
#
# @Singleton
# class A(object):
#     a = 1
#
#     def __init__(self, x=0):
#         self.x = x
#
# a1 = A(2)
# a2 = A(3)
# print(id(a1) == id(a2))          # true
# id 关键字可用来查看对象在内存中的存放位置，这里 a1 和 a2 的 id 值相同，说明他们指向了同一个对象



# 3.使用类方法
# 类创建实例对象并赋给类的属性_instace中，没有_instance动态创建
class Singleton(object):
    def __init__(self, num):
        self.num = num

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            # Singleton._instance = Singleton(*args, **kwargs)
            cls._instance = cls(*args, **kwargs)
        # return Singleton._instance
        return cls._instance

aa = Singleton(2)
bb = Singleton(3)
print(aa)
print(bb)
# 此方法无法支持大量多线程
# https://www.cnblogs.com/huchong/p/8244279.html
# 解决办法：加锁！未加锁部分并发执行,加锁部分串行执行,速度降低,但是保证了数据安全
import time
import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

def task(arg):
    obj = Singleton.instance()
    print(obj)
for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
time.sleep(20)
obj = Singleton.instance()
print(obj)
# 从上可知：当我们实现单例时，为了保证线程安全需要在内部加入锁




# 4.基于__new__方法实现（推荐使用，方便）  ！！！
# 实例化一个对象时，是先执行了类的__new__方法（没写时，默认调用object.__new__，实例化对象），然后再执行类的__init__方法，对这个对象进行初始化，
# 所以我们可以基于这个，实现单例模式
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(id(obj1) == id(obj2))

def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()





# 元类(metaclass) 可以通过方法 __metaclass__ 创造了类(class)，而类(class)通过方法 __new__ 创造了实例(instance)



# 5.基于元类metaclass方式实现：在类的创建时进行干预，从而达到实现单例的目的
# 1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
# 2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法

# 实现单例之前，需要先了解使用 type 创造类的方法
def func(self):
    print("do sth")

Klass = type("Klass", (), {"func": func})

c = Klass()
c.func()

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Cls4(metaclass=Singleton):
    pass

cls1 = Cls4()
cls2 = Cls4()
print(id(cls1) == id(cls2))
# 将 metaclass 指向 Singleton 类，让 Singleton 中的 type 来创造新的 Cls4 实例






class Foo:
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        pass
obj = Foo()           # 执行type的 __call__ 方法，调用 Foo类（是type的对象）的 __new__方法，用于创建对象，然后调用 Foo类（是type的对象）的 __init__方法，用于对对象初始化。
obj()                 # 执行Foo的 __call__ 方法


# 元类的使用
class SingletonType(type):
    def __init__(self,*args,**kwargs):
        super(SingletonType,self).__init__(*args,**kwargs)
    def __call__(cls, *args, **kwargs): # 这里的cls，即Foo类
        print('cls',cls)
        obj = cls.__new__(cls,*args, **kwargs)
        cls.__init__(obj,*args, **kwargs) # Foo.__init__(obj)
        return obj

class Foo(metaclass=SingletonType): # 指定创建Foo的type为SingletonType
    def __init__(self, name):
        self.name = name
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

obj = Foo('xx')



# 实现单例模式
class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance

class Foo(metaclass=SingletonType):
    def __init__(self,name):
        self.name = name


obj1 = Foo('name')
obj2 = Foo('name')
print(obj1,obj2)


































