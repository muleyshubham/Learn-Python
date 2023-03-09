#list of tuples

def function1():
    #list of tuples
    l1=[
        (10,20,30),
        (40,50,60)
    ]
    print(f"L1 = {l1} type = {type(l1)}")

#function1()

def function2():
    #list of tuples
    persons=[
        ("p1","p1@gmail.com",35),
        ("p2","p2@gmail.com",28),
        ("p3","p3@gmail.com",37)
    ]

    for p in persons:
        print(p)
    print("Access the element by position")
    for p in persons:
        print(f"Name = {persons[0]}")
        print(f"Email = {persons[1]}")
        print(f"Age = {persons[2]}")

#function2()

def function3():
    #list of tuples
    persons=[
        ("p1","p1@gmail.com",35),
        ("p2","p2@gmail.com",28),
        ("p3","p3@gmail.com",37)
    ]

    for p in persons:
        name,email,age=p  # Unpacking
        print(f"Name = {name}")
        print(f"Email = {email}")
        print(f"Age = {age}")
        print("-"*80)

function3()
