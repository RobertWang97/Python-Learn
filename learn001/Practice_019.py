# import pandas as pd
# table = [[str(j*i + 1) for i in range(1,6)] for j in range(1, 11)]
# # table = [[1,2,3,4,5],[6,7,8,9,10],]
# # print(table)
# df = pd.DataFrame(table)
# df.columns = ["title1", "title2", "title3", "title4", "title5",]
# df['index'] = df.index
# print(df.head())
# print(df.loc[0])

def decorator_first(param, value):
    def decorator(func):
        def update(param):
            print("update1")
            func(param)
            print("update2")
            return
        return update
    return decorator

@decorator_first("value", "aaaaa")
def f(value):
    print(value)

f('222')