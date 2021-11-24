# 包

# 导入法一
# import mypackage.my_module1
# mypackage.my_module1.info_print1()

# 导入法二
# 必须在__init__中添加__all__ = [] 控制允许导入的模块
# from mypackage import *
# my_module1.info_print1()
# my_module2.info_print2()             # 若__all__ = []中没有my_module2 则无法导入

# 别名
# import mypackage.my_module1 as mod1
# mod1.info_print1()




