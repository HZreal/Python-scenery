# pymysql 完成对数据的增删改


import pymysql


def run():
    # 2.创建连接对象
    conn = pymysql.connect(host='192.168.94.131',
                           port=3306,
                           user='huangzhen',
                           password='root',
                           database='stu',
                           charset='utf8')

    # 3.获取游标
    cursor = conn.cursor()

    sql_1 = 'insert into class(name) values("G-5");'
    sql_2 = 'update class set name = "G-9" where id = 9;'
    sql_3 = 'delete from class where id = 11111;'
    # 对表的增、删、改操作，需要把修改的数据提交到数据库，查询不需要提交
    try:
        # 4.执行SQL语句
        cursor.execute(sql_3)
        # 提交修改的数据到数据库
        conn.commit()
    except Exception as e:
        # 捕获到异常则撤销修改的数据,即数据回滚
        conn.rollback()
    finally:
        # 5.关闭游标
        cursor.close()
        # 6.关闭连接
        conn.close()

# 批量插入
# INSERT INTO example
# VALUES
# (100, 'Name 1', 'Value 1', 'Other 1'),
# (101, 'Name 2', 'Value 2', 'Other 2'),
# (102, 'Name 3', 'Value 3', 'Other 3'),
# (103, 'Name 4', 'Value 4', 'Other 4');
#  ...

# 使用存储过程



if __name__ == '__main__':

    run()

























