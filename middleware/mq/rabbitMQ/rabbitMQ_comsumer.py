# 消费者代码：rabbitmq_customer.py
import pika

# amqp://zeng:123456@192.168.1.7:5672/%2Fdev

# 链接到rabbitmq服务器
credentials = pika.PlainCredentials(username='zeng', password='123456')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.7', 5672, '/default', credentials))
# credentials = pika.PlainCredentials(username='rabbitMQ', password='mdR42JnqxdqC')
# connection = pika.BlockingConnection(pika.ConnectionParameters('121.37.225.58', 5672, '/', credentials))
# 创建频道，声明消息队列
channel = connection.channel()

channel.exchange_declare(exchange='alg-server.default_send_topic.exchange')  # 默认direct
channel.queue_declare(queue='alg-server.default_send_topic.queue')
channel.queue_bind(queue='alg-server.default_send_topic.queue', exchange='alg-server.default_send_topic.exchange', routing_key='alg-server.default_send_topic.route')

# 定义接受消息的回调函数
def callback(ch, method, properties, body):
    print(body)


# 告诉RabbitMQ使用callback来接收信息
channel.basic_consume(queue='alg-server.default_send_topic.queue', on_message_callback=callback, auto_ack=True)
# 开始接收信息
channel.start_consuming()
