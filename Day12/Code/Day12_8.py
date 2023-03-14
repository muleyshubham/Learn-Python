# __add__() method is not overloaded
# so when we try to add two objects it will give error TypeErro

class MyNumber:
    def __init__(self,number):
        self.__number=number
    def __str__(self):
        return f"Number = {self.__number}"

n1=MyNumber(25) # n1 is Object
n2=MyNumber(15) # n2 is Object
print(f"N1 + N2 = {n1+n2}") # TypeError
# we are trying to add two objects
# not possible in this scenario
# Solution :
# overload __add__() method inside the class MyNumber