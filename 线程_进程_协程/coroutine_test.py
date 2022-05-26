def func():
    html = yield 1
    yield 2
    yield 3
    return "bobby"


if __name__ == "__main__":
    f = func()
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
