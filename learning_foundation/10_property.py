# property属性
# property属性就是负责把一个方法当做属性进行使用



# 类装饰器方式的实现
class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 18

    # 获取私有属性(类装饰器)
    @property              # 这里的property实际就是一个类。当对象调用age属性的时候会执行下面的方法
    def age(self):
        print('获取私有属性')
        return self.__age

    @age.setter            # 当对象调用age属性设置值的时候会调用下面的方法
    def age(self, new_age):
        print('设置私有属性')
        if new_age >= 0 and new_age <= 120:
            self.__age = new_age
        else:
            print('不合法的年龄')

# 注意：使用装饰器方式的property属性，函数名必须一致，即上面获取设置的两个age方法函数名必须一致，但不一定非要是age

stu = Student()
# 获取私有属性
# age = stu.age()         # 以前的做法
age = stu.age             # 把方法当成属性来使用, 系统自动调用age()
print(age)

# 设置私有属性
stu.age = 22
age = stu.age
print(age)



# 类属性方式的实现
class School(object):
    def __init__(self):
        self.__num = 15

    # get_num 表示获取num属性时执行的方法
    def get_num(self):
        return self.__num

    # set_num 表示修改num属性时执行的方法
    def set_num(self, new_num):
        if new_num >= 0 and new_num <= 100:
            self.__num = new_num
        else:
            print('不合法年龄')

    # property是一个类，初始化时调用初始化函数，参数有fget, fset, fdel, fdoc
    # 以后获取num时，系统会自动调用get_num函数；修改num时，系统会自动调用set_num函数；
    num = property(get_num, set_num)

# TODO num究竟是什么？ 通过类调用会如何？
# number1 = School.num
# print('number1', number1)        # 说明num是一个对象？

# 获取私有属性
sch = School()
number2 = sch.num            # 系统自动调用get_num()
print('number2', number2)

# 设置私有属性
sch.num = 25                 # 系统自动调用set_num()
number = sch.num
print(number)




















