#Tuple
# always inside ()
# immutable collection of values
# we can not perform append(), insert(), extend(), remove(), pop()
# sort() , reverse() , copy()

def function1():
    t1=(10,20,30,40,50,60,70)
    print(f"T1 = {t1} type = {type(t1)}")

#function1()

def function2():
    t1=(10,20,30,40,50,30,50)
    print(f"T1 = {t1} type = {type(t1)}")
#function2()

def function3():
    t1=(10,20,30,40,50,30,50)
    print(t1)

    for ele in t1:
        print(ele,end=" ")

    print()
    #Length
    print(f"Length = {len(t1)}")
    #Count
    print(f"Count the element 50 in tuple = {t1.count(50)}")
    #find the index
    print(f"Index of element 20 = {t1.index(20)}")
#function3()

def function4():
    t1=(1,2,3,4,5)
    print(t1)
    t1.append(77) # AttributeError

#function4()

def function5():
    t1=(11,22,33,44,55)
    print(f"T1 = {t1} Type = {type(t1)}")
    t2=10,20,30,40,50
    print(f"T2 = {t2} Type = {type(t2)}")

function5()


#num=10   ===> type ===> class 'int'
#num=10,20,30 ===> type ===> class 'tuple'