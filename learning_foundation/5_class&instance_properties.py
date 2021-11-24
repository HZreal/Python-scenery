# 类属性和实例属性
# 类属性指的是类对象所拥有的的属性，可用该类和该类创建得实例访问
# 实例属性指的是实例对象创建且独自拥有的属性
class Dog(object):
    tooth = 10     #设置类属性


# 用该类访问
print(Dog.tooth)
# 用该类创建的实例对象访问
dog1 = Dog()
print(dog1.tooth)


# 类属性的修改只能通过类本身去修改，不能通过实例对象修改
Dog.tooth = 12
# 再次访问
print(Dog.tooth)
print(dog1.tooth)


dog2 = Dog()


# 如果通过实例对象去修改，实际是该实例创建了一个与类同名的、独属于自己的实例属性
dog1.tooth = 32
# 访问类属性
print(Dog.tooth)                  # 还是12，说明类属性未被修改

# ！！！当再次访问dog1.tooth的时候，检测到dog1实例对象中有实例属性，就不会去类Dog中寻找了
# 所以此时访问的是dog1实例对象独属于自己的实例属性tooth，而不是访问类属性
print(dog1.tooth)                 # 实例属性tooth = 32

# dog2实例对象访问tooth时，结果为12 说明dog1实例对象创建的实例属性独属于dog1自己，此时dog2.tooth访问的是类属性
print(dog2.tooth)

# dog2实例对象创建自己的实例属性
dog2.tooth = 45
print(dog2.tooth, dog1.tooth, Dog.tooth)              # 45  32  12


# 总结：通过实例对象访问属性时，优先检测该实例对象是否有该属性，有则获取，没有再检测类对象的类属性





















































































































































