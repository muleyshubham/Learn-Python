import numpy as np
# create a function(print details about numpy array)
# print_properties is user defined function ,
# taking one argument of type numpy array

def print_properties(arr):
    print(f"Array = {arr} Type = {type(arr)}")
    print(f"Data type of an array = {arr.dtype}")
    print(f"Size = {arr.size}")
    print(f"Item Size = {arr.itemsize}")
    print(f"Dimensions = {arr.ndim}")
    print(f"Total Size = {arr.nbytes}")
    print("-"*85)

def function1():
    n1=np.array([2,4,6,8,10,12,14])
    # 7 elements
    # each element will receive 4 bytes
    # 7 * 4 = 28 bytes
    print_properties(n1)

#function1()

def function2():
    n2=np.array([1,2,3,4,5],dtype=np.int64)
    #total elements = size = 5
    #each item size = 8bytes
    # total size = 5*8 = 40bytes
    print_properties(n2)
#function2()


def function3():
    n3=np.array([10,20,30,40,50,60],dtype=np.int16)
    #total elements = size = 6
    #each item size = 2bytes
    # total size = 6*2 = 12bytes
    print_properties(n3)
#function3()


def function4():
    n4=np.array([11,22,33,44],dtype=np.int8)
    #total elements = size = 4
    #each item size = 1 byte
    # total size = 4*1 = 4bytes
    print_properties(n4)
function4()
