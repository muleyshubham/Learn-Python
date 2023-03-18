import numpy as np
def function1():
    a1=np.array([11,22,33,44,55,66])
    print(f"A1 = {a1}")
    print(f"A1 * 10 = {a1 * 10}") # Broadcast operation
    print(f"A1 > 33 = {a1 > 33}") # filtering
    print(f" a1 > 33 = {a1[a1>33]}")
    print(f" a1 > 33 = {np.size(a1[a1 > 33])}")
    print(f" a1 = {a1}")
#function1()

#indexing , slicing , filtering

def function2():
    a1=np.array([10,20,30,40,50])
    print(f"A1 = {a1}")
    print(f"value at index 2 = {a1[2]}") # indexing
    print(f" values from index 1 to 4 {a1[1:4]}") # slicing
    print(f"Values = {a1[[2,3,4]]}") # fetch the values at multiple locations
    print(f"Values = {a1[[1,4]]}")
    print(f"a1 <= 20 {a1<=20}") # filtering
    print(f"a1 <= 20 {a1[a1 <= 20]}")  # filtering

#function2()

#negative indexing
# last element in numpy array is identified by index -1

def function3():
    a1=np.array([11,22,33,44,55,66])
    print(f"a1[0] = {a1[0]}")
    print(f"a1[1] = {a1[1]}")
    print(f"a1[2] = {a1[2]}")
    print(f"a1[-1] = {a1[-1]}")
    print(f"a1[-2] = {a1[-2]}")
function3()
