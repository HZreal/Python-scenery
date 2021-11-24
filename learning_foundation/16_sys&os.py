from pathlib import Path
import sys,os

# sys.path#    即PYTHONPATH
# print(sys.path)


# sys.argv 实现从程序外部向程序传递参数，或者说接收本模块外部的某程序的参数
# 如终端执行：python "16_sys&os.py" aaaaa   传了两个参数
# print(sys.argv)                      # argv获取到参数列表 ['16_sys&os.py', 'aaaaa']
# print(sys.argv[0])                   # argv[0]获取到第一个参数 16_sys&os.py
# print(sys.argv[1])                   #  argv[1]获取到第二个参数 aaaaa


# sys.exit(status) 执行到主程序末尾，解释器自动退出，但是如果需要中途退出程序，可以调用sys.exit函数，带有一个可选的整数参数返回给调用它的程序，表示你可以在主程序中捕获对sys.exit的调用。（0是正常退出，其他为异常）
# def exitfunc(value):          # 退出函数：打印退出码(0为正常，1为异常)，并正常退出
# 	print(value)
# 	sys.exit(0)
#
# print('hello')                # 正常执行
#
# try:
# 	sys.exit(1)                  # 尝试异常退出
# except SystemExit as value:      # 捕获到异常退出   value=1
# 	exitfunc(value)              # 调用退出函数，正常退出主程序，以下的代码不会在执行
#
# print('come')                    # 由于调用了exitfunc(value=1) 导致主程序中途退出，print('come')以及以下代码不会执行


# sys.modules是一个全局字典，该字典是python启动后就加载在内存中。它拥有字典所拥有的一切方法
# 作用：每当程序员导入新的模块，sys.modules将自动记录该模块。当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。
# 本模块导入了sys和os模块
print(sys.modules["os"])
print(sys.modules.get('os'))                            # 对字典的操作

print(sys.modules.keys())                               # 'sys', 'os'等等
print(sys.modules.values())                             # <module 'sys' (built-in)> 等等






path = Path(__file__)                # 当前模块路径

print(os.path.abspath(path))	     # 返回绝对路径
# print(os.path.basename(path))	     # 返回文件名
# print(os.path.dirname(path))	     # 返回文件父目录
# print(os.path.exists(path))	     # 路径存在则返回True,路径损坏返回False
# os.path.getatime(path)	         # 返回最近访问时间（浮点型秒数）
# os.path.getmtime(path)	         # 返回最近文件修改时间
# os.path.getctime(path)	         # 返回文件 path 创建时间
# os.path.getsize(path)	             # 返回文件大小，如果文件不存在就返回错误
# os.path.isabs(path)	             # 判断是否为绝对路径
# os.path.isfile(path)	             # 判断路径是否为文件
# os.path.isdir(path)	             # 判断路径是否为目录



















































