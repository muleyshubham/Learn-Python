#range()

def function1():
    l1=[]
    l1=list()
#function1()

def function2():
    #0 : start from 0 , 50 : till 50  , 1:increament value
    l1=list(range(0,20,1))
    print(f"L1 = {l1}")
    l2=list(range(15)) #similar to range(0,15,1)
    print(f"L2 = {l2}")
    l3=list(range(10,50,5))
    print(f"L3 = {l3}")
#function2()

#sorting the list
def function3():
    numbers=[4,1,6,7,9,12,3,2]
    print(f"List = {numbers}")
    numbers.sort()
    print(f"List = {numbers}")

#function3()


#sorting the list
def function4():
    numbers=[4,1,6,7,9,12,3,2]
    print(f"List = {numbers}")
    numbers.sort(reverse=True)
    print(f"List = {numbers}")
#function4()