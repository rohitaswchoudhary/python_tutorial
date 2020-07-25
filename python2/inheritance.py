# Inheritance allows us to define a class that inherits 
# all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
print()


# create a child class
# To create a class that inherits the functionality from another class, 
# send the parent class as a parameter when creating the child class:
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
print()


# add _init_ function to child class
# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).
# When you add the __init__() function, 
# the child class will no longer inherit the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, 
# add a call to the parent's __init__() function:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()
print()
# now we are ready to add functionality to the _init_ function of child class

# use super() function
# Python also has a super() function that will make the child class 
# inherit all the methods and properties from its parent:
# By using the super() function, you do not have to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parent.



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()
print("/////////////////////////////////////////////////////////////")

# add properties
# add property called graduation year, roll no to child class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, rollno, year):
        super().__init__(fname, lname)
        self.roll_no = rollno
        self.graduationyear = year

    def details(self):
        print(self.firstname,self.lastname)
        print(self.roll_no)
        print(self.graduationyear)
    
    def welcome(self):
        print("Welcome", self.firstname,self.lastname," to the class of",self.graduationyear)

n1 = input("enter your first name: ")
n2 = input("enter your last name: ")
roll = input("enter your roll no: ")
g= input("enter your graduation year: ")

x = Student(n1,n2,roll,g)
x.details()
x.welcome()
