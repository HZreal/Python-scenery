from Crypto.Cipher import ARC4, AES
import base64
import json
from Crypto.Util.Padding import pad, unpad

# 注意加解密时不能用同一个对象，需要重新new一个


# ps:
# 以表单上传文件时整个body的加解密
# 在中间件ARC4EncryptMiddleware中模拟


class ARC4Encrypt:
    # 注意加解密时不能用同一个对象，需要重新new一个
    key = 'solid'

    def __init__(self):
        self.arc4 = ARC4.new(key=self.key.encode())

    def arc4_encrypt(self, text: bytes) -> bytes:
        """
        加密    text -> response.content
        """

        # a = self.arc4.encrypt(text.encode())
        # b = base64.b16encode(a)
        # return b
        return base64.b16encode(self.arc4.encrypt(text))

    def arc4_decrypt(self, en_text: str) -> bytes:
        """
        解密   待解密串en_text -> request.body
        """
        # c = en_text.upper().encode()
        # b = base64.b16decode(c)
        # a = self.arc4.encrypt(b)
        # return a
        return self.arc4.decrypt(base64.b16decode(en_text.upper().encode()))      # 配合GO语言加密后在这里解密

    def arc4_file_encrypt(self, content: bytes) -> str:
        # 加密文件
        # return base64.b16encode(self.arc4.encrypt(content)).decode()
        return self.arc4_encrypt(content).decode()

    def arc4_file_decrypt(self, content: bytes) -> bytes:
        # 解密文件
        return self.arc4.decrypt(base64.b16decode(content))

def string_encrypt_with_ARC4():
    """
    ARC4对字符串加解密
    :return:
    """

    # 数据
    data = {
        "common": {
            "device_id": "8a189b6b-3d37-41e5-92fe-84e5866fa930",
        }
    }
    data = json.dumps(data)
    # 对字符串进行加密
    en_data = ARC4Encrypt().arc4_encrypt(data.encode()).decode()
    print('en_data------->  ', en_data)  # str      en_data = 'F3A66F74004DC3AF08927B7FED67FB7D6022A08E37CED62CD9A7131214F28315F8F6F57D75B6EDCEF71FC6214307A7A939B63892B2156B0D6FED2A18A6E495D27F'

    # 数据解密
    de_data = ARC4Encrypt().arc4_decrypt(en_data).decode()
    print('de_data------->  ', de_data)

def file_encrypt_with_ARC4():

    # 打开二进制文件
    with open('for_ARC4_encrypt.png', 'rb') as f:
        content = f.read()
        # print(content)       # bytes

    # 文件二进制内容加密
    en_str = ARC4Encrypt().arc4_file_encrypt(content=content)
    print('文件内容的加密结果------->  ', en_str)

    # 加密数据写入一个txt文件
    with open('_encrypt_data.txt', 'wb') as f:
        f.write(en_str.encode())

    # 文件解密
    de_content = ARC4Encrypt().arc4_file_decrypt(en_str.encode())
    print('compare ------>  ', de_content == content)   # True

def run_ARC4():
    # string_encrypt_with_ARC4()

    file_encrypt_with_ARC4()


