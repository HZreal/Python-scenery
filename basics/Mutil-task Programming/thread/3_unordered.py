# 线程的执行是无序的，其执行顺序取决于当时CPU调度
import threading
import time


def task():
    time.sleep(1)
    print(threading.current_thread())


if __name__ == '__main__':
    # 循环创建大量线程，测试线程无序
    for i in range(20):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()

# 执行的某次结果：
# <Thread(Thread-1, started 10336)>
# <Thread(Thread-3, started 3044)>
# <Thread(Thread-2, started 11164)>
# <Thread(Thread-6, started 11072)>
# <Thread(Thread-5, started 6888)>
# <Thread(Thread-4, started 9164)>
# <Thread(Thread-9, started 5492)>
# <Thread(Thread-7, started 14056)>
# <Thread(Thread-10, started 13428)>
# <Thread(Thread-11, started 8520)>
# <Thread(Thread-12, started 8868)>
# <Thread(Thread-14, started 5956)>
# <Thread(Thread-17, started 11004)>
# <Thread(Thread-13, started 12448)>
# <Thread(Thread-19, started 13120)>
# <Thread(Thread-8, started 7392)>
# <Thread(Thread-16, started 12828)>
# <Thread(Thread-18, started 10356)>
# <Thread(Thread-20, started 5496)>
# <Thread(Thread-15, started 9940)>
