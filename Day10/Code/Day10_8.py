class Person:
    def __init__(self,name,address,age):
        self.name=name
        self.address=address
        self.age=age

    def printData(self):
        print(f"Name = {self.name}")
        print(f"Address = {self.address}")
        print(f"Age = {self.age}")

p1=Person("Akshita","Pune",35)
p1.printData()