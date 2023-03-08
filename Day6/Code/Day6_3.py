def function1():
    l1=[5,3,1,2,4]
    l2=l1  #shallow copy
    l3=l1.copy()  #deep copy
    print(f"L1 = {l1} L2 = {l2} L3 = {l3}")
    l1.append(88)
    print(f"L1 = {l1} L2 = {l2} L3 = {l3}")
function1()