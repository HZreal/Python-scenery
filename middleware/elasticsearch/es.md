# ElasticSearch

## 1.1.1. 介绍

Elasticsearch（ES）是一个基于Lucene构建的开源、分布式、RESTful接口的全文搜索引擎。

Elasticsearch还是一个分布式文档数据库，其中每个字段均可被索引，而且每个字段的数据均可被搜索，ES能够横向扩展至数以百计的服务器存储以及处理PB级的数据。可以在极短的时间内存储、搜索和分析大量的数据。通常作为具有复杂搜索场景情况下的核心发动机。



http通信端口 9200
tcp通信端口 9300

## 安装

Ubuntu:

Docker:



配置文件：/etc/elasticserach/elasticserach.yml

## 背景

1. 检索的业务需求很多，可以通过对数据库的模糊查询实现检索功能，但是针对大数据量的操作，基于数据库的检索就显得力不从心了（查询效率很低）

2. 需要寻求一种高效的数据检索解决方案

3. 所谓搜索引擎，就是根据用户需求与一定算法，运用特定策略从互联网检索出指定的信息反馈给用户的一门检索技术。搜索引擎依托于多种技术，如网络爬虫技术、检索排序技术、网页处理技术、大数据处理技术、自然语言处理技术等，为信息检索用户提供快速、高相关性的信息服务。搜索引擎技术的核心模块一般包括爬虫、索引、检索和排序等，同时可添加其他一系列辅助模块，以为用户创造更好的网络使用环境

4. 搜索方式是搜索引擎的一个关键环节，大致可分为四种：全文搜索引擎、元搜索引擎、垂直搜索引擎和目录搜索引擎，它们各有特点并适用于不同的搜索环境

## Lucene简介

参考：https://blog.csdn.net/qq_41484287/article/details/123825397

Lucene是Apache Jakarta家族中的一个开源项目，是一个开放源代码的全文检索引擎工具包，但它不是一个完整的 全文检索引擎，而是一个全文检索引擎的架构，提供了完整的查询引擎、索引引擎和部分文本分析引擎。

Lucene提供了一个简单却强大的应用程式接口，能够做全文索引和搜寻。在Java开发环境里Lucene是一个成熟的免费开源工具，是目前最为流行的基于 Java 开源全文检索工具包。

数据总体分为两种：

   * 结构化数据
   
     指具有固定格式或有限长度的数据，如数据库、元数据等
   
     对于结构化数据的全文搜索很简单，因为数据都是有固定格式的，例如搜索数据库中数据使用SQL语句即可

   * 非结构化数据
     
     指不定长或无固定格式的数据，如邮件、word文档等磁盘上的文件
   
     对于非结构化数据，有以下两种方法：
   
     * 顺序扫描法(Serial Scanning)
     
       如果要找包含某一特定内容的文件，对于每一个文档，从头到尾扫描内容，如果此文档包含此字符串， 则此文档为我们要找的文件，接着看下一个文件，直到扫描完所有的文件，因此速度很慢。
     
     * 全文检索(Full-text Search)
     
       将非结构化数据中的一部分信息提取出来，重新组织，使其变得具有一定结构，然后对此有一定结构的数 据进行搜索，从而达到搜索相对较快的目的。这部分从非结构化数据中提取出的然后重新组织的信息，我们称之索引。

Lucene全文检索流程:

* 创建索引过程，对要搜索的原始内容进行索引构建一个索引库。索引过程包括：确定原始内容即要搜索的内容→采集文档→创建文档→分析文档→索引文档。

* 搜索索引过程，从索引库中搜索内容。搜索过程包括：用户通过搜索界面→创建查询→执行搜索，从索引库搜索→ 渲染搜索结果。


## ElasticSearch vs Lucene的关系

简单一句话就是，成品与半成品的关系。

（1）Lucene专注于搜索底层的建设，而ElasticSearch专注于企业应用。

（2）Luncene是单节点的API，ElasticSearch是分布式的—为集群而生。

（3）Luncene需要二次开发，才能使用。不能像百度或谷歌一样，它只是提供一个接口需要被实现才能使用, ElasticSearch直接拿来用。

