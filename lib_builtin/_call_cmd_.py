import os

# python调用shell的两种方式
# os.system()  返回值是脚本的退出状态码，只会有0(成功),1,2；
# os.popen()  返回的是命令执行的输出，是一个file-like的对象，可实现一个“管道”，从这个命令获取的值可以继续被调用。os.popen方法是非阻塞的。


cmd = 'ls'

# status = os.system('ls')
# print('exec result ---->  ', status)

f = os.popen(cmd)
print(f.read())




