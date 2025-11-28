# Example -2 of decorator


def before_after_ui_test(func):

    def wrapper():
        print("Before running the UI code")
        func()
        print("After running the UI code")
    return wrapper()







@before_after_ui_test
def test_ui():
    print("Hi,I am testing a UI Test")
