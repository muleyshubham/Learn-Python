#print even numbers using lambda and using map
from functools import reduce


def function1():
    even=lambda a : a % 2 == 0
    l1=list(map(even,range(20)))
    print(f"Even List = {l1}")
#function1()

def function2():
    even=lambda a : a % 2 == 0
    l1=list(filter(even,range(20)))
    print(f"Even List = {l1}")
#function2()


def function3():
    print(list(map(lambda a : a % 2 == 0,range(20))))
    print(list(filter(lambda a: a % 2 == 0, range(20))))
#function3()

def function4():
    l1=[12,4,13,15,8,9,16]
    print(list(map(lambda a : a % 2 == 0,l1)))
    print(list(filter(lambda a: a % 2 == 0, l1)))
#function4()

def function5():
    t1=(12,4,13,15,8,9,16)
    print(list(map(lambda a : a % 2 == 0,t1)))
    print(list(filter(lambda a: a % 2 == 0, t1)))
#function5()

def function6():
    l1=[12,4,13,15,8,9,16]
    print(tuple(map(lambda a : a % 2 == 0,l1)))
    print(tuple(filter(lambda a: a % 2 == 0, l1)))
#function6()

def function7():
    numbers=[1,2,3,4,5]
    sum=lambda a,b : a+b
    result = reduce(sum,numbers)
    print(f"Result = {result}")
#function7()

def function8():
    numbers=[1,2,3,4,5]
    print(reduce(lambda a,b : a+b,numbers))
function8()


