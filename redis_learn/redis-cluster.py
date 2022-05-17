# redis集群
# 一般至少6个节点，其中3个主节点，3个从节点
# 集成了哨兵，主节点宕机时自动故障转移

from rediscluster import RedisCluster


# redis集群的某几个节点
nodes = [
    {'host': '192.168.94.131', 'port': '7000'},
    {'host': '192.168.94.131', 'port': '7001'},
    {'host': '192.168.94.131', 'port': '7002'}
]


def redis_cluster():


    try:
        # 构建RedisCluster对象
        rc = RedisCluster(startup_nodes=nodes, decode_responses=True)
    except Exception as e:
        print(e)

    # RedisCluster对象当做普通redis连接操作即可
    result = rc.set('name', 'liu')
    print(result)
    name = rc.get('name')
    print(name)



if __name__ == '__main__':
    redis_cluster()



















































