# array of string
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
    n1=np.array(["str1","str2","str3"])
    #<U4
    # Unicode Character Set of less than 4 bytes
    # 1 byte = 8 bits
    print_properties(n1)
#function1()

def function2():
    n2=np.array(["str1","str1234","str456"])
    #<U7
    # Unicode Character Set of less than 4 bytes
    # 1 byte = 8 bits
    print_properties(n2)
function2()