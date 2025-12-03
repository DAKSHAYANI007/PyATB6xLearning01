# Making variable into global ?

count = 0

def increment():
    global count
    count = count +1

increment()
increment()
increment()
increment()
increment()
print(count)
