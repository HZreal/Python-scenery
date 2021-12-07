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