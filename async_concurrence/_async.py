# python 异步协程并发

# 并发编程的一个好处就是可以让数量有限的CPU核心，“看起来”同时执行数量远远大于核心数量的任务，换句话说，增加系统的对请求的响应程度。
# 并发模型最常见的程序其实就是操作系统，一个普通的操作系统运行在一个8核CPU上，却可以“看起来”同时执行成千上万个任务，这就是并发模型的效果。

# Python提供了三种并发的工具：多线程（threading）、多进程（process）和协程（Coroutine）。前两种其实就是利用了操作系统提供的并发模型。
# Python会根据操作系统调用对应系统的线程API，然后把调度工作移交OS。这里需要注意的是，由于GIL的存在，每一个Python解释器进程中，同一时间只能有一个线程执行。这意味着，在这种情况下，利用线程实现的并发模型中，不存在并行。
# 弊端也很明显：
#     线程创建和切换的开销相对较大，数量有限
#     移交操作系统调度后，程序员基本失去了对任务的控制，属于抢占式
# 为了解决上面的弊端，Python也给出了协程的方案。协程跟线程的最大区别就是：协程是协作式的，线程是抢占式的。具体讲就是一个协程会在预订的位置让出执行权，并且主动的移交给其他协程，而线程则是抢占式的，一个线程会在任意时间被夺去执行权。

# 协程，调度完全由用户控制
#     一个线程（进程）可以有多个协程
#     每个线程（进程）循环按照指定的任务清单顺序完成不同的任务（当任务被堵塞时，执行下一个任务；当恢复时，再回来执行这个任务；任务间切换只需要保存任务的上下文，没有内核的开销，可以不加锁的访问全局变量）
#     协程需要保证是非堵塞的，且没有相互依赖
#     协程基本上不能同步通讯，多采用异步的消息通讯，效率比较高

# python协程奉行共享内存来通信，而不是通过通信来共享内存(GO语言协程直接通过channel通信)
# 在协程函数内部 return 任意的Python内置类型、例如整数、字符串、列表、或任意object的派生类型，Python解释器默许你这么做。这是合法的，Python会隐式封装成一个可等待对象返回。

#   event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数（协程）注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。执行协程函数，必须使用事件循环!
#   coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
#   future 对象： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别。
#   task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。Task 对象是 Future 的子类，它将 coroutine 和 Future 联系在一起，将 coroutine 封装成一个 Future 对象。

# asyncio流程：
#     1、定义/创建协程对象；
#     2、定义事件循环对象容器；
#     3、将协程转化为task对象；
#     4、将task任务扔进事件循环对象中触发。
# 协程对象：执行协程函数得到的对象
# 执行协程函数得到协程对象，函数内部代码不会执行
# 执行协程函数内部代码，必须把协程对象交给事件循环处理

# await + 可等待对象（协程对象，Future对象，Task对象（IO等待））   等待到对象的返回结果，才会继续执行后续代码
# await调用被async def定义的函数或者实现了__await__()的类
# await 的作用就是等待当前的协程运行结束之后再继续进行下面代码。

# asyncio 库的 sleep() 机制与 time.sleep() 不同, 前者是 “假性睡眠”, 模拟协程函数的睡眠，后者是会导致线程阻塞的 "真性睡眠"


import asyncio
import time
import random
import typing

import requests



class A:
    def __init__(self):
        pass
    def __await__(self):
        pass

async def hello():
    # await A()
    await asyncio.sleep(1)
    print('executing hello function ...')
    return 'data from hello function'
# print(hello())               # <coroutine object>  执行协程函数得到协程对象，函数内部代码不会执行
# print(hello().send(None))

def asyncio_attr_func():
    # 协程对象、asyncio的相关属性方法等
    g = hello().__await__()
    is_coroutine = asyncio.iscoroutine(hello())
    is_coroutine_function = asyncio.iscoroutinefunction(hello())
    awaitable = isinstance(hello(), typing.Awaitable)
    coroutine = isinstance(hello(), typing.Coroutine)
    is_await = hasattr(hello(), '__await__')
    print(g, is_coroutine, is_coroutine_function, awaitable, coroutine, is_await)

