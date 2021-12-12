# greenlet属于更底层的异步协程实现， 需要人工切换

from greenlet import greenlet
import time

def task_1():
    while True:
        print("--This is task 1!--")
        g2.switch()  # 切换到g2中运行
        time.sleep(0.5)

def task_2():
    while True:
        print("--This is task 2!--")
        g1.switch()  # 切换到g1中运行
        time.sleep(0.5)


g1 = greenlet(task_1)  # 定义greenlet对象
g2 = greenlet(task_2)

g1.switch()  # 切换到g1中运行


# gevent是进行了封装

# import gevent
#
# def task_1(num):
#     for i in range(num):
#         print(gevent.getcurrent(), i)
#         gevent.sleep(1)  # 模拟一个耗时操作，注意不能使用time模块的sleep
#
#
# g1 = gevent.spawn(task_1, 5)  # 创建协程
# g2 = gevent.spawn(task_1, 5)
# g3 = gevent.spawn(task_1, 5)
#
# g1.join()  # 等待协程运行完毕
# g2.join()
# g3.join()
