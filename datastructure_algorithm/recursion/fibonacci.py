def fibo(n):
    """递归函数实现斐波那契数列"""
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def test1():
    n = int(input("请输入数列的项数："))
    res = fibo(n)
    print(res)


def test2():
    n = int(input("请输入数列的项数："))
    fibo = [x[0] for x in [(a[i][0], a.append([a[i][1], a[i][0] + a[i][1]])) for a in ([[1, 1]],) for i in range(n)]]
    print(fibo)

if __name__ == '__main__':
    # test1()
    test2()