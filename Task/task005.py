#In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.

#expected_title = "Dashboard"
#actual_title = "Dashboard "
expected_title = "Dashboard"
actual_title = "dashboard "

if expected_title.strip().lower() == actual_title.strip().lower():
    print("Test case passed")
else:
    print("Test case failed")


# We can have 3 scenarios here
#1.without strip
#2.With strip
#3lower case