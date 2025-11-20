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
age = int(input("Enter age: ").strip())
if age >= 21:
    print("Yes, can go")
else:
    print("No, can't go")

    # Step 4. Check for the edge cases.
    # We should consider edge cases such as :
    # Negative ages or extremely high values -> programs will break.
    # Non-numeric input -> ABC
    # Age which is valid. > 130

# Step 5. Optimize the code.
# Handle all the edges. ---> Chatgpt  ====> Get improved Code




