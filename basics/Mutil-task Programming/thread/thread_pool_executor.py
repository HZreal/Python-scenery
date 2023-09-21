# 线程池
# 因为新建线程系统需要分配资源、终止线程系统需要回收资源，所以如果可以重用线程，则可以减去新建/终止的开销以提升性能。同时，使用线程池的语法比自己新建线程执行线程更加简洁。
# Python为我们提供了ThreadPoolExecutor来实现线程池，此线程池默认子线程守护。它的适应场景为突发性大量请求或需要大量线程完成任务，但实际任务处理时间较短。


import threading
import time
from concurrent.futures import as_completed
from concurrent.futures.process import ProcessPoolExecutor       # 进程池
from concurrent.futures.thread import ThreadPoolExecutor         # 线程池
from time import sleep


# Exectuor 提供了如下常用方法：
#     submit(fn, *args, **kwargs)：将 fn 函数提交给线程池。*args 代表传给 fn 函数的参数，*kwargs 代表以关键字参数的形式为 fn 函数传入参数。
#     map(func, *iterables, timeout=None, chunksize=1)：该函数类似于全局函数 map(func, *iterables)，只是该函数将会启动多个线程，以异步方式立即对 iterables 执行 map 处理。
#     shutdown(wait=True)：关闭线程池。

# 程序将 task 函数提交（submit）给线程池后，submit 方法会返回一个 Future 对象，Future 类主要用于获取线程任务函数的返回值。由于线程任务会在新线程中以异步方式执行，因此，线程执行的函数相当于一个“将来完成”的任务，所以 Python 使用 Future 来代表。
# Future 提供了如下方法：
#     cancel()：取消该 Future 代表的线程任务。如果该任务正在执行，不可取消，则该方法返回 False；否则，程序会取消该任务，并返回 True。
#     cancelled()：返回 Future 代表的线程任务是否被成功取消。
#     running()：如果该 Future 代表的线程任务正在执行、不可被取消，该方法返回 True。
#     done()：如果该 Funture 代表的线程任务被成功取消或执行完成，则该方法返回 True。
#     result(timeout=None)：获取该 Future 代表的线程任务最后返回的结果。如果 Future 代表的线程任务还未完成，该方法将会阻塞当前线程，其中 timeout 参数指定最多阻塞多少秒。
#     exception(timeout=None)：获取该 Future 代表的线程任务所引发的异常。如果该任务成功完成，没有异常，则该方法返回 None。
#     add_done_callback(fn)：为该 Future 代表的线程任务注册一个“回调函数”，当该任务成功完成时，程序会自动触发该 fn 函数。


# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum

def demo():
    # 创建一个包含2条线程的线程池
    pool = ThreadPoolExecutor(max_workers=2)

    # 向线程池提交一个task, 50会作为action()函数的参数
    future1 = pool.submit(action, 5)
    # 向线程池再提交一个task, 100会作为action()函数的参数
    future2 = pool.submit(action, 10)

    # 判断future1代表的任务是否结束
    print(future1.done())

    time.sleep(3)

    # 判断future2代表的任务是否结束
    print(future2.done())

    # 查看future1代表的任务返回的结果，但result()会阻塞当前主线程，只有等到钱程任务完成后，result() 方法的阻塞才会被解除。
    # print(future1.result())
    # 查看future2代表的任务返回的结果
    # print(future2.result())

    # 关闭线程池
    pool.shutdown()

def demo2():
    with ThreadPoolExecutor(max_workers=2) as pool:
        # 向线程池提交一个task, 50会作为action()函数的参数
        future1 = pool.submit(action, 5)
        # 向线程池再提交一个task, 100会作为action()函数的参数
        future2 = pool.submit(action, 10)

        def get_result(future):
            print(future.result())

        # 由于result()会阻塞当前主线程，可通过Future的add_done_callback()方法来添加回调函数
        # 该回调函数形如fn(future)。当线程任务完成后，程序会自动触发该回调函数，并将对应的Future对象作为参数传给该回调函数

        # 为future1添加线程完成的回调函数
        future1.add_done_callback(get_result)
        # 为future2添加线程完成的回调函数
        future2.add_done_callback(get_result)


# fun为定义的待运行函数
def task(num):
    for i in num:
        print('exec task ...')

def demo3():
    # map(func, *iterables, timeout=None, chunksize=1)方法，该方法的功能类似于全局函数map()，区别在于线程池的map()方法会为iterables的每个元素启动一个线程，以并发方式来执行func函数。
    # 这种方式相当于启动len(iterables)个线程，井收集每个线程的执行结果。

    with ThreadPoolExecutor(max_workers=5) as pool:
        results = pool.map(action, (5, 10, 15))
        for res in results:
            # 最后收集的action()函数的执行结果，依然与传入参数的结果保持一致
            print(res)

    # with ThreadPoolExecutor(max_workers=5) as executor:
    #     _list = ['遍历值', '', '']
    #     ans = [executor.submit(task, i) for i in _list]
    #     for res in as_completed(ans):
    #         print(res.result())



# 其中max_workers为线程池中的线程个数，常用的遍历方法有map和submit+as_completed。根据业务场景的不同，若我们需要输出结果按遍历顺序返回，我们就用map方法，若想谁先完成就返回谁，我们就用submit+as_complete方法。







if __name__ == '__main__':
    # demo()
    # demo2()
    demo3()

