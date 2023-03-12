# modify private fields
# setter (it is used to set a new value to the private field of the class)
# it is a member function of the class
#getter function
# it is also member function of the class
# it is used to fetch individual private field of the class


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

    def set_salary(self,salary):
        self.__salary=salary

    def get_salary(self):
        return self.__salary;

e1=Employee("akshita",123,60000,35)
#e1.dispData()
e1.set_salary(80000)
#e1.dispData()
print(f"Salary of e1 object {e1.get_salary()}")