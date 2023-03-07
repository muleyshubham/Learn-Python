# remove and pop functions in list
#pop() if its called without any arguments, it removes last element
# pop(index) it will remove element at specified index location

#remove()
#is used when we are not aware about index
# when we want to remove specific element by its data then we use remove

def function1():
    l1=[10,20,30,40,50]
    print(f"L1 = {l1}")   # 10 20 30 40 50
    l1.pop()  # last element 50 is removed
    print(f"L1 = {l1}")  # 10 20 30 40
    l1.pop(2)  # pop at index location 2 it means element 30
    print(f"L1 = {l1}")  # 10 20 40


#function1()

def function2():
    l1 = [10, 20, 30, 40, 50]
    print(f"L1 = {l1}")  # 10 20 30 40 50
    l1.remove(40)
    print(f"L1 = {l1}")  # 10 20 30  50


#function2()

def function3():
    l1=[10,15,10,20,15]
    print(f"L1 = {l1}")  #10  15   10  20 15
    l1.remove(15)  # 10   10  20   15
    print(f"L1 = {l1}")
function3()