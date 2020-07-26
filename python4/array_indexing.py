# access array elements

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

print()

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])
print()


# access 2D array

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[0, 1])
print()

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])


print('Last element from 2nd dim: ', arr[1, -1])  #-(ve) indexing
print()

# access 3D array.

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("third element of the second array of the first array:",arr[0, 1, 2])




