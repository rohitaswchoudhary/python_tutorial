# Python Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.




#  creating a class.
# To create a class, use the keyword class:
import inheritance



class MyClass:
  x = 5         # property name for this class is x

print(MyClass)
print()

# creating object
# Now we can use the class named MyClass to create objects:

p1= MyClass()
print(p1.x)
print()
print()

# the _init_()function
# The examples above are classes and objects in their simplest form, 
# and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), 
# which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created:

# Create a class named Person, use the __init__() function to assign values for name and age:

# class Person:
#   def __init__(self, name, age):
#     #   The __init__() function is called automatically 
#     #    every time the class is being used to create a new object.
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
# print()

# # Object Methods
# # Objects can also contain methods. 
# # Methods in objects are functions that belong to the object.

# # Let us create a method in the Person class:
# # Insert a function that prints a greeting, and execute it on the p1 object:

# class person1:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person1("John", 36)
# p1.myfunc()
# print()

# # self parameter
# # The self parameter is a reference to the current instance of the class, 
# # and is used to access variables that belongs to the class.

# # It does not have to be named self , 
# # you can call it whatever you like, 
# # but it has to be the first parameter of any function in the class:
# class person2:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
    

# p1 = person2("Rohit", 36)
# p1.myfunc()
# print()
# # modify object proprety
# p1.age = 18
# p1.myfunc()
# print(p1.age)

# print()

# # delete object property

# # del p1.name
# # p1.myfunc()

# # delete object
# # del p1
# # p1.myfunc()

