# *args与**kwargs传参


kwargs = {'name': 'huang', 'age': 24, 'interest': 'python', 'date_time': 2021}
args = ('huang', 24, 'mysql', 'kotlin')


def run(name: str, age: int, *args, **kwargs):
    print(name, age)

    print(args)          # 此时的args为位置传参后 剩余的参数元组
    print(kwargs)        # 此时的kwargs为关键字传参后 剩余的参数字典


if __name__ == '__main__':

    run(**kwargs)     # 将字典按照关键字传参,未传入的参数放在kwargs里
    print('-----------------------------------------')
    print('-----------------------------------------')
    run(*args)        # 将元组按照位置传参,未传入的参数放在args里

