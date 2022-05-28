import inspect
def gen_func():
    value = yield "11"
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration as e:
        pass
    print(inspect.getgeneratorstate(gen))