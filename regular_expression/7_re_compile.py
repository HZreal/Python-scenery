import re

pattern = re.compile('is')

# string1 = 'this is a file'
# res_list = pattern.findall(string1)
# print(res_list)

string2 = 'this is a file'
match_obj = pattern.match(string2)
if match_obj:
    print(match_obj.group())
else:
    print('no match')


string3 = 'this is a file'
match_obj = pattern.search(string2)
if match_obj:
    print(match_obj.group())
else:
    print('no match')