# 进程之间不共享全局变量
import multiprocessing
import  time

g_list = []      #全局列表

def add_data():
    for num in range(3):
        # 列表是可变类型，可以在原内存地址处修改数据，且地址不变、
        # 故不需global
        # global 表示声明修改全局变量的内存地址
        g_list.append(num)
        print('添加数据:',num)   
        time.sleep(0.2)
    else:
        print('添加完成:',g_list)

def read_data():
    print(g_list)

if __name__ == '__main__':

    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    add_process.start()
    # 当前主进程等待子进程(数据添加进程)执行完成以后，代码再继续向下执行，即同步
    add_process.join()
    read_process.start()

# 结论：进程之间不共享全局变量
# 主进程创建子进程时，子进程会将主进程的资源拷贝一份，子进程其实就是主进程的一个副本
# 子进程修改全局变量时，实际上是在修改自己拷贝的变量值，并不会改变主进程和其他子进程(也拷贝主进程该变量)的变量值
































































