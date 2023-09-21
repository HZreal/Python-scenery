import tornado.ioloop
import tornado.web


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        print('Enter ------')
        self.write("the First Tornado Application")


def make_app():
    return tornado.web.Application([
        (r"/", TestHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
