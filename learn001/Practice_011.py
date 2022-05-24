import json

dict = {'name': 'many', 'age': 10, 'sex': 'male'}
print(type(dict), dict)  # 输出：<class 'dict'> {'name': 'many', 'age': 10, 'sex': 'male'}

# dict转json
j = json.dumps(dict)
print(type(j), j)  # 输出：<class 'str'> {"name": "many", "age": 10, "sex": "male"}

# json转dict
data2 = json.loads()
print(type(data2), data2)  # 输出：<class 'dict'> {'name': 'many', 'age': 10, 'sex': 'male'}
