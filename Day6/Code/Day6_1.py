def function1():
    l1=[10,20,30,40,50]
    print(f"List = {l1}")
    l1.clear()
    print(f"List = {l1}")

#function1()


#display the list elements using for loop
#iteration is controlled by python

def function2():
    l1=[11,22,33,44,55,66]
    #for each loop (advanced for loop)
    # for each element "i" inside the list "l1"
    # please print element "i"
    for i in l1:
        print(i)
#function2()


def function3():
    l1=[1,2,3]
    # i = l1[0]    i = l1[1]   i = l1[2]
    for i in l1:
        print(i)
#function3()



def function4():
    values=[10,20,30,40,50,60,70,80,90]
    print(f"Values = {values}")
    for element in values:
        print(element)
    positions=[1,3,5]
    for i in positions:
        print(f"Data = {values[i]}")

function4()







