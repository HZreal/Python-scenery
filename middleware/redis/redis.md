#Redis

## 介绍

redis客户端命令官方文档：https://redis.io

redis是单进程单线程运行

## 下载安装配置

* /usr/local/redis/redis.conf    安装路径
* /etc/redis/                   复制到的路径

当前终端窗口启动默认本机redis服务器

    redis-server
    redis-server &     后台启动服务
    sudo redis-server /etc/redis/redis.conf  指定加载配置文件

查看redis服务器进程

    ps aux | grep redis
    lsof -i :6379
    netstat -tunlp

关闭redis服务

    sudo kill -9 pid 

连接本机redis客户端

    redis-cli     
    redis-cli -h 192.168.26.128 -p 6379  指定ip、port

数据库没有名称，默认有16个，通过0-15来标识，连接redis默认选择第一个数据库

    select 0

设置过期时间(对所有类型通用)

    expire key seconds 

## redis数据类型

### String类型   

一个数据最多512M

    set key value   插入/更新（修改）
    get key   获取
    del key  删除

    setex key seconds value 设置过期时间(只对字符串类型有效)  主要是set、exprire合并，省得先set后再expire
    set name 100 Tom
    ttl key   查看过期时间  返回值若为-1，表示一直存在
    ttl name  查看剩余过期时间

    mset key1 value1 key2 value2 ...    设置多个
    mset addr Beijing like soccer
    mget key1 key2   得到多个
    mget sddr like

    append --------在key对应的value后追加
    append name lalalala  返回的是数据长度

    keys *   查看所有key
    keys a*   查看以a开头的key

    exists key  查看key是否存在
    type key  查看key类型


### Hash类型

用于存储对象，对象的结构为属性，值(类型为string)

    hset key field value      设置一个hash结构
    例如：hset person name huangzhen
    hmset key field1 value1 field2 value2 ...
    例如：hmset person name huangzhen age 22 address Beijing
    type key                        查看类型 -> hash
    hget key field                  获取key中某个field的值
    hget key                        会报错，用hgetall即可
    hgetall key                     获得key中所有field和value
    hmget key field1 field2         获取key中部分field对应的value
    hkeys key                       获得key中所有field
    hvals key                       获得key中所有value
    del key                         全部删除
    hdel key field1                 删除key里面某一个field及其value

ps: 用户购物车类型为hash类型



### List类型

（元素有序可重复） 元素类型为string

    lpush key value  左插
    rpush key value  右插
    例如：lpush class zhangsan       返回的是里面有几个元素
    例如：rpush class  wangwu

    lrange key start stop           获取从下标start到下标stop的数据
    例如：lrange class 0 0           获取从下标0到下标0的数据
    例如：lrange class 0 1
    例如：lrange class 0 -1          获取所有的数据
    ltrim key start stop            截取从start到stop的元素，即切片

    lrem key count value 从左边移除      count为0即删除所有等于value的数据，count>0即从表头开始删除count个等于value的数据，count<0即从表尾开始删除count个等于value的数据

    lset key i new_data    设置key中下标索引为i的数据为new_data
    linsert key before/after old_value new_value        在key里old_value之前/之后插入new_value




### set类型

（元素无序不重复） 元素为string 没有修改操作！  

    sadd key member1 member2 ...   添加数据
    smembers key                   获取所有
    srem key member1               删除某个member
    sismember                      判断某个数据是否在集合中

查看元素是否在set中的速度O(1)比在list中的速度O(n)更快


### zset类型

（权重有序不重复） 元素为string  元素唯一不重复，有序  没有修改操作！

每个元素都会关联一个double类型的score，表示权重，通过权重自动将元素从小到大排序，权重可以重复，权重相同时按照元素值的字母排序

    zadd key score member                        在key中添加权重为score的member
    zadd key score1 member1 score2 member2 score3 member3 ...

    zrange key start stop                        查看获取从下标start到下标stop的数据，
    zrangebyscore key min max                    获取权重在min到max之间的数据

    zscore key member                            返回某个member的权重score
    zmscore key member1 member2 member3 ...      返回多个member的权重score1 score2 ...

    zrem key member1 member2 ...                 根据成员名删除
    zremrangebyscore key min max                 根据权重删除权重范围在min到max之间的


## Redis的 C - S 架构：

* 基于客户端-服务端模型以及请求/响应协议的TCP服务。
* 客户端向服务端发送一个查询请求，并监听Socket返回。
* 通常是以阻塞模式，等待服务端响应。
* 服务端处理命令，并将结果返回给客户端

