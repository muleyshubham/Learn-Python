class Developer:
    def __init__(self,language):
        self.__language=language

class Tester:
    def __init__(self,role):
        self.__role=role

class DataEngg:
    def __init__(self,domain):
        self.__domain=domain

class Employee(Developer,Tester,DataEngg):
    def __init__(self,name,id,language,role,domain):
        self.__name=name
        self.__id=id
        Developer.__init__(self,language)
        Tester.__init__(self,role)
        DataEngg.__init__(self,domain)

e1=Employee("Akshita",123,"Python","Trainer","ML")
print(f"E1 = {e1.__dict__}")

