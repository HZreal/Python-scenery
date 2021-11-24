# 异常
# try:                              # 一般下方只放一行代码尝试执行
#     f = open('text2.txt','r')     # r模式，文件不存在会报错
# except:
#     f = open('text2.txt','w')     # w模式，文件不存在不会报错，自动创建

# 异常类型
# print(num)            # NameError
# print(1/0)            #ZeroDivisionError

# 捕获指定异常类型
# try:
#     print(num)
# except NameError:       # 如果尝试执行的代码的异常类型和要捕获的异常类型一致，则捕获，执行except后的代码，不一致则无法捕获，不执行except后的代码
#     print('有错误')

# try:
#     print(1/0)
# except NameError:         # 捕获失败不继续执行
#     print('有错误')


# 捕获多个指定异常
# try:
#     print(1/0)
# except (NameError,ZeroDivisionError,NotADirectoryError):    #捕获多个异常，将可能的异常类型名放到except后，以元组的方式书写
#     print('有错误')

# 捕获异常描述信息
# try:
#     print(1/0)
# except (NameError,ZeroDivisionError,NotADirectoryError) as result:
#     print(result)

# 捕获所有异常
# Exception是所有程序异常类的父类
# try:
#     print(1/0)
# except Exception as result:
#     print(result)


# 异常中的else
# try:
#     print(1)
# except Exception as result:
#     print(result)
# else:                       # try后没有异常时会执行
#     print('这里是try后没有异常时会执行的代码')

# 异常的finally
# try:
#     f = open('text4.txt','r')
# except Exception as error_info:
#     f = open('text4.txt','w')
# else:
#     print('这里是try后没有异常时会执行的代码')
# finally:                 # 无论是否异常都要执行的代码，如关闭文件
#     f.close()


# 异常传递(异常的嵌套写法，先执行外层异常，再执行内层异常)
# 需求：
#         1.尝试以只读方式打开文件，若存在则读取，否则提示用户不存在
#         2.读取时要求循环读取，若读取过程检测到用户意外终止程序，则捕获异常并提示用户
# import time
# try:
#     f = open('text.txt','r')        #尝试打开文件
#     try:
#         while True:                 #尝试循环读取文件
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)            #等待两秒再执行下一行代码
#             print(content)
#     except:
#         #在命令提示符中,按下Ctrl+C(终止结束键)
#         print('读取过程被意外终止')
#     finally:
#         f.close()
#
# except:
#     print('文件不存在，无法读取')


# 自定义异常    语法：raise 异常类对象
# 需求：密码长度不足，报异常
# 用户输入密码，长度不足3位，则报错，即抛出自定义异常，并捕获该异常
# 自定义异常类
class ShortInputError(Exception):
    def __init__(self, input_len, min_len):
        self.input_len = input_len
        self.min_len = min_len

    def __str__(self):          #设置异常描述信息
        return f'你输入的密码长度是{self.input_len},不能少于{self.min_len}个字符'

def main():
    try:
        password = input('请输入密码：')
        if len(password) < 3:
            raise ShortInputError(len(password), 3)          #抛出异常
    except Exception as result:                              #捕获异常
        print(result)
    else:
        print('密码输入完成')
    finally:
        print('提交！')

main()















































































































































































































































