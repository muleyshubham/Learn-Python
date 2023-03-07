#Collection
#Collection means collection of similar or dissimilar type of values

#List []
# list can hold similar or dissimilar type of elements
# list can hold duplicate elements too


def myEmptyList():
    """creating a list collection"""
    l1=[]  #first syntax to create a list
    l2=list() #second way to create an empty list
    print(f"L1 = {l1} L2 = {l2}")
    print(f"Type of L1 = {type(l1)} Type of L2 = {type(l2)}")

#myEmptyList()

def function1():
    #list of int
    numbers = [1,2,3,4,5]  #(homogenious , same type of data)
    print(f"Number list = {numbers} Type = {type(numbers)}")

#function1()

def function2():
    #list of strings (homogenious , same type of data)
    languages = ['C','C++','Python','Java']
    print(f"Languages = {languages} Type = {type(languages)}")
#function2()

def function3():
    status=[True,False,True,True]  #(homogenious , same type of data)
    print(f"Status = {status} Type = {type(status)}")
#function3()

def function4():
    #list of different data type (hetrogenous)
    l1=["Akshita",36,80000,True,True]
    print(f"List = {l1} Type = {type(l1)}")
function4()



