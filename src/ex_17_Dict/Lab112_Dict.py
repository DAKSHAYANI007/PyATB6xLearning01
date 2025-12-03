dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1.keys())   # o/p: dict_keys(['a', 'b', 'c'])

print(dict1.values()) # o/p :dict_values([1, 2, 3])


#-----------------------------------
# subtraction of dictionaries
"""dict2 = {"a": 1, "b": 2}

#missing_keys = dict1- dict2

print(missing_keys) #o/p :unsupported operand type(s) for -: 'dict' and 'dict'"""

# Correct one

dict2 = {"a": 1, "b": 2}

missing_keys = set(dict1.keys()- dict2.keys())# adding key and converting them to set

print(missing_keys)  # output :{'c'}

# this is exactly used in API automation to find the difference between 2 json files.

