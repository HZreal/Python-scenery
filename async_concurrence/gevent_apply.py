# gevent 应用场景



# 1. gevent-zeremq
# 一个非常强大的，为构建并发和分布式应用的消息传递层。
# import gevent
# from gevent_zeromq import zmq
#
# # Global Context
# context = zmq.Context()
#
#
# def server():
#     server_socket = context.socket(zmq.REQ)
#     server_socket.bind("tcp://127.0.0.1:5000")
#
#     for request in range(1, 10):
#         server_socket.send("Hello")
#         print('Switched to Server for %s' % request)
#         # Implicit context switch occurs here
#         server_socket.recv()
#
# def client():
#     client_socket = context.socket(zmq.REP)
#     client_socket.connect("tcp://127.0.0.1:5000")
#
#     for request in range(1, 10):
#         client_socket.recv()
#         print('Switched to Client for %s' % request)
#         # Implicit context switch occurs here
#         client_socket.send("World")
#
# publisher = gevent.spawn(server)
# client = gevent.spawn(client)
#
# gevent.joinall([publisher, client])



# 2. 简单 StreamServer
# 继承自 BaseServer
from gevent.server import StreamServer
from gevent.pool import Pool

# def handle(socket, address):
#     print('new connection!')
#     socket.send(b"Hello from a telnet!\n")
#     for i in range(5):
#         socket.send(b'haha')
#     socket.close()
#
# pool = Pool(1000)   # 限制最大并发连接数
# server = StreamServer(('127.0.0.1', 5000), handle, spawn=pool)
# server.serve_forever()



# 3. WSGIServer
# 继承自 StreamServer
from gevent.pywsgi import WSGIServer

def application(environ, start_response):
    # print('wsgi application environ ---->  ', environ)
    print('start_response ---->  ', start_response)

    if environ['PATH_INFO'] == '/':
        status = '200 OK'
        headers = [
            ('Content-Type', 'text/html')
        ]
        start_response(status, headers)
        return [b"<b>index page</b>"]
    start_response('404 Not Found', [('Content-Type', 'text/html')])
    return [b'<h1>Not Found</h1>']

# WSGIServer(('127.0.0.1', 8000), application).serve_forever()

# 支持HTTPS
server = WSGIServer(('127.0.0.1', 8443), application, keyfile='server.key', certfile='server.crt')
# server.start()           # 异步启动
server.serve_forever()     # we use blocking serve_forever() here because we have no other jobs



# 4. gevent-websocket
# import json
# import random
# from gevent import pywsgi, sleep
# from geventwebsocket.handler import WebSocketHandler
#
# class WebSocketApp(object):
#     '''Send random data to the websocket'''
#
#     def __call__(self, environ, start_response):
#         ws = environ['wsgi.websocket']
#         x = 0
#         while True:
#             data = json.dumps({'x': x, 'y': random.randint(1, 5)})
#             ws.send(data)
#             x += 1
#             sleep(0.5)
#
# server = pywsgi.WSGIServer(
#     ("", 10000), WebSocketApp(),
#     handler_class=WebSocketHandler
# )
# server.serve_forever()







