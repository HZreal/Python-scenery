import threading
# 与进程创建类似
# Thread(group, target, name, args, kwargs)
import time


# 线程
#     共享变量（解决了通讯麻烦的问题，但是对于变量的访问需要加锁）
#     调度由操作系统完成（由于共享内存，上下文切换变得高效）
#     一个进程可以有多个线程，每个线程会共享父进程的资源（创建线程开销占用比进程小很多，可创建的数量也会很多）
#     通讯除了可使用进程间通讯的方式，还可以通过共享内存的方式进行通信（通过共享内存通信比通过内核要快很多）

# 注意：Python的线程并不是标准线程，是系统级进程，线程间上下文切换有开销，
# 而且Python在执行多线程时默认加了一个全局解释器锁（GIL），因此Python的多线程其实是串行的，所以并不能利用多核的优势，也就是说一个进程内的多个线程只能使用一个CPU。


def sing():
    # 获取当前线程(子线程)
    sing_thread = threading.current_thread()
    print(sing_thread, sing_thread.getName(), sing_thread.ident)
    for i in range(3):
        print('唱歌中...')
        time.sleep(0.2)


def dance():
    dance_thread = threading.current_thread()
    # 当前子线程对象,当前线程名,当前线程id
    print(dance_thread, dance_thread.getName(), dance_thread.ident)
    for j in range(3):
        print('跳舞中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 获取当前线程(主线程)
    main_thread = threading.current_thread()
    # 当前主线程对象,当前线程名,当前线程id
    print(main_thread, main_thread.getName(), main_thread.ident)

    # 创建子线程
    sing_thread = threading.Thread(target=sing, name='sing')
    dance_thread = threading.Thread(target=dance, name='dance')

    # 启动子线程
    sing_thread.start()
    dance_thread.start()
