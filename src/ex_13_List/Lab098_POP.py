# Asking many times

squares = [1, 4, 9, 16, 25]
print(squares)  #[1, 4, 9, 16, 25]


print(squares.pop())   #25, Remove and return item at index (default last).
print(squares)         # [1, 4, 9, 16]



print(squares.pop(1))  #4
print(squares)         #[1, 9, 16]



squares.clear()
print(squares)

# index(element, start, end)
# Returns the index of the first occurrence of the element.
numbers = [10, 20, 30, 20, 40]
print(numbers.index(20))

print(numbers.count(20)) #-> 2

numbers.sort()
print(numbers)  #[10, 20, 20, 30, 40]

numbers.sort(reverse=True)
print(numbers)  #[40, 30, 20, 20, 10]


# reverse() Reverses the list in place.

numbers.reverse()
print(numbers)

# max() / min() / sum() Works for numerical lists.
print(max(numbers))  # 40
print(min(numbers))  # 10
print(sum(numbers))  # 120

# Slicing
print(numbers)  # [10, 20, 20, 30, 40]
print(numbers[1:4])  # from index of 1 to 3
print(numbers[-1])  # # Last element

print("apple" in numbers) # False
print(20 in numbers)      #True


# List Creation and Comprehension

# List Creation and Comprehension
# range(1,5) -> list
l = list(range(1, 5))
print(l)             # [1, 2, 3, 4]

# Nested Lists(List of list)
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][2])

# del statement - Deletes an element by index or the whole list.
del numbers[0]   #--delete will never return the element
print(numbers)  #[20, 20, 30, 40]

# Remove is a function and del is a keyword.

#==================Story of list=========================#

