import numpy as np

#while creating numpy array we have passed values
a1=np.array([10,20,30,40])
print(f"A1 = {a1}")

# if we want sequential values to be stored
# 1 to 10
a2=np.arange(0,10,1)
print(f"A2 = {a2} Type = {type(a2)}")

a3=np.arange(0,30,5)
print(f"A3 = {a3} Type = {type(a3)}")

# create a np array having all values as zeros
a4=np.zeros(5)
print(f"A4 = {a4} Type = {type(a4)}")

a5=np.ones(6)
print(f"A5 = {a5} Type = {type(a5)}")

a6=np.ones([2,3],dtype=np.int32)
print(f"A6 = {a6} Type = {type(a6)}")


