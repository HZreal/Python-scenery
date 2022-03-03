# 类是一系列具有相同特征和行为的事物统称，是一个抽象概念。
# 特征即属性，行为即方法
# 类使用来创建对象-----洗衣机图纸
# 对象是抽象类创建出来的真实实物-----洗衣机

# class Washer():   #首字母大写，，，类名遵循大驼峰命名
#     name = 'haier'
#     def wash(self):
#         print('洗衣服')
#         print(self)      #Haier实例的地址

# Haier = Washer()
# print(Haier)         #Haier实例的地址
# Haier.wash()
# 说明self指的是调用该函数的对象/实例

# 创建多个对象
# Haier1 = Washer()
# Haier1.wash()
# Haier2 = Washer()
# Haier2.wash()
# 两者地址不同，再次说明self指代调用该函数的对象

# 在类外为对象添加属性
# Haier1.width = 400
# Haier1.height = 500
# print(f'海尔洗衣机的宽度是{Haier1.width}')
# print(f'海尔洗衣机的高度是{Haier1.height}')


# 在类里面获取对象属性
# self.属性名
# class Washer():
#     def wash(self):
#         print('洗衣服')
#     def print_info(self):
#         print(self.width)
#         print(self.height)
# Haier1 = Washer()
# Haier1.width = 452     #类外添加对象属性
# Haier1.height = 556
# Haier1.print_info()

# 魔法方法 ：   __xxx__() 函数，具有特殊功能  系统自动调用
# 初始化  __init__()
# class Washer():
#     name = 'Haier 500Pro'
#     def __init__(self):
#         self.width = 400
#         self.height = 500
#     def print_info(self):
#         print(f'洗衣机的宽度是:{self.height},高度是:{self.width}')
# Haier = Washer()    #创建对象时自动调用__init__()初始化
# Haier.print_info()  #能执行，__init__()初始化函数默认已经执行
# print(Haier.name)

# 带参数的__init__()
# 一个类可创建多个对象，这多个对象有相同属性但属性值初始不同， 用传参数的__init__()
# class Washer():
#     name = 'Haier 500Pro'
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def print_info(self):
#         print(f'洗衣机的宽度是:{self.width},高度是:{self.height}')
# Haier1 = Washer(255,372) #创建对象时必须给实参否则报错
# Haier1.print_info()
# Haier2 = Washer(452,565)
# Haier2.print_info()


# __str__()
# print(对象)时默认打印对象的内存地址，此时有__str__() 则打印此方法中的返回值(一般是解释说明文字)
# class Washer():
#     name = 'Haier 500Pro'
#     def __init__(self):
#         self.width = 400
#         self.height = 500
#     def __str__(self):
#         return '海尔洗衣机说明书'
# Haier = Washer()
# print(Haier)    #此时不再输出对象Haier的内存地址，而是输出__str__()中的返回值

# __del__()删除对象
# class Washer():
#     def __init__(self):
#         self.width = 300
#     def __del__(self):
#         print('对象已经被删除！')
# Haier = Washer()     # 执行完代码自动执行__del__()删除对象
# print(Washer.__dict__)
# print(Haier.__dict__)

# __dict__
# 类对象和实例对象都拥有的方法
# 收集类、实例的属性和方法以及对应的值，返回一个字典
# class AA():
#     a = 11      #类属性
#     def __init__(self):
#         self.b = 12     #实例属性
#
# aa = AA()
# print(AA.__dict__)      # 返回该类的各个属性和方法以及对应值
# print(aa.__dict__)      # # 返回该对象的各个属性和方法以及对应值


class SSS():
    def abc(self):
        print('aaa111')

sss = SSS()
# sss.aaa()         # 实例对象调用
# getattr()方法获取类里面的实例方法名getattr(object, attr_name, default)
bbb = getattr(sss, 'abc')
bbb()


# 初始化方法，初始化未传则去类里找
class Spider:
    def __init__(self, name=None, **kwargs):
        if name is not None:
            self.name = name
        elif not getattr(self, 'name', None):
            raise ValueError(f"{type(self).__name__} must have a name")
        self.__dict__.update(kwargs)
        if not hasattr(self, 'start_urls'):
            self.start_urls = []

class mySpider(Spider):
    name = 'hello'
    allowed_domains = ['itcast.cn']
    start_url = ['https://www.baidu.cn/']

    def parse(self):
        pass
