import numpy as np
import pandas as pd

df = pd.read_csv('./aa.csv', sep=',', encoding='utf-8')

# y = np.array(df)
# keys = df.columns.to_list()
# arr = [{title: z for title, z in zip(keys, x)} for x in y]
# print(arr)

print(df.index.values)
print(list(df.iloc[2]))