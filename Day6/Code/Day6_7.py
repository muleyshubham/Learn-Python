#packing and unpacking
def function1():
    t1=("akshita",36,123456)
    print(f"T1 = {t1} Type = {type(t1)}")
    print(f"Name = {t1[0]}")
    print(f"Age = {t1[1]}")
    print(f"ID = {t1[2]}")
    # disadvantage is we need to remember the index position

#function1()

#unpacking the values
#fetching the tuple values individually
def function2():
    #t1 is tuple consist of multiple items
    # PACKING
    t1 = ("akshita", 36, 123456)
    #Unpacking
    (name,age,id)=t1
    print(f"Name = {name}")
    print(f"Age = {age}")
    print(f"Id = {id}")

#function2()


def function3():
    #Unpacking example
    (n1,n2,n3)=(10,20,30)
    #n1,n2,n3=(10,20,30)
    #n1, n2, n3 = 10, 20, 30
    print(f"N1 = {n1} type = {type(n1)}")
    print(f"N2 = {n2} type = {type(n2)}")
    print(f"N3 = {n3} type = {type(n3)}")
#function3()


def function4():
    n1,n2=3,5
    print(f"Before swap N1 = {n1} N1 ={n2}")
    temp = n1
    n1=n2
    n2=temp
    print(f"After swap N1 = {n1} N1 ={n2}")

#function4()


def function5():
    n1,n2=3,5
    print(f"Before swap N1 = {n1} N1 ={n2}")
    n1,n2=n2,n1
    print(f"After swap N1 = {n1} N1 ={n2}")

function5()