# How to override the function?



class BaseTest:
    def run(self):
        print("Running generic test")


class LoginTest(BaseTest):

    def run(self):
        print("Running Login Test")


# t = LoginTest()
t = BaseTest()  # o/p depends which object mentioned. 
t.run()

#Note: In case of JAVA you should write override annotation.