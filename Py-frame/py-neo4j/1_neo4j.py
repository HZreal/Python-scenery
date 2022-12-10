# https://neo4j.com/docs/api/python-driver/4.4/api.html

from neo4j import GraphDatabase, Auth, Query, Bookmark, Transaction, Result, Record
from neo4j import WRITE_ACCESS, READ_ACCESS, DEFAULT_DATABASE, TRUST_ALL_CERTIFICATES, TRUST_SYSTEM_CA_SIGNED_CERTIFICATES
from neo4j.graph import Graph, Node, Relationship, Path
from neo4j.exceptions import Neo4jError, DriverError, TransactionError, SessionExpired, CypherTypeError, CypherSyntaxError, AuthError, DatabaseError

username = 'neo4j'
password = '123456'

# 自定义解析器
def custom_resolver(socket_address):
    if socket_address == ("example.com", 9999):
        yield "::1", 7687
        yield "127.0.0.1", 7687
    else:
        from socket import gaierror
        raise gaierror("Unexpected socket address %r" % socket_address)
# transaction_function
def do_cypher_tx(tx, cypher):
    result = tx.run(cypher)
    values = []
    for record in result:
        values.append(record.values())
    return values
def get_two_tx(tx):
    result = tx.run("UNWIND [1,2,3,4] AS x RETURN x")
    values = []
    for ix, record in enumerate(result):
        if ix > 1:
            break
        values.append(record.values())
    info = result.consume()  # discard the remaining records if there are any
    # use the info for logging etc.
    return values
def create_node_tx(tx, name):
    result = tx.run("CREATE (n:NodeExample { name: $name }) RETURN id(n) AS node_id", name=name)
    record = result.single()
    return record["node_id"]


uri = 'bolt://127.0.0.1:7687'
# Available valid URIs:
#   bolt://example.com:7687                                   无加密的BoltDriver
#   bolt+ssc://example.com:7687                               加密的BoltDriver，接受自签名证书
#   bolt+s://example.com:7687                                 加密的BoltDriver，仅接受由证书颁发机构签署的证书），完整的证书检查
#   neo4j://example.com:7687[?routing_context]                无加密的Neo4jDriver
#   neo4j+ssc://example.com:7687[?routing_context]            加密的Neo4jDriver，接受自签名证书
#   neo4j+s://example.com:7687[?routing_context]              加密的Neo4jDriver，仅接受由证书颁发机构签署的证书），完整的证书检查


# auth 是 class neo4j.Auth 的实例
# auth = Auth(scheme='', principal=None, credentials=None, realm=None, **{})        # 参数：scheme：身份验证类型,例如：“basic”、“kerberos”
# auth = Auth("basic", "neo4j", "password")
auth = (username, password)



driver_config = {
    'connection_timeout': 30.0,                                 # 等待建立 TCP 连接的最长时间
    'connection_acquisition_timeout': 60.0,                     # 连接池请求连接时会话将等待的最长时间,确保大于connection_timeout
    'encrypted': False,                                         # 是否在驱动程序和服务器之间使用加密连接
    'keep_alive': False,                                        # 是否应启用 TCP keep-alive
    'max_connection_lifetime': 3600,                            # 池中删除之前，驱动程序将保持连接的最长时间
    'max_connection_pool_size': 100,                            # 连接池集群节点允许的最大连接总数
    'max_transaction_retry_time': 30.0,                         # 托管事务在失败前重试的最长时间
    'resolver': custom_resolver,                                # 自定义解析器功能，用于在 DNS 解析之前解析主机和端口值，返回 2 元组 (host, port) 的可迭代对象
    'trust': TRUST_SYSTEM_CA_SIGNED_CERTIFICATES,               # 如何确定加密证书的真实性
    'user_agent': '',                                           # 指定客户端代理名称
}
driver = GraphDatabase.driver(uri=uri, auth=auth, **driver_config)                # 返回 Neo4jDriver or BoltDriver 对象 取决于 uri scheme


# session配置
session_config = {
    'database': DEFAULT_DATABASE,                               # 要查询数据库的名称, 最好指定，使驱动程序不必首先解析主数据库，从而更高效查询
    'bookmarks': (),                                            # 迭代器
    'fetch_size': 1000,                                         # 返回结果数量
    'default_access_mode': WRITE_ACCESS,                        # 访问模式  READ_ACCESS or WRITE_ACCESS
    'impersonated_user': 'alice'                                # 模拟用户的名称， 即此会话中的所有操作在一个模拟的安全管理器中，此模拟用户需要有适当权限
}
session = driver.session(**session_config)
# 通常session会频繁创建使用销毁，可用上下文管理器实现，自动提交事务
# with driver.session() as session:
#     result = session.run("MATCH (a:Person) RETURN a.name AS name")


# session方法
# 执行cypher  参数query是一个 neo4j.Query 对象
# query = Query(text='MATCH (o:Order)-[rel:CONTAINS]->(p:Product) RETURN p, rel, o LIMIT 50;', metadata={}, timeout=30)
query = 'MATCH (o:Order)-[rel:CONTAINS]->(p:Product) RETURN p, rel, o LIMIT 50;'
result = session.run(query=query, parameters={})                # 返回 neo4j.Result 对象 , 下述详解


# 返回上次事务结束时的书签(游标) neo4j.Bookmark 对象
bookmark = session.last_bookmark()


# 在session内创建一个非托管事务, 返回事务实例 neo4j.Transaction
unmanaged_tx = session.begin_transaction(metadata={}, timeout=10)
with session.begin_transaction() as tx:
    pass


# 读取事务
values_ = session.read_transaction(do_cypher_tx, 'RETURN 1 AS x')       # 自动提交，除非有异常
with driver.session() as session:
    values = session.read_transaction(get_two_tx)


# 写入事务
values__ = session.write_transaction(transaction_function=do_cypher_tx)
with driver.session() as session:
    node_id = session.write_transaction(create_node_tx, "example")


# session.close()



# 事务Transaction 有三种：
# Auto-commit transactions           自动提交事务
# Explicit Transactions              显示事务
# Managed Transactions               托管事务
tx_ = Transaction(connection=DEFAULT_DATABASE, fetch_size=1000)
tx_.run(query='')
tx_.commit()
tx_.rollback()
tx_.closed()                          # 判断事务是否关闭
tx_.close()



# 查询返回的结果  通常在执行Session.run() 或 Transaction.run() 中返回，为一个 neo4j.Result 实例
result.keys()
result.consume()
record = result.single()                   # 每次取下一条数据(记录)，直到取尽result中的所有数据，类似fetchone, 返回 neo4j.Record 对象，类似于字典的迭代器
result.peek()
graph = result.graph()                    # 返回图实例neo4j.graph.Graph， 包含result的所有的图对象
nodes = graph.nodes
relationships = graph.relationships
relationship = graph.relationship_type(name='')
result.value()
result.values()
result.data()                     # 返回结果的剩余data



# Record     neo4j.Record 类似于字典的迭代器，
record_obj = result.single()
record_obj.data()
# 适用于字典的操作
record_obj.get('key')
record_obj.keys()
record_obj.values()
record_obj.items()






driver.close()
