# Q - You receive an API response code from your test script.
# Write an if - else block to check whether the response is successful (Status code 200) or not.

# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

response = int(input("Enter API Response code: "))
# Check if the response is succesful

if response == 200:
    print("✅ Passed API Request")
else:
    print("❌ Failed API Request")
