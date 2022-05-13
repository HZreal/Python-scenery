# 闭包的使用

def config_name(name):

    def talk_info(info):

        print(name + ':' +    info)

    return talk_info


func_ = config_name('Tom')
func_('你吃饭了吗？')


# 下条语句能够执行
# config_name('Tom')('吃饭了吗？')





# 闭包在数据处理方面高效便捷性
# 如果想计算：y = a * x + b 的值利用一般函数计算要传递三个参数并且，当要计算多组值时就变得非常繁琐
# 但是，利用闭包来计算就非常简便
def line(a,b):
    def line_inner(x):
        return a*x+b
    return line_inner

line1 = line(2,4)
line2 = line(1,5)

print("y=2x+4 当x=2时 值为：%d" % line1(2)) #计算2x+4 当x=2时的值
print("y=2x+4 当x=3时 值为：%d" % line1(3)) #计算2x+4 当x=3时的值

print("y=x+5 当x=2时 值为：%d" % line2(2)) #计算x+5 当x=2时的值
print("y=x+5 当x=3时 值为：%d" % line2(3)) #计算x+5 当x=3时的值














