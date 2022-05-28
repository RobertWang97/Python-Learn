import asyncio, time, random


async def get_html(url):
    print(f"Start running {url}")
    x = random.randint(0, 5)
    await asyncio.sleep(x)
    print(f"end running {url}")


if __name__ == "__main__":
    start = time.time()
    print(start)
    loop = asyncio.get_event_loop()
    task = [get_html("http://www.bbb.com"),
            get_html("http://www.baidu.com"),
            get_html("http://www.xxx.com"),
            get_html("http://www.zzz.com"),
            get_html("http://www.mmm.com"),]
    loop.run_until_complete(asyncio.wait(task))

    print(time.time() - start)
