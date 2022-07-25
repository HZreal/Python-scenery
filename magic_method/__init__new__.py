# __init__与__new__
#     __init__ 方法为初始化方法, __new__方法才是真正的构造函数。
#     __new__方法默认返回实例对象供__init__方法、实例方法使用。
#     __init__ 方法为初始化方法，为类的实例提供一些属性或完成一些动作。
#     __new__ 方法创建实例对象供__init__ 方法使用，__init__方法定制实例对象。
#     __new__是一个静态方法，而__init__是一个实例方法。



class AAA:

    def __new__(cls, *args, **kwargs):
        """
        在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例
        类方法，属于类所有。类实例化前即可调用
        :param args:
        :param kwargs:
        """

        # 实例创建之前的操作

        # 创建实例，即__new__方法为实际上的构造函数

        # 返回实例，即返回实例对象供__init__等实例方法使用(实例对象作为__init__等实例方法的第一个参数self传入)


    def __init__(self, params1, params2):
        """
        当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
        """


        # 将创建的实例进行初始化























