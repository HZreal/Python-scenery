# 通用装饰器
# 基本原则：内部函数的参数类型以及是否有返回值与被装饰的函数保持一致

# -----------------装饰带有参数的函数-------------------
# def decorator(func):
#     def inner(a, b):
#         print('计算进行中...')
#         func(a, b)
#     return inner
#
# @decorator
# def add(num1, num2):
#     result = num1 + num2
#     print('结果为：', result)
#
# add(1, 3)



# --------------装饰带有返回值的函数------------------
# def decorator(func):
#     def inner(a, b):
#         print('计算进行中...')
#         result = func(a, b)
#         return result
#     return inner
#
# @decorator
# def add(num1, num2):
#     result = num1 + num2
#     return result
#
# result = add(2, 5)
# print(result)



# ---------------装饰带有不定长参数和返回值的函数-----------------
# 此装饰器称为通用装饰器
def decorator(func):
    def inner(*args, **kwargs):
        print('计算进行中...')

        # *args把元组里面的每一个元素按照位置参数的方式进行传参
        # **kwargs把字典里面的每一个键值对按照关键字参数的方式进行传参
        # 这里对元组和字典进行拆包，仅限于结合不定长参数的函数使用
        result = func(*args, **kwargs)       # 函数没有返回值时，接收的为None
        return result
    return inner

@decorator
def add(*args, **kwargs):        # args 为元组类型; kwargs 为字典类型
    result = 0

    # 若是位置参数则args接收
    for value in args:
        result += value
    # 若是关键字参数则kwargs接收
    for value in kwargs.values():
        result += value

    return result

result = add(1, 5)
print(result)


@decorator
def show():
    print('哈哈')

show()


@decorator
def re_info():
    return 'a nice day'

result = re_info()
print(result)



'''
if __name__ == '__main__':
    my = {'a': 1}      
    print(**my)         # 不合法
'''














































