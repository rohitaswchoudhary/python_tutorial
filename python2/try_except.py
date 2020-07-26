# # The try block lets you test a block of code for errors.

# # The except block lets you handle the error.

# # The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:

# x = 10
try:
  print(x)
except:
  print("An exception occurred")

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt",'a')
  f.write("Lorum Ipsum\n")
  f.write("rohitasw choudhary")
except NameError:
    print("no file of this name exists")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()


x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")