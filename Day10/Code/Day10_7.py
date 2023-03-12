# create object
# check  age if >18 display the msg "Can Vote" else "Can not Vote"S

class Person:
    def __init__(self,name,address,age):
        setattr(self,'Name',name)
        setattr(self,'Address',address)
        setattr(self,'Age',age)

    def printData(self):
        print(f"Name = {getattr(self,'Name')}")
        print(f"Address = {getattr(self, 'Address')}")
        print(f"Age = {getattr(self, 'Age')}")

    def canVote(self):
        if(getattr(self,'Age')>18):
            print("Person can Vote")
        else:
            print("Person can not Vote")


p1=Person("Akshita","Pune",35)
p2=Person("Person2","Mumbai",16)
p1.printData()
print("-"*80)
p2.printData()
print("-"*80)
p1.canVote()
print("-"*80)
p2.canVote()
print("-"*80)
p3=Person('Person3',"hinjewadi",45)
setattr(p3,'mobile',1234567)
print(f"P3 = {p3.__dict__}")


