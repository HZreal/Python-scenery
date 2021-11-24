
import redis

if __name__ == '__main__':
    # 在连接/获取外接资源的时候一定要注意使用try     !!!
    try:
        r = redis.Redis(host='192.168.94.131', port=6379, db=0)   # 参数可不写，默认
        # r = redis.Redis(host='192.168.94.131', port=6379, db=0)   # 参数可不写，默认
    except Exception as e:
        print(e)

    # 操作语句
    result = r.set('name', 'huangzhen')
    print(result)

    # 获取
    name = r.get('name')
    print(name)

# ResponseError: DENIED Redis is running in protected mode because protected mode is enabled, no bind address was specified, no authentication password is requested to clients.












