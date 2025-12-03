#Converting time into millisecond

response_times_ms = [1200, 1500, 1800]

def mil_sec(x):
    return x / 1000



response_times_s = list(map(mil_sec, response_times_ms))



print(response_times_s)

#if we don't use map ,should use for loop.

#o/p :[1.2, 1.5, 1.8]
#-----------------------------------------------------or

#using Lambda
response_times_s = list(map(lambda x: x/1000, response_times_ms))


