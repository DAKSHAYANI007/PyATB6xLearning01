   ## Multiple inheritance#
#---------------------------------------------------#


class APIBase:    #Parent1
    def api_auth(self):
        print("Authentication API")


class DBBase:   # Parent 2
    def db_connect(self):
        print("Connecting to the DB")


class TestHybrid(APIBase, DBBase): # Child
    def run(self):
        self.api_auth()          # calling
        self.db_connect()       #Calling
        print("Test Case Running.")


tc1 = TestHybrid()        # Object of TestHybrid
tc1.run()                # Executes all methods in order.


# In case of JAVA its not possible.