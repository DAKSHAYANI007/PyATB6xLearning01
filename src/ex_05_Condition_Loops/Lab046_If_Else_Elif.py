# Find the maximum between 3 numbers.

# Step 1:
# Logic Building
# I/P - num1, num2, num3
# O/P - int or string is max

num1= int(input("Enter num1:\n"))  #5
num2= int(input("Enter num2:\n")) #3
num3= int(input("Enter num3:\n")) #2

# if 5>3, 5>2 -> max is 5
# num1 > num2 and num1 > num3 -> num1
#num2 > num1 and num2> num3 -> num2
#else print num3

if num1 >= num2 and num1 >= num3:   #---> Condition 1
    print(num1, "Max")
elif  num2 >= num1 and num2 >= num3: #---> Condition 2
    print(num2, "Max")
else:
    print (num3,"Max")
# When i/p is 5,5,3  o/p is 3 -- bug here add >= everywhere hence solved now


