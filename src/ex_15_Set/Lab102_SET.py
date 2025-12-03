# # SET
# # Collection of Unique
# # {} - parenthesis

#set doesnt follow any order

list_of_unique_items = {1, 2, 3, 4, 4, 5, 5}
print(list_of_unique_items)

list1 = [45.2, 33, 33, 45, 21]
set1 = set(list1)
print(set1)


#converting tuple to test
t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(t)
print(set(t))

mixed = {1, "QA", True, 3.5} # -> incase of python 1=True
print(mixed)

#empty_set
empty = set()
print(type(empty))

# set is also a list
for item in mixed:
 print(item)

# is it mutable or not
mixed.add(10)   # you can add multiple element
print(mixed)
mixed.remove(10)
print(mixed)

