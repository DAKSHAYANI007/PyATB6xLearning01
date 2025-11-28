"""
Write a Python program to calculate the area of a circle given its radius using the formula
" area= pie * r^2 "  take pie as 3.14
"""
#    "Always ask for input and output.Never assume anything"

#So Input -> r - float
# Output  -> String formatted o/p of area.?
import math
# Answer
# Logic building formula
#----------------------------
#  ||  Step 1   ||
# Figure out the input and output
# input -> r -> datatype -> float
# pi = 3.14
# Power -> pow or ** -> any one
# o/p  -> String -> float - area ,print area
# ||  Step 2  ||
# rough logic = area = 3.14 * pow (r, 2)
# ||  Step 3 ||
radius = float(input("Enter radius of circle:\n "))
print ( radius)
area = math.pi * (radius ** 2)
#area = 3.149877654 * (pow(radius, 2))
# print ("Area of the circle is:", area)  ---Converting to ---// String data formatting
print( f"Area of circle is --> {area:.2f}")

