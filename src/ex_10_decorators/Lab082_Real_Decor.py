import time

def print_logs(func):
    def wrapper():
        print("Start of the logs")
        func()
        print("End of the logs")
    return wrapper

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total Time Take by Func -> ", end_time - start_time)
    return wrapper


@time_decorator
@print_logs
def test_ui_1():
    print("Add a function,time taken by this function 1")
    time.sleep(2)


@time_decorator
@print_logs
def test_ui_2():
    print("Add a function,time taken by this function 2")
    time.sleep(5)

test_ui_1()
test_ui_2()


""" o/p  1764296845.5450296
Start of the logs
Add a function,time taken by this function 1
End of the logs
1764296847.5461452
Total Time Take by Func ->  2.001115560531616
1764296847.546218
Start of the logs
Add a function,time taken by this function 2
End of the logs
1764296852.7681534
Total Time Take by Func ->  5.221935510635376"""