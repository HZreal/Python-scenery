# 生成器实现生产者-消费者模型，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高


def consumer():
    """
    消费者生成器
    """
    print('--3、开始执行生成器代码--')
    response = None
    while True:
        print('--4、yield，中断，保存上下文--')
        n = yield response     # 4、yield，中断，保存上下文，返回response给生产者
        print('--7、恢复上下文，获取到生产者发来的产品n=c.send，继续往下执行--')
        if not n:
            return
        print("[Consumer]: consuming {} ..".format(n))
        response = "第%s个OK" % n


def produce():
    """
    生产者函数
    """
    n = 0
    while n < 5:
        n += 1
        print("[Producer]: producing the {} production ...".format(n))
        print("--6、发送生产结果n给消费者，第{}次唤醒生成器，从yield位置继续往下执行！--".format(n + 1))
        r = c.send(n)  # 唤醒生成器     r等于response的返回值
        print("--8、获取到生产者返回的response--")
        print("[Producer]: consumer return {} ..".format(r))

    c.close()

if __name__ == "__main__":
    c = consumer()          # 1、定义生成器，consumer并不执行
    print("--2、启动消费者生成器，开始执行生成器consumer--使之执行到yield挂起(等待生产者产出)")
    res = c.send(None)
    print(res)             # 返回None
    print("--5、运行produce函数--")
    produce()

# --2、启动消费者生成器，开始执行生成器consumer--使之执行到yield挂起(等待生产者产出)
# --3、开始执行生成器代码--
# --4、yield，中断，保存上下文--
# None
# --5、运行produce函数--
# [Producer]: producing the 1 production ...
# --6、发送生产结果n给消费者，第2次唤醒生成器，从yield位置继续往下执行！--
# --7、恢复上下文，获取到生产者发来的产品n=c.send，继续往下执行--
# [Consumer]: consuming 1 ..
# --4、yield，中断，保存上下文--
# --8、获取到生产者返回的response--
# [Producer]: consumer return 第1个OK ..
# [Producer]: producing the 2 production ...
# --6、发送生产结果n给消费者，第3次唤醒生成器，从yield位置继续往下执行！--
# --7、恢复上下文，获取到生产者发来的产品n=c.send，继续往下执行--
# [Consumer]: consuming 2 ..
# --4、yield，中断，保存上下文--
# --8、获取到生产者返回的response--
# [Producer]: consumer return 第2个OK ..
# [Producer]: producing the 3 production ...
# --6、发送生产结果n给消费者，第4次唤醒生成器，从yield位置继续往下执行！--
# --7、恢复上下文，获取到生产者发来的产品n=c.send，继续往下执行--
# [Consumer]: consuming 3 ..
# --4、yield，中断，保存上下文--
# --8、获取到生产者返回的response--
# [Producer]: consumer return 第3个OK ..
# [Producer]: producing the 4 production ...
# --6、发送生产结果n给消费者，第5次唤醒生成器，从yield位置继续往下执行！--
# --7、恢复上下文，获取到生产者发来的产品n=c.send，继续往下执行--
# [Consumer]: consuming 4 ..
# --4、yield，中断，保存上下文--
# --8、获取到生产者返回的response--
# [Producer]: consumer return 第4个OK ..
# [Producer]: producing the 5 production ...
# --6、发送生产结果n给消费者，第6次唤醒生成器，从yield位置继续往下执行！--
# --7、恢复上下文，获取到生产者发来的产品n=c.send，继续往下执行--
# [Consumer]: consuming 5 ..
# --4、yield，中断，保存上下文--
# --8、获取到生产者返回的response--
# [Producer]: consumer return 第5个OK ..




















