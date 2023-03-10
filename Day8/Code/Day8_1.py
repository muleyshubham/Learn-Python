def function1():
    d1={"name":"Akshita","Address":"Pune","age":36}
    print(f"D1 = {d1}")
    print(f"Keys = {d1.keys()}")
    print(f"Values = {d1.values()}")
#function1()

# if we wish to fetch individual values use array notation
# or we can use get()

def function2():
    d1={"name":"Akshita","Address":"Pune","age":36}
    print(f"Name = {d1['name']}")
    print(f"Address = {d1['Address']}")
    print(f"Age  = {d1['age']}")

    print(f"Name = {d1.get('name')}")
    print(f"Address = {d1.get('Address')}")
    print(f"Age  = {d1.get('age')}")

#function2()



def function3():
    d1={"name":"Akshita","Address":"Pune","age":36}
    #print(d1)
    print(f"email = {d1['email']}")
    # if we try to fetch any value whose key is not present
    # and if we use array notation then it will give error "KeyError"
    print(f"Name = {d1['Name']}")
    #if we supply key wrongly then it will give us KeyError
    # case sensitive

#function3()


def function4():
    d1={"name":"Akshita","Address":"Pune","age":36}
    #print(d1)
    print(f"email = {d1.get('email')}")
    # if we use get() and if key doesnot exists
    #it will return None
    print(f"Name = {d1.get('NAME')}")
    #if you supply wrong key name inside get() then it will return None

#function4()

# dictionary can consist of duplicate values inside keys
# dictionary can not contain duplicate keys (keys should be unique)
def function5():
    d1={"eid":1,"name":"akshita","age":36,"org":"sunbeam","eid":50,"dept":"sunbeam"}
    print(d1)
#function5()

#dictionary one key hold multiple values
def function6():
    d1={
        "name":"akshita",
        "address":"pune",
        "age":36,
        "org":"sunbeam",
        "Languages":["C","C++","Python","Java"]
    }
    print(d1)
    print(d1.get("Languages"))
    l1=d1.get("Languages") # this will give output as List
    print(l1) # this will print the complete list
    print(l1[0]) # we can apply indexing
function6()