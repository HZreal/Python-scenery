

# args合并
args1 = ('value1', 'value2')
args2 = ('value3', 'value4', 'value5')
args12 = (*args1, *args2)
print(args12)


# kwargs合并
kwargs1 = {'key1': 'value1', 'key2': 'value2'}
kwargs2 = {'key3': 'value3', 'key4': 'value4'}
kwargs12 = {**kwargs1, **kwargs2}
print(kwargs12)



# *args与**kwargs传参

params1 = {'name': 'huang', 'age': 24, 'interest': 'python', 'date_time': 2021}
params2 = ('huang', 24, 'mysql', 'kotlin')

def run(name: str, age: int, *args, **kwargs):
    print(name, age)

    print(args)          # 此时的args为位置传参后 剩余的参数元组
    print(kwargs)        # 此时的kwargs为关键字传参后 剩余的参数字典

run(**params1)     # 将字典按照关键字传参,未传入的参数放在kwargs里
run(*params2)        # 将元组按照位置传参,未传入的参数放在args里


