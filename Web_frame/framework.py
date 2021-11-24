# web框架负责处理动态资源请求

import time
import pymysql
import json
import logging


# 路由列表,每一个元素就是一个路由，手动添加路由到路由列表(后续Django使用)
route_list = [
    # ('/index.html', index),
    # ('/center.html', center)
]

# 定义一个带有参数的装饰器,将路由添加到路由列表(后续flask使用)
def route(path):
    def decorator(func):
        # 当执行装饰器的时候就要把路由添加到路由列表
        route_list.append((path, func))       # 少了一对括号报错，(path,func)是一个整体作为元组传参
        def inner():
            # route_list.append(path, func)   不能放在这，否则调用一次就要添加一次，也就是刷新一次本网页就会添加一次路由
            result = func()
            return result

        return inner

    return decorator


# 获取首页数据
@route('/index.html')    # ==>@decorator  ==>index = decorator(index)
def index():
    # 状态信息
    status = '200 OK'
    # 响应头
    # response_header = [{'server':'pws'},{'Content-Type': 'text/html; charset=UTF-8'}]
    response_header = [('server', 'PWS/1.1'), ('Content-Type','text/html; charset=UTF-8')]

    # web框架处理后的数据
    #   1.打开模板文件并读取
    with open('./template/index.html', 'r', encoding='utf-8') as file:       #这里读的仅是html文件，不会有图片等超文本，所以不需以rb方式读取，且windows里要指定utf-8编码！
        file_data = file.read()

    #   2.查询数据库，初始化模板文件里面的模板变量(%content%)
    conn = pymysql.connect(host='192.168.94.131',
                    port=3306,
                    user='huangzhen',
                    password='root',
                    database='stock_db',
                    charset='utf8')
    cursor = conn.cursor()
    sql = 'select * from info;'
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)          #查询的表格返回的是元组，且其元素也是元组
    cursor.close()
    conn.close()

    # 遍历每一条数据，完成tr标签的封装
    db_data = ''
    for row in result:         # row即是查询表格的每一行，是一个元组
        db_data += '''<tr>
                 <td>%s</td>
                 <td>%s</td>
                 <td>%s</td>
                 <td>%s</td>
                 <td>%s</td>
                 <td>%s</td>
                 <td>%s</td>
                 <td>%s</td>
                 <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue></td>
                 </tr>'''%row
    # db_data = time.ctime()
    data = file_data.replace('%content%', db_data)
    return status, response_header, data                    # 这里返回的是一个元祖


# 个人中心数据接口
@route('/center_data.html')
def center_data():
    # 从数据库查询数据，并转成字符串
    conn = pymysql.connect(host='192.168.94.131',
                    port=3306,
                    user='huangzhen',
                    password='root',
                    database='stock_db',
                    charset='utf8')
    cursor = conn.cursor()
    sql = '''select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info 
            from info i inner join focus f 
            on i.id = f.info_id;
        '''
    cursor.execute(sql)
    result = cursor.fetchall()       # 返回的是元组,每一个元素也是元组
    # print(result)

    # 把元组转成列表字典(列表推导式)
    center_data_list = [{'code': row[0],
             'short': row[1],
             'chg': row[2],
             'turnover': row[3],
             'price': str(row[4]),
             'highs': str(row[5]),
             'note_info': row[6]
             } for row in result]
    # print(center_data_list)
    # 把列表转成json字符串数据         ensure_ascii=False表示在控制台显示为中文
    json_str = json.dumps(center_data_list, ensure_ascii=False)
    # print(json_str)
    # print(type(json_str))

    cursor.close()
    conn.close()

    status = '200 OK'
    # 此时response_header里要指定编码格式'Content-Type','text/html; charset=UTF-8'，否则乱码
    response_header = [('server', 'PWS/1.1'), ('Content-Type','text/html; charset=UTF-8')]

    return  status, response_header, json_str


@route('/center.html')
def center():
    # 状态信息
    status = '200 OK'
    # 响应头
    # response_header = [{'server':'pws'},{'Content-Type': 'text/html; charset=UTF-8'}]
    response_header = [('server', 'PWS/1.1'), ('Content-Type','text/html; charset=UTF-8')]

    # web框架处理后的数据
    #   1.打开模板文件并读取
    with open('./template/center.html', 'r', encoding='utf-8') as file:       #这里读的仅是html文件，不会有图片等超文本，所以不需以rb方式读取，且需要指定utf-8编码！
        file_data = file.read()

    #   2.查询数据库，初始化模板文件里面的模板变量(%content%)
    # 这里先仅模拟查询数据库内容
    # data =  time.ctime()
    # data = file_data.replace('{%content%}', data)
    data = file_data.replace('{%content%}', '')

    return status, response_header, data


def not_found():
    status = '404 Not Found'
    # response_header = [{'server':'pws'},{'Content-Type': 'text/html; charset=UTF-8'}]
    response_header = [('server', 'PWS/1.1'), ('Content-Type', 'text/html; charset=UTF-8')]
    data = '请求失败'
    return status, response_header, data



def handle_request(env):
    # 获取动态资源请求路径
    request_path = env['request_path']
    print('动态资源请求路径：', request_path)
    # print(route_list)             # 输出显示路由列表

    # 遍历路由列表，匹配请求的url
    for path, func in route_list:
        # 找到指定路由，执行对应处理函数
        if request_path == path:
            result = func()
            return result
    else:
        result = not_found()
        logging.error('没有设置相关的路由信息：' + request_path)
        return result


    # # 判断请求的动态资源路径，选择指定函数处理对应请求
    # if request_path == '/index.html':
    #     # 获取首页数据
    #     result = index()
    #     # 处理结果返回给web服务器，让web服务器拼接响应报文时使用
    #     return result
    # elif request_path == '/center.html':
    #     result = center()
    #     return result
    # else:
    #     # 返回404
    #     result = not_found()
    #     return result


# if __name__ == '__main__':
#     center_data()



































