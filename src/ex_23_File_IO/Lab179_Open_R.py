#with open('testdata.txt', 'r') as file:
    #content = file.readlines() o/p: in list format
    #content = file.read()
#print(content)

# if there is an error , we can use try catch

try:
    with open('testdata.txt', 'r') as file:
     content = file.read()
    print(content)
except FileNotFoundError as fnfe:
    print(fnfe)