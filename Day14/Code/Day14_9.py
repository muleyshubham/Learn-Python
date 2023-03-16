import numpy as np

# Broadcast operations
def function1():
    a1=np.arange(1,10,1)
    print(f"A1 = {a1}")
    print(f"A1 + 100 = {a1+100}")
    print(f"A1 - 100 = {a1 - 100}")
    print(f"A1 * 5 = {a1 * 5}")
    print(f"A1 / 2 = {a1 /2}")
    print(f"A1 ** 2 = {a1 ** 2}")

#function1()

def function2():
    a1=np.array([1,2,3,4])
    a2=np.array([6,7,8,9])
    print(f"A1 = {a1}")
    print(f"A2 = {a2}")
    print(f"A1 + A2 = {a1+a2}")
#function2()

# filtering
# all the fields having values > 30
def function3():
    a1=np.array([10,20,30,40,50,60,70,80])
    print(f"A1 = {a1}")
    print(f"A1 > 30 ={a1>30}")
    print(f"A1 > 30 ={a1[a1 > 30]}")
    print(f"A1 > 30 ={np.size(a1[a1 > 30])}")
function3()
