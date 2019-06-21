# -*- coding: utf-8 -*-
import time
from tornado import web, ioloop


class MainHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello Word4")


if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler)
    ], debug=True)
    app.listen(8888)
    ioloop.IOLoop.current().start()



