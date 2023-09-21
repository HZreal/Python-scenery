# 继承
# 继承方式
# class Father(object):
#     def __init__(self):
#         self.wallet = '100'
#     def info_print(self):
#         print(self.wallet)

# class Son(Father):
#     pass

# son = Son()
# print(son.wallet)


# 单继承
# class Master():
#     def __init__(self):
#         self.skill = '专业全栈开发技能'
#     def make_object(self):
#         print(f'使用{self.skill},独立完成大型项目开发')

# class Prentice(Master):
#     pass

# pre = Prentice()
# print(pre.skill)
# pre.make_object()


# 多继承----------------------MRO顺序继承
# 一个类继承多个父类
# class Master():
#     def __init__(self):
#         self.name = 'master'
#         self.skill = '专业全栈开发技能'
#     def make_object(self):
#         print(f'使用{self.skill},独立完成大型项目开发')
# class School():
#     def __init__(self):
#         self.str = 'school'
#         self.skill = '极致Web开发技能'
#     def make_object(self):
#         print(f'使用{self.skill},独立完成大型服务器开发')
# #
# class Prentice(Master, School):
#     pass

# pre = Prentice()
# print(pre.skill)
# pre.make_object()              # 继承所有父类属性和方法，其中同名属性和方法默认优先继承第一个父类的!!!
# 查看某个类的继承关系
# print(Prentice.__mro__)


# 子类重写父类同名属性和方法
# class Pretice1(Master, School):
#     def __init__(self):
#         self.skill = '独创网页爬虫技术'
#     def make_object(self):
#         print(f'自学成才，用{self.skill}完成论坛爬取数据')

# pre1 = Pretice1()
# print(pre1.skill)
# pre1.make_object()        # 若子类与父类有同名属性和方法，那么子类创建对象调用同名属性和方法时，优先调用到的是子类的该同名属性和方法。简言之，子类重写父类的属性和方法




# 子类调用父类的同名属性和方法，只需把父类的同名属性和方法再次封装
'''
class Master():
    def __init__(self):
        self.skill = '专业全栈开发技能'
    def make_object(self):
        print(f'使用{self.skill},完成大型项目开发')
class School():
    def __init__(self):
        self.skill = '极致Web开发技能'
    def make_object(self):
        print(f'使用{self.skill},完成大型项目开发')

class Prentice(Master, School):
    def __init__(self):
        self.skill = '独创网页爬虫技术'
    def make_object(self):
        self.__init__()                     # 若不初始化，则此调用的同名属性值是上一次调用的init属性值
        print(f'使用{self.skill},完成大型项目123开发')

    def make_master_object(self):          # 调用父类Master的同名属性和方法
        # 需再次调用父类的初始化，因为父类的同名属性在init里。若没有调用父类初始化init,则使用的是子类本身的同名属性值
        Master.__init__(self)              # 没有self参数会报错
        Master.make_object(self)           # 没有self参数会报错

    def make_school_object(self):          # 调用父类School的同名属性和方法
        School.__init__(self)
        School.make_object(self)

    def make_master_object_1(self):         # 调用父类Master的同名属性值用的是子类的同名方法
        Master.__init__(self)
        self.make_object()

    def make_school_object_1(self):         # 调用父类School的同名属性值用的是子类的同名方法
        School.__init__(self)
        self.make_object()

    def make_master_object_2(self):         # 调用子类的同名属性值用的是父类Master的同名方法
        #无初始化即默认调用子类的初始化
        Master.make_object(self)

    def make_school_object_2(self):         # 调用子类的同名属性值用的是父类School的同名方法
        School.make_object(self)

pre = Prentice()
pre.make_object()
pre.make_master_object()
pre.make_master_object_1()
pre.make_master_object_2()
pre.make_school_object()
pre.make_school_object_1()
pre.make_school_object_2()

# 再次调用子类的make_object()
pre.make_object()                         # 若make_object(self)里没有self.__init__()，则调用的同名属性值是School的(上一次初始化的)，因为这一行的上行代码用的是School初始化
'''


# 多层继承
# class Student(Prentice):
#     pass
# stu = Student()
# stu.make_object()
# stu.make_master_object()
# stu.make_school_object()



