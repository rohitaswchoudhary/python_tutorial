import datetime
import time

today = datetime.date.today()
print(today)

time_today = datetime.datetime.today()

print(time_today)

times = time.localtime()
print(times)

today = datetime.datetime.now()
print(today)

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime.now()

print(x.strftime("%a"))

x = datetime.datetime.now()

print(x.strftime("%w"))

x = datetime.datetime.now()
print(x.strftime("%d"))

x = datetime.datetime.now()

print(x.strftime("%b"))

x = datetime.datetime.now()

print(x.strftime("%B"))

x = datetime.datetime.now()

print(x.strftime("%m"))

x = datetime.datetime.now()

print(x.strftime("%y"))

x = datetime.datetime.now()

print(x.strftime("%Y"))

x = datetime.datetime.now()

print(x.strftime("%H"))

x = datetime.datetime.now()

print(x.strftime("%I"))

x = datetime.datetime.now()

print(x.strftime("%p"))

x = datetime.datetime.now()

print(x.strftime("%M"))

x = datetime.datetime.now()

print(x.strftime("%S"))

x = datetime.datetime.now()

print(x.strftime("%f"))

x = datetime.datetime.now()

print(x.strftime("%z"))

x = datetime.datetime.now()

print(x.strftime("%Z"))

x = datetime.datetime.now()

print(x.strftime("%j"))


x = datetime.datetime.now()

print(x.strftime("%U"))

x = datetime.datetime.now()

print(x.strftime("%W"))

x = datetime.datetime.now()

print(x.strftime("%c"))

x = datetime.datetime.now()

print(x.strftime("%x"))

x = datetime.datetime.now()

print(x.strftime("%X"))

x = datetime.datetime.now()

print(x.strftime("%%"))


x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))