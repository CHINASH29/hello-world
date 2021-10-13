
# # Q1. Availability of Numpy and its version in Python  (Screenshot)


import numpy as np
import numpy


print(numpy.version.version)


# # Q2. Differenciate List and Numpy array with three operations


listt = ["apple", "banana", "cherry", 3]
print(listt)


# Python list can contains value of different datatypes whereas Numpy array contains value of same datatype


arr = np.array([1, 2, 3, 4, 5])

print(arr)


print("Length of the list: ", len(listt))


print("Length of the array: ", arr.size)

# We use len() method to find the length of the list whereas for numpy we use variable_name.size operation


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers3 = []
for n in numbers:
    numbers3.append(n**3)

print('Original list:', numbers)
print('Cubic list:', numbers3)


print('First array is:')
print(arr)
print('\nApplying power function:')
print(np.power(arr, 3))


# %%
