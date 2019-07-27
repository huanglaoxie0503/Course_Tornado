# -*- coding: utf-8 -*-
import aiomysql

from tornado import gen, httpclient, ioloop


async def test_example():
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='root',
                                      db='message', charset='utf8')
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * from message;")
            value = await cur.fetchone()
            print(value)
    pool.close()
    await pool.wait_closed()


if __name__ == '__main__':
    # import asyncio
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(test_example())

    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(test_example)
