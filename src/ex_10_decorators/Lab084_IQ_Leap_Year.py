# Checking for a Leap Year , 2024 → Yes
#
# Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.(Wikipedia for more details)
#-------------------------------------------------------------------------------#

# Leap year= multiple of 4 and not divisible by 100 or divisible by 400:

def check_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


year =2004
result = check_leap_year(year)
print(result)