（4）Elasticsearch基于Lucene的，而Lucene底层是java实现



## 1.1.2. ES应用场景

* 当你经营一家网上商店，你可以让你的客户搜索你卖的商品。在这种情况下，你可以使用ElasticSearch来存储你的整个产品目录和库存信息，为客户提供精准搜索，可以为客户推荐相关商品。

* 当你想收集日志或者交易数据的时候，需要分析和挖掘这些数据，寻找趋势，进行统计，总结，或发现异常。在这种情况下，你可以使用Logstash或者其他工具来进行收集数据，当这引起数据存储到ElasticsSearch中。你可以搜索和汇总这些数据，找到任何你感兴趣的信息。

* 对于程序员来说，比较有名的案例是GitHub，GitHub的搜索是基于ElasticSearch构建的，在github.com/search页面，你可以搜索项目、用户、issue、pull request，还有代码。共有40~50个索引库，分别用于索引网站需要跟踪的各种数据。虽然只索引项目的主分支（master），但这个数据量依然巨大，包括20亿个索引文档，30TB的索引文件。

## 1.1.3. ES基本概念

* Near Realtime(NRT) 几乎实时

  Elasticsearch是一个几乎实时的搜索平台。意思是，从索引一个文档到这个文档可被搜索只需要一点点的延迟，这个时间一般为毫秒级

* Cluster 集群

  群集是一个或多个节点（服务器）的集合， 这些节点共同保存整个数据，并在所有节点上提供联合索引和搜索功能。

* Node节点

  节点是单个服务器实例，它是群集的一部分，可以存储数据，并参与群集的索引和搜索功能。

* Index索引

  索引是具有相似特性的文档集合。例如，可以为客户数据提供索引，为产品目录建立另一个索引，以及为订单数据建立另一个索引。索引由名称（必须全部为小写）标识，该名称用于在对其中的文档执行索引、搜索、更新和删除操作时引用索引。在单个群集中，你可以定义尽可能多的索引。

  索引是一个逻辑单元，ES中的数据实际上是存储在分片中的

* Type类型

  在索引中，可以定义一个或多个类型。类型是索引的逻辑类别/分区，其语义完全取决于你。一般来说，类型定义为具有公共字段集的文档。例如，假设你运行一个博客平台，并将所有数据存储在一个索引中。在这个索引中，你可以为用户数据定义一种类型，为博客数据定义另一种类型，以及为注释数据定义另一类型。

* Document文档

  文档是可以被索引的信息的基本单位。例如，你可以为单个客户提供一个文档，单个产品提供另一个文档，以及单个订单提供另一个文档。本文件的表示形式为JSON（JavaScript Object Notation）格式，这是一种非常普遍的互联网数据交换格式。

  在索引/类型中，你可以存储尽可能多的文档。请注意，尽管文档物理驻留在索引中，文档实际上必须索引或分配到索引中的类型。

* Shards & Replicas分片与副本

  索引可以存储大量的数据，这些数据可能超过单个节点的硬件限制。例如，十亿个文件占用磁盘空间1TB的单指标可能不适合对单个节点的磁盘或可能太慢服务仅从单个节点的搜索请求。

  为了解决这一问题，Elasticsearch提供细分你的指标分成多个块称为分片的能力。当你创建一个索引，你可以简单地定义你想要的分片数量。每个分片本身是一个全功能的、独立的“指数”，可以托管在集群中的任何节点。

  **Shards分片的重要性主要体现在以下两个特征**：

  1. 副本为分片或节点失败提供了高可用性。为此，需要注意的是，一个副本的分片不会分配在同一个节点作为原始的或主分片，副本是从主分片那里复制过来的。

  2. 副本允许用户扩展你的搜索量或吞吐量，因为搜索可以在所有副本上并行执行。

* ES基本概念与关系型数据库的比较

ES概念 | 关系型数据库
|:---: | :---:|
Index（索引）| 支持全文检索	Database（数据库）
Type（类型）| Table（表）
Document（文档）| 不同文档可以有不同的字段集合	Row（数据行）
Field（字段）| Column（数据列）
Mapping（映射）| Schema（模式）

