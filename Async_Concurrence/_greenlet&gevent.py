# greenlet属于更底层的异步协程实现，对yield的封装，实现代码执行过程中的挂起，唤醒操作，没有自己的调度过程，需要手动switch切换调度
# eventlet是一个并发网络库。是基于greenlet的扩展封装，实现了协程自动切换
#     实现了自己调度器Hub，类似于Tornado的IOLoop，是单实例的。在Hub中有一个event loop，根据不同的事件来切换到对应的GreenThread。
#     还实现了一系列的补丁来使 Python 标准库中的 socket 等等module 来支持 GreenThread 的切换。
# gevent是基于协程的Python网络库。基于greenlet 和 libev(C语言实现的异步事件库libevent)
#     Gevent 通过 Cython 调用 libev 来实现一个高效的 event loop 调度循环。
#     有自己的 monkey_patch，在打了补丁后，完全可以使用 python 线程的方式来无感知的使用协程，减少了开发成本。
#     猴子补丁 Monkey Patch: 使用猴子补丁的方式，gevent 能够修改标准库里面大部分的阻塞式系统调用，包括 socket、ssl、threading 和 select 等模块，而变为协作式运行。也就是通过猴子补丁的 monkey.patch_xxx() 来将 python 标准库中 模块 或 函数 改成 gevent 中的响应的具有协程的协作式对象。这样在不改变原有代码的情况下，将应用的阻塞式方法，变成协程式的。

from lxml import etree
from gevent import monkey
monkey.patch_all()          # 猴子补丁尽可能早的导入执行
import gevent, requests, random, socket
from gevent.testing.six import xrange
from gevent import Greenlet, pool, Timeout
from gevent.event import Event, AsyncResult
from gevent.queue import Queue
from gevent.lock import BoundedSemaphore
from gevent.local import local




# ##################   greenlet   #######################
# from greenlet import greenlet
# import time
#
# def task_1():
#     while True:
#         print("--This is task 1!--")
#         g2.switch()  # 切换到g2中运行
#         time.sleep(0.5)
#
# def task_2():
#     while True:
#         print("--This is task 2!--")
#         g1.switch()  # 切换到g1中运行
#         time.sleep(0.5)
#
# g1 = greenlet(task_1)         # 定义greenlet对象
# g2 = greenlet(task_2)
# g1.switch()                   # 协程切换到g1中运行



# ##################   gevent   #######################

# def task_1(num):
#     for i in range(num):
#         print(gevent.getcurrent(), i)
#         gevent.sleep(1)  # 模拟一个耗时操作，注意不能使用time模块的sleep
#
# g1 = gevent.spawn(task_1, 5)  # 创建协程/Greenlet对象
# g2 = gevent.spawn(task_1, 5)
# g3 = gevent.spawn(task_1, 5)
#
# # g1.join()  # 等待协程运行完毕
# # g2.join()
# # g3.join()
# gevent.joinall([g1, g2, g3])             # 会等待所有传入的Greenlet协程运行结束后再退出


# class Task(Greenlet):
#     def __init__(self, name):
#         Greenlet.__init__(self)
#         self.name = name
#
#     def _run(self):
#         print("Task %s: some task..." % self.name)
#
# t1 = Task("task1")
# t2 = Task("task2")
# t1.start()
# t2.start()
# # here we are waiting all tasks
# gevent.joinall([t1, t2])



# 获取三个网站的IP地址
# urls = ['www.baidu.com', 'www.gevent.org', 'www.python.org']
# jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
# gevent.joinall(jobs, timeout=5)
# print(job.value for job in jobs)           # 通过协程对象的”value”属性，来获取协程函数的返回值
# 上述例子在没有使用猴子补丁时，其实程序运行的时间和不用协程是一样的，是三个网站打开时间的总和。可是理论上协程是非阻塞的，那运行时间应该等于最长的那个网站打开时间呀？
# 其实这是因为Python标准库里的socket是阻塞式的，DNS解析无法并发，包括像urllib库也一样，所以这种情况下用协程完全没意义。
# 一种方法是使用gevent下的socket模块，通过”from gevent import socket”来导入。
# 另一种方法是使用猴子布丁（Monkey patching），更常用



# 获取协程状态
# 协程对象的”started”属性和”ready()”方法来判断启动停止。
# 用”successful()”方法来判断其是否成功运行且没抛异常。
# 如果协程执行完有返回值，可以通过”value”属性来获取。
# greenlet协程运行过程中发生的异常是不会被抛出到协程外的，因此需要用协程对象的”exception”属性来获取协程中的异常。
# def win():
#     return 'You win!'
#
# def fail():
#     raise Exception('You failed!')
#
# winner = gevent.spawn(win)
# loser = gevent.spawn(fail)
#
# print(winner.started)     # True
# print(loser.started)      # True

