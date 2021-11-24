# 上下文管理器:在类里面实现__enter__()和__exit__()方法，创建的对象就是上下文管理器

# __enter__() ：上文方法，提供对象资源
# __exit__()方法：下文方法，释放对象资源

# 自定义一个上下文管理器类
class File(object):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    #TODO
    # 上文方法，负责返回操作对象资源。比如文件对象，数据库连接对象
    # with语句执行前，自动执行
    def __enter__(self):
        print('enter...')
        # file = open(self.file_name, self.file_mode)    变量名为file时，下面__exit__()方法无法访问
        self.file = open(self.file_name, self.file_mode)
        return self.file                 # 返回文件对象

    # 下文方法，负责释放对象资源。比如关闭文件，关闭数据库连接对象
    # with语句执行后，自动执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('over...')
        self.file.close()


# with语句结合上下文管理器使用
with File('text.txt', 'r') as file:
    file_data = file.read()
    print(file_data)
    # file.write('aaaaa')      #报错了，但是__exit__()也执行了,保证了对象资源释放的安全性




# 函数上下文管理器
from contextlib import contextmanager
# 自定义一个函数，加上装饰器，这个函数创建的对象就是一个上下文管理器
@contextmanager
def my_open(file_name, file_mode):
    try:
        file = open(file_name, file_mode)
        print('begin...')
        # yield 关键字之前的代码是上文方法，负责返回操作对象资源
        yield file
    except Exception as e:
        print(e)
    finally:
        print('over...')
        # yield 关键字之后的代码是下文方法，负责释放操作对象资源
        file.close()


# 普通函数不能结合with语句使用,必须用@contextmanager进行装饰
with my_open('text.txt', 'r') as file:
    file_data = file.read()
    print(file_data)
    # file.write('sss')          #此处没有输出over... 说明文件没有释放，需要异常捕获


































































