#dictionary
def function1():
    d1={}
    print(f"D1 = {d1} type = {type(d1)}")
    d2=dict()
    print(f"D2 = {d2} type = {type(d2)}")
#function1()

def function2():
    d1={"name":"akshita", "address":"pune", "designation":"technical trainer"}
    print(d1)
    print(f"Keys = {d1.keys()}")
    print(f"Values ={d1.values()}")

function2()