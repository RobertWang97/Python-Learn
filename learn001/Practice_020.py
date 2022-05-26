# a = (i*i for i in range(10000))
# for i in range(10000):
#     print(next(a))
#
#
# b = iter(i for i in range(1000000))
# for i in range(1000000):
#     print(next(b))

def generator():
    for i in range(10000):
        yield i


# while True:
print(list(generator()))
