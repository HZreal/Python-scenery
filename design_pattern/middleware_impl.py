class MiddlewareManager:
    def __init__(self, get_response):
        self.get_response = get_response
        self.middlewares = []

    def add_middleware(self, middleware):
        self.middlewares.append(middleware)

    def __call__(self, request):
        for middleware in self.middlewares:
            if hasattr(middleware, 'process_request'):
                request = middleware.process_request(request)

        response = self.get_response(request)

        for middleware in reversed(self.middlewares):
            if hasattr(middleware, 'process_response'):
                response = middleware.process_response(request, response)
        return response


class MiddlewareA:
    def process_request(self, request):
        print("Middleware A: Before view")
        request['A'] = 'Processed by Middleware A'
        return request

    def process_response(self, request, response):
        print("Middleware A: After view")
        response['A'] = 'Response processed by Middleware A'
        return response


class MiddlewareB:
    def process_request(self, request):
        print("Middleware B: Before view")
        request['B'] = 'Processed by Middleware B'
        return request

    def process_response(self, request, response):
        print("Middleware B: After view")
        response['B'] = 'Response processed by Middleware B'
        return response


# 假设这是你的Django视图函数
def view_function(request):
    print("View function")
    print("Request in view function:", request)
    return {"response": "View function response"}


# 创建中间件管理器并添加中间件
manager = MiddlewareManager(view_function)
manager.add_middleware(MiddlewareA())
manager.add_middleware(MiddlewareB())

# 模拟请求
request = {}
response = manager(request)
print("Final response:", response)