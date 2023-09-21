from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch, Match
from elasticsearch_dsl import Q

es = Elasticsearch(
    ['127.0.0.1:9200']
)

# query接收的是查询体语句
# exclude接收的是不匹配的字段 就像 must_not
# filter接收的是过滤语句 ，过滤的条件意思是在返回结果中有这些条件的信息
# 该Search对象代表整个搜索请求：
# 查询（queries）
# 过滤器（filters）
# 聚合（aggregations）
# 排序（sort）
# 分页（pagination）
# 附加的参数（additional parameters）
# 关联客户端（associated client）
# API 被设计为可链接的。除了聚合功能以外，这意味着Search对象是不可变的（对对象的所有更改都将导致创建（拷贝）一个包含更改的副本）。这意味着您可以安全地将Search对象传递给外部代码，而不必担心这个对象会被修改。

s = Search(
    using=es,
    index="logstash-2017.11.14"
).filter("match", Gy='20160521491').query("match", TransId='06100021650016153').exclude("match", message="M(")

# 请求发送到Elasticsearch
response = s.execute()
# 结果总数
s.count()
# response.hits.total










