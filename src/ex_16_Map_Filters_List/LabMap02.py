#Real example of Map

# converting to list into upper case.

name = ["dakshayani", "yallappa", "muniyamma", "kalavaTHI", "renuKA","bHavani"]

def upper_case(string):
    return string.upper()


upper_names = list(map(upper_case, name))
print(upper_names)