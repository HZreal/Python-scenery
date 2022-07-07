# Lock与Rlock的区别
# 区别一：Lock被称为原始锁，一个线程只能请求一次；RLock被称为重入锁，可以被一个线程请求多次，即锁中可以嵌套锁。
# 区别二：当Lock处于锁定状态时，不属于特定线程，可在另一个线程中进行解锁释放；而RLock只有当前线程才能释放本线程上的锁，不可由其他线程进行释放，所以在使用RLock时，acquire与release必须成对出现，即解铃还须系铃人。


import threading
import time

lock = threading.Lock()
def task():
    lock.release()
    print("在子线程解锁后打印")


def run1():
    lock.acquire()
    t = threading.Thread(target=task)
    t.start()



# 在主线程中定义Lock锁，然后上锁，再创建一个子线程t运行main函数释放锁，结果正常输出，说明主线程上的锁，可由子线程解锁。
# 如果把上面的锁改为RLock则报错。在实际中设计程序时，我们会将每个功能分别封装成一个函数，每个函数中都可能会有临界区域，所以就需要用到RLock

rlock = threading.RLock()
def fun_1():
    print('开始')
    time.sleep(1)
    rlock.acquire()
    print("第一道锁")
    fun_2()
    rlock.release()
    print("释放第一道锁")

def fun_2():
    rlock.acquire()
    print("第二道锁")
    rlock.release()
    print("释放第二道锁")

def run2():
    t1 = threading.Thread(target=fun_1)
    t2 = threading.Thread(target=fun_1)
    t1.start()
    t2.start()


if __name__ == '__main__':
    # run1()
    run2()

# 一句话总结就是Lock不能套娃，RLock可以套娃；Lock可以由其他线程中的锁进行操作，RLock只能由本线程进行操作







