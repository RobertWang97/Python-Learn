class A:
    def __init__(self):
        self.title = 'A'
        print('A')

    def goA(self):
        print('goAAAAAAAAAAAAAAA')


class B:
    def __init__(self):
        self.title = 'B'
        print('B')


class C:
    t = 3

    def __init__(self):
        print('C')

    def goC(self):
        print('GoC')


class AB:
    def __init__(self):
        self.elements = {}
        a = A()
        b = B()
        self.elements.update({getattr(a, 'title'): a, getattr(b, 'title'): b})


ab = AB()
print(ab)
for key, value in ab.elements.items():
    print(key, value)
print(ab.elements['A'])
a = ab.elements['A']
a.goA()