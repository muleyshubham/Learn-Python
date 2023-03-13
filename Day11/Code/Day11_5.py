#Multilevel inheritance
class Person:
    def __init__(self,name,address,age):
        print(f"Object = {self}")
        self.__name=name
        self.__address=address
        self.__age=age

    def __del__(self):
        print(f"Deallocation = {self}")

    def printDetails(self):
        print("Inside PrintDetails function of Person class")
        print(f"Name {self.__name}")
        print(f"Address = {self.__address}")
        print(f"Age = {self.__age}")
        print("-"*50)


class Employee(Person):
    def __init__(self,name,address,age,id):
        #calling the initializer method of base class from the derived class
        Person.__init__(self,name,address,age)
        self.__id=id

    def printDetails(self):
        print("Inside PrintDetails function of Employee class")
        Person.printDetails(self)
        print(f"ID = {self.__id}")
        print("-"*80)

class Manager(Employee):
    def __init__(self, name, address, age, id,dept):
        Employee.__init__(self,name,address,age,id)
        self.__dept=dept

    def printDetails(self):
        print("Inside PrintDetails function of Manager class")
        Employee.printDetails(self)
        print(f"Dept = {self.__dept}")
        print("-" * 80)

m1=Manager("Akshita","Pune",36,123,"Training")
print(f"M1 = {m1.__dict__}")
m1.printDetails()


