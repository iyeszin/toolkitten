#day1 summer of code

year = 365
hour = year*24
print("Hours in a year: ",hour)

decade = year*10 #without consider leap year
minute = decade*24*60

print("Minutes in a decade: ",minute)

age = 24
age_in_second = age*hour*60*60

print("My age in second: ", age_in_second)

andr_age = 48618000/60/60/hour
print("Andreea Visanoiu's age: ",round(andr_age,2))

# a bit tough questions

###########################################
# how many days to take for a 32-bit system 
# and 64-bit system to timeout 
###########################################

#assuming +1 for every milliseconds
#with max possible number is (2^32)-1

milliseconds = (2**32)-1
day = milliseconds/1000/60/60/24

milliseconds2 = (2**64)-1
day2 = milliseconds2/1000/60/60/24

print("It take %.2f days for a 32-bit system to timeout" % day)
print("It take %.2f days for a 64-bit system to timeout" % day2)


import datetime
now = datetime.datetime.now()

# 12:00:00 utc on 21 oct 1994
mybirthday = datetime.datetime(1994, 10, 21, 12, 0, 0)

calc = now - mybirthday

age = calc.total_seconds()/60/60/ hour
print("My age is %.2f based on my birthday" % age)
