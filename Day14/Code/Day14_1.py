#numpy provides ndarrays (n-dimensional array)
# collection of similar type of values
# memory will be allocated contiguously
# it is immutable in nature

# import numpy package
# np is an alias given to numpy package

import numpy as np
#function to create  list of numpy array
# np.array()

def function1():
    number_list=[10,20,30,40,50]
    print(f"number list = {number_list} Type = {type(number_list)}")
    #array of numbers
    number_arr=np.array([10,20,30,40,50])
    print(f"number arr = {number_arr} Type = {type(number_arr)}")

#function1()

#properties of numpy array
def function2():
    number_arr = np.array([11, 22, 33, 44, 55])
    print(f"Number arr = {number_arr} Type = {type(number_arr)}")
    print(f"Data type of values inside the array = {number_arr.dtype}")
    print(f"Size of each element in the array = {number_arr.itemsize}")
    print(f"Number of items in array = {number_arr.size}")
    print(f"Dimension = {number_arr.ndim}")
    print(f"total bytes = {number_arr.nbytes}")

function2()

# dtype , which type of datatype is considered by python for each element
# itemsize will tell us size of each element in an array
# size will tell us number of elements present in a numpy  array
# ndim (number of dimensions) of numpy array
# nbytes number of bytes occupied by whole numpy array
