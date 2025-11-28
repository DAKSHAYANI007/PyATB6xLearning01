# Write a program to calcuclate even and odd
# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


#######------------> Convert this to lambda expression------------->##########

User_input= int(input("Enter a number: "))

result_l_e_o = lambda num:"Even"if num % 2==0 else "Odd"

print(result_l_e_o(User_input))