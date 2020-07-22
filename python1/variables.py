x=10
print(x)

a, b, c = 10, 20, 30
print(a)
print(b)
print(c)
print()
print()

y="awesome."       #HERE y is a global variable.

def myfunc():
    print("python is "+y)

myfunc()
print()

def myfunc2():

    z="fantastic."  # z is a local variable.
    print("python is "+z)
myfunc2()
myfunc()
print()

# global keyword//////To create a global variable inside a function, 
# you can use the global keyword.
def myfunc():
  global d
  d = "fantastic"

myfunc()

print("Python is " + d)
