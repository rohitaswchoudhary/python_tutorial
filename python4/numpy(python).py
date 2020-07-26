"""

NumPy is a python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

NumPy stands for Numerical Python.

Why Use NumPy ?
In Python we have lists that serve the purpose of arrays, but they are slow to process.

NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.

Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

Why is NumPy Faster Than Lists?
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

This behavior is called locality of reference in computer science.

This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

Which Language is NumPy written in?
NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print()
print(np.__version__)
print()
print(type(arr))  # The array object in NumPy is called ndarray.
print("The array object in NumPy is called ndarray.")

print()

#  dimensions in arrays
print("dimensions in arrays")

a = np.array(42)
print("0D-array",a)
print()

b = np.array([1, 2, 3, 4, 5])
print("1D-array",b)
print()
c = np.array([[1, 2, 3], [4, 5, 6]])
print("2D-array",c)
print()
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("3D-array",d)
print()

# check number of dimensions:
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher dimension arrays:
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
