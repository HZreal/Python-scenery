import etcd3

client = etcd3.client(host="192.168.1.7", port=2379)

# set
client.put("/name", "huang")

# get
v, path = client.get("/name")
print(v.decode("utf-8"))
print(path.key.decode())

