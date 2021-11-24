# 生成器的应用：    Fibonacci数列  0, 1, 1, 2, 3, 5, 8, 13 ...

def fibonacci(num):     #表示生成的个数
    a = 0
    b = 1
    index = 0
    while index < num:
        c = a          # 记录未交换前的a值
        a, b = b, a + b
        index += 1
        yield c

generator = fibonacci(5)
for i in generator:
    print(i)






































































