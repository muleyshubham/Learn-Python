#__base__

#in python all the classes are having super class as "object"
#object is root class of all the classes in python

#class Person ==> base class of Person is Object ==>done implicitely
# class Person(object): ==> base class of Person is Object
# explicit

class Person:
    pass
class Employee(Person):
    pass

print(f"Base class of Employee = {Employee.__base__}")
print(f"Base class of Person = {Person.__base__}")