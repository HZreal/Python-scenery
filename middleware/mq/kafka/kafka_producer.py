# confluent_kafka     适用于Python的高性能Kafka客户端，它利用了高性能C客户端librdkafka
# kafka-python     类似于官方的Java客户端，并带有大量的pythonic接口
# pykafka        简单易用的Kafka客户端，它包括Kafka生产者和使用者


import json
# kafka-python库
from kafka import KafkaClient, KafkaProducer, KafkaConsumer
from kafka.errors import kafka_errors

# producer = KafkaProducer(bootstrap_servers='localhost:9092')
# producer.send(topic='', value=b'', key=b'', partition=None)
# topic: 发送消息的所属分类，必须指定。
# key/value: 必须是字节字符串，二选一至少指定一个
# partition: kafka默认配置一个分区，即默认0号分区

# 只发送value
# future = producer.send('foobar', b'another_message')
# 只发送key
# future = producer.send('foobar', key=b'foo')
# 发送key和value
# future = producer.send('foobar', key=b'foo111', value=b'bar111')



# 发送json类型消息
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=lambda k: str(k).encode(),
    value_serializer=lambda v: json.dumps(v).encode()
)
future = producer.send('foobar', {'value': 'value11'}, 'key')


# 接收ACK应答
result = future.get(timeout=10)
print(result)















