import uuid

# 8-4-4-4-12 共32位的16进制数的字符串




# 由 MAC 地址（主机物理地址）、当前时间戳、随机数生成。可以保证全球范围内的唯一性， 但这会导致MAC地址的暴露，局域网中可以使用 IP 来代替MAC。
# 若在Global的分布式计算环境下，最好用uuid1；
u1 = uuid.uuid1()
print(type(u1))        # uuid.UUID Object

u1_hexdigits_str = str(u1)         # 转换成标准形式的16进制字符串
u1_bytes = u1.bytes                # 获取UUID的原始16字节
print('u1 ---->  ', u1_hexdigits_str, u1_bytes)



# Python中没有 uuid.uuid2() -- 基于分布式计算环境DCE
# 算法与uuid1相同，不同的是把时间戳的前 4 位置换为 POSIX 的 UID。实际中很少用到该方法。


# uuid.uuid3(namespace, name) -- 基于名字的MD5散列值
# 通过计算命名空间和名字的MD5散列值得到，保证了同一命名空间中不同名字的唯一性， 和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。
# namespace有几个默认提供的：NAMESPACE_DNS   NAMESPACE_URL   NAMESPACE_OID   NAMESPACE_X500
u3 = uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name='name')
u3_hexdigits_str = str(u3)
u3_bytes = u3.bytes
print('u3 ---->  ', u3_hexdigits_str, u3_bytes)



# uuid.uuid4() -- 基于随机数
# 生成随机uuid，由伪随机数得到，有极小的重复概率
u4 = uuid.uuid4()
print('u4 ---->  ', str(u4))



# uuid.uuid5() -- 基于名字的SHA-1散列值
# 与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法。
# 若有名字的唯一性要求，最好用uuid3或uuid5。
u5 = uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name='salt')
print('u5 ---->  ', str(u5))





# ps:
# \x：16 进制的意思，后边跟两位，则表示单字节编码；       '\xE4\xB8\x89\xE7\xBA\xA7\xE8\x8A\x82\xE7\x82\xB9'
# \d：十进制；
# \o：八进制；
# \u：unicode 码； 一般其后跟 4 个 16 进制数           '\u4f60\u597d'




