# 进程通信


# 为什么进程之间需要通信？
# 1.数据传输
#     一个进程需要将它的数据发送给另一个进程;
# 2.资源共享
#     多个进程之间共享同样的资源;
# 3.事件通知
#     一个进程需要向另一个或一组进程发送消息，通知它们发生了某种事件;
# 4.进程控制
#     有些进程希望完全控制另一个进程的执行(如Debug进程)，该控制进程希望能够拦截另一个进程的所有操作，并能够及时知道它的状态改变。

# 进程间通信的几种方式
# 管道
#     匿名管道
#         管道是一种半双工的通信方式，数据只能单向流动，而且只能在具有亲缘关系的进程间使用。进程的亲缘关系通常是指父子进程关系。
#     命名管道
#         有名管道也是半双工的通信方式，但是它允许无亲缘关系进程间的通信。
# 消息队列
#     消息队列是由消息的链表，存放在内核中并由消息队列标识符标识。消息队列克服了信号传递信息少、管道只能承载无格式字节流以及缓冲区大小受限等缺点。
# 共享内存通信
#     共享内存就是映射一段能被其他进程所访问的内存，这段共享内存由一个进程创建，但多个进程都可以访问。共享内存是最快的 IPC 方式，它是针对其他进程间通信方式运行效率低而专门设计的。它往往与其他通信机制，如信号量，配合使用，来实现进程间的同步和通信。
# 信号量
#     信号量是一个计数器，可以用来控制多个进程对共享资源的访问。它常作为一种锁机制，防止某进程正在访问共享资源时，其他进程也访问该资源。因此，主要作为进程间以及同一进程内不同线程之间的同步手段。
# 套接字（socket）通信
#     套接口也是一种进程间通信机制，与其他通信机制不同的是，它可用于不同机器之间的进程通信。
# 信号
#     信号是一种比较复杂的通信方式，用于通知接收进程某个事件已经发生。

# Python中如何实现进程通信？
# 进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的。


# 对于共享内存，数据操作最快，因为是直接在内存层面操作，省去中间的拷贝工作。但是共享内存只能在单机上运行，且只能操作基础数据格式，无法直接共享复杂对象。
# 管道和队列传递数据没有共享内存快，且每次传递的数据大小受限。但是使用队列可以在多个进程间传递，可以在不同主机上的进程间共享，以实现分布式。
# 匿名管道则只能在父子进程间共享，而命名管道可在同一台计算机的不同进程之间或在跨越一个网络的不同计算机的进程间共享。
import collections
from multiprocessing import Process, Pipe, Queue, set_start_method, Manager, Lock, Semaphore, Event
import time, random, os


# 此函数的调用位置，必须位于所有与多进程有关的代码之前。
set_start_method('fork')


# --------------------- 管道Pipe -------------------------

def consumer(p, name):
    left, right = p
    left.close()       # 关闭左连接器，使用右连接器接收管道内容
    while True:
        try:
            baozi = right.recv()
            print('%s 收到包子:%s' % (name, baozi))
        except EOFError:
            right.close()
            break


def producer(seq, p):
    left, right = p
    right.close()       # 关闭右连接器，使用左连接器向管道发送内容
    for i in seq:
        left.send(i)
        time.sleep(1)
    else:
        left.close()


def use_pipe():
    # 管道可以用于双向通信，利用在客户端 / 服务器中使用的请求／响应模型或远程过程调用，就可以使用管道编写与进程交互的程序。
    # 生产者和消费者都没有使用管道的某个端点，就应该将其关闭，如在生产者中关闭管道的右端，在消费者中关闭管道的左端。如果忘记执行这些步骤，程序可能在消费者中的recv()操作上挂起。
    # 管道是由操作系统进行引用计数的, 必须在所有进程中关闭管道后才能生产EOFError异常。因此，在生产者中关闭管道不会有任何效果，消费者中也应该关闭相同的管道端点。

    left, right = Pipe()

    #      producer(关闭right)  --->  (left   Pipe   right)   --->    consumer(关闭left)

    c1 = Process(target=consumer, args=((left, right), 'c1'))
    c1.start()

    seq = (i for i in range(10))
    producer(seq, (left, right))

    right.close()
    left.close()

    c1.join()            # 主进程等待c1执行完再进行下面的打印
    print('进程间通信-管道-主进程')


