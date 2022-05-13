# 闭包
# 定义：在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包
# 作用：保存外部函数的变量
# 形成条件:
# 1.在函数嵌套(函数里面再定义函数)的前提下
# 2.内部函数使用了外部函数的变量(还包括外部函数的参数)
# 3.外部函数返回了内部函数


# 函数嵌套
def func_out():
    num1 = 10

    def func_inner(num2):
        # 内部函数必须使用了外部函数的变量或参数
        result = num1 + num2
        print('结果:', result)

    # 外部函数返回了内部函数
    return func_inner                  # 返回的是函数名，而不是函数的执行func_inner()

# 获取闭包对象
# 这个new_func就是闭包
new_func = func_out()

# 执行闭包
new_func(5)

# 闭包存在时，外部函数的变量一直存在，直到闭包释放



# 外部函数含参
def func_out_(num1):

    def func_inner_(num2):
        result = num1 + num2
        print('结果:', result)

    return func_inner_

new_func_ = func_out_(1)
new_func_(5)














































