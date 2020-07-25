# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
#  This page shows you how to use LISTS as ARRAYS, however, 
#  to work with arrays in Python you will have to import a library, 
#  like the NumPy library.

# Arrays are used to store multiple values in one single variable:
cars = ["Ford", "Volvo", "BMW"]

print(cars)

print(cars[0])
cars[0] = "Toyota"
print(cars)

for x in cars:
  print(x)

cars.append("honda")
print(cars)
cars.pop(0)
print(cars)



cars.remove("Volvo")
print(cars)