# --------------------- 队列Queue -------------------------

def consumer2(q: Queue):
    while True:
        # 从队列中读取
        res = q.get()
        if res is None:
            break  # 收到结束信号则结束
        time.sleep(random.randint(1, 3))
        print('\033[45m%s 吃 %s\033[0m' % (os.getpid(), res))


def producer2(q: Queue):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        res = '包子%s' % i
        # 向队列中发送
        q.put(res)
        print('\033[46m%s 生产了 %s\033[0m' % (os.getpid(), res))

    q.put(None)  # 发送结束信号， 但结束信号None，不一定要由生产者发，主进程里同样可以发，但主进程需要等生产者结束后才应该发送该信号。


def use_queue():
    # 此函数的调用位置，必须位于所有与多进程有关的代码之前。
    # set_start_method('fork')               # 写在这里会报错

    q = Queue()
    # 生产者们: 即厨师们
    p1 = Process(target=producer2, args=(q,))             # 未设置 daemon = True，主进程会等待子进程全部执行完再结束

    # 消费者们: 即吃货们
    c1 = Process(target=consumer2, args=(q,))

    # 开始
    p1.start()
    c1.start()

    # p1.join()
    # q.put(None)         # 主进程等待p1完成后可以发送结束信号

    print('进程间通信-队列-主进程')
    print('主进程会等待子进程全部执行完再结束，等待中。。。')


# --------------------- 内存共享 -------------------------

def work(d, lock):
    with lock:  # 不加锁而操作共享内存的数据，肯定会出现数据错乱
        print(f"计数器减一，当前为：{d['count']}")
        d['count'] -= 1


def use_memory_share():
    # 虽然进程间数据独立，但可以通过Manager实现数据共享
    # 进程间通信应该尽量避免使用本节所讲的共享数据的方式

    lock = Lock()
    with Manager() as m:
        dic = m.dict({'count': 20})        # 共享内存中写入dict数据
        # lis = m.list([1, 2, 3])
        p_l = []
        for i in range(20):
            p = Process(target=work, args=(dic, lock))
            p_l.append(p)
            p.start()

        for p in p_l:
            p.join()
        print(dic)


# --------------------- 信号量 -------------------------

def go_wc(sem, user):
    sem.acquire()
    print('%s 占到一个茅坑' % user)
    time.sleep(random.randint(0, 3))  # 模拟每个人拉屎速度不一样，0代表有的人蹲下就起来了
    sem.release()


def use_semaphore():
    sem = Semaphore(5)        # 最多五个可操作资源
    p_l = []
    for i in range(13):
        p = Process(target=go_wc, args=(sem, 'user%s' % i,))
        p.start()
        p_l.append(p)

    for p in p_l:
        p.join()
    print('主进程等待子进程结束再结束。。。')


# --------------------- 事件 -------------------------

event = Event()


def salesclerk(event: Event):
    print('小贩：生产...')
    print('小贩：售卖...')
    # time.sleep(1)
    print('小贩：等待就餐')
    event.set()
    event.clear()
    event.wait()
    print('小贩：谢谢光临')
    event.set()
    event.clear()


def customer(event: Event):
    print('顾客：准备买早餐')
    event.set()
    event.clear()
    event.wait()
    print('顾客：买到早餐')
    print('顾客：享受美食')
    # time.sleep(2)
    print('顾客：付款，真好吃...')
    event.set()
    event.clear()


def use_signal_or_event():
    set_start_method('fork', True)

    # 创建进程
    sc = Process(target=salesclerk, args=(event,))
    cus = Process(target=customer, args=(event,))
    # 启动进程

    cus.start()
    sc.start()

    # time.sleep(2)


if __name__ == '__main__':
    # use_pipe()
    use_queue()
    # use_memory_share()
    # use_semaphore()
    # use_signal_or_event()
