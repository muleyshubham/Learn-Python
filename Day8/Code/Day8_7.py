#finding the sqaure of numbers using for loop
def function1():
    numbers=[1,2,3,4]
    #get the sqaure of every value
    for i in numbers:
        print(f"Sqaure of value {i} is {i ** 2}")

#function1()


#finding the sqaure of numbers collect the result in a list
def function2():
    result=[]
    numbers = [1, 2, 3, 4]
    for i in numbers:
        result.append(i ** 2)
    print(f"Numbers = {numbers}")
    print(f"Sqaures = {result}")
#function2()
print("-"*80)
a1=function2 # function alias
#a1()

def function3():
    numbers=[1,2,3,4]
    sqaure = lambda x : x ** 2
    print(f"sqaure ={sqaure} type = {type(sqaure)}")
    result=[]
    for i in numbers:
        result.append(sqaure(i))
    print(f"Numbers = {numbers}")
    print(f"Sqaure = {result}")
#function3()

def function4():
    l1=[4,5,6,7]
    sqaure = lambda x : x ** 2
    result=list(map(sqaure,l1))
    print(f"L1 = {l1}")
    print(f"Result = {result}")
function4()




