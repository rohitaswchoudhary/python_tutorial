def myfunc():
    print("hello from a function")
# calling a function.

myfunc()

# arguments of a function.

'''
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses.
You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). 
When the function is called, we pass along a first name,
which is used inside the function to print the full name:
'''
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

print()

def my_function(fname, lname):
  print(fname + " " + lname)
  print("my name is " + fname+ " " + lname)

# fname = input("enter your first name: ")
# lname = input("enter your last name: ")

# my_function(fname,lname)
my_function("Emil", "Refsnes")
my_function("Rohitasw","Choudhary")

# If you try to call the function with 1 or 3 arguments, you will get an error:
"""
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
"""
def my_function(*kids):
  print("\n\n\tThe youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")

print()

def my_function(*flname):
  if(flname[1]== chr(10)):
    print("your name is "+flname[0]+" "+flname[2])

  else:
    print("your name is "+flname[0]+" "+flname[1]+" "+flname[2])  
    
    
n1=input("enter your first name: ")
n2=input("enter your middle name: ")
n3= input("enter your last name: ")  
my_function(n1,n2,n3)
# my_function("rohitasw","choudhary")  

# passing lists as an argument:
# You can send any data types of argument to a function (string, number, list, dictionary etc.), 
# and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# default parameter value


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# return value.
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# recursion 
'''
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. 
It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it 
can be quite easy to slip into writing a function which never terminates, 
or one that uses excess amounts of memory or processor power. However,
when written correctly recursion can be a very efficient and 
mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse").
 We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends 
 when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, 
best way to find out is by testing and modifying it.
'''

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)

