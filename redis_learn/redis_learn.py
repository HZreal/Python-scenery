

# Redis可视化桌面工具    https://github.com/FuckDoctors/rdm-builder/releases
#  RESP.app使用说明文档       https://docs.resp.app/en/latest/quick-start/
import redis

if __name__ == '__main__':
    # 在连接/获取外接资源的时候一定要注意使用try     !!!
    try:
        # r = redis.Redis(host='192.168.94.131', port=6379, db=0)   # 参数可不写，默认

        # password仅在redis配置了requirepass时使用，无需用户名   https://redis.io/commands/AUTH
        # username仅在redis6.0版本以后且设置ACL时才使用        https://redis.io/topics/acl
        r = redis.Redis(host='192.168.197.129', port=6379, db=0, password='root123456')
    except Exception as e:
        print(e)

    # 操作语句
    result = r.set('names', 'huangzhens')
    print(result)

    # 获取
    name = r.get('names')
    print(name)

# ResponseError: DENIED Redis is running in protected mode because protected mode is enabled, no bind address was specified, no authentication password is requested to clients.












