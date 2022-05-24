class A:
    x = [1, 2, 3, 4, 5]

    def __init__(self):
        self.title = 'A'
        print('A')

    def get_xx(self):
        print('goAAAAAAAAAAAAAAA')
        return "xx"

    def test(self, key):
        if hasattr(self, key):
            return eval(f"self.{key}")
        elif hasattr(self, f"get_{key}"):
            return eval(f"self.get_{key}()")
        else:
            return 1


aa = A()
print(aa.test("xx"))
