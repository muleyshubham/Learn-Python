class Person:
    def __init__(self,name,address,age):
        setattr(self,'Name',name)
        setattr(self,'Address',address)
        setattr(self,'Age',age)

    #dispData() is printing the contents inside the object
    # it is called as Facilitator
    def dispData(self):
        print(f"Name = {getattr(self,'Name')}")
        print(f"Address = {getattr(self,'Address')}")
        print(f"Age = {getattr(self,'Age')}")


p1=Person("Person1","Pune",25)
p2 = Person("Person2", "Mumbai", 30)
p1.dispData() # dispData() is called upon p1 object , self ==> p1
p2.dispData() #dispData() is called upon p2 object, self = p2