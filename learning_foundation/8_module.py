# 模块

# import math
# print(math.sqrt(9))

# from math import fabs, sqrt,sin
# print(fabs(-5))
# print(sqrt(16))
# print(sin(math.pi/6))

# from random import *
# print(randint(1,10))

# 定义别名
# import time as tt                          # 模块定义别名，以后只能用别名
# from random import randint as rint         # 功能定义别名
# tt.sleep(2)
# print('等2秒后再打印我')
# print(rint(1,5))

# 自定义模块并测试
# 每个python文件都可以作为一个模块，自定义模块必须符合标识符命名规则
# import selfdefine_module1
# result = selfdefine_module1.add(2, 3)
# print(result)

# 模块搜索顺序：Python解析器按由近及远搜索。模块搜索路径存储在system模块的sys.path变量中(PYTHONPATH)。变量里有当前目录，PYTHONPATH和由安装过程决定的默认⽬录
# 先搜索当前目录搜索，没有再搜索PYTHONPATH下的每个目录，还没有则查看默认路径

# 注意1.自己的文件名不要和已有模块名重名，会导致系统模块无法使用
# import random
# num = random.randint(1, 10)
# print(num)

# 注意2.导入的功能若有名字重复，则调用到的是最后定义或导入的那个功能
# from math import sqrt
# def sqrt(i):
#     return f'我是自定义的sqrt,结果为{i *2}'
# print(sqrt(4))            #调用到的是后面自定义的

# def sqrt(i):
#     return f'我是自定义的sqrt,结果为{i *2}'
# from math import sqrt
# print(sqrt(4))            #调用到的是导入的

# 名字重复的严重性
# import module 不需担心功能名重复的问题
# 变量能够覆盖模块，因为python语言中，数据是通过 引用 传递的
# import time
# print(time)
# time = 1
# print(time)     # 将上面的time覆盖


# from selfdefine_module2 import *
# textA()
# textB()      #没有添加到__all__列表，只有__all__列表里面的功能才能导入使用










































































































































































































































