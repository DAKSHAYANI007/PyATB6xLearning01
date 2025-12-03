my_dict = {
    "name": "Aman",
    "age": 34,
    "role": "SDET",
    "exp": 3

}

print(my_dict)
print(my_dict["age"])
print(my_dict["role"])

my_dict["role"] = "Manual Tester"  # dictionary are mutable in nature
print(my_dict)

del my_dict["age"] # You can add or delete a key
print(my_dict)

for key, value in my_dict.items(): #if you want to navigate or iterate over a key
 print(key, value)

print("age" in my_dict)
print("role" in my_dict)