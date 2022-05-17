class A:
    def __init__(self):
        print('A')


class B:
    def __init__(self):
        print('B')


class C:
    t = 3

    def __init__(self):
        print('C')

    def goC(self):
        print('GoC')


class AB(A, B):
    def CC(self):
        self.C = C()


ab = AB()
ab.CC()
# print(ab.C.goC.)

# import operator
#
#
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return 'name=%s, age=%s' % (self.name, self.age)
#
# p_list = [Person('xiemanR', 18), Person('zhangshan', 17), Person('lisi', 20), Person('wangwu', 25)]
#
# r = sorted(p_list, key=operator.attrgetter('age'))
#
# for i in r:
#     print(i)
