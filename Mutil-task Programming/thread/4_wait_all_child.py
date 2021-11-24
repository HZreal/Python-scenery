# 主线程会等待所有的子线程执行结束再结束
# 两种办法解决
import threading
import time

def task():
    while True:
        print('任务中...')
        time.sleep(0.3)

if __name__ == '__main__':
    # sub_thread = threading.Thread(target=task)

    # 1. daemon=True参数表示创建的子线程守护主线程，主线程退出时子线程直接销毁
    # sub_thread = threading.Thread(target=task, daemon=True)

    # 2. 把子线程设置成守护主线程
    sub_thread = threading.Thread(target=task)
    sub_thread.setDaemon(True)

    sub_thread.start()
    time.sleep(1)
    print('over')
    # exit()





