存在的问题：
* 如果Redis服务端需要同时处理多个请求，加上网络延迟，那么服务端利用率不高，效率降低。

解决的办法
* 管道pipeline
  * 可以一次性发送多条命令并在执行完后一次性将结果返回。
  * pipeline通过减少客户端与Redis的通信次数来实现降低往返延时时间。
  * 实现的原理(队列)
    * Client可以将三个命令放到一个tcp报文一起发送。
    * Server则可以将三条命令的处理结果放到一个tcp报文返回。
    * 队列是先进先出，这样就保证数据的顺序性。


## Redis 事务

### 基本事务指令

Redis提供了一定的事务支持，可以保证一组操作原子执行不被打断，但是如果执行中出现错误，事务不能回滚，Redis未提供回滚支持。
* multi 开启事务
* exec 执行事务

使用multi开启事务后，操作的指令并未立即执行，而是被redis记录在队列中，等待一起执行。当执行exec命令后，开始执行事务指令，最终得到每条指令的结果。


      127.0.0.1:6379> multi
      OK
      127.0.0.1:6379> set a 100
      QUEUED
      127.0.0.1:6379> set b 200
      QUEUED
      127.0.0.1:6379> get a
      QUEUED
      127.0.0.1:6379> get b
      QUEUED
      127.0.0.1:6379> exec
      1) OK
      2) OK
      3) "100"
      4) "200"


如果事务中出现了某条指令错误，事务并不会终止执行，而是会记录下这条错误的信息，并继续执行后面的指令。所以事务中出错不会影响后续指令的执行。

### Python客户端操作redis事务

在Redis的Python 客户端库redis-py中，提供了pipeline (称为流水线 或 管道)，该工具的作用是：
* 在客户端统一收集操作指令
* 补充上multi和exec指令，当作一个事务发送到redis服务器执行

### watch监视

正是因为redis事务无法回滚，在执行遇错也不会停止后续的执行，于是提供了watch机制补足

当构建的redis事务在执行时依赖某些数据，可以使用watch对该数据值进行监视。
* 事务exec执行前，被监视的stock值未变化，事务正确执行。
* 若有变化(其他地方改动)，则事务不执行。

简之，开启watch监听后，事务执行前会先判断监听的数据是否变化，无改变则执行。原理与乐观锁一致

使用方法: 在开启事务(multi)之前，监听某个key，即

    watch key

注意：Redis Cluster 集群不支持事务


## Redis 持久化

edis可以将数据写入到磁盘中，在停机或宕机后，再次启动redis时，将磁盘中的备份数据加载到内存中恢复使用。这是redis的持久化。持久化有如下两种机制。

### RDB 快照持久化

redis可以将内存中的数据写入磁盘进行持久化。在进行持久化时，redis会创建子进程来执行。

redis默认开启了快照持久化机制。

进行快照持久化的时机如下

* 定期触发

  在redis.conf配置文件中snapshot部分，save seconds count可设置触发的频次

* BGSAVE

  执行 BGSAVE 命令，手动触发RDB持久化，生产全量的RDB文件

* SHUTDOWN

  关闭redis时触发

### AOF 追加文件持久化

redis可以将执行的所有指令追加记录到文件中持久化存储，默认未开启。

可以通过redis.conf如下项开启AOF机制

    appendonly yes  # 是否开启AOF
    appendfilename "appendonly.aof"  # AOF文件

AOF机制记录操作触发的时机，或者说同步文件策略(过于频繁会影响性能)

    # appendfsync always    # 每个操作都写到磁盘中
    appendfsync everysec    # 每秒写一次磁盘，默认
    # appendfsync no        # 由操作系统决定写入磁盘的时机，redis不保证

使用AOF机制的缺点是随着时间的流逝，AOF文件会变得很大。但redis可以压缩AOF文件(配置文件中设置)。


### RDB、AOF结合使用

redis允许我们同时使用两种机制，通常情况下我们会设置AOF机制为everysec 每秒写入，则最坏仅会丢失一秒内的数据。

## Redis 高可用

为了保证redis最大程度上能够使用，redis提供了主从同步+Sentinel哨兵机制。

### Sentinel 哨兵

https://redis.io/topics/sentinel

