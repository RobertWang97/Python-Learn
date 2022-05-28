import asyncio
import socket
# from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

async def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.setblocking(False)
    # try:
    #     client.connect((host, 80))
    # except BlockingIOError as e:
    #     pass
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    all_lines = []
    async for row_line in  reader:
        data = row_line.decode("utf8")
        all_lines.append(data)
    html = 'n'.join(all_lines)
    # print(html)
    return html

async def main():
    tasks = []
    for i in range(20):
        url = f'http://shop.projectsedu.com/goods/{i}/'
        # task = loop.run_in_executor(executor, get_url, url)
        tasks.append(asyncio.ensure_future(get_url(url)))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # tasks = []
    # for i in range(20):
    #     url = f'http://shop.projectsedu.com/goods/{i}/'
    #     # task = loop.run_in_executor(executor, get_url, url)
    #     tasks.append(asyncio.ensure_future(get_url(url)))
    loop.run_until_complete(main())
    # loop.run_until_complete(asyncio.wait(tasks))
    # for task in tasks:
    #     print(task.result())