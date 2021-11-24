import hashlib
md5_obj = hashlib.md5()
print(md5_obj)
str_byte = 'how to use md5 in hashlib?'.encode('utf-8')
print(str_byte)
md5_obj.update(str_byte)        # hashlib是对二进制进行加密的，如果直接对字符串加密的话， 会报错
# 中文字符在Python中是以unicode存在的
# 在hash前要求进行编码转换，是因为同一个字符串在不同的编码体系下有不同的值，为确保不发生歧义必须要进行一次显性转换
md5_value = md5_obj.hexdigest()        # 返回加密后的16进制字符串
print(md5_value)