## 1.1.4. ES 基本操作

| 请求方式 |                   REST请求                   |      功能描述      |
| :------: | :------------------------------------------: | :----------------: |
|   PUT    |          http://eshost:9200/index1           |     创建index      |
|   POST   |     http://eshost:9200/index/type/doc_id     |    添加document    |
|   POST   | http://eshost:9200/index/type/doc_id/_update |    修改document    |
|  DELETE  |     http://eshost:9200/index/type/doc_id     | 根据ID删除document |
|   GET    |     http://eshost:9200/index/type/doc_id     | 根据ID查询document |
|   POST   |    http://eshost:9200/index/type/_search     | 查询索引下所有数据 |


* 查看健康状态

  ```
  GET _cat/indices?v
  GET _cat/health?v
  ```
  or
  ```
  curl -X GET 127.0.0.1:9200/_cat/health?v
  ```

* 查询当前es集群中所有的indices

  ```
  curl -X GET 127.0.0.1:9200/_cat/indices?v
  ```

* 查询索引

  ```angular2html
  # 查询索引信息
  GET index
  
  # 查询索引的mappings信息
  GET index/_mappings
  
  # 查询索引的属性设置
  GET index/_settings
  ```

* 创建索引

  ```
  PUT index_name
  {
    "mappings": {            # 定义字段的存储类型、分词方式和是否存储等信息
      "properties": {
        "book_id":{
          "type":"long"       # 指定field类型
        },
        "book_name":{
          "type": "text"
        },
        "book_author":{
          "type": "keyword"
        },
        "book_price":{
          "type": "float"
        },
        "book_desc":{
          "type": "text"
        }
      }
    },
    "settings": {                # 设置索引的属性
      "number_of_shards": 2
    }
  }
  ```
  or
  ```
  curl -X PUT 127.0.0.1:9200/index
  ```

* 创建文档，插入记录到ES

  ```
  POST index3/_doc/101
  {
    "book_id":101,
    "book_name":"python",
    "book_author":"huang", 
    "book_price":22.22,
    "book_desc":"这是一本看了就会的python秘籍"
  }
   
  POST index3/_doc/102
  {
    "book_id":102,
    "book_name":"C++程序设计",
    "book_author":"谭浩强",
    "book_price":22.22,
    "book_desc":"C++程序设计中的名著"
  }
   
  POST index3/_doc/103
  {
    "book_id":103,
    "book_name":"SQL经典",
    "book_author":"zgper",
    "book_price":33.22,
    "book_desc":"SQL从入门到精通"
  }
  ```

  ```
  curl -H "ContentType:application/json" -X POST 127.0.0.1:9200/user/person -d '
      {
          "name": "LMH",
          "age": 18,
          "married": true
      }'
  ```

  也可以使用PUT方法，但是需要传入id

  ```
   curl -H "ContentType:application/json" -X PUT 127.0.0.1:9200/user/person/4 -d '
      {
          "name": "LMH",
          "age": 18,
          "married": false
      }'
  ```

* 修改文档：修改记录
  * 使用新增操作的请求覆盖原记录(不同则覆盖，没有则创建)
  
    ```
    POST index/type/doc_id     # 索引/类型/文档id
    {
      "book_id":103,
      "book_name":"Python",
      "book_author":"kk",
      "book_price":33.22,
      "book_desc":"Python从入门到放弃"
    }
    ```
  * 使用_update修改

    ```
    POST index/type/doc_id/_update      # 索引/类型/文档id/操作
    {
      "book_id":103,
      "book_name":"Python",
      "book_author":"kk",
      "book_price":33.22,
      "book_desc":"Python从入门到放弃"
    }
    ```

* 检索、查询文档

  ES检索语法比较特别，使用GET方法携带JSON格式的查询条件

  * 根据id检索

    ```
    GET index/type/doc_id
    ```

  * 全检索：查询索引中的所有数据（type使用自定名称）
  
    ```
    POST /index/type/_search
    ```
  
  * 按条件检索：
  
    ```
    curl -H "ContentType:application/json" -X PUT 127.0.0.1:9200/user/person/4 -d '
        {
            "query":{
                "match": {"name": "LMH"}
            }    
        }'
    ```
  
    默认一次最多返回10条结果，可以像下面的示例通过size字段来设置返回结果的数目
  
    ```
    curl -H "ContentType:application/json" -X PUT 127.0.0.1:9200/user/person/4 -d '
        {
            "query":{
                "match": {"name": "LMH"},
                "size": 2
            }    
        }'
    ```

