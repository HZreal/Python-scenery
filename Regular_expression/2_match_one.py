# 匹配单个字符
# .        匹配任意一个字符，除了换行符\n
# []       匹配中括号中列举的任意一个字符
# \d       匹配一个数字，即0-9
# \D       匹配一个非数字
# \s       匹配一个空白字符，即空格，tab等
# \S       匹配一个非空白
# \w       匹配一个非特殊字符，即a-z, A-Z, 0-9， 下划线_， 汉字
# \W       匹配一个特殊字符，即非字母，非数字，非汉字, 非下划线

import re

# .   匹配任意一个字符，除了换行符\n
result = re.match('t.o', 'tfo')
# result = re.match('t.o','t\no')    # 匹配失败
if result:  # 匹配存在
    print(result.group())
else:
    print('匹配失败')

# []   匹配任意一个中括号中列举的字符
result = re.match('葫芦娃[12]', '葫芦娃1')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')

result = re.match('[0123456789]', '7')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')
result = re.match('[0-9]', '7')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')

# \d   匹配一个数字，即0-9
#  \d 等价于 [0-9]
result = re.match('\d', '7')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')

# \D   匹配一个非数字
result = re.match('\D', 'aa')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')

# \s   匹配一个空白字符，即空格，tab等
result = re.match('葫芦娃\s[12]', '葫芦娃 1')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')

result = re.match('葫芦娃\s[12]', '葫芦娃\t1')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')

# \S   匹配一个非空白
# result = re.match('葫芦娃\S[12]','葫芦娃 1')     # 匹配失败
result = re.match('葫芦娃\S[12]', '葫芦娃+1')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')

# \w   匹配一个非特殊字符，即a-z, A-Z, 0-9， 下划线_， 汉字
result = re.match('[a-zA-Z0-9_]', '_')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')

result = re.match('\w', '_')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')

result = re.match('\w', '厉害')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')

# \W   匹配一个特殊字符，即非字母，非数字，非汉字, 非下划线
# result = re.match('\W','黄')      # 匹配失败
# result = re.match('\W','_')       # 匹配失败
result = re.match('\W', '$')
# result = re.match('\W','%')
if result:
    # 匹配存在
    print(result.group())
else:
    print('匹配失败')
