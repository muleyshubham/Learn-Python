#List operations (append, insert , len, extend , + )

#append example
def function1():
    #list of numbers
    l1=[10,20,30,40,50]
    print(f"L1 = {l1}")
    l1.append(60)
    print(f"L1 = {l1}")
    l1.append(5)
    print(f"L1 = {l1}")

#function1()

def function2():
    l1=[5,2,8,9,7]
    print(f"Length = {len(l1)}")
#function2()


def function3():
    l1=[10,20,30,40,50]
    print(f"List = {l1}")
    print(f"Length = {len(l1)}")

    #insert the element in between the list
    # syntax : insert(index,value)
    l1.insert(3,35)
    print(f"List after inserting element at location 3 = {l1}")
    print(f"Length = {len(l1)}")
    l1.insert(6,55)
    print(f"List after inserting element at location 6 = {l1}")
    print(f"Length = {len(l1)}")
    #if we try to insert the element in the list
    # but index value does not exist
    # so it will behave similar to append()
    l1.insert(500,88)
    print(f"List after inserting element at index which is not existing  = {l1}")


#function3()

def function4():
    l1=[1,2,3,4,5]
    print(f"L1 = {l1} Length = {len(l1)}")
    l1.insert(3,22)
    print(f"L1 = {l1} Length = {len(l1)}")
    l1.insert(0,44)
    print(f"L1 = {l1} Length = {len(l1)}")
    l1.insert(50,88)
    print(f"L1 = {l1} Length = {len(l1)}")
    l1.insert(49, 99)
    print(f"L1 = {l1} Length = {len(l1)}")
    l1.insert(2,"Akshita")
    print(f"L1 = {l1} Length = {len(l1)}")
    l1.insert(-1,76) # OK
    print(f"L1 = {l1} Length = {len(l1)}")
#function4()

def function5():
    l1=[10,20,30]
    print(f"L1[0] = {l1[0]}")
    print(f"L1[1] = {l1[1]}")
    print(f"L1[2] = {l1[2]}")

    print(f"L1[-1] = {l1[-1]}")
    print(f"L1[-2] = {l1[-2]}")
    print(f"L1[-3] = {l1[-3]}")
#function5()


def function6():
    l1=[1,2,3,4]
    l2=[5,6,7,8]
    print(f"L1 = {l1} Length = {len(l1)}")
    print(f"L2 = {l2} Length = {len(l2)}")
    l1.append(l2)
    print(f"L1 = {l1} Length = {len(l1)}")
#function6()

def function7():
    l1=[1,2,3,4]
    print(f"L1 = {l1} Length = {len(l1)}")
    l2=[5,6,7,8]
    print(f"L2 = {l2} Length = {len(l2)}")

    l1.extend(l2) #extend is used to append bulk values individually
    print(f"L1 = {l1} Length = {len(l1)}")
#function7()


def function8():
    l1=[1,2,3,4]
    l2=[5,6,7,8]
    print(f"L1 = {l1} Length = {len(l1)}")
    print(f"L2 = {l2} Length = {len(l2)}")
    l1 = l1+l2
    print(f"L1 = {l1} Length = {len(l1)}")

#function8()

def function9():
    l1=[1,2,3]
    l2=["akshita","sunbeam"]
    l1=l1+l2
    print(f"L1 = {l1}")
    l3=[5.5,4.4,8.9]
    l1.insert(2,l3)
    print(f"L1 = {l1}")
    l1.insert(5,l3[2])
    print(f"L1 = {l1}")
function9()