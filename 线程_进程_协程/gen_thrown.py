import time


def func():
    yield "http://projectsedu.com"
    yield 2
    yield 3
    return "bobby"


if __name__ == "__main__":
    f = func()
    print(next(f))
    f.throw(Exception, "My error") #  这是针对第一个yield的异常
    print(next(f))
    f.close()
    # f.throw(Exception, "My error")
    print("end")