* 删除索引

  ```
  curl -X DELETE 127.0.0.1:9200/index
  ```

* 删除文档

  ```
  DELETE index/type/doc_id
  ```

#### 数据类型

string

* text 可分词

* keyword 不能分词

Numeric datatypes

* long, integer, short, byte, double, float, half_float, scaled_float

Date datatype

* data --- 日期的存储时以 long 类型存储的毫秒数

Boolean datatype

* boolean --- true | false | "true" | "false"

Binary datatype

* binary 基于base64编码的字符串

Range datatypes

* integer_range, float_range, long_range, double_range, date_range

#### 复杂查询-数据搜索

示例数据：

```
PUT index4
{
  "mappings": {
    "properties": {
      "bookId":{
        "type": "long"
      },
      "bookName":{
        "type": "text"
      },
      "author":{
        "type": "keyword"
      },
      "time":{
        "type": "date"
      }
    }
  }
}
 
POST index4/_doc/1
{
  "bookId":10001,
  "bookName":"Java程序设计",
  "author":"张三",
  "time":234567890
}
POST index4/_doc/2
{
  "bookId":10002,
  "bookName":"C语言程序设计",
  "author":"Java谭浩强",
  "time":2345678999
}
POST index4/_doc/3
{
  "bookId":10003,
  "bookName":"程序设计进阶",
  "author":"李三",
  "time":2345678222
}
POST index4/_doc/4
{
  "bookId":10004,
  "bookName":"Java编程思想",
  "author":"三毛",
  "time":23456783452
}
```

查询语法：

```
GET /index/_search
{
  "query": {               # 构建查询
    "term": {              # 条件匹配方式，这里为term精确匹配方式
      "author": "张三",     # 查询条件
    }
  }
}
```

查询方式之**term和terms**

用于对字段进行精确匹配，类似于SQL中 where id=1

