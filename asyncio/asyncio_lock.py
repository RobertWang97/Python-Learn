import asyncio
from asyncio import Lock,Queue
import aiohttp

cache = {}
lock = Lock()
# queue = Queue #限流
# await queue.get()
# queue =[] #协程间通信
async def get_stuff(url):
    # await lock.acquire()
    # with await lock:
    async with lock:
        # async for
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        return stuff
    # lock.release()

async def parse_stuff():
    stuff = await get_stuff()



async def use_stuff():
    stuff = await get_stuff()

tasks = [parse_stuff(), use_stuff()]
# total = 0
#
# async def add():
#     global total
#     for i in range(1000000):
#         total += 1
#
# async def desc():
#     global total
#     for i in range(1000000):
#         total -= 1
# if __name__ == "__main__":
#     import asyncio
#     tasks = [add(), desc()]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(total)
# import threading
# thread1 = threading.Thread(target=add)
# thread2 = threading.Thread(target=desc)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print(total)