# 在Greenlet中发生的异常，不会被抛到Greenlet外面。
# 控制台会打出Stacktrace，但程序不会停止
# try:
#     gevent.joinall([winner, loser])
# except Exception as e:
#     # 这段永远不会被执行
#     print('This will never be reached')
#
# print(winner.ready())      # True
# print(loser.ready())       # True
#
# print(winner.value)        # 'You win!'
# print(loser.value)         # None
#
# print(winner.successful())  # True
# print(loser.successful())   # False
#
# # 这里可以通过raise loser.exception 或 loser.get()来将协程中的异常抛出
# print(loser.exception)



# 协程超时
# timeout = Timeout(2)            # 2 seconds
# timeout.start()                 # 此后所有协程的运行，如果超过两秒就会抛出”Timeout”异常
#
# with Timeout(1):                # 这样超时设置只在with语句块中有效
#     gevent.sleep(10)
#
# class TooLong(Exception):       # 指定超时所抛出的异常，来替换默认的”Timeout”异常。
#     pass
# with Timeout(1, TooLong):
#     gevent.sleep(10)



# 协程间通讯
# 异步协程之间的同步
# 使用事件（Event）对象。该对象的”wait()”方法可以阻塞当前协程，而”set()”方法可以唤醒之前阻塞的协程。
# evt = Event()
#
# def setter1():
#     print('Wait for me')
#     gevent.sleep(3)                 # 3秒后唤醒所有在evt上等待的协程
#     print("Ok, I'm done")
#
#     # Set the internal flag to true.
#     evt.set()                       # 唤醒
#
# def waiter1():
#     print("I'll wait for you")
#     evt.wait()                      # 阻塞，所有waiter协程等待直到某个协程调用set方法，于是立即被唤醒
#     print('Finish waiting')
#
# gevent.joinall([                    # 5个waiter协程都会等待事件evt，当setter协程在3秒后设置evt事件，所有的waiter协程即被唤醒。
#     gevent.spawn(setter1),
#     gevent.spawn(waiter1),
#     gevent.spawn(waiter1),
#     gevent.spawn(waiter1),
#     gevent.spawn(waiter1),
#     gevent.spawn(waiter1)
# ])


# AsyncResult事件，它可以在唤醒时传递消息数据。
# 让我们将上例中的setter和waiter作如下改动
# aevt = AsyncResult()
#
# def setter2():
#     print('Wait for me')
#     gevent.sleep(3)                               # 3秒后唤醒所有在evt上等待的协程
#     print("Ok, I'm done")
#     aevt.set({'data': 'hello'})                   # 唤醒正被阻塞的协程，并传递消息
#
# def waiter2():
#     print("I'll wait for you")
#     message = aevt.get()                          # 等待，并在唤醒时获取消息
#     print('Got wake up message: %s' % message)
#
# gevent.joinall([
#     gevent.spawn(setter2),
#     gevent.spawn(waiter2),
#     gevent.spawn(waiter2),
#     gevent.spawn(waiter2),
#     gevent.spawn(waiter2),
#     gevent.spawn(waiter2)
# ])


# Queue数据队列（有点类似于GO异步通信使用通道channel）
# 可以用它的put和get方法来存取队列中的元素。gevent的队列对象可以让greenlet协程之间安全的访问。
# put(item, block=True, timeout=None) 往队列放入数据，可选是否阻塞和超时时间
# get(block=True, timeout=None) 从队列读出数据，可选是否阻塞和超时时间
# peek(block=True, timeout=None) 和get()类似，但获取的数据不会从队列移除
# put和get方法都是阻塞式的，它们都有非阻塞的版本：put_nowait和get_nowait。如果调用get方法时队列为空，则抛出”gevent.queue.Empty”异常。
# Queue对象常用方法:
#     full()           # 是否为空
#     qsize()          # 队列中的数据长度

# products = Queue()

# def consumer(name):
#     while not products.empty():
#         print('%s got product %s' % (name, products.get()))
#         gevent.sleep(0)
#     print('%s Quit')
#
# def producer():
#     for i in xrange(1, 10):
#         products.put(i)
#
# gevent.joinall([
#     gevent.spawn(producer),
#     gevent.spawn(consumer, 'steve'),
#     gevent.spawn(consumer, 'john'),
#     gevent.spawn(consumer, 'nancy'),
# ])



