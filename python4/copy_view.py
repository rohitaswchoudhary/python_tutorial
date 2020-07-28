# The Difference Between Copy and View
# The main difference between a copy and a view of an array is 
# that the copy is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not 
# affect original array, and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will 
# affect the original array, and any changes made to the original array will affect the view.

# copy
# Make a copy, change the original array, and display both arrays:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
arr[1] = 10
print(arr)
print(x)
print()

# view
# Make a view, change the original array, and display both arrays:

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)
print()

# Make Changes in the VIEW:
# Make a view, change the view, and display both arrays:

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)
print()

# Check if Array Owns it's Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

# Every NumPy array has the attribute base that returns None if the array owns the data.

# Otherwise, the base  attribute refers to the original object.

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()  # copy returns none
y = arr.view()  # view returns original array

print(x.base)
print(y.base)
print()