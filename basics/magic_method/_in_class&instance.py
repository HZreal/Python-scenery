

class DemoClass:
    """
    Demo class
    """
    a = 1

    def __init__(self, b):
        self.b = b

    def method(self):
        pass


class B:
    pass

DemoInstance = DemoClass(2)
DemoInstance2 = DemoClass(3)


print(DemoClass.__class__)                                       # 所有类的__class__都是'type'
print('all class have the same type ?  ==>  ', B.__class__ == DemoClass.__class__)
print(DemoInstance.__class__)                                    # 实例的__class__即是实例对应的类名
print('class.__dict__   ==>  ', DemoClass.__dict__)              # 类.__dict__ 获取属于该类的所有属性
print('instance.__dict__   ==>  ', DemoInstance.__dict__)        # 实例.__dict__ 获取属于该实例独有的实例属性
print('instance.__dict__   ==>  ', DemoInstance2.__dict__)
print('class.__name__   ==>  ', DemoClass.__name__)              # 类的类名
print('class.__doc__   ==>  ', DemoClass.__doc__)                # 显示函数、类的注释
print('instance.__doc__   ==>  ', DemoInstance.__doc__)
print(DemoInstance.__hash__())

# def __new__(cls):
# print(DemoClass.__new__)
# print(DemoInstance.__new__)




class A(object):
    pass

class B(A):
    pass

b = B()

print(issubclass(B, A))






