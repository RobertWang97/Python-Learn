class A:
    pass
class AB:
    def __init__(self):
        self.page_x = A()
        pass

    def page_1(self):
        # print("page_1")
        attr = self.__dir__()
        for item in attr:
            if item[0:4] == "page":
                print(item)


ab = AB()
ab.page_1()
# attr = ab.__dir__()
# ab.
# print(hasattr(ab, "page*"))
# ab.
# for item in attr:
#     if item[0:4]=="page":
#         print(item)
# # print(ab.__dir__())
