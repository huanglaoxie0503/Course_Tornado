# -*- coding: utf-8 -*-
from chapter04.model import Goods, Supplier
from chapter04.data import supplier_list, goods_list

"""Model 数据保存、查询、删除"""


def save_model():
    for data in supplier_list:
        supplier = Supplier()
        supplier.name = data["name"]
        supplier.address = data["address"]
        supplier.phone = data["phone"]
        supplier.save()

    for data in goods_list:
        good = Goods(**data)
        good.save()


def query_model():
    # 获取某一条数据
    # 1.
    # good = Goods.get(Goods.id == 3)
    # 2.
    # good = Goods.get_by_id(3)
    # 3.
    # good = Goods[3]
    # print(good.name)

    # 获取所有数据
    # 1. 等价于 select * from goods，select 返回的是model select 对象
    # goods = Goods.select()
    # goods = Goods.select(Goods.name, Goods.price)
    # 查询价格大于100的商品
    # goods = Goods.select().where(Goods.price > 100)
    # select * from goods where price>100 and click_num>200
    # goods = Goods.select().where((Goods.price > 100) & (Goods.click_num > 200))
    # select * from goods where name like "%飞天"
    goods = Goods.select().where(Goods.name.contains("飞天"))
    for good in goods:
        print(good.name, good.price)


if __name__ == '__main__':
    # save_model()
    query_model()

