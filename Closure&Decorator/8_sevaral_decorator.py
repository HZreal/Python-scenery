# 多个装饰器:
# 多个装饰器的装饰过程是: 离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰，由内到外的装饰过程



def make_p(func):
    print('make_p装饰器执行了...')
    def inner():
        result = '<p>' + func() + '</p>'
        return result

    return inner

def make_dir(func):
    print('make_div装饰器执行了...')
    def inner():
        result = '<div>' + func() + '</div>'
        return result

    return inner


# 原理剖析：content = make_dir(make_p(content))
# 即：
#   1. content = make_p.inner = make_p(content)
#   2.content = make_dir.inner = make_dir(content)
@make_dir
@make_p
def content():
    return '人生苦短，我爱python'


result = content()
print(result)













































