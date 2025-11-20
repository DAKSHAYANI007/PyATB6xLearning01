# Find the maximum between numbers.

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
if num1 > num2:
    print( num1,"maximum than", num2)
else:
    print( num2,"maximum than" ,num1)

# if both are equal ,then edge case.

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
if num1 >= num2:
    print( num1,"is max ", num2)
else:
    print("num1 is max" if num1 > num2 else "num2 is max")

    # if interviewer says both numbers are positive edge case
""" if num1>0 and num2>0:
    print("Numbers should be positive") """
#################################################
#     "Always ask User what he/she wants"