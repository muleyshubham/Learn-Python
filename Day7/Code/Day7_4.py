#list of tuples VS tuple of list

# list []  ==> we can modify the list
# tuple () ==> we can not modify tuple

def function1():
    #list of lists  #outer ==> list  #inner ==> list
    l1=[
        [1,2,3,4]
    ]
    print(f"L1 = {l1}")
    #modify the outer list
    # append() function
    l1.append([50,60,70])
    print(f"L1 = {l1}")
    l1[0].append(5)
    print(f"L1 = {l1}")

#function1()

def function2():
    # list of tuple #Outer ==> list #inner ==> tuple
    numbers=[
        (1,2,3,4)
    ]
    print(f"Numbers List = {numbers}")
    numbers.append(88) #modified outer list
    print(f"Numbers List = {numbers}")
    numbers[0].append(55) # trying to modify inner part (tuple) #not allowed
    # AttributeError
    print(f"Numbers List = {numbers}")

function2()