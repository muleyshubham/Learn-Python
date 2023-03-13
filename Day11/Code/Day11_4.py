# Simple Inheritance / Single Inheritance
# Student is-a Person
# class Student is derived from the class Person
class  Person:
    def __init__(self,name,address,age):
        print(f"Object = {self}")
        self.__name=name
        self.__address=address
        self.__age=age

    def __del__(self):
        print(f"Deallocation = {self}")

    def printDetails(self):
        print(f"Name {self.__name}")
        print(f"Address = {self.__address}")
        print(f"Age = {self.__age}")
        print("-"*50)

#Student class is derived from Person
# all the members of the Person class are copied to Student object

class Student(Person):
    pass

#p1=Person("person1","pune",40) # p1 is parent class object
#p1.printDetails()
#print(f"P1 = {p1.__dict__}")


#create object of derived / child class

s1=Student("st1","mumbai",20)
s1.printDetails()
print(f"S1 = {s1.__dict__}")



