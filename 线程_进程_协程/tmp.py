import time, random
def async_func(func, *args, callback):
    aa = func(*args)
    callback.send(aa)


def add(x, y):
    return x + y


def yield_func():
    aa = 1

    while True:
        aa = yield
        aa += 1
        x = random.randint(0, 8)
        time.sleep(x)
        print(f"wait {x}")
        print(f"run {aa}")

start = time.time()
x = yield_func()
# next(x)
x.send(None)
# print(id(x))
y = yield_func()
# next(y)
y.send(None)
# print(id(y))
z = yield_func()
# next(z)
z.send(None)
m = yield_func()
# next(m)
m.send(None)
print(time.time()-start)
async_func(add, 1, 7, callback=x)
async_func(add, 2,3, callback=y)
async_func(add, 5, 8, callback=z)
async_func(add, 3, 3, callback=m)
print(time.time()-start)
# import random, time
# def run_gen():
#     i = 1
#     while True:
#         x = yield
#         i += 1
#         if x is None:
#             break
#         print('go', x, i)
#
#
# a = run_gen()
# a.send(None)
# a.send(3)
# a.send(None)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
