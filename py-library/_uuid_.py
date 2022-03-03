import uuid

u1 = uuid.uuid1()
u3 = uuid.uuid3(namespace=u1, name='salt')
u4 = uuid.uuid4()
u5 = uuid.uuid5(namespace=u1, name='salt')

print(str(u1))
print(str(u3))
print(str(u4))
print(str(u5))

# print(uuid.uuid4().hex[: 8])








