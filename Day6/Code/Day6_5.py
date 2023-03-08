#Slicing in list

# firstvalue:secondvalue:thirdvalue
# first value : start
# second value : end
# thirdvalue : step value

def function1():
    l1=[10,20,30,40,50,60,70,80,90,100]
    for ele in l1:
        print(ele,end=" ")
    print()
    print("-"*80)
    print("Print the numbers form two to seven")
    for i in range(2,7):
        print(l1[i],end=" ")

#function1()


def function2():
    l1=[10,20,30,40,50,60,70,80,90,100]
    print(f"Numbers from 2 to 7 {l1[2:7]}")
    print(f"Numbers from 5 to 9 {l1[5:9]}")

#function2()

def function3():
    l1=[10,20,30,40,50,60,70,80,90,100]
    print(f"l1[6:] = {l1[6:]}")
    print(f"l1[:5] = {l1[:5]}")
    print(f"l1[0:] = {l1[0:]}")
    print(f"l1[:] = {l1[:]}") # similar to print(f"l1[]= {l1[]})

#function3()


def function4():
    l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(l1[0:10:1])
    print(l1[0:10:2])
#function4()

def function5():
    l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(l1[0:8:1])
    print(l1[0:8:2])
function5()