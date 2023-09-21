from elasticsearch import Elasticsearch

es = Elasticsearch(['127.0.0.1:9200'], ignore=400)

start = 0
size = 8
response = es.search(
    index="logstash-2017.11.14",  # 索引名
    body={  # 请求体
        "query": {  # 关键字，把查询语句给 query
            "bool": {  # 关键字，表示使用 filter 查询，没有匹配度
                "must": [  # 表示里面的条件必须匹配，多个匹配元素可以放在列表里
                    {
                        "match": {  # 关键字，表示需要匹配的元素
                            "TransId": '06100021650016153'  # TransId 是字段名， 06100021650016153 是此字段需要匹配到的值
                        }
                    },
                    {
                        "match": {
                            "Ds": '2017-05-06'
                        }
                    },
                    {
                        "match": {
                            "Gy": '2012020235'
                        }
                    }, ],
                "must_not": {  # 关键字，表示查询的结果里必须不匹配里面的元素
                    "match": {  # 关键字
                        "message": "M("  # message 字段名，这个字段的值一般是查询到的结果内容体。这里的意思是，返回的结果里不能包含特殊字符 'M('
                    }
                }
            }
        },

        # 下面是对返回的结果继续排序
        "sort": [{"@timestamp": {"order": "desc"}}],
        "from": start,  # 从匹配到的结果中的第几条数据开始返回，值是匹配到的数据的下标，从 0 开始
        "size": size  # 返回多少条数据
    }
)