# Frequency of Characters in a String
# Write a program to count the frequency
# of each character in a given string.
# Using dictionary function

# Logic building
# I/P - string e.g automation
# O/P -> dict  # {a : 2, u : 1 , t : 2 , o : 2, m : 1, i : 1,

string = "automation"
string = input("\nEnter the input e.g automation\n")

char_count = {}
for char in string:
  char_count[char] = char_count.get(char, 0) + 1  # get(char, 0) is a built in function,so get is a function here.

print(char_count)
#o/p :automation
{'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}