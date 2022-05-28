import time


def func():
    yield "http://projectsedu.com"
    # print(html)
    try:
        yield 2
    except GeneratorExit as e:
        raise StopIteration
    yield 3
    return "bobby"


if __name__ == "__main__":
    f = func()
    print(next(f))
    print(next(f))
    f.close()
    # print(next(f))
    # print(next(f))
    print("end")
