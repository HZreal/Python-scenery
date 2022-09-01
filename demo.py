import json
import os
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
    with open(r'C:\Users\sizhong\file\project\ft-ts-server\schedule\pop_log5.txt', 'r') as f:
        res = f.readlines()
        count = 0
        for i in res:
            count += int(i.strip())
        print(count)


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


if __name__ == '__main__':
    count()
    # tt()