# 信号量Semaphore/锁
# 信号量可以用来限制协程并发的个数。限制并发访问或运行的低层次的同步原语。
# 范围为1的信号量也称为锁(lock)。它向单个greenlet提供了互斥访问。 信号量和锁常常用来保证资源只在程序上下文被单次使用。
# 两个方法acquire和release。acquire就是获取信号量，而release就是释放信号量。当所有信号量都已被获取，那剩余的协程就只能等待任一协程释放信号量后才能得以运行
# sem = BoundedSemaphore(1)    # 2表示信号量数，即最多有两个信号量可被获取，亦即只有两个协程能够运行，其他协程需等待信号量锁的释放才能执行；若为1则表示锁，只能当前协程运行

# def worker(n):
#     # 信号量-1，即拿到锁
#     sem.acquire()
#     print('Worker %i acquired semaphore' % n)
#
#     gevent.sleep(0)
#
#     # 信号量+1，即释放锁
#     sem.release()
#     print('Worker %i released semaphore' % n)
#
# gevent.joinall([gevent.spawn(worker, i) for i in xrange(0, 6)])



# 协程local变量
# 同线程类似，协程也有local变量，也就是只在当前协程内可被访问的变量
# 将变量存放在local对象中，即可将其的作用域限制在当前协程内，当其他协程要访问该变量时，就会抛出异常。
# 不同协程间可以有重名的本地变量，而且互相不影响。因为协程本地变量的实现，就是将其存放在以的”greenlet.getcurrent()”的返回为键值的私有的命名空间内。
# data = local()
#
# def f1():
#     data.x = 1
#
# def f2():
#     try:
#         print(data.x)
#     except AttributeError:
#         print('there is no x in f2')
#
# gevent.joinall([
#     gevent.spawn(f1),
#     gevent.spawn(f2)
# ])



# demo
# 并发请求
class DoubanMovie(object):
    """A class containing interface test method of Douban object"""

    def __init__(self):
        self.host = 'movie.douban.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Referer': 'https://movie.douban.com/',
        }

    def get_response(self, url, data):
        resp = requests.post(url=url, data=data, headers=self.headers).content.decode('utf-8')
        return resp

    def test_search_tags_movie(self):
        method = 'search_tags'
        url = 'https://%s/j/%s' % (self.host, method)
        post_data = {
            'type': 'movie',
            'source': 'index'
        }
        resp = self.get_response(url=url, data=post_data)
        print(resp)
        return resp

def async_spider_douban():
    douban = DoubanMovie()
    threads = []
    for i in range(6):
        thread = gevent.spawn(douban.test_search_tags_movie)
        threads.append(thread)

    # threads = [gevent.spawn(douban.test_search_tags_movie) for i in range(6)]
    gevent.joinall(threads)


def downloader(img_name, img_url):
    req = requests.get(img_url)
    img_content = req.content
    with open(img_name, "wb") as f:
        f.write(img_content)

def async_spider_pic():
    r = requests.get('http://www.nsgirl.com/portal.php')
    if r.status_code == 200:
        img_src_xpath = '//div[@id="frameXWswSe"]//div[@class="portal_block_summary"]//li//img/@src'
        s_html = etree.HTML(text=r.text)
        all_img_src = s_html.xpath(img_src_xpath)

        count = 0
        for img_src in all_img_src:
            count += 1
            # print(img_src)
            # http://www.nsgirl.com/forum.php?mod=image&aid=342&size=218x285&key=cd6828baf05c305c
            url = 'http://www.nsgirl.com/' + img_src
            gevent.joinall(
                [gevent.spawn(downloader, f"{count}.jpg", url), ]
            )


# gevent 组
# 组(group) 是一个运行中 greenlet 的集合，集合中的 greenlet 像一个组一样 会被共同管理和调度。
def talk(msg):
    for i in range(3):
        print(msg)

g1 = gevent.spawn(talk, 'bar')
g2 = gevent.spawn(talk, 'foo')
g3 = gevent.spawn(talk, 'fizz')

group = pool.Group()
group.add(g1)
group.add(g2)
group.join()

group.add(g3)
group.join()



# gevent 池
# 池(pool)是一个为处理数量变化并且需要限制并发的greenlet而设计的结构。 在需要并行地做很多受限于网络和IO的任务时常常需要用到它。
gevent_pool = pool.Pool(5)

def func_1():
    for index in range(100):
        gevent_pool.spawn(func_2, index)

def func_2(arg=None):
    print(f'func_2 ---> {arg}')

# gevent_pool.spawn(func_1)
# gevent_pool.join()




if __name__ == '__main__':
    # async_spider_douban()
    # async_spider_pic()
    # run_producer_consumer()


    pass












