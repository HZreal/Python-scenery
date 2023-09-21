import json

import pymysql, csv

conn = pymysql.connect(**{
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root123456',
        'database': 'trojan_platform',
        'charset': 'utf8'
})


def handle_fetchall(cursor):
    """
    将查询的数据行列表的每一行与其数据库字段一一对应，形成一个字典，最后返回字典列表
    """
    columns = [col[0] for col in cursor.description]

    res_dict_list = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return columns, res_dict_list


def run():
    cursor = conn.cursor()
    sql = 'select * from device_plugin_report_data;'
    cursor.execute(sql)

    columns, res_dict_list = handle_fetchall(cursor)
    print('columns -------', columns)
    # print(res_dict_list)

    for item in res_dict_list:
        item['rt_time'] = item['rt_time'].strftime('%Y-%m-%d %H:%M:%S')
        item['data'] = json.loads(item['data'])


    for item in res_dict_list:
        item['data'] = json.loads(item['data'])
        for k, v in item['data'].items():
            k.strip()
            v.strip()

    print(res_dict_list)


    with open('data.csv', 'w', newline="") as f:
        writer = csv.DictWriter(f, columns)

        writer.writeheader()
        writer.writerows(res_dict_list)



def ff():
    t = '\r\nqwert\r\n'
    t.strip()
    print(t)

if __name__ == '__main__':
    run()
    # ff()