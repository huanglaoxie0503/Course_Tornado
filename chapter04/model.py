# -*- coding: utf-8 -*-
import peewee_async
from peewee import *
from peewee import Model
from datetime import datetime


db = MySQLDatabase('message', host="127.0.0.1", port=3306, user="root", password="root0503")

database = peewee_async.MySQLDatabase(
    database='message',
    user='root',
    host='127.0.0.1',
    port='3306',
    password='root0503',
    charset='utf-8'
)
# Create async models manager:

objects = peewee_async.Manager(database)

# No need for sync anymore!

database.set_allow_sync(False)


class BaseModel(Model):
    add_time = DateTimeField(default=datetime.now(), verbose_name="添加时间")

    class Meta:
        database = database


class Supplier(BaseModel):
    name = CharField(max_length=100, verbose_name="名称", index=True)
    address = CharField(max_length=100, verbose_name="联系地址")
    phone = CharField(max_length=11, verbose_name="联系方式")

    class Meta:
        database = db
        table_name = "supplier"


class Goods(BaseModel):
    supplier = ForeignKeyField(Supplier, verbose_name="商家", backref="goods")
    name = CharField(max_length=100, verbose_name="商品名称", index=True)
    click_num = IntegerField(default=0, verbose_name="点击量")
    goods_num = IntegerField(default=0, verbose_name="库存")
    price = IntegerField(default=0.0, verbose_name="价格")
    brief = TextField(verbose_name="商品简介")

    class Meta:
        table_name = "goods"


def init_table():
    db.create_tables([Goods, Supplier])


if __name__ == '__main__':
    init_table()

