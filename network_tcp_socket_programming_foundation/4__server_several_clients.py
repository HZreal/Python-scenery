# 多任务版TCP服务端程序，TCP服务端服务于多个客户端

import socket
import threading

# 处理客户端请求
def handle_client_request(new_client, ip_port):
    print('客户端的ip和端口号为：', ip_port)
    # 5.接收数据
    # 循环接收客户端的数据，保持多次交互
    while True:

        recv_data = new_client.recv(1024)
        print('接收的数据长度是：', len(recv_data))
        if len(recv_data) > 0:
        # 或者if recv_data:
            recv_content = recv_data.decode('gbk')
            print('接收到的内容为：', recv_content, '来自ip:', ip_port)

            # 实际开发中的处理
            send_content = '问题正在处理中...'
            # 对字符串进行编码
            send_data = send_content.encode('gbk')

            # 6.发送数据
            new_client.send(send_data)
        else:
            # 若接收数据长度为0，则退出此次通信过程
            print(f'客户端{ip_port}已下线!')
            break

    # 关闭通信套接字，表示此次通信结束
    new_client.close()


if __name__ == '__main__':

    # 1.创建服务端端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 2.绑定端口号
    tcp_server_socket.bind(('', 9090))

    # 3.设置监听
    # 参数backing = 128，表示最大等待建立连接个数
    tcp_server_socket.listen(128)

    # 4.等待接受客户端的连接请求
    # 循环等待接收客户端请求
    while True:

        new_client, ip_port = tcp_server_socket.accept()
        # 代码执行到此，说明连接建立成功


        # 当客户端与服务端建立连接成功，就创建子线程专门负责与该客户端通信(打通10086后，平台给你分配一个客服)
        sub_thread = threading.Thread(target=handle_client_request, args=(new_client, ip_port))
        sub_thread.setDaemon(True)
        sub_thread.start()


    # 7.关闭服务器端套接字
    # 实际中的服务端是一直运行的，所以不需关闭套接字，只有在维护时才关闭
    # tcp_server_socket.close()