class AESEncrypt:
    """
    高级加密标准，目前最常用
    """
    key = 'gdf4jf1gz3sj5ys5'  # key 必须为16/24/32字节长，分别对应AES-128、AES-192和AES-256
    mode_ECB = AES.MODE_ECB   # ECB模式加密不需要偏移量iv
    mode_CBC = AES.MODE_CBC   # CBC模式加密需要一个十六位iv(偏移量)  且 block_size = 16
    mode_GCM = AES.MODE_GCM
    BLOCK_SIZE = 16  # Bytes
    iv = '1234567890123456'

    def __init__(self, mode: str = 'ECB'):
        """
        # 工厂模式创建AES实例
        :param mode: AES mode
        """

        self.mode = mode.upper()
        if self.mode == 'ECB':
            # 此模式必须填充到块大小
            self.aes = AES.new(key=self.key.encode(), mode=self.mode_ECB)
        elif self.mode == 'CBC':
            # 此模式加密数据长度必须为16倍数
            self.aes = AES.new(key=self.key.encode(), mode=self.mode_CBC, iv=self.iv.encode())
        elif self.mode == 'GCM':
            self.aes = AES.new(key=self.key.encode(), mode=self.mode_GCM, nonce='qwertyuiop'.encode())
        else:
            raise Exception('The mode you specify is unsupported here')

    def aes_encrypt_bytes(self, content: bytes) -> str:
        """加密 from bytes to str"""
        if self.mode == 'ECB' or self.mode == 'CBC':
            # ECB/CBC模式  字符(字节)长度必须为16的倍数, 即数据块大小为16的倍数，需要用block_size补充位数
            content = pad(content, self.BLOCK_SIZE)
        return base64.b64encode(self.aes.encrypt(content)).decode()

    def aes_decrypt_bytes(self, content: bytes) -> bytes:
        """解密 from bytes to bytes"""
        de_bytes = self.aes.decrypt(base64.b64decode(content))
        if self.mode == 'ECB' or self.mode == 'CBC':
            de_bytes = unpad(de_bytes, self.BLOCK_SIZE)
        return de_bytes

    def aes_encrypt_str(self, text: str) -> str:
        """加密 from str to str"""
        content = text.encode()
        if self.mode == 'ECB' or self.mode == 'CBC':
            content = pad(content, self.BLOCK_SIZE)
        return base64.b64encode(self.aes.encrypt(content)).decode()

    def aes_decrypt_str(self, text: str) -> bytes:
        """解密 from str to bytes"""
        de_bytes = self.aes.decrypt(base64.b64decode(text.encode()))
        if self.mode == 'ECB' or self.mode == 'CBC':
            de_bytes = unpad(de_bytes, self.BLOCK_SIZE)
        return de_bytes


def use_ECB_Mode():
    # ECB mode

    text = 'today is a nice day'
    # 加密
    en_text_1 = AESEncrypt(mode='ECB').aes_encrypt_str(text)
    en_text_2 = AESEncrypt(mode='ECB').aes_encrypt_bytes(text.encode())
    print(en_text_1)
    print(en_text_2)
    print('加密结果一样？？？', en_text_1 == en_text_2)

    # 解密
    de_text_1 = AESEncrypt(mode='ECB').aes_decrypt_str(en_text_1)
    de_text_2 = AESEncrypt(mode='ECB').aes_decrypt_bytes(en_text_2.encode())
    print(de_text_1, de_text_2, sep='\n')
    print('解密结果一样？？？', de_text_1 == de_text_2)

def use_CBC_Mode():
    # CBC mode

    text = 'today is a nice day'
    # 加密
    en_text_1 = AESEncrypt(mode='CBC').aes_encrypt_str(text)
    en_text_2 = AESEncrypt(mode='CBC').aes_encrypt_bytes(text.encode())
    print(en_text_1)
    print(en_text_2)
    print('加密结果一样？？？', en_text_1 == en_text_2)

    # 解密
    de_text_1 = AESEncrypt(mode='CBC').aes_decrypt_str(en_text_1)
    de_text_2 = AESEncrypt(mode='CBC').aes_decrypt_bytes(en_text_2.encode())
    print(de_text_1, de_text_2, sep='\n')
    print('解密结果一样？？？', de_text_1 == de_text_2)

def  use_GCM_Mode():
    # GCM mode

    # 加密
    text = 'today is a nice day'
    en_text_1 = AESEncrypt(mode='GCM').aes_encrypt_str(text)
    en_text_2 = AESEncrypt(mode='GCM').aes_encrypt_bytes(text.encode())
    print(en_text_1)
    print(en_text_2)
    print('加密结果一样？？？', en_text_1 == en_text_2)

    # 解密
    de_text_1 = AESEncrypt(mode='GCM').aes_decrypt_str(en_text_1)
    de_text_2 = AESEncrypt(mode='GCM').aes_decrypt_bytes(en_text_1.encode())
    print(de_text_1, de_text_2, sep='\n')
    print('解密结果一样？？？', de_text_1 == de_text_2)

def run_AES():
    # use_ECB_Mode()
    # use_CBC_Mode()
    use_GCM_Mode()




if __name__ == '__main__':

    # run_ARC4()
    run_AES()


