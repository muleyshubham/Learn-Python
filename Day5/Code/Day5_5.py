
# count , index
def function1():
    #list can consist of duplicate elements
    l1=[1,2,3,4,5,2,3,6,7,8,2,3,2]
    print(f"L1 = {l1} Length = {len(l1)}")
    #if we wish to count the number of occurence of some element
    print(f"Element 2 is repeated = {l1.count(2)}")
#function1()

def function2():
    # list can consist of duplicate elements
    l1 = [10, 20, 30, 400, 50, 20, 30, 60, 70, 80, 20, 30, 20]
    print(f"L1 = {l1}")
    print(f"element 30 is at index location = {l1.index(30)}")
    print(f"element 30 is at index location = {l1.index(30,5)}")
function2()