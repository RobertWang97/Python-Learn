import time
def func():
    html = yield "http://projectsedu.com"
    print(html)
    yield 2
    yield 3
    return "bobby"


if __name__ == "__main__":
    f = func()
    url = next(f)
    print(url)
    html = "bobby"
    time.sleep(4)
    f.send(html)
    print(next(f))
