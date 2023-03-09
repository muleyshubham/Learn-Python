#set operations
#union (| or union())
def function1():
    s1={10,20,30,40}
    s2={30,40,50,60}
    print(f"S1 = {s1}")
    print(f"S2 = {s2}")
    print(f"Union = {s1 | s2}")
    print(f"Union = {s1.union(s2)}")
#function1()

#Intersect
# ( & or intersection())
def function2():
    s1={10,20,30,40}
    s2={30,40,50,60}
    print(f"S1 = {s1}")
    print(f"S2 = {s2}")
    print(f"intersect = {s1 & s2}")
    print(f"intersect = {s1.intersection(s2)}")

#function2()


#difference
def function3():
    s1={10,20,30,40}
    s2={30,40,50,60}
    print(f"S1 = {s1}")
    print(f"S2 = {s2}")
    print(f"s1 - s2 = {s1 - s2}")
    print(f"s2 - s1 = {s2 - s1}")
    print(f"s1-s2 {s1.difference(s2)}")
    print(f"s2-s1 {s2.difference(s1)}")
    print(f"symmetric difference = {s1.symmetric_difference(s2)}")

function3()
