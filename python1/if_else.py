'''
rohit = input("enter weight of rohit:")
rohitasw = input("enter weight of rohitasw: ")

if rohit > rohitasw:
  print("rohit weight is greater")
else:
  print("rohitasw weight is greater")
'''  

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////")
a = 33
b = 200
if b > a:
  print("b is greater than a")

# elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# short hand if
if a > b: print("a is greater than b")

# short hand if...else
a = 2
b = 330
print("A") if a > b else print("B")


# multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# and keyword
# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# OR keyword
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# pass statement
# if statements cannot be empty, 
# but if you for some reason have an if statement with no content,
#  put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass

