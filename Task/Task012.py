# Skip numbers divisible by 3, from (0,100)

#for i in range(0,101,1):
 #   if i % 3 != 0:
  #      print (i)



for i in range(0,101,1):
    if i % 3 == 0:
        continue
    print (i)