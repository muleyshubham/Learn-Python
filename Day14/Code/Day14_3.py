
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
    n1=np.array([1.1,2.2,3.3,4.4])
    #each element is 8 bytes
    # 4 elements = 4*8 = 32 bytes
    print_properties(n1)
#function1()

def function2():
    n2=np.array([1.1,2.2,3.3,4.4],dtype=np.float32)
    #each element is 4 bytes
    # 4 elements = 4*4 = 16 bytes
    print_properties(n2)
#function2()

def function3():
    n3=np.array([1.1,2.2,3.3,4.4,5.5],dtype=np.float16)
    #each element is 2 bytes
    # 5 elements = 5*2 = 10 bytes
    print_properties(n3)
function3()
