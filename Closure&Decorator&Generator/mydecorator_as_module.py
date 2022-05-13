
# 定义装饰器
def decorator(func):
    print('装饰器执行了')
    def inner():
        print('test()登录验证进行中...')
        func()
    return inner

@decorator        # 实际就是对 comment = decorator(comment) 的封装  comment=inner
def comment():
    print('发表评论')


# comment()        # 此处注释掉，作为test_time文件调用测试对比






































