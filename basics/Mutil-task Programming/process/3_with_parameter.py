import multiprocessing

def show_info(name, age):
    print(name, age)

if __name__ == '__main__':
    # 以元组方式传参，参数顺序需一致(位置参数)
    sub_process1 = multiprocessing.Process(target=show_info, args=('huang', 22))
    sub_process1.start()

    # 以字典方式传参，键值对应即可，无需顺序(关键字参数)
    sub_process2 = multiprocessing.Process(target=show_info, kwargs={'age': 22, 'name': 'huang'})
    sub_process2.start()

    # 同时用元组，字典传参
    sub_process3 = multiprocessing.Process(target=show_info, args=('huang', ), kwargs={'age': 22})
    # sub_process3 = multiprocessing.Process(target=show_info, kwargs={'age': 22}, args=('huang',))
    sub_process3.start()






















