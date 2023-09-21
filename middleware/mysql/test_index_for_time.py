import pymysql


def run():
    conn = pymysql.connect(
        host='192.168.94.131',
        port=3306,
        user='huangzhen',
        password='root',
        database='stu',
        charset='utf8'
    )

    cursor = conn.cursor()
    sql = 'insert into mytest(name) values(%s);'
    try:
        p = 1
        for i in range(10000):
            params = ('名字' + str(p),)
            cursor.execute(sql, params)
            p += 1

        conn.commit()
    except Exception as e:
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    run()
