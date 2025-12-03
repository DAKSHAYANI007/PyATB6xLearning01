my_list = [1, 2, 3]
my_list[0]= "Daksha"  # Can change the items in list -yes ,list is muteable
my_list[1]= "Akshaya"


for a in my_list:
    print(a)

# range () this is  also function which returns the list.
print("#--------------------------------------------------")


for i in range(1,10,):
    print(i)

my_list = [1, 2, 3]
# Indexing
print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])

# append() - # Append object to the end of the list.
my_list.append(4)
print(my_list)

my_list.append(5)
print(my_list)

# extend() - Append a new list
my_list.extend([7, 8, 10, 9])
print(my_list)

#insert()
my_list.insert(1,"Daksha")
print(my_list)
print(len(my_list))

my_list.insert(0, 0)
print(my_list)

#remove
my_list.remove("Daksha")
print(my_list)

#my_copy
my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

#sort
#my_copy_list.sort()





