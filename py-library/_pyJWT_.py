import jwt
# doc:  https://pyjwt.readthedocs.io/en/stable/
# 将字典转换成JWT token字符串


payload = {'username': 'huang', 'password': '123456'}
key = 'secret'
algorithm='HS256'


# 将载荷转为jwt串
jwt_str = jwt.encode(payload=payload, key=key, algorithm=algorithm)
print('Token --------', jwt_str)


# 将jwt串还原为原始载荷
payload_ = jwt.decode(jwt_str, key=key, algorithms=[algorithm])
print('origin payload -------', payload_)



print(payload == payload_)    # True
