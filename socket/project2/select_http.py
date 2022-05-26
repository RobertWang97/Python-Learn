# epoll并不一定代表比select和poll好
# 在并发高的情况下连接活跃度不高的情况， epoll好，
# 非阻塞

import socket
from urllib.parse import urlparse
# import select
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
urls = []
stop = False


class Fetcher:
    #  回调函数1
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    #  回调函数2
    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass

        #  注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            callback = key.data
            callback(key)


if __name__ == '__main__':

    # fetcher.get_url("http://www.baidu.com")
    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