redis提供的哨兵机制是用来监护redis实例进程的，可以自动进行故障转移，其功能如下
* Monitoring: 不间断检查主从节点是否正常运行(心跳机制)
* Notification: 发现节点问题，会通过API通知系统管理或者另一个进程(这些应用注册了通知事件)
* Automatic failover: 如果主节点出问题，Sentinel可以启动一个故障转移进程，使某个从节点被提升为主节点，其他从节点被重新配置使用新的主节点，同时告知使用Redis服务的应用程序在连接redis时的新地址，当原主节点修复完成后将自动降级为从节点。
* Configuration provider: Sentinelc充当客户端服务发现的授权源: 客户端连接Sentinel是为了获取当前可用的Redis主节点的地址。如果发生故障转移，sentinel将报告新的地址

redis安装后，会自带sentinel哨兵程序(与redis-server命令同目录)，修改sentinel.conf配置文件:

    bind 127.0.0.1  
    port 26380
    daemonize yes
    logfile /var/log/redis-sentinel.log
    sentinel monitor cluster_name 127.0.0.1 6380 2      
    sentinel down-after-milliseconds cluster_name 30000         心跳频率，超过30000毫秒则判定节点故障
    sentinel parallel-syncs cluster_name 1
    sentinel failover-timeout cluster_name 180000               判断故障发生到实际进行故障转移的时间缓冲，因为故障有可能是临时的网络问题而非节点本身故障，若超过这个时间则认定是真故障，进行故障转移

sentinel monitor cluster_name 127.0.0.1 6380 2 表示说明如下，
* cluster_name 为定义的sentinel监护的redis主从集群名称，客户端连接哨兵访问时会用到
* 127.0.0.1 6300 为主从中任一台机器地址，哨兵会自动获取到其他节点信息
* 2 表示有两个以上的sentinel程序判定某台redis宕机后，才会进行自动故障转移。这个数目一般是哨兵数量一半以上

启动哨兵方式：

    redis-sentinel sentinel.conf

由于哨兵是客户端与redis集群连接的桥梁，同时保证高可用，则
* 至少搭建三个以上的sentinel程序，防止单个哨兵挂掉影响所有的服务
* 且sentinel程序要分布式运行在不同的机器上


### Python客户端使用哨兵

python客户端只需要与哨兵程序通讯，获取主节点地址即可

    # redis 哨兵
    REDIS_SENTINELS = [
        ('127.0.0.1', '26380'),
        ('127.0.0.1', '26381'),
        ('127.0.0.1', '26382'),
    ]
    REDIS_SENTINEL_SERVICE_NAME = 'mymaster'
    
    from redis.sentinel import Sentinel
    _sentinel = Sentinel(REDIS_SENTINELS)
    redis_master = _sentinel.master_for(REDIS_SENTINEL_SERVICE_NAME)
    redis_slave = _sentinel.slave_for(REDIS_SENTINEL_SERVICE_NAME)

使用示例

    # 读数据，master读不到去slave读
    try:
        real_code = redis_master.get(key)
    except ConnectionError as e:
        real_code = redis_slave.get(key)
    
    # 写数据，只能在master里写
    try:
        current_app.redis_master.delete(key)
    except ConnectionError as e:
        logger.error(e)



## Redis 集群

### 基本描述

文档：https://redis.io/topics/partitioning

Reids Cluster集群方案，内部已经集成了sentinel机制来做到高可用。

redis主从只能是一主多从，但是从节点可以当做另一台从节点的主

注意：
* redis cluster 不支持事务
* redis cluster 不支持多键操作，如mset

常用查看信息命令：
* 命令 info                查看当前节点信息、运行状态等
* info replication        查看当前节点主从信息
* info memory             查看节点占用内存信息
* info stats              查看节点状态

### 分片

分片集群特征：
* 集群中有多个master，每个master保存不同数据
* 每个master都可以有多个slave节点
* master之间通过ping监测彼此健康状态

Redis实例的增加或者移除很方便，不需要暂停所有Redis实例服务

客户端请求可以访问集群任意节点，最终根据散列插槽都会被转发到正确节点

#### 散列插槽

Redis会把每一个master节点映射到0~16383共16384个插槽（hash slot）上

数据key不是与节点绑定，而是与插槽绑定。redis会根据key的有效部分计算插槽值，分两种情况：
* key中包含"{}"，且“{}”中至少包含1个字符，则“{}”中的部分是有效部分
* key中不包含“{}”，则整个key都是有效部分

例如：key是num，那么就根据num计算，如果是{gangya}num，则根据gangya计算。

计算方式是利用CRC16算法得到一个hash值，然后对16384取余，得到的结果就是slot值。

