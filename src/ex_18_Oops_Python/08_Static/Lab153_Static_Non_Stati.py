class MathOperation:

    def div(self, a, b):
            return  a/ b


    @staticmethod
    def sum(a, b):
          return a + b


t = MathOperation()
print(t.div(10, 10))

# this is Non-static operation,has to be called with object reference.

print(MathOperation.sum(10, 10))# This is static without object reference.