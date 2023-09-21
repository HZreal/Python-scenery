import signal
import time







def run():
    # 3秒后终止程序
    print(signal.alarm(3))  # output:0
    time.sleep(1)
    print(signal.alarm(3))  # output:2

    # 阻塞等待信号的发生，无论什么信号都可以。
    # signal.pause()                   # 使程序进入休眠直到程序接收到某个信号量

    while True:
        time.sleep(1)
        print("working")

def _handle_timeout(signum, frame):
    # err_msg = f'Function {func.__name__} timed out after {sec} seconds'
    # device_status = get_redis_connection('default')
    # device_status.set('handing', 'fail')
    # raise TimeoutError(err_msg)
    pass

def run2():
    # 获取当前程序注册signalnum信号量的处理函数
    signal.getsignal(1)

    # 按照handler处理器制定的信号处理方案处理函数
    # signal.signal(sig, handler)
    # signal.signal(signal.SIGINT, signal.SIG_IGN)           # 当遇到SIGINT即CTRL+C时忽略SIG_IGN
    signal.signal(signal.SIGALRM, _handle_timeout)

    # 信号拦截
    # 第一种是发出kill信号
    # SIGTERM 表示关闭程序信号
    # signal.signal(signal.SIGTERM, self._term_handler)
    # 第二种是发出 CTRL+C 信号
    # SIGINT表示CTRL+C信号
    # signal.signal(signal.SIGINT, self._term_handler)

if __name__ == '__main__':
    run()




