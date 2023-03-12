
#in this example we can easily modify the fields of the class
# no data security
# to achive data security we need to create fields as private
class Employee:
    def __init__(self,name,eid,salary):
        self.name=name
        self.eid=eid
        self.salary=salary
    def dispData(self):
        print(f"Name = {self.name} EID = {self.eid} Salary = {self.salary}")

e1=Employee("emp1",1,70000)
e2=Employee("emp2",2,50000)
e1.dispData()
e2.dispData()
print("-"*80)
e1.salary=2000 #fields of the class are easily accssible outside the class
# No Security
e1.dispData()