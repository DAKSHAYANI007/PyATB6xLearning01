print("Enter the which test you want to run")

test_type = input("Enter the test type : API , UI, Performance , Security")

match test_type:
    # (case _: print(" Invalid type.")# error SyntaxError: wildcard makes remaining patterns unreachable)
    case "API":
        print(" We are running a POSTMAN API testcase.")
    case "UI":
        print(" We are running a Selenium testcase.")
    case "Performance":
        print(" We are running a Performance testcase.")
    case "Security":
        print(" We are running a Security testcase.")
    case _:
        print("Invalid test type.")
        # ###########################################################################
        # #############################################################################
        # same with if else condtions--------------------------------------------------------------------------------------------------
        print("Enter the which test you want to run:")

        test_type = input("Enter the test type : API , UI, Performance , Security")

if test_type == "API":
    print(" We are running a POSTMAN API testcase.")
elif test_type == "UI":
    print(" We are running a Selenium testcase.")
elif test_type == "Performance":
    print(" We are running a Performance testcase.")
elif test_type == "Security":
   print(" We are running a Security testcase.")
else:
   print("Invalid test type.")
