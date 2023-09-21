import jwt
from datetime import datetime, timedelta

# doc:  https://pyjwt.readthedocs.io/en/stable/
# 将字典转换成JWT token字符串

payload = {'username': 'huang', 'password': '123456'}
JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'


# JWT 最常见的两种签名算法：HS256(HMAC-SHA256) 和 RS256(RSA-SHA256)。
# HS256 和 RS256 都是一种消息签名算法，得到的都只是一段无法还原的签名。区别在于消息签名与签名验证需要的 「key」不同。
# HS256 使用同一个「secret_key」进行签名与验证。一旦 secret_key 泄漏，就毫无安全性可言了。因此 HS256 只适合集中式认证，签名和验证都必须由可信方进行。
# RS256 是使用 RSA 私钥进行签名，使用 RSA 公钥进行验证。公钥即使泄漏也毫无影响，只要确保私钥安全就行。RS256 可以将验证委托给其他应用，只要将公钥给他们就行。
# 对于单体应用而言，HS256 和 RS256 的安全性没有任何差别。而对于需要进行多方验证的微服务架构而言，显然 RS256 安全性更高。
# 只有 user 微服务需要用 RSA 私钥生成 JWT，其他微服务使用公钥即可进行签名验证，私钥得到了更好的保护。


# jwt库基本使用
def basic_use():
    # 将载荷转为jwt串
    jwt_str = jwt.encode(payload=payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM)
    print('Token --------', jwt_str)

    # 将jwt串还原为原始载荷
    payload_ = jwt.decode(jwt_str, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
    print('origin payload -------', payload_)

    print(payload == payload_)  # True


# JWT机制自己简单实现，生成JWS
def genertate_JWS_token():
    import base64
    import hmac

    header = {
        'type': 'JWT',
        'alg': 'HS256',
    }
    now = datetime.utcnow()
    exp = now + timedelta(hours=2)
    payload = {
        'iss': 'huang',
        'iat': now.strftime('%Y%m%d%H%M%S'),
        'exp': exp.strftime('%Y%m%d%H%M%S'),          # 过期时间点，不是duration
    }
    payload.update({'user_id': '269'})

    # jwt第一部分
    first_segment = base64.b64encode(str(header).encode()).decode()
    print('first segment ---->  ', first_segment)

    # jwt第二部分
    second_segment = base64.b64encode(str(payload).encode()).decode()
    print('second segment ---->  ', second_segment)

    # jwt第三部分
    secret = 'TPmi4aLWRbyVq8zu9v8-2dWYW17z+UvRnYTt4P6fAXA'            # 即 JWK
    msg = first_segment + '.' + second_segment
    h = hmac.new(key=secret.encode(), msg=msg.encode(), digestmod='SHA256')         # 使用HS256
    third_segment = h.hexdigest()
    print('third segment signature ---->  ', third_segment)

    # 完整jwt token
    print('JWT token ---->  ', first_segment + '.' + second_segment + '.' + third_segment)



# 封装
class JWTEncodeDecodeHandler:

    def __init__(self, secret=None, algorithm=None):
        self.secret = secret or JWT_SECRET
        self.algorithm = algorithm or JWT_ALGORITHM

    def generate_jwt(self, payload, expiry):
        """
        生成JWT token
        :param payload:
        :param expiry:     表示截止时间     unix时间
        :return:
        """
        payload.update({'exp': expiry})
        return jwt.encode(payload, key=self.secret, algorithm=self.algorithm)

    def verify_jwt(self, token):
        """
        验证token是否有效
        :param token:
        :return:
        """
        try:
            payload = jwt.decode(token, key=self.secret, algorithms=[self.algorithm])
        except jwt.PyJWTError as e:
        # except Exception as e:
            print(e)
            payload = None

        return payload

def useJWTEncodeDecodeHandler():
    """
    封装测试
    :return:
    """
    expiry = datetime.utcnow() + timedelta(seconds=2)  # 设置有效期2秒，即当前时间+2秒
    _jwt = JWTEncodeDecodeHandler()
    token = _jwt.generate_jwt(payload, expiry)
    print('encode token ->  ', token)

    # time.sleep(3)
    verified_info = _jwt.verify_jwt(token)
    print('decode payload ->  ', verified_info)

if __name__ == '__main__':
    # basic_use()
    genertate_JWS_token()
    # useJWTEncodeDecodeHandler()





