import json
import os
import random
from datetime import datetime


def get_target_count(arr: list):
    num = 0
    temp = []
    for i in arr:
        if (2018 - i) in arr:
            temp.append(2018 - i)
        if i not in temp:
            num += 1
    return num


# arr = [283, 1068, 1735, 283, 950]
# ret = get_target_count(arr)
# print(ret)


# 1 ---- 2 ---- 3 ---- 4 ---- 5 ---- 6 ----


def count():
    with open(r'C:\Users\sizhong\file\project\SEV\源数据\路口斑马线\金牛湖_路口_人行横道\人行横道（金牛湖）.json', 'r') as f:
        dict_data = json.loads(f.read())
        print('count ---->  ', len(dict_data['features']))

    res = []
    for item in dict_data['features']:
        res.append(item['geometry'])

    with open(r'C:\Users\sizhong\file\project\SEV\源数据\路口斑马线\金牛湖_路口_人行横道\人行横道（金牛湖）-处理成可导入.json', 'w') as f2:
        f2.write(json.dumps(res))



def tt():
    import re, json
    with open('111.txt', 'r', encoding='utf8') as f:
        full_str = f.read()

    res1 = re.findall('层级 \d+', full_str, flags=0)
    print(res1)

    res2 = re.findall('高度 \d+\.\d+', full_str, flags=0)
    print(res2)

    rres = [{'level': int(res1[i].split(' ')[1]), 'alt': float(res2[i].split(' ')[1])} for i in range(len(res1))]
    print(rres)

    with open('333.txt', 'w', encoding='utf8') as f:
        f.write(json.dumps(rres))

def aa():
    with open(r'C:\Users\sizhong\file\project\SEV\源数据\车辆位置20230108-9点.json', 'r', encoding='utf8') as f:
        data_list = json.loads(f.read())
    for item in data_list:
        item['battery_capacity'] = round(random.random(), 2)
    with open(r'C:\Users\sizhong\file\project\SEV\源数据\车辆位置20230108-9点-添加电池信息.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(data_list))



if __name__ == '__main__':
    # count()
    # tt()
    aa()



