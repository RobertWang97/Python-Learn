class Father:
    def create(self, name):
        self.name = name
        print("Create Father")

class Son1(Father):
    def create(self, name, age, *args):
        self.age = age
        super().create(name, *args)
        print("Create Son1")

class Son2(Father):
    def create(self, name, band,*args):
        self.band = band
        super().create(name, *args)
        print("Create Son2")

class GrandSon1(Son1, Son2):
    def create(self, name, age, band,*args):
        # self.todo = todo
        super().create(name,age,band,*args)
        print("Create GrandSon1")

gd = GrandSon1()
gd.create("xxx", 14, "L1")
print(GrandSon1.__mro__)