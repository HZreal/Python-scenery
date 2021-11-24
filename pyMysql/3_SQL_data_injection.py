# 数据注入：用户提交带有恶意的数据与SQL语句进行字符串方式的拼接，从而影响了SQL语句的语义，最终产生数据泄露的现象。
# 防止：SQL语句参数化,使用%s来占位

import pymysql

if __name__ == '__main__':

    # 2.创建连接对象
    conn = pymysql.connect(host='192.168.94.131',
                           port=3306,
                           user='huangzhen',
                           password='root',
                           database='stu',
                           charset='utf8')

    # 3.获取游标
    cursor = conn.cursor()

    # 演示数据注入：
    # 原本查一条数据，结果查了全部数据
    # sql = 'select * from student where name = "黄真";'
    # sql = 'select * from student where name = "%s";' % '黄真"or 1 = 1 or "'
    # print(sql)

    # 防止数据注入：
    # 这里的%s是SQL语句的参数，和字符串里面的%s不一样，不要加引号
    sql_s = 'select * from student where name = %s;'
    params = ('huang',)
    # 此时加了不合理字符串无法非法查询
    # params = ('huang"or 1=1 or "',)

    # 多个参数的情况也是用多个%s站位，并以列表或元组或字典的方式传参
    # sql_i = 'insert into teacher(name, s_id, c_id) values(%s, %s, %s);'
    # params = ('li', 2, 3)


    try:
        # 4.执行SQL语句
        cursor.execute(sql_s, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
    else:
        result = cursor.fetchall()
        # print(result)
        for row in result:
            print(row)
    finally:
        # 5.关闭游标
        cursor.close()

        # 6.关闭连接
        conn.close()






































