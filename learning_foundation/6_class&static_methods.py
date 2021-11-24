# 类方法
# 使用场景：当方法中需要使用类对象(如访问私有类属性等)时，定义类方法
# 类方法一般和类属性配合使用
class Dog1():
    __tooth = 10

    @classmethod                       # 需要用装饰器@classmethod来标识其为类方法
    def get__tooth(cls):               # 类方法的第一个参数cls必须是类对象
        return cls.__tooth

    # 实例方法
    def func(self):                    # 参数self传入的是实例对象
        pass


# 类方法推荐使用类名直接调用
tooth = Dog1.get__tooth()
print(tooth)
# 当然也可以使用实例对象来调用（不推荐）
dog1 = Dog1()
result = dog1.get__tooth()
print(result)


# 静态方法
# 使用场景：当方法中既不需要使用实例对象(如实例对象，实例属性)也不需要使用类对象(如类属性，类方法，创建实例等)时，创建静态方法
# 取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
class Dog2():
    @staticmethod                          # 需要用装饰器@staticmethod来标识其为静态方法
    def info_print():                      # 既不需要类对象作为参数也不需要实例对象作为参数(形参没有self/cls)
        print('这是一个静态方法')

# 静态方法两种调用方式：
# 1.静态方法通过类对象(类名)去访问
Dog2.info_print()
# 2.静态方法通过实例对象访问
dog2 = Dog2()
dog2.info_print()



# 在实际编程中，几乎不会用到类方法和静态方法，因为我们完全可以使用函数代替它们实现想要的功能，
# 但在一些特殊的场景中（例如工厂模式中），使用类方法和静态方法也是很不错的选择。











































































