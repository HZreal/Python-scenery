# 线程之间共享全局变量(同一个进程里)

# import threading
# import time

# g_list = []
# def add_data():
#     for i in range(5):
#         g_list.append(i)
#         print('添加:',i)
#         time.sleep(0.2)
#     else:
#         print('添加完成:',g_list)
#
# def read_data():
#     print('read:',g_list)
#
# if __name__ == '__main__':
#     add_thread = threading.Thread(target=add_data)
#     read_thread = threading.Thread(target=read_data)
#
#     add_thread.start()
#     join函数：主线程(main_thread)等待当前子线程(add_thread)执行完成，代码再继续往下执行
    # add_thread.join()       # 线程同步，使添加数据线程先执行完
    # read_thread.start()






# 线程之间共享全局变量数据出现错误问题
import threading
num = 0

# def task1():
#     for i in range(1000000):
#         global num
#         num += 1
#     else:
#         print('task1:',num)
#
# def task2():
#     for i in range(1000000):
#         global num     #表示声明修改全局变量的内存地址
#         num += 1
#     else:
#         print('task2:',num)
#
# if __name__ == '__main__':
#     first_thread = threading.Thread(target=task1)
#     # 1. 线程同步：主线程等待子线程(first_thread)执行完,再往下执行
#     first_thread.join()        # 没有此语句，结果是不确定的
#     second_thread = threading.Thread(target=task2)
#
#     first_thread.start()
#     second_thread.start()

# 当没有 first_thread.join()语句实行线程同步时，结果是不确定的！！！

# 错误分析:
# 两个线程first_thread和second_thread都要对全局变量g_num(默认是0)进行加1运算，但是由于是多线程同时操作，有可能出现下面情况：
# 在g_num=0时，first_thread取得g_num=0。此时系统把first_thread调度为”sleeping”状态，把second_thread转换为”running”状态，t2也获得g_num=0
# 然后second_thread对得到的值进行加1并赋给g_num，使得g_num=1
# 然后系统又把second_thread调度为”sleeping”，把first_thread转为”running”。线程t1又把它之前得到的0加1后赋值给g_num。
# 这样导致虽然first_thread和first_thread都对g_num加1，但结果仍然是g_num=1


# 全局变量数据错误的解决办法:
#   1. 线程同步:     join()函数
#       保证同一时刻只能有一个线程去操作全局变量 同步: 就是协同步调，按预定的先后次序进行运行。如:你说完，我再说, 好比现实生活中的对讲机
#
#
#
#   2. 互斥锁：     lock
# threading模块中定义了Lock变量，这个变量本质上是一个函数，通过调用这个函数可以获取一把互斥锁。
lock = threading.Lock()

def task1():
    # 上锁
    lock.acquire()

    for i in range(1000000):
        global num
        num += 1
    else:
        print('task1:',num)

    # 释放锁
    lock.release()

def task2():
    # 上锁
    lock.acquire()

    for i in range(1000000):
        global num     #表示声明修改全局变量的内存地址
        num += 1
    else:
        print('task2:',num)

    # 释放锁
    lock.release()

if __name__ == '__main__':
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    first_thread.start()
    second_thread.start()

# 互斥锁的作用就是保证同一时刻只能有一个线程去操作共享数据，保证共享数据不会出现错误问题
# 使用互斥锁的好处确保某段关键代码只能由一个线程从头到尾完整地去执行
# 使用互斥锁会影响代码的执行效率，多任务改成了单任务执行
# 互斥锁如果没有使用好容易出现死锁的情况












































