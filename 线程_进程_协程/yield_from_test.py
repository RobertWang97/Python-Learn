from itertools import chain

list1 = [1, 2, 3, 4]
dict1 = {"a": "111", "b": "222"}
for value in chain(list1, dict1):
    print(value)

print("*" * 100)


def my_chain(*args):
    for my_iterable in args:
        for value in my_iterable:
            yield value


for value in my_chain(list1, dict1):
    print(value)
print(my_chain(list1, dict1))

print("*" * 100)


def my_chain(*args):
    for my_iterable in args:
        yield from my_iterable


for value in my_chain(list1, dict1):
    print(value)
print(my_chain(list1, dict1))

print("*" * 100)


def g1(iterable):
    yield iterable


def g2(iterable):
    yield from iterable


for value in g1(range(10)):
    print(value)

for value in g2(range(10)):
    print(value)
print("*" * 100)
def g1(gen):
    yield from gen
def main():
    g = g1()
    g.send(None)
main()

print("*" * 100)
print("*" * 100)
print("*" * 100)
