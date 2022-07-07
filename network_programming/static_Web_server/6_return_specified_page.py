# 服务器返回客户端指定的页面数据

import socket
import os

def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 8000))
    tcp_server_socket.listen(128)

    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        recv_data = new_socket.recv(4096)
        # 显示接收的数据(此处终端的显示是被解码才看到的，实际此数据为二进制数据)
        # print(recv_data)         # 通过终端打印可以看出：接收数据为http请求报文'GET /grand.html HTTP/1.1\r\nHost...\r\n.....\r\n.......'

        # 避免客户端不发数据时，下面的数据分割成list无法取下标为1的数据，即out of range
        if len(recv_data) == 0:
            new_socket.close()
            return

        # 对二进制数据进行解码
        recv_content = recv_data.decode('utf-8')
        # print(recv_content)      # 通过终端打印可以看出：解码即将请求报文中的\r\n去掉，并换行显示

        # 对数据按照空格进行分割--------- 'GET /index2.html HTTP/1.1\r\n...............'
        request_list = recv_content.split(' ', maxsplit=2)                  # 返回列表
        # 请求资源路径
        request_path = request_list[1]
        print(request_path)
        # 判断请求是否是根目录，若是则默认打开首页(自己指定)
        if request_path == '/':
            request_path = '/index.html'

        # 判断服务器文件不存在方法一：
        # os.path.exists('static' + request_path)

        # 判断服务器文件不存在方法二：
        try:
            # with open操作不需关闭文件，系统完成
            # rb模式打开文件，兼容打开图片
            with open('static' + request_path, 'rb') as file:
                file_data = file.read()            # 此时读的数据file_data是二进制类型
        except Exception as e:
            # 代码执行到此，说明没有请求文件，返回404状态信息
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            response_header = 'server:PWS/1.0\r\n'
            with open('static/error.html', 'rb') as file:
                file_data = file.read()
            response_body = file_data
            response_data = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            new_socket.send(response_data)

        else:
            # 代码执行到此，说明文件存在，返回200状态信息
            # 把数据封装成http响应报文格式的数据
            # 响应行-------协议版本 状态码 状态描述
            response_line = 'HTTP/1.1 200 OK\r\n'
            # 响应头
            response_header = 'server:PWS/1.0\r\n'
            # 空行
            # 响应体
            response_body = file_data

            # 把数据封装成http响应报文
            # response = response_line + response_header + '\r\n' + response_body      # 会报错，因为response_line, response_header, '\r\n'是字符串，而response_body是二进制类型，不能拼接
            response_data = (response_line + response_header + '\r\n').encode('utf-8') + response_body

            # 发送给浏览器的响应报文
            new_socket.send(response_data)
        finally:
            new_socket.close()




if __name__ == '__main__':

    main()
















































































































