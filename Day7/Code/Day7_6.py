#set
#It is a collection of unique values

def function1():
    #create an empty set
    # its a dictionary
    s1={}
    print(f"S1 = {s1} type = {type(s1)}") #dict
#function1()


def function2():
    #create an empty set
    s1=set()
    print(f"S1 = {s1} type = {type(s1)}") # set

#function2()

def function3():
    s1={10,20,30,40,50,60,20,30} #duplicate elements are not stored
    print(f"S1 = {s1} type = {type(s1)}")  # set
    print(f"Length = {len(s1)}") # length = 6
#function3()

def function4():
    s1={"python","java","c","c++","python"}
    print(f"S1 = {s1} type = {type(s1)}")
    print(f"Length = {len(s1)}")

#function4()


def function5():
    s1={10,20,30,40,50,60,20,30,40}
    print(f"S1 = {s1}")
    print(f"s1[0] ={s1[0]}") # indexing is not possible in set # TypeError
#function5()


def function6():
    s1={10,20,30,40,50,60,20,30,40}
    for i in s1:
        print(f"Value = {i}")
function6()




