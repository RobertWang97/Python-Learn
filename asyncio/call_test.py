import asyncio


def callback(sleep_time):
    print(f"sleep {sleep_time} success!")


def stop_loop(loop):
    loop.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()
    loop.call_soon(callback, 2)
    loop.call_later(1, callback, 1)  # 延迟1秒
    loop.call_later(2, callback, 2)  # 延迟2秒
    loop.call_later(3, callback, 3)  # 延迟3秒
    loop.call_at(now + 2, callback, 4)
    loop.call_at(now + 3, callback, 5)
    loop.call_at(now + 4, callback, 6)
    # loop.call_soon(stop_loop, loop)
    loop.run_forever()
