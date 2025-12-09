import os

#print(os.getcwd())

# You can join the directories

full_path = os.path.join(os.getcwd(),"Daksha.txt")

#full_path = os.path.join("C:\Users\DELL\PycharmProjects\PyATB6xLearning\src\ex_22_Collections","Daksha.txt")

print(full_path)

file = open(full_path,"r+")

print(file.read())