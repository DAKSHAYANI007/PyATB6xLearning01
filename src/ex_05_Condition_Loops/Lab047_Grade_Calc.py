# GRADE CALCULATOR:
""" Write a program that calculates and displays the letter grade
for a given numerical score (e.g., A, B, C, D or F)
based on the following grading scale
"""

# A : 90 -100
# B : 80-89
# C : 70-79
# D : 60-69
# F : 0-59
#-----------------------------------------------------------#
# Logic Building Formula

# 1 -> User Inputs - Score -> Int
# 2 -> O/P  -> str -> A,B
score = int (input("Enter the score:".strip()))
if score <= -1 or score > 101:
  print ("Grade cant be calculated, You are a superman!")
else:
    if score >= 90 and score <= 100:    #90 <= score <= 100: Simplified chain is there only in Python not JAVA
        print("A")
    elif score >= 80 and score <= 90:
        print("B")
    elif score >= 70 and score <= 80:
        print("C")
    elif score >= 60 and score <= 70:
        print("D")
    else:
        print("F")

 # Float and Char - try catch.
