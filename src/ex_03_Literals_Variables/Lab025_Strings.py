name = "This is a Big line"   # so datatype is string
print(type(name))
#name = name + 1
#print(type(name)) ---> so concatenate error,so
name = name + str(1) #--> converting to int to str
print(type(name))

first_name = "DAkshayani "
last_name = "Yellappa"
full_name = first_name + " " + last_name # Concatination between strings absolutely allowed
                                         # not allowed only between incompatible datas
print(full_name)
print(type(full_name))