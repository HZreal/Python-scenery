# |    匹配左右任意一个结果
# (abcd)    将括号中的字符作为一个分组(一个整体)
# \num    引用第num个分组
# (?P<name>)      对分组起别名为name
# (?P=<name>)     引用别名为name的分组，匹配相同的字符串


import re


# |    匹配左右任意一个结果
fruit_list = ['apple', 'banana', 'orange', 'pear', 'peach']
for value in fruit_list:
    # 对每个字符串进行正则匹配
    match_obj = re.match('banana|pear', value)
    if match_obj:
        print(f'我想吃的水果:{match_obj.group()}')
    else:
        print('我不想吃的水果:', value)


# (ab)    将括号中的字符作为一个分组(一个整体)
# 例如：匹配出163、126、qq邮箱
# !!!!!!出现一个小括号就是一个分组，分组索引是从1开始的，且顺序是从左到右依次排序
match_obj = re.match('([a-zA-Z0-9_]{4,20})@(163|126|qq)\.com', 'hello@163.com')
# .  表示匹配任意一个字符， 用\转义变成真正的.字符，否则邮箱那个点改成任意其他字符也能匹配
print(type(match_obj))
if match_obj:
    print(match_obj.group())          # 默认是0，取整个匹配结果
    print('获取匹配到的第一个分组：', match_obj.group(1), '\n获取匹配到的第二个分组：', match_obj.group(2), '\n匹配结果：', match_obj.group(0))         # 获取第2个分组
    print('span方法 匹配到的字符串的索引位置，返回元祖-----', match_obj.span())
else:
    print('匹配失败')

# 匹配5~12位qq号码(首位非0)
match_obj = re.match('qq:([1-9]\d{4,11})', 'qq:3014587')
if match_obj:
    print(match_obj.group())      # qq:3014587
    print(match_obj.group(1))     #获取第一个分组，结果是 3014587
else:
    print('匹配失败')


# \num    引用第num个分组
# 匹配标签
match_obj = re.match('<[a-zA-Z1-6]+>.*</[a-zA-Z1-6]+>','<html>hh</html>')
# match_obj = re.match('<[a-zA-Z1-6]+>.*</[a-zA-Z1-6]+>','<html>hh</div>')
# 此时<html>hhhh</div>也能匹配成功，但不合实际，需要用到引用分组
if match_obj:
    print(match_obj.group())     # <html>hh</html>
else:
    print('匹配失败')

# 采用引用分组，匹配与前面分组内容相同的字符串
match_obj = re.match('<([a-zA-Z1-6]+)>.*</\\1>','<html>hh</html>')
# 此时<html>hhhh</div>无法匹配了
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')

# 匹配 <html><hl>www.baidu.com</hl></html>
match_obj = re.match('<([a-zA-Z1-6]+)><([a-zA-Z1-6]+)>.*</\\2></\\1>','<html><hl>www.baidu.com</hl></html>')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')


# (?P<name>)      分组起别名为name
# (?P=<name>)     引用别名为name的分组，匹配相同的字符串
match_obj = re.match('<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>','<html><hl>www.baidu.com</hl></html>')
if match_obj:
    print(match_obj.group())     # <html>hh</html>
else:
    print('匹配失败')







































































































































