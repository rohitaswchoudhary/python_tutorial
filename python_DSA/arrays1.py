from array import *

array1 = array('i', [1, 2, 3, 4, 5])

for x in array1:
    print(x)


# accessing array elements

print("----------------------------------")

print(array1[1])

print(array1[-2])

print("----------------------------------")


array1.insert(2, 10)

for i in array1:
    print(i)


# deleting array elements

print("----------------------------------")

array1.remove(1)

for i in array1:
    print(i)


# searching array elements

print("----------------------------------")

print(array1.index(10))


# updating array elements

print("----------------------------------")

array1[1] = 20

for i in array1:
    print(i)

    