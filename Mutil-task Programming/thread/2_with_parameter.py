import threading


def show_info(name, age):
    print(name, age)


if __name__ == '__main__':
    # 以元组方式传参
    # sub_thread1 = threading.Thread(target=show_info, args=('huang', 22))
    # sub_thread1.start()
    # 以字典方式传参
    # sub_thread2 = threading.Thread(target=show_info, kwargs={'name': 'huang', 'age': 22})
    # sub_thread2.start()
    # 元组，字典混合传参
    sub_thread3 = threading.Thread(target=show_info, args=('huang',), kwargs={'age': 22})
    sub_thread3.start()






