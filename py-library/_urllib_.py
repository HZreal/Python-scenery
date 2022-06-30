# urllib   urllib3

# 模块urllib 和 urllib3的功能差不多，但 urllib3 更好一些。对于简单的下载，urllib 绰绰有余。如果要实现 HTTP 身份验证或 Cookie，抑或编写扩展来处理自己的协议，urllib3 可能是更好的选择。
import urllib.parse


string = 'hf:j23@kq黄'

# 转码
urlencode = urllib.parse.quote(string)
print(urlencode)

# 解码
urldecode = urllib.parse.unquote(urlencode)
print(urldecode)
















