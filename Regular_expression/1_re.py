# 导入模块
import re

# 使用match方法进行匹配，第一个参数是正则，第二个参数是匹配对象，返回的是一个对象
# match_obj = re.match('hel','hello')

# 使用group方法获取匹配结果，匹配失败，则match_obj是一个None
# result = match_obj.group()
# print(result)


# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
# re.search(pattern, string)         # 扫描整个字符串并返回第一个成功的匹配
# re.sub(pattern, rep, string, count)      # 用于替换字符串中的匹配项
