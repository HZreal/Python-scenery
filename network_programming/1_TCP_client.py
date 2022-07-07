# 开发 TCP 客户端程序:

import socket


def client_start():
    # 1.创建客户端套接字对象
    # 参数：AF_INET为ipv4地址类型    SOCK_STREAM为TCP传输协议类型
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # TCP客户端程序一般不需要绑定端口号，因为客户端是主动发起建立连接的，系统自动生成一个端口号，也可以绑定
    # tcp_client_socket.bind('', 8080)

    # 2.和服务端套接字建立连接
    tcp_client_socket.connect(('192.168.94.1', 8080))

    send_content = input('请输入发送的数据：')
    # 数据进行编码成二进制数据才能发送，否则发送提示数据类型错误
    # windows里网络调试助手使用gbk编码，Linux里面的网络调试助手使用UTF-8编码
    send_data = send_content.encode('gbk')

    # 3.发送数据到服务器端
    tcp_client_socket.send(send_data)

    # 4.接收服务器端数据
    # 1024 表示每次接收的最大字节数
    recv_data = tcp_client_socket.recv(1024)

    # 对接收的二进制数据进行解码
    recv_content = recv_data.decode('gbk')
    print('接收服务器端的内容为：', recv_content)

    # 5.关闭客户端套接字
    tcp_client_socket.close()



if __name__ == '__main__':
    client_start()




# send原理剖析：
# send是不是直接把数据发给服务端?
# 不是，要想发数据，必须得通过网卡发送数据。
# 应用程序是无法直接通过网卡发送数据的，它需要调用操作系统接口，也就是说，应用程序把发送的数据先写入到内存的发送缓冲区，再由操作系统调用网卡把发送缓冲区的数据发送给服务端网卡。

# recv原理剖析：
# recv是不是直接从客户端接收数据?
# 不是，应用软件是无法直接通过网卡接收数据的，它需要调用操作系统接口，操作系统调用网卡接收数据，把接收的数据写入到内存的接收缓冲区，应用程序再从接收缓存区获取客户端发送的数据。


# 网卡：network interface card
# ifconfig
# netplan设置ip连接wifi
# hostapd开启热点
# dhcp动态分配IP












































































































































































































































