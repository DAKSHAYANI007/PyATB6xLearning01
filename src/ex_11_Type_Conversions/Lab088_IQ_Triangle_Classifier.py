# Triangle Classifier:

# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
#=============================================================#

def classify_triangle_type(a,b,c):
    if a>0 and b>0 and c>0: # -> edge cases
        if a+b>c and a+c>b and b+c>a:  #-> edge case
            if a==b==c:
                return "Equilateral"
            elif a==b or b==c or b==c:
                return "isosceles"
            else:
                 a!=b!=c
                 return "Scalene"
        else:
            print("Its not triangle")
    else:
        print("Invalid lengths")


result=classify_triangle_type(1,1,1)
print(f"The triangle is classified as {result}")


