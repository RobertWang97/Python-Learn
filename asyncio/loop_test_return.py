import asyncio, time, random
from functools import partial


async def get_html(url):
    print(f"Start running {url}")
    x = random.randint(0, 5)
    await asyncio.sleep(x)
    print(f"end running {url}")
    return "cxxxxx"


def callback(url, future):
    print(url)
    print("Send email")


if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(get_html("http://www.xxx.com"))
    task = loop.create_task(get_html("http://www.xxx.com"))
    task.add_done_callback(partial(callback, "http://www.xxx.com"))
    # loop.run_until_complete(get_future)
    # print(get_future.result())
    loop.run_until_complete(task)
    print(task.result())
    print(time.time() - start)
    loop.close()
