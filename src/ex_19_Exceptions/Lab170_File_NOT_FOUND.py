try:
    data = open("test.json").read()  #Trying to read file test.json
except FileNotFoundError as fnf:
    print(fnf)