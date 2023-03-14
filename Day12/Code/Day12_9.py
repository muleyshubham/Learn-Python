# __add__() method is overloaded

class MyNumber:
    def __init__(self,number):
        self.__number=number

    def __add__(self,other):
        return MyNumber(self.__number + other.__number)
    def __str__(self):
        return f"{self.__number}"

n1=MyNumber(25) # n1 is Object
n2=MyNumber(15) # n2 is Object
print(f"N1 + N2 = {n1+n2}")
# print(f"N1 + N2 = {n1.__add__(n2)}) # internally it will be converted
# n1.__add__(n2)
# self ==> n1 and it will take one argument as n2 other object
