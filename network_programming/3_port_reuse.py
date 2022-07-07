# 设置端口号复用：

import socket


if __name__ == '__main__':

    # 1.创建服务端端套接字对象
    # 参数：AF_INET为ipv4地址类型    SOCK_STREAM为TCP传输协议类型
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口号复用，表示服务端程序退出后立即释放端口号
    # SOL_SOCKET表示当前套接字，SO_REUSEADDR表示复用端口号选项，True表示确定复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 2.绑定端口号
    # 第一个参数host表示ip地址，一般不指定，表示本机的任何一个ip都可，防止有些本机有多个网卡(多个ip)时只能访问其中一个
    # 第二个参数port为端口号
    tcp_server_socket.bind(('', 9090))

    # 3.设置监听
    # 参数backing = 128，表示最大等待建立连接个数
    tcp_server_socket.listen(128)

    # 4.等待接受客户端的连接请求
    # 注意：tcp_server_socket 只负责等待接收客户端的连接请求(相当于10086电话平台)，
    # 每次客户端和服务端连接成功，accept都会返回一个套接字result(相当于接通10086给你的客服)，此套接字(元组)不与客户端通信
    # 返回的套接字result是一个元组，第一个元素为一个新的套接字(与客户端通信)，第二个元素为ip和端口号
    # result = tcp_server_socket.accept()
    # print(result)
    # 解决上述结果是将返回值(元组)拆包，如下
    new_connection, ip_port = tcp_server_socket.accept()           # new_connection套接字才与客户端通信
    # 代码执行到此，说明连接建立成功
    print('客户端的ip和端口号为：',ip_port)

    # 5.接收数据
    # 收发消息用拆包后的新套接字new_connection
    recv_data = new_connection.recv(1024)
    recv_content = recv_data.decode('gbk')
    print('接收到的内容为：',recv_content)

    # 实际开发中的处理
    send_content = '问题正在处理中...'
    # 对字符串进行编码
    send_data = send_content.encode('gbk')

    # 6.发送数据
    new_connection.send(send_data)
    # 关闭服务通信套接字，表示与客户端终止通信(相当于与10086客服挂断)
    new_connection.close()

    # 7.关闭服务器端套接字，表示以后不再等待接收客户端的连接请求(相当于10086平台停服升级)
    tcp_server_socket.close()