def run():
    # 创建一个事件循环对象，用于管理协程
    event_loop = asyncio.get_event_loop()
    # 时间循环调度执行协程(参数可以是一个协程，或者一个task对象)
    res = event_loop.run_until_complete(hello())
    print('res ----  ', res)


#####################################################################################################################
# await等待多个协程
async def add_prefix(what, delay=1):
    print('exec add_prefix time ----->  ', time.strftime('%X'))
    await asyncio.sleep(delay)
    return what + '!!!str!!!  '

async def run1():
    print(f"started at {time.strftime('%X')}")

    s1 = await add_prefix('hello', 1)    # 此语句执行完之后，才继续向下执行，好像与正常的顺序执行逻辑没有什么不同
    s2 = await add_prefix('world', 2)
    print(s1 + s2)

    print(f"finished at {time.strftime('%X')}")

async def run2():
    # 创建两个任务，两个任务被调度执行，后续在需要的地方await阻塞获取结果
    # asyncio.create_task方法封装了创建事件循环对象loop并调用loop.create_task创建task
    task1 = asyncio.create_task(add_prefix('hello', 1))
    task2 = asyncio.create_task(add_prefix('world', 2))

    print(f"started at {time.strftime('%X')}")

    # 获取task1的结果
    await task1
    s1 = task1.result()
    # 获取task2的结果
    s2 = await task2

    # 使用两个协程的结果进一步处理
    print(s1 + s2)

    print(f"finished at {time.strftime('%X')}")


#####################################################################################################################
# 模拟爬虫
url_list = [
    "https://www.baidu.com",
    "https://www.baidu.com",
    "https://www.baidu.com",
]

# 正常的完全同步执行
def http_request1(url):
    res = requests.get(url)
    return res.status_code

def spider1():
    start_time = time.time()
    print("start_time:", start_time)

    for url in url_list:
        code = http_request1(url)
        print('code --->  ', code)

    end_time = time.time()
    sep_time = end_time - start_time
    print("end_time:  ", end_time)
    print("all_execute_time:", sep_time)

# 使用协程，提高了程序的执行效率，程序数量越多，越能体现出协程对程序的执行效率越高
async def http_request2(url):
    res = requests.get(url)
    return res.status_code

async def spider2():
    start_time = time.time()
    print(f"start_time:{start_time}\n")

    for url in url_list:
        code = await http_request2(url)
        print('code --->  ', code)

    end_time = time.time()
    sep_time = end_time - start_time
    print("end_time:  ", end_time)
    print("all_execute_time:  ", sep_time)


#####################################################################################################################
start = time.time()

def take_time():
    return "%1.2f秒" % (time.time() - start)

async def task_A():
    print("运行task_A")
    await asyncio.sleep(random.uniform(1.0, 8.0) / 10)
    print(f"task_A结束!!耗时{take_time()}")

async def task_B():
    print("运行task_B")
    await asyncio.sleep(random.uniform(1.0, 8.0) / 10)
    print(f"task_B结束!!耗时{take_time()}")

async def task_C():
    print("运行task_C")
    await asyncio.sleep(random.uniform(1.0, 8.0) / 10)
    print(f"task_C结束!!耗时{take_time()}")

async def task_exect():
    cors = [task_A(), task_B(), task_C()]
    await asyncio.gather(*cors)          # 调度顺序按照cors列表元素顺序；若协程有返回值，则gather也会返回一个列表存储，顺序与cors列表一致
# 执行输出:
# 运行task_A
# 运行task_B
# 运行task_C
# task_C结束!!耗时0.56秒
# task_A结束!!耗时0.71秒
# task_B结束!!耗时0.79秒
# 分析:
# task_A、task_B和task_C之间在各自I/O状态等待时间是不可预知的，也就是说三个携程的各自await语句的后半部分的代码执行顺序是随机。


#####################################################################################################################



if __name__ == "__main__":

    asyncio_attr_func()

    # 自定义创建事件对象再执行
    # run()

    # py3.7省略了创建事件循环等过程，封装在run方法中直接执行协程，执行完成后创建的事件循环被关闭。
    # asyncio.run(hello())

    # asyncio.run(run1())
    # asyncio.run(run2())

    # spider1()
    # asyncio.run(spider2())

    # asyncio.run(task_exect())

    pass























