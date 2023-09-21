# 修改闭包内使用的外部变量

def func_out():
    num1 = 10
    def func_inner():
        # 在闭包内修改外部函数变量

        # num1 = 20             # 这种写法其实是在闭包内自定义了一个局部变量num1

        # global num1
        # num1 = 20             # 这种写法则是定义了一个全局变量

        nonlocal num1           # 闭包内声明外部函数变量
        num1 = 20

        result = num1 + 10
        print(result)


    print('修改前的num1：',num1)
    func_inner()
    print('修改后的num1：',num1)

    return func_inner

func_ = func_out()           # 程序在这一步时已经在执行func_out()，并且调用了一次func_inner()了

func_()                   # 程序在这里又执行了一次内部函数