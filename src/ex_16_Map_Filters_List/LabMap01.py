numbers = [1, 2, 3, 4, 5]


def sq(x):
    return x ** 2


sq_all_numbers = list(map(sq, numbers)) # -> square (function) is applied to each element in a list.
print(sq_all_numbers)