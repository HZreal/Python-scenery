# 导入进程包
import multiprocessing
from time import *

def dance():
    for i in range(3):
        print('跳舞中...')
        sleep(0.2)       # 休息0.2秒

def sing():
    for i in range(3):
        print('唱歌中...')
        sleep(0.2)       # 休息0.2秒

# 创建子进程(自己手动创建的为子进程)
dance_process = multiprocessing.Process(target=dance)

# 主进程子进程
# if __name__ == '__main__':
#     dance_process.start()     # 子进程执行跳舞
#     sing()      #主进程执行唱歌

 # 两个子进程
sing_process = multiprocessing.Process(target=sing)
if __name__ == '__main__':
    sing_process.start()
    dance_process.start()

# 进程执行是无序的、具体谁先执行由OS调度决定的


















































































































