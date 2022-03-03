# io库
# 实现了解释器内置的 open() 后面的类，用于基于文件的输入和输出操作，提供了多个流式处理接口
from io import StringIO, BytesIO, FileIO, TextIOWrapper


# 原始I/O  即RawIOBase及其子类        也被称为无缓存IO，操作底层块，既可以用于文本I/O，也可以用于字节I/O。不推荐使用
# 文本I/O  即TextIOBase及其子类       读取一个str对象，得到一个str对象。
# 字节I/O  即BufferedIOBase及其子类   也称为缓存I/O， BytesIO 缓冲IO


# 文本I/O之StringIO 顾名思义就是在内存中以 io 流的方式读写 str
f = StringIO('Hhhhello!\nWorld!')             # 初始化StringIO对象时，此时指针在首部
f.write('\npython')                           # write方法写入时，是从指针位置开始覆盖写入，写入后指针在内容的尾部; 注意read/readline/readlines读取时指针的位置，可适当seek。此处从首部开始覆盖7个字符，指针移到了7
print('value-------->', f.getvalue())         # getvalue取值无需关心指针位置，指针位置不改变
print('read--------->', f.read())
f.seek(0)
print('read--------->', f.read())
f.seek(0)
print('readline--------->', f.readline())     # 读到的是'\n'  打印不可见。。。
print('readline--------->', f.readline())     # 读到的是'pythono!'
print('readline--------->', f.readline())     # 读到的是'World!'
f.close()


# readline/readlines读取
ff = StringIO('Hello!\nWorld!\nqwer\n1234')
while True:
    line = ff.readline()
    if line == '':
        break
    # print(line)
    print(line.strip())
ff.seek(0)
for line in ff.readlines():
    print(line.strip())
ff.close()




# 字节I/O之BytesIO
# bytes_io = BytesIO(b'hhhhello')
bytes_io = BytesIO('This goes into the buffer. '.encode('utf-8'))
print(bytes_io.getvalue())
print(bytes_io.read())
bytes_io.close()



# 包装文本数据的字节流
b_io = BytesIO()
wrapper = TextIOWrapper(
    buffer=b_io,
    encoding='utf-8',
    write_through=True
)
wrapper.write('This goes into the buffer. ')
wrapper.write('ace')
wrapper.seek(0)
print(wrapper.read())
print(b_io.getvalue())
b_io.close()

