# if we wish to create the fields as private
# the variables / fields are preceded with two times underscore __

class Employee:
    def __init__(self,name,eid,salary,age):
        self.__name=name
        self.__eid=eid
        self.__salary=salary
        self.__age=age
    def dispData(self):
        print(f"Name = {self.__name} EID = {self.__eid}")
        print(f"Salary ={self.__salary} Age = {self.__age}")
        print("-"*80)

e1=Employee("emp1",1,40000,25)
e2=Employee("emp2",2,60000,28)
e1.dispData()
e2.dispData()

e1.__salary=20000 # private fields can not be changed outside the class
e1.dispData()



