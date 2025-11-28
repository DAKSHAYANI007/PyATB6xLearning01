# Question 2 :
#
# An API sometimes fails due to network delays.
#
# Write a program to retry the API call 3 times until the response code becomes 200.
#
# If it still fails after 3 tries, print a failure message.
#
# Hint: Use a while loop with a counter.
# Hint: Use a while loop with a counter.
#------------------------------------------------------------------#

max_attempt = 3
response = None
attempt = 1
while attempt <= max_attempt:

    response = int(input("Enter the API response code: "))

    if response == 200:
        print("Test case is passed")
        break
    else:
        attempt =attempt + 1

if response != 200:
        print("Test case is failed after 3 attempts")





