import base64

# ASCII编码是8位一个字节
# 将ASCII字符集中可打印的字符对应的二进制字节数据进行编码

# Base16编码
# 编码表:  数值 0~15 分别对应字符 0~9 A~F
# 编码方式:
#     1. 将数据转成对应的二进制数,不足8比特位的高位补0.
#     2. 然后将所有的二进制全部串起来,4个二进制位为一组,转化成对应十进制数. 4位二进制数可表示十进制的0~15
#     2. 根据十进制数值找到Base16编码表里面对应的字符.

# Base16是4个比特位表示一个字符,所以原始是1个字节(8个比特位)刚好可以分成两组,也就是说原先如果使用ASCII编码后的一个字符,现在转化成两个字符.数据量是原先的2倍.


# Base32编码
# 编码表:  数值 0~31 分别对应字符 A~Z 2~7
# 与Base16编码区别的是,Base32将串起来的二进制数据按照5个二进制位分为一组, 转化成对应十进制数. 5位二进制数可表示十进制数的范围0~31
# 编码后的数据量是原先的 8/5 倍

# Base64编码
# 编码表:  数值 0~63 分别对应字符 A~Z a~z 0~9 + /
# 与Base16编码区别的是,Base64将串起来的二进制数据按照6个二进制位分为一组, 转化成对应十进制数. 6位二进制数可表示十进制数的范围0~63
# 编码后的数据量是原先的 3 倍


text = 'qwertyuiop'
b_text = text.encode()


# b64编码
b_str = base64.b64encode(b_text)
print(b_str.decode())

# b64解码
res_b_text = base64.b64decode(b_str)
print('解码结果与原串一致？   ', res_b_text.decode() == text)


# b16
# b_str2 = base64.b16encode(b_text)
# print(b_str2.decode())

# res_b_text = base64.b32decode(b_str)
# print('解码结果与原串一致？   ', res_b_text.decode() == text)



# b32
# b_str2 = base64.b32encode(b_text)
# print(b_str2.decode())

# res_b_text = base64.b32decode(b_str)
# print('解码结果与原串一致？   ', res_b_text.decode() == text)
