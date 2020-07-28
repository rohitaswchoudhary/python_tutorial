# # Data Types in NumPy.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


# checking data type in numpy


import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)
print()

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)
print()

# creating array with defined data type

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)
print()

# Create an array with data type 4 bytes integer:

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)
print()

# Change data type from float to integer by using 'i' as parameter value:


arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)
print()

# changing to int.
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)
print()

# changing to boolen

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)


