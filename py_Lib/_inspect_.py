# inspect模块
# inspect模块主要提供了四种用处：
# 　　1.对是否是模块、框架、函数进行类型检查
# 　　2.获取源码
# 　　3.获取类或者函数的参数信息
# 　　4.解析堆栈

import inspect

# 一、type and members
# 1. inspect.getmembers(object[, predicate])
# 返回值为对象的所有成员，为一个元组列表，列表元素是元组（name, value）

class Obj:
    a = 1

    def func(self):
        pass

obj = Obj()
print(inspect.getmembers(obj))

# 第二个参数通常可以根据需要调用如下16个方法；
# inspect.ismodule(object)                    # 是否为模块
# inspect.isclass(object)                     # 是否为类
# inspect.ismethod(object)                    # 是否为方法（bound method written in python）
# inspect.isfunction(object)                  # 是否为函数(python function, including lambda expression)
# inspect.isgeneratorfunction(object)         # 是否为python生成器函数
# inspect.isgenerator(object)                 # 是否为生成器
# inspect.istraceback(object)                 # 是否为traceback
# inspect.isframe(object)                     # 是否为frame
# inspect.iscode(object)                      # 是否为code
# inspect.isbuiltin(object)                   # 是否为built-in函数或built-in方法
# inspect.isroutine(object)                   # 是否为用户自定义或者built-in函数或方法
# inspect.isabstract(object)                  # 是否为抽象基类
# inspect.ismethoddescriptor(object)                 # 是否为方法标识符
# inspect.isdatadescriptor(object)                   # 是否为数字标识符，数字标识符有__get__ 和__set__属性； 通常也有__name__和__doc__属性
# inspect.isgetsetdescriptor(object)                 # 是否为getset descriptor
# inspect.ismemberdescriptor(object)                 # 是否为member descriptor
b = inspect.getmembers(obj, inspect.isclass(obj))

# inspect的getmembers()方法可以获取对象（module、class、method等）的如下属性：
# module：   __doc__
#  	         __file__
# class：	 __doc__
#  	         __module__
# method：	 __doc__
#  	         __name__
#  	         im_class
#  	         im_func or __func__
#  	         im_self or __self__


# 2. inspect.getmoduleinfo(path)： 返回一个命名元组<named tuple>(name, suffix, mode, module_type)
#       name：模块名（不包括其所在的package）
#       suffix：
#       mode：open()方法的模式，如：'r', 'a'等
#       module_type: 整数，代表了模块的类型


# 3. inspect.getmodulename(path)：根据path返回模块名（不包括其所在的package）


# 二、Retrieving source code
# 1. inspect.getdoc(object)： 获取object的documentation信息
# 2. inspect.getcomments(object)
# 3. inspect.getfile(object): 返回对象的文件名
# 4. inspect.getmodule(object)：返回object所属的模块名
# 5. inspect.getsourcefile(object)： 返回object的python源文件名；object不能使built-in的module, class, mothod
# 6. inspect.getsourcelines(object)：返回object的python源文件代码的内容，行号+代码行
# 7. inspect.getsource(object)：以string形式返回object的源代码
# 8. inspect.cleandoc(doc)：


# 三、class and functions
# 1. inspect.getclasstree(classes[, unique])
# 2. inspect.getargspec(func)
# 3. inspect.getargvalues(frame)
# 4. inspect.formatargspec(args[, varargs, varkw, defaults, formatarg, formatvarargs, formatvarkw, formatvalue, join])
# 5. inspect.formatargvalues(args[, varargs, varkw, locals, formatarg, formatvarargs, formatvarkw, formatvalue, join])
# 6. inspect.getmro(cls)： 元组形式返回cls类的基类（包括cls类），以method resolution顺序;通常cls类为元素的第一个元素
# 7. inspect.getcallargs(func[, *args][, **kwds])：将args和kwds参数到绑定到为func的参数名；对bound方法，也绑定第一个参数（通常为self）到相应的实例；返回字典，对应参数名及其值；

# >>> from inspect import getcallargs
# >>> def f(a, b=1, *pos, **named):
# ...     pass
# >>> getcallargs(f, 1, 2, 3)
# {'a': 1, 'named': {}, 'b': 2, 'pos': (3,)}
# >>> getcallargs(f, a=2, x=4)
# {'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()}
# >>> getcallargs(f)
# Traceback (most recent call last):
# ...
# TypeError: f() takes at least 1 argument (0 given)


# 四、The interpreter stack
# 1. inspect.getframeinfo(frame[, context])
# 2. inspect.getouterframes(frame[, context])
# 3. inspect.getinnerframes(traceback[, context])
# 4. inspect.currentframe()
# 5. inspect.stack([context])
# 6. inspect.trace([context])
