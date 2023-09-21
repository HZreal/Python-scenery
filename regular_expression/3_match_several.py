# 匹配多个字符
# *   匹配前一个字符0次或者无限次，即可有可无
# +   匹配前一个字符1次或者无限次，即至少一次
# ？   匹配前一个字符0次或者1次，即要么一次要么没有，如http和https
# {m}   匹配前一个字符只能出现m次
# {m,n}  匹配前一个字符出现m到n次

import re

# *   匹配前一个字符0次或者无限次，即可有可无
match_obj = re.match('tw*o', 'twwwwwwwwo')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')

match_obj = re.match('t.*o', 'tsdfgwo')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')

# +   匹配前一个字符1次或者无限次，即至少一次
# match_obj = re.match('t.+o','to')      # 匹配失败
match_obj = re.match('t.+o', 'trgjyo')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')

# ？   匹配前一个字符0次或者1次，即要么一次要么没有，如http和https
match_obj = re.match('https?', 'http')
# match_obj = re.match('https?','https')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')

# {m}   匹配前一个字符只能出现m次
match_obj = re.match('ht{2}p', 'http')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')

# {m,n}  匹配前一个字符出现m到n次
match_obj = re.match('ht{1,3}p', 'http')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')

# {m,}  匹配前一个字符至少出现m次
match_obj = re.match('ht{2,}p', 'htttttp')
if match_obj:
    print(match_obj.group())
else:
    print('匹配失败')
