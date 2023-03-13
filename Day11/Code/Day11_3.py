#Public declaration
# any variable not preceded with any underscores it is public

class Person:
    #custom initializer / parametrized initializer
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def printDetails(self):
        print(f"Name = {self.name}")
        print(f"Address = {self.address}")
        print(f"Age = {self.age}")
        print("-"*80)

p1=Person("Akshita",36,"pune")
print(f"Contents of p1  = {p1.__dict__}")


#{'name': 'Akshita', 'age': 36, 'address': 'pune'}
