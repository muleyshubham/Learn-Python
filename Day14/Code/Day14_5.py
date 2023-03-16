# two dimensional array

import numpy as np

def print_properties(arr):
    print(f"Array = {arr} Type = {type(arr)}")
    print(f"Data type of an array = {arr.dtype}")
    print(f"Size = {arr.size}")
    print(f"Item Size = {arr.itemsize}")
    print(f"Dimensions = {arr.ndim}")
    print(f"Total Size = {arr.nbytes}")
    print("-"*85)

def function1():
    n1=np.array([
        [10,20,30],
        [40,50,60]
    ])
    print_properties(n1)
    print(f"values at 0th row = {n1[0]}")
    print(f"values at 1st row = {n1[1]}")
    print(f"value at 0th row second column {n1[0][2]}")
    print(f"value at 1st row first column {n1[1][1]}")

function1()