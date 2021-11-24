
from rediscluster import RedisCluster

if __name__ == '__main__':
    # 组织集群的host和端口
    nodes = [{'host': '192.168.94.131', 'port': '7000'},
             {'host': '192.168.94.131', 'port': '7001'},
             {'host': '192.168.94.131', 'port': '7002'}]

    try:
        # 构建RedisCluster对象
        src = RedisCluster(startup_nodes=nodes, decode_responses=True)
        name1 = src.get('name')
        print(name1)
        result = src.set('name', 'liu')
        print(result)
    except Exception as e:
        print(e)
    name2 = src.get('name')
    print(name2)



















































