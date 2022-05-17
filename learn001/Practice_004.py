class A:
    def __init__(self):
        pass


class B:
    def __init__(self):
        pass

    def runB(self):
        print('runB')


class C:
    t = 3

    def __init__(self):
        pass

    def goC(self):
        print('GoC')


class AB:
    def __init__(self):
        self.children = {}

    def add(self, **kwargs):
        for key, value in kwargs.items():
            # print(type(key), value)
            self.children.update({key: value})


a = A()
b = B()

ab = AB()
ab.add(navi=a, right=b)
func = 'runB'
for _, item in ab.children.items():
    if hasattr(item, func):
        eval(f"item.{func}()")
        # item.eval('runB')()
