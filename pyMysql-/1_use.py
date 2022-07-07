# python与mysql连接基本使用

# 1.导入包
import pymysql

def run():
    # 2.创建连接对象
    # connect = Connection = Connect  本质上是一个函数，任意一个都可以创建一个连接对象
    # pymysql.connect或者pymysql.Connect或者pymysql.Connection都可
    conn = pymysql.connect(
        host='192.168.94.131',
        port=3306,
        user='huangzhen',
        password='root',
        database='stu',
        charset='utf8'
    )

    # 3.获取游标，目的就是执行SQL语句
    cursor = conn.cursor()
    # 书写对数据库的操作，赋给一个变量(str)
    sql = 'select * from student;'

    # 4.执行SQL语句，返回结果记录的条数
    count = cursor.execute(sql)
    print('查询结果的条数=============', count)

    # 获取查询结果,   返回的是以表字段的值为元素的元组
    one_row = cursor.fetchone()          # 获取查询的一条记录
    print('获取结果中的一条数据==========', one_row)                       # (1, '黄真', 24, '男', datetime.datetime(2021, 4, 5, 7, 44, 34), 0, Decimal('1.80'), 1)
    one_row = cursor.fetchone()          # 游标前移指向下一条记录
    print('获取结果中的一条数据==========', one_row)                       # (2, '葛临婧', 24, '女', datetime.datetime(2021, 4, 22, 7, 45, 11), 0, Decimal('1.80'), 2)
    one_row = cursor.fetchone()          # 游标前移指向下一条记录
    print('获取结果中的一条数据==========', one_row)                       # (3, '张三', 25, '男', datetime.datetime(2019, 5, 28, 9, 22, 11), 0, Decimal('1.82'), 1)

    # result = cursor.fetchall()           # 获取所有结果：元组，其元素还是一个元祖，
    # print(result)
    # 循环遍历结果元组，每一条记录仍然是一个元组
    # for row in result:
    #     print(row)


    # 5.关闭游标
    cursor.close()
    # 6.关闭连接
    conn.close()





# pymysql连接封装
class OperateMysql():
    def __init__(self, config):
        self.conn = pymysql.connect(**config)

    def exec(self, sql, params):
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
            query_result = cursor.fetchall()

        return self.parse_query_result(query_result)

    @staticmethod
    def parse_query_result(query_result):
        print('对查询结果数据进行解析。。。')
        res = query_result
        return res

    def close(self):
        self.conn.close()

def run1():
    config = {'host': '192.168.94.131', 'port': 3306, 'user': 'huangzhen', 'password': 'root', 'database': 'stu', 'charset': 'utf8'}
    conn = OperateMysql(config)
    sql = 'select * from student where id=%s;'
    params = ['1']
    res = conn.exec(sql, params)             # 可大量操作
    print(res)




# 上下文管理器方式连接mysql
class DoMysql():
    def __init__(self, config):
        self.conn = pymysql.connect(**config)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

def run2():
    config = {'host': '192.168.94.131', 'port': 3306, 'user': 'huangzhen', 'password': 'root', 'database': 'stu', 'charset': 'utf8'}
    sql = 'select * from student where id=%s;'
    params = ['1']
    with DoMysql(config) as cursor:
        cursor.execute(sql, params)
        result = cursor.fetchall()



# 单例实现pymysql的连接
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            conn = pymysql.connect(host='192.168.94.131', port=3306, user='huangzhen', password='root', database='stu', charset='utf8')
            cls._instance.db = conn
        return cls._instance

    def exec(self, sql, params):
        cursor = self.db.cursor()
        cursor.execute(sql, params)

def run3():
    sql = 'select * from student where id = %s;'
    params = [1]
    Singleton().exec(sql, params)



# Python与MySQL的长连接
class KeepLongConnect(object):
    def __init__(self, conn):
        self.conn = conn

    def test_connect(self):
        try:
            self.conn.ping()          # Check if the server is alive.
        except Exception:
            self.conn = pymysql.connect(host='192.168.94.131', port=3306, user='huangzhen', password='root', database='stu', charset='utf8')

    def exec(self, sql, params):
        with self.conn.cursor as cursor:
            cursor.execute(sql, params)
            ret = cursor.fetchall()

def run4():
    conn = pymysql.connect(host='192.168.94.131', port=3306, user='huangzhen', password='root', database='stu', charset='utf8')
    KeepLongConnect(conn).test_connect()



if __name__ == '__main__':
    run()
    # run1()
    # run2()
    # run3()
    # run4()













