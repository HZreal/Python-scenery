import etcd3
client = etcd3.client('192.168.1.7', 2379)

# 返回一个事件迭代器和一个取消触发器
iterators, cancel = client.watch('/name')
for event in iterators:
    print(event.value.decode())

