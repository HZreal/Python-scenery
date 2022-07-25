# 正则表达式可以包含一些可选标志修饰符来控制匹配的模式
# 修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志
import re

# re.S
# 表示 “.” 的作用扩展到整个字符串，包括“\n”
a = '''asdfhellopass:
    123worldaf
    '''

# ps:     .*？ 表示匹配任意字符到下一个符合条件的字符
# 如 a.*?bbb  可以匹配 acbbb  abbbbb  accccccccbbb

b = re.findall('hello(.*?)world', a)
c = re.findall('hello(.*?)world', a, re.S)
print('b is ', b)
print('c is ', c)
# “.”的作用是匹配除“\n”以外的任何字符，也就是说，它是在一行中进行匹配。这里的“行”是以“\n”进行区分的。a字符串有每行的末尾有一个“\n”
# 如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。


# re.I
# 不区分大小写
res = re.findall(r"A", "abc", re.I)
print(res)

# re.M多行模式
# 将所有行的尾字母输出
s = '12 34\n56 78\n90'
print(s)
s1 = re.findall(r'^\d+', s, re.M)  # 匹配位于行首的数字
s2 = re.findall(r'\A\d+', s, re.M)  # 匹配位于字符串开头的数字
s3 = re.findall(r'\d+$', s, re.M)  # 匹配位于行尾的数字
s4 = re.findall(r'\d+\Z', s, re.M)  # 匹配位于字符串尾的数字
print(s1, s2, s3, s4)


str1 = "Python's features"
str2 = re.match(r'(.*)on(.*?) .*', str1, re.M | re.I)
print(str2.group())
print(str2.span())         # 匹配到的字符串的索引位置
print(str2.group(1))
print(str2.group(2))
