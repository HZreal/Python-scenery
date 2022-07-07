# 主进程会等待所有的子进程执行结束再结束
# 若让主进程停止时，子进程跟随销毁不再执行，只需设置子进程守护主进程即可
import multiprocessing
import time

def task():
    while True:       # 死循环
        print('子进程任务中...')
        time.sleep(0.5)

if __name__ == '__main__':

    sub_process = multiprocessing.Process(target=task)
    # 1. 将子进程设置守护主进程，主进程退出后子进程直接销毁
    sub_process.daemon = True
    sub_process.start()

    # 主进程等待2s
    time.sleep(2)
    # 2. 主进程退出前先让子进程销毁
    sub_process.terminate()
    print('main process over')

# 结论：主进程正常情况下会等待子进程完成之后再退出
# 如何解决强制主进程退出，销毁子进程？
# 1. 让子进程设置守护主进程，主进程提出则子进程销毁
# 2. 主进程退出前先让子进程销毁














