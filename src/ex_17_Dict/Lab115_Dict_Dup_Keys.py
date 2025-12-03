# Can we have duplicat keys in dictionary - No


p = {"name": "Pramod", "name": "Amit"}

print(p)


my_list = [1, 2, 2, 3, 4, 4, 5]

#o/p :{'name': 'Amit'}

# only first key will be used.Interesting thing is Python will never give you that only duplicate
# keys will exist, only it will override.

# Very important question asked in interview

