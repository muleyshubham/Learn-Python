#PRIVATE (Name Mangling)
#any variable preceded with two underscores it is private
class Person:
    #custom initializer / parametrized initializer
    def __init__(self,name,age,address):
        self.__name=name
        self.__age=age
        self.__address=address

    def printDetails(self):
        print(f"Name = {self.__name}")
        print(f"Address = {self.__address}")
        print(f"Age = {self.__age}")
        print("-"*80)

p1=Person("Akshita",36,"pune")

print(f"Contents of p1  = {p1.__dict__}")

# Name Mangling
# _classname__fieldname : value
#'_Person__name': 'Akshita'
# '_Person__age': 36
# '_Person__address': 'pune',




