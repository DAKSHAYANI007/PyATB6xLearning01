from logging import exception

import requests

"""url= input("Enter the url")

#response = requests.get("http://www.api.example.com/")

response = requests.get("http://www.api.example.com/")

print(response.status_code) #o/p :ConnectionError"""


# How to fix it

try:
    url = input("Enter the url")

    # response = requests.get("http://www.api.example.com/")

    response = requests.get(url,timeout=3)

    print(response.status_code)

except requests.exceptions.ConnectionError:

    print("Error due to  the wrong URL or connection failed!")

except requests.exceptions.Timeout:

    print("Timeout error,not able to load URL")

except Exception as e:

    print(e)