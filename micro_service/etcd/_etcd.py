import etcd3
# etcd3==0.12.0
# grpcio==1.44.0 , 版本1.45.0有点冲突

client = etcd3.client(host="192.168.1.7", port=2379, user='huang', password='Root123456')

# set
client.put("/name", "huang")

# get
v, path = client.get("/name")
print(v.decode("utf-8"))
print(path.key.decode())

