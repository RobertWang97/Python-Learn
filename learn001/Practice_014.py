import random

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

value = 10
list_options = [str(i+1) for i in range(value)]
print(list_options)
a = random.sample(list_options, random.randint(1, len(list_options)))
print(a)
s = " ".join(a)
print(s)
