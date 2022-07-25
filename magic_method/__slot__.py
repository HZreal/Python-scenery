# 实例的__dict__只保持实例的变量，对于类的属性是不保存的，类的属性包括类属性和类方法。
# 由于每次实例化一个类都要分配一个新的dict，因此存在空间的浪费，因此有了__slots__。
#     更快的属性访问速度
#     减少内存消耗

# __slots__ 是一个元组，包括了当前能访问到的属性。
# __slots__属性用来限制实例对象的属性，实例对象的实例属性最多只能在__slots__属性值的范围内。
# 如果子类没有定义__slots__属性，则不会继承父类的__slots__属性，如果子类定义了__slots__属性，则子类对象允许的实例属性包括子类的__slots__加上父类的__slots_。
# 当定义了slots后，slots中定义的变量变成了类的描述符，类的实例只能拥有__slots__中定义的变量，不能再增加新的变量。注意：定义了slots后，就不再有__dict__。

class Base(object):
    __slots__ = ('x', )

    var = 8

    def __init__(self):
        pass


b = Base()
b.x = 88  # 添加实例变量
print(b.x)

# b.y = 99  # 无法添加slots之外的变量 (AttributeError: 'base' object has no attribute 'y')
# print(b.__dict__)  # 定义了__slots__后，就不再有__dict__ (AttributeError: 'base' object has no attribute '__dict__')
