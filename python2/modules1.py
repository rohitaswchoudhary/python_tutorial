import mymodules

# built in modules
import platform

mymodules.greeting("rohit")

a= mymodules.person1["age"]
print(a)

print(mymodules.person1)

x = platform.system()
print(x)
print()
print()
print()

# there is a built in function to list all the function names (or variable names ) in a module:
x= dir(platform)
print(x)

