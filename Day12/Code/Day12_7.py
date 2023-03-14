class MyNumber:
    def __init__(self,number):
        self.__number=number
    def __str__(self):
        return f"Number = {self.__number}"

def function1():
    n1=MyNumber(10)  #n1 is Object of MyNumber class
    n2=MyNumber(5)  # n2 is Object of MyNumber class
    print(f"N1 = {n1}") # n1.__str__()
    print(f"N2 = {n2}") # n2.__str__()

#function1()

def function2():
    num1=15 # num1 is variable holding value 15
    num2=25 #num2 is variable holding value 25
    print(f"num1 = {num1} Num2 = {num2}")
    print(f"Addition = {num1+num2}") # 15+25
    print(f"num1 + num2 {num1.__add__(num2)}")

    str1="sunbeam"
    str2="infotech"
    print(f"Str1 = {str1} Str2 = {str2} {str1.__add__(str2)}")
    print(f"Str1 = {str1} Str2 = {str2} {str1+str2}")

    f1=5.4
    f2=3.5
    print(f" F1 = {f1} F2 = {f2} {f1+f2}")
    print(f" F1 = {f1} F2 = {f2} {f1.__add__(f2)}")

function2()
