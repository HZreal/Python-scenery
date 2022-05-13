# __repr__ 与 __str__

# __repr__  目标是毫不含糊    ---------  面向程序员，程序调用，显示专业的开发者详细信息
# __str__   目标是可读       ---------  面向用户，显示用户友好型信息
# print打印操作时会首先尝试调用__str__，它通常应该返回一个用户友好型的显示。若未定义__str__，则调用__repr__进行显示
# 实际上，定义了__str__后，当进行print操作，__str__将覆盖__repr__被调用
# __repr__用于所有其他的环境中：用于交互模式下提示回应以及repr函数，如果没有使用__str__，会使用print和str。它通常应该返回一个编码字符串，可以用来重新创建对象，或者给开发者详细的显示
# 当我们想所有环境下都统一显示的话，可以直接重构定义__repr__方法；
# 当我们想在不同环境下支持不同的显示，例如终端用户显示使用__str__，而程序员在开发期间则使用底层的__repr__来显示



class Test:
    def __init__(self, data):
        self.data = data

# 在 python console 中执行
# >>> t = Test()
# >>> t
# <__main__.Test at 0x7fa91c307190>
# >>> print(t)
# <__main__.Test object at 0x7fa91c307190>


# 重构__repr__
# 重构__repr__方法后，不管直接输出对象还是通过print打印，都执行的是重构的__repr__
class TestRepr(Test):
    def __repr__(self):
        return 'TestRepr(%s)' % self.data

# >>> tr = TestRepr()
# >>> tr                              直接终端控制台输出，不使用print，面向程序
# TestRepr(hello, world!)
# >>> print(tr)                       print是面向用户
# TestRepr(hello, world!)


# 重构__str__
# 重构__str__方法后，print打印时，__str__会将__repr__覆盖，故执行的是重构的__str__；直接输出对象还是执行的是__repr__
class TestStr(Test):
    def __str__(self):
        return '[Value: %s]' % self.data

# >>> ts = TestStr()
# >>> ts                                            直接输出对象时并没有按__str__方法中的内容进行输出
# <__main__.TestStr at 0x7fa91c314e50>
# >>> print(ts)
# [Value: hello, world!]                            用print输出时显示__str__的内容








