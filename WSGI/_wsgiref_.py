# CGI (Common Gateway Interface)  即通用网关接口，即接口协议，前端向服务器发送一个URL（携带请求类型、参数、cookie等信息）请求，服务器把这个请求的各种参数写进进程的环境变量
# 比如REQUEST_METHOD，PATH_INFO之类的，然后开启 cgi模块以后，将其发送给CGI程序，CGI程序（可以由各种语言编写，比如C、C ++、VB 和Delphi 等）从环境变量中解析出各种参数，然后向标准输出输出内容（比如cout了一段HTML代码），这些内容没有被打印到控制台上，而是最终响应给了你的浏览器，渲染出了网页。
# 每一次向CGI发送请求，都会生成一个CGI进程，这就是所谓的fork-and-exec模式，这也通常是导致并发瓶颈的症结，反向代理加上大型的的分布式系统可以一定程度上减轻这些压力。

# WSGI (Python Web Server Gateway Interface) 即web服务器网关接口，也是接口协议，
# 前端向服务器发送一个URL（携带请求类型、参数、cookie等信息）请求，服务器把这个请求的各种参数传给WSGI模块，wsgi将各种参数进行python化，封装为request对象传递给按照WSGI接口标准调用注册的WSGI Application，并返回response参数给客户端。



# wsgiref是python内置库，实现了一个简单的WSGI Server 和 WSGI Application，使用该库我们将很容易实现自定义的web架构而不用考虑TCP/HTTP层协议
# 该库提供了5个模块:
#     * util -- Miscellaneous useful functions and wrappers
#     * headers -- Manage response headers
#     * handlers -- base classes for server/gateway implementations
#     * simple_server -- a simple BaseHTTPServer that supports WSGI
#     * validate -- validation wrapper that sits between an app and a server to detect errors in either



from wsgiref.simple_server import make_server, demo_app
from wsgiref.util import setup_testing_defaults

def app(environ, start_response):
    # setup_testing_defaults(environ)
    print('enter ----------')
    # print(environ, start_response)

    return [b'hello world']

# 创建server
# ws = make_server('127.0.0.1', 9999, demo_app)
ws = make_server('127.0.0.1', 9999, app)




# 启动服务
ws.serve_forever()





