# Real time example of Functions

def validate_status_code(response_code):

    if response_code == 200:

          print("Request is successful")

    else:
        print("Request is not successful")

validate_status_code(200)
validate_status_code(400)
validate_status_code(response_code=200)  # -> With keyword also it is possible
validate_status_code(input("Enter the response code"))
