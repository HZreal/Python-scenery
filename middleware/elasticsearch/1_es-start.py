import random
from datetime import datetime
from elasticsearch import Elasticsearch

# doc: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html


es = Elasticsearch()  # 默认连接本机
# es = Elasticsearch(['192.168.200.228:9200'], ignore=400)
# es = Elasticsearch(
#     # 连接集群
#     # ["192.168.1.10:9200", "192.168.1.11:9200", "192.168.1.12"],     # 以列表的形式存放各节点的IP
#     [{'host': '127.0.0.1'}, {'host': '192.168.200.228', 'port': 9200, 'url_prefix': 'es', 'use_ssl': True}],   # 节点详细
#
#     # 动态连接
#     sniff_on_start=True,                                       # 连接前测试
#     sniff_on_connection_fail=True,                             # 节点无响应时刷新节点
#     sniff_timeout=60,                                          # 设置超时时间
#
#     http_auth=('elastic', 'changeme'),                         # 认证信息
#
#     # ssl连接
#     use_ssl=True,                                             # 打开SSL
#     verify_certs=True,                                        # 确保我们验证了SSL证书（默认关闭）
#     ca_certs='/path/to/CA_certs',                             # 提供CA证书的路径
#     client_cert='/path/to/clientcert.pem',                    # PEM格式的SSL客户端证书
#     client_key='/path/to/clientkey.pem'                       # PEM格式的SSL客户端密钥
#
# )


# 集群基本信息
# info = es.info()
# print(info)


# es.index(index, body, doc_type=None, id=None, params=None, headers=None)
# doc = {
#     'author': 'huang',
#     'text': 'hello world',
#     'timestamp': datetime.now(),
# }
# 在某个index中创建/更新文档
# res = es.index(index='test', doc_type='_doc', id=1, body={'name': 'huang', 'age': 22})
# print('res-------', res)
# print('操作方式-------', res['result'])


# es.indices
# es.indices.add_block(index, block, params=None, headers=None)
# es.indices.clone(index, target, body=None, params=None, headers=None)
# es.indices.create(index, body=None, params=None, headers=None)
# es.indices.close(index, params=None, headers=None)
# es.indices.delete(index, params=None, headers=None)
# es.indices.exist(index, params=None, headers=None)
# es.indices.flush(index, params=None, headers=None)
# es.indices.freeze(index, params=None, headers=None)
# es.indices.get(index, params=None, headers=None)
# es.indices.get_mapping(index, doc_type=None, params=None, headers=None)
# es.indices.get_settings(index=None, name=None, params=None, headers=None)
# es.indices.get_template(name=None, params=None, headers=None)
# es.indices.refresh(index="test-index")


# 查询es.search(index, body, doc_type, _source, _source_excludes, _source_includes, scroll)
# index：表名。es的结构只有表没有库，index就类似于mysql的表名，指定需要查询的数据表
# body：查询体。就是es的查询语句，使用DSL语句，相比SQL语句要复杂得多，但是基本逻辑其实是类似的
# _source – 指示为匹配文档返回哪些源字段。这些字段在搜索响应的 hits._source 属性中返回
# scroll：游标有效期 。指定了这个参数之后，会启用scroll方法，用于批量获取数据。"20m"代表scroll游标的有效期为20分钟
# request_timeout：超时等待时间 。20表示20秒没有响应，会终止查询并报错
# size：返回大小 。返回结果的长度，10000表示查询最大返回10000条记录，超出的结果不会返回。单次查询最大长度为10000，设置太大了会报错。当查询的结果比较多的时候，还是得用scroll方法


# res = es.search(index="test-index", query={"match_all": {}})
# print('返回结果的总条数:', res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print(hit["_source"])                                        # {'author': 'kimchy', 'text': 'Elasticsearch: cool. bonsai cool.', 'timestamp': '2021-12-12T18:22:56.241947'}
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

# res = es.search(index="customers", query={"match_all": {}})
# print("Got Hits:", res['hits'])
# print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print(hit['_source'])


# 批量操作
# 允许在单个请求中执行多个索引/更新/删除操作。
# es.bulk(body, index=None, doc_type=None, params=None, headers=None)


# 返回匹配查询的文档数。
# es.count()

# 在索引中创建一个新文档
# res = es.create('test', 2222, body={'g_name': 'apple', 'num': 3})       # 当索引中文档id已存在时，返回409
# print(res)

# 文档是否存在于索引中
# is_existed = es.exists('index4', 1)
# print(is_existed)

# 获取一个文档，返回查询结果，文档源数据包含在内
# query_res = es.get(index="index4", id=1)
# print('get doc by id in index ---->  ', query_res['_source'])

# 获取查询的文档源数据
# source_doc = es.get_source('test', 2)
# print(source_doc)

# 从索引中删除文档
# res = es.delete('test', 2)

# 一个请求查询多个文档
mul_doc = es.mget(body={'ids': [1, 2]}, index='index4')
print(mul_doc)

# Allows to execute several search operations in one request.
# es.msearch(body, index=None, doc_type=None, params=None, headers=None)


# Returns whether the cluster is running.
# es.ping(params=None, headers=None)


# 允许将文档从一个索引复制到另一个索引，可选择通过查询过滤源文档、更改目标索引设置或从远程集群获取文档
# es.reindex(body, params=None, headers=None)


# scroll游标
# 允许从单个搜索请求中检索大量结果。
# es.scroll(body=None, scroll_id=None, params=None, headers=None)

# Updates a document with a script or partial document.
# es.update(index, id, body, doc_type=None, params=None, headers=None)


# es实例的 cluster 属性
# print('-------------------------------------------------------------')
# print('集群健康状态信息-------', es.cluster.health())
# print('当前连接的集群节点信息-------', es.cluster.client.info())
# print('获取集群的更多信息-------', es.cluster.state())

# es实例的 cat 属性得到更简单易读的信息
# print('-------------------------------------------------------------')
# print('health----', es.cat.health(), sep='\n')
# print('master----', es.cat.master(), sep='\n')
# print('nodes----', es.cat.nodes(), sep='\n')
# print('indices----', es.cat.indices(), sep='\n')
# print('count----', es.cat.count(), sep='\n')
# print('plugins----', es.cat.plugins(), sep='\n')
# print('templates----', es.cat.templates(), sep='\n')

# 快照
# es.snapshot

# es实例的 task 属性
# print('-------------------------------------------------------------')
# print('get----', es.tasks.get(), sep='\n')
# print('list----', es.tasks.list(), sep='\n')


# helpers是bulk的帮助程序，是对bulk的封装。有三种方式bulk（），streaming_bulk（），parallel_bulk（），
# 都需要接受Elasticsearch类的实例和一个可迭代的actions.actions里面的操作可以有多种
from elasticsearch import helpers

# helpers.bulk()
# helpers.streaming_bulk()
# helpers.parallel_bulk()
# helpers.scan()
# actions = []
# levels = ['info', 'debug', 'warn', 'error']
# for i in range(100):
#     level = levels[random.randrange(0, len(levels))]
#     action = {
#         '_op_type': 'index',  # 操作 index update create delete
#         '_index': 'log_level',  # index
#         '_type': 'doc',  # type
#         '_source': {'level': level}
#     }
#     actions.append(action)
# 使用bulk方式
# helpers.bulk(client=es, actions=actions)
# streaming_bulk与parallel_bulk类似  需要遍历才会运行
# 都可以设置每个批次的大小，parallel_bulk还可以设置线程数
# for ok, response in helpers.streaming_bulk(es, actions):
#     if not ok:
#         print(response)
