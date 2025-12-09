# # COUNTER - data s
# user_input = input("Enter a string")
# count_char = Counter(user_input)
# print(count_char)
from collections import namedtuple

#namedtuple
# info = ('Pramod', 34, True, 9.8)
# print(info)

info = namedtuple ('info', ['name', 'age', 'ismarried', 'number'])

t = info('Dakshayani', 32, False, 9.3)

print(t.name)
print(t.age)
print(t.ismarried)
print(t.number)