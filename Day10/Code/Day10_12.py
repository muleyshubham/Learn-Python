# destructor
class Employee:
    def __init__(self,name,eid,salary,age):
        print(f"Initializer = {self}")
        self.__name=name
        self.__eid=eid
        self.__salary=salary
        self.__age=age
    def dispData(self):
        print(f"Name = {self.__name} EID = {self.__eid}")
        print(f"Salary ={self.__salary} Age = {self.__age}")
        print("-"*80)
    def __del__(self): # similar to destructor
        print(f"Deallocation = {self}")

e1=Employee("Akshita",123,60000,35)
e1.dispData()