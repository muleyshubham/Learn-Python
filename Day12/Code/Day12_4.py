#__str__
class Car:
    def __init__(self,model,company,price):
        self.__model=model
        self.__company=company
        self.__price=price
    def disp_data(self):
        print(f"Details = {self.__model} {self.__company} {self.__price}")

c=Car("baleno",'maruti',11)
print(f"C = {c}")  # implicit call to __str__
print(f"__str__ = {c.__str__()}") # explicit call to __str__
c.disp_data()