# super()调用父类方法-----------单继承直接使用，自动查找父类。
# 对于多继承，调用顺序遵循__mro__()的结果的顺序(即MRO顺序)，super方法会使用一个D3算法，确保所有类的初始化方法仅仅调用一次
# super()如果指定参数的话super(current_class, self)，会直接调用指定参数类的方法。将会打破MRO指定的默认顺序，跳转到对应类上去执行

# 需求：一次性调用父类Master, School的方法
# class Master(object):
#     def __init__(self):
#         self.skill = '专业全栈开发技能'
#
#     def make_object(self):
#         print(f'使用{self.skill},完成大型项目开发')
#
# class School(Master):
#     def __init__(self):
#         self.skill = '极致Web开发技能'
#
#     def make_object(self):
#         print(f'使用{self.skill},完成大型项目开发')
#         # 有参数super
#         super(School, self).__init__()
#         super(School, self).make_object()
#
#         # 无参数super
#         # super().__init__()
#         # super().make_object()
#
# class Prentice(School):
#     def __init__(self):
#         self.skill = '独创网页爬虫技术'
#
#     def make_object(self):
#         self.__init__()
#         print(f'使用{self.skill},完成大型项目123开发')
#
#     def make_old_object(self):
#         # 方法一:
#         # 若定义类名被修改，则此函数体也得修改
#         # 当类较多时，代码庞大冗余
#         # School.__init__(self)
#         # School.make_object(self)
#         # Master.__init__(self)
#         # Master.make_object(self)
#
#         # 方法二:
#         # super(当前类名，self).函数()          # 有参数super()
#         super(Prentice,self).__init__()
#         super(Prentice,self).make_object()
#
#         # super().函数()                       # 无参数super()
#         # super().__init__()
#         # super().make_object()
#
# pre = Prentice()
# pre.make_old_object()


# Python类中如何调用父类？
# 1.直接写父类的名字
# 2.使用不带参数的super()方法
# 3.使用带参数的super(父类）方法
# 第1种方法较简单，在调用的时候指定父类名即可。这种方法在单继承的时候没问题，但是如果是多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等问题.父类的初始化方法会被多次调用。
# 解决方法就是使用不带参数的super方法，该方法会使用一个D3算法，该算法会确保所有类的初始化方法仅仅调用一次。
# class Parent(object):
#     def __init__(self, name, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
#         print('parent的init开始被调用')
#         self.name = name
#         print('parent的init结束被调用')
#
# class Son1(Parent):
#     def __init__(self, name, age, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
#         print('Son1的init开始被调用')
#         self.age = age
#         super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
#         print('Son1的init结束被调用')
#
# class Son2(Parent):
#     def __init__(self, name, gender, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
#         print('Son2的init开始被调用')
#         self.gender = gender
#         super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
#         print('Son2的init结束被调用')
#
# class Grandson(Son1, Son2):
#     def __init__(self, name, age, gender):
#         print('Grandson的init开始被调用')
#         # 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍
#         # 而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
#         # super(Grandson, self).__init__(name, age, gender)
#         super().__init__(name, age, gender)
#         print('Grandson的init结束被调用')
#
# print(Grandson.__mro__)
# # 利用.__mro__方法查询super在多继承中调用父类的顺序
# gs = Grandson('grandson', 12, '男')                          # super方法采用D3算法，确保所有类的初始化方法仅仅调用一次。
# print('姓名：', gs.name)
# print('年龄：', gs.age)
# print('性别：', gs.gender)
# print("******多继承使用super().__init__ 发生的状态******\n\n")





# 私有属性和私有方法    ----------------不能继承给子类
# 私有属性和私有方法只能在类里面访问和修改
class School():
    str1 = '123456'            # 此为类属性，若定义为私有，则需要通过类方法获取(后面讲)

    def __init__(self):
        self.name = 'Peking'
        self.__money = 20000

    # 获取私有属性值
    def get_money(self):
        return self.__money

    # 修改私有属性值
    def set_money(self, money):
        self.__money = money

    def __info_private(self):
        print('这是私有方法')

class Student(School):
    pass

sch = School()
stu = Student()
print(stu.name)
# print(stu.__money)                          # 报错
# stu.__info_private()                        # 报错
# print(sch.__money)                          # 报错
# sch.__info_private()                        # 报错
# 上述均报错，是因为类外无法获取私有属性，只能通过类里面的封装函数获取
# print(stu.get_money())
# stu.set_money()
# print(stu.get_money())


















































































































































