* term 表示完全匹配，搜索之前不会对关键字进行分词

  ```
  GET /index4/_search
  {
    "query": {
      "term": {
        "author": "张三"         # 只有author=’张三‘才被检索到
      }
    }
  }

* terms 也表示完全匹配，可以为一个field指定多个匹配关键词

  ```
  GET /index4/_search
  {
    "query": {
      "terms": {
        "author": ["三","李三"]     # author=’三‘ 不能检索出 author=’三毛‘
      }
    }
  }
  ```

查询方式之**match查询（重点）**

match查询表示对text字段进行部分匹配（模糊查询）

* match 表示部分匹配，搜索之前会对关键词进行分词

  ```
  GET /index4/_search
  {
    "query": {
      "match": {
        "bookName": "无聊程序"     # 分词成 无聊,聊,程序,序  bookName字段只要含有分词即可被检索到
      }
    }
  }
  ```

* match_all 表示查询全部内容，不指定任何条件

  ```
  GET /index4/_search
  {
    "query": {
      "match_all": {}
    }
  }
  ```

* multi_match 在多个字段中匹配同一个关键字

  ```
  GET /index4/_search
  {
    "query": {
      "multi_match": {
        "query": "Java",                    # 检索`java`
        "fields": ["bookName","author"]     # 在bookName、author这两个字段中搜索’java‘
      }
    }
  }
  ```

查询方式之**id查询**

- 根据一个id查询一个document

  ```
  GET /index4/_doc/1
  ```

- 根据多个id查询多个document ==> select * from ... where id in [1,2,3]

  ```
  GET /index4/_search
  {
    "query":{
    	"ids":{
    		"values":["1","2","3"]         # 检索文档id
    	}
    }
  }
  ```

其他查询方式

- prefix查询，根据指定字段的前缀值进行查询，类似于SQL的where name like 'python%'

  ```
  GET /index4/_search
  {
    "query": {
      "prefix": {                    # 前缀检索
        "author": {
          "value": "张"
        }
      }
    }
  }
  ```

- fuzzy查询，模糊查询，输入大概的内容es检索相关的数据，相当于正则search模糊搜索

  ```
  GET /index4/_search
  {
    "query": {
      "fuzzy": {                   # 在字符串中检索，不一定是开头结尾
        "bookName": {
          "value": "jav"
        }
      }
    }
  }
  ```

- wildcard查询：正则匹配

  ```
  GET /index4/_search
  {
      "query": {
          "wildcard": {               # 正则匹配检索
              "author": {
                  "value": "*三"
              }
          }
      }
  }
  ```

- range查询，根据范围进行查询

  ```
  GET /index4/_search
  {
      "query": {
          "range" : {                    # 字段的范围检索
              "bookId" : {               # 字段名
                  "gt" : 10001,          # 范围    10001 < bookId <= 10003
                  "lte" : 10003
              }
          }
      }
  }
  ```

- 分页查询

  ```
  GET /index4/_search
  {
    "query": {
      "match_all": {}
    },
    "_source": ["bookId","bookName"],          # 查询的字段
    "from": 0,                                 # 类似于SQL的 limit 0, 20
    "size": 20
  }
  ```



#### 复合查询—bool

多条件查询

- should   ==>   or
- must   ==>   and
- must_not   ==>   not

```
GET /index4/_search                   
{
  "query": {
    "bool":{                        # 表示复合查询，里面为逻辑语法
      "must_not": [                 # 以下两个条件都不成立
        {
          "match": {                # 会先分词
            "bookName": "Java"      
          }
        },
        {
          "match": {
            "author": "张三"
          }
        }
      ]
    }
  }
}
```

#### 结果过滤—filter

filter——根据条件进行查询，不计算分数，会对经常被过滤的数据进行缓存

```
GET /index4/_search
{
  "query": {
    "bool":{                           # 表示复合查询
      "filter": [                      # 检索下面两个match条件都符合的
        {
          "match": {
            "bookName": "Java"
          }
        },
        {
          "match": {
            "author": "张三"
          }
        }
      ]
    }
  }
}
```

#### 高亮显示

对匹配的关键词进行特殊样式的标记

```
GET /index4/_search
{
  "query": {
    "match": {
      "bookName": "Java"
    }
  },
  "highlight": {
    "fields": {
      "bookName": {}
    },
    "pre_tags": "<label style='color:red'>",
    "post_tags": "</label>"
  }
}
```







## ik分词

### 分词器的作用

- 在创建索引的时候需要用到分词器，在使用字符串搜索的时候也会用到分词器，并且这两个地方要使用同一个 分词器，否则可能会搜索不出来结果。 

- 分词器(Analyzer)的作用是把一段文本中的词按规则取出所包含的所有词，对应的是Analyzer类，这是一个抽 象类(public abstract class org.apache.lucene.analysis.Analyzer)，切分词的具体规则是由子类实现的，所以对于不 同的语言规则，要有不同的分词器。

### 英文分词器的原理

* 英文的处理流程为：输入文本，词汇切分，词汇过滤(去除停用词)，词干提取(形态还原)、大写转小写，结果输 出。

* 何为形态还原，意思是：去除单词词尾的形态变化，将其还原为词的原形，这样做可以搜索出更多有意义的结 果，比如在搜索student的时候，同事也可以搜索出students的结果。

* 任何一个分词法对英文的支持都是还可以的。

### 中文分词器的原理

中文分词比较复杂，并没有英文分词那么简单，这主要是因为中文的词与词之间并不是像英文那样用空格来隔 开，因为不是一个字就是一个词，而且一个词在另外一个地方就可能不是一个词，如："我们是中国人"，"是中"就不是一 个词，对于中文分词，通常有三种方式：单字分词、二分法分词、词典分词。

* 单字分词

  就是按照中文一个字一个字的进行分词，比如:"我们是中国人"，分词的效果就是"我"，"们"，"是"，"中"，"国"，"人"，StandardAnalyzer分词法就是单字分词。

* 二分法分词

  按照两个字进行切分，比如："我们是中国人"，分词的效果就是："我们"，"们是"，"是 中"，"中国"，"国人"，CJKAnalyzer分词法就是二分法分词

* 词库分词

  按照某种算法构造词，然后去匹配已建好的词库集合，如果匹配到就切分出来成为词语，通常词 库分词被认为是最好的中文分词算法，如："我们是中国人"，分词的效果就是:"我们"，"中国人"，极易分词 MMAnalyzer、庖丁分词、IkAnalyzer等分词法就是属于词库分词。

### 停用词

有些词在文本中出现的频率非常高，但是对文本所携带的信息基本不产生影响，例如英文的"a、an、the、of"或中文 的"的、了、着、是"，以及各种标点符号等，这样的词称为停用词，文本经过分词处理后，停用词通常会被过滤掉， 不会被进行索引，在检索的时候，用户的查询中如果含有停用词，检索系统也会将其过滤掉，这是因为用户输入查询字符串也要进行分词处理，排除停用词可以提升建立索引的速度，减小索引库文件的大小。

### 常用分词器

* WhitespaceAnalyzer

  仅仅是去掉了空格，没有其他任何操作，不支持中文。

* SimpleAnalyzer

  将除了字母以外的符号全部去除，并且将所有字符变为小写，需要注意的是这个分词器同样把数据也去除了，同样不支持中文。

* StopAnalyzer

  这个和SimpleAnalyzer类似，不过比他增加了一个的是，在其基础上还去除了所谓的stop words，比如the, a, this这些。这个也是不支持中文的。

* StandardAnalyzer

  英文方面的处理和StopAnalyzer一样的，对中文支持，使用的是单字切割。

* CJKAnalyzer

  这个支持中日韩，前三个字母也就是这三个国家的缩写。这个对于中文基本上不怎么用吧，对中文的支持很烂，它是 用每两个字作为分割，分割方式个人感觉比较奇葩，在下面比较举例。

* SmartChineseAnalyzer

  中文的分词,比较标准的中文分词，对一些搜索处理的并不是很好。

* IKAnalyzer 

  中国人自己开发，对于中文分词比较精准

### IK分词器

ES中文分词我们采用Ik分词，ik有两种分词模式：ik_max_word和ik_smart模式

* ik_max_word:

  会将文本做最细粒度的拆分，比如会将“中华人民共和国国歌”拆分为“中华人民共和国,中华人民, 中华,华人,人民共和国,人民,人,民,共和国,共和,和国,国歌”，会穷尽各种可能的组合；

* ik_smart:

  会做最粗粒度的拆分，比如会将“中华人民共和国国歌”拆分为“中华人民,共和国,国歌”。 索引时，为了提供索引的覆盖范围，通常会采用ik_max_word分析器，会以最细粒度分词索引，搜索时为了提高搜索准确度，会采用ik_smart分析器，会以粗粒度分词

[Analyzer在线工具，IK Analyzer—在线分词器工具](https://www.sojson.com/analyzer)

```
“今天天气太热”的分词结果为：
[
    {
        "endOffset": 4,
        "position": 0,
        "startOffset": 0,
        "term": "今天天气",
        "type": "CN_WORD"
    },
    {
        "endOffset": 2,
        "position": 1,
        "startOffset": 0,
        "term": "今天",
        "type": "CN_WORD"
    },
    {
        "endOffset": 3,
        "position": 2,
        "startOffset": 1,
        "term": "天天",
        "type": "CN_WORD"
    },
    {
        "endOffset": 4,
        "position": 3,
        "startOffset": 2,
        "term": "天气",
        "type": "CN_WORD"
    },
    {
        "endOffset": 6,
        "position": 4,
        "startOffset": 4,
        "term": "太热",
        "type": "CN_WORD"
    }
]
```



### 安装

解压下载的ik分词压缩包，到es的plugins目录中

配置完成后重启es

### 配置自定义词库

在es/plugins/ik/config目录中定义词典文件（.dic）

在es/plugins/ik/config/IKAnalyzer.cfg.xml加载自定义词典文件

  





