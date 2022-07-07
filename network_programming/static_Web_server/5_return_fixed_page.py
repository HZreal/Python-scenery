# 服务器返回固定的页面

import socket

def server_start():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 8000))
    tcp_server_socket.listen(128)

    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        recv_data = new_socket.recv(4096)
        print(recv_data)

        # with open操作不需关闭文件，系统完成
        with open('static/index.html', 'r') as file:
            file_data = file.read()

        # 把数据封装成http响应报文格式的数据
        # 响应行-------协议版本 状态码 状态描述
        response_line = 'HTTP/1.1 200 OK\r\n'
        # 响应头
        response_header = 'server:PWS/1.0\r\n'
        # 空行
        # 响应体
        response_body = file_data

        # 把数据封装成http响应报文
        response = response_line + response_header + '\r\n' + response_body
        # 把字符串编码成二进制
        response_data = response.encode('utf-8')
        # 发送给浏览器的响应报文
        new_socket.send(response_data)

        new_socket.close()



if __name__ == '__main__':

    server_start()





# 运行，浏览器输入localhost:8000/index.html












































































































