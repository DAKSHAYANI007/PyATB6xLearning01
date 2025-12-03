# # *
# # * *
# # * * *
# # * * * *
# # * * * * *
rows = int(input("Enter the rows for the Right Angle Triangle"))

for i in range(1, rows + 1):
     for j in range(i):
         print("*",end="")
     print()

     #OR#

#for i in range(1, 6):
    #print("*" * i)