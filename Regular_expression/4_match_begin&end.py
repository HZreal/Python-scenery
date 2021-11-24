# ^   匹配以指定字符串开头
# $   匹配以指定字符串结尾
# [^指定字符]   表示除了指定字符都匹配
import re


# ^   匹配以指定字符串开头
match_obj = re.match('^\d.*', '1abc')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')


# $   匹配以指定字符串结尾
match_obj = re.match('.*\d$', '1abc1')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')

match_obj = re.match('^\d.*\d$', '2abfjdc5')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')


# [^指定字符]   表示除了指定字符都匹配
match_obj = re.match('.*^\d[^47]$', '1abc5')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')












































































