def add(a, b):
    return a + b

# 测试信息
# print(add(1, 5))

# print(__name__)
# __name__是系统变量，当在本文件里执行时,其值为__main__ ;当被其他文件导入执行时,其值为文件名
if __name__ == '__main__':
    print(add(1,5))


