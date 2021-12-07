import pymysql
from builtins import zip


def dict_fetchall(cursor):
    "将查询的数据值与其数据库字段一一对应，返回字典列表"
    # cursor.description返回游标活动状态，包含7个元素的元组：(name, type_code, display_size, internal_size, precision, scale, null_ok)
    print('description==================', cursor.description)             # (('name', 253, None, 10, 10, 0, False), ('age', 1, None, 4, 4, 0, True), ('height', 246, None, 5, 5, 2, True))
    columns = [col[0] for col in cursor.description]
    print('columns======================', columns)                        # ['name', 'age', 'height']
    res_dict_list = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return res_dict_list                                        # 字典列表，使数据库字段与值对应  [{'name': '黄真', 'age': 24, 'height': Decimal('1.80')}, {'name': '葛临婧', 'age': 24, 'height': Decimal('1.80')},  ...{}, ...]


conn = pymysql.connect(**{
        'host': '192.168.94.131',
        'port': 3306,
        'user': 'huangzhen',
        'password': 'root',
        'database': 'stu',
        'charset': 'utf8'
})

def run():
    cursor = conn.cursor()
    sql = 'select name, age, height from student;'
    cursor.execute(sql)

    res_dict_list = dict_fetchall(cursor)
    print(res_dict_list)


def run2():
    # DictCursor() 以字典的形式返回操作结果
    dictcursor = pymysql.cursors.DictCursor(conn)
    sql = 'select name,age,height from student;'
    dictcursor.execute(sql)
    res = dictcursor.fetchall()
    print(res)


def run3():
    # SSCursor()不缓存游标，主要用于当操作需要返回大量数据的时候
    sscursor = pymysql.cursors.SSCursor(conn)


def run4():
    # 不缓存游标，将结果以字典的形式进行返回
    ssdictcursor = pymysql.cursors.SSDictCursor(conn)
    pass


if __name__ == '__main__':
    # run()
    run2()