# Find the given postive number is even or odd

num = int(input("Enter a number: ".strip()))
if num % 2 == 0:  # (num divided by 2 , remainder is equal to 0)
    print("Number is even")
else:
    print("Number is odd")
# ----------DONE----------#

# wht if entered number is -ve number
# so nested if
num = int(input("Enter a number: ".strip()))
if num >= 0:
    if num % 2 == 0:
        print("Number is even number")
    else:
        print("Number is odd number")
else:
    print("Number is negative number")

# You can write short one-liner conditions using ternary operator:
num = int(input("Enter a number: ".strip()))
if num >= 0:
    print("Even" if num % 2 == 0  else "Odd")
else:
    print("Negative number")
