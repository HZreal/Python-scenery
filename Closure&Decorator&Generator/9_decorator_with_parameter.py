

# ！！！装饰器函数必须是：参数仅有一个且是函数类型！！！


# 带有参数的装饰器：本质是将装饰器封装在一个带参有返回值的函数里
def return_decorator(flag):
    # 对装饰器外包一个带参且有返回值函数，即可实现对装饰器的传参(这里的参数是decorator本身需要的，而不是inner需要的)

    # def decorator(func, flag):    # 不合法，flag无法接收
    def decorator(func):            # 装饰器函数，有且仅有一个函数类型的参数
        def inner(a, b):
            if flag == '+':
                print('加法计算进行中...')
            elif flag == '-':
                print('减法计算进行中...')
            func(a, b)
        return inner

    # 调用外包函数时，返回该装饰器，此时拿到了参数flag
    return decorator



@return_decorator('+')      # 相当于decorator = return_decorator('+')   @decorator ==> add = decorator(add)
def add(a, b):
    result = a + b
    print(result)

@return_decorator('-')
def sub(a, b):
    result = a - b
    print(result)

add(1, 5)
sub(4, 2)














































