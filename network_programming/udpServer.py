import socket
import json
import threading
import time
import select
import queue
import logging
from concurrent.futures import ThreadPoolExecutor
# note: No such file currently
from common.run_status import RunStatusInstance


class UDPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 2097152)  # 2 * 1024 * 1024
        self.socket.bind((self.host, self.port))
        self.running = False

    # 采用线程池
    def start(self, msg_queue):
        self.running = True
        logging.info(f"UDP服务器已启动,监听地址：{self.host}:{self.port}...")
        frameNo = 0
        with ThreadPoolExecutor(max_workers=10) as executor:
            while self.running and RunStatusInstance().get_handle_thread_status():
                data, client_address = self.socket.recvfrom(2097152)
                executor.submit(self.handle_client, data, client_address, msg_queue)
                frameNo += 1
            # print(f"################################### recv frame {frameNo}\n")

    def start_select(self, msg_queue):
        self.running = True
        logging.info(f"UDP服务器已启动,监听地址：{self.host}:{self.port}...")
        frameNo = 0
        while self.running:
            rlist, wlist, elist = select.select([self.socket], [], [], 1)
            if self.socket in rlist:
                data, client_address = self.socket.recvfrom(2097152)
                self.handle_client(data, client_address, msg_queue)
                frameNo += 1

    def start_thread(self, msg_queue):
        self.running = True
        logging.info(f"UDP服务器已启动,监听地址：{self.host}:{self.port}...")
        frameNo = 0
        while self.running:
            data, client_address = self.socket.recvfrom(65536)
            t = threading.Thread(target=self.handle_client, args=(data, client_address, msg_queue))
            t.start()
            frameNo += 1
            print(f"################################### recv frame {frameNo}\n")

    def stop(self):
        self.running = False
        self.socket.close()
        # while self.msg_queue.not_empty():
        #     self.msg_queue.get();

        logging.info(f"UDP服务器已关闭")

    def handle_client(self, data, client_address, msg_queue):
        logging.info(f"接收到来自 {client_address} 的数据...")
        json_str = data.decode()
        json_obj = json.loads(json_str)
        logging.info(f"从 {client_address} 接收到数据：{json_obj}")
        recv_info = [json_obj, client_address]
        recv_info_str = json.dumps(recv_info)
        msg_queue.put(recv_info_str)
        # print(f"recv dd frame data, curbuffer size ++++++++++++++++ {msg_queue.qsize()}\n")

        # 在这里可以对接收到的数据进行处理
        # 处理完毕后，可以将处理结果发送回客户端
        # response = {
        #     "msg_type":json_obj["msg_type"],
        #     "msg_data":{'status': 'ok'}
        # }
        # response_str = json.dumps(response)
        # self.socket.sendto(response_str.encode(), client_address)


if __name__ == '__main__':
    msg_queue = queue.Queue()
    server = UDPServer('192.168.1.8', 8000)
    server.start(msg_queue)
