import json

def basic_use():
    _dict = {                   # 字段没有格式，处理之前去掉编辑器中的格式，就是{'name': 'gg'}
        'name': 'gg'
    }

    # json_str = json.dumps(_dict)      # 字典无格式要求
    # print(json_str)
    # print(type(json_str))             # json是特殊格式的字符串


    _s = str(_dict)
    print(_s)

    j_s = json.dumps(_s)
    print(j_s)





def test_():
    json_str = """{                 
        "a": 1,
        "b": 2
    }"""
    c = json.loads(json_str)              # 必须是严格json类型的字符串，必须双引号，最后一个键值对不能有逗号
    print(c)


    _dd = "{\"db_key\":\"\\u003cC:\\\\ProgramData\\\\update\\u003e[F2][Ctrl]c\"}"
    rr = json.loads(_dd)               # dict
    print(rr)

    gg = json.dumps(_dd)
    print(gg)


    # d = {
    #     'a': 1,
    #     'f': 2
    # }
    # s = json.dumps(d)
    # print(s, type(s))




# eval的作用：将字符串str当成有效的表达式来求值并返回计算结果
def ttt():
    str1 = "{'a': 1, 'b': 2, }"
    a = eval(str1)
    print(type(a))
    print(a)

    str1 = "([1,2], [3,4], [5,6], [7,8], (9,0))"
    b = eval(str1)
    print(type(b))
    print(b)


def gg():
    pass


if __name__ == '__main__':
    # basic_use()
    test_()
    # ttt()
    # gg()



