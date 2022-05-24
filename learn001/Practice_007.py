import random
from faker import Faker

faker = Faker()
dt = faker.future_date(end_date='+30d')
print(type(dt), dt)

fdt1 = dt.strftime("%Y-%m-%d")

print(type(fdt1),fdt1)
print("*"*100)
import datetime

dt = datetime.date.today()
print(type(dt))
print(dt)
print(dt.strftime("%Y-%m-%d"))
