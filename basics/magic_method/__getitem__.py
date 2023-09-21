
# 返回所给键对应的值。当对象是序列时，键是整数。当对象是映射时（字典），键是任意值。

class Fib():  # 定义类Fib
    def __init__(self, start=0, step=1):
        self.step = step

    def __getitem__(self, key):  # 定性__getitem__函数，key为类Fib的键
        a = key + self.step
        return a  # 当按照键取值时，返回的值为a


s = Fib()
ret = s[1]  # 返回2 ，因为类有 __getitem__方法，所以可以直接通过键来取对应的值
print(ret)





