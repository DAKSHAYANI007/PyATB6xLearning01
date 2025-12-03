shopping_list_wife = ["bread", "butter", "paneer"]
shopping_list_wife[2] = "milk"
print(shopping_list_wife)

# Real of Tuples
#-----------------------------------------------------------------------

my_tuple = ("tta.com", "sdet.live") #- In automation we will be storing URL's,which will be constant.
print(my_tuple)                     # - Changing
my_api_list = list(my_tuple)  # list is function
print(my_api_list.append("item2"))

my_api_list2=tuple(my_api_list)
print(my_api_list2)

# Real case, where we Tuples
API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[0])
print(API_URLSs[1])

# Can create empty tuple
t=tuple()
print(t)

#Can create empty list
l=list()
print(l)

# Conversion List to Tuple
t1 = tuple(["DAKSHA", "Samartha", "Dhruva"])
print(t1)


hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
new_tuple = (hero1, hero2)
print(new_tuple)    #  (('Batman', 'Bruce Wayne'), ('Wonder Woman', 'Diana Prince'))
print(new_tuple[0])  #  ('Batman', 'Bruce Wayne')
print(new_tuple[0][0])# Batman
print(new_tuple[1][1])# Diana Prince

