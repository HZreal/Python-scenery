import etcd3
import time
client = etcd3.client('192.168.1.7', 2379)

# 创建租约
my_lease = client.lease(ttl=30, lease_id=303030)  # id只能用数字表示

# 通过 id 打印租期的相关信息
lease_info = client.get_lease_info(303030)
print(lease_info)

# set 并指定租约
client.put('/test', '我只能存活30秒', lease=my_lease)



# time.sleep(5)
# my_lease.refresh()刷新
# list(client.refresh_lease(303030))

# lease_info = client.get_lease_info(303030)
# print(lease_info)
