import numpy as np

def function1():
    a1=np.array([
        [10,20,30],
        [40,50,60]
    ])
    print(f"A1 = {a1}")
    print(f"Shape = {a1.shape} Ndim = {a1.ndim}")  # (2,3) 2 rows and 3 columns
    print("-"*80)
    a2=a1.reshape([1,6]) # 1,6  1 row and 6 columns
    print(f"A2 = {a2}")
    print(f"Shape = {a2.shape} Ndim = {a2.ndim}")
    print("-" * 80)
    a3=a1.reshape([6,1]) # 6 rows and 1 column
    print(f"A3 = {a3}")
    print(f"Shape = {a3.shape} Ndim = {a3.ndim}")

function1()