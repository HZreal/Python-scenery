import threading

lock = threading.Lock()


def get_data(index):
    lock.acquire()
    g_list = [1, 4, 6]
    if i >= len(g_list):
        print('下标越界:', index)
        lock.release()
        return  # 当某个线程判断越界时退出而未释放锁，导致其他线程无尽等待，形成死锁。有了上一句release则解除
    value = g_list[index]
    print(value)
    lock.release()


if __name__ == '__main__':
    for i in range(10):
        sub_thread = threading.Thread(target=get_data, args=(i,))
        sub_thread.start()
