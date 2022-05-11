# 多个装饰器:
# 多个装饰器的装饰过程是: 离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰，由内到外的装饰过程
# 实际函数调用时，装饰器内部函数inner执行的过程是：最外层的内部函数inner先执行


def make_p(func):
    print('make_p装饰器执行了...')

    def inner1():
        print('调用make_p装饰器的inner----------------')
        result = '<p>' + func() + '</p>'
        return result

    return inner1


def make_div(func):
    print('make_div装饰器执行了...')

    def inner2():
        print('调用make_div装饰器的inner----------------')
        result = '<div>' + func() + '</div>'
        return result

    return inner2


# 装饰过程原理剖析：content = make_div(make_p(content))
# 即：
#   1. content = make_p.inner = make_p(content)
#   2.content = make_div.inner = make_div(content)

@make_div
@make_p
def content():
    return '人生苦短，我 use python'




# content()执行过程原理：
# content的调用content()即是inner2的调用inner2()，inner2调用过程中又去调用inner1，inner1调用过程中又去调用原始的content
result = content()
print(result)
