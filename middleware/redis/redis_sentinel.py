# redis哨兵

# redis提供的哨兵机制是用来监护redis实例进程的，可以自动进行故障转移，其功能如下
#     * Monitoring: 不间断检查主从节点是否正常运行(心跳机制)
#     * Notification: 发现节点问题，会通过API通知系统管理或者另一个进程(这些应用注册了通知事件)
#     * Automatic failover: 如果主节点出问题，Sentinel可以启动一个故障转移进程，使某个从节点被提升为主节点，其他从节点被重新配置使用新的主节点，同时告知使用Redis服务的应用程序在连接redis时的新地址，当原主节点修复完成后将自动降级为从节点。
#     * Configuration provider: Sentinelc充当客户端服务发现的授权源: 客户端连接Sentinel是为了获取当前可用的Redis主节点的地址。如果发生故障转移，sentinel将报告新的地址



from redis import sentinel
import logging

logger = logging.Logger('sentinel')

# 哨兵集群
REDIS_SENTINELS = [
    ('127.0.0.1', '26379'),
]

# 哨兵所连接的redis集群名称，在哨兵的配置文件中指定，与这里保持一致
REDIS_SENTINEL_SERVICE_NAME = 'mymaster'


def run():
    # 创建Sentinel哨兵
    _sentinel = sentinel.Sentinel(REDIS_SENTINELS)

    # 获取master节点连接
    redis_master_client = _sentinel.master_for(REDIS_SENTINEL_SERVICE_NAME)
    # 获取slave节点连接
    redis_slave_client = _sentinel.slave_for(REDIS_SENTINEL_SERVICE_NAME)

    key = 'sentinel_key'

    # 写数据，只能在master里写
    try:
        redis_master_client.set(key, 'hello world')
    except ConnectionError as e:
        logger.error(e)

    # 读数据，master读不到可以去slave读
    try:
        ret = redis_master_client.get(key)
    except ConnectionError as e:
        ret = redis_slave_client.get(key)
    print(ret)




if __name__ == '__main__':
    run()


