# with 语法    -------------既简单又安全
# with 语句执行完成以后自动调用关闭文件操作，即使出现异常也会自动调用关闭文件操作。

'''
try:
    file = open('text3.txt', 'r')
    result = file.write('over')
except Exception as e:
    print(e)
finally:
    print('over')
    file.close()
'''


with open('text.txt', 'r') as file:
    file_data = file.read()
    print(file_data)
    # file.write('aaaaaaaa')    # 此处即使报错，也会自动关闭文件


# 对于大文件需要分块写入
# for chunk in file.chunks():
#     file.write(chunk)














