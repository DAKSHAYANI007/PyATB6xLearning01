# Q - Create a function which will take a positive number from the
# user and perform square of the number?


a = int(input("Enter a positive num"))

if a <= 0:

 print("Enter a positive num")

else:

   def square_r(a):
    return a * a
   result = square_r(a)
   print(result)

    # Note: Alignment is so important