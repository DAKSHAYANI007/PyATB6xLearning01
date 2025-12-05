   # OR#

class MathClass:
    def add(self, a, b):
        return a + b

    def add(self, a, b,c=10 ):   # for c =10 it 's not getting error
        return a + b + c


obj_ref = MathClass()
obj_ref.add(3,4, 5) #    3 arguments
obj_ref.add(3.14,4.14)  # 2 arguments

# It's  not happening bcz proper method overloading is not supported
#  its possible in JAVA - we can call function 2 or 3 argument with same name.