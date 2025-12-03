# Find the number of vowel in string

input_string = "hello, world!"
# a,e, i,o,u.
# vowel ?

vowels = "aeiou"

vowels_count = 0
result = list()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count+1
        result.append(char) # -- to add into list


print(vowels_count)
print(result)

# O/p :3
# ['e', 'o', 'o']