

## WSGI

WSGI 是为 Python 语言定义的 Web 服务器和 Web 应用程序或框架之间的一种简单而通用的接口规范。描述的是**Web服务器与Web应用之间**如何进行通信

一种**通信协议**，用于通信。

它不是服务器、python模块、框架、API或者任何软件，只是一种描述web服务器（如nginx，uWSGI等服务器）如何与web应用程序（如用Django、Flask框架写的程序）通信的规范。

它是一个Gateway，也就是网关。网关的作用就是在协议之间进行转换。

## uwsgi

是一种**uWSGI服务器自有**的协议

是一种**线路协议**，用于数据传输

用于定义传输信息的类型（type of information），每一个uwsgi packet前4byte为传输信息类型描述，用于与nginx等代理服务器通信

它与WSGI相比是两样不同的东西

## uWSGI

uWSGI是一种实现了WSGI协议、uwsgi、http等协议的**Web应用服务器**。

uWSGI服务器要做的就是把HTTP协议转化成语言支持的网络协议。比如把HTTP协议转化成WSGI协议，让Python可以直接使用。Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。

## nginx、Apache是常用的Web服务器

一般的web服务器，如Apache和nginx，都没有内置WSGI协议的支持，而是通过扩展来完成。

* 比如Apache服务器，会通过扩展模块mod_wsgi来支持WSGI。Apache和mod_wsgi之间通过程序内部接口传递信息，mod_wsgi会实现WSGI的server端、进程管理以及对application的调用。

* Nginx上一般是用proxy的方式，用nginx的协议将请求封装好，发送给应用服务器如uWSGI或者Gunicorn，应用服务器会实现WSGI的服务端、进程管理以及对application的调用。


为什么有了uWSGI为什么还需要nginx？

因为nginx具备优秀的静态内容处理能力，而动态内容会转发给uWSGI服务器，这样可以达到很好的客户端响应。



