# -*- coding: utf-8 -*-
import aiomysql
from tornado import web, ioloop
from tornado.web import StaticFileHandler


class MainHandler(web.RequestHandler):
    def initialize(self, db):
        self.db = db

    async def get(self, *args, **kwargs):
        id = ""
        name = ""
        email = ""
        address = ""
        message = ""
        pool = await aiomysql.create_pool(host=self.db['host'], port=self.db['port'],
                                          user=self.db['user'], password=self.db['password'],
                                          db=self.db['name'], charset='utf8')
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT * from message;")
                try:
                    id, name, email, address, message = await cur.fetchone()
                except Exception as e:
                    pass
        # pool.close()
        # await pool.wait_closed()
        self.render("message.html", id=id, name=name, email=email, address=address, message=message)

    async def post(self, *args, **kwargs):
        id = self.get_body_argument("id", "")
        name = self.get_body_argument("name", "")
        email = self.get_body_argument("email", "")
        address = self.get_body_argument("address", "")
        message = self.get_body_argument("message", "")

        pool = await aiomysql.create_pool(host=self.db['host'], port=self.db['port'],
                                          user=self.db['user'], password=self.db['password'],
                                          db=self.db['name'], charset='utf8')
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT INTO message(name, email, address, message) values ('', '', '', '');".format(name, email,
                                                                                                         address,
                                                                                                         message))
                await conn.commit()

        pool.close()
        await pool.wait_closed()
        self.render("message.html", id=id, name=name, email=email, address=address, message=message)


settings = {
    "static_path": "D:/work/Course_Tornado/chapter03/static",
    "static_url_prefix": "/static/",
    "template_path": "templates",
    "db": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "root",
        "name": "message",
        "port": "3306"
    }
}

if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler, {"db": settings["db"]}),
        ("/static/(.*)", StaticFileHandler, {"path": "D:/work/Course_Tornado/chapter03/static"})
    ], debug=True, **settings)

    app.listen(8888)
    ioloop.IOLoop.current().start()
