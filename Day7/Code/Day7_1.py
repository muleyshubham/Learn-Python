#Multidimensional Collection
#collection of collection

def function1():
    #one dimensional collection
    l1=[10,20,30,40,50]
    print(f"L1[0] = {l1[0]}")
    print(f"L1[1] = {l1[1]}")
    print(f"L1[2] = {l1[2]}")
    print(f"L1[3] = {l1[3]}")
    print(f"L1[4] = {l1[4]}")
    print("-"*80)
    for i in l1:
        print(f"value = {i}")
    print("-" * 80)
    print(f"L1 = {l1}")

#function1()

def function2():
    #list of lists
    l1=[[10,20,30],
        [40,50,60]
    ]
    print(f"L1 = {l1}")
    #indexing on list of lists
    print(f"l1[0][0] = {l1[0][0]}")
    print(f"l1[0][1] = {l1[0][1]}")
    print(f"l1[0][2] = {l1[0][2]}")
    print(f"l1[1][0] = {l1[1][0]}")
    print(f"l1[1][1] = {l1[1][1]}")
    print(f"l1[1][2] = {l1[1][2]}")

    print("-"*80)
    for i in l1:  # i = l1[0]  i= l1[1]
        print(i)

    print("-"*80)
    print("using nested for loop")
    for row in l1:  #outer for loop for the row data
        for value in row: #inner for loop for column data 
            print(f"val = {value}")
function2()

