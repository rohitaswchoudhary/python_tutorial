# 2023-04-26 17:11:06
# program to add two matrices


X = [[12,7,3], [4,5,6],[7,8,9]]
Y = [[5,8,1],[6,7,3],[4,5,9]]
Z = [[5,8,1],[6,7,3],[4,5,9]]

result = [[0,0,0],[0,0,0],[0,0,0]]
print(len(X))
print(len(Y))
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]= X[i][j]+Y[i][j]

for r in result:
    print(r)    

# add two matrices using numpy module

import numpy as np      # import the numpy module.

arr1 = np.array(X)
arr2 = np.array(Y)


print("\nAdd matrix using numpy module\n")
sum = np.add(arr1,arr2)
print(sum)

# dot product of two matrices using numpy.

product = np.dot(arr1,arr2)
print("\nDot product of two matrix is :")
print(product)
# another method to get dot product.
print(arr1 @ arr2)


# cross product of two matrix using numpy

cross_product= np.cross(arr1,arr2)
print("\ncross_product of two matrix: ")
print(cross_product)

print()
# python program to shuffle a deck of card

import itertools, random

deck = list(itertools.product(range(1,14), ['Spade','Heart','Diamond','Club']))

random.shuffle(deck)

print("you got: ")
for i in range(5):
    print(deck[i][0], "of ", deck[i][1])



