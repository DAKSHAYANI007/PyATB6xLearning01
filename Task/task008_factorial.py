"""Question 1. :
Given  a number you need to calculate the factorial of that number
n = 5
Fact = 5×4×3*2*1 = 120
Fact = 0 → 1, """


fact =1

num = int(input("Enter a number, which you want to calculate the factorial of:  "))

if num < 0:

    print("Factorial  cant be defined")

if num == 0:

  print("factorial  is 1")

else:
    for i in range(1,num+1):

        fact = fact * i

        print("factorial of :",fact)



