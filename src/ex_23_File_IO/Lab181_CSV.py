# Its very easy to use Python to read csv files



import csv

with open('TD.csv') as csvfile:
    reader = csv.reader(csvfile)
    for column in reader:
        print(column[0],column[1],sep="|")

#o/p

#Username|password
#admin|password
#admin|password123
#admin123|pass123 #