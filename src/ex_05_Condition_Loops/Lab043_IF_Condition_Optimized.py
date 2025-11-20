# Write  a program to take a user age and
# let him know if he can go the club.
# 21

# Logic Building Formula

# Step 1
# i/p --- User will enter the age -- int
# o/p --- String (Result  --> Can go to club or not.

# Step 2 . Rough Logic ( brute force)
"""age > 21 -> print can go
age < 21 -> print can't go
"""

# Step 3. Write the logic
age = int(input("Enter age:  ".strip()))  # strip will make sure whatever the input your getting will not take extra spaces
if age <= 0 or age > 130:
    print("Enter valid age ")
else:
    if age >= 21:

        print("Yes, u can go ")
    else:
        print("No, u can't go")
#------------It is covered almost all cases ---------# except char - this is handled by
