# 导入线程模块
import threading
# 与进程创建类似
# Thread(group, target, name, args, kwargs)

import time


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
