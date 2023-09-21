# 生产者代码：rabbitmq_producer.py
import json

import pika

# 链接到RabbitMQ服务器
credentials = pika.PlainCredentials(username='zeng', password='123456')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.7', 5672, '/default', credentials))
# credentials = pika.PlainCredentials(username='rabbitMQ', password='mdR42JnqxdqC')
# connection = pika.BlockingConnection(pika.ConnectionParameters('121.37.225.58', 5672, '/', credentials))

# 创建频道
channel = connection.channel()
# 声明消息队列
# channel.exchange_declare(exchange='alg-server.default_receive_topic.exchange')  # 默认direct
# channel.queue_declare(queue='alg-server.default_receive_topic.queue')
# routing_key是队列名 body是要插入的内容
channel.basic_publish(exchange='alg-server.default_receive_topic.exchange', routing_key='alg-server.default_receive_topic.route', body=bytes(json.dumps({'username': 'huang'}), encoding = "utf8"))
print("已经发送 -------------")
# 关闭链接
channel.close()
connection.close()
