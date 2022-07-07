import imghdr

# imghdr模块用于识别图片的格式。它通过检测文件的前几个字节(文件头)，从而判断图片的格式。

# imghdr.what(file, h)
# 参数，第一个参数file是一个文件路径字符串或者PathLike对象，第二个参数h是一个字节流。
# 文件对象用来对本地文件做检测，字节流用来对网络上的做检测。
# 当需要对一个字节流检测的时候第一个参数传None，第二个参数传入字节流即可，当指定了第二个参数时，第一个参数就会被忽略掉了，所以值是什么无所谓
# 返回值是一个字符串，是图片类型中的一种，表示检测到的此图片的类型。

file_path = '/Users/hz/Desktop/WeChat323b195bcc71489a188da4a087620c69.png'


file_type1 = imghdr.what(file_path)
print(file_type1)         # png

with open(file_path, 'rb') as f:
    content = f.read()
    file_type2 = imghdr.what(None, content)
    print(file_type2)     # png

    # TODO 传入文件对象无法读取
    file_type3 = imghdr.what(f)
    print(file_type3)      # None



