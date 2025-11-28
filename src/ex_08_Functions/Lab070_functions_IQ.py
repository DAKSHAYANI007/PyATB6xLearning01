# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

#================================================================#

# Step 1 : Input - int
#         Output - int

#step 2 : Logic building
# return n1+n2+n3

# Step3 : Write a logic

num1=int(input("Enter a number: "))      #-> ideally this i/p name(num1) should nor be same as argument name in function(num1)
num2=int(input("Enter another number: "))
num3=int(input("Enter third number: "))

def sum_num (num1=100,num2=200,num3=300):

    return num1+num2+num3

#result =sum_num(num1=100,num2=200,num3=300)
#result1 = sum_num() ----> no Argument
result= sum_num(num1=1)
#result2 =sum_num(0,2,7) # based on position it will take

##### One of the best concept , Java wont support this ####

print(result)

