#__init__(self,parameters)
#CUSTOM INITIALIZER
# similar to paramatrized constuctor

class Person:
    def __init__(self,name,address,age):
        setattr(self,'Name',name)
        setattr(self,'Address',address)
        setattr(self,'Age',age)

p1=Person("Akshita","Pune",36)
#print(f"P1 = {p1.__dict__}")
print(f"Name of person one = {getattr(p1,'Name')}")