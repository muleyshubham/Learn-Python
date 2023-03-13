
# protected field (CONVENTION)
# any variable preceded with one underscores it is protected
# It is just a convention

class Person:
    #custom initializer / parametrized initializer
    def __init__(self,name,age,address):
        self._name=name
        self._age=age
        self._address=address

    def printDetails(self):
        print(f"Name = {self._name}")
        print(f"Address = {self._address}")
        print(f"Age = {self._age}")
        print("-"*80)

p1=Person("Akshita",36,"pune")
print(f"Contents of p1  = {p1.__dict__}")

#{'_name': 'Akshita', '_age': 36, '_address': 'pune'}
