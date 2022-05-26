class T:
    __slots__ = ('x')
    pass


t = T()
t.x = 234
print(t.x)
t.a = 100
print(t.__dict__, t.a)
