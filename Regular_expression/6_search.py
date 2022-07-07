import re
sssss = 'abcdefg'
obj = re.search('cde', sssss)          # re.search 扫描整个字符串并返回第一个成功的匹配
if obj:
    print('match对象------', obj)
    result = obj.group()
    index = obj.span()
    a = obj.span()[0]
    b = obj.span()[1]
    start = obj.start()
    end = obj.end()
    print('匹配结果------', result)
    print('匹配串的索引---start=a end=b------>', start, a, end, b, index)         # 打印  2  2  5  5   (2, 5)

print(sssss.find('e'))        # 4







# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
string = 'hello'
pattern = 'll'
# match_1 = re.search(pattern, string)         # 扫描整个字符串并返回第一个成功的匹配
# print(match_1.group())

replaced_string = re.sub(pattern, '22', string, count=2)      # 用于替换字符串中的匹配项
print(replaced_string)




