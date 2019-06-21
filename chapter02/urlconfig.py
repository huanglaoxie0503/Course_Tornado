# -*- coding: utf-8 -*-
import tornado
from tornado import web, ioloop


class MainHandler(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("Hello Word4")


class PeopleHandler(web.RequestHandler):
    async def get(self, id, *args, **kwargs):
        self.write("用户id:{0}".format(id))


class PeopleNameHandler(web.RequestHandler):
    async def get(self, name, *args, **kwargs):
        self.redirect(self.reverse_url("people_name", 'Tom'))


# 配置如 people/1/1


urls = [
    tornado.web.URLSpec("/", MainHandler, name="index"),
    tornado.web.URLSpec("/people/(\d+)/?", PeopleHandler, name="people_id"),
    tornado.web.URLSpec("/people/(\w+)/(\d+)/?", PeopleNameHandler, name="people_name"),
]

if __name__ == '__main__':
    app = web.Application(urls, debug=True)
    app.listen(8888)
    ioloop.IOLoop.current().start()
