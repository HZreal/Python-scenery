import multiprocessing
from time import *
import os

def dance():
    # 获取当前进程(此处为子进程)的id
    dance_process_id = os.getpid()
    print('dance_process_id:', dance_process_id, '\t\t子进程对象:', multiprocessing.current_process())
    # 获取当前进程的父进程的id
    dance_process_parent_id = os.getppid()
    print('dance父进程id:', dance_process_parent_id)

    for i in range(3):
        print('跳舞中...')
        sleep(0.2)
        # 扩展: 根据进程编号杀死指定进程
        # os.kill(dance_process_id, 9)

def sing():
    sing_process_id = os.getpid()
    print('sing_process_id:', sing_process_id, '\t\t子进程对象:', multiprocessing.current_process())

    sing_process_parent_id = os.getppid()
    print('sing父进程id', sing_process_parent_id)

    for i in range(3):
        print('唱歌中...')
        sleep(0.2)



if __name__ == '__main__':
    # 获取当前进程(此处为主进程)的id
    main_process_id = os.getpid()
    # 获取当前主进程对象:multiprocessing.current_process()  用来查看当前代码是由哪个进程执行
    print('主进程id:', main_process_id, '\t\t主进程对象:', multiprocessing.current_process())

    # 创建两个子进程
    dance_process = multiprocessing.Process(target=dance,name='dance_process')
    print('dance子进程对象:', dance_process)
    sing_process = multiprocessing.Process(target=sing, name='sing_process')
    print('sing子进程对象:', sing_process)

    sing_process.start()
    dance_process.start()

# 执行结果是两个子进程的父进程id与当前主进程一致，即两个子进程的父进程是当前主进程

















































































































