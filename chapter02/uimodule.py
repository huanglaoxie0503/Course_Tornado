# -*- coding: utf-8 -*-
import tornado
from tornado import web, ioloop
from tornado.web import template
from tornado.web import StaticFileHandler, RedirectHandler


class OrderModule(tornado.web.UIModule):
    """
    组件化开发
    """
    def cal_total(self, price, nums):
        return price * nums

    def render(self, *args, **kwargs):
        self.render_string("ui_modules/order_list.html")


class MainHandler(web.RequestHandler):
    """

    """
    async def get(self, *args, **kwargs):
        orders = [
            {
                "name": "小米T恤 忍者米兔双截棍 军绿 XXL",
                "image": "http://i1.mifile.cn/a1/T11lLgB5YT1RXrhCrK!40x40.jpg",
                "price": 39,
                "nums": 3,
                "detail": "<a href='http://www.baidu.com'>查看详情</a>"
            },
            {
                "name": "招财猫米兔 白色",
                "image": "http://i1.mifile.cn/a1/T14BLvBKJT1RXrhCrK!40x40.jpg",
                "price": 49,
                "nums": 2,
                "detail": "<a href='http://www.baidu.com'>查看详情</a>"
            },
            {
                "name": "小米圆领纯色T恤 男款 红色 XXL",
                "image": "http://i1.mifile.cn/a1/T1rrDgB4DT1RXrhCrK!40x40.jpg",
                "price": 59,
                "nums": 1,
                "detail": "<a href='http://www.baidu.com'>查看详情</a>"
            }
        ]
        self.render("index2.html", orders=orders)


settings = {
    "static_path": "D:/work/Course_Tornado/chapter02/static",
    "static_url_prefix": "/static2",
    "template_path": "templates",
    "ui_modules": {
        "OrderModule": OrderModule
    }
}


if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler),
        ("/2/", RedirectHandler, {"url": "/"}),
        ("/static/(.*)", StaticFileHandler, {"path": "D:/work/Course_Tornado/chapter02/static"})
    ], debug=True, **settings)
    app.listen(8888)
    ioloop.IOLoop.current().start()






