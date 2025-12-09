"""t = open('testdata.txt', 'r') # reading mode
t = open('testdata.txt', 'w') # writing mode
t = open('testdata.txt', 'r+') # reading and writing mode
t = open('testdata.txt', 'w+')
t = open('testdata.txt', 'b')
t.close()   # In the end always close ur file.

# Automatically close"""


with open('testdata.txt', 'r') as f: # -> aliyas

 data = f.read()

print(data)