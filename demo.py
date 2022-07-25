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



def test_():
    pass




if __name__ == '__main__':
    test_()
    pass



