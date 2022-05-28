async def downloader(url):
    return "bobby"


import types


@types.coroutine
def downloarder2(url):
    yield "bobby2"


async def download_url(url):
    html = await downloader(url)
    html1 = await downloarder2(url)
    return html1, html1


if __name__ == "__main__":
    coro = download_url("http://www.imooc.com")
    # next(None)
    coro.send(None)
    # print(next(coro))
    for a, b in coro:
        print(a,b)
