
# Q - Create a function which will take the
# 3 values from the user, which are length of the triangle.  side1, side2, side3

# i/p - int side1 == side2 =side3 → isoceles
#o/p = result in string - iso, eq, scalene

#--------------------------------------------------------#

s1= int(input("Enter s1:"))
s2= int(input("Enter s2:"))
s3= int(input("Enter s3:"))

def triangle_type(s1,s2,s3):
    return s1 ,s2, s3

if s1==s2==s3:

      result=triangle_type(s1,s2,s3)

      print("its a equilateral triangle")

elif s1 != s2 and s2 != s3 and s3!= s1:

     result=triangle_type(s1,s2,s3)

     print("its scalene triangle")

elif s1 == s2 or s2 == s3 or s3 == s1:

     result=triangle_type(s1,s2,s3)

     print("its a isosceles triangle")











