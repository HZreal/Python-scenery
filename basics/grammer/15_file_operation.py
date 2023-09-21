# 文件操作



# 打开文件
# open(name, mode, buffering)
# name: 目标文件名字符串或者目标文件路径
# mode: 访问模式  省略时默认为r
# buffering: 设置缓冲

# 访问模式mode
#   r: 只读,不可写，r模式打开文件不存在时会报错
#   w: 只写 ,文件不存在则新建文件，执行写入，会覆盖原有内容
#   a: 追加  ----文件不存在则新建，在原有内容上新增内容
#   rb:
#   wb:

# 设置缓冲buffering
# buffering=-1 系统默认缓冲
# buffering=0或者False      关闭缓冲   只能在二进制模式下设置
# buffering=1或者True       选择为行缓冲  只能在text模式下可用
# buffering>1              表示缓冲区块大小

# f = open('text1.txt', 'r')
# f.write('aaa')
# f.close()                   # 文件不存在则报错

# f = open('text2.txt', 'w')
# f.write('bbbbbbb')
# f.close()                  # 文件不存在则新建

# f = open('text3.txt', 'a')
# f.write('aaaaaa' + '\n')
# f.close()


# 文件数据读取
# read(size)   ------size为读取字节数长度，默认为-1表示一次性读取所有，文件过大时不可取，容易造成内存不够崩溃
# f = open('text.txt', 'r')
# print(f.read())                 # 读取所有
# print(f.read(10))               # 换行符\n 也是一个字符
# f.close()

# readlines()  ----按照行的方式把文件整个内容一次性读取，返回一个列表，列表元素为每一行的数据
# f = open('text.txt', 'r')
# content = f.readlines()
# print(content)                     # 原文件最后一行没有换行，所以打印出来最后一行没有换行符
# f.close()

# readline()   -------一次读取一行内容
# f = open('text.txt', 'r')
# row1 = f.readline()
# print(row1)
# row2 = f.readline()
# print(row2)
# con3 = f.readline()
# print(con3)
# f.close()

# seek() ------用来移动文件指针
# 偏移量offset   当前指针移动偏移量
# 文件指针位置whence：    0表示文件开头   1表示当前位置   2表示文件结尾
# f.seek(offset, whence)
# f.seek(0, 0)




# 文件备份
# 1.用户接收文件名
# old_name = input('请输入您要备份的文件名：')
# print(old_name)
# 2.定义备份文件名
# 2.1 找后缀                # sound.txt.mp3
# index = old_name.rfind('.')
# print(index)
# 2.2 切片，取前一半名字和后一半后缀
# name = old_name[:index]
# print(name)
# if index > 0:
#     postfix = old_name[index:]
# new_name = name + '[备份]' + postfix
# print(new_name)
# 3.写入数据
# old_file = open(old_name, 'rb')
# new_file = open(new_name, 'wb')
# 不确定文件大小，避免内存不够读取用，采用循环读取写入，当读取出来的数据没有了则终止循环
# while True:
#     content = old_file.read()
#     if len(content) == 0:
#         # 表示读取完
#         break
# new_file.write(content)
# old_file.close()
# new_file.close()



# 文件和文件夹的操作      ----- 借助os模块
import os

# 文件
# os.rename(src, dst)
# os.rename('text2.txt', 'text222.txt')                     # 重命名
# os.remove('text222.txt')                                  # 删除

# 文件夹
# os.mkdir('file1')                   # 创建文件夹 参数为文件名
# os.rmdir('file1')                   # 删除文件夹
# print(os.getcwd())                  # 返回当前文件所在目录路径

# 需求：在 aa文件夹 里面创建 bb文件夹
# 先切换目录再创建
# os.chdir('aa')
# os.mkdir('bb')

# print(os.listdir())                 # 返回某文件夹下所有文件的一个列表
# print(os.listdir('mypackage'))


# 批量重命名
# 添加字符串
# file_list = os.listdir()
# print(file_list)
# for i in file_list:
#     new_name = 'Python_' + i
#     os.rename(i, new_name)

# 删除字符串
# flag = 2
# file_list = os.listdir()
# for i in file_list:
#     if flag == 1:
#         new_name = 'Python_' + i
#     elif flag == 2:
#         num = len('Python_')
#         new_name = i[num:]
#     os.rename(i,new_name)