Redis如何判断某个key应该在哪个实例？
* 将16384个插槽分配到不同的实例
* 根据key的有效部分计算哈希值，对16384取余
* 余数作为插槽，寻找插槽所在实例即可

如何将同一类数据固定的保存在同一个Redis实例？
* 这一类数据使用相同的有效部分，例如key都以{typeId}为前缀

### 搭建redis集群

* 命令 slaveof host port，指定当前节点为某个host:port的从节点
* 配置文件创建redis服务时，修改slaveof <masterip> <masterport>

### 集群伸缩

redis-cli提供了很多操作集群的命令，可以通过redis-cli --cluster help查看

需求：向集群中添加一个新的master节点，并向其中存储 num = 10
* 启动一个新的redis实例，端口为7004，假设原集群7001(Master)、7002(Slave1)、7003(Slave2)
* 添加7004到之前的集群，并作为一个master节点
* 给7004节点分配插槽，使得num这个key可以存储到7004实例，此时会将部分插槽分配到新插槽

1. 创建redis实例
   * 配置文件7004.conf并修改
   * 启动reids
2. 添加新节点到redis集群
   * 执行集群添加节点命令
   
         redis-cli --cluster add-node new_host:new_port existing_host:existing_port
   * 查看集群状态，可看到7004加入了集群，并且默认是一个master节点
   
         redis-cli -p 7001 cluster nodes
   * 但是，也可以看到7004节点的插槽数量为0，因此没有任何数据可以存储到7004上，于是需要转移插槽
3. 转移插槽

   要将num存储到7004节点，因此需要先看看num的插槽是多少，执行：

       get num
       输出redirected to slot [2765] located at ...... : ....，即num的插槽为2765

   可以将0~3000的插槽从7001转移到7004，命令格式如下：

       redis-cli --cluster reshard host:port
   然后设置移动的槽数，设置接收的node(即7004)，设置槽数从哪里移出，如all表示从原集群所有节点中各转移一部分，最后确认转移

### 故障转移

#### 自动故障转移

当集群中有一个master宕机会发生什么? 不妨直接停止一个redis(7002)实例，shutdown命令：

    redis-cli -p 7002 shutdown

1）首先是该实例与其它实例失去连接

2）然后是疑似宕机(因为实际情况中有可能是因为网络问题，而非redis本身故障，后面会恢复网络连接)

3）最后是确定下线(超时时间已过)，自动提升一个slave为新的master

4）当7002再次启动，就会变为一个slave节点了

#### 手动故障转移

利用cluster failover命令可以手动让集群中的某个master宕机，切换到执行cluster failover命令的这个slave节点，实现无感知的数据迁移

这种failover命令可以指定三种模式：
* 缺省：默认的流程，如图Manual_failover.png中  1~6歩
* force：省略了对offset的一致性校验
* takeover：直接执行第5歩，忽略数据一致性、忽略master状态和其它master的意见

案例需求：在7002这个slave节点执行手动故障转移，重新夺回master地位，步骤如下：
* redis-cli连接7002这个节点
* 执行cluster failover命令

###  RedisTemplate访问分片集群

RedisTemplate底层同样基于lettuce实现了分片集群的支持，而使用的步骤与哨兵模式基本一致：
* 1）引入redis的starter依赖
* 2）配置分片集群地址
* 3）配置读写分离

与哨兵模式相比，其中只有分片集群的配置方式略有差异

### Python客户端连接redis集群

    # redis 集群
    REDIS_CLUSTER = [
        {'host': '127.0.0.1', 'port': '7000'},
        {'host': '127.0.0.1', 'port': '7001'},
        {'host': '127.0.0.1', 'port': '7002'},
    ]
    
    from rediscluster import StrictRedisCluster
    redis_cluster = StrictRedisCluster(startup_nodes=REDIS_CLUSTER)
    
    # 可以将redis_cluster就当作普通的redis客户端使用
    redis_master.delete(key)

## Redis单线程

Redis单线程优势：
* 避免线程切换和竞争产生的消耗
* 避免同步机制的开销
* 实现简单，底层数据结构的设计无需考虑线程安全

Redis6.0版本引入了多线程的目的是解决Redis在网络 I/O 上的性能瓶颈

## 用途

### 缓存

### 持久存储
* 数据库的统计冗余字段 放到 redis中保存




## 相关补充
* https://redis.io/documentation
* 《Redis实践》 （Redis in action)



