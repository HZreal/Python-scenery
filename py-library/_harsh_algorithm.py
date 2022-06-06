# MD5、SHA-1、SHA-256、HMAC-SHA256等属于哈希算法，计算数字摘要，不可逆，有极小的碰撞可能性
import hashlib
import hmac



test_str = 'how to use md5 in hashlib?'

# 一、md5
# （1）MD5的特点
# 长度固定:不管多长的字符串,加密后长度都是一样长。
# 作用:方便平时信息的统计和管理。
# 详解：经过MD5加密生成一个固定长度为128bit的串。因为128位0 和1的二进制串表达不友好，因此转化为了16进制，128/4 = 32位的 16进制。将32位去掉前8位和后8位得到的是16位。因此会有MD5的 32位 和16位加密说法。
# （2）易计算
# 字符串和文件加密的过程是容易的。
# 作用：开发者很容易理解和做出加密工具。
# （3）细微性
# 一个文件,不管多大,小到几k,大到几G,你只要改变里面某个字符,那么 都会导致MD5值改变。
# 作用:很多软件和应用在网站提供下载资源,其中包含了对文件的MD5码, 用户下载后只需要用工具测一下下载好的文件,通过对比就知道该文件是 否有过更改变动。
# （4）不可逆性
# 你明明知道密文和加密方式,你却无法反向计算出原密码。
# 作用:基于这个特点,很多安全的加密方式都是用到，大大提高了数据的 安全性。
# 不可逆的原因：摘要是部分内容，因此由MD5的密文和加密方式会得 到很多明文，而无法确定明文。
# 一个原始数据，只对应一个md5值；但是一个md5值，可能对应多个原始数据。
# 补充：MD5常用于字符串和文件的加密。

md5_obj = hashlib.md5()                               # 创建对象时亦可传入数据
md5_obj.update(test_str.encode())                     # 继续增添数据   ps: 中文字符在Python中是以unicode存在的，在hash前要求进行编码转换，是因为同一个字符串在不同的编码体系下有不同的值，为确保不发生歧义必须要进行一次显性转换
md5_value = md5_obj.hexdigest()                       # 返回加密后的16进制字符串
print('md5 ---->  ', md5_value)                       # 059ac3f7bcb536cfc295d028c5c64ec6

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5_obj1 = hashlib.md5()
md5_obj1.update('how to use md5 '.encode('utf-8'))
md5_obj1.update('in hashlib?'.encode('utf-8'))
print('md5 ---->  ', md5_obj1.hexdigest())

# MD5撞库
# 关于撞库破解: 这是概率极低的破解方法,原理就是:
# （1）建立一个大型的数据库,把日常的各个语句,通过MD5加密成为密文, 不断的积累大量的句子,放在一个庞大的数据库里。
# （2）比如一个人拿到了别人的密文,想去查询真实的密码,就需要那这个 密文去到提供这个数据库的公司网站去查询。

# MD5加盐   ----------实际就是一种HMAC算法(计算哈希的过程中，把key混入计算过程中)
# 比如我的银行密码是"12345"
# （1）得到的MD5是:827ccb0eea8a706c4c34a16891f84e7b
# （2）一个人截取到这个密文,那么通过撞库肯定容易撞出12345.
# （3）我们要做的就是加盐,银行密码还是"12345",然后把银行密码拼接上特定的字符串(如用户id)再计算MD5。
# 加盐可以保证相同密码下md5值不同，只需要盐不同即可，可以用用户id当盐
salt = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXA'
password = '123456'
print('password md5 without salt---->  ', hashlib.md5(password.encode()).hexdigest())
md5_obj2 = hashlib.md5(salt.encode())
md5_obj2.update(password.encode())
# print('password md5 with salt ---->  ', hashlib.md5((salt + password).encode()).hexdigest())
print('password md5 with salt ---->  ', md5_obj2.hexdigest())

# 文件摘要
# with open('_harsh_algorithm.py', 'rb') as f:
#     content = f.read()
# file_md5 = hashlib.md5(content).hexdigest()
# print('file_md5 ---->  ', file_md5)
# 大文件摘要
# big_file_md5 = hashlib.md5()
# with open('_encrypt_data.txt', 'rb') as f:
#     while True:
#         chunk = f.read(4096)
#         if not chunk:
#             break
#         big_file_md5.update(chunk)
# print('file md5 ---->  ', big_file_md5.hexdigest())



# 二、sha
# sha1
sha1_obj = hashlib.sha1()
sha1_obj.update(test_str.encode())
sha1_value = md5_obj.hexdigest()
print('sha1_value ---->  ', sha1_value)

# sha256
sha256_obj = hashlib.sha256()
sha256_obj.update(test_str.encode())
sha256_value = sha256_obj.hexdigest()
print('sha256_value ---->  ', sha256_value)



# 三、内置函数hash()
# hash(obj)
# 对对象取哈希值
class HashObj:
    pass

obj = HashObj()
ret_hash = hash(obj)
print('对象的哈希值 ---->  ', ret_hash)        # 结果不固定



# 四、hmac库
# HMAC算法 -------->  就是哈希摘要算法 + 盐
message = password.encode()
key = salt.encode()
h = hmac.new(key, message, digestmod='MD5')            # HMAC-MD5
print('hmac md5 value ---->  ', h.hexdigest())
h2 = hmac.new(key, message, digestmod='SHA256')        # 即HMAC-SHA256，简称HS256
print('hmac sha256 value ---->  ', h2.hexdigest())





# url数量上亿进行哈希操作存redis
# url-hash
# 布隆过滤器
# 编辑距离
