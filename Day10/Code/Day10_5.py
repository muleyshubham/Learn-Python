class Person:
    def __init__(self,name,address,age):
        setattr(self,'Name',name)
        setattr(self,'Address',address)
        setattr(self,'Age',age)

p1=Person("Person1","Pune",25)
p2 = Person("Person2", "Mumbai", 30)

print(f"Name of first object = {getattr(p1,'Name')}")
print(f"Address of first object = {getattr(p1,'Address')}")
print(f"Age of first object = {getattr(p1,'Age')}")

print(f"Name of Second object = {getattr(p2,'Name')}")
print(f"Address of Second object = {getattr(p2,'Address')}")
print(f"Age of Second object = {getattr(p2,'Age')}")