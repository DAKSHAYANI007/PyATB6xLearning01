squares = {x ** 2 for x in range(5)}   # x in range(5) means 0,1,2,3,4
print(squares) # output-> {0, 1, 4, 9, 16}
# one line coder is never advised, many people get confused.

# Frozen Set (Immutable Set)
# A frozenset cannot be changed after creation.
my_list = [1, 2, 3, 3]
fset = frozenset([1, 2, 3, 3])
print(fset)
# fset.add(4) #AttributeError: 'frozenset' object has no attribute 'add'