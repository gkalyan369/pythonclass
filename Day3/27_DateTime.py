import time
import datetime

# All dates are represented as no. of seconds elapsed
# since 1st Jan 1970

# Using datetime module
print(datetime.time(6, 35, 34))
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

print(datetime.date.today())
print(datetime.date.today().timetuple())

d1 = datetime.date(2017, 3, 2)
print(d1)
d2 = d1.replace(month=4)
delta = d2-d1
print(delta)
print(type(delta))


print("Current time: ", time.time())
print("Local time: ", time.localtime(time.time()))
print("Formatted time: ", time.asctime(time.localtime(time.time())))

