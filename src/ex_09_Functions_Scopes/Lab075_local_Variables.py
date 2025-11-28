pb_global_b = 12

def my_function():
    pb_a = 10

    print(pb_a)

print(pb_global_b)  # -> global variable is available everywhere


# print(pb_a) -> cant be done because its local variable.

my_function()