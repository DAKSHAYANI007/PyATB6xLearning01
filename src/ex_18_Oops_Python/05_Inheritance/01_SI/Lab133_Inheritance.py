# Single Inheritance
# A Subclass/Child/Son inherits from one Parent/Base/Father.


class BaseTest:
    driver = "Chrome"
    __driver2 = "FF"

    def setup(self): # Parent
        print("Base setup with the browser and env -->"+self.__driver2)

# Creating a child
class LoginTest(BaseTest):
    def run(self): #so if I call run function,can call my parent function
        self.setup()
        print("Running the Testcases -->"+self.driver )


t = LoginTest()
t.run()



