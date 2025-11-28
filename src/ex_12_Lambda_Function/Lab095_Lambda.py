import math

# def give_me_power(num):
#     return math.pow(num, 2)
#
# op=  give_me_power(10)
# print(op)
#-----------Converting to lambda-------#

#user_input = int(input("Enter a number: "))
#op_l=lambda num:math.pow(num,2)
#print(op_l(user_input))

#------interesting------------------

print(lambda: math.pow(int(input("Enter a number ")), 7)()) # dont use this
# avoid this difficult to understand